"""test_kit_terraform_providers.py -- the Terraform provider kit, on this box and on stand-ins. NO NETWORK.

(1) required on the real tree; (2) located on this box; (3) pack into a temporary directory and verify; (4) one byte flipped, verify
refuses; (5) THE SEAM PROBE: a real `terraform init` against the packed mirror with a CLI config that installs only from the mirror and
excludes the registry; (6) no command the tool constructs, and no line of the tool's source, carries a registry address or a
downloading verb. AMENDMENT 4 adds (7) the Terraform binary is located by the wrapper's own order, (8) pack carries it and
`verify --run-binary` passes, (9) one byte of the packed binary flipped -> verify refuses BEFORE running it (a marker-writing runner is
the proof it was never executed), (10) `readback` on a temporary local-backend root with only locals and outputs reads init=ok
plan_exit=0. LAST line: TF-KIT-TEST cases=<k>/10 skipped=<s> ok=<True|False>.
"""
from __future__ import annotations

import importlib.util
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
TOOL = HERE / "kit_terraform_providers.py"
spec = importlib.util.spec_from_file_location("kit_terraform_providers", str(TOOL))
kit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kit)

RESULTS = []  # (case, status, detail)


def record(case, status, detail):
    RESULTS.append((case, status, detail))
    print("CASE %d %s: %s" % (case, status, detail))


def run_tool(*args, timeout=300):
    p = subprocess.run([sys.executable, str(TOOL)] + list(args), capture_output=True, text=True, timeout=timeout)
    return p.returncode, p.stdout + p.stderr


def last_line(text):
    lines = [x for x in text.splitlines() if x.strip()]
    return lines[-1] if lines else ""


def make_standin(base):
    """A stand-in search tree holding one fake provider in the mirror layout; returns (search_dir, target)."""
    pdir = base / "search" / kit.HOST / "example" / "fake" / "1.2.3" / kit.PLATFORM
    pdir.mkdir(parents=True)
    (pdir / "terraform-provider-fake_v1.2.3_x5.exe").write_bytes(b"MZ-fake-provider-binary-" * 4096)
    (pdir / "LICENSE.txt").write_bytes(b"stand-in licence text\n")
    return base / "search", {"source": "%s/example/fake" % kit.HOST, "version": "1.2.3", "h1": []}


def case1():
    with tempfile.TemporaryDirectory() as td:
        out = pathlib.Path(td) / "req.json"
        rc, txt = run_tool("required", "--out", str(out))
        data = json.loads(out.read_text(encoding="utf-8"))
    ll = last_line(txt)
    aws = [p for p in data["providers"] if p["source"] == "%s/hashicorp/aws" % kit.HOST]
    ident = [r for r in data["roots"] if r["root"] == "nfra-ctlpln-identity"]
    agent = [r for r in data["roots"] if r["root"] == "nfra-ctlpln-agentbus"]
    ident_ok = bool(ident) and ident[0]["status"] == "LOCKED" and any(p["version"] == "5.100.0" for p in ident[0]["providers"])
    # the order expected the agentbus root to lock a different major version; the tree carries NO lock file for it
    agent_nolock = bool(agent) and agent[0]["status"] == "NO-LOCK" and any(d["constraint"] == "~> 6.0" for d in agent[0].get("declared", []))
    ok = rc == 0 and "ok=True" in ll and bool(aws) and ident_ok and agent_nolock
    record(1, "PASS" if ok else "FAIL",
           "%s | aws locked versions=%s | identity=%s | agentbus=%s (no lock file; declares ~> 6.0, premise of two locked majors does not hold)"
           % (ll, ",".join(p["version"] for p in aws), ident[0]["status"] if ident else "ABSENT", agent[0]["status"] if agent else "ABSENT"))


def case2():
    rc, txt = run_tool("located")
    ll = last_line(txt)
    m = re.search(r"distinct_versions=(\d+) found=(\d+) not_on_this_box=(\d+) h1_verified=(\d+)/(\d+)", ll)
    ok = rc == 0 and bool(m) and int(m.group(2)) + int(m.group(3)) == int(m.group(1)) and "ok=True" in ll
    record(2, "PASS" if ok else "FAIL", ll)
    return txt


