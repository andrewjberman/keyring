#!/usr/bin/env python3
"""test_round25_journey_record.py -- READ-ONLY journey record test for NFRA_CTLPLN round 25, CT-ao-1.

Batch intake-20261016-tabulate: ONE tabulate 0.9.0 wheel, the pure-Python py3-none-any one, fetched through
intake_fetch.py and checked by intake_check.py (checks 1-7; check 8 awaits the CTO's signature file). This test only
READS the records and the holding folder. It makes no network request, writes nothing, installs nothing and runs no
package file. It is the round-22 test's shape, wired to this batch; the constants are this batch's own.

Flags (each prints one line; exit 0 only when every requested line says ok=True):
  --fetch   JOURNEY-FETCH wheels=<n> file=<name> device=<d> sha256=<12 hex> requests=<r> ok=<True|False>
            (state-aware: the batch's one wheel, in holding OR release; a released wheel is moved; mutants held)
  --check   JOURNEY-CHECK checks_run=<n> failed=<f> check8=<AWAITING|SIGNED|OTHER> released=<True|False> ok=<True|False>
            (state-aware: ok only in the pre-signature state (AWAITING, not released) or the post-release state
            (SIGNED, released), with checks 1-7 run and 0 failed; mutants held)
--fetch ok requires: exactly ONE wheel in the batch wherever it sits, named WHEEL_NAME; no file other than .whl in the
holding folder; the SHA-256 on disk equals the fetch record's held_sha256; the fetch record's device equals this box.
Mutants (must read held=True): a second wheel in the holding folder; a record whose SHA-256 differs from the disk file.

The check record is read from the records folder only; check 8 is SIGNED only when the signature file exists at the
path the check tool requires.

Paths: records  OPAL_INTAKE_RECORDS (a base; batch folder under it), else org/devices/intake/records beside this repo.
       holding  OPAL_INTAKE_ROOT (a root; holding/<batch>/ under it), else <drive of this repo>/opal-intake.
       release  the same root, release/<batch>/.
Standard library only; Python 3.12; ASCII output.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import pathlib
import sys

BATCH = "intake-20261016-tabulate"
WHEEL_NAME = "tabulate-0.9.0-py3-none-any.whl"
SECOND_WHEEL = "tabulate-0.9.0-py2.py3-none-any.whl"
REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
CHECK8_SIGNATURE_REL = "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_CHECK8_NFRA_CTLPLN_INTAKE_TABULATE_20261016.md"
CHECKS_FIRST, CHECKS_LAST = 1, 7


def records_dir() -> pathlib.Path:
    base = os.environ.get("OPAL_INTAKE_RECORDS") or str(REPO_ROOT / "org" / "devices" / "intake" / "records")
    return pathlib.Path(base) / BATCH


def holding_root() -> pathlib.Path:
    root = os.environ.get("OPAL_INTAKE_ROOT")
    if not root:
        drive = os.path.splitdrive(str(REPO_ROOT))[0]
        root = drive + os.sep + "opal-intake"
    return pathlib.Path(root)


def holding_dir() -> pathlib.Path:
    return holding_root() / "holding" / BATCH


def release_dir() -> pathlib.Path:
    return holding_root() / "release" / BATCH


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


def batch_wheels() -> list[tuple[str, str]]:
    """Every .whl of the batch wherever it sits: (where, name), where = holding or release. A released wheel is MOVED,
    so one place holds it; two entries means a copy was left behind."""
    found = []
    for where, folder in (("holding", holding_dir()), ("release", release_dir())):
        if folder.is_dir():
            found += [(where, p.name) for p in sorted(folder.iterdir()) if p.is_file() and p.suffix == ".whl"]
    return found


def holding_non_wheel_files() -> list[str]:
    folder = holding_dir()
    if not folder.is_dir():
        return []
    return sorted(p.name for p in folder.iterdir() if p.is_file() and p.suffix != ".whl")


def fetch_state_ok(found: list, disk_sha_matches: bool, rec_ok: bool, device_ok: bool, other_files: int) -> bool:
    """ok for --fetch: exactly ONE wheel in the batch wherever it sits, that wheel is WHEEL_NAME, its disk SHA-256 equals
    the fetch record's, the fetch record is present, the device is this box, and the holding folder holds no file other
    than .whl files."""
    if len(found) != 1 or found[0][1] != WHEEL_NAME:
        return False
    return disk_sha_matches and rec_ok and device_ok and other_files == 0


# (label, keyword overrides against the all-good baseline) -- each must read ok=False, i.e. held=True
FETCH_MUTANTS = (
    ("second_wheel_in_holding", {"found": [("holding", WHEEL_NAME), ("holding", SECOND_WHEEL)]}),
    ("record_sha_differs", {"disk_sha_matches": False}),
)


def cmd_fetch() -> bool:
    found = batch_wheels()
    name = found[0][1] if len(found) == 1 else "NONE"
    fetch_path = records_dir() / (WHEEL_NAME + ".fetch.json")
    rec = read_json(fetch_path) if fetch_path.is_file() else {}
    device = rec.get("device")
    requests = len(rec.get("requests", []))
    sha12 = "-"
    disk_matches = False
    if len(found) == 1:
        folder = holding_dir() if found[0][0] == "holding" else release_dir()
        disk = sha256_of(folder / name)
        sha12 = disk[:12]
        disk_matches = disk == rec.get("held_sha256")
    box = this_box()
    others = holding_non_wheel_files()
    ok = fetch_state_ok(found, disk_matches, bool(rec), device == box, len(others))
    # every mutant starts from the all-good baseline (one held wheel, digests equal, device this box, no stray file)
    baseline = {"found": [("holding", WHEEL_NAME)], "disk_sha_matches": True, "rec_ok": True, "device_ok": True,
                "other_files": 0}
    mutants_held = True
    for label, over in FETCH_MUTANTS:
        args = dict(baseline, **over)
        m_ok = fetch_state_ok(args["found"], args["disk_sha_matches"], args["rec_ok"], args["device_ok"], args["other_files"])
        mutants_held = mutants_held and not m_ok
        print("JOURNEY-FETCH-MUTANT case=%s wheels=%d ok=%s expected=False held=%s"
              % (label, len(args["found"]), m_ok, not m_ok))
    ok = ok and mutants_held
    where = "+".join(sorted(set(w for w, _ in found))) or "NONE"
    print("JOURNEY-FETCH wheels=%d file=%s device=%s sha256=%s requests=%d ok=%s"
          % (len(found), name, device, sha12, requests, ok))
    print("JOURNEY-FETCH-DETAIL box=%s where=%s fetch_record=%s disk_matches_record=%s holding_non_wheel=%s"
          % (box, where, fetch_path.is_file(), disk_matches, others))
    return ok


PRE_SIGNATURE = ("AWAITING", False)   # check 8 awaits the CTO's signature, nothing released (state before the signature)
POST_RELEASE = ("SIGNED", True)       # check 8 signed and the wheel released (state after release)
# the two mismatch states the ok expression must refuse
MUTANT_CASES = (("signed_not_released", "SIGNED", False), ("awaiting_released", "AWAITING", True))


def check_state_ok(ran_count: int, failed_count: int, check8: str, released: bool) -> bool:
    """ok for --check: checks 1-7 all ran with 0 failed, AND the state is either PRE_SIGNATURE or POST_RELEASE.
    Any other pairing of check8 and released (SIGNED without a release, AWAITING with a release) is not ok."""
    if ran_count != CHECKS_LAST - CHECKS_FIRST + 1 or failed_count != 0:
        return False
    return (check8, released) in (PRE_SIGNATURE, POST_RELEASE)


def cmd_check() -> bool:
    check_path = records_dir() / (WHEEL_NAME + ".check.json")
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
    elif c8.get("verdict") in ("awaiting", "failed", "unsigned") and not sig_exists:
        # 'awaiting' is the tool's recorded state; 'failed' plus an absent file is the form written before it existed
        check8 = "AWAITING"
    else:
        check8 = "OTHER"
    print("JOURNEY-CHECK-DETAIL check8_verdict=%s check8_summary=%s signature_file_exists=%s"
          % (c8.get("verdict"), (c8.get("evidence") or {}).get("summary"), sig_exists))
    released = (release_dir() / WHEEL_NAME).exists()
    ok = check_state_ok(len(ran), len(failed), check8, released)
    mutants_held = True
    for label, m8, mrel in MUTANT_CASES:
        m_ok = check_state_ok(CHECKS_LAST - CHECKS_FIRST + 1, 0, m8, mrel)
        mutants_held = mutants_held and not m_ok
        print("JOURNEY-CHECK-MUTANT case=%s check8=%s released=%s ok=%s expected=False held=%s"
              % (label, m8, mrel, m_ok, not m_ok))
    ok = ok and mutants_held
    print("JOURNEY-CHECK checks_run=%d failed=%d check8=%s released=%s ok=%s"
          % (len(ran), len(failed), check8, released, ok))
    return ok


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--fetch", action="store_true")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    run_all = not (args.fetch or args.check)
    results = []
    if args.fetch or run_all:
        results.append(cmd_fetch())
    if args.check or run_all:
        results.append(cmd_check())
    return 0 if results and all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
