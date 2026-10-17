"""BUILD the release-34h resident tarball and its four host scripts from a pin (BUILD ONLY: nothing is uploaded, installed, applied or run on a host).

usage: python -I r34j_build.py --pin <full 40-hex commit> --out <stage folder outside the repository> --record <RESIDENT_R34J_BUILD.json to write>

Run it from the repository root (or any worktree of it). The stage folder must not exist yet. It refuses unless the builder, the packer, the
clock wrapper, the script generator and the files-from list on disk equal the same files at the pin. Steps: verify the r34h base tarball (the
root running on the host when the install starts);
build twice under one fixed clock and compare member by member; pack once; extract; diff against the r34h tarball (changed, added, removed; the build REFUSES unless exactly SHA256SUMS, reports/resident_bindings.json (only provenance.package_pin and the files-from list's count and sha256), intake/yfinance_check.py and ycharts/research/price_adapter_ycharts.py changed and ycharts/research/price_form_ycharts.py and ycharts/research/ycharts_client.py added);
derive the four host scripts from the r31 set over the r34h root; `bash -n` each; dry-run the two sha256 gates (an unchanged copy passes, a one-byte copy refuses);
write the record. Prints one RESULT line: R34J-BUILD-OK <members> ... or R34J-BUILD-BAD <why>. ASCII only. No aws call of any kind.
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
R34 = "org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/"
TOOLS = ["build_resident_package.py", "pack_r34.py", "run_builder_fixed_clock.py", "make_scripts_r34j.py", "files_from_r34.txt"]
R32_DIR = "C:/dev/irpt-release-r34r"  # the r34h stage folder: the OLD root is the r34h tarball that runs on the host
R32_TAR = R32_DIR + "/irpt-resident-0485393f3a-r34h.tar.gz"
R32_TAR_SHA = "60cc8d1d68627c993121df7eca946a40046f1d7f63ddfd2968f83e27077b93c0"
EXPECT_CHANGED = ["SHA256SUMS", "reports/resident_bindings.json", "intake/yfinance_check.py", "ycharts/research/price_adapter_ycharts.py"]  # the bindings differ only as checked below
EXPECT_ADDED = ["ycharts/research/price_form_ycharts.py", "ycharts/research/ycharts_client.py"]
POOL_SRC = "org/tier2_senior/0.7.0_AE_CloudOps~AQ2/deliverables/irpt_anlreq_r34/swap_pool.json"
R31_SCRIPTS = "org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~144"
STATE_JSON = "org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~55/r19/recipe_evidence/state_st32_from_bindings.json"
STATE_SHA = "dda583923b92532e53796d8c0270f9a013196873bbeb841b75b2a2bc72c40808"
BASE_PIN = "0485393f3ad0a7e564f4867f5e70003e2e62195b"
MAPS = "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/"
FIXED_CLOCK = "2026-10-16T00:00:00Z"
PRICING = '{"enabled": true, "tiers": ["estate", "yfinance", "ycharts"]}'
BUDGET = '{"calls": 6, "window_s": 390}'  # the floor the paced read showed clean (CTO msgs 9757, 9761); every securities_info CALL counts
BUILD_ARGS = [
    "--enrolled-user-id", "1276035", "--census-pin", "2874e37647", "--research",
    "--opal-map", MAPS + "overview_map.json", "--opal-map-comparison", MAPS + "comparison_map.json",
    "--opal-map-multicomp", MAPS + "multi_map.json", "--opal-pricing-binding", PRICING, "--ycharts-window-budget", BUDGET,
    "--member", "ycharts/research/etf_classifications_dynamodb.py=infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py",
    "--member", "lib/trading_calendar.py=lib/trading_calendar.py", "--opal-swap-pool", POOL_SRC, "--base-pin", BASE_PIN,
    "--member", "ycharts/research/ycharts_client.py=infra/aws/lambda/ycharts-market-data-pull/ycharts_client.py",  # the estate client, at its pinned blob (AR-g-155 calls its builder)
    "--analysis-ready-queue-url", "https://sqs.us-east-1.amazonaws.com/313476888478/outlook-global-commentary-draft-analysis-ready-queue",
    "--commentary-ready-queue-url", "https://sqs.us-east-1.amazonaws.com/313476888478/outlook-global-commentary-draft-commentary-ready-queue",
    "--packager", "api_base=https://7k3ed8px20.execute-api.us-east-1.amazonaws.com,secret_name=opal/ticketing/svc-irpt-packager",
]


def bad(why):
    print("R34J-BUILD-BAD %s" % why)
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
        at_pin = git("show", "%s:%s%s" % (pin, R34, name))
        with open(os.path.join(REPO, R34, name), "rb") as fh:
            if fh.read().replace(b"\r\n", b"\n") != at_pin.replace(b"\r\n", b"\n"):
                bad("%s on disk differs from the pin" % name)
    # 2. the base
    if not os.path.isfile(R32_TAR) or sha_file(R32_TAR) != R32_TAR_SHA:
        bad("the r34h base tarball is absent or not %s" % R32_TAR_SHA)
    if sha_file(os.path.join(REPO, STATE_JSON)) != STATE_SHA:
        bad("the core state file is not the one r31 used")
    os.makedirs(out)
    x32 = out + "/x32"
    tarfile.open(R32_TAR).extractall(x32)
    files_from = os.path.join(REPO, R34, "files_from_r34.txt").replace("\\", "/")
    state = os.path.join(REPO, STATE_JSON).replace("\\", "/")
    builder = os.path.join(REPO, R34, "build_resident_package.py").replace("\\", "/")
    wrapper = os.path.join(REPO, R34, "run_builder_fixed_clock.py").replace("\\", "/")
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
    tar_path = out + "/irpt-resident-0485393f3a-r34j.tar.gz"
    pack = run([sys.executable, "-I", os.path.join(REPO, R34, "pack_r34.py"), out + "/build_a", tar_path, "pax", "gzip", "dotslash"])
    if pack.returncode != 0:
        bad("packer rc %d: %s" % (pack.returncode, pack.stderr[-200:]))
    sums_path = out + "/irpt-resident-0485393f3a-r34j.package.SHA256SUMS"
    shutil.copy(out + "/build_a/SHA256SUMS", sums_path)
    x34 = out + "/x34"
    tarfile.open(tar_path).extractall(x34)
    if walk(x34) != a:
        bad("the extracted tarball differs from build_a")
    # 4. the delta against r34h
    w34, w32 = walk(x34), walk(x32)
    changed = sorted(n for n in w34 if n in w32 and w34[n] != w32[n])
    added = sorted(set(w34) - set(w32))
    removed = sorted(set(w32) - set(w34))
    unchanged = len(set(w34) & set(w32)) - len(changed)
    if changed != sorted(EXPECT_CHANGED) or added != sorted(EXPECT_ADDED) or removed:
        bad("the delta against r34h is not exactly changed %s added %s: changed %s added %s removed %s" % (EXPECT_CHANGED, EXPECT_ADDED, changed, added, removed))
    bindings = json.load(open(x34 + "/reports/resident_bindings.json", encoding="utf-8"))
    bindings32 = json.load(open(x32 + "/reports/resident_bindings.json", encoding="utf-8"))
    keys_added = sorted(set(bindings) - set(bindings32))
    keys_changed = sorted(k for k in bindings if k in bindings32 and bindings[k] != bindings32[k])
    prov_changed = sorted(k for k in set(bindings["provenance"]) | set(bindings32["provenance"]) if bindings["provenance"].get(k) != bindings32["provenance"].get(k))
    if keys_added or keys_changed != ["provenance"] or prov_changed != ["files_from_count", "files_from_sha256", "members_added", "package_pin"]:
        bad("the bindings differ from r34h beyond provenance (package_pin, the files-from list's count and sha256, which grew by one line, and members_added, which grew by the estate client): added %s changed %s provenance %s" % (keys_added, keys_changed, prov_changed))
    if bindings["provenance"]["members_added"] != bindings32["provenance"]["members_added"] + [{"packaged": "ycharts/research/ycharts_client.py", "repo_path": "infra/aws/lambda/ycharts-market-data-pull/ycharts_client.py", "sha256": w34["ycharts/research/ycharts_client.py"]}]:
        bad("members_added is not the r34h list plus exactly the estate client at its pinned blob: %r" % (bindings["provenance"]["members_added"],))
    if bindings["opal_pricing"] != {"enabled": True, "tiers": ["estate", "yfinance", "ycharts"]} or bindings32["opal_pricing"] != bindings["opal_pricing"]:
        bad("opal_pricing is not exactly the tiers estate, yfinance, ycharts (enabled) in both r34h and r34j: %r -> %r" % (bindings32["opal_pricing"], bindings["opal_pricing"]))
    if bindings["ycharts_window_budget"] != {"calls": 6, "window_s": 390} or bindings32["ycharts_window_budget"] != bindings["ycharts_window_budget"]:
        bad("ycharts_window_budget is %r (want 6 calls, 390 s, unchanged from r34h)" % (bindings["ycharts_window_budget"],))
    # 5. the scripts
    scripts_dir = out + "/scripts"
    os.makedirs(scripts_dir)
    gen = run([sys.executable, "-I", os.path.join(REPO, R34, "make_scripts_r34j.py"), os.path.join(REPO, R31_SCRIPTS), scripts_dir, x34, x32,
               tar_path, sums_path])
    if gen.returncode != 0:
        bad("script generator rc %d: %s" % (gen.returncode, (gen.stdout + gen.stderr)[-300:]))
    scripts = []
    for name in ("pre_read_r34.sh", "install_r34.sh", "rollback_r34.sh", "resident_host_install_0485393f3a-r34j.sh"):
        path = "%s/%s" % (scripts_dir, name)
        data = open(path, "rb").read()
        syntax = run(["bash", "-n", path])
        scripts.append({"name": name, "path": path, "bytes": len(data), "sha256": sha_bytes(data), "bash_n_rc": syntax.returncode,
                        "ascii_only": all(c < 128 for c in data)})
    if any(s["bash_n_rc"] != 0 or not s["ascii_only"] for s in scripts):
        bad("a script fails bash -n or is not ASCII")
    # 6. the gate dry run: the two sha256 gate lines of install_r32.sh, evaluated against scratch copies
    install = open("%s/install_r34.sh" % scripts_dir, encoding="ascii").read().split("\n")
    g1 = [ln for ln in install if "sha256sum $T |" in ln]
    g2 = [ln for ln in install if "sha256sum $S |" in ln]
    want = next(ln for ln in install if ln.startswith("WANT=")).split("=", 1)[1]
    want_sum = next(ln for ln in install if ln.startswith("WANTSUM=")).split("=", 1)[1]
    if len(g1) != 1 or len(g2) != 1:
        bad("gate lines found %d and %d, want 1 and 1" % (len(g1), len(g2)))
    scratch = out + "/gate_scratch"
    os.makedirs(scratch)
    host_ok = "%s/host_ok.sh" % scratch
    shutil.copy("%s/resident_host_install_0485393f3a-r34j.sh" % scripts_dir, host_ok)
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
    worker_text = open(x34 + "/ycharts/generate/resident_worker.py", encoding="utf-8").read()
    pool_doc = json.load(open(x34 + "/ycharts/research/swap_pool.json", encoding="utf-8"))
    producer_line = next(ln for ln in worker_text.split("\n") if ln.startswith("OPAL_PRODUCER_PRINCIPALS"))
    record = {
        "schema_version": "irpt-resident-r34j-build-v1", "record_id": "RESIDENT_R34J_BUILD", "issued_by": "2.0.0_SA_COO~G2",
        "scope_statement": "BUILD ONLY: nothing was uploaded, installed, applied, invoked or run on a host; no aws call was made.",
        "artifact": {"path": tar_path, "bytes": os.path.getsize(tar_path), "sha256": sha_file(tar_path), "member_count": len(w34),
                     "sha256sums_file": {"path": sums_path, "sha256": sha_file(sums_path), "lines": len(open(sums_path).read().splitlines())}},
        "release_input": {"pin_full_sha": pin, "base_pin": BASE_PIN, "census_pin": "2874e37647", "clock_held_to": FIXED_CLOCK,
                          "builder_sha256_on_disk": sha_file(os.path.join(REPO, R34, "build_resident_package.py")),
                          "files_from_sha256": sha_file(os.path.join(REPO, R34, "files_from_r34.txt")),
                          "files_from_count": stdout_a.get("files_from_count"), "arguments": BUILD_ARGS},
        "two_builds": {"files_compared": len(a), "identical": len(a), "build_a": out + "/build_a", "build_b": out + "/build_b"},
        "delta_vs_r34h": {"r34h_tarball_sha256": R32_TAR_SHA, "live_members": len(w32), "release_members": len(w34), "unchanged": unchanged,
                         "changed": changed, "added": added, "removed": removed},
        "bindings_diff": {"keys_added": keys_added, "keys_changed": keys_changed},
        "producer_list": producer_line,
        "swap_pool": {"source": POOL_SRC, "member": "ycharts/research/swap_pool.json", "sha256": sha_file(x34 + "/ycharts/research/swap_pool.json"),
                      "pool_as_of": pool_doc["pool_as_of"], "pool_claim": pool_doc["pool_claim"], "rows": len(pool_doc["rows"])},
        "scripts": scripts, "gate_dry_run": results,
        "rollback": {"rollback_root": "/opt/irpt-resident/0485393f3a-r34h", "base_tarball_sha256": R32_TAR_SHA},
        "not_read": ["the live host", "the live S3 objects", "the live root and cutover receipt", "the release-34h key"],
    }
    with open(args.record, "w", encoding="ascii", newline="\n") as fh:
        fh.write(json.dumps(record, indent=2, sort_keys=True) + "\n")
    print("R34J-BUILD-OK %d members, builds identical %d of %d, changed %d added %d removed %d, scripts %d, tar %s" % (
        len(w34), len(a), len(a), len(changed), len(added), len(removed), len(scripts), record["artifact"]["sha256"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
