"""kit_python_wheels.py -- for each line of the root requirements.txt, is there ON THIS MACHINE (no fetch) a wheel that
Python 3.14 on 64-bit Windows can install?

NO NETWORK. This tool makes no request to any package index. The only pip invocations it constructs are the read-only
`pip cache dir`, `pip cache list`, `pip config list` and `pip --version` (see PIP_ALLOWED; a test asserts it). It never
installs, downloads, builds or re-packs anything: it classifies.

Verbs:
  required                          parse requirements.txt and compare with org/devices/kit_python_required.json.
  wheels --python-tag cp314 --platform win_amd64 [--out <json>] [--from-file <json>]
                                    classify every requirement; write the JSON; print the last line.
                                    --from-file re-prints the last line from a saved JSON (the bounded form).

Classes (exactly one per requirement; precedence in this order):
  NOT-APPLICABLE  the environment marker excludes the target (Python 3.14 on win32/AMD64).
  WHEEL-ON-DISK   a .whl file on this machine whose *.dist-info/WHEEL Tag lines include a tag the target supports.
  ABI3-INSTALLED  no file, but an installed build that fits and is not pure Python: a stable-ABI build (cp3X-abi3-win_amd64,
                  X <= 14), or a build tagged for the platform with no Python ABI (py3-none-win_amd64), or native cp314.
  PURE-INSTALLED  no file, but an installed pure-Python copy (Root-Is-Purelib true, a py*-none-any tag, a RECORD) that can
                  be re-packed into a wheel offline.
  NEEDS-FETCH     compiled for another Python only, absent, or an installed copy with no wheel metadata.
  UNPARSED        a line that cannot be parsed.
(PURE-INSTALLED outranks ABI3-INSTALLED when one copy could be either; the order above is the order of the task order.)

Compatibility is decided with the `packaging` library's tag logic (packaging.tags) computed for the TARGET, not the running
interpreter. Evidence paths are stored relative to a named root (<pip-cache>, <site-packages:3.12>, <downloads>, <repo>,
<repo-base>, <tmp-kit>), resolved only at run time; no home-directory path is written to the JSON.
It does NOT follow dependencies: for each found copy it prints the Requires-Dist names that are not lines of requirements.txt.
"""
from __future__ import annotations

import argparse
import datetime
import email.parser
import hashlib
import io
import json
import os
import pathlib
import re
import subprocess
import sys
import tempfile
import time
import zipfile

try:
    from packaging import tags as ptags
    from packaging.markers import InvalidMarker, UndefinedComparison, UndefinedEnvironmentName
    from packaging.requirements import InvalidRequirement, Requirement
    from packaging.specifiers import InvalidSpecifier, SpecifierSet
    from packaging.utils import canonicalize_name
    from packaging.version import InvalidVersion, Version
    HAVE_PACKAGING = True
except ImportError:  # pragma: no cover - this box has packaging; the fallback is stated in the output
    HAVE_PACKAGING = False

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
DEFAULT_OUT = HERE / "kit_python_wheels_cp314.json"
CENSUS_JSON = HERE / "kit_python_required.json"
SCHEMA = "kit_python_wheels/1"

# Every pip command this tool constructs must be one of these (read-only, no request to an index). Recorded in PIP_LOG.
PIP_ALLOWED = (("--version",), ("cache", "dir"), ("cache", "list"), ("config", "list"))
PIP_LOG: list = []

CLASS_ORDER = ("NOT-APPLICABLE", "WHEEL-ON-DISK", "ABI3-INSTALLED", "PURE-INSTALLED", "NEEDS-FETCH", "UNPARSED")
PRUNE = {"node_modules", ".git", "__pycache__", ".venv", "venv", ".tox", ".mypy_cache", ".ruff_cache"}


def asc(text):
    return str(text).encode("ascii", "replace").decode("ascii")


def norm(name):
    return re.sub(r"[-_.]+", "-", str(name)).lower()


# --------------------------------------------------------------------------------------------------------------- target

def parse_target(python_tag, platform):
    m = re.fullmatch(r"cp(\d)(\d+)", python_tag)
    if not m:
        raise SystemExit("ERROR: --python-tag must look like cp314")
    ver = (int(m.group(1)), int(m.group(2)))
    plat_env = {
        "win_amd64": ("win32", "Windows", "nt", "AMD64"),
        "win32": ("win32", "Windows", "nt", "x86"),
        "win_arm64": ("win32", "Windows", "nt", "ARM64"),
    }
    if platform not in plat_env:
        raise SystemExit("ERROR: only the Windows platform tags win_amd64, win32, win_arm64 are supported")
    sys_platform, system, os_name, machine = plat_env[platform]
    env = {
        "python_version": "%d.%d" % ver,
        "python_full_version": "%d.%d.0" % ver,
        "implementation_name": "cpython",
        "platform_python_implementation": "CPython",
        "implementation_version": "%d.%d.0" % ver,
        "sys_platform": sys_platform,
        "platform_system": system,
        "os_name": os_name,
        "platform_machine": machine,
        "platform_release": "",
        "platform_version": "",
        "extra": "",
    }
    return {"python_tag": python_tag, "platform": platform, "version": ver, "env": env}


