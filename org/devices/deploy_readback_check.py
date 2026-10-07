#!/usr/bin/env python3
"""deploy_readback_check.py -- the deploy read-back a Dell runs AFTER it deploys a commit no other box has merged
(NFRA_CTLPLN round 4, cell CT-d-4; PRD v0.12 ADDENDUM v0.9 (b)).

Run on the Dell, in a checkout that holds the commit, after the deploy:

    AGENTBUS_DEVICE=dell1 python org/devices/deploy_readback_check.py --commit <40-hex> \\
        --object <repo path>=s3://<bucket>/<key> [--object ...] \\
        [--lambda-sha256 <function name>=<expected CodeSha256, hex or base64>] \\
        --ledger org/critical_paths/change_management/<entry>.md [--aws <command>] [--remote origin] [--device dell1]

Steps, one printed line each:
  STEP 1 NAMED-COMMIT  .tools/named_commit_check.py check, called as a tool (never re-implemented); the run continues
                       only on ADMITTED (an UNCHANGED verdict, a non-execution box, is not ADMITTED here).
  STEP 2 NOT-MERGED    after a fetch, the commit is NOT an ancestor of <remote>/CLOUD (on_trunk=False). On the trunk the run
                       still completes and reports on_trunk=True, which fails the exercised bar.
  STEP 3 OBJECT        per --object: the bytes of `git show <commit>:<repo path>` against the S3 object's bytes
                       (`s3api get-object` to a temporary file), by SHA-256 and length, both digests printed. Binary reads
                       only; no text mode touches either side.
         LAMBDA        per --lambda-sha256: the function's deployed CodeSha256 (`lambda get-function`) against the expected
                       digest. A Lambda package is BUILT (zipped, with timestamps), so its bytes cannot be compared to a
                       repo path without the build step; the expected digest is the one the build or the Terraform plan
                       recorded. Each such check counts in the same e/n denominator as the objects.
  STEP 4 LEDGER        the entry at --ledger exists, is CLOSED, and carries `named_commit=<this hash>` (the line
                       named_commit_check.py --record leaves in the entry's `## Log`, which deploy_ledger.py re-renders
                       from the sentinel's log array on every mutation, so it survives close).

LAST line:
  DEPLOY-READBACK commit=<h> device=<d> admitted=<True|False> on_trunk=<True|False|Unknown> objects_equal=<e>/<n>
      ledger=<closed-named|open|missing|other-commit> ok=<True|False> failed=<comma list of the fields that failed | none>
ok=True only when admitted, on_trunk=False, e == n, n >= 1 and the ledger is closed-named. rc 0 on ok, else 1.
When step 1 does not admit, steps 2-4 are SKIPPED (not run), and the last line says so by on_trunk=Unknown,
objects_equal=0/<n> and ledger=missing, which then mean "not read", not "read and absent".

ledger=other-commit means: the entry is closed but does not carry this hash (it carries another named commit, or none).
"""
import argparse
import base64
import binascii
import hashlib
import importlib.util
import json
import os
import re
import shlex
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
NAMED_CHECK = ROOT / ".tools" / "named_commit_check.py"
FULL_HASH = re.compile(r"^[0-9a-f]{40}$")
NAMED_RE = re.compile(r"named_commit=([0-9a-f]{40})")
# A readback-closed entry is a COMPLETED deploy. deploy_ledger.py's terminal set also holds ROLLBACK, CANCEL, SUPERSEDED,
# ABANDONED, VOID, RESOLVED: those are not a completed deploy of this commit, so they are not "closed" here.
DONE_TOKENS = ("CLOSED", "COMPLETE", "DONE")


def step(n, name, text):
    print("STEP %d %s: %s" % (n, name, text), flush=True)


def run_cmd(argv, timeout=120):
    """(rc, stdout bytes, stderr text). A timeout is rc 124 and a missing executable rc 127, with the reason as stderr."""
    try:
        r = subprocess.run(argv, capture_output=True, timeout=timeout)
        return r.returncode, r.stdout, r.stderr.decode("utf-8", "replace")
    except subprocess.TimeoutExpired:
        return 124, b"", "timeout after %ss: %s" % (timeout, " ".join(argv[:4]))
    except OSError as exc:
        return 127, b"", "cannot run %s: %s" % (argv[0], exc)


def aws_argv(aws_arg):
    """The AWS command as an argv list: --aws (shell-split) when given, else the repo's .tools/aws shim through Git Bash."""
    if aws_arg:
        return shlex.split(aws_arg)
    sys.path.insert(0, str(ROOT / ".tools"))
    import git_bash_resolver
    return git_bash_resolver.bash_argv(str(ROOT / ".tools" / "aws"))


def digest(data):
    return hashlib.sha256(data).hexdigest(), len(data)


