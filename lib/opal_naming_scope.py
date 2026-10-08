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
  python lib/opal_naming_scope.py unassigned   (every name still assigned to no root, grouped by folder, with its reason)

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


# ---- BF-v-4: names the literal reader does not count -------------------------------------------------------------
# census_repo() reads a name only when the name attribute of a graded resource is ONE string literal. A name built in a
# `locals` block, from a `var.`, through a module or from a generated .json is counted by nothing, so a root that builds
# all its names that way read names=0. scan_dir() reads one folder of .tf files and puts every such name in one of two
# places: COUNTED (it resolves to a literal inside the folder's own files: a literal local, a .tfvars.json value) or
# UNCOUNTED with a reason naming what was not followed: local, var, module, json, interpolation.

UNCOUNTED_REASONS = ("local", "var", "module", "json", "interpolation")
_INTERP_RE = re.compile(r"\$\{([^{}]*)\}")
_REF_LOCAL_RE = re.compile(r"^local\.([A-Za-z_][A-Za-z0-9_-]*)$")
_REF_VAR_RE = re.compile(r"^var\.([A-Za-z_][A-Za-z0-9_-]*)$")
_REF_EACH_RE = re.compile(r"^each\.(key|value(?:\.[A-Za-z_][A-Za-z0-9_-]*)*)$")
_INTERP_KIND_RE = re.compile(r"\$\{\s*(local|var|module)[.\[]")
_TAG_NAME_RE = re.compile(r'(?:^|[{,\s])"?Name"?\s*=\s*([^\n,}]+)')


class _Unres(Exception):
    """An expression the folder's own files do not resolve to a literal; .reason is what was not followed."""

    def __init__(self, reason):
        Exception.__init__(self, reason)
        self.reason = reason


def _flat(raw):
    return " ".join(str(raw).split())


def _kind_of(ref):
    """The reason a reference that is not followed carries, by what it starts with."""
    ref = ref.strip()
    for k in ("local", "var", "module"):
        if ref.startswith(k + ".") or ref.startswith(k + "["):
            return k
    return "interpolation"


def _json_line(text, path):
    """The 1-based line of the last key of `path` in a pretty-printed JSON text: each key is searched for after the line
    of the one before it. 1 when a key is not found."""
    lines, start, found = text.split("\n"), 0, 1
    for key in path:
        pat = re.compile(r'"%s"\s*:' % re.escape(str(key)))
        for n in range(start, len(lines)):
            if pat.search(lines[n]):
                found, start = n + 1, n
                break
    return found


class _Ctx(object):
    def __init__(self, locals_, jvars):
        self.locals = locals_      # name -> (raw expression, "file", line)
        self.vars = jvars          # name -> (value, "file", text)
        self.each = None           # (var name, key, value) while a for_each binding is read


def _eval(raw, ctx, depth=0):
    """(string, source) the expression spells: source is ("file", line) of the declaring line when the whole expression
    is one reference, else None. _Unres when the folder's files do not resolve it."""
    raw = str(raw).strip()
    if depth > 8:
        raise _Unres("local")
    m = opal_naming._TF_LITERAL_RE.match(raw)
    if not m:
        q = _INTERP_KIND_RE.search(raw) if raw.startswith('"') else None
        if q:
            raise _Unres(q.group(1))  # a string with a quote inside an interpolation: the first reference not followed
        return _ref(raw, ctx, depth)
    body = m.group(1)
    if "%{" in body:
        raise _Unres("interpolation")
    parts = list(_INTERP_RE.finditer(body))
    if not parts:
        if "${" in body:
            raise _Unres("interpolation")
        return body.replace('\\"', '"').replace("\\\\", "\\"), None
    if len(parts) == 1 and parts[0].span() == (0, len(body)):
        return _ref(parts[0].group(1).strip(), ctx, depth)
    out, pos = [], 0
    for p in parts:
        out.append(body[pos:p.start()])
        out.append(_ref(p.group(1).strip(), ctx, depth)[0])
        pos = p.end()
    out.append(body[pos:])
    text = "".join(out)
    if "${" in text:
        raise _Unres("interpolation")
    return text, None


