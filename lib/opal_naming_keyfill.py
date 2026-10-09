#!/usr/bin/env python3
"""Key classifier (LGIC_BLANKFIX BF-t-5).

grade() prints a storage key's canonical form with {source} and {scope} blanks when the name does not
carry them. This module classes each such row as exactly one of:

  PATTERN    the current name has a variable segment (opal_naming._VAR_RE); nothing to fill
  LEGACY     the key is a store of infra/logic/registry/legacy_addresses.json AND the key's bucket is that
             entry's bucket; it keeps its bytes (a key path alone never decides it)
  RULED      infra/logic/registry/key_rulings.json answers the key (the root check's match rule): the ruling's whole
             address, or none owed; it is neither filled nor refused
  REFUSED-CROSS-FIRM  the key's bucket belongs to another firm than the root entry's scope, or its own path
             names another firm, or a source other than the one source the registry says its bucket belongs to;
             it is never filled with this root's firm
  ADDRESS    the root's map entry fills {source} and {scope}: a whole address
  UNDECIDED  none of the above (no root entry, or a hole left after the fill)

Every row carries the bucket its key is used with (bucket_of: read from the same source file) and the basis.

  python lib/opal_naming_keyfill.py dir SOURCE_DIR --root ROOT_NAME --map PATH

Python 3.9 syntax; ASCII only; no dependency beyond lib/opal_naming.py and lib/opal_naming_rootmap.py.
It reads the registry and never writes it.
"""
import argparse
import ast
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import opal_naming  # noqa: E402
import opal_naming_rootmap  # noqa: E402

_FILLED = ("{source}", "{scope}")
_BLANK_RE = re.compile(r"\{[^}]*\}")
_TOKEN_RE = re.compile(r"[a-z0-9]+")


def _blanks(canonical):
    """The brace blanks of a canonical form, minus {system} and {cadence} (those are other cells' blanks)."""
    return [b for b in _BLANK_RE.findall(canonical) if b not in ("{system}", "{cadence}")]


def _legacy_entries():
    """[(row key, bucket, segment list)] from legacy_addresses.json, in the shape _on_list() takes."""
    doc = opal_naming._registry().get("legacy_addresses")
    if not isinstance(doc, dict):
        raise opal_naming.RegistryError("infra/logic/registry/legacy_addresses.json is absent from this package")
    out = []
    for row in doc.get("legacy_addresses", []):
        segs = row["template"].split("/")
        if row.get("shape") == "prefix" and segs and segs[-1] == "":
            segs = segs[:-1]
        out.append((row["key"], row["bucket"], segs))
    return out


def _key_segments(name, v):
    """(segments, is_prefix) of a key name as _grade_key() reads it: annotation dropped, bucket taken out."""
    sp = name.find(" ")
    key_ = name[:sp] if sp >= 0 else name
    prefix = key_.endswith("/")
    segs = key_.split("/")
    if prefix:
        segs = segs[:-1]
    if segs and segs[0] in v.buckets:
        segs = segs[1:]
    return segs, prefix


def _legacy_matches(name, v, entries):
    """[(row key, bucket)] of every legacy entry the key's PATH matches (the bucket is not read here)."""
    segs, prefix = _key_segments(name, v)
    if not segs or any(s == "" for s in segs):
        return []
    return [(key, bucket) for key, bucket, tpl in entries if opal_naming._on_list([tpl], segs, prefix)]


def _is_bucket_literal(value, v):
    """A string that is a bucket name the registry knows, or an opal-data- name."""
    return (isinstance(value, str) and bool(opal_naming._BUCKET_NAME_RE.match(value))
            and (value in v.buckets or value.startswith("opal-data-")))


def _s3_url_bucket(value, v):
    """The bucket named by the host of an s3://<bucket>/... string: a bucket-shaped host is a bucket by the URI itself
    (the registry need not know it)."""
    if isinstance(value, str) and value.startswith("s3://"):
        b = value[5:].partition("/")[0]
        if _is_bucket_literal(b, v) or opal_naming._BUCKET_NAME_RE.match(b):
            return b
    return None


def _s3_url_key_bucket(value, key, v):
    """The bucket of an s3://<bucket>/<path> constant whose path is the key (or begins with it), else None."""
    if isinstance(value, str) and key and value.startswith("s3://"):
        b = _s3_url_bucket(value, v)
        path = value[5:].partition("/")[2]
        if b and (path == key or path.startswith(key.rstrip("/") + "/")):
            return b
    return None


def _bucket_named_consts(tree, v):
    """{NAME: set of bucket-shaped literals} for a module-level NAME assigned a string that is not a registry bucket but IS
    used as a bucket in the file: the value of a Bucket= keyword, or the host of an s3://{NAME}/ f-string. The name's
    spelling is never the evidence; its use as the bucket is."""
    used = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.keyword) and n.arg == "Bucket" and isinstance(n.value, ast.Name):
            used.add(n.value.id)
        elif isinstance(n, ast.JoinedStr):
            vals = n.values
            if (len(vals) >= 2 and isinstance(vals[0], ast.Constant) and vals[0].value == "s3://"
                    and isinstance(vals[1], ast.FormattedValue) and isinstance(vals[1].value, ast.Name)):
                used.add(vals[1].value.id)
    out = {}
    for stmt in tree.body:
        if (isinstance(stmt, ast.Assign) and len(stmt.targets) == 1 and isinstance(stmt.targets[0], ast.Name)
                and stmt.targets[0].id in used and isinstance(stmt.value, ast.Constant)
                and isinstance(stmt.value.value, str) and opal_naming._BUCKET_NAME_RE.match(stmt.value.value)):
            out.setdefault(stmt.targets[0].id, {})[stmt.value.value] = stmt.lineno
    return out


def _split_where(where):
    path, _, line = (where or "").rpartition(":")
    return (path, int(line)) if path and line.isdigit() else (None, None)


