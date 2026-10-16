"""IRPT_ANLREQ release 35 Lambda leg, BUILD ONLY (cell AR-g-115, issuer 2.0.0_SA_COO~G2): the irpt-status package at a pin, built twice, recorded.

    python -I r35l_build.py --pin <40-hex> --out <stage folder outside the repo, absent or empty> --record <record.json>

Builds `irpt-status` with the repository's own builder (`infra/aws/lambda/ci/build-and-upload.sh`,
BUILD_ONLY=1: nothing is uploaded, no AWS call is made, the source map is untouched) from a throwaway detached worktree at the pin,
TWICE with a private TMPDIR, and refuses unless the two zips are byte-identical. It then opens each zip and compares its
members with `release-census.build_members` at the pin (the issuer's offline census builder) and with the same build at each function's
LAST DEPLOYED COMMIT (`last_deployed_commit` in the source map at the pin: the commit the live package was built from), and records the
delta, which is the expected release delta against the live zip. It reads no live zip: the member diff against the LIVE package is the
applier's census.

Prints `R35L-BUILD-OK <summary>` and exits 0, or `R35L-BUILD-BAD <why>` and exits 1. ASCII only; stdlib only.
"""
import argparse
import base64
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys
import zipfile
from pathlib import Path

GEN, STATUS = "irpt-ycharts-generate", "irpt-status"
# The live irpt-status package is the release-33 build (order TO-APPLY-R33, AQ2 msg 8976): built from the pin of AR-g-102's merge. The map's own
# last_deployed_commit for it is a later, test-only commit and is NOT the build commit, so the baseline is named here.
STATUS_BASELINE = "927337a741f40a83e7daa9e09154436a813b05dd"
BUILDER = "infra/aws/lambda/ci/build-and-upload.sh"
# The builder reads the source dirs from the tree and every staged row from git; a sparse cone of these folders is enough (the CodeSha256
# must equal a full checkout's, which the issuer's trial build confirmed).
SPARSE = ("infra", "lib", "data", "docs", "org/standards", "org/tier1_exec/2.0.0_SA_COO", ".tools")
CENSUS = "infra/aws/lambda/ci/release-census.py"
HEX40 = re.compile(r"[0-9a-f]{40}")


def bad(why):
    print("R35L-BUILD-BAD " + why)
    sys.exit(1)


def git(*args, cwd=None, check=True):
    out = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    if check and out.returncode != 0:
        bad("git %s failed: %s" % (" ".join(args[:3]), out.stderr.strip()[:200]))
    return out.stdout.strip()


def load_census(root):
    spec = importlib.util.spec_from_file_location("release_census", str(Path(root) / CENSUS))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build_once(wt, function, tmp):
    Path(tmp).mkdir(parents=True)
    env = {k: v for k, v in os.environ.items() if k != "MSYS_NO_PATHCONV"}
    env.update(TMPDIR=str(tmp).replace("\\", "/"), BUILD_ONLY="1")
    out = subprocess.run(["bash", BUILDER, "investor-reporting", function], cwd=wt, env=env, capture_output=True, text=True, timeout=900)
    text = out.stdout + out.stderr
    m = re.search(r"BUILD_ONLY: (\S+) sha256=(\S+) key=", text)
    if out.returncode != 0 or not m:
        bad("the builder failed for %s: rc=%d %s" % (function, out.returncode, text[-300:].replace("\n", " ")))
    path = Path(tmp) / ("lambda-artifact-%s.zip" % function)
    if not path.is_file():
        bad("the builder's zip is absent from the private TMPDIR: " + function)
    data = path.read_bytes()
    code_sha = base64.b64encode(hashlib.sha256(data).digest()).decode()
    if code_sha != m.group(2):
        bad("the builder's digest differs from the zip's own for " + function)
    return data, code_sha


def members_of(data):
    out = {}
    with zipfile.ZipFile(__import__("io").BytesIO(data)) as zf:
        for info in zf.infolist():
            if not info.is_dir():
                out[info.filename] = hashlib.sha256(zf.read(info.filename)).hexdigest()
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pin", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--record", required=True)
    args = parser.parse_args()
    root = Path.cwd()
    if not (root / ".git").exists() or not (root / BUILDER).is_file():
        bad("run from a repository root that holds the builder")
    if not HEX40.fullmatch(args.pin) or git("cat-file", "-t", args.pin, check=False) != "commit":
        bad("--pin must be a full 40-hex commit")
    out = Path(args.out)
    if out.exists() and any(out.iterdir()):
        bad("the stage folder is not empty")
    if str(out.resolve()).startswith(str(root.resolve())):
        bad("the stage folder must be OUTSIDE the repository")
    out.mkdir(parents=True, exist_ok=True)
    census = load_census(root)
    if git("show", "%s:%s" % (args.pin, BUILDER)).count("BUILD_ONLY") < 1:
        bad("the builder at the pin has no BUILD_ONLY guard")
    wt = out / "wt"
    git("-c", "core.longpaths=true", "worktree", "add", "--detach", "--no-checkout", str(wt), args.pin)
    git("sparse-checkout", "init", "--cone", cwd=str(wt))
    git("sparse-checkout", "set", *SPARSE, cwd=str(wt))
    git("-c", "core.longpaths=true", "checkout", cwd=str(wt))
    record = {"schema": "irpt-r35l-build.v1", "pin": args.pin, "functions": {}, "live_read": False}
    try:
        for function in (STATUS,):
            a, code_a = build_once(wt, function, out / ("tmp_%s_a" % function))
            b, code_b = build_once(wt, function, out / ("tmp_%s_b" % function))
            if a != b or code_a != code_b:
                bad("two builds of %s differ" % function)
            zip_path = out / ("%s.zip" % function)
            zip_path.write_bytes(a)
            built = members_of(a)
            expected = {k: hashlib.sha256(v).hexdigest() for k, v in census.build_members(root, function, args.pin).items()}
            if built != expected:
                bad("%s: the zip's members differ from the census build at the pin: %s" % (function, sorted(set(built) ^ set(expected))[:5]))
            deployed = STATUS_BASELINE
            if not HEX40.fullmatch(deployed) or subprocess.run(["git", "merge-base", "--is-ancestor", deployed, args.pin]).returncode != 0:
                bad("%s: last_deployed_commit is not an ancestor commit of the pin" % function)
            base = {k: hashlib.sha256(v).hexdigest() for k, v in census.build_members(root, function, deployed).items()}
            delta = sorted(k for k in set(built) | set(base) if built.get(k) != base.get(k))
            record["functions"][function] = {
                "zip": zip_path.name, "zip_sha256": hashlib.sha256(a).hexdigest(), "code_sha256": code_a, "bytes": len(a), "members": len(built),
                "builds_identical": True, "member_sha256": built, "deployed_commit": deployed, "delta_vs_deployed_commit": delta}
    finally:
        subprocess.run(["git", "worktree", "remove", "--force", str(wt)], capture_output=True, text=True)
    record_path = Path(args.record)
    record_path.parent.mkdir(parents=True, exist_ok=True)
    record_path.write_text(json.dumps(record, indent=1, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    parts = ["%s members=%d delta=%d code_sha256=%s" % (f, v["members"], len(v["delta_vs_deployed_commit"]), v["code_sha256"]) for f, v in record["functions"].items()]
    print("R35L-BUILD-OK " + "; ".join(parts))
    return 0


if __name__ == "__main__":
    sys.exit(main())
