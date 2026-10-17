#!/usr/bin/env python3
"""test_round30_estate_prefetch.py -- the estate runner prefetches blob ids before it checks paths out (NFRA_CTLPLN
round 30, TO-CT-ci-1).

Standard library only, ASCII only, offline. Every repository is built in a temporary folder and cloned by file:// URL,
blobless and without a checkout, as clone_repo does. Runner under test:
infra/aws/ec2/estate-report-runner/estate_report_runner.py (helpers prefetch_blobs and checkout_paths; the checkout sites
route through them).

Arms:
  a  SEQUENCE  one checkout_paths call over the fixture paths records ls-tree, fetch, checkout, in that order; the fetch
               carries exactly the blob ids that git rev-parse gives for the files (derived here, not by the helper)
  b  REAL CLONE a blobless file:// clone checks out every file with the bytes of the source
  c  CONTROL   the same kind of clone with a bare checkout and no prefetch; REPORTED, the arm passes either way
  d  SITES     no line outside checkout_paths names the checkout argv; the three callers call the helper
  e  SOFT      a clone whose origin is a missing folder logs one WARN and still reaches the checkout, which is last
  f  MUTANT    a copy of the runner with the fetch removed from the helper fails arm a
  ascii        this file is ASCII

Usage: python .tools/tests/test_round30_estate_prefetch.py
Last line: ESTATE-PREFETCH arms=<k>/<n> ok=<True|False>
"""
import ast
import contextlib
import importlib.util
import io
import os
import shutil
import stat
import subprocess
import sys
import tempfile
import types
from pathlib import Path

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "lib"))
RUNNER = os.path.join(REPO, "infra", "aws", "ec2", "estate-report-runner", "estate_report_runner.py")
BRANCH = "CLOUD"
PACK = "pack"
TOP = "top.txt"
FILES = {("pack/f%02d.txt" % i): ("fixture file %02d, unique bytes\n" % i).encode("ascii") for i in range(32)}
FILES[TOP] = b"top level fixture file\n"
PATHS = [PACK, TOP]
HELPER = "checkout_paths"
CALLERS = ("load_function_map", "load_attribution_maps", "capture_census")
PREFETCH_WARN = "WARN: blob prefetch failed"
SEQUENCE = ["ls-tree", "fetch", "checkout"]

ARMS = []
ROOTS = []
REAL_RUN = subprocess.run


def arm(name, cond, detail=""):
    ARMS.append((name, bool(cond)))
    print("%s %s %s" % ("PASS" if cond else "FAIL", name, detail))


def tmp(prefix):
    d = tempfile.mkdtemp(prefix=prefix)
    ROOTS.append(d)
    return d


def _rm_readonly(func, path, _exc):
    os.chmod(path, stat.S_IWRITE)
    func(path)


def git(cwd, *args):
    """git -C cwd args with text output and check=True. Never the runner's own call."""
    return REAL_RUN(["git", "-C", cwd] + list(args), check=True, capture_output=True, text=True)


def read_bytes(path):
    with open(path, "rb") as f:
        return f.read()


def make_source():
    """A non-bare repository whose CLOUD branch holds FILES, with the two upload-pack settings a blobless clone needs."""
    d = tmp("ci1-src-")
    REAL_RUN(["git", "init", "-q", d], check=True, capture_output=True)
    git(d, "symbolic-ref", "HEAD", "refs/heads/" + BRANCH)
    git(d, "config", "core.autocrlf", "false")
    git(d, "config", "user.name", "ci1")
    git(d, "config", "user.email", "ci1@test")
    for rel, data in FILES.items():
        p = os.path.join(d, rel.replace("/", os.sep))
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "wb") as f:
            f.write(data)
    git(d, "add", "-A")
    git(d, "commit", "-q", "-m", "fixture")
    git(d, "config", "uploadpack.allowFilter", "true")
    git(d, "config", "uploadpack.allowAnySHA1InWant", "true")
    return d


def blobless_clone(src):
    """A fresh clone made the way clone_repo makes it: --filter=blob:none --no-checkout --branch CLOUD, by file:// URL."""
    dst = os.path.join(tmp("ci1-clone-"), "repo")
    REAL_RUN(["git", "clone", "-q", "--filter=blob:none", "--no-checkout", "--branch", BRANCH,
              Path(src).as_uri(), dst], check=True, capture_output=True, text=True)
    git(dst, "config", "core.autocrlf", "false")
    return dst