def _header_nodes(stmt):
    """The nodes of one statement, a compound statement's body left out (its header is the statement)."""
    out, todo = [], [stmt]
    while todo:
        n = todo.pop()
        out.append(n)
        for field, val in ast.iter_fields(n):
            if n is stmt and field in ("body", "orelse", "finalbody", "handlers", "cases"):
                continue
            for ch in (val if isinstance(val, list) else [val]):
                if isinstance(ch, ast.AST):
                    todo.append(ch)
    return out


def _bucket_via_uses(tree, parent, node, consts, v):
    """(bucket or None, basis): the key literal `node` is assigned to a NAME; follow the name to its use sites in the
    same file. A use site names a bucket by a bucket literal or by a name assigned a bucket literal in the same file,
    in its own statement's header. All such sites naming the SAME bucket decide it; different buckets return None with a
    basis starting DIFFERENT; no site naming one returns None with what was seen (basis may be empty: no name)."""
    stmt = node
    while id(stmt) in parent and not isinstance(stmt, ast.stmt):
        stmt = parent[id(stmt)]
    if isinstance(stmt, ast.Assign) and len(stmt.targets) == 1 and isinstance(stmt.targets[0], ast.Name):
        name = stmt.targets[0].id
    elif isinstance(stmt, ast.AnnAssign) and isinstance(stmt.target, ast.Name) and stmt.value is not None:
        name = stmt.target.id
    else:
        return None, ""
    uses, named = [], {}
    for n in ast.walk(tree):
        if isinstance(n, ast.Name) and n.id == name and isinstance(n.ctx, ast.Load):
            us = n
            while id(us) in parent and not isinstance(us, ast.stmt):
                us = parent[id(us)]
            if not isinstance(us, ast.stmt):
                continue
            uses.append(n.lineno)
            for h in _header_nodes(us):
                b = None
                how = None
                if isinstance(h, ast.Constant) and isinstance(h.value, str):
                    b = h.value if _is_bucket_literal(h.value, v) else _s3_url_bucket(h.value, v)
                    how = "literal %r" % (b,)
                    if b is not None:
                        named.setdefault(b, []).append((n.lineno, getattr(h, "lineno", n.lineno), how))
                elif isinstance(h, ast.Name) and h.id in consts and h.id != name:
                    for b in sorted(consts[h.id]):
                        named.setdefault(b, []).append((n.lineno, getattr(h, "lineno", n.lineno),
                                                        "%s = %r" % (h.id, b)))
    if not uses:
        return None, "key constant %s (line %d) has no use site in the file" % (name, node.lineno)
    if not named:
        return None, "key constant %s (line %d) is used at lines %s, none names a bucket" % (
            name, node.lineno, ",".join(str(x) for x in sorted(set(uses))))
    desc = "; ".join("%s at line %d (use of %s at line %d: %s)" % (b, min(x[1] for x in r), name,
                     min(x[0] for x in r), r[0][2]) for b, r in sorted(named.items()))
    if len(named) > 1:
        return None, "DIFFERENT buckets at the use sites of key constant %s (line %d): %s" % (name, node.lineno, desc)
    b = next(iter(named))
    return b, "key constant %s (line %d) is used with bucket %s: %s" % (name, node.lineno, b, desc)


def _stmt_of(parent, node):
    """The nearest statement that holds `node` (the node itself when it is one)."""
    while id(node) in parent and not isinstance(node, ast.stmt):
        node = parent[id(node)]
    return node if isinstance(node, ast.stmt) else None


def _header_buckets(stmt, consts, v):
    """[(bucket, line, how)]: the buckets one statement's header names, by a bucket literal or by a name assigned a bucket
    literal in the same file (a compound statement's body is not its header)."""
    out = []
    for h in _header_nodes(stmt):
        if isinstance(h, ast.Constant) and isinstance(h.value, str):
            b = h.value if _is_bucket_literal(h.value, v) else _s3_url_bucket(h.value, v)
            if b is not None:
                out.append((b, getattr(h, "lineno", stmt.lineno), "literal %r" % (b,)))
        elif isinstance(h, ast.Name) and h.id in consts:
            for b in sorted(consts[h.id]):
                out.append((b, getattr(h, "lineno", stmt.lineno), "%s = %r" % (h.id, b)))
    return out


def _field_of(parent, node):
    """The constant string field name a key literal is the value of in a dict literal (the key literal itself, or an element
    of a list, tuple or set that is the value), else None. The climb stops at the statement."""
    child = node
    while id(child) in parent and not isinstance(child, ast.stmt):
        par = parent[id(child)]
        if isinstance(par, ast.Dict):
            for k, val in zip(par.keys, par.values):
                if val is child and isinstance(k, ast.Constant) and isinstance(k.value, str):
                    return k.value
            return None
        if not isinstance(par, (ast.List, ast.Tuple, ast.Set)):
            return None
        child = par
    return None


def _bucket_via_field(tree, parent, node, consts, v):
    """(bucket or None, basis): the key literal is the value of the field F of a dict literal. Every place the same file
    READS that field (x["F"], x.get("F")) in a statement whose header names a bucket decides it: all such places naming the
    SAME bucket give it; different buckets return None with a basis starting DIFFERENT; no place naming one returns
    (None, "") and leaves the question to the container rule."""
    field = _field_of(parent, node)
    if field is None:
        return None, ""
    named = {}
    for n in ast.walk(tree):
        hit = False
        if isinstance(n, ast.Subscript) and isinstance(n.ctx, ast.Load):
            sl = n.slice
            hit = isinstance(sl, ast.Constant) and sl.value == field
        elif (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr == "get" and n.args
              and isinstance(n.args[0], ast.Constant) and n.args[0].value == field):
            hit = True
        if not hit:
            continue
        us = _stmt_of(parent, n)
        if us is None:
            continue
        for b, ln, how in _header_buckets(us, consts, v):
            named.setdefault(b, []).append((n.lineno, ln, how))
    if not named:
        return None, ""
    desc = "; ".join("%s (read at line %d, %s)" % (b, min(x[0] for x in r), r[0][2]) for b, r in sorted(named.items()))
    if len(named) > 1:
        return None, "DIFFERENT buckets where the file reads the field %r the key is the value of: %s" % (field, desc)
    b = next(iter(named))
    return b, "the key is the value of field %r (line %d), which the file reads with bucket %s: %s" % (
        field, node.lineno, b, desc)


