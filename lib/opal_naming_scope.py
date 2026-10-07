#!/usr/bin/env python3
"""opal_naming_scope -- the names the naming check reads for ONE Terraform root (LGIC_BLANKFIX BF-t-1).

`python lib/opal_naming.py census --repo` reads the whole repository. This module cuts the repository plane down to one
Terraform root: the root's own .tf names plus the names in the Lambda source folders the root deploys. The tie from a root
to a source folder is DERIVED from the repository, never typed; three kinds of evidence are read:

  source-map   infra/aws/lambda/ci/lambda-source-map.json: a function whose tf_file sits in the root and whose source_dir
               is a real tracked folder.
  tf-path      a non-comment line of the root's .tf files that names a tracked folder under infra/aws/lambda/
               (a `../lambda/<dir>/...` path, an `infra/aws/lambda/<dir>` path or `lambda_base_dir}/<dir>`).
  artifact-key an `artifact_key = "<prefix>/..."` literal in the root's .tf files, where infra/aws/lambda/<prefix>/ is a
               tracked folder (the pipeline folder the root's artifacts are built from).

A folder tied to two roots, or overlapping (ancestor or descendant of) a folder tied to another root, is CONTESTED: it is
reported under stats["contested_dirs"] and assigned to no root -- unless a root map (--map PATH, the short list) names the
one root that reads it: a map entry may carry "source_dirs": ["<repo-relative folder>", ...]. A contested folder listed by
exactly one entry is assigned to that root (and its un-tied sub-folders with it, the longest listed folder winning); a
folder listed by two entries raises ValueError; one no entry lists stays unassigned. A map key is a root's folder path
under infra/aws/terraform/, its full repo path, or its folder name when that is unique. With no map nothing changes.

Commands (each takes an optional --map PATH):
  python lib/opal_naming_scope.py items ROOT
  python lib/opal_naming_scope.py table
  python lib/opal_naming_scope.py pick
  python lib/opal_naming_scope.py contested

Python 3.9 syntax; stdlib only; ASCII only.
"""
from __future__ import annotations

import json
import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
import opal_naming  # noqa: E402

REPO = opal_naming.REPO
TF_ROOT = "infra/aws/terraform/"
LAMBDA_ROOT = "infra/aws/lambda/"
SOURCE_MAP = "infra/aws/lambda/ci/lambda-source-map.json"
NOT_JUDGED = ("org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/NOT_JUDGED_R13.json")

_TF_PATH_RE = re.compile(r"(?:infra/aws/lambda/|\.\./lambda/|lambda_base_dir\}/)([A-Za-z0-9_./-]+)")
_ARTIFACT_RE = re.compile(r'artifact_key\s*=\s*"([A-Za-z0-9_.-]+)/')
_PASCAL_RE = re.compile(r"^[A-Z][a-z0-9]+(?:[A-Z][a-z0-9]*)*$")
_BLANK_RE = re.compile(r"\{([a-z_]+)\}")

_CACHE = {}


