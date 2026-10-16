#!/usr/bin/env python3
"""opal_naming_scope -- the names the naming check reads for ONE Terraform root (LGIC_BLANKFIX BF-t-1).

`python lib/opal_naming.py census --repo` reads the whole repository. This module cuts the repository plane down to one
Terraform root: the root's own .tf names plus the names in the Lambda source folders the root deploys. The tie from a root
to a source folder is DERIVED from the repository, never typed; three kinds of evidence are read:

  source-map   infra/aws/lambda/ci/function-map/<name>.json: a function whose tf_file sits in the root and whose source_dir
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
import opal_lambda_map  # noqa: E402  -- CT-ca-1: the Lambda function map, one file per function

REPO = opal_naming.REPO
TF_ROOT = "infra/aws/terraform/"
LAMBDA_ROOT = "infra/aws/lambda/"
SOURCE_MAP = "infra/aws/lambda/ci/function-map"  # the folder: one <name>.json per function (CT-ca-1)
NOT_JUDGED = ("org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/NOT_JUDGED_R13.json")

_TF_PATH_RE = re.compile(r"(?:infra/aws/lambda/|\.\./lambda/|lambda_base_dir\}/)([A-Za-z0-9_./-]+)")
_ARTIFACT_RE = re.compile(r'artifact_key\s*=\s*"([A-Za-z0-9_.-]+)/')
_PASCAL_RE = re.compile(r"^[A-Z][a-z0-9]+(?:[A-Z][a-z0-9]*)*$")
_BLANK_RE = re.compile(r"\{([a-z_]+)\}")

_CACHE = {}


def _lambda_functions():
    """{name: entry} of the Lambda function map: one file per function under SOURCE_MAP (CT-ca-1). Raises when absent or empty."""
    return opal_lambda_map.load_all(root=REPO)


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

    smap = _lambda_functions()
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


# ---- BF-v-4 / BF-w-2: names the literal reader does not count ----------------------------------------------------
# census_repo() reads a name only when the name attribute of a graded resource is ONE string literal. A name built in a
# `locals` block, from a `var.`, through a module call, from a generated .json or from another resource is counted by
# nothing, so a root that builds its names that way read names=0. scan_dir() reads one folder of .tf files with a small
# HCL expression reader (strings and templates, references, objects, lists, conditionals, for expressions and the
# functions listed in _FUNCS) and puts every such name in one of two places:
#   COUNTED    the repository decides the value: a literal local or a chain of locals; a `var.` with a default, a value in
#              the folder's own *.tfvars / *.tfvars.json, or the argument a module call passes; a module call to a folder of
#              this repository (its source path followed, once per for_each / count key); a reference to another resource
#              of the folder whose name or other argument resolves (aws_s3_bucket.x.id is that bucket's name).
#   UNCOUNTED  the repository does not decide it. The reason is one of the closed set below, never a bare kind.
#
# The closed set of reasons an UNCOUNTED line carries (UNCOUNTED_REASONS; one line each):
#   apply-time       the value exists only after apply: an attribute AWS or the provider computes (an arn, an id that is not
#                    the name), a data source, or a resource argument that is not written in the repository
#   var-unset        a variable of this root with no default and no value in the root's own *.tfvars / *.tfvars.json: it is
#                    supplied outside the repository (-var, environment, the CI that applies the root)
#   module-input     a variable of a reusable module folder (under a modules/ directory) read by itself: each call site
#                    supplies it, and the call sites resolve it in the root that calls the module
#   external-module  a module whose source is not a folder of this repository (registry, git, a missing path)
#   open-key-domain  a count / for_each key with no literal domain: each.* or count.index where the repository spells no
#                    collection to run over
#   unevaluated      an expression form this reader does not evaluate (a function outside _FUNCS, a splat, a heredoc, a
#                    directive, a reference cycle): the repository may decide it, this reader does not

UNCOUNTED_REASONS = ("apply-time", "var-unset", "module-input", "external-module", "open-key-domain", "unevaluated")
REASON_WHY = {
    "apply-time": "the value exists only after apply: a provider-computed attribute, a data source, an argument not written here",
    "var-unset": "a variable of this root with no default and no value in its own tfvars: supplied outside the repository",
    "module-input": "an input of a reusable module read by itself: each call site supplies it and is resolved in the calling root",
    "external-module": "a module whose source is not a folder of this repository",
    "open-key-domain": "each.* or count.index where the repository spells no collection to run over",
    "unevaluated": "an expression form this reader does not evaluate (function outside _FUNCS, splat, heredoc, directive, cycle)",
}
_ID_IS_NAME = ("S3_BUCKET", "IAM_ROLE", "LAMBDA", "EVENT_RULE", "LOG_GROUP", "DYNAMODB_TABLE", "INSTANCE_PROFILE")
_MODULE_META = ("source", "for_each", "count", "depends_on", "providers", "version")
_MAX_DEPTH = 40
_NAME_TAG_RE = re.compile(r'(?:^|[{,\s])"?Name"?\s*=\s*("(?:[^"\\\n]|\\.)*")')


class Unk(object):
    """A value the folder's own files do not decide; .reason is one of UNCOUNTED_REASONS."""

    def __init__(self, reason):
        self.reason = reason


class _Bad(Exception):
    """Syntax this reader does not evaluate."""


class _S(str):
    """A string with the (path, line) pairs that spell it: where the literal it came from sits."""
    srcs = frozenset()


def _s(text, srcs=()):
    o = _S(text)
    o.srcs = frozenset(srcs)
    return o


def _srcs_of(v, depth=0):
    if isinstance(v, _S):
        return v.srcs
    if depth < 3 and isinstance(v, (list, tuple)):
        out = set()
        for x in v:
            out |= _srcs_of(x, depth + 1)
        return out
    return frozenset()


def _flat(raw):
    return " ".join(str(raw).split())


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


