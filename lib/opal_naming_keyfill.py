#!/usr/bin/env python3
"""Key classifier (LGIC_BLANKFIX BF-t-5).

grade() prints a storage key's canonical form with {source} and {scope} blanks when the name does not
carry them. This module classes each such row as exactly one of:

  PATTERN    the current name has a variable segment (opal_naming._VAR_RE); nothing to fill
  LEGACY     the key is a store of infra/logic/registry/legacy_addresses.json AND the key's bucket is that
             entry's bucket; it keeps its bytes (a key path alone never decides it)
  REFUSED-CROSS-FIRM  the key's bucket belongs to another firm than the root entry's scope, or its own path
             names another firm/source; it is never filled with this root's firm
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
    if isinstance(value, str) and value.startswith("s3://"):
        b = value[5:].partition("/")[0]
        if _is_bucket_literal(b, v):
            return b
    return None


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
    here = [n for n in ast.walk(tree) if isinstance(n, ast.Constant) and isinstance(n.value, str)
            and getattr(n, "lineno", 0) == line and id(n) not in docs]
    mine = [n for n in here if n.value == key] or [n for n in here if key and key in n.value]
    if mine:
        node = mine[0]
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
            return None, "the key's own statement names several buckets, none picked: %s" % ", ".join(sorted(pooled))
    seen = ""
    if mine:
        got, seen = _bucket_via_uses(tree, parent, mine[0], consts, v)
        if got is not None:
            return got, seen
        if seen.startswith("DIFFERENT"):
            return None, seen
        seen = "; " + seen if seen else ""
    if len(allb) == 1:
        b = next(iter(allb))
        return b, "the file's only bucket literal %r (line %d); the key's own statement names none" % (b, allb[b])
    if not allb:
        return None, "no bucket literal in the file and none in the key's statement"
    return None, "the file has %d bucket candidates and the key's statement picks none: %s%s" % (
        len(allb), ", ".join("%s (line %d)" % (b, n) for b, n in sorted(allb.items())), seen)


def bucket_of(item, text=None):
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


def _conflict(name, v, root_entry):
    """A token of the key's own path that names a firm or source other than the root's, else None."""
    own_scope = v.scope.get(root_entry.get("scope"), root_entry.get("scope"))
    own_names = {root_entry.get("source"), root_entry.get("system")}
    for tok in _TOKEN_RE.findall(name.lower()):
        if tok in v.scope and v.scope[tok] != own_scope:
            return "path token %r names firm %r, the root entry's scope is %r" % (tok, v.scope[tok], own_scope)
        if tok in v.v1 and tok not in own_names:
            return "path token %r names source %r, the root entry's source is %r" % (tok, tok, root_entry.get("source"))
    return None


def _item_bucket(it, name, v, text_of=None):
    """(bucket or None, basis): a bucket the key itself names wins, else bucket_of() reads the source."""
    segs0 = name.split(" ")[0].split("/")
    if segs0 and segs0[0] in v.buckets and len(segs0) > 1:
        return segs0[0], "the key names its bucket as its first segment"
    return bucket_of(it, text_of(it) if text_of else None)


def _classify(items, root_entry, text_of=None):
    """(rows, raising, graded): the classified rows, the count grade() raised on, the count of graded
    items that carry a {source}/{scope} blank (the rows' denominator). text_of(item) may stand in for the
    source file bucket_of() would read (the test's way in)."""
    v = opal_naming._vocab()
    entries = _legacy_entries()
    rows, raising = [], 0
    own_scope = None if root_entry is None else v.scope.get(root_entry.get("scope"), root_entry.get("scope"))
    # `fills` (root map): the slots the entry may fill; absent means all of them. A slot it leaves out is the key's own,
    # so the entry's HOME scope/source is neither written into a name nor used to judge the key's firm.
    fills = None if root_entry is None else root_entry.get("fills")
    can_scope = fills is None or "scope" in fills
    can_source = fills is None or "source" in fills
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
        matches = [] if var else _legacy_matches(name, v, entries)
        leg = [m for m in matches if bucket is not None and m[1] == bucket]
        bfirm = v.bucket_firm.get(bucket) if bucket else None
        clash = None if (var or root_entry is None or not (can_scope and can_source)) else _conflict(name, v, root_entry)
        not_legacy = ""
        if matches and not leg:
            not_legacy = "; not LEGACY: the path matches legacy row %s of bucket %s, this key's bucket is %s" % (
                matches[0][0], matches[0][1], bucket if bucket else "unread (%s)" % bbasis)
        if var:
            row["class"] = "PATTERN"
            row["basis"] = "variable segment %r in the current name" % (var.group(0),)
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
                    "firm" if "{scope}" in left else "source", not_legacy)
            elif "{" in filled:
                row["class"] = "UNDECIDED"
                row["basis"] = "a blank remains after the root entry fills source and scope: %s%s" % (filled, not_legacy)
            else:
                row["class"] = "ADDRESS"
                row["canonical"] = filled
                row["basis"] = "root entry source=%s scope=%s%s" % (root_entry["source"], root_entry["scope"], not_legacy)
        rows.append(row)
    graded = len(rows)
    return rows, raising, graded


def fill_keys(items, root_entry):
    """One dict per item whose graded canonical carries a blank other than {system}/{cadence}:
    type, current, where, class, canonical (or None), basis, bucket (or None), bucket_basis. An item grade()
    raises on is skipped."""
    return _classify(items, root_entry)[0]


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
    count = {"ADDRESS": 0, "LEGACY": 0, "PATTERN": 0, "REFUSED-CROSS-FIRM": 0, "UNDECIDED": 0}
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
    out("KEYFILL-DIR ok=%s dir=%s rows=%d address=%d legacy=%d pattern=%d refused=%d undecided=%d raising=%d "
        "with_bucket=%d"
        % (ok, prefix.rstrip("/"), len(rows), count["ADDRESS"], count["LEGACY"], count["PATTERN"],
           count["REFUSED-CROSS-FIRM"], count["UNDECIDED"], raising, sum(1 for r in rows if r["bucket"])))
    return 0 if ok else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    d = sub.add_parser("dir")
    d.add_argument("source_dir")
    d.add_argument("--root", required=True)
    d.add_argument("--map", required=True)
    a = ap.parse_args(argv)
    return cmd_dir(a.source_dir, a.root, a.map)


if __name__ == "__main__":
    sys.exit(main())
