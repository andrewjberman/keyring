"""intake_check.py -- the eight narrow checks on ONE held package file, the check record, the release, and the pack.

NOTHING FROM A PACKAGE FILE IS EVER INSTALLED, IMPORTED OR EXECUTED. A wheel is opened with `zipfile`, its member names are
listed and its bytes are compared; no member is extracted to disk and no member is run. No request leaves this machine from
this tool: it makes none. The only processes it starts are a read-only PowerShell query of the Windows Security Center's
antivirus registrations (check 7; it changes no security setting) and, for information only, `git log` on the signature
file (check 8). Check 7 never runs a scanner: it reads which antivirus product is active, writes a copy of the held file
beside it (`<file name>.scan-copy`, always removed afterwards) so the active product's on-access scanning sees it, waits,
and records whether the file and the copy are still present and unchanged.

Verbs:
  check   --batch <id> --file <file name> [--approved-by <path>] [--signed-by <path>]
          [--min-release-age-days 14] [--min-earlier-releases 3] [--scan-wait-seconds 20]
          [--ecosystem pypi|npm] [--lockfile <bun.lock>]   (npm: the CT-cc-1 limb; a missing --lockfile is a refusal)
  release --batch <id> --file <file name> [--ecosystem pypi|npm]
  pack    --batch <id> --out <dir> [--released-only] [--ecosystem pypi|npm]
  selftest-unsigned
  selftest-av   (reads the REAL Security Center, prints one INTAKE-AV line, writes no file)

Records are JSON, ASCII only, under <records>/<batch>/ (see records_dir). The FETCH record is read; the CHECK record is
written. Paths:
  holding root  OPAL_INTAKE_ROOT, else <drive of the workspace root>/opal-intake  (holding/<batch>/, release/<batch>/)
  records       OPAL_INTAKE_RECORDS (a base; records live in <base>/<batch>/), else org/devices/intake/records/<batch>/
  AV answer     OPAL_INTAKE_AV_JSON (tests: a path to a JSON file standing in for the Security Center answer), else the
                real query (root/SecurityCenter2, class AntiVirusProduct)
  site-packages OPAL_INTAKE_SITE (os.pathsep list), else this interpreter's site-packages
  signer dir    OPAL_INTAKE_SIGNER_DIR (tests), else org/tier1_exec/1.0.0_SA_CTO/deliverables under the repository root
The ONLY producer of the overall verdicts "checked" and "released-with-waiver" is compute_verdict() (over _derive()).
A failed check 3 to 7 is carried to release only by a WAIVE line in the signed check-8 file (see parse_waivers).
"""
from __future__ import annotations

import argparse
import base64
import configparser
import csv
import datetime
import email.parser
import hashlib
import itertools
import json
import os
import pathlib
import posixpath
import re
import shutil
import site
import subprocess
import sys
import tarfile
import tempfile
import time
import zipfile
import zlib

REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]
DEFAULT_SIGNER_REL = "org/tier1_exec/1.0.0_SA_CTO/deliverables"
COMPILED_SUFFIXES = (".pyd", ".dll", ".so", ".exe")
AV_QUERY_TIMEOUT = 30
DEFAULT_SCAN_WAIT = 20
SCAN_COPY_SUFFIX = ".scan-copy"
MAX_PY_BYTES = 50 * 1024 * 1024
PRINT_CAP = 10

# ---------------------------------------------------------------------------------------------------------------------
# The brief's own words (docs/briefs/nfra-ctlpln-package-intake-and-download-tiers-brief-20261007.md, Part V.1).
# Copied verbatim; test_intake_check.py fails if any string no longer appears in the brief file.
# ---------------------------------------------------------------------------------------------------------------------
CHECK_TABLE = [
    {"n": 1, "name": "sha256 equals the digest the index publishes",
     "rules_out": "a file altered in transit or served by an impostor",
     "leaves": "anything the real project published"},
    {"n": 2, "name": "name, version and tags are exactly the approved line",
     "rules_out": "a near-name package; a resolver substituting another version or pulling an unlisted package",
     "leaves": "a wrong approval"},
    {"n": 3, "name": "the version is one this machine already runs",
     "rules_out": "a brand-new release nobody has used",
     "leaves": "a build for Python 3.14 that differs from the 3.12 build of the same version"},
    {"n": 4, "name": "the release's age and the project's earlier releases",
     "rules_out": "a package or release published days ago",
     "leaves": "an old compromise not yet found"},
    {"n": 5, "name": "build attestation present or absent",
     "rules_out": "where present: a file uploaded by hand from a stolen account",
     "leaves": "where absent: nothing; many projects publish none"},
    {"n": 6, "name": "the archive opened and listed, never installed",
     "rules_out": "code added outside the compiled files",
     "leaves": "code inside the compiled files"},
    {"n": 7, "name": "Windows' own malware scan of the file",
     "rules_out": "known malware",
     "leaves": "anything new or targeted"},
    {"n": 8, "name": "a person reads the result of 1 to 7 and signs the batch",
     "rules_out": "a tool's silent failure being read as a pass",
     "leaves": "what none of 1 to 7 can see"},
]
DELIVERY_SENTENCE = (
    "What no check here rules out: a compiled file that the real project's own compromised release process published. "
    "Checks 3 and 4 shrink that case by taking only versions that have been public and in use for a while. "
    "They do not close it."
)
VERDICTS = ("passed", "failed", "not_applicable", "unsigned", "awaiting")
ACCEPTED_VERDICTS = ("checked", "released-with-waiver")   # the two overall verdicts that release and pack accept
# Check 7's limit, in the words the CTO ruled (msg 106549). It travels in the check record beside check 7 and in the delivery
# text. The brief's own "Leaves" text for check 7 (CHECK_TABLE) stays as it is, beside it.
LIMIT_SENTENCE = (
    "No test-virus file was planted as a control, because it would raise the managed product's alarm; so this check shows "
    "that an enabled, current product did not remove or alter the file within the wait, and does not show that the product "
    "inspected it."
)
DECODING_NOTE = (
    "productState is read as six hex digits 0xAABBCC: BB is real-time protection (0x10 or 0x11 on; 0x00 or 0x01 off; any "
    "other byte unknown); CC is the definitions (0x00 current; 0x10 out of date; any other byte unknown); unknown is never "
    "treated as on or current. Worked examples: 393472 = 0x060100 -> off; 266240 = 0x041000 -> on, definitions current."
)


# ---------------------------------------------------------------------------------------------------------------------
# configuration
# ---------------------------------------------------------------------------------------------------------------------
def derive_drive_prefix() -> pathlib.Path:
    """The drive root of the workspace, derived: /cygdrive/c if it exists, else /c on a POSIX shell; the repository's own
    drive anchor on Windows."""
    if os.name == "nt":
        return pathlib.Path(REPO_ROOT.anchor)
    if os.path.isdir("/cygdrive/c"):
        return pathlib.Path("/cygdrive/c")
    return pathlib.Path("/c")


class Cfg:
    def __init__(self, root=None, records=None, av_json=None, sites=None, signer_dir=None):
        env = os.environ
        self.root = pathlib.Path(root or env.get("OPAL_INTAKE_ROOT") or (derive_drive_prefix() / "opal-intake"))
        self.records_base = pathlib.Path(
            records or env.get("OPAL_INTAKE_RECORDS") or (REPO_ROOT / "org" / "devices" / "intake" / "records"))
        # a path to a JSON file standing in for the Security Center answer; "" or None-with-no-env means the REAL query
        self.av_json = av_json if av_json is not None else env.get("OPAL_INTAKE_AV_JSON")
        if sites is not None:
            self.sites = [pathlib.Path(s) for s in sites]
        elif env.get("OPAL_INTAKE_SITE"):
            self.sites = [pathlib.Path(s) for s in env["OPAL_INTAKE_SITE"].split(os.pathsep) if s]
        else:
            self.sites = default_site_dirs()
        sd = signer_dir or env.get("OPAL_INTAKE_SIGNER_DIR")
        self.signer_dir = pathlib.Path(sd) if sd else None

    def holding(self, batch):
        return self.root / "holding" / batch

    def release(self, batch):
        return self.root / "release" / batch

    def records_dir(self, batch):
        return self.records_base / batch


def default_site_dirs():
    out = []
    try:
        out.extend(site.getsitepackages())
    except Exception:
        pass
    try:
        out.append(site.getusersitepackages())
    except Exception:
        pass
    seen = []
    for s in out:
        p = pathlib.Path(s)
        if p.is_dir() and p not in seen:
            seen.append(p)
    return seen


# ---------------------------------------------------------------------------------------------------------------------
# small helpers
# ---------------------------------------------------------------------------------------------------------------------
def now_utc():
    return datetime.datetime.now(datetime.timezone.utc)


def stamp(dt=None):
    return (dt or now_utc()).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_time(text):
    t = str(text).strip()
    if t.endswith("Z"):
        t = t[:-1] + "+00:00"
    dt = datetime.datetime.fromisoformat(t)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=datetime.timezone.utc)
    return dt


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def norm_name(name):
    return re.sub(r"[-_.]+", "-", str(name)).strip().lower()


def ascii_clean(text):
    return "".join(ch if 32 <= ord(ch) < 127 or ch in "\n\t" else "?" for ch in str(text))


def cap(items, n=PRINT_CAP):
    items = list(items)
    if len(items) <= n:
        return items
    return items[:n] + ["... (+%d more; full list in the record)" % (len(items) - n)]


def write_json_atomic(path, obj):
    path = pathlib.Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(obj, indent=2, ensure_ascii=True, sort_keys=False) + "\n"
    tmp = path.with_name(path.name + ".tmp")
    with open(tmp, "w", encoding="ascii", newline="\n") as fh:
        fh.write(text)
    os.replace(str(tmp), str(path))


def read_json(path):
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def rec(verdict, summary, **detail):
    ev = {"summary": ascii_clean(summary)}
    ev.update(detail)
    return verdict, ev


def parse_wheel_name(file_name):
    """distribution-version[-build]-python-abi-platform.whl, five or six dash-separated parts."""
    if not file_name.endswith(".whl"):
        return None
    parts = file_name[:-4].split("-")
    if len(parts) not in (5, 6):
        return None
    return {"dist": parts[0], "version": parts[1], "build": parts[2] if len(parts) == 6 else "",
            "python_tag": parts[-3], "abi_tag": parts[-2], "platform_tag": parts[-1]}


def expand_tags(py, abi, plat):
    return {"%s-%s-%s" % t for t in itertools.product(py.split("."), abi.split("."), plat.split("."))}


def header_of(text):
    msg = email.parser.HeaderParser().parsestr(text)
    return msg


def wheel_dist_info(zf):
    """The names of the members of the single *.dist-info directory, or (None, reason)."""
    dirs = sorted({n.split("/")[0] for n in zf.namelist() if "/" in n and n.split("/")[0].endswith(".dist-info")})
    if len(dirs) != 1:
        return None, "expected exactly one *.dist-info directory, found %d" % len(dirs)
    return dirs[0], ""


