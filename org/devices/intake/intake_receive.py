#!/usr/bin/env python3
"""intake_receive.py -- the RECEIVING machine's tool for a delivered pack (TO NFRA_CTLPLN.TO-CT-e-4, C-INTAKE clause 5).

Standard library only; written for Python 3.12 and 3.14. Makes NO network request and offers NO flag that adds an index.

A PACK is a folder holding, for each wheel, <file name>, <file name>.check.json and <file name>.delivery.txt, plus one
MANIFEST.json listing every file in the folder except itself. PRIMARY shape (what intake_check.py pack writes): an object
{schema, batch, created, files[]} with ONE entry per wheel: name, sha256, size, check_record, check_record_sha256, delivery,
delivery_sha256; the wheel and both companions are verified by hash and all three count as listed. Also accepted: one entry
per FILE (name, sha256, bytes) in an object with a "files" key or as a bare list; "bytes" and "size" are synonyms.
receipts/ inside the pack is this tool's to create.

Verbs:
  verify  --from <pack>                       read-only; one INTAKE-VERIFY-WAIVED line per waived check; LAST line INTAKE-VERIFY ...
          (a record reads 'checked' or 'released-with-waiver'; the waiver is re-derived from the record's own checks)
  verify  --from <pack> --ecosystem npm --lockfile <bun.lock>
          the npm limb (CT-cc-1): each .tgz is re-read against its check record AND its lockfile entry (sha512); the LAST
          line reads INTAKE-VERIFY pack=... tarballs=... ; the pack is verified and stops there (no placement verb here)
  prove   --from <pack> --scratch <new dir>   verify, then install each wheel with no index into its own scratch target,
                                              import it, write one receipt per wheel into <pack>/receipts/; LAST line INTAKE-PROVE ...
  install --from <pack> --python <exe> | --target <new dir> | --user [--dry-run]
                                              the real install, refused without good receipts and without EXACTLY ONE target.
                                              --python <exe>: pip in that interpreter's own site, no --user (a fresh venv's
                                              python); --python equal to this interpreter is refused unless --user is also given.
                                              --target <new dir>: pip --target into a new or empty folder.
                                              --user: the old user-site install of this interpreter, only when asked for by name.
                                              The old default (a --user install with no target) is gone. Each real install writes
                                              receipts/<wheel>.install.<device>.json with install.target_form and the interpreter;
                                              LAST line INTAKE-INSTALL ...
  install --ecosystem npm --pack <pack> --lockfile <bun.lock> --target <bun cache dir> [--by <serial>] [--receipt-dir <dir>]
                                              the npm limb (CT-cc-2): verifies the pack as 'verify' does, then unpacks each
                                              tarball into <target>/<name>@<version>@@@1 (a scoped name keeps its slash as a
                                              folder), the layout ops/bun_cache_precheck.py reads. Whole-install refusal: nothing
                                              is written when any tarball is not cleared or any destination exists and is not
                                              present. Never runs a script, bun or a package manager. LAST line INTAKE-NPM-INSTALL
  selftest-unchecked                          synthetic pack with one "not_checked" wheel; proves it is refused

The device name comes from the environment variable AGENTBUS_DEVICE and from nothing else.
"""
import argparse
import base64
import csv
import hashlib
import importlib.util
import io
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import zipfile
import zlib
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
# ANSI colour and control sequences: CSI (ESC [ params intermediates final byte) and OSC (ESC ] ... BEL or ESC \)
ANSI_RE = re.compile(r"\x1b\[[0-?]*[ -/]*[@-~]|\x1b\][^\x07\x1b]*(?:\x07|\x1b\\)")
COLOUR_PINS = {"PYTHON_COLORS": "0", "NO_COLOR": "1"}
IMPORT_CODE = (
    "import sys, importlib; sys.path.insert(0, sys.argv[1]); importlib.import_module(sys.argv[2])"
)
ACCEPTABLE_INSTALL_OUTCOMES = ("installed_imported", "installed_import_failed")

# every pip command line this process has built and run (the test reads it)
COMMANDS_RUN = []
# the last pip run in full: command, the inherited PIP_* NAMES removed, rc and pip's full captured text (write_pip_log reads it)
LAST_PIP_RUN = {}
PIP_LOG_CAP = 200000
# the pins build_child_env sets, in the order the log's env_pins= line states them
PIP_ENV_PINS = (("PIP_NO_INDEX", "1"), ("PIP_DISABLE_PIP_VERSION_CHECK", "1"), ("PIP_CONFIG_FILE", os.devnull))


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

def _is_int(v):
    return isinstance(v, int) and not isinstance(v, bool)


def _read_manifest(pack):
    """Return (entries, defect). entries is a list of dicts name/sha256/bytes/owner; defect is None or a string.

    Shapes read: (1) the check tool's pack: an object with files[], ONE entry per wheel carrying name, sha256, size, and the
    companions check_record + check_record_sha256 and delivery + delivery_sha256 (each companion becomes a listed file whose
    owner is the wheel); (2) an object with files[] of one entry per FILE (name, sha256, bytes); (3) a bare list of those.
    `bytes` and `size` are synonyms."""
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
    out = []
    for e in data:
        if not (isinstance(e, dict) and isinstance(e.get("name"), str) and isinstance(e.get("sha256"), str)):
            return None, "MANIFEST.json entry lacks name/sha256/size"
        sizes = [e[k] for k in ("size", "bytes") if k in e]
        if not sizes or not all(_is_int(v) for v in sizes) or len(set(sizes)) != 1:
            return None, "MANIFEST.json entry lacks name/sha256/size"
        out.append({"name": e["name"], "sha256": e["sha256"], "bytes": sizes[0], "owner": None})
        for fkey, hkey in (("check_record", "check_record_sha256"), ("delivery", "delivery_sha256")):
            if fkey not in e and hkey not in e:
                continue
            if not (isinstance(e.get(fkey), str) and isinstance(e.get(hkey), str)):
                return None, "MANIFEST.json entry names a companion without its name and sha256"
            out.append({"name": e[fkey], "sha256": e[hkey], "bytes": None, "owner": e["name"]})
    return out, None


