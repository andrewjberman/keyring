#!/usr/bin/env python3
"""portal-dev-approval-read.py -- FWD-4 per-commit read of portal DEV (NFRA_DEVPLN cell DP-c-1).

Usage:
  python .tools/portal-dev-approval-read.py [--portal portal] [--ref origin/DEV] [--since <sha>]
  python .tools/portal-dev-approval-read.py --selftest

Every git call is a read, run as `git -C <portal> ...`. Standard library only. No fetch, no push, no write.

The walk is `git rev-list --first-parent <since>..<ref>`, oldest first. A commit is APPROVED only when its
message body carries a line `Feature: <x>` AND a line `Approved-By: <who> @<row>`: the two trailers that
.tools/portal-merge-forward.sh writes onto the MERGE commit. Any other commit is UNAPPROVED.
The read reports; it does not gate: exit 0 whatever the unapproved count is. A refused read exits 3.
"""

import argparse
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile

# The settlement commit on portal (DEV = PROD there). Feature and approval trailers are read after it.
SETTLEMENT = "63c4f9e35f259ad76071b1099aeb9dddb150409f"

FEATURE_RE = re.compile(r"^Feature:[ \t]*(\S.*?)[ \t]*$")
APPROVED_RE = re.compile(r"^Approved-By:[ \t]*(\S.*?)[ \t]+@(\S+)[ \t]*$")
SUBJECT_MAX = 60
SELFTEST_CASES = 7