def expected_ids(src):
    """Blob ids of the fixture files, read with git rev-parse one file at a time (independent of ls-tree -r)."""
    return [git(src, "rev-parse", "%s:%s" % (BRANCH, rel)).stdout.strip() for rel in sorted(FILES)]


def recording(sink):
    """A subprocess.run wrapper that records every argv and still runs the command."""
    def run(argv, *a, **k):
        sink.append(list(argv))
        return REAL_RUN(argv, *a, **k)
    return run


def verb(argv):
    return argv[3] if len(argv) > 3 and argv[1] == "-C" else argv[1]


def fetch_ids(argv):
    return argv[argv.index("origin") + 1:]


def sequence_ok(sink, want):
    """True when the recorded calls are exactly ls-tree, fetch, checkout, and the fetch carries the wanted ids."""
    verbs = [verb(a) for a in sink]
    if verbs != SEQUENCE:
        return False
    return sorted(fetch_ids(sink[1])) == sorted(want)


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run_arms():
    # the runner reads its environment at import; the branch is fixed to the fixture branch
    for var in ("ESTATE_REPORT_BUCKET", "ESTATE_GITHUB_SECRET_ID", "ESTATE_KIMI_SECRET_ID", "ESTATE_KIMI_URL",
                "ESTATE_KIMI_MODEL", "ESTATE_REPO_URL"):
        os.environ.setdefault(var, "ci1-test")
    os.environ["ESTATE_REPO_BRANCH"] = BRANCH
    if "boto3" not in sys.modules:
        try:
            import boto3  # noqa: F401
        except ImportError:
            sys.modules["boto3"] = types.SimpleNamespace(client=lambda *a, **k: None, resource=lambda *a, **k: None)
    runner = load_module("estate_report_runner_ci1", RUNNER)

    src = make_source()
    want = expected_ids(src)
    arm("a fixture denominator", len(want) == len(FILES) == 33, "ids=%d files=%d" % (len(want), len(FILES)))

    # arm a: one helper call over the fixture paths, recorded
    clone_a = blobless_clone(src)
    sink_a = []
    error_a = None
    subprocess.run = recording(sink_a)
    try:
        runner.checkout_paths(clone_a, PATHS)
    except Exception as exc:  # noqa: BLE001
        error_a = exc
    finally:
        subprocess.run = REAL_RUN
    verbs_a = [verb(a) for a in sink_a]
    arm("a sequence ls-tree,fetch,checkout", verbs_a == SEQUENCE and error_a is None,
        "verbs=%s error=%s" % (",".join(verbs_a), type(error_a).__name__ if error_a else "none"))
    fetched = [fetch_ids(a) for a in sink_a if verb(a) == "fetch"]
    got = sorted(fetched[0]) if len(fetched) == 1 else []
    arm("a fetch carries the ls-tree ids", len(fetched) == 1 and got == sorted(want),
        "fetch_ids=%d want=%d" % (len(got), len(want)))

    # arm b: a real blobless clone, checked out by the helper, carries the source's bytes
    clone_b = blobless_clone(src)
    runner.checkout_paths(clone_b, PATHS)
    present = 0
    for rel in FILES:
        here = os.path.join(clone_b, rel.replace("/", os.sep))
        there = os.path.join(src, rel.replace("/", os.sep))
        if os.path.isfile(here) and read_bytes(here) == read_bytes(there):
            present += 1
    arm("b real clone bytes equal the source", present == len(FILES), "files=%d/%d" % (present, len(FILES)))

    # arm c: the control, a bare checkout on a fresh blobless clone with no prefetch; reported, passes either way
    clone_c = blobless_clone(src)
    rc = REAL_RUN(["git", "-C", clone_c, "checkout", BRANCH, "--"] + PATHS, capture_output=True, text=True)
    control_reproduced = rc.returncode != 0
    last_err = ((rc.stderr or "").strip().splitlines() or ["no stderr"])[-1]
    version = REAL_RUN(["git", "--version"], capture_output=True, text=True).stdout.strip()
    print("control_reproduced=%s rc=%d git=%s stderr_last=%s" % (control_reproduced, rc.returncode, version, last_err))
    arm("c control bare checkout ran", True, "control_reproduced=%s" % control_reproduced)

    # arm d: the sites, read from the runner's syntax tree
    with open(RUNNER, encoding="utf-8") as f:
        text = f.read()
    tree = ast.parse(text)
    funcs = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
    helper = funcs.get(HELPER)
    lines = text.splitlines()
    literal = '"checkout", REPO_BRANCH'
    hits = [i + 1 for i, ln in enumerate(lines) if literal in ln]
    inside = [h for h in hits if helper is not None and helper.lineno <= h <= helper.end_lineno]
    outside = [h for h in hits if h not in inside]
    arm("d checkout argv only in %s" % HELPER, helper is not None and len(hits) >= 1 and not outside,
        "hits=%s outside=%s" % (hits, outside))
    for name in CALLERS:
        fn = funcs.get(name)
        calls = fn is not None and any(
            isinstance(c, ast.Call) and isinstance(c.func, ast.Name) and c.func.id == HELPER for c in ast.walk(fn))
        arm("d %s calls %s" % (name, HELPER), calls)

    # arm e: the prefetch fails (origin is a missing folder); one WARN, then the checkout is still reached and is last
    clone_e = blobless_clone(src)
    missing = os.path.join(tmp("ci1-missing-"), "no-such-repo")
    git(clone_e, "remote", "set-url", "origin", Path(missing).as_uri())
    sink_e = []
    raised = None
    buf = io.StringIO()
    subprocess.run = recording(sink_e)
    try:
        with contextlib.redirect_stdout(buf):
            runner.checkout_paths(clone_e, PATHS)
    except Exception as exc:  # noqa: BLE001
        raised = exc
    finally:
        subprocess.run = REAL_RUN
    verbs_e = [verb(a) for a in sink_e]
    warned = buf.getvalue().count(PREFETCH_WARN)
    arm("e one WARN on failed prefetch", warned == 1, "warn_lines=%d" % warned)
    raised_from_checkout = isinstance(raised, subprocess.CalledProcessError) and verb(list(raised.cmd)) == "checkout"
    arm("e checkout reached last, raising only from checkout",
        verbs_e == SEQUENCE and raised_from_checkout,
        "verbs=%s raised=%s" % (",".join(verbs_e), type(raised).__name__ if raised else "none"))

    # arm f: a mutant with the fetch removed from the helper must fail arm a
    anchor = "    if not ids:\n        return\n"
    anchors = text.count(anchor)
    arm("f mutant anchor unique", anchors == 1, "anchors=%d" % anchors)
    mutant_text = text.replace(anchor, "    return  # MUTANT: fetch removed\n", 1)
    mpath = os.path.join(tmp("ci1-mutant-"), "estate_report_runner_mutant.py")
    with open(mpath, "w", encoding="utf-8", newline="\n") as f:
        f.write(mutant_text)
    mutant = load_module("estate_report_runner_mutant_ci1", mpath)
    clone_f = blobless_clone(src)
    sink_f = []
    subprocess.run = recording(sink_f)
    try:
        mutant.checkout_paths(clone_f, PATHS)
    except Exception:  # noqa: BLE001
        pass
    finally:
        subprocess.run = REAL_RUN
    mut_ok = sequence_ok(sink_f, want)
    print("MUTANT verbs=%s arm_a=%s" % (",".join(verb(a) for a in sink_f), mut_ok))
    arm("f mutant reads ok=False on arm a", mut_ok is False, "verbs=%s" % ",".join(verb(a) for a in sink_f))

    raw = read_bytes(os.path.abspath(__file__))
    arm("ascii this file", all(b < 128 for b in raw))


def cleanup():
    for d in ROOTS:
        shutil.rmtree(d, onerror=_rm_readonly, ignore_errors=True)


def main():
    # an arm body that raises is a FAIL arm, never a crash: the last line is always printed
    try:
        run_arms()
    except Exception as e:  # noqa: BLE001
        arm("abort %s" % type(e).__name__, False, str(e)[:200])
    finally:
        subprocess.run = REAL_RUN
        cleanup()
    k = sum(1 for _n, ok in ARMS if ok)
    n = len(ARMS)
    print("ESTATE-PREFETCH arms=%d/%d ok=%s" % (k, n, k == n))
    return 0 if k == n else 1


if __name__ == "__main__":
    sys.exit(main())
