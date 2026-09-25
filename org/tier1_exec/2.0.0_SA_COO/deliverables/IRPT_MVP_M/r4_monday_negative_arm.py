"""CTO R4 condition 3 (SIGNOFF_HOLDINGS_PRINCIPALS_DISPATCH_20260925.md @6c5c27a666): the NEGATIVE ARM, exercised as the
principals -- ledger irpt-holdings-principals-dispatch-m-20260925, leg N1.

The firm holdings principals trust ONLY the daily-runner host role, so the arm runs ON the host, over SSM. For each
case the host assumes the principal and tries one GetObject:
- COT's principal on opal-data-bd is expected REFUSED (AccessDenied);
- 49F's principal on opal-data-cot is expected REFUSED;
- each principal on its own firm's directory is the POSITIVE CONTROL, expected ALLOWED.
A refusal only means something beside an allow on the same call shape.

Read-only: GetObject to a discarded /dev/null, nothing written. Run in the host's up window (weekdays ~12:52Z-16:41Z):
  python org/.../IRPT_MVP_M/r4_monday_negative_arm.py --send       # sends the one SSM command, prints its id
  python org/.../IRPT_MVP_M/r4_monday_negative_arm.py --read <cid> # reads the result; exit 0 only if 4 of 4 match
"""
import argparse
import json
import sys
import time

import boto3

REGION = "us-east-1"
KEY = "investor-reporting/directory/latest.json"
# (principal role name, bucket, expectation). Role names are the applied opal_name output (plan @885ae2f3d6).
CASES = [
    ("irpt-cot-holdings-role", "opal-data-bd", "REFUSED"),
    ("irpt-49f-holdings-role", "opal-data-cot", "REFUSED"),
    ("irpt-cot-holdings-role", "opal-data-cot", "ALLOWED"),
    ("irpt-49f-holdings-role", "opal-data-bd", "ALLOWED"),
]


def _instance_id():
    manifest = json.load(open("infra/aws/ec2/EC2_MANIFEST.json", encoding="utf-8"))
    return manifest["services"]["mdpf-daily-runner"]["instance_id"]


def script(account):
    lines = ["set -u"]
    for role, bucket, want in CASES:
        arn = "arn:aws:iam::%s:role/%s" % (account, role)
        lines += [
            "if C=$(aws sts assume-role --role-arn '%s' --role-session-name irpt-n1 "
            "--query 'Credentials.[AccessKeyId,SecretAccessKey,SessionToken]' --output text); then" % arn,
            "  OUT=$(AWS_ACCESS_KEY_ID=$(echo \"$C\" | cut -f1) AWS_SECRET_ACCESS_KEY=$(echo \"$C\" | cut -f2) "
            "AWS_SESSION_TOKEN=$(echo \"$C\" | cut -f3) aws s3api get-object --bucket %s --key %s /dev/null 2>&1)" % (bucket, KEY),
            "  if [ $? -eq 0 ]; then R=ALLOWED; elif echo \"$OUT\" | grep -q AccessDenied; then R=REFUSED; else R=OTHER; fi",
            "else R=ASSUME-FAILED; fi",
            "echo \"N1 %s %s expect=%s got=$R\"" % (role, bucket, want),
        ]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--send", action="store_true")
    ap.add_argument("--read")
    args = ap.parse_args()
    ssm = boto3.client("ssm", region_name=REGION)
    iid = _instance_id()
    if args.send:
        account = boto3.client("sts").get_caller_identity()["Account"]
        cid = ssm.send_command(InstanceIds=[iid], DocumentName="AWS-RunShellScript",
                               Comment="irpt R4 N1 negative arm",
                               Parameters={"commands": [script(account)]})["Command"]["CommandId"]
        print(cid)
        return 0
    if args.read:
        for _ in range(30):
            inv = ssm.get_command_invocation(CommandId=args.read, InstanceId=iid)
            if inv["Status"] not in ("Pending", "InProgress", "Delayed"):
                break
            time.sleep(4)
        rows = [row for row in inv.get("StandardOutputContent", "").splitlines() if row.startswith("N1 ")]
        ok = sum(1 for row in rows if "expect=REFUSED got=REFUSED" in row or "expect=ALLOWED got=ALLOWED" in row)
        print("\n".join(rows))
        print("N1 %d of %d match (status %s)" % (ok, len(CASES), inv["Status"]))
        return 0 if ok == len(CASES) else 1
    ap.error("--send or --read <cid>")


if __name__ == "__main__":
    sys.exit(main())
