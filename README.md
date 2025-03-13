# bib-cleaner
Oh, sure, because who doesn't love manually cleaning up messy `.bib` files? `bib_cleaner.py` heroically steps in to remove those lazy, unused citations and reorder the survivors exactly as they appear in the `.tex` file—because, clearly, chaos is the default setting for bibliographies.

Step 1: `pip install bibtexparser` (Python 3)

Step 2: Run `python bib_cleaner.py main.tex ref.bib ref_clean.bib` 

(`main.tex` is your `.tex` filename, `ref.bib` is your `.bib` filename, `ref_clean.bib` is the desired filename for the new `.bib` file.

Step 3: Use `ref_clean.bib`
