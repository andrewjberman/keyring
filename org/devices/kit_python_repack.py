"""kit_python_repack.py -- rebuild a wheel for each requirement that FITS Python 3.14 (class PURE-INSTALLED or ABI3-INSTALLED in
org/devices/kit_python_wheels_cp314.json), from the INSTALLED copy on this machine, offline, with the standard library only.

NO NETWORK. This tool makes no request to any package index and installs nothing on the machine that builds the kit.
The only pip command it constructs is the Dell's `install-check`, which always carries `--no-index` and `--no-deps` and
always installs into a scratch `--target` directory (see pip_install_cmd; a test asserts it).

Verbs:
  repack --out <dir> [--from-file <json>] [--root LABEL=DIR ...] [--min-free-gb 10]
        For each selected requirement: read the installed dist-info RECORD, compare EVERY listed file's bytes with the hash
        RECORD states (a missing file or a different hash marks the package MODIFIED and leaves it OUT of the kit), then
        write a wheel: the RECORD-listed files, the dist-info as installed MINUS INSTALLER, REQUESTED, direct_url.json and
        RECORD, a regenerated RECORD, a file name built from the WHEEL file's own Tag lines. Verify each wheel by re-opening it.
        Writes <dir>/MANIFEST.json and <dir>/requirements-kit.txt. LAST line PY-REPACK ...
  verify --from <dir>
        Every wheel against MANIFEST.json (sha256, size); nothing in the folder the manifest does not list; prints the
        commands a Dell runs. LAST line PY-KIT-VERIFY ...  (stdlib only: runs on a Dell)
  install-check --from <dir> [--scratch <dir>]
        pip install --no-index --no-deps --find-links <dir> -r <dir>/requirements-kit.txt --target <scratch>, then one import
        of each distribution's top-level module in its own subprocess (60 s bound), scratch first on the path.
        LAST line PY-KIT-INSTALL ...  (stdlib only: runs on a Dell)

Files outside site-packages named by RECORD (paths starting ../):
  - a Scripts/ file that is a LAUNCHER pip regenerates at install from entry_points.txt is NOT packed and does NOT make the
    package partial. A file is decided to be a generated launcher when it is directly under Scripts/ and its name is
    <entry>.exe, <entry>-script.py(w), <entry>.exe.manifest, or <entry>-X.Y.exe / <entry>X.exe, where <entry> is a key of the
    distribution's console_scripts or gui_scripts. An .exe with NO such entry (ruff's own binary) is NOT a launcher: it is
    real content and is packed under <name>-<version>.data/scripts/.
  - any other file directly under Scripts/ is placed under <name>-<version>.data/scripts/ (a first line `#!<path>python.exe`
    that pip wrote at install is put back to `#!python`, which pip rewrites again at install; the file is reported).
  - anything else outside site-packages is not packed and marks the package PARTIAL (reported with its paths).
RECORD entries with an empty hash (other than RECORD itself) cannot be checked: the file is packed if present and counted as
`unverified`; this is stated in the manifest and the output.
"""
from __future__ import annotations

import argparse
import base64
import configparser
import csv
import datetime
import email.parser
import hashlib
import io
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
DEFAULT_CLASSIFICATION = HERE / "kit_python_wheels_cp314.json"
SCHEMA = "kit_python_repack/1"
SELECTED_CLASSES = ("PURE-INSTALLED", "ABI3-INSTALLED")
FIXED_DATE = (1980, 1, 1, 0, 0, 0)
CHUNK = 1 << 20
ZIP64_LIMIT = (1 << 31) - 1
DIST_SKIP = {"INSTALLER", "REQUESTED", "direct_url.json", "RECORD"}
IMPORT_BOUND = 60
PIP_LOG: list = []


def asc(text):
    return str(text).encode("ascii", "replace").decode("ascii")


def now_utc():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_file(path):
    """Return (urlsafe-base64 digest without padding, hex digest, size), streaming."""
    h = hashlib.sha256()
    size = 0
    with open(path, "rb") as fh:
        while True:
            chunk = fh.read(CHUNK)
            if not chunk:
                break
            h.update(chunk)
            size += len(chunk)
    return b64(h.digest()), h.hexdigest(), size


def b64(digest):
    return base64.urlsafe_b64encode(digest).rstrip(b"=").decode("ascii")


def norm_dist(name):
    """Wheel-file name component: runs of - _ . become one _, lower case."""
    return re.sub(r"[-_.]+", "_", str(name)).lower()


def norm_version(version):
    return str(version).replace("-", "_")


def compress_tags(tag_lines):
    """Compress the WHEEL file's Tag lines as the wheel specification does (py2.py3-none-any). Raises ValueError when the
    set is not the cartesian product of its three components (then no single compressed name states it exactly)."""
    triples = []
    for tag in tag_lines:
        parts = tag.strip().split("-")
        if len(parts) != 3 or not all(parts):
            raise ValueError("unparseable Tag line: " + tag)
        triples.append(tuple(parts))
    if not triples:
        raise ValueError("no Tag line")
    pys = sorted({t[0] for t in triples})
    abis = sorted({t[1] for t in triples})
    plats = sorted({t[2] for t in triples})
    if {(a, b, c) for a in pys for b in abis for c in plats} != set(triples):
        raise ValueError("Tag lines are not a cartesian product: " + ", ".join(tag_lines))
    return "-".join((".".join(pys), ".".join(abis), ".".join(plats)))


