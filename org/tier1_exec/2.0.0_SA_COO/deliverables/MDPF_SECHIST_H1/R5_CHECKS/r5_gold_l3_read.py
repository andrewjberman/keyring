"""MDPF_SECHIST gold deploy, leg L3 (issuer's read): the first scheduled gold run after the apply (2026-10-10 13:00Z).

Read only. Four limbs, each printed with its denominator:
  1. served page: s3://opal-data-portal-v2/platinum/etfs/positioning_data.json LastModified on/after the run date, its data_as_of = D;
  2. gap record: the object at etf_history_gap_record.record_address(D) exists (SH-t-15 wrote it; the R1 grant worked);
  3. run log: CloudWatch /aws/lambda/etf-positioning-producer between <date> 12:55Z and 13:40Z -- 0 lines with ImportError /
     'WRITE FAILED' / Traceback, and at least one 'gap record' line;
  4. served vs the prior-day snapshot (CTO half condition 2): the same holdings keys; weight still a fraction (presentation unchanged);
     industry_group unchanged per key; SALXX / FXFXX 1D and WTD printed both days.

Usage: python r5_gold_l3_read.py <run_date YYYY-MM-DD> <prior_snapshot.json>
Last line: GOLD-L3-OK as_of=<D> ...   or   GOLD-L3-BAD <reason>.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import sys

import boto3

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, *[".."] * 6))
sys.path.insert(0, REPO)
sys.path.insert(0, os.path.join(REPO, "data", "etfs", "scripts", "silver"))
import etf_history_gap_record as gr  # noqa: E402

FN_LOG = "/aws/lambda/etf-positioning-producer"
MMF = ("SALXX", "FXFXX")


def _keyed(page):
    return {(c, h.get("ticker")): h for c, p in (page.get("portfolios") or {}).items() for h in p.get("holdings") or []}


def main(argv) -> int:
    run_date, prior_path = argv[1], argv[2]
    s3 = boto3.client("s3")
    o = s3.get_object(Bucket="opal-data-portal-v2", Key="platinum/etfs/positioning_data.json")
    page, lm = json.loads(o["Body"].read()), o["LastModified"]
    d = page.get("data_as_of")
    print("1 served: LastModified=" + lm.isoformat() + " data_as_of=" + str(d))
    if lm.date().isoformat() < run_date:
        print("GOLD-L3-BAD served-not-refreshed-since " + run_date)
        return 1

    addr = gr.record_address(d)
    bucket, key = addr[len("s3://"):].split("/", 1)
    try:
        rec = json.loads(s3.get_object(Bucket=bucket, Key=key)["Body"].read())
    except s3.exceptions.NoSuchKey:
        print("GOLD-L3-BAD no-gap-record " + addr)
        return 1
    print("2 gap record: " + addr + " keys=" + ",".join(sorted(rec)[:8]))

    logs = boto3.client("logs")
    t0 = int(dt.datetime.fromisoformat(run_date + "T12:55:00+00:00").timestamp() * 1000)
    t1 = int(dt.datetime.fromisoformat(run_date + "T13:40:00+00:00").timestamp() * 1000)
    lines, tok = [], None
    while True:
        kw = dict(logGroupName=FN_LOG, startTime=t0, endTime=t1)
        if tok:
            kw["nextToken"] = tok
        r = logs.filter_log_events(**kw)
        lines += [e["message"] for e in r.get("events", [])]
        tok = r.get("nextToken")
        if not tok:
            break
    bad = [x for x in lines if "ImportError" in x or "WRITE FAILED" in x or "Traceback" in x]
    gapl = [x for x in lines if "gap record" in x]
    print("3 log: lines=" + str(len(lines)) + " bad=" + str(len(bad)) + " gap_record_lines=" + str(len(gapl)))
    for x in (bad + gapl)[:6]:
        print("   " + x.strip()[:200])
    if not lines:
        print("GOLD-L3-BAD no-log-lines-in-window")
        return 1
    if bad:
        print("GOLD-L3-BAD log-errors=" + str(len(bad)))
        return 1
    if not gapl:
        print("GOLD-L3-BAD no-gap-record-line")
        return 1

    prior = _keyed(json.load(open(prior_path, encoding="utf-8")))
    now = _keyed(page)
    common = set(prior) & set(now)
    w_bad = [k for k in now if now[k].get("weight") is not None and now[k]["weight"] > 1.0]
    ig_diff = [k for k in common if prior[k].get("industry_group") != now[k].get("industry_group")]
    print("4 diff vs prior: keys now=" + str(len(now)) + " prior=" + str(len(prior)) + " common=" + str(len(common))
          + " weight>1=" + str(len(w_bad)) + " industry_group changed=" + str(len(ig_diff)))
    for k in sorted(k for k in common if k[1] in MMF):
        print("   " + str(k) + " prior 1D/WTD=" + str((prior[k]["returns"].get("1D"), prior[k]["returns"].get("WTD")))
              + " now 1D/WTD=" + str((now[k]["returns"].get("1D"), now[k]["returns"].get("WTD"))))
    if w_bad or ig_diff:
        print("GOLD-L3-BAD presentation-changed weight>1=" + str(len(w_bad)) + " ig=" + str(len(ig_diff)))
        return 1
    print("GOLD-L3-OK as_of=" + str(d) + " record=" + addr + " log_lines=" + str(len(lines)) + " common=" + str(len(common)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
