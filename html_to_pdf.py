# #!/usr/bin/env python3
# """
# HTML to PDF Converter using WeasyPrint
# Converts recipe-f.html to PDF format
# """

# import os
# import sys
# import re
# from pathlib import Path
# from datetime import datetime

# try:
#     from weasyprint import HTML, CSS
#     from weasyprint.text.fonts import FontConfiguration
# except ImportError:
#     print("Error: WeasyPrint is not installed.")
#     print("Please install it using: pip install weasyprint")
#     sys.exit(1)


# def inject_dynamic_values(html_content):
#     """
#     Inject current date and time into HTML content to replace JavaScript placeholders
#     and add data attributes for CSS access
    
#     Args:
#         html_content (str): The HTML content as string
        
#     Returns:
#         str: HTML content with dynamic values injected
#     """
#     now = datetime.now()
#     current_year = str(now.year)
#     current_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
    
#     # Replace the span placeholders with actual values
#     html_content = re.sub(
#         r'<span id="current-year"></span>', 
#         current_year, 
#         html_content
#     )
#     html_content = re.sub(
#         r'<span id="current-datetime"></span>', 
#         current_datetime, 
#         html_content
#     )
    
#     # Add data attributes to the body tag for CSS access
#     html_content = re.sub(
#         r'<body>', 
#         f'<body data-year="{current_year}" data-datetime="{current_datetime}">', 
#         html_content
#     )
    
#     return html_content


# def convert_html_to_pdf(html_file_path, output_pdf_path=None, css_file_path=None):
#     """
#     Convert HTML file to PDF using WeasyPrint
    
#     Args:
#         html_file_path (str): Path to the HTML file
#         output_pdf_path (str, optional): Path for output PDF. If None, uses HTML filename with .pdf extension
#         css_file_path (str, optional): Path to external CSS file. If None, relies on CSS linked in HTML
    
#     Returns:
#         str: Path to the generated PDF file
#     """
    
#     # Convert to Path objects for easier handling
#     html_path = Path(html_file_path)
    
#     # Check if HTML file exists
#     if not html_path.exists():
#         raise FileNotFoundError(f"HTML file not found: {html_file_path}")
    
#     # Generate output PDF path if not provided
#     if output_pdf_path is None:
#         output_pdf_path = html_path.with_suffix('.pdf')
#     else:
#         output_pdf_path = Path(output_pdf_path)
    
#     # Create output directory if it doesn't exist
#     output_pdf_path.parent.mkdir(parents=True, exist_ok=True)
    
#     print(f"Converting {html_path} to PDF...")
#     print(f"Output file: {output_pdf_path}")
    
#     try:
#         # Read HTML file content
#         with open(html_path, 'r', encoding='utf-8') as file:
#             html_content = file.read()
        
#         # Inject dynamic date/time values
#         html_content = inject_dynamic_values(html_content)
        
#         # Remove CSS link from HTML to ensure we use our modified CSS
#         html_content = re.sub(r'<link rel="stylesheet" href="recipe-f\.css">', '', html_content)
        
#         print("✅ Injected current date and time into HTML")
#         print("✅ Removed original CSS link to use dynamic CSS")
        
#         # Initialize font configuration for better font handling
#         font_config = FontConfiguration()
        
#         # Handle CSS file with dynamic content
#         stylesheets = []
#         if css_file_path and Path(css_file_path).exists():
#             # Read CSS file and inject dynamic values
#             with open(css_file_path, 'r', encoding='utf-8') as css_file:
#                 css_content = css_file.read()
            
#             # Replace placeholder with actual datetime
#             now = datetime.now()
#             current_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
            
#             # Debug: Check if placeholder exists
#             if '[DYNAMIC_DATETIME]' in css_content:
#                 css_content = css_content.replace('[DYNAMIC_DATETIME]', current_datetime)
#                 print(f"✅ Replaced [DYNAMIC_DATETIME] with: {current_datetime}")
#             else:
#                 print("⚠️  [DYNAMIC_DATETIME] placeholder not found in CSS")
            
