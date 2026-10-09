"""kit_terraform_providers.py -- the Terraform provider kit (NFRA_CTLPLN PRD v0.14 C-KIT-PYTHON, TO-CT-k-2 AMENDMENT 1).

A box that cannot reach a provider registry cannot run `terraform init`. This kit reads which provider versions the Dell-placed
projects' Terraform roots lock, finds those provider binaries ALREADY on this machine's disk, lays them out as a Terraform
FILESYSTEM MIRROR with a checksum manifest and the CLI-config snippet that makes `terraform init` read the mirror and never the
registry, and verifies such a pack on the receiving box. Pure stdlib. NO NETWORK: nothing here downloads, and no command this tool
constructs names a registry address or a downloading verb (a test asserts it).

    python org/devices/kit_terraform_providers.py required [--out <json>] [--all-roots]
    python org/devices/kit_terraform_providers.py located  [--search <dir> ...] [--platform windows_amd64] [--all-roots]
    python org/devices/kit_terraform_providers.py binary   [--tools-dir <dir>]
    python org/devices/kit_terraform_providers.py pack --out <dir> [--search <dir> ...] [--only <ns/type[@ver]> ...] [--include-unlocked] [--no-binary]
                                                   [--all-roots] [--mirror-zips <dir> ...]
    python org/devices/kit_terraform_providers.py verify --from <dir> [--write-config <file>] [--run-binary] [--install-binary <target>]
    python org/devices/kit_terraform_providers.py readback --root <dir> [--from <pack dir> | --config <file>] [--timeout <s>] [--init-only]

AMENDMENT 4: the pack also carries the Terraform BINARY this box's .tools/safe-apply.sh would run, resolved by the wrapper's own order
(SAFE_APPLY_TERRAFORM override, then the sibling terraform.exe beside the wrapper in the base checkout's .tools/, then PATH). The binary
is hashed against the manifest BEFORE it is ever executed; every terraform run here sets CHECKPOINT_DISABLE=1 so even `version` makes no
network call.

AMENDMENT 9: --all-roots adds every other directory under infra/aws/terraform that holds a lock file (dell2 counts every lock);
--mirror-zips <dir> lays a release zip from a downloaded-mirror output directory into the pack in the PACKED form (Terraform
matches it on zh: or h1:, so a lock holding only another platform's h1 still accepts it); readback --init-only runs `init -backend=false`
with the pack as the sole provider source, restores the root's lock file byte for byte, and runs NO plan.

The roots are derived by importing placed_projects() and cited_roots() from
infra/aws/terraform/nfra-ctlpln-identity/tests/derive_resource_kinds.py (the method is not written twice), plus this project's own
two roots. A root with no `.terraform.lock.hcl` anywhere under it is NO-LOCK (counted); its declared required_providers constraint
is recorded and, with --include-unlocked, the highest version on this box that satisfies it joins the pack.

The h1 hash is Terraform's dirhash "h1" scheme: SHA-256 over lines "<sha256 hex of file>  <path>\\n" for each file of the unpacked
provider directory sorted by path, base64, prefixed "h1:". It is compared with the lock's h1 values. A mismatch is reported.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import importlib.util
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
REQUIRED_PATH = HERE / "kit_terraform_required.json"
TF_BASE = ROOT / "infra" / "aws" / "terraform"
DERIVE_PATH = TF_BASE / "nfra-ctlpln-identity" / "tests" / "derive_resource_kinds.py"
OWN_ROOTS = ("nfra-ctlpln-identity", "nfra-ctlpln-agentbus")
HOST = "registry.terraform.io"
PLATFORM = "windows_amd64"
MANIFEST = "MANIFEST.json"
SNIPPET_NAME = "terraform.rc.snippet"
LOCK_NAME = ".terraform.lock.hcl"
BIN_REL = "bin/terraform.exe"
OVERRIDE_ENV = "SAFE_APPLY_TERRAFORM"


# ---------------------------------------------------------------- the hash


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def h1_of_dir(directory):
    """Terraform's dirhash H1 of an unpacked provider directory."""
    directory = pathlib.Path(directory)
    names = []
    for dirpath, _dirs, files in os.walk(directory):
        for fn in files:
            rel = (pathlib.Path(dirpath) / fn).relative_to(directory)
            names.append(rel.as_posix())
    names.sort()
    summary = hashlib.sha256()
    for name in names:
        summary.update(("%s  %s\n" % (sha256_file(directory / name), name)).encode("utf-8"))
    return "h1:" + base64.b64encode(summary.digest()).decode("ascii")


def dir_size(directory):
    return sum(f.stat().st_size for f in pathlib.Path(directory).rglob("*") if f.is_file())


def zip_name(source, version, platform):
    return "terraform-provider-%s_%s_%s.zip" % (source.split("/")[2], version, platform)


def h1_of_zip(zip_path):
    """The h1 of a provider release zip = the dirhash h1 of its unpacked contents."""
    import zipfile
    with tempfile.TemporaryDirectory() as td:
        with zipfile.ZipFile(str(zip_path)) as zf:
            zf.extractall(td)
        return h1_of_dir(td)


def find_zip(source, version, platform, zip_dirs):
    """A release zip in a downloaded-mirror output dir: <dir>/<host>/<ns>/<type>/terraform-provider-<type>_<ver>_<platform>.zip."""
    host, ns, typ = source.split("/")
    for zd in zip_dirs or []:
        z = pathlib.Path(zd) / host / ns / typ / zip_name(source, version, platform)
        if z.is_file():
            return z
    return None


# ---------------------------------------------------------------- reading the roots


def load_derive():
    spec = importlib.util.spec_from_file_location("derive_resource_kinds_for_kit", str(DERIVE_PATH))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def derive_roots():
    """{root: [project codes]} exactly as derive_resource_kinds derives them, plus this project's own two roots."""
    mod = load_derive()
    roots = {}
    for code, pdir, _placement in mod.placed_projects():
        for r in mod.cited_roots(pdir):
            roots.setdefault(r, []).append(code)
    for r in OWN_ROOTS:
        roots.setdefault(r, []).append("NFRA_CTLPLN")
    return roots


