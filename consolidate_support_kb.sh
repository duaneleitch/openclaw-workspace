#!/bin/bash
OUTPUT_FILE="/mnt/obsidian/00_Alfred/10_Diversys/Support/Support_FAQ_KB.md"
TARGET_DIRS=(
    "/mnt/obsidian/00_Alfred/10_Diversys/Support/FAQs"
    "/mnt/obsidian/00_Alfred/10_Diversys/Support/FAQ - PDFs"
)

echo "# Support FAQ Knowledge Base\n\n" > "$OUTPUT_FILE"
echo "Generated on $(date -u) (UTC)\n\n" >> "$OUTPUT_FILE"

found_support_docs=()

for dir in "${TARGET_DIRS[@]}"; do
    find "$dir" -type f \( -name "*.md" -o -name "*.txt" \) | sort | while read -r file; do
        if [ -f "$file" ]; then
            # Calculate relative path to use as a readable source identifier
            # This handles cases where file might be directly in dir or in subdirectories
            relative_path="${file#$dir/}"
            # If the file is directly in the root of the target_dir, relative_path will be its basename
            if [ "$relative_path" == "$file" ]; then
                relative_path="$(basename "$file")"
            fi

            echo "## Source: $relative_path\n\n" >> "$OUTPUT_FILE"
            cat "$file" >> "$OUTPUT_FILE"
            echo "\n\n---\n\n" >> "$OUTPUT_FILE"
            found_support_docs+=("$(basename "$file")")
        fi
    done
done
echo "---SUMMARY_START---"
echo "FOUND_SUPPORT_DOCS: ${found_support_docs[*]}"
echo "---SUMMARY_END---"