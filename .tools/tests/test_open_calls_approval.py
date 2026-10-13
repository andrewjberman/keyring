#!/usr/bin/env python3
"""test_open_calls_approval.py -- the `approval` kind of .tools/open-calls.py (NFRA_DEVPLN round 1, cell DP-b-1).

Runs the tool as a subprocess against a TEMPORARY state root (OPAL_STATE_ROOT). The tool never puts to the cluster copy
when OPAL_STATE_ROOT is set, and OPAL_OPENCALLS_CLOUD=0 is set as well. The real org/devices/state lists are never written.
The measurement (`scope`) reads the real repository read-only, as the tool always does.

Last line: OPEN-CALLS-APPROVAL-TEST cases=<k>/<n> ok=<True|False>
"""
import json
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TOOL = os.path.join(ROOT, ".tools", "open-calls.py")
BOX = "laptop"
SERIAL = "0.9.0_WK_NFRA_DEVPLN~1"
CTO = "1.0.0_SA_CTO"
PRD = "org/missions/D0/NFRA/NFRA_DEVPLN/prd/NFRA_DEVPLN_PRD.md"
CONTEXT = "Created by the approval-kind test; gates the portal merge-forward cell under test here."


class Env:
    """A temporary state root and ruling file. Every file this run creates is removed by name, then the directories."""

    def __init__(self):
        self.base = tempfile.mkdtemp(prefix="opalcalls_approval_")
        self.state = os.path.join(self.base, "state")
        self.box_dir = os.path.join(self.state, BOX)
        self.list = os.path.join(self.box_dir, "open_calls.json")
        self.ruling = os.path.join(self.base, "RULING.md")
        self.files, self.dirs = [], [self.box_dir, self.state, self.base]
        self.write(self.ruling, "ruling for the approval-kind test\n")

    def write(self, path, text):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        if path not in self.files:
            self.files.append(path)
        return path

    def cleanup(self):
        for f in self.files + [self.list, self.list + ".tmp"]:
            try:
                os.remove(f)
            except OSError:
                pass
        for d in self.dirs:
            try:
                os.rmdir(d)
            except OSError:
                pass


def run(env, args, serial=SERIAL):
    """(rc, stdout, stderr) of one tool call; the serial is what OPAL_AGENT_SERIAL holds for that call."""
    e = dict(os.environ)
    e.update({"OPAL_STATE_ROOT": env.state, "OPAL_OPENCALLS_CLOUD": "0", "AGENTBUS_DEVICE": BOX, "OPAL_AGENT_SERIAL": serial})
    try:
        p = subprocess.run([sys.executable, TOOL] + args, cwd=ROOT, env=e, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=120)
    except subprocess.TimeoutExpired:
        return 124, "", "TIMEOUT"
    return p.returncode, p.stdout, p.stderr


def rows(env):
    if not os.path.exists(env.list):
        return []
    with open(env.list, encoding="utf-8") as fh:
        return json.load(fh)["rows"]


def row_for(env, branch):
    hits = [r for r in rows(env) if r.get("kind") == "approval" and r["approval"]["branch"] == branch]
    return hits[-1] if hits else None


def add_approval(env, branch, klass, serial=SERIAL):
    return run(env, ["add", "--kind", "approval", "--project", "NFRA_DEVPLN", "--box", BOX, "--branch", branch,
                     "--purpose", "test feature for the approval kind", "--pages", "portal/a.tsx,portal/b.tsx",
                     "--class", klass, "--how", "open the page and look at it"], serial)


def close_approval(env, cid, ruled_by, decision, serial=SERIAL):
    return run(env, ["close", "--id", cid, "--ruled-by", ruled_by, "--ruling-file", env.ruling, "--decision", decision], serial)


def status(env, branch, store=None):
    rc, out, _err = run(env, ["approval-status", "--branch", branch, "--store-dir", store or env.state])
    return rc, out.strip()


