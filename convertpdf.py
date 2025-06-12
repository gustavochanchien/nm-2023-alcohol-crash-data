"""
convert_pdf_to_png.py

A simple script to convert each page of a PDF into a high-resolution PNG image.

Dependencies:
  • pdf2image  (pip install pdf2image)
  • poppler     (system package; e.g. apt install poppler-utils or download binaries for Windows)

Usage:
  python convert_pdf_to_png.py input.pdf

Example:
  python convert_pdf_to_png.py albuquerque.pdf
"""
import os
import sys
from pdf2image import convert_from_path

def convert_pdf_to_png(input_path: str, dpi: int = 300):
    if not os.path.isfile(input_path):
        print(f"Error: File '{input_path}' does not exist.")
        return

    output_dir = os.path.dirname(input_path) or '.'
    base_name = os.path.splitext(os.path.basename(input_path))[0]

    try:
        pages = convert_from_path(input_path, dpi=dpi)
    except Exception as e:
        print(f"Error converting PDF: {e}")
        return

    for i, page in enumerate(pages, start=1):
        output_path = os.path.join(output_dir, f"{base_name}_page_{i:03d}.png")
        page.save(output_path, 'PNG')
        print(f"Saved: {output_path}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python convert_pdf_to_png.py input.pdf")
        return

    input_path = sys.argv[1]
    convert_pdf_to_png(input_path)

if __name__ == '__main__':
    main()