#             # Create CSS object from string content
#             css_doc = CSS(string=css_content, font_config=font_config)
#             stylesheets.append(css_doc)
#             print(f"✅ Injected dynamic values into CSS: {css_file_path}")
        
#         # Create HTML object from string content
#         html_doc = HTML(string=html_content, base_url=str(html_path.parent))
        
#         # Generate PDF
#         if stylesheets:
#             html_doc.write_pdf(str(output_pdf_path), stylesheets=stylesheets, font_config=font_config)
#             print(f"✅ Used external stylesheets with dynamic content")
#         else:
#             # Rely on CSS linked in HTML file
#             html_doc.write_pdf(str(output_pdf_path), font_config=font_config)
#             print("⚠️  Using CSS linked in HTML (may not have dynamic content)")
        
#         print(f"PDF successfully generated: {output_pdf_path}")
#         print(f"File size: {output_pdf_path.stat().st_size / 1024:.1f} KB")
        
#         return str(output_pdf_path)
        
#     except Exception as e:
#         print(f"Error during PDF conversion: {e}")
#         raise


# def main():
#     """Main function to handle command line usage"""
    
#     # Default file paths
#     current_dir = Path(__file__).parent
#     html_file = current_dir / "recipe-f.html"
#     css_file = current_dir / "recipe-f.css"
    
#     # Generate output filename with timestamp
#     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#     output_file = current_dir / f"recipe-f_{timestamp}.pdf"
    
#     print("=" * 50)
#     print("HTML to PDF Converter (WeasyPrint)")
#     print("=" * 50)
    
#     try:
#         # Check if files exist
#         if not html_file.exists():
#             print(f"HTML file not found: {html_file}")
#             print("Please ensure recipe-f.html is in the same directory as this script.")
#             return
        
#         if not css_file.exists():
#             print(f"CSS file not found: {css_file}")
#             print("Will rely on CSS linked in HTML file.")
#             css_file = None
        
#         # Convert HTML to PDF
#         result_pdf = convert_html_to_pdf(
#             html_file_path=str(html_file),
#             output_pdf_path=str(output_file),
#             css_file_path=str(css_file) if css_file else None
#         )
        
#         print(f"\nConversion completed successfully!")
#         print(f"📄 PDF file: {result_pdf}")
        
#         # Optional: Open the PDF file (Windows)
#         if sys.platform.startswith('win'):
#             try:
#                 os.startfile(result_pdf)
#                 print("Opening PDF file...")
#             except Exception:
#                 pass
    
#     except Exception as e:
#         print(f"\nConversion failed: {e}")
#         return 1
    
#     return 0


# if __name__ == "__main__":
#     exit_code = main()
#     sys.exit(exit_code)


#!/usr/bin/env python3
"""
HTML to PDF Converter using WeasyPrint
Converts HTML file to PDF with base64 embedded images and dynamic date/time
"""

import os
import sys
import re
import base64
import time
from pathlib import Path
import argparse
import json
from datetime import datetime

try:
    from weasyprint import HTML, CSS
    from weasyprint.text.fonts import FontConfiguration
except ImportError:
    print("Error: WeasyPrint is not installed.")
    print("Please install it using: pip install weasyprint")
    sys.exit(1)


def inject_dynamic_values(html_content):
    """Inject current year and datetime in placeholders."""
    now = datetime.now()
    current_year = str(now.year)
    current_datetime = now.strftime("%Y-%m-%d %H:%M:%S")

    html_content = re.sub(
        r'<span id="current-year"></span>',
        current_year,
        html_content
    )
    html_content = re.sub(
        r'<span id="current-datetime"></span>',
        current_datetime,
        html_content
    )
    html_content = re.sub(
        r'<body>',
        f'<body data-year="{current_year}" data-datetime="{current_datetime}">',
        html_content
    )
    return html_content


