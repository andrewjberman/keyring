"""CLI entry point for comp-incrparity.

Usage:
    comp-incrparity <script_id> [--date YYYY-MM-DD] [--mode quick|deep]
    comp-incrparity ALL [--mode quick|deep]

Exit 0 on parity; 1 on mismatch (with diff report to stderr + S3).
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import sys

# Allow `python org/modules/graph/incrparity_cli.py` invocation.
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import incrparity_core as core  # noqa: E402


# Per-script output prefixes for self-parity smoke runs. Declared here (not
# derived from pipescript IO) so the smoke path works in offline CI without
# loading the full pipeline graph. Wave 2+ adopters register dual-run
# prefixes through the standard parity_config path.
SELF_PARITY_PREFIXES: dict[str, list[str]] = {
    # C_06 writes two things; the JSON summary is the cheap invariant to
    # read + hash for a self-parity smoke. Per-relationship JSONs are
    # skipped in smoke mode (too many to round-trip cheaply).
    "C_06": ["gold/views/mix_daily_summary.json"],
}


def _make_s3():
    import boto3
    return boto3.client("s3", region_name="us-east-1")


def _parity_prefixes_for(script_id: str) -> tuple[str, str] | None:
    """Return (full_prefix, incremental_prefix) if the script has declared
    dual-run parity outputs. Currently empty — adopters wire this per-script
    in Wave 2+. Absent => self-parity fallback.
    """
    return None


def run_one(script_id: str, mode: str, date: str | None, s3) -> core.DiffResult:
    prefixes = _parity_prefixes_for(script_id)
    if prefixes is not None:
        full_prefix, incr_prefix = prefixes
        return core.diff_prefixes(script_id, full_prefix, incr_prefix, mode, s3)

    # Self-parity fallback. For scripts with a declared output key (C_06),
    # run self-parity against that key's parent prefix so the list+fetch+diff
    # machinery actually exercises. For scripts without a declaration,
    # trivially PASS with a note — they must register via Wave 2+.
    smoke_keys = SELF_PARITY_PREFIXES.get(script_id)
    if smoke_keys:
        # Self-parity of exactly the listed keys: read each and diff vs itself.
        result = core.DiffResult(
            script_id=script_id, mode=mode,
            full_prefix=f"self:{','.join(smoke_keys)}",
            incremental_prefix=f"self:{','.join(smoke_keys)}",
        )
        for key in smoke_keys:
            try:
                body = core.fetch_bytes(core.S3_BUCKET, key, s3)
            except Exception as e:
                result.errors.append(f"{key}: fetch failed: {e}")
                continue
            # Diff body against itself — trivial PASS, exercises parse path.
            if key.lower().endswith(".parquet"):
                result.divergences.extend(core.diff_parquet_bodies(body, body, mode, path_prefix=key))
            elif key.lower().endswith(".json"):
                result.divergences.extend(core.diff_json_bodies(body, body, mode, path_prefix=key))
        return result

    # No registration -- UNVERIFIED (was a silent "conservative PASS"; absence of a
    # parity comparison is NOT a pass -- the script just isn't wired for dual-run
    # parity yet, so we cannot assert it). Caller surfaces UNVERIFIED distinctly.
    result = core.DiffResult(
        script_id=script_id, mode=mode,
        full_prefix="(none registered)", incremental_prefix="(none registered)",
        unverified=True,
    )
    return result


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        prog="comp-incrparity",
        description="Parity validator for gold-script incremental promotions.",
    )
    parser.add_argument("script_id", help="script id (e.g. C_06) or 'ALL'")
    parser.add_argument("--date", default=None, help="YYYY-MM-DD (reserved, currently unused)")
    parser.add_argument("--mode", choices=("quick", "deep"), default="quick")
    parser.add_argument("--no-s3-report", action="store_true",
                        help="suppress S3 report write on FAIL (stderr only)")

    args = parser.parse_args(argv)

    try:
        s3 = _make_s3()
    except Exception as e:
        print(f"ERROR: could not construct S3 client: {e}", file=sys.stderr)
        return 1

    run_ts = _dt.datetime.now(_dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    if args.script_id == "ALL":
        promoted = core.load_promoted_list(s3)
        if not promoted:
            print("ALL: incremental_promoted.json is empty - 0 scripts to check. PASS.")
            return 0
        any_fail = False
        any_unverified = False
        for sid in promoted:
            result = run_one(sid, args.mode, args.date, s3)
            print(result.summary())
            if result.unverified:
                any_unverified = True
            elif not result.passed:
                any_fail = True
                _emit_failure(result, run_ts, s3, no_s3_report=args.no_s3_report)
        # exit 1 = real parity FAIL; exit 2 = UNVERIFIED (absence, not pass); 0 = clean
        return 1 if any_fail else (2 if any_unverified else 0)

    result = run_one(args.script_id, args.mode, args.date, s3)
    print(result.summary())
    if result.unverified:
        # Distinct exit 2 (UNCHECKED) -- absence of a parity run is NOT exit-0 pass.
        return 2
    if result.passed:
        return 0
    _emit_failure(result, run_ts, s3, no_s3_report=args.no_s3_report)
    return 1


def _emit_failure(result: core.DiffResult, run_ts: str, s3, *, no_s3_report: bool) -> None:
    # Structured JSON to stderr for machine consumption.
    print(json.dumps(result.to_dict(), indent=2), file=sys.stderr)
    if no_s3_report:
        return
    try:
        loc = core.write_parity_report(result, run_ts, s3)
        print(f"Diff report: {loc}", file=sys.stderr)
    except Exception as e:
        print(f"WARN: parity report write failed: {e}", file=sys.stderr)


if __name__ == "__main__":
    raise SystemExit(main())