def _bucket_via_container(parent, node, consts, v):
    """(bucket or None, basis): the key literal is a keyword argument of a call or a value of a dict literal; the OTHER
    direct values of that same call or dict that are bucket literals (or names assigned one) are the bucket the file pairs
    with it. Exactly one distinct bucket decides; none or several return (None, "")."""
    child = node
    while id(child) in parent and not isinstance(child, ast.stmt):
        par = parent[id(child)]
        sibs, what = None, None
        if isinstance(par, ast.keyword) and isinstance(parent.get(id(par)), ast.Call):
            call = parent[id(par)]
            sibs = [k.value for k in call.keywords if k is not par]
            what = "call (line %d), where the key is the argument %s" % (call.lineno, par.arg)
        elif isinstance(par, ast.Dict) and any(val is child for val in par.values):
            sibs = [val for val in par.values if val is not child]
            what = "dict (line %d)" % par.lineno
        if sibs is not None:
            found = set()
            for s in sibs:
                if isinstance(s, ast.Constant) and isinstance(s.value, str):
                    b = s.value if _is_bucket_literal(s.value, v) else _s3_url_bucket(s.value, v)
                    if b:
                        found.add(b)
                elif isinstance(s, ast.Name) and s.id in consts:
                    found |= consts[s.id]
            if len(found) == 1:
                b = next(iter(found))
                return b, "bucket %s is in the same %s as the key" % (b, what)
            return None, ""
        child = par
    return None, ""


def _params(fn):
    a = fn.args
    return [x.arg for x in list(getattr(a, "posonlyargs", [])) + list(a.args) + list(a.kwonlyargs)]


def _param_default(fn, pname):
    a = fn.args
    pos = list(getattr(a, "posonlyargs", [])) + list(a.args)
    for i, x in enumerate(pos):
        if x.arg == pname:
            j = i - (len(pos) - len(a.defaults))
            return a.defaults[j] if j >= 0 else None
    for x, d in zip(a.kwonlyargs, a.kw_defaults):
        if x.arg == pname:
            return d
    return None


def _param_sites(tree, parent, fn, pname, consts, v, depth, seen):
    """(buckets, problems): what every call site in the file passes for parameter `pname` of function `fn`. A site passing a
    bucket literal, a name assigned one, or a default that is one, names it; a site passing a parameter of its own function
    is followed (to depth 4); anything else is a problem that says what the site passes."""
    if (id(fn), pname) in seen or depth > 4:
        return set(), ["the call chain through %s is circular or deeper than 4" % fn.name]
    seen = seen | {(id(fn), pname)}
    in_class = isinstance(parent.get(id(fn)), ast.ClassDef)
    pos = list(getattr(fn.args, "posonlyargs", [])) + list(fn.args.args)
    idx = [x.arg for x in pos].index(pname) if pname in [x.arg for x in pos] else None
    sites = [c for c in ast.walk(tree) if isinstance(c, ast.Call) and (
        (isinstance(c.func, ast.Name) and c.func.id == fn.name)
        or (isinstance(c.func, ast.Attribute) and c.func.attr == fn.name))]
    if not sites:
        return set(), ["%s(...) is called nowhere in this file, so its parameter %s is set elsewhere" % (fn.name, pname)]
    found, problems = set(), []
    for c in sites:
        arg = None
        for kw in c.keywords:
            if kw.arg == pname:
                arg = kw.value
        if arg is None and idx is not None:
            at = idx - (1 if in_class and isinstance(c.func, ast.Attribute) else 0)
            if 0 <= at < len(c.args) and not isinstance(c.args[at], ast.Starred):
                arg = c.args[at]
        if arg is None:
            arg = _param_default(fn, pname)
            if arg is None:
                problems.append("line %d calls %s without %s" % (c.lineno, fn.name, pname))
                continue
        shown = ast.unparse(arg) if hasattr(ast, "unparse") else "an expression"
        owner = c
        while id(owner) in parent and not isinstance(owner, (ast.FunctionDef, ast.AsyncFunctionDef)):
            owner = parent[id(owner)]
        if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
            b = arg.value if _is_bucket_literal(arg.value, v) else _s3_url_bucket(arg.value, v)
            if b:
                found.add(b)
            else:
                problems.append("line %d passes %s, which is not a bucket name" % (c.lineno, shown))
        elif (isinstance(arg, ast.Name) and isinstance(owner, (ast.FunctionDef, ast.AsyncFunctionDef))
              and arg.id in _params(owner)):
            got, probs = _param_sites(tree, parent, owner, arg.id, consts, v, depth + 1, seen)
            found |= got
            problems.extend("line %d passes %s, a parameter of %s; %s" % (c.lineno, shown, owner.name, p) for p in probs)
        elif isinstance(arg, ast.Name) and arg.id in consts and len(consts[arg.id]) == 1:
            found |= consts[arg.id]
        else:
            problems.append("line %d passes %s, which names no bucket literal in this file" % (c.lineno, shown))
    return found, problems


def _bucket_via_param(tree, parent, node, consts, v):
    """(bucket or None, basis): the key literal is an argument of a call that also passes Bucket=<NAME>, NAME a parameter of
    the function holding the call. The call sites of that function in the same file decide it when every one names the same
    bucket (_param_sites). (None, "") when the key is in no such call; (None, why) when the file does not decide."""
    call = None
    child = node
    while id(child) in parent and not isinstance(child, ast.stmt):
        child = parent[id(child)]
        if isinstance(child, ast.Call) and any(k.arg == "Bucket" for k in child.keywords):
            call = child
            break
    if call is None:
        return None, ""
    val = [k.value for k in call.keywords if k.arg == "Bucket"][0]
    fn = call
    while id(fn) in parent and not isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)):
        fn = parent[id(fn)]
    if not (isinstance(val, ast.Name) and isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef))
            and val.id in _params(fn)):
        return None, ""
    found, problems = _param_sites(tree, parent, fn, val.id, consts, v, 0, frozenset())
    head = "the key is used with Bucket=%s (line %d), a parameter of %s" % (val.id, call.lineno, fn.name)
    if problems:
        return None, "%s; the file does not decide it: %s" % (head, "; ".join(problems))
    if len(found) > 1:
        return None, "DIFFERENT buckets at the call sites of %s: %s" % (fn.name, ", ".join(sorted(found)))
    b = next(iter(found))
    return b, "%s; every call site in the file names bucket %s" % (head, b)