WAIVABLE_CHECKS = (3, 4, 5, 6, 7)


def _derive_waived(checks):
    """A STANDALONE MIRROR of intake_check._derive, for a record that reads 'released-with-waiver' (this tool ships alone to the
    receiving box, so it cannot import intake_check). Returns (verdict, carried): 'released-with-waiver' and the sorted failed
    checks 3..7 that check 8's waiver lines carry, or 'not_checked' and []. The parity arms in
    .tools/tests/test_round27_waiver.py hold the two derivations equal."""
    ev8 = checks[7].get("evidence") or {}
    if checks[7].get("verdict") != "passed" or not isinstance(ev8, dict) or not (ev8.get("signer") and ev8.get("path")) \
            or ev8.get("refused_waivers"):
        return "not_checked", []
    waived = set()
    for w in ev8.get("waivers") or []:
        if isinstance(w, dict) and w.get("check") in WAIVABLE_CHECKS and str(w.get("reason", "")).strip():
            waived.add(w["check"])
    carried = []
    for c in checks[:7]:
        ev = c.get("evidence") or {}
        if c.get("verdict") == "passed":
            continue
        if c.get("verdict") == "not_applicable" and isinstance(ev, dict) and str(ev.get("reason", "")).strip():
            continue
        if c.get("verdict") == "failed" and c["n"] in waived:
            carried.append(c["n"])
            continue
        return "not_checked", []
    if carried:
        return "released-with-waiver", sorted(carried)
    return "not_checked", []


def _waiver_lines(rec):
    """[(check, reason)] for each waived check of a 'released-with-waiver' record; [] for any other record."""
    if rec.get("verdict") != "released-with-waiver":
        return []
    ev8 = rec["checks"][7].get("evidence") or {}
    out = []
    for n in rec.get("waived_checks") or []:
        reason = next((w.get("reason", "") for w in ev8.get("waivers") or []
                       if isinstance(w, dict) and w.get("check") == n), "")
        out.append((n, reason))
    return out


def _record_problems(rec, wheel_name, wheel_sha):
    """The reasons a CHECK record does not clear its wheel (empty list = cleared)."""
    if not isinstance(rec, dict):
        return ["check record is not a JSON object"]
    out = []
    if rec.get("file_name") != wheel_name:
        out.append("record file_name %r != wheel name" % (rec.get("file_name"),))
    if wheel_sha is None or rec.get("held_sha256") != wheel_sha:
        out.append("record held_sha256 != wheel sha256")
    verdict = rec.get("verdict")
    if verdict not in ("checked", "released-with-waiver"):
        out.append("record verdict is %r, not 'checked' or 'released-with-waiver'" % (verdict,))
    checks = rec.get("checks")
    if not isinstance(checks, list) or len(checks) != 8:
        out.append("record checks is not a list of exactly eight")
    else:
        ns = [c.get("n") if isinstance(c, dict) else None for c in checks]
        if ns != [1, 2, 3, 4, 5, 6, 7, 8]:
            out.append("record checks are not numbered 1 to 8 in order")
        elif checks[7].get("verdict") != "passed":
            out.append("record check 8 reads %r, not 'passed'" % (checks[7].get("verdict"),))
        elif verdict == "released-with-waiver":
            derived, carried = _derive_waived(checks)
            if derived != "released-with-waiver":
                out.append("record reads 'released-with-waiver' but its checks re-derive as %r" % (derived,))
            elif list(rec.get("waived_checks") or []) != carried:
                out.append("record waived_checks %r disagree with the re-derivation %r" % (rec.get("waived_checks"), carried))
    return out


NPM_EXT = ".tgz"
NPM_FILE_RE = re.compile(r"^[A-Za-z0-9_.+-]+\.tgz$")


def load_bun_lock(path):
    """STANDALONE MIRROR of intake_check.load_bun_lock (this tool ships alone): the bun text lockfile as a dict with a packages
    object. Trailing commas are removed outside strings, then JSON is read. Parity arms are in test_intake_npm.py."""
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
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
    data = json.loads("".join(out))
    if not isinstance(data, dict) or not isinstance(data.get("packages"), dict):
        raise ValueError("the lockfile has no packages object")
    return data


def lock_integrities(lock, ident):
    """STANDALONE MIRROR of intake_check.lock_integrities: the distinct integrity strings of the entries whose first element is
    ident (name@version); the fourth element is the integrity, None when absent."""
    found = []
    for _key, val in lock["packages"].items():
        if isinstance(val, list) and val and val[0] == ident:
            integ = val[3] if len(val) > 3 and isinstance(val[3], str) else None
            if integ not in found:
                found.append(integ)
    return found


def _sha512_sri(path):
    h = hashlib.sha512()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return "sha512-" + base64.b64encode(h.digest()).decode("ascii")


def _npm_tarball_problems(rec, path, lock):
    """The reasons one npm tarball is not cleared against its record and its lockfile entry (empty = cleared)."""
    checks = rec.get("checks") if isinstance(rec, dict) else None
    if not isinstance(checks, list) or len(checks) < 2 or not all(isinstance(c, dict) for c in checks[:2]):
        return ["check record lacks the npm check 1 and check 2 evidence"]
    ev1 = checks[0].get("evidence") or {}
    ev2 = checks[1].get("evidence") or {}
    ident = ev2.get("ident")
    if not isinstance(ident, str):
        return ["check 2 record names no name@version"]
    if lock is None:
        return ["no lockfile: the tarball cannot be read against its lockfile entry"]
    found = lock_integrities(lock, ident)
    actual = _sha512_sri(path)
    out = []
    try:
        with tarfile.open(path, mode="r:gz") as tf:
            _root, root_reason = npm_package_root([(m.name, m.isdir()) for m in tf.getmembers()])
    except (tarfile.TarError, OSError, EOFError, zlib.error) as exc:
        root_reason = "not a readable gzip tar: %s" % type(exc).__name__
    if root_reason:
        out.append("no package root: %s" % root_reason)
    if ev1.get("computed_sha512") != actual:
        out.append("tarball sha512 differs from the check record's computed_sha512")
    if len(found) != 1 or found[0] is None:
        out.append("lockfile holds %d integrity entr%s for %s" % (len(found), "y" if len(found) == 1 else "ies", ident))
    elif found[0] != actual:
        out.append("tarball sha512 differs from the lockfile's integrity for %s" % ident)
    return out


