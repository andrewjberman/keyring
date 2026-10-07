"""test_kit_portal_tree.py -- the portal dependency-tree kit, on stand-ins and on this box. NO NETWORK, NO INSTALL.

(1) describe on a synthetic portal reads absent=0 ok=True (and equals_dev is read True / False / DEV-REF-ABSENT); (2) one package
directory removed -> absent=1 ok=False and pack refuses; (3) pack then verify passes; (4) one archive byte flipped -> archive=mismatch;
(5) the target's lockfile changed -> lockfile=differs; (6) a manifest with another bun version -> bun=differs (and another platform ->
platform=differs); (7) --extract into an empty target reproduces the file count and the portal's typecheck runs as read-back; (8) THE
REAL READ: describe on the base checkout's real portal, read-only, bounded to 100 seconds, plus the assertion that no command the tool
built is a package-manager fetch verb or names a registry. LAST line: PORTAL-KIT-TEST cases=<k>/8 ok=<True|False>.
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import time

HERE = pathlib.Path(__file__).resolve().parent
TOOL = HERE / "kit_portal_tree.py"
spec = importlib.util.spec_from_file_location("kit_portal_tree", str(TOOL))
kit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kit)

RESULTS = []
CRLF = bytes([13, 10])
LF = bytes([10])
LOCK = """{
  "lockfileVersion": 1,
  "workspaces": {
    "": {
      "name": "synthportal",
      "dependencies": {
        "alpha": "^1.0.0",
        "@scope/beta": "^2.0.0",
      },
    },
  },
  "packages": {
    "alpha": ["alpha@1.0.0", "", { "dependencies": { "gamma": "^3.0.0", }, }, "sha512-AAAA"],

    "@scope/beta": ["@scope/beta@2.1.0", "", {}, "sha512-BBBB"],

    "@scope/beta-linux-x64": ["@scope/beta-linux-x64@2.1.0", "", { "os": "linux", "cpu": "x64" }, "sha512-CCCC"],

    "gamma": ["gamma@3.4.5", "", {}, "sha512-DDDD"],
  }
}
"""


def record(case, ok, detail):
    RESULTS.append((case, ok))
    print("CASE %d %s: %s" % (case, "PASS" if ok else "FAIL", detail))


def run_kit(*args):
    """Run the tool in-process (so the commands it builds are captured); returns (rc, output)."""
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = kit.main(list(args))
    return rc, buf.getvalue()


def last_line(text):
    lines = [x for x in text.splitlines() if x.strip()]
    return lines[-1] if lines else ""


def write_pkg(root, name, version, extra=None, files=None):
    d = root / "node_modules" / name
    d.mkdir(parents=True, exist_ok=True)
    pj = {"name": name, "version": version}
    pj.update(extra or {})
    (d / "package.json").write_text(json.dumps(pj), encoding="utf-8")
    (d / "index.js").write_text("module.exports = %r;\n" % name * 20, encoding="utf-8")
    for fn, data in (files or {}).items():
        (d / fn).parent.mkdir(parents=True, exist_ok=True)
        (d / fn).write_bytes(data)


def make_portal(base, name, with_tree=True):
    root = base / name
    root.mkdir(parents=True)
    (root / "package.json").write_text(json.dumps({"name": "synthportal", "scripts": {"typecheck": "echo typecheck-ok"}}), encoding="utf-8")
    (root / "bun.lock").write_bytes(LOCK.replace("\n", "\r\n").encode("utf-8"))  # CRLF on purpose: the hash folds line endings
    if with_tree:
        write_pkg(root, "alpha", "1.0.0")
        write_pkg(root, "@scope/beta", "2.1.0", files={"native/addon.node": b"\x00" * 64})
        write_pkg(root, "gamma", "3.4.5")
        # a nested copy and a dot-directory the walk must count but not treat as a package
        write_pkg(root / "node_modules" / "alpha", "gamma-nested", "0.0.1")
        (root / "node_modules" / ".bin").mkdir()
        (root / "node_modules" / ".bin" / "alpha.cmd").write_text("@echo off\n", encoding="utf-8")
    return root


def parse_tree(line):
    return dict(re.findall(r"(\w+)=(\S+)", line))


def git(args, cwd, env=None):
    e = dict(os.environ)
    e.update(env or {})
    return subprocess.run(["git"] + args, cwd=str(cwd), capture_output=True, text=True, env=e, check=True).stdout.strip()


def make_dev_ref(portal, lock_bytes):
    """Turn the synthetic portal into a repository whose refs/remotes/origin/DEV holds the given lockfile (plumbing only)."""
    git(["init", "-q"], portal)
    blob = subprocess.run(["git", "hash-object", "-w", "--stdin"], cwd=str(portal), input=lock_bytes, capture_output=True,
                          check=True).stdout.decode().strip()
    git(["update-index", "--add", "--cacheinfo", "100644,%s,bun.lock" % blob], portal)
    tree = git(["write-tree"], portal)
    env = {"GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t", "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t"}
    commit = git(["commit-tree", tree, "-m", "synthetic"], portal, env)
    git(["update-ref", "refs/remotes/origin/DEV", commit], portal)


def case1(base):
    root = make_portal(base, "p1")
    rc, out = run_kit("describe", "--portal", str(root))
    t = parse_tree(last_line(out))
    ok = rc == 0 and t.get("absent") == "0" and t.get("ok") == "True" and t.get("packages") == "4" and t.get("present") == "3"
    ok = ok and t.get("equals_dev") == "DEV-REF-ABSENT" and "OPTIONAL-OTHER-PLATFORM=1" in out and "PORTAL-PLATFORM-SPECIFIC installed=1" in out
    # equals_dev arms: same lockfile (only the line endings differ) -> True; a different lockfile -> False
    lock_bytes = (root / "bun.lock").read_bytes()
    make_dev_ref(root, lock_bytes.replace(CRLF, LF))
    _rc, out_true = run_kit("describe", "--portal", str(root))
    eq_t = parse_tree(last_line(out_true)).get("equals_dev")
    ok = ok and eq_t == "True"
    # a real content difference must read False
    (root / "bun.lock").write_bytes(lock_bytes.replace(b"3.4.5", b"3.4.6"))
    _rc, out_diff = run_kit("describe", "--portal", str(root))
    eq_d = parse_tree(last_line(out_diff)).get("equals_dev")
    ok = ok and eq_d == "False"
    record(1, ok, "describe synthetic: %s | equals_dev same=%s differs=%s" % (last_line(out)[:230], eq_t, eq_d))


def case2(base):
    root = make_portal(base, "p2")
    shutil.rmtree(str(root / "node_modules" / "gamma"))
    rc, out = run_kit("describe", "--portal", str(root))
    t = parse_tree(last_line(out))
    out_dir = base / "pack2"
    rc2, out2 = run_kit("pack", "--portal", str(root), "--out", str(out_dir))
    refused = rc2 != 0 and "REFUSED" in out2 and not (out_dir / kit.ARCHIVE).exists()
    ok = rc != 0 and t.get("absent") == "1" and t.get("ok") == "False" and refused
    record(2, ok, "package removed: %s | pack rc=%s refused=%s archive_written=%s" % (
        last_line(out)[-120:], rc2, "REFUSED" in out2, (out_dir / kit.ARCHIVE).exists()))


def case3(base, root):
    pdir = base / "pack3"
    rc, out = run_kit("pack", "--portal", str(root), "--out", str(pdir))
    man = json.loads((pdir / kit.MANIFEST).read_text(encoding="utf-8"))
    target = make_portal(base, "t3", with_tree=False)
    rc2, out2 = run_kit("verify", "--from", str(pdir), "--portal", str(target))
    ll = last_line(out2)
    ok = rc == 0 and rc2 == 0 and "archive=ok lockfile=ok bun=ok node=ok platform=ok extracted=- ok=True" in ll
    ok = ok and man["lockfile"]["name"] == "bun.lock" and man["bun"] == kit.tool_version("bun") and man["node"] == kit.tool_version("node")
    ok = ok and man["platform_specific"] and man["archive"]["sha256"] == kit.sha256_file(pdir / kit.ARCHIVE) and man["format"] == "tar+gzip-1"
    record(3, ok, "pack %s | verify %s | manifest lockfile sha=%s bun=%s node=%s files=%s platform_specific=%d" % (
        last_line(out)[:110], ll, man["lockfile"]["sha256"][:12], man["bun"], man["node"], man["files"], len(man["platform_specific"])))
    return pdir, man


def case4(base, pdir):
    bad = base / "pack4"
    shutil.copytree(str(pdir), str(bad))
    arc = bad / kit.ARCHIVE
    data = bytearray(arc.read_bytes())
    data[len(data) // 2] ^= 0xFF
    arc.write_bytes(bytes(data))
    target = make_portal(base, "t4", with_tree=False)
    rc, out = run_kit("verify", "--from", str(bad), "--portal", str(target), "--extract")
    ll = last_line(out)
    ok = rc != 0 and "archive=mismatch" in ll and "extracted=- ok=False" in ll and not (target / "node_modules").exists()
    record(4, ok, "one byte flipped: %s" % ll)


def case5(base, pdir):
    target = make_portal(base, "t5", with_tree=False)
    (target / "bun.lock").write_bytes((target / "bun.lock").read_bytes().replace(b"3.4.5", b"3.4.6"))
    rc, out = run_kit("verify", "--from", str(pdir), "--portal", str(target), "--extract")
    ll = last_line(out)
    ok = rc != 0 and "lockfile=differs" in ll and "archive=ok" in ll and "ok=False" in ll and not (target / "node_modules").exists()
    record(5, ok, "target lockfile changed: %s" % ll)


def case6(base, pdir):
    alt = base / "pack6"
    shutil.copytree(str(pdir), str(alt))
    man = json.loads((alt / kit.MANIFEST).read_text(encoding="utf-8"))
    man["bun"] = "0.0.1-other"
    (alt / kit.MANIFEST).write_text(json.dumps(man), encoding="utf-8")
    target = make_portal(base, "t6", with_tree=False)
    rc, out = run_kit("verify", "--from", str(alt), "--portal", str(target), "--extract")
    ll = last_line(out)
    man["bun"] = kit.tool_version("bun")
    man["platform"]["os"] = "linux" if man["platform"]["os"] != "linux" else "win32"
    (alt / kit.MANIFEST).write_text(json.dumps(man), encoding="utf-8")
    rc2, out2 = run_kit("verify", "--from", str(alt), "--portal", str(target), "--extract")
    ll2 = last_line(out2)
    man["platform"]["os"] = kit.this_platform()[0]
    man["node"] = "v0.0.1-other"
    (alt / kit.MANIFEST).write_text(json.dumps(man), encoding="utf-8")
    rc3, out3 = run_kit("verify", "--from", str(alt), "--portal", str(target))
    ll3 = last_line(out3)
    ok = rc != 0 and "bun=differs" in ll and "extracted=- ok=False" in ll
    ok = ok and rc2 != 0 and "platform=differs" in ll2 and rc3 != 0 and "node=differs" in ll3 and not (target / "node_modules").exists()
    record(6, ok, "manifest bun other: %s | platform other: %s | node other: %s" % (ll, ll2[-60:], ll3[-80:]))


def case7(base, pdir, man):
    target = make_portal(base, "t7", with_tree=False)
    rc, out = run_kit("verify", "--from", str(pdir), "--portal", str(target), "--extract")
    ll = last_line(out)
    m = re.search(r"extracted=(\d+)", ll)
    count = int(m.group(1)) if m else -1
    again_rc, again = run_kit("verify", "--from", str(pdir), "--portal", str(target), "--extract")
    refused_nonempty = again_rc != 0 and "REFUSED" in again and "--replace" in again
    rep_rc, rep = run_kit("verify", "--from", str(pdir), "--portal", str(target), "--extract", "--replace")
    desc_rc, desc = run_kit("describe", "--portal", str(target))
    tc_rc, tc = run_kit("typecheck", "--portal", str(target), "--timeout", "60")
    tcl = last_line(tc)
    ok = rc == 0 and count == man["files"] and "ok=True" in ll and refused_nonempty and rep_rc == 0
    ok = ok and desc_rc == 0 and "absent=0" in last_line(desc) and tc_rc == 0 and "exit=0" in tcl and "last_line=typecheck-ok " in tcl
    # a script the package.json does not name is refused, never guessed
    miss_rc, miss = run_kit("typecheck", "--portal", str(target), "--script", "no-such-script")
    ok = ok and miss_rc != 0 and "REFUSED" in miss
    record(7, ok, "extract: %s (manifest files=%d) | nonempty refused=%s replace rc=%s | describe after: %s | typecheck: %s" % (
        ll, man["files"], refused_nonempty, rep_rc, last_line(desc)[-70:], tcl))


FORBIDDEN_TOKENS = {"install", "add", "ci", "i", "update", "upgrade", "x", "create", "init", "pm", "link", "dlx"}
GIT_READ = {"rev-parse", "show", "branch", "worktree", "ls-files", "cat-file"}


def bad_command(argv):
    exe = os.path.basename(argv[0]).lower()
    exe = re.sub(r"\.(exe|cmd|bat)$", "", exe)
    if exe in ("npm", "npx", "yarn", "pnpm", "bunx", "pip", "curl", "wget"):
        return "package-manager or download tool %s" % exe
    for tok in argv[1:]:
        low = tok.lower()
        if "http://" in low or "https://" in low or "registry" in low:
            return "registry/URL in %r" % tok
    if exe == "bun":
        rest = argv[1:]
        if rest[:1] == ["--version"] or (rest[:1] == ["run"] and "--no-install" in rest):
            return None
        return "bun verb %r is not --version or `run --no-install`" % rest[:1]
    if exe == "node":
        return None if argv[1:] == ["--version"] else "node with %r" % argv[1:]
    if exe == "git":
        rest = argv[1:]
        if rest[:1] == ["-C"]:
            rest = rest[2:]
        return None if rest[:1] and rest[0] in GIT_READ else "git verb %r is not a read verb" % rest[:1]
    return "unexpected executable %s" % exe


def case8(commands_before):
    # THE REAL READ: a subprocess so the 100 s bound is a real kill; commands logged through the tool's own choke point.
    with tempfile.TemporaryDirectory() as td:
        log = pathlib.Path(td) / "commands.jsonl"
        env = dict(os.environ)
        env[kit.COMMAND_LOG_ENV] = str(log)
        t0 = time.time()
        try:
            p = subprocess.run([sys.executable, str(TOOL), "describe"], capture_output=True, text=True, timeout=100, env=env)
        except subprocess.TimeoutExpired:
            print("REAL-READ-TIMEOUT after 100 s: describe did not finish on the real portal")
            record(8, False, "REAL-READ-TIMEOUT")
            return
        secs = round(time.time() - t0, 1)
        line = last_line(p.stdout)
        real_cmds = [json.loads(x) for x in log.read_text(encoding="utf-8").splitlines() if x.strip()] if log.exists() else []
    print("REAL PORTAL-TREE (%ss, rc=%s): %s" % (secs, p.returncode, line))
    all_cmds = list(commands_before) + real_cmds
    bad = [(c, bad_command(c)) for c in all_cmds if bad_command(c)]
    src = TOOL.read_text(encoding="utf-8")
    src_hits = re.findall(r"[\"'](install|add|ci|i|npm|npx|yarn|pnpm|bunx)[\"']|https?://", src)
    completed = line.startswith("PORTAL-TREE ") and p.returncode in (0, 1)
    ok = completed and not bad and not src_hits and len(real_cmds) >= 4
    record(8, ok, "real read completed=%s in %ss; commands checked=%d (synthetic %d + real %d) bad=%s; source verb/URL hits=%s" % (
        completed, secs, len(all_cmds), len(commands_before), len(real_cmds), bad[:3], src_hits[:3]))


def main():
    with tempfile.TemporaryDirectory() as td:
        base = pathlib.Path(td)
        try:
            case1(base)
            case2(base)
            root = make_portal(base, "p3")
            pdir, man = case3(base, root)
            case4(base, pdir)
            case5(base, pdir)
            case6(base, pdir)
            case7(base, pdir, man)
        except Exception as exc:  # a crash is a failed case, never a skipped one
            print("CRASH: %r" % (exc,))
            import traceback
            traceback.print_exc()
        case8(list(kit.COMMANDS_BUILT))
    passed = sum(1 for _c, ok in RESULTS if ok)
    done = {c for c, _ok in RESULTS}
    allok = passed == 8 and done == set(range(1, 9))
    print("PORTAL-KIT-TEST cases=%d/8 ok=%s" % (passed, allok))
    return 0 if allok else 1


if __name__ == "__main__":
    sys.exit(main())
