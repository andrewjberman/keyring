#!/usr/bin/env python3
"""DEV payload limb for the portal pre-push hook (NFRA_DEVPLN DP-f-1, S03 structural close).

Portal DEV is written only through .tools/portal-merge-forward.sh. This checker runs from git's own pre-push
limb (.tools/portal-hooks/pre-push), so it sees every push, typed or scripted, and admits a commit only when
one route passes:

  ROUTE A  an approved feature: two parents; the body carries Feature: <branch> and Approved-By: <who> @<row>;
           the approval reader says APPROVED valid=yes for <branch>, the same row, and head_sha = the second parent.
  ROUTE B  test-only: every path the commit changes against its first parent is a test path (CLAUDE.md law).
  ROUTE C  PROD-into-DEV back-merge (settlement rule): two parents; the second parent is an ancestor of --prod-ref.

A live FAST lease held by $OPAL_AGENT_SERIAL admits the whole push (CLAUDE.md law). Any other ref is skipped.

Usage: dev_push_payload_gate.py --local-sha <sha> --remote-sha <sha> --remote-ref <ref>
                                [--portal <repo path, default .>] [--prod-ref origin/PROD]
Last line: DEV-PUSH-GATE result=ADMITTED|REFUSED|SKIPPED reason=<token|-> commits=<n>
Exit 0 for ADMITTED and SKIPPED, 1 for REFUSED. Python standard library only.
"""

import argparse
import json
import os
import re
import shlex
import subprocess
import sys
import time

ZERO = "0" * 40
DEV_REF = "refs/heads/DEV"
HERE = os.path.dirname(os.path.abspath(__file__))
WORKSPACE = os.path.dirname(os.path.dirname(HERE))

TEST_ONLY_RE = re.compile(
    r"(^|/)(__tests__|__harness__|__fixtures__|__mocks__)/"
    r"|\.(test|spec)\.[cm]?[jt]sx?$"
    r"|(^|/)(tests?|e2e|fixtures?)/"
)
FEATURE_RE = re.compile(r"^Feature:[ \t]*(\S+)[ \t]*$", re.M)
APPROVED_BY_RE = re.compile(r"^Approved-By:[ \t]*(.+?)[ \t]+@(\S+)[ \t]*$", re.M)
FIELD_RE = {
    "state": re.compile(r"(?:^|\s)state=(\S+)"),
    "valid": re.compile(r"(?:^|\s)valid=(\S+)"),
    "row": re.compile(r"(?:^|\s)row=(\S+)"),
    "head_sha": re.compile(r"(?:^|\s)head_sha=(\S+)"),
}


def _git_env():
    env = dict(os.environ)
    for key in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE"):
        env.pop(key, None)   # hook-provided GIT_DIR is relative to the hook's cwd; the checker works from --portal
    return env


def git(portal, *args):
    return subprocess.run(["git", "-C", portal] + list(args), capture_output=True, text=True,
                          encoding="utf-8", errors="replace", env=_git_env())


def is_ancestor(portal, anc, desc):
    """0 yes, 1 no, other = the history could not be read."""
    return git(portal, "merge-base", "--is-ancestor", anc, desc).returncode


def reader_argv():
    cmd = os.environ.get("OPAL_APPROVAL_STATUS_CMD", "").strip()
    if cmd:
        return shlex.split(cmd, posix=True)
    return [sys.executable, os.path.normpath(os.path.join(HERE, "..", "open-calls.py")), "approval-status"]


def approved(argv, branch, row, head):
    """(ok, why). Fail closed: a reader that cannot run, exits non-zero, or prints no APPROVAL line is not approved."""
    try:
        got = subprocess.run(argv + ["--branch", branch], capture_output=True, text=True, encoding="utf-8",
                             errors="replace", timeout=110, stdin=subprocess.DEVNULL)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return False, "approval reader did not run (%s)" % type(exc).__name__
    line = next((ln for ln in got.stdout.splitlines() if ln.startswith("APPROVAL ")), None)
    if line is None:
        return False, "approval reader output unparsable (rc %d)" % got.returncode
    fields = {}
    for key, rx in FIELD_RE.items():
        hit = rx.search(line)
        fields[key] = hit.group(1) if hit else ""
    if got.returncode != 0 or not fields["state"]:
        return False, "approval reader rc %d, state=%s" % (got.returncode, fields["state"] or "-")
    if fields["state"] != "APPROVED" or fields["valid"] != "yes":
        return False, "approval state=%s valid=%s" % (fields["state"], fields["valid"] or "-")
    if fields["row"] != row:
        return False, "approval row %s is not the trailer row %s" % (fields["row"], row)
    if fields["head_sha"].lower() != head.lower():
        return False, "approval head_sha %s is not the second parent %s" % (fields["head_sha"], head[:10])
    return True, ""


def changed_paths(portal, parents, commit):
    if parents:
        got = git(portal, "diff-tree", "-r", "-z", "--name-only", "--no-renames", parents[0], commit)
    else:
        got = git(portal, "diff-tree", "-r", "-z", "--root", "--name-only", "--no-renames", commit)
    if got.returncode != 0:
        return None
    return [p for p in got.stdout.split("\0") if p]