# ---------------------------------------------------------------------------------------------------------------------
# installed copies, found by reading *.dist-info/METADATA, never by importing
# ---------------------------------------------------------------------------------------------------------------------
def find_installed(cfg, name, version):
    """Return (list of copies matching name+version, sorted list of versions of that name found)."""
    want = norm_name(name)
    found, versions = [], set()
    for sd in cfg.sites:
        try:
            entries = sorted(os.listdir(sd))
        except OSError:
            continue
        for ent in entries:
            if not ent.endswith(".dist-info"):
                continue
            meta = sd / ent / "METADATA"
            try:
                with open(meta, "r", encoding="utf-8", errors="replace") as fh:
                    head = []
                    for line in fh:
                        if not line.strip():
                            break
                        head.append(line)
                msg = header_of("".join(head))
            except OSError:
                continue
            if norm_name(msg.get("Name", "")) != want:
                continue
            versions.add(msg.get("Version", ""))
            if msg.get("Version", "") == version:
                found.append({"site": sd, "dist_info": sd / ent, "dist_info_name": ent})
    return found, sorted(versions)


def installed_record_paths(dist_info):
    paths = set()
    try:
        with open(dist_info / "RECORD", "r", encoding="utf-8", errors="replace", newline="") as fh:
            for row in csv.reader(fh):
                if row:
                    entry = row[0].replace("\\", "/")
                    while entry.startswith("./"):
                        entry = entry[2:]
                    paths.add(entry)
    except OSError:
        pass
    return paths


def entry_point_set(text):
    cp = configparser.ConfigParser(delimiters=("=",), strict=False, interpolation=None)
    cp.optionxform = str
    cp.read_string(text)
    out = set()
    for sec in ("console_scripts", "gui_scripts"):
        if cp.has_section(sec):
            for k, v in cp.items(sec):
                out.add((sec, k.strip(), re.sub(r"\s+", "", v)))
    return out


# ---------------------------------------------------------------------------------------------------------------------
# the eight checks. Each returns (verdict, evidence dict). Any exception is a FAILED check, never a pass.
# ---------------------------------------------------------------------------------------------------------------------
def check_1(ctx):
    fr, path = ctx["fetch"], ctx["path"]
    if fr.get("outcome") != "held":
        return rec("failed", "fetch record outcome is %r, not 'held'" % fr.get("outcome"))
    pub = fr.get("published") or {}
    want_sha, want_size = pub.get("sha256"), pub.get("size")
    if not want_sha or want_size is None:
        return rec("failed", "the fetch record does not state both published sha256 and size")
    got = sha256_file(path)
    size = os.path.getsize(path)
    same_sha = got.lower() == str(want_sha).lower()
    same_size = int(size) == int(want_size)
    detail = {"computed_sha256": got, "published_sha256": want_sha, "computed_size": size, "published_size": want_size,
              "record_held_sha256_matches_disk": str(fr.get("held_sha256", "")).lower() == got.lower()}
    if same_sha and same_size:
        return rec("passed", "re-read from disk now: sha256 and size equal the index's published values", **detail)
    return rec("failed", "disk sha256 %s size %d vs published %s size %s" % (got, size, want_sha, want_size), **detail)


def check_2(ctx):
    fr, path, file_name = ctx["fetch"], ctx["path"], ctx["file_name"]
    req = fr.get("requested") or {}
    problems = []
    if req.get("file_name") != file_name:
        problems.append("requested file_name %r != %r" % (req.get("file_name"), file_name))
    parsed = parse_wheel_name(file_name)
    if parsed is None:
        return rec("failed", "the file name is not a wheel name (5 or 6 dash-separated parts, .whl)")
    if norm_name(parsed["dist"]) != norm_name(req.get("name", "")):
        problems.append("name %r != requested %r" % (parsed["dist"], req.get("name")))
    if parsed["version"] != req.get("version"):
        problems.append("version %r != requested %r" % (parsed["version"], req.get("version")))
    for key in ("python_tag", "abi_tag", "platform_tag"):
        if parsed[key] != req.get(key):
            problems.append("%s %r != requested %r" % (key, parsed[key], req.get(key)))
    req_tags = expand_tags(str(req.get("python_tag")), str(req.get("abi_tag")), str(req.get("platform_tag")))
    with zipfile.ZipFile(path) as zf:
        di, why = wheel_dist_info(zf)
        if di is None:
            return rec("failed", why)
        meta = header_of(zf.read(di + "/METADATA").decode("utf-8", "replace"))
        wheel = header_of(zf.read(di + "/WHEEL").decode("utf-8", "replace"))
    if norm_name(meta.get("Name", "")) != norm_name(req.get("name", "")):
        problems.append("METADATA Name %r != requested %r" % (meta.get("Name"), req.get("name")))
    if meta.get("Version") != req.get("version"):
        problems.append("METADATA Version %r != requested %r" % (meta.get("Version"), req.get("version")))
    wheel_tags = set()
    for t in wheel.get_all("Tag") or []:
        bits = t.strip().split("-")
        if len(bits) == 3:
            wheel_tags |= expand_tags(*bits)
        else:
            problems.append("malformed WHEEL Tag line %r" % t)
    if wheel_tags != req_tags:
        problems.append("WHEEL Tag set %s != requested %s" % (sorted(wheel_tags), sorted(req_tags)))
    approved = ctx.get("approved_by")
    approved_line = "%s==%s" % (norm_name(req.get("name", "")), req.get("version"))
    on_list = False
    if not approved:
        problems.append("no approved list given (--approved-by); the approval line was not checked")
    else:
        try:
            with open(approved, "r", encoding="utf-8", errors="replace") as fh:
                for line in fh:
                    line = line.split("#", 1)[0].strip()
                    if "==" in line:
                        nm, _, ver = line.partition("==")
                        if norm_name(nm) == norm_name(req.get("name", "")) and ver.strip() == req.get("version"):
                            on_list = True
        except OSError as exc:
            problems.append("approved list unreadable: %s" % exc)
        if not on_list and not any(p.startswith("approved list unreadable") for p in problems):
            problems.append("no line of the approved list reads %s" % approved_line)
    detail = {"parsed_file_name": parsed, "metadata_name": meta.get("Name"), "metadata_version": meta.get("Version"),
              "wheel_tags": sorted(wheel_tags), "approved_line_sought": approved_line,
              "approved_list": os.path.basename(approved) if approved else None, "on_approved_list": on_list}
    if problems:
        return rec("failed", "; ".join(problems), problems=problems, **detail)
    return rec("passed", "file name, METADATA, WHEEL tags and the approved list all say %s" % approved_line, **detail)


def editable_source(dist_info):
    """None when the distribution is not an editable install; else the url its direct_url.json names (a string, '' if none).
    An editable install is read from <dist-info>/direct_url.json, key dir_info.editable true. Unreadable = not editable."""
    try:
        data = json.loads((dist_info / "direct_url.json").read_text(encoding="utf-8", errors="replace"))
    except (OSError, ValueError):
        return None
    di = data.get("dir_info") if isinstance(data, dict) else None
    if isinstance(di, dict) and di.get("editable") is True:
        return ascii_clean(str(data.get("url", "")))
    return None


def check_3(ctx):
    req = ctx["fetch"].get("requested") or {}
    found_all, versions = find_installed(ctx["cfg"], req.get("name", ""), req.get("version", ""))
    editable = [(f, editable_source(f["dist_info"])) for f in found_all]
    found = [f for f, src in editable if src is None]
    ed = [(f, src) for f, src in editable if src is not None]
    ctx["installed"] = found
    ctx["installed_editable"] = bool(ed)
    if not found and ed:
        reason = "the installed distribution is an editable install (source at %s), not a copy of the published files" % ed[0][1]
        return rec("not_applicable", reason, reason=reason, installed_versions=versions,
                   editable_installs=[f["dist_info_name"] for f, _ in ed])
    if not found:
        reason = "this machine holds no installed copy of %s %s (installed versions of that name: %s)" % (
            req.get("name"), req.get("version"), ", ".join(versions) if versions else "none")
        return rec("not_applicable", reason, reason=reason, installed_versions=versions)
    names = [f["dist_info_name"] for f in found]
    return rec("passed", "an installed distribution of the same name and version exists here: %s" % ", ".join(names),
               installed=names, installed_versions=versions)


def check_4(ctx):
    fr = ctx["fetch"]
    mn_age, mn_earlier = ctx["min_age"], ctx["min_earlier"]
    proj = fr.get("project") or {}
    pub = fr.get("published") or {}
    this_at = proj.get("this_release_at") or pub.get("upload_time")
    first_at, count = proj.get("first_release_at"), proj.get("release_count")
    if not this_at or not first_at or count is None:
        return rec("failed", "the fetch record lacks this_release_at, first_release_at or release_count")
    age_days = (now_utc() - parse_time(this_at)).total_seconds() / 86400.0
    earlier = int(count) - 1
    detail = {"this_release_at": this_at, "first_release_at": first_at, "release_count": count, "earlier_releases": earlier,
              "age_days": round(age_days, 2), "min_release_age_days": mn_age, "min_earlier_releases": mn_earlier,
              "yanked": pub.get("yanked")}
    problems = []
    if age_days < mn_age:
        problems.append("release is %.2f days old, below the minimum %s" % (age_days, mn_age))
    if earlier < mn_earlier:
        problems.append("%d earlier releases, below the minimum %s" % (earlier, mn_earlier))
    if problems:
        return rec("failed", "; ".join(problems), **detail)
    return rec("passed", "release %.2f days old (min %s); %d earlier releases (min %s)" % (age_days, mn_age, earlier, mn_earlier),
               **detail)


def check_5(ctx):
    att = ctx["fetch"].get("attestation")
    if isinstance(att, dict):
        state = att.get("state") or att.get("status") or att.get("value")
        url = att.get("url")
    else:
        state, url = att, ctx["fetch"].get("attestation_url")
    if state == "present":
        return rec("passed", "the index shows a build attestation for this file", attestation=state, url=url)
    if state == "absent":
        reason = "the project publishes none"
        return rec("not_applicable", reason, reason=reason, attestation=state, url=url)
    return rec("failed", "attestation read as %r (it was not read, or is not 'present'/'absent')" % (state,), attestation=state)


def _site_rel(name):
    m = re.match(r"^[^/]+\.data/(purelib|platlib)/(.*)$", name)
    return m.group(2) if m else name


def _unsafe(name):
    return name.startswith("/") or "\\" in name or re.match(r"^[A-Za-z]:", name) is not None or ".." in name.split("/")


def installed_platform_tag(inst_di):
    """The platform part of the FIRST `Tag:` line of the installed copy's own WHEEL file; None when unreadable or absent.
    Recorded by check 6 as evidence only: it never changes the verdict."""
    try:
        text = (pathlib.Path(inst_di) / "WHEEL").read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    for line in text.splitlines():
        if line.startswith("Tag:"):
            tag = line[len("Tag:"):].strip()
            return tag.rsplit("-", 1)[-1] if tag else None
    return None