def _bucket_of_py(tree, line, key, v):
    """(bucket or None, basis) for the key constant on `line` of a parsed Python source."""
    parent = {}
    for node in ast.walk(tree):
        for ch in ast.iter_child_nodes(node):
            parent[id(ch)] = node
    docs = set()
    consts = {}  # module-level NAME -> set of bucket literals assigned to it
    allb = {}    # distinct bucket literal -> first line, over the whole file (docstrings skipped)
    for node in ast.walk(tree):
        body = getattr(node, "body", None)
        if isinstance(body, list) and body and isinstance(body[0], ast.Expr)                 and isinstance(body[0].value, ast.Constant):
            docs.add(id(body[0].value))
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str) and id(node) not in docs:
            b = node.value if _is_bucket_literal(node.value, v) else _s3_url_bucket(node.value, v)
            if b:
                allb.setdefault(b, getattr(node, "lineno", 0))
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            val = [n.value for n in ast.walk(node.value)
                   if isinstance(n, ast.Constant) and isinstance(n.value, str) and _is_bucket_literal(n.value, v)]
            if val:
                consts.setdefault(node.targets[0].id, set()).update(val)
    for nm, lits in _bucket_named_consts(tree, v).items():
        consts.setdefault(nm, set()).update(lits)
        for b, ln in lits.items():
            allb.setdefault(b, ln)
    here = [n for n in ast.walk(tree) if isinstance(n, ast.Constant) and isinstance(n.value, str)
            and getattr(n, "lineno", 0) == line and id(n) not in docs]
    mine = [n for n in here if n.value == key] or [n for n in here if key and key in n.value]
    extra = ""
    if mine:
        node = mine[0]
        ub = _s3_url_key_bucket(node.value, key, v)
        if ub is not None:
            return ub, "bucket %s is the host of the s3:// constant that holds the key (line %d)" % (ub, node.lineno)
        fb, fwhy = _bucket_via_field(tree, parent, node, consts, v)
        if fb is not None:
            return fb, fwhy
        if fwhy.startswith("DIFFERENT"):
            return None, fwhy
        stmt = node
        while id(stmt) in parent and not isinstance(stmt, ast.stmt):
            stmt = parent[id(stmt)]
        lits, names = set(), {}
        for n in _header_nodes(stmt):
            if n is node:
                continue
            if isinstance(n, ast.Constant) and isinstance(n.value, str):
                b = n.value if _is_bucket_literal(n.value, v) else _s3_url_bucket(n.value, v)
                if b:
                    lits.add(b)
            elif isinstance(n, ast.Name) and n.id in consts:
                names[n.id] = consts[n.id]
        pooled = set(lits)
        for vals in names.values():
            pooled |= vals
        if len(pooled) == 1:
            b = next(iter(pooled))
            if lits:
                return b, "bucket literal %r in the same statement as the key" % b
            return b, "constant %s = %r, named in the same statement as the key" % (sorted(names)[0], b)
        if len(pooled) > 1:
            cb, cwhy = _bucket_via_container(parent, node, consts, v)
            if cb is not None:
                return cb, cwhy
            return None, "the key's own statement names several buckets, none picked: %s" % ", ".join(sorted(pooled))
        pb, pwhy = _bucket_via_param(tree, parent, node, consts, v)
        if pb is not None:
            return pb, pwhy
        if pwhy.startswith("DIFFERENT"):
            return None, pwhy
        extra = pwhy
    seen = ""
    if mine:
        got, seen = _bucket_via_uses(tree, parent, mine[0], consts, v)
        if got is not None:
            return got, seen
        if seen.startswith("DIFFERENT"):
            return None, seen
        direct = isinstance(stmt, (ast.Assign, ast.AnnAssign)) and stmt.value is mine[0]
        seen = "; " + seen if seen and (direct or allb) else ""
    if extra:
        seen = "; " + extra + seen
    if len(allb) == 1:
        b = next(iter(allb))
        return b, "the file's only bucket literal %r (line %d); the key's own statement names none" % (b, allb[b])
    if not allb:
        return None, "no bucket literal in the file and none in the key's statement" + seen
    return None, "the file has %d bucket candidates and the key's statement picks none: %s%s" % (
        len(allb), ", ".join("%s (line %d)" % (b, n) for b, n in sorted(allb.items())), seen)


_PER_FIRM_VAR_RE = re.compile(r"^[A-Z][A-Z0-9_]*_BUCKET_MAP$")


def _item_text(item, text=None):
    """(path, source text or None) of the file an item's `where` names; `text` stands in for the file when given."""
    path, _line = _split_where(item.get("where"))
    if path is None:
        return None, None
    if text is not None:
        return path, text
    try:
        return path, opal_naming._read_text(os.path.join(opal_naming.REPO, *path.split("/")))
    except (OSError, UnicodeDecodeError, ValueError):
        return path, None


def _string_constants(path, text):
    """[(value, line)] of the string constants of a source file (a Python docstring is not one)."""
    if path.endswith(".py"):
        try:
            tree = ast.parse(text)
        except (SyntaxError, ValueError):
            return []
        docs = set()
        for node in ast.walk(tree):
            body = getattr(node, "body", None)
            if isinstance(body, list) and body and isinstance(body[0], ast.Expr)                     and isinstance(body[0].value, ast.Constant):
                docs.add(id(body[0].value))
        return [(n.value, getattr(n, "lineno", 0)) for n in ast.walk(tree)
                if isinstance(n, ast.Constant) and isinstance(n.value, str) and id(n) not in docs]
    if path.endswith(opal_naming.CENSUS_SOURCE_EXT):
        return [(val, n) for val, _c, n in opal_naming._js_literals(text)]
    return []