def verify_pack(pack, ecosystem="pypi", lockfile=None):
    """Read-only verification. Returns a dict (see keys below); never raises on a bad pack. ecosystem npm reads .tgz files and
    re-reads each against its check record and its lockfile entry; pypi (the default) is unchanged."""
    npm = ecosystem == "npm"
    res = {"pack": os.path.basename(os.path.normpath(pack)), "wheels": [], "stray": [], "pack_defects": [],
           "verified": 0, "checked": 0, "ok": False, "ecosystem": "npm" if npm else "pypi"}
    if not os.path.isdir(pack):
        res["pack_defects"].append("pack dir does not exist")
        return res
    lock = None
    if npm:
        if not lockfile:
            res["pack_defects"].append("npm verify needs --lockfile <bun.lock>: a missing lockfile is a refusal, never a skip")
        else:
            try:
                lock = load_bun_lock(lockfile)
            except (OSError, ValueError) as exc:
                res["pack_defects"].append("lockfile unreadable: %s" % type(exc).__name__)
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
    if npm:
        wheel_names = sorted(n for n in present if n.endswith(NPM_EXT) and os.path.isfile(os.path.join(pack, n)))
    else:
        wheel_names = sorted(n for n in present if n.endswith(".whl") and os.path.isfile(os.path.join(pack, n)))
    # per-file manifest result: name -> None (good) or reason
    file_bad = {}
    for nm, e in listed.items():
        path = os.path.join(pack, nm)
        if os.path.basename(nm) != nm or nm in ("", ".", ".."):
            file_bad[nm] = "manifest name is not a plain file name"
        elif not os.path.isfile(path):
            file_bad[nm] = "listed in manifest but absent"
        elif e["bytes"] is not None and os.path.getsize(path) != e["bytes"]:
            file_bad[nm] = "size differs from manifest"
        elif sha256_file(path) != e["sha256"].lower():
            file_bad[nm] = "sha256 differs from manifest"
    wheel_related = set()
    owned = {}
    for nm, e in listed.items():
        if e["owner"] is not None:
            owned.setdefault(e["owner"], []).append(nm)
            wheel_related.add(nm)
    for w in wheel_names:
        wheel_related.update((w, w + CHECK_SUFFIX))
    for nm, why in sorted(file_bad.items()):
        if nm not in wheel_related:
            res["pack_defects"].append("%s: %s" % (nm, why))
    for w in wheel_names:
        wpath = os.path.join(pack, w)
        info = {"name": w, "path": wpath, "file_ok": False, "record_ok": False, "reasons": [],
                "check_record_sha256": None, "wheel_sha256": None, "modules": [], "waived": []}
        reasons = info["reasons"]
        if not (NPM_FILE_RE if npm else WHEEL_RE).match(w):
            reasons.append("wheel file name has unexpected characters")
        if w not in listed:
            reasons.append("wheel not listed in manifest")
        elif w in file_bad:
            reasons.append("wheel %s" % file_bad[w])
        else:
            info["file_ok"] = True
        info["wheel_sha256"] = sha256_file(wpath)
        for comp in owned.get(w, []):
            if comp in file_bad:
                reasons.append("companion %s %s" % (comp, file_bad[comp]))
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
                if npm and not probs:
                    probs = _npm_tarball_problems(rec, wpath, lock)
                reasons.extend(probs)
                if not probs and rname in listed and rname not in file_bad:
                    info["record_ok"] = True
                    info["waived"] = _waiver_lines(rec)
        if info["file_ok"] and not reasons and not npm:
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
    if res.get("ecosystem") == "npm":
        return "INTAKE-VERIFY pack=%s tarballs=%d verified=%d checked=%d stray=%d ok=%s" % (
            res["pack"], len(res["wheels"]), res["verified"], res["checked"], len(res["stray"]), res["ok"])
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
    # a waived wheel is checked, and every waived check is named (its failure stays in the record): one line per check,
    # printed before the INTAKE-VERIFY last line
    for i in res["wheels"]:
        for n, reason in i.get("waived", []):
            print("INTAKE-VERIFY-WAIVED %s check %d: %s" % (ascii_line(i["name"]), n, ascii_line(reason, limit=1000)))


# ---------------------------------------------------------------- npm install (the CTO ruling item 5, 2026-10-16)
# install --ecosystem npm --pack <pack> --lockfile <bun.lock> --target <bun cache dir> [--by <serial>] [--receipt-dir <dir>]
# Places each verified npm tarball into a bun install cache as the UNPACKED folder <name>@<version>@@@1 (a scoped name keeps
# its slash as a folder), the layout ops/bun_cache_precheck.py reads. The 'present' rule is that script's own, loaded by path.
# Nothing runs: no lifecycle script, no bun, no package manager, no socket. Whole-install refusal: when any tarball is not
# cleared, or any destination exists and is not present, nothing is written to the target.

NPM_INSTALL_SCHEMA = "intake-npm-install/1"
NPM_INSTALL_NAME_RE = re.compile(r"^(?:@[a-z0-9][a-z0-9._-]*/)?[a-z0-9][a-z0-9._-]*$")
NPM_INSTALL_VER_RE = re.compile(r"^[0-9A-Za-z][0-9A-Za-z.+-]*$")
NPM_MAX_MEMBER = 64 * 1024 * 1024
NPM_MAX_EXPANDED = 256 * 1024 * 1024
HERE_RECEIVE = os.path.dirname(os.path.abspath(__file__))
NPM_PRECHECK = os.path.normpath(os.path.join(
    HERE_RECEIVE, "..", "..", "..", "infra", "aws", "ec2", "opal-gateway", "ops", "bun_cache_precheck.py"))


