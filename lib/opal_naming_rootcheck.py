#!/usr/bin/env python3
"""opal_naming_rootcheck -- one line per name of a Terraform root, every line one of six kinds (LGIC_BLANKFIX BF-t-6).

    python lib/opal_naming_rootcheck.py ROOT --map PATH [--report-only]

Kinds, decided by the first test that applies: CARDED, PATTERN, HOLE (grade() raised), RIGHT, NOT-ASKED, then a wrong
name (ALIAS or OUT-OF-PATTERN) is completed from the root map, the cadence reader and the key classifier and prints as
FIX when nothing is left blank, as HOLE when a blank cannot be filled. A hole is printed, never hidden or invented.
The five modules (scope, rootmap, cadence, keyfill, the grader) are read, never edited. Python 3.9; ASCII only.
"""
import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import opal_naming  # noqa: E402
import opal_naming_cadence  # noqa: E402
import opal_naming_keyfill  # noqa: E402
import opal_naming_rootmap  # noqa: E402
import opal_naming_scope  # noqa: E402

NOT_JUDGED = opal_naming_scope.NOT_JUDGED
KINDS = ("RIGHT", "FIX", "NOT-ASKED", "PATTERN", "CARDED", "HOLE")
_INLINE_POLICY = "an inline policy takes its role's system; the root map does not decide it"


def _schema_fourth():
    path = os.path.join(opal_naming.REPO, "org", "standards", "NAMING_SCHEMA.json")
    with open(path, "rb") as fh:
        doc = json.loads(fh.read().decode("utf-8"))
    return [v for v in doc["grade"]["verdicts"] if v not in ("CONFORMANT", "ALIAS", "OUT-OF-PATTERN")][0]


def load_cards(path=None):
    """The card list as a set of (plane, name), read from the repository's own file."""
    path = path or os.path.join(opal_naming.REPO, *NOT_JUDGED.split("/"))
    with open(path, "rb") as fh:
        rows = json.loads(fh.read().decode("utf-8"))
    return set((r.get("plane"), r.get("name")) for r in rows)


def decide(item, ans, fourth=None):
    """(kind, detail) for one item. `ans` is plain data from the five modules:
    carded (bool), key (a fill_keys row or None), graded ((verdict, canonical)) or raised (text),
    resolved (resolve()'s dict or None), cadence (the cadences() row with the same where, or None)."""
    fourth = fourth or _schema_fourth()
    cur, typ = item["current"], item["type"]
    if ans.get("carded"):
        return "CARDED", "skipped by a card the repository holds"
    key = ans.get("key")
    var = opal_naming._VAR_RE.search(cur)
    if var or (key and key.get("class") == "PATTERN"):
        what = var.group(0) if var else key.get("basis")
        return "PATTERN", "a code pattern, not a name; variable %r" % (what,)
    if ans.get("raised") is not None:
        return "HOLE", str(ans["raised"])
    verdict, canon = ans["graded"]
    if verdict == "CONFORMANT":
        return "RIGHT", cur
    if verdict == fourth:
        return "NOT-ASKED", "this kind of name is not asked to carry a system; %s" % (canon,)
    if canon is None:
        return "HOLE", "the grader gave verdict %s and no canonical form" % (verdict,)
    if key is not None:
        if key.get("class") == "LEGACY":
            return "RIGHT", "legacy store, keeps its address"
        if key.get("class") == "ADDRESS":
            canon = key["canonical"]
    form, why = canon, []
    if "{system}" in form:
        res = ans.get("resolved")
        if res is None:
            why.append("{system}: no map entry for this root")
        elif typ == "IAM_POLICY" and res.get("basis") == "root-default":
            why.append("{system}: " + _INLINE_POLICY)
        else:
            form = form.replace("{system}", res["system"])
    if "{cadence}" in form:
        cad = ans.get("cadence")
        if cad is None:
            why.append("{cadence}: no cadence row for this name")
        elif cad.get("word") is None:
            why.append("{cadence}: %s" % (cad.get("basis"),))
        else:
            form = form.replace("{cadence}", cad["word"])
    if key is not None and key.get("class") == "UNDECIDED":
        why.append("{source}/{scope}: %s" % (key.get("basis"),))
    if "{" not in form:
        return "FIX", form
    if not why:
        why.append("a blank remains that no module fills")
    return "HOLE", "partial form %s; could not fill " % (form,) + "; ".join(why)


def check_root(root, map_path, not_judged=None, out=print, report_only=False):
    root = root.replace("\\", "/").rstrip("/")
    items, _stats = opal_naming_scope.root_items(root)
    cards = load_cards() if not_judged is None else set(
        (c.get("plane"), c.get("name")) if isinstance(c, dict) else tuple(c) for c in not_judged)
    doc = opal_naming_rootmap.load_map(map_path)
    name = os.path.basename(opal_naming_scope._norm_root(root))
    entry = (doc.get("roots") or {}).get(name)
    krows = {}
    for r in opal_naming_keyfill.fill_keys(items, entry):
        krows[(r["type"], r["current"], r["where"])] = r
    cads = {}
    for r in opal_naming_cadence.cadences(root):
        cads.setdefault(r["where"], r)

    def answer_of(it):
        ans = {"carded": ("repo", it["current"]) in cards,
               "key": krows.get((it["type"], it["current"], it["where"])),
               "cadence": cads.get(it["where"]),
               "resolved": opal_naming_rootmap.resolve(doc, name, it["current"], it["type"])}
        try:
            ans["graded"] = opal_naming.grade(it["current"], it["type"])
        except opal_naming.RaiseDefect as exc:
            ans["raised"] = exc
        return ans

    return run_items(root, items, answer_of, len(opal_naming_scope.root_items(root)[0]), out, report_only)


def run_items(root, items, answer_of, expected_n, out=print, report_only=False):
    """One line per item, then the ROOTCHECK line; the return value is the exit code."""
    fourth = _schema_fourth()
    count = dict((k, 0) for k in KINDS)
    for it in items:
        kind, detail = decide(it, answer_of(it), fourth)
        count[kind] += 1
        out("%s %s %s -> %s  [%s]" % (kind, it["type"], it["current"], detail, it["where"]))
    n = len(items)
    ok = sum(count.values()) == n and n == expected_n
    out("ROOTCHECK ok=%s root=%s items=%d right=%d fix=%d not_asked=%d pattern=%d carded=%d hole=%d"
        % (ok, root, n, count["RIGHT"], count["FIX"], count["NOT-ASKED"], count["PATTERN"], count["CARDED"],
           count["HOLE"]))
    if count["HOLE"] > 0 and not report_only:
        return 1
    return 0 if ok else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("root")
    ap.add_argument("--map", required=True)
    ap.add_argument("--report-only", action="store_true")
    a = ap.parse_args(argv)
    return check_root(a.root, a.map, report_only=a.report_only)


if __name__ == "__main__":
    sys.exit(main())