# Build-metadata files that a wheel and an installed copy built on DIFFERENT platforms legitimately differ in (a file the
# package's own build writes with the build machine's compiler and flags). Adding an entry is a CTO ruling, never a worker's
# (round-27 analysis, ruling 3, ledger/ROUND_ANALYSIS.round27.md). Matched against the site-relative path.
CHECK6_BUILD_METADATA_FILES = ("numpy/__config__.py",)
DELVEWHEEL_START = b"# start delvewheel patch"
DELVEWHEEL_END = b"# end delvewheel patch"
# CTO rulings, round 28: the delvewheel block is removed together with up to DELVEWHEEL_PAD empty lines directly before it and up
# to DELVEWHEEL_PAD directly after it (msg 109671). At the seam where a block was removed from the installed copy, the run of
# empty lines is collapsed on BOTH sides, the wheel's run at the same seam included, at most DELVEWHEEL_PAD each side (msg
# 109673, which replaces the padding-only rule). Only that one seam per removed block is touched; empty lines elsewhere are
# never removed, a file with no block gets no leniency, and a non-empty line at a seam is never removed.
DELVEWHEEL_PAD = 4


def _platform_lines(data):
    """CRLF to LF, then the lines; the final newline of the file is not a line. Returns (lines, trailing_newline)."""
    lines = data.replace(b"\r\n", b"\n").split(b"\n")
    trailing = lines[-1] == b""
    return (lines[:-1] if trailing else lines), trailing


def _join_lines(lines, trailing):
    return b"\n".join(lines) + (b"\n" if trailing else b"")


def _remove_blocks(lines):
    """Remove every delvewheel block: from a line containing the start marker through the first following line containing the
    end marker (both included), together with up to DELVEWHEEL_PAD empty lines directly before and up to DELVEWHEEL_PAD directly
    after. A start with no end after it is not a block and is left as it is. Returns (kept lines, seams): one seam per removed
    block, the number of non-empty kept lines before that block."""
    out, seams, nonempty, i = [], [], 0, 0
    while i < len(lines):
        if DELVEWHEEL_START in lines[i]:
            end = next((j for j in range(i, len(lines)) if DELVEWHEEL_END in lines[j]), None)
            if end is not None:
                for _ in range(DELVEWHEEL_PAD):      # up to DELVEWHEEL_PAD empty lines directly before the block
                    if out and out[-1] == b"":
                        out.pop()
                    else:
                        break
                seams.append(nonempty)
                i = end + 1
                for _ in range(DELVEWHEEL_PAD):      # up to DELVEWHEEL_PAD empty lines directly after the block
                    if i < len(lines) and lines[i] == b"":
                        i += 1
                    else:
                        break
                continue
        out.append(lines[i])
        if lines[i] != b"":
            nonempty += 1
        i += 1
    return out, seams


def _collapse_seam(lines, seam):
    """The run of empty lines at a seam on a side that carries no block there: the run that follows the seam-th non-empty line
    (the start of the file when seam is 0). Up to DELVEWHEEL_PAD empty lines are dropped from its start and up to DELVEWHEEL_PAD
    from its end; the lines between them stay. A seam the lines do not reach changes nothing."""
    start = 0
    if seam:
        seen = 0
        for idx, ln in enumerate(lines):
            if ln != b"":
                seen += 1
                if seen == seam:
                    start = idx + 1
                    break
        else:
            return lines
    end = start
    while end < len(lines) and lines[end] == b"":
        end += 1
    width = end - start
    head = min(width, DELVEWHEEL_PAD)
    tail = min(width - head, DELVEWHEEL_PAD)
    return lines[:start] + lines[start + head:end - tail] + lines[end:]


def _platform_rule(rel, held_bytes, inst_bytes):
    """Check 6's platform rule for ONE differing .py file of a cross-platform comparison: 'equal' when the two sides are equal
    after the platform normalisation (CRLF to LF, delvewheel blocks removed, the empty-line run at each block's seam collapsed
    on both sides), 'build' when they differ and the site-relative path is a listed build-metadata file, else None (a residual
    difference that still fails check 6)."""
    held_lines, held_nl = _platform_lines(held_bytes)
    inst_lines, inst_nl = _platform_lines(inst_bytes)
    held_out, held_seams = _remove_blocks(held_lines)
    inst_out, inst_seams = _remove_blocks(inst_lines)
    # a seam the other side carries is collapsed here too; a seam both sides carry is collapsed by each side's own block removal
    for seam in sorted(set(inst_seams) - set(held_seams)):
        held_out = _collapse_seam(held_out, seam)
    for seam in sorted(set(held_seams) - set(inst_seams)):
        inst_out = _collapse_seam(inst_out, seam)
    if _join_lines(held_out, held_nl) == _join_lines(inst_out, inst_nl):
        return "equal"
    if rel in CHECK6_BUILD_METADATA_FILES:
        return "build"
    return None


def check_6(ctx):
    if not ctx.get("installed"):
        reason = ("check 3 was not applicable: the installed distribution is an editable install, not a copy of the published files"
                  if ctx.get("installed_editable") else
                  "check 3 was not applicable: no installed copy of this version to compare with")
        return rec("not_applicable", reason, reason=reason)
    inst = ctx["installed"][0]
    site_dir, inst_di = inst["site"], inst["dist_info"]
    inst_record = installed_record_paths(inst_di)
    record_readable = bool(inst_record)       # no readable (or an empty) RECORD: no listing to separate missing from extra
    inst_record_base = {p.rsplit("/", 1)[-1].lower() for p in inst_record}
    try:
        inst_eps = entry_point_set((inst_di / "entry_points.txt").read_text(encoding="utf-8", errors="replace"))
    except OSError:
        inst_eps = set()
    py_total = py_ident = 0
    py_diff, py_missing, py_extra, compiled, hooks_new, hooks_old, unsafe = [], [], [], [], [], [], []
    crlf_only = []
    # py_diff = every byte-different .py (the raw count); py_residual = those the platform rule does not clear (the verdict)
    platform_equal, build_meta, py_residual = [], [], []
    installed_plat = installed_platform_tag(inst_di)
    held_plat = (parse_wheel_name(ctx["file_name"]) or {}).get("platform_tag")
    cross = bool(installed_plat and held_plat and installed_plat != held_plat)
    with zipfile.ZipFile(ctx["path"]) as zf:
        infos = [i for i in zf.infolist() if not i.is_dir()]
        for info in infos:
            n = info.filename
            low = n.lower()
            if _unsafe(n):
                unsafe.append(n)
                continue
            if low.endswith(COMPILED_SUFFIXES):
                compiled.append(n)
            in_scripts = re.match(r"^[^/]+\.data/scripts/.+", n) is not None
            if in_scripts:
                base = n.rsplit("/", 1)[-1].lower()
                known = base in inst_record_base or (base + ".exe") in inst_record_base
                (hooks_old if known else hooks_new).append(n)
            rel = _site_rel(n)
            if low.endswith(".pth") or rel.lower() in ("sitecustomize.py", "usercustomize.py"):
                target = site_dir / rel
                same = False
                if target.is_file():
                    same = target.read_bytes() == zf.read(info)
                (hooks_old if same else hooks_new).append(n)
            if low.endswith(".py"):
                py_total += 1
                if re.match(r"^[^/]+\.data/(scripts|headers|data)/", n):
                    py_diff.append(n)
                    py_residual.append(n)     # never cleared by the platform rule
                    continue
                target = site_dir / rel
                if not target.is_file():
                    # absent on disk: the installed copy's own RECORD separates a file its install wrote and lost (missing)
                    # from a file it never wrote (extra); with no readable RECORD every absent file is extra
                    if record_readable and rel in inst_record:
                        py_missing.append(n)
                    else:
                        py_extra.append(n)
                elif info.file_size > MAX_PY_BYTES:
                    py_diff.append(n)
                    py_residual.append(n)     # over-size files are never cleared by the platform rule
                else:
                    held_bytes, inst_bytes = zf.read(info), target.read_bytes()
                    if inst_bytes == held_bytes:
                        py_ident += 1
                    else:
                        py_diff.append(n)
                        if inst_bytes.replace(b"\r\n", b"\n") == held_bytes.replace(b"\r\n", b"\n"):
                            crlf_only.append(n)   # recorded only: the verdict is decided by py_residual
                        decided = _platform_rule(rel, held_bytes, inst_bytes) if cross else None
                        if decided == "equal":
                            platform_equal.append(n)
                        elif decided == "build":
                            build_meta.append(n)
                        else:
                            py_residual.append(n)
        di, _ = wheel_dist_info(zf)
        wheel_eps = set()
        if di and (di + "/entry_points.txt") in zf.namelist():
            wheel_eps = entry_point_set(zf.read(di + "/entry_points.txt").decode("utf-8", "replace"))
    for ep in sorted(wheel_eps):
        label = "entry_point %s:%s = %s" % ep
        (hooks_old if ep in inst_eps else hooks_new).append(label)
    compared = py_ident + len(py_diff)
    detail = {"installed_copy": "<site-packages>/" + inst["dist_info_name"], "py_in_wheel": py_total, "py_identical": py_ident,
              "py_compared": compared, "py_missing_count": len(py_missing), "py_missing": py_missing,
              "py_extra_count": len(py_extra), "py_extra": py_extra, "installed_record_readable": record_readable,
              "py_differing_count": len(py_diff), "py_differing": py_residual, "compiled_count": len(compiled), "compiled": compiled,
              "py_differing_after_platform_rules": len(py_residual),
              "platform_normalised_equal": platform_equal, "build_metadata_residual": build_meta,
              "differ_after_crlf_normalisation": len(py_diff) - len(crlf_only),
              "compared_across_platforms": cross,
              "installed_platform": installed_plat, "held_platform": held_plat,
              "hooks_only_in_wheel": hooks_new, "hooks_also_in_installed_copy": hooks_old, "unsafe_member_names": unsafe}
    counts = "compared=%d missing=%d extra=%d differ=%d" % (compared, len(py_missing), len(py_extra), len(py_residual))
    absent = len(py_missing) + len(py_extra)
    # nothing present to compare, and (no readable RECORD, or nothing the RECORD fails to list): not applicable
    if py_total and absent == py_total and not unsafe and (not record_readable or not py_extra):
        reason = "no installed file to compare (0 of %d present)" % py_total
        return rec("not_applicable", reason, reason=reason, **detail)
    problems = []
    if py_extra:
        problems.append("%s: %d .py file(s) in the wheel that the installed copy never had: %s" % (counts, len(py_extra), cap(py_extra)))
    if py_residual:
        problems.append("%s: %d of %d .py files differ from the installed copy: %s" % (
            counts, len(py_residual), py_total, cap(py_residual)))
    if hooks_new:
        problems.append("installer/script/start-up hook(s) not in the installed copy: %s" % cap(hooks_new))
    if unsafe:
        problems.append("unsafe member name(s): %s" % cap(unsafe))
    if problems:
        return rec("failed", "; ".join(problems), **detail)
    cleared = ""
    if platform_equal or build_meta:
        cleared = "; platform-normalised-equal=%d build-metadata-residual=%d" % (len(platform_equal), len(build_meta))
    return rec("passed", "%d of %d .py files byte-identical (%s); %d compiled file(s) named; no new hook%s" % (
        py_ident, py_total, counts, len(compiled), cleared), **detail)


def _ascii_name(text):
    """A display name reduced to printable ASCII: every other character becomes '?'. Returns (clean, replaced?)."""
    clean = "".join(ch if 32 <= ord(ch) < 127 else "?" for ch in str(text))
    return clean, clean != str(text)


