#!/usr/bin/env python3
"""intake_receive.py -- the RECEIVING machine's tool for a delivered pack (TO NFRA_CTLPLN.TO-CT-e-4, C-INTAKE clause 5).

Standard library only; written for Python 3.12 and 3.14. Makes NO network request and offers NO flag that adds an index.

A PACK is a folder holding, for each wheel, <file name>, <file name>.check.json and <file name>.delivery.txt, plus one
MANIFEST.json listing every file in the folder except itself (name, sha256, bytes). MANIFEST.json is either that bare list
or an object with a "files" key holding that list. receipts/ inside the pack is this tool's to create.

Verbs:
  verify  --from <pack>                       read-only; LAST line INTAKE-VERIFY ...
  prove   --from <pack> --scratch <new dir>   verify, then install each wheel with no index into its own scratch target,
                                              import it, write one receipt per wheel into <pack>/receipts/; LAST line INTAKE-PROVE ...
  install --from <pack> [--dry-run]           the real (--user) install, refused without good receipts; LAST line INTAKE-INSTALL ...
  selftest-unchecked                          synthetic pack with one "not_checked" wheel; proves it is refused

The device name comes from the environment variable AGENTBUS_DEVICE and from nothing else.
"""
import argparse
import base64
import csv
import hashlib
import io
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from datetime import datetime, timezone

MANIFEST_NAME = "MANIFEST.json"
RECEIPTS_DIR = "receipts"
CHECK_SUFFIX = ".check.json"
IMPORT_TIMEOUT_S = 60
PIP_TIMEOUT_S = 600
MODULE_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*(\.[A-Za-z_][A-Za-z0-9_]*)*$")
WHEEL_RE = re.compile(r"^[A-Za-z0-9_.+-]+\.whl$")
DEVICE_RE = re.compile(r"^[A-Za-z0-9_.-]+$")
MISSING_RE = re.compile(r"ModuleNotFoundError: No module named '([^']+)'")
IMPORT_CODE = (
    "import sys, importlib; sys.path.insert(0, sys.argv[1]); importlib.import_module(sys.argv[2])"
)
ACCEPTABLE_INSTALL_OUTCOMES = ("installed_imported", "installed_import_failed")

# every pip command line this process has built and run (the test reads it)
COMMANDS_RUN = []


def now_utc():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def ascii_line(text, limit=300):
    text = (text or "").strip()
    return text.encode("ascii", "backslashreplace").decode("ascii")[:limit]


def stem_of(wheel_name):
    return wheel_name[: -len(".whl")] if wheel_name.endswith(".whl") else wheel_name


# ---------------------------------------------------------------- wheel inspection

def wheel_top_level_modules(wheel_path):
    """Top-level importable names: top_level.txt if present, else derived from RECORD. [] means no_module."""
    try:
        with zipfile.ZipFile(wheel_path) as zf:
            names = zf.namelist()
            tl = [n for n in names if n.count("/") == 1 and n.endswith(".dist-info/top_level.txt")]
            mods = []
            if tl:
                text = zf.read(tl[0]).decode("utf-8", "replace")
                for line in text.splitlines():
                    line = line.strip().replace("/", ".")
                    if line:
                        mods.append(line)
            else:
                rec = [n for n in names if n.count("/") == 1 and n.endswith(".dist-info/RECORD")]
                if rec:
                    text = zf.read(rec[0]).decode("utf-8", "replace")
                    paths = [row[0] for row in csv.reader(io.StringIO(text)) if row]
                else:
                    paths = names
                for p in paths:
                    first = p.split("/")[0]
                    if first.endswith(".dist-info") or first.endswith(".data") or first == "__pycache__":
                        continue
                    if "/" in p:
                        mods.append(first)
                    elif p.endswith(".py"):
                        mods.append(p[:-3])
                    elif p.endswith((".so", ".pyd")):
                        mods.append(p.split(".")[0])
    except (zipfile.BadZipFile, OSError, KeyError):
        return []
    out = []
    for m in mods:
        if MODULE_RE.match(m) and m not in out:
            out.append(m)
    return out