def _ref(ref, ctx, depth):
    m = _REF_LOCAL_RE.match(ref)
    if m:
        row = ctx.locals.get(m.group(1))
        if row is None:
            raise _Unres("local")
        try:
            val = _eval(row[0], ctx, depth + 1)[0]
        except _Unres:
            raise _Unres("local")
        return val, (row[1], row[2])
    m = _REF_VAR_RE.match(ref)
    if m:
        row = ctx.vars.get(m.group(1))
        if row is None or not isinstance(row[0], str):
            raise _Unres("var")
        return row[0], (row[1], _json_line(row[2], [m.group(1)]))
    m = _REF_EACH_RE.match(ref)
    if m:
        if ctx.each is None:
            raise _Unres("json")
        vname, key, value = ctx.each
        _v, fname, text = ctx.vars[vname]
        path, cur = [vname, key], value
        if m.group(1) == "key":
            return key, (fname, _json_line(text, path))
        for part in m.group(1).split(".")[1:]:
            if not isinstance(cur, dict) or part not in cur:
                raise _Unres("json")
            cur = cur[part]
            path.append(part)
        if not isinstance(cur, str):
            raise _Unres("json")
        return cur, (fname, _json_line(text, path))
    raise _Unres(_kind_of(ref))


def _bindings(raw, ctx):
    """[(var name, key, value)] a for_each over a JSON-backed var spells; _Unres when it is not one."""
    m = _REF_VAR_RE.match(str(raw).strip())
    if not m:
        raise _Unres(_kind_of(str(raw)))
    row = ctx.vars.get(m.group(1))
    if row is None or not isinstance(row[0], dict):
        raise _Unres("var")
    return [(m.group(1), k, v) for k, v in row[0].items()]


def _dir_vars(directory, json_names, label):
    out = {}
    for fn in sorted(json_names):
        if not fn.endswith(".tfvars.json"):
            continue
        try:
            with open(os.path.join(directory, fn), encoding="utf-8", errors="replace") as fh:
                text = fh.read().replace("\r\n", "\n")
            doc = json.loads(text)
        except (OSError, ValueError):
            continue
        if isinstance(doc, dict):
            for k, v in doc.items():
                out[k] = (v, label + "/" + fn, text)
    return out


_SCAN_CACHE = {}


def scan_dir(directory, label, tf_names=None, json_names=None):
    """(literal, resolved, uncounted) of the .tf files in ONE folder (a Terraform configuration: its locals and its
    .tfvars.json files are the folder's own).
      literal    the names census_repo() counts (read here by the census's own reader, for a test to read once);
      resolved   the names the census cannot read that the folder's own files resolve to a literal: items
                 {plane, type, current, where};
      uncounted  one dict {type, attribute, expression, reason, where} per graded resource whose name does not resolve,
                 and per module call whose called module builds names it does not state (reason module).
    label is the repository-relative folder path that prefixes every `where`."""
    directory = os.path.abspath(directory)
    key = (directory, label, tuple(sorted(tf_names)) if tf_names is not None else None,
           tuple(sorted(json_names)) if json_names is not None else None)
    if key in _SCAN_CACHE:
        return _SCAN_CACHE[key]
    _SCAN_CACHE[key] = ([], [], [])  # a module cycle reads empty, never loops
    names = sorted(tf_names) if tf_names is not None else sorted(f for f in os.listdir(directory) if f.endswith(".tf"))
    jnames = sorted(json_names) if json_names is not None else sorted(
        f for f in os.listdir(directory) if f.endswith(".tfvars.json"))
    texts = {}
    for fn in names:
        try:
            with open(os.path.join(directory, fn), encoding="utf-8", errors="replace") as fh:
                texts[fn] = fh.read().replace("\r\n", "\n")
        except OSError:
            continue
    lcl = {}
    for fn in sorted(texts):
        t = texts[fn]
        for it in opal_naming._tf_items(t, 0, len(t)):
            if it[0] == "block" and it[1] == "locals" and not it[2]:
                for a in opal_naming._tf_items(t, it[4], it[5]):
                    if a[0] == "attr":
                        lcl.setdefault(a[1], (a[3], label + "/" + fn, opal_naming._line_of(t, a[2])))
    ctx = _Ctx(lcl, _dir_vars(directory, jnames, label))
    attr_map = opal_naming._census_tf_attr()
    literal, resolved, uncounted = [], [], []
    for fn in sorted(texts):
        t = texts[fn]
        rel = label + "/" + fn
        names_, _exprs = opal_naming.census_tf_names(rel, t)
        literal += [{"plane": "repo", "type": a, "current": b, "where": c} for a, b, c in names_]
        for it in opal_naming._tf_items(t, 0, len(t)):
            if it[0] != "block":
                continue
            where = "%s:%d" % (rel, opal_naming._line_of(t, it[3]))
            if it[1] == "module" and len(it[2]) == 1:
                src = [a for a in opal_naming._tf_items(t, it[4], it[5]) if a[0] == "attr" and a[1] == "source"]
                raw = src[0][3] if src else ""
                if _module_unstated(directory, opal_naming._tf_literal(raw)):
                    uncounted.append({"type": "module", "attribute": "source", "expression": _flat(raw),
                                      "reason": "module", "where": where})
                continue
            if it[1] != "resource" or len(it[2]) != 2 or it[2][0] not in attr_map:
                continue
            typ, attr = attr_map[it[2][0]]
            attrs = {a[1]: a for a in opal_naming._tf_items(t, it[4], it[5]) if a[0] == "attr"}
            raw = None
            if attr == "tags.Name":
                tags = attrs.get("tags")
                m = _TAG_NAME_RE.search(tags[3]) if tags else None
                raw = m.group(1).strip() if m else None
            elif attr in attrs:
                raw = attrs[attr][3]
            if raw is None:
                continue
            if opal_naming._tf_literal(raw) is not None:
                continue  # one literal: the census counts it (an empty literal names nothing)
            got, bad = [], None
            try:
                binds = [None]
                if "each." in raw:
                    fe = attrs.get("for_each")
                    if fe is None:
                        raise _Unres("json")
                    binds = _bindings(fe[3], ctx)
                for b in binds:
                    ctx.each = b
                    val, src = _eval(raw, ctx)
                    if not val:
                        raise _Unres("interpolation")
                    w = "%s:%d" % src if src is not None else where
                    if (typ, val, w) not in got:
                        got.append((typ, val, w))
            except _Unres as exc:
                bad = exc.reason
            finally:
                ctx.each = None
            if bad is not None:
                uncounted.append({"type": typ, "attribute": attr, "expression": _flat(raw), "reason": bad,
                                  "where": where})
            else:
                resolved += [{"plane": "repo", "type": a, "current": b, "where": c} for a, b, c in got]
    _SCAN_CACHE[key] = (literal, resolved, uncounted)
    return _SCAN_CACHE[key]


