# Website Scripts

Helpers for the Enproof static site. No Node.js is required.

## preview.cmd

Double-click `scripts\preview.cmd` (or run from the repo root). It starts
`python -m http.server 8080` and opens `http://localhost:8080`.

## Version bumping

The **single source of truth** is the `VERSION` file in the repository root.
That value is copied into `.site-version` on the pages and into `styles.css?v=`.

From the repo root:

```powershell
python scripts/bump-version.py --current
python scripts/bump-version.py patch
python scripts/bump-version.py minor
python scripts/bump-version.py major
python scripts/bump-version.py 1.2.0
python scripts/bump-version.py patch --commit
```

Or double-click the files in `scripts\site-version\`:

- `get-current-version.bat`
- `increment-current-version - patch.bat`
- `increment-current-version - minor.bat`
- `increment-current-version - major.bat`
- `increment-current-version - patch+commit.bat`

`--commit` also creates an annotated git tag `site-vX.Y.Z`.