# ---------------------------------------------------------------- verify

def _read_manifest(pack):
    """Return (entries, defect). entries is a list of dicts; defect is None or a string."""
    mpath = os.path.join(pack, MANIFEST_NAME)
    if not os.path.isfile(mpath):
        return None, "MANIFEST.json absent"
    try:
        with open(mpath, "rb") as fh:
            data = json.loads(fh.read().decode("utf-8"))
    except (OSError, ValueError) as exc:
        return None, "MANIFEST.json unreadable (%s)" % type(exc).__name__
    if isinstance(data, dict) and isinstance(data.get("files"), list):
        data = data["files"]
    if not isinstance(data, list):
        return None, "MANIFEST.json is neither a list nor an object with a files list"
    for e in data:
        if not (isinstance(e, dict) and isinstance(e.get("name"), str) and isinstance(e.get("sha256"), str)
                and isinstance(e.get("bytes"), int) and not isinstance(e.get("bytes"), bool)):
            return None, "MANIFEST.json entry lacks name/sha256/bytes"
    return data, None


def _record_problems(rec, wheel_name, wheel_sha):
    """The reasons a CHECK record does not clear its wheel (empty list = cleared)."""
    if not isinstance(rec, dict):
        return ["check record is not a JSON object"]
    out = []
    if rec.get("file_name") != wheel_name:
        out.append("record file_name %r != wheel name" % (rec.get("file_name"),))
    if wheel_sha is None or rec.get("held_sha256") != wheel_sha:
        out.append("record held_sha256 != wheel sha256")
    if rec.get("verdict") != "checked":
        out.append("record verdict is %r, not 'checked'" % (rec.get("verdict"),))
    checks = rec.get("checks")
    if not isinstance(checks, list) or len(checks) != 8:
        out.append("record checks is not a list of exactly eight")
    else:
        ns = [c.get("n") if isinstance(c, dict) else None for c in checks]
        if ns != [1, 2, 3, 4, 5, 6, 7, 8]:
            out.append("record checks are not numbered 1 to 8 in order")
        elif checks[7].get("verdict") != "passed":
            out.append("record check 8 reads %r, not 'passed'" % (checks[7].get("verdict"),))
    return out