def supported_tags(target):
    """The set of (interpreter, abi, platform) triples Python <target> on <platform> installs, from packaging.tags."""
    ver, plat = target["version"], [target["platform"]]
    py_tag = target["python_tag"]
    out = set()
    for t in ptags.cpython_tags(python_version=ver, abis=[py_tag], platforms=plat):
        out.add((t.interpreter, t.abi, t.platform))
    for t in ptags.compatible_tags(python_version=ver, interpreter=py_tag, platforms=plat):
        out.add((t.interpreter, t.abi, t.platform))
    return out


def tag_fits(tag_str, supported):
    """tag_str is a possibly compressed tag ('py2.py3-none-any'); true when ANY expansion is supported."""
    fits = []
    for t in ptags.parse_tag(tag_str):
        trip = (t.interpreter, t.abi, t.platform)
        if trip in supported:
            fits.append(trip)
    return fits


# ------------------------------------------------------------------------------------------------------------ requirements

def strip_comment(line):
    return re.sub(r"(^|\s+)#.*$", "", line).strip()


def read_requirement_lines(path):
    """Return (installable [(lineno, text)], options [(lineno, text)], total_physical_lines)."""
    raw = pathlib.Path(path).read_bytes().decode("utf-8", "replace").splitlines()
    installable, options = [], []
    i = 0
    while i < len(raw):
        lineno = i + 1
        text = strip_comment(raw[i])
        while text.endswith("\\") and i + 1 < len(raw):
            i += 1
            text = text[:-1] + " " + strip_comment(raw[i])
        i += 1
        if not text:
            continue
        if text.startswith("-"):
            options.append((lineno, text))
        else:
            installable.append((lineno, text))
    return installable, options, len(raw)


def parse_requirement(text, target):
    """Return a dict: ok, name, specifier, extras, marker, applicable, error."""
    try:
        req = Requirement(text)
    except (InvalidRequirement, ValueError) as exc:
        return {"ok": False, "error": asc(exc).splitlines()[0][:160], "raw": text}
    applicable = True
    marker = str(req.marker) if req.marker is not None else None
    if req.marker is not None:
        try:
            applicable = bool(req.marker.evaluate(dict(target["env"])))
        except (UndefinedComparison, UndefinedEnvironmentName, InvalidMarker, TypeError, ValueError) as exc:
            return {"ok": False, "error": "marker: " + asc(exc)[:140], "raw": text}
    return {"ok": True, "name": req.name, "norm": canonicalize_name(req.name), "specifier": str(req.specifier),
            "extras": sorted(req.extras), "marker": marker, "applicable": applicable, "raw": text,
            "_req": req}


# ----------------------------------------------------------------------------------------------------- metadata readers

def parse_metadata_text(text):
    msg = email.parser.Parser().parsestr(text, headersonly=True)
    return msg


def wheel_info_from_texts(meta_text, wheel_text):
    msg = parse_metadata_text(meta_text)
    wmsg = parse_metadata_text(wheel_text) if wheel_text is not None else None
    tags = []
    purelib = None
    if wmsg is not None:
        tags = [t.strip() for t in (wmsg.get_all("Tag") or [])]
        rp = (wmsg.get("Root-Is-Purelib") or "").strip().lower()
        purelib = True if rp == "true" else False if rp == "false" else None
    return {"name": (msg.get("Name") or "").strip(), "version": (msg.get("Version") or "").strip(),
            "requires": [str(r).strip() for r in (msg.get_all("Requires-Dist") or [])],
            "tags": tags, "purelib": purelib, "has_wheel_file": wmsg is not None}


def read_wheel_zip(zf):
    """Identify a wheel by its *.dist-info/WHEEL and METADATA members, never by a file name. None when it is not a wheel."""
    names = zf.namelist()
    wheel_members = [n for n in names if n.count("/") == 1 and n.endswith(".dist-info/WHEEL")]
    meta_members = [n for n in names if n.count("/") == 1 and n.endswith(".dist-info/METADATA")]
    if not wheel_members or not meta_members:
        return None
    wt = zf.read(wheel_members[0]).decode("utf-8", "replace")
    mt = zf.read(meta_members[0]).decode("utf-8", "replace")
    info = wheel_info_from_texts(mt, wt)
    if not info["name"]:
        return None
    return info


def open_possible_wheel(path, size, max_prefix=4096, max_whole=268435456):
    """Return (info|None, status) where status is one of 'wheel', 'zip-not-wheel', 'not-zip', 'unreadable'.

    A cached HTTP body may carry a small header before the zip: try the file as a zip first (zipfile tolerates a prefix),
    then locate the PK signature in the first kilobytes and open the slice from there."""
    try:
        with zipfile.ZipFile(path) as zf:
            info = read_wheel_zip(zf)
            return (info, "wheel") if info else (None, "zip-not-wheel")
    except zipfile.BadZipFile:
        pass
    except (OSError, ValueError, KeyError, RuntimeError, NotImplementedError):
        return None, "unreadable"
    try:
        with open(path, "rb") as fh:
            head = fh.read(max_prefix)
            off = head.find(b"PK\x03\x04")
            if off < 0:
                return None, "not-zip"
            if size > max_whole:
                return None, "unreadable"
            fh.seek(off)
            data = fh.read()
        with zipfile.ZipFile(io.BytesIO(data)) as zf:
            info = read_wheel_zip(zf)
            return (info, "wheel") if info else (None, "zip-not-wheel")
    except zipfile.BadZipFile:
        return None, "not-zip"
    except (OSError, ValueError, KeyError, RuntimeError, NotImplementedError, MemoryError):
        return None, "unreadable"


# ------------------------------------------------------------------------------------------------------------- roots

