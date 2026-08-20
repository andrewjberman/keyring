#!/usr/bin/env python3
"""Emit one PRD sec.2.1 Observation_Record from a supported precursor."""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PACKAGE_ROOT.parents[4]
sys.path.insert(0, str(PACKAGE_ROOT / "src"))

from observation_envelope import (  # noqa: E402
    canonical_bytes,
    validate_record,
    wrap_census_substrate,
    wrap_comp_estate,
    wrap_comp_find,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--observed-at", default=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))
    sub = parser.add_subparsers(dest="instrument", required=True)
    find = sub.add_parser("comp-find")
    find.add_argument("pattern")
    find.add_argument("pathspec", nargs="*")
    estate = sub.add_parser("comp-estate")
    estate.add_argument("argv", nargs=argparse.REMAINDER)
    census = sub.add_parser("census-substrate")
    census.add_argument("descriptor")
    args = parser.parse_args()

    if args.instrument == "comp-find":
        record = wrap_comp_find(REPO_ROOT, args.pattern, args.pathspec, args.observed_at)
    elif args.instrument == "comp-estate":
        record = wrap_comp_estate(REPO_ROOT, args.argv or ["--list"], args.observed_at)
    else:
        record = wrap_census_substrate(REPO_ROOT, args.descriptor, args.observed_at)

    errors = validate_record(record)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    sys.stdout.buffer.write(canonical_bytes(record))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