def decode_state(state):
    """Decode a Security Center productState by its documented bytes. Returns a dict: state, hex, realtime (on|off|unknown),
    definitions (current|out_of_date|unknown). A byte value outside those known decodes to 'unknown', never on or current."""
    s = int(state)
    if not 0 <= s <= 0xFFFFFF:
        return {"state": s, "hex": "0x%X" % s, "realtime": "unknown", "definitions": "unknown"}
    mid, last = (s >> 8) & 0xFF, s & 0xFF
    rt = "on" if mid in (0x10, 0x11) else "off" if mid in (0x00, 0x01) else "unknown"
    df = "current" if last == 0x00 else "out_of_date" if last == 0x10 else "unknown"
    return {"state": s, "hex": "0x%06X" % s, "realtime": rt, "definitions": df}


def parse_av_answer(text):
    """The JSON the Security Center query prints: one object, a list of objects, or nothing. Returns a list of product dicts."""
    text = (text or "").strip()
    if not text:
        return []
    data = json.loads(text)
    if isinstance(data, dict):
        data = [data]
    if not isinstance(data, list):
        raise ValueError("the answer is neither an object nor a list")
    out = []
    for item in data:
        if not isinstance(item, dict) or "displayName" not in item or "productState" not in item:
            raise ValueError("an entry lacks displayName or productState: %r" % (item,))
        ps = item["productState"]
        if isinstance(ps, bool) or not isinstance(ps, (int, str)):
            raise ValueError("productState is not a number: %r" % (ps,))
        name, replaced = _ascii_name(item["displayName"])
        row = {"display_name": name, "name_non_ascii_replaced": replaced}
        row.update(decode_state(ps))
        out.append(row)
    return out


def read_security_center(cfg):
    """Read the antivirus registrations. Returns (products, error): error is '' when the read worked (products may be empty).
    READ-ONLY: a PowerShell query of root/SecurityCenter2 AntiVirusProduct, 30-second bound, or the file OPAL_INTAKE_AV_JSON."""
    if cfg.av_json:
        try:
            with open(cfg.av_json, "r", encoding="utf-8-sig") as fh:
                return parse_av_answer(fh.read()), ""
        except (OSError, ValueError) as exc:
            return [], "the stand-in answer %s is unreadable: %s: %s" % (os.path.basename(str(cfg.av_json)), type(exc).__name__, exc)
    ps = shutil.which("powershell") or shutil.which("powershell.exe") or shutil.which("pwsh")
    if not ps:
        return [], "powershell was not found on this machine"
    cmd = ("Get-CimInstance -Namespace root/SecurityCenter2 -ClassName AntiVirusProduct -ErrorAction Stop | "
           "Select-Object displayName, productState | ConvertTo-Json -Compress")
    try:
        proc = subprocess.run([ps, "-NoProfile", "-NonInteractive", "-Command", cmd], capture_output=True,
                              timeout=AV_QUERY_TIMEOUT, stdin=subprocess.DEVNULL)
    except subprocess.TimeoutExpired:
        return [], "the Security Center query did not finish within %d seconds" % AV_QUERY_TIMEOUT
    except OSError as exc:
        return [], "the Security Center query could not start: %s" % exc
    out = (proc.stdout or b"").decode("utf-8", "replace")
    if proc.returncode != 0:
        err = (proc.stderr or b"").decode("utf-8", "replace").strip().splitlines()
        return [], "the Security Center query exited %d: %s" % (proc.returncode, ascii_clean(err[0][:200]) if err else "no message")
    try:
        return parse_av_answer(out), ""
    except (ValueError, TypeError) as exc:
        return [], "the Security Center answer could not be parsed: %s: %s" % (type(exc).__name__, exc)


def is_scan_copy(file_name):
    return str(file_name).endswith(SCAN_COPY_SUFFIX)


def _file_state(path, want_sha):
    """'unchanged' | 'changed' | 'missing' | 'unreadable: ...' for one file against the expected SHA-256."""
    try:
        if not os.path.isfile(path):
            return "missing"
        return "unchanged" if sha256_file(path) == want_sha else "changed"
    except OSError as exc:
        return "unreadable: %s" % exc


def on_access_read(path, wait, hook=None):
    """Write a copy of the held file beside it, read the copy back fully, wait, then re-read BOTH and compare each with the held
    file's hash from before. The copy is ALWAYS removed in the finally. `hook(path, copy)` is called at the start of the wait
    (tests use it to change a file or remove the copy). Returns a dict of what was seen; never raises for a file problem."""
    path = pathlib.Path(path)
    copy = path.with_name(path.name + SCAN_COPY_SUFFIX)
    r = {"copy_name": copy.name, "stale_copy_removed": False, "problems": [], "held_after": None, "copy_after": None,
         "copy_cleanup": None}
    try:
        if copy.exists():
            copy.unlink()
            r["stale_copy_removed"] = True
        before = sha256_file(path)
        r["held_sha256_before"] = before
        with open(path, "rb") as src, open(copy, "xb") as dst:
            shutil.copyfileobj(src, dst, 1 << 20)
            dst.flush()
            os.fsync(dst.fileno())
        r["copy_sha256_readback"] = sha256_file(copy)
        if r["copy_sha256_readback"] != before:
            r["problems"].append("the copy read back differently from the held file")
        if hook is not None:
            hook(path, copy)
        if wait > 0:
            time.sleep(wait)
        r["held_after"] = _file_state(path, before)
        r["copy_after"] = _file_state(copy, before)
    except Exception as exc:  # the read could not be made: a failed check, never a pass
        r["problems"].append("the on-access read could not be made: %s: %s" % (type(exc).__name__, exc))
    finally:
        try:
            if copy.exists():
                copy.unlink()
                r["copy_cleanup"] = "removed"
            else:
                r["copy_cleanup"] = "already gone before cleanup"
        except OSError as exc:
            r["copy_cleanup"] = "REMOVAL REFUSED: %s" % exc
    return r


def check_7(ctx):
    cfg = ctx["cfg"]
    wait = int(ctx.get("scan_wait", DEFAULT_SCAN_WAIT))
    products, err = read_security_center(cfg)
    base = {"decoding": DECODING_NOTE, "scan_wait_seconds": wait, "limit": LIMIT_SENTENCE}
    if err:
        return rec("failed", "the Security Center antivirus registrations could not be read: %s" % err, query_failed=True, **base)
    base["products"] = products
    base["products_count"] = len(products)
    active = [p for p in products if p["realtime"] == "on"]
    base["active"] = [p["display_name"] for p in active]
    if not active:
        return rec("failed", "no antivirus product is registered as on (%d registered: %s)" % (
            len(products), "; ".join("%s %s realtime=%s" % (p["display_name"], p["hex"], p["realtime"]) for p in products) or "none"),
            **base)
    stale = [p for p in active if p["definitions"] != "current"]
    if stale:
        return rec("failed", "active product(s) whose definitions are not current: %s" % "; ".join(
            "%s %s definitions=%s" % (p["display_name"], p["hex"], p["definitions"]) for p in stale), **base)
    got = on_access_read(ctx["path"], wait, ctx.get("wait_hook"))
    base.update(got)
    bad = list(got["problems"])
    if got["held_after"] not in (None, "unchanged"):
        bad.append("the held file is %s after the wait" % got["held_after"])
    if got["copy_after"] not in (None, "unchanged"):
        bad.append("the scan copy is %s after the wait%s" % (
            got["copy_after"], " (a product that removed it has given a verdict)" if got["copy_after"] == "missing" else ""))
    if str(got["copy_cleanup"]).startswith("REMOVAL REFUSED"):
        bad.append("the scan copy could not be removed afterwards: %s" % got["copy_cleanup"])
    if bad:
        return rec("failed", "; ".join(bad), **base)
    names = "; ".join(p["display_name"] for p in active)
    return rec("passed", "on-access scan by %s, state enabled and current; file present and unchanged after %d s; "
               "no on-demand verdict available" % (names, wait), **base)


def _git_author(path):
    try:
        out = subprocess.run(["git", "log", "-1", "--format=%an", "--", str(path)], cwd=str(REPO_ROOT),
                             capture_output=True, timeout=30, stdin=subprocess.DEVNULL)
        text = out.stdout.decode("utf-8", "replace").strip()
        return ascii_clean(text) if text else "not committed"
    except Exception:
        return "unread"


SIGN_MARKERS = ("CHECK 8 SIGNED", "SIGNED, check 8")


def has_sign_marker(text):
    """True when some line, once markdown emphasis, backticks, dashes-as-bullets and spaces are stripped from its start, BEGINS
    with one of SIGN_MARKERS (case-sensitive). A phrase met mid-sentence (e.g. 'It is NOT check 8') is not a marker."""
    for line in text.splitlines():
        lead = line.lstrip(" 	*`_#>-").rstrip()
        if any(lead.startswith(m) for m in SIGN_MARKERS):
            return True
    return False


WAIVABLE_CHECKS = (3, 4, 5, 6, 7)      # checks 1 and 2 (digest, identity) are never waivable; check 8 is the waiver itself
WAIVE_RE = re.compile(r"^WAIVE (\S+) check ([0-9]+):(?: (.*))?$")   # no text after the colon reads as an empty reason


def parse_waivers(text, file_name):
    """The WAIVE lines of a signed check-8 file that name THIS file exactly. A line reads, after the same leading markdown
    stripping has_sign_marker uses, `WAIVE <file name> check <N>: <reason>` (case-sensitive; no wildcard, no batch form).
    Returns (waivers, refused, ignored): waivers = [{check, reason}] for checks 3 to 7; refused = the same for checks 1 and 2
    (check 8 then reads failed); ignored = {check, reason, why} for check 8, a number outside 1 to 7, or an empty reason."""
    waivers, refused, ignored = [], [], []
    for line in text.splitlines():
        lead = line.lstrip(" \t*`_#>-").rstrip()
        m = WAIVE_RE.match(lead)
        if m is None or m.group(1) != file_name:
            continue
        n = int(m.group(2))
        reason = (m.group(3) or "").strip().rstrip("*`_").strip()
        if not reason:
            ignored.append({"check": n, "reason": "", "why": "empty reason"})
        elif n in WAIVABLE_CHECKS:
            waivers.append({"check": n, "reason": reason})
        elif n in (1, 2):
            refused.append({"check": n, "reason": reason})
        else:
            ignored.append({"check": n, "reason": reason, "why": "check 8 is the waiver itself" if n == 8 else
                            "not a check number 1 to 7"})
    return waivers, refused, ignored