class Roots:
    """Named roots: evidence is stored as <name>/relative, resolved only at run time."""

    def __init__(self):
        self.items = []  # (label, pathlib.Path)

    def add(self, label, path):
        try:
            p = pathlib.Path(path).resolve()
        except OSError:
            p = pathlib.Path(path)
        self.items.append((label, p))

    def rel(self, path):
        p = pathlib.Path(path)
        try:
            p = p.resolve()
        except OSError:
            pass
        best = None
        for label, root in self.items:
            try:
                r = p.relative_to(root)
            except ValueError:
                continue
            if best is None or len(root.parts) > len(best[1].parts):
                best = (label, root, r)
        if best is None:
            return "<other>/" + p.name
        return best[0] + "/" + best[2].as_posix()


def run_pip(args, timeout=60):
    """Run ONE read-only pip command. Refuses anything not in PIP_ALLOWED."""
    key = tuple(args)
    if key not in PIP_ALLOWED:
        raise SystemExit("ERROR: refused pip command not in the read-only allow-list: pip " + " ".join(args))
    cmd = [sys.executable, "-m", "pip"] + list(args)
    PIP_LOG.append(cmd)
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return r.returncode, (r.stdout or "").strip()
    except (OSError, subprocess.TimeoutExpired) as exc:
        return 124, "ERROR: " + asc(exc)


def git_base(repo):
    """<base> = the first entry of `git worktree list --porcelain` (derived, never hardcoded)."""
    try:
        r = subprocess.run(["git", "-C", str(repo), "worktree", "list", "--porcelain"], capture_output=True, text=True,
                           timeout=30)
    except (OSError, subprocess.TimeoutExpired):
        return None
    for line in (r.stdout or "").splitlines():
        if line.startswith("worktree "):
            return pathlib.Path(line[len("worktree "):].strip())
    return None


# ------------------------------------------------------------------------------------------------- wheel-file sources

def find_whl_files(root, deadline, stats_key, stats):
    """os.walk for *.whl under root, pruning heavy trees; bounded by deadline. Returns list of paths."""
    out = []
    stack = [str(root)]
    while stack:
        if time.time() > deadline:
            stats[stats_key + "_budget_cut"] = True
            break
        cur = stack.pop()
        try:
            with os.scandir(cur) as it:
                for ent in it:
                    try:
                        if ent.is_dir(follow_symlinks=False):
                            if ent.name not in PRUNE:
                                stack.append(ent.path)
                        elif ent.name.lower().endswith(".whl"):
                            out.append(ent.path)
                    except OSError:
                        stats[stats_key + "_scan_errors"] = stats.get(stats_key + "_scan_errors", 0) + 1
            stats[stats_key + "_dirs"] = stats.get(stats_key + "_dirs", 0) + 1
        except OSError:
            stats[stats_key + "_scan_errors"] = stats.get(stats_key + "_scan_errors", 0) + 1
    return out


def scan_pip_cache(cache_dir, budget_bytes, deadline):
    """Read every file in the pip cache by size ascending until the byte budget or deadline. Counts everything."""
    res = {"present": False, "entries": 0, "bytes_total": 0, "entries_read": 0, "bytes_read": 0, "wheels": 0,
           "zip_not_wheel": 0, "not_zip": 0, "unreadable": 0, "not_read_budget": 0, "wheel_infos": []}
    if not cache_dir or not os.path.isdir(cache_dir):
        return res
    res["present"] = True
    files = []
    for r, _d, fs in os.walk(cache_dir):
        for f in fs:
            p = os.path.join(r, f)
            try:
                files.append((os.path.getsize(p), p))
            except OSError:
                res["unreadable"] += 1
                res["entries"] += 1
    res["entries"] += len(files)
    res["bytes_total"] = sum(s for s, _ in files)
    files.sort()
    for size, p in files:
        if res["bytes_read"] + size > budget_bytes or time.time() > deadline:
            res["not_read_budget"] += 1
            continue
        info, status = open_possible_wheel(p, size)
        res["entries_read"] += 1
        res["bytes_read"] += size
        if status == "wheel":
            res["wheels"] += 1
            res["wheel_infos"].append((p, size, info))
        elif status == "zip-not-wheel":
            res["zip_not_wheel"] += 1
        elif status == "not-zip":
            res["not_zip"] += 1
        else:
            res["unreadable"] += 1
    return res


def scan_wheel_files(paths):
    """Open each .whl by its members. Returns (infos [(path,size,info)], unreadable, not_wheel)."""
    infos, unreadable, not_wheel = [], 0, 0
    for p in paths:
        try:
            size = os.path.getsize(p)
        except OSError:
            unreadable += 1
            continue
        info, status = open_possible_wheel(p, size)
        if status == "wheel":
            infos.append((p, size, info))
        elif status == "unreadable":
            unreadable += 1
        else:
            not_wheel += 1
    return infos, unreadable, not_wheel


# --------------------------------------------------------------------------------------------- installed distributions

