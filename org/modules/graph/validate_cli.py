#!/usr/bin/env python3
"""
comp-validate -- check gold artifact output invariants before S3 upload.

Usage:
    comp-validate D_04 --artifact /tmp/leaderboard.json
    comp-validate D_00 --artifact /tmp/timeseries_chart.json
    comp-validate --list                          # show all configured scripts and checks
    comp-validate D_04 --list                     # show checks for one script
    comp-validate nna_atomic --schema             # pass-through to standalone validator
    comp-validate role_aua --artifact /tmp/...    # standalone validator with args

Exits 0 if all ERROR-severity checks PASS.
Exits 1 if any ERROR-severity check FAILS.
Exits 0 if only WARN checks fail (prints warnings but does not block).

Config: data/black_diamond/scripts/gold/gold_validate_config.yaml

Standalone validators: data/black_diamond/scripts/validators/validate_{script_id}.py
When extra flags (e.g. --schema, --certified, --cross-check) are present OR the
script_id has no config entry, the CLI dispatches to the standalone validator
via sys.executable with all trailing flags preserved (ADVI_ROLLUP ADHC_ROUTER.T4,
closes proposal E pass-through gap from COMPILER_VALIDATE_COVERAGE_AND_PASSTHROUGH.md).
"""

from __future__ import annotations

import argparse
import platform
import subprocess
import sys
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_WORKSPACE = _THIS_DIR.parent.parent.parent

sys.path.insert(0, str(_WORKSPACE))

from org.modules.graph.extract_validate import load_validate_config, run_validate  # noqa: E402

STANDALONE_VALIDATORS_DIR = _WORKSPACE / "data" / "black_diamond" / "scripts" / "validators"


def _translate_artifact_path(raw: str) -> Path:
    """On Windows, translate POSIX /tmp/ and /c/ paths to native Windows paths.

    Linux/macOS: paths pass through unchanged.
    Windows (platform.system() == 'Windows', mocked via sitecustomize.py per
    MEMORY.md "AWS CLI Hang Fixes Fix 2"):
      /tmp/foo.json              -> C:/tmp/foo.json
      /c/Users/AndrewBerman/...  -> C:/Users/AndrewBerman/...
    Any other path is returned as-is.

    Caller is responsible for checking existence and emitting the dual-path
    error message when neither original nor translated path exists.
    """
    if platform.system() != 'Windows':
        return Path(raw)
    if raw.startswith('/tmp/'):
        return Path('C:/tmp/' + raw[5:])
    if raw.startswith('/c/'):
        return Path('C:/' + raw[3:])
    return Path(raw)


def _find_standalone_validator(script_id: str) -> Path | None:
    """Return path to data/.../validators/validate_{script_id}.py if it exists."""
    if not script_id:
        return None
    candidate = STANDALONE_VALIDATORS_DIR / f"validate_{script_id}.py"
    return candidate if candidate.is_file() else None


def _dispatch_standalone(validator_path: Path, passthrough_args: list[str]) -> int:
    """Invoke a standalone validator via sys.executable, forwarding all args verbatim.

    Preserves the validator's exit code and stderr so pass-through is transparent.
    """
    print(f"COMP-VALIDATE: dispatching to standalone validator {validator_path.name}")
    print(f"  args: {passthrough_args}")
    print()
    completed = subprocess.run(
        [sys.executable, str(validator_path), *passthrough_args],
        cwd=str(_WORKSPACE),
    )
    return completed.returncode


def cmd_list(args):
    configs = load_validate_config(_WORKSPACE)
    if not configs:
        print("No validate config found.")
        print("  Expected: data/black_diamond/scripts/gold/gold_validate_config.yaml")
        return

    script_filter = args.script_id or ""

    print(f"VALIDATE CONFIG ({len(configs)} scripts)")
    print("  Config: data/black_diamond/scripts/gold/gold_validate_config.yaml")
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
    artifact_path = _translate_artifact_path(args.artifact)

    # On Windows, when neither the original nor translated path exists, show both
    if not artifact_path.exists():
        translated_str = str(artifact_path)
        if platform.system() == 'Windows' and args.artifact != translated_str:
            print("Artifact not found:", file=sys.stderr)
            print(f"  Input path:      {args.artifact}", file=sys.stderr)
            print(f"  Translated path: {translated_str}", file=sys.stderr)
        else:
            print(f"Artifact not found: {artifact_path}", file=sys.stderr)
        sys.exit(1)

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

    # Use parse_known_args() so unknown flags (e.g. --schema, --certified,
    # --cross-check) become pass-through args for the standalone validator
    # instead of hard-erroring in argparse (proposal E).
    args, extras = parser.parse_known_args()

    # List path is unchanged.
    if args.list_only:
        cmd_list(args)
        return

    # Pass-through dispatch: if extras are present OR no --artifact is given
    # (which the config engine requires), try routing to the standalone
    # validator at data/black_diamond/scripts/validators/validate_{id}.py.
    if extras or not args.artifact:
        standalone = _find_standalone_validator(args.script_id)
        if standalone is not None:
            # Reconstruct full arg list for the standalone script: if --artifact
            # was parsed by us, translate path and forward it back; ditto extras.
            forward: list[str] = []
            if args.artifact:
                forward.extend(['--artifact', str(_translate_artifact_path(args.artifact))])
            forward.extend(extras)
            sys.exit(_dispatch_standalone(standalone, forward))

        # No standalone validator + no artifact = show config list (existing
        # behavior for bare `comp-validate` or `comp-validate <id>`).
        if not args.artifact and not extras:
            cmd_list(args)
            return

        # Extras supplied but no route for them: surface clearly rather than
        # silently dropping flags.
        print(
            f"comp-validate: unrecognized arguments {extras} and no standalone "
            f"validator found for '{args.script_id}' at "
            f"{STANDALONE_VALIDATORS_DIR.relative_to(_WORKSPACE)}/"
            f"validate_{args.script_id}.py",
            file=sys.stderr,
        )
        sys.exit(2)

    if not args.script_id:
        parser.print_help()
        sys.exit(1)

    cmd_validate(args)


if __name__ == '__main__':
    main()