def norm_source(src):
    parts = src.split("/")
    if len(parts) == 2:
        return "%s/%s" % (HOST, src)
    return src


def parse_lock(text):
    out = []
    for m in re.finditer(r'provider\s+"([^"]+)"\s*\{(.*?)\n\}', text, re.S):
        body = m.group(2)
        ver = re.search(r'^\s*version\s*=\s*"([^"]+)"', body, re.M)
        con = re.search(r'^\s*constraints\s*=\s*"([^"]*)"', body, re.M)
        hashes = re.findall(r'"((?:h1|zh):[^"]+)"', body)
        out.append({
            "source": norm_source(m.group(1)),
            "version": ver.group(1) if ver else None,
            "constraints": con.group(1) if con else None,
            "h1": [h for h in hashes if h.startswith("h1:")],
            "zh": [h for h in hashes if h.startswith("zh:")],
        })
    return out


def _brace_block(text, start):
    depth = 0
    for i in range(start, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return text[start + 1:i]
    return text[start + 1:]


def declared_constraints(root_dir):
    """required_providers entries of a root's .tf files: [{source, constraint}]."""
    found = []
    for dirpath, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d != ".terraform"]
        for fn in sorted(files):
            if not fn.endswith(".tf"):
                continue
            text = (pathlib.Path(dirpath) / fn).read_text(encoding="utf-8", errors="replace")
            for m in re.finditer(r"required_providers\s*\{", text):
                block = _brace_block(text, m.end() - 1)
                for em in re.finditer(r"(\w+)\s*=\s*\{", block):
                    entry = _brace_block(block, em.end() - 1)
                    src = re.search(r'source\s*=\s*"([^"]+)"', entry)
                    ver = re.search(r'version\s*=\s*"([^"]+)"', entry)
                    found.append({
                        "source": norm_source(src.group(1) if src else "hashicorp/%s" % em.group(1)),
                        "constraint": ver.group(1) if ver else None,
                    })
    seen, out = set(), []
    for f in found:
        key = (f["source"], f["constraint"])
        if key not in seen:
            seen.add(key)
            out.append(f)
    return out


def lock_files(root_dir):
    found = []
    for dirpath, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d != ".terraform"]
        if LOCK_NAME in files:
            found.append((pathlib.Path(dirpath) / LOCK_NAME).relative_to(root_dir).as_posix())
    return sorted(found)


def build_required(all_roots=False):
    """Derived roots (the Dell-placed projects plus this project's two); with all_roots, EVERY directory under
    infra/aws/terraform holding a lock file that the derived roots did not already read (AMENDMENT 9: dell2 counts every lock)."""
    roots = derive_roots()
    rows, providers, unlocked, errors = [], {}, [], []
    read_locks = set()

    def absorb(name, rdir, rel, row):
        for p in parse_lock((rdir / rel).read_text(encoding="utf-8")):
            row["providers"].append({"source": p["source"], "version": p["version"], "lock": rel})
            rec = providers.setdefault((p["source"], p["version"]), {
                "source": p["source"], "version": p["version"], "constraints": [], "roots": [], "h1": [], "zh": []})
            if p["constraints"] and p["constraints"] not in rec["constraints"]:
                rec["constraints"].append(p["constraints"])
            tag = name if rel == LOCK_NAME else "%s/%s" % (name, rel[:-len(LOCK_NAME) - 1])
            if tag not in rec["roots"]:
                rec["roots"].append(tag)
            for h in p["h1"]:
                if h not in rec["h1"]:
                    rec["h1"].append(h)
            for h in p["zh"]:
                if h not in rec["zh"]:
                    rec["zh"].append(h)

    for name in sorted(roots):
        rdir = TF_BASE / name
        row = {"root": name, "projects": sorted(set(roots[name])), "status": None, "lock_files": [], "providers": []}
        if not rdir.is_dir():
            row["status"] = "ROOT-MISSING"
            errors.append(name)
            rows.append(row)
            continue
        locks = lock_files(rdir)
        row["lock_files"] = locks
        if not locks:
            row["status"] = "NO-LOCK"
            row["declared"] = declared_constraints(rdir)
            for d in row["declared"]:
                unlocked.append({"root": name, "source": d["source"], "constraint": d["constraint"]})
        else:
            row["status"] = "LOCKED"
            for rel in locks:
                read_locks.add(os.path.normcase(os.path.abspath(str(rdir / rel))))
                absorb(name, rdir, rel, row)
        rows.append(row)
    if all_roots:
        extra = {}
        for rel in lock_files(TF_BASE):
            lp = TF_BASE / rel
            if os.path.normcase(os.path.abspath(str(lp))) in read_locks:
                continue
            extra.setdefault(pathlib.PurePosixPath(rel).parent.as_posix(), []).append(lp)
        for name in sorted(extra):
            rdir = TF_BASE / name
            row = {"root": name, "projects": ["ALL-LOCKS"], "status": "LOCKED", "lock_files": [LOCK_NAME], "providers": []}
            absorb(name, rdir, LOCK_NAME, row)
            rows.append(row)
    plist = [providers[k] for k in sorted(providers)]
    for p in plist:
        p["roots"].sort()
    return {"roots": rows, "providers": plist, "unlocked": unlocked, "errors": errors}


def required_summary(req):
    r = len(req["roots"])
    k = sum(1 for x in req["roots"] if x["status"] == "LOCKED")
    n = sum(1 for x in req["roots"] if x["status"] == "NO-LOCK")
    p = len({x["source"] for x in req["providers"]})
    v = len(req["providers"])
    ok = not req["errors"] and k + n == r
    return r, k, n, p, v, ok


