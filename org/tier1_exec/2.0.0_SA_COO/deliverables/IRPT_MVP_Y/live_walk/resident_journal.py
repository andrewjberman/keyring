"""Read-only: the resident service's journal lines since a UTC time, via SSM on P's host (no restart, no write).

    python resident_journal.py "2026-09-26 13:50:00" [grep-regex]
"""
import json
import os
import subprocess
import sys
import time

AWS = r"C:\Users\AndrewBerman\Desktop\ajb_workspace\.tools\aws.cmd"
INSTANCE = "i-0167fd745ad906a66"
since = sys.argv[1]
pattern = sys.argv[2] if len(sys.argv) > 2 else "."
script = ("journalctl -u irpt-analysis-resident.service --since '%s UTC' --no-pager -o short-iso "
          "| grep -E '%s' | cut -c1-400 | tail -80; echo \"lines_total=$(journalctl -u irpt-analysis-resident.service "
          "--since '%s UTC' --no-pager | wc -l)\"; systemctl is-active irpt-analysis-resident.service" % (since, pattern, since))


def aws(*args):
    out = subprocess.run([AWS, *args, "--output", "json"], capture_output=True, text=True)
    if out.returncode != 0:
        raise SystemExit("ERROR: aws %s rc=%d %s" % (args[1], out.returncode, out.stderr.strip()[:300]))
    return json.loads(out.stdout)


params = os.path.join(os.path.dirname(os.path.abspath(__file__)), "resident_journal_params.json")
with open(params, "w", encoding="utf-8") as fh:  # a file keeps cmd.exe from parsing the shell pipes
    json.dump({"commands": [script]}, fh)
sent = aws("ssm", "send-command", "--instance-ids", INSTANCE, "--document-name", "AWS-RunShellScript",
           "--comment", "2.0.0_SA_COO~Y read-only resident journal", "--parameters",
           "file://" + params.replace("\\", "/"))
cid = sent["Command"]["CommandId"]
for _ in range(30):
    time.sleep(2)
    try:
        inv = aws("ssm", "get-command-invocation", "--command-id", cid, "--instance-id", INSTANCE)
    except SystemExit:
        continue
    if inv["Status"] not in ("Pending", "InProgress", "Delayed"):
        print("ssm", cid, inv["Status"])
        print(inv.get("StandardOutputContent", ""))
        err = inv.get("StandardErrorContent", "")
        if err:
            print("STDERR:", err[:500])
        break
else:
    print("WARN: no result for", cid)
