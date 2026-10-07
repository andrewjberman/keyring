"""test_round_created_resources.py -- cases for org/devices/round_created_resources.py (NFRA_CTLPLN cell CT-d-7, AMENDMENT 1).

Every case builds a temporary git repository and a temporary registry file; the cloud-graph arm is pointed (--graph-tool) at a
RECORDER script written into the case's temporary directory, which answers in comp-find's output format from a fixture and logs
every call it receives. No case calls the real comp-find or any AWS API. The registry arm's reader is the real
lib/opal_naming.py (its vocabulary: `demo` is a scope, `cloudops` a system) and the validator's count line is the real one.
LAST line: ROUND-RESOURCES-TEST cases=<k>/6 ok=<True|False>
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "round_created_resources.py")
ROOT_REL = "infra/aws/terraform/demo-root"

HEAD_TF = 'terraform {\n  required_version = ">= 1.5.0"\n}\n\n'
USER_A = 'resource "aws_iam_user" "alpha" {\n  name = "demo-alpha-user"\n}\n\n'      # `demo` is a scope: no system from its tokens
USER_B = 'resource "aws_iam_user" "beta" {\n  name = "demo-beta-user"\n}\n\n'
USER_C = 'resource "aws_iam_user" "gamma" {\n  name = "cloudops-alpha-user"\n}\n\n'  # `cloudops` is a system: self-resolving
ATTACH = ('resource "aws_iam_user_policy_attachment" "alpha" {\n  user       = aws_iam_user.gamma.name\n'
          '  policy_arn = "arn:aws:iam::000000000000:policy/demo"\n}\n\n')
BAD = 'resource "aws_iam_policy" "delta" {\n  name = var.policy_name\n}\n\n'

RECORDER = r'''import json, os, sys
here = os.path.dirname(os.path.abspath(__file__))
fx = json.load(open(os.path.join(here, "fixture.json")))
pat = sys.argv[sys.argv.index("aws") + 1] if "aws" in sys.argv else sys.argv[1]
with open(os.path.join(here, "calls.log"), "a") as fh:
    fh.write(pat + "\n")
if fx.get("fail"):
    sys.stderr.write("recorder: simulated failure\n")
    sys.exit(1)
name = pat.replace("\\", "")
hit = fx.get("nodes", {}).get(name)
print("comp-find [aws content] %r" % pat)
print("  WITHIN BUDGET: scanned 1 of 1 pull; recorder")
print("  DEFERRED: 0 of 1 pull(s) did not return")
print("  VINTAGE: Built from the estate as of %s UTC. recorder" % fx["vintage"])
print("  DENOMINATOR: %d hit(s) across 100 aws node(s) scanned [corpus=aws]" % (1 if hit else 0))
if hit:
    print("  [%s]" % hit[0])
    print("    %s  drift=%s src=recorder" % (name, hit[1]))
    print("      arn:aws:iam::000000000000:user/%s" % name)
    print("      ...props...")
'''


def git(repo, *args):
    cmd = ["git", "-c", "user.name=t", "-c", "user.email=t@example.invalid", "-c", "commit.gpgsign=false",
           "-c", "core.hooksPath=" + os.devnull, "-C", repo] + list(args)
    p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if p.returncode != 0:
        raise RuntimeError("git %s failed: %s" % (" ".join(args), p.stderr.strip()))
    return p.stdout.strip()


def commit_files(repo, files, message):
    for rel, text in files.items():
        path = os.path.join(repo, *rel.split("/"))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", message)
    return git(repo, "rev-parse", "HEAD")


def recorder(tmp, vintage="2099-01-01 00:00:00", nodes=None, fail=False):
    """Write the recorder and its fixture into tmp/rec; return (script path, calls-log path)."""
    d = os.path.join(tmp, "rec")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "graph_recorder.py"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(RECORDER)
    with open(os.path.join(d, "fixture.json"), "w", encoding="utf-8") as fh:
        json.dump({"vintage": vintage, "nodes": nodes or {}, "fail": fail}, fh)
    return os.path.join(d, "graph_recorder.py"), os.path.join(d, "calls.log")


def calls_of(log):
    if not os.path.isfile(log):
        return []
    with open(log, encoding="utf-8", errors="replace") as fh:
        return [ln.strip() for ln in fh if ln.strip()]


def run_read(repo, registry, since, until, tool, *extra):
    p = subprocess.run([sys.executable, SCRIPT, "--repo", repo, "--registry", registry, "--since", since, "--until", until,
                        "--graph-tool", tool] + list(extra), capture_output=True, text=True, encoding="utf-8", errors="replace")
    lines = [ln for ln in p.stdout.splitlines() if ln.strip()]
    return lines, (lines[-1] if lines else "")


def registry_file(tmp, names):
    path = os.path.join(tmp, "resources.json")
    rows = [{"name": n, "type": "IAM_USER", "system": "demo", "evidence": "test"} for n in names]
    with open(path, "w", encoding="utf-8") as fh:
        json.dump({"_about": "test", "resources": rows}, fh)
    return path


def new_repo(tmp):
    repo = os.path.join(tmp, "repo")
    os.makedirs(repo)
    git(repo, "init", "-q")
    base = commit_files(repo, {"README.md": "base\n"}, "base")
    return repo, base


def case_registered_and_row_needed(tmp):
    """One registered, one whose tokens resolve no system and has no row; the graph (newer than the commit) finds one node, not the other."""
    repo, base = new_repo(tmp)
    end = commit_files(repo, {ROOT_REL + "/main.tf": HEAD_TF + USER_A + USER_B}, "two users")
    tool, log = recorder(tmp, nodes={"demo-alpha-user": ["IAM_USER", "DECLARED"]})
    lines, last = run_read(repo, registry_file(tmp, ["demo-alpha-user"]), base, end, tool)
    ok = ("created=2" in last and "named=2" in last and "self_resolving=0" in last and "registered=1 " in last and "row_needed=1" in last
          and "unresolved=0" in last and "graph_nodes=1" in last and "no_node=1 " in last and "no_node_graph_older=0" in last
          and "graph_unread=0" in last and "graph_built=2099-01-01T00:00:00Z" in last and "ok=False" in last
          and any(ln.startswith("ROW-NEEDED") and "demo-beta-user" in ln for ln in lines)
          and any(ln.startswith("REGISTERED") and "demo-alpha-user" in ln and "node_type=IAM_USER drift_class=DECLARED" in ln for ln in lines)
          and any(ln.startswith("VALIDATOR rc=0 VALIDATE: OK") for ln in lines)
          and sorted(calls_of(log)) == ["demo-alpha-user", "demo-beta-user"])
    return ok, last


def case_nameless(tmp):
    """A self-resolving user plus an attachment: the attachment is NAMELESS and is not read; a graph older than the commit labels the miss."""
    repo, base = new_repo(tmp)
    end = commit_files(repo, {ROOT_REL + "/main.tf": HEAD_TF + USER_C + ATTACH}, "user and attachment")
    tool, log = recorder(tmp, vintage="2000-01-01 00:00:00")
    lines, last = run_read(repo, registry_file(tmp, []), base, end, tool)
    ok = ("created=2" in last and "nameless=1" in last and "named=1" in last and "self_resolving=1" in last and "registered=0 " in last
          and "row_needed=0" in last and "graph_nodes=0" in last and "no_node=0 " in last and "no_node_graph_older=1" in last
          and "ok=True" in last and any(ln.startswith("NAMELESS") and "aws_iam_user_policy_attachment.alpha" in ln for ln in lines)
          and any(ln.startswith("SELF-RESOLVING") and "NO-NODE-GRAPH-OLDER" in ln for ln in lines)
          and calls_of(log) == ["cloudops-alpha-user"])
    return ok, last


def case_removed(tmp):
    repo, base0 = new_repo(tmp)
    mid = commit_files(repo, {ROOT_REL + "/main.tf": HEAD_TF + USER_A + USER_B}, "two users")
    end = commit_files(repo, {ROOT_REL + "/main.tf": HEAD_TF + USER_A}, "beta removed")
    tool, log = recorder(tmp)
    lines, last = run_read(repo, registry_file(tmp, []), mid, end, tool)
    ok0 = "created=0" in last and "ok=True" in last and not any("beta" in ln for ln in lines)
    # and a resource that exists at --since is never "created" even when it is still there
    lines2, last2 = run_read(repo, registry_file(tmp, []), mid, end, tool, "--root", ROOT_REL)
    ok = ok0 and "created=0" in last2 and not any("alpha" in ln or "beta" in ln for ln in lines2) and calls_of(log) == []
    return ok, last + " | " + last2


def case_unresolved(tmp):
    repo, base = new_repo(tmp)
    end = commit_files(repo, {ROOT_REL + "/main.tf": HEAD_TF + USER_C + BAD}, "a variable-named policy")
    tool, log = recorder(tmp, nodes={"cloudops-alpha-user": ["IAM_USER", "DECLARED"]})
    lines, last = run_read(repo, registry_file(tmp, []), base, end, tool)
    ok = ("created=2" in last and "unresolved=1" in last and "self_resolving=1" in last and "row_needed=0" in last
          and "graph_nodes=1" in last and "graph_unread=0" in last and "ok=False" in last
          and any(ln.startswith("UNRESOLVED") and "aws_iam_policy.delta" in ln for ln in lines)
          and calls_of(log) == ["cloudops-alpha-user"])
    return ok, last


def case_no_tf_change(tmp):
    repo, base = new_repo(tmp)
    end = commit_files(repo, {"docs/notes.md": "no terraform here\n"}, "docs only")
    tool, log = recorder(tmp)
    lines, last = run_read(repo, registry_file(tmp, []), base, end, tool)
    ok = "created=0" in last and "roots=-" in last and "ok=True" in last and calls_of(log) == []
    return ok, last


def case_graph_unread(tmp):
    """A recorder that fails: the resource is GRAPH-UNREAD, counted, never NO-NODE."""
    repo, base = new_repo(tmp)
    end = commit_files(repo, {ROOT_REL + "/main.tf": HEAD_TF + USER_C}, "one user")
    tool, log = recorder(tmp, fail=True)
    lines, last = run_read(repo, registry_file(tmp, []), base, end, tool)
    ok = ("created=1" in last and "named=1" in last and "self_resolving=1" in last and "graph_unread=1" in last
          and "graph_nodes=0" in last and "no_node=0 " in last and "no_node_graph_older=0" in last and "ok=False" in last
          and any("GRAPH-UNREAD" in ln and "rc=1" in ln for ln in lines) and calls_of(log) == ["cloudops-alpha-user"])
    return ok, last


CASES = [("registered_and_row_needed", case_registered_and_row_needed), ("nameless", case_nameless), ("removed", case_removed),
         ("unresolved", case_unresolved), ("no_tf_change", case_no_tf_change), ("graph_unread", case_graph_unread)]


def main():
    passed = 0
    for name, fn in CASES:
        with tempfile.TemporaryDirectory() as tmp:
            try:
                ok, evidence = fn(tmp)
            except Exception as exc:  # a case that cannot run is a FAIL, printed
                ok, evidence = False, "EXC %s: %s" % (type(exc).__name__, exc)
        print("%s case_%s: %s" % ("PASS" if ok else "FAIL", name, evidence))
        passed += bool(ok)
    print("ROUND-RESOURCES-TEST cases=%d/%d ok=%s" % (passed, len(CASES), passed == len(CASES)))
    return 0 if passed == len(CASES) else 1


if __name__ == "__main__":
    sys.exit(main())
