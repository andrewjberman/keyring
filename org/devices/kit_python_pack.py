"""kit_python_pack.py -- the laptop packs the Python distributions a Dell lacks, from what is ALREADY on this disk
(NFRA_CTLPLN PRD v0.14 C-KIT-PYTHON, cell CT-k-2).

    python org/devices/kit_python_pack.py --for <installed.json> --out <dir> [--wheelhouse <dir> ...] [--no-pip-check]

`<installed.json>` is the output of `kit_python_census.py installed --out` run on the TARGET box. For each distribution the target lacks
(and each of ITS dependencies the target also lacks, read recursively from THIS box's installed metadata Requires-Dist) the packer
produces one installable wheel, by order of preference:

  (a) a wheel already on this disk -- pip's local `wheels` cache, any directory named with --wheelhouse or in KIT_WHEELHOUSE -- that
      is the laptop's installed version and fits the target's Python tag and platform (found without the network);
  (b) a wheel rebuilt from the INSTALLED files via the distribution's RECORD. A PURE-Python distribution (WHEEL says
      Root-Is-Purelib: true and a `-none-any` tag, and ships no .pyd/.dll/.so/.exe) is always rebuildable. A COMPILED one is rebuilt
      only when the target's Python minor version and platform tag equal this machine's, and the manifest says so;
  (c) UNPACKABLE <name> <reason>.

It REFUSES OUTRIGHT, writing nothing, when the target's Python minor version or platform tag differs from this machine's and any
distribution to pack is compiled. NO PACKAGE INDEX, NO NETWORK: nothing here constructs a pip download or a wheel-by-name; the one pip
call (a self-check, `--dry-run`) goes through kit_python_install.build_pip_cmd, which always carries `--no-index`.
Writes MANIFEST.json (file, sha256, size, distribution, version, how) beside the wheels. Nothing is committed.
"""
from __future__ import annotations

import argparse
import base64
import csv
import hashlib
import io
import json
import os
import pathlib
import subprocess
import sys
import zipfile
import importlib.metadata as md

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import kit_python_census as census  # noqa: E402
import kit_python_install as install  # noqa: E402

try:
    from packaging.requirements import Requirement
except ImportError:  # pragma: no cover
    from pip._vendor.packaging.requirements import Requirement

COMPILED_SUFFIXES = (".pyd", ".dll", ".so", ".dylib", ".exe")
SKIP_NAMES = {"INSTALLER", "REQUESTED", "RECORD", "direct_url.json"}
FIXED_TIME = (1980, 1, 1, 0, 0, 0)


class Unpackable(Exception):
    pass


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def record_hash(data):
    return "sha256=" + base64.urlsafe_b64encode(hashlib.sha256(data).digest()).rstrip(b"=").decode("ascii")


# ---------------------------------------------------------------- reading a laptop distribution


def get_dist(name):
    try:
        return md.distribution(name)
    except md.PackageNotFoundError:
        return None


def wheel_info(dist):
    txt = dist.read_text("WHEEL") or ""
    purelib = None
    tags = []
    for line in txt.splitlines():
        k, _, v = line.partition(":")
        if k.strip() == "Root-Is-Purelib":
            purelib = v.strip().lower() == "true"
        elif k.strip() == "Tag":
            tags.append(v.strip())
    return {"purelib": purelib, "tags": tags}


def record_entries(dist):
    """[(normalised posix path, hash or None)] from RECORD, deduplicated, .pyc and __pycache__ dropped."""
    txt = dist.read_text("RECORD")
    if txt is None:
        raise Unpackable("no RECORD in the installed metadata")
    seen = {}
    for row in csv.reader(io.StringIO(txt)):
        if not row or not row[0]:
            continue
        p = row[0].replace("\\", "/")
        if p.endswith(".pyc") or "/__pycache__/" in p:
            continue
        h = row[1] if len(row) > 1 and row[1] else None
        if p not in seen or (seen[p] is None and h):
            seen[p] = h
    return sorted(seen.items())


def is_compiled(dist):
    """True when the distribution is platform- or interpreter-specific: WHEEL says so, or it ships .pyd/.dll/.so/.exe files."""
    w = wheel_info(dist)
    if w["purelib"] is False:
        return True
    if any(not t.endswith("-none-any") for t in w["tags"]):
        return True
    try:
        entries = record_entries(dist)
    except Unpackable:
        return False
    console = console_script_names(dist)
    for p, _h in entries:
        base = p.rsplit("/", 1)[-1]
        if p.startswith("..") and (base[:-4] if base.lower().endswith(".exe") else base) in console:
            continue  # a console-script launcher pip generates; not shipped compiled code
        low = p.lower()
        if low.endswith(COMPILED_SUFFIXES) or ".so." in low:
            return True
    return False