def check_8(ctx):
    signed = ctx.get("signed_by")
    if not signed:
        return "unsigned", {"summary": "no --signed-by given: nobody has signed this file", "signer": None, "path": None}
    cfg = ctx["cfg"]
    base = cfg.signer_dir if cfg.signer_dir else REPO_ROOT / DEFAULT_SIGNER_REL
    p = pathlib.Path(signed)
    if not p.is_absolute():
        p = REPO_ROOT / p
    try:
        rp, rb = p.resolve(), base.resolve()
    except OSError as exc:
        return rec("failed", "signature path unresolvable: %s" % exc)
    if rb not in rp.parents:
        return rec("failed", "the signature file is not under the required directory %s" % (
            DEFAULT_SIGNER_REL if cfg.signer_dir is None else "<OPAL_INTAKE_SIGNER_DIR>"))
    if not rp.is_file():
        # the CTO's signature has not been written yet: a recorded state of its own, never a failed check
        return rec("awaiting", "check 8 awaits the signature: the signature file does not exist", signer=None, path=None)
    approved = ctx.get("approved_by")
    if approved:
        ap = pathlib.Path(approved)
        if not ap.is_absolute():
            ap = REPO_ROOT / ap
        try:
            if ap.is_file() and (ap.resolve() == rp or sha256_file(ap) == sha256_file(rp)):
                return rec("failed", "the signature file is the --approved-by file (same path or same content): an approval "
                           "to fetch is not a signature")
        except OSError as exc:
            return rec("failed", "the signature file could not be compared with the --approved-by file: %s" % exc)
    text = rp.read_text(encoding="utf-8", errors="replace")
    miss = [what for what, s in (("batch id", ctx["batch"]), ("file name", ctx["file_name"])) if s not in text]
    if miss:
        return rec("failed", "the signature file's text does not contain the %s" % " and the ".join(miss))
    if not has_sign_marker(text):
        return rec("failed", "the signature file has no line beginning 'CHECK 8 SIGNED' or 'SIGNED, check 8'")
    # the waivers: a waiver line counts only in a file that has passed every rule above (the CHECK 8 SIGNED marker included)
    waivers, refused, ignored = parse_waivers(text, ctx["file_name"])
    if refused:
        return rec("failed", "the signature file waives check %s for this file: checks 1 and 2 (the digest and the identity "
                   "of the file) can never be waived" % ", ".join(str(w["check"]) for w in refused),
                   signer=None, path=None, waivers=waivers, refused_waivers=refused, ignored_waivers=ignored)
    npm_extra = {}
    if ctx.get("ecosystem") == "npm":
        # CT-cc-1: a tarball that lists a lifecycle script or names a native binary needs ITS OWN line in this file
        err, required = npm_required_lines(ctx)
        if err:
            return rec("failed", "check 8 cannot know which lines this tarball needs: %s" % err, signer=None, path=None)
        have = parse_npm_lines(text, ctx["file_name"])
        absent = [k for k in required if not have[k]]
        if absent:
            need = "; ".join("`%s <file name>: <reason>`" % k for k in absent)
            return rec("failed", "the signature file has no line for this file that the archive requires (it lists a lifecycle "
                       "script or names a native binary): missing %s" % need,
                       signer=None, path=None, npm_required=required, npm_lines={k: len(v) for k, v in have.items()})
        npm_extra = {"npm_required": required, "npm_lines": {k: len(v) for k, v in have.items()}}
    if cfg.signer_dir is None:
        rel = rp.relative_to(REPO_ROOT.resolve()).as_posix()
        parts = rel.split("/")
        signer = parts[2] if len(parts) > 3 and parts[0] == "org" and parts[1] == "tier1_exec" else "unknown"
        author = _git_author(rp)
    else:
        rel = rp.name
        signer = "override-dir:" + rb.name
        author = "not read (override dir)"
    summary = "signature file names the batch and the file and carries the signing line"
    if waivers:
        summary += "; waives check %s for this file" % ", ".join(str(w["check"]) for w in waivers)
    return rec("passed", summary, signer=signer, path=rel,
               signature_file_sha256=sha256_bytes(rp.read_bytes()), signature_file_git_author=author,
               waivers=waivers, ignored_waivers=ignored, **npm_extra)


# ---------------------------------------------------------------------------------------------------------------------
# the npm limb (CT-cc-1; the CTO ruling of 2026-10-16). Each check takes the place of the wheel check it replaces, with the
# same record shape and verdict vocabulary. A tarball is read IN MEMORY (tarfile, mode r:gz); nothing is extracted to disk
# and no lifecycle script is run. Checks 1 and 2 are never waivable (WAIVABLE_CHECKS is unchanged).
# ---------------------------------------------------------------------------------------------------------------------
NPM_EXT = ".tgz"
NPM_EXPANDED_CAP = 200 * 1024 * 1024        # the declared sizes of the members, summed: over this is a tarball bomb
NPM_MEMBER_CAP = 20000                      # over this many members is a tarball bomb
NPM_PKG_JSON_CAP = 5 * 1024 * 1024          # package/package.json is read whole only below this size
NPM_LIFECYCLE_KEYS = ("preinstall", "install", "postinstall", "prepare")
NPM_NATIVE_SUFFIXES = (".node", ".exe", ".dll", ".so", ".dylib")
NPM_NAME_RE = re.compile(r"^(?:@[a-z0-9][a-z0-9._-]*/)?[a-z0-9][a-z0-9._-]*$")
NPM_VERSION_RE = re.compile(r"^[0-9A-Za-z][0-9A-Za-z.+-]*$")
NPM_LINE_RE = re.compile(r"^(NATIVE|LIFECYCLE) (\S+): (.*)$")   # the check-8 lines an npm tarball needs


def npm_held_name(name, version):
    """The held file name (page section 1a), taken from intake_fetch.npm_held_name by path, never copied."""
    here = os.path.dirname(os.path.abspath(__file__))
    if here not in sys.path:
        sys.path.insert(0, here)
    import intake_fetch  # noqa: E402  (stdlib-only module beside this file)
    return intake_fetch.npm_held_name(name, version)


def _file_digest(path, algo):
    h = hashlib.new(algo)
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h


def npm_strip_trailing_commas(text):
    """bun writes its text lockfile as JSON with trailing commas. Each comma followed (after whitespace) by a closing brace or
    bracket is dropped, outside strings only; nothing else changes."""
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


def load_bun_lock(path):
    """The bun TEXT lockfile as a dict with a packages object. Raises ValueError or OSError when it is not one."""
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    data = json.loads(npm_strip_trailing_commas(text))
    if not isinstance(data, dict) or not isinstance(data.get("packages"), dict):
        raise ValueError("the lockfile has no packages object")
    return data


def lock_integrities(lock, ident):
    """The distinct integrity strings of the packages entries whose first element is ident (name@version). An entry is
    [ident, registry, {deps}, integrity]; a missing fourth element reads as None."""
    found = []
    for _key, val in lock["packages"].items():
        if isinstance(val, list) and val and val[0] == ident:
            integ = val[3] if len(val) > 3 and isinstance(val[3], str) else None
            if integ not in found:
                found.append(integ)
    return found


def _unsafe_member(name):
    if not name or name.startswith("/") or "\\" in name or re.match(r"^[A-Za-z]:", name) is not None:
        return True
    return ".." in name.split("/")


def _link_escapes(base_dir, target):
    t = str(target).replace("\\", "/")
    if not t or t.startswith("/") or re.match(r"^[A-Za-z]:", t) is not None:
        return True
    joined = posixpath.normpath(posixpath.join(base_dir, t))
    return joined == ".." or joined.startswith("../") or joined.startswith("/")


def npm_listing(path):
    """Read the tarball's members IN MEMORY. Returns the listing dict; error is None or a reason (not gzip, a bomb, empty)."""
    out = {"members": 0, "expanded_bytes": 0, "unsafe": [], "error": None, "package_json": None,
           "package_json_error": None, "lifecycle": [], "lifecycle_commands": {}, "native_members": [], "restricted": None}
    try:
        with tarfile.open(str(path), "r:gz") as tf:
            for m in tf:
                out["members"] += 1
                if out["members"] > NPM_MEMBER_CAP:
                    out["error"] = "more than %d members: refused as a tarball bomb" % NPM_MEMBER_CAP
                    break
                out["expanded_bytes"] += max(int(m.size), 0)
                if out["expanded_bytes"] > NPM_EXPANDED_CAP:
                    out["error"] = "more than %d bytes expanded: refused as a tarball bomb" % NPM_EXPANDED_CAP
                    break
                name = m.name
                if m.issym() or m.islnk():
                    base_dir = posixpath.dirname(name) if m.issym() else ""
                    if _unsafe_member(name) or _link_escapes(base_dir, m.linkname):
                        out["unsafe"].append(name)
                elif not (m.isreg() or m.isdir()) or _unsafe_member(name):
                    out["unsafe"].append(name)
                elif m.isreg():
                    if name.lower().endswith(NPM_NATIVE_SUFFIXES):
                        out["native_members"].append(name)
                    if name == "package/package.json":
                        if m.size > NPM_PKG_JSON_CAP:
                            out["package_json_error"] = "package/package.json is larger than %d bytes" % NPM_PKG_JSON_CAP
                        else:
                            _npm_package_json(tf.extractfile(m).read(), out)
        if out["members"] == 0 and out["error"] is None:
            out["error"] = "the archive holds no members"
    except (tarfile.TarError, OSError, EOFError, zlib.error, ValueError) as exc:
        out["error"] = "not a readable gzip tar (%s)" % type(exc).__name__
    return out


def _npm_package_json(data, out):
    try:
        pkg = json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, ValueError):
        out["package_json_error"] = "package/package.json is not readable JSON"
        return
    if not isinstance(pkg, dict):
        out["package_json_error"] = "package/package.json is not a JSON object"
        return
    out["package_json"] = pkg
    scripts = pkg.get("scripts") if isinstance(pkg.get("scripts"), dict) else {}
    for key in NPM_LIFECYCLE_KEYS:
        if key in scripts:
            out["lifecycle"].append(key)
            out["lifecycle_commands"][key] = ascii_clean(str(scripts[key]))[:200]
    restr = {k: pkg[k] for k in ("os", "cpu") if isinstance(pkg.get(k), list) and pkg.get(k)}
    if restr:
        out["restricted"] = restr


def npm_named_native(listing):
    """The native binaries the record NAMES: every native member, and the package itself when its os or cpu is restricted."""
    named = sorted(set(listing["native_members"]))
    if listing["restricted"]:
        named.append("package/package.json os/cpu restriction: %s" % ", ".join(sorted(listing["restricted"])))
    return named


def _npm_listing(ctx):
    if "_npm_listing" not in ctx:
        ctx["_npm_listing"] = npm_listing(ctx["path"])
    return ctx["_npm_listing"]


def npm_required_lines(ctx):
    """(error or None, the check-8 line kinds this tarball needs). An archive that cannot be read gives an error: the lines it
    would need cannot be known, so check 8 reads failed rather than passed."""
    listing = _npm_listing(ctx)
    if listing["error"]:
        return listing["error"], []
    need = []
    if listing["lifecycle"]:
        need.append("LIFECYCLE")
    if npm_named_native(listing):
        need.append("NATIVE")
    return None, need


def parse_npm_lines(text, file_name):
    """The NATIVE and LIFECYCLE lines that name THIS file: {'NATIVE': [reason...], 'LIFECYCLE': [reason...]}. A line reads, after
    the markdown stripping of parse_waivers, `NATIVE <file name>: <reason>`; an empty reason is not a line."""
    out = {"NATIVE": [], "LIFECYCLE": []}
    for line in text.splitlines():
        lead = line.lstrip(" \t*`_#>-").rstrip()
        m = NPM_LINE_RE.match(lead)
        if m is None or m.group(2) != file_name:
            continue
        reason = (m.group(3) or "").strip().rstrip("*`_").strip()
        if reason:
            out[m.group(1)].append(reason)
    return out