def embed_images_as_base64(html_content, base_path):
    """
    Replace all <img src=""> local image URLs with base64 embedded images.
    Args:
        html_content (str): HTML content string
        base_path (Path): Path where images are located
    Returns:
        str: Modified HTML content
    """
    def convert_match(match):
        img_tag = match.group(0)
        src = match.group(1)
        if src.startswith("data:image/"):
            return img_tag  # Already embedded
        img_path = base_path / src
        if img_path.exists():
            ext = img_path.suffix.lower().lstrip('.')
            with open(img_path, 'rb') as f:
                b64 = base64.b64encode(f.read()).decode()
            data_uri = f"data:image/{ext};base64,{b64}"
            new_img_tag = img_tag.replace(src, data_uri)
            return new_img_tag
        else:
            return img_tag  # leave as is if file not found

    pattern = r'<img[^>]+src=[\'"]([^\'"]+)[\'"]'
    return re.sub(pattern, convert_match, html_content)


def apply_recipe_data_to_section(section_html: str, recipe: dict) -> str:
    """Replace key fields inside a single <main> section using recipe data."""
    title = recipe.get('title')
    category = recipe.get('category')
    image_url = recipe.get('image_url')

    # Replace <h1>..</h1>
    if title:
        section_html = re.sub(r'(<h1>)([\s\S]*?)(</h1>)', rf'\1{title}\3', section_html, flags=re.IGNORECASE)

    # Replace category inside <div class="sub">..</div>
    if category:
        section_html = re.sub(r'(<div class="sub">)([\s\S]*?)(</div>)', rf'\1{category}\3', section_html, flags=re.IGNORECASE)

    # Replace first image src (panel image)
    if image_url:
        section_html = re.sub(r'(<img[^>]+src=[\"\'])([^\"\']+)([\"\'][^>]*>)', rf'\1{image_url}\3', section_html, count=1)

    return section_html


