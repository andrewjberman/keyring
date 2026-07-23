"""comp_keys.py -- KEY / PARTITION ENUMERATION primitive (NFRA_MSBEFF.R5, 2026-07-23, 0.8.0_AE_CloudComp).

Answers WHAT EXISTS, distinct from IS IT FRESH. Closes the single largest measured rail-override demand:
268 aws_freshness rail entries (178 DENY + 90 RUN-OVERRIDE) whose intents were mostly key-discovery,
prefix/content enumeration, and earliest/latest-partition discovery -- NOT freshness questions. Agents were
running raw `aws s3 ls s3://opal-data-*/silver/holdings/` because no comp-tool answered "which keys exist".

WHY A SEPARATE PRIMITIVE, not a `comp-freshness --raw-prefix` mode (shape decision, per the TO): the intent
is categorically different. comp-freshness's whole contract is a trading-day-frontier STALENESS VERDICT
(fresh/FAIL/REFUSE) -- a raw prefix has no freshness basis, so it would return rc2 REFUSE, the wrong
semantics for an inventory answer. comp-keys renders an INVENTORY (a plane-APPLIED enumeration), never a
staleness verdict. One tool, one job (the same one-layer-one-job principle the estate runs on).

THREE CAPABILITIES (drawn from the logged override intents):
  prefix      A. enumerate keys under an ARBITRARY prefix (not only modeled/registered artifacts).
  partitions  B. per-prefix PARTITION-DATE enumeration -- earliest, latest, and GAPS (the backfill-ceiling
                 and depth questions). Partition prefixes are DERIVED from the full key listing, never from
                 `--delimiter /` (which MSYS-mangles under Git Bash to a clean-EMPTY CommonPrefixes, rc=0 --
                 a false 'no partitions'; banked lesson feedback_aws_shim_delimiter_slash_msys_mangle).
  exists      C. per-firm existence across the firm registry (data/firm_registry.json) -- complete-over a
                 DECLARED scope, never a hand-typed firm list.

LAWS (VERIFICATION LAW 11 + Rule 22 denominator):
  - EXPLICIT-Z timestamps only: `s3api list-objects-v2` LastModified is ISO-8601 Z. NEVER parse
    `aws s3 ls` (its LastModified renders in LOCAL time on this UTC-4 host -- a liveness-oracle trap).
  - NEVER a zero without its denominator: every count states 'N of WHAT' (bucket + exact prefix, or the
    firm set). A true-zero on the wrong prefix is the misleading-PASS class; here it renders LOUD.
  - Carries the R1R3 OUTPUT CONTRACT: coverage + plane/vintage header (comp-keys reads a LIVE plane).

Exit contract (declared in comp-output-contracts.yaml): 0 = query ran (N keys OR a LOUD zero, both with
denominator); 1 = tool/input error (bad args, aws unavailable, bucket unreadable/access-denied).
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_WS = _THIS_DIR.parent.parent.parent
if str(_WS) not in sys.path:
    sys.path.insert(0, str(_WS))

try:
    from org.modules.graph import comp_output_contract as _oc
except Exception:  # pragma: no cover
    _oc = None

_FIRM_REGISTRY = _WS / "data" / "firm_registry.json"
# A date partition token: YYYY-MM-DD, YYYYMMDD, or date=YYYY-MM-DD (the common S3 partition shapes).
_DATE_RE = re.compile(r"(?:date=)?(\d{4})-?(\d{2})-?(\d{2})")


def _emit_contract(sub: str) -> None:
    """R1R3 output contract to stderr (stdout stays parseable), like comp-kuzu's provenance header."""
    if _oc is None:
        print("COVERAGE: UNKNOWN (output-contract helper unavailable) | PLANE: applied (live S3)",
              file=sys.stderr)
        return
    print(_oc.coverage_line("comp-keys", sub), file=sys.stderr)
    print(_oc.plane_header("comp-keys", sub), file=sys.stderr)


def _aws_json(args):
    """Run an aws CLI call through the .tools/aws PATH shim, parse JSON stdout. Returns (obj, err).
    err is a string on failure (never a silent None-as-empty). s3api LastModified is ISO-Z."""
    exe = shutil.which("aws") or shutil.which("aws.cmd")
    if not exe:
        return None, "aws CLI not on PATH (.tools/aws shim missing)"
    p = subprocess.run([exe] + args + ["--output", "json"], capture_output=True, text=True)
    if p.returncode != 0:
        return None, (p.stderr.strip() or f"aws exited {p.returncode}")[:400]
    out = p.stdout.strip()
    if not out:
        return {}, None
    try:
        return json.loads(out), None
    except Exception as e:  # noqa: BLE001
        return None, f"unparseable aws JSON: {e}"