def scan_site_packages(sp_dir):
    """Read every *.dist-info (and *.egg-info) in a site-packages directory. No code is executed."""
    out = []
    unreadable = 0
    try:
        entries = sorted(os.listdir(sp_dir))
    except OSError:
        return out, 1
    for name in entries:
        full = os.path.join(sp_dir, name)
        if name.endswith(".dist-info") and os.path.isdir(full):
            try:
                mt = pathlib.Path(full, "METADATA").read_bytes().decode("utf-8", "replace")
            except OSError:
                unreadable += 1
                continue
            wt = None
            wp = pathlib.Path(full, "WHEEL")
            if wp.is_file():
                try:
                    wt = wp.read_bytes().decode("utf-8", "replace")
                except OSError:
                    wt = None
            info = wheel_info_from_texts(mt, wt)
            info["has_record"] = pathlib.Path(full, "RECORD").is_file()
            info["editable"] = False
            du = pathlib.Path(full, "direct_url.json")
            if du.is_file():
                try:
                    info["editable"] = bool(json.loads(du.read_text(encoding="utf-8", errors="replace"))
                                            .get("dir_info", {}).get("editable"))
                except (OSError, ValueError, AttributeError):
                    pass
            info["path"] = full
            info["kind"] = "dist-info"
            if info["name"]:
                out.append(info)
        elif name.endswith(".egg-info"):
            pi = pathlib.Path(full, "PKG-INFO") if os.path.isdir(full) else pathlib.Path(full)
            try:
                mt = pi.read_bytes().decode("utf-8", "replace")
            except OSError:
                unreadable += 1
                continue
            info = wheel_info_from_texts(mt, None)
            info.update({"has_record": False, "editable": False, "path": full, "kind": "egg-info"})
            if info["name"]:
                out.append(info)
    return out, unreadable


def discover_interpreters(repo):
    """List the Python interpreters this machine holds and their site-packages: `py -0p`, the registry's PythonCore keys,
    the running interpreter, and the standard install folders. Reports a folder with no interpreter as such."""
    found = {}  # key (resolved root str) -> dict

    def add(root, source, exe=None, ver=None):
        try:
            rp = pathlib.Path(root).resolve()
        except OSError:
            rp = pathlib.Path(root)
        key = str(rp).lower()
        d = found.setdefault(key, {"root": rp, "sources": [], "exe": None, "version": None})
        if source not in d["sources"]:
            d["sources"].append(source)
        if exe and not d["exe"]:
            d["exe"] = exe
        if ver and not d["version"]:
            d["version"] = ver

    py_cmd = ["py", "-0p"]
    try:
        r = subprocess.run(py_cmd, capture_output=True, text=True, timeout=30)
        for line in (r.stdout or "").splitlines():
            m = re.match(r"\s*-V:(\S+)\s+\*?\s*(.+?)\s*$", line) or re.match(r"\s*-(\d+\.\d+)\S*\s+\*?\s*(.+?)\s*$", line)
            if m and os.path.isfile(m.group(2)):
                add(pathlib.Path(m.group(2)).parent, "py -0p", exe=m.group(2), ver=m.group(1))
    except (OSError, subprocess.TimeoutExpired):
        pass
    add(pathlib.Path(sys.executable).parent, "running interpreter", exe=sys.executable,
        ver="%d.%d" % sys.version_info[:2])
    reg_notes = []
    try:
        import winreg  # noqa: PLC0415 - Windows only
        for hive, hname in ((winreg.HKEY_CURRENT_USER, "HKCU"), (winreg.HKEY_LOCAL_MACHINE, "HKLM")):
            try:
                with winreg.OpenKey(hive, r"Software\Python\PythonCore") as k:
                    i = 0
                    while True:
                        try:
                            vname = winreg.EnumKey(k, i)
                        except OSError:
                            break
                        i += 1
                        try:
                            with winreg.OpenKey(k, vname + r"\InstallPath") as ip:
                                path = winreg.QueryValueEx(ip, "")[0]
                            if os.path.isdir(path):
                                add(path, "registry " + hname, ver=vname.split("-")[0])
                                reg_notes.append("%s PythonCore %s: InstallPath present" % (hname, vname))
                            else:
                                reg_notes.append("%s PythonCore %s: InstallPath names a folder that does not exist"
                                                 % (hname, vname))
                        except OSError:
                            reg_notes.append("%s PythonCore %s: no InstallPath" % (hname, vname))
            except OSError:
                pass
    except ImportError:
        pass
    cands = []
    for env in ("LOCALAPPDATA", "ProgramFiles", "ProgramFiles(x86)"):
        base = os.environ.get(env)
        if not base:
            continue
        for sub in ((pathlib.Path(base) / "Programs" / "Python"), pathlib.Path(base)):
            try:
                for ent in sub.iterdir():
                    if re.fullmatch(r"Python3\d+(-\d+)?", ent.name) and ent.is_dir():
                        cands.append(ent)
            except OSError:
                pass
    for c in cands:
        m = re.fullmatch(r"Python(3)(\d+)", c.name)
        add(c, "standard folder", ver=("%s.%s" % (m.group(1), m.group(2))) if m else None)
    interps = []
    for d in found.values():
        root = d["root"]
        exe = d["exe"] or (str(root / "python.exe") if (root / "python.exe").is_file() else None)
        ver = d["version"]
        if exe and os.path.isfile(exe) and not ver:
            ver = "?"
        sp = root / "Lib" / "site-packages"
        interps.append({"root": root, "version": ver or "?", "exe_present": bool(exe and os.path.isfile(exe)),
                        "site_packages": sp if sp.is_dir() else None, "sources": d["sources"]})
    # user site-packages for each version, when present
    appdata = os.environ.get("APPDATA")
    user_sites = []
    if appdata:
        for it in interps:
            m = re.fullmatch(r"3\.(\d+)", it["version"])
            if m:
                us = pathlib.Path(appdata) / "Python" / ("Python3" + m.group(1)) / "site-packages"
                if us.is_dir() and (it["version"], us) not in user_sites:
                    user_sites.append((it["version"], us))
    interps.sort(key=lambda x: (x["version"], str(x["root"])))
    return interps, user_sites, reg_notes


