<!-- # bib-cleaner
Oh, sure, because who doesn't love manually cleaning up messy `.bib` files? `bib_cleaner.py` heroically steps in to remove those lazy, *unused* citations and *reorder* the survivors exactly as they appear in the `.tex` file—because, clearly, chaos is the default setting for bibliographies.

In layman's terms, it automates bibliography management by removing unused citations and reordering the remaining ones to match their appearance in the `.tex` file.

**Input Files:**
- `main.tex` – The LaTeX source file.
- `ref.bib` – The original bibliography file.  

These input files will **remain unchanged**.

**Output File:**
- `ref_clean.bib` – The newly generated, cleaned bibliography file.

------------------------------------------------------------------------------
### Steps to Clean Your Bibliography

1. **Install Dependencies**  
   ```sh
   pip install bibtexparser  # Requires Python 3
2. **Run the Script**  
   ```sh
   python bib_cleaner.py main.tex ref.bib ref_clean.bib
3. **Use the Cleaned Bibliography**  
   Replace `ref.bib` with `ref_clean.bib` in your LaTeX project.



_____________
Lastly executed on Python `3.10` and bibtexparser `4.3` -->


<h1 id="bib-optimizer">bib-optimizer</h1>
<p>Oh, sure, because who doesn&#39;t love manually cleaning up messy <code>.bib</code> files? <code>bib_optimizer.py</code> heroically steps in to remove those lazy, <em>unused</em> citations and <em>reorder</em> the survivors exactly as they appear in the <code>.tex</code> file—because, clearly, chaos is the default setting for bibliographies.</p>
<p>In layman&#39;s terms, it automates bibliography management by:</p>
<ol>
  <li>Removing unused citations</li>
  <li>Reordering the remaining ones to match their appearance in the <code>.tex</code> file.</li>
</ol>

<p><strong>Input Files:</strong></p>
<ul>
<li><code>main.tex</code> – The LaTeX source file.</li>
<li><code>ref.bib</code> – The original bibliography file.  </li>
</ul>
<p>These input files will <strong>remain unchanged</strong>.</p>
<p><strong>Output File:</strong></p>
<ul>
<li><code>ref_clean.bib</code> – The newly generated, cleaned bibliography file.</li>
</ul>
<hr>
<h3 id="steps-to-clean-your-bibliography">Steps to Clean Your Bibliography</h3>
<ol>
<li><strong>Install Dependencies</strong><br>```sh
pip install bibtexparser  # Requires Python 3</li>
<li><strong>Run the Script</strong><br>```sh
python bib_cleaner.py main.tex ref.bib ref_clean.bib</li>
<li><strong>Use the Cleaned Bibliography</strong><br>Replace <code>ref.bib</code> with <code>ref_clean.bib</code> in your LaTeX project.</li>
</ol>
<hr>
<p>Lastly executed on Python <code>3.10</code> and bibtexparser <code>4.3</code></p>