# ---- the lexer and the parser -----------------------------------------------------------------------------------

_ID_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_-]*")
_NUM_RE = re.compile(r"[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?")
_OPS2 = ("==", "!=", "<=", ">=", "&&", "||", "=>")
_ESC = {"n": "\n", "t": "\t", '"': '"', "\\": "\\", "r": "\r"}


def _close_brace(raw, i):
    """The index of the } that closes the { at raw[i], skipping strings."""
    depth, n = 0, len(raw)
    while i < n:
        c = raw[i]
        if c == '"':
            i = _lex_string(raw, i)[1]
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return i
        i += 1
    raise _Bad("unclosed brace")


def _lex_string(raw, i):
    """(parts, index after the closing quote) of the string that opens at raw[i]: parts are ("s", text) and
    ("e", start, end) for a ${ } expression."""
    j, n, buf, parts = i + 1, len(raw), [], []
    while j < n:
        c = raw[j]
        if c == "\\":
            nxt = raw[j + 1:j + 2]
            buf.append(_ESC.get(nxt, "\\" + nxt))
            j += 2
            continue
        if c == '"':
            if buf:
                parts.append(("s", "".join(buf)))
            return parts, j + 1
        if raw.startswith("$${", j):
            buf.append("${")
            j += 3
            continue
        if raw.startswith("%%{", j):
            buf.append("%{")
            j += 3
            continue
        if raw.startswith("${", j):
            e = _close_brace(raw, j + 1)
            if buf:
                parts.append(("s", "".join(buf)))
                buf = []
            parts.append(("e", j + 2, e))
            j = e + 1
            continue
        if raw.startswith("%{", j):
            raise _Bad("directive")
        buf.append(c)
        j += 1
    raise _Bad("unterminated string")


def _lex(raw):
    toks, i, n = [], 0, len(raw)
    while i < n:
        c = raw[i]
        if c in " \t\r\n":
            i += 1
            continue
        if c == "#" or raw.startswith("//", i):
            j = raw.find("\n", i)
            i = n if j < 0 else j + 1
            continue
        if raw.startswith("/*", i):
            j = raw.find("*/", i + 2)
            i = n if j < 0 else j + 2
            continue
        if c == '"':
            parts, j = _lex_string(raw, i)
            toks.append(("str", parts, i))
            i = j
            continue
        if raw.startswith("<<", i):
            raise _Bad("heredoc")
        if c.isdigit():
            m = _NUM_RE.match(raw, i)
            txt = m.group(0)
            toks.append(("num", float(txt) if ("." in txt or "e" in txt or "E" in txt) else int(txt), i))
            i = m.end()
            continue
        m = _ID_RE.match(raw, i)
        if m:
            toks.append(("id", m.group(0), i))
            i = m.end()
            continue
        if raw.startswith("...", i):
            toks.append(("op", "...", i))
            i += 3
            continue
        if raw[i:i + 2] in _OPS2:
            toks.append(("op", raw[i:i + 2], i))
            i += 2
            continue
        if c in "+-*/%<>!?:.,()[]{}=":
            toks.append(("op", c, i))
            i += 1
            continue
        raise _Bad("character %r" % c)
    return toks