def named_check(repo, commit, remote, device):
    argv = [sys.executable, str(NAMED_CHECK), "check", "--commit", commit, "--repo", str(repo), "--remote", remote]
    if device:
        argv += ["--device", device]
    rc, out, err = run_cmd(argv, timeout=240)
    text = out.decode("utf-8", "replace")
    line = next((ln for ln in text.splitlines() if ln.startswith("NAMED-COMMIT ")), "")
    if not line:
        line = "NAMED-COMMIT REFUSED reason=no result line from named_commit_check.py rc=%s %s" % (rc, err.strip()[:160])
    verdict = line.split()[1] if len(line.split()) > 1 else "REFUSED"
    dev = re.search(r" device=(\S+)", line)
    return verdict, (dev.group(1) if dev else (device or "-")), line


def on_trunk(repo, commit, remote):
    """True / False / None (None = the fetch or the ancestry read failed; never read as False)."""
    rc, _, err = run_cmd(["git", "-C", str(repo), "fetch", "--prune", remote], timeout=240)
    if rc != 0:
        return None, "git fetch %s rc=%s: %s" % (remote, rc, err.strip()[:160])
    rc, _, err = run_cmd(["git", "-C", str(repo), "merge-base", "--is-ancestor", commit, "%s/CLOUD" % remote])
    if rc == 0:
        return True, "commit is an ancestor of %s/CLOUD" % remote
    if rc == 1:
        return False, "commit is not an ancestor of %s/CLOUD" % remote
    return None, "merge-base --is-ancestor rc=%s: %s" % (rc, err.strip()[:160])


def split_pair(spec):
    left, sep, right = spec.partition("=")
    return (left, right) if sep and left and right else (None, None)


def check_object(repo, commit, spec, aws, tmp, idx):
    """(equal, line) for one --object <repo path>=<s3 uri>."""
    path, uri = split_pair(spec)
    m = re.match(r"^s3://([^/]+)/(.+)$", uri or "")
    if path is None or not m:
        return False, "OBJECT %s: unusable spec, want <repo path>=s3://<bucket>/<key>" % spec
    rc, git_bytes, err = run_cmd(["git", "-C", str(repo), "show", "%s:%s" % (commit, path)])
    if rc != 0:
        return False, "OBJECT %s: git show %s:%s failed rc=%s: %s" % (uri, commit[:12], path, rc, err.strip()[:160])
    dest = Path(tmp) / ("object_%d.bin" % idx)
    rc, _, err = run_cmd(aws + ["s3api", "get-object", "--bucket", m.group(1), "--key", m.group(2), str(dest)])
    if rc != 0 or not dest.is_file():
        return False, "OBJECT %s: s3api get-object rc=%s: %s" % (uri, rc, err.strip()[:160])
    deployed = dest.read_bytes()
    g_sha, g_len = digest(git_bytes)
    s_sha, s_len = digest(deployed)
    eq = g_sha == s_sha and g_len == s_len
    return eq, ("OBJECT %s git_sha256=%s git_len=%d deployed_sha256=%s deployed_len=%d equal=%s [%s]"
                % (path, g_sha, g_len, s_sha, s_len, eq, uri))


def b64_of(value):
    """A CodeSha256 as base64 (what Lambda returns), from a 64-hex or a base64 spelling; None when neither."""
    value = value.strip()
    if re.fullmatch(r"[0-9a-fA-F]{64}", value):
        return base64.b64encode(binascii.unhexlify(value)).decode("ascii")
    try:
        raw = base64.b64decode(value, validate=True)
    except (binascii.Error, ValueError):
        return None
    return base64.b64encode(raw).decode("ascii") if len(raw) == 32 else None


def check_lambda(spec, aws):
    name, expected = split_pair(spec)
    want = b64_of(expected) if expected else None
    if name is None or want is None:
        return False, "LAMBDA %s: unusable spec, want <function name>=<64-hex or base64 sha256>" % spec
    rc, out, err = run_cmd(aws + ["lambda", "get-function", "--function-name", name,
                                  "--query", "Configuration.CodeSha256", "--output", "text"])
    got = out.decode("utf-8", "replace").strip()
    if rc != 0 or not got:
        return False, "LAMBDA %s: get-function rc=%s: %s" % (name, rc, err.strip()[:160])
    eq = got == want
    return eq, "LAMBDA %s deployed_CodeSha256=%s expected_CodeSha256=%s equal=%s" % (name, got, want, eq)


