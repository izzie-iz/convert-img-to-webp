# Image to WebP Converter

A simple and efficient Python tool to convert PNG and JPEG images to WebP format with customizable quality settings.

## Features

- 🖼️ Converts PNG and JPEG images to WebP format
- 📁 Batch processing of multiple images
- 🎨 Preserves transparency for RGBA images
- ⚙️ Customizable quality settings (0-100)
- 📊 Detailed conversion summary with success/error reporting
- 🔄 Automatic output directory creation

## Requirements

- Python 3.6 or higher
- Pillow (PIL) library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/izzie-iz/convert-img-to-webp.git
cd convert-img-to-webp
```

2. Create a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Place your PNG or JPEG files in the `png files` folder (or modify the `input_folder` variable in `main.py`)

2. Run the converter:
```bash
python main.py
```

3. Converted WebP files will be saved in the `webp files` folder

## Supported Formats

**Input formats:**
- PNG (`.png`, `.PNG`)
- JPEG (`.jpg`, `.JPG`, `.jpeg`, `.JPEG`)

**Output format:**
- WebP (`.webp`)

## Why WebP?

WebP is a modern image format that provides superior compression for images on the web. Benefits include:

- **Smaller file sizes**: 25-35% smaller than PNG and JPEG
- **Faster loading**: Reduced bandwidth usage
- **Quality preservation**: Supports both lossy and lossless compression
- **Transparency support**: Like PNG, but with better compression
- **Wide browser support**: Supported by all modern browsers


## Project Structure

```
convert-img-to-webp/
├── main.py              # Main converter script
├── requirements.txt     # Python dependencies
├── README.md           # This file
├── .gitignore          # Git ignore rules
├── png files/          # Input folder (create this)
└── webp files/         # Output folder (auto-created)
```

## Acknowledgments

- Built with [Pillow (PIL)](https://python-pillow.org/) - The friendly PIL fork

