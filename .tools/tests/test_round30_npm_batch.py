#!/usr/bin/env python3
"""test_round30_npm_batch.py -- READ-ONLY batch record test for NFRA_CTLPLN round 30, CT-ce-1.

Batch intake-20261016-npm-mcportal-bun: 50 approved npm tarballs (name@version lines of the CTO approval file for
mcportal@c66ca82952, dell1 AMGT_HARVST HVST-cc-7). This test only READS the approval file, the lockfile, the fetch and
check records, the holding and release folders, the facts file and the lib/devices register. It makes no network
request, writes nothing, installs nothing, runs no package manager and never opens a tarball's members (the names of
the held files and their sha512 digests are read; no archive is extracted or listed here).

Flags (each prints the summary line last; exit 0 only when every requested line says ok=True):
  --fetch    NPM-BATCH-FETCH tarballs=<n> expected=50 names_equal=<True|False> sha512_equal=<True|False> held=<h>
             device=<d> ok=<True|False>
             ok: exactly the 50 approved held file names in the holding folder and no other file, each file's sha512
             (base64, as npm writes dist.integrity) equal to BOTH the lockfile integrity for its name@version and its
             fetch record's published integrity, every fetch record's outcome 'held', the record's device equal to this
             box, and nothing in the release folder. Mutants (must read held=True): a 51st file on disk; one record whose
             digest differs.
  --check    NPM-BATCH-CHECK tarballs=<n> checks_run_each=<k> failed_total=<f> not_applicable_total=<m> check8=<AWAITING|SIGNED|OTHER>
             released=<True|False> ok=<True|False>
             one NPM-BATCH-CHECK-FAIL <file> check <n> <evidence> line per failed check 1-7 (a finding, never an error).
             ok: all 50 check records present, checks 1-7 each carrying a verdict, check 8 AWAITING (no signature file,
             nothing released) or SIGNED and released. failed_total does NOT make ok False.
             Mutants (must read held=True): check 8 SIGNED without a release; AWAITING with a release; 49 of 50 records.
  --natives  NPM-BATCH-NATIVES tarballs=<n> lifecycle=<l> native=<v> listed_in_facts=<True|False> ok=<True|False>
             one NPM-BATCH-LIFECYCLE <file> <scripts> line and one NPM-BATCH-NATIVE <file> <named> line per package.
             ok: the lifecycle and native counts equal what the check 6 records carry, the facts file's two lists name
             exactly those packages, and the facts file's own count lines agree. Mutant (must read held=True): one
             package dropped from the facts list.

Paths: records  OPAL_INTAKE_RECORDS (a base; batch folder under it), else org/devices/intake/records beside this repo.
       holding  OPAL_INTAKE_ROOT (a root; holding/<batch>/ and release/<batch>/ under it), else <drive of this repo>/opal-intake.
Standard library only; Python 3.12; ASCII output.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import pathlib
import re
import sys

BATCH = "intake-20261016-npm-mcportal-bun"
EXPECTED = 50
CHECKS_TOTAL = 7
REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
RECORDS_DEFAULT = REPO_ROOT / "org" / "devices" / "intake" / "records"
APPROVAL_REL = ("org/tier1_exec/1.0.0_SA_CTO/deliverables/"
                "CTO_APPROVAL_TO_FETCH_NFRA_CTLPLN_INTAKE_NPM_MCPORTAL_BUN_20261016.md")
LOCK_REL = "org/tier0_exec/0.0.0_AB_MSTR/deliverables/MCPORTAL_c66ca82952_bun.lock"
LOCK_SHA256 = "7e6b71c2ea3876561f18e2df606203a78b48bd7013404bf26d614ea70d10c4bc"
LOCK_LINES = 278
CHECK8_SIG_REL = ("org/tier1_exec/1.0.0_SA_CTO/deliverables/"
                  "CTO_CHECK8_NFRA_CTLPLN_INTAKE_NPM_MCPORTAL_BUN_20261016.md")
FACTS_REL = ("org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~149/NPM_BATCH_FACTS.md")
RAN = ("passed", "failed", "not_applicable")
LINE_RE = re.compile(r"^((?:@[a-z0-9][a-z0-9._-]*/)?[a-z0-9][a-z0-9._-]*)@([0-9][^\s]*)$")
FAIL_LINE_CAP = 400


def ascii_text(value):
    return str(value).replace("\r", " ").replace("\n", " ").encode("ascii", "replace").decode("ascii")


def records_dir() -> pathlib.Path:
    base = os.environ.get("OPAL_INTAKE_RECORDS") or str(RECORDS_DEFAULT)
    return pathlib.Path(base) / BATCH


def holding_root() -> pathlib.Path:
    root = os.environ.get("OPAL_INTAKE_ROOT")
    if not root:
        return pathlib.Path(REPO_ROOT.anchor) / "opal-intake"
    return pathlib.Path(root)


def holding_dir() -> pathlib.Path:
    return holding_root() / "holding" / BATCH


def release_dir() -> pathlib.Path:
    return holding_root() / "release" / BATCH


def read_json(path: pathlib.Path):
    if not path.is_file():
        return None
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def sha512_b64(path: pathlib.Path) -> str:
    h = hashlib.sha512()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return "sha512-" + base64.b64encode(h.digest()).decode("ascii")


def strip_trailing_commas(text: str) -> str:
    """bun writes its text lockfile as JSON with trailing commas; each comma followed by a closing brace or bracket is
    dropped, outside strings only."""
    out, in_str, esc, i, n = [], False, False, 0, len(text)
    while i < n:
        ch = text[i]
        if in_str:
            out.append(ch)
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
            i += 1
            continue
        if ch == '"':
            in_str = True
        elif ch == ",":
            j = i + 1
            while j < n and text[j] in " \t\r\n":
                j += 1
            if j < n and text[j] in "}]":
                i += 1
                continue
        out.append(ch)
        i += 1
    return "".join(out)


def lock_integrities(ident: str) -> list:
    raw = (REPO_ROOT / LOCK_REL).read_bytes()
    lock = json.loads(strip_trailing_commas(raw.decode("utf-8")))
    found = []
    for _key, val in lock.get("packages", {}).items():
        if isinstance(val, list) and val and val[0] == ident:
            integ = val[3] if len(val) > 3 and isinstance(val[3], str) else None
            if integ not in found:
                found.append(integ)
    return found


def expected_table() -> dict:
    """held file name -> {name, version, ident}, from the approval file's name@version lines (exactly 50 expected)."""
    out = {}
    text = (REPO_ROOT / APPROVAL_REL).read_text(encoding="utf-8", errors="replace")
    for ln in text.splitlines():
        s = ln.split("#", 1)[0].strip()
        m = LINE_RE.match(s)
        if not m:
            continue
        name, version = m.group(1), m.group(2)
        held = name.replace("@", "").replace("/", "__") + "-" + version + ".tgz"
        out[held] = {"name": name, "version": version, "ident": "%s@%s" % (name, version)}
    return out


