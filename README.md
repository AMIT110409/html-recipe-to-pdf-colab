# html-recipe-to-pdf-colab
convert html and css staticfile to pdf  for client project 

# HTML Recipe to PDF Generator (Google Colab)

Easily convert any recipe in HTML/CSS format to a beautiful, shareable PDF with professional footer—including cautionary notes, page numbers, and generation timestamp.  
Perfect for chefs, nutritionists, or anyone who wants to standardize recipe sheets.

---

## Features

- Upload your HTML and CSS recipe files.
- Automatic PDF generation with:
  - Clean A4 formatting.
  - Customizable layout via your CSS.
  - Footer on every page, including cautionary note, copyright, page numbers, and creation date.
- Designed to run in [Google Colab](https://colab.research.google.com/)—no installation or server setup needed!

---

## How to Use

1. Open the project notebook in Google Colab.
2. Run the first cell to install Playwright and its dependencies.
3. Run the second cell to upload your `.html` and `.css` files (your recipe and your styling).
4. Run the third cell to generate and download your finished PDF.

---

### Example Usage

Install Playwright and dependencies
!pip install playwright
!playwright install

Upload your recipe files
from google.colab import files
uploaded = files.upload() # Upload your .html and .css files

Python PDF generator code (see script in this repo)
Generates output_recipe.pdf


---

## Output

- A file called `output_recipe.pdf` will be automatically generated and ready for download in Colab.
- Cautionary Note appears prominently in the footer on every page.
- CSS fully controls appearance, so you can reuse your favorite recipe template.

---

## Requirements

- Google Colab (free to use)
- Two files to upload:  
  - HTML file (`*.html`)—your recipe template  
  - CSS file (`*.css`)—your recipe print styles

---

## Files in this Repo

| File Name          | Description                                   |
|--------------------|-----------------------------------------------|
| `colab_recipe_pdf.py` | Main Python script (see example in README)   |
| `example.html`     | Sample recipe HTML file                       |
| `example.css`      | Sample recipe print CSS                       |
| `README.md`        | This Documentation                            |

---

## License

MIT License. Free to use in commercial and personal projects.

---

## Author

Created by [Your Name] — 2025

If you encounter bugs or want to request features, please open an issue on GitHub.