class _Parser(object):
    """Recursive descent over the tokens of one expression text. `path` and `base` give every string literal the
    (path, line) that spells it."""

    def __init__(self, text, path, base):
        self.text, self.path, self.base = text, path, base
        self.toks = _lex(text)
        self.i = 0

    def line(self, pos):
        return self.base + self.text.count("\n", 0, pos)

    def peek(self, k=0):
        j = self.i + k
        return self.toks[j] if j < len(self.toks) else ("eof", None, len(self.text))

    def take(self):
        t = self.peek()
        self.i += 1
        return t

    def is_op(self, v, k=0):
        t = self.peek(k)
        return t[0] == "op" and t[1] == v

    def is_id(self, v, k=0):
        t = self.peek(k)
        return t[0] == "id" and t[1] == v

    def expect(self, v):
        t = self.take()
        if t[0] != "op" or t[1] != v:
            raise _Bad("expected %s" % v)

    def parse_all(self):
        n = self.expr()
        if self.peek()[0] != "eof":
            raise _Bad("trailing tokens")
        return n

    def expr(self):
        c = self.binary(0)
        if self.is_op("?"):
            self.take()
            a = self.expr()
            self.expect(":")
            b = self.expr()
            return ("cond", c, a, b)
        return c

    _LEVELS = (("||",), ("&&",), ("==", "!="), ("<", ">", "<=", ">="), ("+", "-"), ("*", "/", "%"))

    def binary(self, lvl):
        if lvl >= len(self._LEVELS):
            return self.unary()
        left = self.binary(lvl + 1)
        while self.peek()[0] == "op" and self.peek()[1] in self._LEVELS[lvl]:
            op = self.take()[1]
            left = ("bin", op, left, self.binary(lvl + 1))
        return left

    def unary(self):
        if self.is_op("!") or self.is_op("-"):
            op = self.take()[1]
            return ("un", op, self.unary())
        return self.postfix(self.primary())

    def postfix(self, node):
        while True:
            if self.is_op("."):
                nxt = self.peek(1)
                if nxt[0] == "id":
                    self.take()
                    node = ("attr", node, self.take()[1])
                elif nxt[0] == "num" and isinstance(nxt[1], int):
                    self.take()
                    node = ("idx", node, ("lit", self.take()[1]))
                else:
                    raise _Bad("splat")
            elif self.is_op("["):
                if self.is_op("*", 1):
                    raise _Bad("splat")
                self.take()
                k = self.expr()
                self.expect("]")
                node = ("idx", node, k)
            else:
                return node

    def primary(self):
        t = self.take()
        kind, val, pos = t
        if kind == "num":
            return ("lit", val)
        if kind == "str":
            return self.template(val, pos)
        if kind == "id":
            if val == "true":
                return ("lit", True)
            if val == "false":
                return ("lit", False)
            if val == "null":
                return ("lit", None)
            if self.is_op("("):
                self.take()
                args = []
                while not self.is_op(")"):
                    args.append(self.expr())
                    if self.is_op("..."):
                        raise _Bad("expansion")
                    if self.is_op(","):
                        self.take()
                    elif not self.is_op(")"):
                        raise _Bad("call arguments")
                self.take()
                return ("call", val, args)
            return ("id", val)
        if kind == "op" and val == "(":
            n = self.expr()
            self.expect(")")
            return n
        if kind == "op" and val == "[":
            if self.is_id("for"):
                return self.for_expr("]")
            items = []
            while not self.is_op("]"):
                items.append(self.expr())
                if self.is_op(","):
                    self.take()
            self.take()
            return ("tuple", items)
        if kind == "op" and val == "{":
            if self.is_id("for"):
                return self.for_expr("}")
            ents = []
            while not self.is_op("}"):
                ents.append(self.entry())
                if self.is_op(","):
                    self.take()
            self.take()
            return ("obj", ents)
        raise _Bad("unexpected %s" % (val,))

    def entry(self):
        t = self.peek()
        if t[0] == "id" and (self.is_op("=", 1) or self.is_op(":", 1)):
            self.take()
            key = ("lit", _s(t[1], [(self.path, self.line(t[2]))]))
        else:
            key = self.expr()
        if not (self.is_op("=") or self.is_op(":")):
            raise _Bad("object entry")
        self.take()
        return (key, self.expr())

    def for_expr(self, close):
        self.take()  # for
        a = self.take()
        if a[0] != "id":
            raise _Bad("for variable")
        kvar, vvar = None, a[1]
        if self.is_op(","):
            self.take()
            b = self.take()
            if b[0] != "id":
                raise _Bad("for variable")
            kvar, vvar = a[1], b[1]
        if not self.is_id("in"):
            raise _Bad("for in")
        self.take()
        coll = self.expr()
        self.expect(":")
        k = self.expr()
        v = None
        if close == "}":
            self.expect("=>")
            v = self.expr()
            if self.is_op("..."):
                raise _Bad("grouping")
        cond = None
        if self.is_id("if"):
            self.take()
            cond = self.expr()
        self.expect(close)
        return ("for", close, kvar, vvar, coll, k, v, cond)

    def template(self, parts, pos):
        out = []
        for p in parts:
            if p[0] == "s":
                out.append(("s", p[1]))
            else:
                sub = self.text[p[1]:p[2]]
                out.append(("e", _Parser(sub, self.path, self.line(p[1])).parse_all()))
        line = self.line(pos)
        if all(p[0] == "s" for p in out):
            return ("lit", _s("".join(p[1] for p in out), [(self.path, line)]))
        if len(out) == 1:
            return out[0][1]
        return ("tpl", out, (self.path, line))


_PARSE_CACHE = {}


def _parse(raw, path, line):
    key = (path, line, raw)
    if key not in _PARSE_CACHE:
        try:
            _PARSE_CACHE[key] = _Parser(raw, path, line).parse_all()
        except (_Bad, IndexError):
            _PARSE_CACHE[key] = None
    return _PARSE_CACHE[key]


# ---- the evaluator ----------------------------------------------------------------------------------------------

class _Env(object):
    def __init__(self, scope, each=None, count=None, loop=None, depth=0):
        self.scope, self.each, self.count, self.loop, self.depth = scope, each, count, loop or {}, depth

    def sub(self, **kw):
        e = _Env(self.scope, self.each, self.count, dict(self.loop), self.depth + 1)
        for k, v in kw.items():
            setattr(e, k, v)
        return e


class _Thunk(object):
    """An expression read lazily, once, in the scope and the for_each / count binding it was written in."""

    def __init__(self, raw, path, line, env):
        self.raw, self.path, self.line, self.env = raw, path, line, env
        self.done, self.val = False, None

    def get(self):
        if not self.done:
            self.val = Unk("unevaluated")  # a cycle reads unevaluated
            self.val = _run(self.raw, self.path, self.line, self.env)
            self.done = True
        return self.val


def _run(raw, path, line, env):
    node = _parse(raw, path, line)
    if node is None or env.depth > _MAX_DEPTH:
        return Unk("unevaluated")
    try:
        return _ev(node, env)
    except (TypeError, ValueError, KeyError, IndexError, AttributeError, ZeroDivisionError, RecursionError, OverflowError):
        return Unk("unevaluated")


def _first_unk(*vals):
    for v in vals:
        if isinstance(v, Unk):
            return v
    return None


def _text_of(v):
    if isinstance(v, str):
        return v
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, int):
        return str(v)
    if isinstance(v, float):
        return str(int(v)) if v == int(v) else repr(v)
    return None


def _ev(node, env):
    k = node[0]
    if k == "lit":
        return node[1]
    if k == "tpl":
        out = []
        for p in node[1]:
            if p[0] == "s":
                out.append(p[1])
                continue
            v = _ev(p[1], env)
            if isinstance(v, Unk):
                return v
            t = _text_of(v)
            if t is None:
                return Unk("unevaluated")
            out.append(t)
        return _s("".join(out), [node[2]])  # a template is spelled where it is written
    if k == "id":
        return _root(node[1], env)
    if k == "attr":
        return _member(_ev(node[1], env), node[2], env)
    if k == "idx":
        return _index(_ev(node[1], env), _ev(node[2], env), env)
    if k == "tuple":
        return [_ev(x, env) for x in node[1]]
    if k == "obj":
        d = {}
        for kn, vn in node[1]:
            key = _ev(kn, env)
            if isinstance(key, Unk):
                return key
            t = _text_of(key)
            if t is None:
                return Unk("unevaluated")
            d[key if isinstance(key, _S) else t] = _ev(vn, env)
        return d
    if k == "un":
        v = _ev(node[2], env)
        if isinstance(v, Unk):
            return v
        if node[1] == "!":
            return (not v) if isinstance(v, bool) else Unk("unevaluated")
        return -v
    if k == "cond":
        c = _ev(node[1], env)
        if isinstance(c, Unk):
            return c
        if not isinstance(c, bool):
            return Unk("unevaluated")
        return _ev(node[2] if c else node[3], env)
    if k == "bin":
        return _binary(node, env)
    if k == "call":
        return _call(node[1], node[2], env)
    if k == "for":
        return _for(node, env)
    raise _Bad(k)


