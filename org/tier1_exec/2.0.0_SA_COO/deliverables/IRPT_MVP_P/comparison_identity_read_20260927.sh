#!/bin/bash
# The comparison identity read (1.0.0_SA_CTO 102028 (1); spec 2.0.0_SA_COO~Y P_COMPARISON_IDENTITY_READ_ACT_20260927.md).
# Run ONCE on the resident host (i-0167fd745ad906a66) by SSM AWS-RunShellScript, inside a signed window.
#
# EXACTLY four GETs of /securities/securities_info on the resident's OWN published vendor session, through the
# resident factory's ResidentSession (the `_opal` operation lease serializes it with the worker). No body, no
# create, no retry. A non-200, a login destination or a non-JSON answer STOPS the act: that read is recorded as
# refused and the rest are not sent. The only output is the evidence JSON on stdout (gzip+base64 between markers);
# nothing is written to S3, the queue or any job row.
set -u
R=/opt/irpt-resident
UNIT=irpt-analysis-resident.service
RUN=$(systemctl show $UNIT -p ExecStart | grep -o "$R/[0-9a-z-]*" | head -1)
[ -n "$RUN" ] && [ -d "$RUN" ] || { echo "BLOCKED: no running resident root"; exit 10; }
echo "running root $RUN"
sudo -u ec2-user PYTHONPATH="$RUN" /usr/bin/python3.12 - "$RUN" <<'PY'
import base64, datetime, gzip, json, sys, urllib.parse
sys.path.insert(0, sys.argv[1] + "/reports")
import resident_installed as ri

IDS = ["P:1728413", "P:1728415", "P:1728315", "P:1728420"]
session = ri.build_resident_runtime()["assembly"].session
transport = session.acquire(request_budget=60, ttl=120)
reads, stopped = [], None
try:
    for ident in IDS:
        path = "/securities/securities_info?" + urllib.parse.urlencode({"securities": ident})
        try:
            info, body = transport.request(path)
        except Exception as exc:  # noqa: BLE001 -- a refused read is recorded, never retried
            reads.append({"identity": ident, "status": None, "error": type(exc).__name__})
            stopped = "%s:%s" % (ident, type(exc).__name__)
            break
        raw = body if isinstance(body, (bytes, bytearray)) else base64.b64decode(body or b"")
        ctype = str(info.get("content_type") or "")
        record = {"identity": ident, "status": info.get("status"), "content_type": ctype,
                  "waf_action": info.get("waf_action"), "login_destination": bool(info.get("login_destination")),
                  "final_url_path": info.get("final_url_path")}
        ok = info.get("status") == 200 and not record["login_destination"] and "json" in ctype
        record["body"] = json.loads(raw.decode("utf-8")) if ok else None
        reads.append(record)
        if not ok:
            stopped = "%s:status=%s login=%s" % (ident, info.get("status"), record["login_destination"])
            break
finally:
    transport.close()
evidence = {"retrieved_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "reads": reads, "stopped": stopped, "sent": len(reads)}
print("reads sent %d of 4; stopped %s; statuses %s" % (len(reads), stopped, [r.get("status") for r in reads]))
print("EVIDENCE_B64GZ_BEGIN")
print(base64.b64encode(gzip.compress(json.dumps(evidence, sort_keys=True).encode("utf-8"))).decode("ascii"))
print("EVIDENCE_B64GZ_END")
PY
echo "rc=$?"
