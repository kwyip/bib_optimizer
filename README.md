  <figure>
    <img src="https://github.com/kwyip/bib_optimizer/blob/main/logo.png?raw=True" alt="logo" height="143" />
    <!-- <figcaption>An elephant at sunset</figcaption> -->
  </figure>

[![](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/kwyip/bib_optimizer/blob/main/LICENSE)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/bib_optimizer)](https://pypi.org/project/bib-optimizer/)
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

### Install from PyPI with pip

Create and activate a virtual environment, then install the latest release from PyPI:

```bash
python -m venv .venv

# Linux/macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate

python -m pip install --upgrade bib_optimizer
```

Alternatively, install the command in an isolated environment with [uv](https://docs.astral.sh/uv/):

```bash
uv tool install bib_optimizer
```

After either installation method, the `bibopt` command is available in your terminal.

### Install from source for development

This repository uses uv for project and dependency management.

1. **Clone the repository**

   ```bash
   git clone https://github.com/kwyip/bib_optimizer.git
   cd bib_optimizer
   ```

2. **Install environment**

   ```bash
   # This creates the virtual environment and installs all dependencies
   uv sync
   ```

3. **Activate environment**

   ```bash
   # Linux/MacOS
   source .venv/bin/activate

   # Windows
   .venv\Scripts\activate
   ```

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

* * *

## Code-free use with an AI agent

[**Download `SKILL.md`**](./SKILL.md), then upload these files to your AI agent:

- `SKILL.md`,
- the root `.tex` file,
- the source `.bib` file, and if any:
- every `.tex` file referenced through `\input` or `\include`.

> [!TIP]
> Use this prompt:
>
> ```text
> Use the attached `SKILL.md` to optimize the attached LaTeX and BibTeX files.
> Return only the optimized `.bib` file.
> ```


https://github.com/user-attachments/assets/2b4e3224-2aee-44c1-974c-812dead72e2f


* * *

#### New feature (version 0.4.0)

If the `main.tex` calls inputs from other `.tex` (e.g., with `\input{...}`), the newly generated `ref_opt.bib` will preserve the order of appearances in the `main.tex` with each inputted `.tex` as well. \
(The dependent `.tex` files need to be placed in the same directory as `main.tex`.)

---
#### New feature (version 0.4.1)

On top of version 0.4, skip any `\input` `.tex` file if not found.

---
#### New feature/Fix (version 0.4.2)

Added support for the `\include{...}` command in addition to `\input{...}`, fixing missing citations when a LaTeX project uses `\include` to split its content across files.

---
#### New feature/Fix (version 0.4.3)

Added Python 3.14 support and constrained `bibtexparser` to the compatible 1.x release series, fixing `ModuleNotFoundError: No module named 'bibtexparser.bwriter'` during fresh installations.

---
#### New feature/Fix (version 0.5.0)

Add code-free SKILL.md

♥ Lastly executed on Python `3.14` on 2026-09-29.