def _parse_s3_uri(bucket: str, prefix: str = "") -> tuple[str, str]:
    """Accept either ('s3://bucket/prefix', '') or ('bucket', 'prefix'). Returns (bucket, prefix)."""
    if bucket.startswith("s3://"):
        rest = bucket[5:]
        b, _, p = rest.partition("/")
        return b, (p if not prefix else prefix)
    return bucket, prefix


def _list_keys(bucket: str, prefix: str, cap: int = 5000):
    """List up to `cap` keys under s3://bucket/prefix via s3api (paginated). Returns
    (rows, truncated, err). rows = [{key,size,last_modified(Z)}]. NEVER --delimiter / (MSYS-mangles)."""
    rows = []
    token = None
    truncated = False
    while True:
        args = ["s3api", "list-objects-v2", "--bucket", bucket, "--prefix", prefix,
                "--max-items", str(min(1000, cap - len(rows)))]
        if token:
            args += ["--starting-token", token]
        obj, err = _aws_json(args)
        if err is not None:
            return rows, truncated, err
        for c in (obj.get("Contents") or []):
            rows.append({"key": c.get("Key"), "size": c.get("Size"),
                         "last_modified": c.get("LastModified")})  # already ISO-Z
            if len(rows) >= cap:
                truncated = bool(obj.get("NextToken") or obj.get("Contents"))
                return rows, truncated, None
        token = obj.get("NextToken")
        if not token:
            return rows, truncated, None


def _partition_dates(bucket: str, prefix: str, cap: int = 20000):
    """DERIVE the set of date partitions from the full key listing under prefix (never --delimiter /).
    Returns (sorted_dates, sample_key_by_date, truncated, err)."""
    rows, truncated, err = _list_keys(bucket, prefix, cap=cap)
    if err is not None:
        return [], {}, truncated, err
    dates = {}
    for r in rows:
        key = r["key"] or ""
        tail = key[len(prefix):] if key.startswith(prefix) else key
        m = _DATE_RE.search(tail)
        if m:
            d = f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
            dates.setdefault(d, key)
    return sorted(dates), dates, truncated, None


def _calendar_gaps(dates):
    """Calendar gaps between earliest and latest (weekdays only flagged as suspicious). Returns list of
    missing YYYY-MM-DD (weekday-only, since weekend absence is expected for trading data)."""
    if len(dates) < 2:
        return []
    try:
        lo = date.fromisoformat(dates[0])
        hi = date.fromisoformat(dates[-1])
    except ValueError:
        return []
    present = set(dates)
    gaps = []
    d = lo
    while d <= hi:
        iso = d.isoformat()
        if iso not in present and d.weekday() < 5:  # weekday missing -> candidate gap
            gaps.append(iso)
        d += timedelta(days=1)
    return gaps


