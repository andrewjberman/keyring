"""test_kit_bun_no_egress.py -- the bun no-egress kit, measured against loopback listeners. NO REQUEST LEAVES THIS MACHINE.

(1) the two listeners log requests made by Python itself (the listener works) -- run before any bun process; (2) `measure` on this
machine reads ok=True; (3) `wrap` refuses install / add / x / create / update without running bun, and its --allow-registry decision
is loud (decided in-process: no registry verb is ever executed here); (4) `wrap -- --version` passes and made zero requests, run
inside the harness environment; (5) a planted regression -- the grader told to treat every candidate as passing, including the ones
that DID make a request -- is caught by the independent audit and turns ok False; (6) every bun process the measurement started ran
inside the harness: proxy variables on loopback, an isolated home, a directory outside this repository; (7) no arm ran a registry
verb, and this script's source bakes no bun path and no version number.
LAST line: BUN-KIT-TEST cases=<k>/7 ok=<True|False>.
"""
from __future__ import annotations

import importlib.util
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
TOOL = HERE / "kit_bun_no_egress.py"
spec = importlib.util.spec_from_file_location("kit_bun_no_egress", str(TOOL))
kit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kit)

RESULTS = []


def record(case, ok, detail):
    RESULTS.append((case, ok))
    print("CASE %d %s: %s" % (case, "PASS" if ok else "FAIL", detail))


