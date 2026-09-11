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

Leave `_domainconnect` and all Google Workspace MX, SPF, DKIM, and DMARC
records unchanged.

There must be only one `www` CNAME. Do not keep `www → enproof.com`.

## HTTPS

After DNS points at GitHub, Pages issues a Let's Encrypt certificate. That
can take from a few minutes up to 24 hours. Until it succeeds, browsers may
warn on `https://www.enproof.com`.

When GitHub shows a valid certificate:

1. Open [Pages settings](https://github.com/Enproof/enproof-site/settings/pages)
2. Confirm Custom domain is `www.enproof.com`
3. Enable **Enforce HTTPS**
4. Under the Enproof org, **Settings → Pages → Add a domain**, verify
   `enproof.com` so another GitHub user cannot claim it

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
