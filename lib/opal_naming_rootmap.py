#!/usr/bin/env python3
"""Root map reader (LGIC_BLANKFIX BF-t-3).

A Terraform root's names belong to one system, one firm and one source; a handful are genuine exceptions.
This module reads that map (a JSON file whose path is ALWAYS an argument) and answers, per (root, name,
type), which system/scope/source applies and on what basis. It never writes the registry.

  python lib/opal_naming_rootmap.py reference ROOT --map PATH
  python lib/opal_naming_rootmap.py views --map PATH

Python 3.9 syntax; ASCII only; no dependency beyond lib/opal_naming.py.
"""
import argparse
import filecmp
import json
import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import opal_naming  # noqa: E402

_ROOT_FIELDS = ("system", "scope", "source", "evidence")
_EXC_FIELDS = ("name", "type", "system", "evidence")


def _bad(root, field, why):
    return ValueError("root %r field %s: %s" % (root, field, why))


def _system_keys():
    return {s["key"] for s in opal_naming._systems(opal_naming._registry())}


def _check_system(root, field, value):
    if not isinstance(value, str) or value not in _system_keys():
        raise _bad(root, field, "%r is not a systems.json key" % (value,))


def _check_source(root, field, value):
    # the same checks opal_naming.key() makes on its source argument
    try:
        opal_naming._segment("source", value)
    except ValueError as exc:
        raise _bad(root, field, str(exc))
    if value not in _system_keys():
        raise _bad(root, field, "source %r is not a systems.json key" % (value,))


def _check_scope(root, field, value, source):
    # the same checks opal_naming.key() makes on its scope argument
    try:
        opal_naming._segment("scope", value)
        opal_naming._long_scope(opal_naming._registry(), value)
    except ValueError as exc:
        raise _bad(root, field, str(exc))
    if value == source:
        raise _bad(root, field, "a product is never a scope beneath itself (scope == source %r)" % (value,))


def load_map(path):
    """The root map at `path`, validated. ValueError names the root and the field of the first bad value."""
    with open(path, "rb") as fh:
        doc = json.loads(fh.read().decode("utf-8"))
    if not isinstance(doc, dict) or not isinstance(doc.get("roots"), dict):
        raise ValueError("root map %s: top level must be an object with a 'roots' object" % (path,))
    for root, ent in doc["roots"].items():
        if not isinstance(ent, dict):
            raise _bad(root, "(entry)", "must be an object")
        for f in _ROOT_FIELDS:
            if not isinstance(ent.get(f), str) or not ent[f].strip():
                raise _bad(root, f, "missing or not a non-empty string")
        _check_system(root, "system", ent["system"])
        _check_source(root, "source", ent["source"])
        _check_scope(root, "scope", ent["scope"], ent["source"])
        excs = ent.get("exceptions", [])
        if not isinstance(excs, list):
            raise _bad(root, "exceptions", "must be a list")
        seen = set()
        for i, ex in enumerate(excs):
            where = "exceptions[%d]" % i
            if not isinstance(ex, dict):
                raise _bad(root, where, "must be an object")
            for f in _EXC_FIELDS:
                if not isinstance(ex.get(f), str) or not ex[f].strip():
                    raise _bad(root, where + "." + f, "missing or not a non-empty string")
            _check_system(root, where + ".system", ex["system"])
            k = (ex["name"], ex["type"])
            if k in seen:
                raise _bad(root, where, "duplicate exception for %r" % (k,))
            seen.add(k)
    return doc


def resolve(map, root, name, type):
    """None when `root` has no entry; else {system, scope, source, basis}."""
    ent = (map.get("roots") or {}).get(root)
    if ent is None:
        return None
    system, basis = ent["system"], "root-default"
    for ex in ent.get("exceptions", []):
        if ex["name"] == name and ex["type"] == type:
            system, basis = ex["system"], "exception"
            break
    return {"system": system, "scope": ent["scope"], "source": ent["source"], "basis": basis}