def check_1_npm(ctx):
    """digest: the tarball's sha512 equals the registry document's dist.integrity AND the lockfile's integrity for name@version
    (two independent sources). dist.shasum (sha1) is compared as well when the registry publishes one."""
    fr, path = ctx["fetch"], ctx["path"]
    if fr.get("outcome") != "held":
        return rec("failed", "fetch record outcome is %r, not 'held'" % fr.get("outcome"))
    pub = fr.get("published") or {}
    req = fr.get("requested") or {}
    reg = pub.get("integrity")
    if not isinstance(reg, str) or not reg.startswith("sha512-"):
        return rec("failed", "the fetch record holds no sha512 dist.integrity from the registry document")
    if not ctx.get("lockfile"):
        return rec("failed", "no --lockfile given: npm refuses to check a tarball against one source alone (a refusal, never a skip)")
    ident = "%s@%s" % (req.get("name", ""), req.get("version", ""))
    try:
        lock = load_bun_lock(ctx["lockfile"])
    except (OSError, ValueError) as exc:
        return rec("failed", "the lockfile is unreadable: %s: %s" % (type(exc).__name__, exc))
    found = lock_integrities(lock, ident)
    got = "sha512-" + base64.b64encode(_file_digest(path, "sha512").digest()).decode("ascii")
    sha256 = _file_digest(path, "sha256").hexdigest()
    sha1 = _file_digest(path, "sha1").hexdigest()
    shasum = pub.get("shasum")
    detail = {"computed_sha512": got, "registry_integrity": reg, "lockfile": os.path.basename(ctx["lockfile"]),
              "lockfile_ident": ident, "lockfile_entries": len(found), "lockfile_integrity": found[0] if len(found) == 1 else None,
              "computed_sha256": sha256, "computed_sha1": sha1, "registry_shasum": shasum,
              "record_held_sha256_matches_disk": str(fr.get("held_sha256", "")).lower() == sha256.lower()}
    problems = []
    if got != reg:
        problems.append("disk sha512 differs from the registry document's dist.integrity")
    if len(found) != 1 or found[0] is None:
        problems.append("the lockfile holds %d integrity entr%s for %s" % (len(found), "y" if len(found) == 1 else "ies", ident))
    elif found[0] != got:
        problems.append("disk sha512 differs from the lockfile's integrity for %s" % ident)
    if isinstance(shasum, str) and shasum.lower() != sha1:
        problems.append("disk sha1 differs from the registry document's dist.shasum")
    if problems:
        return rec("failed", "; ".join(problems), problems=problems, **detail)
    return rec("passed", "re-read from disk now: sha512 equals the registry document's dist.integrity AND the lockfile's "
               "integrity for %s" % ident, **detail)


def check_2_npm(ctx):
    """identity: the file name is the held name of the request, package/package.json names the requested name and version,
    and the approved list has the exact line name@version."""
    fr, file_name = ctx["fetch"], ctx["file_name"]
    req = fr.get("requested") or {}
    name, version = req.get("name", ""), req.get("version", "")
    problems = []
    if not (isinstance(name, str) and NPM_NAME_RE.match(name)):
        problems.append("requested name %r is not an npm package name" % (name,))
    if not (isinstance(version, str) and NPM_VERSION_RE.match(version)):
        problems.append("requested version %r is not an npm version" % (version,))
    want_file = npm_held_name(str(name), str(version))
    if req.get("file_name") != file_name:
        problems.append("requested file_name %r != %r" % (req.get("file_name"), file_name))
    if file_name != want_file:
        problems.append("file name %r is not the held name %r" % (file_name, want_file))
    listing = _npm_listing(ctx)
    pkg = listing["package_json"]
    if listing["error"]:
        problems.append("the archive cannot be read: %s" % listing["error"])
    elif pkg is None:
        problems.append("package/package.json is absent or unreadable (%s)" % (listing["package_json_error"] or "absent"))
    else:
        if pkg.get("name") != name:
            problems.append("package.json name %r != requested %r" % (pkg.get("name"), name))
        if pkg.get("version") != version:
            problems.append("package.json version %r != requested %r" % (pkg.get("version"), version))
    ident = "%s@%s" % (name, version)
    approved = ctx.get("approved_by")
    on_list = False
    if not approved:
        problems.append("no approved list given (--approved-by); the approval line was not checked")
    else:
        try:
            with open(approved, "r", encoding="utf-8", errors="replace") as fh:
                for line in fh:
                    line = line.split("#", 1)[0].strip()
                    nm, sep, ver = line.rpartition("@")
                    if sep and nm and nm == name and ver == version:
                        on_list = True
        except OSError as exc:
            problems.append("approved list unreadable: %s" % exc)
        if not on_list and not any(p.startswith("approved list unreadable") for p in problems):
            problems.append("no line of the approved list reads %s" % ident)
    detail = {"requested_name": name, "requested_version": version, "ident": ident, "file_name_expected": want_file,
              "package_json_name": pkg.get("name") if pkg else None, "package_json_version": pkg.get("version") if pkg else None,
              "approved_line_sought": ident, "approved_list": os.path.basename(approved) if approved else None,
              "on_approved_list": on_list}
    if problems:
        return rec("failed", "; ".join(problems), problems=problems, **detail)
    return rec("passed", "file name, package/package.json and the approved list all say %s" % ident, **detail)


def check_3_npm(ctx):
    reason = ("npm tarball: check 3 reads the Python site-packages of this machine, and this route installs no npm package "
              "into them")
    return rec("not_applicable", reason, reason=reason)


def check_4_npm(ctx):
    """release age (CT-cc-1 addendum 3, the CTO ruling of 2026-10-16): the publish time is time[<version>] of the registry
    packument, which the fetch read and recorded as the project facts; the earlier releases are the packument's other
    versions. The same rule and the same evidence as check 4 for PyPI: nothing here is waived."""
    verdict, ev = check_4(ctx)
    ev["release_age_source"] = "registry packument time[<version>] (the packument read by the fetch, same host)"
    return verdict, ev


def check_6_npm(ctx):
    """the archive listed, never installed: unsafe member names and links, a bomb, a non-gzip file FAIL. Lifecycle scripts and
    native binaries are LISTED here; check 8 then needs a NATIVE or LIFECYCLE line for each file that carries one."""
    listing = _npm_listing(ctx)
    named = npm_named_native(listing)
    lifecycle = [{"name": k, "command": listing["lifecycle_commands"].get(k, "")} for k in listing["lifecycle"]]
    detail = {"members": listing["members"], "expanded_bytes": listing["expanded_bytes"],
              "unsafe_member_names": listing["unsafe"], "archive_error": listing["error"],
              "lifecycle_scripts": lifecycle, "native_binaries": named, "restricted": listing["restricted"],
              "package_json_error": listing["package_json_error"], "executed": False}
    if listing["error"]:
        return rec("failed", "the archive cannot be read: %s" % listing["error"], **detail)
    if listing["unsafe"]:
        return rec("failed", "unsafe member name(s) or link(s) leaving the package: %s" % "; ".join(cap(listing["unsafe"])), **detail)
    scripts = ", ".join("%s (listed, not run)" % k for k in listing["lifecycle"]) or "none"
    return rec("passed", "%d members, %d bytes expanded, read in memory and never extracted; no unsafe member name or link; "
               "lifecycle script(s): %s; native binary(ies) named: %s" % (
                   listing["members"], listing["expanded_bytes"], scripts, "; ".join(named) or "none"), **detail)


NPM_CHECKS = [check_1_npm, check_2_npm, check_3_npm, check_4_npm, check_5, check_6_npm, check_7, check_8]
CHECKS = [check_1, check_2, check_3, check_4, check_5, check_6, check_7, check_8]


# ---------------------------------------------------------------------------------------------------------------------
# the verdict: the ONE place "checked" is produced
# ---------------------------------------------------------------------------------------------------------------------
def _derive(checks):
    """(verdict, carried): the one derivation. 'checked' when checks 1..7 are each passed, or not_applicable WITH a stated
    reason, and check 8 reads passed with a signer and a file path. A failed check 3..7 is accepted ONLY when check 8 carries
    a waiver line for exactly that check with a non-empty reason; then the verdict is 'released-with-waiver' and carried is
    the sorted list of those checks. A failed check 1 or 2, or a check 8 that refused a waiver, is never accepted.
    Anything else, including a malformed list, is 'not_checked' with carried []."""
    if not isinstance(checks, list) or len(checks) != 8:
        return "not_checked", []
    for i, c in enumerate(checks):
        if not isinstance(c, dict) or c.get("n") != i + 1:
            return "not_checked", []
    c8 = checks[7]
    ev8 = c8.get("evidence") or {}
    if not (c8.get("verdict") == "passed" and isinstance(ev8, dict) and ev8.get("signer") and ev8.get("path")):
        return "not_checked", []
    if ev8.get("refused_waivers"):
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
    return "checked", []


def compute_verdict(checks):
    """The verdict string alone: 'checked', 'released-with-waiver' or 'not_checked' (see _derive)."""
    return _derive(checks)[0]


def waived_checks_of(checks):
    """The failed checks carried by the signed waiver, when the record reads 'released-with-waiver'; else []."""
    return _derive(checks)[1]


# ---------------------------------------------------------------------------------------------------------------------
# verbs
# ---------------------------------------------------------------------------------------------------------------------
def read_fetch_record(cfg, batch, file_name):
    for d in (cfg.records_dir(batch), cfg.records_base):
        p = d / (file_name + ".fetch.json")
        if p.is_file():
            return read_json(p), p
    return None, None


def held_path_ok(fetch, batch, file_name):
    hp = str(fetch.get("held_path", "")).replace("\\", "/")
    return hp in ("holding/%s/%s" % (batch, file_name), "%s/%s" % (batch, file_name))


