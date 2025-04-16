<<<<<<< HEAD
<!DOCTYPE html>
<html>
<header>
  <h1 id="bib-optimizer">bib-optimizer</h1>
</header>
<main>
  <p>Oh, sure, because who doesn&#39;t love manually cleaning up messy <code>.bib</code> files?
    <code>bib_optimizer.py</code> heroically steps in to remove those lazy, <em>unused</em> citations and
    <em>reorder</em> the survivors exactly as they appear in the <code>.tex</code> file—because, clearly, chaos is
    the
    default setting for bibliographies.
  </p>
  <p>In layman&#39;s terms, it automates bibliography management by:</p>
  <ol>
    <li>removing unused citations,</li>
    <li>reordering the remaining ones to match their order of appearance in the <code>.tex</code> file.</li>
  </ol>

  <p><strong>Input Files:</strong></p>
  <ul>
    <li><code>main.tex</code> – The LaTeX source file.</li>
    <li><code>ref.bib</code> – The original bibliography file. </li>
  </ul>
  <p>These input files will <strong>remain unchanged</strong>.</p>
  <p><strong>Output File:</strong></p>
  <ul>
    <li><code>ref_opt.bib</code> – The newly generated, cleaned and ordered bibliography file.</li>
  </ul>
</main>
<hr>
<h2> Installation </h2>
<footnote>
  <h3 id="steps-to-clean-your-bibliography">Steps to Clean Your Bibliography</h3>
  <ol>
    <li><strong>Install Dependencies</strong>:&nbsp<code>pip install bibtexparser # Requires Python 3</code>
    </li>
    <li><strong>Run the Script</strong>:&nbsp<code>python bib_optimizer.py main.tex ref.bib ref_opt.bib</code>
    </li>
    <li><strong>Use the Cleaned Bibliography</strong><br />
      Replace <code>ref.bib</code> with
      <code>ref_opt.bib</code> in
      your LaTeX project.
    </li>
  </ol>
  <hr>
  <marquee>
    <summary>
      <p>&hearts; Lastly executed on Python <code>3.10</code> and bibtexparser <code>1.4.3</code></p>
    </summary>
  </marquee>
</footnote>

</html>
=======
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

♥ Lastly executed on Python `3.10` and bibtexparser `1.4.3`
>>>>>>> test_packaging