# ------------------------------------------------------------------------------------------------------------ classify

def best_by_version(cands, spec):
    """Prefer a copy that satisfies the specifier, then the highest version."""
    def key(c):
        try:
            v = Version(c["info"]["version"])
        except InvalidVersion:
            v = Version("0")
        sat = c.get("satisfies")
        return (1 if sat else 0, v)
    return sorted(cands, key=key, reverse=True)


def satisfies(spec_text, version_text):
    try:
        spec = SpecifierSet(spec_text) if spec_text else None
    except InvalidSpecifier:
        return None
    if spec is None or not str(spec):
        return True
    try:
        return spec.contains(Version(version_text), prereleases=True)
    except InvalidVersion:
        return None


def undeclared_names(info, req_parsed, declared, target):
    """Requires-Dist names (marker evaluated for the target, extras of the requirement) not lines of requirements.txt."""
    names = set()
    extras = set(req_parsed.get("extras") or [])
    for rd in info.get("requires", []):
        try:
            r = Requirement(rd)
        except (InvalidRequirement, ValueError):
            continue
        ok = True
        if r.marker is not None:
            ok = False
            for ex in ([""] + sorted(extras)):
                env = dict(target["env"])
                env["extra"] = ex
                try:
                    if r.marker.evaluate(env):
                        ok = True
                        break
                except (UndefinedComparison, UndefinedEnvironmentName, TypeError, ValueError):
                    continue
        if ok:
            n = canonicalize_name(r.name)
            if n not in declared:
                names.add(n)
    return sorted(names)


def classify_installed(info, supported):
    """Return (class, fit_kind, reason, tags, fit_tags) for ONE installed copy."""
    if info.get("editable"):
        return "NEEDS-FETCH", None, "editable install (no wheel can be re-packed from it)", info["tags"], []
    if not info["has_wheel_file"] or not info["tags"]:
        return "NEEDS-FETCH", None, "no wheel metadata", [], []
    fit = []
    for t in info["tags"]:
        fit.extend(tag_fits(t, supported))
    if not fit:
        return "NEEDS-FETCH", None, "compiled for another Python only: " + ", ".join(info["tags"]), info["tags"], []
    pure_fit = [t for t in fit if t[2] == "any"]
    if info["purelib"] is True and pure_fit:
        if not info.get("has_record"):
            return "NEEDS-FETCH", None, "pure-Python tag but no RECORD to re-pack from", info["tags"], fit
        return "PURE-INSTALLED", "pure", None, info["tags"], fit
    if any(t[1] == "abi3" for t in fit):
        return "ABI3-INSTALLED", "abi3", None, info["tags"], fit
    if any(t[1] == "none" and t[2] != "any" for t in fit):
        return "ABI3-INSTALLED", "no-abi-platform", None, info["tags"], fit
    if any(t[1].startswith("cp") for t in fit):
        return "ABI3-INSTALLED", "native-target", None, info["tags"], fit
    return "NEEDS-FETCH", None, "tags fit but not pure and not re-packable: " + ", ".join(info["tags"]), info["tags"], fit


def classify_requirement(parsed, wheel_index, installed_index, supported, declared, target, roots):
    entry = {"name": parsed.get("name"), "specifier": parsed.get("specifier"), "marker": parsed.get("marker"),
             "extras": parsed.get("extras"), "line": parsed.get("raw"), "class": None, "evidence": None,
             "found_version": None, "satisfies": None, "tags": [], "fit_kind": None, "reason": None,
             "other_copies": [], "undeclared_deps": []}
    if not parsed.get("ok"):
        entry.update({"class": "UNPARSED", "reason": parsed.get("error")})
        return entry
    if not parsed["applicable"]:
        entry.update({"class": "NOT-APPLICABLE", "reason": "marker excludes the target: " + str(parsed["marker"])})
        return entry
    n = parsed["norm"]
    spec_text = parsed["specifier"]
    # 1. wheel files that fit
    wheels = []
    non_fit = []
    for path, size, info in wheel_index.get(n, []):
        fit = []
        for t in info["tags"]:
            fit.extend(tag_fits(t, supported))
        c = {"path": path, "info": info, "fit": fit, "satisfies": satisfies(spec_text, info["version"])}
        (wheels if fit else non_fit).append(c)
    installed = installed_index.get(n, [])
    chosen_info = None
    if wheels:
        best = best_by_version(wheels, spec_text)[0]
        info = best["info"]
        entry.update({"class": "WHEEL-ON-DISK", "evidence": roots.rel(best["path"]), "found_version": info["version"],
                      "satisfies": best["satisfies"], "tags": info["tags"],
                      "fit_kind": "wheel file; fitting tags: " + ", ".join("-".join(t) for t in best["fit"])})
        chosen_info = info
    else:
        scored = []
        for c in installed:
            klass, kind, reason, tags, fit = classify_installed(c["info"], supported)
            scored.append({"class": klass, "kind": kind, "reason": reason, "tags": tags, "fit": fit, "info": c["info"],
                           "label": c["label"], "satisfies": satisfies(spec_text, c["info"]["version"])})
        rank = {"ABI3-INSTALLED": 0, "PURE-INSTALLED": 1, "NEEDS-FETCH": 2}
        if scored:
            scored.sort(key=lambda s: (rank[s["class"]], 0 if s["satisfies"] else 1))
            best = scored[0]
            entry.update({"class": best["class"], "evidence": roots.rel(best["info"]["path"]),
                          "found_version": best["info"]["version"], "satisfies": best["satisfies"], "tags": best["tags"],
                          "fit_kind": best["kind"], "reason": best["reason"]})
            chosen_info = best["info"]
            for s in scored[1:]:
                entry["other_copies"].append({"evidence": roots.rel(s["info"]["path"]), "version": s["info"]["version"],
                                              "class": s["class"]})
        else:
            reason = "absent: no wheel file and no installed copy on this machine"
            if non_fit:
                reason = "wheel files found but none fits the target"
            entry.update({"class": "NEEDS-FETCH", "reason": reason})
    for c in non_fit:
        entry["other_copies"].append({"evidence": roots.rel(c["path"]), "version": c["info"]["version"],
                                      "class": "wheel-not-fitting", "tags": c["info"]["tags"]})
    if chosen_info is not None:
        entry["undeclared_deps"] = undeclared_names(chosen_info, parsed, declared, target)
    return entry


