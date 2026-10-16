"""IRPT_ANLREQ round 55, workstream T -- the issuer's LIVE read-only check of the commentary hop's FWD-4 release (2.0.0_SA_COO~T2).

  ap1  R55-AP1  the release is applied: the draft-store role's inline policy carries S6 and S7 (and S6 allows exactly dynamodb:UpdateItem),
                the draft-store Lambda no longer runs the pre-act digest cwf6bUEb, and the commentary function runs a digest that is neither
                the pre-act hUZY39qN nor the pull functions' (which still run hUZY39qN: the surgical zip reached the commentary function only).

Read-only: one policy read and three configuration reads. Prints R55-AP1-OK or R55-AP1-FAIL <reason>.
"""
import json
import subprocess
import sys

DRAFT_STORE = "irpt-commentary-draft-store-lambda"
ROLE = "irpt-commentary-draft-store-role"
POLICY = "irpt-commentary-draft-store-policy"
COMMENTARY = "outlook-global-commentary-draft-lambda"
PULLS = ["teams-global-transcripts-pull-lambda", "outlook-global-transcripts-pull-lambda"]
PRE_DRAFT_STORE = "cwf6bUEb"
PRE_COMMENTARY = "hUZY39qN"
AWS = [sys.executable, "-c", "import subprocess,sys;sys.exit(subprocess.call(['bash','.tools/aws']+sys.argv[1:]))"]


def aws(*args):
    r = subprocess.run(AWS + list(args), capture_output=True, text=True, timeout=120)
    return r.returncode, r.stdout, r.stderr


def digest(fn):
    rc, so, _ = aws("lambda", "get-function-configuration", "--function-name", fn, "--query", "CodeSha256", "--output", "text")
    return so.strip() if rc == 0 and so.strip() else None


def statements():
    rc, so, _ = aws("iam", "get-role-policy", "--role-name", ROLE, "--policy-name", POLICY, "--query", "PolicyDocument.Statement", "--output", "json")
    if rc != 0:
        return None
    try:
        return json.loads(so)
    except ValueError:
        return None


def check_policy(stmts):
    """(ok, why) over a statement list: S6 and S7 present, S6 allows exactly dynamodb:UpdateItem, S1..S5 still present."""
    by = {str(s.get("Sid", ""))[:2]: s for s in (stmts or [])}
    missing = [k for k in ("S1", "S2", "S3", "S4", "S5", "S6", "S7") if k not in by]
    if missing:
        return False, "inline policy lacks %s" % ",".join(missing)
    act = by["S6"].get("Action")
    acts = [act] if isinstance(act, str) else list(act or [])
    if acts != ["dynamodb:UpdateItem"]:
        return False, "S6 actions are %s, not exactly dynamodb:UpdateItem" % acts
    return True, "S1..S7 present, S6 = UpdateItem only"


def main():
    ok, why = check_policy(statements())
    if not ok:
        return False, why
    ds = digest(DRAFT_STORE)
    cm = digest(COMMENTARY)
    pulls = [digest(p) for p in PULLS]
    if None in [ds, cm] + pulls:
        return False, "a configuration read failed"
    if ds.startswith(PRE_DRAFT_STORE):
        return False, "the draft-store Lambda still runs the pre-act digest %s" % ds[:8]
    if cm.startswith(PRE_COMMENTARY):
        return False, "the commentary function still runs the pre-act digest %s" % cm[:8]
    if any(not p.startswith(PRE_COMMENTARY) for p in pulls):
        return False, "a pull function moved off %s (the surgical zip must reach the commentary function only): %s" % (PRE_COMMENTARY, [p[:8] for p in pulls])
    return True, "%s; draft-store=%s commentary=%s pulls=%s" % (why, ds[:8], cm[:8], [p[:8] for p in pulls])


def self_test():
    good = [{"Sid": "S%d%s" % (i, "X"), "Action": ["dynamodb:UpdateItem"] if i == 6 else ["x"]} for i in range(1, 8)]
    cases = [("green", good, True), ("S7 absent", good[:6], False),
             ("S6 widened", [dict(s, Action=["dynamodb:UpdateItem", "dynamodb:PutItem"]) if s["Sid"].startswith("S6") else s for s in good], False),
             ("none", None, False)]
    for name, stmts, want in cases:
        got, _ = check_policy(stmts)
        if got != want:
            print("R55-SELFTEST-FAIL %s" % name)
            return 1
    print("R55-SELFTEST-OK green plus three mutants refused")
    return 0


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--self-test":
        sys.exit(self_test())
    if len(sys.argv) != 2 or sys.argv[1] != "ap1":
        print("usage: r55_checks.py ap1 | --self-test")
        sys.exit(2)
    ok, why = main()
    print("R55-AP1-%s %s" % ("OK" if ok else "FAIL", why))
    sys.exit(0 if ok else 1)
