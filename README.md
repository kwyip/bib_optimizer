  <figure>
    <img src="https://github.com/kwyip/bib_optimizer/blob/main/logo.png?raw=True" alt="logo" height="143" />
    <!-- <figcaption>An elephant at sunset</figcaption> -->
  </figure>

[![](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/kwyip/bib_optimizer/blob/main/LICENSE)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/bib-optimizer)](https://pypi.org/project/bib-optimizer/)
[![Static Badge](https://img.shields.io/badge/CalVer-2025.0416-ff5733)](https://pypi.org/project/bib-optimizer)
[![Static Badge](https://img.shields.io/badge/PyPI-wheels-d8d805)](https://pypi.org/project/bib-optimizer/#files)
[![](https://pepy.tech/badge/bib_optimizer/month)](https://pepy.tech/project/bib_optimizer)

[bib-optimizer](https://bibopt.github.io/)
==========================================

Oh, sure, because who doesn't love manually cleaning up messy `.bib` files? `bib_optimizer.py` heroically steps in to remove those lazy, _unused_ citations and _reorder_ the survivors exactly as they appear in the `.tex` file—because, clearly, chaos is the default setting for bibliographies.

In layman's terms, it automates bibliography management by:

1.  removing unused citations,
2.  reordering the remaining ones to match their order of appearance in the `.tex` file.

**Input Files:**

*   `main.tex` – The LaTeX source file.
*   `ref.bib` – The original bibliography file.

These input files will **remain unchanged**.

**Output File:**

*   `ref_opt.bib` – A placeholder filename for the newly generated, cleaned, and ordered bibliography file.

* * *

Installation
------------

It can be installed with `pip`, ideally by using a [virtual environment](https://realpython.com/what-is-pip/#using-pip-in-a-python-virtual-environment). Open up a terminal and install the package and the dependencies with:  
  

    `pip install bib_optimizer`

_or_

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

<img src="https://github.com/kwyip/bib_optimizer/blob/main/sample_main_shot.png?raw=True" alt="sample_main_shot"  width="34.83%"/>&nbsp;&nbsp;<img src="https://github.com/kwyip/bib_optimizer/blob/main/sample_ref_shot.png?raw=True" alt="sample_ref_shot" width="43%" />

`sample_main.tex` _and_ `sample_ref.bib`

<img src="https://github.com/kwyip/bib_optimizer/blob/main/sample_ref_opt_shot.png?raw=True" alt="sample_ref_opt_shot" width="43%" />

_A sample_ `ref_opt.bib` _created after running_ `bibopt sample_main.tex sample_ref.bib ref_opt.bib`

---
#### New feature (version 0.4.0)

If the `main.tex` calls inputs from other `.tex` (e.g., with `\input{...}`), the newly generated `ref_opt.bib` will preserve the order of appearances in the `main.tex` with each inputted `.tex` as well. \
(The dependent `.tex` files need to be placed in the same directory as `main.tex`.)

---
#### New feature (version 0.4.1)

On top of version 0.4, skip any `\input` `.tex` file if not found.

---
#### New feature (version 0.4.2)

In addition to handling the `\input{...}` command, it also supports the `\include{...}` command.

♥ Lastly executed on Python `3.10` on 2025-07-14.