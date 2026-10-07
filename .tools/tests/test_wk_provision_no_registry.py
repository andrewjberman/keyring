"""test_wk_provision_no_registry.py -- `.tools/wk-provision.sh` and the registry: the install mode refuses, link and none are unchanged.

Runs the REAL script on SCRATCH repositories built by this test (a superproject with a `portal` gitlink and a nested portal
repository), under the harness environment of org/devices/kit_bun_no_egress.py: a loopback registry listener and a loopback proxy
listener, the proxy variables pointing at the proxy, an isolated temporary HOME. A fake `bun` placed first on PATH records every
call and does nothing, and the test proves the fake is the `bun` the script will resolve BEFORE any provision runs, so the real bun
is never started and no bun install ever runs.

Arms (each a full `provision` on the scratch repository):
  A install, no registry redirect        -> rc 2, REFUSED line naming link and none, no worktree created, fake bun never called
  B install, redirect to a PUBLIC host   -> refused the same way
  C install, redirect to a loopback host -> not refused; the fake bun records `install --frozen-lockfile` (the allowed branch)
  D no --node-modules (the default)      -> `NODE_MODULES: link`
  E --node-modules none / F link         -> `NODE_MODULES: none` / `NODE_MODULES: link`
  G the same three runs of the script as it stood before this change (git object pinned below) print the same lines (paths and
    branch names normalised): link and none behave exactly as before.
Zero requests must reach either listener across all arms.
LAST line: WK-PROVISION-REGISTRY install_refused=<True|False> requests=<n> default=<mode> ok=<True|False>
"""
from __future__ import annotations

import importlib.util
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[2]
SCRIPT = ROOT / ".tools" / "wk-provision.sh"
PRE_CHANGE_OBJECT = "69288c8ca0:.tools/wk-provision.sh"  # the script as it stood before the install-mode refusal

spec = importlib.util.spec_from_file_location("kit_bun_no_egress", str(ROOT / "org" / "devices" / "kit_bun_no_egress.py"))
kit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kit)
sys.path.insert(0, str(ROOT / ".tools"))
import git_bash_resolver  # noqa: E402

FAKE_BUN = "#!/usr/bin/env bash\necho \"$@\" >> \"$(dirname \"$0\")/bun.calls\"\nexit 0\n"
CHECKS = []


def _make_writable(func, path, _exc):
    """git object files are read-only on Windows: make them writable and retry the removal of this test's OWN scratch tree."""
    os.chmod(path, 0o700)
    func(path)


def check(name, ok, detail):
    CHECKS.append((name, ok))
    print("CHECK %s %s: %s" % (name, "PASS" if ok else "FAIL", detail))


def git(cwd, *args, env=None):
    base = ["git", "-c", "user.name=scratch", "-c", "user.email=scratch@example.invalid", "-c", "commit.gpgsign=false"]
    return subprocess.run(base + list(args), cwd=str(cwd), capture_output=True, text=True, env=env, timeout=60)


def build_scratch(base):
    """A superproject with a `portal` gitlink, and a nested portal repository that holds a node_modules directory to link to."""
    main = base / "main"
    nested = main / "portal"
    nested.mkdir(parents=True)
    git(nested, "init", "-q")
    (nested / "package.json").write_text('{"name":"scratch-portal"}\n', encoding="ascii")
    git(nested, "add", "package.json")
    git(nested, "commit", "-q", "--no-verify", "-m", "portal")
    nested_sha = git(nested, "rev-parse", "HEAD").stdout.strip()
    (nested / "node_modules" / "pkg").mkdir(parents=True)
    (nested / "node_modules" / "pkg" / "index.js").write_text("module.exports = 1;\n", encoding="ascii")
    git(main, "init", "-q")
    (main / "README").write_text("scratch\n", encoding="ascii")
    git(main, "add", "README")
    git(main, "update-index", "--add", "--cacheinfo", "160000,%s,portal" % nested_sha)
    git(main, "commit", "-q", "--no-verify", "-m", "super")
    return main, nested