def case3_4():
    with tempfile.TemporaryDirectory() as td:
        base = pathlib.Path(td)
        search, target = make_standin(base)
        out = base / "mirror"
        summary, manifest = kit.pack([target], [search], out)
        res = kit.verify(out)
        placed = out / kit.HOST / "example" / "fake" / "1.2.3" / kit.PLATFORM / "terraform-provider-fake_v1.2.3_x5.exe"
        snippet = (out / kit.SNIPPET_NAME).read_text(encoding="utf-8")
        ok3 = (summary["providers"] == 1 and summary["files"] == 2 and not summary["not_on_box"] and placed.is_file()
               and res["verified"] == 2 and not res["problems"] and "filesystem_mirror" in snippet and "direct" in snippet
               and not any(p.is_symlink() for p in out.rglob("*")))
        record(3, "PASS" if ok3 else "FAIL", "stand-in pack files=%d bytes=%d linked=%d copied=%d; verify verified=%d/%d problems=%s"
               % (summary["files"], summary["bytes"], summary["linked"], summary["copied"], res["verified"], res["files"], res["problems"]))
        # AMENDMENT 9: a release zip is packed in the PACKED mirror form, matched on its zh against the lock, and refused when it
        # matches no locked hash
        import zipfile
        zdir = base / "zips" / kit.HOST / "example" / "zipped"
        zdir.mkdir(parents=True)
        zpath = zdir / kit.zip_name("%s/example/zipped" % kit.HOST, "9.9.9", kit.PLATFORM)
        with zipfile.ZipFile(str(zpath), "w") as zf:
            zf.writestr("terraform-provider-zipped_v9.9.9_x5.exe", b"MZ-zipped-" * 2048)
        zh = "zh:" + kit.sha256_file(zpath)
        zt = {"source": "%s/example/zipped" % kit.HOST, "version": "9.9.9", "h1": [], "zh": [zh]}
        zbad = {"source": "%s/example/zipped" % kit.HOST, "version": "9.9.9", "h1": [], "zh": ["zh:" + "0" * 64]}
        zout = base / "zmirror"
        zsum, _zm = kit.pack([zt], [search], zout, zip_dirs=[base / "zips"])
        zres = kit.verify(zout)
        bsum, _bm = kit.pack([zbad], [search], base / "zmirror_bad", zip_dirs=[base / "zips"])
        ok_zip = (zsum["providers"] == 1 and (zout / kit.HOST / "example" / "zipped" / zpath.name).is_file() and zres["verified"] == 1
                  and not zres["problems"] and bsum["providers"] == 0 and len(bsum["not_on_box"]) == 1)
        zip_detail = ("zip form: packed=%d verified=%d/%d; a zip matching no locked hash refused=%s"
                      % (zsum["providers"], zres["verified"], zres["files"], bool(bsum["not_on_box"])))
        # the CLI tool's own verify, as a Dell runs it
        rc_v, txt_v = run_tool("verify", "--from", str(out))
        data = bytearray(placed.read_bytes())
        data[100] ^= 0xFF
        # break the hard link first so the source tree is never touched
        placed.unlink()
        placed.write_bytes(bytes(data))
        res2 = kit.verify(out)
        rc_t, txt_t = run_tool("verify", "--from", str(out))
        src_intact = (search / kit.HOST / "example" / "fake" / "1.2.3" / kit.PLATFORM / "terraform-provider-fake_v1.2.3_x5.exe").read_bytes() != bytes(data)
        ok4 = rc_v == 0 and rc_t == 1 and res2["mismatched"] == 1 and "REFUSED" in txt_t and "ok=False" in last_line(txt_t) and src_intact and ok_zip
        record(4, "PASS" if ok4 else "FAIL", "untouched verify rc=%d; one byte flipped -> rc=%d mismatched=%d; %s | %s" % (rc_v, rc_t, res2["mismatched"], last_line(txt_t), zip_detail))


def smallest_probe_root(req):
    best = None
    for r in req["roots"]:
        if r["status"] != "LOCKED" or kit.LOCK_NAME not in r["lock_files"]:
            continue
        rdir = kit.TF_BASE / r["root"]
        text = "".join(f.read_text(encoding="utf-8", errors="replace") for f in rdir.glob("*.tf"))
        if re.search(r"^\s*module\s", text, re.M):
            continue
        size = len(text)
        if best is None or size < best[0]:
            best = (size, r)
    return best[1] if best else None