def load_precheck():
    """ops/bun_cache_precheck.py loaded by path. Returns (module, None), or (None, the reason it cannot be used)."""
    if not os.path.isfile(NPM_PRECHECK):
        return None, "bun_cache_precheck.py is absent at %s" % NPM_PRECHECK
    spec = importlib.util.spec_from_file_location("bun_cache_precheck", NPM_PRECHECK)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except Exception as exc:  # a precheck that cannot load is a refusal, never a skip
        return None, "bun_cache_precheck.py cannot be loaded: %s: %s" % (type(exc).__name__, exc)
    return mod, None


def npm_package_root(members):
    """STANDALONE MIRROR of intake_check.npm_package_root (this tool ships alone): the package root of one npm tarball, its
    single top-level folder whatever its name. members: (name, is_dir) for every member in archive order. Returns (root, None)
    or (None, the reason). Refused: no members; an absolute, drive-qualified or backslashed name; a first component of '', '.'
    or '..'; a regular file at the archive root; a file where the top-level folder should be; more than one top-level folder.
    Parity arms (this text against the intake_check original) are in test_intake_npm_topdir.py."""
    if not members:
        return None, "the archive holds no members"
    bare_files, with_children, firsts = set(), set(), set()
    for name, is_dir in members:
        if is_dir:
            name = name.rstrip("/")
        if name.startswith("/") or re.match(r"^[A-Za-z]:", name) or "\\" in name:
            return None, "a member name is absolute, drive-qualified or backslashed: %s" % ascii(name)
        parts = name.split("/")
        if parts[0] in ("", ".", ".."):
            return None, "the first component of %s is %s: no top-level folder" % (ascii(name), ascii(parts[0]))
        firsts.add(parts[0])
        if len(parts) > 1:
            with_children.add(parts[0])
        elif not is_dir:
            bare_files.add(parts[0])
    if bare_files:
        clash = sorted(bare_files & with_children)
        if clash:
            return None, "a file where the top-level folder should be: %s" % ascii(clash[0])
        return None, "a member at the archive root, not inside a folder: %s" % ascii(sorted(bare_files)[0])
    if len(firsts) > 1:
        return None, "more than one top-level folder: %s" % ", ".join(ascii(n) for n in sorted(firsts))
    return sorted(firsts)[0], None


def npm_plan_members(tgz_path):
    """Read one npm tarball IN MEMORY and name what it would place. Returns a dict: root (the package root, npm_package_root),
    files (path inside the package root, size), dirs, package_json (bytes or None) and problems. A non-empty problems list
    refuses the tarball. A tarball with no single top-level folder is refused first. A member is refused when its name is
    absolute, drive-qualified, backslashed, has a '..' or an empty component, is outside the one root folder, is a link of any
    kind (links are refused outright, so none can leave the package), is not a regular file or folder, or is over
    NPM_MAX_MEMBER; the expanded total is capped at NPM_MAX_EXPANDED. Nothing is written."""
    files, dirs, problems, seen = [], [], [], set()
    package_json, total = None, 0
    try:
        with tarfile.open(tgz_path, mode="r:gz") as tf:
            members = tf.getmembers()
            root, reason = npm_package_root([(m.name, m.isdir()) for m in members])
            if reason:
                return {"root": None, "files": [], "dirs": [], "package_json": None, "problems": ["no package root: " + reason]}
            for m in members:
                shown = ascii_line(m.name, 120)
                name = m.name.rstrip("/") if m.isdir() else m.name
                parts = name.split("/")
                reason = None
                if name.startswith("/") or re.match(r"^[A-Za-z]:", name) or "\\" in name:
                    reason = "absolute, drive-qualified or backslashed name"
                elif ".." in parts:
                    reason = "a '..' component"
                elif parts[0] != root:
                    reason = "member outside the package root %s" % ascii_line(root, 80)
                elif m.issym() or m.islnk():
                    reason = "a link member (links are refused, never unpacked)"
                elif not (m.isreg() or m.isdir()):
                    reason = "member is not a regular file or folder"
                elif m.size > NPM_MAX_MEMBER:
                    reason = "member over %d bytes" % NPM_MAX_MEMBER
                elif len(parts) > 1 and "" in parts[1:]:
                    reason = "an empty path component"
                if reason:
                    problems.append("%s: %s" % (shown, reason))
                    continue
                rel = "/".join(parts[1:])
                if not rel:
                    continue  # the package root folder itself
                if rel in seen:
                    problems.append("%s: duplicate member" % shown)
                    continue
                seen.add(rel)
                if m.isdir():
                    dirs.append(rel)
                    continue
                total += m.size
                if total > NPM_MAX_EXPANDED:
                    problems.append("expanded size over %d bytes" % NPM_MAX_EXPANDED)
                    break
                files.append((rel, m.size))
                if rel == "package.json":
                    package_json = tf.extractfile(m).read()
    except (tarfile.TarError, OSError, EOFError, zlib.error) as exc:
        problems.append("not a readable gzip tar: %s" % type(exc).__name__)
    if package_json is None and not problems:
        problems.append("%s/package.json is absent" % root)
    return {"root": root, "files": files, "dirs": dirs, "package_json": package_json, "problems": problems}