def _module_unstated(directory, source):
    """True when the module a call names builds names the call's folder cannot read: its source is not a local folder, the
    folder is unreadable, or its own scan has an uncounted name."""
    if not source or not source.startswith(("./", "../")):
        return True
    target = os.path.normpath(os.path.join(directory, source))
    if not os.path.isdir(target):
        return True
    try:
        rel = os.path.relpath(target, REPO).replace("\\", "/")
    except ValueError:  # another drive
        rel = ".."
    if rel.startswith(".."):
        rel = os.path.basename(target)
    return bool(scan_dir(target, rel)[2])


def root_extra(root):
    """(resolved, uncounted) for a Terraform root: scan_dir over every folder that holds the root's tracked .tf files, in
    file order. Reads the folders on disk; a root with no tracked .tf file reads ([], [])."""
    r = str(root).replace("\\", "/").strip().rstrip("/")
    by_dir = {}
    for f in _tf_files():
        if _under(f, r):
            d, fn = f.rsplit("/", 1)
            by_dir.setdefault(d, []).append(fn)
    jfiles = {}
    for f in _files():
        if f.endswith(".tfvars.json") and _under(f, r):
            d, fn = f.rsplit("/", 1)
            jfiles.setdefault(d, []).append(fn)
    resolved, uncounted = [], []
    for d in sorted(by_dir):
        _lit, res, unc = scan_dir(os.path.join(REPO, *d.split("/")), d, by_dir[d], jfiles.get(d, []))
        resolved += res
        uncounted += unc
    return resolved, uncounted


def root_names(root, map_path=None):
    """(items, uncounted, stats): root_items() plus the names the root's own files resolve to a literal (BF-v-4), and the
    names it builds that they do not resolve. A root whose items and uncounted are both empty has nothing to name."""
    items, stats = root_items(root, map_path)
    resolved, uncounted = root_extra(root)
    return list(items) + resolved, uncounted, stats


def uncounted_line(u):
    """The one printed line of an uncounted name."""
    return _safe("UNCOUNTED %s %s = %s -- %s  [%s]" % (u["type"], u["attribute"], u["expression"], u["reason"], u["where"]))


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


# The closed list of reasons a name is assigned to no root; each is one branch of the code above (BF-r-3).
REASONS = ("map-lists-uncontested-folder", "contested-unlisted", "beside-tied-folder", "lambda-folder-no-root-claim",
           "terraform-folder-under-no-root", "infra-aws-non-lambda", "script-folder-outside-infra-aws")