def convert_html_to_pdf(html_file_path, output_pdf_path=None, css_file_path=None, repeat_count=1, data_file_path=None):
    start_time = time.time()

    html_path = Path(html_file_path)
    if not html_path.exists():
        raise FileNotFoundError(f"HTML file not found: {html_file_path}")

    if output_pdf_path is None:
        output_pdf_path = html_path.with_suffix('.pdf')
    else:
        output_pdf_path = Path(output_pdf_path)

    output_pdf_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"Converting {html_path} to PDF...")
    print(f"Output file: {output_pdf_path}")

    with open(html_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Duplicate content either from data file (per-recipe) or by repeat_count
    if data_file_path:
        try:
            with open(data_file_path, 'r', encoding='utf-8') as df:
                recipes = json.load(df)
            if not isinstance(recipes, list):
                raise ValueError('Data file must contain a JSON array of recipes')
        except Exception as e:
            raise RuntimeError(f"Failed to read data file {data_file_path}: {e}")

        main_match = re.search(r'<main[\s\S]*?</main>', html_content, flags=re.IGNORECASE)
        if main_match:
            main_html = main_match.group(0)
            repeated = []
            for idx, recipe in enumerate(recipes):
                section = apply_recipe_data_to_section(main_html, recipe)
                repeated.append(section)
                if idx != len(recipes) - 1:
                    repeated.append('<div style="page-break-before: always;"></div>')
            html_content = re.sub(r'<main[\s\S]*?</main>', ''.join(repeated), html_content, flags=re.IGNORECASE)
            print(f"✅ Built document from data file with {len(recipes)} recipes")
        else:
            print("⚠️  <main> section not found; skipping data-driven build")

    elif repeat_count and repeat_count > 1:
        main_match = re.search(r'<main[\s\S]*?</main>', html_content, flags=re.IGNORECASE)
        if main_match:
            main_html = main_match.group(0)
            repeated = []
            for i in range(repeat_count):
                repeated.append(main_html)
                if i != repeat_count - 1:
                    repeated.append('<div style="page-break-before: always;"></div>')
            html_content = re.sub(r'<main[\s\S]*?</main>', ''.join(repeated), html_content, flags=re.IGNORECASE)
            print(f"✅ Repeated recipe section {repeat_count} times")
        else:
            print("⚠️  <main> section not found; skipping repetition")

    # Embed images as base64
    html_content = embed_images_as_base64(html_content, base_path=html_path.parent)

    # Inject dynamic date/time
    html_content = inject_dynamic_values(html_content)

    # Remove reference to original CSS so we can inject or use CSS file explicitly
    html_content = re.sub(r'<link rel="stylesheet" href="recipe-f\.css">', '', html_content)

    print("✅ Injected dynamic date/time")
    print("✅ Embedded images as base64")
    print("✅ Removed original CSS link to allow stylesheet injection")

    font_config = FontConfiguration()
    stylesheets = []
    if css_file_path and Path(css_file_path).exists():
        with open(css_file_path, 'r', encoding='utf-8') as css_file:
            css_content = css_file.read()

        now = datetime.now()
        current_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
        if '[DYNAMIC_DATETIME]' in css_content:
            css_content = css_content.replace('[DYNAMIC_DATETIME]', current_datetime)
            print(f"✅ Replaced [DYNAMIC_DATETIME] placeholder in CSS")
        else:
            print("⚠️  [DYNAMIC_DATETIME] placeholder not found in CSS")

        css_doc = CSS(string=css_content, font_config=font_config)
        stylesheets.append(css_doc)

    html_doc = HTML(string=html_content, base_url=str(html_path.parent))

    if stylesheets:
        html_doc.write_pdf(str(output_pdf_path), stylesheets=stylesheets, font_config=font_config)
        print("✅ PDF generated using external stylesheet with dynamic content")
    else:
        html_doc.write_pdf(str(output_pdf_path), font_config=font_config)
        print("⚠️  PDF generated using CSS linked in HTML (may lack dynamic content)")

    elapsed_time = time.time() - start_time
    try:
        file_size_bytes = output_pdf_path.stat().st_size
        size_mb = file_size_bytes / (1024 * 1024)
        print(f"PDF successfully generated: {output_pdf_path}")
        print(f"Time taken: {elapsed_time:.2f} seconds | Size: {size_mb:.2f} MB")
    except Exception:
        print(f"PDF successfully generated: {output_pdf_path}")
        print(f"Time taken: {elapsed_time:.2f} seconds")

    return str(output_pdf_path)


def main():
    parser = argparse.ArgumentParser(description="Convert HTML to PDF using WeasyPrint.")
    parser.add_argument("--html", type=str, help="Path to the HTML file. Defaults to recipe-f.html in script directory.")
    parser.add_argument("--css", type=str, help="Path to the CSS file. Defaults to recipe-f.css in script directory.")
    parser.add_argument("--output", type=str, help="Output PDF path. Defaults to recipe-f_YYYYmmdd_HHMMSS.pdf in script directory.")
    parser.add_argument("--repeat", type=int, default=1, help="Number of times to repeat the recipe section in the PDF (e.g., 100).")
    parser.add_argument("--data", type=str, help="Path to JSON file containing an array of recipes to render.")

    args = parser.parse_args()

    script_dir = Path(__file__).parent
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    html_file = Path(args.html) if args.html else (script_dir / "recipe-f.html")
    css_file = Path(args.css) if args.css else (script_dir / "recipe-f.css")
    output_file = Path(args.output) if args.output else (script_dir / f"recipe-f_{timestamp}.pdf")

    print("=" * 60)
    print("HTML to PDF Converter (WeasyPrint) with Base64 Images")
    print("=" * 60)

    if not html_file.exists():
        print(f"HTML file not found: {html_file}")
        return 1
    if not css_file.exists():
        print(f"CSS file not found: {css_file}")
        css_file = None

    try:
        result_pdf = convert_html_to_pdf(
            html_file_path=str(html_file),
            output_pdf_path=str(output_file),
            css_file_path=str(css_file) if css_file else None,
            repeat_count=int(args.repeat) if hasattr(args, 'repeat') and args.repeat else 1,
            data_file_path=str(args.data) if hasattr(args, 'data') and args.data else None
        )

        print(f"PDF file generated: {result_pdf}")

    except Exception as e:
        print(f"Error during PDF conversion: {e}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())