# --------------------------------------------------------------------------- reference
def _tf_names(root_dir):
    out = []
    for fn in sorted(os.listdir(root_dir)):
        if not fn.endswith(".tf"):
            continue
        p = os.path.join(root_dir, fn)
        with open(p, "rb") as fh:
            text = fh.read().decode("utf-8")
        names, _exprs = opal_naming.census_tf_names(p.replace(os.sep, "/"), text)
        out.extend(names)
    return out


def cmd_reference(root_path, map_path, out=print):
    root = os.path.basename(os.path.normpath(root_path))
    doc = load_map(map_path)
    reg_rows = {}
    for r in opal_naming._registry()["resources"].get("resources", []):
        reg_rows.setdefault((r["name"], r["type"]), r["system"])
    rows = agree = disagree = 0
    for typ, nm, where in _tf_names(root_path):
        want = reg_rows.get((nm, typ))
        if want is None:
            continue
        rows += 1
        got = resolve(doc, root, nm, typ)
        gsys = got["system"] if got else None
        ok = gsys == want
        agree += 1 if ok else 0
        disagree += 0 if ok else 1
        out("%s %s %s row=%s map=%s basis=%s" % ("AGREE" if ok else "DISAGREE", typ, nm, want, gsys,
                                                 got["basis"] if got else "none"))
    good = disagree == 0 and rows > 0
    out("ROOTMAP-REFERENCE ok=%s root=%s rows=%d agree=%d disagree=%d" % (good, root, rows, agree, disagree))
    return 0 if good else 1


# --------------------------------------------------------------------------- views
def _generate_into(out_dir, reg_dir):
    old = opal_naming.REGISTRY_DIR
    opal_naming.REGISTRY_DIR = reg_dir
    try:
        return opal_naming.generate(out_dir)
    finally:
        opal_naming.REGISTRY_DIR = old


def cmd_views(map_path, out=print):
    load_map(map_path)
    tmp = tempfile.mkdtemp(prefix="rootmap_views_")
    try:
        base_out = os.path.join(tmp, "base")
        with_out = os.path.join(tmp, "with")
        reg_copy = os.path.join(tmp, "registry")
        shutil.copytree(opal_naming.REGISTRY_DIR, reg_copy)
        shutil.copyfile(map_path, os.path.join(reg_copy, "root_map.json"))
        base_res = _generate_into(base_out, opal_naming.REGISTRY_DIR)
        with_res = _generate_into(with_out, reg_copy)
        wrote = [r[1] for r in base_res if r[0] == "WROTE"]
        wrote_with = [r[1] for r in with_res if r[0] == "WROTE"]
        changed = 0
        for rel in sorted(set(wrote) | set(wrote_with)):
            a = os.path.join(base_out, *rel.split("/"))
            b = os.path.join(with_out, *rel.split("/"))
            same = os.path.isfile(a) and os.path.isfile(b) and filecmp.cmp(a, b, shallow=False)
            if not same:
                changed += 1
            out("%s %s" % ("SAME" if same else "CHANGED", rel))
        good = changed == 0 and len(wrote) > 0
        out("ROOTMAP-VIEWS ok=%s files=%d changed=%d" % (good, len(wrote), changed))
        return 0 if good else 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Root map reader (BF-t-3).")
    sub = ap.add_subparsers(dest="verb", required=True)
    r = sub.add_parser("reference", help="compare the map with resources.json rows for a root")
    r.add_argument("root")
    r.add_argument("--map", required=True)
    v = sub.add_parser("views", help="a map file in the registry folder moves no generated view")
    v.add_argument("--map", required=True)
    a = ap.parse_args(argv)
    try:
        if a.verb == "reference":
            return cmd_reference(a.root, a.map)
        return cmd_views(a.map)
    except (ValueError, OSError, opal_naming.RegistryError) as exc:
        print("ERROR: %s" % exc)
        print("ROOTMAP-%s ok=False error=1" % ("REFERENCE" if a.verb == "reference" else "VIEWS"))
        return 1


if __name__ == "__main__":
    sys.exit(main())
