"""Peers V shape, take 2: resolve the numeric scanner tickers as SEDOL stems.

Take 1 could only resolve peers whose scanner ticker was a US symbol, and 12 of 34 covered names
served. The numeric tickers turned out to be SEDOL stems that Bloomberg resolves directly
(/sedol/688910 returns TSMC, identical to 2330 TT Equity -- positive control run). This re-measures
with both routes, and carries an identity check so no peer is priced as the wrong security.
"""
import collections
import difflib
import json
import os
import re
import sys

import boto3

REPO = "C:/Users/Opal Bloomberg/Desktop/ajb_workspace"
sys.path.insert(0, REPO)
sys.path.insert(0, os.path.join(REPO, "integrations", "bloomberg", "mcp"))

import blp_client  # noqa: E402
from lib.research.scores import peers_v  # noqa: E402

SP = ("C:/Users/OPALBL~1/AppData/Local/Temp/claude/C--Users-Opal-Bloomberg-Desktop-ajb-workspace/"
      "d60f6524-dc92-4e15-937e-45e7685911cb/scratchpad/")
BUCKET = "opal-data-harvest"
OVERRIDES = {"BEST_FPERIOD_OVERRIDE": peers_v.BEST_FPERIOD_OVERRIDE_VALUE,
             "EQY_FUND_CRNCY": peers_v.FUND_CRNCY_OVERRIDE_VALUE}
FIELDS = list(peers_v.FIELDS) + ["NAME", "TICKER", "EXCH_CODE"]
US_LIKE = re.compile(r"^[A-Z][A-Z.\-/*]{0,6}$")

covered = [k.strip() for k in open(SP + "covered_keys.txt", encoding="utf-8") if k.strip()]
s3 = boto3.client("s3")


def latest_peer_key(sec):
    best = None
    for page in s3.get_paginator("list_objects_v2").paginate(
            Bucket=BUCKET, Prefix="peers/v1/%s/" % sec):
        for o in page.get("Contents", []):
            if o["Key"].endswith(".json") and (best is None or o["Key"] > best):
                best = o["Key"]
    return best


def peer_security(ticker):
    return ("%s US Equity" % ticker) if US_LIKE.match(ticker) else ("/sedol/%s" % ticker)


def names_agree(bbg_name, member_name):
    if not bbg_name or not member_name:
        return False
    a = re.sub(r"[^A-Z ]", " ", bbg_name.upper()).split()
    b = re.sub(r"[^A-Z ]", " ", member_name.upper()).split()
    if not a or not b:
        return False
    if a[0][:4] == b[0][:4]:
        return True
    return difflib.SequenceMatcher(None, " ".join(a[:3]), " ".join(b[:3])).ratio() >= 0.6


members = {}
for sec in covered:
    k = latest_peer_key(sec)
    members[sec] = []
    if not k:
        continue
    d = json.loads(s3.get_object(Bucket=BUCKET, Key=k)["Body"].read())
    for m in d.get("members") or []:
        t = str(m.get("ticker") or "")
        if t:
            members[sec].append({"ticker": t, "name": m.get("name") or "",
                                 "security": peer_security(t)})

universe = sorted({m["security"] for ms in members.values() for m in ms})
subjects = [k.replace("_", " ") for k in covered]
print("covered: %d | distinct peer securities to resolve: %d" % (len(covered), len(universe)))

data = {}
allsec = subjects + universe
for i in range(0, len(allsec), 40):
    chunk = allsec[i:i + 40]
    data.update(blp_client.reference_data(chunk, FIELDS, overrides=OVERRIDES, timeout_s=120.0))
    print("  pulled %d of %d" % (min(i + 40, len(allsec)), len(allsec)))

resolved = sum(1 for s in universe if data.get(s) and "__error__" not in data[s]
               and data[s].get("NAME"))
print("\nPEER RESOLUTION: %d of %d peer securities returned a NAME" % (resolved, len(universe)))

rows = []
mismatch = 0
for k in covered:
    subj = peers_v.compute_measures(data.get(k.replace("_", " "), {}))
    subj_ok = [m for m in peers_v.MEASURE_IDS if subj.get(m) is not None]
    peers_ok = collections.Counter()
    K = 0
    for m in members[k]:
        row = data.get(m["security"])
        if not row or "__error__" in row or not row.get("NAME"):
            continue
        if not names_agree(row.get("NAME"), m["name"]):
            mismatch += 1
            continue
        K += 1
        pm = peers_v.compute_measures(row)
        for mid in peers_v.MEASURE_IDS:
            if pm.get(mid) is not None:
                peers_ok[mid] += 1
    M = [m for m in subj_ok if peers_ok[m] >= peers_v.MIN_PEERS_PER_MEASURE]
    serves = K >= peers_v.MIN_PEERS_FOR_V and len(M) >= peers_v.MIN_MEASURES_FOR_V
    rows.append({"key": k, "subject_M": len(subj_ok), "K": K, "M_with_peers": len(M),
                 "members": len(members[k]), "serves": serves})
    print("   %-22s subj|M|=%d  K=%2d of %2d  |M|=%d  -> %s"
          % (k, len(subj_ok), K, len(members[k]), len(M), "SERVES" if serves else "suppressed"))

served = sum(1 for r in rows if r["serves"])
print("\nWOULD SERVE WITH SEDOL RESOLUTION: %d of %d covered names" % (served, len(covered)))
print("peer rows dropped on a NAME disagreement: %d" % mismatch)
json.dump(rows, open(SP + "peersv_shape2.json", "w", encoding="utf-8"), indent=1)