def this_box():
    sys.path.insert(0, str(REPO_ROOT / "lib"))
    import devices  # the register reader (lib/devices.py); fail-closed: an unresolved box is None
    name, _basis = devices.this_device()
    return name


def files_in(folder: pathlib.Path) -> list:
    if not folder.is_dir():
        return []
    return sorted(p.name for p in folder.iterdir() if p.is_file())


# ------------------------------------------------------------------------------------------------------------ --fetch

def fetch_ok(expected_n, present_n, names_equal, sha_equal, held, device_ok, released_n) -> bool:
    return (expected_n == EXPECTED and present_n == EXPECTED and names_equal and sha_equal
            and held == EXPECTED and device_ok and released_n == 0)


FETCH_MUTANTS = (
    ("fifty_first_file_on_disk", {"names_equal": False}),
    ("record_digest_differs", {"sha_equal": False}),
)


def cmd_fetch() -> bool:
    exp = expected_table()
    lock_ok = True
    lock_bytes = (REPO_ROOT / LOCK_REL).read_bytes()
    lock_sha = hashlib.sha256(lock_bytes).hexdigest()
    lock_lines = lock_bytes.decode("utf-8").count("\n")
    if lock_sha != LOCK_SHA256 or lock_lines != LOCK_LINES:
        lock_ok = False
    print("NPM-BATCH-LOCK sha256=%s lines=%d ok=%s" % (lock_sha, lock_lines, lock_ok))
    on_disk = set(files_in(holding_dir()))
    names_equal = (len(exp) == EXPECTED and on_disk == set(exp))
    released = files_in(release_dir())
    box = this_box()
    sha_equal = True
    device_ok = True
    held = 0
    present = 0
    for fn, e in sorted(exp.items()):
        rec = read_json(records_dir() / (fn + ".fetch.json"))
        integs = lock_integrities(e["ident"])
        lock_one = integs[0] if len(integs) == 1 else None
        if lock_one is None or not lock_one.startswith("sha512-"):
            sha_equal = False
            print("NPM-BATCH-FETCH-LOCK %s lockfile entries=%d" % (e["ident"], len(integs)))
        if rec is None or rec.get("device") != box:
            device_ok = False
        reg = ((rec or {}).get("published") or {}).get("integrity")
        if fn in on_disk:
            present += 1
            if rec is not None and rec.get("outcome") == "held":
                held += 1
            digest = sha512_b64(holding_dir() / fn)
            if not (digest == lock_one and digest == reg):
                sha_equal = False
                print("NPM-BATCH-FETCH-DIGEST %s disk=%s lock=%s record=%s" % (fn, digest, lock_one, reg))
        else:
            sha_equal = False
            print("NPM-BATCH-FETCH-MISSING %s record=%s" % (fn, (rec or {}).get("outcome", "NONE")))
    for fn in sorted(on_disk - set(exp)):
        print("NPM-BATCH-FETCH-EXTRA %s" % fn)
    for fn in released:
        print("NPM-BATCH-FETCH-RELEASED %s" % fn)
    ok = fetch_ok(len(exp), present, names_equal, sha_equal, held, device_ok, len(released)) and lock_ok
    mutants_held = True
    for label, over in FETCH_MUTANTS:
        base = dict(expected_n=len(exp), present_n=present, names_equal=names_equal, sha_equal=sha_equal,
                    held=held, device_ok=device_ok, released_n=len(released))
        base.update(over)
        m_ok = fetch_ok(**base)
        mutants_held = mutants_held and not m_ok
        print("NPM-BATCH-FETCH-MUTANT case=%s ok=%s expected=False held=%s" % (label, m_ok, not m_ok))
    ok = ok and mutants_held
    print("NPM-BATCH-FETCH tarballs=%d expected=%d names_equal=%s sha512_equal=%s held=%d device=%s ok=%s"
          % (present, EXPECTED, names_equal, sha_equal, held, ascii_text(box), ok))
    return ok


