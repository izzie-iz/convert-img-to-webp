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

### Basic Usage

1. Place your PNG or JPEG files in the `png files` folder.
2. Run the converter:
```bash
python main.py
```

3. Converted WebP files will be saved in the `webp files` folder

### Custom Usage

You can use the converter as a module in your own Python scripts:

```python
from main import convert_png_to_webp

# Convert images with custom settings
successful, errors = convert_png_to_webp(
    input_folder="path/to/input",
    output_folder="path/to/output",
    quality=85
)

print(f"Converted {successful} images")
```

### Parameters

- `input_folder`: Path to the folder containing your PNG/JPEG files
- `output_folder`: Path where converted WebP files will be saved
- `quality`: WebP quality setting (0-100, default: 80)
  - Higher values = better quality but larger file size
  - Lower values = smaller file size but reduced quality

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

## Example Output

```
============================================================
PNG/JPEG to WebP Converter
============================================================
Input folder: png files
Output folder: webp files
Quality: 80
============================================================

Found 5 image file(s) to convert...

✓ Converted: image1.png → image1.webp
✓ Converted: image2.png → image2.webp
✓ Converted: photo.jpg → photo.webp
✓ Converted: graphic.PNG → graphic.webp
✓ Converted: picture.jpeg → picture.webp

============================================================
Conversion Summary
============================================================
Successfully converted: 5 file(s)
No errors encountered!
============================================================
```

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

## Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest new features
- Submit pull requests

## License

This project is open source and available under the MIT License.

## Author

Created by [izzie-iz](https://github.com/izzie-iz)

## Acknowledgments

- Built with [Pillow (PIL)](https://python-pillow.org/) - The friendly PIL fork

