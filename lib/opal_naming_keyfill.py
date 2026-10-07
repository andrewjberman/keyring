#!/usr/bin/env python3
"""Key classifier (LGIC_BLANKFIX BF-t-5).

grade() prints a storage key's canonical form with {source} and {scope} blanks when the name does not
carry them. This module classes each such row as exactly one of:

  PATTERN    the current name has a variable segment (opal_naming._VAR_RE); nothing to fill
  LEGACY     the key is a store of infra/logic/registry/legacy_addresses.json; it keeps its bytes
  ADDRESS    the root's map entry fills {source} and {scope}: a whole address
  UNDECIDED  none of the above (no root entry, a hole left, or a path that names another firm/source)

  python lib/opal_naming_keyfill.py dir SOURCE_DIR --root ROOT_NAME --map PATH

Python 3.9 syntax; ASCII only; no dependency beyond lib/opal_naming.py and lib/opal_naming_rootmap.py.
It reads the registry and never writes it.
"""
import argparse
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


def _legacy_match(name, v, entries):
    segs, prefix = _key_segments(name, v)
    if not segs or any(s == "" for s in segs):
        return None
    for key, bucket, tpl in entries:
        if opal_naming._on_list([tpl], segs, prefix):
            return key, bucket
    return None


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


def _classify(items, root_entry):
    """(rows, raising, graded): the classified rows, the count grade() raised on, the count of graded
    items that carry a {source}/{scope} blank (the rows' denominator)."""
    v = opal_naming._vocab()
    entries = _legacy_entries()
    rows, raising = [], 0
    for it in items:
        name, typ = it["current"], it["type"]
        try:
            _verdict, canon = opal_naming.grade(name, typ)
        except opal_naming.RaiseDefect:
            raising += 1
            continue
        if canon is None or not _blanks(canon):
            continue
        row = {"type": typ, "current": name, "where": it.get("where"), "class": None, "canonical": None,
               "basis": None}
        var = opal_naming._VAR_RE.search(name)
        leg = None if var else _legacy_match(name, v, entries)
        if var:
            row["class"] = "PATTERN"
            row["basis"] = "variable segment %r in the current name" % (var.group(0),)
        elif leg:
            row["class"] = "LEGACY"
            row["canonical"] = name
            row["basis"] = "legacy_addresses.json row %s (bucket %s)" % leg
        elif root_entry is None:
            row["class"] = "UNDECIDED"
            row["basis"] = "no root map entry: nothing fills the blanks %s" % ",".join(_blanks(canon))
        else:
            clash = _conflict(name, v, root_entry)
            if clash:
                row["class"] = "UNDECIDED"
                row["basis"] = "conflict: " + clash
            else:
                filled = canon
                for blank, field in (("{source}", "source"), ("{scope}", "scope")):
                    if isinstance(root_entry.get(field), str) and root_entry[field]:
                        filled = filled.replace(blank, root_entry[field])
                if "{" in filled:
                    row["class"] = "UNDECIDED"
                    row["basis"] = "a blank remains after the root entry fills source and scope: %s" % filled
                else:
                    row["class"] = "ADDRESS"
                    row["canonical"] = filled
                    row["basis"] = "root entry source=%s scope=%s" % (root_entry["source"], root_entry["scope"])
        rows.append(row)
    graded = len(rows)
    return rows, raising, graded


def fill_keys(items, root_entry):
    """One dict per item whose graded canonical carries a blank other than {system}/{cadence}:
    type, current, where, class, canonical (or None), basis. An item grade() raises on is skipped."""
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
    count = {"ADDRESS": 0, "LEGACY": 0, "PATTERN": 0, "UNDECIDED": 0}
    for r in rows:
        count[r["class"]] += 1
        out("%s %s %r canonical=%s where=%s basis=%s" % (r["class"], r["type"], r["current"], r["canonical"],
                                                         r["where"], r["basis"]))
    holes = [r for r in rows if r["class"] == "ADDRESS"
             and ("{" in r["canonical"] or "%s" in r["canonical"] or "*" in r["canonical"])]
    ind = _independent_count(sel)
    ok = (root_entry is not None and sum(count.values()) == len(rows) and len(rows) == ind and not holes
          and len(rows) > 0)
    out("KEYFILL-DIR ok=%s dir=%s rows=%d address=%d legacy=%d pattern=%d undecided=%d raising=%d"
        % (ok, prefix.rstrip("/"), len(rows), count["ADDRESS"], count["LEGACY"], count["PATTERN"],
           count["UNDECIDED"], raising))
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
