#!/usr/bin/env python3
"""test_round27_yfinance_batch.py -- READ-ONLY batch record test for NFRA_CTLPLN round 27, CT-at-1.

Batch intake-20261016-yfinance-linux: 17 approved wheels for cp312 linux x86_64. Sixteen are named by the resolve table
(RESOLVED_cp312_linux_x86_64.json) and the CTO's ADDENDUM 1; the seventeenth, multitasking-0.0.13-py3-none-any.whl, by
ADDENDUM 2 (its sha256 and size are read from the approval file text). This test only READS the fetch and check records,
the holding and release folders, the approval file and the closure and host files. It makes no network request, writes
nothing, installs nothing, imports no package and runs no package file. Wheels are opened with zipfile for METADATA only.

Flags (each prints one summary line; exit 0 only when every requested line says ok=True):
  --fetch     BATCH-FETCH wheels=<n> expected=17 names_equal=<T|F> sha_equal=<T|F> held=<h> device=<d> ok=<T|F>
              ok: exactly the 17 approved file names on disk (holding or release), no other file, each file's SHA-256
              equal to BOTH the approval/resolve value and its fetch record's, every record outcome held, record device
              equal to this box. Mutants (must read held=True): an 18th file on disk; one record whose SHA-256 differs.
  --check     BATCH-CHECK wheels=<n> expected=17 checks_run_each=<k> failed_total=<f> not_applicable_total=<m>
              check8=<AWAITING|SIGNED|OTHER> released=<T|F> ok=<T|F>
              one BATCH-CHECK-FAIL <file> check <n> <evidence> line per failed check 1-7 (a finding, never an error).
              ok: all 17 check records present, checks 1-7 each with a verdict, check 8 AWAITING (no signature file,
              nothing released) or SIGNED and released. failed_total does NOT make ok False.
              Mutants (must read held=True): check 8 SIGNED without a release; AWAITING with a release; 16 of 17 records.
  --requires  BATCH-REQUIRES wheels=<n> expected=17 new_deps=<d> specifier_mismatches=<s> host_conflicts=<h>
              multitasking_requires=<lines or NONE or NOT-HELD> ok=<T|F>
              for each held wheel, its own METADATA Requires-Dist, minus lines whose marker is false for the linux cp312
              target and any 'extra' line. Every named distribution must be one of the 17 (its chosen version meets the
              specifier) or one of the 7 host-satisfied (the host version meets it). Each violation prints one
              BATCH-REQUIRES-STOP line. ok also needs all 17 wheels read and exactly 7 host-satisfied members.

  --release   BATCH-RELEASE released=<n> check8=<SIGNED|OTHER> names_equal=<True|False> sha_equal=<True|False> ok=<True|False>
              read-only. ok: the release folder holds exactly the 17 approved wheels plus one <name>.delivery.txt each, each
              wheel's bytes equal its fetch record's held_sha256, every check record reads 'checked' with check 8 passed and
              naming the CTO's signed check-8 file, and the holding folder holds none of the 17. Opt-in: not in the default run.
  --pack      BATCH-PACK files=<n> manifest_ok=<True|False> verify=<INTAKE-VERIFY last line> ok=<True|False>
              read-only; runs intake_receive.py verify locally on ~/tdrop/out/<batch> (never sends). ok: 52 files in the pack
              folder, MANIFEST.json names the 17 wheels with their on-disk SHA-256, and verify's last line reads wheels=17
              verified=17 checked=17 stray=0 ok=True. Opt-in: not in the default run.

Paths: records  OPAL_INTAKE_RECORDS (a base; batch folder under it), else org/devices/intake/records beside this repo.
       holding  OPAL_INTAKE_ROOT (a root; holding/<batch>/ and release/<batch>/ under it), else <drive of this repo>/opal-intake.
Standard library plus the kit (org/devices/kit_python_wheels.py) for markers and specifiers; Python 3.12; ASCII output.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import pathlib
import re
import subprocess
import sys
import zipfile

BATCH = "intake-20261016-yfinance-linux"
EXPECTED = 17
HOST_SATISFIED_EXPECTED = 7
REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
RECORDS_DEFAULT = REPO_ROOT / "org" / "devices" / "intake" / "records"
RESOLVED_REL = "org/devices/intake/records/intake-20261016-yfinance-linux/RESOLVED_cp312_linux_x86_64.json"
HOST_PYDEPS_REL = "org/devices/intake/records/intake-20261016-yfinance-linux/HOST_PYDEPS.json"
CLOSURE_REL = "org/devices/intake/closure_cp312_linux_x86_64_yfinance.json"
KIT_REL = "org/devices/kit_python_wheels.py"
APPROVAL_REL = ("org/tier1_exec/1.0.0_SA_CTO/deliverables/"
                "CTO_APPROVAL_TO_FETCH_NFRA_CTLPLN_INTAKE_YFINANCE_LINUX_20261016.md")
CHECK8_SIG_REL = ("org/tier1_exec/1.0.0_SA_CTO/deliverables/"
                  "CTO_CHECK8_NFRA_CTLPLN_INTAKE_YFINANCE_LINUX_20261016.md")
RAN = ("passed", "failed", "not_applicable")
MULTI_FILE = "multitasking-0.0.13-py3-none-any.whl"


def ascii_text(value):
    return str(value).replace("\r", " ").replace("\n", " ").encode("ascii", "replace").decode("ascii")


def records_dir() -> pathlib.Path:
    base = os.environ.get("OPAL_INTAKE_RECORDS") or str(RECORDS_DEFAULT)
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


def read_json(path: pathlib.Path):
    if not path.is_file():
        return None
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def sha256_of(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def this_box():
    sys.path.insert(0, str(REPO_ROOT / "lib"))
    import devices  # the register reader (lib/devices.py); fail-closed: an unresolved box is None
    name, _basis = devices.this_device()
    return name


def load_kit():
    spec = importlib.util.spec_from_file_location("kit_python_wheels", str(REPO_ROOT / KIT_REL))
    mod = importlib.util.module_from_spec(spec)
    sys.modules["kit_python_wheels"] = mod
    spec.loader.exec_module(mod)
    if not mod.HAVE_PACKAGING:
        raise RuntimeError("the packaging library is not installed here")
    return mod


def expected_table() -> dict:
    """file name -> {name, version, sha256, size}: 16 from the resolve table, multitasking from ADDENDUM 2 of the approval."""
    out = {}
    doc = read_json(REPO_ROOT / RESOLVED_REL) or {}
    for r in doc.get("rows", []):
        fn = r.get("file_name")
        if isinstance(fn, str):
            out[fn] = {"name": r["name"], "version": r["version"], "sha256": r["sha256"], "size": r["size"]}
    text = (REPO_ROOT / APPROVAL_REL).read_text(encoding="utf-8", errors="replace")
    m = re.search(r"(multitasking-0\.0\.13-py3-none-any\.whl)\s+sha256\s+([0-9a-f]{64})\s+(\d+)\s+bytes", text)
    if m:
        out[m.group(1)] = {"name": "multitasking", "version": "0.0.13", "sha256": m.group(2), "size": int(m.group(3))}
    return out


def files_on_disk() -> dict:
    """file name -> list of places it sits ('holding' and/or 'release'); every file, wheel or not."""
    seen = {}
    for where, folder in (("holding", holding_dir()), ("release", release_dir())):
        if folder.is_dir():
            for p in sorted(folder.iterdir()):
                if p.is_file():
                    seen.setdefault(p.name, []).append(where)
    return seen


def folder_of(where: str) -> pathlib.Path:
    return holding_dir() if where == "holding" else release_dir()


# ------------------------------------------------------------------------------------------------------------ --fetch

def fetch_ok(expected_n, present_n, names_equal, sha_equal, held, device_ok) -> bool:
    return (expected_n == EXPECTED and present_n == EXPECTED and names_equal and sha_equal
            and held == EXPECTED and device_ok)


FETCH_MUTANTS = (
    ("eighteenth_file_on_disk", {"names_equal": False}),
    ("record_sha_differs", {"sha_equal": False}),
)


def cmd_fetch() -> bool:
    exp = expected_table()
    on_disk = files_on_disk()
    box = this_box()
    names_equal = (len(exp) == EXPECTED and set(on_disk) == set(exp)
                   and all(len(v) == 1 for v in on_disk.values()))
    sha_equal = True
    device_ok = True
    held = 0
    present = 0
    for fn, e in sorted(exp.items()):
        rec = read_json(records_dir() / (fn + ".fetch.json"))
        if rec is None or rec.get("device") != box:
            device_ok = False
        if rec is None or rec.get("held_sha256") != e["sha256"]:
            sha_equal = False
        if fn in on_disk:
            present += 1
            if rec is not None and rec.get("outcome") == "held":
                held += 1
            if sha256_of(folder_of(on_disk[fn][0]) / fn) != e["sha256"]:
                sha_equal = False
        else:
            sha_equal = False
            print("BATCH-FETCH-MISSING %s record=%s" % (fn, (rec or {}).get("outcome", "NONE")))
    for fn in sorted(set(on_disk) - set(exp)):
        print("BATCH-FETCH-EXTRA %s places=%s" % (fn, "+".join(on_disk[fn])))
    ok = fetch_ok(len(exp), present, names_equal, sha_equal, held, device_ok)
    mutants_held = True
    for label, over in FETCH_MUTANTS:
        base = dict(expected_n=len(exp), present_n=present, names_equal=names_equal, sha_equal=sha_equal,
                    held=held, device_ok=device_ok)
        base.update(over)
        m_ok = fetch_ok(**base)
        mutants_held = mutants_held and not m_ok
        print("BATCH-FETCH-MUTANT case=%s ok=%s expected=False held=%s" % (label, m_ok, not m_ok))
    ok = ok and mutants_held
    print("BATCH-FETCH wheels=%d expected=%d names_equal=%s sha_equal=%s held=%d device=%s ok=%s"
          % (present, EXPECTED, names_equal, sha_equal, held, ascii_text(box), ok))
    return ok


# ------------------------------------------------------------------------------------------------------------ --check

def check_ok(wheels, ran_each, check8, released) -> bool:
    if wheels != EXPECTED or ran_each != CHECKS_TOTAL:
        return False
    return (check8, released) in (("AWAITING", False), ("SIGNED", True))


CHECKS_TOTAL = 7
CHECK_MUTANTS = (
    ("signed_not_released", (EXPECTED, CHECKS_TOTAL, "SIGNED", False)),
    ("awaiting_released", (EXPECTED, CHECKS_TOTAL, "AWAITING", True)),
    ("seventeen_minus_one", (EXPECTED - 1, CHECKS_TOTAL, "AWAITING", False)),
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
        print("BATCH-CHECK-FAIL %s check %d %s" % (fn, n, ascii_text(summary)))
    ran_each = min(ran_counts) if ran_counts else 0
    check8 = states.pop() if len(states) == 1 else "OTHER"
    on_disk = files_on_disk()
    released = any("release" in places for places in on_disk.values())
    ok = check_ok(len(present), ran_each, check8, released)
    mutants_held = True
    for label, args in CHECK_MUTANTS:
        m_ok = check_ok(*args)
        mutants_held = mutants_held and not m_ok
        print("BATCH-CHECK-MUTANT case=%s ok=%s expected=False held=%s" % (label, m_ok, not m_ok))
    ok = ok and mutants_held
    print("BATCH-CHECK wheels=%d expected=%d checks_run_each=%d failed_total=%d not_applicable_total=%d "
          "check8=%s released=%s ok=%s"
          % (len(present), EXPECTED, ran_each, len(failed), na_total, check8, released, ok))
    return ok


# -------------------------------------------------------------------------------------------------------- --requires

def cmd_requires() -> bool:
    kw = load_kit()
    target = kw.parse_target("cp312", "linux_x86_64")
    exp = expected_table()
    closure = read_json(REPO_ROOT / CLOSURE_REL) or {}
    host7 = {kw.norm(m["name"]) for m in closure.get("members", []) if m.get("host_class") == "HOST-SATISFIED"}
    host_doc = read_json(REPO_ROOT / HOST_PYDEPS_REL) or {}
    host_ver = {kw.norm(k): v for k, v in (host_doc.get("dists") or {}).items()}
    chosen = {kw.norm(e["name"]): e["version"] for e in exp.values()}
    on_disk = files_on_disk()
    read_n = 0
    new_deps = 0
    mismatches = 0
    conflicts = 0
    unparsed = 0
    multi_line = "NOT-HELD"
    for fn, e in sorted(exp.items()):
        if fn not in on_disk:
            continue
        path = folder_of(on_disk[fn][0]) / fn
        with zipfile.ZipFile(path) as zf:
            info = kw.read_wheel_zip(zf)
        if info is None:
            unparsed += 1
            print("BATCH-REQUIRES-STOP unreadable-wheel %s" % fn)
            continue
        read_n += 1
        reqs = info["requires"]
        if e["name"] == "multitasking":
            multi_line = " | ".join(ascii_text(r) for r in reqs) if reqs else "NONE"
        for raw in reqs:
            p = kw.parse_requirement(raw, target)
            if not p.get("ok"):
                unparsed += 1
                print("BATCH-REQUIRES-STOP unparsed %s requirement=%s" % (fn, ascii_text(raw)))
                continue
            marker = p.get("marker") or ""
            if "extra" in marker or not p["applicable"]:
                continue
            n = kw.norm(p["name"])
            spec = p["specifier"]
            if n in chosen:
                if kw.satisfies(spec, chosen[n]) is not True:
                    mismatches += 1
                    print("BATCH-REQUIRES-STOP specifier-mismatch %s requirement=%s chosen=%s"
                          % (fn, ascii_text(raw), chosen[n]))
            elif n in host7:
                hv = host_ver.get(n)
                if hv is None or kw.satisfies(spec, hv) is not True:
                    conflicts += 1
                    print("BATCH-REQUIRES-STOP host-conflict %s requirement=%s host=%s" % (fn, ascii_text(raw), hv))
            else:
                new_deps += 1
                print("BATCH-REQUIRES-STOP new-dependency %s requirement=%s" % (fn, ascii_text(raw)))
    ok = (read_n == EXPECTED and new_deps == 0 and mismatches == 0 and conflicts == 0 and unparsed == 0
          and len(host7) == HOST_SATISFIED_EXPECTED)
    print("BATCH-REQUIRES wheels=%d expected=%d new_deps=%d specifier_mismatches=%d host_conflicts=%d "
          "multitasking_requires=%s ok=%s" % (read_n, EXPECTED, new_deps, mismatches, conflicts, multi_line, ok))
    return ok


# ------------------------------------------------------------------------------------------------------- --release

DELIVERY_SUFFIX = ".delivery.txt"
PACK_EXPECTED_FILES = EXPECTED * 3 + 1   # per wheel: wheel, .check.json, .delivery.txt; plus MANIFEST.json
VERIFY_WANT = "wheels=17 verified=17 checked=17 stray=0 ok=True"


def pack_dir() -> pathlib.Path:
    return pathlib.Path(os.path.expanduser("~")) / "tdrop" / "out" / BATCH


def cmd_release() -> bool:
    exp = expected_table()
    rel = release_dir()
    rel_names = set(p.name for p in rel.iterdir() if p.is_file()) if rel.is_dir() else set()
    delivery = set(n for n in rel_names if n.endswith(DELIVERY_SUFFIX))
    wheels_on_disk = rel_names - delivery
    names_equal = (set(exp) == wheels_on_disk and delivery == set(fn + DELIVERY_SUFFIX for fn in exp))
    hold = holding_dir()
    held_left = [fn for fn in exp if (hold / fn).exists()]
    sha_equal = True
    check8_ok = True
    records_checked = True
    released = 0
    for fn, e in sorted(exp.items()):
        frec = read_json(records_dir() / (fn + ".fetch.json")) or {}
        crec = read_json(records_dir() / (fn + ".check.json")) or {}
        by_n = {c.get("n"): c for c in crec.get("checks", []) if isinstance(c, dict)}
        c8 = by_n.get(8) or {}
        c8_ev = c8.get("evidence") or {}
        if not (c8.get("verdict") == "passed" and c8_ev.get("path") == CHECK8_SIG_REL and c8_ev.get("signer")):
            check8_ok = False
            print("BATCH-RELEASE-FAIL %s check 8 verdict=%s path=%s" % (fn, c8.get("verdict"), c8_ev.get("path")))
        if crec.get("verdict") != "checked":
            records_checked = False
        if fn in wheels_on_disk:
            released += 1
            got = sha256_of(rel / fn)
            if got != e["sha256"] or got != frec.get("held_sha256") or got != crec.get("held_sha256"):
                sha_equal = False
                print("BATCH-RELEASE-FAIL %s sha256 differs from the index value or its records" % fn)
    check8 = "SIGNED" if (check8_ok and records_checked and (REPO_ROOT / CHECK8_SIG_REL).is_file()) else "OTHER"
    ok = (released == EXPECTED and names_equal and sha_equal and check8 == "SIGNED" and not held_left)
    if held_left:
        print("BATCH-RELEASE-FAIL still in holding: %s" % ", ".join(held_left))
    print("BATCH-RELEASE released=%d check8=%s names_equal=%s sha_equal=%s ok=%s"
          % (released, check8, names_equal, sha_equal, ok))
    return ok


# ---------------------------------------------------------------------------------------------------------- --pack

def cmd_pack() -> bool:
    exp = expected_table()
    pdir = pack_dir()
    files = sorted(p for p in pdir.iterdir() if p.is_file()) if pdir.is_dir() else []
    n = len(files)
    man = read_json(pdir / "MANIFEST.json") if pdir.is_dir() else None
    man = man if isinstance(man, dict) else {}
    entries = [e for e in man.get("files", []) if isinstance(e, dict)]
    man_names = set(e.get("name") for e in entries)
    man_ok = (man.get("schema") == "intake-manifest/1" and man.get("batch") == BATCH and man_names == set(exp)
              and all((pdir / e["name"]).is_file() and sha256_of(pdir / e["name"]) == e.get("sha256") for e in entries))
    if pdir.is_dir() and (pdir / "MANIFEST.json").is_file():
        vline = "NONE"
        env = dict(os.environ, AGENTBUS_DEVICE="laptop")
        proc = subprocess.run([sys.executable, str(REPO_ROOT / "org" / "devices" / "intake" / "intake_receive.py"),
                               "verify", "--from", str(pdir)],
                              capture_output=True, text=True, encoding="utf-8", errors="replace", env=env, timeout=200)
        lines = [ln for ln in proc.stdout.splitlines() if ln.strip()]
        if lines:
            vline = lines[-1]
    else:
        vline = "NO-PACK"
    verify_ok = vline.startswith("INTAKE-VERIFY") and VERIFY_WANT in vline
    ok = n == PACK_EXPECTED_FILES and man_ok and verify_ok
    print("BATCH-PACK files=%d manifest_ok=%s verify=%s ok=%s" % (n, man_ok, ascii_text(vline), ok))
    return ok


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--fetch", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--requires", action="store_true")
    ap.add_argument("--release", action="store_true")
    ap.add_argument("--pack", action="store_true")
    a = ap.parse_args()
    flags = [a.fetch, a.check, a.requires]
    if not any(flags) and not (a.release or a.pack):
        flags = [True, True, True]
    results = []
    if flags[0]:
        results.append(cmd_fetch())
    if flags[1]:
        results.append(cmd_check())
    if flags[2]:
        results.append(cmd_requires())
    if a.release:
        results.append(cmd_release())
    if a.pack:
        results.append(cmd_pack())
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
