#!/usr/bin/env python3
"""Battery for .tools/portal-hooks/dev_push_payload_gate.py (NFRA_DEVPLN DP-f-1, S03 structural close).

Every case runs on temporary git repositories (a bare origin, a clone, DEV and PROD branches) in the system temp
directory; nothing under the real portal is written. The approval reader is a fixture command whose answer is a
JSON file the case writes. The last case pair drives the REAL .tools/portal-hooks/pre-push at its own path in this
worktree, with a pushed-ref line on stdin.

Run from the worktree root: python .tools/tests/test_dev_push_payload_gate.py
Last line: DEV-PUSH-GATE-TEST cases=<k>/<n> ok=True|False
"""

import json
import os
import shlex
import shutil
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CHECKER = os.path.join(REPO, ".tools", "portal-hooks", "dev_push_payload_gate.py")
PRE_PUSH = os.path.join(REPO, ".tools", "portal-hooks", "pre-push")
SERIAL = "0.9.0_WK_NFRA_DEVPLN~1"
ZERO = "0" * 40
ROW = "laptop-20261013T200117Z-9e8a"

_ENV = {k: v for k, v in os.environ.items() if k not in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE")}
_ENV.update({"GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t", "GIT_COMMITTER_NAME": "t",
             "GIT_COMMITTER_EMAIL": "t@t"})

RESULTS = []   # (name, ok, detail)


def git(cwd, *args):
    got = subprocess.run(["git", "-c", "core.autocrlf=false", "-c", "commit.gpgsign=false"] + list(args), cwd=cwd,
                         capture_output=True, text=True, encoding="utf-8", errors="replace", env=_ENV)
    if got.returncode != 0:
        raise RuntimeError("git %s rc=%d: %s" % (" ".join(args), got.returncode, got.stderr.strip()[:300]))
    return got.stdout.strip()


def write_commit(clone, files, msg):
    for path, text in files.items():
        full = os.path.join(clone, path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as fh:
            fh.write(text)
        git(clone, "add", "--", path)
    git(clone, "commit", "-q", "-m", msg)
    return git(clone, "rev-parse", "HEAD")


def fresh_repos(root):
    """A bare origin and a clone. main, PROD and DEV all point at one base commit; PROD and DEV are pushed."""
    origin = os.path.join(root, "origin.git")
    clone = os.path.join(root, "clone")
    git(root, "init", "-q", "--bare", origin)
    git(root, "clone", "-q", origin, clone)
    git(clone, "checkout", "-q", "-b", "main")
    base = write_commit(clone, {"src/app.txt": "base\n"}, "base")
    git(clone, "branch", "PROD", base)
    git(clone, "branch", "DEV", base)
    git(clone, "push", "-q", "origin", "main", "PROD", "DEV")
    git(clone, "checkout", "-q", "DEV")
    return clone, base


def feature_branch(clone, base, name, files):
    """A feature commit on a side branch off base; returns its head sha. DEV is left checked out."""
    git(clone, "checkout", "-q", "-b", name, base)
    head = write_commit(clone, files, "feature work on " + name)
    git(clone, "checkout", "-q", "DEV")
    return head


def approved_merge(clone, branch, head, row):
    """DEV gets a --no-ff merge of `branch` carrying the Feature and Approved-By trailers; returns the merge sha."""
    git(clone, "merge", "-q", "--no-ff", "-m", "Merge %s into DEV (approved feature)" % branch,
        "-m", "Feature: %s\nApproved-By: 1.0.0_SA_CTO @%s" % (branch, row), branch)
    return git(clone, "rev-parse", "HEAD")


class Fixture:
    """The approval reader stand-in: a command whose answer is the JSON file at self.path."""

    def __init__(self, root):
        self.path = os.path.join(root, "fixture.json")
        script = os.path.join(root, "approval_fixture.py")
        with open(script, "w", encoding="utf-8") as fh:
            fh.write(
                "import json, os, sys\n"
                "doc = json.load(open(os.environ['DPG_FIXTURE_JSON'], encoding='utf-8'))\n"
                "branch = sys.argv[sys.argv.index('--branch') + 1] if '--branch' in sys.argv else '?'\n"
                "if doc.get('mode') == 'unreadable':\n"
                "    print('APPROVAL branch=%s state=UNREADABLE valid=- row=- by=- head_sha=- commits=- class=- "
                "box=- pages=- why=fixture' % branch)\n"
                "    sys.exit(2)\n"
                "if doc.get('mode') == 'garbage':\n"
                "    print('no approval line here')\n"
                "    sys.exit(0)\n"
                "print('APPROVAL branch=%s state=%s valid=%s row=%s by=1.0.0_SA_CTO head_sha=%s commits=1 "
                "class=opal-internal box=laptop pages=-' % (branch, doc['state'], doc['valid'], doc['row'], "
                "doc['head_sha']))\n"
                "sys.exit(0)\n")
        self.command = " ".join(shlex.quote(p) for p in [sys.executable, script, "approval-status"])

    def set(self, **doc):
        with open(self.path, "w", encoding="utf-8") as fh:
            json.dump(doc, fh)


def approved_doc(head, row=ROW):
    return {"mode": "line", "state": "APPROVED", "valid": "yes", "row": row, "head_sha": head}


def env_for(case_root, fixture, serial=SERIAL):
    env = dict(_ENV)
    env["OPAL_AGENT_SERIAL"] = serial
    env["OPAL_APPROVAL_STATUS_CMD"] = fixture.command
    env["DPG_FIXTURE_JSON"] = fixture.path
    env["DRIVE_MODE_DIR"] = os.path.join(case_root, "leases")   # created only by the lease scenarios
    return env


def run_checker(clone, env, local, remote, ref="refs/heads/DEV"):
    got = subprocess.run([sys.executable, CHECKER, "--portal", clone, "--local-sha", local, "--remote-sha", remote,
                          "--remote-ref", ref], capture_output=True, text=True, encoding="utf-8", errors="replace",
                         env=env, timeout=110, stdin=subprocess.DEVNULL)
    return got.returncode, got.stdout


def last_line(out):
    lines = [ln for ln in out.splitlines() if ln.strip()]
    return lines[-1] if lines else ""


def find_bash():
    git_path = shutil.which("git")
    if git_path:
        cand = os.path.join(os.path.dirname(os.path.dirname(git_path)), "bin", "bash.exe")
        if os.path.isfile(cand):
            return cand
    return shutil.which("bash")


def check(name, cond, detail=""):
    RESULTS.append((name, bool(cond), detail))
    print("%s %s%s" % ("ok  " if cond else "FAIL", name, "" if cond else " :: " + detail))


def expect_checker(name, root, fixture, want_rc, want_result, setup, serial=SERIAL, ref="refs/heads/DEV"):
    """One checker case: setup(clone) returns (local, remote); the checker's last line must name the result."""
    case_root = tempfile.mkdtemp(prefix="case-", dir=root)
    clone, base = fresh_repos(case_root)
    local, remote = setup(clone, base, case_root, fixture)
    env = env_for(case_root, fixture, serial=serial)
    rc, out = run_checker(clone, env, local, remote, ref=ref)
    tail = last_line(out)
    ok = rc == want_rc and ("DEV-PUSH-GATE result=%s" % want_result) in tail
    check(name, ok, "rc=%d want=%d last=%r" % (rc, want_rc, tail))


def scenario_route_a(row=ROW, head_of="feature", state="APPROVED", valid="yes", mode="line"):
    def setup(clone, base, case_root, fixture):
        head = feature_branch(clone, base, "cand/laptop/t1", {"portal/x.md": "feature\n"})
        merge = approved_merge(clone, "cand/laptop/t1", head, ROW)
        second = git(clone, "rev-parse", merge + "^2")
        first = git(clone, "rev-parse", merge + "^1")
        doc = approved_doc(second, row=row)
        doc["state"], doc["valid"] = state, valid
        if head_of == "first":
            doc["head_sha"] = first
        doc["mode"] = mode
        fixture.set(**doc)
        return merge, base
    return setup


def scenario_plain(clone, base, case_root, fixture):
    local = write_commit(clone, {"portal/docs.md": "plain change\n"}, "plain docs change")
    return local, base


def scenario_test_only(clone, base, case_root, fixture):
    local = write_commit(clone, {"src/lib/__tests__/foo.ts": "x\n", "e2e/a.spec.ts": "y\n"}, "test only change")
    return local, base


def scenario_back_merge(clone, base, case_root, fixture):
    git(clone, "checkout", "-q", "PROD")
    write_commit(clone, {"portal/prod-only.md": "prod\n"}, "prod-only change")
    git(clone, "push", "-q", "origin", "PROD")
    git(clone, "checkout", "-q", "DEV")
    git(clone, "merge", "-q", "--no-ff", "-m", "Merge PROD into DEV (settlement back-merge)", "origin/PROD")
    return git(clone, "rev-parse", "HEAD"), base


def scenario_delete(clone, base, case_root, fixture):
    return ZERO, base


def scenario_new_ref(clone, base, case_root, fixture):
    local = write_commit(clone, {"portal/n.md": "n\n"}, "plain change")
    return local, ZERO


def scenario_non_ff(clone, base, case_root, fixture):
    side = feature_branch(clone, base, "side", {"portal/side.md": "side\n"})
    local = write_commit(clone, {"portal/y.md": "y\n"}, "plain change on base")
    return local, side


def scenario_plain_fast_lease(lease_doc_fn):
    def setup(clone, base, case_root, fixture):
        local = write_commit(clone, {"portal/fl.md": "fl\n"}, "plain change under a lease")
        lease_dir = os.path.join(case_root, "leases")
        os.makedirs(lease_dir, exist_ok=True)
        with open(os.path.join(lease_dir, "NFRA_DEVPLN.json"), "w", encoding="utf-8") as fh:
            fh.write(lease_doc_fn())
        return local, base
    return setup


def _lease(seat, mode, expires):
    return json.dumps({"code": "NFRA_DEVPLN", "mode": mode, "seat": seat, "expires_epoch": expires})


def run_hook_case(name, root, fixture, want_rc, want_text, setup):
    case_root = tempfile.mkdtemp(prefix="hook-", dir=root)
    clone, base = fresh_repos(case_root)
    local, remote = setup(clone, base, case_root, fixture)
    bash = find_bash()
    env = env_for(case_root, fixture)
    stdin = "refs/heads/DEV %s refs/heads/DEV %s\n" % (local, remote)
    # bytes, not text: git writes LF on stdin; text mode on Windows would write CRLF and corrupt the sha fields
    got = subprocess.run([bash, PRE_PUSH.replace("\\", "/")], cwd=clone, input=stdin.encode("utf-8"),
                         capture_output=True, env=env, timeout=300)
    text = (got.stdout + got.stderr).decode("utf-8", errors="replace")
    ok = got.returncode == want_rc and want_text in text
    check(name, ok, "rc=%d want=%d text-hit=%s tail=%r" % (got.returncode, want_rc, want_text in text,
                                                           text.strip()[-300:]))


def main():
    root = tempfile.mkdtemp(prefix="dpg-test-")
    fixture = Fixture(root)
    try:
        now = int(time.time())
        expect_checker("routeA admitted (approved row, head = second parent)", root, fixture, 0, "ADMITTED",
                       scenario_route_a())
        expect_checker("routeA refused: different row", root, fixture, 1, "REFUSED",
                       scenario_route_a(row="other-row-0000"))
        expect_checker("routeA refused: head is the first parent, not the second", root, fixture, 1, "REFUSED",
                       scenario_route_a(head_of="first"))
        expect_checker("routeA refused: state OPEN", root, fixture, 1, "REFUSED",
                       scenario_route_a(state="OPEN", valid="-"))
        expect_checker("routeA refused: reader unreadable (rc 2)", root, fixture, 1, "REFUSED",
                       scenario_route_a(mode="unreadable"))
        expect_checker("routeA refused: reader output unparsable", root, fixture, 1, "REFUSED",
                       scenario_route_a(mode="garbage"))
        expect_checker("plain commit refused", root, fixture, 1, "REFUSED", scenario_plain)
        expect_checker("test-only commit admitted (route B)", root, fixture, 0, "ADMITTED", scenario_test_only)
        expect_checker("PROD-into-DEV back-merge admitted (route C)", root, fixture, 0, "ADMITTED",
                       scenario_back_merge)
        expect_checker("non-DEV ref skipped", root, fixture, 0, "SKIPPED", scenario_plain,
                       ref="refs/heads/PROD")
        expect_checker("delete refused", root, fixture, 1, "REFUSED", scenario_delete)
        expect_checker("new ref refused", root, fixture, 1, "REFUSED", scenario_new_ref)
        expect_checker("non-fast-forward refused", root, fixture, 1, "REFUSED", scenario_non_ff)
        expect_checker("live FAST lease for the serial admitted", root, fixture, 0, "ADMITTED",
                       scenario_plain_fast_lease(lambda: _lease(SERIAL, "FAST", now + 3600)))
        expect_checker("expired FAST lease admits nothing", root, fixture, 1, "REFUSED",
                       scenario_plain_fast_lease(lambda: _lease(SERIAL, "FAST", now - 60)))
        expect_checker("FAST lease for another seat admits nothing", root, fixture, 1, "REFUSED",
                       scenario_plain_fast_lease(lambda: _lease("0.9.0_WK_OTHER~1", "FAST", now + 3600)))
        expect_checker("unreadable lease file admits nothing", root, fixture, 1, "REFUSED",
                       scenario_plain_fast_lease(lambda: "{not json"))
        run_hook_case("real pre-push admits an approved DEV push", root, fixture, 0,
                      "DEV-PUSH-GATE result=ADMITTED", scenario_route_a())
        run_hook_case("real pre-push refuses a plain commit onto DEV", root, fixture, 1,
                      "ERROR: portal DEV is written only through .tools/portal-merge-forward.sh",
                      scenario_plain)
    finally:
        shutil.rmtree(root, ignore_errors=True)
    k = sum(1 for _n, ok, _d in RESULTS if ok)
    n = len(RESULTS)
    print("DEV-PUSH-GATE-TEST cases=%d/%d ok=%s" % (k, n, k == n))
    return 0 if k == n else 1


if __name__ == "__main__":
    sys.exit(main())