def terraform_env(config_path, trace=False):
    env = dict(os.environ)
    for k in ("TF_PLUGIN_CACHE_DIR", "TF_CLI_ARGS", "TF_CLI_ARGS_init", "TF_LOG", "TF_DATA_DIR"):
        env.pop(k, None)
    env["TF_CLI_CONFIG_FILE"] = str(config_path)
    env["TF_IN_AUTOMATION"] = "1"
    env["CHECKPOINT_DISABLE"] = "1"
    if trace:
        env["TF_LOG"] = "TRACE"
    return env


def case5():
    req = kit.build_required()
    root = smallest_probe_root(req)
    search = kit.default_search_dirs()
    needed = [p for p in req["providers"] if root and any(r == root["root"] or r.startswith(root["root"] + "/") for r in p["roots"])]
    if not root or not needed:
        record(5, "FAIL", "no module-free locked root to probe")
        return 0
    missing = [p for p in needed if not kit.candidates(p["source"], p["version"], search, kit.PLATFORM)]
    if missing:
        record(5, "SKIPPED-NOT-ON-BOX", "root %s needs %s; search of %d dirs found none"
               % (root["root"], ",".join("%s@%s" % (p["source"], p["version"]) for p in missing), len(search)))
        return 1
    with tempfile.TemporaryDirectory() as td:
        base = pathlib.Path(td)
        mirror = base / "mirror"
        summary, _m = kit.pack(needed, search, mirror)
        res = kit.verify(mirror)
        cfg = base / "probe.rc"
        cfg.write_text(kit.config_snippet(mirror), encoding="utf-8")
        copy = base / "root"
        shutil.copytree(str(kit.TF_BASE / root["root"]), str(copy), ignore=shutil.ignore_patterns(".terraform", "tests", "*.tfstate"))
        cmd = kit.terraform_init_command()
        try:
            p = subprocess.run(cmd, cwd=str(copy), env=terraform_env(cfg, trace=True), capture_output=True, text=True, timeout=600)
            out, rc = p.stdout + p.stderr, p.returncode
        except subprocess.TimeoutExpired:
            out, rc = "TIMEOUT", 124
        # control: the same init with an EMPTY mirror and the registry excluded must fail, never reaching for a registry
        empty = base / "empty"
        empty.mkdir()
        cfg2 = base / "empty.rc"
        cfg2.write_text(kit.config_snippet(empty), encoding="utf-8")
        copy2 = base / "root2"
        shutil.copytree(str(kit.TF_BASE / root["root"]), str(copy2), ignore=shutil.ignore_patterns(".terraform", "tests", "*.tfstate"))
        try:
            p2 = subprocess.run(cmd, cwd=str(copy2), env=terraform_env(cfg2), capture_output=True, text=True, timeout=600)
            out2, rc2 = p2.stdout + p2.stderr, p2.returncode
        except subprocess.TimeoutExpired:
            out2, rc2 = "TIMEOUT", 124
        mirror_lines = [x for x in out.splitlines() if "ProviderInstallationFilesystemMirror" in x or "InstallPackage: installing" in x]
        installed = [x for x in out.splitlines() if "Installing" in x or "Installed" in x or "successfully initialized" in x.lower()] + mirror_lines
        for line in installed:
            print("  init> %s" % line.strip())
        print("  control (empty mirror, registry excluded): rc=%d %s" % (rc2, " / ".join(x.strip() for x in out2.splitlines() if x.strip())[:300]))
        ok = (rc == 0 and "successfully initialized" in out.lower() and res["verified"] == res["files"] and rc2 != 0
              and "Installing" in out and not summary["not_on_box"]
              and any("ProviderInstallationFilesystemMirror" in x for x in mirror_lines)
              and any("excludes [registry.terraform.io/*/*]" in x for x in out.splitlines()))
        record(5, "PASS" if ok else "FAIL", "root %s init rc=%d; mirror files verified=%d/%d; control rc=%d (init without the mirror's provider fails: no registry fallback)"
               % (root["root"], rc, res["verified"], res["files"], rc2))
        if not ok:
            print("  init output: %s" % out[:1500])
    return 0