def console_script_names(dist):
    out = set()
    txt = dist.read_text("entry_points.txt") or ""
    sect = None
    for line in txt.splitlines():
        line = line.strip()
        if line.startswith("[") and line.endswith("]"):
            sect = line[1:-1]
        elif sect in ("console_scripts", "gui_scripts") and "=" in line:
            out.add(line.split("=")[0].strip())
    return out


def wheel_filename(dist, name_norm):
    """name-version-pytag-abitag-platformtag.whl, the WHEEL file's Tag lines compressed (py2.py3-none-any)."""
    tags = wheel_info(dist)["tags"] or ["py3-none-any"]
    cols = [[], [], []]
    for t in tags:
        for i, part in enumerate(t.split("-")[-3:]):
            if part not in cols[i]:
                cols[i].append(part)
    return "%s-%s-%s.whl" % (name_norm.replace("-", "_"), dist.version, "-".join(".".join(c) for c in cols))


def rebuild_wheel(dist, name_norm, out_dir):
    """Rebuild a wheel from the installed files named in RECORD. Raises Unpackable with the reason."""
    entries = record_entries(dist)
    distinfo = None
    for rel, _h in entries:
        top = rel.split("/")[0]
        if top.endswith(".dist-info"):
            distinfo = top
            break
    if distinfo is None:
        raise Unpackable("RECORD names no .dist-info directory")
    datadir = distinfo[: -len(".dist-info")] + ".data"
    data_hash = {rel.rsplit("/", 1)[-1]: h for rel, h in entries if rel.startswith(datadir + "/scripts/")}
    console = console_script_names(dist)
    files = {}  # archive name -> bytes
    for rel, rec_hash in entries:
        base = rel.rsplit("/", 1)[-1]
        if rel.split("/")[0].endswith(".dist-info") and base in SKIP_NAMES:
            continue
        if rel.startswith(".."):
            parts = [x for x in rel.split("/") if x != ".."]
            top = parts[0] if parts else ""
            if top in ("Scripts", "bin"):
                stem = base[:-4] if base.lower().endswith(".exe") else base
                if stem in console or base in console or base.endswith("-script.py"):
                    continue  # a console-script launcher: pip regenerates it from entry_points.txt
                arc = "%s/scripts/%s" % (datadir, base)
                rec_hash = rec_hash or data_hash.get(base)
            elif top in ("Include", "include") and len(parts) > 1:
                arc = "%s/headers/%s" % (datadir, "/".join(parts[1:]))
            elif top in ("share", "etc") and len(parts) > 1:
                arc = "%s/data/%s" % (datadir, "/".join(parts))
            else:
                raise Unpackable("RECORD entry outside site-packages that is not under Scripts/bin, Include, share or etc: %s" % rel)
        else:
            arc = rel
        loc = pathlib.Path(str(dist.locate_file(rel)))
        if not loc.is_file():
            if rel.startswith(datadir + "/"):
                continue  # the .data copy is not on disk; the Scripts/bin entry carries the same file
            raise Unpackable("RECORD lists a file that is not on disk: %s" % rel)
        data = loc.read_bytes()
        if rec_hash and rec_hash.startswith("sha256=") and record_hash(data) != rec_hash:
            raise Unpackable("an installed file differs from its RECORD hash (modified after install): %s" % rel)
        files[arc] = data
    for need in ("METADATA", "WHEEL"):
        if "%s/%s" % (distinfo, need) not in files:
            raise Unpackable("the installed dist-info lacks %s" % need)
    dest = pathlib.Path(out_dir) / wheel_filename(dist, name_norm)
    rec = io.StringIO()
    w = csv.writer(rec, lineterminator="\n")
    for arc in sorted(files):
        w.writerow([arc, record_hash(files[arc]), len(files[arc])])
    w.writerow(["%s/RECORD" % distinfo, "", ""])
    with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as z:
        for arc, data in sorted(files.items()) + [("%s/RECORD" % distinfo, rec.getvalue().encode("utf-8"))]:
            zi = zipfile.ZipInfo(arc, FIXED_TIME)
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o644 << 16
            z.writestr(zi, data)
    return dest


# ---------------------------------------------------------------- (a) wheels already on disk