def verify_pack(pack):
    """Read-only verification. Returns a dict (see keys below); never raises on a bad pack."""
    res = {"pack": os.path.basename(os.path.normpath(pack)), "wheels": [], "stray": [], "pack_defects": [],
           "verified": 0, "checked": 0, "ok": False}
    if not os.path.isdir(pack):
        res["pack_defects"].append("pack dir does not exist")
        return res
    entries, defect = _read_manifest(pack)
    if defect:
        res["pack_defects"].append(defect)
        entries = []
    listed = {}
    for e in entries:
        nm = e["name"]
        if nm in listed:
            res["pack_defects"].append("manifest lists %s twice" % nm)
        listed[nm] = e
    present = sorted(n for n in os.listdir(pack) if n != MANIFEST_NAME and n != RECEIPTS_DIR)
    for n in present:
        if os.path.isdir(os.path.join(pack, n)) or n not in listed:
            res["stray"].append(n)
    wheel_names = sorted(n for n in present if n.endswith(".whl") and os.path.isfile(os.path.join(pack, n)))
    # per-file manifest result: name -> None (good) or reason
    file_bad = {}
    for nm, e in listed.items():
        path = os.path.join(pack, nm)
        if os.path.basename(nm) != nm or nm in ("", ".", ".."):
            file_bad[nm] = "manifest name is not a plain file name"
        elif not os.path.isfile(path):
            file_bad[nm] = "listed in manifest but absent"
        elif os.path.getsize(path) != e["bytes"]:
            file_bad[nm] = "size differs from manifest"
        elif sha256_file(path) != e["sha256"].lower():
            file_bad[nm] = "sha256 differs from manifest"
    wheel_related = set()
    for w in wheel_names:
        wheel_related.update((w, w + CHECK_SUFFIX))
    for nm, why in sorted(file_bad.items()):
        if nm not in wheel_related:
            res["pack_defects"].append("%s: %s" % (nm, why))
    for w in wheel_names:
        wpath = os.path.join(pack, w)
        info = {"name": w, "path": wpath, "file_ok": False, "record_ok": False, "reasons": [],
                "check_record_sha256": None, "wheel_sha256": None, "modules": []}
        reasons = info["reasons"]
        if not WHEEL_RE.match(w):
            reasons.append("wheel file name has unexpected characters")
        if w not in listed:
            reasons.append("wheel not listed in manifest")
        elif w in file_bad:
            reasons.append("wheel %s" % file_bad[w])
        else:
            info["file_ok"] = True
        info["wheel_sha256"] = sha256_file(wpath)
        rname = w + CHECK_SUFFIX
        rpath = os.path.join(pack, rname)
        if not os.path.isfile(rpath):
            reasons.append("check record absent")
        else:
            info["check_record_sha256"] = sha256_file(rpath)
            if rname not in listed:
                reasons.append("check record not listed in manifest")
            elif rname in file_bad:
                reasons.append("check record %s" % file_bad[rname])
            try:
                with open(rpath, "rb") as fh:
                    rec = json.loads(fh.read().decode("utf-8"))
            except (OSError, ValueError):
                reasons.append("check record unreadable")
                rec = None
            if rec is not None:
                probs = _record_problems(rec, w, info["wheel_sha256"])
                reasons.extend(probs)
                if not probs and rname in listed and rname not in file_bad:
                    info["record_ok"] = True
        if info["file_ok"] and not reasons:
            info["modules"] = wheel_top_level_modules(wpath)
        res["wheels"].append(info)
    res["verified"] = sum(1 for i in res["wheels"] if i["file_ok"])
    res["checked"] = sum(1 for i in res["wheels"] if i["record_ok"])
    n = len(res["wheels"])
    res["ok"] = bool(n > 0 and not res["pack_defects"] and not res["stray"]
                     and res["verified"] == n and res["checked"] == n
                     and all(not i["reasons"] for i in res["wheels"]))
    return res


def verify_last_line(res):
    return "INTAKE-VERIFY pack=%s wheels=%d verified=%d checked=%d stray=%d ok=%s" % (
        res["pack"], len(res["wheels"]), res["verified"], res["checked"], len(res["stray"]), res["ok"])


def print_verify_detail(res):
    for d in res["pack_defects"]:
        print("PACK-DEFECT: %s" % ascii_line(d))
    for s in res["stray"]:
        print("STRAY: %s" % ascii_line(s))
    for i in res["wheels"]:
        if i["reasons"]:
            print("REFUSED: %s: %s" % (ascii_line(i["name"]), "; ".join(ascii_line(r) for r in i["reasons"])))
        else:
            print("OK: %s" % ascii_line(i["name"]))


# ---------------------------------------------------------------- pip and import plumbing

def build_pip_command(wheel_path, target=None, user=False):
    """The one pip command line this tool ever builds: a list, no shell, never an index, never a resolver."""
    cmd = [sys.executable, "-m", "pip", "install", "--no-index", "--no-deps"]
    if user:
        cmd.append("--user")
    else:
        cmd += ["--target", target]
    cmd.append(wheel_path)
    return cmd


def build_child_env():
    """Environment for the pip child: no inherited PIP_* setting, no user config, no pip self-version check (a network call)."""
    env = {k: v for k, v in os.environ.items() if not k.upper().startswith("PIP_")}
    env["PIP_NO_INDEX"] = "1"
    env["PIP_DISABLE_PIP_VERSION_CHECK"] = "1"
    env["PIP_CONFIG_FILE"] = os.devnull
    return env


