"""LAND-TIME RE-CONFIRM tool for the comp-freshness partition-key FIX-TO (23a7be2a1 / b0f0e335a).

CTO banked (151616Z): the fix's land is a THRESHOLD change (~24h stricter -- the date-key runs ~1 day
behind mtime), NOT a no-op, so it is sequenced with "a fresh dry-run at land-time to re-confirm 0 surprise
flips." THIS is that re-confirm tool. Run it immediately BEFORE landing the _max_partition_date fix:
  - 0 verdict flips (old->new) => no cot entry is surprised => safe to land on that axis.
  - any flip => a cot entry crosses a threshold under the fix => STOP, surface to CTO/COO before landing
    (esp. mid the tracked cot freeze; memory: close-nothing-on-cot's-alarm-state).

It compares the CURRENT comp-freshness _max_partition_date (reads the aws-s3-ls LastModified, the anti-
correlated defect) against the PROPOSED fix (reads the object KEY = line.split()[-1]) for the 5 cot
partition-key entries. IN-SCOPE cot READ, INFORMATIONAL only -- compares verdicts, acts on nothing.
Does NOT modify the live .tools/comp-freshness. First run 2026-07-12: 0 of 5 flipped (safe-but-not-urgent).

Author: 3.0.0_SA_CVO~B. Baseline dry-run + the FIX-TO context: the FIX-TO deliverable (this dir).
"""
from __future__ import annotations
import datetime
import importlib.machinery
import importlib.util
import os
import re
from pathlib import Path

REPO = Path(os.environ.get("OPAL_WS", r"C:\Users\AndrewBerman\Desktop\ajb_workspace"))
TOOL = REPO / ".tools" / "comp-freshness"
_ldr = importlib.machinery.SourceFileLoader("cf_reconfirm", str(TOOL))
_spec = importlib.util.spec_from_loader(_ldr.name, _ldr)
cf = importlib.util.module_from_spec(_spec)
_ldr.exec_module(cf)

DATE = re.compile(r"(\d{4}-\d{2}-\d{2})")


def old_max(listing):
    """CURRENT _max_partition_date: DATE.search(WHOLE line) = FIRST date = the LastModified column."""
    best = None
    for line in (listing or "").splitlines():
        m = DATE.search(line)
        if not m:
            continue
        try:
            d = datetime.datetime.strptime(m.group(1), "%Y-%m-%d").date()
        except ValueError:
            continue
        if best is None or d > best:
            best = d
    return best


def new_max(listing):
    """PROPOSED fix: DATE.search(line.split()[-1]) = the OBJECT KEY (basename / PRE subprefix), not mtime."""
    best = None
    for line in (listing or "").splitlines():
        toks = line.split()
        if not toks:
            continue
        m = DATE.search(toks[-1])
        if not m:
            continue
        try:
            d = datetime.datetime.strptime(m.group(1), "%Y-%m-%d").date()
        except ValueError:
            continue
        if best is None or d > best:
            best = d
    return best


def status_for(max_date, warn, fail, sev, now):
    if max_date is None:
        return "UNCHECKED(None)", None
    dt = datetime.datetime(max_date.year, max_date.month, max_date.day, tzinfo=datetime.timezone.utc)
    age_h = (now - dt).total_seconds() / 3600.0
    return cf._status_from_age(age_h, warn, fail, sev), round(age_h, 1)


def main():
    entries = [e for e in cf._load_config(cf.COT_CONFIG)
               if str(e.get("as_of_source", "")).strip() == "silver-partition-key"]
    now = datetime.datetime.now(tz=datetime.timezone.utc)
    print("LAND-TIME RE-CONFIRM -- cot partition-key old(LastModified) vs new(date-key). now=%s"
          % now.isoformat())
    print("=" * 110)
    changed = 0
    for e in entries:
        prefix = e["s3_key_prefix"]
        warn, fail, sev = e.get("warn_age_hours"), e.get("fail_age_hours"), e.get("severity", "ERROR")
        listing = cf._aws("s3", "ls", prefix if prefix.endswith("/") else prefix + "/", check_aws=False)
        om, nm = old_max(listing), new_max(listing)
        os_, oa = status_for(om, warn, fail, sev, now)
        ns_, na = status_for(nm, warn, fail, sev, now)
        flag = "  <== VERDICT CHANGES -- STOP, surface before landing" if os_ != ns_ else ""
        if os_ != ns_:
            changed += 1
        print("%-24s old: %s (%sh, %s) -> new: %s (%sh, %s)%s"
              % (e["artifact_id"], os_, oa, om, ns_, na, nm, flag))
    print("=" * 110)
    print("ENTRIES CHANGING VERDICT (old->new): %d of %d" % (changed, len(entries)))
    if changed == 0:
        print("SAFE TO LAND on the surprise-flip axis (0 flips). Still confirm cot-clarity (07-14 alarm / Andrew word).")
    else:
        print("DO NOT LAND YET -- a cot entry crosses a threshold under the fix. Surface to CTO/COO first.")
    return 0 if changed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
