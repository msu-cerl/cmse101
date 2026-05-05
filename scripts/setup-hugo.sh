#!/bin/bash
# setup-hugo.sh
# Initialize Hugo site with Book theme

set -e

echo "=== Setting Up Hugo Site ==="

# Check if Hugo is installed
if ! command -v hugo &> /dev/null; then
    echo "Hugo is not installed. Installing..."
    # For macOS
    if [[ "$OSTYPE" == "darwin"* ]]; then
        brew install hugo
    else
        echo "Please install Hugo from https://gohugo.io/installation/"
        exit 1
    fi
fi

echo "✓ Hugo installed"

# Clone the Book theme
if [ ! -d "themes/book" ]; then
    echo "Downloading Book theme..."
    git clone https://github.com/alex-shpak/hugo-book themes/book
    echo "✓ Theme installed"
else
    echo "✓ Theme already exists"
fi

# Create .gitignore
cat > .gitignore << 'EOF'
# Hugo
resources/
public/
themes/book/.git

# Pandoc output
output/

# OS
.DS_Store
Thumbs.db

# Editor
.vscode/
.idea/
*.swp
*.swo

# Dependencies
node_modules/
EOF

echo "✓ .gitignore created"

# Create base template for UDL PDF header
cat > pdf-header.tex << 'EOF'
% UDL-Compliant PDF Header
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{hyperref}
\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    urlcolor=blue,
    pdfinfo={
        Title={\@title},
        Author={AI and Society Course},
        Subject={Course Materials},
        Keywords={AI, Society, Education},
    }
}

% Accessibility: Set PDF to be tagged for screen readers
\usepackage{tagpdf}
\tagpdfsetup{activate-all}

% Font sizing for accessibility
\usepackage{fontspec}
\setmainfont{Calibri}[
    Path=./fonts/,
    Extension=.ttf,
    UprightFont=*-regular,
    BoldFont=*-bold,
    ItalicFont=*-italic,
    BoldItalicFont=*-bolditalic
]
EOF

echo "✓ PDF template created"

echo ""
echo "=== Setup Complete ==="
echo "To start editing:"
echo "  hugo server"
echo ""
echo "To build the site:"
echo "  hugo"
echo ""
echo "Next: Edit content/ files and config.toml with your course details"