def run_pip(cmd):
    COMMANDS_RUN.append(list(cmd))
    try:
        cp = subprocess.run(cmd, env=build_child_env(), capture_output=True, text=True, encoding="utf-8",
                            errors="replace", timeout=PIP_TIMEOUT_S, stdin=subprocess.DEVNULL)
    except subprocess.TimeoutExpired:
        return 124, "pip timed out after %ds" % PIP_TIMEOUT_S
    except OSError as exc:
        return 127, "pip could not start (%s)" % type(exc).__name__
    last = ""
    for line in (cp.stderr + "\n" + cp.stdout).splitlines():
        if line.strip():
            last = line
    return cp.returncode, ascii_line(last)


def classify_import(rc, stderr, own_modules):
    """Returns (class, missing_name, first_error_line). class: imported | import_missing_dep | failed."""
    if rc == 0:
        return "imported", None, ""
    lines = [ln for ln in (stderr or "").splitlines() if ln.strip()]
    err = ascii_line(lines[-1]) if lines else "exit code %s with no stderr" % rc
    m = MISSING_RE.search(stderr or "")
    if m:
        missing = m.group(1)
        top = missing.split(".")[0]
        if top not in own_modules and missing not in own_modules:
            return "import_missing_dep", missing, err
    return "failed", None, err


def run_import(target, module, own_modules):
    cmd = [sys.executable, "-I", "-c", IMPORT_CODE, target, module]
    try:
        cp = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace",
                            timeout=IMPORT_TIMEOUT_S, stdin=subprocess.DEVNULL)
    except subprocess.TimeoutExpired:
        return {"module": module, "rc": 124, "first_error_line": "import timed out after %ds" % IMPORT_TIMEOUT_S,
                "class": "failed"}
    cls, missing, err = classify_import(cp.returncode, cp.stderr, own_modules)
    row = {"module": module, "rc": cp.returncode, "first_error_line": err, "class": cls}
    if missing:
        row["missing_dep"] = missing
    return row


# ---------------------------------------------------------------- receipts

def device_name():
    """Device from AGENTBUS_DEVICE only. Returns (name, problem)."""
    raw = os.environ.get("AGENTBUS_DEVICE")
    if raw is None or not raw.strip():
        return None, "AGENTBUS_DEVICE is not set; refusing to write a receipt without a device name"
    if not DEVICE_RE.match(raw.strip()):
        return None, "AGENTBUS_DEVICE has characters not allowed in a file name"
    return raw.strip(), None


def receipt_path(pack, wheel_name, device):
    return os.path.join(pack, RECEIPTS_DIR, "%s.receipt.%s.json" % (wheel_name, device))


def write_receipt(pack, info, device, outcome, reason, command=None, rc=None, imports=None):
    rec = {
        "schema": "intake-receipt/1",
        "device": device,
        "python": platform.python_version(),
        "file_name": info["name"],
        "received_sha256": info.get("wheel_sha256"),
        "check_record_sha256": info.get("check_record_sha256"),
        "install": {"command": command if command is not None else [], "rc": rc},
        "imports": imports or [],
        "outcome": outcome,
        "reason": reason,
        "at": now_utc(),
    }
    os.makedirs(os.path.join(pack, RECEIPTS_DIR), exist_ok=True)
    with open(receipt_path(pack, info["name"], device), "w", encoding="ascii", newline="\n") as fh:
        json.dump(rec, fh, indent=2, ensure_ascii=True)
        fh.write("\n")
    return rec


# ---------------------------------------------------------------- prove

def prove_last_line(device, n, installed, imported, missing, failed, refused, ok):
    return ("INTAKE-PROVE device=%s python=%s wheels=%d installed=%d imported=%d import_missing_dep=%d "
            "failed=%d refused=%d ok=%s" % (device, platform.python_version(), n, installed, imported, missing,
                                            failed, refused, ok))