def _npm_unpack_into(tgz_path, folder):
    """Write the members of one tarball (already cleared by npm_plan_members) into an EXISTING empty folder, the one top-level
    folder removed, whatever its name. Regular files and folders only; no permission or time is restored from the archive.
    A tarball with no single top-level folder raises before anything is written."""
    with tarfile.open(tgz_path, mode="r:gz") as tf:
        members = tf.getmembers()
        root, reason = npm_package_root([(m.name, m.isdir()) for m in members])
        if reason:
            raise ValueError("no package root: %s" % reason)
        for m in members:
            name = m.name.rstrip("/") if m.isdir() else m.name
            rel = "/".join(name.split("/")[1:])
            if not rel:
                continue
            out = os.path.join(folder, *rel.split("/"))
            if m.isdir():
                os.makedirs(out, exist_ok=True)
                continue
            os.makedirs(os.path.dirname(out), exist_ok=True)
            with open(out, "wb") as fh:
                shutil.copyfileobj(tf.extractfile(m), fh)


def _npm_sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def _npm_plan_item(pack, fn, pc, target):
    """One tarball's plan, read-only: name@version from its check record (check 2's requested fields), the in-memory member
    plan, the package.json that must name the same name and version, and the destination's state by the precheck's rule."""
    item = {"file_name": fn, "name": None, "version": None, "dest": None, "outcome": None, "reason": None,
            "package_json_sha256": None, "files": [], "dirs": [], "package_json": None}

    def refuse(why):
        item["outcome"], item["reason"] = "refused", why
        return item

    try:
        with open(os.path.join(pack, fn + CHECK_SUFFIX), "rb") as fh:
            rec = json.loads(fh.read().decode("utf-8"))
    except (OSError, ValueError):
        return refuse("check record absent or unreadable")
    checks = rec.get("checks") if isinstance(rec, dict) else None
    ev2 = checks[1].get("evidence") if isinstance(checks, list) and len(checks) > 1 and isinstance(checks[1], dict) else None
    name = ev2.get("requested_name") if isinstance(ev2, dict) else None
    version = ev2.get("requested_version") if isinstance(ev2, dict) else None
    if not (isinstance(name, str) and NPM_INSTALL_NAME_RE.match(name) and isinstance(version, str)
            and NPM_INSTALL_VER_RE.match(version)):
        return refuse("check record names no valid npm name and version")
    item["name"], item["version"] = name, version
    plan = npm_plan_members(os.path.join(pack, fn))
    if plan["problems"]:
        return refuse("; ".join(plan["problems"][:3]))
    try:
        doc = json.loads(plan["package_json"].decode("utf-8-sig"))
    except ValueError:
        return refuse("%s/package.json does not parse" % plan["root"])
    if not isinstance(doc, dict) or doc.get("name") != name or doc.get("version") != version:
        return refuse("%s/package.json does not name %s@%s" % (plan["root"], name, version))
    item["files"], item["dirs"], item["package_json"] = plan["files"], plan["dirs"], plan["package_json"]
    dest = os.path.abspath(os.path.join(target, *("%s@%s@@@1" % (name, version)).split("/")))
    item["dest"] = dest
    state = pc._state(target, name, version)
    if state == "ok":
        item["outcome"], item["reason"] = "already", "present by the precheck's own definition; left untouched"
        pj = os.path.join(dest, "package.json")
        if os.path.isfile(pj):
            with open(pj, "rb") as fh:
                item["package_json_sha256"] = _npm_sha256_bytes(fh.read())
    elif os.path.lexists(dest):
        return refuse("destination exists and is not present (%s); never overwritten: the issuer or the cache's owner decides" % state)
    else:
        item["outcome"], item["reason"] = "unpack", "absent; to be unpacked"
        item["package_json_sha256"] = _npm_sha256_bytes(plan["package_json"])
    return item


def _npm_place(item, target):
    """Unpack one planned package into a hidden sibling folder, then rename it into place: a half-unpacked folder is never
    visible under its final name. Raises on any failure, after removing the sibling."""
    parent = os.path.dirname(item["dest"])
    os.makedirs(parent, exist_ok=True)
    tmp = tempfile.mkdtemp(prefix=".intake-unpack-", dir=parent)
    try:
        _npm_unpack_into(item["pack_path"], tmp)
        if not os.path.isfile(os.path.join(tmp, "package.json")):
            raise OSError("unpacked folder holds no package.json")
        os.rename(tmp, item["dest"])
    except Exception:
        shutil.rmtree(tmp, ignore_errors=True)
        raise


