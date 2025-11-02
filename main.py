from PIL import Image
from pathlib import Path

def convert_png_to_webp(input_folder, output_folder, quality=80):
    """
    Convert all PNG and JPEG images in input_folder to WebP format and save to output_folder.
    
    Args:
        input_folder: Path to folder containing PNG/JPEG files
        output_folder: Path to folder where WebP files will be saved
        quality: WebP quality (0-100), default is 80
    
    Returns:
        Tuple of (successful_count, errors_list)
    """
    input_path = Path(input_folder)
    output_path = Path(output_folder)
    
    # Create output directory if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Track conversions
    successful = 0
    errors = []
    
    # Get all PNG and JPEG files
    image_files = []
    image_files.extend(input_path.glob("*.png"))
    image_files.extend(input_path.glob("*.PNG"))
    image_files.extend(input_path.glob("*.jpg"))
    image_files.extend(input_path.glob("*.JPG"))
    image_files.extend(input_path.glob("*.jpeg"))
    image_files.extend(input_path.glob("*.JPEG"))
    
    if not image_files:
        print(f"No PNG or JPEG files found in {input_folder}")
        return 0, []
    
    print(f"Found {len(image_files)} image file(s) to convert...")
    print()
    
    # Convert each image file
    for image_file in image_files:
        try:
            # Open the image
            img = Image.open(image_file)
            
            # Convert to RGB if necessary (for JPEG compatibility)
            if img.mode in ("RGBA", "LA", "P"):
                # Keep transparency for RGBA images
                pass
            elif img.mode != "RGB":
                img = img.convert("RGB")
            
            # Create output filename (same name but .webp extension)
            output_file = output_path / f"{image_file.stem}.webp"
            
            # Convert and save as WebP
            img.save(output_file, "WEBP", quality=quality)
            
            print(f"✓ Converted: {image_file.name} → {output_file.name}")
            successful += 1
            
        except Exception as e:
            error_msg = f"{image_file.name}: {str(e)}"
            errors.append(error_msg)
            print(f"✗ Failed: {error_msg}")
    
    return successful, errors


def main():
    # Define paths
    input_folder = "png files"
    output_folder = "webp files"
    quality = 80
    
    print("=" * 60)
    print("PNG/JPEG to WebP Converter")
    print("=" * 60)
    print(f"Input folder: {input_folder}")
    print(f"Output folder: {output_folder}")
    print(f"Quality: {quality}")
    print("=" * 60)
    print()
    
    # Perform conversion
    successful, errors = convert_png_to_webp(input_folder, output_folder, quality)
    
    # Print summary
    print()
    print("=" * 60)
    print("Conversion Summary")
    print("=" * 60)
    print(f"Successfully converted: {successful} file(s)")
    
    if errors:
        print(f"Failed conversions: {len(errors)}")
        print("\nErrors:")
        for error in errors:
            print(f"  - {error}")
    else:
        print("No errors encountered!")
    
    print("=" * 60)


if __name__ == "__main__":
    main()