def git(portal, *args):
    """One read-only git call against the portal repo: returns (rc, decoded stdout)."""
    proc = subprocess.run(["git", "-C", portal] + list(args), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return proc.returncode, proc.stdout.decode("utf-8", "replace")


def ascii_only(text):
    """Fold line breaks and replace every non-ASCII character, so each printed line is one ASCII line."""
    flat = text.replace("\r", " ").replace("\n", " ").replace("\t", " ")
    return "".join(ch if ord(ch) < 128 else "?" for ch in flat)


def classify(message):
    """Return (state, feature, who, row). APPROVED needs both trailer lines; the first of each counts."""
    feature = None
    approver = None
    for raw in message.split("\n"):
        line = raw.rstrip("\r")
        if feature is None:
            hit = FEATURE_RE.match(line)
            if hit:
                feature = hit.group(1)
        if approver is None:
            hit = APPROVED_RE.match(line)
            if hit:
                approver = (hit.group(1), hit.group(2))
    if feature is not None and approver is not None:
        return "APPROVED", feature, approver[0], approver[1]
    return "UNAPPROVED", None, None, None


def resolve(portal, rev):
    """Full sha of a commit-ish, or None when it does not resolve."""
    rc, out = git(portal, "rev-parse", "--verify", "-q", rev + "^{commit}")
    if rc != 0:
        return None
    return out.strip()


def read_dev(portal, ref, since):
    """Return (rc, lines): the per-commit read of the first-parent commits since..ref, oldest first."""
    lines = []
    ref_sha = resolve(portal, ref)
    if ref_sha is None:
        lines.append("DEV-APPROVAL result=REFUSED reason=ref-not-found")
        return 3, lines
    since_sha = resolve(portal, since)
    if since_sha is None:
        lines.append("DEV-APPROVAL result=REFUSED reason=since-not-found")
        return 3, lines
    rc, _ = git(portal, "merge-base", "--is-ancestor", since_sha, ref_sha)
    if rc == 1:
        lines.append("DEV-APPROVAL result=REFUSED reason=since-not-ancestor")
        return 3, lines
    if rc != 0:
        lines.append("DEV-APPROVAL result=REFUSED reason=git-read-failed")
        return 3, lines
    span = since_sha + ".." + ref_sha
    rc, listed = git(portal, "rev-list", "--first-parent", "--reverse", span)
    rc2, counted = git(portal, "rev-list", "--first-parent", "--count", span)
    if rc != 0 or rc2 != 0 or not counted.strip().isdigit():
        lines.append("DEV-APPROVAL result=REFUSED reason=git-read-failed")
        return 3, lines
    shas = listed.split()
    total = len(shas)
    if total != int(counted.strip()):
        lines.append("DEV-APPROVAL result=REFUSED reason=count-mismatch")
        return 3, lines
    approved = 0
    unapproved = 0
    for sha in shas:
        rc, raw = git(portal, "log", "-1", "--format=%an%x00%B", sha)
        if rc != 0:
            lines.append("DEV-APPROVAL result=REFUSED reason=git-read-failed")
            return 3, lines
        author, _, message = raw.partition("\x00")
        state, feature, who, row = classify(message)
        if state == "APPROVED":
            approved += 1
            lines.append(ascii_only("DEV-COMMIT %s APPROVED feature=%s by=%s row=%s"
                                    % (sha[:8], feature, who, row)))
        else:
            unapproved += 1
            subject = message.split("\n", 1)[0].strip()[:SUBJECT_MAX]
            lines.append(ascii_only("DEV-COMMIT %s UNAPPROVED author=%s subject=%s"
                                    % (sha[:8], author.strip(), subject)))
    lines.append(ascii_only("DEV-APPROVAL since=%s ref=%s first_parent_commits=%d approved=%d unapproved=%d"
                            % (since_sha[:8], ref, total, approved, unapproved)))
    return 0, lines


# ---- selftest -------------------------------------------------------------------------------

def _run(args, env):
    proc = subprocess.run(args, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        raise RuntimeError("%s rc=%d: %s" % (" ".join(args[:3]), proc.returncode,
                                             proc.stderr.decode("utf-8", "replace").strip()))
    return proc.stdout.decode("utf-8", "replace").strip()


def _sgit(repo, env, *args):
    return _run(["git", "-C", repo] + list(args), env)


def _write(repo, name, text):
    with open(os.path.join(repo, name), "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


def _commit(repo, msgdir, env, name, message, files):
    for fname in files:
        _write(repo, fname, "content of " + fname + "\n")
    msgfile = os.path.join(msgdir, name)
    with open(msgfile, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(message)
    _sgit(repo, env, "add", "-A")
    _sgit(repo, env, "commit", "-q", "-F", msgfile)
    return _sgit(repo, env, "rev-parse", "HEAD")


def _merge(repo, msgdir, env, name, branch, message):
    msgfile = os.path.join(msgdir, name)
    with open(msgfile, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(message)
    _sgit(repo, env, "merge", "--no-ff", "-q", "-F", msgfile, branch)
    return _sgit(repo, env, "rev-parse", "HEAD")


def _build_fixture(repo, msgdir, env):
    """Settlement, then: a both-trailer merge, a Feature-only merge, plain commits, a quoting merge, a side commit."""
    _run(["git", "init", "-q", repo], env)
    settle = _commit(repo, msgdir, env, "settle.msg", "Settlement commit\n", ["a.txt"])
    main = _sgit(repo, env, "symbolic-ref", "--short", "HEAD")
    _sgit(repo, env, "checkout", "-q", "-b", "f1")
    _commit(repo, msgdir, env, "f1.msg", "Feature one work\n", ["b.txt"])
    _sgit(repo, env, "checkout", "-q", main)
    c1 = _commit(repo, msgdir, env, "c1.msg", "Plain commit one\n", ["c.txt"])
    m1 = _merge(repo, msgdir, env, "m1.msg", "f1",
                "Merge f1 into DEV (approved feature)\n\nFeature: f1\nApproved-By: 1.0.0_SA_CTO @selftest-row-1\n")
    _sgit(repo, env, "checkout", "-q", "-b", "f2")
    _commit(repo, msgdir, env, "f2.msg", "Feature two work\n", ["d.txt"])
    _sgit(repo, env, "checkout", "-q", main)
    m2 = _merge(repo, msgdir, env, "m2.msg", "f2",
                "Merge f2 into DEV (feature line only)\n\nFeature: f2\n")
    e1 = _commit(repo, msgdir, env, "e1.msg", "Plain commit two\n", ["e.txt"])
    _sgit(repo, env, "checkout", "-q", "-b", "f3")
    _commit(repo, msgdir, env, "f3.msg", "Feature three work\n", ["f.txt"])
    _sgit(repo, env, "checkout", "-q", main)
    m3 = _merge(repo, msgdir, env, "m3.msg", "f3",
                "Merge f3 into DEV\n\nThis merge quotes the word Approved-By: in a sentence, not as a trailer.\n")
    _sgit(repo, env, "checkout", "-q", "-b", "side", settle)
    side = _commit(repo, msgdir, env, "side.msg", "Side commit off settlement\n", ["s.txt"])
    _sgit(repo, env, "checkout", "-q", main)
    return {"settle": settle, "main": main, "c1": c1, "m1": m1, "m2": m2, "e1": e1, "m3": m3, "side": side}


def _rm_readonly(func, path, _exc):
    os.chmod(path, stat.S_IWRITE)
    func(path)


def selftest():
    env = dict(os.environ)
    env.update({"GIT_AUTHOR_NAME": "selftest", "GIT_AUTHOR_EMAIL": "selftest@example.invalid",
                "GIT_COMMITTER_NAME": "selftest", "GIT_COMMITTER_EMAIL": "selftest@example.invalid"})
    tmp = tempfile.mkdtemp(prefix="dev-approval-selftest-")
    checks = []
    try:
        repo = os.path.join(tmp, "repo")
        fx = _build_fixture(repo, tmp, env)
        rc, lines = read_dev(repo, fx["main"], fx["settle"])
        s = {k: v[:8] for k, v in fx.items()}
        checks.append(("approved merge read APPROVED with feature, by and row",
                       "DEV-COMMIT %s APPROVED feature=f1 by=1.0.0_SA_CTO row=selftest-row-1" % s["m1"] in lines))
        checks.append(("feature-only merge read UNAPPROVED",
                       "DEV-COMMIT %s UNAPPROVED author=selftest subject=Merge f2 into DEV (feature line only)"
                       % s["m2"] in lines))
        checks.append(("plain commit one read UNAPPROVED",
                       "DEV-COMMIT %s UNAPPROVED author=selftest subject=Plain commit one" % s["c1"] in lines))
        checks.append(("plain commit two read UNAPPROVED",
                       "DEV-COMMIT %s UNAPPROVED author=selftest subject=Plain commit two" % s["e1"] in lines))
        checks.append(("mid-sentence Approved-By quote read UNAPPROVED",
                       "DEV-COMMIT %s UNAPPROVED author=selftest subject=Merge f3 into DEV" % s["m3"] in lines))
        summary = ("DEV-APPROVAL since=%s ref=%s first_parent_commits=5 approved=1 unapproved=4"
                   % (s["settle"], fx["main"]))
        checks.append(("summary counts first-parent walk and exits 0", rc == 0 and summary in lines))
        rc_side, lines_side = read_dev(repo, fx["main"], fx["side"])
        checks.append(("since not an ancestor of ref is REFUSED rc=3",
                       rc_side == 3 and lines_side[-1] == "DEV-APPROVAL result=REFUSED reason=since-not-ancestor"))
    except (RuntimeError, OSError) as exc:
        print(ascii_only("SELFTEST-FIXTURE failed: %s" % exc))
    finally:
        shutil.rmtree(tmp, onerror=_rm_readonly)
    ok_count = 0
    for name, passed in checks:
        ok_count += 1 if passed else 0
        print(ascii_only("SELFTEST-CASE ok=%s name=%s" % (passed, name)))
    ok = len(checks) == SELFTEST_CASES and ok_count == SELFTEST_CASES
    print("DEV-APPROVAL-SELFTEST cases=%d/%d ok=%s" % (ok_count, SELFTEST_CASES, ok))
    return 0 if ok else 1


def main(argv=None):
    parser = argparse.ArgumentParser(description="Per-commit read of portal DEV: APPROVED or UNAPPROVED.")
    parser.add_argument("--portal", default="portal", help="portal repo path (default: portal)")
    parser.add_argument("--ref", default="origin/DEV", help="ref to read (default: origin/DEV)")
    parser.add_argument("--since", default=SETTLEMENT,
                        help="exclusive lower bound; default is the DEV = PROD settlement commit 63c4f9e3")
    parser.add_argument("--selftest", action="store_true", help="run the fixture self-test")
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest()
    rc, lines = read_dev(args.portal, args.ref, args.since)
    for line in lines:
        print(line)
    return rc


if __name__ == "__main__":
    sys.exit(main())
