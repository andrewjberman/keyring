"""TR-x-2 AC2 -- the deployed layout imports both sources' modules without shadowing (issuer's check; base: FAIL as expected).

CTO issuer rule 103374: a cell that changes a runner-deployed script's imports proves the import in the deployed layout.
Builds the Lambda bundle with its own build.sh, extracts the EXACT zip it ships to a temp dir, and in a fresh interpreter
whose sys.path is ONLY that extract: imports handler, the teams pull and the outlook pull, and requires (a) two distinct
module objects, (b) no bare top-level land_bronze / pull / criterion in sys.modules, (c) handler.lambda_handler callable.
Prints BUNDLE-IMPORT-OK files=N, else BUNDLE-IMPORT-FAIL <reason>.
"""
import os
import subprocess
import sys
import tempfile
import zipfile

BUILD = "infra/aws/lambda/transcripts-pull/build.sh"
ZIP = "infra/aws/lambda/transcripts-pull/dist/transcripts-pull.zip"
PROBE = r"""
import sys, importlib
import os
repo = os.environ.get('R2_REPO_ROOT', '').lower()
sys.path[:] = [sys.argv[1]] + [p for p in sys.path if p and not (repo and os.path.abspath(p).lower().startswith(repo))]
import handler
tp = importlib.import_module('data.transcripts.scripts.teams.pull')
op = importlib.import_module('data.transcripts.scripts.outlook.pull')
bare = sorted(m for m in ('land_bronze', 'pull', 'criterion', 'gateway_client', 'parse_silver') if m in sys.modules)
assert tp is not op, 'teams and outlook pull are one module'
assert not bare, 'bare top-level modules loaded: %s' % bare
assert callable(getattr(handler, 'lambda_handler', None)), 'no lambda_handler'
print('PROBE-OK')
"""


def _bash_argv():
    # CLAUDE.md: Python shelling to bash resolves Git Bash through .tools/git_bash_resolver.py (a bare "bash" on
    # Windows can resolve to the WSL launcher, which is not the estate's shell).
    sys.path.insert(0, ".tools")
    try:
        from git_bash_resolver import bash_argv  # noqa: PLC0415
        return bash_argv(BUILD)
    except Exception:  # noqa: BLE001
        return ["bash", BUILD]


def main():
    r = subprocess.run(_bash_argv(), capture_output=True, text=True)
    if r.returncode != 0 or not os.path.exists(ZIP):
        print("BUNDLE-IMPORT-FAIL build rc=%d: %s" % (r.returncode, (r.stdout + r.stderr)[-300:]))
        return 1
    with tempfile.TemporaryDirectory() as tmp:
        with zipfile.ZipFile(ZIP) as z:
            names = z.namelist()
            z.extractall(tmp)
        env = {k: v for k, v in os.environ.items() if k != "PYTHONPATH"}
        env["R2_REPO_ROOT"] = os.path.abspath(".")
        p = subprocess.run([sys.executable, "-c", PROBE, tmp], capture_output=True, text=True, cwd=tmp, env=env)
        if "PROBE-OK" not in p.stdout:
            err = (p.stderr.strip().splitlines() or [""])[-1]
            print("BUNDLE-IMPORT-FAIL %s" % err[:300])
            return 1
    print("BUNDLE-IMPORT-OK files=%d" % len(names))
    return 0


if __name__ == "__main__":
    sys.exit(main())
