# Enproof

Minimal public website for [enproof.com](https://enproof.com), hosted with
GitHub Pages.

## Local preview

From the repository root, run:

```powershell
python -m http.server 8080
```

Then open `http://localhost:8080`.

## Publishing

GitHub Pages publishes the root of the `main` branch. The `CNAME` file sets
`enproof.com` as the custom domain.

## DNS

In GoDaddy, configure these website records:

| Type | Name | Value |
| --- | --- | --- |
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | `boris-j-goldberg.github.io` |

Do not modify the domain's Google Workspace MX, SPF, DKIM, or DMARC records.

After DNS propagation, confirm the custom domain in **Repository settings →
Pages**, then enable **Enforce HTTPS**.

## Privacy

This site uses no cookies, analytics, external fonts, forms, or client-side
JavaScript. The private `docs/` directory is intentionally excluded from Git.
