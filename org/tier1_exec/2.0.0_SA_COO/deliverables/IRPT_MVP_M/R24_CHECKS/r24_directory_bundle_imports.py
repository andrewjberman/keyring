"""Round 24 (~M) check IBM24-241-AC1 (row S217): a directory bundle built LOCALLY from the declared members imports.

Builds the investor_reporting bundle in memory with .tools/safe_deploy_core.py's own build_bundle_payload (no upload),
extracts it to a temp directory, and then:
  (a) every sibling module that directory_runner.py imports at MODULE level is a member of the bundle; and
  (b) `import directory_runner` succeeds in a fresh interpreter whose only path to the investor_reporting modules is
      the extracted tree (the repo's own copy is not on sys.path).
Run from the repo (or worktree) root. Prints BUNDLE-IMPORTS <n members> or NOT-IMPORTABLE: <reason>. Writes nothing
in the repo; no network.
"""
import ast
import io
import os
import subprocess
import sys
import tarfile
import tempfile

REPO = os.getcwd()
RUNNER_DIR = "data/assets/scripts/gold/investor_reporting"


def main():
    sys.path.insert(0, os.path.join(REPO, ".tools"))
    import safe_deploy_core as sdc  # noqa: E402
    found = sdc.find_bundle("investor_reporting")
    if not found:
        print("NOT-IMPORTABLE: no bundle named investor_reporting in safe_deploy_core")
        return 1
    payload, _meta, why = sdc.build_bundle_payload(found[2])
    if payload is None:
        print("NOT-IMPORTABLE: build_bundle_payload refused: %s" % why)
        return 1
    tf = tarfile.open(fileobj=io.BytesIO(payload), mode="r:*")
    names = [m.name for m in tf.getmembers() if m.isfile()]
    src = open(os.path.join(REPO, RUNNER_DIR, "directory_runner.py"), encoding="utf-8").read()
    siblings = {os.path.splitext(f)[0] for f in os.listdir(os.path.join(REPO, RUNNER_DIR)) if f.endswith(".py")}
    top = set()
    for n in ast.parse(src).body:
        if isinstance(n, ast.Import):
            top |= {a.name.split(".")[0] for a in n.names}
        elif isinstance(n, ast.ImportFrom) and n.module and n.level == 0:
            top.add(n.module.split(".")[0])
    have = {os.path.splitext(os.path.basename(x))[0] for x in names if x.endswith(".py")}
    missing = sorted(m for m in top if m in siblings and m not in have)
    if missing:
        print("NOT-IMPORTABLE: module-level sibling imports not in the bundle: %s" % missing)
        return 1
    with tempfile.TemporaryDirectory() as tmp:
        tf.extractall(tmp)
        runner = [x for x in names if x.endswith("/directory_runner.py") or x == "directory_runner.py"]
        if len(runner) != 1:
            print("NOT-IMPORTABLE: %d directory_runner.py members" % len(runner))
            return 1
        rdir = os.path.dirname(os.path.join(tmp, runner[0]))
        code = "import sys; sys.path.insert(0, %r); import directory_runner; print('ok')" % rdir
        r = subprocess.run([sys.executable, "-c", code], cwd=tmp, capture_output=True, text=True, timeout=100)
        if r.returncode != 0 or "ok" not in r.stdout:
            print("NOT-IMPORTABLE: import directory_runner from the extracted bundle failed: %s"
                  % (r.stderr.strip().splitlines() or ["rc=%d" % r.returncode])[-1])
            return 1
    print("BUNDLE-IMPORTS %d members" % len(names))
    return 0


if __name__ == "__main__":
    sys.exit(main())
