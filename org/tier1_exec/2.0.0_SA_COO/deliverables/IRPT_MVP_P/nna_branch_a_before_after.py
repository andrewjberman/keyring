"""NNA Branch A (row IRPT_BCKEND-W97-S3): the three keys before and after, on the guard's OWN rule, and the vendor's re-typing re-read.

Usage: python nna_branch_a_before_after.py <repo root> <proposed excusals json>

Reads only. (1) The four transaction ids in the silver the served partition was built from (2026-09-25) and in the newest silver.
(2) The served partition gold/canonical/canonical_nna_2026-09-24.parquet read through the guard's own load_prior_partition_accounts.
(3) nna_coverage_guard.assert_partition_coverage_continuity with the served partition as the prior basis and the same partition
minus the three accounts as the rewrite: with the DEPLOYED excusals (positive control: it must raise and name the three), with the
PROPOSED excusals (it must pass and log three excusals), and with the proposed excusals when the same three accounts drop from a
DIFFERENT partition (negative control: date-scoped, it must still raise).
"""
from __future__ import annotations

import io
import sys

import boto3
import pandas as pd

root, proposed = sys.argv[1:3]
# The runner flattens gold/lib beside the scripts (/tmp/orion_gold_scripts); the guard imports its siblings flat.
sys.path.insert(0, root + "/data/inf/scripts/gold")
sys.path.insert(0, root + "/data/inf/scripts/gold/lib")
import nna_coverage_guard as g  # noqa: E402

BUCKET = "opal-data-inf"
ACCOUNTS = (866, 769, 1096)
IDS = (5885260, 5885261, 5885298, 5885276)
s3 = boto3.client("s3", region_name="us-east-1")

keys = sorted(o["Key"] for page in s3.get_paginator("list_objects_v2").paginate(Bucket=BUCKET, Prefix="silver/transactions/2026-")
              for o in page.get("Contents", []) if o["Key"].endswith(".parquet"))
print("silver/transactions partitions in 2026: %d; newest %s" % (len(keys), keys[-1]))
for key in ("silver/transactions/2026-09-25.parquet", keys[-1]):
    df = pd.read_parquet(io.BytesIO(s3.get_object(Bucket=BUCKET, Key=key)["Body"].read()))
    idcol = "id" if "id" in df.columns else [c for c in df.columns if c.lower() in ("transaction_id", "transid")][0]
    hit = df[df[idcol].isin(IDS)]
    cols = [c for c in (idcol, "accountId", "account_id", "transDate", "trans_date", "amount", "transTypeId", "trans_type_id",
                        "transType", "trans_type", "type") if c in hit.columns]
    print("== %s: %d rows; the four ids found: %d" % (key, len(df), len(hit)))
    for _, r in hit.sort_values(idcol).iterrows():
        print("    " + " | ".join("%s=%s" % (c, r[c]) for c in cols))

served_key = "gold/canonical/canonical_nna_2026-09-24.parquet"
head = s3.head_object(Bucket=BUCKET, Key=served_key)
served = pd.read_parquet(io.BytesIO(s3.get_object(Bucket=BUCKET, Key=served_key)["Body"].read()))
print("== served %s: %d rows, LastModified %s, columns %s" % (served_key, len(served), head["LastModified"].strftime("%Y-%m-%d %H:%M:%SZ"),
                                                                list(served.columns)))
acct = "account_id" if "account_id" in served.columns else "accountId"
three = served[served[acct].astype(int).isin(ACCOUNTS)]
show = [c for c in (acct, "advisor_key", "rep_id", "daily_inflow", "daily_outflow", "net_nna", "n_inflow_events", "n_outflow_events")
        if c in three.columns]
print("   the three keys as SERVED (%d rows):" % len(three))
for _, r in three.iterrows():
    print("     " + " | ".join("%s=%s" % (c, r[c]) for c in show))
for col in ("daily_inflow", "daily_outflow", "net_nna"):
    if col in served.columns:
        print("   partition total %-14s before %14.2f | after (the three rows gone) %14.2f"
              % (col, served[col].sum(), served[~served[acct].astype(int).isin(ACCOUNTS)][col].sum()))
if "advisor_key" in served.columns and "net_nna" in served.columns:
    for adv, grp in three.groupby("advisor_key"):
        whole = served[served["advisor_key"] == adv]
        print("   advisor %s: net_nna before %.2f | after %.2f; inflow before %.2f | after %.2f; outflow before %.2f | after %.2f"
              % (adv, whole["net_nna"].sum(), whole["net_nna"].sum() - grp["net_nna"].sum(),
                 whole["daily_inflow"].sum(), whole["daily_inflow"].sum() - grp["daily_inflow"].sum(),
                 whole["daily_outflow"].sum(), whole["daily_outflow"].sum() - grp["daily_outflow"].sum()))

prior, failures, absent = g.load_prior_partition_accounts(
    s3, BUCKET, lambda d: "gold/canonical/canonical_nna_%s.parquet" % d, ["2026-09-24", "2026-09-23"])
print("== guard's own prior read: partitions %s; read failures %d; absent %s; accounts in 2026-09-24: %d"
      % (sorted(prior), len(failures), absent, len(prior.get("2026-09-24", {}))))
new_0924 = {a: v for a, v in prior["2026-09-24"].items() if int(a) not in ACCOUNTS}
deployed = g.load_excusals()
prop = g.load_excusals(proposed)
print("   excusals: deployed/HEAD file %d account(s); proposed file %d account(s); added %s"
      % (len(deployed), len(prop), sorted(set(prop) - set(deployed))))


def run(label, prior_by_date, new_by_date, excusals, expect_raise):
    lines = []
    try:
        g.assert_partition_coverage_continuity(prior_by_date, [], new_by_date, excusals=excusals, log=lines.append)
        outcome = "PASSED: " + (lines[-1][:150] if lines else "")
        raised = False
    except g.NNACoverageRegression as exc:
        text = str(exc)
        outcome = "RAISED: " + text[:118] + " ... accounts named: %s" % sorted(
            int(tok.split(":")[0]) for tok in text.split("account ")[1:] if tok.split(":")[0].strip().isdigit())
        raised = True
    print("   %-58s %s  [%s]" % (label, outcome, "as expected" if raised == expect_raise else "NOT AS EXPECTED"))
    for ln in lines:
        if "EXCUSED" in ln:
            print("        " + ln.strip()[:140])
    return raised == expect_raise


ok = run("positive control: deployed excusals, 09-24 rewrite", {"2026-09-24": prior["2026-09-24"]}, {"2026-09-24": new_0924}, deployed, True)
ok &= run("PROPOSED excusals, 09-24 rewrite", {"2026-09-24": prior["2026-09-24"]}, {"2026-09-24": new_0924}, prop, False)
other = dict(prior.get("2026-09-23", {}))
other.update({866: -1.0, 769: 1.0, 1096: 1.0})
ok &= run("negative control: proposed excusals, same accounts, 09-23", {"2026-09-23": other},
          {"2026-09-23": {a: v for a, v in other.items() if int(a) not in ACCOUNTS}}, prop, True)
print("RESULT: %s" % ("3 of 3 arms as expected" if ok else "AN ARM DID NOT BEHAVE AS EXPECTED"))
