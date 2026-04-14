#!/usr/bin/env python3
"""
comp-validate -- check gold artifact output invariants before S3 upload.

Usage:
    comp-validate D_04 --artifact /tmp/leaderboard.json
    comp-validate D_00 --artifact /tmp/timeseries_chart.json
    comp-validate --list                          # show all configured scripts and checks
    comp-validate D_04 --list                     # show checks for one script

Exits 0 if all ERROR-severity checks PASS.
Exits 1 if any ERROR-severity check FAILS.
Exits 0 if only WARN checks fail (prints warnings but does not block).

Config: data/black_diamond/scripts/gold/gold_validate_config.yaml
"""

import argparse
import sys
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_WORKSPACE = _THIS_DIR.parent.parent.parent

sys.path.insert(0, str(_WORKSPACE))

from org.modules.graph.extract_validate import load_validate_config, run_validate


def cmd_list(args):
    configs = load_validate_config(_WORKSPACE)
    if not configs:
        print("No validate config found.")
        print(f"  Expected: data/black_diamond/scripts/gold/gold_validate_config.yaml")
        return

    script_filter = args.script_id or ""

    print(f"VALIDATE CONFIG ({len(configs)} scripts)")
    print(f"  Config: data/black_diamond/scripts/gold/gold_validate_config.yaml")
    print()

    for sid, config in sorted(configs.items()):
        if script_filter and script_filter.upper() not in sid.upper():
            continue

        artifact_str = config.primary_artifact or "(no primary artifact)"
        print(f"  {sid}  ({artifact_str})")

        if config.checks:
            for check in config.checks:
                sev = check.get("severity", "WARN")
                ctype = check.get("type", "?")
                cname = check.get("name", "unnamed")
                print(f"    [{sev}] {cname} (type: {ctype})")
                if check.get("why"):
                    print(f"          {check['why']}")
        else:
            print("    (no checks declared)")
        print()


def cmd_validate(args):
    configs = load_validate_config(_WORKSPACE)

    script_id = args.script_id
    artifact_path = Path(args.artifact)

    print(f"VALIDATE: {script_id}")
    print(f"  Artifact: {artifact_path}")
    print()

    results = run_validate(script_id, artifact_path, configs)

    error_count = 0
    warn_count = 0
    pass_count = 0
    skip_count = 0

    for r in results:
        if r.status == "PASS":
            pass_count += 1
            print(f"  PASS  [{r.severity}] {r.name}")
            print(f"         {r.message}")
        elif r.status == "FAIL":
            if r.severity == "ERROR":
                error_count += 1
                print(f"  FAIL  [{r.severity}] {r.name}")
            else:
                warn_count += 1
                print(f"  WARN  [{r.severity}] {r.name}")
            print(f"         {r.message}")
            if r.detail:
                print(f"         Why: {r.detail}")
        elif r.status == "SKIP":
            skip_count += 1
            print(f"  SKIP  [{r.severity}] {r.name}: {r.message}")
        elif r.status == "ERROR":
            error_count += 1
            print(f"  ERROR [{r.severity}] {r.name}: {r.message}")
        print()

    print(f"  Summary: {pass_count} PASS, {error_count} ERROR, {warn_count} WARN, {skip_count} SKIP")

    if error_count > 0:
        print()
        print(f"  BLOCKED: {error_count} ERROR check(s) failed. Do not upload artifact to S3.")
        sys.exit(1)
    elif warn_count > 0:
        print()
        print(f"  ADVISORY: {warn_count} WARN check(s) failed. Review before uploading.")
    else:
        print()
        print("  All checks passed. Artifact is ready for S3 upload.")


def main():
    parser = argparse.ArgumentParser(
        prog='comp-validate',
        description='Validate gold artifact output invariants before S3 upload.',
    )
    parser.add_argument('script_id', nargs='?', default='',
                        help='Script ID (e.g., D_04, D_00, build_canonical_prices_v2)')
    parser.add_argument('--artifact', default='',
                        help='Path to local artifact file (.json or .parquet)')
    parser.add_argument('--list', action='store_true', dest='list_only',
                        help='List all configured checks and exit')

    args = parser.parse_args()

    if args.list_only or not args.artifact:
        cmd_list(args)
        return

    if not args.script_id:
        parser.print_help()
        sys.exit(1)

    cmd_validate(args)


if __name__ == '__main__':
    main()