def case6():
    cmds = kit.constructed_commands()
    forbidden = "providers" + " mirror"
    bad = [c for c in cmds if forbidden in c or "://" in c or kit.HOST + "/" in c.replace(kit.HOST + "/*/*", "")]
    src = TOOL.read_text(encoding="utf-8")
    src_bad = [x for x in src.splitlines() if "://" in x or forbidden in x]
    non_ascii = sum(1 for ch in src if ord(ch) > 127)
    ok = not bad and not src_bad and non_ascii == 0 and len(cmds) >= 2
    record(6, "PASS" if ok else "FAIL", "%d constructed command strings; offending=%d; source lines with a URL or the download verb=%d; non-ascii=%d"
           % (len(cmds), len(bad), len(src_bad), non_ascii))


def norm(path):
    return os.path.normcase(os.path.abspath(str(path))).removesuffix(".exe")


def wrapper_block():
    """The wrapper's own resolution block, cut verbatim from .tools/safe-apply.sh (from the override test to its exit 5 and fi)."""
    text = (kit.ROOT / ".tools" / "safe-apply.sh").read_text(encoding="utf-8")
    m = re.search(r'^if \[ -n "\$\{SAFE_APPLY_TERRAFORM:-\}" \]; then.*?exit 5\nfi\n', text, re.S | re.M)
    return m.group(0) if m else None


def bash_resolution(block, script_dir, env):
    """Run the wrapper's own block in bash with SCRIPT_DIR set; -> the TERRAFORM path it picks, or None (exit 5)."""
    bash = shutil.which("bash")
    if not bash or not block:
        return "NO-BASH"
    script = 'SCRIPT_DIR="%s"\n%s\ncygpath -w "$TERRAFORM"\n' % (pathlib.Path(script_dir).as_posix(), block)
    p = subprocess.run([bash, "-c", script], capture_output=True, text=True, timeout=60, env=env)
    return p.stdout.strip().splitlines()[-1] if p.returncode == 0 and p.stdout.strip() else None


def real_binary():
    res = kit.resolve_binary()
    if res["path"] is None:
        return None
    return kit.describe_binary(res["path"], res["source"])


def case7():
    block = wrapper_block()
    with tempfile.TemporaryDirectory() as td:
        base = pathlib.Path(td)
        tools = base / "tools"
        tools.mkdir()
        sib = tools / "terraform.exe"
        ovr = base / "override.exe"
        pathdir = base / "pathdir"
        pathdir.mkdir()
        (pathdir / "terraform.exe").write_bytes(b"MZ-path")
        stand = {}
        # 1: nothing at all -> unresolved; 2: PATH only -> path; 3: sibling beats PATH; 4: override beats the sibling
        stand["none"] = kit.resolve_binary(tools, env={}, env_path=str(base / "empty"))["source"]
        stand["path"] = kit.resolve_binary(tools, env={}, env_path=str(pathdir))["source"]
        sib.write_bytes(b"MZ-sibling")
        stand["sibling"] = kit.resolve_binary(tools, env={}, env_path=str(pathdir))["source"]
        ovr.write_bytes(b"MZ-override")
        stand["override"] = kit.resolve_binary(tools, env={kit.OVERRIDE_ENV: str(ovr)}, env_path=str(pathdir))["source"]
        want = {"none": None, "path": "path", "sibling": "sibling", "override": "override"}
        order_ok = stand == want
        # the wrapper's own text, run in bash on the sibling-beats-PATH stand-in, picks the same file
        env = dict(os.environ)
        env.pop(kit.OVERRIDE_ENV, None)
        env["PATH"] = str(pathdir) + os.pathsep + env.get("PATH", "")
        bash_pick = bash_resolution(block, tools, env)
        mine = kit.resolve_binary(tools, env={}, env_path=env["PATH"])["path"]
        stand_ok = bash_pick == "NO-BASH" or (bash_pick is not None and norm(bash_pick) == norm(mine))
    # on this box: the kit and the wrapper block agree, from the base checkout's .tools
    base_tools = kit.wrapper_tools_dir()
    env2 = dict(os.environ)
    real = kit.resolve_binary()
    bash_real = bash_resolution(block, base_tools, env2)
    real_ok = real["path"] is not None and (bash_real == "NO-BASH" or (bash_real is not None and norm(bash_real) == norm(real["path"])))
    rc, txt = run_tool("binary")
    ll = last_line(txt)
    ok = (order_ok and stand_ok and real_ok and rc == 0 and ll.startswith("TF-BINARY found=True") and "ok=True" in ll and block is not None)
    record(7, "PASS" if ok else "FAIL", "order stand-ins %s (want %s); wrapper block vs kit on stand-in: %s; on this box wrapper=%s kit=%s source=%s | %s"
           % (stand, want, bash_pick, bash_real, str(real["path"]).replace("\\", "/"), real["source"], ll))


