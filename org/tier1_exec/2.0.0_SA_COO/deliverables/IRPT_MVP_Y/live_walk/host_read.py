"""Run ONE shell script on the resident host through Systems Manager and print its output.

    python host_read.py <script-file> [comment]

The script file is sent verbatim as the AWS-RunShellScript command list (one entry). This tool adds no command of its
own. It is the caller's discipline that a READ script only reads; an install script is run with this same tool, under
its ledger. The instance id is the resident host's. Output: the SSM command id and status, stdout, and stderr if any.
ASCII only.
"""
import json
import os
import subprocess
import sys
import tempfile
import time

AWS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "..", "..", ".tools", "aws.cmd")
INSTANCE = "i-0167fd745ad906a66"


def aws(*args):
    out = subprocess.run([os.path.normpath(AWS), *args, "--output", "json"], capture_output=True, text=True)
    if out.returncode != 0:
        raise SystemExit("ERROR: aws %s rc=%d %s" % (args[1], out.returncode, out.stderr.strip()[:300]))
    return json.loads(out.stdout)


def main(argv):
    with open(argv[1], "r", encoding="utf-8") as fh:
        script = fh.read()
    comment = (argv[2] if len(argv) > 2 else "2.0.0_SA_COO~Y host read")[:100]
    with tempfile.TemporaryDirectory() as tmp:
        params = os.path.join(tmp, "params.json")
        with open(params, "w", encoding="utf-8") as fh:  # a file keeps cmd.exe from parsing the shell pipes
            json.dump({"commands": [script], "executionTimeout": ["600"]}, fh)
        sent = aws("ssm", "send-command", "--instance-ids", INSTANCE, "--document-name", "AWS-RunShellScript",
                   "--comment", comment, "--parameters", "file://" + params.replace("\\", "/"))
    cid = sent["Command"]["CommandId"]
    for _ in range(150):
        time.sleep(2)
        try:
            inv = aws("ssm", "get-command-invocation", "--command-id", cid, "--instance-id", INSTANCE)
        except SystemExit:
            continue
        if inv["Status"] not in ("Pending", "InProgress", "Delayed"):
            print("ssm", cid, inv["Status"], "rc", inv.get("ResponseCode"))
            print(inv.get("StandardOutputContent", ""))
            err = inv.get("StandardErrorContent", "")
            if err:
                print("STDERR:", err[:1500])
            return 0 if inv["Status"] == "Success" else 1
    print("WARN: no result for", cid)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
