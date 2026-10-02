#!/usr/bin/env python3
"""Row IRPT_BCKEND-S270 (CTO batch 169): server REPORT durations of irpt-status's owned reads, beside client wall times.

    python s270_timing.py <tenant> <request-id> <out.json>

One login as svc-irpt-analysis; GETs only, in sequence: history (default page), history (limit=50), the single read,
and the job status (with the portal's dates capability). Then the irpt-status log group's REPORT lines for the window
are read and printed in order (Duration, Billed, Max Memory, Init). Nothing is created; no vendor is reached. ASCII only.
"""
import json
import subprocess
import sys
import time

import served_reads_before_after as reads
import svc_principal as sp

AWS = sp.AWS if hasattr(sp, "AWS") else None


def aws_json(*args):
    import os
    tool = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "..", "..", ".tools", "aws.cmd")
    out = subprocess.run([os.path.normpath(tool), *args, "--output", "json"], capture_output=True, text=True)
    if out.returncode != 0:
        raise SystemExit("aws %s rc=%d %s" % (args[1], out.returncode, out.stderr.strip()[:300]))
    return json.loads(out.stdout)


def main(argv):
    tenant, rid, out = argv[1], argv[2], argv[3]
    log = []
    password = sp._sm().get_secret_value(SecretId=sp.SECRET)["SecretString"]
    code, login = sp._call("POST", "/auth/login", {"email": sp.EMAIL, "password": password},
                           {"Content-Type": "application/json"}, log)
    del password
    headers = {"Authorization": "Bearer " + login["accessToken"], "X-Contract-Version": "v1",
               "Content-Type": "application/json"}
    q = "?selected_tenant=" + tenant
    start_ms = int(time.time() * 1000) - 1000
    calls = [("history default", "analysis/requests" + q, headers),
             ("history limit=50", "analysis/requests" + q + "&limit=50", headers),
             ("single read", "analysis/requests/%s%s" % (rid, q), headers),
             ("status (dates)", "status/%s%s" % (rid, q), dict(headers, **{"X-IRPT-Status-Dates": "prospect-v1"}))]
    rows = []
    for name, path, sent in calls:
        t0 = time.time()
        code, resp = sp._call("GET", reads.BASE + path, None, sent, log)
        wall = time.time() - t0
        row = {"call": name, "http": code, "client_wall_s": round(wall, 2)}
        row.update(reads.shape(resp))
        data = resp.get("data") if isinstance(resp, dict) else None
        if isinstance(data, dict) and isinstance(data.get("items"), list):
            row["items"] = len(data["items"])
        rows.append(row)
        print("%-18s HTTP %s ok %s reason %s items %s client wall %.2f s" % (
            name, code, row.get("ok"), row.get("reason"), row.get("items", "-"), wall))
        time.sleep(1)
    time.sleep(15)  # REPORT lines reach CloudWatch Logs a few seconds after the invocation ends
    events = aws_json("logs", "filter-log-events", "--log-group-name", "/aws/lambda/irpt-status",
                      "--start-time", str(start_ms), "--filter-pattern", "REPORT")["events"]
    reports = []
    for e in sorted(events, key=lambda e: e["timestamp"]):
        msg = e["message"]
        fields = {}
        for part in msg.split("\t"):
            if ":" in part:
                k, v = part.split(":", 1)
                fields[k.strip()] = v.strip()
        reports.append({"at_ms": e["timestamp"], "duration": fields.get("Duration"), "billed": fields.get("Billed Duration"),
                        "max_memory": fields.get("Max Memory Used"), "init": fields.get("Init Duration")})
        print("REPORT duration %-12s billed %-10s max memory %-8s init %s" % (
            fields.get("Duration"), fields.get("Billed Duration"), fields.get("Max Memory Used"), fields.get("Init Duration")))
    json.dump({"at": sp._now(), "tenant": tenant, "request_id": rid, "calls": rows, "reports": reports},
              open(out, "w", encoding="utf-8", newline="\n"), indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