def _binary(node, env):
    op = node[1]
    a = _ev(node[2], env)
    if op == "&&" and a is False:
        return False
    if op == "||" and a is True:
        return True
    b = _ev(node[3], env)
    u = _first_unk(a, b)
    if u is not None:
        return u
    if op == "==":
        return a == b
    if op == "!=":
        return a != b
    if op == "&&":
        return bool(a and b)
    if op == "||":
        return bool(a or b)
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        return a / b
    if op == "%":
        return a % b
    if op == "<":
        return a < b
    if op == ">":
        return a > b
    if op == "<=":
        return a <= b
    return a >= b


def _items_of(coll):
    """[(key, value)] a for expression or a for_each runs over; None when it is not a collection."""
    if isinstance(coll, dict):
        return list(coll.items())
    if isinstance(coll, (list, tuple)):
        return [(i, v) for i, v in enumerate(coll)]
    return None


def _for(node, env):
    _k, close, kvar, vvar, collnode, kexpr, vexpr, cond = node
    coll = _ev(collnode, env)
    if isinstance(coll, Unk):
        return coll
    items = _items_of(coll)
    if items is None:
        return Unk("unevaluated")
    out_l, out_d = [], {}
    for key, val in items:
        loop = dict(env.loop)
        loop[vvar] = val
        if kvar is not None:
            loop[kvar] = key
        e = env.sub(loop=loop)
        if cond is not None:
            c = _ev(cond, e)
            if isinstance(c, Unk):
                return c
            if not c:
                continue
        if close == "]":
            out_l.append(_ev(kexpr, e))
        else:
            kk = _ev(kexpr, e)
            if isinstance(kk, Unk):
                return kk
            out_d[kk if isinstance(kk, _S) else _text_of(kk)] = _ev(vexpr, e)
    return out_l if close == "]" else out_d


# ---- references: locals, variables, modules, resources ----------------------------------------------------------

class _Ns(object):
    def __init__(self, scope, kind):
        self.scope, self.kind = scope, kind


class _ResType(object):
    def __init__(self, scope, rtype):
        self.scope, self.rtype = scope, rtype


class _ResRef(object):
    def __init__(self, scope, res):
        self.scope, self.res = scope, res


class _ResInst(object):
    def __init__(self, scope, res, binding):
        self.scope, self.res, self.binding = scope, res, binding

    def member(self, attr):
        sc, res = self.scope, self.res
        kind, bk, bv = self.binding
        guard = (id(res), attr, _text_of(bk))
        if guard in sc.busy:
            return Unk("unevaluated")
        sc.busy.add(guard)
        try:
            env = _Env(sc, each=({"key": bk, "value": bv} if kind == "for_each" else None),
                       count=(bk if kind == "count" else None))
            row = res["attrs"].get(attr)
            if row is not None:
                return _run(row[0], res["path"], row[1], env)
            am = sc.attr_map.get(res["type"])
            if attr == "id" and am is not None and am[0] in _ID_IS_NAME and am[1] in res["attrs"]:
                r2 = res["attrs"][am[1]]
                return _run(r2[0], res["path"], r2[1], env)
            return Unk("apply-time")
        finally:
            sc.busy.discard(guard)


class _ModRef(object):
    def __init__(self, scope, call):
        self.scope, self.call = scope, call


class _ModInst(object):
    def __init__(self, scope):
        self.scope = scope

    def output(self, name):
        return self.scope.output(name)


def _root(name, env):
    if name in env.loop:
        return env.loop[name]
    sc = env.scope
    if name in ("local", "var", "module"):
        return _Ns(sc, name)
    if name == "each":
        return env.each if env.each is not None else Unk("open-key-domain")
    if name == "count":
        return {"index": env.count} if env.count is not None else Unk("open-key-domain")
    if name == "data":
        return Unk("apply-time")
    if name == "path":
        return {"module": sc.f.directory, "root": sc.root_dir, "cwd": sc.root_dir}
    if name in sc.f.res_types:
        return _ResType(sc, name)
    return Unk("unevaluated")


def _member(base, key, env):
    if isinstance(base, Unk):
        return base
    if isinstance(base, dict):
        return base[key] if key in base else Unk("unevaluated")
    if isinstance(base, _Ns):
        if base.kind == "local":
            return base.scope.local(key)
        if base.kind == "var":
            return base.scope.var(key)
        call = base.scope.f.modules.get(key)
        return _ModRef(base.scope, base.scope.module_call(key)) if call is not None else Unk("unevaluated")
    if isinstance(base, _ResType):
        res = base.scope.f.res_by_addr.get((base.rtype, key))
        return _ResRef(base.scope, res) if res is not None else Unk("unevaluated")
    if isinstance(base, _ResRef):
        if base.res["bind"] is not None:
            return Unk("unevaluated")
        return _ResInst(base.scope, base.res, (None, None, None)).member(key)
    if isinstance(base, _ResInst):
        return base.member(key)
    if isinstance(base, _ModRef):
        if base.call.kind is not None:
            return Unk("unevaluated")
        inst = base.call.instance(None)
        return inst.output(key) if isinstance(inst, _ModInst) else inst
    if isinstance(base, _ModInst):
        return base.output(key)
    return Unk("unevaluated")