def _called_names(path, text, names):
    """{name: line} of the asked `names` that a Python source CALLS (f(...) or x.f(...)), first call by line."""
    if not names or not path.endswith(".py"):
        return {}
    try:
        tree = ast.parse(text)
    except (SyntaxError, ValueError):
        return {}
    out = {}
    for n in ast.walk(tree):
        if isinstance(n, ast.Call):
            f = n.func
            nm = f.id if isinstance(f, ast.Name) else (f.attr if isinstance(f, ast.Attribute) else None)
            if nm in names and (nm not in out or n.lineno < out[nm]):
                out[nm] = n.lineno
    return out


def runtime_bucket(item, text=None, names=()):
    """([variable or function names], basis): the per-firm run-time bucket the item's source file shows. A variable shows
    as a string constant of the file that is an upper-case name ending _BUCKET_MAP (one bucket per firm), or is one of
    `names` (the variables a registry row asks for). A FUNCTION shows as a call in the file to a name in `names` (a
    registry row's bucket_from that is a function: the code gets the firm's bucket by calling it). The basis says which line
    of which file shows each. ([], "") when the file is unreadable or shows none."""
    path, src = _item_text(item, text)
    if path is None or src is None:
        return [], ""
    found = {}
    for val, ln in _string_constants(path, src):
        if _PER_FIRM_VAR_RE.match(val) or val in names:
            found.setdefault(val, ln)
    calls = dict((k, ln) for k, ln in _called_names(path, src, set(names)).items() if k not in found)
    if not found and not calls:
        return [], ""
    parts = ["line %d of %s holds the name %s, an environment variable that gives one bucket per firm" % (
        ln, path.rsplit("/", 1)[-1], name) for name, ln in sorted(found.items())]
    parts += ["line %d of %s calls the function %s, which gives one bucket per firm" % (
        ln, path.rsplit("/", 1)[-1], name) for name, ln in sorted(calls.items())]
    return sorted(set(found) | set(calls)), "the bucket is chosen at run time: " + "; ".join(parts)


def bucket_of(item, text=None):
    """(bucket or None, basis): as _bucket_of_read(); a bucket that is not read, in a file that shows a per-firm run-time
    bucket variable (runtime_bucket), also says so in the basis."""
    b, why = _bucket_of_read(item, text)
    if b is None and not item.get("bucket"):
        names, rb = runtime_bucket(item, text)
        if names:
            why = "%s; %s" % (why, rb)
    return b, why


def _bucket_of_read(item, text=None):
    """(bucket or None, basis): the bucket the key at item["where"] is used with, read from the SAME source file
    (`text` stands in for the file when given). A bucket the item already carries comes first. Never read from the
    folder name. None comes with the reason, or the candidates when the file has several and the key picks none."""
    v = opal_naming._vocab()
    if item.get("bucket"):
        return item["bucket"], item.get("bucket_basis") or "carried by the item"
    path, line = _split_where(item.get("where"))
    if path is None:
        return None, "item has no path:line where"
    if text is None:
        try:
            text = opal_naming._read_text(os.path.join(opal_naming.REPO, *path.split("/")))
        except (OSError, UnicodeDecodeError, ValueError) as exc:
            return None, "source %s unreadable: %s" % (path, type(exc).__name__)
    key = item["current"]
    if path.endswith(".py"):
        try:
            tree = ast.parse(text)
        except (SyntaxError, ValueError):
            return None, "source %s does not parse as Python" % path
        return _bucket_of_py(tree, line, key, v)
    # non-Python source: this line's literals, else the file's
    lits = opal_naming._js_literals(text) if path.endswith(opal_naming.CENSUS_SOURCE_EXT) else []
    same = {val for val, _c, n in lits if n == line and _is_bucket_literal(val, v)}
    if len(same) == 1:
        return sorted(same)[0], "bucket literal in the same line as the key"
    allb = {val for val, _c, _n in lits if _is_bucket_literal(val, v)}
    if len(allb) == 1:
        return sorted(allb)[0], "the file's only bucket literal"
    if not allb:
        return None, "no bucket literal in the file"
    return None, "the file has %d bucket candidates and the key's line picks none: %s" % (len(allb), ", ".join(sorted(allb)))


def _firms(v):
    """The scope words that are a firm (a firm has a bucket); global and the numbered scopes are not."""
    return set(v.bucket_firm.values())


_REASONS = ("bucket-names-no-firm", "bucket-not-read", "bucket-chosen-at-run-time", "no-path-word-names-a-firm")


def _tok_firm(tok, v):
    """The firm a path token names, else None: a firm word (long or short), or a master account of a firm (08242234 names
    49financial); global and a product are no firm."""
    long_ = v.scope.get(tok)
    if long_ is None:
        return None
    for s in opal_naming._scopes(opal_naming._registry()):
        if s.get("long") == long_ and s.get("class") == "MASTER":
            return s.get("firm") or long_
    return long_


def _bucket_source(bucket, v):
    """The one source the registry says a bucket belongs to, else None. The registry (scopes.json) says it only for a
    PRODUCT scope's bucket whose key is also a source of systems.json (mdpf, etfs, irpt, harvest); a firm's bucket and the
    shared stores hold many sources, so they name none."""
    if not bucket:
        return None
    found = set()
    for s in opal_naming._scopes(opal_naming._registry()):
        names = [s.get("bucket")] + [a.get("spelling") for a in s.get("aliases", []) if "bucket" in a.get("planes", [])]
        if s.get("class") == "PRODUCT" and bucket in names and s.get("key") in v.v1:
            found.add(s["key"])
    return next(iter(found)) if len(found) == 1 else None