def run_check(cfg, batch, file_name, approved_by=None, signed_by=None, min_age=14.0, min_earlier=3, out=None,
              scan_wait=DEFAULT_SCAN_WAIT, wait_hook=None, ecosystem="pypi", lockfile=None):
    out = out or sys.stdout
    path = cfg.holding(batch) / file_name
    fetch, fpath = read_fetch_record(cfg, batch, file_name)
    ctx = {"cfg": cfg, "batch": batch, "file_name": file_name, "path": path, "fetch": fetch or {},
           "approved_by": approved_by, "signed_by": signed_by, "min_age": min_age, "min_earlier": min_earlier,
           "scan_wait": scan_wait, "wait_hook": wait_hook, "ecosystem": ecosystem, "lockfile": lockfile}
    held_sha = None
    checks = []
    print("INTAKE-CHECK thresholds: min_release_age_days=%s min_earlier_releases=%s scan_wait_seconds=%s" % (
        min_age, min_earlier, scan_wait), file=out)
    for fn, row in zip(NPM_CHECKS if ecosystem == "npm" else CHECKS, CHECK_TABLE):
        if fetch is None:
            verdict, ev = rec("failed", "no fetch record <%s.fetch.json> found for this file" % file_name)
        elif not path.is_file():
            verdict, ev = rec("failed", "the held file is not in holding/%s/" % batch)
        elif row["n"] == 1 and not held_path_ok(fetch, batch, file_name):
            verdict, ev = rec("failed", "the fetch record's held_path %r does not name this file" % fetch.get("held_path"))
        else:
            try:
                verdict, ev = fn(ctx)
            except Exception as exc:  # a check that could not run is a failed check, never a pass
                verdict, ev = rec("failed", "the check could not run: %s: %s" % (type(exc).__name__, exc))
        assert verdict in VERDICTS
        if row["n"] == 7:
            ev["limit"] = LIMIT_SENTENCE   # the limit travels beside check 7 whatever its verdict
        checks.append({"n": row["n"], "name": row["name"], "verdict": verdict, "evidence": ev,
                       "rules_out": row["rules_out"], "leaves": row["leaves"]})
        print("c%d %-14s %s" % (row["n"], verdict, ev.get("summary", "")), file=out)
        if row["n"] == 7:
            for pr in ev.get("products", []):
                print("c7 product %s state=%d hex=%s realtime=%s definitions=%s" % (
                    pr["display_name"], pr["state"], pr["hex"], pr["realtime"], pr["definitions"]), file=out)
            print("c7 decoding: %s" % ev.get("decoding", ""), file=out)
            print("c7 limit: %s" % LIMIT_SENTENCE, file=out)
    if path.is_file():
        held_sha = sha256_file(path)
    verdict, carried = _derive(checks)
    record = {"schema": "intake-check/1", "batch": batch, "file_name": file_name, "held_sha256": held_sha,
              "checks": checks, "verdict": verdict, "waived_checks": carried,
              "checked_by": os.environ.get("OPAL_AGENT_SERIAL", "unknown"), "at": stamp()}
    if ecosystem == "npm":
        record["ecosystem"] = "npm"
    write_json_atomic(cfg.records_dir(batch) / (file_name + ".check.json"), record)
    line = "INTAKE-CHECK batch=%s file=%s %s verdict=%s" % (
        batch, file_name, " ".join("c%d=%s" % (c["n"], c["verdict"]) for c in checks), record["verdict"])
    print(line, file=out)
    return record, line


def delivery_text(record, sha):
    lines = ["DELIVERY STATEMENT -- what was checked before this file was sent, and what was not",
             "batch: %s" % record["batch"], "file: %s" % record["file_name"], "sha256: %s" % sha,
             "overall: %s" % record["verdict"], ""]
    waived = {w["check"]: w["reason"] for w in ((record["checks"][7].get("evidence") or {}).get("waivers") or [])
              if isinstance(w, dict) and w.get("check") in (record.get("waived_checks") or [])}
    for c in record["checks"]:
        row = "%d. %s -- %s -- LEAVES: %s" % (c["n"], c["name"], c["verdict"], c["leaves"])
        if c["verdict"] == "not_applicable":
            row += " (not applicable: %s)" % (c.get("evidence") or {}).get("reason", "")
        lines.append(row)
        if c["n"] in waived:
            lines.append("   WAIVED BY THE SIGNED CHECK 8 FILE (the failure is kept above): %s" % waived[c["n"]])
        if c["n"] == 7:
            lines.append("   LIMIT OF CHECK 7: %s" % LIMIT_SENTENCE)
    lines += ["", DELIVERY_SENTENCE, ""]
    return ascii_clean("\n".join(lines))


def load_check_record(cfg, batch, file_name):
    p = cfg.records_dir(batch) / (file_name + ".check.json")
    if not p.is_file():
        return None, "no check record %s.check.json" % file_name
    try:
        return read_json(p), ""
    except (OSError, ValueError) as exc:
        return None, "check record unreadable: %s" % exc


def record_is_checked(record, batch, file_name):
    """Re-derive the verdict from the record's own checks ('checked' or 'released-with-waiver'); never trust the verdict field
    alone. A waived record must also carry the waived_checks list that the re-derivation gives (absent reads as [])."""
    if record.get("schema") != "intake-check/1" or record.get("batch") != batch or record.get("file_name") != file_name:
        return False, "the check record is for another batch or file, or not intake-check/1"
    derived, carried = _derive(record.get("checks"))
    if derived not in ACCEPTED_VERDICTS or record.get("verdict") != derived:
        return False, "the check record does not read 'checked' or 'released-with-waiver'"
    if list(record.get("waived_checks") or []) != carried:
        return False, "the check record's waived_checks %r disagree with the re-derivation %r" % (
            record.get("waived_checks"), carried)
    return True, ""


def run_release(cfg, batch, file_name, out=None, ecosystem="pypi"):
    out = out or sys.stdout
    if is_scan_copy(file_name):
        print("INTAKE-RELEASE REFUSED batch=%s file=%s reason=a %s file is a check-7 scan copy, never a held or released file" % (
            batch, file_name, SCAN_COPY_SUFFIX), file=out)
        return 1
    if ecosystem == "npm" and not file_name.endswith(NPM_EXT):
        print("INTAKE-RELEASE REFUSED batch=%s file=%s reason=an npm batch releases %s files only" % (
            batch, file_name, NPM_EXT), file=out)
        return 1
    record, why = load_check_record(cfg, batch, file_name)
    if record is None:
        print("INTAKE-RELEASE REFUSED batch=%s file=%s reason=%s" % (batch, file_name, why), file=out)
        return 1
    checks = record.get("checks")
    c8 = checks[7] if isinstance(checks, list) and len(checks) == 8 and isinstance(checks[7], dict) else {}
    if c8.get("verdict") == "awaiting":
        print("INTAKE-RELEASE REFUSED batch=%s file=%s reason=check 8 awaits the signature" % (batch, file_name), file=out)
        return 1
    ok, why = record_is_checked(record, batch, file_name)
    if not ok:
        print("INTAKE-RELEASE REFUSED batch=%s file=%s reason=%s" % (batch, file_name, why), file=out)
        return 1
    src = cfg.holding(batch) / file_name
    if not src.is_file():
        print("INTAKE-RELEASE REFUSED batch=%s file=%s reason=the held file is not in holding" % (batch, file_name), file=out)
        return 1
    now_sha = sha256_file(src)
    if now_sha.lower() != str(record.get("held_sha256", "")).lower():
        print("INTAKE-RELEASE REFUSED batch=%s file=%s reason=the held file changed since its check record: %s != %s" % (
            batch, file_name, now_sha, record.get("held_sha256")), file=out)
        return 1
    dest_dir = cfg.release(batch)
    dest = dest_dir / file_name
    if dest.exists():
        print("INTAKE-RELEASE REFUSED batch=%s file=%s reason=release already holds that file" % (batch, file_name), file=out)
        return 1
    dest_dir.mkdir(parents=True, exist_ok=True)
    deliv = dest_dir / (file_name + ".delivery.txt")
    with open(deliv, "w", encoding="ascii", newline="\n") as fh:
        fh.write(delivery_text(record, now_sha))
    try:
        shutil.move(str(src), str(dest))
    except OSError as exc:
        deliv.unlink()
        print("INTAKE-RELEASE REFUSED batch=%s file=%s reason=move failed: %s" % (batch, file_name, exc), file=out)
        return 1
    print("INTAKE-RELEASE batch=%s file=%s released sha256=%s" % (batch, file_name, now_sha), file=out)
    return 0


def held_back_entry(cfg, batch, name, why):
    """One file of the batch that is NOT in the pack: its current verdict and the check(s) that fail it."""
    record, rwhy = load_check_record(cfg, batch, name)
    row = {"name": name, "where": why, "verdict": None, "failing_checks": []}
    if record is None:
        row["verdict"] = "no_check_record"
        row["note"] = rwhy
        return row
    row["verdict"] = record.get("verdict") if isinstance(record, dict) else "unreadable"
    for c in (record.get("checks") or []) if isinstance(record, dict) else []:
        if isinstance(c, dict) and c.get("verdict") in ("failed", "unsigned", "awaiting"):
            row["failing_checks"].append({"n": c.get("n"), "name": c.get("name"), "verdict": c.get("verdict"),
                                          "summary": ascii_clean(str((c.get("evidence") or {}).get("summary", ""))[:300])})
    return row


def run_pack(cfg, batch, outdir, out=None, released_only=False, ecosystem="pypi"):
    """Refusal rules: (a) any file left in holding/<batch>/ refuses the batch, because a held file is one not yet checked and
    released (or one that failed), and a carrier must never receive a batch that is not whole; (b) every file in
    release/<batch>/ (other than its <name>.delivery.txt) must have a check record that re-derives 'checked', whose
    held_sha256 equals the file's SHA-256, and a delivery text; (c) an empty release folder refuses.
    With released_only=True rule (a) is lifted: the pack holds exactly the released, checked files, and the manifest gains a
    `held_back` list naming every other file of the batch (in holding/, or named by a fetch record) with its verdict and failing
    checks. Rules (b) and (c) still refuse: a released file that is not checked is an integrity fault, not a held file."""
    out = out or sys.stdout
    problems = []
    hold, rel = cfg.holding(batch), cfg.release(batch)
    if hold.is_dir() and not released_only:
        left = sorted(p.name for p in hold.iterdir() if p.is_file())
        if left:
            problems.append("files remain in holding/%s/: %s" % (batch, ", ".join(
                n + (" (a leftover check-7 scan copy, never packable)" if is_scan_copy(n) else "") for n in left)))
    files = sorted(p for p in rel.iterdir() if p.is_file() and not p.name.endswith(".delivery.txt")) if rel.is_dir() else []
    if not files:
        problems.append("release/%s/ holds no files" % batch)
    entries = []
    for f in files:
        if is_scan_copy(f.name):
            problems.append("%s: a check-7 scan copy is never a released file" % f.name)
            continue
        if ecosystem == "npm" and not f.name.endswith(NPM_EXT):
            problems.append("%s: an npm batch packs %s files only" % (f.name, NPM_EXT))
            continue
        record, why = load_check_record(cfg, batch, f.name)
        if record is None:
            problems.append("%s: %s" % (f.name, why))
            continue
        ok, why = record_is_checked(record, batch, f.name)
        if not ok:
            problems.append("%s: %s" % (f.name, why))
            continue
        sha = sha256_file(f)
        if sha.lower() != str(record.get("held_sha256", "")).lower():
            problems.append("%s: the released file's sha256 differs from the check record's" % f.name)
            continue
        deliv = rel / (f.name + ".delivery.txt")
        if not deliv.is_file():
            problems.append("%s: no delivery text" % f.name)
            continue
        entries.append((f, sha, cfg.records_dir(batch) / (f.name + ".check.json"), deliv))
    if problems:
        print("INTAKE-PACK REFUSED batch=%s reasons=%s" % (batch, " | ".join(problems)), file=out)
        return 1
    held_back = []
    if released_only:
        packed = {e[0].name for e in entries}
        names = {}
        if hold.is_dir():
            for q in hold.iterdir():
                if q.is_file() and not is_scan_copy(q.name):
                    names[q.name] = "holding/%s/" % batch
        rdir = cfg.records_dir(batch)
        if rdir.is_dir():
            for q in rdir.iterdir():
                if q.name.endswith(".fetch.json"):
                    names.setdefault(q.name[:-len(".fetch.json")], "fetch record only: not in holding or release")
        held_back = [held_back_entry(cfg, batch, n, names[n]) for n in sorted(names) if n not in packed]
    outdir = pathlib.Path(outdir)
    if outdir.exists() and any(outdir.iterdir()):
        print("INTAKE-PACK REFUSED batch=%s reasons=output folder %s is not empty" % (batch, outdir.name), file=out)
        return 1
    outdir.mkdir(parents=True, exist_ok=True)
    manifest = {"schema": "intake-manifest/1", "batch": batch, "created": stamp(), "files": []}
    for f, sha, chk, deliv in entries:
        shutil.copy2(str(f), str(outdir / f.name))
        shutil.copy2(str(chk), str(outdir / chk.name))
        shutil.copy2(str(deliv), str(outdir / deliv.name))
        manifest["files"].append({"name": f.name, "sha256": sha, "size": f.stat().st_size,
                                  "check_record": chk.name, "check_record_sha256": sha256_file(outdir / chk.name),
                                  "delivery": deliv.name, "delivery_sha256": sha256_file(outdir / deliv.name)})
    if released_only:
        manifest["held_back"] = held_back     # intake_receive.py reads only manifest["files"]; this key is ignored there
    write_json_atomic(outdir / "MANIFEST.json", manifest)
    print("INTAKE-PACK batch=%s files=%d out=%s%s" % (batch, len(entries), outdir.name,
                                                      " held_back=%d" % len(held_back) if released_only else ""), file=out)
    for h in held_back:
        print("INTAKE-PACK held back: %s verdict=%s failing=%s" % (
            h["name"], h["verdict"], ",".join("c%s" % c["n"] for c in h["failing_checks"]) or "none"), file=out)
    return 0


