"""MDPF_SECHIST round 6, SH-t-27 leg L2: the first scheduled gold run after the apply, read in one command. Read only (Lambda config, CloudWatch Logs,
S3 get/list through the dry-run script's guarded client).

  python r6_l2_read.py
Checks, each printed with its denominator:
  1  live CodeSha256 equals the applied package (M6X6eJ3QCDXopGif5PvlrlqBS/ynXHOpuxWDUIGFbAQ=) and LastModified is the apply time;
  2  the first scheduled invocation after the apply: its log has 'run_class=scheduled', 'PUBLISHED opal-data-portal-v2/platinum/etfs/positioning_data.json', and 0 lines
     matching ImportError / Traceback / WRITE FAILED / SHAPE-CHECK FAIL;
  3  the served page was written by that run (generated_at after the apply) and r6_pin_dryrun_diff.py on the page's data_as_of prints changed_holdings=0
     (the dry run of the code at HEAD equals what the deployed code served; BEFORE the run the same command prints changed_holdings=2, the negative arm).
Last line: L2-READ-OK ... or L2-READ-PENDING no scheduled run after the apply yet ... or L2-READ-BAD <reason>.
"""
from __future__ import annotations

import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

import boto3

HERE = Path(__file__).resolve().parent
SHA = "M6X6eJ3QCDXopGif5PvlrlqBS/ynXHOpuxWDUIGFbAQ="
FN = "etf-positioning-producer"
LOG_GROUP = "/aws/lambda/" + FN
BAD = re.compile(r"ImportError|Traceback|WRITE FAILED|SHAPE-CHECK FAIL")


def main():
    lam = boto3.client("lambda", region_name="us-east-1")
    cfg = lam.get_function_configuration(FunctionName=FN)
    applied = dt.datetime.strptime(cfg["LastModified"], "%Y-%m-%dT%H:%M:%S.000+0000").replace(tzinfo=dt.timezone.utc)
    print("1 CodeSha256=" + cfg["CodeSha256"] + " LastModified=" + cfg["LastModified"])
    if cfg["CodeSha256"] != SHA:
        print("L2-READ-BAD live CodeSha256 is not the applied package (rolled back or re-deployed since?)")
        return 1

    logs = boto3.client("logs", region_name="us-east-1")
    start = int(applied.timestamp() * 1000)
    events, token = [], None
    while True:
        kw = {"logGroupName": LOG_GROUP, "startTime": start}
        if token:
            kw["nextToken"] = token
        r = logs.filter_log_events(**kw)
        events += r.get("events", [])
        token = r.get("nextToken")
        if not token:
            break
    starts = [e for e in events if "run_class=scheduled" in e["message"]]
    print("2 log events since the apply: " + str(len(events)) + "; scheduled invocations: " + str(len(starts)))
    if not starts:
        print("L2-READ-PENDING no scheduled run after the apply yet (next cron(0 13 * * ? *))")
        return 2
    first = min(e["timestamp"] for e in starts)
    window = [e for e in events if e["timestamp"] >= first - 5000 and e["timestamp"] <= first + 15 * 60 * 1000]
    bad = [e["message"].strip()[:160] for e in window if BAD.search(e["message"])]
    published = [e for e in window if "PUBLISHED opal-data-portal-v2/platinum/etfs/positioning_data.json" in e["message"]]
    print("2 first scheduled run at " + dt.datetime.fromtimestamp(first / 1000, dt.timezone.utc).isoformat() + ": " + str(len(window)) + " log lines, bad=" + str(len(bad)) + ", published=" + str(len(published)))
    if bad or not published:
        print("L2-READ-BAD bad lines=" + str(bad) + " published=" + str(len(published)))
        return 1

    s3 = boto3.client("s3")
    o = s3.get_object(Bucket="opal-data-portal-v2", Key="platinum/etfs/positioning_data.json")
    page = json.loads(o["Body"].read())
    gen = dt.datetime.strptime(page["generated_at"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=dt.timezone.utc)
    print("3 served generated_at=" + page["generated_at"] + " data_as_of=" + str(page.get("data_as_of")) + " spread=" + str(page.get("data_as_of_spread")))
    if gen <= applied:
        print("L2-READ-BAD served page predates the apply")
        return 1
    carried = {c: [h["ticker"] + "@" + h["returns_frontier"] for h in p["holdings"] if h.get("returns_frontier")] for c, p in page["portfolios"].items()}
    print("3 carried holdings per book: " + json.dumps({c: v for c, v in carried.items() if v}))
    out = subprocess.run([sys.executable, str(HERE / "r6_pin_dryrun_diff.py"), page["data_as_of"]], capture_output=True, text=True)
    last = [ln for ln in out.stdout.splitlines() if ln.startswith("DRYRUN-DIFF")]
    print("3 " + (last[-1] if last else "dry-run diff printed no DRYRUN-DIFF line: " + out.stdout[-300:] + out.stderr[-300:]))
    if not last or "changed_holdings=0" not in last[-1]:
        print("L2-READ-BAD the code at HEAD does not equal what the deployed code served")
        return 1
    print("L2-READ-OK served=" + page["generated_at"] + " published=1 bad_lines=0 dryrun_changed_holdings=0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