def parse_headers(text):
    return email.parser.Parser().parsestr(text, headersonly=True)


# ------------------------------------------------------------------------------------------------------------- RECORD

def read_record(text):
    """Parse an installed RECORD. Paths are normalised to forward slashes; duplicate paths are merged (a hashed entry beats
    an unhashed one: some installed RECORDs list one file twice, once per slash style). Returns (entries, conflicts) where
    entries is a list of (path, algorithm, digest, size_text) and conflicts lists paths whose two hashed entries disagree."""
    merged = {}
    order = []
    conflicts = []
    for row in csv.reader(io.StringIO(text, newline="")):
        if not row or not row[0].strip():
            continue
        path = row[0].replace("\\", "/")
        hashfield = row[1].strip() if len(row) > 1 else ""
        size = row[2].strip() if len(row) > 2 else ""
        alg, digest = ("", "")
        if "=" in hashfield:
            alg, digest = hashfield.split("=", 1)
        entry = (path, alg.lower(), digest, size)
        if path not in merged:
            merged[path] = entry
            order.append(path)
        else:
            old = merged[path]
            if not old[2] and digest:
                merged[path] = entry
            elif old[2] and digest and (old[1], old[2]) != (alg.lower(), digest):
                conflicts.append(path)
    return [merged[p] for p in order], conflicts


def record_text(items):
    """items: list of (arcname, b64 sha256 or '', size or ''). Written with LF line ends."""
    buf = io.StringIO()
    writer = csv.writer(buf, lineterminator="\n")
    for arc, digest, size in items:
        writer.writerow([arc, ("sha256=" + digest) if digest else "", size])
    return buf.getvalue()


def hash_matches(path, alg, digest):
    """Hash the file with the algorithm RECORD names. Returns (matches, sha256_b64, sha256_hex, size)."""
    sha_b64, sha_hex, size = sha256_file(path)
    if alg == "sha256":
        return sha_b64 == digest, sha_b64, sha_hex, size
    try:
        h = hashlib.new(alg)
    except (ValueError, TypeError):
        return False, sha_b64, sha_hex, size
    with open(path, "rb") as fh:
        while True:
            chunk = fh.read(CHUNK)
            if not chunk:
                break
            h.update(chunk)
    return b64(h.digest()) == digest, sha_b64, sha_hex, size


# --------------------------------------------------------------------------------------------------------- planning

def entry_point_names(dist_info):
    """console_scripts and gui_scripts keys from the installed entry_points.txt (case preserved)."""
    path = pathlib.Path(dist_info, "entry_points.txt")
    names = []
    if not path.is_file():
        return names
    cp = configparser.RawConfigParser(delimiters=("=",), interpolation=None, strict=False)
    cp.optionxform = str
    try:
        cp.read_string(path.read_bytes().decode("utf-8", "replace"))
    except configparser.Error:
        return names
    for section in ("console_scripts", "gui_scripts"):
        if cp.has_section(section):
            names.extend(k.strip() for k in cp.options(section))
    return names


def is_generated_launcher(filename, entry_names):
    low = filename.lower()
    for entry in entry_names:
        e = re.escape(entry.lower())
        if re.fullmatch(e + r"(-?\d+(\.\d+)?)?\.exe", low) or re.fullmatch(e + r"-script\.pyw?", low) \
                or low == entry.lower() + ".exe.manifest":
            return True
    return False


def restore_shebang(data):
    """pip rewrites a first line `#!python` to `#!<interpreter path>` at install. Put it back so the Dell's pip writes the
    Dell's interpreter. Returns (data, restored_bool)."""
    nl = data.find(b"\n")
    first = data if nl < 0 else data[:nl]
    if not first.startswith(b"#!"):
        return data, False
    line = first.rstrip(b"\r").decode("utf-8", "replace")
    m = re.fullmatch(r"#!\s*(?:\"?)(?:.*[\\/])?(pythonw?)(?:[0-9.]*)(?:\.exe)?(?:\"?)(?:\s.*)?", line, flags=re.I)
    if not m:
        return data, False
    new = b"#!" + m.group(1).lower().encode("ascii") + b"\n"
    return new + (b"" if nl < 0 else data[nl + 1:]), True


def sort_key(item):
    arc = item["arc"]
    group = 2 if ".dist-info/" in arc else 1 if ".data/" in arc else 0
    return (group, arc)


