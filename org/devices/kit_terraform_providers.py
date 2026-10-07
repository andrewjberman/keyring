"""kit_terraform_providers.py -- the Terraform provider kit (NFRA_CTLPLN PRD v0.14 C-KIT-PYTHON, TO-CT-k-2 AMENDMENT 1).

A box that cannot reach a provider registry cannot run `terraform init`. This kit reads which provider versions the Dell-placed
projects' Terraform roots lock, finds those provider binaries ALREADY on this machine's disk, lays them out as a Terraform
FILESYSTEM MIRROR with a checksum manifest and the CLI-config snippet that makes `terraform init` read the mirror and never the
registry, and verifies such a pack on the receiving box. Pure stdlib. NO NETWORK: nothing here downloads, and no command this tool
constructs names a registry address or a downloading verb (a test asserts it).

    python org/devices/kit_terraform_providers.py required [--out <json>]
    python org/devices/kit_terraform_providers.py located  [--search <dir> ...] [--platform windows_amd64]
    python org/devices/kit_terraform_providers.py pack --out <dir> [--search <dir> ...] [--only <ns/type[@ver]> ...] [--include-unlocked]
    python org/devices/kit_terraform_providers.py verify --from <dir> [--write-config <file>]

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


def build_required():
    roots = derive_roots()
    rows, providers, unlocked, errors = [], {}, [], []
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
    req = build_required()
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
    req = build_required()
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


def constructed_commands():
    """Every command string this tool constructs, for the no-registry-address assertion."""
    return [" ".join(terraform_init_command()), "git worktree list --porcelain", config_snippet("mirror")]


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


def pack(targets, search_dirs, out_dir, platform=PLATFORM):
    """targets: [{source, version, h1:[...]}]. -> (summary dict, manifest dict)."""
    out_dir = pathlib.Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    entries, missing, linked, copied, h1_rows = [], [], 0, 0, []
    for prov in targets:
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
        h1_rows.append({"provider": prov["source"], "version": prov["version"], "h1": rec["h1"], "matches_lock": rec["h1_match"]})
    manifest = {"kind": "terraform-filesystem-mirror", "platform": platform, "files": entries, "providers": h1_rows}
    (out_dir / MANIFEST).write_text(json.dumps(manifest, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    (out_dir / SNIPPET_NAME).write_text(
        "# Put this block in the Terraform CLI config file (%APPDATA%/terraform.rc on Windows), with path set to the\n"
        "# absolute path of the mirror directory on THIS box. 'verify --from <dir> --write-config <file>' writes it filled in.\n"
        + config_snippet("<ABSOLUTE-PATH-OF-THE-MIRROR-DIRECTORY>"), encoding="utf-8")
    summary = {"providers": len(h1_rows), "files": len(entries), "bytes": sum(e["size"] for e in entries), "linked": linked,
               "copied": copied, "not_on_box": missing, "h1_mismatch": [r for r in h1_rows if r["matches_lock"] is False]}
    return summary, manifest


def cmd_pack(args):
    req = build_required()
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
    summary, _m = pack(targets, search, args.out, args.platform)
    for r in _m["providers"]:
        print("PACKED %s %s  h1=%s (%s)" % (r["provider"], r["version"], r["h1"], {True: "MATCHES-LOCK", False: "DOES-NOT-MATCH-LOCK", None: "UNLOCKED-NO-HASH-TO-CHECK"}[r["matches_lock"]]))
    for m in summary["not_on_box"]:
        print("NOT-ON-THIS-BOX %s" % m)
    ok = not summary["not_on_box"] and summary["providers"] > 0
    print("TF-PACK out=%s providers=%d files=%d bytes=%d linked=%d copied=%d not_on_box=%d h1_mismatch=%d ok=%s"
          % (pathlib.Path(args.out).name, summary["providers"], summary["files"], summary["bytes"], summary["linked"],
             summary["copied"], len(summary["not_on_box"]), len(summary["h1_mismatch"]), ok))
    return 0 if ok else 1


def verify(directory):
    """-> dict(files, verified, mismatched, missing, unlisted, problems)"""
    directory = pathlib.Path(directory)
    mf = directory / MANIFEST
    if not mf.is_file():
        return {"files": 0, "verified": 0, "mismatched": 0, "missing": 0, "unlisted": 0, "problems": ["no %s" % MANIFEST]}
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
    return {"files": len(manifest["files"]), "verified": verified, "mismatched": mism, "missing": miss, "unlisted": unlisted, "problems": problems}


def cmd_verify(args):
    res = verify(args.from_dir)
    for p in res["problems"]:
        print(p)
    ok = not res["problems"] and res["files"] > 0
    if ok:
        snippet = config_snippet(args.from_dir)
        print("CLI config block (merge into the Terraform CLI config file):")
        print(snippet)
        if args.write_config:
            pathlib.Path(args.write_config).write_text(snippet, encoding="utf-8")
            print("wrote %s" % args.write_config)
    else:
        print("REFUSED: the pack does not match its manifest; do not use it")
    print("TF-VERIFY from=%s files=%d verified=%d/%d mismatched=%d missing=%d unlisted=%d ok=%s"
          % (pathlib.Path(args.from_dir).name, res["files"], res["verified"], res["files"], res["mismatched"], res["missing"], res["unlisted"], ok))
    return 0 if ok else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description="Terraform provider kit: read the locks, find binaries on this box, pack a filesystem mirror, verify it.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("required")
    p.add_argument("--out")
    p = sub.add_parser("located")
    p.add_argument("--search", action="append")
    p.add_argument("--platform", default=PLATFORM)
    p = sub.add_parser("pack")
    p.add_argument("--out", required=True)
    p.add_argument("--search", action="append")
    p.add_argument("--platform", default=PLATFORM)
    p.add_argument("--only", action="append")
    p.add_argument("--include-unlocked", action="store_true")
    p = sub.add_parser("verify")
    p.add_argument("--from", dest="from_dir", required=True)
    p.add_argument("--write-config")
    args = ap.parse_args(argv)
    return {"required": cmd_required, "located": cmd_located, "pack": cmd_pack, "verify": cmd_verify}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
