#!/usr/bin/env python
"""Simple test query against the obsidian_docs LanceDB table.

Usage (from venv-lancedb):
  python query_obsidian_lancedb.py "your question here"

If no question is provided, it will print a few sample rows instead.
"""

import os
import sys
from pathlib import Path

import lancedb
from openai import OpenAI

DB_ROOT = Path(os.path.expanduser("~/.openclaw/lancedb"))
TABLE_NAME = "obsidian_docs"


def get_openai_client() -> OpenAI:
    return OpenAI()


def embed_text(client: OpenAI, text: str) -> list[float]:
    resp = client.embeddings.create(model="text-embedding-3-small", input=text)
    return resp.data[0].embedding


def main() -> None:
    db = lancedb.connect(DB_ROOT.as_posix())
    if TABLE_NAME not in db.table_names():
        print(f"Table {TABLE_NAME!r} not found in {DB_ROOT}")
        return

    table = db.open_table(TABLE_NAME)

    if len(sys.argv) < 2:
        # No query provided; just show a few sample rows
        print("No query provided. Showing 3 sample rows:\n")
        for row in table.to_pandas().head(3).to_dict(orient="records"):
            print(f"root={row['root']}, path={row['path']}, area={row.get('area')}, agent_hint={row.get('agent_hint')}")
            print(f"text snippet: {row['text'][:200]!r}\n")
        return

    query = sys.argv[1]
    client = get_openai_client()
    q_vec = embed_text(client, query)

    # Retrieve top 5 nearest neighbors
    results = (
        table.search(q_vec, vector_column_name="vector")
        .metric("cosine")
        .limit(5)
        .to_pandas()
    )

    print(f"Top 5 matches for query: {query!r}\n")
    for i, row in enumerate(results.to_dict(orient="records"), start=1):
        print(f"[{i}] root={row['root']}, path={row['path']}, area={row.get('area')}, agent_hint={row.get('agent_hint')}")
        print(f"    text snippet: {row['text'][:300]!r}\n")


if __name__ == "__main__":
    main()