def load_ledger_reader():
    """deploy_ledger.py's own status reader (every markdown spelling of a Status line), loaded by path."""
    spec = importlib.util.spec_from_file_location("deploy_ledger_for_readback", str(ROOT / ".tools" / "deploy_ledger.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def ledger_state(entry, commit):
    """(state, detail). state: closed-named | open | missing | other-commit. The entry is the deploy tools' real layout:
    `**Status:** CLOSED -- nothing stranded` in the header, and the named-commit line in its `## Log`. A live sentinel
    under .open_deploys/ whose entry_path is this file means the deploy is still open, whatever the markdown says."""
    entry = Path(entry)
    if not entry.is_file():
        return "missing", "no ledger entry at %s" % entry
    dl = load_ledger_reader()
    status = dl._md_status(entry)
    head = re.sub(r"^[^0-9A-Z]+", "", (status or "").upper())
    closed = any(head.startswith(tok) for tok in DONE_TOKENS)
    sentinel_dir = entry.resolve().parents[1] / ".open_deploys"
    live = []
    if entry.resolve().parent.name == "change_management" and sentinel_dir.is_dir():
        for sp in sorted(sentinel_dir.glob("*.json")):
            try:
                st = json.loads(sp.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                continue
            if Path(st.get("entry_path", "")).name == entry.name:
                live.append(sp.name)
    if live:
        return "open", "a live sentinel names this entry (%s): the deploy is not closed" % ", ".join(live)
    if not closed:
        return "open", "entry Status is %r, not CLOSED/COMPLETE/DONE" % (status,)
    named = set(NAMED_RE.findall(entry.read_text(encoding="utf-8", errors="replace")))
    if commit in named:
        return "closed-named", "entry Status %r and carries named_commit=%s" % (status, commit)
    return "other-commit", "entry Status %r closed, named_commit values in it: %s" % (status, sorted(named) or "none")


def main(argv):
    ap = argparse.ArgumentParser(prog="deploy_readback_check")
    ap.add_argument("--commit", required=True, help="the full 40-hex hash the Dell deployed")
    ap.add_argument("--object", dest="objects", action="append", default=[], help="<repo path>=s3://<bucket>/<key>")
    ap.add_argument("--lambda-sha256", dest="lambdas", action="append", default=[], help="<function name>=<expected CodeSha256>")
    ap.add_argument("--ledger", required=True, help="the deploy's ledger entry (org/critical_paths/change_management/*.md)")
    ap.add_argument("--aws", default=None, help="the AWS command (default: the repo's .tools/aws shim)")
    ap.add_argument("--remote", default="origin")
    ap.add_argument("--device", default=None, help="this box's name (default: AGENTBUS_DEVICE)")
    ap.add_argument("--repo", default=None, help="repository holding the commit (default: the current directory)")
    a = ap.parse_args(argv)
    repo = Path(a.repo or os.getcwd())
    n = len(a.objects) + len(a.lambdas)

    verdict, device, line = named_check(repo, a.commit, a.remote, a.device)
    step(1, "named-commit", line)
    admitted = verdict == "ADMITTED"
    trunk, equal, ledger, failed = "Unknown", 0, "missing", []
    if not admitted:
        step(2, "not-merged-elsewhere", "SKIPPED (step 1 did not admit the commit)")
        step(3, "deployed-bytes", "SKIPPED (step 1 did not admit the commit)")
        step(4, "ledger", "SKIPPED (step 1 did not admit the commit)")
    else:
        t, why = on_trunk(repo, a.commit, a.remote)
        trunk = "Unknown" if t is None else str(t)
        step(2, "not-merged-elsewhere", "on_trunk=%s -- %s" % (trunk, why))
        with tempfile.TemporaryDirectory(prefix="deploy_readback_") as tmp:
            aws = aws_argv(a.aws) if (a.objects or a.lambdas) else []
            for i, spec in enumerate(a.objects):
                eq, text = check_object(repo, a.commit, spec, aws, tmp, i)
                equal += bool(eq)
                step(3, "deployed-bytes", text)
            for spec in a.lambdas:
                eq, text = check_lambda(spec, aws)
                equal += bool(eq)
                step(3, "deployed-code", text)
        if n == 0:
            step(3, "deployed-bytes", "nothing to compare: no --object and no --lambda-sha256 (n=0 cannot pass)")
        ledger, why = ledger_state(a.ledger, a.commit)
        step(4, "ledger", "%s -- %s" % (ledger, why))
    if not admitted:
        failed.append("admitted")
    if trunk != "False" and admitted:
        failed.append("on_trunk")
    if admitted and (n < 1 or equal != n):
        failed.append("objects_equal")
    if admitted and ledger != "closed-named":
        failed.append("ledger")
    ok = admitted and trunk == "False" and n >= 1 and equal == n and ledger == "closed-named"
    print("DEPLOY-READBACK commit=%s device=%s admitted=%s on_trunk=%s objects_equal=%d/%d ledger=%s ok=%s failed=%s"
          % (a.commit, device, admitted, trunk, equal, n, ledger, ok, ",".join(failed) or "none"), flush=True)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