def _enabled_pipeline_firms():
    """Firm -> bucket from data/firm_registry.json, enabled + pipeline-scoped. The DECLARED scope for
    complete-over existence checks. Returns (list_of(firm_id,bucket), err)."""
    try:
        reg = json.loads(_FIRM_REGISTRY.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        return [], f"firm_registry.json unreadable: {e}"
    out = []
    for f in (reg.get("firms") or []):
        if not isinstance(f, dict) or not f.get("enabled"):
            continue
        if not (f.get("scopes") or {}).get("pipeline"):
            continue
        b = f.get("bucket")
        if b:
            out.append((f.get("firm_id"), b))
    return out, None


# --------------------------------------------------------------------------------------------------
# subcommands
# --------------------------------------------------------------------------------------------------

def cmd_prefix(args) -> int:
    _emit_contract("prefix")
    bucket, prefix = _parse_s3_uri(args.bucket, args.prefix or "")
    rows, truncated, err = _list_keys(bucket, prefix, cap=args.max)
    if err is not None:
        print(f"ERROR: could not list s3://{bucket}/{prefix} -- {err}", file=sys.stderr)
        return 1
    # NEVER a bare zero: always state the denominator (bucket + exact prefix).
    print(f"KEYS under s3://{bucket}/{prefix}  (denominator: this EXACT prefix on this bucket)")
    if not rows:
        print(f"  0 keys -- LOUD NOT-FOUND: nothing exists under s3://{bucket}/{prefix} "
              f"(a true zero on THIS prefix; check the prefix spelling if you expected keys)")
        return 0
    for r in rows if args.all else rows[:args.top]:
        print(f"  {r['last_modified']}  {str(r['size']):>12}  {r['key']}")
    shown = len(rows) if args.all else min(args.top, len(rows))
    print(f"  -- {len(rows)} key(s){' (CAPPED at %d -- rerun --max higher / narrow the prefix)' % args.max if truncated else ''}; "
          f"showing {shown}")
    return 0


def cmd_partitions(args) -> int:
    _emit_contract("partitions")
    bucket, prefix = _parse_s3_uri(args.bucket, args.prefix or "")
    dates, sample, truncated, err = _partition_dates(bucket, prefix, cap=args.max)
    if err is not None:
        print(f"ERROR: could not enumerate partitions under s3://{bucket}/{prefix} -- {err}", file=sys.stderr)
        return 1
    print(f"PARTITIONS under s3://{bucket}/{prefix}  (denominator: date tokens derived from the full key "
          f"listing, NOT --delimiter)")
    if not dates:
        print(f"  0 date partitions -- LOUD NOT-FOUND under s3://{bucket}/{prefix} "
              f"(no YYYY-MM-DD / YYYYMMDD / date= tokens in any key here)")
        return 0
    gaps = _calendar_gaps(dates)
    print(f"  count:    {len(dates)} partition date(s){' (key-listing CAPPED at %d -- earliest may be incomplete)' % args.max if truncated else ''}")
    print(f"  earliest: {dates[0]}")
    print(f"  latest:   {dates[-1]}")
    print(f"  gaps:     {len(gaps)} weekday date(s) missing between earliest and latest"
          + (f" -> {', '.join(gaps[:15])}{' ...' if len(gaps) > 15 else ''}" if gaps else " (contiguous over weekdays)"))
    return 0


def cmd_exists(args) -> int:
    _emit_contract("exists")
    firms, err = _enabled_pipeline_firms()
    if err is not None:
        print(f"ERROR: {err}", file=sys.stderr)
        return 1
    suffix = args.key_suffix.lstrip("/")
    print(f"EXISTENCE of prefix '{suffix}' across {len(firms)} enabled pipeline firm(s) "
          f"(denominator: data/firm_registry.json, enabled + pipeline-scoped)")
    any_err = False
    for firm_id, bucket in firms:
        rows, _trunc, e = _list_keys(bucket, suffix, cap=1)
        if e is not None:
            print(f"  {firm_id:<16} s3://{bucket}/{suffix}  UNREADABLE ({e})")
            any_err = True
            continue
        print(f"  {firm_id:<16} s3://{bucket}/{suffix}  {'EXISTS' if rows else 'ABSENT'}")
    return 1 if any_err else 0


def main(argv) -> int:
    import argparse
    ap = argparse.ArgumentParser(prog="comp-keys",
                                 description="Enumerate WHAT EXISTS in S3 (keys/partitions/existence) -- distinct from comp-freshness (IS IT FRESH).")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("prefix", help="A: enumerate keys under an arbitrary prefix")
    p.add_argument("bucket", help="bucket or s3://bucket/prefix")
    p.add_argument("prefix", nargs="?", default="", help="key prefix (if bucket given bare)")
    p.add_argument("--top", type=int, default=40, help="show first N (default 40)")
    p.add_argument("--all", action="store_true", help="show every key")
    p.add_argument("--max", type=int, default=5000, help="cap keys listed (disclosed if hit)")
    p.set_defaults(fn=cmd_prefix)

    q = sub.add_parser("partitions", help="B: per-prefix partition-date enumeration (earliest/latest/gaps)")
    q.add_argument("bucket", help="bucket or s3://bucket/prefix")
    q.add_argument("prefix", nargs="?", default="", help="table prefix (if bucket given bare)")
    q.add_argument("--max", type=int, default=20000, help="cap keys scanned for date tokens (disclosed if hit)")
    q.set_defaults(fn=cmd_partitions)

    e = sub.add_parser("exists", help="C: per-firm existence across the firm registry")
    e.add_argument("key_suffix", help="prefix to check on every firm bucket (e.g. silver/holdings/)")
    e.set_defaults(fn=cmd_exists)

    args = ap.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
