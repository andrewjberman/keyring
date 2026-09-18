"""Measure the peer-set shape for every covered name: size, and how many members carry a
Bloomberg-resolvable identifier at all. Read-only: S3 GetObject and nothing else."""
import json
import re

import boto3

BUCKET = "opal-data-harvest"
OUT = ("C:/Users/OPALBL~1/AppData/Local/Temp/claude/C--Users-Opal-Bloomberg-Desktop-ajb-workspace/"
       "d60f6524-dc92-4e15-937e-45e7685911cb/scratchpad/peers_shape.json")

s3 = boto3.client("s3")
paginator = s3.get_paginator("list_objects_v2")

latest = {}
n_obj = 0
for page in paginator.paginate(Bucket=BUCKET, Prefix="peers/v1/"):
    for o in page.get("Contents", []):
        n_obj += 1
        k = o["Key"][len("peers/v1/"):]
        if "/" not in k:
            continue
        sec, fn = k.rsplit("/", 1)
        if not fn.endswith(".json"):
            continue
        stamp = fn[:-5]
        if sec not in latest or stamp > latest[sec][0]:
            latest[sec] = (stamp, o["Key"])

print("peer objects listed: %d | subjects with a peer set: %d" % (n_obj, len(latest)))

US_LIKE = re.compile(r"^[A-Z][A-Z.\-/*]{0,6}$")
rows = []
for sec in sorted(latest):
    stamp, key = latest[sec]
    body = s3.get_object(Bucket=BUCKET, Key=key)["Body"].read()
    d = json.loads(body)
    members = d.get("members") or []
    alpha, numeric = [], []
    for m in members:
        t = str(m.get("ticker") or "")
        (alpha if US_LIKE.match(t) else numeric).append(t)
    rows.append({
        "security_key": sec, "as_of": stamp, "members": len(members),
        "alpha_tickers": len(alpha), "numeric_tickers": len(numeric),
        "reaches_K8_on_alpha_only": len(alpha) >= 8,
        "reaches_K8_on_all_members": len(members) >= 8,
        "sample_alpha": alpha[:6], "sample_numeric": numeric[:6],
        "reason": (d.get("reason") or "")[:160],
    })

tot = len(rows)
print("\n%-22s %6s %6s %7s %8s" % ("subject", "K", "alpha", "numeric", "K>=8?"))
for r in rows:
    print("%-22s %6d %6d %7d %8s"
          % (r["security_key"], r["members"], r["alpha_tickers"], r["numeric_tickers"],
             "yes" if r["reaches_K8_on_all_members"] else "NO"))

k8 = sum(1 for r in rows if r["reaches_K8_on_all_members"])
k8a = sum(1 for r in rows if r["reaches_K8_on_alpha_only"])
zero = sum(1 for r in rows if r["members"] == 0)
print("\nDENOMINATOR %d subjects with a landed peer set" % tot)
print("  reach |K|>=8 counting every member        : %d" % k8)
print("  reach |K|>=8 on alpha-ticker members only : %d" % k8a)
print("  empty peer sets                           : %d" % zero)
print("  total members across all sets             : %d" % sum(r["members"] for r in rows))
print("  members with a numeric/SEDOL-shaped ticker: %d"
      % sum(r["numeric_tickers"] for r in rows))

json.dump(rows, open(OUT, "w", encoding="utf-8"), indent=1)
print("\nwrote", OUT)