def _firm_check(name, v, bucket, bbasis, root_entry, runtime=()):
    """The cross-firm check of one stored file. {"home", "home_kind", "clash", "unchecked", "code"}.
    What the key's firm is compared WITH is the firm of its own bucket (the registry's bucket-to-firm table), whatever
    the root entry fills; where the bucket was not read (or names no firm) the root entry's scope stands in, when the
    entry may give one (no `fills`, or `fills` lists scope); otherwise nothing is compared and `unchecked` says why, and
    `code` is one of _REASONS (`runtime` is the per-firm variable names the key's file shows). A path word naming a
    source is judged only against the source the registry says the bucket belongs to (_bucket_source), never against the
    root entry's source: a path whose own first segment is a source the registry knows names ITS source. A key whose path
    names no firm at all has nothing to refuse and is checked (code no-path-word-names-a-firm)."""
    fills = None if root_entry is None else root_entry.get("fills")
    can_scope = root_entry is not None and (fills is None or "scope" in fills)
    bfirm = v.bucket_firm.get(bucket) if bucket else None
    own_scope = v.scope.get(root_entry.get("scope"), root_entry.get("scope")) if can_scope else None
    if bfirm is not None:
        home, kind = bfirm, "bucket"
    elif can_scope:
        home, kind = own_scope, "root"
    else:
        home, kind = None, None
    firms = _firms(v)
    toks = _TOKEN_RE.findall(name.lower())
    bsrc = _bucket_source(bucket, v)
    clash = None
    for tok in toks:
        tf = _tok_firm(tok, v)
        if home is not None and tf is not None and tf != home and (kind == "root" or tf in firms):
            if kind == "root" or own_scope == home:
                # the root's scope and the bucket's firm are the same firm: the wording the root check already reads
                clash = "path token %r names firm %r, the root entry's scope is %r" % (tok, tf, home)
            else:
                clash = "path token %r names firm %r, the firm of bucket %s is %r" % (tok, tf, bucket, home)
            break
        if bsrc is not None and tok in v.v1 and tok != bsrc:
            clash = "path token %r names source %r, bucket %s belongs to source %r" % (tok, tok, bucket, bsrc)
            break
    unchecked, code = None, None
    if home is None and clash is None:
        if not any(_tok_firm(t, v) in firms for t in toks):
            code = "no-path-word-names-a-firm"
        else:
            if bucket is None:
                why = "the key's bucket was not read (%s)" % (bbasis,)
                code = "bucket-chosen-at-run-time" if runtime else "bucket-not-read"
            else:
                why = "bucket %s names no firm" % (bucket,)
                code = "bucket-names-no-firm"
            if root_entry is None:
                unchecked = "the firm could not be checked: %s and there is no root map entry" % why
            elif can_scope:
                unchecked = "the firm could not be checked: %s and the root entry gives no scope" % why
            else:
                unchecked = ("the firm could not be checked: %s and the root entry's fills (%s) leave out scope, so it gives "
                             "no firm to compare with" % (why, ", ".join(fills)))
    return {"home": home, "home_kind": kind, "clash": clash, "unchecked": unchecked, "code": code}


def _address_firm(canonical):
    """The firm a filled address writes: its second segment (source/scope/...) when that segment is a scope word."""
    segs = (canonical or "").split("/")
    v = opal_naming._vocab()
    if len(segs) > 1 and segs[1] in v.scope:
        return v.scope[segs[1]]
    return None


def _item_bucket(it, name, v, text_of=None):
    """(bucket or None, basis): a bucket the key itself names wins, else bucket_of() reads the source."""
    segs0 = name.split(" ")[0].split("/")
    if segs0 and segs0[0] in v.buckets and len(segs0) > 1:
        return segs0[0], "the key names its bucket as its first segment"
    return bucket_of(it, text_of(it) if text_of else None)


def _rulings(key_rulings=None):
    """{(bucket, key): row} of infra/logic/registry/key_rulings.json, read by the root check's own loader
    (opal_naming_rootcheck.load_key_rulings) unless a table is passed. Imported at the call: rootcheck imports this module."""
    if key_rulings is not None:
        return key_rulings
    import opal_naming_rootcheck
    return opal_naming_rootcheck.load_key_rulings()


def ruling_of(item, rulings, text_of=None):
    """The key_rulings.json row that answers a stored-file item, else None: the root check's own match rule
    (opal_naming_rootcheck._ruling_of: a per-firm row by the key and the variable its file shows, else the (bucket, key)
    row with the bucket bucket_of() reads). `text_of(item)` stands in for the source file (the test's way in). An item whose
    key no row carries is not asked (no source is read for it)."""
    if item.get("type") != "S3Key" or not rulings:
        return None
    if not any(k == item["current"] for (_b, k) in rulings):
        return None
    import opal_naming_rootcheck
    if text_of is None:
        return opal_naming_rootcheck._ruling_of(item, rulings)[0]
    return opal_naming_rootcheck._ruling_of(
        item, rulings, bucket_reader=lambda i: bucket_of(i, text_of(i)),
        runtime_reader=lambda i, _t, names: runtime_bucket(i, text_of(i), names))[0]


def _ruling_basis(row):
    if row.get("canonical"):
        return "key ruling: the whole address is %s" % (row["canonical"],)
    return "key ruling: %s" % (str(row["none_owed"]).strip().rstrip("."),)


