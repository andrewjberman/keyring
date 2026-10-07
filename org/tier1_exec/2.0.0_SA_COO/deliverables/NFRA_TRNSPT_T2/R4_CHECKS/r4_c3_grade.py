"""NFRA_TRNSPT round 4, cell TR-p-4 (C3) -- the issuer's grading check for ONE scheduled fire of the mail pull (2.0.0_SA_COO~T2).

READ-ONLY. It prints keys, counts, hashes-equal tallies and field names ONLY -- never a sender, subject, address, name or any
message or meeting content (MSTR msg 957 standing condition; PRD v0.2 C-READERS).

  fire   --since ISO [--until ISO]   CloudWatch: exactly one MAIL-PULL-FIRE line in the window, its fields, landed>=1;
                                     the invocation is the schedule's: one START in the window, within 120 s of HH:30:00Z
                                     (the rule is cron(30 23 * * ? *)), and Lambda Invocations summed over the window = 1
  store  --since ISO [--until ISO]   S3: bronze analysis_commentary keys written in the window; for each sidecar, the
                                     message / attachments / PDF objects' sha256 equal the sidecar's; silver parquet keys
                                     written in the window and their row and held_out counts. A KMS refusal prints
                                     C3-STORE-DECRYPT-REFUSED with the key counts (grade leg (2) by the laptop file then)

Exit 0 = every check in the mode passed; 1 = a check failed; 3 = decrypt refused (store mode only).
"""
import argparse
import hashlib
import io
import json
import sys
from datetime import datetime, timedelta, timezone

FUNCTION = "outlook-global-transcripts-pull-lambda"
LOG_GROUP = "/aws/lambda/" + FUNCTION
BUCKET = "opal-data-transcripts"
BRONZE = "outlook/transcripts/bronze/analysis_commentary/"
SILVER = "outlook/transcripts/silver/analysis_commentary/"
FIELDS = ["run", "window_days", "listed", "admitted", "landed", "skipped_known", "list_refusals", "silver_rows", "held_out"]


def _ts(s):
    return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)


def _events(logs, since, until, pattern):
    out, kw = [], {"logGroupName": LOG_GROUP, "startTime": int(since.timestamp() * 1000),
                   "endTime": int(until.timestamp() * 1000), "filterPattern": pattern}
    while True:
        r = logs.filter_log_events(**kw)
        out += r.get("events", [])
        if not r.get("nextToken"):
            return out
        kw["nextToken"] = r["nextToken"]


def fire(since, until):
    import boto3
    logs, cw = boto3.client("logs"), boto3.client("cloudwatch")
    ok = True
    lines = [e for e in _events(logs, since, until, '"MAIL-PULL-FIRE"') if e["message"].startswith("MAIL-PULL-FIRE ")]
    if len(lines) != 1:
        print("C3-FIRE-FAIL fire_lines=%d (expected 1) window=%s..%s" % (len(lines), since.isoformat(), until.isoformat()))
        ok = False
    else:
        kv = dict(p.split("=", 1) for p in lines[0]["message"].split()[1:])
        if list(kv) != FIELDS:
            print("C3-FIRE-FAIL field set %s" % ",".join(kv))
            ok = False
        else:
            landed = int(kv["landed"])
            print("C3-FIRE-%s %s" % ("OK" if landed >= 1 else "FAIL", " ".join("%s=%s" % (k, kv[k]) for k in FIELDS)))
            ok = ok and landed >= 1
    starts = [e for e in _events(logs, since, until, '"START RequestId"')]
    sched = []
    for e in starts:
        t = datetime.fromtimestamp(e["timestamp"] / 1000, timezone.utc)
        slot = t.replace(minute=30, second=0, microsecond=0)
        sched.append(abs((t - slot).total_seconds()) <= 120)
    m = cw.get_metric_statistics(Namespace="AWS/Lambda", MetricName="Invocations",
                                 Dimensions=[{"Name": "FunctionName", "Value": FUNCTION}], StartTime=since,
                                 EndTime=until, Period=60, Statistics=["Sum"])
    inv = int(sum(p["Sum"] for p in m.get("Datapoints", [])))
    s_ok = len(starts) == 1 and all(sched) and inv == 1
    print("C3-SCHEDULED-%s starts=%d at_cron_slot=%d invocations_metric=%d" % (
        "OK" if s_ok else "FAIL", len(starts), sum(sched), inv))
    return 0 if ok and s_ok else 1


def _keys(s3, prefix, since, until):
    out = []
    for page in s3.get_paginator("list_objects_v2").paginate(Bucket=BUCKET, Prefix=prefix):
        for o in page.get("Contents", []):
            if since <= o["LastModified"] < until:
                out.append(o["Key"])
    return out


def store(since, until):
    import boto3
    from botocore.exceptions import ClientError
    s3 = boto3.client("s3")
    bronze, silver = _keys(s3, BRONZE, since, until), _keys(s3, SILVER, since, until)
    sidecars = [k for k in bronze if k.endswith(".sidecar.json")]
    print("C3-STORE-KEYS bronze_objects=%d sidecars=%d silver_objects=%d (denominator: keys with LastModified in %s..%s)"
          % (len(bronze), len(sidecars), len(silver), since.isoformat(), until.isoformat()))

    def get(key):
        return s3.get_object(Bucket=BUCKET, Key=key)["Body"].read()

    try:
        checked = equal = 0
        for sk in sidecars:
            sc = json.loads(get(sk).decode("utf-8"))
            base = sk[: -len(".sidecar.json")]
            pairs = [(base + ".json", sc["sha256"]["message"]), (base + ".attachments.json", sc["sha256"]["attachments"])]
            d = sk.rsplit("/", 1)[0] + "/"
            pairs += [(d + p["object"], p["sha256"]) for p in sc.get("pdfs", [])]
            for key, want in pairs:
                checked += 1
                equal += hashlib.sha256(get(key)).hexdigest() == want
        rows = held = 0
        import pyarrow.parquet as pq
        for k in [k for k in silver if k.endswith(".parquet")]:
            t = pq.read_table(io.BytesIO(get(k)), columns=["held_out"])
            rows += t.num_rows
            held += sum(1 for v in t.column("held_out").to_pylist() if v)
    except ClientError as exc:
        code = exc.response.get("Error", {}).get("Code", "")
        if code in ("AccessDenied", "AccessDeniedException", "KMS.AccessDeniedException"):
            print("C3-STORE-DECRYPT-REFUSED %s (grade leg (2) by the laptop file)" % code)
            return 3
        raise
    b_ok = bool(sidecars) and checked > 0 and equal == checked
    print("C3-BRONZE-%s messages=%d objects_checked=%d hashes_equal=%d" % ("OK" if b_ok else "FAIL", len(sidecars),
                                                                           checked, equal))
    print("C3-SILVER rows=%d held_out=%d not_held_out=%d" % (rows, held, rows - held))
    return 0 if b_ok else 1


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["fire", "store"])
    ap.add_argument("--since", required=True, type=_ts)
    ap.add_argument("--until", type=_ts)
    a = ap.parse_args(argv)
    until = a.until or min(a.since + timedelta(hours=1), datetime.now(timezone.utc))
    return fire(a.since, until) if a.mode == "fire" else store(a.since, until)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
