"""IB-pr-221 candidate, read-only: the candidate adapter bundle's own holdings reader for ONE Inflection account, beside a chain
computed independently from the gold rows.

Usage: python adapter_candidate_inflection_read.py <aws.cmd> <bundle dir> <raw account id> <end date> [year|since|all]

Runs the bundle's `holdings_gold.calculate` (S3 list and get on the Inflection gold; no persistence, no vendor call, no served
function touched) through `installed._holdings_sources`, for the windows year to date and since inception ending <end date>. The
independent chain: every gold partition in the window read directly, the account's rows with status OK, split by the build that
wrote them (schema_version 1.2 = today's rebuild; anything else = a partition the rebuild did not rewrite).
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

PROBE = r'''
import io, json, math, os, sys
bundle, raw_account, end, which = sys.argv[1:5]
sys.path.insert(0, bundle)
for sub in ("lib", "data/assets/scripts/gold/investor_reporting", "data/assets/scripts/gold/runners_49f"):
    sys.path.insert(0, os.path.join(bundle, sub))
import boto3, pandas as pd
import holdings_gold, installed, tenants
from ids import opaque_account
s3 = boto3.client("s3")
# HARNESS ONLY: this network drops S3 body reads; a partition read that times out is re-read whole. The bundle's own
# reader is otherwise untouched (in its own region it does not see this).
_orig_read = holdings_gold.HoldingsGoldSource._read
def _retrying_read(self, day, account_key):
    for attempt in range(5):
        try:
            return _orig_read(self, day, account_key)
        except Exception as exc:
            if attempt == 4 or 'imeout' not in type(exc).__name__ + str(exc):
                raise
holdings_gold.HoldingsGoldSource._read = _retrying_read
holdings_gold.MAX_READ_WORKERS = 3
sources = installed._holdings_sources(s3)
print("holdings sources composed by the candidate: %s" % sorted(sources))
src = sources[tenants._CANONICAL_INF]
print("Inflection source: %s" % json.dumps(src.describe()))
account = opaque_account(tenants._CANONICAL_INF, raw_account)
dates = src.partition_dates()
print("gold partitions listed: %d (%s .. %s)" % (len(dates), dates[0], dates[-1]))
for label, start in [w for w in (("year to date", end[:4] + "-01-01"), ("since inception", "1970-01-01")) if which == "all" or w[0].startswith(which)]:
    scope = {"resolved_scope": {"scope_ids": [account]}, "permitted_account_set": [account],
             "verified_request_firm_id": tenants._LEGACY_SHORT_ID["INF"], "selection": {}}
    source = installed._holdings_sources(s3)[tenants._CANONICAL_INF]
    source.max_workers = 3
    try:
        out = holdings_gold.calculate(scope, start, end, source)
    except Exception as exc:
        print("  %-16s REFUSED %s: %s" % (label, type(exc).__name__, str(exc)[:160]))
        continue
    rep = out["report"]
    value = rep["returns"]["account_detail"][0]["value"]
    print("  %-16s %s..%s SERVED provider=%s currency=%s value %.12f; partitions read %d"
          % (label, start, end, rep["lineage"]["provider"], rep.get("currency") or (rep.get("returns") or {}).get("currency"), value, len(out["evidence"]["partitions"])))
    for a in out["absences"]:
        if a["fact"] in ("linked_days", "window_edge_inside_linked_days", "excluded_rows"):
            print("      %s [%s]: %s" % (a["fact"], a["status"], a["reason"][:200]))
    days = [d for d in dates if start <= d <= end]
    frame = source.frame(days, raw_account)
    ok = frame[frame["status"] == "OK"].sort_values("business_date")
    ver = ok["schema_version"].astype(str) if "schema_version" in ok.columns else None
    new = ok[ver == "1.2"]
    old = ok[ver != "1.2"]
    chain_new = math.prod(1.0 + float(r) for r in new["daily_return"]) - 1.0
    chain_all = math.prod(1.0 + float(r) for r in ok["daily_return"]) - 1.0
    print("      independent chain over %d OK rows of today's rebuild (schema 1.2): %.12f | over all %d OK rows in the window: %.12f"
          % (len(new), chain_new, len(ok), chain_all))
    print("      OK rows NOT of today's rebuild inside the window: %d %s" % (len(old), sorted(old["business_date"].astype(str))[:8]))
    print("      the candidate's value equals the rebuild-only chain: %s | equals the all-rows chain: %s"
          % (abs(value - chain_new) <= 1e-12, abs(value - chain_all) <= 1e-12))
'''


def main() -> None:
    awscmd, bundle, raw_account, end = sys.argv[1:5]
    which = sys.argv[5] if len(sys.argv) > 5 else "all"
    cfg = json.loads(subprocess.run(["cmd", "/c", awscmd, "lambda", "get-function-configuration", "--function-name",
                                     "irpt-performance-adapter", "--output", "json"], capture_output=True, text=True, check=True).stdout)
    env = dict(os.environ)
    for k, v in ((cfg.get("Environment") or {}).get("Variables") or {}).items():
        env[k] = v.replace("/var/task", bundle)
    env["AWS_DEFAULT_REGION"] = env["AWS_REGION"] = "us-east-1"
    p = subprocess.run([sys.executable, "-c", PROBE, bundle, raw_account, end, which], capture_output=True, text=True, env=env, timeout=1500)
    for ln in p.stdout.splitlines():
        if not ln.startswith("{"):
            print(ln[:300])
    if p.returncode:
        print("PROBE rc=%d: %s" % (p.returncode, p.stderr[-900:]))


if __name__ == "__main__":
    main()