# ---------------------------------------------------------------------------------------------------------------------
# synthetic wheels (used by selftest-unsigned and by the tests); built with the standard library only
# ---------------------------------------------------------------------------------------------------------------------
SYN_NAME, SYN_VERSION = "selftestpkg", "1.0.0"
SYN_TAGS = ("cp312", "cp312", "win_amd64")
SYN_PY = b"VALUE = 1\n"


def syn_file_name(name=SYN_NAME, version=SYN_VERSION, tags=SYN_TAGS):
    return "%s-%s-%s-%s-%s.whl" % ((name, version) + tuple(tags))


def build_synthetic_wheel(path, name=SYN_NAME, version=SYN_VERSION, tags=SYN_TAGS, py_bytes=SYN_PY, extra=None,
                          entry_points="[console_scripts]\nselftest = selftestpkg:main\n"):
    """A tiny harmless wheel: one .py, one fake .pyd (not real machine code), dist-info. `extra` = {member name: bytes}."""
    di = "%s-%s.dist-info" % (name, version)
    members = {
        "%s/__init__.py" % name: py_bytes,
        "%s/_ext.pyd" % name: b"not machine code, synthetic bytes\n",
        di + "/METADATA": ("Metadata-Version: 2.1\nName: %s\nVersion: %s\n\nsynthetic\n" % (name, version)).encode("ascii"),
        di + "/WHEEL": ("Wheel-Version: 1.0\nGenerator: intake_check selftest\nRoot-Is-Purelib: false\nTag: %s\n" % "-".join(tags)).encode("ascii"),
    }
    if entry_points:
        members[di + "/entry_points.txt"] = entry_points.encode("ascii")
    members.update(extra or {})
    members[di + "/RECORD"] = b"".join(("%s,,\n" % k).encode("ascii") for k in sorted(members)) + (di + "/RECORD,,\n").encode("ascii")
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zf:
        for k in sorted(members):
            zf.writestr(k, members[k])
    return pathlib.Path(path)


def build_installed_fixture(site_dir, name=SYN_NAME, version=SYN_VERSION, py_bytes=SYN_PY,
                            entry_points="[console_scripts]\nselftest = selftestpkg:main\n"):
    site_dir = pathlib.Path(site_dir)
    di = site_dir / ("%s-%s.dist-info" % (name, version))
    di.mkdir(parents=True, exist_ok=True)
    (di / "METADATA").write_bytes(("Metadata-Version: 2.1\nName: %s\nVersion: %s\n\nsynthetic\n" % (name, version)).encode("ascii"))
    (di / "RECORD").write_bytes(("%s/__init__.py,,\n" % name).encode("ascii"))
    if entry_points:
        (di / "entry_points.txt").write_bytes(entry_points.encode("ascii"))
    (site_dir / name).mkdir(exist_ok=True)
    (site_dir / name / "__init__.py").write_bytes(py_bytes)
    return di


def fetch_device():
    """The device key a fetch-shaped record carries: intake_fetch.this_device(), imported and never copied, so there is one
    derivation. No cycle: intake_fetch.py imports no module of this one. None (null) when the box cannot be named."""
    here = os.path.dirname(os.path.abspath(__file__))
    if here not in sys.path:
        sys.path.insert(0, here)
    import intake_fetch  # noqa: E402  (stdlib-only module beside this file)
    return intake_fetch.this_device()


def write_fetch_record(cfg, batch, wheel_path, name=SYN_NAME, version=SYN_VERSION, tags=SYN_TAGS, attestation="absent",
                       release_age_days=60, release_count=10, outcome="held", published_sha=None):
    fn = pathlib.Path(wheel_path).name
    sha = sha256_file(wheel_path)
    rel = now_utc() - datetime.timedelta(days=release_age_days)
    first = rel - datetime.timedelta(days=400)
    rec_ = {"schema": "intake-fetch/1", "batch": batch,
            "requested": {"name": name, "version": version, "python_tag": tags[0], "abi_tag": tags[1],
                          "platform_tag": tags[2], "file_name": fn},
            "index_base": "http://127.0.0.1/", "requests": [],
            "published": {"sha256": published_sha or sha, "size": os.path.getsize(wheel_path), "upload_time": stamp(rel),
                          "yanked": False, "requires_python": ">=3.9"},
            "project": {"release_count": release_count, "first_release_at": stamp(first), "this_release_at": stamp(rel)},
            "attestation": attestation, "held_path": "holding/%s/%s" % (batch, fn), "held_sha256": sha,
            "held_bytes": os.path.getsize(wheel_path), "outcome": outcome, "reason": "", "fetched_by": "selftest",
            "device": fetch_device(), "at": stamp()}
    write_json_atomic(cfg.records_dir(batch) / (fn + ".fetch.json"), rec_)
    return rec_


def selftest_unsigned(out=None):
    out = out or sys.stdout
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="intake_selftest_"))
    try:
        site_dir = tmp / "site"
        site_dir.mkdir()
        build_installed_fixture(site_dir)
        av = tmp / "av.json"
        av.write_text(json.dumps([{"displayName": "Synthetic Antivirus (stand-in)", "productState": 266240}]), encoding="ascii")
        cfg = Cfg(root=tmp / "root", records=tmp / "records", av_json=str(av), sites=[site_dir], signer_dir=tmp / "signer")
        batch = "selftest-batch"
        hold = cfg.holding(batch)
        hold.mkdir(parents=True)
        wheel = build_synthetic_wheel(hold / syn_file_name())
        write_fetch_record(cfg, batch, wheel)
        approved = tmp / "approved.txt"
        approved.write_text("%s==%s\n" % (SYN_NAME, SYN_VERSION), encoding="ascii")
        record, line = run_check(cfg, batch, wheel.name, approved_by=str(approved), signed_by=None, out=out, scan_wait=0)
        return 0 if "c8=unsigned verdict=not_checked" in line and record["verdict"] == "not_checked" else 1
    finally:
        shutil.rmtree(str(tmp), ignore_errors=True)


def summarize_av(products):
    """(active names or NONE, realtime on|off, definitions current|out_of_date|unknown, ok). ok = at least one product is on and
    current. unknown is never treated as on or current."""
    active = [p for p in products if p["realtime"] == "on"]
    names = "; ".join(p["display_name"] for p in active) if active else "NONE"
    defs = {p["definitions"] for p in active}
    if not active:
        d = "unknown"
    elif "out_of_date" in defs:
        d = "out_of_date"
    elif defs == {"current"}:
        d = "current"
    else:
        d = "unknown"
    ok = any(p["realtime"] == "on" and p["definitions"] == "current" for p in products)
    return names, "on" if active else "off", d, ok


def selftest_av(cfg=None, out=None):
    """Read the Security Center (the REAL one unless a Cfg with a stand-in is given) and print ONE line. Writes no file."""
    out = out or sys.stdout
    cfg = cfg or Cfg(av_json="")
    products, err = read_security_center(cfg)
    if err:
        print("INTAKE-AV query failed: %s" % err, file=sys.stderr)
    names, rt, df, ok = summarize_av(products)
    print("INTAKE-AV products=%d active=%s realtime=%s definitions=%s ok=%s" % (len(products), names, rt, df, ok), file=out)
    return 0 if ok else 1


def main(argv=None):
    ap = argparse.ArgumentParser(prog="intake_check.py", description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="verb", required=True)
    c = sub.add_parser("check")
    c.add_argument("--batch", required=True)
    c.add_argument("--file", required=True)
    c.add_argument("--approved-by")
    c.add_argument("--signed-by")
    c.add_argument("--min-release-age-days", type=float, default=14)
    c.add_argument("--min-earlier-releases", type=int, default=3)
    c.add_argument("--scan-wait-seconds", type=int, default=DEFAULT_SCAN_WAIT)
    c.add_argument("--ecosystem", choices=("pypi", "npm"), default="pypi")
    c.add_argument("--lockfile", default=None, help="npm: the bun text lockfile; a missing one refuses the npm check")
    r = sub.add_parser("release")
    r.add_argument("--batch", required=True)
    r.add_argument("--file", required=True)
    r.add_argument("--ecosystem", choices=("pypi", "npm"), default="pypi")
    p = sub.add_parser("pack")
    p.add_argument("--batch", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--released-only", action="store_true", dest="released_only")
    p.add_argument("--ecosystem", choices=("pypi", "npm"), default="pypi")
    sub.add_parser("selftest-unsigned")
    sub.add_parser("selftest-av")
    a = ap.parse_args(argv)
    if a.verb == "selftest-unsigned":
        return selftest_unsigned()
    if a.verb == "selftest-av":
        return selftest_av()
    cfg = Cfg()
    if a.verb == "check":
        if is_scan_copy(a.file):
            print("INTAKE-CHECK REFUSED batch=%s file=%s reason=a %s file is a check-7 scan copy, never a held file" % (
                a.batch, a.file, SCAN_COPY_SUFFIX))
            return 1
        if a.scan_wait_seconds < 0:
            print("INTAKE-CHECK REFUSED reason=--scan-wait-seconds must not be negative")
            return 1
        if a.ecosystem == "npm" and not a.lockfile:
            print("INTAKE-CHECK REFUSED batch=%s file=%s reason=--ecosystem npm needs --lockfile <bun.lock>; a missing "
                  "lockfile is a refusal, never a skip" % (a.batch, a.file))
            return 1
        run_check(cfg, a.batch, a.file, a.approved_by, a.signed_by, a.min_release_age_days, a.min_earlier_releases,
                  scan_wait=a.scan_wait_seconds, ecosystem=a.ecosystem, lockfile=a.lockfile)
        return 0
    if a.verb == "release":
        return run_release(cfg, a.batch, a.file, ecosystem=a.ecosystem)
    return run_pack(cfg, a.batch, a.out, released_only=a.released_only, ecosystem=a.ecosystem)


if __name__ == "__main__":
    sys.exit(main())
