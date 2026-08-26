#!/bin/bash

# Build MARP slides to HTML and PDF
# Usage: ./build-slides.sh
# or: ./build-slides.sh lecture-01-welcome

set -e

CONTENT_DIR="./content/slides"
OUTPUT_DIR="./public/slides"
THEME_FILE="${CONTENT_DIR}/_theme.css"

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Build specific slide or all slides
if [ -n "$1" ]; then
  SLIDES="${CONTENT_DIR}/${1}.md"
else
  SLIDES="${CONTENT_DIR}/lecture-*.md"
fi

echo "Building MARP slides..."

for slide_file in $SLIDES; do
  if [ ! -f "$slide_file" ]; then
    echo "Error: $slide_file not found"
    exit 1
  fi

  filename=$(basename "$slide_file" .md)
  html_output="${OUTPUT_DIR}/${filename}.html"
  pdf_output="${OUTPUT_DIR}/${filename}.pdf"

  echo "  → $filename"

  # Generate HTML
  npx marp "$slide_file" \
    --css "$THEME_FILE" \
    --html \
    --output "$html_output"

  # Generate PDF (requires Chromium/Chrome)
  npx marp "$slide_file" \
    --css "$THEME_FILE" \
    --pdf \
    --output "$pdf_output"
done

echo "✓ Slides built successfully!"
echo ""
echo "Output directory: $OUTPUT_DIR"
echo "HTML files: ready for web viewing"
echo "PDF files: ready for download/D2L upload"