def _index(base, key, env):
    if isinstance(base, Unk):
        return base
    if isinstance(key, Unk):
        return key
    if isinstance(base, dict):
        t = _text_of(key)
        return base[t] if t in base else Unk("unevaluated")
    if isinstance(base, (list, tuple)):
        i = int(key)
        return base[i] if 0 <= i < len(base) else Unk("unevaluated")
    if isinstance(base, _ResRef):
        b = base.scope.bindings(base.res)
        if isinstance(b, Unk):
            return b
        kind, pairs = b
        t = _text_of(key)
        for bk, bv in pairs:
            if _text_of(bk) == t:
                return _ResInst(base.scope, base.res, (kind, bk, bv))
        return Unk("unevaluated")
    if isinstance(base, _ModRef):
        inst = base.call.instance(key)
        return inst
    return _member(base, _text_of(key), env)


# ---- functions --------------------------------------------------------------------------------------------------

_FMT_RE = re.compile(r"%(%|[-+ 0#]*[0-9]*(?:\.[0-9]+)?[sdvfxXq])")


def _f_format(a):
    fmt, args, pos = a[0], a[1:], [0]
    srcs = set(_srcs_of(list(a)))

    def rep(m):
        spec = m.group(1)
        if spec == "%":
            return "%"
        arg = args[pos[0]]
        pos[0] += 1
        verb = spec[-1]
        if verb in "sv":
            if _text_of(arg) is None:
                raise ValueError("format argument")
            return ("%" + spec[:-1] + "s") % _text_of(arg)
        if verb == "q":
            return '"%s"' % _text_of(arg)
        if verb in "dxX":
            return ("%" + spec) % int(arg)
        return ("%" + spec) % float(arg)
    return _s(_FMT_RE.sub(rep, fmt), srcs)


def _f_merge(a):
    out = {}
    for d in a:
        if d is None:
            continue
        if not isinstance(d, dict):
            return Unk("unevaluated")
        out.update(d)
    return out


def _f_one(a):
    x = a[0]
    if not isinstance(x, (list, tuple)):
        return Unk("unevaluated")
    if len(x) == 0:
        return None
    return x[0] if len(x) == 1 else Unk("unevaluated")


def _f_toset(a):
    seen, out = set(), []
    for x in a[0]:
        t = _text_of(x)
        if t not in seen:
            seen.add(t)
            out.append(x)
    return sorted(out, key=lambda x: str(_text_of(x)))


def _f_lookup(a):
    m, k = a[0], a[1]
    if isinstance(m, dict):
        t = _text_of(k)
        if t in m:
            return m[t]
    return a[2] if len(a) > 2 else Unk("unevaluated")


def _f_coalesce(a):
    for x in a:
        if x is not None and x != "":
            return x
    return Unk("unevaluated")


def _f_element(a):
    return a[0][int(a[1]) % len(a[0])]


def _f_flatten(a):
    out = []
    for x in a[0]:
        if isinstance(x, (list, tuple)):
            out += _f_flatten([x])
        else:
            out.append(x)
    return out


def _f_join(a):
    parts = [_text_of(x) for x in a[1]]
    if None in parts:
        return Unk("unevaluated")
    return _s(a[0].join(parts), _srcs_of(a[1]) | _srcs_of([a[0]]))


def _f_file(a):
    path = os.path.normpath(str(a[0]))
    if os.path.getsize(path) > 8000000:
        return Unk("unevaluated")
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            return fh.read().replace(chr(13) + chr(10), chr(10))
    except OSError:
        return Unk("unevaluated")


def _f_jsondecode(a):
    try:
        return json.loads(a[0])
    except ValueError:
        return Unk("unevaluated")


def _f_str(fn):
    return lambda a: _s(fn(str(a[0]), *a[1:]), _srcs_of([a[0]]))


_FUNCS = {
    "format": _f_format,
    "file": _f_file,
    "jsondecode": _f_jsondecode,
    "lower": _f_str(lambda s: s.lower()),
    "upper": _f_str(lambda s: s.upper()),
    "replace": _f_str(lambda s, x, y: s.replace(str(x), str(y))),
    "trimprefix": _f_str(lambda s, p: s[len(p):] if s.startswith(p) else s),
    "trimsuffix": _f_str(lambda s, p: s[:-len(p)] if p and s.endswith(p) else s),
    "trimspace": _f_str(lambda s: s.strip()),
    "basename": lambda a: _s(os.path.basename(str(a[0]).replace(chr(92), "/").rstrip("/")), _srcs_of([a[0]])),
    "abspath": lambda a: os.path.abspath(str(a[0])),
    "startswith": lambda a: str(a[0]).startswith(str(a[1])),
    "endswith": lambda a: str(a[0]).endswith(str(a[1])),
    "tostring": lambda a: a[0] if isinstance(a[0], str) else _s(_text_of(a[0])),
    "join": _f_join,
    "split": lambda a: [_s(x, _srcs_of([a[1]])) for x in a[1].split(a[0])],
    "concat": lambda a: [x for lst in a for x in lst],
    "merge": _f_merge,
    "keys": lambda a: sorted(a[0].keys(), key=str),
    "values": lambda a: [a[0][k] for k in sorted(a[0].keys(), key=str)],
    "one": _f_one,
    "toset": _f_toset,
    "tolist": lambda a: list(a[0]),
    "tomap": lambda a: dict(a[0]),
    "tonumber": lambda a: a[0] if isinstance(a[0], (int, float)) else float(a[0]),
    "lookup": _f_lookup,
    "contains": lambda a: _text_of(a[1]) in [_text_of(x) for x in a[0]],
    "coalesce": _f_coalesce,
    "length": lambda a: len(a[0]),
    "flatten": _f_flatten,
    "distinct": _f_toset,
    "sort": lambda a: sorted(a[0], key=str),
    "compact": lambda a: [x for x in a[0] if x not in (None, "")],
    "element": _f_element,
    "zipmap": lambda a: dict(zip([_text_of(k) for k in a[0]], a[1])),
    "setunion": lambda a: _f_toset([[x for lst in a for x in lst]]),
}