def _classify(items, root_entry, text_of=None, key_rulings=None):
    """(rows, raising, graded): the classified rows, the count grade() raised on, the count of graded
    items that carry a {source}/{scope} blank (the rows' denominator). text_of(item) may stand in for the
    source file bucket_of() would read (the test's way in)."""
    v = opal_naming._vocab()
    entries = _legacy_entries()
    rows, raising = [], 0
    rulings = _rulings(key_rulings)
    own_scope = None if root_entry is None else v.scope.get(root_entry.get("scope"), root_entry.get("scope"))
    # `fills` (root map): the slots the entry may fill; absent means all of them. A slot it leaves out is the key's own,
    # so the entry's HOME scope/source is not written into a name. The cross-firm checks do not depend on it: a key's
    # firm is compared with the firm of its own bucket (_firm_check).
    fills = None if root_entry is None else root_entry.get("fills")
    can_scope = fills is None or "scope" in fills
    for it in items:
        name, typ = it["current"], it["type"]
        try:
            _verdict, canon = opal_naming.grade(name, typ)
        except opal_naming.RaiseDefect:
            raising += 1
            continue
        if canon is None or not _blanks(canon):
            continue
        bucket, bbasis = _item_bucket(it, name, v, text_of)
        row = {"type": typ, "current": name, "where": it.get("where"), "class": None, "canonical": None,
               "basis": None, "bucket": bucket, "bucket_basis": bbasis}
        var = opal_naming._VAR_RE.search(name)
        ruled = None if var else ruling_of(it, rulings, text_of)
        matches = [] if var or ruled else _legacy_matches(name, v, entries)
        leg = [m for m in matches if bucket is not None and m[1] == bucket]
        bfirm = v.bucket_firm.get(bucket) if bucket else None
        fc = None if var or ruled else _firm_check(name, v, bucket, bbasis, root_entry)
        clash = None if fc is None else fc["clash"]
        no_check = "" if fc is None or fc["unchecked"] is None else "; " + fc["unchecked"]
        not_legacy = ""
        if matches and not leg:
            not_legacy = "; not LEGACY: the path matches legacy row %s of bucket %s, this key's bucket is %s" % (
                matches[0][0], matches[0][1], bucket if bucket else "unread (%s)" % bbasis)
        if var:
            row["class"] = "PATTERN"
            row["basis"] = "variable segment %r in the current name" % (var.group(0),)
        elif ruled:
            row["class"] = "RULED"
            row["canonical"] = ruled.get("canonical")
            row["basis"] = _ruling_basis(ruled)
        elif leg:
            row["class"] = "LEGACY"
            row["canonical"] = name
            row["basis"] = "legacy_addresses.json row %s (bucket %s), the key's bucket is the same" % leg[0]
        elif root_entry is not None and can_scope and bfirm is not None and bfirm != own_scope:
            row["class"] = "REFUSED-CROSS-FIRM"
            row["basis"] = "bucket %s belongs to firm %r, the root entry's scope is firm %r%s" % (
                bucket, bfirm, own_scope, not_legacy)
        elif clash:
            row["class"] = "REFUSED-CROSS-FIRM"
            row["basis"] = "conflict: " + clash + not_legacy
        elif root_entry is None:
            row["class"] = "UNDECIDED"
            row["basis"] = "no root map entry: nothing fills the blanks %s%s" % (",".join(_blanks(canon)), not_legacy)
        else:
            filled = canon
            for blank, field in (("{source}", "source"), ("{scope}", "scope")):
                if (fills is None or field in fills) and isinstance(root_entry.get(field), str) and root_entry[field]:
                    filled = filled.replace(blank, root_entry[field])
            left = [b for b, f in (("{scope}", "scope"), ("{source}", "source"))
                    if b in filled and fills is not None and f not in fills]
            if left:
                row["class"] = "UNDECIDED"
                row["basis"] = "this root serves more than one firm; its map entry does not give the %s%s" % (
                    "firm" if "{scope}" in left else "source", not_legacy + no_check)
            elif "{" in filled:
                row["class"] = "UNDECIDED"
                row["basis"] = "a blank remains after the root entry fills source and scope: %s%s" % (filled, not_legacy)
            else:
                wfirm = _address_firm(filled)
                if bfirm is not None and wfirm is not None and wfirm != bfirm:
                    row["class"] = "REFUSED-CROSS-FIRM"
                    row["basis"] = "the filled address %s writes firm %r, bucket %s belongs to firm %r%s" % (
                        filled, wfirm, bucket, bfirm, not_legacy)
                else:
                    row["class"] = "ADDRESS"
                    row["canonical"] = filled
                    row["basis"] = "root entry source=%s scope=%s%s%s" % (root_entry["source"], root_entry["scope"],
                                                                        not_legacy, no_check)
        rows.append(row)
    graded = len(rows)
    return rows, raising, graded


def fill_keys(items, root_entry, key_rulings=None):
    """One dict per item whose graded canonical carries a blank other than {system}/{cadence}:
    type, current, where, class, canonical (or None), basis, bucket (or None), bucket_basis. An item grade()
    raises on is skipped. A key infra/logic/registry/key_rulings.json answers (the root check's match rule) is class RULED,
    with the ruling's canonical address or None; `key_rulings` stands in for the file."""
    return _classify(items, root_entry, key_rulings=key_rulings)[0]


def _independent_count(items):
    """The folder's graded items whose canonical carries {source} or {scope}, counted without fill_keys."""
    n = 0
    for it in items:
        try:
            _v, canon = opal_naming.grade(it["current"], it["type"])
        except opal_naming.RaiseDefect:
            continue
        if canon and ("{source}" in canon or "{scope}" in canon):
            n += 1
    return n


def cmd_dir(source_dir, root, map_path, out=print):
    prefix = source_dir.replace("\\", "/").strip("/") + "/"
    doc = opal_naming_rootmap.load_map(map_path)
    root_entry = (doc.get("roots") or {}).get(root)
    items, _stats = opal_naming.census_repo()
    sel = [i for i in items if i["where"].startswith(prefix)]
    rows, raising, _n = _classify(sel, root_entry)
    count = {"ADDRESS": 0, "LEGACY": 0, "PATTERN": 0, "REFUSED-CROSS-FIRM": 0, "UNDECIDED": 0, "RULED": 0}
    for r in rows:
        count[r["class"]] += 1
        out("%s %s %r canonical=%s where=%s bucket=%s bucket_basis=%s basis=%s"
            % (r["class"], r["type"], r["current"], r["canonical"], r["where"], r["bucket"], r["bucket_basis"],
               r["basis"]))
    holes = [r for r in rows if r["class"] == "ADDRESS"
             and ("{" in r["canonical"] or "%s" in r["canonical"] or "*" in r["canonical"])]
    ind = _independent_count(sel)
    ok = (root_entry is not None and sum(count.values()) == len(rows) and len(rows) == ind and not holes
          and len(rows) > 0)
    out("KEYFILL-DIR ok=%s dir=%s rows=%d address=%d legacy=%d pattern=%d ruled=%d refused=%d undecided=%d "
        "raising=%d with_bucket=%d"
        % (ok, prefix.rstrip("/"), len(rows), count["ADDRESS"], count["LEGACY"], count["PATTERN"],
           count["RULED"], count["REFUSED-CROSS-FIRM"], count["UNDECIDED"], raising, sum(1 for r in rows if r["bucket"])))
    return 0 if ok else 1


