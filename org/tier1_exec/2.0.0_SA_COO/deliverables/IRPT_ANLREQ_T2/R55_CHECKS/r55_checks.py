"""IRPT_ANLREQ round 55, workstream T -- the issuer's LIVE read-only check of the commentary hop's FWD-4 release (2.0.0_SA_COO~T2).

  ap1  R55-AP1  the release is applied: the draft-store role's inline policy carries S6 and S7 (and S6 allows exactly dynamodb:UpdateItem),
                the draft-store Lambda no longer runs the pre-act digest cwf6bUEb, and the commentary function runs a digest that is neither
                the pre-act hUZY39qN nor the pull functions' (which still run hUZY39qN: the surgical zip reached the commentary function only).

  hoplog     R55-HOPLOG   the driven refusal (TO-APPLY-t55 leg A): the commentary function's log group holds the line
                `HOP-FAILURE-REPORTED request_id=REQ-d47252fe74634d0c5cdd8067 hop=COMMENTARY code=COMMENTARY_DRAFT_REFUSED written=true`
  hoplog2    R55-HOPLOG2  the SECOND driven refusal (TO-APPLY-t56 leg A): the same line is now in the log twice (t55's event stays; t56 adds one)
  hopabsent  R55-HOPABSENT the synthetic job row REQ-d47252fe74634d0c5cdd8067 (tenant 49financial) carries NO hop_failure (the restored state; a control that passes at the base and after leg B)

Read-only: one policy read and three configuration reads (ap1), one log filter (hoplog), one get-item (hopabsent). Prints R55-<ARM>-OK or -FAIL <reason>.
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


ROW_KEY = '{"tenant":{"S":"49financial"},"job":{"S":"REQ-d47252fe74634d0c5cdd8067"}}'
HOP_LOG_GROUP = "/aws/lambda/outlook-global-commentary-draft-lambda"
HOP_LINE = "HOP-FAILURE-REPORTED request_id=REQ-d47252fe74634d0c5cdd8067 hop=COMMENTARY code=COMMENTARY_DRAFT_REFUSED written=true"


def hoplog(need=1):
    rc, so, _ = aws("logs", "filter-log-events", "--log-group-name", HOP_LOG_GROUP, "--filter-pattern", '"%s"' % HOP_LINE, "--output", "json")
    if rc != 0:
        return False, "log read failed rc=%d" % rc
    try:
        n = len(json.loads(so).get("events") or [])
    except ValueError:
        return False, "log read unparseable"
    return (n >= need), "events_with_line=%d need=%d" % (n, need)


def hopabsent():
    import os
    import tempfile
    # the key JSON goes by file and the queries are plain paths: braces and quotes in an argv entry do not survive the bash shim here
    fd, path = tempfile.mkstemp(suffix=".json")
    try:
        with os.fdopen(fd, "w", encoding="ascii") as fh:
            fh.write(ROW_KEY)
        key = "file://" + path.replace("\\", "/")
        rc1, exists, _ = aws("dynamodb", "get-item", "--table-name", "irpt-jobs", "--key", key, "--consistent-read",
                             "--query", "Item.job.S", "--output", "text")
        rc2, hop, _ = aws("dynamodb", "get-item", "--table-name", "irpt-jobs", "--key", key, "--consistent-read",
                          "--query", "Item.hop_failure", "--output", "json")
    finally:
        os.unlink(path)
    if rc1 != 0 or rc2 != 0:
        return False, "row read failed rc=%d,%d" % (rc1, rc2)
    if not exists.strip() or exists.strip() == "None":
        return False, "the synthetic job row does not exist"
    if hop.strip() not in ("null", "None", ""):
        return False, "the row carries a hop_failure"
    return True, "row exists, hop_failure absent"


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
    arms = {"ap1": ("AP1", main), "hoplog": ("HOPLOG", hoplog), "hoplog2": ("HOPLOG2", lambda: hoplog(2)), "hopabsent": ("HOPABSENT", hopabsent)}
    if len(sys.argv) != 2 or sys.argv[1] not in arms:
        print("usage: r55_checks.py ap1|hoplog|hoplog2|hopabsent | --self-test")
        sys.exit(2)
    name, fn = arms[sys.argv[1]]
    ok, why = fn()
    print("R55-%s-%s %s" % (name, "OK" if ok else "FAIL", why))
    sys.exit(0 if ok else 1)