# ------------------------------------------------------------------------------------------------------------ --check

def check_ok(wheels, ran_each, check8, released) -> bool:
    if wheels != EXPECTED or ran_each != CHECKS_TOTAL:
        return False
    return (check8, released) in (("AWAITING", False), ("SIGNED", True))


CHECK_MUTANTS = (
    ("signed_not_released", (EXPECTED, CHECKS_TOTAL, "SIGNED", False)),
    ("awaiting_released", (EXPECTED, CHECKS_TOTAL, "AWAITING", True)),
    ("forty_nine_of_fifty", (EXPECTED - 1, CHECKS_TOTAL, "AWAITING", False)),
)


def cmd_check() -> bool:
    exp = expected_table()
    present = {}
    for fn in sorted(exp):
        rec = read_json(records_dir() / (fn + ".check.json"))
        if rec is not None:
            present[fn] = rec
    sig_exists = (REPO_ROOT / CHECK8_SIG_REL).is_file()
    ran_counts = []
    failed = []
    na_total = 0
    states = set()
    for fn, rec in sorted(present.items()):
        by_n = {c.get("n"): c for c in rec.get("checks", []) if isinstance(c, dict)}
        ran = 0
        for n in range(1, CHECKS_TOTAL + 1):
            c = by_n.get(n)
            if c is None:
                continue
            v = c.get("verdict")
            if v in RAN:
                ran += 1
            if v == "not_applicable":
                na_total += 1
            if v == "failed":
                summary = (c.get("evidence") or {}).get("summary", "")
                failed.append((fn, n, summary))
        ran_counts.append(ran)
        v8 = (by_n.get(8) or {}).get("verdict")
        if v8 == "awaiting" and not sig_exists:
            states.add("AWAITING")
        elif v8 == "passed" and sig_exists:
            states.add("SIGNED")
        else:
            states.add("OTHER")
    for fn, n, summary in failed:
        print("NPM-BATCH-CHECK-FAIL %s check %d %s" % (fn, n, ascii_text(summary)[:FAIL_LINE_CAP]))
    ran_each = min(ran_counts) if ran_counts else 0
    check8 = states.pop() if len(states) == 1 else "OTHER"
    released = len(files_in(release_dir())) > 0
    ok = check_ok(len(present), ran_each, check8, released)
    mutants_held = True
    for label, args in CHECK_MUTANTS:
        m_ok = check_ok(*args)
        mutants_held = mutants_held and not m_ok
        print("NPM-BATCH-CHECK-MUTANT case=%s ok=%s expected=False held=%s" % (label, m_ok, not m_ok))
    ok = ok and mutants_held
    print("NPM-BATCH-CHECK tarballs=%d checks_run_each=%d failed_total=%d not_applicable_total=%d check8=%s released=%s ok=%s"
          % (len(present), ran_each, len(failed), na_total, check8, released, ok))
    return ok