def _call(name, argnodes, env):
    if name == "try":
        last = Unk("unevaluated")
        for n in argnodes:
            try:
                v = _ev(n, env)
            except (TypeError, ValueError, KeyError, IndexError, AttributeError, ZeroDivisionError):
                continue
            if not isinstance(v, Unk):
                return v
            last = v
        return last
    fn = _FUNCS.get(name)
    if fn is None:
        return Unk("unevaluated")
    args = [_ev(n, env) for n in argnodes]
    u = _first_unk(*args)
    if u is not None:
        return u
    return fn(args)


# ---- one folder of .tf files, and the scopes that read it -------------------------------------------------------

class _Folder(object):
    """The static read of one folder: its locals, variables, outputs, resources and module calls."""

    def __init__(self, directory, label, tf_names=None, json_names=None):
        self.directory, self.label = directory, label
        names = sorted(tf_names) if tf_names is not None else sorted(f for f in os.listdir(directory) if f.endswith(".tf"))
        self.json_names = sorted(json_names) if json_names is not None else sorted(
            f for f in os.listdir(directory) if f.endswith(".tfvars.json") or f.endswith(".tfvars"))
        self.texts = {}
        for fn in names:
            try:
                with open(os.path.join(directory, fn), encoding="utf-8", errors="replace") as fh:
                    self.texts[fn] = fh.read().replace("\r\n", "\n")
            except OSError:
                continue
        self.locals, self.variables, self.outputs, self.resources, self.modules = {}, {}, {}, [], {}
        self.res_types, self.res_by_addr = set(), {}
        for fn in sorted(self.texts):
            t, path = self.texts[fn], label + "/" + fn
            for it in opal_naming._tf_items(t, 0, len(t)):
                if it[0] != "block":
                    continue
                kind, labels, line = it[1], it[2], opal_naming._line_of(t, it[3])
                inner = opal_naming._tf_items(t, it[4], it[5])
                attrs = dict((a[1], (a[3], opal_naming._line_of(t, a[2]))) for a in inner if a[0] == "attr")
                if kind == "locals" and not labels:
                    for a in inner:
                        if a[0] == "attr":
                            self.locals.setdefault(a[1], (a[3], path, opal_naming._line_of(t, a[2])))
                elif kind == "variable" and len(labels) == 1:
                    d = attrs.get("default")
                    self.variables[labels[0]] = (d[0], path, d[1]) if d else None
                elif kind == "output" and len(labels) == 1 and "value" in attrs:
                    self.outputs[labels[0]] = (attrs["value"][0], path, attrs["value"][1])
                elif kind == "resource" and len(labels) == 2:
                    res = {"type": labels[0], "name": labels[1], "attrs": attrs, "path": path, "line": line, "file": fn,
                           "bind": "for_each" if "for_each" in attrs else ("count" if "count" in attrs else None)}
                    self.resources.append(res)
                    self.res_types.add(labels[0])
                    self.res_by_addr.setdefault((labels[0], labels[1]), res)
                elif kind == "module" and len(labels) == 1:
                    self.modules[labels[0]] = {"attrs": attrs, "path": path, "line": line, "file": fn}
        self.tfvars = {}
        for fn in self.json_names:
            if fn.endswith(".tfvars.json"):
                self._json_vars(fn)
            elif fn.endswith(".tfvars"):
                self._hcl_vars(fn)

    def _json_vars(self, fn):
        try:
            with open(os.path.join(self.directory, fn), encoding="utf-8", errors="replace") as fh:
                text = fh.read().replace("\r\n", "\n")
            doc = json.loads(text)
        except (OSError, ValueError):
            return
        path = self.label + "/" + fn

        def conv(v, keypath):
            src = [(path, _json_line(text, keypath))]
            if isinstance(v, str):
                return _s(v, src)
            if isinstance(v, dict):
                return dict((_s(k, [(path, _json_line(text, keypath + [k]))]), conv(x, keypath + [k])) for k, x in v.items())
            if isinstance(v, list):
                return [conv(x, keypath) for x in v]
            return v
        if isinstance(doc, dict):
            for k, v in doc.items():
                self.tfvars[k] = conv(v, [k])

    def _hcl_vars(self, fn):
        try:
            with open(os.path.join(self.directory, fn), encoding="utf-8", errors="replace") as fh:
                t = fh.read().replace("\r\n", "\n")
        except OSError:
            return
        path = self.label + "/" + fn
        empty = _Scope(self)
        for a in opal_naming._tf_items(t, 0, len(t)):
            if a[0] == "attr":
                self.tfvars[a[1]] = _run(a[3], path, opal_naming._line_of(t, a[2]), _Env(empty))


