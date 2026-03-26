#!/usr/bin/env python
"""Index selected Obsidian content into LanceDB for RAG.

First pass: index a small, safe subset (e.g. 05_Diversys/Product) into a single
LanceDB table `obsidian_docs` under ~/.openclaw/lancedb/.

Later we can expand coverage using Agent_Domain_Map.md.
"""

import os
from pathlib import Path

import lancedb
from lancedb.pydantic import LanceModel, Vector
from pydantic import Field

# For now, use OpenAI's embedding API via openai package.
# We can swap this to a local embedder later if desired.
from openai import OpenAI


DB_ROOT = Path(os.path.expanduser("~/.openclaw/lancedb"))
TABLE_NAME = "obsidian_docs"

# Base of the Obsidian vault (mounted path)
VAULT_ROOT = Path("/mnt/obsidian")

# Initial subset of folders to index
# Now: 05_Diversys/Product plus key support/enablement domains
INITIAL_PATHS = [
    VAULT_ROOT / "00_Alfred" / "10_Diversys" / "Product",
    VAULT_ROOT / "00_Alfred" / "10_Diversys" / "Support",
    VAULT_ROOT / "00_Alfred" / "10_Diversys" / "Support_Operations",
    VAULT_ROOT / "00_Alfred" / "10_Diversys" / "Training",
    VAULT_ROOT / "00_Alfred" / "10_Diversys" / "Training_Enablement",
    VAULT_ROOT / "00_Alfred" / "10_Diversys" / "Enablement_Programs",
    VAULT_ROOT / "00_Alfred" / "10_Diversys" / "Risk_Compliance",
    VAULT_ROOT / "00_Alfred" / "10_Diversys" / "Clients",
    VAULT_ROOT / "00_Alfred" / "10_Diversys" / "Operations",
    VAULT_ROOT / "00_Alfred" / "10_Diversys" / "Delivery",
    VAULT_ROOT / "00_Alfred" / "10_Diversys" / "Strategy",
    VAULT_ROOT / "00_Alfred" / "10_Diversys" / "Management_Meetings",
    VAULT_ROOT / "00_Alfred" / "10_Diversys" / "QA",
    VAULT_ROOT / "00_Alfred" / "10_Diversys" / "KPI_Analytics",
]


class ObsidianDoc(LanceModel):
    """Schema for a single text chunk from the Obsidian vault."""

    # Raw text chunk
    text: str = Field(description="Text content of the chunk")

    # Embedding vector (OpenAI text-embedding-3-small is 1536 dimensions)
    vector: Vector(1536) = Field(description="Embedding for the text chunk")

    # Metadata
    root: str = Field(description="Top-level folder (e.g., 05_Diversys)")
    path: str = Field(description="Full Obsidian path from vault root")
    area: str | None = Field(
        default=None,
        description="Second-level area within root (e.g., Product/Support/Clients)",
    )
    agent_hint: str | None = Field(
        default=None,
        description="Agent this chunk is especially relevant to (e.g., 'support_lead')",
    )


def get_openai_client() -> OpenAI:
    """Create an OpenAI client using environment configuration.

    This assumes OPENAI_API_KEY is set in the environment
    (as it already is for your OpenClaw setup).
    """

    return OpenAI()


def embed_text(client: OpenAI, text: str) -> list[float]:
    """Get an embedding vector for a text chunk.

    Uses the same embedding model OpenClaw is configured for (adjust if needed).
    """

    # Model name can be tuned; using text-embedding-3-small as a reasonable default.
    resp = client.embeddings.create(model="text-embedding-3-small", input=text)
    return resp.data[0].embedding


def iter_markdown_files(base_paths: list[Path]):
    """Yield markdown files under the given base paths."""

    for base in base_paths:
        if not base.exists():
            continue
        for path in base.rglob("*.md"):
            # Skip Obsidian system folders if any (e.g., .obsidian)
            if any(part.startswith(".") for part in path.parts):
                continue
            yield path


def chunk_text(text: str, max_chars: int = 1200) -> list[str]:
    """Simple character-based chunking.

    Later we can replace this with a smarter token-based chunker.
    """

    text = text.strip()
    if not text:
        return []

    chunks: list[str] = []
    start = 0
    while start < len(text):
        end = start + max_chars
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        start = end
    return chunks


def infer_metadata(path: Path) -> tuple[str, str | None, list[str] | None]:
    """Infer root, area, and agent_hint from an Obsidian path.

    This uses simple heuristics aligned with Agent_Domain_Map.md.
    """

    # path relative to vault root
    rel = path.relative_to(VAULT_ROOT)
    parts = rel.parts

    root = parts[0] if parts else ""

    area: str | None = None
    if len(parts) >= 3 and root == "00_Alfred" and parts[1] == "05_Diversys":
        area = parts[1]

    agent_hint: str | None = None

    if root == "00_Alfred" and len(parts) >= 3 and parts[1] == "05_Diversys" and area == "Support":
        agent_hint = "support_lead"
    elif root == "50_Health":
        agent_hint = "agent-health"
    elif root in {"80_OpenClaw", "90_Environment", "08_Action_Items"}:
        agent_hint = "main"

    return root, area, agent_hint


def main() -> None:
    DB_ROOT.mkdir(parents=True, exist_ok=True)

    # Connect to LanceDB
    db = lancedb.connect(DB_ROOT.as_posix())

    # For this early test, drop and recreate the table to ensure schema matches
    # Use table_names() for compatibility with the installed LanceDB version.
    existing_tables = db.table_names()
    if TABLE_NAME in existing_tables:
        db.drop_table(TABLE_NAME)

    table = db.create_table(TABLE_NAME, schema=ObsidianDoc.to_arrow_schema())

    client = get_openai_client()

    rows: list[ObsidianDoc] = []

    for md_path in iter_markdown_files(INITIAL_PATHS):
        print(f"Indexing {md_path}")
        with md_path.open("r", encoding="utf-8") as f:
            text = f.read()

        chunks = chunk_text(text)
        if not chunks:
            continue

        root, area, agent_hint = infer_metadata(md_path)
        rel_path = md_path.relative_to(VAULT_ROOT).as_posix()

        for chunk in chunks:
            vec = embed_text(client, chunk)
            rows.append(
                ObsidianDoc(
                    text=chunk,
                    vector=vec,
                    root=root,
                    path=rel_path,
                    area=area,
                    agent_hint=agent_hint,
                )
            )

    if rows:
        table.add([r.model_dump() for r in rows])
        print(f"Indexed {len(rows)} chunks into {TABLE_NAME} at {DB_ROOT}")
    else:
        print("No chunks indexed (no content found in INITIAL_PATHS)")


if __name__ == "__main__":
    main()