# ------------------------------------------------------------------------------------------------------------ --natives

def facts_lists(text: str):
    """(lifecycle {file: 'text'}, native {file: 'text'}, counts {'lifecycle': n, 'native': n}) read from the facts file."""
    counts = {}
    current = None
    lists = {"lifecycle": {}, "native": {}}
    for line in text.splitlines():
        if line.startswith("## "):
            if line.startswith("## Lifecycle-script packages"):
                current = "lifecycle"
            elif line.startswith("## Native-binary or os/cpu-restricted packages"):
                current = "native"
            else:
                current = None
            continue
        if current is None or not line.startswith("- "):
            continue
        body = line[2:]
        m = re.match(r"^count:\s*(\d+)\s*$", body)
        if m:
            counts[current] = int(m.group(1))
            continue
        head, sep, rest = body.partition(": ")
        if sep and head.endswith(".tgz"):
            lists[current][head] = rest
    return lists["lifecycle"], lists["native"], counts


def natives_ok(rec_life: set, rec_nat: set, fact_life: set, fact_nat: set, fact_counts: dict) -> bool:
    return (rec_life == fact_life and rec_nat == fact_nat
            and fact_counts.get("lifecycle") == len(rec_life) and fact_counts.get("native") == len(rec_nat))


def cmd_natives() -> bool:
    exp = expected_table()
    rec_life, rec_nat = {}, {}
    read_n = 0
    for fn in sorted(exp):
        rec = read_json(records_dir() / (fn + ".check.json"))
        if rec is None:
            continue
        read_n += 1
        ev6 = ((rec.get("checks") or [None] * 6)[5] or {}).get("evidence") or {}
        life = ev6.get("lifecycle_scripts") or []
        nat = ev6.get("native_binaries") or []
        restr = ev6.get("restricted")
        if life:
            rec_life[fn] = "; ".join("%s = %s" % (x.get("name", "?"), x.get("command", "")) for x in life)
        if nat or restr:
            rec_nat[fn] = "; ".join(nat) if nat else "os/cpu restricted"
    for fn in sorted(rec_life):
        print("NPM-BATCH-LIFECYCLE %s %s" % (fn, ascii_text(rec_life[fn])))
    for fn in sorted(rec_nat):
        print("NPM-BATCH-NATIVE %s %s" % (fn, ascii_text(rec_nat[fn])))
    facts_path = REPO_ROOT / FACTS_REL
    text = facts_path.read_text(encoding="utf-8") if facts_path.is_file() else ""
    fact_life, fact_nat, fact_counts = facts_lists(text)
    listed = (set(fact_life) == set(rec_life) and set(fact_nat) == set(rec_nat)
              and fact_counts.get("lifecycle") == len(rec_life) and fact_counts.get("native") == len(rec_nat))
    ok = read_n == EXPECTED and listed
    # mutant: one package dropped from the facts list must read not-ok
    mut_fact = dict(fact_life)
    if mut_fact:
        mut_fact.pop(sorted(mut_fact)[0])
    m_ok = natives_ok(set(rec_life), set(rec_nat), set(mut_fact), set(fact_nat), fact_counts)
    mutant_held = not m_ok
    print("NPM-BATCH-NATIVES-MUTANT case=dropped_from_facts ok=%s expected=False held=%s" % (m_ok, mutant_held))
    ok = ok and mutant_held
    print("NPM-BATCH-NATIVES tarballs=%d lifecycle=%d native=%d listed_in_facts=%s ok=%s"
          % (read_n, len(rec_life), len(rec_nat), listed, ok))
    return ok


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--fetch", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--natives", action="store_true")
    a = ap.parse_args()
    if not (a.fetch or a.check or a.natives):
        a.fetch = a.check = a.natives = True
    results = []
    if a.fetch:
        results.append(cmd_fetch())
    if a.check:
        results.append(cmd_check())
    if a.natives:
        results.append(cmd_natives())
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