def route_for(portal, commit, parents, prod_ref, reader):
    """(route letter or None, [failure notes])."""
    notes = []
    body = git(portal, "log", "-1", "--format=%B", commit).stdout
    if len(parents) == 2:
        feat, appr = FEATURE_RE.search(body), APPROVED_BY_RE.search(body)
        if feat and appr:
            ok, why = approved(reader, feat.group(1), appr.group(2), parents[1])
            if ok:
                return "A", notes
            notes.append("route A: " + why)
        else:
            notes.append("route A: no Feature and Approved-By trailers")
    else:
        notes.append("route A: not a two-parent merge")
    paths = changed_paths(portal, parents, commit)
    if paths is None:
        notes.append("route B: changed paths unreadable")
    elif not paths:
        notes.append("route B: no changed paths")
    elif all(TEST_ONLY_RE.search(p) for p in paths):
        return "B", notes
    else:
        notes.append("route B: changes non-test paths")
    if len(parents) == 2:
        if is_ancestor(portal, parents[1], prod_ref) == 0:
            return "C", notes
        notes.append("route C: second parent is not an ancestor of %s" % prod_ref)
    else:
        notes.append("route C: not a two-parent merge")
    return None, notes


def fast_lease(serial, lease_dir, now):
    """Path of a live FAST lease held by `serial`, else None. Absent, expired or unreadable admits nothing."""
    if not serial or not os.path.isdir(lease_dir):
        return None
    try:
        names = sorted(os.listdir(lease_dir))
    except OSError:
        return None
    for name in names:
        if not name.endswith(".json"):
            continue
        path = os.path.join(lease_dir, name)
        try:
            with open(path, encoding="utf-8") as fh:
                doc = json.load(fh)
            if not isinstance(doc, dict) or doc.get("seat") != serial or doc.get("mode") != "FAST":
                continue
            if int(doc.get("expires_epoch")) > now:
                return path
        except (OSError, ValueError, TypeError):
            continue
    return None


def decide(args):
    """(result, reason, commits, lines)."""
    portal, local, remote, ref = args.portal, args.local_sha, args.remote_sha, args.remote_ref
    if ref != DEV_REF:
        return "SKIPPED", "not-dev", "-", []
    if local == ZERO:
        return "REFUSED", "delete", "-", ["REFUSED: deleting %s is not a DEV push" % DEV_REF]
    if remote == ZERO:
        return "REFUSED", "new-ref", "-", ["REFUSED: %s does not exist on the remote yet" % DEV_REF]
    anc = is_ancestor(portal, remote, local)
    if anc == 1:
        return "REFUSED", "not-fast-forward", "-", [
            "REFUSED: remote %s is not an ancestor of %s" % (remote[:10], local[:10])]
    if anc != 0:
        return "REFUSED", "unreadable-history", "-", [
            "REFUSED: could not read history between %s and %s" % (remote[:10], local[:10])]
    lease_dir = os.environ.get("DRIVE_MODE_DIR", "").strip() or os.path.join(WORKSPACE, "org", "mcp", "drive_mode")
    lease = fast_lease(os.environ.get("OPAL_AGENT_SERIAL", "").strip(), lease_dir, int(time.time()))
    if lease:
        return "ADMITTED", "fast-lease", "-", ["LEASE: live FAST lease %s" % lease]
    walk = git(portal, "rev-list", "--first-parent", "--reverse", "%s..%s" % (remote, local))
    if walk.returncode != 0:
        return "REFUSED", "unreadable-history", "-", ["REFUSED: rev-list failed: %s" % walk.stderr.strip()[:200]]
    commits = walk.stdout.split()
    if not commits:
        return "ADMITTED", "no-new-commits", 0, []
    reader = reader_argv()
    lines, refused = [], 0
    for commit in commits:
        parents = git(portal, "rev-list", "--parents", "-n", "1", commit).stdout.split()[1:]
        subject = git(portal, "log", "-1", "--format=%s", commit).stdout.strip()
        route, notes = route_for(portal, commit, parents, args.prod_ref, reader)
        if route:
            lines.append("PASS %s route=%s %s" % (commit[:10], route, subject))
        else:
            refused += 1
            lines.append("UNAPPROVED %s %s :: %s" % (commit[:10], subject, "; ".join(notes)))
    if refused:
        return "REFUSED", "unapproved-commit", len(commits), lines
    return "ADMITTED", "-", len(commits), lines


def main(argv=None):
    ap = argparse.ArgumentParser(description="DEV payload limb (NFRA_DEVPLN DP-f-1)")
    ap.add_argument("--local-sha", required=True)
    ap.add_argument("--remote-sha", required=True)
    ap.add_argument("--remote-ref", required=True)
    ap.add_argument("--portal", default=".")
    ap.add_argument("--prod-ref", default="origin/PROD")
    args = ap.parse_args(argv)
    result, reason, commits, lines = decide(args)
    for line in lines:
        print(line)
    print("DEV-PUSH-GATE result=%s reason=%s commits=%s" % (result, reason, commits))
    return 1 if result == "REFUSED" else 0


if __name__ == "__main__":
    sys.exit(main())