def plan_package(dist_info_dir, site_dir):
    """Read RECORD, verify every file against it and decide where each goes. Returns a plan dict; never raises on a
    modified install (that is a status). Raises OSError/ValueError only for an unreadable dist-info."""
    di = pathlib.Path(dist_info_dir)
    site = pathlib.Path(site_dir)
    di_name = di.name
    prefix = di_name[: -len(".dist-info")]
    meta = parse_headers(pathlib.Path(di, "METADATA").read_bytes().decode("utf-8", "replace"))
    wheel = parse_headers(pathlib.Path(di, "WHEEL").read_bytes().decode("utf-8", "replace"))
    tags = [t.strip() for t in (wheel.get_all("Tag") or [])]
    plan = {"name": (meta.get("Name") or "").strip(), "version": (meta.get("Version") or "").strip(),
            "dist_info": di_name, "tags": tags, "items": [], "modified": [], "partial_paths": [],
            "launchers_skipped": [], "scripts_placed": [], "shebangs_restored": [], "unverified": [],
            "pyc_skipped": 0, "dist_skipped": [], "bytes_in": 0, "notes": []}
    entries, conflicts = read_record(pathlib.Path(di, "RECORD").read_bytes().decode("utf-8", "replace"))
    for path in conflicts:
        plan["modified"].append((path, "RECORD lists this path twice with different hashes"))
    entry_names = entry_point_names(di)
    data_dir = prefix + ".data"
    # Some installers list a script twice: once at its wheel path <name>-<version>.data/scripts/<f> (hashed) and once at its
    # installed path ../../Scripts/<f> (unhashed). Merge the two under the installed path, keeping the hash.
    canon = {}
    for path, alg, digest, size_text in entries:
        segs = path.split("/")
        if len(segs) >= 3 and segs[0] == data_dir and segs[1] == "scripts" and not pathlib.Path(site, *segs).is_file():
            plan["notes"].append("RECORD path %s read as ../../Scripts/%s" % (path, "/".join(segs[2:])))
            path = "../../Scripts/" + "/".join(segs[2:])
        old = canon.get(path)
        if old is None or (not old[2] and digest):
            canon[path] = (path, alg, digest, size_text)
    seen_arcs = set()
    for path, alg, digest, size_text in canon.values():
        segs = path.split("/")
        if path.endswith(".pyc") or "__pycache__" in segs:
            plan["pyc_skipped"] += 1
            continue
        if segs[0] == di_name and len(segs) == 2 and segs[1] in DIST_SKIP:
            plan["dist_skipped"].append(path)
            continue
        outside = ".." in segs
        abs_path = pathlib.Path(os.path.normpath(os.path.join(str(site), *segs)))
        arc = path
        mode = 0o644
        launcher = False
        if outside:
            try:
                rel = abs_path.relative_to(site.parent.parent)
            except ValueError:
                plan["partial_paths"].append(path + " (outside the Python root)")
                continue
            rparts = rel.parts
            if len(rparts) == 2 and rparts[0].lower() == "scripts":
                if is_generated_launcher(rparts[1], entry_names):
                    plan["launchers_skipped"].append(path)
                    launcher = True
                else:
                    arc = data_dir + "/scripts/" + rparts[1]
                    mode = 0o755
            else:
                plan["partial_paths"].append(path)
                continue
        elif ".." in abs_path.parts:  # pragma: no cover - normpath removes these
            plan["partial_paths"].append(path)
            continue
        if launcher:
            continue
        if not abs_path.is_file():
            plan["modified"].append((path, "listed in RECORD, missing on disk"))
            continue
        if digest:
            ok, sha_b64, sha_hex, size = hash_matches(abs_path, alg, digest)
            if not ok:
                plan["modified"].append((path, "bytes on disk differ from the RECORD hash (%s)" % (alg or "none")))
                continue
        else:
            sha_b64, sha_hex, size = sha256_file(abs_path)
            plan["unverified"].append(path)
        if size_text.isdigit() and int(size_text) != size and digest:
            plan["modified"].append((path, "size on disk %d, RECORD states %s" % (size, size_text)))
            continue
        if arc in seen_arcs:
            continue
        seen_arcs.add(arc)
        item = {"arc": arc, "src": str(abs_path), "mode": mode, "sha": sha_b64, "size": size, "data": None}
        if mode == 0o755 and size <= 16 * 1024 * 1024:
            raw = abs_path.read_bytes()
            new, restored = restore_shebang(raw)
            if restored:
                item["data"] = new
                item["sha"] = b64(hashlib.sha256(new).digest())
                item["size"] = len(new)
                plan["shebangs_restored"].append(path)
            if arc.endswith(".data/scripts/" + abs_path.name):
                plan["scripts_placed"].append(path)
        elif mode == 0o755:
            plan["scripts_placed"].append(path)
        plan["bytes_in"] += size
        plan["items"].append(item)
    have = {i["arc"] for i in plan["items"]}
    for needed in (di_name + "/METADATA", di_name + "/WHEEL"):
        if needed not in have and not plan["modified"]:
            plan["modified"].append((needed, "METADATA or WHEEL is not listed in RECORD"))
    plan["items"].sort(key=sort_key)
    return plan


def wheel_file_name(plan):
    return "%s-%s-%s.whl" % (norm_dist(plan["name"]), norm_version(plan["version"]), compress_tags(plan["tags"]))


# --------------------------------------------------------------------------------------------------------- writing

def write_wheel(plan, out_path):
    """Write the wheel to <out_path>.partial then rename. Streams large files; re-hashes while copying. Returns the wheel
    file's (sha256 hex, size). Deterministic: fixed timestamps, sorted members, fixed modes."""
    tmp = str(out_path) + ".partial"
    di_name = plan["dist_info"]
    rec_items = []
    try:
        with zipfile.ZipFile(tmp, "w", compression=zipfile.ZIP_DEFLATED, allowZip64=True) as zf:
            for item in plan["items"]:
                zi = zipfile.ZipInfo(item["arc"], date_time=FIXED_DATE)
                zi.compress_type = zipfile.ZIP_DEFLATED
                zi.create_system = 3
                zi.external_attr = (0o100000 | item["mode"]) << 16
                if item["data"] is not None:
                    zf.writestr(zi, item["data"])
                else:
                    zi.file_size = item["size"]
                    h = hashlib.sha256()
                    with open(item["src"], "rb") as src, zf.open(zi, "w", force_zip64=item["size"] > ZIP64_LIMIT) as dst:
                        while True:
                            chunk = src.read(CHUNK)
                            if not chunk:
                                break
                            h.update(chunk)
                            dst.write(chunk)
                    if b64(h.digest()) != item["sha"]:
                        raise OSError("file changed while it was being packed: " + item["src"])
                rec_items.append((item["arc"], item["sha"], str(item["size"])))
            rec_items.append((di_name + "/RECORD", "", ""))
            zi = zipfile.ZipInfo(di_name + "/RECORD", date_time=FIXED_DATE)
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.create_system = 3
            zi.external_attr = (0o100000 | 0o644) << 16
            zf.writestr(zi, record_text(rec_items).encode("utf-8"))
        os.replace(tmp, out_path)
    except BaseException:
        try:
            os.remove(tmp)
        except OSError:
            pass
        raise
    _b64, hexd, size = sha256_file(out_path)
    return hexd, size


