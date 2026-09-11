# Enproof

Public site for [www.enproof.com](https://www.enproof.com), hosted on GitHub
Pages from [Enproof/enproof-site](https://github.com/Enproof/enproof-site).

Public contact: [support@enproof.com](mailto:support@enproof.com).

## Local preview

From the repository root:

```powershell
python -m http.server 8080
```

Then open `http://localhost:8080`.

## Publishing

GitHub Pages deploys the root of `main`. The `CNAME` file sets
`www.enproof.com` as the canonical custom domain. GitHub redirects
`enproof.com` to `www.enproof.com` when the DNS records below are in place.

Local clone:

```powershell
git remote set-url origin https://github.com/Enproof/enproof-site.git
```

## DNS (GoDaddy)

These records are the live website setup. Do not restore Website Builder
records.

| Type | Name | Value |
| --- | --- | --- |
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | `enproof.github.io` |
| TXT | `_github-pages-challenge-enproof` | `3ac5a631164fabcfd6657282d2a828` |

On GoDaddy, the TXT **Name** is only `_github-pages-challenge-enproof`.
Do not add `.enproof.com`; GoDaddy appends the zone automatically.

Leave `_domainconnect` and all Google Workspace MX, SPF, DKIM, and DMARC
records unchanged.

There must be only one `www` CNAME. Do not keep `www → enproof.com`.

## HTTPS

The repo Pages settings at
[Enproof/enproof-site Pages](https://github.com/Enproof/enproof-site/settings/pages)
should show:

- Custom domain: `www.enproof.com`
- DNS check successful
- **Enforce HTTPS** enabled

Certificate issuance can take up to 24 hours after DNS first points at
GitHub.

## Domain verification (org, not the repo)

Owning the domain at GoDaddy is not the same as locking it on GitHub
Pages. GitHub Pages uses shared IPs. Verification tells GitHub that only
the Enproof org may serve `enproof.com` / `www.enproof.com`.

This is **not** the repository Pages page. Use the organization page:

1. Open [Enproof org Pages](https://github.com/organizations/Enproof/settings/pages)
2. **Add a domain** → `enproof.com` (apex, not `www`)
3. Add the TXT record GitHub shows (see the DNS table above)
4. Click **Verify**
5. Keep that TXT record permanently

## GoDaddy products

Keep the **enproof.com** domain subscription. That is the domain, not the
old website.

The old builder is **Websites + Marketing Free**
(`enproof.godaddysites.com`). That product can be deleted. Do not delete
the `enproof.com` domain row (renews separately).

`padel-up.net` is a different domain and is unrelated to this site.

## Privacy

This site uses no cookies, analytics, external fonts, forms, or client-side
JavaScript. The private `docs/` directory is excluded from Git.
