"""Offline test of the yfinance pydeps host scripts (issuer 2.0.0_SA_COO~G2): builds 17 dummy wheels and a fake pydeps, runs the generated scripts
through the YF_* overrides, and prints one RESULT line: YF-SCRIPTS-TEST-OK <n> cases or YF-SCRIPTS-TEST-FAIL <why>. No network, no AWS, no real host.

usage: python test_yf_scripts.py <wheels json> <inventory file>      (run from any folder; needs bash, pip, sha256sum on PATH)
"""
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

WHEELS, INVENTORY = sys.argv[1:3]
HERE = Path(__file__).resolve().parent
real = json.loads(Path(WHEELS).read_text(encoding="utf-8"))["wheels"]
inv = [ln.strip() for ln in Path(INVENTORY).read_text(encoding="utf-8").splitlines() if ln.strip() and not ln.startswith("COUNT ")]
MOD = {"beautifulsoup4": ("bs4",), "protobuf": ("google", "protobuf"), "curl_cffi": ("curl_cffi",)}
cases = []


def check(name, ok, why=""):
    cases.append((name, bool(ok), why))
    print("CASE", "ok  " if ok else "FAIL", name, "" if ok else why, flush=True)


def make_wheel(dest, name, version):
    mod = MOD.get(name, (name.replace("-", "_"),))
    fname = "%s-%s-py3-none-any.whl" % (name.replace("-", "_"), version)
    dist = "%s-%s.dist-info" % (name.replace("-", "_"), version)
    path = dest / fname
    with zipfile.ZipFile(path, "w") as zf:
        init = "/".join(mod) + "/__init__.py"
        zf.writestr(init, "__version__ = %r\n" % version)
        zf.writestr(dist + "/METADATA", "Metadata-Version: 2.1\nName: %s\nVersion: %s\n" % (name, version))
        zf.writestr(dist + "/WHEEL", "Wheel-Version: 1.0\nGenerator: test\nRoot-Is-Purelib: true\nTag: py3-none-any\n")
        zf.writestr(dist + "/RECORD", "")
    data = path.read_bytes()
    return {"name": name, "version": version, "file": fname, "sha256": hashlib.sha256(data).hexdigest(), "size": len(data)}


def run(script, env, args=()):
    out = subprocess.run(["bash", str(script), *args], capture_output=True, text=True, env=env)
    return out.returncode, out.stdout + out.stderr


