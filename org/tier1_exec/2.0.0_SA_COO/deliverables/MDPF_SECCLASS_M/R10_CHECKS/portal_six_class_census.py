#!/usr/bin/env python3
"""MDPF_SECCLASS round 8, cell SC-e-23 (criterion SC8-e23-AC1): no portal source carries multi_asset as a security class.

READ-ONLY. Walks <portal>/src (default: the portal checkout beside this repo's root, i.e. <worktree>/portal) over
.ts/.tsx/.js/.jsx files and counts the files that carry a security-class spelling of the retired seventh class:
`multi_asset`, `multiAsset`, `MultiAsset` or the label `'Multi-Asset'` / `"Multi-Asset"`.

EXCLUDED, by path, because there the words name a MARKET VIEW, not a security class (measured at portal DEV
8ddfe40994, 2026-10-07): everything under src/pages/MarketPerformance/ (the Multi-Asset tab) and
src/components/market-performance/MarketRegimeIndicator.tsx ("Multi-Asset Momentum"). The excluded files are counted
and printed, so the exclusion is visible, never silent.

Prints one line:
  PORTAL-SIX-CLASS ok=<bool> scanned=<n> excluded=<n> files=<n>
ok=True only when files == 0 and scanned > 0 (an empty walk is a wrong path, never a pass).
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
PATTERN = re.compile(r"multi_asset|multiAsset|MultiAsset|['\"]Multi-Asset['\"]")
EXCLUDE_PREFIXES = ("src/pages/MarketPerformance/",)
EXCLUDE_FILES = {"src/components/market-performance/MarketRegimeIndicator.tsx"}
EXTS = {".ts", ".tsx", ".js", ".jsx"}


def main(argv):
    portal = Path(argv[1]).resolve() if len(argv) > 1 else ROOT / "portal"
    src = portal / "src"
    scanned, excluded, hits = 0, [], []
    for path in sorted(src.rglob("*")):
        if path.suffix not in EXTS or not path.is_file() or "node_modules" in path.parts:
            continue
        rel = path.relative_to(portal).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        if rel.startswith(EXCLUDE_PREFIXES) or rel in EXCLUDE_FILES:
            if PATTERN.search(text):
                excluded.append(rel)
            continue
        scanned += 1
        n = len(PATTERN.findall(text))
        if n:
            hits.append((rel, n))
    for rel in excluded:
        print(f"EXCLUDED {rel} (market view, not a security class)")
    for rel, n in hits:
        print(f"HIT {rel} occurrences={n}")
    ok = scanned > 0 and not hits
    print(f"PORTAL-SIX-CLASS ok={ok} portal={portal.as_posix()} scanned={scanned} excluded={len(excluded)} "
          f"files={len(hits)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