def pip_cache_dirs():
    env = os.environ.get("PIP_CACHE_DIR")
    cands = []
    if env:
        cands.append(pathlib.Path(env))
    if sys.platform == "win32":
        la = os.environ.get("LOCALAPPDATA")
        if la:
            cands.append(pathlib.Path(la) / "pip" / "cache")
    elif sys.platform == "darwin":
        cands.append(pathlib.Path.home() / "Library" / "Caches" / "pip")
    else:
        cands.append(pathlib.Path(os.environ.get("XDG_CACHE_HOME") or (pathlib.Path.home() / ".cache")) / "pip")
    return [c / "wheels" for c in cands if (c / "wheels").is_dir()]


def wheelhouse_dirs(extra):
    dirs = [pathlib.Path(x) for x in (extra or [])]
    for x in os.environ.get("KIT_WHEELHOUSE", "").split(os.pathsep):
        if x:
            dirs.append(pathlib.Path(x))
    dirs.extend(pip_cache_dirs())
    return [d for d in dirs if d.is_dir()]


def fits_target(filename, name_norm, version, target):
    parts = filename[:-4].split("-")
    if len(parts) < 5:
        return False
    nm, ver = parts[0], parts[1]
    pytag, abi, plat = parts[-3], parts[-2], parts[-1]
    if census.norm(nm) != name_norm or ver != version:
        return False
    minor = target["python_minor"].replace(".", "")
    if not any(t in ("py3", "py" + minor, "cp" + minor) or t.startswith("py3") and t[3:] in ("", minor)
               for t in pytag.split(".")):
        return False
    if not any(a in ("none", "abi3", "cp" + minor) for a in abi.split(".")):
        return False
    plats = plat.split(".")
    return "any" in plats or target["platform_tag"] in plats


def find_cached_wheel(name_norm, version, target, dirs):
    for d in dirs:
        for p in sorted(d.rglob("*.whl")):
            if fits_target(p.name, name_norm, version, target):
                return p
    return None


# ---------------------------------------------------------------- the closure


def dependency_names(dist, target):
    """Normalised names this distribution requires, markers evaluated against the TARGET's Python and platform."""
    env = {"extra": "", "python_version": target["python_minor"], "python_full_version": target["python_version"],
           "sys_platform": target["sys_platform"]}
    out = []
    for line in dist.requires or []:
        r = Requirement(line)
        if r.marker is not None and not r.marker.evaluate(env):
            continue
        out.append(census.norm(r.name))
    return out


def closure(missing, target):
    """Breadth-first: missing distributions plus the dependencies the target lacks. Returns (order, parents, unpackable)."""
    have = {k for k, v in target["distributions"].items() if v}
    have |= set(target.get("all_installed", {}))
    order, parent, unpackable = [], {}, {}
    queue = [(m, None) for m in missing]
    while queue:
        name, by = queue.pop(0)
        if name in parent or name in unpackable:
            continue
        dist = get_dist(name)
        if dist is None:
            unpackable[name] = {"reason": "this machine does not have it installed either", "required_by": by}
            continue
        parent[name] = by
        order.append(name)
        for dep in dependency_names(dist, target):
            if dep not in have:
                queue.append((dep, name))
    return order, parent, unpackable


# ---------------------------------------------------------------- the pack


def build_verify_cmd(wheels):
    """The pack's one pip call: a --dry-run self-check of the wheel files just written (never an install, never the network)."""
    return install.build_pip_cmd([str(w) for w in wheels], find_links=None, user=False, dry_run=True, extra=["--no-deps", "--ignore-installed"])


def optional_modules(required_path=None):
    try:
        req = census.load_required(required_path)
    except (OSError, ValueError):
        return set()
    return {"module:" + m["module"] for m in req.get("not_installed_modules", []) if m["usage"] == "OPTIONAL"}


