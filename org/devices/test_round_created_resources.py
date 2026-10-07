"""test_round_created_resources.py -- cases for org/devices/round_created_resources.py (NFRA_CTLPLN cell CT-d-7).

Every case builds a temporary git repository and a temporary registry file; nothing reads the real tree or calls AWS.
LAST line: ROUND-RESOURCES-TEST cases=<k>/5 ok=<True|False>
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
USER_A = 'resource "aws_iam_user" "alpha" {\n  name = "demo-alpha-user"\n}\n\n'
USER_B = 'resource "aws_iam_user" "beta" {\n  name = "demo-beta-user"\n}\n\n'
ATTACH = ('resource "aws_iam_user_policy_attachment" "alpha" {\n  user       = aws_iam_user.alpha.name\n'
          '  policy_arn = "arn:aws:iam::000000000000:policy/demo"\n}\n\n')
BAD = 'resource "aws_iam_policy" "gamma" {\n  name = var.policy_name\n}\n\n'


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


def run_read(repo, registry, since, until, *extra):
    p = subprocess.run([sys.executable, SCRIPT, "--repo", repo, "--registry", registry, "--since", since, "--until", until] + list(extra),
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
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


def case_registered_and_missing(tmp):
    repo, base = new_repo(tmp)
    end = commit_files(repo, {ROOT_REL + "/main.tf": HEAD_TF + USER_A + USER_B}, "two users")
    lines, last = run_read(repo, registry_file(tmp, ["demo-alpha-user"]), base, end)
    ok = ("created=2" in last and "named=2" in last and "registered=1/2" in last and "missing=1" in last and "unresolved=0" in last
          and "ok=False" in last and any(ln.startswith("MISSING") and "demo-beta-user" in ln for ln in lines)
          and any(ln.startswith("REGISTERED") and "demo-alpha-user" in ln for ln in lines))
    return ok, last


def case_nameless(tmp):
    repo, base = new_repo(tmp)
    end = commit_files(repo, {ROOT_REL + "/main.tf": HEAD_TF + USER_A + ATTACH}, "user and attachment")
    lines, last = run_read(repo, registry_file(tmp, ["demo-alpha-user"]), base, end)
    ok = ("created=2" in last and "nameless=1" in last and "named=1" in last and "registered=1/1" in last and "missing=0" in last
          and "ok=True" in last and any(ln.startswith("NAMELESS") and "aws_iam_user_policy_attachment.alpha" in ln for ln in lines))
    return ok, last


def case_removed(tmp):
    repo, base0 = new_repo(tmp)
    mid = commit_files(repo, {ROOT_REL + "/main.tf": HEAD_TF + USER_A + USER_B}, "two users")
    end = commit_files(repo, {ROOT_REL + "/main.tf": HEAD_TF + USER_A}, "beta removed")
    lines, last = run_read(repo, registry_file(tmp, []), mid, end)
    ok0 = "created=0" in last and "ok=True" in last and not any("beta" in ln for ln in lines)
    # and a resource that exists at --since is never "created" even when it is still there
    lines2, last2 = run_read(repo, registry_file(tmp, []), mid, end, "--root", ROOT_REL)
    ok = ok0 and "created=0" in last2 and not any("alpha" in ln or "beta" in ln for ln in lines2)
    return ok, last + " | " + last2


def case_unresolved(tmp):
    repo, base = new_repo(tmp)
    end = commit_files(repo, {ROOT_REL + "/main.tf": HEAD_TF + USER_A + BAD}, "a variable-named policy")
    lines, last = run_read(repo, registry_file(tmp, ["demo-alpha-user"]), base, end)
    ok = ("created=2" in last and "unresolved=1" in last and "registered=1/1" in last and "missing=0" in last and "ok=False" in last
          and any(ln.startswith("UNRESOLVED") and "aws_iam_policy.gamma" in ln for ln in lines))
    return ok, last


def case_no_tf_change(tmp):
    repo, base = new_repo(tmp)
    end = commit_files(repo, {"docs/notes.md": "no terraform here\n"}, "docs only")
    lines, last = run_read(repo, registry_file(tmp, []), base, end)
    ok = "created=0" in last and "roots=-" in last and "ok=True" in last
    return ok, last


CASES = [("registered_and_missing", case_registered_and_missing), ("nameless", case_nameless), ("removed", case_removed),
         ("unresolved", case_unresolved), ("no_tf_change", case_no_tf_change)]


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
    print("ROUND-RESOURCES-TEST cases=%d/5 ok=%s" % (passed, passed == 5))
    return 0 if passed == 5 else 1


if __name__ == "__main__":
    sys.exit(main())