def install_npm(pack, target, lockfile, by, receipt_dir=None):
    """Verify the npm pack, plan every tarball, and place the planned packages only when every one is cleared. Returns
    (summary, verify result, per-tarball items). Writes one receipt; never runs anything."""
    summ = {"schema": NPM_INSTALL_SCHEMA, "pack": os.path.basename(os.path.normpath(pack)), "target": os.path.abspath(target),
            "lockfile": os.path.basename(lockfile) if lockfile else None, "by": by, "tarballs": 0, "unpacked": 0,
            "already": 0, "refused": 0, "present": 0, "ok": False, "reason": None}
    if not os.path.isdir(pack):
        summ["reason"] = "pack dir does not exist"
        return summ, None, []
    pc, why = load_precheck()
    tgzs = sorted(n for n in os.listdir(pack) if n.endswith(NPM_EXT) and os.path.isfile(os.path.join(pack, n)))
    summ["tarballs"] = len(tgzs)
    if pc is None:
        summ["reason"] = why
        return summ, None, []
    res = verify_pack(pack, "npm", lockfile)
    items = [_npm_plan_item(pack, fn, pc, target) for fn in tgzs]
    for it in items:
        it["pack_path"] = os.path.join(pack, it["file_name"])
    cleared = res["ok"] and all(it["outcome"] in ("unpack", "already") for it in items)
    write_failed = False
    if not cleared:
        for it in items:
            if it["outcome"] == "unpack":
                it["outcome"], it["reason"] = "refused", "not written: the install is refused as a whole"
    else:
        for it in items:
            if it["outcome"] != "unpack":
                continue
            if write_failed:
                it["outcome"], it["reason"] = "refused", "not written: an earlier package failed to write"
                continue
            try:
                _npm_place(it, target)
                it["outcome"], it["reason"] = "unpacked", "unpacked into place"
            except Exception as exc:
                write_failed = True
                it["outcome"], it["reason"] = "refused", "write failed: %s: %s" % (type(exc).__name__, exc)
    for it in items:
        it.pop("files", None)
        it.pop("dirs", None)
        it.pop("package_json", None)
        it.pop("pack_path", None)
        it["present"] = bool(it["name"] and it["version"] and pc._state(target, it["name"], it["version"]) == "ok")
    summ["unpacked"] = sum(1 for it in items if it["outcome"] == "unpacked")
    summ["already"] = sum(1 for it in items if it["outcome"] == "already")
    summ["refused"] = sum(1 for it in items if it["outcome"] == "refused")
    summ["present"] = sum(1 for it in items if it["present"])
    summ["ok"] = bool(res["ok"] and cleared and not write_failed and summ["tarballs"] > 0
                      and summ["refused"] == 0 and summ["unpacked"] + summ["already"] == summ["tarballs"]
                      and summ["present"] == summ["tarballs"])
    if not res["ok"]:
        summ["reason"] = "the pack does not verify (see the verify lines)"
    summ["items"] = items
    device, _problem = device_name()
    summ["device"] = device
    summ["at"] = now_utc()
    folder = receipt_dir or os.path.join(pack, RECEIPTS_DIR)
    os.makedirs(folder, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    path = os.path.join(folder, "install-npm.%s.%s.%d.json" % (device or "unnamed", stamp, os.getpid()))
    receipt = {k: v for k, v in summ.items() if k != "items"}
    receipt["packages"] = [{k: it[k] for k in ("file_name", "name", "version", "dest", "outcome", "reason",
                                               "package_json_sha256", "present")} for it in items]
    with open(path, "w", encoding="ascii", newline="\n") as fh:
        json.dump(receipt, fh, indent=2, ensure_ascii=True)
        fh.write("\n")
    summ["receipt"] = path
    return summ, res, items


def npm_install_last_line(summ):
    return "INTAKE-NPM-INSTALL tarballs=%d unpacked=%d already=%d refused=%d present=%d/%d ok=%s" % (
        summ["tarballs"], summ["unpacked"], summ["already"], summ["refused"], summ["present"], summ["tarballs"], summ["ok"])


def run_install_npm(args):
    """The CLI of install --ecosystem npm: usage refusals first, then the install, then the per-package lines and the last line."""
    bad = []
    if not args.npm_pack:
        bad.append("--pack <pack dir>")
    if not args.lockfile:
        bad.append("--lockfile <bun.lock> (the verify check reads the tarballs against it; a missing lockfile is a refusal)")
    if not args.target:
        bad.append("--target <bun cache dir>")
    if args.dry_run or args.python or args.user:
        bad.append("none of --dry-run, --python, --user (those are pip's)")
    if bad:
        print("REFUSED: install --ecosystem npm needs %s" % "; ".join(bad))
        return 1
    by = args.by or os.environ.get("OPAL_AGENT_SERIAL") or "unknown"
    summ, res, items = install_npm(args.npm_pack, args.target, args.lockfile, by, args.receipt_dir)
    if res is not None:
        print_verify_detail(res)
    if summ.get("reason"):
        print("REASON: %s" % ascii_line(summ["reason"]))
    for it in items:
        label = "%s@%s" % (it["name"], it["version"]) if it["name"] else it["file_name"]
        print("PACKAGE %s %s reason=%s" % (ascii_line(label, 160), it["outcome"], ascii_line(it["reason"] or "", 240)))
    print("RECEIPT %s" % ascii_line(summ.get("receipt", "none")))
    print(npm_install_last_line(summ))
    return 0 if summ["ok"] else 1


# ---------------------------------------------------------------- pip and import plumbing

def build_pip_command(wheel_path, target=None, user=False, interpreter=None):
    """The one pip command line this tool ever builds: a list, no shell, never an index, never a resolver.
    interpreter is the python that runs pip (default: this one). user=True adds --user; a target folder adds --target;
    with neither, pip installs into the interpreter's own site (a venv's python)."""
    cmd = [interpreter or sys.executable, "-m", "pip", "install", "--no-index", "--no-deps"]
    if user:
        cmd.append("--user")
    elif target is not None:
        cmd += ["--target", target]
    cmd.append(wheel_path)
    return cmd


def strip_ansi(text):
    """The text with ANSI colour and control sequences removed (a coloured traceback otherwise hides its module name)."""
    return ANSI_RE.sub("", text or "")


def build_plain_env(base=None):
    """A copy of the environment with colour pinned off and FORCE_COLOR removed: a Python 3.14 child started with
    FORCE_COLOR set colours its traceback."""
    env = dict(os.environ if base is None else base)
    for k in list(env):
        if k.upper() == "FORCE_COLOR":
            del env[k]
    env.update(COLOUR_PINS)
    return env


def build_import_env():
    """Environment for the import child (the one that runs a pack module): plain output."""
    return build_plain_env()


def build_child_env():
    """Environment for the pip child: no inherited PIP_* setting, no user config, no pip self-version check (a network call),
    and plain output."""
    env = {k: v for k, v in os.environ.items() if not k.upper().startswith("PIP_")}
    env = build_plain_env(env)
    env["PIP_NO_INDEX"] = "1"
    env["PIP_DISABLE_PIP_VERSION_CHECK"] = "1"
    env["PIP_CONFIG_FILE"] = os.devnull
    return env


def _keep_pip_run(cmd, inherited, rc, text):
    LAST_PIP_RUN.clear()
    LAST_PIP_RUN.update({"command": list(cmd), "inherited": inherited, "rc": rc, "text": text or ""})


def run_pip(cmd):
    """Returns (rc, last non-empty line), as before. The whole run is also kept in LAST_PIP_RUN for write_pip_log."""
    COMMANDS_RUN.append(list(cmd))
    inherited = sorted(k for k in os.environ if k.upper().startswith("PIP_"))
    try:
        cp = subprocess.run(cmd, env=build_child_env(), capture_output=True, text=True, encoding="utf-8",
                            errors="replace", timeout=PIP_TIMEOUT_S, stdin=subprocess.DEVNULL)
    except subprocess.TimeoutExpired:
        msg = "pip timed out after %ds" % PIP_TIMEOUT_S
        _keep_pip_run(cmd, inherited, 124, msg)
        return 124, msg
    except OSError as exc:
        msg = "pip could not start (%s)" % type(exc).__name__
        _keep_pip_run(cmd, inherited, 127, msg)
        return 127, msg
    _keep_pip_run(cmd, inherited, cp.returncode, cp.stdout + cp.stderr)
    last = ""
    for line in (cp.stderr + "\n" + cp.stdout).splitlines():
        if line.strip():
            last = line
    return cp.returncode, ascii_line(last)


def write_pip_log(pack, info, device, kind):
    """Writes receipts/<wheel>.<kind>-pip.<device>.log for the pip run that run_pip just made, and returns the receipt key
    pip_log = {file, sha256, bytes}. ASCII, LF line ends; a non-ASCII character becomes '?'. Pip's text is capped at
    PIP_LOG_CAP bytes and a cut log ends with a TRUNCATED line.

    HONEST LIMIT: the log records the command, the pinned environment and what pip itself printed. It is NOT a network
    trace and does not prove that no packet left the box; it shows that the tool asked pip for no index and that no
    inherited index setting reached pip. python= is this tool's interpreter version, as the receipt's python field is."""
    run = LAST_PIP_RUN
    body = run["text"].replace("\r\n", "\n").replace("\r", "\n").encode("ascii", "replace")
    cut = len(body) > PIP_LOG_CAP
    if cut:
        body = body[:PIP_LOG_CAP]
    if body and not body.endswith(b"\n"):
        body += b"\n"
    if cut:
        body += b"TRUNCATED at %d bytes\n" % PIP_LOG_CAP
    head = [
        "INTAKE-PIP-LOG schema=1",
        "device=%s" % ascii_line(device, 80),
        "utc=%s" % now_utc(),
        "kind=%s" % kind,
        "python=%s" % platform.python_version(),
        "command=" + json.dumps(run["command"]),
        "env_pins=" + " ".join("%s=%s" % pin for pin in PIP_ENV_PINS),
        "inherited_pip_vars_removed=" + ",".join(ascii_line(k, 120) for k in run["inherited"]),
        "rc=%s" % run["rc"],
        "--- pip stdout+stderr ---",
    ]
    data = ("\n".join(head) + "\n").encode("ascii") + body
    name = "%s.%s-pip.%s.log" % (info["name"], kind, device)
    os.makedirs(os.path.join(pack, RECEIPTS_DIR), exist_ok=True)
    with open(os.path.join(pack, RECEIPTS_DIR, name), "wb") as fh:
        fh.write(data)
    return {"file": name, "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}


def classify_import(rc, stderr, own_modules):
    """Returns (class, missing_name, first_error_line). class: imported | import_missing_dep | failed."""
    if rc == 0:
        return "imported", None, ""
    text = strip_ansi(stderr)
    lines = [ln for ln in text.splitlines() if ln.strip()]
    err = ascii_line(lines[-1]) if lines else "exit code %s with no stderr" % rc
    m = MISSING_RE.search(text)
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
                            timeout=IMPORT_TIMEOUT_S, stdin=subprocess.DEVNULL, env=build_import_env())
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


def write_receipt(pack, info, device, outcome, reason, command=None, rc=None, imports=None, form=None, interp=None,
                  pip_log=None):
    rec = {
        "schema": "intake-receipt/1",
        "device": device,
        "python": platform.python_version(),
        "file_name": info["name"],
        "received_sha256": info.get("wheel_sha256"),
        "check_record_sha256": info.get("check_record_sha256"),
        "install": {"command": command if command is not None else [], "rc": rc,
                    "target_form": form, "interpreter": interp},
        "imports": imports or [],
        "outcome": outcome,
        "reason": reason,
        "at": now_utc(),
    }
    if pip_log is not None:
        rec["pip_log"] = pip_log
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
        plog = write_pip_log(pack, info, device, "prove")
        if rc != 0:
            write_receipt(pack, info, device, "install_failed", "pip rc=%d: %s" % (rc, last), cmd, rc,
                          form="target", interp=sys.executable, pip_log=plog)
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
        write_receipt(pack, info, device, outcome, reason, cmd, rc, imports, form="target", interp=sys.executable,
                      pip_log=plog)
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


INSTALL_NEEDS_TARGET = "REFUSED: install needs a target: --python <interpreter> | --target <new dir> | --user"


def _same_interpreter(path):
    return os.path.normcase(os.path.abspath(path)) == os.path.normcase(os.path.abspath(sys.executable))


def resolve_install_target(python, target, user):
    """Exactly one install target. Returns (form, interpreter, target_dir, problem); form is python, target or user.
    Nothing is created or installed here."""
    if python is None and target is None and not user:
        return None, None, None, INSTALL_NEEDS_TARGET
    if target is not None and (python is not None or user):
        return None, None, None, "REFUSED: give exactly one target: --target cannot be combined with --python or --user"
    if target is not None:
        if os.path.exists(target) and (not os.path.isdir(target) or os.listdir(target)):
            return None, None, None, "REFUSED: --target must be a new or empty directory"
        return "target", sys.executable, target, None
    if python is not None:
        if not os.path.isfile(python):
            return None, None, None, "REFUSED: --python %s is not a file" % ascii_line(python)
        if user:
            if not _same_interpreter(python):
                return None, None, None, ("REFUSED: --user with --python is accepted only for this interpreter (%s)"
                                          % ascii_line(sys.executable))
            return "user", sys.executable, None, None
        if _same_interpreter(python):
            return None, None, None, ("REFUSED: --python is this interpreter (%s); add --user to install into its user "
                                      "site, or name another interpreter" % ascii_line(sys.executable))
        return "python", python, None, None
    return "user", sys.executable, None, None


def write_install_record(pack, info, device, form, interpreter, target, cmd, rc, last, pip_log=None):
    """One record per wheel per real install: where the wheel went (install.target_form, the interpreter, the folder).
    It sits beside the prove receipt and the receipt gate does not read it."""
    rec = {
        "schema": "intake-install/1",
        "device": device,
        "file_name": info["name"],
        "received_sha256": info.get("wheel_sha256"),
        "install": {"command": cmd, "rc": rc, "target_form": form, "interpreter": interpreter, "target": target},
        "last_line": ascii_line(last),
        "at": now_utc(),
    }
    if pip_log is not None:
        rec["pip_log"] = pip_log
    os.makedirs(os.path.join(pack, RECEIPTS_DIR), exist_ok=True)
    path = os.path.join(pack, RECEIPTS_DIR, "%s.install.%s.json" % (info["name"], device))
    with open(path, "w", encoding="ascii", newline="\n") as fh:
        json.dump(rec, fh, indent=2, ensure_ascii=True)
        fh.write("\n")
    return rec


def install_pack(pack, dry_run, form, interpreter=None, target=None):
    """form is python, target or user (from resolve_install_target); the caller has already refused a missing target."""
    device, problem = device_name()
    summ = {"device": device or "UNSET", "n": 0, "installed": 0, "refused": 0, "ok": False, "form": form}
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
    where = interpreter or sys.executable
    for info in res["wheels"]:
        cmd = build_pip_command(info["path"], target=target, user=(form == "user"), interpreter=where)
        if dry_run:
            print("DRY-RUN: " + json.dumps(cmd))
            continue
        rc, last = run_pip(cmd)
        plog = write_pip_log(pack, info, device, "install")
        write_install_record(pack, info, device, form, where, target, cmd, rc, last, pip_log=plog)
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

INSTALL_HELP = """install needs EXACTLY ONE target. There is no default: the old --user default is gone.
  --python <exe>   pip installs into that interpreter's own site, with no --user (use a fresh venv's python).
                   Naming this tool's own interpreter is refused unless --user is also given.
  --target <dir>   pip --target into a NEW or EMPTY folder (refused if the folder exists and holds anything).
  --user           the old user-site install of this interpreter, only when asked for by name.
A refused install prints REFUSED and installs nothing. Each real install writes receipts/<wheel>.install.<device>.json
recording install.target_form (python, target or user) and the interpreter."""


def main(argv=None):
    ap = argparse.ArgumentParser(prog="intake_receive.py", description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="verb", required=True)
    v = sub.add_parser("verify")
    v.add_argument("--from", dest="pack", required=True)
    v.add_argument("--ecosystem", choices=("pypi", "npm"), default="pypi")
    v.add_argument("--lockfile", default=None, help="npm: the bun text lockfile the tarballs are re-read against")
    p = sub.add_parser("prove")
    p.add_argument("--from", dest="pack", required=True)
    p.add_argument("--scratch", required=True)
    i = sub.add_parser("install", formatter_class=argparse.RawDescriptionHelpFormatter, description=INSTALL_HELP)
    i.add_argument("--from", dest="pack", default=None)
    i.add_argument("--ecosystem", choices=("pypi", "npm"), default="pypi",
                   help="pypi (default): the wheel install below; npm: unpack each verified tarball into a bun install cache")
    i.add_argument("--pack", dest="npm_pack", default=None, help="npm only: the verified npm pack folder")
    i.add_argument("--lockfile", default=None, help="npm only: the bun text lockfile the verify check reads the tarballs against")
    i.add_argument("--receipt-dir", default=None, help="npm only: where the install receipt is written (default <pack>/receipts)")
    i.add_argument("--by", default=None, help="npm only: the serial that placed the packages (default OPAL_AGENT_SERIAL)")
    i.add_argument("--dry-run", action="store_true", dest="dry_run")
    i.add_argument("--python", metavar="EXE", default=None,
                   help="install with this interpreter's own site and no --user (a fresh venv's python); "
                        "naming this tool's own interpreter needs --user as well")
    i.add_argument("--target", metavar="NEW_DIR", default=None,
                   help="pip --target into this NEW or EMPTY folder")
    i.add_argument("--user", action="store_true",
                   help="the old user-site install of this interpreter; only when asked for by name")
    sub.add_parser("selftest-unchecked")
    args = ap.parse_args(argv)
    if args.verb == "verify":
        if args.ecosystem == "npm" and not args.lockfile:
            print("REFUSED: --ecosystem npm needs --lockfile <bun.lock>; a missing lockfile is a refusal, never a skip")
        res = verify_pack(args.pack, args.ecosystem, args.lockfile)
        print_verify_detail(res)
        print(verify_last_line(res))
        return 0 if res["ok"] else 1
    if args.verb == "prove":
        rc, summ = prove_pack(args.pack, args.scratch)
        print_prove_last(summ)
        return rc
    if args.verb == "install":
        if args.ecosystem == "npm":
            return run_install_npm(args)
        if args.pack is None:
            i.error("the following arguments are required: --from")
        form, interp, target_dir, problem = resolve_install_target(args.python, args.target, args.user)
        if problem:
            print(problem)
            return 1
        rc, summ = install_pack(args.pack, args.dry_run, form, interp, target_dir)
        print("INTAKE-INSTALL device=%s python=%s wheels=%d installed=%d refused=%d target_form=%s dry_run=%s ok=%s" % (
            summ["device"], platform.python_version(), summ["n"], summ["installed"], summ["refused"],
            summ["form"], bool(args.dry_run), summ["ok"]))
        return rc
    summ = selftest_unchecked()
    print_prove_last(summ)
    return 0 if (summ["installed"] == 0 and summ["refused"] == 1) else 1


if __name__ == "__main__":
    sys.exit(main())