def run_script(script, main, env, *args):
    argv = git_bash_resolver.bash_argv(str(script), *args)
    proc = subprocess.run(argv, cwd=str(main), env=env, capture_output=True, text=True, timeout=110)
    return proc.returncode, proc.stdout, proc.stderr


def normalise(text, base):
    text = text.replace(str(base).replace("\\", "/"), "<S>").replace(str(base), "<S>")
    text = re.sub(r"wt[A-Z]+\w*", "WT", text)
    text = re.sub(r"wk-[A-Z]+\w*-1", "BR", text)
    text = re.sub(r"[0-9a-f]{40}", "SHA", text)
    return "\n".join(x.strip() for x in text.splitlines() if x.strip())


def main():
    reg, prx = kit.RegistryListener(), kit.ProxyListener()
    base_dir, _ = kit.pick_tmp_base()
    scratch = pathlib.Path(tempfile.mkdtemp(prefix="wkprov-test-", dir=str(base_dir)))
    default_mode = "unknown"
    install_refused = False
    total_requests = 0
    try:
        listener_check = kit.selfcheck_listeners()
        check("listeners", listener_check["ok"], "the loopback listeners logged the Python-made requests before any provision ran")
        main_repo, nested = build_scratch(scratch)
        fake = scratch / "fakebin"
        fake.mkdir()
        (fake / "bun").write_text(FAKE_BUN, encoding="ascii", newline="\n")
        calls = fake / "bun.calls"
        run_root = scratch / "env"
        run_root.mkdir()
        env = kit.build_env(run_root, prx.url, {}, {})
        for key in [k for k in env if k.upper().startswith("GIT_")]:
            del env[key]
        env["PATH"] = str(fake) + os.pathsep + env.get("PATH", "")
        env_redirect = dict(env)
        env_redirect["BUN_CONFIG_REGISTRY"] = reg.url
        env_public = dict(env)
        env_public["BUN_CONFIG_REGISTRY"] = "https://registry.npmjs.org/"
        # the fake must be what the script resolves: prove it before any provision runs
        resolved = subprocess.run(git_bash_resolver.bash_argv("-c", "command -v bun"), env=env, capture_output=True, text=True,
                                  timeout=60).stdout.strip().lower().replace("\\", "/")
        fake_here = str(fake).lower().replace("\\", "/")
        fake_first = resolved.endswith("/fakebin/bun") or fake_here.split(":", 1)[-1] in resolved
        check("fake-bun-first", fake_first, "command -v bun under the test environment resolves to %s" % resolved)
        if not fake_first:
            print("WK-PROVISION-REGISTRY install_refused=False requests=0 default=unknown ok=False")
            return 1

        # bash -n on the script itself: syntax
        syntax = subprocess.run(git_bash_resolver.bash_argv("-n", str(SCRIPT)), capture_output=True, text=True, timeout=60)
        check("syntax", syntax.returncode == 0, "bash -n .tools/wk-provision.sh rc=%d %s" % (syntax.returncode, syntax.stderr.strip()))

        # A: install, no redirect
        path_a = scratch / "wtA"
        rc_a, out_a, err_a = run_script(SCRIPT, main_repo, env, "provision", "TSTA", "1", "--path", str(path_a), "--node-modules", "install")
        refusal_line = [x for x in err_a.splitlines() if x.startswith("REFUSED:")]
        refused_a = (rc_a == 2 and len(refusal_line) == 1 and "link" in refusal_line[0] and "none" in refusal_line[0]
                     and not path_a.exists() and not calls.exists())
        check("A-install-no-redirect", refused_a, "rc=%s; %s; worktree created=%s; fake bun called=%s"
              % (rc_a, refusal_line[0] if refusal_line else "NO REFUSED LINE: " + err_a.strip()[:200], path_a.exists(), calls.exists()))

        # B: install, redirect to a public host
        path_b = scratch / "wtB"
        rc_b, out_b, err_b = run_script(SCRIPT, main_repo, env_public, "provision", "TSTB", "1", "--path", str(path_b), "--node-modules",
                                        "install")
        refused_b = rc_b == 2 and "REFUSED:" in err_b and not path_b.exists() and not calls.exists()
        check("B-install-public-redirect", refused_b, "rc=%s; worktree created=%s; fake bun called=%s" % (rc_b, path_b.exists(), calls.exists()))
        install_refused = bool(refused_a and refused_b)

        # C: install, redirect to loopback -> allowed branch, the FAKE bun is called
        path_c = scratch / "wtC"
        rc_c, out_c, err_c = run_script(SCRIPT, main_repo, env_redirect, "provision", "TSTC", "1", "--path", str(path_c), "--node-modules",
                                        "install")
        recorded = calls.read_text(encoding="ascii").strip() if calls.exists() else ""
        check("C-install-loopback-redirect", rc_c == 0 and recorded == "install --frozen-lockfile" and "NODE_MODULES: install" in out_c,
              "rc=%s; fake bun recorded %r; %s" % (rc_c, recorded, err_c.strip()[:160]))

        # D/E/F with the new script, G the same three with the pre-change script
        old_script = scratch / "wk-provision.pre-change.sh"
        shown = subprocess.run(["git", "show", PRE_CHANGE_OBJECT], cwd=str(ROOT), capture_output=True, timeout=60)
        have_old = shown.returncode == 0 and len(shown.stdout) > 1000
        if have_old:
            old_script.write_bytes(shown.stdout)
        modes = (("D", "default", None), ("E", "none", "none"), ("F", "link", "link"))
        new_outputs = {}
        for label, name, flag in modes:
            code = "TST" + label
            path = scratch / ("wt" + label)
            args = ["provision", code, "1", "--path", str(path)] + (["--node-modules", flag] if flag else [])
            rc, out, err = run_script(SCRIPT, main_repo, env, *args)
            node_line = [x for x in out.splitlines() if x.startswith("NODE_MODULES:")]
            expect = {"default": "NODE_MODULES: link", "none": "NODE_MODULES: none", "link": "NODE_MODULES: link"}[name]
            check("%s-%s" % (label, name), rc == 0 and bool(node_line) and node_line[0].startswith(expect),
                  "rc=%s; %s" % (rc, node_line[0] if node_line else err.strip()[:200]))
            new_outputs[name] = (rc, normalise(out, scratch))
            if name == "default" and node_line:
                default_mode = node_line[0].split(":", 1)[1].strip().split()[0]
        if have_old:
            same = []
            for label, name, flag in modes:
                code = "OLD" + label
                path = scratch / ("wtOLD" + label)
                args = ["provision", code, "1", "--path", str(path)] + (["--node-modules", flag] if flag else [])
                rc, out, err = run_script(old_script, main_repo, env, *args)
                same.append((rc, normalise(out, scratch)) == new_outputs[name])
            check("G-link-and-none-unchanged", all(same), "the pre-change script (%s) and the new script print the same lines and exit codes "
                  "for default, none and link: %s of %s" % (PRE_CHANGE_OBJECT.split(":")[0], sum(same), len(same)))
        else:
            print("CHECK G-link-and-none-unchanged SKIPPED-NOT-AVAILABLE: git object %s not readable here" % PRE_CHANGE_OBJECT)
        requests = len(reg.log.take()) + len(prx.log.take())
        total_requests += requests
        check("zero-requests", requests == 0, "requests on the registry and proxy listeners across every arm: %d" % requests)
    finally:
        total_requests += len(reg.log.take()) + len(prx.log.take())
        reg.close()
        prx.close()
        for wt in scratch.glob("wt*"):
            junction = wt / "portal" / "node_modules"
            try:
                os.rmdir(str(junction))  # removes a junction (the target stays); fails harmlessly on a real non-empty directory
            except OSError:
                pass
        if sys.version_info >= (3, 12):
            shutil.rmtree(str(scratch), onexc=_make_writable)
        else:
            shutil.rmtree(str(scratch), onerror=_make_writable)
    ok = all(ok for _n, ok in CHECKS) and len(CHECKS) >= 9 and install_refused and default_mode == "link" and total_requests == 0
    print("WK-PROVISION-REGISTRY install_refused=%s requests=%d default=%s ok=%s" % (install_refused, total_requests, default_mode, ok))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
