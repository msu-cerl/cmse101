#!/bin/bash
# convert-to-formats.sh
# Convert markdown files to PDF and Word documents for distribution

set -e

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== Course Material Format Converter ===${NC}"

# Create output directories
mkdir -p output/pdf
mkdir -p output/docx

# Function to convert a markdown file
convert_file() {
    local input_file=$1
    local output_name=$2
    
    if [ ! -f "$input_file" ]; then
        echo "Error: $input_file not found"
        return 1
    fi
    
    echo -e "${BLUE}Converting: $input_file${NC}"
    
    # PDF conversion (basic, accessible format)
    pandoc "$input_file" \
        -f markdown \
        -t pdf \
        -o "output/pdf/${output_name}.pdf" \
        --pdf-engine=xelatex \
        --metadata title="${output_name}"
    echo -e "${GREEN}✓ PDF created: output/pdf/${output_name}.pdf${NC}"
    
    # Word conversion (basic format)
    pandoc "$input_file" \
        -f markdown \
        -t docx \
        -o "output/docx/${output_name}.docx" \
        --metadata title="${output_name}"
    echo -e "${GREEN}✓ Word document created: output/docx/${output_name}.docx${NC}"
    
    echo ""
}

# Convert Syllabus
convert_file "content/docs/syllabus.md" "AI-and-Society-Syllabus"

# Convert all readings
for reading_file in content/readings/week-*.md; do
    if [ -f "$reading_file" ]; then
        week_name=$(basename "$reading_file" .md)
        convert_file "$reading_file" "Readings-${week_name}"
    fi
done

# Convert assignments
for assignment_file in content/assignments/*.md; do
    if [ -f "$assignment_file" ]; then
        assignment_name=$(basename "$assignment_file" .md)
        if [ "$assignment_name" != "_index" ]; then
            convert_file "$assignment_file" "Assignment-${assignment_name}"
        fi
    fi
done

# Convert resources
convert_file "content/docs/resources.md" "Course-Resources"

echo -e "${BLUE}=== Conversion Complete ===${NC}"
echo "Files ready for D2L upload in output/ directory"
echo ""
echo "Next steps:"
echo "1. Review PDF and Word files in output/"
echo "2. Upload to D2L Brightspace"
echo "3. Share documents with students"
