#!/usr/bin/env python3
"""test_round22_journey_record.py -- READ-ONLY journey record test for NFRA_CTLPLN round 22, CT-al-1.

Batch intake-20261015-duckdb: ONE duckdb 1.5.0 wheel, the cp314 one, fetched through intake_fetch.py and checked by
intake_check.py (checks 1-7; check 8 awaits the CTO's signature file). This test only READS the records and the
holding folder. It makes no network request, writes nothing, installs nothing and runs no package file.

Flags (each prints one line; exit 0 only when every requested line says ok=True):
  --fetch   JOURNEY-FETCH wheels=<n> file=<name> device=<d> sha256=<12 hex> requests=<r> ok=<True|False>
  --check   JOURNEY-CHECK checks_run=<n> failed=<f> check8=<AWAITING|SIGNED|OTHER> released=<True|False> ok=<True|False>
  --tag     JOURNEY-TAG recorded=<tag> wheel=<tag> ok=<True|False>

Paths: records  OPAL_INTAKE_RECORDS (a base; batch folder under it), else org/devices/intake/records beside this repo.
       holding  OPAL_INTAKE_ROOT (a root; holding/<batch>/ under it), else <drive of this repo>/opal-intake.
Standard library only; Python 3.12; ASCII output.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import pathlib
import re
import sys

BATCH = "intake-20261015-duckdb"
WHEEL_NAME = "duckdb-1.5.0-cp314-cp314-win_amd64.whl"
WHEEL_CP312_MARK = "duckdb-1.5.0-cp312"
REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
CHECK8_SIGNATURE_REL = "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_CHECK8_NFRA_CTLPLN_INTAKE_DUCKDB_20261015.md"
TAG_RE = re.compile(r"-(cp\d+-cp\d+-[a-z0-9_]+)\.whl")
PYTAG_RE = re.compile(r"^duckdb-1\.5\.0-(cp\d+)-(cp\d+)-(win_amd64)\.whl$")
CHECKS_FIRST, CHECKS_LAST = 1, 7


def records_dir() -> pathlib.Path:
    base = os.environ.get("OPAL_INTAKE_RECORDS") or str(REPO_ROOT / "org" / "devices" / "intake" / "records")
    return pathlib.Path(base) / BATCH


def holding_dir() -> pathlib.Path:
    root = os.environ.get("OPAL_INTAKE_ROOT")
    if not root:
        drive = os.path.splitdrive(str(REPO_ROOT))[0]
        root = drive + os.sep + "opal-intake"
    return pathlib.Path(root) / "holding" / BATCH


def release_dir() -> pathlib.Path:
    root = os.environ.get("OPAL_INTAKE_ROOT")
    if not root:
        drive = os.path.splitdrive(str(REPO_ROOT))[0]
        root = drive + os.sep + "opal-intake"
    return pathlib.Path(root) / "release" / BATCH


def sha256_of(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def read_json(path: pathlib.Path):
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def this_box() -> str | None:
    sys.path.insert(0, str(REPO_ROOT / "lib"))
    import devices  # the register reader (lib/devices.py); fail-closed: an unresolved box is None
    name, _basis = devices.this_device()
    return name


def held_wheels() -> list[str]:
    folder = holding_dir()
    if not folder.is_dir():
        return []
    return sorted(p.name for p in folder.iterdir() if p.is_file() and p.suffix == ".whl")


def cp312_present() -> bool:
    for folder in (holding_dir(), records_dir()):
        if folder.is_dir() and any(WHEEL_CP312_MARK in p.name for p in folder.iterdir()):
            return True
    return False


def cmd_fetch() -> bool:
    wheels = held_wheels()
    name = wheels[0] if len(wheels) == 1 else None
    fetch_path = records_dir() / (WHEEL_NAME + ".fetch.json")
    rec = read_json(fetch_path) if fetch_path.is_file() else {}
    device = rec.get("device")
    requests = len(rec.get("requests", []))
    sha12 = "-"
    disk_matches = False
    if name is not None:
        disk = sha256_of(holding_dir() / name)
        sha12 = disk[:12]
        disk_matches = disk == rec.get("held_sha256")
    box = this_box()
    ok = (
        len(wheels) == 1
        and name == WHEEL_NAME
        and PYTAG_RE.match(name or "") is not None
        and PYTAG_RE.match(name).group(1) == "cp314"
        and bool(rec)
        and device == box
        and disk_matches
        and not cp312_present()
    ) if name is not None else False
    print("JOURNEY-FETCH wheels=%d file=%s device=%s sha256=%s requests=%d ok=%s"
          % (len(wheels), name or "NONE", device, sha12, requests, ok))
    print("JOURNEY-FETCH-DETAIL box=%s fetch_record=%s disk_matches_record=%s cp312_present=%s"
          % (box, fetch_path.is_file(), disk_matches, cp312_present()))
    return ok


def cmd_check() -> bool:
    wheels = held_wheels()
    name = wheels[0] if len(wheels) == 1 else WHEEL_NAME
    check_path = records_dir() / (name + ".check.json")
    rec = read_json(check_path) if check_path.is_file() else {}
    checks = rec.get("checks", [])
    by_n = {c.get("n"): c for c in checks if isinstance(c, dict)}
    first_seven = [by_n.get(n) for n in range(CHECKS_FIRST, CHECKS_LAST + 1)]
    ran = [c for c in first_seven if c and c.get("verdict") in ("passed", "failed", "not_applicable")]
    failed = [c["n"] for c in ran if c.get("verdict") == "failed"]
    for c in first_seven:
        if c is None:
            print("JOURNEY-CHECK-DETAIL n=? verdict=MISSING")
        else:
            print("JOURNEY-CHECK-DETAIL n=%s verdict=%s summary=%s"
                  % (c.get("n"), c.get("verdict"), (c.get("evidence") or {}).get("summary")))
    c8 = by_n.get(8) or {}
    sig_exists = (REPO_ROOT / CHECK8_SIGNATURE_REL).is_file()
    if c8.get("verdict") == "passed" and sig_exists:
        check8 = "SIGNED"
    elif c8.get("verdict") in ("failed", "unsigned") and not sig_exists:
        check8 = "AWAITING"
    else:
        check8 = "OTHER"
    print("JOURNEY-CHECK-DETAIL check8_verdict=%s check8_summary=%s signature_file_exists=%s"
          % (c8.get("verdict"), (c8.get("evidence") or {}).get("summary"), sig_exists))
    released = (release_dir() / name).exists()
    ok = (
        len(ran) == CHECKS_LAST - CHECKS_FIRST + 1
        and not failed
        and check8 == "AWAITING"
        and not released
        and rec.get("verdict") != "checked"
    )
    print("JOURNEY-CHECK checks_run=%d failed=%d check8=%s released=%s ok=%s"
          % (len(ran), len(failed), check8, released, ok))
    return ok


def cmd_tag() -> bool:
    tag_path = records_dir() / "TAG_RECORD.md"
    text = tag_path.read_text(encoding="utf-8") if tag_path.is_file() else ""
    section = text.split("## Tag to fetch", 1)[1] if "## Tag to fetch" in text else ""
    m = TAG_RE.search(section)
    recorded = m.group(1) if m else None
    wheels = held_wheels()
    name = wheels[0] if len(wheels) == 1 else WHEEL_NAME
    w = TAG_RE.search(name)
    wheel = w.group(1) if w else None
    ok = recorded is not None and wheel is not None and recorded == wheel
    print("JOURNEY-TAG recorded=%s wheel=%s ok=%s" % (recorded or "NONE", wheel or "NONE", ok))
    return ok


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--fetch", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--tag", action="store_true")
    args = ap.parse_args()
    run_all = not (args.fetch or args.check or args.tag)
    results = []
    if args.fetch or run_all:
        results.append(cmd_fetch())
    if args.check or run_all:
        results.append(cmd_check())
    if args.tag or run_all:
        results.append(cmd_tag())
    return 0 if results and all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
