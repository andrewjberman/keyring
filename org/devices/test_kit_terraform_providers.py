"""test_kit_terraform_providers.py -- the Terraform provider kit, on this box and on stand-ins. NO NETWORK.

(1) required on the real tree; (2) located on this box; (3) pack into a temporary directory and verify; (4) one byte flipped, verify
refuses; (5) THE SEAM PROBE: a real `terraform init` against the packed mirror with a CLI config that installs only from the mirror and
excludes the registry; (6) no command the tool constructs, and no line of the tool's source, carries a registry address or a
downloading verb. LAST line: TF-KIT-TEST cases=<k>/6 skipped=<s> ok=<True|False>.
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
        ok4 = rc_v == 0 and rc_t == 1 and res2["mismatched"] == 1 and "REFUSED" in txt_t and "ok=False" in last_line(txt_t) and src_intact
        record(4, "PASS" if ok4 else "FAIL", "untouched verify rc=%d; one byte flipped -> rc=%d mismatched=%d; %s" % (rc_v, rc_t, res2["mismatched"], last_line(txt_t)))


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


def main():
    case1()
    case2()
    case3_4()
    skipped = case5()
    case6()
    passed = sum(1 for _c, s, _d in RESULTS if s == "PASS")
    failed = sum(1 for _c, s, _d in RESULTS if s == "FAIL")
    ok = failed == 0 and passed + skipped == 6
    print("TF-KIT-TEST cases=%d/6 skipped=%d ok=%s" % (passed + skipped, skipped, ok))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
