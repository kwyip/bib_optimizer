---
name: bib-optimizer
description: "Reproduce bibopt directly from attached LaTeX and BibTeX files: discover citations in document order across input/include files, remove unused bibliography entries, preserve citation order, and emit a normalized optimized .bib file. Use when asked to clean, trim, reorder, or optimize a BibTeX bibliography without running Python, bibopt, scripts, an MCP server, or installing packages."
---

# Optimize BibTeX directly

Transform the attached `.tex` and `.bib` text yourself. Do not run or generate Python, shell scripts, `bibopt`, a BibTeX parser, an MCP tool, or package-install commands. Never modify either input.

Create exactly the requested output `.bib`; if no output name is given, use `<source-stem>_opt.bib`.

## Contract

Given one root TeX file and one source bibliography, output only bibliography entries selected by citations, in first-citation order.

Match citation keys case-sensitively. Preserve selected entries' semantic content while normalizing presentation as specified below.

Before writing, identify the root TeX file, source `.bib`, and output path. If either input is missing or unreadable, stop and state which one. Never infer missing bibliographic records from titles, DOIs, or the internet.

## 1. Discover citation keys

Scan the root TeX file from beginning to end, recursively expanding included files at the position of each include command.

1. Ignore a physical line only when its first non-whitespace character is `%`. Do **not** strip inline `%` comments; text later on that line remains scanable.
2. Recognize only these exact, case-sensitive forms, with no whitespace or optional argument before `{`:
   - `\cite{...}`
   - `\citet{...}`
   - `\citep{...}`
3. Split each recognized citation body on every comma, trim surrounding whitespace, and process keys left-to-right. Keep each key only on its first global occurrence.
4. Do not recognize `\Cite`, `\cite*`, `\citeauthor`, `\parencite`, `\autocite`, `\nocite`, commands with optional arguments, or commands with whitespace before `{`.
5. `*` has no wildcard meaning; in a recognized citation it is the literal key `*`.
6. Recognize `\input` and `\include` in:
   - braced form: `\input{chapters/a}`
   - unbraced form ending at whitespace/newline: `\include chapters/a`
7. Append `.tex` unless the captured include name already contains the case-sensitive substring `.tex`.
8. Resolve relative includes first beside the containing file, then beside the root file.
9. Scan a found include recursively at that exact point, then resume the containing file.
10. Skip missing or unreadable includes and record a warning.
11. Prevent recursion cycles using the active include stack. Skip a file already on that stack and record a warning.
12. Do not globally suppress previously included files: rescan each non-cyclic inclusion. Citation-key deduplication remains global.

Apply these rules textually, including inside environments or macro definitions. Citation bodies may span lines and end at the first `}`.

## 2. Parse the source bibliography

Read the complete `.bib` before selecting entries.

Recognize entries of the form `@TYPE{KEY, ...}` or `@TYPE(KEY, ...)`, balancing nested braces and respecting quoted strings so that braces, commas, `@`, or `=` inside values do not prematurely end entries or fields.

Apply these rules:

- Normalize entry types and field names to lowercase.
- Preserve citation-key spelling exactly.
- Accept braced, quoted, numeric, and bare-identifier values.
- Remove only the outer value delimiter; preserve intentional inner braces and TeX escapes.
- Resolve `#` concatenation left-to-right.
- Expand bare user `@string` identifiers.
- Expand bare standard month identifiers `jan` through `dec` to `January` through `December`.
- Keep braced or quoted text literal; e.g. `{dec}` remains `dec`.
- Treat an undefined bare string as a parse/validation error; do not invent text.
- Exclude `@comment`, `@preamble`, and `@string` declarations from output, though expanded `@string` text may appear in selected values.
- If the same case-sensitive key appears more than once, the last parsed definition wins, even if its type differs.
- Do not merge duplicate definitions.
- Silently omit cited keys absent from the bibliography; do not create placeholders.
- Select only entries whose keys appear in the ordered citation-key list.

### Entry dependencies

Treat `crossref`, `xref`, `xdata`, `related`, and similarly named fields as ordinary fields.

Do not automatically include referenced entries, follow aliases, sets, or inheritance, or copy fields from parent entries. A referenced entry is included only if its own key was cited.

`@string` is a textual value dependency and must be expanded before declarations are discarded; cross-references are entry dependencies and must not alter selection.

## 3. Emit deterministic BibTeX

Walk the ordered citation-key list and emit the winning bibliography entry for each key that exists.

Use this shape:

```
@article{key,
    author = {Value},
    title = {Value}
}

@book{next,
    title = {Next value}
}
```

Rules:

- Preserve first-citation entry order; never alphabetize entries.
- Start each entry with `@`, lowercase type, `{`, and the preserved key.
- Sort fields by lowercase field name in ascending lexical order.
- Put each field on its own line with four spaces:
  `field = {Value}`
- Enclose each fully resolved value in one new pair of braces.
- Preserve braces already belonging to the value. For example, input `{{Protected Title}}` emits `title = {{Protected Title}}` after removing only the outer input delimiter.
- Add a comma after every field except the last.
- Put no trailing comma before the closing brace.
- End each entry with `}` and a newline.
- Put exactly one empty line between entries.
- Put no leading blank line.
- Preserve Unicode, TeX commands, escapes, capitalization, and meaningful internal whitespace.
- Do not rewrite names, dates, URLs, page ranges, or LaTeX.
- If zero selected cited entries exist in the source, create an empty output file.
- Overwrite the requested output if it already exists.
- Leave the root TeX, included TeX files, and source bibliography byte-for-byte unchanged.

## 4. Validate

Before delivery, verify:

1. Recomputed first-seen citation order matches output entry order for all cited keys present in the source.
2. Every output entry comes from the source and every selected source entry is present.
3. Missing cited keys are allowed.
4. Duplicate citations produce one entry.
5. Duplicate source definitions use the last parsed definition.
6. All `@string` expressions are resolved.
7. Cross-referenced entries were not added unless independently cited.
8. Braces and quotes are balanced.
9. Entry types and field names are lowercase.
10. Fields are lexically sorted.
11. Fields use four-space indentation and correct comma placement.
12. Entries have exactly one blank line between them.
13. UTF-8 text is preserved.
14. A non-empty output ends with a newline.
15. Inputs were not modified and only the requested output was created.

If status text is allowed, report the output path and any skipped includes, cycles, undefined strings, or missing citation keys succinctly.

If the user asks for only the artifact or file contents, return only the completed `.bib`.
