from pathlib import Path
import subprocess
import sys

import bibtexparser
import pytest


def run_cli(cwd, tex, bib, output):
    subprocess.run(
        [sys.executable, "-m", "bib_optimizer", str(tex), str(bib), str(output)],
        cwd=cwd,
        check=True,
        capture_output=True,
        text=True,
    )
    with output.open(encoding="utf-8") as stream:
        return bibtexparser.load(stream).entries


def test_sample_cli_preserves_inputs_and_citation_order(tmp_path):
    samples = Path(__file__).parent
    tex = samples / "sample_main.tex"
    bib = samples / "sample_ref.bib"
    originals = (tex.read_bytes(), bib.read_bytes())
    entries = run_cli(samples, tex, bib, tmp_path / "optimized.bib")
    assert [entry["ID"] for entry in entries] == ["firstref", "secondref", "thirdref"]
    assert (tex.read_bytes(), bib.read_bytes()) == originals


@pytest.mark.parametrize("command", ["input", "include"])
def test_cli_includes_child_citations_and_skips_missing_files(tmp_path, command):
    tex = tmp_path / "main.tex"
    bib = tmp_path / "refs.bib"
    tex.write_text(
        "\\cite{first}\n\\" + command + "{child}\n\\cite{last}\n" "\\input{missing}\n",
        encoding="utf-8",
    )
    (tmp_path / "child.tex").write_text("\\cite{child,first}\n", encoding="utf-8")
    bib.write_text(
        "\n".join(
            "@article{" + key + ", title={Café}}"
            for key in ["unused", "last", "child", "first"]
        ),
        encoding="utf-8",
    )
    entries = run_cli(tmp_path, tex, bib, tmp_path / "optimized.bib")
    assert [entry["ID"] for entry in entries] == ["first", "child", "last"]
    assert all(entry["title"] == "Café" for entry in entries)
