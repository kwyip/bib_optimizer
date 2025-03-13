# bib-cleaner
Oh, sure, because who doesn't love manually cleaning up messy `.bib` files? `bib_cleaner.py` heroically steps in to remove those lazy, unused citations and reorder the survivors exactly as they appear in the `.tex` file—because, clearly, chaos is the default setting for bibliographies.

**Input Files:**
- `main.tex` – The LaTeX source file.
- `ref.bib` – The original bibliography file.  

These input files will **remain unchanged**.

**Output File:**
- `ref_clean.bib` – The newly generated, cleaned bibliography file.

------------------------------------------------------------------------------
Step 1: `pip install bibtexparser` (Python 3)

### Steps to Clean Your Bibliography

1. **Install Dependencies**  
   ```sh
   pip install bibtexparser  # Requires Python 3
2. **Run the Script
   ```sh
   python bib_cleaner.py main.tex ref.bib ref_clean.bib


Step 2: Run `python bib_cleaner.py main.tex ref.bib ref_clean.bib` 

Step 3: Use `ref_clean.bib`



_____________
Lastly executed on Python `3.10` and bibtexparser `4.3`