class _ModCall(object):
    """One module call of a scope: its folder, its meta-arguments and the instances it makes."""

    def __init__(self, scope, name):
        self.scope, self.name = scope, name
        self.block = scope.f.modules[name]
        self.kind = "for_each" if "for_each" in self.block["attrs"] else ("count" if "count" in self.block["attrs"] else None)
        self.folder, self.reason = None, None
        src = self.block["attrs"].get("source")
        lit = opal_naming._tf_literal(src[0]) if src else None
        if not lit or not lit.startswith(("./", "../")):
            self.reason = "external-module"
        else:
            target = os.path.normpath(os.path.join(scope.f.directory, lit))
            if scope.depth >= 6:
                self.reason = "unevaluated"
            elif not os.path.isdir(target):
                self.reason = "external-module"
            else:
                self.folder = _folder_of(target)
        self._inst = {}

    def pairs(self):
        """[(kind, key, value)] one per instance, or an Unk."""
        a = self.block["attrs"]
        env = _Env(self.scope)
        return self.scope.bindings({"attrs": a, "path": self.block["path"], "bind": self.kind}, env)

    def instance(self, key):
        if self.folder is None:
            return Unk(self.reason)
        if self.kind is None:
            b = (None, None, None)
        else:
            pairs = self.pairs()
            if isinstance(pairs, Unk):
                return pairs
            t = _text_of(key)
            b = None
            for bk, bv in pairs[1]:
                if _text_of(bk) == t:
                    b = (pairs[0], bk, bv)
            if b is None:
                return Unk("unevaluated")
        return self.make(b)

    def make(self, b):
        ck = (b[0], _text_of(b[1]))
        if ck not in self._inst:
            kind, bk, bv = b
            env = _Env(self.scope, each=({"key": bk, "value": bv} if kind == "for_each" else None),
                       count=(bk if kind == "count" else None))
            args = {}
            for name, row in self.block["attrs"].items():
                if name not in _MODULE_META:
                    args[name] = _Thunk(row[0], self.block["path"], row[1], env)
            sc = _Scope(self.folder, args=args, depth=self.scope.depth + 1, is_module=True, root_dir=self.scope.root_dir)
            self._inst[ck] = _ModInst(sc)
        return self._inst[ck]


class _Scope(object):
    """One reading of a folder: the root of a scan (its own tfvars) or one instance of a module (its call's arguments)."""

    def __init__(self, folder, args=None, depth=0, is_module=False, root_dir=None):
        self.f, self.depth, self.is_module = folder, depth, is_module
        self.root_dir = root_dir or folder.directory
        self.args = args if args is not None else {}
        self.reusable = "/modules/" in ("/" + folder.label + "/")
        self.memo, self.calls, self.vmemo, self.busy = {}, {}, {}, set()
        self.attr_map = opal_naming._census_tf_attr()

    def local(self, name):
        if name in self.memo:
            return self.memo[name]
        row = self.f.locals.get(name)
        if row is None:
            return Unk("unevaluated")
        self.memo[name] = Unk("unevaluated")  # a cycle reads unevaluated
        v = _run(row[0], row[1], row[2], _Env(self, depth=1))
        self.memo[name] = v
        return v

    def var(self, name):
        if name in self.vmemo:
            return self.vmemo[name]
        if name in self.args:
            v = self.args[name].get()
        elif not self.is_module and name in self.f.tfvars:
            v = self.f.tfvars[name]
        elif self.f.variables.get(name) is not None:
            row = self.f.variables[name]
            v = _run(row[0], row[1], row[2], _Env(self, depth=1))
        else:
            v = Unk("module-input" if (self.reusable and not self.is_module) else "var-unset")
        self.vmemo[name] = v
        return v

    def output(self, name):
        row = self.f.outputs.get(name)
        if row is None:
            return Unk("unevaluated")
        return _run(row[0], row[1], row[2], _Env(self, depth=1))

    def module_call(self, name):
        if name not in self.calls:
            self.calls[name] = _ModCall(self, name)
        return self.calls[name]

    def bindings(self, res, env=None):
        """(kind, [(key, value)]) a resource or module call runs over, (None, [(None, None)]) when it runs once, or an Unk."""
        bind = res["bind"]
        if bind is None:
            return (None, [(None, None)])
        row = res["attrs"][bind]
        env = env or _Env(self)
        v = _run(row[0], res["path"], row[1], env)
        if isinstance(v, Unk):
            return v
        if bind == "count":
            if isinstance(v, bool):
                v = int(v)
            if isinstance(v, float) and v == int(v):
                v = int(v)
            return ("count", [(i, i) for i in range(v)]) if isinstance(v, int) and 0 <= v <= 1000 else Unk("open-key-domain")
        if isinstance(v, dict):
            return ("for_each", list(v.items()))
        if isinstance(v, (list, tuple)):
            return ("for_each", [(x, x) for x in v])
        return Unk("open-key-domain")


_FOLDERS = {}


def _folder_of(target):
    target = os.path.abspath(target)
    if target not in _FOLDERS:
        _FOLDERS[target] = _Folder(target, _label_of(target))
    return _FOLDERS[target]


def _label_of(target):
    try:
        rel = os.path.relpath(target, REPO).replace("\\", "/")
    except ValueError:  # another drive
        rel = ".."
    if rel.startswith(".."):
        rel = os.path.basename(target)
    return rel


# ---- the scan ---------------------------------------------------------------------------------------------------

_SCAN_CACHE = {}


def _name_expr(res, scope, attr, env):
    """(raw expression text, line) of a resource's name attribute, or None when the resource states none or states one
    literal (the census counts that); the tags.Name form is read from the tags map."""
    attrs = res["attrs"]
    if attr == "tags.Name":
        tags = attrs.get("tags")
        if not tags:
            return None
        m = _NAME_TAG_RE.search(tags[0])
        if m and opal_naming._tf_literal(m.group(1)) is not None:
            return None
        return ("tags", tags[1])
    row = attrs.get(attr)
    if row is None or opal_naming._tf_literal(row[0]) is not None:
        return None
    return row


def _where_of(val, label, anchor):
    cand = sorted(set(s for s in _srcs_of([val]) if s[0] == label or s[0].startswith(label + "/")))
    return "%s:%d" % cand[0] if len(cand) == 1 else anchor


