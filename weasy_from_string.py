#!/usr/bin/env python3   ## shebangline that tells the system to use pthon 3 interpreter
"""
Render a PDF from a full HTML string using WeasyPrint and report time + size.

Usage:
  python weasy_from_string.py --html recipes_100.html --output recipes_100_weasy.pdf
"""## docstring help us to understnd the user requirement and function of code . 

import argparse
import time
from pathlib import Path

from weasyprint import HTML


def print_pdf_from_html(html_string: str, output_file: Path, base_url: str | None = None) -> float:
    start = time.perf_counter()
    html = HTML(string=html_string, base_url=base_url)
    html.write_pdf(str(output_file))
    elapsed = time.perf_counter() - start
    return elapsed


def main() -> int:
    parser = argparse.ArgumentParser(description="WeasyPrint: render PDF from HTML string and report metrics.")
    parser.add_argument("--html", required=True, help="Path to the HTML file to read and render as a string.")
    parser.add_argument("--output", default="output.pdf", help="Path to write the resulting PDF.")
    args = parser.parse_args()

    html_path = Path(args.html)
    output_path = Path(args.output)

    if not html_path.exists():
        print(f"HTML file not found: {html_path}")
        return 1

    html_string = html_path.read_text(encoding="utf-8")

    # base_url allows WeasyPrint to resolve linked assets like recipe-f.css
    base_url = str(html_path.parent)

    print("Rendering PDF from HTML string ...")
    elapsed = print_pdf_from_html(html_string, output_path, base_url=base_url)

    size_bytes = output_path.stat().st_size if output_path.exists() else 0
    size_mb = size_bytes / (1024 * 1024)

    print(f"PDF generated successfully: {output_path}")
    print(f"Time taken: {elapsed:.2f} seconds | Size: {size_mb:.2f} MB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