def prove_pack(pack, scratch, device_override=None):
    """Returns (exit_code, summary dict). Prints detail lines; the caller prints the LAST line from the summary."""
    device, problem = (device_override, None) if device_override else device_name()
    summ = {"device": device or "UNSET", "n": 0, "installed": 0, "imported": 0, "missing": 0, "failed": 0,
            "refused": 0, "import_failed": 0, "no_module": 0, "ok": False}
    if problem:
        print("REFUSED: %s" % problem)
        return 2, summ
    if os.path.exists(scratch) and (not os.path.isdir(scratch) or os.listdir(scratch)):
        print("REFUSED: --scratch must be a new or empty directory")
        return 2, summ
    res = verify_pack(pack)
    print_verify_detail(res)
    print(verify_last_line(res))
    summ["n"] = len(res["wheels"])
    pack_level = bool(res["pack_defects"] or res["stray"])
    if not res["wheels"]:
        print("REFUSED: no wheel to prove")
        return 1, summ
    os.makedirs(scratch, exist_ok=True)
    for info in res["wheels"]:
        name = info["name"]
        if pack_level or info["reasons"]:
            why = "pack failed verify: %s" % "; ".join(res["pack_defects"] + ["stray " + s for s in res["stray"]]) \
                if pack_level and not info["reasons"] else "; ".join(info["reasons"])
            write_receipt(pack, info, device, "refused", ascii_line(why, 600))
            summ["refused"] += 1
            continue
        target = os.path.join(scratch, stem_of(name))
        cmd = build_pip_command(info["path"], target=target)
        rc, last = run_pip(cmd)
        if rc != 0:
            write_receipt(pack, info, device, "install_failed", "pip rc=%d: %s" % (rc, last), cmd, rc)
            summ["failed"] += 1
            continue
        summ["installed"] += 1
        mods = info["modules"]
        imports = [run_import(target, m, mods) for m in mods]
        bad = [r for r in imports if r["class"] != "imported"]
        miss = [r for r in bad if r["class"] == "import_missing_dep"]
        hard = [r for r in bad if r["class"] == "failed"]
        if not mods:
            outcome, reason = "installed_imported", "no_module: no importable top-level module"
            summ["no_module"] += 1
        elif not bad:
            outcome, reason = "installed_imported", "all %d top-level module(s) imported" % len(mods)
            summ["imported"] += 1
        elif not hard:
            outcome = "installed_import_failed"
            reason = "import_missing_dep: " + ",".join(sorted({r["missing_dep"] for r in miss}))
            summ["missing"] += 1
        else:
            outcome = "installed_import_failed"
            reason = "import_failed: " + ",".join(r["module"] for r in hard)
            summ["import_failed"] += 1
        write_receipt(pack, info, device, outcome, reason, cmd, rc, imports)
        print("PROVED: %s %s (%s)" % (ascii_line(name), outcome, ascii_line(reason)))
    summ["ok"] = summ["refused"] == 0 and summ["failed"] == 0
    print("INTAKE-PROVE-DETAIL import_failed=%d no_module=%d" % (summ["import_failed"], summ["no_module"]))
    return (0 if summ["ok"] else 1), summ


def print_prove_last(summ):
    print(prove_last_line(summ["device"], summ["n"], summ["installed"], summ["imported"], summ["missing"],
                          summ["failed"], summ["refused"], summ["ok"]))


# ---------------------------------------------------------------- install

def receipt_gate(pack, device, res):
    """Per wheel: (name, ok, reason). A wheel clears only on a receipt from this device that matches its bytes."""
    out = []
    for info in res["wheels"]:
        name = info["name"]
        rp = receipt_path(pack, name, device)
        if info["reasons"]:
            out.append((name, False, "wheel fails verify"))
            continue
        if not os.path.isfile(rp):
            out.append((name, False, "no receipt for device %s (run prove first)" % device))
            continue
        try:
            with open(rp, "rb") as fh:
                rec = json.loads(fh.read().decode("utf-8"))
        except (OSError, ValueError):
            out.append((name, False, "receipt unreadable"))
            continue
        if not isinstance(rec, dict) or rec.get("received_sha256") != info["wheel_sha256"]:
            out.append((name, False, "receipt does not match the wheel's bytes"))
            continue
        if rec.get("check_record_sha256") != info["check_record_sha256"]:
            out.append((name, False, "receipt does not match the check record"))
            continue
        outcome = rec.get("outcome")
        if outcome == "installed_imported":
            out.append((name, True, "installed_imported"))
        elif outcome == "installed_import_failed":
            bad = [r for r in rec.get("imports", []) if isinstance(r, dict) and r.get("rc") != 0]
            if bad and all(r.get("class") == "import_missing_dep" for r in bad):
                out.append((name, True, "installed_import_failed with import_missing_dep only"))
            else:
                out.append((name, False, "receipt records an import failure that is not import_missing_dep"))
        else:
            out.append((name, False, "receipt outcome is %r" % (outcome,)))
    return out