def _read_text(rel):
    with open(os.path.join(REPO, *rel.split("/")), encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _files():
    if "files" not in _CACHE:
        _CACHE["files"] = opal_naming._census_git_files()
    return _CACHE["files"]


def _census():
    if "census" not in _CACHE:
        items, stats = opal_naming.census_repo()
        _CACHE["census"] = (items, stats)
    return _CACHE["census"]


def _file_of(item):
    return item["where"].rsplit(":", 1)[0]


def _tracked_dirs():
    if "dirs" not in _CACHE:
        dirs = set()
        for f in _files():
            parts = f.split("/")
            for i in range(1, len(parts)):
                dirs.add("/".join(parts[:i]))
        _CACHE["dirs"] = dirs
    return _CACHE["dirs"]


def _tf_files():
    return sorted(f for f in _files() if f.startswith(TF_ROOT) and f.endswith(".tf"))


def _roots():
    """Terraform roots: the shallowest folder under infra/aws/terraform/ that directly holds a .tf file, per .tf file."""
    if "roots" not in _CACHE:
        direct = set(f.rsplit("/", 1)[0] for f in _tf_files())
        roots = set()
        for d in direct:
            parts = d.split("/")
            for i in range(4, len(parts) + 1):
                cand = "/".join(parts[:i])
                if cand in direct:
                    roots.add(cand)
                    break
        _CACHE["roots"] = sorted(roots)
    return _CACHE["roots"]


def _root_of_file(f):
    for r in _roots():
        if f.startswith(r + "/"):
            return r
    return None


def _norm_root(root):
    r = str(root).replace("\\", "/").strip().rstrip("/")
    if r not in _roots():
        raise ValueError("unknown Terraform root: %r" % (root,))
    return r


def _under(f, d):
    return f == d or f.startswith(d.rstrip("/") + "/")


def _item_dirs():
    """Folders (tracked) that hold at least one census source item (an item outside the Terraform folders)."""
    items, _ = _census()
    return set(_file_of(i) for i in items if not _file_of(i).startswith(TF_ROOT))


def _holds_items(d):
    return any(_under(f, d) for f in _item_dirs())


def _longest_dir(path):
    """The longest tracked folder that is a prefix of the path (a file name is dropped)."""
    parts = [p for p in path.split("/") if p and p != "."]
    while parts:
        cand = "/".join(parts)
        if cand in _tracked_dirs():
            return cand
        parts.pop()
    return None


def _ties():
    """{root: {dir: [evidence strings]}} -- every folder that holds census items and is tied to a root, per evidence."""
    if "ties" in _CACHE:
        return _CACHE["ties"]
    ties = {}

    def add(root, d, ev):
        if d is None or not _holds_items(d):
            return
        ties.setdefault(root, {}).setdefault(d, [])
        if ev not in ties[root][d]:
            ties[root][d].append(ev)

    smap = json.loads(_read_text(SOURCE_MAP)).get("functions", {})
    for fn in sorted(smap):
        row = smap[fn]
        sd, tfile = row.get("source_dir"), row.get("tf_file")
        if not sd or sd == "EXTERNAL" or not tfile:
            continue
        root = _root_of_file(tfile)
        d = sd.rstrip("/")
        if root and d in _tracked_dirs():
            add(root, d, "source-map: %s function %s tf_file=%s" % (SOURCE_MAP, fn, tfile))
    for f in _tf_files():
        root = _root_of_file(f)
        for n, line in enumerate(_read_text(f).split("\n"), 1):
            if line.strip().startswith(("#", "//")):
                continue
            for m in _TF_PATH_RE.finditer(line):
                p = m.group(1).rstrip(".")
                p = re.split(r"[$]", p)[0]
                d = _longest_dir(LAMBDA_ROOT + p)
                if d and d.startswith(LAMBDA_ROOT) and d != LAMBDA_ROOT.rstrip("/"):
                    add(root, d, "tf-path: %s:%d %s" % (f, n, m.group(0)))
            for m in _ARTIFACT_RE.finditer(line):
                d = LAMBDA_ROOT + m.group(1)
                if d in _tracked_dirs():
                    add(root, d, "artifact-key: %s:%d artifact_key prefix %s/" % (f, n, m.group(1)))
    _CACHE["ties"] = ties
    return ties


def _overlap(a, b):
    return a == b or a.startswith(b + "/") or b.startswith(a + "/")


def _resolve():
    """(per-root uncontested source dirs with basis, contested dirs {dir: [roots]})."""
    if "resolved" in _CACHE:
        return _CACHE["resolved"]
    ties = _ties()
    claims = [(r, d) for r in ties for d in ties[r]]
    contested = {}
    for r, d in claims:
        for r2, d2 in claims:
            if r2 != r and _overlap(d, d2):
                contested.setdefault(d, set()).update([r, r2])
    contested = {d: sorted(v) for d, v in sorted(contested.items())}
    per = {}
    for r in ties:
        dirs = sorted(d for d in ties[r] if d not in contested)
        keep = [d for d in dirs if not any(d != o and _under(d, o) for o in dirs)]
        basis = {}
        for k in keep:
            ev = []
            for d in dirs:
                if _under(d, k):
                    ev += ["%s => %s" % (d, e) for e in ties[r][d]] if d != k else list(ties[r][d])
            basis[k] = ev
        per[r] = (keep, basis)
    _CACHE["resolved"] = (per, contested)
    return _CACHE["resolved"]


def _map_key_root(key):
    """The Terraform root a root-map key names: full repo path, path under infra/aws/terraform/, or a unique folder name."""
    k = str(key).replace("\\", "/").strip().rstrip("/")
    roots = _roots()
    if k in roots:
        return k
    if (TF_ROOT + k) in roots:
        return TF_ROOT + k
    hits = [r for r in roots if r.rsplit("/", 1)[1] == k]
    if len(hits) == 1:
        return hits[0]
    if len(hits) > 1:
        raise ValueError("root map key %r names %d roots: %s" % (key, len(hits), ", ".join(hits)))
    raise ValueError("root map key %r names no Terraform root" % (key,))


def _map_dirs(map_path):
    """{folder: root} from the source_dirs lists of the root map at map_path; {} for no map. ValueError on a bad entry or
    on a folder two entries list."""
    if map_path is None:
        return {}
    with open(map_path, "rb") as fh:
        doc = json.loads(fh.read().decode("utf-8"))
    roots = doc.get("roots") if isinstance(doc, dict) else None
    if not isinstance(roots, dict):
        raise ValueError("root map %s: top level must be an object with a 'roots' object" % (map_path,))
    out, owner_key = {}, {}
    for key in sorted(roots):
        ent = roots[key]
        dirs = ent.get("source_dirs") if isinstance(ent, dict) else None
        if dirs is None:
            continue
        if not isinstance(dirs, list) or not all(isinstance(d, str) and d.strip() for d in dirs):
            raise ValueError("root map entry %r: source_dirs must be a list of folder strings" % (key,))
        r = _map_key_root(key)
        for d in dirs:
            d = d.replace("\\", "/").strip().rstrip("/")
            if d in out and owner_key[d] != key:
                raise ValueError("folder %s is listed by two root map entries: %r and %r" % (d, owner_key[d], key))
            out[d] = r
            owner_key[d] = key
    return out


def _listed_root(f, mdirs):
    """(root, folder) of the longest listed folder that holds the path f, or (None, None)."""
    best = None
    for d in mdirs:
        if _under(f, d) and (best is None or len(d) > len(best)):
            best = d
    return (mdirs[best], best) if best else (None, None)


def root_items(root, map_path=None):
    """(items, stats): the subset of opal_naming.census_repo()'s items that belong to the root, in its order.
    With a root map (map_path), a contested folder the map lists for this root joins its source folders."""
    r = _norm_root(root)
    per, contested = _resolve()
    keep, basis = per.get(r, ([], {}))
    items, _ = _census()
    out = [i for i in items if _under(_file_of(i), r) or any(_under(_file_of(i), d) for d in keep)]
    mdirs = {d: x for d, x in _map_dirs(map_path).items() if d in contested}
    mine = sorted(d for d in mdirs if mdirs[d] == r)
    if mine:
        base = _assignment()
        have = set(id(i) for i in out)
        out = [it for it, b in zip(items, base)
               if id(it) in have or (b is None and _listed_root(_file_of(it), mdirs)[0] == r)]
        keep, basis = list(keep) + mine, dict(basis)
        for d in mine:
            basis[d] = ["root-map: %s lists %s for %s" % (os.path.basename(str(map_path)), d, r)]
    tfs = [f for f in _tf_files() if f.startswith(r + "/")]
    stats = {"root": r, "tf_files": len(tfs), "source_dirs": list(keep), "source_dir_basis": dict(basis),
             "contested_dirs": {d: v for d, v in contested.items() if r in v}}
    return out, stats


def _cards():
    if "cards" not in _CACHE:
        with open(os.path.join(REPO, *NOT_JUDGED.split("/")), encoding="utf-8") as fh:
            _CACHE["cards"] = set((e.get("plane"), e.get("name")) for e in json.load(fh))
    return _CACHE["cards"]


def _purpose_words():
    if "pw" not in _CACHE:
        with open(os.path.join(REPO, "infra", "logic", "registry", "systems.json"), encoding="utf-8") as fh:
            _CACHE["pw"] = set(json.load(fh)["refused_keys"]["purpose_word"])
    return _CACHE["pw"]


def classify(item):
    """One of: carded, pattern, raising, A, B, C, D, plain."""
    cur = item["current"]
    if ("repo", cur) in _cards():
        return "carded"
    if "{" in cur or "%s" in cur or "*" in cur:
        return "pattern"
    try:
        _, canon = opal_naming.grade(cur, item["type"])
    except opal_naming.RaiseDefect:
        return "raising"
    blanks = set(_BLANK_RE.findall(canon or ""))
    if "system" in blanks:
        first = re.split(r"[-_/.]", cur)[0].lower()
        if item["type"] == "LAMBDA_LAYER" or (("-" not in cur) and _PASCAL_RE.match(cur)) or first in _purpose_words():
            return "A"
        return "B"
    if "cadence" in blanks:
        return "C"
    if blanks:
        return "D"
    return "plain"


def _classes():
    if "cls" not in _CACHE:
        items, _ = _census()
        _CACHE["cls"] = [classify(i) for i in items]
    return _CACHE["cls"]


def _assignment():
    """index of census item -> root or None (a contested or untied folder is None)."""
    if "assign" not in _CACHE:
        items, _ = _census()
        per, _c = _resolve()
        out = []
        for it in items:
            f, hit = _file_of(it), None
            r = _root_of_file(f)
            if r:
                hit = r
            else:
                for rr, (keep, _b) in per.items():
                    if any(_under(f, d) for d in keep):
                        hit = rr
                        break
            out.append(hit)
        _CACHE["assign"] = out
    return _CACHE["assign"]


def _assignment_with(map_path):
    """_assignment(), plus the root a contested folder is listed for in the map (an item no other rule placed)."""
    base = _assignment()
    mdirs = _map_dirs(map_path)
    if not mdirs:
        return base
    _per, contested = _resolve()
    mdirs = {d: r for d, r in mdirs.items() if d in contested}
    items, _ = _census()
    return [b if b is not None else _listed_root(_file_of(it), mdirs)[0] for it, b in zip(items, base)]


def root_table(map_path=None):
    items, _ = _census()
    cls, asg = _classes(), _assignment_with(map_path)
    rows = {}
    for it, c, r in zip(items, cls, asg):
        if r is None:
            continue
        row = rows.setdefault(r, {"root": r, "items": 0, "group_a": 0, "group_b": 0, "group_c": 0, "group_d": 0,
                                  "pattern": 0, "raising": 0, "carded": 0, "plain": 0})
        row["items"] += 1
        key = {"A": "group_a", "B": "group_b", "C": "group_c", "D": "group_d"}.get(c, c)
        row[key] += 1
    return [rows[r] for r in sorted(rows)]


def _safe(s):
    return str(s).encode("ascii", "backslashreplace").decode("ascii")


def cmd_items(root, map_path=None):
    items, st = root_items(root, map_path)
    for it in items:
        print(_safe("%s\t%s\t%s" % (it["type"], it["current"], it["where"])))
    tf_items = sum(1 for i in items if _under(_file_of(i), st["root"]))
    print("SCOPE-ITEMS ok=True root=%s items=%d tf_items=%d source_items=%d source_dirs=%d"
          % (st["root"], len(items), tf_items, len(items) - tf_items, len(st["source_dirs"])))
    return 0


def _row_text(r):
    return ("%s items=%d group_a=%d group_b=%d group_c=%d group_d=%d pattern=%d raising=%d carded=%d plain=%d"
            % (r["root"], r["items"], r["group_a"], r["group_b"], r["group_c"], r["group_d"], r["pattern"],
               r["raising"], r["carded"], r["plain"]))


def cmd_table(map_path=None):
    items, _ = _census()
    rows = root_table(map_path)
    for r in rows:
        print(_row_text(r))
    assigned = sum(r["items"] for r in rows)
    unassigned = len(items) - assigned
    _, contested = _resolve()
    where = {}
    for it, r in zip(items, _assignment_with(map_path)):
        if r is None:
            f = _file_of(it)
            k = "/".join(f.split("/")[:4]) if f.startswith(LAMBDA_ROOT) else "/".join(f.split("/")[:3])
            where[k] = where.get(k, 0) + 1
    for k in sorted(where):
        print("UNASSIGNED %d %s" % (where[k], k))
    for d in sorted(contested):
        print("CONTESTED %s roots=%s" % (d, ",".join(contested[d])))
    ok = (assigned + unassigned == len(items)) and len(rows) > 0
    print("SCOPE-TABLE ok=%s roots=%d items=%d assigned=%d unassigned=%d" % (ok, len(rows), len(items), assigned,
                                                                         unassigned))
    return 0 if ok else 1


def cmd_pick(map_path=None):
    rows = [r for r in root_table(map_path) if r["group_a"] and r["group_b"] and r["group_c"] and r["group_d"]]
    for r in rows:
        print(_row_text(r))
    if not rows:
        print("SCOPE-PICK ok=False root=NONE items=0 group_a=0 group_b=0 group_c=0 group_d=0 qualifying=0")
        return 1
    p = sorted(rows, key=lambda r: (r["items"], r["root"]))[0]
    print("SCOPE-PICK ok=True root=%s items=%d group_a=%d group_b=%d group_c=%d group_d=%d qualifying=%d"
          % (p["root"], p["items"], p["group_a"], p["group_b"], p["group_c"], p["group_d"], len(rows)))
    return 0


def _kinds(evs):
    k = {}
    for e in evs:
        n = e.split(":", 1)[0]
        k[n] = k.get(n, 0) + 1
    return ", ".join("%s x%d" % (n, k[n]) for n in sorted(k))


def contested_rows(map_path=None):
    """One dict per contested folder: dir, roots, evidence {root: (via folder, [evidence])}, items (census items under it
    that no other rule assigns, the longest contested folder owning an item), assigned (root or None)."""
    items, _ = _census()
    ties = _ties()
    _per, contested = _resolve()
    mdirs = {d: r for d, r in _map_dirs(map_path).items() if d in contested}
    base = _assignment()
    count = dict((d, 0) for d in contested)
    for it, b in zip(items, base):
        if b is not None:
            continue
        f = _file_of(it)
        own = [d for d in contested if _under(f, d)]
        if own:
            count[max(own, key=len)] += 1
    rows = []
    for d in sorted(contested):
        ev = {}
        for r in contested[d]:
            direct = ties.get(r, {}).get(d)
            if direct:
                ev[r] = (d, list(direct))
            else:
                for d2 in sorted(ties.get(r, {})):
                    if _overlap(d, d2):
                        ev[r] = (d2, list(ties[r][d2]))
                        break
        rows.append({"dir": d, "roots": list(contested[d]), "evidence": ev, "items": count[d],
                     "assigned": _listed_root(d, mdirs)[0]})
    return rows


def cmd_contested(map_path=None):
    rows = contested_rows(map_path)
    for r in rows:
        parts = []
        for root in r["roots"]:
            via, evs = r["evidence"].get(root, (r["dir"], []))
            tag = "" if via == r["dir"] else " via " + via
            parts.append("%s[%s%s]" % (root, _kinds(evs), tag))
        print(_safe("CONTESTED %s items=%d assigned=%s claimants=%d %s"
                    % (r["dir"], r["items"], r["assigned"] or "UNASSIGNED", len(r["roots"]), " ".join(parts))))
    n_items = sum(r["items"] for r in rows)
    n_asg = sum(r["items"] for r in rows if r["assigned"])
    ok = all(r["roots"] and all(root in r["evidence"] and r["evidence"][root][1] for root in r["roots"])
             for r in rows)
    print("SCOPE-CONTESTED ok=%s folders=%d items=%d assigned=%d unassigned=%d"
          % (ok, len(rows), n_items, n_asg, n_items - n_asg))
    return 0 if ok else 1


_USAGE = "usage: opal_naming_scope.py items ROOT | table | pick | contested   (each takes --map PATH)"


def main(argv):
    argv = list(argv)
    map_path = None
    if "--map" in argv:
        i = argv.index("--map")
        if i + 1 >= len(argv):
            print(_USAGE)
            return 2
        map_path = argv[i + 1]
        del argv[i:i + 2]
    cmd = argv[1] if len(argv) > 1 else ""
    try:
        if len(argv) >= 3 and cmd == "items":
            try:
                return cmd_items(argv[2], map_path)
            except ValueError as exc:
                print("SCOPE-ITEMS ok=False root=%s error=%s" % (argv[2], _safe(exc)))
                return 1
        if len(argv) == 2 and cmd == "table":
            return cmd_table(map_path)
        if len(argv) == 2 and cmd == "pick":
            return cmd_pick(map_path)
        if len(argv) == 2 and cmd == "contested":
            return cmd_contested(map_path)
    except (ValueError, OSError) as exc:
        print("SCOPE-%s ok=False error=%s" % (cmd.upper(), _safe(exc)))
        return 1
    print(_USAGE)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