tmp = Path(tempfile.mkdtemp(prefix="yf_test_"))
try:
    wheels_dir = tmp / "wheels"
    wheels_dir.mkdir()
    table = {"schema": "irpt-yf-wheels.v1", "approved_by": "test", "source": "test", "wheels": [make_wheel(wheels_dir, w["name"], w["version"]) for w in real]}
    tjson = tmp / "table.json"
    tjson.write_text(json.dumps(table), encoding="utf-8")
    scripts = tmp / "scripts"
    subprocess.run([sys.executable, "-I", str(HERE / "make_scripts_yf.py"), str(tjson), INVENTORY, str(scripts)], check=True, capture_output=True)
    for s in ("pre_read_yf.sh", "install_yf.sh", "rollback_yf.sh"):
        check("bash -n " + s, subprocess.run(["bash", "-n", str(scripts / s)]).returncode == 0)
    h = tmp / "host"
    pyd = h / "pydeps"
    pyd.mkdir(parents=True)
    for line in inv:
        name, version = line.rsplit(" ", 1)
        d = pyd / ("%s-%s.dist-info" % (name.replace("-", "_").replace(".", "_"), version))
        d.mkdir()
        (d / "METADATA").write_text("Metadata-Version: 2.1\nName: %s\nVersion: %s\n" % (name, version), encoding="utf-8")
        pkg = pyd / name.replace("-", "_").split(".")[0]
        pkg.mkdir(exist_ok=True)
        (pkg / "__init__.py").write_text("__version__ = %r\n" % version, encoding="utf-8")
    # a clean interpreter (no site packages beyond pip), so "not importable" means what it means on the host; forward-slash paths so sha256sum prints a plain hash
    subprocess.run([sys.executable, "-m", "venv", str(tmp / "venv")], check=True, capture_output=True)
    vpy = tmp / "venv" / ("Scripts" if os.name == "nt" else "bin") / ("python.exe" if os.name == "nt" else "python")
    env = dict(os.environ, YF_H=h.as_posix(), YF_PYD=pyd.as_posix(), YF_PY=vpy.as_posix(), YF_FETCH_DIR=wheels_dir.as_posix(), YF_W=(tmp / "stage").as_posix())
    rc, out = run(scripts / "pre_read_yf.sh", env)
    check("pre-read passes on the clean host", rc == 0 and "PRE OK" in out, out[-300:])
    before_listing = sorted(os.listdir(pyd))
    # a tampered wheel stops the install before anything moves
    bad = tmp / "bad_wheels"
    shutil.copytree(wheels_dir, bad)
    victim = sorted(bad.glob("*.whl"))[0]
    victim.write_bytes(victim.read_bytes() + b"x")
    rc, out = run(scripts / "install_yf.sh", dict(env, YF_FETCH_DIR=str(bad)))
    check("a changed wheel is refused (sha256) and nothing is installed", rc == 42 and sorted(os.listdir(pyd)) == before_listing and not (h / ("yf_added_irpt-yf-pydeps-20261016.txt")).exists(), "rc=%d %s" % (rc, out[-200:]))
    shutil.rmtree(tmp / "stage", ignore_errors=True)
    rc, out = run(scripts / "install_yf.sh", env)
    imports = [ln for ln in out.splitlines() if ln.startswith("V2 IMPORT OK")]
    check("the install passes", rc == 0 and "INSTALL OK" in out, "rc=%d %s" % (rc, out[-400:]))
    check("17 dist-info added, none removed", "dist-info added: 17 (want 17)" in out and "removed: 0 (want 0)" in out)
    check("18 imports ok, all under pydeps", len(imports) == 18 and all("under_pydeps=True" in ln for ln in imports), str(len(imports)))
    check("the 22 pre-existing distributions are reported unchanged", "the 22 pre-existing distributions are unchanged" in out)
    added_file = h / "yf_added_irpt-yf-pydeps-20261016.txt"
    added = added_file.read_text(encoding="utf-8").split() if added_file.exists() else []
    check("the added list holds 17 dist-info and their packages", sum(a.endswith(".dist-info") for a in added) == 17 and len(added) >= 34, str(len(added)))
    rc, out = run(scripts / "install_yf.sh", env)
    check("a second install under the same ledger is refused", rc == 45, "rc=%d" % rc)
    rc, out = run(scripts / "rollback_yf.sh", env)
    check("the rollback moves the added entries aside and restores the listing", rc == 0 and "ROLLBACK listing equals the before listing" in out and sorted(os.listdir(pyd)) == before_listing, "rc=%d %s" % (rc, out[-300:]))
    check("nothing was deleted: the moved entries sit in the removed folder", os.path.isdir(h / "pydeps.removed-irpt-yf-pydeps-20261016") and len(os.listdir(h / "pydeps.removed-irpt-yf-pydeps-20261016")) == len(added))
    # a name already importable stops the pre-read
    (pyd / "requests").mkdir()
    (pyd / "requests" / "__init__.py").write_text("", encoding="utf-8")
    (h / "yf_added_irpt-yf-pydeps-20261016.txt").unlink()
    rc, out = run(scripts / "pre_read_yf.sh", env)
    check("a name that is already importable stops the pre-read", rc == 24, "rc=%d %s" % (rc, out[-200:]))
finally:
    shutil.rmtree(tmp, ignore_errors=True)
failed = [(n, w) for n, ok, w in cases if not ok]
for n, w in failed:
    print("CASE-FAIL", n, w)
if failed:
    print("YF-SCRIPTS-TEST-FAIL %d of %d cases failed" % (len(failed), len(cases)))
    sys.exit(1)
print("YF-SCRIPTS-TEST-OK %d cases" % len(cases))