def marker_runner(marker, version, platform):
    def runner(path):
        pathlib.Path(marker).write_text("executed %s" % path, encoding="utf-8")
        return 0, json.dumps({"terraform_version": version, "platform": platform})
    return runner


def case8():
    rb = real_binary()
    if rb is None or rb["rc"] != 0:
        record(8, "SKIPPED-NOT-ON-BOX", "no terraform binary resolves by the wrapper order")
        return 1
    with tempfile.TemporaryDirectory() as td:
        base = pathlib.Path(td)
        search, target = make_standin(base)
        out = base / "pack"
        summary, manifest = kit.pack([target], [search], out, binary=rb)
        mb = manifest.get("binary") or {}
        placed = out / "bin" / "terraform.exe"
        rc_v, txt_v = run_tool("verify", "--from", str(out), "--run-binary")
        ll = last_line(txt_v)
        target_bin = base / "dell_tools" / "terraform.exe"
        rc_i, txt_i = run_tool("verify", "--from", str(out), "--install-binary", str(target_bin))
        installed_ok = target_bin.is_file() and kit.sha256_file(target_bin) == rb["sha256"] and "re-verified" in txt_i
        rc_i2, txt_i2 = run_tool("verify", "--from", str(out), "--install-binary", str(target_bin))
        # a different file already at the target is never overwritten
        other = base / "other_tools" / "terraform.exe"
        other.parent.mkdir()
        other.write_bytes(b"MZ-some-other-file")
        rc_i3, txt_i3 = run_tool("verify", "--from", str(out), "--install-binary", str(other))
        refuse_ok = rc_i3 == 1 and "REFUSED to overwrite" in txt_i3 and other.read_bytes() == b"MZ-some-other-file"
        # --no-binary shape: pack with no binary carries none
        summary2, manifest2 = kit.pack([target], [search], base / "pack2")
        ok = (placed.is_file() and mb.get("sha256") == rb["sha256"] and mb.get("version") == rb["version"] and mb.get("platform") == rb["platform"]
              and mb.get("size") == rb["size"] and rc_v == 0 and "run=ok" in ll and "binary=ok" in ll and "ok=True" in ll
              and rc_i == 0 and installed_ok and rc_i2 == 0 and "identical" in txt_i2 and refuse_ok
              and "binary" not in manifest2 and not (base / "pack2" / "bin").exists() and "BINARY-PLACEMENT" in txt_v)
        record(8, "PASS" if ok else "FAIL", "binary packed (%s, %d bytes, %s); %s; install re-verified=%s, repeat identical rc=%d, different target refused=%s; no-binary pack has none"
               % (mb.get("version"), mb.get("size", 0), "linked" if summary["linked"] > 2 else "copied", ll, installed_ok, rc_i2, refuse_ok))
    return 0


