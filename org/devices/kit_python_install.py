"""kit_python_install.py -- the Dell's half of the Python kit delivery (NFRA_CTLPLN PRD v0.14 C-KIT-PYTHON, cell CT-k-2).

    AGENTBUS_DEVICE=<d> python org/devices/kit_python_install.py --from <dir> [--dry-run]

`<dir>` is a directory the laptop's `kit_python_pack.py` wrote: wheels plus MANIFEST.json. This tool

  1. verifies every wheel against MANIFEST.json (SHA-256 and size; an unlisted wheel in the directory counts as a failure) -- ONE
     mismatch refuses the whole install and nothing is run;
  2. runs ONE `python -m pip install --no-index --find-links <dir> --user <name==version ...>` (`--dry-run` adds pip's --dry-run);
  3. re-runs the census's `installed` and `compare` against the committed required list and prints the result.

NO PACKAGE INDEX: every pip command is built by build_pip_cmd, which always carries `--no-index`. Pure stdlib; it runs on a Dell that has
only its interpreter. The box's name is AGENTBUS_DEVICE and must equal the manifest's target (a pack for dell1 is not installed on dell2).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import pathlib
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


def build_pip_cmd(targets, find_links, user, dry_run, extra=None):
    """The ONLY place a pip command is built. `--no-index` is unconditional: no package index, no network."""
    cmd = [sys.executable, "-m", "pip", "install", "--no-index"]
    if find_links is not None:
        cmd += ["--find-links", str(find_links)]
    if user:
        cmd.append("--user")
    if dry_run:
        cmd.append("--dry-run")
    cmd += list(extra or [])
    cmd += list(targets)
    return cmd


def census_norm(name):
    import re
    return re.sub(r"[-_.]+", "-", name).lower()


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def verify(directory):
    """Return (verified, total, problems, manifest). A problem list that is not empty refuses the install."""
    d = pathlib.Path(directory)
    mp = d / "MANIFEST.json"
    if not mp.is_file():
        return 0, 0, ["MANIFEST.json is not in %s" % d], None
    manifest = json.loads(mp.read_text(encoding="utf-8"))
    problems = []
    ok = 0
    listed = set()
    for e in manifest["files"]:
        listed.add(e["file"])
        p = d / e["file"]
        if not p.is_file():
            problems.append("MISSING %s" % e["file"])
        elif p.stat().st_size != e["size"]:
            problems.append("SIZE %s manifest=%d actual=%d" % (e["file"], e["size"], p.stat().st_size))
        elif sha256_file(p) != e["sha256"]:
            problems.append("SHA-256 %s differs from the manifest" % e["file"])
        else:
            ok += 1
    for p in sorted(d.iterdir()):
        if p.suffix in (".whl", ".zip", ".gz") and p.name not in listed:
            problems.append("UNLISTED %s is in the directory but not in the manifest" % p.name)
    return ok, len(manifest["files"]), problems, manifest


def census_after(device):
    """Re-run the census's installed and compare in fresh subprocesses; return (compare_line, missing, installed distributions)."""
    census = str(HERE / "kit_python_census.py")
    env = dict(os.environ, AGENTBUS_DEVICE=device)
    with tempfile.TemporaryDirectory() as td:
        out = str(pathlib.Path(td) / "installed_after.json")
        subprocess.run([sys.executable, census, "installed", "--out", out], env=env, capture_output=True, text=True, check=False)
        r = subprocess.run([sys.executable, census, "compare", out], env=env, capture_output=True, text=True, check=False)
        try:
            have = json.loads(pathlib.Path(out).read_text(encoding="utf-8"))["all_installed"]
        except (OSError, ValueError, KeyError):
            have = {}
    line = [x for x in r.stdout.splitlines() if x.startswith("KIT-COMPARE")]
    line = line[-1] if line else "KIT-COMPARE unreadable: %s" % (r.stdout + r.stderr).strip()[-200:]
    missing = -1
    for tok in line.split():
        if tok.startswith("missing="):
            missing = int(tok.split("=")[1])
    return line, missing, have


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--from", dest="src", required=True)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)
    device = os.environ.get("AGENTBUS_DEVICE", "").strip()
    if not device:
        print("REFUSED: AGENTBUS_DEVICE is unset; this box's name is never derived. Set it and re-run.")
        return 2
    ok, total, problems, manifest = verify(args.src)
    refuse = list(problems)
    if manifest is not None:
        if manifest.get("target_device") != device:
            refuse.append("TARGET the manifest is for %r, this box is %r" % (manifest.get("target_device"), device))
        sys_tag = "%d.%d" % sys.version_info[:2]
        if manifest.get("target_python_minor") != sys_tag:
            refuse.append("PYTHON the manifest is for python %s, this is %s" % (manifest.get("target_python_minor"), sys_tag))
    for p in refuse:
        print("VERIFY FAILED: %s" % p)
    if refuse:
        print("REFUSED: the whole install is refused; no pip command was run.")
        line, missing, _have = census_after(device)
        print(line)
        print("KIT-INSTALL device=%s verified=%d/%d installed=0 missing_after=%d ok=False" % (device, ok, total, missing))
        return 1
    names = ["%s==%s" % (e["distribution"], e["version"]) for e in manifest["files"]]
    print("verified %d/%d against MANIFEST.json" % (ok, total))
    if not names:
        print("nothing to install")
    cmd = build_pip_cmd(names, find_links=args.src, user=True, dry_run=args.dry_run)
    print("RUN: %s" % " ".join(cmd))
    rc = 0
    installed = 0
    if names:
        r = subprocess.run(cmd, capture_output=True, text=True, check=False)
        rc = r.returncode
        print((r.stdout + r.stderr).strip()[-1500:])
        installed = 0 if (rc != 0 or args.dry_run) else len(names)
    line, missing, have = census_after(device)
    print(line)
    delivered = all(census_norm(e["distribution"]) in have for e in manifest["files"])
    good = rc == 0 and ok == total and (args.dry_run or delivered)
    if not args.dry_run and rc == 0 and missing != 0:
        print("NOTE: every packed distribution is %s; compare still reports missing=%d (items the pack listed UNPACKABLE)"
              % ("installed" if delivered else "NOT all installed", missing))
    print("KIT-INSTALL device=%s verified=%d/%d installed=%d missing_after=%d ok=%s" % (device, ok, total, installed, missing, good))
    return 0 if good else 1


if __name__ == "__main__":
    sys.exit(main())
