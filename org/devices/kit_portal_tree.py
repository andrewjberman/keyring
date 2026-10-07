"""kit_portal_tree.py -- the portal dependency-tree kit (NFRA_CTLPLN PRD v0.14 C-KIT-PYTHON, TO-CT-k-2 AMENDMENT 2).

A box that may not fetch from a package registry cannot `bun install` the web portal. This kit DESCRIBES the dependency tree
(`node_modules`) that is ALREADY on this machine against the portal's lockfile, PACKS it into one archive with a manifest, VERIFIES
and EXTRACTS such a pack on the receiving box (refusing a differing lockfile, tool version or platform), and runs the portal's own
typecheck script as the read-back. Pure stdlib. NO NETWORK: no command this tool constructs is a package-manager fetch verb, names a
registry address, or runs `npx`; the only subprocesses are `git` read verbs, `bun --version`, `node --version`, and
`bun run --no-install <script>` for the typecheck (a test asserts the list).

    python org/devices/kit_portal_tree.py describe  [--portal <dir>] [--json <file>]
    python org/devices/kit_portal_tree.py pack      --out <dir> [--portal <dir>]
    python org/devices/kit_portal_tree.py verify    --from <dir> --portal <dir> [--extract] [--replace]
    python org/devices/kit_portal_tree.py typecheck --portal <dir> [--timeout <sec>] [--script <name>]

HOW "PACKAGES THE LOCKFILE NAMES" IS DERIVED (bun.lock, lockfileVersion 1, text but JSONC: it carries trailing commas, which are
stripped OUTSIDE string literals by a small scanner before json.loads; comments are stripped likewise): the top-level `packages`
object. Each KEY is an install path relative to the top node_modules: `react`, `@babel/core`, and for a nested install
`@babel/core/@babel/parser` meaning node_modules/@babel/core/node_modules/@babel/parser. Each VALUE is an array whose first element is
`<name>@<spec>`; the first dict in the array is the package's metadata (os, cpu, bin, dependencies, ...). A spec that begins with a
digit is a registry version (compared exactly with the version in the on-disk package.json); any other spec (a tarball URL, workspace:,
file:, npm: alias) is matched by name only. The `workspaces` and `overrides` sections name no installs and are not counted.

CLASSIFICATION of every lock entry (the counts are printed):
  PRESENT                  on disk at its key path with the locked version (or, for a non-registry spec, the name)
  RELOCATED                not at its key path, but the same name@version is elsewhere in the tree (counted present)
  OPTIONAL-OTHER-PLATFORM  absent, and the entry's own `os` / `cpu` markers exclude this machine (win32 / x64 as Node names them;
                           a `!x` value is a block list), or an ancestor entry in the key path is so excluded
  WORKSPACE                spec begins with `workspace:` (linked, not installed): not counted absent
  VERSION-DIFFERS          at its key path with another version: counted ABSENT (the locked version is not present)
  ABSENT                   should be present on this platform and is not
`present` = PRESENT + RELOCATED; `absent` = ABSENT + VERSION-DIFFERS. A package on disk that no lock entry names is EXTRA (reported,
never failing). The lockfile SHA-256 is taken over the file with CRLF folded to LF, so a checkout's line endings cannot make two
identical lockfiles differ; the raw-byte SHA-256 is printed beside it.

PACK FORMAT: tar, gzip level 1 (tarfile w:gz, compresslevel=1). node_modules is mostly JavaScript text, which gzip shrinks several-fold
even at level 1, and the archive crosses the tailnet once per Dell, so smaller wins; level 1 keeps pack time near the disk's speed
where level 9 costs several times as long for a few percent more. Symlinks and junctions are never followed; one whose target
resolves INSIDE the tree is stored as a relative symlink, any other is NOT carried and is listed in the manifest and the output.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import pathlib
import platform
import re
import shutil
import subprocess
import sys
import tarfile
import time

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
MANIFEST = "MANIFEST.json"
ARCHIVE = "portal_node_modules.tar.gz"
LOCK_CANDIDATES = ("bun.lock", "bun.lockb", "package-lock.json")
NOT_INSTALLED = "NOT-INSTALLED"
DEV_REF = "origin/DEV"
REPARSE = 0x400
COMMAND_LOG_ENV = "PORTAL_KIT_COMMAND_LOG"
COMMANDS_BUILT = []  # every subprocess argv this module has built, in order (a test reads it)


# ---------------------------------------------------------------- subprocess (one choke point)


def run_cmd(argv, cwd=None, timeout=120, env=None):
    """Run one argv list, recording it. Returns (rc, stdout bytes, stderr bytes); rc is -1 if it could not start, 124 on timeout."""
    COMMANDS_BUILT.append(list(argv))
    log = os.environ.get(COMMAND_LOG_ENV)
    if log:
        with open(log, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(list(argv)) + "\n")
    try:
        p = subprocess.run(argv, cwd=cwd, capture_output=True, timeout=timeout, env=env)
    except FileNotFoundError:
        return -1, b"", b"not found"
    except subprocess.TimeoutExpired:
        return 124, b"", b"timeout"
    return p.returncode, p.stdout, p.stderr


def tool_version(name):
    rc, out, _err = run_cmd([name, "--version"], timeout=30)
    if rc != 0:
        return NOT_INSTALLED
    return out.decode("utf-8", "replace").strip().splitlines()[0].strip() if out.strip() else NOT_INSTALLED


def base_checkout():
    """The first entry of `git worktree list --porcelain`, run from this repository."""
    rc, out, _err = run_cmd(["git", "-C", str(ROOT), "worktree", "list", "--porcelain"], timeout=30)
    if rc != 0:
        return None
    for line in out.decode("utf-8", "replace").splitlines():
        if line.startswith("worktree "):
            return line[len("worktree "):].strip()
    return None


def default_portal():
    base = base_checkout()
    return str(pathlib.Path(base) / "portal") if base else None


# ---------------------------------------------------------------- hashing and the lockfile


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def norm_eol(data):
    return data.replace(b"\r\n", b"\n")


def strip_jsonc(text):
    """Remove comments and trailing commas that sit OUTSIDE string literals (bun.lock is JSONC)."""
    out = []
    i = 0
    n = len(text)
    in_str = False
    while i < n:
        c = text[i]
        if in_str:
            out.append(c)
            if c == "\\" and i + 1 < n:
                out.append(text[i + 1])
                i += 2
                continue
            if c == '"':
                in_str = False
            i += 1
            continue
        if c == '"':
            in_str = True
            out.append(c)
            i += 1
        elif c == "/" and text[i:i + 2] == "//":
            while i < n and text[i] != "\n":
                i += 1
        elif c == "/" and text[i:i + 2] == "/*":
            end = text.find("*/", i + 2)
            i = n if end < 0 else end + 2
        elif c == ",":
            j = i + 1
            while j < n and text[j] in " \t\r\n":
                j += 1
            if j < n and text[j] in "}]":
                i += 1  # trailing comma: drop it
            else:
                out.append(c)
                i += 1
        else:
            out.append(c)
            i += 1
    return "".join(out)


def key_segments(key):
    """'@babel/core/@babel/parser' -> ['@babel/core', '@babel/parser']; 'a/b' -> ['a', 'b']."""
    parts = key.split("/")
    segs = []
    i = 0
    while i < len(parts):
        if parts[i].startswith("@") and i + 1 < len(parts):
            segs.append(parts[i] + "/" + parts[i + 1])
            i += 2
        else:
            segs.append(parts[i])
            i += 1
    return segs


def read_lock(path, name):
    """Parse the lockfile into {key: {name, spec, version, meta}}. Raises ValueError when it cannot be read."""
    raw = pathlib.Path(path).read_bytes()
    if name == "bun.lockb":
        raise ValueError("bun.lockb is a binary lockfile; `bun pm ls --all` is not run because it cannot be proven offline")
    text = raw.decode("utf-8")
    if name == "bun.lock":
        try:
            doc = json.loads(strip_jsonc(text))
        except ValueError as exc:
            raise ValueError("bun.lock does not parse after stripping trailing commas and comments: %s" % exc)
        pk = doc.get("packages")
        if not isinstance(pk, dict) or not pk:
            raise ValueError("bun.lock has no `packages` object")
        entries = {}
        for key, val in pk.items():
            if not isinstance(val, list) or not val or not isinstance(val[0], str):
                raise ValueError("bun.lock entry %r has an unexpected shape" % key)
            segs = key_segments(key)
            pname = segs[-1]
            head = val[0]
            spec = head[len(pname) + 1:] if head.startswith(pname + "@") else head.rpartition("@")[2]
            meta = next((x for x in val[1:] if isinstance(x, dict)), {})
            entries[key] = {"name": pname, "spec": spec, "version": spec if spec[:1].isdigit() else "", "meta": meta}
        return entries
    doc = json.loads(text)  # package-lock.json
    pk = doc.get("packages")
    if not isinstance(pk, dict):
        raise ValueError("package-lock.json has no `packages` object")
    entries = {}
    for path_key, val in pk.items():
        if not path_key:
            continue
        chain = path_key.split("node_modules/")[1:]
        key = "/".join(c.rstrip("/") for c in chain)
        pname = key_segments(key)[-1]
        entries[key] = {"name": pname, "spec": val.get("version", ""), "version": val.get("version", ""),
                        "meta": {"os": val.get("os"), "cpu": val.get("cpu")}}
    return entries


# ---------------------------------------------------------------- this platform

def this_platform():
    mach = platform.machine().lower()
    cpu = {"amd64": "x64", "x86_64": "x64", "arm64": "arm64", "aarch64": "arm64"}.get(mach, mach)
    osn = {"win32": "win32", "linux": "linux", "darwin": "darwin"}.get(sys.platform, sys.platform)
    return osn, cpu


def field_allows(values, current):
    """The package-manager os/cpu rule: no list -> allowed; `!x` entries block; otherwise the value must be listed."""
    if values is None or values == [] or values == "":
        return True
    if isinstance(values, str):
        values = [values]
    neg = [v[1:] for v in values if isinstance(v, str) and v.startswith("!")]
    pos = [v for v in values if isinstance(v, str) and not v.startswith("!")]
    if current in neg:
        return False
    if pos and current not in pos:
        return False
    return True


def platform_allows(meta):
    osn, cpu = this_platform()
    return field_allows(meta.get("os"), osn) and field_allows(meta.get("cpu"), cpu)


# ---------------------------------------------------------------- the walk


BS = chr(92)
EXT_PREFIX = BS * 2 + "?" + BS
EXT_UNC = EXT_PREFIX + "UNC" + BS


def ext(path):
    """On Windows, the extended-length form of an absolute path so a nested node_modules path past 260 characters can be read."""
    path = str(path)
    if os.name == "nt" and not path.startswith(EXT_PREFIX):
        path = os.path.abspath(path)
        if path.startswith(BS * 2):
            return EXT_UNC + path[2:]
        return EXT_PREFIX + path
    return path


def plain(path):
    path = str(path)
    if path.startswith(EXT_UNC):
        return BS * 2 + path[len(EXT_UNC):]
    if path.startswith(EXT_PREFIX):
        return path[len(EXT_PREFIX):]
    return path


def is_link(entry):
    try:
        if entry.is_symlink():
            return True
        junction = getattr(entry, "is_junction", None)
        if junction is not None:
            return bool(junction())
        return bool(getattr(entry.stat(follow_symlinks=False), "st_file_attributes", 0) & REPARSE)
    except OSError:
        return False


def link_target(path):
    try:
        return os.readlink(path)
    except OSError:
        return None


def read_package_json(path):
    try:
        with open(path, "rb") as fh:
            return json.loads(fh.read().decode("utf-8-sig"))
    except (OSError, ValueError):
        return None


def scan_tree(nm_root):
    """One os.scandir walk of a node_modules directory. Counts every file and byte, reads only package.json at package roots
    (node_modules/<name>, node_modules/@scope/<name>, and the same under nested node_modules), never follows a link."""
    nm_root = ext(nm_root)
    res = {"files": 0, "bytes": 0, "dirs": 0, "links": [], "packages": {}, "no_package_json": [], "bad_package_json": [],
           "walk_errors": [], "toplevel": 0}
    # stack items: (path, kind, prefix, pkg_record)  kind: container | scope | body (inside a package) | plain
    stack = [(nm_root, "container", "", None)]
    while stack:
        path, kind, prefix, rec = stack.pop()
        try:
            it = os.scandir(path)
        except OSError as exc:
            res["walk_errors"].append("%s: %s" % (plain(path), exc))
            continue
        with it:
            for entry in it:
                name = entry.name
                full = entry.path
                try:
                    if is_link(entry):
                        res["links"].append({"path": plain(full), "target": link_target(full), "key": _link_key(kind, prefix, name)})
                        continue
                    if entry.is_dir(follow_symlinks=False):
                        res["dirs"] += 1
                        if kind == "container":
                            if name.startswith("@"):
                                stack.append((full, "scope", (prefix + "/" if prefix else "") + name, None))
                            elif name.startswith("."):
                                stack.append((full, "plain", prefix, None))
                            else:
                                key = (prefix + "/" if prefix else "") + name
                                stack.append((full, "body", key, _new_pkg(full, key, name, res)))
                        elif kind == "scope":
                            key = prefix + "/" + name
                            stack.append((full, "body", key, _new_pkg(full, key, name, res)))
                        elif rec is not None and name == "node_modules":
                            stack.append((full, "container", prefix, None))
                        else:
                            stack.append((full, kind, prefix, rec))
                        continue
                    st = entry.stat(follow_symlinks=False)
                    res["files"] += 1
                    res["bytes"] += st.st_size
                    if rec is not None:
                        low = name.lower()
                        if low.endswith(".node"):
                            rec["node_addon"] = True
                        elif low.endswith(".exe"):
                            rec["exe"] = True
                except OSError as exc:
                    res["walk_errors"].append("%s: %s" % (plain(full), exc))
    return res


def _link_key(kind, prefix, name):
    if kind == "container":
        return (prefix + "/" if prefix else "") + name
    if kind == "scope":
        return prefix + "/" + name
    return None


def _new_pkg(full, key, name, res):
    pj = read_package_json(os.path.join(full, "package.json"))
    rec = {"key": key, "dirname": name, "path": plain(full), "name": None, "version": None, "os": None, "cpu": None,
           "bin_exe": False, "node_addon": False, "exe": False}
    if pj is None:
        res["no_package_json"].append(key)
    elif not isinstance(pj, dict):
        res["bad_package_json"].append(key)
    else:
        rec["name"] = pj.get("name")
        rec["version"] = pj.get("version")
        rec["os"] = pj.get("os")
        rec["cpu"] = pj.get("cpu")
        bn = pj.get("bin")
        vals = [bn] if isinstance(bn, str) else list(bn.values()) if isinstance(bn, dict) else []
        rec["bin_exe"] = any(isinstance(v, str) and v.lower().endswith(".exe") for v in vals)
    res["packages"][key] = rec
    if len(key_segments(key)) == 1:
        res["toplevel"] += 1
    return rec


# ---------------------------------------------------------------- describe


def git_state(portal):
    """(head, branch, toplevel_ok). A directory that is not itself a repository root reads NO-GIT (never an outer repository)."""
    rc, out, _e = run_cmd(["git", "-C", portal, "rev-parse", "--show-toplevel"], timeout=30)
    if rc != 0:
        return "NO-GIT", "-", False
    top = out.decode("utf-8", "replace").strip()
    if os.path.normcase(os.path.realpath(top)) != os.path.normcase(os.path.realpath(portal)):
        return "NO-GIT", "-", False
    rc, out, _e = run_cmd(["git", "-C", portal, "rev-parse", "HEAD"], timeout=30)
    head = out.decode("utf-8", "replace").strip() if rc == 0 else "NO-COMMIT"
    rc, out, _e = run_cmd(["git", "-C", portal, "branch", "--show-current"], timeout=30)
    branch = out.decode("utf-8", "replace").strip() if rc == 0 and out.strip() else "DETACHED-OR-NONE"
    return head, branch, True


def dev_compare(portal, lock_name, working_bytes, is_repo):
    """equals_dev as True / False / 'DEV-REF-ABSENT'. Reads the blob with `git show`; never fetches."""
    if not is_repo:
        return "DEV-REF-ABSENT", "not a repository"
    rc, _o, _e = run_cmd(["git", "-C", portal, "rev-parse", "--verify", "--quiet", DEV_REF], timeout=30)
    if rc != 0:
        return "DEV-REF-ABSENT", "%s is not present locally; nothing was fetched" % DEV_REF
    rc, blob, _e = run_cmd(["git", "-C", portal, "show", "%s:%s" % (DEV_REF, lock_name)], timeout=60)
    if rc != 0:
        return False, "%s holds no %s" % (DEV_REF, lock_name)
    if blob == working_bytes:
        return True, "byte-identical"
    if norm_eol(blob) == norm_eol(working_bytes):
        return True, "identical after folding CRLF to LF (line endings differ only)"
    return False, "content differs (DEV blob %d bytes sha256 %s, working %d bytes sha256 %s)" % (
        len(blob), sha256_bytes(norm_eol(blob))[:12], len(working_bytes), sha256_bytes(norm_eol(working_bytes))[:12])


def classify(entries, scan):
    pkgs = scan["packages"]
    by_nv = {}
    for rec in pkgs.values():
        by_nv.setdefault((rec["name"] or rec["dirname"], rec["version"]), []).append(rec["key"])
    link_keys = {lk["key"] for lk in scan["links"] if lk.get("key")}
    classes = {"PRESENT": [], "RELOCATED": [], "OPTIONAL-OTHER-PLATFORM": [], "WORKSPACE": [], "VERSION-DIFFERS": [], "ABSENT": []}
    other = {}
    for key, ent in entries.items():
        other[key] = not platform_allows(ent["meta"])
    for key, ent in entries.items():
        rec = pkgs.get(key)
        if rec is not None:
            if not ent["version"] or rec["version"] == ent["version"]:
                classes["PRESENT"].append(key)
            else:
                classes["VERSION-DIFFERS"].append("%s lock=%s disk=%s" % (key, ent["version"], rec["version"]))
            continue
        if key in link_keys:
            classes["PRESENT"].append(key)
            continue
        if ent["spec"].startswith("workspace:"):
            classes["WORKSPACE"].append(key)
            continue
        if ent["version"] and by_nv.get((ent["name"], ent["version"])):
            classes["RELOCATED"].append(key)
            continue
        segs = key_segments(key)
        anc_other = any(other.get("/".join(segs[:i]), False) for i in range(1, len(segs)))
        if other[key] or anc_other:
            classes["OPTIONAL-OTHER-PLATFORM"].append(key)
            continue
        classes["ABSENT"].append(key)
    extra = sorted(k for k in pkgs if k not in entries)
    return classes, extra


def platform_specific(scan):
    out = []
    for rec in scan["packages"].values():
        why = []
        if rec["node_addon"]:
            why.append("node-addon")
        if rec["bin_exe"] or rec["exe"]:
            why.append("exe")
        if rec["os"]:
            why.append("os=%s" % json.dumps(rec["os"]))
        if rec["cpu"]:
            why.append("cpu=%s" % json.dumps(rec["cpu"]))
        if why:
            out.append({"key": rec["key"], "name": rec["name"] or rec["dirname"], "version": rec["version"], "why": why})
    out.sort(key=lambda x: x["key"])
    return out


def describe(portal, quiet=False):
    """Returns a dict; res['ok'] is the PORTAL-TREE ok. Prints the detail lines unless quiet."""
    emit = (lambda *_a: None) if quiet else print
    portal = str(portal)
    res = {"portal": portal, "ok": False, "reasons": []}
    head, branch, is_repo = git_state(portal)
    res.update(head=head, branch=branch)
    emit("PORTAL-HEAD portal=%s head=%s branch=%s" % (portal, head, branch))
    existing = [n for n in LOCK_CANDIDATES if os.path.isfile(os.path.join(portal, n))]
    used = next((n for n in LOCK_CANDIDATES if n in existing), None)
    res.update(lockfile=used or "NONE", lockfiles_present=existing)
    bun = tool_version("bun")
    node = tool_version("node")
    osn, cpu = this_platform()
    res.update(bun=bun, node=node, platform="%s/%s" % (osn, cpu))
    emit("PORTAL-TOOLS bun=%s node=%s platform=%s/%s" % (bun, node, osn, cpu))
    entries = {}
    raw = b""
    if used is None:
        res["reasons"].append("no lockfile (looked for %s)" % ", ".join(LOCK_CANDIDATES))
        res.update(lock_sha256="-" * 12, lock_sha256_full="", lock_sha256_raw="", equals_dev="DEV-REF-ABSENT")
        emit("PORTAL-LOCKFILE present=[] used=NONE")
    else:
        raw = pathlib.Path(portal, used).read_bytes()
        sha = sha256_bytes(norm_eol(raw))
        res.update(lock_sha256=sha[:12], lock_sha256_full=sha, lock_sha256_raw=sha256_bytes(raw))
        try:
            entries = read_lock(os.path.join(portal, used), used)
        except (ValueError, OSError) as exc:
            res["reasons"].append("lockfile not read: %s" % exc)
        emit("PORTAL-LOCKFILE present=%s used=%s sha256=%s (CRLF folded to LF) raw_sha256=%s entries=%d parse=%s" % (
            existing, used, sha[:12], res["lock_sha256_raw"][:12], len(entries),
            "tolerant: comments and trailing commas stripped outside strings; section=packages" if used == "bun.lock" else used))
        eq, why = dev_compare(portal, used, raw, is_repo)
        res["equals_dev"] = eq
        emit("PORTAL-DEV equals_dev=%s (%s)" % (eq, why))
    res.setdefault("equals_dev", "DEV-REF-ABSENT")
    nm = os.path.join(portal, "node_modules")
    nm_link = os.path.islink(nm) or (os.path.isdir(nm) and _is_junction_path(nm))
    t0 = time.time()
    if nm_link:
        res["reasons"].append("node_modules is a link (-> %s); a link is never followed" % link_target(nm))
        scan = {"files": 0, "bytes": 0, "dirs": 0, "links": [], "packages": {}, "no_package_json": [], "bad_package_json": [],
                "walk_errors": [], "toplevel": 0}
    elif not os.path.isdir(nm):
        res["reasons"].append("no node_modules directory")
        scan = {"files": 0, "bytes": 0, "dirs": 0, "links": [], "packages": {}, "no_package_json": [], "bad_package_json": [],
                "walk_errors": [], "toplevel": 0}
    else:
        scan = scan_tree(nm)
    res["walk_seconds"] = round(time.time() - t0, 2)
    nested = len(scan["packages"]) - scan["toplevel"]
    res.update(files=scan["files"], bytes=scan["bytes"], toplevel_packages=scan["toplevel"], nested_packages=nested,
               links=scan["links"], walk_errors=scan["walk_errors"], scan_packages=len(scan["packages"]))
    emit("PORTAL-SIZE top_level_packages=%d nested_packages=%d directories=%d files=%d bytes=%d links=%d walk_errors=%d "
         "no_package_json=%d bad_package_json=%d walk_seconds=%s" % (
             scan["toplevel"], nested, scan["dirs"], scan["files"], scan["bytes"], len(scan["links"]), len(scan["walk_errors"]),
             len(scan["no_package_json"]), len(scan["bad_package_json"]), res["walk_seconds"]))
    for lk in scan["links"][:20]:
        emit("PORTAL-LINK %s -> %s" % (lk["path"], lk["target"]))
    for we in scan["walk_errors"][:10]:
        emit("PORTAL-WALK-ERROR %s" % we)
    classes, extra = classify(entries, scan)
    present = len(classes["PRESENT"]) + len(classes["RELOCATED"])
    absent = len(classes["ABSENT"]) + len(classes["VERSION-DIFFERS"])
    res.update(packages=len(entries), present=present, absent=absent, classes={k: len(v) for k, v in classes.items()},
               absent_names=classes["ABSENT"] + classes["VERSION-DIFFERS"], extra=len(extra))
    emit("PORTAL-CLASSES lock_packages=%d PRESENT=%d RELOCATED=%d OPTIONAL-OTHER-PLATFORM=%d WORKSPACE=%d VERSION-DIFFERS=%d ABSENT=%d "
         "extra_on_disk=%d" % (len(entries), len(classes["PRESENT"]), len(classes["RELOCATED"]),
                               len(classes["OPTIONAL-OTHER-PLATFORM"]), len(classes["WORKSPACE"]), len(classes["VERSION-DIFFERS"]),
                               len(classes["ABSENT"]), len(extra)))
    for nm_ in (classes["ABSENT"] + classes["VERSION-DIFFERS"])[:40]:
        emit("PORTAL-ABSENT %s" % nm_)
    for nm_ in extra[:10]:
        emit("PORTAL-EXTRA %s" % nm_)
    ps = platform_specific(scan)
    res["platform_specific"] = ps
    emit("PORTAL-PLATFORM-SPECIFIC installed=%d (a .node file, an .exe, or an os/cpu field in package.json)" % len(ps))
    for rec in ps:
        emit("PORTAL-PLATFORM-SPECIFIC-PKG %s@%s %s" % (rec["key"], rec["version"], " ".join(rec["why"])))
    res["ok"] = bool(entries) and absent == 0 and not scan["walk_errors"] and not nm_link and os.path.isdir(nm)
    emit("PORTAL-TREE head=%s lockfile=%s lock_sha256=%s equals_dev=%s bun=%s node=%s packages=%d present=%d absent=%d files=%d "
         "bytes=%d ok=%s" % (head, res["lockfile"], res["lock_sha256"], res["equals_dev"], bun, node, len(entries), present, absent,
                             scan["files"], scan["bytes"], res["ok"]))
    return res


def _is_junction_path(path):
    try:
        return bool(os.lstat(path).st_file_attributes & REPARSE)
    except (OSError, AttributeError):
        return False


# ---------------------------------------------------------------- pack


def lock_hash(portal, lock_name):
    return sha256_bytes(norm_eol(pathlib.Path(portal, lock_name).read_bytes()))


def _norm_ti(ti):
    ti.uid = ti.gid = 0
    ti.uname = ti.gname = ""
    ti.mode = 0o755 if ti.isdir() else 0o644
    return ti


def pack(portal, out_dir, quiet=False):
    emit = (lambda *_a: None) if quiet else print
    res = describe(portal, quiet=True) if quiet else describe(portal)
    if not res["ok"]:
        emit("REFUSED: describe is not ok (%s); nothing is packed" % ("; ".join(res["reasons"]) or "absent=%d" % res["absent"]))
        emit("PORTAL-PACK files=0 bytes=0 archive_bytes=0 links=0 unrepresented=0 platform_specific=0 ok=False")
        return res, False
    out_dir = pathlib.Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    nm = ext(os.path.join(portal, "node_modules"))
    nm_real = plain(os.path.realpath(plain(nm)))
    archive = out_dir / ARCHIVE
    packed_files = packed_links = 0
    unrep = []
    t0 = time.time()
    with tarfile.open(str(archive), "w:gz", compresslevel=1, format=tarfile.PAX_FORMAT) as tf:
        stack = [(nm, "node_modules")]
        tf.add(nm, arcname="node_modules", recursive=False, filter=_norm_ti)
        while stack:
            path, arc = stack.pop()
            with os.scandir(path) as it:
                entries = sorted(it, key=lambda e: e.name)
            for entry in entries:
                full = entry.path
                sub = arc + "/" + entry.name
                if is_link(entry):
                    tgt = link_target(full)
                    rel = _inside_relative(full, tgt, nm_real)
                    if rel is None:
                        unrep.append({"path": sub, "target": tgt})
                        continue
                    ti = tarfile.TarInfo(sub)
                    ti.type = tarfile.SYMTYPE
                    ti.linkname = rel
                    ti.mtime = int(entry.stat(follow_symlinks=False).st_mtime)
                    tf.addfile(_norm_ti(ti))
                    packed_links += 1
                elif entry.is_dir(follow_symlinks=False):
                    tf.add(full, arcname=sub, recursive=False, filter=_norm_ti)
                    stack.append((full, sub))
                else:
                    tf.add(full, arcname=sub, recursive=False, filter=_norm_ti)
                    packed_files += 1
    pack_seconds = round(time.time() - t0, 2)
    asha = sha256_file(archive)
    manifest = {
        "kit": "portal-node-modules", "format": "tar+gzip-1", "built_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "builder_device": os.environ.get("AGENTBUS_DEVICE", "NOT-SET"),
        "archive": {"name": ARCHIVE, "sha256": asha, "size": archive.stat().st_size},
        "lockfile": {"name": res["lockfile"], "sha256": res["lock_sha256_full"], "sha256_raw": res["lock_sha256_raw"],
                     "sha256_basis": "file bytes with CRLF folded to LF", "equals_dev": res["equals_dev"]},
        "portal_head": res["head"], "portal_branch": res["branch"], "bun": res["bun"], "node": res["node"],
        "platform": {"os": this_platform()[0], "cpu": this_platform()[1], "python_platform": platform.platform()},
        "files": res["files"], "bytes": res["bytes"], "files_packed": packed_files, "links_packed": packed_links,
        "packages": res["packages"], "present": res["present"], "pack_seconds": pack_seconds,
        "platform_specific": res["platform_specific"], "unrepresented_links": unrep,
    }
    (out_dir / MANIFEST).write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    ok = packed_files == res["files"]
    emit("PORTAL-PACK archive=%s sha256=%s format=tar+gzip-1 seconds=%s" % (archive, asha[:12], pack_seconds))
    for u in unrep:
        emit("PORTAL-UNREPRESENTED %s -> %s" % (u["path"], u["target"]))
    emit("PORTAL-PACK files=%d bytes=%d archive_bytes=%d links=%d unrepresented=%d platform_specific=%d ok=%s" % (
        packed_files, res["bytes"], archive.stat().st_size, packed_links, len(unrep), len(res["platform_specific"]), ok))
    return manifest, ok


def _inside_relative(link_path, target, nm_real):
    """A relative link target when the link resolves inside the tree, else None."""
    if not target:
        return None
    target = plain(target)
    link_path = plain(link_path)
    absolute =target if os.path.isabs(target) else os.path.join(os.path.dirname(link_path), target)
    absolute = os.path.normpath(absolute)
    nm_norm = os.path.normcase(os.path.normpath(nm_real))
    low = os.path.normcase(absolute)
    if not (low == nm_norm or low.startswith(nm_norm + os.sep)):
        return None
    return os.path.relpath(absolute, os.path.dirname(link_path)).replace("\\", "/")


# ---------------------------------------------------------------- verify / extract


def verify(from_dir, portal, extract=False, replace=False, quiet=False):
    emit = (lambda *_a: None) if quiet else print
    from_dir = pathlib.Path(from_dir)
    portal = str(portal)
    state = {"archive": "mismatch", "lockfile": "differs", "bun": "differs", "node": "differs", "platform": "differs"}
    extracted = "-"
    try:
        man = json.loads((from_dir / MANIFEST).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        emit("REFUSED: %s is unreadable: %s" % (MANIFEST, exc))
        return _verify_line(emit, state, extracted, False)
    arc = from_dir / man.get("archive", {}).get("name", ARCHIVE)
    if arc.is_file() and arc.stat().st_size == man["archive"]["size"] and sha256_file(arc) == man["archive"]["sha256"]:
        state["archive"] = "ok"
    lock_name = man["lockfile"]["name"]
    lp = pathlib.Path(portal, lock_name)
    if lp.is_file() and lock_hash(portal, lock_name) == man["lockfile"]["sha256"]:
        state["lockfile"] = "ok"
    here_bun = tool_version("bun")
    state["bun"] = "ok" if here_bun == man.get("bun") else "differs"
    here_node = tool_version("node")
    mnode = man.get("node")
    if not mnode or mnode == NOT_INSTALLED:
        state["node"] = "absent"
    elif here_node == NOT_INSTALLED:
        state["node"] = "absent"
    else:
        state["node"] = "ok" if here_node == mnode else "differs"
    here_os, here_cpu = this_platform()
    mp = man.get("platform", {})
    state["platform"] = "ok" if (mp.get("os"), mp.get("cpu")) == (here_os, here_cpu) else "differs"
    emit("PORTAL-VERIFY-DETAIL manifest bun=%s node=%s platform=%s/%s lockfile=%s sha256=%s | here bun=%s node=%s platform=%s/%s" % (
        man.get("bun"), mnode, mp.get("os"), mp.get("cpu"), lock_name, man["lockfile"]["sha256"][:12], here_bun, here_node, here_os,
        here_cpu))
    node_fine = state["node"] == "ok" or (state["node"] == "absent" and (not mnode or mnode == NOT_INSTALLED))
    gates = state["archive"] == "ok" and state["lockfile"] == "ok" and state["bun"] == "ok" and node_fine and state["platform"] == "ok"
    if not gates:
        emit("REFUSED: the pack does not match this box; nothing is extracted")
        return _verify_line(emit, state, extracted, False)
    if not extract:
        return _verify_line(emit, state, extracted, True)
    target = pathlib.Path(portal, "node_modules")
    if os.path.islink(str(target)) or _is_junction_path(str(target)):
        emit("REFUSED: %s is a link; it is never followed or replaced" % target)
        return _verify_line(emit, state, extracted, False)
    if target.exists() and any(target.iterdir()):
        if not replace:
            emit("REFUSED: %s exists and is not empty; pass --replace to remove it first" % target)
            return _verify_line(emit, state, extracted, False)
        shutil.rmtree(str(target))
    count, link_fail = _extract(arc, pathlib.Path(portal))
    for lf in link_fail:
        emit("PORTAL-EXTRACT-LINK-FAILED %s" % lf)
    extracted = str(count)
    ok = count == man["files"] and not link_fail
    if count != man["files"]:
        emit("REFUSED-LATE: extracted %d files, the manifest says %d" % (count, man["files"]))
    return _verify_line(emit, state, extracted, ok)


def _verify_line(emit, state, extracted, ok):
    line = "PORTAL-VERIFY archive=%s lockfile=%s bun=%s node=%s platform=%s extracted=%s ok=%s" % (
        state["archive"], state["lockfile"], state["bun"], state["node"], state["platform"], extracted, ok)
    emit(line)
    return line, ok


def _extract(archive, portal):
    """Member-by-member extract into <portal>; every member must live under node_modules/; links are checked by the 'data' filter."""
    count = 0
    link_fail = []
    with tarfile.open(str(archive), "r:gz") as tf:
        for member in tf:
            name = member.name
            if not (name == "node_modules" or name.startswith("node_modules/")) or ".." in name.split("/") or os.path.isabs(name):
                raise ValueError("archive member outside node_modules: %r" % name)
            try:
                tf.extract(member, path=str(portal), filter="data")
            except (OSError, tarfile.TarError) as exc:
                if member.issym() or member.islnk():
                    link_fail.append("%s (%s)" % (name, exc))
                    continue
                raise
            if member.isreg():
                count += 1
    return count, link_fail


# ---------------------------------------------------------------- typecheck


def typecheck(portal, timeout=600, script="typecheck", quiet=False):
    emit = (lambda *_a: None) if quiet else print
    pj = read_package_json(os.path.join(str(portal), "package.json"))
    scripts = pj.get("scripts", {}) if isinstance(pj, dict) else {}
    if script not in scripts:
        emit("REFUSED: package.json has no scripts.%s (scripts: %s)" % (script, ", ".join(sorted(scripts)) or "none"))
        emit("PORTAL-TYPECHECK script=%s command=- exit=- last_line=- ok=False" % script)
        return None, False
    command = scripts[script]
    env = dict(os.environ)
    env["NO_UPDATE_NOTIFIER"] = "1"
    argv = ["bun", "run", "--silent", "--no-install", script]
    emit("PORTAL-TYPECHECK-COMMAND package.json scripts.%s = %s ; run as: %s (cwd %s, timeout %ss)" % (
        script, command, " ".join(argv), portal, timeout))
    rc, out, err = run_cmd(argv, cwd=str(portal), timeout=timeout, env=env)
    ansi = re.compile(r"\x1b\[[0-9;]*m")
    text = ansi.sub("", (out if out.strip() else err).decode("utf-8", "replace"))
    lines = [x for x in text.splitlines() if x.strip()]
    last = lines[-1].strip() if lines else ""
    if rc == 124:
        last = "TIMEOUT after %ss" % timeout
    emit("PORTAL-TYPECHECK script=%s command=%s exit=%s last_line=%s ok=%s" % (script, command, rc, last, rc == 0))
    return rc, rc == 0


# ---------------------------------------------------------------- main


def main(argv=None):
    ap = argparse.ArgumentParser(description="Portal dependency-tree kit: describe, pack, verify/extract, typecheck. No network.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("describe")
    p.add_argument("--portal")
    p.add_argument("--json")
    p = sub.add_parser("pack")
    p.add_argument("--out", required=True)
    p.add_argument("--portal")
    p = sub.add_parser("verify")
    p.add_argument("--from", dest="from_dir", required=True)
    p.add_argument("--portal", required=True)
    p.add_argument("--extract", action="store_true")
    p.add_argument("--replace", action="store_true")
    p = sub.add_parser("typecheck")
    p.add_argument("--portal", required=True)
    p.add_argument("--timeout", type=int, default=600)
    p.add_argument("--script", default="typecheck")
    args = ap.parse_args(argv)
    if args.cmd in ("describe", "pack"):
        portal = args.portal or default_portal()
        if not portal:
            print("REFUSED: no --portal and the base checkout could not be derived from `git worktree list --porcelain`")
            return 1
        if args.cmd == "describe":
            res = describe(portal)
            if args.json:
                pathlib.Path(args.json).write_text(json.dumps(res, indent=2, default=str) + "\n", encoding="utf-8")
            return 0 if res["ok"] else 1
        _m, ok = pack(portal, args.out)
        return 0 if ok else 1
    if args.cmd == "verify":
        _line, ok = verify(args.from_dir, args.portal, extract=args.extract, replace=args.replace)
        return 0 if ok else 1
    _rc, ok = typecheck(args.portal, timeout=args.timeout, script=args.script)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
