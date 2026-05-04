#!/bin/bash
OUTPUT_FILE="/mnt/obsidian/00_Alfred/10_Diversys/Product/Product_KB.md"
TARGET_DIR="/mnt/obsidian/00_Alfred/10_Diversys/Product"

echo "# Product Knowledge Base\n\n" > "$OUTPUT_FILE"
echo "Generated on $(date -u) (UTC)\n\n" >> "$OUTPUT_FILE"

found_product_docs=()

# Ensure the output directory exists
mkdir -p "$(dirname "$OUTPUT_FILE")"

# Exclude the output file from the find results
find "$TARGET_DIR" -type f -name "*.md" ! -path "$OUTPUT_FILE" | sort | while read -r file; do
    if [ -f "$file" ]; then
        # Calculate relative path to use as a readable source identifier
        relative_path="${file#$TARGET_DIR/}"
        if [ "$relative_path" == "$file" ]; then # Fallback if path doesn't start with TARGET_DIR
            relative_path="$(basename "$file")"
        fi

        echo "## Source: $relative_path\n\n" >> "$OUTPUT_FILE"
        cat "$file" >> "$OUTPUT_FILE"
        echo "\n\n---\n\n" >> "$OUTPUT_FILE"
        found_product_docs+=("$(basename "$file")")
    fi
done
echo "---SUMMARY_START---"
echo "FOUND_PRODUCT_DOCS: ${found_product_docs[*]}"
echo "---SUMMARY_END---"