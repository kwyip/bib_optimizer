# Dependency security

The CLI supports Python >=3.8 and retains `bibtexparser>=1.4.3,<2`, locked to
1.4.4 for compatibility with the existing parser API.

Development and build tools use uv dependency groups and require Python >=3.10.
Install them with:

```bash
uv sync --locked --all-groups
```

The dependency constraints and lockfile enforce these minimum tooling versions:

| Package | Minimum version |
| --- | --- |
| urllib3 | 2.8.0 |
| cryptography | 50.0.0 |
| Black | 26.10.1 |
| pytest | 9.0.3 |
| Requests | 2.33.0 |
| Pygments | 2.20.0 |

These tooling dependencies are not added to the CLI's runtime requirements.
The updates address known dependency vulnerabilities; they do not guarantee
that no other vulnerabilities exist.
