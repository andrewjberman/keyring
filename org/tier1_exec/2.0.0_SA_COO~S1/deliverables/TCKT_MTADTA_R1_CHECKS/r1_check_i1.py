"""TCKT_MTADTA round 1, cell MD-i-1 checks. Run from the repo (worktree) root.

  python r1_check_i1.py app  -> I1-APP-OK  (one permission, app-only, secret never printed)
  python r1_check_i1.py subs -> I1-SUBS-OK (three content types, dry-run by default)
  python r1_check_i1.py tf   -> I1-TF-OK   (a secret container and no secret value)
"""
import contextlib
import importlib.util
import io
import os
import re
import sys

ROOT = os.getcwd()
APPDIR = os.path.join(ROOT, "data", "m365_metadata", "scripts", "app")
IDENT_TF = os.path.join(ROOT, "infra", "aws", "terraform", "trino", "identity.tf")
SECRET_ID = "m365-metadata/trino/api-credentials"


def load(name):
    p = os.path.join(APPDIR, name + ".py")
    if not os.path.exists(p):
        raise FileNotFoundError(p)
    spec = importlib.util.spec_from_file_location("i1_" + name, p)
    m = importlib.util.module_from_spec(spec)
    sys.path.insert(0, APPDIR)
    spec.loader.exec_module(m)
    return m


class FakeSM:
    def __init__(self):
        self.calls = []

    def put_secret_value(self, **kw):
        self.calls.append(kw)
        return {}


def app():
    m = load("register_app")
    bad = []
    plan = m.build_plan()
    perms = [(p.get("resource"), p.get("permission"), p.get("type")) for p in plan.get("permissions", [])]
    if perms != [("Office 365 Management APIs", "ActivityFeed.Read", "Role")]:
        bad.append("permissions %r" % (perms,))
    if plan.get("secret_id") != SECRET_ID:
        bad.append("secret id %r" % plan.get("secret_id"))
    if plan.get("signin_audience") != "AzureADMyOrg" or plan.get("graph_permissions"):
        bad.append("single tenant and no Graph permission")
    sm = FakeSM()
    buf = io.StringIO()
    value = "VALUE-THAT-MUST-NOT-PRINT-9f3c"
    with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
        m.store_secret(sm, value)
    if value in buf.getvalue():
        bad.append("the secret value was printed")
    if len(sm.calls) != 1 or sm.calls[0].get("SecretId") != SECRET_ID:
        bad.append("secret not stored by id: %r" % (sm.calls,))
    if bad:
        print("I1-APP-REFUSED " + "; ".join(bad))
        return 1
    print("I1-APP-OK")
    return 0


def subs():
    m = load("start_subscriptions")
    bad = []
    if list(m.CONTENT_TYPES) != ["Audit.Exchange", "Audit.SharePoint", "Audit.General"]:
        bad.append("content types %r" % (list(m.CONTENT_TYPES),))
    calls = []
    plan = m.run(lambda *a, **k: calls.append((a, k)), apply=False)
    if calls:
        bad.append("a network call was made without apply")
    if len(plan) != 3:
        bad.append("plan has %d entries" % len(plan))
    if bad:
        print("I1-SUBS-REFUSED " + "; ".join(bad))
        return 1
    print("I1-SUBS-OK")
    return 0


def tf():
    if not os.path.exists(IDENT_TF):
        print("I1-TF-REFUSED no identity.tf")
        return 1
    t = open(IDENT_TF, encoding="utf-8").read()
    bad = []
    if not re.search(r'resource\s+"aws_secretsmanager_secret"', t):
        bad.append("no secret container")
    if re.search(r'aws_secretsmanager_secret_version|secret_string|secret_binary', t):
        bad.append("a secret value in Terraform")
    if SECRET_ID not in t and "opal_name" not in t and "local." not in t:
        bad.append("secret id not the ruled one")
    if re.search(r'resource\s+"(aws_sns_[a-z_]+|aws_cloudwatch_metric_alarm)"', t):
        bad.append("alarm or notification (C-NOALERT)")
    if bad:
        print("I1-TF-REFUSED " + "; ".join(bad))
        return 1
    print("I1-TF-OK")
    return 0


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    fn = {"app": app, "subs": subs, "tf": tf}.get(mode)
    try:
        sys.exit(fn() if fn else 2)
    except FileNotFoundError as e:
        print("%s-REFUSED missing %s" % (mode.upper(), e))
        sys.exit(1)