# ------------------------------------------------------------------------------------------------------- verification

def tag_support(python_tag, platform):
    sys.path.insert(0, str(HERE))
    try:
        import kit_python_wheels as kpw  # noqa: PLC0415 - needs `packaging`; the laptop's half only
    finally:
        sys.path.pop(0)
    target = kpw.parse_target(python_tag, platform)
    return kpw, target, kpw.supported_tags(target)


def verify_wheel(path, supported, kpw):
    """Re-open a wheel and check it. Returns a list of problems (empty = verified) and a facts dict."""
    problems = []
    facts = {}
    path = pathlib.Path(path)
    try:
        zf = zipfile.ZipFile(path)
    except (zipfile.BadZipFile, OSError) as exc:
        return ["not a readable zip: " + asc(exc)], facts
    with zf:
        bad = zf.testzip()
        if bad:
            problems.append("zip member fails its CRC: " + bad)
        names = zf.namelist()
        if len(set(names)) != len(names):
            problems.append("duplicate member names")
        for n in names:
            segs = n.split("/")
            if ".." in segs or n.startswith("/") or "\\" in n or re.match(r"^[A-Za-z]:", n):
                problems.append("unsafe member path: " + n)
            if n.endswith(".pyc") or "__pycache__" in segs:
                problems.append("compiled cache member present: " + n)
        dis = sorted({n.split("/")[0] for n in names if n.split("/")[0].endswith(".dist-info")})
        if len(dis) != 1:
            return problems + ["expected exactly one dist-info directory, found %d" % len(dis)], facts
        di = dis[0]
        facts["dist_info"] = di
        try:
            rec_entries, conflicts = read_record(zf.read(di + "/RECORD").decode("utf-8"))
        except KeyError:
            return problems + ["no RECORD member"], facts
        listed = {}
        for p, alg, digest, size_text in rec_entries:
            listed[p] = (alg, digest, size_text)
        if conflicts:
            problems.append("RECORD conflicts: " + ", ".join(conflicts))
        if listed.get(di + "/RECORD", ("x", "x", "x"))[1] != "":
            problems.append("the RECORD line for RECORD itself is not empty")
        for n in names:
            if n.endswith("/"):
                continue
            if n == di + "/RECORD":
                continue
            if n not in listed:
                problems.append("member not listed in RECORD: " + n)
                continue
            alg, digest, size_text = listed[n]
            h = hashlib.sha256()
            size = 0
            with zf.open(n) as fh:
                while True:
                    chunk = fh.read(CHUNK)
                    if not chunk:
                        break
                    h.update(chunk)
                    size += len(chunk)
            if alg != "sha256" or b64(h.digest()) != digest:
                problems.append("RECORD hash differs from the member: " + n)
            if size_text != str(size):
                problems.append("RECORD size differs from the member: " + n)
        for p in listed:
            if p not in names:
                problems.append("RECORD lists a member the wheel does not hold: " + p)
        try:
            wheel = parse_headers(zf.read(di + "/WHEEL").decode("utf-8"))
            meta = parse_headers(zf.read(di + "/METADATA").decode("utf-8"))
        except (KeyError, UnicodeDecodeError) as exc:
            return problems + ["WHEEL or METADATA unreadable: " + asc(exc)], facts
        tags = [t.strip() for t in (wheel.get_all("Tag") or [])]
        if not wheel.get("Wheel-Version") or not tags:
            problems.append("WHEEL lacks Wheel-Version or Tag")
        if not meta.get("Name") or not meta.get("Version"):
            problems.append("METADATA lacks Name or Version")
        facts.update({"name": (meta.get("Name") or "").strip(), "version": (meta.get("Version") or "").strip(),
                      "tags": tags})
        stem = path.name[:-4] if path.name.endswith(".whl") else path.name
        parts = stem.split("-")
        if len(parts) != 5:
            problems.append("file name does not have five parts: " + path.name)
        else:
            try:
                want_tag = compress_tags(tags)
            except ValueError as exc:
                want_tag = None
                problems.append(str(exc))
            if want_tag and "-".join(parts[2:]) != want_tag:
                problems.append("file name tags %s differ from WHEEL tags %s" % ("-".join(parts[2:]), want_tag))
            if norm_dist(facts["name"]) != parts[0] or norm_version(facts["version"]) != parts[1]:
                problems.append("file name name/version differ from METADATA")
            if di[: -len(".dist-info")].lower() != (parts[0] + "-" + parts[1]).lower() and \
                    norm_dist(di[: -len(".dist-info")].rsplit("-", 1)[0]) != parts[0]:
                problems.append("dist-info directory name does not match the file name")
            if kpw is not None and supported is not None and not kpw.tag_fits("-".join(parts[2:]), supported):
                problems.append("tags do not fit the target: " + "-".join(parts[2:]))
        facts["top_level"] = top_levels(zf)
    return problems, facts