def _scan_scope(scope, label, resolved, uncounted, call_anchor=None):
    """Count or leave uncounted every graded resource of one scope, then follow its module calls."""
    attr_map = scope.attr_map
    for res in scope.f.resources:
        if res["type"] not in attr_map:
            continue
        typ, attr = attr_map[res["type"]]
        row = _name_expr(res, scope, attr, None)
        if row is None:
            continue
        anchor = call_anchor or "%s:%d" % (res["path"], res["line"])
        b = scope.bindings(res)
        got, bad = [], None
        if isinstance(b, Unk):
            bad = b.reason
        else:
            for bk, bv in b[1]:
                kind = b[0]
                env = _Env(scope, each=({"key": bk, "value": bv} if kind == "for_each" else None),
                           count=(bk if kind == "count" else None))
                if attr == "tags.Name":
                    tv = _run(res["attrs"]["tags"][0], res["path"], row[1], env)
                    val = tv if isinstance(tv, Unk) else (tv.get("Name") if isinstance(tv, dict) else Unk("unevaluated"))
                else:
                    val = _run(row[0], res["path"], row[1], env)
                if isinstance(val, Unk):
                    bad = val.reason
                    break
                if val is None or val == "":
                    continue
                if not isinstance(val, str):
                    bad = "unevaluated"
                    break
                w = _where_of(val, label, anchor)
                if (typ, str(val), w) not in got:
                    got.append((typ, str(val), w))
        if bad is not None:
            raw = row[0] if attr != "tags.Name" else "tags.Name"
            if attr == "tags.Name":
                m = _NAME_TAG_RE.search(res["attrs"]["tags"][0]) or re.search(r'Name\s*=\s*([^\n]+)', res["attrs"]["tags"][0])
                raw = m.group(1) if m else res["attrs"]["tags"][0]
            u = {"type": typ, "attribute": attr, "expression": _flat(raw), "reason": bad, "where": anchor}
            if u not in uncounted:
                uncounted.append(u)
        else:
            resolved += [{"plane": "repo", "type": a, "current": b_, "where": c} for a, b_, c in got]
    for name in sorted(scope.f.modules, key=lambda n: scope.f.modules[n]["line"]):
        call = scope.module_call(name)
        anchor = call_anchor or "%s:%d" % (call.block["path"], call.block["line"])
        if call.folder is None:
            _module_gap(call, call.reason, anchor, resolved, uncounted, label)
            continue
        pairs = call.pairs()
        if isinstance(pairs, Unk):
            _module_gap(call, pairs.reason, anchor, resolved, uncounted, label)
            continue
        for bk, bv in pairs[1]:
            inst = call.make((pairs[0], bk, bv))
            _scan_scope(inst.scope, label, resolved, uncounted, anchor)


def _module_gap(call, reason, anchor, resolved, uncounted, label):
    """A module call that makes no instance to read: the graded names its folder states without a literal are UNCOUNTED at
    the call, with the reason the call gives."""
    if call.folder is None:
        if call.reason == "external-module":
            uncounted.append({"type": "module", "attribute": "source", "expression": _flat(
                call.block["attrs"].get("source", ("", 0))[0]), "reason": reason, "where": anchor})
        return
    sc = _Scope(call.folder, args={}, depth=call.scope.depth + 1, is_module=True, root_dir=call.scope.root_dir)
    gap = Unk(reason)
    for name, row in call.block["attrs"].items():
        if name not in _MODULE_META:
            t = _Thunk("null", call.block["path"], row[1], _Env(call.scope))
            t.done, t.val = True, gap
            sc.args[name] = t
    tmp = []
    _scan_scope(sc, label, tmp, uncounted, anchor)


def scan_dir(directory, label, tf_names=None, json_names=None):
    """(literal, resolved, uncounted) of the .tf files in ONE folder (a Terraform configuration: its locals, its
    .tfvars / .tfvars.json files and the module folders it calls are read with it).
      literal    the names census_repo() counts (read here by the census's own reader, for a test to read once);
      resolved   the names the census cannot read that the repository resolves to a literal: items
                 {plane, type, current, where}, `where` the line that gives the literal;
      uncounted  one dict {type, attribute, expression, reason, where} per graded name the repository does not decide,
                 `reason` one of UNCOUNTED_REASONS.
    label is the repository-relative folder path that prefixes every `where`."""
    directory = os.path.abspath(directory)
    key = (directory, label, tuple(sorted(tf_names)) if tf_names is not None else None,
           tuple(sorted(json_names)) if json_names is not None else None)
    if key in _SCAN_CACHE:
        return _SCAN_CACHE[key]
    folder = _Folder(directory, label, tf_names, json_names)
    literal, resolved, uncounted = [], [], []
    for fn in sorted(folder.texts):
        names_, _exprs = opal_naming.census_tf_names(label + "/" + fn, folder.texts[fn])
        literal += [{"plane": "repo", "type": a, "current": b, "where": c} for a, b, c in names_]
    scope = _Scope(folder)
    _FOLDERS.clear()
    _scan_scope(scope, label, resolved, uncounted)
    seen, once = set(), []
    for i in resolved:  # two resources that take one name from one line (a record pair) are one name at one place
        k = (i["type"], i["current"], i["where"])
        if k not in seen:
            seen.add(k)
            once.append(i)
    _SCAN_CACHE[key] = (literal, once, uncounted)
    return _SCAN_CACHE[key]


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
        if (f.endswith(".tfvars.json") or f.endswith(".tfvars")) and _under(f, r):
            d, fn = f.rsplit("/", 1)
            jfiles.setdefault(d, []).append(fn)
    resolved, uncounted = [], []
    for d in sorted(by_dir):
        _lit, res, unc = scan_dir(os.path.join(REPO, *d.split("/")), d, by_dir[d], jfiles.get(d, []))
        resolved += res
        uncounted += unc
    return resolved, uncounted


def root_names(root, map_path=None):
    """(items, uncounted, stats): root_items() plus the names the root's own files and the module folders it calls resolve to
    a literal (BF-v-4, BF-w-2), and the names it builds that they do not resolve. A root whose items and uncounted are both
    empty has nothing to name."""
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
    smap = _lambda_functions()
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
