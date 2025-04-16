bib-optimizer
=============

Oh, sure, because who doesn't love manually cleaning up messy `.bib` files? `bib_optimizer.py` heroically steps in to remove those lazy, _unused_ citations and _reorder_ the survivors exactly as they appear in the `.tex` file—because, clearly, chaos is the default setting for bibliographies.

In layman's terms, it automates bibliography management by:

1.  removing unused citations,
2.  reordering the remaining ones to match their order of appearance in the `.tex` file.

**Input Files:**

*   `main.tex` – The LaTeX source file.
*   `ref.bib` – The original bibliography file.

These input files will **remain unchanged**.

**Output File:**

*   `ref_opt.bib` – The newly generated, cleaned and ordered bibliography file.

* * *

Installation
------------

`pip install bib_optimizer`  
or  
`python -m pip install bib_optimizer`  
  
_🐍 This requires Python 3.8 or newer versions_

* * *

### Steps to Clean Your Bibliography

1.  **Prepare the input files (e.g., by downloading them from Overleaf)**.
2.  **Run the command to generate a new `.bib` file (for example, you may name it `ref_opt.bib`)**:   
    `bibopt main.tex ref.bib ref_opt.bib`
3.  **Use the Cleaned Bibliography**  
    Replace `ref.bib` with `ref_opt.bib` in your LaTeX project.

* * *

### Test

You may test the installation using the sample input files (`sample_main.tex` and `sample_ref.bib`) located in the test folder.

♥ Lastly executed on Python `3.10` and bibtexparser `1.4.3`