def _word_firm(name, v):
    """The first firm a path word of the key names, else None."""
    firms = _firms(v)
    for tok in _TOKEN_RE.findall(name.lower()):
        if tok in v.scope and v.scope[tok] in firms:
            return v.scope[tok]
    return None


def crossfirm_rows(root, root_entry, map_path=None, key_rulings=None):
    """One dict per stored file (type S3Key) of a mapped root: root, current, where, bucket, bucket_firm, word_firm
    (the firm the path word, or the filled address, names), verdict (OK, RULED, REFUSED, UNCHECKED), code (the reason
    of an UNCHECKED row, one of _REASONS; no-path-word-names-a-firm also on an OK row), reason."""
    import opal_naming_scope
    v = opal_naming._vocab()
    rulings = _rulings(key_rulings)
    items, _stats = opal_naming_scope.root_items("infra/aws/terraform/" + root, map_path)
    items = [i for i in items if i["type"] == "S3Key"]
    filled = {}
    for r in _classify(items, root_entry, key_rulings=rulings)[0]:
        filled[(r["type"], r["current"], r["where"])] = r
    out = []
    for it in items:
        name = it["current"]
        bucket, bbasis = _item_bucket(it, name, v)
        names, _rb = runtime_bucket(it)
        fc = _firm_check(name, v, bucket, bbasis, root_entry, names)
        row = filled.get((it["type"], name, it["where"]))
        wfirm = _word_firm(name, v)
        if row is not None and row["class"] == "ADDRESS":
            wfirm = _address_firm(row["canonical"]) or wfirm
        rec = {"root": root, "current": name, "where": it["where"], "bucket": bucket,
               "bucket_firm": v.bucket_firm.get(bucket) if bucket else None, "word_firm": wfirm,
               "verdict": None, "code": None, "reason": None, "runtime": names}
        ruled = ruling_of(it, rulings)
        if ruled:
            rec["verdict"], rec["reason"] = "RULED", _ruling_basis(ruled)
        elif row is not None and row["class"] == "REFUSED-CROSS-FIRM":
            rec["verdict"], rec["reason"] = "REFUSED", row["basis"]
        elif fc["clash"]:
            rec["verdict"], rec["reason"] = "REFUSED", fc["clash"]
        elif fc["unchecked"]:
            rec["verdict"], rec["code"], rec["reason"] = "UNCHECKED", fc["code"], fc["unchecked"]
        elif fc["code"]:
            rec["verdict"], rec["code"] = "OK", fc["code"]
            rec["reason"] = "no path word names a firm: nothing to refuse"
        else:
            rec["verdict"] = "OK"
            rec["reason"] = "path words name no firm other than the %s's %r" % (
                "bucket" if fc["home_kind"] == "bucket" else "root entry scope", fc["home"])
        out.append(rec)
    return out


def _detail(r):
    """What a reason's table row names: the bucket, the variable, or the bucket candidates seen."""
    if r["code"] == "bucket-chosen-at-run-time":
        return ",".join(r["runtime"])
    if r["code"] == "bucket-names-no-firm":
        return r["bucket"]
    m = re.search(r"\((no bucket literal[^;)]*|the key's own statement names several buckets, none picked: [^)]*|"
                  r"the file has \d+ bucket candidates[^)]*)", r["reason"] or "")
    return m.group(1) if m else (r["reason"] or "")


def cmd_crossfirm(map_path, out=print, key_rulings=None):
    doc = opal_naming_rootmap.load_map(map_path)
    roots = doc.get("roots") or {}
    rulings = _rulings(key_rulings)
    n = {"OK": 0, "RULED": 0, "REFUSED": 0, "UNCHECKED": 0}
    keys = 0
    table = {}
    reasons_ok = True
    for root in sorted(roots):
        for r in crossfirm_rows(root, roots[root], map_path, rulings):
            keys += 1
            n[r["verdict"]] += 1
            if r["verdict"] == "UNCHECKED":
                reasons_ok = reasons_ok and bool(r["reason"]) and r["code"] in _REASONS[:3]
                det = _detail(r)
                table.setdefault(r["code"], {})
                table[r["code"]][det] = table[r["code"]].get(det, 0) + 1
            out("%s root=%s key=%r where=%s bucket=%s bucket_firm=%s word_firm=%s code=%s reason=%s"
                % (r["verdict"], r["root"], r["current"], r["where"], r["bucket"], r["bucket_firm"], r["word_firm"],
                   r["code"], r["reason"]))
    for code in _REASONS[:3]:
        det = table.get(code, {})
        out("UNCHECKED-BY-REASON %s n=%d %s" % (code, sum(det.values()),
                                                "; ".join("%s x%d" % (d, c) for d, c in sorted(det.items()))))
    refused, ruled, unchecked, checked = n["REFUSED"], n["RULED"], n["UNCHECKED"], n["OK"]
    ok = bool(roots) and checked + ruled + unchecked + refused == keys and reasons_ok
    out("KEYFILL-CROSSFIRM ok=%s roots=%d keys=%d checked=%d ruled=%d unchecked=%d refused=%d"
        % (ok, len(roots), keys, checked, ruled, unchecked, refused))
    return 0 if ok else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    d = sub.add_parser("dir")
    d.add_argument("source_dir")
    d.add_argument("--root", required=True)
    d.add_argument("--map", required=True)
    c = sub.add_parser("crossfirm")
    c.add_argument("--map", required=True)
    a = ap.parse_args(argv)
    if a.cmd == "crossfirm":
        return cmd_crossfirm(a.map)
    return cmd_dir(a.source_dir, a.root, a.map)


if __name__ == "__main__":
    sys.exit(main())
