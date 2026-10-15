"""BUILD the release-32 resident tarball and its four host scripts from a pin (BUILD ONLY: nothing is uploaded, installed, applied or run on a host).

usage: python -I r32_build.py --pin <full 40-hex commit> --out <stage folder outside the repository> --record <RESIDENT_R32_BUILD.json to write>

Run it from the repository root (or any worktree of it). The stage folder must not exist yet. It refuses unless the builder, the packer, the
clock wrapper, the script generator and the files-from list on disk equal the same files at the pin. Steps: verify the r31 base tarball;
build twice under one fixed clock and compare member by member; pack once; extract; diff against the r31 tarball (changed, added, removed);
derive the four host scripts from the r31 set; `bash -n` each; dry-run the two sha256 gates (an unchanged copy passes, a one-byte copy refuses);
write the record. Prints one RESULT line: R32-BUILD-OK <members> ... or R32-BUILD-BAD <why>. ASCII only. No aws call of any kind.
"""
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tarfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = subprocess.run(["git", "-C", HERE, "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True).stdout.strip()
R32 = "org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r32/"
TOOLS = ["build_resident_package.py", "pack_r32.py", "run_builder_fixed_clock.py", "make_scripts_r32.py", "files_from_r32.txt"]
R31_DIR = "C:/dev/irpt-release-r31"
R31_TAR = R31_DIR + "/irpt-resident-0485393f3a-r31.tar.gz"
R31_TAR_SHA = "22193944345ce2dd52d2b732ce0ac8d569aa2359958601686239b7e1da8e6021"
R31_SCRIPTS = "org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~144"
STATE_JSON = "org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~55/r19/recipe_evidence/state_st32_from_bindings.json"
STATE_SHA = "dda583923b92532e53796d8c0270f9a013196873bbeb841b75b2a2bc72c40808"
BASE_PIN = "0485393f3ad0a7e564f4867f5e70003e2e62195b"
MAPS = "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/"
FIXED_CLOCK = "2026-10-15T00:00:00Z"
PRICING = '{"enabled": false, "tiers": ["estate", "yfinance"]}'
BUILD_ARGS = [
    "--enrolled-user-id", "1276035", "--census-pin", "2874e37647", "--research",
    "--opal-map", MAPS + "overview_map.json", "--opal-map-comparison", MAPS + "comparison_map.json",
    "--opal-map-multicomp", MAPS + "multi_map.json", "--opal-pricing-binding", PRICING,
    "--member", "ycharts/research/etf_classifications_dynamodb.py=infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py",
    "--member", "lib/trading_calendar.py=lib/trading_calendar.py", "--base-pin", BASE_PIN,
    "--analysis-ready-queue-url", "https://sqs.us-east-1.amazonaws.com/313476888478/outlook-global-commentary-draft-analysis-ready-queue",
    "--commentary-ready-queue-url", "https://sqs.us-east-1.amazonaws.com/313476888478/outlook-global-commentary-draft-commentary-ready-queue",
    "--packager", "api_base=https://7k3ed8px20.execute-api.us-east-1.amazonaws.com,secret_name=opal/ticketing/svc-irpt-packager",
]


def bad(why):
    print("R32-BUILD-BAD %s" % why)
    sys.exit(1)


def sha_bytes(data):
    return hashlib.sha256(data).hexdigest()


def sha_file(path):
    with open(path, "rb") as fh:
        return sha_bytes(fh.read())


def git(*args):
    out = subprocess.run(["git", "-C", REPO] + list(args), capture_output=True, check=False)
    if out.returncode != 0:
        bad("git %s failed: %s" % (" ".join(args), out.stderr.decode(errors="replace")[:160]))
    return out.stdout


def walk(root):
    out = {}
    for dp, _dn, fn in os.walk(root):
        for f in fn:
            p = os.path.join(dp, f)
            out[os.path.relpath(p, root).replace(os.sep, "/")] = sha_file(p)
    return out


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", **kw)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pin", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--record", required=True)
    args = ap.parse_args()
    pin = git("rev-parse", args.pin).decode().strip()
    if pin != args.pin:
        bad("--pin must be the full 40-hex sha (rev-parse gives %s)" % pin)
    out = args.out.replace("\\", "/")
    if os.path.exists(out):
        bad("the stage folder %s already exists" % out)
    if os.path.abspath(out).startswith(os.path.abspath(REPO)):
        bad("the stage folder is inside the repository")
    # 1. the tools on disk are the tools at the pin
    for name in TOOLS:
        at_pin = git("show", "%s:%s%s" % (pin, R32, name))
        with open(os.path.join(REPO, R32, name), "rb") as fh:
            if fh.read().replace(b"\r\n", b"\n") != at_pin.replace(b"\r\n", b"\n"):
                bad("%s on disk differs from the pin" % name)
    # 2. the base
    if not os.path.isfile(R31_TAR) or sha_file(R31_TAR) != R31_TAR_SHA:
        bad("the r31 base tarball is absent or not %s" % R31_TAR_SHA)
    if sha_file(os.path.join(REPO, STATE_JSON)) != STATE_SHA:
        bad("the core state file is not the one r31 used")
    os.makedirs(out)
    x31 = out + "/x31"
    tarfile.open(R31_TAR).extractall(x31)
    files_from = os.path.join(REPO, R32, "files_from_r32.txt").replace("\\", "/")
    state = os.path.join(REPO, STATE_JSON).replace("\\", "/")
    builder = os.path.join(REPO, R32, "build_resident_package.py").replace("\\", "/")
    wrapper = os.path.join(REPO, R32, "run_builder_fixed_clock.py").replace("\\", "/")
    env = dict(os.environ, MSYS_NO_PATHCONV="1", BUILD_ONLY="1")
    stdout_a = None
    for tag in ("build_a", "build_b"):
        cmd = [sys.executable, "-I", wrapper, builder, FIXED_CLOCK, "--", "--pin", pin, "--out", "%s/%s" % (out, tag), "--files-from", files_from,
               "--state-json", state] + BUILD_ARGS
        proc = run(cmd, env=env, cwd=REPO)
        if proc.returncode != 0:
            bad("builder %s rc %d: %s" % (tag, proc.returncode, proc.stderr[-200:]))
        if tag == "build_a":
            stdout_a = json.loads(proc.stdout)
    a, b = walk(out + "/build_a"), walk(out + "/build_b")
    if a != b:
        bad("build_a and build_b differ: %s" % sorted(set(a) ^ set(b) or [n for n in a if a[n] != b.get(n)])[:5])
    # 3. pack once, stage the sums beside it
    tar_path = out + "/irpt-resident-0485393f3a-r32.tar.gz"
    pack = run([sys.executable, "-I", os.path.join(REPO, R32, "pack_r32.py"), out + "/build_a", tar_path, "pax", "gzip", "dotslash"])
    if pack.returncode != 0:
        bad("packer rc %d: %s" % (pack.returncode, pack.stderr[-200:]))
    sums_path = out + "/irpt-resident-0485393f3a-r32.package.SHA256SUMS"
    shutil.copy(out + "/build_a/SHA256SUMS", sums_path)
    x32 = out + "/x32"
    tarfile.open(tar_path).extractall(x32)
    if walk(x32) != a:
        bad("the extracted tarball differs from build_a")
    # 4. the delta against r31
    w32, w31 = walk(x32), walk(x31)
    changed = sorted(n for n in w32 if n in w31 and w32[n] != w31[n])
    added = sorted(set(w32) - set(w31))
    removed = sorted(set(w31) - set(w32))
    unchanged = len(set(w32) & set(w31)) - len(changed)
    bindings = json.load(open(x32 + "/reports/resident_bindings.json", encoding="utf-8"))
    bindings31 = json.load(open(x31 + "/reports/resident_bindings.json", encoding="utf-8"))
    keys_added = sorted(set(bindings) - set(bindings31))
    keys_changed = sorted(k for k in bindings if k in bindings31 and bindings[k] != bindings31[k])
    # 5. the scripts
    scripts_dir = out + "/scripts"
    os.makedirs(scripts_dir)
    gen = run([sys.executable, "-I", os.path.join(REPO, R32, "make_scripts_r32.py"), os.path.join(REPO, R31_SCRIPTS), scripts_dir, x32, x31,
               tar_path, sums_path])
    if gen.returncode != 0:
        bad("script generator rc %d: %s" % (gen.returncode, (gen.stdout + gen.stderr)[-300:]))
    scripts = []
    for name in ("pre_read_r32.sh", "install_r32.sh", "rollback_r32.sh", "resident_host_install_0485393f3a-r32.sh"):
        path = "%s/%s" % (scripts_dir, name)
        data = open(path, "rb").read()
        syntax = run(["bash", "-n", path])
        scripts.append({"name": name, "path": path, "bytes": len(data), "sha256": sha_bytes(data), "bash_n_rc": syntax.returncode,
                        "ascii_only": all(c < 128 for c in data)})
    if any(s["bash_n_rc"] != 0 or not s["ascii_only"] for s in scripts):
        bad("a script fails bash -n or is not ASCII")
    # 6. the gate dry run: the two sha256 gate lines of install_r32.sh, evaluated against scratch copies
    install = open("%s/install_r32.sh" % scripts_dir, encoding="ascii").read().split("\n")
    g1 = [ln for ln in install if "sha256sum $T |" in ln]
    g2 = [ln for ln in install if "sha256sum $S |" in ln]
    want = next(ln for ln in install if ln.startswith("WANT=")).split("=", 1)[1]
    want_sum = next(ln for ln in install if ln.startswith("WANTSUM=")).split("=", 1)[1]
    if len(g1) != 1 or len(g2) != 1:
        bad("gate lines found %d and %d, want 1 and 1" % (len(g1), len(g2)))
    scratch = out + "/gate_scratch"
    os.makedirs(scratch)
    host_ok = "%s/host_ok.sh" % scratch
    shutil.copy("%s/resident_host_install_0485393f3a-r32.sh" % scripts_dir, host_ok)
    sums_ok = "%s/sums_ok" % scratch
    shutil.copy(sums_path, sums_ok)
    host_bad, sums_bad = "%s/host_bad.sh" % scratch, "%s/sums_bad" % scratch
    for src, dst, off in ((host_ok, host_bad, 100), (sums_ok, sums_bad, 50)):
        data = bytearray(open(src, "rb").read())
        data[off] ^= 0x01
        open(dst, "wb").write(bytes(data))

    def evaluate(line, T, S):
        script = "WANT=%s\nWANTSUM=%s\nT=\"%s\"\nS=\"%s\"\nrm() { :; }\n%s\n" % (want, want_sum, T, S, line)
        return run(["bash", "-c", script]).returncode
    results = {"gate1_unchanged_rc": evaluate(g1[0], host_ok, sums_ok), "gate1_one_byte_rc": evaluate(g1[0], host_bad, sums_ok),
               "gate2_unchanged_rc": evaluate(g2[0], host_ok, sums_ok), "gate2_one_byte_rc": evaluate(g2[0], host_ok, sums_bad)}
    if (results["gate1_unchanged_rc"], results["gate1_one_byte_rc"], results["gate2_unchanged_rc"], results["gate2_one_byte_rc"]) != (0, 31, 0, 33):
        bad("gate dry run: %s" % results)
    shutil.rmtree(scratch)
    worker_text = open(x32 + "/ycharts/generate/resident_worker.py", encoding="utf-8").read()
    producer_line = next(ln for ln in worker_text.split("\n") if ln.startswith("OPAL_PRODUCER_PRINCIPALS"))
    record = {
        "schema_version": "irpt-resident-r32-build-v1", "record_id": "RESIDENT_R32_BUILD", "issued_by": "2.0.0_SA_COO~G2",
        "scope_statement": "BUILD ONLY: nothing was uploaded, installed, applied, invoked or run on a host; no aws call was made.",
        "artifact": {"path": tar_path, "bytes": os.path.getsize(tar_path), "sha256": sha_file(tar_path), "member_count": len(w32),
                     "sha256sums_file": {"path": sums_path, "sha256": sha_file(sums_path), "lines": len(open(sums_path).read().splitlines())}},
        "release_input": {"pin_full_sha": pin, "base_pin": BASE_PIN, "census_pin": "2874e37647", "clock_held_to": FIXED_CLOCK,
                          "builder_sha256_on_disk": sha_file(os.path.join(REPO, R32, "build_resident_package.py")),
                          "files_from_sha256": sha_file(os.path.join(REPO, R32, "files_from_r32.txt")),
                          "files_from_count": stdout_a.get("files_from_count"), "arguments": BUILD_ARGS},
        "two_builds": {"files_compared": len(a), "identical": len(a), "build_a": out + "/build_a", "build_b": out + "/build_b"},
        "delta_vs_r31": {"r31_tarball_sha256": R31_TAR_SHA, "live_members": len(w31), "release_members": len(w32), "unchanged": unchanged,
                         "changed": changed, "added": added, "removed": removed},
        "bindings_diff": {"keys_added": keys_added, "keys_changed": keys_changed},
        "producer_list": producer_line,
        "scripts": scripts, "gate_dry_run": results,
        "rollback": {"rollback_root": "/opt/irpt-resident/0485393f3a-r31", "base_tarball_sha256": R31_TAR_SHA},
        "not_read": ["the live host", "the live S3 objects", "the live root and cutover receipt", "the release-32 key"],
    }
    with open(args.record, "w", encoding="ascii", newline="\n") as fh:
        fh.write(json.dumps(record, indent=2, sort_keys=True) + "\n")
    print("R32-BUILD-OK %d members, builds identical %d of %d, changed %d added %d removed %d, scripts %d, tar %s" % (
        len(w32), len(a), len(a), len(changed), len(added), len(removed), len(scripts), record["artifact"]["sha256"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