def _reason(f, mdirs, ties, contested, smap):
    """(reason, evidence) for an item whose file is f and that no root owns."""
    d = f.rsplit("/", 1)[0]
    listed, ldir = _listed_root(f, mdirs)
    if listed and ldir not in contested:
        return ("map-lists-uncontested-folder",
                "the map lists %s for %s, but no two roots claim it, so the scope reads no listing there" % (ldir, listed))
    if f.startswith(LAMBDA_ROOT):
        under_c = sorted(c for c in contested if _under(f, c))
        if under_c:
            c = max(under_c, key=len)
            return ("contested-unlisted", "%s is claimed by %d roots (%s); no map entry lists it or a folder above it"
                    % (c, len(contested[c]), ", ".join(contested[c])))
        over = sorted(set((r, t) for r in ties for t in ties[r] if _overlap(d, t)))
        if over:
            return ("beside-tied-folder", "the name sits outside the tied folder(s): %s"
                    % "; ".join("%s tied to %s" % (t, r) for r, t in over))
        rows = ["%s tf_file=%s" % (fn, row.get("tf_file") or "none") for fn, row in sorted(smap.items())
                if row.get("source_dir") and _overlap(d, str(row["source_dir"]).rstrip("/"))]
        return ("lambda-folder-no-root-claim",
                "no tie (source-map, tf-path or artifact-key) of any of the %d roots covers or sits inside %s "
                "(%d .tf files read); source map rows for it: %s"
                % (len(_roots()), d, len(_tf_files()), "; ".join(rows) if rows else "none"))
    if f.startswith(TF_ROOT):
        return ("terraform-folder-under-no-root", "%s is under %s but under none of the %d Terraform roots"
                % (d, TF_ROOT, len(_roots())))
    if f.startswith("infra/aws/"):
        return ("infra-aws-non-lambda", "%s is under infra/aws/ but not under %s or %s" % (d, TF_ROOT, LAMBDA_ROOT))
    return ("script-folder-outside-infra-aws", "%s is a script folder outside infra/aws/, under no Terraform root" % d)


def unassigned_rows(map_path=None):
    """(groups, n_items, n_assigned): one dict per folder holding unassigned names: dir, items, reason, evidence."""
    items, _ = _census()
    asg = _assignment_with(map_path)
    mdirs = _map_dirs(map_path)
    ties = _ties()
    _per, contested = _resolve()
    smap = json.loads(_read_text(SOURCE_MAP)).get("functions", {})
    groups = {}
    for it, r in zip(items, asg):
        if r is not None:
            continue
        f = _file_of(it)
        reason, ev = _reason(f, mdirs, ties, contested, smap)
        g = groups.setdefault(f.rsplit("/", 1)[0], {"dir": f.rsplit("/", 1)[0], "items": 0, "reason": reason, "evidence": ev})
        g["items"] += 1
        if g["reason"] != reason:
            g["reason"] = "MIXED"
    return [groups[k] for k in sorted(groups)], len(items), sum(1 for r in asg if r is not None)


def cmd_unassigned(map_path=None):
    groups, n_items, n_asg = unassigned_rows(map_path)
    n_un = sum(g["items"] for g in groups)
    reasoned = sum(g["items"] for g in groups if g["reason"] in REASONS)
    for g in groups:
        print(_safe("UNASSIGNED-GROUP %s items=%d reason=%s evidence=%s" % (g["dir"], g["items"], g["reason"], g["evidence"])))
    by = {}
    for g in groups:
        by[g["reason"]] = by.get(g["reason"], 0) + g["items"]
    for k in sorted(by):
        print("UNASSIGNED-REASON %s items=%d" % (k, by[k]))
    ok = (n_asg + n_un == n_items) and reasoned == n_un
    print("SCOPE-UNASSIGNED ok=%s items=%d assigned=%d unassigned=%d reasoned=%d unreasoned=%d"
          % (ok, n_items, n_asg, n_un, reasoned, n_un - reasoned))
    return 0 if ok else 1


_USAGE = "usage: opal_naming_scope.py items ROOT | table | pick | contested | unassigned   (each takes --map PATH)"


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
        if len(argv) == 2 and cmd == "unassigned":
            return cmd_unassigned(map_path)
    except (ValueError, OSError) as exc:
        print("SCOPE-%s ok=False error=%s" % (cmd.upper(), _safe(exc)))
        return 1
    print(_USAGE)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
