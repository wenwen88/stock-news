#!/usr/bin/env python3
"""Generate reports.json — the static index that drives index.html.

Scans repo-root ``stock-report-YYYYMMDD.html`` files, takes the date from the
filename and the one-line summary from ``<meta name="report-summary">``
(falling back to ``<title>`` then a generic label), and writes a
newest-first JSON index. index.html fetches this same-origin file, so the
homepage needs no browser-side GitHub API calls.

Run locally:  python3 .github/scripts/gen_index.py
(No args. Reads/writes relative to the repo root resolved from __file__.)
"""
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # .github/scripts/gen_index.py -> repo root
NAME_RE = re.compile(r"^stock-report-(\d{4})(\d{2})(\d{2})\.html$")
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.IGNORECASE | re.DOTALL)
SUMMARY_RE = re.compile(r'<meta\s+name="report-summary"\s+content="(.*?)"', re.IGNORECASE)
GENERIC = "三面向日報 · 收盤快照"


def extract_summary(path: Path) -> str:
    """Prefer the dedicated report-summary meta, else <title>, else generic."""
    text = path.read_text(encoding="utf-8", errors="replace")
    m = SUMMARY_RE.search(text)
    if m:
        return m.group(1).strip() or GENERIC
    m = TITLE_RE.search(text)
    if m:
        return m.group(1).strip() or GENERIC
    return GENERIC


def main() -> int:
    reports = []
    for p in ROOT.glob("stock-report-*.html"):
        m = NAME_RE.match(p.name)
        if not m:
            continue
        y, mo, d = m.group(1), m.group(2), m.group(3)
        try:
            datetime(int(y), int(mo), int(d))  # reject impossible dates like 1345
        except ValueError:
            print(f"skip {p.name} (invalid date)", file=sys.stderr)
            continue
        reports.append({"date": f"{y}-{mo}-{d}", "file": p.name, "sub": extract_summary(p)})

    reports.sort(key=lambda r: r["date"], reverse=True)
    out = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "count": len(reports),
        "reports": reports,
    }
    target = ROOT / "reports.json"
    target.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {target.name} with {len(reports)} report(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
