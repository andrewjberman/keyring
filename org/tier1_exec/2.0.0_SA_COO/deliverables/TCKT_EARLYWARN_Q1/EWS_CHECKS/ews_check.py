"""TCKT_EARLYWARN TO-EWS-d1 criteria (read-only: AWS get/describe/simulate and local files; no write, nothing sends).
  python ews_check.py running   EWS-RUN-OK  : the deploy manifest exists, names the resources built by ews/names.py resource_names() (task, role), and the one task reads RUNNING
  python ews_check.py iam       EWS-IAM-OK  : the role, SIMULATED, may GetSecretValue on opal/ews/graph-app-cert and read the two Schwab silver prefixes, and may NOT
                                              GetSecretValue on any other secret, write to S3, or send (ses, sns, sqs)
  python ews_check.py ledger    EWS-LED-OK  : the NEVER-2 ledger entry for this deploy is CLOSED and its sentinel is committed
Else EWS-BAD <why>. Run from the repository root. The manifest is written by the deploying lane: org/tier1_exec/0.7.0_AE_CloudOps~TM1/deliverables/EWS_DEPLOY.json with keys
cluster, task_arn, role_arn, role_name, task_name, ledger_slug. The positive arms are unexercised until the first deploy; a misfiring check is a surprise row, never a weakened check.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

MANIFEST = os.path.join("org", "tier1_exec", "0.7.0_AE_CloudOps~TM1", "deliverables", "EWS_DEPLOY.json")
NAMES_DIR = os.path.join("infra", "aws", "ec2", "client-ops-early-warning")
SECRET = "opal/ews/graph-app-cert"
BUCKET = "opal-data-assets"
MASTERS = ("08335338", "08242234")


def bad(why: str) -> int:
    print("EWS-BAD " + why)
    return 1


def aws(*args: str) -> dict:  # no bare "*" argument: the shim re-expands it against the working directory
    r = subprocess.run(["bash", ".tools/aws", *args, "--output", "json"], capture_output=True, text=True, timeout=100, check=False)
    if r.returncode != 0:
        raise RuntimeError("aws %s rc=%d: %s" % (" ".join(args[:3]), r.returncode, (r.stderr or r.stdout)[-300:]))
    return json.loads(r.stdout)


def manifest() -> dict:
    if not os.path.isfile(MANIFEST):
        raise FileNotFoundError("no deploy manifest at " + MANIFEST)
    return json.load(open(MANIFEST, encoding="utf-8"))


def built_names() -> dict:
    sys.path.insert(0, NAMES_DIR)
    from ews.names import resource_names  # noqa: E402
    return resource_names()


def running() -> int:
    m, names = manifest(), built_names()
    if m.get("task_name") != names["task"] or m.get("role_name") != names["role"]:
        return bad("manifest names %r/%r, name() builds %r/%r" % (m.get("task_name"), m.get("role_name"), names["task"], names["role"]))
    d = aws("ecs", "describe-tasks", "--cluster", m["cluster"], "--tasks", m["task_arn"])
    tasks = d.get("tasks") or []
    if len(tasks) != 1 or tasks[0].get("lastStatus") != "RUNNING" or len(tasks[0].get("containers") or []) != 1:
        return bad("expected one RUNNING task with one container, read %s" % json.dumps([(t.get("lastStatus"), len(t.get("containers") or [])) for t in tasks]))
    print("EWS-RUN-OK")
    return 0


def simulate(role_arn: str, action: str, resource: str) -> str:
    d = aws("iam", "simulate-principal-policy", "--policy-source-arn", role_arn, "--action-names", action, "--resource-arns", resource)
    return d["EvaluationResults"][0]["EvalDecision"]


def iam() -> int:
    m = manifest()
    role = m["role_arn"]
    acct = role.split(":")[4]
    secret_arn = "arn:aws:secretsmanager:us-east-1:%s:secret:%s-*" % (acct, SECRET)
    other_secret = "arn:aws:secretsmanager:us-east-1:%s:secret:opal/other/not-ews-*" % acct
    allow = [("secretsmanager:GetSecretValue", secret_arn)]
    for mst in MASTERS:
        allow.append(("s3:GetObject", "arn:aws:s3:::%s/schwab/%s/silver/x" % (BUCKET, mst)))
    deny = [("secretsmanager:GetSecretValue", other_secret),
            ("s3:PutObject", "arn:aws:s3:::%s/schwab/%s/silver/x" % (BUCKET, MASTERS[0])),
            ("s3:GetObject", "arn:aws:s3:::%s/schwab/%s/bronze/x" % (BUCKET, MASTERS[0])),
            ("ses:SendEmail", "arn:aws:ses:us-east-1:%s:identity/opalinvest.com" % acct),
            ("sns:Publish", "arn:aws:sns:us-east-1:%s:ews-probe-topic" % acct),
            ("sqs:SendMessage", "arn:aws:sqs:us-east-1:%s:ews-probe-queue" % acct)]
    for act, res in allow:
        got = simulate(role, act, res)
        if got != "allowed":
            return bad("%s on %s reads %s, wanted allowed" % (act, res, got))
    for act, res in deny:
        got = simulate(role, act, res)
        if got == "allowed":
            return bad("%s on %s reads allowed, wanted denied" % (act, res))
    print("EWS-IAM-OK")
    return 0


def ledger() -> int:
    m = manifest()
    slug = m.get("ledger_slug")
    if not slug:
        return bad("manifest has no ledger_slug")
    sentinel = os.path.join("org", "critical_paths", ".open_deploys", slug + ".json")
    cm = [f for f in os.listdir(os.path.join("org", "critical_paths", "change_management")) if slug in f and f.endswith("_deploy_completion.md")]
    if not cm:
        return bad("no closed change-management entry for " + slug)
    r = subprocess.run(["git", "ls-files", "--error-unmatch", sentinel], capture_output=True, text=True, check=False)
    if r.returncode != 0:
        return bad("sentinel %s is not committed" % sentinel)
    print("EWS-LED-OK")
    return 0


if __name__ == "__main__":
    arm = sys.argv[1] if len(sys.argv) > 1 else ""
    try:
        sys.exit({"running": running, "iam": iam, "ledger": ledger}[arm]())
    except KeyError:
        sys.exit(bad("unknown arm %r" % arm))
    except Exception as exc:  # a failed read is BAD, never an error
        sys.exit(bad("%s: %s" % (type(exc).__name__, exc)))