def pack(target, out_dir, wheelhouse=None, pip_check=True, required_path=None):
    here = census.box_facts()
    same = target["python_minor"] == here["python_minor"] and target["platform_tag"] == here["platform_tag"]
    req_missing = sorted(k for k, v in target["distributions"].items() if not v and not k.startswith("module:"))
    mod_missing = sorted(k for k, v in target.get("modules_importable", {}).items() if not v)
    order, parent, unpackable = closure(req_missing, target)
    for mname in mod_missing:
        unpackable["module:" + mname] = {"reason": "an importable module with no distribution on this machine (not on pip, not installed here)",
                                         "required_by": None}
    compiled = {n: is_compiled(get_dist(n)) for n in order}
    result = {"target": target.get("device"), "missing": len(req_missing) + len(mod_missing), "packed": 0,
              "dependencies": 0, "unpackable": len(unpackable), "bytes": 0, "ok": False, "refused": False, "lines": []}
    if not same and any(compiled.values()):
        names = sorted(n for n, c in compiled.items() if c)
        result["refused"] = True
        result["lines"].append("REFUSED: target python %s / %s differs from this machine's %s / %s and %d distribution(s) to pack are "
                               "compiled: %s. A compiled wheel is not portable across interpreters or platforms; nothing was written."
                               % (target["python_minor"], target["platform_tag"], here["python_minor"], here["platform_tag"],
                                  len(names), ", ".join(names)))
        return result
    out = pathlib.Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    dirs = wheelhouse_dirs(wheelhouse)
    result["lines"].append("wheel sources on disk (no network): %s" % (", ".join(str(d) for d in dirs) or "none found"))
    entries = []
    for name in order:
        dist = get_dist(name)
        ver = dist.version
        src = find_cached_wheel(name, ver, target, dirs)
        try:
            if src is not None:
                dest = out / src.name
                dest.write_bytes(src.read_bytes())
                how = "cached-wheel:%s" % src
            elif compiled[name] and not same:
                raise Unpackable("compiled and the target's python/platform differ")
            else:
                dest = rebuild_wheel(dist, name, out)
                how = ("rebuilt-from-installed-files (COMPILED distribution; target python %s and platform %s equal this machine's)"
                       % (here["python_minor"], here["platform_tag"])) if compiled[name] else "rebuilt-from-installed-files (pure Python)"
        except Unpackable as e:
            unpackable[name] = {"reason": str(e), "required_by": parent.get(name)}
            result["lines"].append("UNPACKABLE %s %s" % (name, e))
            continue
        entries.append({"file": dest.name, "sha256": sha256_file(dest), "size": dest.stat().st_size, "distribution": name,
                        "version": ver, "how": how, "compiled": compiled[name], "required_by": parent.get(name)})
        result["lines"].append("PACKED %s %s -> %s (%s)" % (name, ver, dest.name, how))
    for name, info in sorted(unpackable.items()):
        if not any(ln.startswith("UNPACKABLE %s " % name) for ln in result["lines"]):
            result["lines"].append("UNPACKABLE %s %s" % (name, info["reason"]))
    result["packed"] = len(entries)
    result["dependencies"] = sum(1 for e in entries if e["required_by"] is not None)
    result["unpackable"] = len(unpackable)
    result["bytes"] = sum(e["size"] for e in entries)
    check_ok = True
    if pip_check and entries:
        cmd = build_verify_cmd([out / e["file"] for e in entries])
        r = subprocess.run(cmd, capture_output=True, text=True, check=False)
        check_ok = r.returncode == 0
        result["lines"].append("pip self-check (--no-index --dry-run, rc=%d): %s" % (r.returncode, " ".join(cmd[:6]) + " ..."))
        if not check_ok:
            result["lines"].append("pip said: %s" % (r.stdout + r.stderr).strip()[-600:])
    manifest = {"schema": "kit_python_manifest/1", "target_device": target.get("device"),
                "target_python_minor": target["python_minor"], "target_platform_tag": target["platform_tag"],
                "packed_on": {"python_version": here["python_version"], "platform_tag": here["platform_tag"]},
                "files": entries,
                "unpackable": [{"name": k, **v} for k, v in sorted(unpackable.items())],
                "directly_missing": req_missing + ["module:" + m for m in mod_missing]}
    (out / "MANIFEST.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    optional_gone = optional_modules(required_path)
    hard_unpackable = [k for k in unpackable if k not in optional_gone]
    if len(hard_unpackable) != len(unpackable):
        result["lines"].append("note: %d UNPACKABLE item(s) are OPTIONAL imports with no distribution (%s); they are counted and do not fail ok"
                               % (len(unpackable) - len(hard_unpackable), ", ".join(sorted(set(unpackable) - set(hard_unpackable)))))
    result["ok"] = check_ok and not hard_unpackable
    return result


def last_line(r):
    return ("KIT-PACK target=%s missing=%d packed=%d dependencies=%d unpackable=%d bytes=%d ok=%s"
            % (r["target"], r["missing"], r["packed"], r["dependencies"], r["unpackable"], r["bytes"], r["ok"]))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--for", dest="target", required=True, help="installed.json from the target box")
    ap.add_argument("--out", required=True)
    ap.add_argument("--wheelhouse", action="append")
    ap.add_argument("--no-pip-check", action="store_true")
    ap.add_argument("--required", help="the required json (default: the committed one)")
    args = ap.parse_args(argv)
    target = json.loads(pathlib.Path(args.target).read_text(encoding="utf-8"))
    r = pack(target, args.out, args.wheelhouse, pip_check=not args.no_pip_check, required_path=args.required)
    for line in r["lines"]:
        print(line)
    print(last_line(r))
    return 0 if r["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