def case9():
    with tempfile.TemporaryDirectory() as td:
        base = pathlib.Path(td)
        search, target = make_standin(base)
        stand_bin = base / "stand_terraform.exe"
        stand_bin.write_bytes(b"MZ-stand-in-terraform-binary-" * 2048)
        info = {"path": stand_bin, "source": "stand-in", "version": "9.9.9", "platform": "windows_amd64"}
        out = base / "pack"
        kit.pack([target], [search], out, binary=info)
        marker = base / "marker.txt"
        runner = marker_runner(marker, "9.9.9", "windows_amd64")
        # positive control: an untouched pack IS executed through the runner and leaves the marker
        good = kit.verify(out, run_binary=True, runner=runner)
        control_ok = marker.is_file() and good["binary_run"] == "ok" and not good["problems"]
        marker.unlink()
        # tamper one byte of the packed binary (a copy, never the source), then verify with --run-binary
        placed = out / "bin" / "terraform.exe"
        data = bytearray(placed.read_bytes())
        data[100] ^= 0xFF
        placed.unlink()
        placed.write_bytes(bytes(data))
        bad = kit.verify(out, run_binary=True, runner=runner)
        in_proc_ok = (bad["binary"] == "mismatch" and bad["binary_run"] == "refused-before-run" and not marker.exists())
        rc, txt = run_tool("verify", "--from", str(out), "--run-binary")
        ll = last_line(txt)
        cli_ok = (rc == 1 and "REFUSED" in txt and "the binary was not executed" in txt and "run=refused-before-run" in ll
                  and "BINARY-RUN" not in txt.replace("BINARY-RUN reported", "") and "binary=mismatch" in ll and "ok=False" in ll)
        src_intact = stand_bin.read_bytes() != bytes(data)
        ok = control_ok and in_proc_ok and cli_ok and src_intact
        record(9, "PASS" if ok else "FAIL", "control: untouched pack executed (marker written=%s); one byte flipped -> binary=%s run=%s, runner marker absent=%s; CLI rc=%d %s"
               % (control_ok, bad["binary"], bad["binary_run"], not marker.exists(), rc, ll))


def case10():
    rb = real_binary()
    if rb is None or rb["rc"] != 0:
        record(10, "SKIPPED-NOT-ON-BOX", "no terraform binary resolves by the wrapper order")
        return 1
    main_tf = ('terraform {\n  backend "local" {\n    path = "terraform.tfstate"\n  }\n}\nlocals {\n  a = "x"\n}\n'
               'output "o" {\n  value = local.a\n}\n')
    state = ('{"version":4,"terraform_version":"%s","serial":1,"lineage":"00000000-0000-0000-0000-000000000001",'
             '"outputs":{"o":{"value":"x","type":"string"}},"resources":[],"check_results":null}\n' % rb["version"])
    with tempfile.TemporaryDirectory() as td:
        base = pathlib.Path(td)
        search, target = make_standin(base)
        mirror = base / "mirror"
        kit.pack([target], [search], mirror, binary=None)
        zero = base / "root_zero"
        zero.mkdir()
        (zero / "main.tf").write_text(main_tf, encoding="utf-8")
        (zero / "terraform.tfstate").write_text(state, encoding="utf-8")
        two = base / "root_two"
        two.mkdir()
        (two / "main.tf").write_text(main_tf, encoding="utf-8")
        rc0, txt0 = run_tool("readback", "--root", str(zero), "--from", str(mirror))
        rc2, txt2 = run_tool("readback", "--root", str(two), "--from", str(mirror))
        l0, l2 = last_line(txt0), last_line(txt2)
        ok0 = rc0 == 0 and "init=ok plan_exit=0 ok=True" in l0 and ("version=%s" % rb["version"]) in l0 and "(a) terraform version" in txt0
        # the control for the 0/2 distinction: a fresh output not yet in state reads 2, loudly, and is still not a kit failure
        ok2 = rc2 == 0 and "plan_exit=2 ok=True" in l2 and "CHANGES ARE PRESENT" in txt2
        ok = ok0 and ok2
        record(10, "PASS" if ok else "FAIL", "local-backend root with locals+outputs and a state holding them: %s; control (output not in state): %s" % (l0, l2))
        if not ok:
            print(txt0[-1500:])
            print(txt2[-1500:])
    return 0


def main():
    case1()
    case2()
    case3_4()
    skipped = case5()
    case6()
    case7()
    skipped += case8()
    case9()
    skipped += case10()
    passed = sum(1 for _c, s, _d in RESULTS if s == "PASS")
    failed = sum(1 for _c, s, _d in RESULTS if s == "FAIL")
    ok = failed == 0 and passed + skipped == 10
    print("TF-KIT-TEST cases=%d/10 skipped=%d ok=%s" % (passed + skipped, skipped, ok))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
