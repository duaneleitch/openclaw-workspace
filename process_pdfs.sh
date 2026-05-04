#!/bin/bash
# process_pdfs.sh

PDF_TO_TEXT_SCRIPT="/home/duane/.local/bin/pdf-to-text.sh"
declare -a processed_files
declare -a new_conversions
declare -a errors

process_directory() {
    local dir="$1"
    echo "Processing directory: $dir"
    find "$dir" -type f -name "*.pdf" | while read -r pdf_file; do
        txt_file="${pdf_file%.pdf}.txt"
        
        # Check if the PDF file exists and is readable
        if [ ! -f "$pdf_file" ]; then
            errors+=("PDF file not found or unreadable: $pdf_file")
            continue
        fi

        processed_files+=("$(basename "$pdf_file")")

        if [ ! -f "$txt_file" ] || [ "$pdf_file" -nt "$txt_file" ]; then
            echo "Converting $pdf_file to $txt_file..."
            "$PDF_TO_TEXT_SCRIPT" "$pdf_file" > "$txt_file" 2>&1
            if [ $? -eq 0 ]; then
                new_conversions+=("$(basename "$pdf_file")")
                echo "Successfully converted $pdf_file"
            else
                errors+=("Error converting $pdf_file")
                echo "Error converting $pdf_file" >&2
            fi
        else
            echo "Skipping $pdf_file, $txt_file is up to date."
        fi
    done
}

# Call process_directory for each argument passed to this script
for arg_dir in "$@"; do
    process_directory "$arg_dir"
done

# Output summary for the parent agent
echo "---SUMMARY_START---"
echo "PROCESSED_PDFS: ${processed_files[*]}"
echo "NEW_CONVERSIONS: ${new_conversions[*]}"
echo "ERRORS: ${errors[*]}"
echo "---SUMMARY_END---"
