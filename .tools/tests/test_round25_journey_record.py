#!/usr/bin/env python3
"""test_round25_journey_record.py -- READ-ONLY journey record test for NFRA_CTLPLN round 25, CT-ao-1 and CT-ao-2.

Batch intake-20261016-tabulate: ONE tabulate 0.9.0 wheel, the pure-Python py3-none-any one, fetched through
intake_fetch.py, checked by intake_check.py (checks 1-8), released, packed and sent by Taildrop to dell1 (CT-ao-2).
This test only READS the records, the holding, release and pack folders and TAILDROP_RECORD.md. It makes no network
request, writes nothing, installs nothing, runs no package file and never calls Tailscale. It is the round-22 test's
shape, wired to this batch; the constants are this batch's own.

Flags (each prints one line; exit 0 only when every requested line says ok=True):
  --fetch   JOURNEY-FETCH wheels=<n> file=<name> device=<d> sha256=<12 hex> requests=<r> ok=<True|False>
            (state-aware: the batch's one wheel, in holding OR release; a released wheel is moved; mutants held)
  --check   JOURNEY-CHECK checks_run=<n> failed=<f> check8=<AWAITING|SIGNED|OTHER> released=<True|False> ok=<True|False>
            (state-aware: ok only in the pre-signature state (AWAITING, not released) or the post-release state
            (SIGNED, released), with checks 1-7 run and 0 failed; mutants held)
  --release JOURNEY-RELEASE released=<n> check8=<SIGNED|OTHER> file=<name> sha256=<12 hex> ok=<True|False>
            (the release folder holds exactly the wheel and its delivery text; the bytes equal the fetch and check
            records' SHA-256; the check record reads checked with checks 1-7 passed and names the CTO's signed file)
  --pack    JOURNEY-PACK files=<n> manifest_ok=<True|False> verify=<INTAKE-VERIFY last line> ok=<True|False>
            (the pack folder holds exactly the wheel, its .check.json, its .delivery.txt and MANIFEST.json; the manifest
            names their SHA-256; the local intake_receive.py verify last line reads wheels=1 verified=1 checked=1
            stray=0 ok=True; the verify is local, read only)
  --taildrop JOURNEY-TAILDROP files_sent=<n> failed=<f> target=dell1 ok=<True|False>
            (reads ONLY TAILDROP_RECORD.md: four send rows, each exit code 0, each to dell1, each naming one pack file)
  --taildrop-sitez JOURNEY-TAILDROP-SITEZ files_sent=<n> failed=<f> target=sitez ok=<True|False>
            (reads ONLY TAILDROP_RECORD_SITEZ.md for its send rows and its file table; the pack folder is read for SHA-256
            only; it never calls Tailscale. ok: four send rows, each exit code 0, 0 failed, each to sitez:, each naming one
            pack file once, distinct commands, and the record's SHA-256 of each file equal to the pack file on disk.
            Mutants (must read held=True): a row with a nonzero exit code; a row naming another device.)
--fetch ok requires: exactly ONE wheel in the batch wherever it sits, named WHEEL_NAME; no file other than .whl in the
holding folder; the SHA-256 on disk equals the fetch record's held_sha256; the fetch record's device equals this box.
Mutants (must read held=True): a second wheel in the holding folder; a record whose SHA-256 differs from the disk file.

The check record is read from the records folder only; check 8 is SIGNED only when the signature file exists at the
path the check tool requires.

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

BATCH = "intake-20261016-tabulate"
WHEEL_NAME = "tabulate-0.9.0-py3-none-any.whl"
SECOND_WHEEL = "tabulate-0.9.0-py2.py3-none-any.whl"
DELIVERY_NAME = WHEEL_NAME + ".delivery.txt"
CHECK_NAME = WHEEL_NAME + ".check.json"
MANIFEST_NAME = "MANIFEST.json"
PACK_NAMES = sorted([WHEEL_NAME, CHECK_NAME, DELIVERY_NAME, MANIFEST_NAME])
PACK_FILE_COUNT = 4
REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
CHECK8_SIGNATURE_REL = "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_CHECK8_NFRA_CTLPLN_INTAKE_TABULATE_20261016.md"
CHECKS_FIRST, CHECKS_LAST = 1, 7
TIME_RE = re.compile(r"^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
TAILDROP_RECORD_NAME = "TAILDROP_RECORD.md"
TAILDROP_TARGET = "dell1"
SITEZ_RECORD_NAME = "TAILDROP_RECORD_SITEZ.md"
SITEZ_TARGET = "sitez"
FILE_ROW_RE = re.compile(r"^[1-9]\d*$")


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


def pack_dir() -> pathlib.Path:
    return pathlib.Path(os.path.expanduser("~")) / "tdrop" / "out" / BATCH


def seven_row_ok(row) -> bool:
    """A check 1-7 row is good when it passed, or it is not_applicable WITH a stated reason (the check tool's own rule)."""
    if not isinstance(row, dict):
        return False
    if row.get("verdict") == "passed":
        return True
    ev = row.get("evidence") or {}
    return row.get("verdict") == "not_applicable" and bool(str(ev.get("reason", "")).strip())


def cmd_release() -> bool:
    folder = release_dir()
    members = sorted(p.name for p in folder.iterdir() if p.is_file()) if folder.is_dir() else []
    wheels_here = [m for m in members if not m.endswith(".delivery.txt")]
    released = len(wheels_here)
    name = wheels_here[0] if released == 1 else "NONE"
    exact_members = members == sorted([WHEEL_NAME, DELIVERY_NAME])
    check_path = records_dir() / CHECK_NAME
    check = read_json(check_path) if check_path.is_file() else {}
    fetch_path = records_dir() / (WHEEL_NAME + ".fetch.json")
    fetch = read_json(fetch_path) if fetch_path.is_file() else {}
    by_n = {c.get("n"): c for c in check.get("checks", []) if isinstance(c, dict)}
    c8 = by_n.get(8) or {}
    sig_exists = (REPO_ROOT / CHECK8_SIGNATURE_REL).is_file()
    check8 = "SIGNED" if (c8.get("verdict") == "passed" and sig_exists
                          and (c8.get("evidence") or {}).get("path") == CHECK8_SIGNATURE_REL) else "OTHER"
    seven_passed = all(seven_row_ok(by_n.get(n)) for n in range(CHECKS_FIRST, CHECKS_LAST + 1))
    sha = sha256_of(folder / name) if released == 1 else "-"
    sha_matches = (released == 1 and name == WHEEL_NAME and sha == fetch.get("held_sha256")
                   and sha == check.get("held_sha256"))
    ok = (
        released == 1
        and name == WHEEL_NAME
        and exact_members
        and sha_matches
        and check8 == "SIGNED"
        and seven_passed
        and check.get("verdict") == "checked"
    )
    print("JOURNEY-RELEASE released=%d check8=%s file=%s sha256=%s ok=%s" % (released, check8, name, sha[:12], ok))
    print("JOURNEY-RELEASE-DETAIL release_folder=%s members=%s exact_members=%s sha_equals_fetch_and_check=%s "
          "checks_1_to_7_passed=%s check_verdict=%s check8_path=%s signature_file_exists=%s"
          % (folder.name, members, exact_members, sha_matches, seven_passed, check.get("verdict"),
             (c8.get("evidence") or {}).get("path"), sig_exists))
    return ok


def cmd_pack() -> bool:
    folder = pack_dir()
    files = sorted(p.name for p in folder.iterdir() if p.is_file()) if folder.is_dir() else []
    names_exact = files == PACK_NAMES
    manifest_ok = False
    man_path = folder / MANIFEST_NAME
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
                and e.get("check_record") == CHECK_NAME
                and e.get("check_record_sha256") == sha256_of(folder / CHECK_NAME)
                and e.get("delivery") == DELIVERY_NAME
                and e.get("delivery_sha256") == sha256_of(folder / DELIVERY_NAME)
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
    ok = len(files) == PACK_FILE_COUNT and names_exact and manifest_ok and verify_ok
    print("JOURNEY-PACK files=%d manifest_ok=%s verify=%s ok=%s" % (len(files), manifest_ok, verify_last, ok))
    print("JOURNEY-PACK-DETAIL pack=%s names=%s names_exact=%s verify_rc=%d"
          % (folder.name, files, names_exact, proc.returncode))
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
    to_dell1 = bool(rows) and all(r[1].rstrip("`").endswith(TAILDROP_TARGET + ":") for r in rows)
    distinct = len(set(r[1] for r in rows)) == len(rows)
    # each command's quoted path ends in one pack file name (backslash before, quote after): one row per name
    each_pack_file = all(sum(1 for r in rows if ("\\" + n + '"') in r[1]) == 1 for n in PACK_NAMES)
    ok = (sent == PACK_FILE_COUNT and failed == 0 and len(rows) == PACK_FILE_COUNT and to_dell1 and distinct
          and each_pack_file)
    print("JOURNEY-TAILDROP files_sent=%d failed=%d target=%s ok=%s" % (sent, failed, TAILDROP_TARGET, ok))
    print("JOURNEY-TAILDROP-DETAIL record=%s rows=%d exit_codes=%s to_dell1=%s distinct_commands=%s each_pack_file_once=%s"
          % (path.name, len(rows), [r[2] for r in rows], to_dell1, distinct, each_pack_file))
    return ok


def sitez_parse(text: str):
    """(send rows, file rows). A send row is [time, command, exit, outcome] with a UTC time and a 'tailscale file cp'
    command; a file row is [n, name, bytes, sha256] with a positive integer n. Other table rows are ignored."""
    sends, files = [], []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 4:
            continue
        if TIME_RE.match(cells[0]) and "tailscale file cp" in cells[1]:
            sends.append(cells)
        elif FILE_ROW_RE.match(cells[0]):
            files.append(cells)
    return sends, files


def sitez_target_of(command: str) -> str:
    """The last token of a send command: the target with its trailing colon (backtick wrapper stripped)."""
    toks = command.strip().strip("`").split()
    return toks[-1] if toks else ""


def sitez_command_names(command: str) -> list[str]:
    """The pack file names a command's quoted path ends in: a path separator before the name, a quote after it."""
    return [n for n in PACK_NAMES if re.search(r'[\\/]' + re.escape(n) + r'"', command)]


def sitez_facts(sends, files, disk: dict) -> dict:
    """Every fact the --taildrop-sitez ok is built from; disk maps each pack file name to its SHA-256 read from disk."""
    table = {r[1]: r[3] for r in files}
    named = [sitez_command_names(r[1]) for r in sends]
    return {
        "rows": len(sends),
        "files_rows": len(files),
        "exit_zero": sum(1 for r in sends if r[2] == "0"),
        "to_sitez": bool(sends) and all(sitez_target_of(r[1]) == SITEZ_TARGET + ":" for r in sends),
        "distinct": len(set(r[1] for r in sends)) == len(sends),
        "names_once": sorted(x for ns in named for x in ns) == PACK_NAMES and all(len(ns) == 1 for ns in named),
        "shas_equal": all(n in disk and table.get(n) == disk[n] for n in PACK_NAMES),
    }


def sitez_ok(f: dict) -> bool:
    """ok: four send rows, each exit 0 (so 0 failed), each to sitez:, distinct, each pack file named once, and the
    record's SHA-256 of every pack file equal to the file on disk."""
    return (f["rows"] == PACK_FILE_COUNT and f["files_rows"] == PACK_FILE_COUNT and f["exit_zero"] == PACK_FILE_COUNT
            and f["to_sitez"] and f["distinct"] and f["names_once"] and f["shas_equal"])


def sitez_mutate(sends, kind: str):
    """A copy of the send rows with one defect: 'exit' sets the first row's exit code to 1; 'device' retargets it to dell1:."""
    out = [list(r) for r in sends]
    if kind == "exit":
        out[0][2] = "1"
    elif kind == "device":
        out[0][1] = re.sub(r"sitez:(`?)$", r"dell1:\1", out[0][1])
    return out


SITEZ_MUTANTS = (("nonzero_exit_row", "exit"), ("other_device_row", "device"))


def pack_sha256s() -> dict:
    folder = pack_dir()
    return {n: sha256_of(folder / n) for n in PACK_NAMES if (folder / n).is_file()}


def cmd_taildrop_sitez() -> bool:
    path = records_dir() / SITEZ_RECORD_NAME
    text = path.read_text(encoding="utf-8") if path.is_file() else ""
    sends, files = sitez_parse(text)
    disk = pack_sha256s()
    facts = sitez_facts(sends, files, disk)
    ok = sitez_ok(facts)
    mutants_held = True
    for label, kind in SITEZ_MUTANTS:
        m_ok = sitez_ok(sitez_facts(sitez_mutate(sends, kind), files, disk))
        mutants_held = mutants_held and not m_ok
        print("JOURNEY-TAILDROP-SITEZ-MUTANT case=%s ok=%s expected=False held=%s" % (label, m_ok, not m_ok))
    ok = ok and mutants_held
    sent = facts["exit_zero"]
    print("JOURNEY-TAILDROP-SITEZ files_sent=%d failed=%d target=%s ok=%s"
          % (sent, len(sends) - sent, SITEZ_TARGET, ok))
    print("JOURNEY-TAILDROP-SITEZ-DETAIL record=%s rows=%d files_rows=%d exit_codes=%s to_sitez=%s distinct_commands=%s "
          "names_once=%s shas_equal_pack_on_disk=%s pack_files_on_disk=%d mutants_held=%s"
          % (path.name, facts["rows"], facts["files_rows"], [r[2] for r in sends], facts["to_sitez"], facts["distinct"],
             facts["names_once"], facts["shas_equal"], len(disk), mutants_held))
    return ok


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--fetch", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--release", action="store_true")
    ap.add_argument("--pack", action="store_true")
    ap.add_argument("--taildrop", action="store_true")
    ap.add_argument("--taildrop-sitez", action="store_true")
    args = ap.parse_args()
    run_all = not (args.fetch or args.check or args.release or args.pack or args.taildrop or args.taildrop_sitez)
    results = []
    if args.fetch or run_all:
        results.append(cmd_fetch())
    if args.check or run_all:
        results.append(cmd_check())
    if args.release:
        results.append(cmd_release())
    if args.pack:
        results.append(cmd_pack())
    if args.taildrop:
        results.append(cmd_taildrop())
    if args.taildrop_sitez:
        results.append(cmd_taildrop_sitez())
    return 0 if results and all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
