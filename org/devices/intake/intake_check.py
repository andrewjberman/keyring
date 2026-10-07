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
  release --batch <id> --file <file name>
  pack    --batch <id> --out <dir>
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
The ONLY producer of the overall verdict "checked" is compute_verdict().
"""
from __future__ import annotations

import argparse
import configparser
import csv
import datetime
import email.parser
import hashlib
import itertools
import json
import os
import pathlib
import re
import shutil
import site
import subprocess
import sys
import tempfile
import time
import zipfile

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
VERDICTS = ("passed", "failed", "not_applicable", "unsigned")
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
                    paths.add(row[0].replace("\\", "/"))
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


def check_3(ctx):
    req = ctx["fetch"].get("requested") or {}
    found, versions = find_installed(ctx["cfg"], req.get("name", ""), req.get("version", ""))
    ctx["installed"] = found
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


def check_6(ctx):
    if not ctx.get("installed"):
        reason = "check 3 was not applicable: no installed copy of this version to compare with"
        return rec("not_applicable", reason, reason=reason)
    inst = ctx["installed"][0]
    site_dir, inst_di = inst["site"], inst["dist_info"]
    inst_record = installed_record_paths(inst_di)
    inst_record_base = {p.rsplit("/", 1)[-1].lower() for p in inst_record}
    try:
        inst_eps = entry_point_set((inst_di / "entry_points.txt").read_text(encoding="utf-8", errors="replace"))
    except OSError:
        inst_eps = set()
    py_total = py_ident = 0
    py_diff, compiled, hooks_new, hooks_old, unsafe = [], [], [], [], []
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
                    continue
                target = site_dir / rel
                if info.file_size > MAX_PY_BYTES or not target.is_file():
                    py_diff.append(n)
                elif target.read_bytes() == zf.read(info):
                    py_ident += 1
                else:
                    py_diff.append(n)
        di, _ = wheel_dist_info(zf)
        wheel_eps = set()
        if di and (di + "/entry_points.txt") in zf.namelist():
            wheel_eps = entry_point_set(zf.read(di + "/entry_points.txt").decode("utf-8", "replace"))
    for ep in sorted(wheel_eps):
        label = "entry_point %s:%s = %s" % ep
        (hooks_old if ep in inst_eps else hooks_new).append(label)
    detail = {"installed_copy": "<site-packages>/" + inst["dist_info_name"], "py_in_wheel": py_total, "py_identical": py_ident,
              "py_differing_count": len(py_diff), "py_differing": py_diff, "compiled_count": len(compiled), "compiled": compiled,
              "hooks_only_in_wheel": hooks_new, "hooks_also_in_installed_copy": hooks_old, "unsafe_member_names": unsafe}
    problems = []
    if py_diff:
        problems.append("%d of %d .py files differ from the installed copy: %s" % (len(py_diff), py_total, cap(py_diff)))
    if hooks_new:
        problems.append("installer/script/start-up hook(s) not in the installed copy: %s" % cap(hooks_new))
    if unsafe:
        problems.append("unsafe member name(s): %s" % cap(unsafe))
    if problems:
        return rec("failed", "; ".join(problems), **detail)
    return rec("passed", "%d of %d .py files byte-identical; %d compiled file(s) named; no new hook" % (py_ident, py_total, len(compiled)),
               **detail)


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
        return rec("failed", "the signature file does not exist")
    text = rp.read_text(encoding="utf-8", errors="replace")
    miss = [what for what, s in (("batch id", ctx["batch"]), ("file name", ctx["file_name"])) if s not in text]
    if miss:
        return rec("failed", "the signature file's text does not contain the %s" % " and the ".join(miss))
    if cfg.signer_dir is None:
        rel = rp.relative_to(REPO_ROOT.resolve()).as_posix()
        parts = rel.split("/")
        signer = parts[2] if len(parts) > 3 and parts[0] == "org" and parts[1] == "tier1_exec" else "unknown"
        author = _git_author(rp)
    else:
        rel = rp.name
        signer = "override-dir:" + rb.name
        author = "not read (override dir)"
    return rec("passed", "signature file names the batch and the file", signer=signer, path=rel,
               signature_file_sha256=sha256_bytes(rp.read_bytes()), signature_file_git_author=author)


CHECKS = [check_1, check_2, check_3, check_4, check_5, check_6, check_7, check_8]


# ---------------------------------------------------------------------------------------------------------------------
# the verdict: the ONE place "checked" is produced
# ---------------------------------------------------------------------------------------------------------------------
def compute_verdict(checks):
    """'checked' only when checks 1..7 are each passed, or not_applicable WITH a stated reason, and check 8 reads passed
    with a signer and a file path. Anything else, including a malformed list, is 'not_checked'."""
    if not isinstance(checks, list) or len(checks) != 8:
        return "not_checked"
    for i, c in enumerate(checks):
        if not isinstance(c, dict) or c.get("n") != i + 1:
            return "not_checked"
    for c in checks[:7]:
        ev = c.get("evidence") or {}
        if c.get("verdict") == "passed":
            continue
        if c.get("verdict") == "not_applicable" and isinstance(ev, dict) and str(ev.get("reason", "")).strip():
            continue
        return "not_checked"
    c8 = checks[7]
    ev8 = c8.get("evidence") or {}
    if c8.get("verdict") == "passed" and isinstance(ev8, dict) and ev8.get("signer") and ev8.get("path"):
        return "checked"
    return "not_checked"


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
              scan_wait=DEFAULT_SCAN_WAIT, wait_hook=None):
    out = out or sys.stdout
    path = cfg.holding(batch) / file_name
    fetch, fpath = read_fetch_record(cfg, batch, file_name)
    ctx = {"cfg": cfg, "batch": batch, "file_name": file_name, "path": path, "fetch": fetch or {},
           "approved_by": approved_by, "signed_by": signed_by, "min_age": min_age, "min_earlier": min_earlier,
           "scan_wait": scan_wait, "wait_hook": wait_hook}
    held_sha = None
    checks = []
    print("INTAKE-CHECK thresholds: min_release_age_days=%s min_earlier_releases=%s scan_wait_seconds=%s" % (
        min_age, min_earlier, scan_wait), file=out)
    for fn, row in zip(CHECKS, CHECK_TABLE):
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
    record = {"schema": "intake-check/1", "batch": batch, "file_name": file_name, "held_sha256": held_sha,
              "checks": checks, "verdict": compute_verdict(checks),
              "checked_by": os.environ.get("OPAL_AGENT_SERIAL", "unknown"), "at": stamp()}
    write_json_atomic(cfg.records_dir(batch) / (file_name + ".check.json"), record)
    line = "INTAKE-CHECK batch=%s file=%s %s verdict=%s" % (
        batch, file_name, " ".join("c%d=%s" % (c["n"], c["verdict"]) for c in checks), record["verdict"])
    print(line, file=out)
    return record, line


def delivery_text(record, sha):
    lines = ["DELIVERY STATEMENT -- what was checked before this file was sent, and what was not",
             "batch: %s" % record["batch"], "file: %s" % record["file_name"], "sha256: %s" % sha,
             "overall: %s" % record["verdict"], ""]
    for c in record["checks"]:
        row = "%d. %s -- %s -- LEAVES: %s" % (c["n"], c["name"], c["verdict"], c["leaves"])
        if c["verdict"] == "not_applicable":
            row += " (not applicable: %s)" % (c.get("evidence") or {}).get("reason", "")
        lines.append(row)
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
    """Re-derive 'checked' from the record's own checks; never trust the verdict field alone."""
    if record.get("schema") != "intake-check/1" or record.get("batch") != batch or record.get("file_name") != file_name:
        return False, "the check record is for another batch or file, or not intake-check/1"
    if record.get("verdict") != "checked" or compute_verdict(record.get("checks")) != "checked":
        return False, "the check record does not read 'checked'"
    return True, ""


