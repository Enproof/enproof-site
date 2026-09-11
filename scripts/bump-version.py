#!/usr/bin/env python3
"""Enproof website version bumper.

Single source of truth: VERSION in the repository root.
The same value is written into page footers and CSS cache-buster query strings.

Usage:
  python scripts/bump-version.py --current
  python scripts/bump-version.py patch
  python scripts/bump-version.py minor
  python scripts/bump-version.py major
  python scripts/bump-version.py 1.2.0
  python scripts/bump-version.py patch --commit
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERSION_PATH = ROOT / "VERSION"
HTML_FILES = [ROOT / "index.html", ROOT / "404.html"]
TRACKED_FILES = ["VERSION", "index.html", "404.html"]


def read_version() -> str:
    if not VERSION_PATH.exists():
        raise SystemExit("Could not find VERSION in the repository root")
    value = VERSION_PATH.read_text(encoding="utf-8").strip()
    if not value:
        raise SystemExit("VERSION file is empty")
    return value


def parse_semver(value: str) -> list[int]:
    cleaned = value.lstrip("v").strip()
    parts = [int(p) if p.isdigit() else 0 for p in cleaned.split(".")]
    while len(parts) < 3:
        parts.append(0)
    return parts[:3]


def format_semver(parts: list[int]) -> str:
    return ".".join(str(p) for p in parts)


def bump(current: str, spec: str) -> str:
    if spec in {"major", "minor", "patch"}:
        parts = parse_semver(current)
        if spec == "major":
            parts = [parts[0] + 1, 0, 0]
        elif spec == "minor":
            parts = [parts[0], parts[1] + 1, 0]
        else:
            parts = [parts[0], parts[1], parts[2] + 1]
        return format_semver(parts)
    return format_semver(parse_semver(spec))


def update_files(new_version: str) -> None:
    VERSION_PATH.write_text(f"{new_version}\n", encoding="utf-8")
    version_re = re.compile(r'(<span class="site-version">)v?[^<]*(</span>)')
    css_re = re.compile(r'(href="/styles\.css)(?:\?v=[^"]*)?(")')
    for path in HTML_FILES:
        src = path.read_text(encoding="utf-8")
        if not version_re.search(src):
            raise SystemExit(f"Could not find .site-version in {path.name}")
        src = version_re.sub(rf"\1v{new_version}\2", src)
        src = css_re.sub(rf"\1?v={new_version}\2", src)
        path.write_text(src, encoding="utf-8")


def run_git(new_version: str) -> None:
    status = subprocess.check_output(
        ["git", "status", "--porcelain", *TRACKED_FILES],
        cwd=ROOT,
        text=True,
    ).strip()
    if not status:
        print("\nNo changes to commit.")
        return
    print("\nStaging changes...")
    subprocess.check_call(["git", "add", *TRACKED_FILES], cwd=ROOT)
    subprocess.check_call(
        ["git", "commit", "-m", f"chore(site): bump version to {new_version}"],
        cwd=ROOT,
    )
    tag = f"site-v{new_version}"
    subprocess.check_call(
        ["git", "tag", "-a", tag, "-m", f"Site version {new_version}"],
        cwd=ROOT,
    )
    print(f"\nCommitted and created tag {tag}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Bump the Enproof site version")
    parser.add_argument(
        "spec",
        nargs="?",
        help="patch, minor, major, or an explicit X.Y.Z version",
    )
    parser.add_argument("--current", action="store_true", help="print the current version")
    parser.add_argument("--commit", "--tag", action="store_true", help="commit and tag the bump")
    args = parser.parse_args()

    if args.current or not args.spec:
        current = read_version()
        if args.current:
            print(current)
            return 0
        print(f"Current version: {current}")
        print("\nUsage:")
        print("  python scripts/bump-version.py patch")
        print("  python scripts/bump-version.py minor")
        print("  python scripts/bump-version.py major")
        print("  python scripts/bump-version.py 1.2.0")
        print("  python scripts/bump-version.py --current")
        print("  python scripts/bump-version.py patch --commit")
        return 0

    current = read_version()
    new_version = bump(current, args.spec)
    print(f"Current: {current}")
    print(f"New:     {new_version}")
    if new_version == current:
        print("Version unchanged.")
        return 0

    update_files(new_version)
    print(f"\nUpdated VERSION and page footers/assets to {new_version}")
    if args.commit:
        run_git(new_version)
    else:
        print("\nNext steps (optional):")
        print("  git add VERSION index.html 404.html")
        print(f'  git commit -m "chore(site): bump version to {new_version}"')
        print(f'  git tag -a site-v{new_version} -m "Site version {new_version}"')
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.CalledProcessError as exc:
        print("\nGit operation failed:", file=sys.stderr)
        raise SystemExit(exc.returncode)