def install_pack(pack, dry_run):
    device, problem = device_name()
    summ = {"device": device or "UNSET", "n": 0, "installed": 0, "refused": 0, "ok": False}
    if problem:
        print("REFUSED: %s" % problem)
        return 2, summ
    res = verify_pack(pack)
    print_verify_detail(res)
    print(verify_last_line(res))
    summ["n"] = len(res["wheels"])
    if not res["ok"]:
        print("REFUSED: pack does not verify; nothing installed")
        summ["refused"] = summ["n"]
        return 1, summ
    gate = receipt_gate(pack, device, res)
    for name, ok, why in gate:
        print("%s: %s: %s" % ("RECEIPT-OK" if ok else "REFUSED", ascii_line(name), ascii_line(why)))
    if not all(ok for _, ok, _ in gate):
        summ["refused"] = sum(1 for _, ok, _ in gate if not ok)
        print("REFUSED: install needs a good receipt for every wheel; nothing installed")
        return 1, summ
    for info in res["wheels"]:
        cmd = build_pip_command(info["path"], user=True)
        if dry_run:
            print("DRY-RUN: " + json.dumps(cmd))
            summ["installed"] += 0
            continue
        rc, last = run_pip(cmd)
        if rc != 0:
            print("FAILED: %s pip rc=%d: %s" % (ascii_line(info["name"]), rc, last))
            summ["refused"] += 1
            break
        summ["installed"] += 1
    summ["ok"] = summ["refused"] == 0
    summ["dry_run"] = dry_run
    return (0 if summ["ok"] else 1), summ


# ---------------------------------------------------------------- synthetic wheels (selftest and the test file)

def _record_hash(data):
    return "sha256=" + base64.urlsafe_b64encode(hashlib.sha256(data).digest()).rstrip(b"=").decode("ascii")


def build_synthetic_wheel(out_dir, dist, version, modules, top_level=True):
    """Build a py3-none-any wheel. modules: {import name: source text}; a name is a package dir with __init__.py.
    Returns the wheel path."""
    name = "%s-%s-py3-none-any.whl" % (dist, version)
    di = "%s-%s.dist-info" % (dist, version)
    files = []
    for mod, src in sorted(modules.items()):
        files.append(("%s/__init__.py" % mod, src.encode("ascii")))
    files.append((di + "/METADATA", ("Metadata-Version: 2.1\nName: %s\nVersion: %s\n" % (dist, version)).encode("ascii")))
    files.append((di + "/WHEEL", b"Wheel-Version: 1.0\nGenerator: intake-synthetic\nRoot-Is-Purelib: true\nTag: py3-none-any\n"))
    if top_level and modules:
        files.append((di + "/top_level.txt", ("\n".join(sorted(modules)) + "\n").encode("ascii")))
    rows = [[p, _record_hash(d), str(len(d))] for p, d in files]
    rows.append([di + "/RECORD", "", ""])
    buf = io.StringIO()
    csv.writer(buf, lineterminator="\n").writerows(rows)
    files.append((di + "/RECORD", buf.getvalue().encode("ascii")))
    path = os.path.join(out_dir, name)
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zf:
        for p, d in files:
            zf.writestr(zipfile.ZipInfo(p, date_time=(2026, 1, 1, 0, 0, 0)), d, zipfile.ZIP_DEFLATED)
    return path