def run_release(cfg, batch, file_name, out=None):
    out = out or sys.stdout
    if is_scan_copy(file_name):
        print("INTAKE-RELEASE REFUSED batch=%s file=%s reason=a %s file is a check-7 scan copy, never a held or released file" % (
            batch, file_name, SCAN_COPY_SUFFIX), file=out)
        return 1
    record, why = load_check_record(cfg, batch, file_name)
    if record is None:
        print("INTAKE-RELEASE REFUSED batch=%s file=%s reason=%s" % (batch, file_name, why), file=out)
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


def run_pack(cfg, batch, outdir, out=None):
    """Refusal rules: (a) any file left in holding/<batch>/ refuses the batch, because a held file is one not yet checked and
    released (or one that failed), and a carrier must never receive a batch that is not whole; (b) every file in
    release/<batch>/ (other than its <name>.delivery.txt) must have a check record that re-derives 'checked', whose
    held_sha256 equals the file's SHA-256, and a delivery text; (c) an empty release folder refuses."""
    out = out or sys.stdout
    problems = []
    hold, rel = cfg.holding(batch), cfg.release(batch)
    if hold.is_dir():
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
    write_json_atomic(outdir / "MANIFEST.json", manifest)
    print("INTAKE-PACK batch=%s files=%d out=%s" % (batch, len(entries), outdir.name), file=out)
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
            "held_bytes": os.path.getsize(wheel_path), "outcome": outcome, "reason": "", "fetched_by": "selftest", "at": stamp()}
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
    r = sub.add_parser("release")
    r.add_argument("--batch", required=True)
    r.add_argument("--file", required=True)
    p = sub.add_parser("pack")
    p.add_argument("--batch", required=True)
    p.add_argument("--out", required=True)
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
        run_check(cfg, a.batch, a.file, a.approved_by, a.signed_by, a.min_release_age_days, a.min_earlier_releases,
                  scan_wait=a.scan_wait_seconds)
        return 0
    if a.verb == "release":
        return run_release(cfg, a.batch, a.file)
    return run_pack(cfg, a.batch, a.out)


if __name__ == "__main__":
    sys.exit(main())