def top_levels(zf):
    """Top-level import names: the wheel's top_level.txt when present, else derived from the member paths."""
    names = zf.namelist()
    found = []
    for n in names:
        segs = n.split("/")
        if len(segs) == 2 and segs[0].endswith(".dist-info") and segs[1] == "top_level.txt":
            for line in zf.read(n).decode("utf-8", "replace").splitlines():
                line = line.strip().replace("/", ".")
                if line and all(s.isidentifier() for s in line.split(".")):
                    found.append(line)
            return sorted(set(found))
    for n in names:
        segs = n.split("/")
        if segs[0].endswith((".dist-info", ".data")) or "__pycache__" in segs:
            continue
        if len(segs) == 1:
            m = re.fullmatch(r"([A-Za-z_]\w*)(?:\.[\w-]+)?\.(?:py|pyd|so)", segs[0])
            if m:
                found.append(m.group(1))
        elif segs[0].isidentifier() and re.search(r"\.(py|pyd|so)$", n):
            found.append(segs[0])
    return sorted(set(found))


# ------------------------------------------------------------------------------------------------------------ repack

def git_commit_of(path):
    try:
        r = subprocess.run(["git", "-C", str(REPO), "log", "-1", "--format=%H", "--", str(path)],
                           capture_output=True, text=True, timeout=30)
        return (r.stdout or "").strip() or "UNKNOWN"
    except (OSError, subprocess.TimeoutExpired):
        return "UNKNOWN"


def inside_git_tree(path):
    p = pathlib.Path(path).resolve()
    for parent in [p] + list(p.parents):
        if (parent / ".git").exists():
            return str(parent)
    return None


def resolve_roots(labels, overrides):
    """Map evidence labels (<site-packages:3.12>) to directories: --root overrides first, then the interpreters this machine
    holds (kit_python_wheels.discover_interpreters)."""
    mapping = dict(overrides)
    need = [lab for lab in labels if lab not in mapping]
    if need:
        sys.path.insert(0, str(HERE))
        try:
            import kit_python_wheels as kpw  # noqa: PLC0415
        finally:
            sys.path.pop(0)
        interps, user_sites, _notes = kpw.discover_interpreters(REPO)
        seen = {}
        for it in interps:
            if it["site_packages"] is None:
                continue
            lab = "<site-packages:%s>" % it["version"]
            seen[lab] = seen.get(lab, 0) + 1
            if seen[lab] > 1:
                lab = "<site-packages:%s#%d>" % (it["version"], seen[lab])
            mapping.setdefault(lab, str(it["site_packages"]))
        for ver, us in user_sites:
            mapping.setdefault("<user-site-packages:%s>" % ver, str(us))
    return mapping