def write_check_record(pack, wheel_name, verdict="checked", **override):
    sha = sha256_file(os.path.join(pack, wheel_name))
    ok = verdict == "checked"
    checks = [{"n": n, "name": "check%d" % n, "verdict": "passed" if (ok or n < 8) else "unsigned",
               "evidence": "synthetic", "rules_out": "synthetic", "leaves": "synthetic"} for n in range(1, 9)]
    rec = {"schema": "intake-check/1", "batch": "synthetic", "file_name": wheel_name, "held_sha256": sha,
           "checks": checks, "verdict": verdict, "checked_by": "synthetic", "at": now_utc()}
    rec.update(override)
    with open(os.path.join(pack, wheel_name + CHECK_SUFFIX), "w", encoding="ascii", newline="\n") as fh:
        json.dump(rec, fh, indent=2)
        fh.write("\n")
    with open(os.path.join(pack, wheel_name + ".delivery.txt"), "w", encoding="ascii", newline="\n") as fh:
        fh.write("synthetic delivery note\n")


def write_manifest(pack, shape="list"):
    entries = []
    for n in sorted(os.listdir(pack)):
        p = os.path.join(pack, n)
        if n in (MANIFEST_NAME, RECEIPTS_DIR) or not os.path.isfile(p):
            continue
        entries.append({"name": n, "sha256": sha256_file(p), "bytes": os.path.getsize(p)})
    data = entries if shape == "list" else {"files": entries}
    with open(os.path.join(pack, MANIFEST_NAME), "w", encoding="ascii", newline="\n") as fh:
        json.dump(data, fh, indent=2)
        fh.write("\n")


def selftest_unchecked():
    tmp = tempfile.mkdtemp(prefix="intake-selftest-")
    try:
        pack = os.path.join(tmp, "pack")
        os.makedirs(pack)
        wheel = os.path.basename(build_synthetic_wheel(pack, "selftestpkg", "1.0", {"selftestpkg": "VALUE = 1\n"}))
        write_check_record(pack, wheel, verdict="not_checked")
        write_manifest(pack)
        device = os.environ.get("AGENTBUS_DEVICE", "").strip() or "selftest"
        scratch = os.path.join(tmp, "scratch")
        rc, summ = prove_pack(pack, scratch, device_override=device)
        installed_on_disk = os.path.isdir(os.path.join(scratch, stem_of(wheel)))
        if installed_on_disk:
            print("ERROR: scratch target exists for a not_checked wheel")
            summ["installed"] += 1
            summ["ok"] = False
        return summ
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# ---------------------------------------------------------------- CLI

def main(argv=None):
    ap = argparse.ArgumentParser(prog="intake_receive.py", description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="verb", required=True)
    v = sub.add_parser("verify")
    v.add_argument("--from", dest="pack", required=True)
    p = sub.add_parser("prove")
    p.add_argument("--from", dest="pack", required=True)
    p.add_argument("--scratch", required=True)
    i = sub.add_parser("install")
    i.add_argument("--from", dest="pack", required=True)
    i.add_argument("--dry-run", action="store_true", dest="dry_run")
    sub.add_parser("selftest-unchecked")
    args = ap.parse_args(argv)
    if args.verb == "verify":
        res = verify_pack(args.pack)
        print_verify_detail(res)
        print(verify_last_line(res))
        return 0 if res["ok"] else 1
    if args.verb == "prove":
        rc, summ = prove_pack(args.pack, args.scratch)
        print_prove_last(summ)
        return rc
    if args.verb == "install":
        rc, summ = install_pack(args.pack, args.dry_run)
        print("INTAKE-INSTALL device=%s python=%s wheels=%d installed=%d refused=%d dry_run=%s ok=%s" % (
            summ["device"], platform.python_version(), summ["n"], summ["installed"], summ["refused"],
            bool(args.dry_run), summ["ok"]))
        return rc
    summ = selftest_unchecked()
    print_prove_last(summ)
    return 0 if (summ["installed"] == 0 and summ["refused"] == 1) else 1


if __name__ == "__main__":
    sys.exit(main())