def last_line(target_label, entries, undeclared):
    counts = {k: 0 for k in CLASS_ORDER}
    for e in entries:
        counts[e["class"]] = counts.get(e["class"], 0) + 1
    classified = sum(1 for e in entries if e["class"] in CLASS_ORDER)
    ok = classified == len(entries) and counts["UNPARSED"] == 0
    return ("PY-WHEELS target=%s requirements=%d wheel_on_disk=%d pure_installed=%d abi3_installed=%d needs_fetch=%d "
            "not_applicable=%d unparsed=%d undeclared_deps=%d ok=%s"
            % (target_label, len(entries), counts["WHEEL-ON-DISK"], counts["PURE-INSTALLED"], counts["ABI3-INSTALLED"],
               counts["NEEDS-FETCH"], counts["NOT-APPLICABLE"], counts["UNPARSED"], len(undeclared), ok)), ok


def classify_all(req_lines, wheel_infos, installed_dists, target, roots, supported):
    """Pure core (the test drives it): req_lines [(lineno,text)], wheel_infos [(path,size,info)],
    installed_dists [(label, info)]. Returns (entries, undeclared)."""
    parsed = []
    for lineno, text in req_lines:
        p = parse_requirement(text, target)
        p["lineno"] = lineno
        parsed.append(p)
    declared = {p["norm"] for p in parsed if p.get("ok")}
    wheel_index, installed_index = {}, {}
    for path, size, info in wheel_infos:
        wheel_index.setdefault(canonicalize_name(info["name"]), []).append((path, size, info))
    for label, info in installed_dists:
        installed_index.setdefault(canonicalize_name(info["name"]), []).append({"label": label, "info": info})
    entries = []
    for p in parsed:
        e = classify_requirement(p, wheel_index, installed_index, supported, declared, target, roots)
        e["lineno"] = p["lineno"]
        entries.append(e)
    und = {}
    for e in entries:
        for d in e["undeclared_deps"]:
            und.setdefault(d, []).append(norm(e["name"]))
    return entries, und


# ------------------------------------------------------------------------------------------------------- the wheels verb

def scrub_check(text):
    """The saved JSON must not bake a user name or home path."""
    home = str(pathlib.Path.home())
    user = os.environ.get("USERNAME") or os.environ.get("USER") or ""
    low = text.lower()
    bad = []
    for needle in {home.lower(), home.replace("\\", "/").lower(), home.replace("\\", "\\\\").lower(),
                   user.lower() if len(user) > 2 else None}:
        if needle and needle in low:
            bad.append(needle[:3] + "...")
    return bad