def main():
    env = Env()
    cases = []

    def check(label, ok):
        cases.append((label, bool(ok)))

    try:
        # 1. add makes an OPEN approval row; head_sha and commits are null (DP-b-5 computes them)
        rc, out, _err = add_approval(env, "cand/laptop/t-cf", "client-facing")
        r = row_for(env, "cand/laptop/t-cf")
        check("add makes an OPEN approval row (head_sha and commits null, pages split)",
              rc == 0 and "kind=approval" in out and r is not None and r["state"] == "OPEN"
              and r["approval"]["head_sha"] is None and r["approval"]["commits"] is None
              and r["approval"]["pages"] == ["portal/a.tsx", "portal/b.tsx"] and r["approval"]["class"] == "client-facing"
              and r["subject"] == "approval: cand/laptop/t-cf")
        cid = r["id"] if r else "none"

        # 2. close approved by andrew on a client-facing row reads APPROVED valid=yes
        rc, _out, _err = close_approval(env, cid, "andrew", "approved", serial=CTO)
        rc2, line = status(env, "cand/laptop/t-cf")
        r = row_for(env, "cand/laptop/t-cf")
        check("close approved by andrew on a client-facing row reads APPROVED valid=yes",
              rc == 0 and rc2 == 0 and "state=APPROVED valid=yes" in line and r["closed"]["decision"] == "approved"
              and r["closed"]["by"] == "andrew" and r["closed"]["ruled_by"] == "andrew")

        # 3. a CTO serial closing a client-facing row: recorded, but not valid for the merge
        add_approval(env, "cand/laptop/t-cto", "client-facing")
        cid = row_for(env, "cand/laptop/t-cto")["id"]
        rc, _out, _err = close_approval(env, cid, "cto", "approved", serial=CTO)
        rc2, line = status(env, "cand/laptop/t-cto")
        check("close approved by a CTO serial on a client-facing row reads valid=no",
              rc == 0 and rc2 == 0 and "state=APPROVED valid=no" in line and row_for(env, "cand/laptop/t-cto")["closed"]["by"] == CTO)

        # 4. the same CTO close on an opal-internal row reads valid=yes
        add_approval(env, "cand/laptop/t-oi", "opal-internal")
        cid = row_for(env, "cand/laptop/t-oi")["id"]
        close_approval(env, cid, "cto", "approved", serial=CTO)
        rc2, line = status(env, "cand/laptop/t-oi")
        check("the same CTO close on an opal-internal row reads APPROVED valid=yes", rc2 == 0 and "state=APPROVED valid=yes" in line)

        # 5. close declined reads DECLINED valid=no and writes no approval
        add_approval(env, "cand/laptop/t-dec", "client-facing")
        cid = row_for(env, "cand/laptop/t-dec")["id"]
        close_approval(env, cid, "andrew", "declined")
        rc2, line = status(env, "cand/laptop/t-dec")
        check("close declined reads DECLINED valid=no", rc2 == 0 and "state=DECLINED valid=no" in line)

        # 6. a test-only row accepts any APPROVED
        add_approval(env, "cand/laptop/t-to", "test-only")
        cid = row_for(env, "cand/laptop/t-to")["id"]
        close_approval(env, cid, "cto", "approved", serial=CTO)
        rc2, line = status(env, "cand/laptop/t-to")
        check("a test-only approval by a CTO serial reads APPROVED valid=yes", rc2 == 0 and "state=APPROVED valid=yes" in line)

        # 7. a branch with no row reads ABSENT, rc 0
        rc2, line = status(env, "cand/laptop/none-9")
        check("a branch with no row reads ABSENT (rc 0)",
              rc2 == 0 and line.startswith("APPROVAL branch=cand/laptop/none-9 state=ABSENT valid=-"))

        # 8. an unreadable store exits rc 2 and never prints ABSENT
        bad = os.path.join(env.base, "bad")
        env.write(os.path.join(bad, BOX, "open_calls.json"), "{not json")
        rc_bad, line_bad = status(env, "cand/laptop/t-cf", store=bad)
        rc_none, line_none = status(env, "cand/laptop/t-cf", store=os.path.join(env.base, "no-such-dir"))
        check("unreadable JSON and a missing store exit rc 2 as UNREADABLE, never ABSENT",
              rc_bad == 2 and "state=UNREADABLE" in line_bad and "state=ABSENT" not in line_bad
              and rc_none == 2 and "state=UNREADABLE" in line_none and "state=ABSENT" not in line_none)

        # 9. a bad class and a bad branch name are refused naming the field, rc 2, with nothing written
        before = len(rows(env))
        rc_c, _o, err_c = add_approval(env, "cand/laptop/x-cls", "secret")
        rc_b, _o, err_b = run(env, ["add", "--kind", "approval", "--project", "NFRA_DEVPLN", "--box", BOX,
                                    "--branch", "cand/laptop", "--purpose", "p", "--pages", "a", "--class", "test-only",
                                    "--how", "h"])
        rc_m, _o, err_m = run(env, ["add", "--kind", "approval", "--project", "NFRA_DEVPLN", "--box", BOX,
                                    "--branch", "cand/dell1/x1", "--purpose", "p", "--pages", "a", "--class", "test-only",
                                    "--how", "h"])
        check("a bad class, a bad branch and a branch of another box are refused (rc 2, field named, nothing written)",
              rc_c == 2 and "--class" in err_c and rc_b == 2 and "--branch" in err_b and rc_m == 2 and "--branch" in err_m
              and len(rows(env)) == before)

        # 10. the decision: required on an approval row, refused on any other kind; CTO close needs OPAL_AGENT_SERIAL
        add_approval(env, "cand/laptop/t-nd", "test-only")
        nd = row_for(env, "cand/laptop/t-nd")["id"]
        rc_nd, _o, _e = run(env, ["close", "--id", nd, "--ruled-by", "andrew", "--ruling-file", env.ruling])
        rc_unset, _o, _e = close_approval(env, nd, "cto", "approved", serial="")
        still_open = row_for(env, "cand/laptop/t-nd")["state"] == "OPEN"
        rc_f, _o, err_f = run(env, ["add", "--project", "NONE", "--subject", "a fork for the refusal test", "--asked-by", SERIAL,
                                    "--source", PRD, "--context", CONTEXT, "--rec", "(a) because the test says so"])
        fork_id = [r["id"] for r in rows(env) if r.get("kind", "fork") == "fork"][-1]
        rc_fd, _o, err_fd = run(env, ["close", "--id", fork_id, "--by", "andrew", "--ruling-file", env.ruling,
                                      "--decision", "approved"])
        check("an approval close needs --decision and a CTO close needs OPAL_AGENT_SERIAL; --decision on a fork is refused",
              rc_nd == 1 and rc_unset == 1 and still_open and rc_f == 0 and rc_fd == 1 and "REFUSED" in err_fd)

        # 11. a fork add and a fork close behave as before: kind fork, closed keeps the old key set (no decision)
        fork_row = [r for r in rows(env) if r["id"] == fork_id][0]
        rc_c2, _o, _e = run(env, ["close", "--id", fork_id, "--by", "andrew", "--ruling-file", env.ruling])
        closed_fork = [r for r in rows(env) if r["id"] == fork_id][0]
        check("a fork add and a fork close behave as before (kind fork, no decision key on the closure)",
              rc_f == 0 and fork_row["kind"] == "fork" and rc_c2 == 0 and closed_fork["state"] == "CLOSED"
              and "decision" not in closed_fork["closed"] and closed_fork["closed"]["by"] == "andrew")

        # 12. a row without a kind key reads as a fork in the listing
        doc = json.load(open(env.list, encoding="utf-8"))
        legacy = dict(doc["rows"][0], id="legacy-row-0001", state="OPEN", closed=None)
        legacy.pop("kind", None)
        legacy.pop("approval", None)
        doc["rows"].append(legacy)
        env.write(env.list, json.dumps(doc, indent=1) + "\n")
        rc_l, out_l, _e = run(env, ["list", "--device", BOX])
        check("a row without a kind key lists as a fork (as before)",
              rc_l == 0 and "legacy-row-0001 [OPEN] fork" in out_l)

        # 13. a fork add without --context is refused rc 2, naming the field
        rc_nc, _o, err_nc = run(env, ["add", "--project", "NONE", "--subject", "s", "--asked-by", SERIAL, "--source", PRD,
                                      "--rec", "(a) x"])
        check("a fork add without --context is refused rc 2 naming --context", rc_nc == 2 and "--context" in err_nc)
    finally:
        env.cleanup()

    fails = 0
    for label, ok in cases:
        print("  %s  %s" % ("PASS" if ok else "FAIL", label))
        fails += 0 if ok else 1
    print("OPEN-CALLS-APPROVAL-TEST cases=%d/%d ok=%s" % (len(cases) - fails, len(cases), fails == 0))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