def main():
    # (1) the listener works: Python-made requests, no bun process
    sc = kit.selfcheck_listeners()
    record(1, sc["ok"], "registry logged %r and answered 404=%s; proxy logged %d lines (CONNECT + absolute-URI GET) and answered 502"
           % (sc["registry_log"], sc["registry_answers_404"], len(sc["proxy_log"])))

    # (2) measure on this machine
    out_dir = pathlib.Path(tempfile.mkdtemp(prefix="kit-bun-test-", dir=str(kit.pick_tmp_base()[0])))
    out_json = out_dir / "measure.json"
    buf_lines = []

    class Tee:
        def write(self, text):
            buf_lines.append(text)
            sys.stdout.write(text)

        def flush(self):
            sys.stdout.flush()

    rc, result = kit.measure(str(out_json), None, Tee())
    last = [x for x in "".join(buf_lines).splitlines() if x.strip()][-1]
    ok2 = rc == 0 and result is not None and result["summary"]["ok"] and last.startswith("BUN-NO-EGRESS ") and last.endswith("ok=True")
    record(2, ok2, "measure rc=%s; %s" % (rc, last))

    # (3) wrap refuses a registry verb (subprocess: the real entry point), and the allow decision is loud (in-process only)
    refused = []
    for verb in (["install"], ["add", "left-pad"], ["x", "cowsay"], ["create", "vite"], ["update"], ["--cwd", "somewhere", "install"]):
        proc = subprocess.run([sys.executable, str(TOOL), "wrap", "--"] + verb, capture_output=True, text=True, timeout=60)
        refused.append(proc.returncode == 2 and "REFUSED" in proc.stderr and "link or none" in proc.stderr)
    act, msg = kit.decide(["install"], "test-only-decision-never-executed")
    loud = act == "ALLOW-REGISTRY" and msg.startswith("LOUD:") and "request may leave this machine" in msg
    act_i, _ = kit.decide(["--version"])
    record(3, all(refused) and loud and act_i == "PASS-INFO",
           "refused %d of %d verbs with rc=2 naming link or none; allow decision=%s (loud=%s); --version decision=%s"
           % (sum(refused), len(refused), act, loud, act_i))

    # (4) wrap -- --version passes, inside the harness environment, zero requests
    bun = shutil.which("bun")
    reg, prx = kit.RegistryListener(), kit.ProxyListener()
    root = pathlib.Path(tempfile.mkdtemp(prefix="run-", dir=str(out_dir)))
    try:
        env = kit.build_env(root, prx.url, {"BUN_CONFIG_REGISTRY": reg.url}, {})
        proc = subprocess.run([sys.executable, str(TOOL), "wrap", "--", "--version"], capture_output=True, text=True, env=env,
                              cwd=str(root), timeout=60)
        direct = subprocess.run([bun, "--version"], capture_output=True, text=True, env=env, cwd=str(root), timeout=60)
        reg_n, prx_n = len(reg.log.take()), len(prx.log.take())
        # the form applied end to end: an unresolvable import under wrap, inside the same harness, makes zero requests
        probe_dir = root / "probe"
        probe_dir.mkdir()
        probe_src = 'import x from "@opal-no-such-scope-%s/probe";' % ("ab" * 8)
        (probe_dir / "probe.js").write_text(probe_src + " console.log(x);", encoding="ascii")
        run_probe = subprocess.run([sys.executable, str(TOOL), "wrap", "--", "run", "probe.js"], capture_output=True, text=True,
                                   env=env, cwd=str(probe_dir), timeout=60)
        probe_reg, probe_prx = len(reg.log.take()), len(prx.log.take())
        applied = "applied: bun --no-install run probe.js" in run_probe.stderr and run_probe.returncode != 0
    finally:
        reg.close()
        prx.close()
    record(4, proc.returncode == 0 and proc.stdout.strip() == direct.stdout.strip() and proc.stdout.strip() != ""
           and reg_n == 0 and prx_n == 0 and applied and probe_reg == 0 and probe_prx == 0,
           "wrap --version rc=%s printed %r (bare bun printed %r); requests registry=%d proxy=%d; wrap run of an unresolvable import "
           "rc=%s form applied=%s requests registry=%d proxy=%d"
           % (proc.returncode, proc.stdout.strip(), direct.stdout.strip(), reg_n, prx_n, run_probe.returncode, applied,
              probe_reg, probe_prx))

    # (5) the planted regression: a grader that passes everything, including candidates that made requests
    bad = kit.summarize(result, grader=lambda arm, positive: True)
    made_requests = [a["name"] for a in result["arms"] if a["role"] == "candidate" and (a["requests_registry"] or a["requests_proxy"])]
    good = kit.summarize(result)
    record(5, (not bad["ok"]) and len(bad["regressions"]) >= 1 and len(made_requests) >= 1 and good["ok"],
           "planted grader (all PASS): ok=%s, %d regression(s) flagged (%s); candidates that made requests: %s; honest grader ok=%s"
           % (bad["ok"], len(bad["regressions"]), "; ".join(bad["regressions"][:2]), made_requests, good["ok"]))

    # (6) every bun process ran inside the harness
    repo = pathlib.Path(__file__).resolve().parents[2]
    arms = result["arms"]
    inside = []
    for a in arms:
        urls = set(v for k, v in a["proxy_env"].items() if k in kit.PROXY_VARS)
        noproxy_empty = all(a["proxy_env"].get(k) in ("", None) for k in kit.NOPROXY_VARS)
        inside.append(a["proxy_set"] and urls and all(u.startswith("http://127.0.0.1:") for u in urls) and noproxy_empty
                      and a["isolated_home"])
    outside_repo = not str(pathlib.Path(result["tmp_base"]).resolve()).lower().startswith(str(repo).lower())
    record(6, all(inside) and len(arms) > 0 and outside_repo and not result.get("stopped"),
           "%d of %d arms ran with loopback proxy variables, empty NO_PROXY and an isolated home; temporary base %s outside the "
           "repository=%s" % (sum(1 for x in inside if x), len(arms), result["tmp_base"], outside_repo))

    # (7) no registry verb was run; nothing baked
    verbs = [a["args"][0] for a in arms if a["args"]]
    allowed = {"--version", "--no-install", "run", "--help"}
    src = TOOL.read_text(encoding="ascii")
    no_version = re.search(r"(?<![\d.])\d+\.\d+\.\d+(?![\d.])", src) is None
    no_path = not re.search(r"[\\/]\.bun[\\/]|bun\.exe|[A-Za-z]:[\\/]Users|/c/Users", src)
    record(7, set(verbs) <= allowed and no_version and no_path,
           "first argument of every bun process: %s (registry verbs run: 0); source has a version-like token=%s, a baked path=%s"
           % (sorted(set(verbs)), not no_version, not no_path))

    shutil.rmtree(str(out_dir), ignore_errors=True)
    passed = sum(1 for _c, ok in RESULTS if ok)
    ok_all = passed == 7
    print("BUN-KIT-TEST cases=%d/7 ok=%s" % (passed, ok_all))
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