def cmd_wheels(args):
    if args.from_file:
        data = json.loads(pathlib.Path(args.from_file).read_text(encoding="utf-8"))
        ents = data["requirements"]
        und = data["undeclared_deps"]
        ll, ok = last_line(data["target"]["label"], ents, und)
        print("(re-printed from " + asc(args.from_file) + "; saved " + data.get("generated_utc", "?") + ")")
        print(ll)
        return 0 if ok else 1
    if not HAVE_PACKAGING:
        print("ERROR: the packaging library is not installed here; this build of the tool needs it")
        return 2
    t0 = time.time()
    target = parse_target(args.python_tag, args.platform)
    supported = supported_tags(target)
    label = "%s-%s" % (args.python_tag, args.platform)
    req_path = pathlib.Path(args.requirements) if args.requirements else REPO / "requirements.txt"
    req_lines, options, physical = read_requirement_lines(req_path)
    print("Target: %s (Python %d.%d on %s), tag logic: packaging %s, %d supported tags"
          % (label, target["version"][0], target["version"][1], args.platform,
             __import__("packaging").__version__, len(supported)))
    print("requirements.txt: %d physical lines, %d installable lines, %d options lines"
          % (physical, len(req_lines), len(options)))
    for ln, o in options:
        print("  OPTION line %d: %s (printed, counted, not followed)" % (ln, asc(o)))
    print("NOTE: dependencies of the listed packages are NOT followed; the file is stated to be the full list "
          "(its caveat: a clean-start resolve is unverified).")

    roots = Roots()
    deadline = t0 + args.budget_seconds
    stats = {}
    rc, pip_ver = run_pip(["--version"])
    rc2, cache_dir = run_pip(["cache", "dir"])
    cache_dir = cache_dir if rc2 == 0 else ""
    rc3, cache_list = run_pip(["cache", "list"])
    rc4, cfg = run_pip(["config", "list"])
    base = git_base(REPO)
    tmp_parents = []
    for cand in (pathlib.Path(REPO.anchor) / "tmp", REPO.parent, pathlib.Path(tempfile.gettempdir())):
        try:
            cand = cand.resolve()
        except OSError:
            continue
        if cand.is_dir() and cand not in tmp_parents:
            tmp_parents.append(cand)
    kit_dirs = []
    for tp in tmp_parents:
        try:
            for ent in tp.iterdir():
                if ent.name.startswith("kit-") and ent.is_dir() and ent not in kit_dirs:
                    kit_dirs.append(ent)
        except OSError:
            pass
    downloads = pathlib.Path.home() / "Downloads"

    if cache_dir:
        roots.add("<pip-cache>", cache_dir)
    for kd in kit_dirs:
        roots.add("<tmp-kit>/" + kd.name, kd)
    roots.add("<downloads>", downloads)
    roots.add("<repo>", REPO)
    if base:
        roots.add("<repo-base>", base)

    # sources of wheel FILES
    sources = []
    cache_res = scan_pip_cache(cache_dir, args.cache_budget_mb * 1024 * 1024, deadline)
    wheel_infos = [(p, s, i) for p, s, i in cache_res["wheel_infos"]]
    sources.append({"source": "pip HTTP and wheel cache", "root": "<pip-cache>", "present": cache_res["present"],
                    "entries": cache_res["entries"], "bytes_total": cache_res["bytes_total"],
                    "entries_read": cache_res["entries_read"], "bytes_read": cache_res["bytes_read"],
                    "not_read_budget": cache_res["not_read_budget"], "wheels_identified": cache_res["wheels"],
                    "zip_not_wheel": cache_res["zip_not_wheel"], "not_zip": cache_res["not_zip"],
                    "unreadable": cache_res["unreadable"]})
    file_sources = [("kit pack output (C:/tmp/kit-*)", kit_dirs), ("user Downloads folder", [downloads] if downloads.is_dir() else []),
                    ("repository (this worktree)", [REPO]), ("repository (base checkout)", [base] if base else [])]
    for name, dirs in file_sources:
        whl = []
        key = re.sub(r"\W+", "_", name)
        for d in dirs:
            whl.extend(find_whl_files(d, deadline, key, stats))
        infos, unread, notw = scan_wheel_files(whl)
        wheel_infos.extend(infos)
        sources.append({"source": name, "roots": len(dirs), "dirs_walked": stats.get(key + "_dirs", 0),
                        "whl_files_found": len(whl), "wheels_identified": len(infos), "unreadable": unread,
                        "not_a_wheel": notw, "walk_budget_cut": bool(stats.get(key + "_budget_cut")),
                        "walk_errors": stats.get(key + "_scan_errors", 0)})
    # installed distributions
    interps, user_sites, reg_notes = discover_interpreters(REPO)
    installed = []
    interp_rows = []
    seen_labels = {}
    for it in interps:
        ver = it["version"]
        lab = "<site-packages:%s>" % ver
        seen_labels[lab] = seen_labels.get(lab, 0) + 1
        if seen_labels[lab] > 1:
            lab = "<site-packages:%s#%d>" % (ver, seen_labels[lab])
        n_dists, unread = 0, 0
        if it["site_packages"]:
            roots.add(lab, it["site_packages"])
            dists, unread = scan_site_packages(str(it["site_packages"]))
            n_dists = len(dists)
            installed.extend((lab, d) for d in dists)
        interp_rows.append({"version": ver, "interpreter_exe_present": it["exe_present"],
                            "site_packages_present": bool(it["site_packages"]), "root_label": lab,
                            "found_by": it["sources"], "distributions_read": n_dists, "unreadable": unread})
    for ver, us in user_sites:
        lab = "<user-site-packages:%s>" % ver
        roots.add(lab, us)
        dists, unread = scan_site_packages(str(us))
        installed.extend((lab, d) for d in dists)
        interp_rows.append({"version": ver, "interpreter_exe_present": True, "site_packages_present": True,
                            "root_label": lab, "found_by": ["user site"], "distributions_read": len(dists),
                            "unreadable": unread})

    entries, und = classify_all(req_lines, wheel_infos, installed, target, roots, supported)
    ll, ok = last_line(label, entries, und)
    counts = {k: 0 for k in CLASS_ORDER}
    for e in entries:
        counts[e["class"]] += 1

    print("Sources (each counted):")
    for s in sources:
        print("  " + asc(json.dumps(s, sort_keys=True)))
    print("Interpreters this machine holds (%d); registry notes: %s" % (len(interp_rows), asc("; ".join(reg_notes) or "none")))
    for r in interp_rows:
        print("  " + asc(json.dumps(r, sort_keys=True)))
    print("pip (read-only calls only): %s | cache list: %s" % (asc(pip_ver.splitlines()[0] if pip_ver else "?"),
                                                             asc(cache_list.splitlines()[0] if cache_list else "?")))
    print("%-24s %-16s %-16s %-14s %s" % ("requirement", "specifier", "class", "found", "evidence / reason"))
    for e in entries:
        print("%-24s %-16s %-16s %-14s %s" % (asc(e["name"] or e["line"])[:24], asc(e["specifier"] or "")[:16], e["class"],
                                              asc(e["found_version"] or "-")[:14],
                                              asc((e["evidence"] or "") + (" | " + e["reason"] if e["reason"] else ""))[:140]))
    for e in entries:
        if e["class"] in ("PURE-INSTALLED", "WHEEL-ON-DISK", "ABI3-INSTALLED") and e["satisfies"] is False:
            print("NOT-SATISFYING %s found %s specifier %s (%s)" % (asc(e["name"]), e["found_version"], e["specifier"],
                                                                   e["class"]))
    print("Requires-Dist names that are NOT lines of requirements.txt (count %d): %s"
          % (len(und), asc(", ".join(sorted(und)) or "none")))

    result = {
        "schema": SCHEMA,
        "claim": "measured: a read of files on this machine; no request to any package index was made",
        "generated_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "target": {"label": label, "python_tag": args.python_tag, "platform": args.platform,
                   "supported_tag_count": len(supported), "tag_logic": "packaging.tags " + __import__("packaging").__version__},
        "running_python": "%d.%d.%d" % sys.version_info[:3],
        "requirements_file": {"physical_lines": physical, "installable_lines": len(req_lines),
                              "sha256": hashlib.sha256(req_path.read_bytes()).hexdigest(),
                              "options_lines": [{"line": ln, "text": asc(o)} for ln, o in options]},
        "dependencies_followed": False,
        "pip_commands_run": [" ".join(c[1:]) for c in PIP_LOG],
        "pip_cache_list_first_line": asc(cache_list.splitlines()[0] if cache_list else ""),
        "pip_config_list_lines": len([x for x in cfg.splitlines() if x.strip()]) if rc4 == 0 else None,
        "sources": sources,
        "interpreters": interp_rows,
        "registry_notes": [asc(x) for x in reg_notes],
        "counts": counts,
        "requirements": [{k: v for k, v in e.items() if k != "_req"} for e in entries],
        "undeclared_deps": {k: sorted(v) for k, v in sorted(und.items())},
        "last_line": ll,
        "elapsed_seconds": round(time.time() - t0, 1),
    }
    text = json.dumps(result, indent=1, sort_keys=True, ensure_ascii=True) + "\n"
    leaks = scrub_check(text)
    if leaks:
        print("ERROR: the result would bake a user path or name into the saved file (%s); not written" % leaks)
        return 2
    out = pathlib.Path(args.out) if args.out else DEFAULT_OUT
    out.write_text(text, encoding="ascii")
    print("Wrote " + out.name + " (%d bytes) in %.1f s" % (len(text), time.time() - t0))
    print(ll)
    return 0 if ok else 1


