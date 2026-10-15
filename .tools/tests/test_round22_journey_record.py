#!/usr/bin/env python3
"""test_round22_journey_record.py -- READ-ONLY journey record test for NFRA_CTLPLN round 22, CT-al-1.

Batch intake-20261015-duckdb: ONE duckdb 1.5.0 wheel, the cp314 one, fetched through intake_fetch.py and checked by
intake_check.py (checks 1-7; check 8 awaits the CTO's signature file). This test only READS the records and the
holding folder. It makes no network request, writes nothing, installs nothing and runs no package file.

Flags (each prints one line; exit 0 only when every requested line says ok=True):
  --fetch   JOURNEY-FETCH wheels=<n> file=<name> device=<d> sha256=<12 hex> requests=<r> ok=<True|False> where=<holding|release|holding+release|NONE>
            (state-aware: the batch's one cp314 wheel, in holding OR release; a released wheel is moved; mutants held)
  --check   JOURNEY-CHECK checks_run=<n> failed=<f> check8=<AWAITING|SIGNED|OTHER> released=<True|False> ok=<True|False>
  --tag     JOURNEY-TAG recorded=<tag> wheel=<tag> ok=<True|False>
  --release JOURNEY-RELEASE released=<n> check8=<SIGNED|OTHER> file=<name> sha256=<12 hex> ok=<True|False>
  --pack    JOURNEY-PACK files=<n> manifest_ok=<True|False> verify=<INTAKE-VERIFY last line> ok=<True|False>
  --taildrop JOURNEY-TAILDROP files_sent=<n> failed=<f> target=dell1 ok=<True|False>
--check is state-aware: ok=True only in the pre-signature state (check8=AWAITING, released=False) or the post-release
state (check8=SIGNED, released=True), with checks 1-7 run and 0 failed; its two mismatch mutants print JOURNEY-CHECK-MUTANT
lines and must read held=True.
The three new flags run only when named; the default run is the original three. --release is read-only (it reads the
release folder, the fetch and check records, and the CTO's signature file). --pack re-runs `intake_receive.py verify`
locally on the pack and sends nothing. --taildrop reads ONLY TAILDROP_RECORD.md and never calls Tailscale.

Paths: records  OPAL_INTAKE_RECORDS (a base; batch folder under it), else org/devices/intake/records beside this repo.
       holding  OPAL_INTAKE_ROOT (a root; holding/<batch>/ under it), else <drive of this repo>/opal-intake.
       release  the same root, release/<batch>/.
       pack     <home>/tdrop/out/<batch> (the staging folder; outside every git tree).
Standard library only; Python 3.12; ASCII output.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import pathlib
import re
import subprocess
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


def batch_wheels() -> list[tuple[str, str]]:
    """Every .whl of the batch wherever it sits: (where, name), where = holding or release. A released wheel is MOVED,
    so one place holds it; two entries means a copy was left behind."""
    found = []
    for where, folder in (("holding", holding_dir()), ("release", release_dir())):
        if folder.is_dir():
            found += [(where, p.name) for p in sorted(folder.iterdir()) if p.is_file() and p.suffix == ".whl"]
    return found


def cp312_present() -> bool:
    for folder in (holding_dir(), release_dir(), records_dir()):
        if folder.is_dir() and any(WHEEL_CP312_MARK in p.name for p in folder.iterdir()):
            return True
    return False


FETCH_MUTANT_CASES = (
    ("wheel_in_both_folders", [("holding", WHEEL_NAME), ("release", WHEEL_NAME)], False),
    ("cp312_wheel_present", [("release", WHEEL_NAME)], True),
)


def fetch_state_ok(found: list, disk_sha_matches: bool, rec_ok: bool, device_ok: bool, cp312: bool) -> bool:
    """ok for --fetch (state-aware, holding or release): exactly ONE wheel in the batch wherever it sits, that wheel is the
    cp314 one, its disk SHA-256 equals the fetch record's, the fetch record is present, the device is this box, and no cp312
    wheel is in holding, release or the records."""
    if len(found) != 1 or found[0][1] != WHEEL_NAME:
        return False
    tag = PYTAG_RE.match(found[0][1])
    return (tag is not None and tag.group(1) == "cp314" and disk_sha_matches and rec_ok and device_ok and not cp312)


def cmd_fetch() -> bool:
    found = batch_wheels()
    name = found[0][1] if len(found) == 1 else "NONE"
    where = "+".join(sorted(set(w for w, _ in found))) or "NONE"
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
    cp312 = cp312_present()
    ok = fetch_state_ok(found, disk_matches, bool(rec), device == box, cp312)
    mutants_held = True
    for label, m_found, m_cp312 in FETCH_MUTANT_CASES:
        m_ok = fetch_state_ok(m_found, True, True, True, m_cp312)
        mutants_held = mutants_held and not m_ok
        print("JOURNEY-FETCH-MUTANT case=%s wheels=%d places=%s cp312=%s ok=%s expected=False held=%s"
              % (label, len(m_found), "+".join(sorted(set(w for w, _ in m_found))), m_cp312, m_ok, not m_ok))
    ok = ok and mutants_held
    print("JOURNEY-FETCH wheels=%d file=%s device=%s sha256=%s requests=%d ok=%s where=%s"
          % (len(found), name, device, sha12, requests, ok, where))
    print("JOURNEY-FETCH-DETAIL box=%s fetch_record=%s disk_matches_record=%s cp312_present=%s"
          % (box, fetch_path.is_file(), disk_matches, cp312))
    return ok


PRE_SIGNATURE = ("AWAITING", False)   # check 8 awaits the CTO's signature, nothing released (state before the signature)
POST_RELEASE = ("SIGNED", True)       # check 8 signed and the wheel released (state after release)
# the two mismatch states the ok expression must refuse (ruling from 2.0.0_SA_COO~C on W122-S4)
MUTANT_CASES = (("signed_not_released", "SIGNED", False), ("awaiting_released", "AWAITING", True))


def check_state_ok(ran_count: int, failed_count: int, check8: str, released: bool) -> bool:
    """ok for --check: checks 1-7 all ran with 0 failed, AND the state is either PRE_SIGNATURE or POST_RELEASE.
    Any other pairing of check8 and released (SIGNED without a release, AWAITING with a release) is not ok."""
    if ran_count != CHECKS_LAST - CHECKS_FIRST + 1 or failed_count != 0:
        return False
    return (check8, released) in (PRE_SIGNATURE, POST_RELEASE)


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
    elif c8.get("verdict") in ("awaiting", "failed", "unsigned") and not sig_exists:
        # 'awaiting' is the tool's recorded state; 'failed' plus an absent file is the form written before it existed
        check8 = "AWAITING"
    else:
        check8 = "OTHER"
    print("JOURNEY-CHECK-DETAIL check8_verdict=%s check8_summary=%s signature_file_exists=%s"
          % (c8.get("verdict"), (c8.get("evidence") or {}).get("summary"), sig_exists))
    released = (release_dir() / name).exists()
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


TIME_RE = re.compile(r"^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
TAILDROP_RECORD_NAME = "TAILDROP_RECORD.md"
PACK_FILE_COUNT = 4


def pack_dir() -> pathlib.Path:
    return pathlib.Path(os.path.expanduser("~")) / "tdrop" / "out" / BATCH


def cmd_release() -> bool:
    folder = release_dir()
    members = sorted(p for p in folder.iterdir() if p.is_file()) if folder.is_dir() else []
    wheels_here = [p for p in members if not p.name.endswith(".delivery.txt")]
    released = len(wheels_here)
    name = wheels_here[0].name if released == 1 else "NONE"
    delivery_here = (folder / (WHEEL_NAME + ".delivery.txt")).is_file()
    check_path = records_dir() / (WHEEL_NAME + ".check.json")
    check = read_json(check_path) if check_path.is_file() else {}
    fetch_path = records_dir() / (WHEEL_NAME + ".fetch.json")
    fetch = read_json(fetch_path) if fetch_path.is_file() else {}
    by_n = {c.get("n"): c for c in check.get("checks", []) if isinstance(c, dict)}
    c8 = by_n.get(8) or {}
    sig_exists = (REPO_ROOT / CHECK8_SIGNATURE_REL).is_file()
    check8 = "SIGNED" if (c8.get("verdict") == "passed" and sig_exists
                          and (c8.get("evidence") or {}).get("path") == CHECK8_SIGNATURE_REL) else "OTHER"
    seven_passed = all((by_n.get(n) or {}).get("verdict") == "passed" for n in range(CHECKS_FIRST, CHECKS_LAST + 1))
    sha = sha256_of(wheels_here[0]) if released == 1 else "-"
    sha_matches = (released == 1 and sha == fetch.get("held_sha256") and sha == check.get("held_sha256")
                   and name == WHEEL_NAME)
    ok = (
        released == 1
        and name == WHEEL_NAME
        and sha_matches
        and check8 == "SIGNED"
        and seven_passed
        and check.get("verdict") == "checked"
    )
    print("JOURNEY-RELEASE released=%d check8=%s file=%s sha256=%s ok=%s" % (released, check8, name, sha[:12], ok))
    print("JOURNEY-RELEASE-DETAIL release_folder=%s members=%s delivery_text_present=%s sha_equals_fetch_and_check=%s "
          "checks_1_to_7_passed=%s check_verdict=%s check8_path=%s signature_file_exists=%s"
          % (folder.name, [p.name for p in members], delivery_here, sha_matches, seven_passed, check.get("verdict"),
             (c8.get("evidence") or {}).get("path"), sig_exists))
    return ok


def cmd_pack() -> bool:
    folder = pack_dir()
    files = sorted(p.name for p in folder.iterdir() if p.is_file()) if folder.is_dir() else []
    manifest_ok = False
    man_path = folder / "MANIFEST.json"
    if man_path.is_file():
        try:
            man = read_json(man_path)
            entries = man.get("files", [])
            e = entries[0] if len(entries) == 1 and isinstance(entries[0], dict) else {}
            manifest_ok = (
                man.get("schema") == "intake-manifest/1"
                and man.get("batch") == BATCH
                and len(entries) == 1
                and e.get("name") == WHEEL_NAME
                and e.get("sha256") == sha256_of(folder / WHEEL_NAME)
                and e.get("check_record") == WHEEL_NAME + ".check.json"
                and e.get("check_record_sha256") == sha256_of(folder / e["check_record"])
                and e.get("delivery") == WHEEL_NAME + ".delivery.txt"
                and e.get("delivery_sha256") == sha256_of(folder / e["delivery"])
            )
        except (OSError, ValueError, KeyError, TypeError):
            manifest_ok = False
    verify_script = REPO_ROOT / "org" / "devices" / "intake" / "intake_receive.py"
    env = dict(os.environ, AGENTBUS_DEVICE="laptop")
    proc = subprocess.run([sys.executable, str(verify_script), "verify", "--from", str(folder)],
                          capture_output=True, text=True, env=env, timeout=120)
    vlines = [ln for ln in proc.stdout.splitlines() if ln.startswith("INTAKE-VERIFY")]
    verify_last = vlines[-1] if vlines else "NONE"
    verify_ok = (proc.returncode == 0
                 and re.search(r"wheels=1 verified=1 checked=1 stray=0 ok=True$", verify_last) is not None)
    ok = len(files) == PACK_FILE_COUNT and manifest_ok and verify_ok
    print("JOURNEY-PACK files=%d manifest_ok=%s verify=%s ok=%s" % (len(files), manifest_ok, verify_last, ok))
    print("JOURNEY-PACK-DETAIL pack=%s names=%s verify_rc=%d" % (folder.name, files, proc.returncode))
    return ok


def cmd_taildrop() -> bool:
    path = records_dir() / TAILDROP_RECORD_NAME
    text = path.read_text(encoding="utf-8") if path.is_file() else ""
    rows = []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 4 and TIME_RE.match(cells[0]) and "tailscale file cp" in cells[1]:
            rows.append(cells)
    sent = sum(1 for r in rows if r[2] == "0")
    failed = len(rows) - sent
    to_dell1 = bool(rows) and all(r[1].rstrip("`").endswith("dell1:") for r in rows)
    distinct = len(set(r[1] for r in rows)) == len(rows)
    ok = sent == PACK_FILE_COUNT and failed == 0 and to_dell1 and distinct and len(rows) == PACK_FILE_COUNT
    print("JOURNEY-TAILDROP files_sent=%d failed=%d target=dell1 ok=%s" % (sent, failed, ok))
    print("JOURNEY-TAILDROP-DETAIL record=%s rows=%d exit_codes=%s to_dell1=%s distinct_commands=%s"
          % (path.name, len(rows), [r[2] for r in rows], to_dell1, distinct))
    return ok


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--fetch", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--tag", action="store_true")
    ap.add_argument("--release", action="store_true")
    ap.add_argument("--pack", action="store_true")
    ap.add_argument("--taildrop", action="store_true")
    args = ap.parse_args()
    run_all = not (args.fetch or args.check or args.tag or args.release or args.pack or args.taildrop)
    results = []
    if args.fetch or run_all:
        results.append(cmd_fetch())
    if args.check or run_all:
        results.append(cmd_check())
    if args.tag or run_all:
        results.append(cmd_tag())
    if args.release:
        results.append(cmd_release())
    if args.pack:
        results.append(cmd_pack())
    if args.taildrop:
        results.append(cmd_taildrop())
    return 0 if results and all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