def cmd_required(args):
    req = build_required(getattr(args, "all_roots", False))
    for row in req["roots"]:
        if row["status"] == "LOCKED":
            print("root %-28s LOCKED   %s" % (row["root"], ", ".join("%s %s" % (p["source"].split("/", 1)[1], p["version"]) for p in row["providers"])))
        elif row["status"] == "NO-LOCK":
            print("root %-28s NO-LOCK  declared: %s" % (row["root"], ", ".join("%s %s" % (d["source"].split("/", 1)[1], d["constraint"]) for d in row["declared"]) or "none"))
        else:
            print("root %-28s %s" % (row["root"], row["status"]))
    for p in req["providers"]:
        print("provider %s %s  locked-by %d roots: %s" % (p["source"], p["version"], len(p["roots"]), ", ".join(p["roots"])))
    out = pathlib.Path(args.out) if args.out else REQUIRED_PATH
    out.write_text(json.dumps(req, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print("wrote %s" % out.name)
    r, k, n, p, v, ok = required_summary(req)
    print("TF-REQUIRED roots=%d locked=%d no_lock=%d providers=%d distinct_versions=%d ok=%s" % (r, k, n, p, v, ok))
    return 0 if ok else 1


# ---------------------------------------------------------------- finding binaries on this box


def cli_config_plugin_cache():
    cands = []
    if os.environ.get("TF_CLI_CONFIG_FILE"):
        cands.append(pathlib.Path(os.environ["TF_CLI_CONFIG_FILE"]))
    if os.environ.get("APPDATA"):
        cands.append(pathlib.Path(os.environ["APPDATA"]) / "terraform.rc")
    cands.append(pathlib.Path.home() / ".terraformrc")
    for c in cands:
        if c.is_file():
            m = re.search(r'^\s*plugin_cache_dir\s*=\s*"([^"]+)"', c.read_text(encoding="utf-8", errors="replace"), re.M)
            if m:
                return pathlib.Path(os.path.expanduser(m.group(1)))
    return None


def worktrees():
    try:
        out = subprocess.run(["git", "worktree", "list", "--porcelain"], cwd=str(ROOT), capture_output=True, text=True, timeout=60).stdout
    except (OSError, subprocess.SubprocessError):
        return []
    return [pathlib.Path(line[9:].strip()) for line in out.splitlines() if line.startswith("worktree ")]


def default_search_dirs():
    """Plugin cache dirs first, then the base checkout (first worktree entry), then every other worktree and sibling wk-ctlpln-* dir."""
    dirs = []
    if os.environ.get("TF_PLUGIN_CACHE_DIR"):
        dirs.append(pathlib.Path(os.environ["TF_PLUGIN_CACHE_DIR"]))
    pc = cli_config_plugin_cache()
    if pc:
        dirs.append(pc)
    dirs.extend(worktrees())
    dirs.extend(sorted(ROOT.parent.glob("wk-ctlpln-*")))
    seen, out = set(), []
    for d in dirs:
        key = os.path.normcase(os.path.abspath(str(d)))
        if key not in seen and d.is_dir():
            seen.add(key)
            out.append(d)
    return out


def trees_in(search_dir):
    """Directories laid out as <base>/registry.terraform.io/<ns>/<type>/<ver>/<os_arch>/ under a search dir."""
    d = pathlib.Path(search_dir)
    bases = []
    if (d / HOST).is_dir():
        bases.append(d)
    for pat in ("infra/aws/terraform/*/.terraform/providers", "infra/aws/terraform/*/*/.terraform/providers"):
        bases.extend(sorted(b for b in d.glob(pat) if (b / HOST).is_dir()))
    if d.name == "providers" and d.parent.name == ".terraform" and (d / HOST).is_dir() and d not in bases:
        bases.append(d)
    return bases


def candidates(source, version, search_dirs, platform):
    host, ns, typ = source.split("/")
    found, seen = [], set()
    for sd in search_dirs:
        for base in trees_in(sd):
            pdir = base / host / ns / typ / version / platform
            if pdir.is_dir() and any(f.is_file() for f in pdir.iterdir()):
                key = os.path.normcase(os.path.realpath(str(pdir)))
                if key not in seen:
                    seen.add(key)
                    found.append((pdir, sd))
    return found


def locate_one(prov, search_dirs, platform):
    """-> dict(source, version, path|None, size, h1, h1_match, h1_checked, candidates)"""
    cands = candidates(prov["source"], prov["version"], search_dirs, platform)
    rec = {"source": prov["source"], "version": prov["version"], "path": None, "size": 0, "h1": None, "h1_match": None, "candidates": len(cands)}
    for pdir, _sd in cands:
        h = h1_of_dir(pdir)
        match = (h in prov["h1"]) if prov.get("h1") else None
        if rec["path"] is None or match:
            rec.update({"path": pdir, "size": dir_size(pdir), "h1": h, "h1_match": match})
        if match or match is None:
            break
    return rec


# ---------------------------------------------------------------- constraints on unlocked roots


def _vt(v):
    return tuple(int(x) for x in re.findall(r"\d+", v.split("-")[0])[:3])


def satisfies(version, constraint):
    vt = _vt(version)
    for part in (c.strip() for c in constraint.split(",")):
        m = re.match(r"^(~>|>=|<=|!=|=|>|<)?\s*(\d+(?:\.\d+)*)$", part)
        if not m:
            return False
        op, cv = m.group(1) or "=", m.group(2)
        ct = _vt(cv)
        pad = lambda t, n=3: t + (0,) * (n - len(t))  # noqa: E731
        if op == "=":
            ok = pad(vt) == pad(ct)
        elif op == "!=":
            ok = pad(vt) != pad(ct)
        elif op == ">=":
            ok = pad(vt) >= pad(ct)
        elif op == "<=":
            ok = pad(vt) <= pad(ct)
        elif op == ">":
            ok = pad(vt) > pad(ct)
        elif op == "<":
            ok = pad(vt) < pad(ct)
        else:  # ~> allows the last given component to rise
            n = len(ct)
            ok = pad(vt) >= pad(ct) and vt[:n - 1] == ct[:n - 1] if n > 1 else pad(vt) >= pad(ct)
        if not ok:
            return False
    return True


def versions_on_box(source, search_dirs, platform):
    host, ns, typ = source.split("/")
    vers = set()
    for sd in search_dirs:
        for base in trees_in(sd):
            tdir = base / host / ns / typ
            if tdir.is_dir():
                for vd in tdir.iterdir():
                    pdir = vd / platform
                    if pdir.is_dir() and any(f.is_file() for f in pdir.iterdir()):
                        vers.add(vd.name)
    return sorted(vers, key=_vt)


def resolve_unlocked(req, search_dirs, platform):
    """For each NO-LOCK root's declared provider: the versions on this box and the highest that satisfies the constraint."""
    out = []
    for u in req["unlocked"]:
        vers = versions_on_box(u["source"], search_dirs, platform)
        sat = [v for v in vers if u["constraint"] is None or satisfies(v, u["constraint"])]
        out.append({"root": u["root"], "source": u["source"], "constraint": u["constraint"], "on_box": vers, "best": sat[-1] if sat else None})
    return out


def read_required(args_path=None):
    p = pathlib.Path(args_path) if args_path else REQUIRED_PATH
    if p.is_file():
        return json.loads(p.read_text(encoding="utf-8"))
    return build_required()


def run_located(req, search_dirs, platform):
    recs = [locate_one(p, search_dirs, platform) for p in req["providers"]]
    return recs


def cmd_located(args):
    req = build_required(getattr(args, "all_roots", False))
    search = [pathlib.Path(s) for s in args.search] if args.search else default_search_dirs()
    print("search dirs (%d): %s" % (len(search), "; ".join(str(s) for s in search)))
    recs = run_located(req, search, args.platform)
    found = [r for r in recs if r["path"] is not None]
    for r in recs:
        if r["path"] is None:
            print("NOT-ON-THIS-BOX %s %s" % (r["source"], r["version"]))
        else:
            print("FOUND %s %s  %s  size=%d  h1=%s (%s)" % (r["source"], r["version"], str(r["path"]).replace("\\", "/"), r["size"], r["h1"], {True: "MATCHES-LOCK", False: "DOES-NOT-MATCH-LOCK", None: "NO-LOCK-HASH"}[r["h1_match"]]))
    for u in resolve_unlocked(req, search, args.platform):
        print("UNLOCKED root=%s %s constraint=%s on_box=%s best=%s" % (u["root"], u["source"], u["constraint"], ",".join(u["on_box"]) or "none", u["best"] or "none"))
    h = sum(1 for r in found if r["h1_match"])
    ok = len(found) + (len(recs) - len(found)) == len(recs)
    print("TF-LOCATED distinct_versions=%d found=%d not_on_this_box=%d h1_verified=%d/%d bytes=%d ok=%s"
          % (len(recs), len(found), len(recs) - len(found), h, len(found), sum(r["size"] for r in found), ok))
    return 0 if ok else 1


# ---------------------------------------------------------------- the Terraform binary (AMENDMENT 4)


def wrapper_tools_dir(tools_dir=None):
    """The directory .tools/safe-apply.sh calls SCRIPT_DIR when a seat runs it from the BASE checkout (first worktree entry)."""
    if tools_dir:
        return pathlib.Path(tools_dir)
    wts = worktrees()
    return (wts[0] if wts else ROOT) / ".tools"


def terraform_run_env(extra=None):
    env = dict(os.environ)
    for k in ("TF_CLI_ARGS", "TF_CLI_ARGS_init", "TF_CLI_ARGS_plan", "TF_LOG", "TF_DATA_DIR"):
        env.pop(k, None)
    env["CHECKPOINT_DISABLE"] = "1"  # no version-check call to any server
    env["TF_IN_AUTOMATION"] = "1"
    if extra:
        env.update(extra)
    return env


def run_version(path, timeout=120):
    """-> (rc, stdout+stderr) of `<path> version -json`."""
    try:
        p = subprocess.run([str(path), "version", "-json"], capture_output=True, text=True, timeout=timeout, env=terraform_run_env())
        return p.returncode, p.stdout + p.stderr
    except (OSError, subprocess.SubprocessError) as exc:
        return 1, "RUN-FAILED %s" % exc


def parse_version(text):
    try:
        data = json.loads(text)
        return data.get("terraform_version"), data.get("platform")
    except ValueError:
        return None, None


def path_lookup(env_path=None):
    """The first PATH entry holding terraform or terraform.exe, in PATH order, as bash `command -v terraform` finds it."""
    for d in (env_path if env_path is not None else os.environ.get("PATH", "")).split(os.pathsep):
        if not d:
            continue
        for name in ("terraform", "terraform.exe"):
            c = pathlib.Path(d) / name
            if c.is_file():
                return c
    return None


def resolve_binary(tools_dir=None, env=None, env_path=None):
    """Resolve exactly as .tools/safe-apply.sh does: override, sibling, PATH. -> dict(sources, winner, path, source)."""
    env = os.environ if env is None else env
    sibling = wrapper_tools_dir(tools_dir) / "terraform.exe"
    sources = []
    ov = env.get(OVERRIDE_ENV, "")
    sources.append({"source": "override", "path": pathlib.Path(ov) if ov else None, "set": bool(ov), "exists": bool(ov) and pathlib.Path(ov).is_file()})
    sources.append({"source": "sibling", "path": sibling, "set": True, "exists": sibling.is_file()})
    pth = path_lookup(env_path)
    sources.append({"source": "path", "path": pth, "set": pth is not None, "exists": pth is not None})
    winner = None
    if ov:
        winner = sources[0]  # the wrapper takes a non-empty override as given and never falls through
    elif sibling.is_file():
        winner = sources[1]
    elif pth is not None:
        winner = sources[2]
    return {"sources": sources, "winner": winner, "path": winner["path"] if winner else None, "source": winner["source"] if winner else None}


def describe_binary(path, source=None):
    """-> dict(path, source, size, sha256, version, platform, rc) or None when path is not a file."""
    path = pathlib.Path(path)
    if not path.is_file():
        return None
    rc, out = run_version(path)
    ver, plat = parse_version(out) if rc == 0 else (None, None)
    return {"path": path, "source": source, "size": path.stat().st_size, "sha256": sha256_file(path), "version": ver, "platform": plat, "rc": rc}


def cmd_binary(args):
    res = resolve_binary(args.tools_dir)
    print("wrapper order (.tools/safe-apply.sh): $%s, then <base>/.tools/terraform.exe (the sibling), then PATH" % OVERRIDE_ENV)
    own = ROOT / ".tools" / "terraform.exe"
    base_tools = wrapper_tools_dir(args.tools_dir)
    print("sibling directory resolved as the base checkout's .tools: %s" % str(base_tools).replace("\\", "/"))
    if os.path.normcase(str(own.parent)) != os.path.normcase(str(base_tools)):
        print("this worktree's own .tools/terraform.exe: %s" % ("PRESENT" if own.is_file() else "ABSENT"))
    infos = {}
    for src in res["sources"]:
        label = src["source"]
        if src["path"] is None:
            print("  %-8s not set" % label)
            continue
        if not src["exists"]:
            print("  %-8s %s  ABSENT" % (label, str(src["path"]).replace("\\", "/")))
            continue
        info = describe_binary(src["path"], label)
        infos[label] = info
        print("  %-8s %s  size=%d sha256=%s version=%s platform=%s" % (label, str(info["path"]).replace("\\", "/"), info["size"], info["sha256"][:12], info["version"], info["platform"]))
    distinct = {(i["version"], i["sha256"]) for i in infos.values()}
    if len(infos) > 1 and len(distinct) > 1:
        print("SOURCES-DISAGREE: %s" % "; ".join("%s=%s" % (k, v["version"]) for k, v in infos.items()))
    if res["winner"] is None:
        print("the wrapper would run: NOTHING (it exits 5, no terraform binary found)")
        print("TF-BINARY found=False version=none platform=none sha256=none bytes=0 source=none ok=False")
        return 1
    print("the wrapper would run: %s (source=%s)" % (str(res["path"]).replace("\\", "/"), res["source"]))
    win = infos.get(res["source"])
    if win is None:
        print("TF-BINARY found=False version=none platform=none sha256=none bytes=0 source=%s ok=False" % res["source"])
        return 1
    ok = win["rc"] == 0 and win["version"] is not None
    print("TF-BINARY found=True version=%s platform=%s sha256=%s bytes=%d source=%s ok=%s" % (win["version"], win["platform"], win["sha256"][:12], win["size"], res["source"], ok))
    return 0 if ok else 1


# ---------------------------------------------------------------- the CLI config and the commands this tool builds


def config_snippet(mirror_path):
    path = mirror_path if str(mirror_path).startswith("<") else pathlib.Path(mirror_path).resolve().as_posix()
    return (
        "provider_installation {\n"
        "  filesystem_mirror {\n"
        "    path    = \"%s\"\n"
        "    include = [\"%s/*/*\"]\n"
        "  }\n"
        "  direct {\n"
        "    exclude = [\"%s/*/*\"]\n"
        "  }\n"
        "}\n" % (path, HOST, HOST))


def terraform_init_command():
    """The one terraform command the kit's probe runs: init against the mirror, no backend, no prompt."""
    return ["terraform", "init", "-backend=false", "-input=false", "-no-color"]


def readback_init_command(root):
    return ["terraform", "-chdir=%s" % root, "init", "-input=false", "-no-color"]


def readback_plan_command(root):
    return ["terraform", "-chdir=%s" % root, "plan", "-input=false", "-lock=false", "-detailed-exitcode", "-no-color"]


def constructed_commands():
    """Every command string this tool constructs, for the no-registry-address assertion."""
    return [" ".join(terraform_init_command()), "git worktree list --porcelain", config_snippet("mirror"),
            " ".join(["terraform", "version", "-json"]), " ".join(readback_init_command("root")), " ".join(readback_plan_command("root"))]


# ---------------------------------------------------------------- pack and verify


def place(src, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        dst.unlink()
    try:
        os.link(str(src), str(dst))
        return "link"
    except OSError:
        shutil.copy2(str(src), str(dst))
        return "copy"


def pack(targets, search_dirs, out_dir, platform=PLATFORM, binary=None, zip_dirs=None):
    """targets: [{source, version, h1:[...]}]; binary: a describe_binary() dict or None. -> (summary dict, manifest dict)."""
    out_dir = pathlib.Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    entries, missing, linked, copied, h1_rows = [], [], 0, 0, []
    for prov in targets:
        zsrc = find_zip(prov["source"], prov["version"], platform, zip_dirs)
        if zsrc is not None:
            # AMENDMENT 9: a release zip is laid out as the PACKED mirror form; Terraform hashes it as zh: (the zip) and h1: (its
            # contents), so a lock that holds only another platform's h1 but carries the zh list still accepts it.
            host, ns, typ = prov["source"].split("/")
            zh = "zh:" + sha256_file(zsrc)
            h1 = h1_of_zip(zsrc)
            match = None if not (prov.get("h1") or prov.get("zh")) else (zh in prov.get("zh", []) or h1 in prov.get("h1", []))
            if match is False:
                missing.append("%s@%s (zip %s matches NO lock hash)" % (prov["source"], prov["version"], zsrc.name))
                continue
            dest = out_dir / host / ns / typ / zsrc.name
            how = place(zsrc, dest)
            linked += how == "link"
            copied += how == "copy"
            entries.append({"path": dest.relative_to(out_dir).as_posix(), "sha256": sha256_file(dest), "size": dest.stat().st_size,
                            "provider": prov["source"], "version": prov["version"]})
            h1_rows.append({"provider": prov["source"], "version": prov["version"], "h1": h1, "zh": zh, "form": "zip", "matches_lock": match})
            continue
        rec = locate_one(prov, search_dirs, platform)
        if rec["path"] is None:
            missing.append("%s@%s" % (prov["source"], prov["version"]))
            continue
        host, ns, typ = prov["source"].split("/")
        dest = out_dir / host / ns / typ / prov["version"] / platform
        for f in sorted(p for p in pathlib.Path(rec["path"]).rglob("*") if p.is_file()):
            rel = f.relative_to(rec["path"])
            how = place(f, dest / rel)
            linked += how == "link"
            copied += how == "copy"
            placed = dest / rel
            entries.append({
                "path": placed.relative_to(out_dir).as_posix(),
                "sha256": sha256_file(placed),
                "size": placed.stat().st_size,
                "provider": prov["source"],
                "version": prov["version"],
            })
        h1_rows.append({"provider": prov["source"], "version": prov["version"], "h1": rec["h1"], "form": "unpacked", "matches_lock": rec["h1_match"]})
    manifest = {"kind": "terraform-filesystem-mirror", "platform": platform, "files": entries, "providers": h1_rows}
    bin_bytes = 0
    if binary is not None:
        dest_bin = out_dir / BIN_REL
        how = place(pathlib.Path(os.path.realpath(str(binary["path"]))), dest_bin)
        linked += how == "link"
        copied += how == "copy"
        manifest["binary"] = {"path": BIN_REL, "sha256": sha256_file(dest_bin), "size": dest_bin.stat().st_size,
                              "version": binary["version"], "platform": binary["platform"], "resolved_by": binary.get("source")}
        bin_bytes = dest_bin.stat().st_size
    (out_dir / MANIFEST).write_text(json.dumps(manifest, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    (out_dir / SNIPPET_NAME).write_text(
        "# Put this block in the Terraform CLI config file (%APPDATA%/terraform.rc on Windows), with path set to the\n"
        "# absolute path of the mirror directory on THIS box. 'verify --from <dir> --write-config <file>' writes it filled in.\n"
        + config_snippet("<ABSOLUTE-PATH-OF-THE-MIRROR-DIRECTORY>"), encoding="utf-8")
    summary = {"providers": len(h1_rows), "files": len(entries), "bytes": sum(e["size"] for e in entries), "linked": linked,
               "copied": copied, "not_on_box": missing, "h1_mismatch": [r for r in h1_rows if r["matches_lock"] is False],
               "binary": manifest.get("binary"), "binary_bytes": bin_bytes}
    return summary, manifest


def cmd_pack(args):
    req = build_required(getattr(args, "all_roots", False))
    targets = list(req["providers"])
    if args.only:
        sel = []
        for o in args.only:
            src, _, ver = o.partition("@")
            src = norm_source(src)
            sel.extend(t for t in targets if t["source"] == src and (not ver or t["version"] == ver))
        if not sel:
            print("ERROR: --only matched no locked provider")
            return 1
        targets = sel
    search = [pathlib.Path(s) for s in args.search] if args.search else default_search_dirs()
    if args.include_unlocked:
        for u in resolve_unlocked(req, search, args.platform):
            if u["best"] and not any(t["source"] == u["source"] and t["version"] == u["best"] for t in targets):
                targets.append({"source": u["source"], "version": u["best"], "h1": []})
                print("INCLUDE-UNLOCKED %s %s (root %s constraint %s)" % (u["source"], u["best"], u["root"], u["constraint"]))
    binary = None
    if not args.no_binary:
        res = resolve_binary()
        binary = describe_binary(res["path"], res["source"]) if res["path"] is not None else None
        if binary is None or binary["rc"] != 0:
            print("ERROR: no usable terraform binary by the wrapper resolution order (use --no-binary to pack providers alone)")
            return 1
        print("BINARY %s (source=%s) version=%s platform=%s sha256=%s" % (str(binary["path"]).replace("\\", "/"), binary["source"], binary["version"], binary["platform"], binary["sha256"][:12]))
    summary, _m = pack(targets, search, args.out, args.platform, binary, getattr(args, "mirror_zips", None))
    for r in _m["providers"]:
        print("PACKED %s %s  form=%s h1=%s%s (%s)" % (r["provider"], r["version"], r.get("form", "unpacked"), r["h1"], " " + r["zh"] if r.get("zh") else "", {True: "MATCHES-LOCK", False: "DOES-NOT-MATCH-LOCK", None: "UNLOCKED-NO-HASH-TO-CHECK"}[r["matches_lock"]]))
    for m in summary["not_on_box"]:
        print("NOT-ON-THIS-BOX %s" % m)
    ok = not summary["not_on_box"] and summary["providers"] > 0
    print("TF-PACK out=%s providers=%d files=%d bytes=%d binary=%s binary_bytes=%d linked=%d copied=%d not_on_box=%d h1_mismatch=%d ok=%s"
          % (pathlib.Path(args.out).name, summary["providers"], summary["files"], summary["bytes"],
             summary["binary"]["version"] if summary["binary"] else "none", summary["binary_bytes"], summary["linked"],
             summary["copied"], len(summary["not_on_box"]), len(summary["h1_mismatch"]), ok))
    return 0 if ok else 1


def verify(directory, run_binary=False, runner=None):
    """-> dict(files, verified, mismatched, missing, unlisted, problems, binary, binary_run).

    The binary is hashed against the manifest FIRST; it is executed (`version -json`, only with run_binary) only when the whole pack
    verified with no problem at all. runner(path) -> (rc, text) is the execution seam (default run_version)."""
    directory = pathlib.Path(directory)
    mf = directory / MANIFEST
    res = {"files": 0, "verified": 0, "mismatched": 0, "missing": 0, "unlisted": 0, "problems": [], "binary": "absent",
           "binary_run": "not-requested", "binary_version": None, "has_binary": False, "binary_entry": None}
    if not mf.is_file():
        res["problems"].append("no %s" % MANIFEST)
        return res
    manifest = json.loads(mf.read_text(encoding="utf-8"))
    problems, verified, mism, miss = [], 0, 0, 0
    listed = set()
    for e in manifest["files"]:
        listed.add(e["path"])
        f = directory / e["path"]
        if not f.is_file():
            miss += 1
            problems.append("MISSING %s" % e["path"])
        elif f.stat().st_size != e["size"] or sha256_file(f) != e["sha256"]:
            mism += 1
            problems.append("MISMATCH %s" % e["path"])
        else:
            verified += 1
    unlisted = 0
    for dirpath, _dirs, files in os.walk(directory / HOST) if (directory / HOST).is_dir() else []:
        for fn in files:
            rel = (pathlib.Path(dirpath) / fn).relative_to(directory).as_posix()
            if rel not in listed:
                unlisted += 1
                problems.append("UNLISTED %s" % rel)
    mb = manifest.get("binary")
    if mb is not None:
        listed.add(mb["path"])
        bf = directory / mb["path"]
        if not bf.is_file():
            res["binary"] = "missing"
            problems.append("MISSING %s" % mb["path"])
        elif bf.stat().st_size != mb["size"] or sha256_file(bf) != mb["sha256"]:
            res["binary"] = "mismatch"
            problems.append("MISMATCH %s" % mb["path"])
        else:
            res["binary"] = "ok"
    if (directory / "bin").is_dir():
        for dirpath, _dirs, files in os.walk(directory / "bin"):
            for fn in files:
                rel = (pathlib.Path(dirpath) / fn).relative_to(directory).as_posix()
                if rel not in listed:
                    unlisted += 1
                    problems.append("UNLISTED %s" % rel)
    if run_binary:
        if mb is None:
            res["binary_run"] = "refused-no-binary-in-manifest"
            problems.append("--run-binary asked but the manifest carries no binary")
        elif problems:
            res["binary_run"] = "refused-before-run"
        else:
            rc, text = (runner or run_version)(directory / mb["path"])
            ver, plat = parse_version(text) if rc == 0 else (None, None)
            res["binary_version"] = ver
            if rc == 0 and ver == mb["version"] and plat == mb["platform"]:
                res["binary_run"] = "ok"
            else:
                res["binary_run"] = "mismatch"
                problems.append("BINARY-RUN reported version=%s platform=%s rc=%d; the manifest says version=%s platform=%s" % (ver, plat, rc, mb["version"], mb["platform"]))
    res.update({"files": len(manifest["files"]), "verified": verified, "mismatched": mism, "missing": miss, "unlisted": unlisted,
                "problems": problems, "has_binary": mb is not None, "binary_entry": mb})
    return res


def install_binary(directory, target, mb):
    """Copy the verified packed binary to target (a file path, or a directory -> terraform.exe in it); never clobber a different file.
    -> (ok, message, final path)."""
    target = pathlib.Path(target)
    if target.is_dir():
        target = target / "terraform.exe"
    src = pathlib.Path(directory) / mb["path"]
    shown = str(target).replace("\\", "/")
    if target.exists():
        if sha256_file(target) == mb["sha256"]:
            return True, "INSTALLED %s already holds the identical binary (sha256 %s)" % (shown, mb["sha256"][:12]), target
        return False, "REFUSED to overwrite %s: it holds a different file; move it aside first" % shown, target
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(str(src), str(target))
    if target.stat().st_size != mb["size"] or sha256_file(target) != mb["sha256"]:
        return False, "INSTALL-FAILED the copy at %s does not match the manifest" % shown, target
    return True, "INSTALLED %s sha256=%s re-verified against the manifest" % (shown, mb["sha256"][:12]), target


def cmd_verify(args):
    res = verify(args.from_dir, run_binary=args.run_binary)
    for pr in res["problems"]:
        print(pr)
    ok = not res["problems"] and (res["files"] > 0 or res["has_binary"])
    installed = "-"
    if ok:
        if args.run_binary:
            print("BINARY-RUN version=%s matches the manifest (platform %s)" % (res["binary_version"], res["binary_entry"]["platform"]))
        snippet = config_snippet(args.from_dir)
        print("CLI config block (merge into the Terraform CLI config file):")
        print(snippet)
        if args.write_config:
            pathlib.Path(args.write_config).write_text(snippet, encoding="utf-8")
            print("wrote %s" % args.write_config)
        if res["has_binary"]:
            tools = wrapper_tools_dir()
            print("BINARY-PLACEMENT .tools/safe-apply.sh resolves terraform in this order: $%s, then <base checkout>/.tools/terraform.exe (the sibling), then PATH." % OVERRIDE_ENV)
            print("BINARY-PLACEMENT on a box with none of the three the wrapper takes the sibling first: install to %s (gitignored; no path is baked into any file), or put a directory holding terraform.exe on PATH."
                  % str(tools / "terraform.exe").replace("\\", "/"))
            if args.install_binary:
                iok, msg, _final = install_binary(args.from_dir, args.install_binary, res["binary_entry"])
                print(msg)
                installed = "yes" if iok else "no"
                ok = ok and iok
        elif args.install_binary:
            print("REFUSED: --install-binary asked but the pack carries no binary")
            installed = "no"
            ok = False
    else:
        print("REFUSED: the pack does not match its manifest; do not use it" + (" (the binary was not executed)" if args.run_binary else ""))
        if args.install_binary:
            installed = "no"
    print("TF-VERIFY from=%s files=%d verified=%d/%d mismatched=%d missing=%d unlisted=%d binary=%s run=%s installed=%s ok=%s"
          % (pathlib.Path(args.from_dir).name, res["files"], res["verified"], res["files"], res["mismatched"], res["missing"], res["unlisted"],
             res["binary"], res["binary_run"], installed, ok))
    return 0 if ok else 1


def run_tf(argv, cwd, env, timeout):
    """Run one terraform command; -> (rc, text). rc 124 is a timeout."""
    try:
        p = subprocess.run(argv, cwd=cwd, env=env, capture_output=True, text=True, timeout=timeout)
        return p.returncode, p.stdout + p.stderr
    except subprocess.TimeoutExpired:
        return 124, "TIMEOUT after %ds" % timeout
    except OSError as exc:
        return 1, "RUN-FAILED %s" % exc


def cmd_readback(args):
    """The Dell read-back: (a) terraform version through the wrapper resolution; (b) init with the mirror config, then one no-op plan."""
    res = resolve_binary(args.tools_dir)
    if res["path"] is None or not pathlib.Path(res["path"]).is_file():
        print("ERROR: the wrapper resolution finds no terraform binary (override, sibling, PATH)")
        print("TF-READBACK version=none init=fail plan_exit=- ok=False")
        return 1
    tf = str(res["path"])
    print("(a) terraform resolved by the wrapper order: %s (source=%s)" % (tf.replace("\\", "/"), res["source"]))
    rc, out = run_version(tf)
    ver, plat = parse_version(out) if rc == 0 else (None, None)
    print("(a) terraform version -json rc=%d version=%s platform=%s" % (rc, ver, plat))
    if rc != 0:
        print("TF-READBACK version=none init=fail plan_exit=- ok=False")
        return 1
    extra = {}
    cfg_path = None
    if args.config:
        extra["TF_CLI_CONFIG_FILE"] = str(pathlib.Path(args.config).resolve())
    elif args.from_dir:
        fd, cfg_path = tempfile.mkstemp(suffix=".rc")
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(config_snippet(args.from_dir))
        extra["TF_CLI_CONFIG_FILE"] = cfg_path
        print("(b) CLI config: the pack mirror at %s, registry excluded" % pathlib.Path(args.from_dir).resolve().as_posix())
    else:
        print("(b) CLI config: none given (--from or --config); this box own Terraform CLI config applies")
    init_only = getattr(args, "init_only", False)
    data_dir = None
    if init_only:
        # AMENDMENT 9: init only, NO backend (no state read, no plan): the pack is the sole provider source (the laptop's own plugin
        # cache variable is dropped), a package that matches no locked hash is an init error, and the .terraform data directory
        # lives in a scratch directory.
        data_dir = tempfile.mkdtemp(prefix="tfdata_")
        extra["TF_DATA_DIR"] = data_dir
    env = terraform_run_env(extra)
    if init_only and "TF_CLI_CONFIG_FILE" in extra:
        env.pop("TF_PLUGIN_CACHE_DIR", None)
    root = str(pathlib.Path(args.root).resolve())
    prc = 1
    try:
        if init_only:
            lockp = pathlib.Path(root) / LOCK_NAME
            before = lockp.read_bytes() if lockp.is_file() else None
            try:
                irc, iout = run_tf([tf, "-chdir=%s" % root, "init", "-backend=false", "-input=false", "-no-color"], None, env, args.timeout)
                after = lockp.read_bytes() if lockp.is_file() else None
            finally:
                # init may prune or add lock entries (a lock entry the root no longer requires, a package hash it records);
                # the root's lock file is put back byte for byte so the read-back leaves the tree as it found it.
                if before is not None:
                    lockp.write_bytes(before)
            print("(b) init -backend=false rc=%d  lock file %s" % (irc, "ABSENT" if before is None else ("unchanged by init" if before == after else "CHANGED by init (restored)")))
            for ln in iout.strip().splitlines():
                if ln.strip():
                    print("    init> %s" % ln.strip())
            if irc != 0:
                print("TF-READBACK version=%s init=fail plan_exit=- ok=False" % ver)
                return 1
            print("TF-READBACK version=%s init=ok plan_exit=skipped ok=True" % ver)
            return 0
        irc, iout = run_tf([tf] + readback_init_command(root)[1:], None, env, args.timeout)
        print("(b) init rc=%d" % irc)
        for ln in iout.strip().splitlines()[-6:]:
            print("    init> %s" % ln.strip())
        if irc != 0:
            print("TF-READBACK version=%s init=fail plan_exit=- ok=False" % ver)
            return 1
        prc, pout = run_tf([tf] + readback_plan_command(root)[1:], None, env, args.timeout)
        for ln in pout.strip().splitlines()[-6:]:
            print("    plan> %s" % ln.strip())
    finally:
        if cfg_path is not None:
            try:
                os.unlink(cfg_path)
            except OSError:
                pass
        if data_dir is not None:
            shutil.rmtree(data_dir, ignore_errors=True)
    if prc == 2:
        print("!!! PLAN EXIT 2: CHANGES ARE PRESENT in %s. This is not a failure of the kit; it is a finding about the root." % root.replace("\\", "/"))
    elif prc == 0:
        print("(b) plan exit 0: no changes")
    else:
        print("(b) plan exit %d: ERROR" % prc)
    ok = prc in (0, 2)
    print("TF-READBACK version=%s init=ok plan_exit=%d ok=%s" % (ver, prc, ok))
    return 0 if ok else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description="Terraform provider kit: read the locks, find binaries on this box, pack a filesystem mirror, verify it.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("required")
    p.add_argument("--out")
    p.add_argument("--all-roots", action="store_true")
    p = sub.add_parser("located")
    p.add_argument("--all-roots", action="store_true")
    p.add_argument("--search", action="append")
    p.add_argument("--platform", default=PLATFORM)
    p = sub.add_parser("pack")
    p.add_argument("--out", required=True)
    p.add_argument("--search", action="append")
    p.add_argument("--platform", default=PLATFORM)
    p.add_argument("--only", action="append")
    p.add_argument("--include-unlocked", action="store_true")
    p.add_argument("--no-binary", action="store_true")
    p.add_argument("--all-roots", action="store_true")
    p.add_argument("--mirror-zips", action="append")
    p = sub.add_parser("verify")
    p.add_argument("--from", dest="from_dir", required=True)
    p.add_argument("--write-config")
    p.add_argument("--run-binary", action="store_true")
    p.add_argument("--install-binary")
    p = sub.add_parser("binary")
    p.add_argument("--tools-dir")
    p = sub.add_parser("readback")
    p.add_argument("--root", required=True)
    p.add_argument("--from", dest="from_dir")
    p.add_argument("--config")
    p.add_argument("--tools-dir")
    p.add_argument("--timeout", type=int, default=600)
    p.add_argument("--init-only", action="store_true")
    args = ap.parse_args(argv)
    return {"required": cmd_required, "located": cmd_located, "pack": cmd_pack, "verify": cmd_verify, "binary": cmd_binary,
            "readback": cmd_readback}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