# ------------------------------------------------------------------------------------------------------- required verb

def cmd_required(args):
    if not HAVE_PACKAGING:
        print("ERROR: the packaging library is not installed here")
        return 2
    target = parse_target("cp314", "win_amd64")
    req_path = pathlib.Path(args.requirements) if args.requirements else REPO / "requirements.txt"
    lines, options, physical = read_requirement_lines(req_path)
    parsed = [parse_requirement(t, target) for _ln, t in lines]
    bad = [(ln, p) for (ln, _t), p in zip(lines, parsed) if not p.get("ok")]
    for ln, o in options:
        print("OPTION line %d: %s (printed, counted, not followed)" % (ln, asc(o)))
    for ln, p in bad:
        print("UNPARSED line %d: %s -- %s" % (ln, asc(p.get("raw")), p.get("error")))
    req_names = {p["norm"]: p["name"] for p in parsed if p.get("ok")}
    census_path = pathlib.Path(args.census) if args.census else CENSUS_JSON
    census = json.loads(census_path.read_text(encoding="utf-8"))
    cen_names = {canonicalize_name(d["distribution"]): d["distribution"] for d in census["distributions"]}
    both = sorted(set(req_names) & set(cen_names))
    only_req = sorted(set(req_names) - set(cen_names))
    only_cen = sorted(set(cen_names) - set(req_names))
    print("physical lines %d, installable lines %d, options lines %d" % (physical, len(lines), len(options)))
    print("IN BOTH (%d): %s" % (len(both), asc(", ".join(both))))
    print("ONLY IN requirements.txt (%d): %s" % (len(only_req), asc(", ".join(only_req))))
    print("ONLY IN the cell's own census (%d): %s" % (len(only_cen), asc(", ".join(only_cen))))
    ok = not bad
    print("PY-REQ lines=%d parsed=%d unparsed=%d in_both=%d only_requirements=%d only_census=%d ok=%s"
          % (len(lines), len(lines) - len(bad), len(bad), len(both), len(only_req), len(only_cen), ok))
    return 0 if ok else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="verb", required=True)
    r = sub.add_parser("required", help="parse requirements.txt and compare with the cell's own census")
    r.add_argument("--requirements")
    r.add_argument("--census")
    w = sub.add_parser("wheels", help="classify each requirement against wheels on this machine (no fetch)")
    w.add_argument("--python-tag", default="cp314")
    w.add_argument("--platform", default="win_amd64")
    w.add_argument("--out")
    w.add_argument("--from-file")
    w.add_argument("--requirements")
    w.add_argument("--budget-seconds", type=int, default=420)
    w.add_argument("--cache-budget-mb", type=int, default=2048)
    a = ap.parse_args(argv)
    if a.verb == "required":
        return cmd_required(a)
    return cmd_wheels(a)


if __name__ == "__main__":
    sys.exit(main())