def cmd_repack(args):
    cls_path = pathlib.Path(args.from_file)
    data = json.loads(cls_path.read_text(encoding="utf-8"))
    selected = [r for r in data["requirements"] if r.get("class") in SELECTED_CLASSES]
    out = pathlib.Path(args.out)
    tree = inside_git_tree(out.parent if not out.exists() else out)
    if tree:
        print("ERROR: --out is inside a git tree (%s); the kit is cut outside every git tree" % tree)
        return 2
    if out.exists() and any(out.iterdir()):
        print("ERROR: --out exists and is not empty; the kit goes to a NEW directory: " + str(out))
        return 2
    overrides = {}
    for spec in args.root or []:
        lab, _eq, directory = spec.partition("=")
        overrides[lab] = directory
    labels = sorted({r["evidence"].split("/", 1)[0] for r in selected})
    mapping = resolve_roots(labels, overrides)
    tgt = data.get("target") or {}
    kpw, target, supported = tag_support(tgt.get("python_tag", "cp314"), tgt.get("platform", "win_amd64"))
    target_label = "%s-%s" % (target["python_tag"], target["platform"])
    print("kit_python_repack: %d requirements in %s; %d selected (%s); target %s; claim: measured, offline, no fetch"
          % (len(data["requirements"]), cls_path.name, len(selected), "/".join(SELECTED_CLASSES), target_label))
    plans = []
    failed = []
    for req in selected:
        label, _slash, rel = req["evidence"].partition("/")
        site = mapping.get(label)
        if not site or not pathlib.Path(site, rel).is_dir():
            failed.append({"name": req["name"], "status": "FAILED",
                           "problems": ["evidence %s does not resolve to an installed dist-info on this machine"
                                        % req["evidence"]]})
            print("FAILED %s: evidence %s does not resolve" % (req["name"], req["evidence"]))
            continue
        try:
            plan = plan_package(pathlib.Path(site, rel), site)
        except (OSError, ValueError) as exc:
            failed.append({"name": req["name"], "status": "FAILED", "problems": ["unreadable dist-info: " + asc(exc)]})
            print("FAILED %s: unreadable dist-info: %s" % (req["name"], asc(exc)))
            continue
        plan["req"] = req
        plan["site"] = site
        plan["label"] = label
        plans.append(plan)
    need = sum(p["bytes_in"] for p in plans if not p["modified"])
    parent = out.parent if out.parent.exists() else pathlib.Path(out.anchor or ".")
    free = shutil.disk_usage(parent).free
    remain = free - need
    print("disk: free %.2f GB, up to %.2f GB to write, %.2f GB would remain (floor %s GB)"
          % (free / 1e9, need / 1e9, remain / 1e9, args.min_free_gb))
    if remain < args.min_free_gb * 1e9:
        print("ERROR: fewer than %s GB would remain; stopping before writing anything" % args.min_free_gb)
        return 2
    out.mkdir(parents=True, exist_ok=True)
    wheels = []
    left_out = list(failed)
    built = verified = partial = modified = 0
    total_bytes = 0
    for plan in plans:
        req = plan["req"]
        tag = "%s==%s" % (req["name"], plan["version"])
        if plan["modified"]:
            modified += 1
            left_out.append({"name": req["name"], "version": plan["version"], "status": "MODIFIED",
                             "problems": ["%s: %s" % (p, why) for p, why in plan["modified"]]})
            print("MODIFIED %s left OUT of the kit: %s" % (tag, "; ".join("%s (%s)" % m for m in plan["modified"][:6])))
            continue
        problems = []
        if plan["version"] != req.get("found_version"):
            problems.append("installed version %s differs from the classification's %s"
                            % (plan["version"], req.get("found_version")))
        try:
            fname = wheel_file_name(plan)
        except ValueError as exc:
            fname = None
            problems.append(str(exc))
        if problems:
            left_out.append({"name": req["name"], "version": plan["version"], "status": "FAILED", "problems": problems})
            print("FAILED %s: %s" % (tag, "; ".join(problems)))
            continue
        out_path = out / fname
        built += 1
        try:
            sha_hex, size = write_wheel(plan, out_path)
            probs, facts = verify_wheel(out_path, supported, kpw)
        except (OSError, zipfile.BadZipFile, ValueError) as exc:
            probs, facts, sha_hex, size = ["write failed: " + asc(exc)], {}, "", 0
        if probs:
            if out_path.exists():
                os.remove(out_path)
            left_out.append({"name": req["name"], "version": plan["version"], "status": "FAILED", "problems": probs[:10]})
            print("FAILED %s: wheel did not verify: %s" % (tag, "; ".join(probs[:3])))
            continue
        verified += 1
        is_partial = bool(plan["partial_paths"])
        if is_partial:
            partial += 1
        total_bytes += size
        wheels.append({
            "name": req["name"], "version": plan["version"], "requirement": req.get("line"), "file": fname,
            "sha256": sha_hex, "bytes": size, "tags": plan["tags"], "tag_compressed": compress_tags(plan["tags"]),
            "class": req["class"], "source_interpreter": plan["label"], "evidence": req["evidence"],
            "files": len(plan["items"]) + 1, "partial": is_partial, "partial_paths": plan["partial_paths"],
            "launchers_skipped": plan["launchers_skipped"], "scripts_placed": plan["scripts_placed"],
            "shebangs_restored": plan["shebangs_restored"], "unverified_files": len(plan["unverified"]),
            "pyc_skipped": plan["pyc_skipped"], "top_level": facts.get("top_level", [])})
        print("BUILT %s -> %s %d bytes class=%s files=%d%s%s%s" % (
            tag, fname, size, req["class"], len(plan["items"]) + 1,
            " PARTIAL(%d paths)" % len(plan["partial_paths"]) if is_partial else "",
            " launchers_skipped=%d" % len(plan["launchers_skipped"]) if plan["launchers_skipped"] else "",
            " unverified=%d" % len(plan["unverified"]) if plan["unverified"] else ""))
    req_file = data.get("requirements_file") or {}
    rf_path = REPO / "requirements.txt"
    rf_sha = hashlib.sha256(rf_path.read_bytes()).hexdigest() if rf_path.is_file() else None
    manifest = {
        "schema": SCHEMA,
        "claim": "measured: every wheel was rebuilt offline from an installed copy, hashes of the installed files "
                 "compared with RECORD before packing, each wheel re-opened and verified; nothing was installed or fetched",
        "generated_utc": now_utc(),
        "target": target_label,
        "classification_file": {"name": cls_path.name, "sha256": hashlib.sha256(cls_path.read_bytes()).hexdigest()},
        "requirements_file": {"path": "requirements.txt", "commit": git_commit_of(rf_path),
                              "sha256_now": rf_sha, "sha256_at_classification": req_file.get("sha256"),
                              "unchanged_since_classification": bool(rf_sha and rf_sha == req_file.get("sha256"))},
        "counts": {"selected": len(selected), "built": built, "verified": verified, "partial": partial,
                   "modified": modified, "failed": len(failed) + (built - verified), "bytes": total_bytes},
        "wheels": wheels,
        "left_out": left_out,
    }
    (out / "MANIFEST.json").write_text(json.dumps(manifest, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    kept = {w["name"]: w for w in wheels}
    lines = ["%s==%s" % (r["name"], kept[r["name"]]["version"]) for r in selected if r["name"] in kept]
    (out / "requirements-kit.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    nfailed = manifest["counts"]["failed"]
    ok = built == verified and nfailed == 0
    print("PY-REPACK target=%s selected=%d built=%d verified=%d partial=%d modified=%d failed=%d bytes=%d ok=%s"
          % (target_label, len(selected), built, verified, partial, modified, nfailed, total_bytes, ok))
    return 0 if ok else 1


# ------------------------------------------------------------------------------------------------------ verify (Dell)

def load_manifest(folder):
    mp = pathlib.Path(folder, "MANIFEST.json")
    if not mp.is_file():
        return None
    return json.loads(mp.read_text(encoding="utf-8"))


def verify_folder(folder):
    """Return (rows, stray, n_wheels, n_ok). rows: per wheel (file, ok, why)."""
    folder = pathlib.Path(folder)
    manifest = load_manifest(folder)
    if manifest is None:
        return [("MANIFEST.json", False, "absent")], [], 0, 0
    rows = []
    listed = {"MANIFEST.json", "requirements-kit.txt"}
    for w in manifest.get("wheels", []):
        listed.add(w["file"])
        p = folder / w["file"]
        if not p.is_file():
            rows.append((w["file"], False, "missing"))
            continue
        _b, hexd, size = sha256_file(p)
        if hexd != w["sha256"]:
            rows.append((w["file"], False, "sha256 differs from the manifest"))
        elif size != w["bytes"]:
            rows.append((w["file"], False, "size differs from the manifest"))
        else:
            rows.append((w["file"], True, "ok"))
    expected = ["%s==%s" % (w["name"], w["version"]) for w in manifest.get("wheels", [])]
    rq = folder / "requirements-kit.txt"
    if not rq.is_file() or [ln.strip() for ln in rq.read_text(encoding="utf-8").splitlines() if ln.strip()] != expected:
        rows.append(("requirements-kit.txt", False, "absent or differs from the manifest's wheel list"))
    stray = sorted(n for n in os.listdir(folder) if n not in listed)
    n = len(manifest.get("wheels", []))
    return rows, stray, n, sum(1 for r in rows if r[1] and r[0].endswith(".whl"))


def dell_commands(folder):
    folder = str(pathlib.Path(folder))
    me = "python org/devices/kit_python_repack.py"
    return [
        "%s verify --from %s" % (me, folder),
        "%s install-check --from %s --scratch <a NEW scratch folder>" % (me, folder),
        "(by hand, the same install into a scratch target) %s" % " ".join(
            pip_install_cmd(folder, "<scratch>", exe="python")),
        "(the real install, on the Dell's own decision) python -m pip install --no-index --no-deps --find-links %s "
        "-r %s --user" % (folder, str(pathlib.Path(folder, "requirements-kit.txt"))),
    ]


def cmd_verify(args):
    rows, stray, n, n_ok = verify_folder(args.from_)
    for name, ok, why in rows:
        print("%s %s %s" % ("OK:" if ok else "FAIL:", name, "" if ok else why))
    for name in stray:
        print("FAIL: stray file the manifest does not list: " + name)
    ok = bool(rows) and all(r[1] for r in rows) and not stray and n > 0
    print("commands a Dell runs, in order:")
    for i, cmd in enumerate(dell_commands(args.from_), 1):
        print("  %d. %s" % (i, cmd))
    print("PY-KIT-VERIFY wheels=%d verified=%d stray=%d ok=%s" % (n, n_ok, len(stray), ok))
    return 0 if ok else 1


# ---------------------------------------------------------------------------------------------------- install-check

def pip_install_cmd(folder, scratch, exe=None):
    """The ONE pip command this tool constructs. --no-index and --no-deps are always present (asserted)."""
    cmd = [exe or sys.executable, "-m", "pip", "install", "--no-index", "--no-deps", "--find-links", str(folder),
           "-r", str(pathlib.Path(folder, "requirements-kit.txt")), "--target", str(scratch)]
    assert "--no-index" in cmd and "--no-deps" in cmd and "--target" in cmd
    return cmd


def pip_one_cmd(folder, scratch, requirement):
    cmd = [sys.executable, "-m", "pip", "install", "--no-index", "--no-deps", "--find-links", str(folder),
           requirement, "--target", str(scratch)]
    assert "--no-index" in cmd and "--no-deps" in cmd
    return cmd


IMPORT_SNIPPET = ("import sys, importlib\nsys.path.insert(0, sys.argv[1])\nimportlib.import_module(sys.argv[2])\n")


ANSI_ESCAPE = re.compile(r"\x1b\[[0-9;?]*[A-Za-z]")


def import_one(scratch_dirs, module):
    """One import in its own subprocess. Returns ('ok', '') | ('missing', module) | ('failed', first error line)."""
    code = IMPORT_SNIPPET.replace("sys.path.insert(0, sys.argv[1])",
                                  "[sys.path.insert(0, p) for p in sys.argv[1].split(%r)[::-1]]" % os.pathsep)
    cmd = [sys.executable, "-c", code, os.pathsep.join(str(s) for s in scratch_dirs), module]
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    env.pop("FORCE_COLOR", None)
    env["NO_COLOR"] = "1"
    env["PYTHON_COLORS"] = "0"
    try:
        r = subprocess.run(cmd, capture_output=True, timeout=IMPORT_BOUND, cwd=str(scratch_dirs[0]), env=env)
    except subprocess.TimeoutExpired:
        return "failed", "timeout after %d s" % IMPORT_BOUND
    except OSError as exc:
        return "failed", asc(exc)
    if r.returncode == 0:
        return "ok", ""
    lines = [ANSI_ESCAPE.sub("", ln) for ln in r.stderr.decode("utf-8", "replace").splitlines() if ln.strip()]
    last = asc(lines[-1]) if lines else "exit %d with no message" % r.returncode
    m = re.search(r"ModuleNotFoundError: No module named '([^']+)'", last)
    if m:
        return "missing", m.group(1)
    return "failed", last[:200]


def cmd_install_check(args):
    folder = pathlib.Path(args.from_)
    manifest = load_manifest(folder)
    if manifest is None:
        print("ERROR: no MANIFEST.json in " + str(folder))
        return 2
    scratch = pathlib.Path(args.scratch) if args.scratch else pathlib.Path(tempfile.mkdtemp(prefix="kit-py-scratch-"))
    if scratch.exists() and any(scratch.iterdir()):
        print("ERROR: --scratch exists and is not empty; use a NEW folder: " + str(scratch))
        return 2
    scratch.mkdir(parents=True, exist_ok=True)
    wheels = manifest.get("wheels", [])
    reqs = [ln.strip() for ln in pathlib.Path(folder, "requirements-kit.txt").read_text(encoding="utf-8").splitlines()
            if ln.strip()]
    cmd = pip_install_cmd(folder, scratch)
    print("RUN: " + " ".join(cmd))
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=1800)
    tails = (r.stdout or "").strip().splitlines()[-1:] + (r.stderr or "").strip().splitlines()[-3:]
    print("pip rc=%d: %s" % (r.returncode, asc(" | ".join(tails))))
    installed = {}
    dirs_by_name = {}
    if r.returncode == 0:
        for w in wheels:
            installed[w["name"]] = True
            dirs_by_name[w["name"]] = [scratch]
    else:
        print("the one install failed; installing each requirement on its own to find which wheel will not install")
        for i, req in enumerate(reqs):
            sub = scratch / ("one-%03d" % i)
            rr = subprocess.run(pip_one_cmd(folder, sub, req), capture_output=True, text=True, timeout=900)
            name = req.split("==")[0]
            installed[name] = rr.returncode == 0
            if rr.returncode != 0:
                tail = (rr.stderr or rr.stdout).strip().splitlines()[-1:] or [""]
                print("NOT INSTALLED %s: %s" % (req, asc(tail[0])[:200]))
        dirs_by_name = {n: [scratch / d for d in sorted(os.listdir(scratch)) if d.startswith("one-")] or [scratch]
                        for n in installed}
    n_installed = n_imported = n_missing = n_failed_import = n_nomod = 0
    for w in wheels:
        name = w["name"]
        if not installed.get(name):
            print("%s==%s not_installed" % (name, w["version"]))
            continue
        n_installed += 1
        with zipfile.ZipFile(folder / w["file"]) as zf:
            tops = top_levels(zf)
        if not tops:
            n_nomod += 1
            print("%s==%s installed no_module (a namespace or data-only distribution; nothing to import)"
                  % (name, w["version"]))
            continue
        statuses = [(t,) + import_one(dirs_by_name[name], t) for t in tops]
        # a module of the package's OWN top-level names that cannot be found is a broken wheel, not a missing dependency
        statuses = [(s[0], "failed", "own module missing: " + s[2]) if s[1] == "missing" and s[2].split(".")[0] in tops
                    else s for s in statuses]
        failed = [s for s in statuses if s[1] == "failed"]
        missing = [s for s in statuses if s[1] == "missing"]
        if failed:
            n_failed_import += 1
            print("%s==%s installed import_failed: %s: %s" % (name, w["version"], failed[0][0], failed[0][2]))
        elif missing:
            n_missing += 1
            print("%s==%s installed import_missing_dep: missing %s (importing %s)"
                  % (name, w["version"], missing[0][2], missing[0][0]))
        else:
            n_imported += 1
            print("%s==%s installed imported [%s]" % (name, w["version"], ",".join(tops)))
    n_failed = (len(wheels) - n_installed) + n_failed_import
    ok = n_installed == len(wheels)
    print("accounting: wheels=%d = installed %d + not installed %d; installed %d = imported %d + import_missing_dep %d + "
          "no_module %d + import_failed %d" % (len(wheels), n_installed, len(wheels) - n_installed, n_installed,
                                                n_imported, n_missing, n_nomod, n_failed_import))
    print("scratch target: %s (the Dell's real environment was not touched)" % scratch)
    print("PY-KIT-INSTALL python=%s wheels=%d installed=%d imported=%d import_missing_dep=%d failed=%d ok=%s"
          % ("%d.%d.%d" % sys.version_info[:3], len(wheels), n_installed, n_imported, n_missing, n_failed, ok))
    return 0 if ok else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="verb", required=True)
    rp = sub.add_parser("repack")
    rp.add_argument("--out", required=True)
    rp.add_argument("--from-file", default=str(DEFAULT_CLASSIFICATION))
    rp.add_argument("--root", action="append", help="LABEL=DIR, overrides where an evidence label resolves")
    rp.add_argument("--min-free-gb", type=float, default=10.0)
    vp = sub.add_parser("verify")
    vp.add_argument("--from", dest="from_", required=True)
    ip = sub.add_parser("install-check")
    ip.add_argument("--from", dest="from_", required=True)
    ip.add_argument("--scratch")
    args = ap.parse_args(argv)
    return {"repack": cmd_repack, "verify": cmd_verify, "install-check": cmd_install_check}[args.verb](args)


if __name__ == "__main__":
    sys.exit(main())
