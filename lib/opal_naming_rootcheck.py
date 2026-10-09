#!/usr/bin/env python3
"""opal_naming_rootcheck -- one line per name of a Terraform root, every line one of seven kinds (LGIC_BLANKFIX BF-t-6, BF-e-8).

    python lib/opal_naming_rootcheck.py ROOT --map PATH [--report-only]

    python lib/opal_naming_rootcheck.py lines ROOT --map PATH     (the run checks its own lines)

Kinds, decided by the first test that applies: PATTERN (before CARDED: a variable segment is a pattern, not a name),
a stored-file key the registry's key_rulings.json answers by (bucket, key), by a per-firm variable or by the declaring
file (declared_in), and a name its name_rulings.json answers by (name, type) (tested before the card: FIX or RIGHT on its
canonical address, NOT-ASKED when none is owed),
CARDED (a card that names a correct name, or says none is owed; a card that does neither prints HOLE), REFUSED (a key
a path word or a bucket ties to another firm: says what was measured and what the reader does; counted, never a blank,
never makes the run exit 1), HOLE (grade() raised), RIGHT, NOT-ASKED (says why, and whether a rename is owed), then a wrong name (ALIAS or OUT-OF-PATTERN) is completed from the root map, the schedule's word, the
inline policy's role and the key classifier and prints as FIX when nothing is left blank, as HOLE when a blank cannot be
filled. A name that carries a cadence word its schedule contradicts is rebuilt on the schedule's word. A hole is printed,
never hidden or invented. After every line is decided, two different current names of one type whose FIX target is one
string both become HOLE. The modules (scope, rootmap, cadence, policyrole, keyfill, the grader) are read, never edited.
Python 3.9; ASCII only.
"""
import argparse
import ast
import builtins
import io
import json
import os
import posixpath
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import opal_naming  # noqa: E402
import opal_naming_cadence  # noqa: E402
import opal_naming_keyfill  # noqa: E402
import opal_naming_policyrole  # noqa: E402
import opal_naming_rootmap  # noqa: E402
import opal_naming_scope  # noqa: E402

NOT_JUDGED = opal_naming_scope.NOT_JUDGED
KINDS = ("RIGHT", "FIX", "NOT-ASKED", "PATTERN", "CARDED", "REFUSED", "HOLE")
_CADENCE_TYPES = ("EVENT_RULE", "SCHEDULE")
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


def load_card_rows(path=None):
    """{(plane, name): [card rows]} from the repository's own card file."""
    path = path or os.path.join(opal_naming.REPO, *NOT_JUDGED.split("/"))
    with open(path, "rb") as fh:
        rows = json.loads(fh.read().decode("utf-8"))
    out = {}
    for r in rows:
        out.setdefault((r.get("plane"), r.get("name")), []).append(r)
    return out


KEY_RULINGS_FILE = "key_rulings.json"


def load_key_rulings(path=None):
    """{(bucket, key): row} from the registry's key rulings file (opal_naming.REGISTRY_DIR). Each row carries exactly one
    of `canonical` and `none_owed`, and exactly one of `bucket` and (`bucket_per` 'firm' with `bucket_from`); a row with
    both or neither, or a second row for one (bucket, key), is an error. A per-firm row is keyed ("per:" + bucket_from, key)."""
    path = path or os.path.join(opal_naming.REGISTRY_DIR, KEY_RULINGS_FILE)
    with open(path, "rb") as fh:
        doc = json.loads(fh.read().decode("utf-8"))
    out = {}
    for r in doc.get("key_rulings") or []:
        if bool(r.get("canonical")) == bool(r.get("none_owed")):
            raise ValueError("key ruling %r/%r carries not exactly one of canonical and none_owed" % (
                r.get("bucket"), r.get("key")))
        per = bool(r.get("bucket_per") or r.get("bucket_from"))
        if bool(r.get("bucket")) == per or (per and not (r.get("bucket_per") == "firm" and r.get("bucket_from"))):
            raise ValueError("key ruling %r carries not exactly one of bucket and (bucket_per 'firm' with bucket_from)" % (
                r.get("key"),))
        di = r.get("declared_in")
        if di is not None and not (isinstance(di, list) and di and all(isinstance(x, str) and x for x in di)):
            raise ValueError("key ruling %r/%r: declared_in is not a non-empty list of file paths" % (r.get("bucket"), r.get("key")))
        fl = r.get("fills")
        if fl is not None and not (isinstance(fl, dict) and all(isinstance(v, str) and v.strip() for v in fl.values())):
            raise ValueError("key ruling %r/%r: fills is not an object of plain sentences" % (r.get("bucket"), r.get("key")))
        k = ("per:" + r["bucket_from"], r.get("key")) if per else (r.get("bucket"), r.get("key"))
        if k in out:
            raise ValueError("two key rulings for %r" % (k,))
        out[k] = r
    return out


NAME_RULINGS_FILE = "name_rulings.json"


def load_name_rulings(path=None):
    """{(name, type): row} from the registry's name rulings file. Each row carries exactly one of `canonical` and
    `none_owed`; a second row for one (name, type) is an error."""
    path = path or os.path.join(opal_naming.REGISTRY_DIR, NAME_RULINGS_FILE)
    with open(path, "rb") as fh:
        doc = json.loads(fh.read().decode("utf-8"))
    out = {}
    for r in doc.get("name_rulings") or []:
        if bool(r.get("canonical")) == bool(r.get("none_owed")):
            raise ValueError("name ruling %r/%r carries not exactly one of canonical and none_owed" % (
                r.get("name"), r.get("type")))
        k = (r.get("name"), r.get("type"))
        if not k[0] or not k[1]:
            raise ValueError("name ruling %r carries no name or no type" % (r,))
        if k in out:
            raise ValueError("two name rulings for %r" % (k,))
        out[k] = r
    return out


def named_in_source(item, asked, text=None):
    """[names] of `asked` that the item's own Python source file NAMES as code: a variable, a function, an attribute
    (`directory_handler._bucket_for(...)`) or an imported name. The keyfill reader sees a variable only as a string
    constant; a per-firm row names a function the file calls, so the row's match reads the file's code as well. Docstrings,
    comments and strings do not count. [] when the file is not Python, unreadable or does not parse."""
    path, src = opal_naming_keyfill._item_text(item, text)
    if path is None or src is None or not path.endswith(".py") or not asked:
        return []
    try:
        tree = ast.parse(src)
    except (SyntaxError, ValueError):
        return []
    seen = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            seen.add(node.id)
        elif isinstance(node, ast.Attribute):
            seen.add(node.attr)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            seen.add(node.name)
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            for al in node.names:
                seen.add(al.name.split(".")[-1])
                if al.asname:
                    seen.add(al.asname)
    return sorted(a for a in asked if a in seen)


def _where_file(item):
    return str(item.get("where") or "").replace("\\", "/").rsplit(":", 1)[0]


STALE_MARK = "the ruling's declared_in names "


def _stale_note(item, row):
    """"" or the note of a STALE HINT: a declared_in row matched an item whose file is not among its declared_in paths."""
    if not row or row.get("bucket_per") or not row.get("declared_in"):
        return ""
    f = _where_file(item)
    if f in row["declared_in"]:
        return ""
    return "; %s%s; the key is declared in %s" % (STALE_MARK, ", ".join(row["declared_in"]), f)


def _ruling_of(item, rulings, bucket_reader=None, runtime_reader=None):
    """(row or None, unread reason or None) for a stored-file item. A PER-FIRM row (bucket_per, bucket_from) is matched first:
    its key equals the item's key AND the item's own source file names its bucket_from variable (opal_naming_keyfill.
    runtime_bucket). Then the rows with `declared_in` whose key equals the item's key: ONE such row matches whatever the
    file (the path is a hint; a file not among its declared_in is a STALE HINT, printed by run_items); several: the one whose
    declared_in holds the item's file, else the one holding a file of the same base name, else none and the reason. A candidate must also agree on the bucket wherever the item's bucket is known (bucket_of); a bucket not read leaves it open. Else the row matching (bucket, key) where the bucket is the one opal_naming_keyfill.bucket_of(item)
    reads. An item whose bucket is not read matches no row; the reason says the bucket is chosen at run time and names the
    variable when its file shows one, else says it was not read, but only when some row carries the item's key under a
    bucket (otherwise there is nothing the bucket would have decided)."""
    if item["type"] != "S3Key":
        return None, None
    runtime_reader = runtime_reader or opal_naming_keyfill.runtime_bucket
    asked = sorted(set(r["bucket_from"] for r in (rulings or {}).values() if r.get("bucket_from")))
    names, _rb = runtime_reader(item, None, asked)
    names = sorted(set(names) | set(named_in_source(item, asked)))
    for (_b, k), row in sorted((rulings or {}).items(), key=lambda kv: (str(kv[0][0]), str(kv[0][1]))):
        if row.get("bucket_per") and k == item["current"] and row["bucket_from"] in names:
            return row, None
    where_file = _where_file(item)
    cands = [row for (_b, k), row in sorted((rulings or {}).items(), key=lambda kv: (str(kv[0][0]), str(kv[0][1])))
             if row.get("declared_in") and k == item["current"]]
    if cands:
        # a candidate must agree on the bucket wherever the item's bucket is known; a bucket not read leaves the field open
        known, _why = (bucket_reader or opal_naming_keyfill.bucket_of)(item)
        if known is not None:
            cands = [r for r in cands if r.get("bucket") in (None, known)]
    if len(cands) == 1:
        return cands[0], None
    if cands:
        hit = [r for r in cands if where_file in r["declared_in"]]
        if not hit:
            base = posixpath.basename(where_file)
            hit = [r for r in cands if any(posixpath.basename(d) == base for d in r["declared_in"])]
        if len(hit) == 1:
            return hit[0], None
        return None, ("several key rulings carry this key and no hint names this file: %s" % (
            "; ".join("%s declared_in %s" % (r.get("bucket") or r.get("bucket_from"), ", ".join(r["declared_in"]))
                      for r in cands),))
    if not rulings:
        return None, None
    bucket, why = (bucket_reader or opal_naming_keyfill.bucket_of)(item)
    if bucket is None:
        if names:
            return None, ("the bucket is chosen at run time from %s, one bucket per firm, and the registry holds no per-firm "
                          "answer for this key and variable, so no key ruling is matched" % (", ".join(names),))
        if any(k == item["current"] for (_b, k) in rulings):
            return None, "the bucket was not read (%s), so no key ruling is matched" % (why,)
        return None, None
    return rulings.get((bucket, item["current"])), None


def _is_per_firm(row):
    return bool(row) and bool(row.get("bucket_per"))


def stray_braces(text, per_firm=False, places=()):
    """True when `text` carries a brace. A per-firm answer's {scope} is admitted, and so is each open place in `places`
    (the places a key ruling's `fills` explains)."""
    if per_firm:
        text = text.replace("{scope}", "")
    for p in places:
        text = text.replace("{%s}" % (p,), "")
    return "{" in text or "}" in text


_PLACE_RE = re.compile(r"\{([^{}]*)\}")


def admitted_places(row):
    """The open places of a key ruling's canonical that its `fills` explains: every place of the canonical has an entry in
    fills and fills names no place the canonical lacks. () for a per-firm row (unchanged), a row with no canonical, a row
    with no open place, no fills, or any mismatch."""
    if not row or _is_per_firm(row) or not row.get("canonical") or not isinstance(row.get("fills"), dict):
        return ()
    order = []
    for p in _PLACE_RE.findall(row["canonical"]):
        if p not in order:
            order.append(p)
    if not order or set(order) != set(row["fills"]):
        return ()
    return tuple(order)


def _ruling_line(item, row):
    """(kind, detail) of a stored-file item the key rulings answer: the whole canonical address, or none owed."""
    if row.get("canonical"):
        if _is_per_firm(row):
            return "FIX", ("%s (the firm's place {scope} is filled per firm: the code reads its bucket from %s, one bucket "
                           "per firm, so the firm is the one whose bucket is being served)" % (row["canonical"], row["bucket_from"]))
        if row["canonical"] == item["current"]:
            return "RIGHT", row["canonical"]
        places = admitted_places(row)
        if places:
            return "FIX", "%s (each open place is filled where the code holds it: %s)" % (
                row["canonical"], "; ".join("{%s}: %s" % (p, str(row["fills"][p]).strip().rstrip(".")) for p in places))
        return "FIX", row["canonical"]
    return "NOT-ASKED", "no name is owed for this stored file: %s; no rename is owed" % (
        str(row["none_owed"]).strip().rstrip("."),)


def _name_ruling_line(item, row):
    """(kind, detail) of a name (a bucket, a group, a secret) the name rulings answer: the whole correct name, or none owed."""
    if row.get("canonical"):
        return ("RIGHT", row["canonical"]) if row["canonical"] == item["current"] else ("FIX", row["canonical"])
    return "NOT-ASKED", "%s; no rename is owed" % (str(row["none_owed"]).strip().rstrip("."),)


def _card_for(card_rows, item):
    """The card row of this item: the one on the same where when there is one, else the first of the name."""
    rows = card_rows.get(("repo", item["current"])) or card_rows.get((item.get("plane"), item["current"])) or []
    for r in rows:
        if r.get("where") == item["where"]:
            return r
    return rows[0] if rows else None


def _kind_of_thing(typ):
    """Plain words for what a name is, for a line a reader who did not build the check must act on."""
    if typ == "S3Key":
        return "a stored-file path the check cannot read"
    return "a %s name the check cannot read" % (str(typ).lower().replace("_", " "),)


def _card_line(item, card):
    """(kind, detail) of a carded name that is not a pattern: CARDED when the card names a correct name or says none
    is owed (fields `canonical`, `no_name_owed`), else HOLE in plain words, no rule code."""
    if isinstance(card, dict):
        if card.get("canonical"):
            return "CARDED", "skipped by a card that names the correct name: %s" % (card["canonical"],)
        if card.get("no_name_owed"):
            return "CARDED", "skipped by a card; no name is owed: %s" % (str(card["no_name_owed"]).strip(),)
    return "HOLE", ("%s; it was skipped by a card; the card gives no correct name and does not say none is owed"
                    % (_kind_of_thing(item["type"]),))


_RULE_CODES = ("K1", "K3", "K4", "K4a", "V7")
_REFUSE_PATH_RE = re.compile(r"path token '([^']+)' names (firm|source) '([^']+)'")
_REFUSE_SCOPE_RE = re.compile(r"scope is (?:firm )?'([^']+)'")


def _bucket_firm(bucket):
    return opal_naming._vocab().bucket_firm.get(bucket) if bucket else None


def _refused_line(key):
    """The REFUSED detail: what was measured and what the reader does. Two cases, read from the fill_keys row
    (`bucket`, `basis`) and the registry's bucket-to-firm table: the key's bucket is another firm's, or the key's
    bucket is this root's firm's and only a path word names another firm."""
    bucket, basis = key.get("bucket"), key.get("basis") or ""
    bfirm = _bucket_firm(bucket)
    sc = _REFUSE_SCOPE_RE.search(basis)
    scope = sc.group(1) if sc else None
    path = _REFUSE_PATH_RE.search(basis)
    ask = "ask the owner of the code at the place shown"
    if bfirm is not None and scope is not None and bfirm != scope:
        return ("the key is used with bucket %s, which belongs to another firm's store (firm %s; this root's firm is %s); "
                "no rename is given: %s why this root uses it" % (bucket, bfirm, scope, ask))
    if bfirm is not None and scope is not None and bfirm == scope and path:
        other = path.group(3) if path.group(2) == "firm" else "source " + path.group(3)
        return ("a file named for %s (%s) is kept in this firm's bucket %s; no rename is given: %s whether it should "
                "run another firm's file" % (other, path.group(1), bucket, ask))
    return ("this key is tied to another firm by %s; its bucket is %s; no rename is given: %s"
            % (basis or "no reason read", bucket or "unread", ask))


def _not_asked_line(item, canon):
    """The NOT-ASKED detail: why the name is not asked for a system (the grader's own tests), then whether a rename is owed."""
    cur, typ = item["current"], item["type"]
    v = opal_naming._vocab()
    try:
        first = opal_naming._res_tokens(cur, v, "a resource name")[0]
    except (opal_naming.RaiseDefect, IndexError):
        first = None
    if first is not None and first in v.purpose:
        why = "its first word is an AWS service or action word (%s)" % (first,)
    elif typ == "IAM_POLICY" and opal_naming._PASCAL_POLICY.match(cur):
        why = "it is an inline policy name written as one capitalised word"
    elif typ == "LAMBDA_LAYER":
        why = "it is a library layer"
    else:
        why = "the grader says no system is asked and no test names the kind"
    if canon is None or canon == cur:
        owed = "no rename is owed"
    else:
        owed = "a rename is owed for the form only, not for a system: %s" % (canon,)
    return "this name is not asked to carry a system: %s; %s" % (why, owed)


def _rebuild_on_word(base, carried, word):
    """`base` with its trailing carried cadence word replaced by the schedule's word, or None when it does not end so."""
    if not base.endswith("-" + carried):
        return None
    return base[:len(base) - len(carried)] + word


def policy_system(ans):
    """(system or None, which, basis) for an inline policy whose declaration policy_roles() knows (ans["policy"]).
    The role's system wins; the root map's answer wins only when the exception names this policy's role (resolve()
    basis "exception-with-role"). An exception without a role never overrides the role. which is "exception-with-role",
    "role" or "unresolved"."""
    pol, res = ans.get("policy"), ans.get("resolved")
    if res is not None and res.get("basis") == "exception-with-role":
        return res["system"], "exception-with-role", "the exception names role %s" % (pol.get("role_name"),)
    if pol.get("role_system"):
        return pol["role_system"], "role", pol.get("basis")
    return None, "unresolved", pol.get("basis")


def decide(item, ans, fourth=None):
    """(kind, detail) for one item. `ans` is plain data from the five modules:
    carded (bool), key (a fill_keys row or None), graded ((verdict, canonical)) or raised (text),
    resolved (resolve()'s dict or None), cadence (the cadences() row with the same where, plus verdict_for()'s carried,
    agrees and canonical, or None), policy (policyrole's row of this declaration or None), card (the card row or None),
    key_ruling (the key_rulings.json row matched on (bucket, key), per firm, or declared_in, or None),
    name_ruling (the name_rulings.json row matched on (name, type) or None; tested after the key ruling, before the card), ruling_unread (why no row was matched: the bucket was not read)."""
    fourth = fourth or _schema_fourth()
    cur, typ = item["current"], item["type"]
    key = ans.get("key")
    var = opal_naming._VAR_RE.search(cur)
    if var or (key and key.get("class") == "PATTERN"):
        what = var.group(0) if var else key.get("basis")
        return "PATTERN", "a code pattern, not a name; variable %r" % (what,)
    if ans.get("key_ruling"):
        kind, detail = _ruling_line(item, ans["key_ruling"])
        if kind == "FIX" and stray_braces(detail, _is_per_firm(ans["key_ruling"]), admitted_places(ans["key_ruling"])):
            return "HOLE", "partial form %s; a brace remains that no per-firm answer admits" % (detail,)
        return kind, detail
    if ans.get("name_ruling"):
        return _name_ruling_line(item, ans["name_ruling"])
    if ans.get("carded"):
        kind, detail = _card_line(item, ans.get("card"))
        if ans.get("ruling_unread"):
            detail += "; " + ans["ruling_unread"]
        return kind, detail
    if key is not None and key.get("class") == "REFUSED-CROSS-FIRM":
        return "REFUSED", _refused_line(key)
    if ans.get("raised") is not None:
        return "HOLE", str(ans["raised"]) + ("; " + ans["ruling_unread"] if ans.get("ruling_unread") else "")
    verdict, canon = ans["graded"]
    cad = ans.get("cadence") if typ in _CADENCE_TYPES else None
    rebuilt = False
    if cad is not None:
        ruled = cad.get("canonical")
        if ruled and "{" not in ruled:
            return ("RIGHT", cur) if cur == ruled else ("FIX", ruled)
        if cad.get("agrees") is False and cad.get("word"):
            base = canon or cur
            canon = _rebuild_on_word(base, cad["carried"], cad["word"])
            if canon is None:
                return "HOLE", "the name carries %r, the schedule says %r, and %s has no such ending to rebuild" % (
                    cad["carried"], cad["word"], base)
            rebuilt = True
    if verdict == "CONFORMANT" and not rebuilt:
        return "RIGHT", cur
    if verdict == fourth:
        return "NOT-ASKED", _not_asked_line(item, canon)
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
        pol = ans.get("policy") if typ == "IAM_POLICY" else None
        fills = ans.get("fills")
        if pol is not None:
            psys, _which, pbasis = policy_system(ans)
            if psys:
                form = form.replace("{system}", psys)
            else:
                why.append("{system}: the role's system is not resolved: %s" % (pbasis,))
        elif res is None:
            why.append("{system}: no map entry for this root")
        elif typ == "IAM_POLICY" and res.get("basis") == "root-default":
            why.append("{system}: " + _INLINE_POLICY)
        elif res.get("basis") == "root-default" and fills is not None and "system" not in fills:
            why.append("{system}: this root serves more than one firm; its map entry does not give the system")
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


_TF_PREFIX = "infra/aws/terraform/"
NTN_STOP = "the map says nothing to name and the root names %d"


def map_key(root):
    """The root's map key: its folder path RELATIVE to infra/aws/terraform/ (investor-reporting/directory), whether the
    root is given with or without that prefix and with or without a trailing slash. Never its last path word."""
    r = str(root).replace("\\", "/").strip().strip("/")
    return r[len(_TF_PREFIX):] if r.startswith(_TF_PREFIX) else r


class _RootState(object):
    """What check_root and place() both read of one root: its normalised path, the registry rulings, the root's items and
    the map entry. Plain data."""


def _root_state(root, map_path, not_judged=None, key_rulings=None, name_rulings=None):
    st = _RootState()
    st.root = _TF_PREFIX + map_key(root)
    st.rulings = load_key_rulings() if key_rulings is None else key_rulings
    st.nrulings = load_name_rulings() if name_rulings is None else name_rulings
    st.items, _unc, _stats = opal_naming_scope.root_names(st.root, map_path)
    if not_judged is None:
        st.card_rows = load_card_rows()
    else:
        st.card_rows = {}
        for c in not_judged:
            c = c if isinstance(c, dict) else {"plane": c[0], "name": c[1]}
            st.card_rows.setdefault((c.get("plane"), c.get("name")), []).append(c)
    st.doc = opal_naming_rootmap.load_map(map_path)
    st.name = map_key(opal_naming_scope._norm_root(st.root))
    st.entry = (st.doc.get("roots") or {}).get(st.name)
    return st


def _answer_fn(st):
    """The per-item answers of a root (answer_of): the five modules' plain data for ONE item. check_root and place() both
    decide every item from this, so there is one assembly of the answers and one decide()."""
    root, doc, name, entry, card_rows = st.root, st.doc, st.name, st.entry, st.card_rows
    rulings, nrulings = st.rulings, st.nrulings
    krows = {}
    for r in opal_naming_keyfill.fill_keys(st.items, entry):
        krows[(r["type"], r["current"], r["where"])] = r
    cads = {}
    for r in opal_naming_cadence.cadences(root):
        cads.setdefault(r["where"], r)

    def answer_of(it):
        crow = cads.get(it["where"])
        ans = {"carded": ("repo", it["current"]) in card_rows,
               "card": _card_for(card_rows, it),
               "key": krows.get((it["type"], it["current"], it["where"])),
               "cadence": None if crow is None else dict(crow, **opal_naming_cadence.verdict_for(crow)),
               "policy": (opal_naming_policyrole.system_for(root, it["current"], it["where"])
                          if it["type"] == "IAM_POLICY" else None),
               "fills": None if entry is None else entry.get("fills"),
               "resolved": None}
        ans["key_ruling"], ans["ruling_unread"] = _ruling_of(it, rulings)
        ans["name_ruling"] = nrulings.get((it["current"], it["type"]))
        pol = ans["policy"]
        ans["resolved"] = opal_naming_rootmap.resolve(doc, name, it["current"], it["type"],
                                                      role=None if pol is None else pol.get("role_name"))
        try:
            ans["graded"] = opal_naming.grade(it["current"], it["type"])
        except opal_naming.RaiseDefect as exc:
            ans["raised"] = exc
        return ans

    return answer_of


def check_root(root, map_path, not_judged=None, out=print, report_only=False, sink=None, key_rulings=None,
               name_rulings=None):
    st = _root_state(root, map_path, not_judged, key_rulings, name_rulings)
    root, entry = st.root, st.entry
    if opal_naming_rootmap.nothing_to_name(entry):
        n = len(st.items)
        if n:
            raise ValueError(NTN_STOP % (n,))
        out("NOTHING-TO-NAME %s why=%s names=0" % (st.name, entry.get("why")))
        return 0
    answer_of = _answer_fn(st)
    if sink is not None:
        sink.append(entry)
    return run_items(root, st.items, answer_of, len(opal_naming_scope.root_names(root, map_path)[0]), out, report_only, sink)


def _collisions(decided):
    """{index: detail} for every FIX line whose target is also the FIX target of a DIFFERENT current name of the same
    type. One resource named in two files (the same current name) is not a collision."""
    groups = {}
    for i, (it, kind, detail) in enumerate(decided):
        if kind == "FIX":
            groups.setdefault((it["type"], detail), []).append(i)
    out = {}
    for (_typ, target), idx in groups.items():
        if len(set(decided[i][0]["current"] for i in idx)) < 2:
            continue
        for i in idx:
            mine = decided[i][0]["current"]
            others, seen = [], set()
            for j in idx:
                o = decided[j][0]
                if o["current"] != mine and (o["current"], o["where"]) not in seen:
                    seen.add((o["current"], o["where"]))
                    others.append("%s at %s" % (o["current"], o["where"]))
            out[i] = ("this target is also given to %s; two resources cannot take one name, and nothing here says "
                      "which keeps it; the target: %s" % (" and to ".join(others), target))
    return out


def _decide_items(items, answer_of, fourth):
    """([(item, kind, detail)], [answers]) for the items of one root: decide() on each, then the collisions. The one place
    that decides a root's lines; run_items prints them and place() reads them."""
    decided, anss = [], []
    for it in items:
        ans = answer_of(it)
        kind, detail = decide(it, ans, fourth)
        decided.append((it, kind, detail))
        anss.append(ans)
    for i, detail in _collisions(decided).items():
        decided[i] = (decided[i][0], "HOLE", detail)
    return decided, anss


def run_items(root, items, answer_of, expected_n, out=print, report_only=False, sink=None):
    """One line per item, then the ROOTCHECK line; the return value is the exit code.
    sink, when a list, receives (item, answers, kind, detail) per line, in order (the `lines` command reads it)."""
    fourth = _schema_fourth()
    count = dict((k, 0) for k in KINDS)
    decided, anss = _decide_items(items, answer_of, fourth)
    for (it, kind, detail), ans in zip(decided, anss):
        count[kind] += 1
        out("%s %s %s -> %s%s  [%s]" % (kind, it["type"], it["current"], detail, _stale_note(it, ans.get("key_ruling")),
                                         it["where"]))
        if sink is not None:
            sink.append((it, ans, kind, detail))
    n = len(items)
    ok = sum(count.values()) == n and n == expected_n
    out("ROOTCHECK ok=%s root=%s items=%d right=%d fix=%d not_asked=%d pattern=%d carded=%d refused=%d hole=%d"
        % (ok, root, n, count["RIGHT"], count["FIX"], count["NOT-ASKED"], count["PATTERN"], count["CARDED"],
           count["REFUSED"], count["HOLE"]))
    if count["HOLE"] > 0 and not report_only:
        return 1
    return 0 if ok else 1


def lines_check(root, map_path, out=print):
    """Run the root and check its own output; the last printed line is ROOTCHECK-LINES. Returns the exit code."""
    root = _TF_PREFIX + map_key(root)
    lines, sink = [], []
    check_root(root, map_path, out=lines.append, report_only=True, sink=sink)
    entry = sink[0] if sink else None
    rows = sink[1:]
    v = opal_naming._vocab()
    scope = None if not isinstance(entry, dict) else v.scope.get(entry.get("scope"), entry.get("scope"))
    bad = []
    code_re = re.compile(r"(?:%s)" % "|".join(_RULE_CODES))
    targets = {}
    for (it, _ans, kind, detail), line in zip(rows, lines):
        if code_re.search(line):
            bad.append("a rule code in: " + line)
        if kind == "NOT-ASKED" and "rename" not in line:
            bad.append("a NOT-ASKED line without 'rename': " + line)
        if kind == "FIX" and stray_braces(detail, _is_per_firm(_ans.get("key_ruling")),
                                          admitted_places(_ans.get("key_ruling"))):
            bad.append("a FIX line carries a brace: " + line)
        if kind == "FIX":
            targets.setdefault((it["type"], detail), set()).add(it["current"])
        if kind == "REFUSED" and "belongs to another firm's store" in line:
            key = _ans.get("key") or {}
            bfirm = _bucket_firm(key.get("bucket"))
            if bfirm is None or scope is None or bfirm == scope:
                bad.append("a REFUSED line says another firm's store though its bucket is not another firm's: " + line)
    coll = sum(1 for names in targets.values() if len(names) > 1)
    if coll:
        bad.append("%d FIX target(s) shared by different names of one type" % coll)
    count = dict((k, 0) for k in KINDS)
    for (_it, _a, kind, _d) in rows:
        count[kind] += 1
    if not lines or not lines[-1].startswith("ROOTCHECK ok=True "):
        bad.append("the run's own count line is not ok=True")
    if len(rows) != len(lines) - 1:
        bad.append("%d lines for %d items" % (len(lines) - 1, len(rows)))
    for line in lines:
        out(line)
    for b in bad:
        out("FAIL: " + b)
    out("ROOTCHECK-LINES ok=%s root=%s not_asked=%d carded=%d refused=%d hole=%d collisions=%d"
        % (not bad, root, count["NOT-ASKED"], count["CARDED"], count["REFUSED"], count["HOLE"], coll))
    return 0 if not bad else 1


def keys_check(root, map_path, out=print):
    """One line per inline policy of the root: the system printed, the role's system, the exception if any and which won.
    The last line is ROOTCHECK-KEYS. Returns the exit code."""
    root = _TF_PREFIX + map_key(root)
    lines, sink = [], []
    check_root(root, map_path, out=lines.append, report_only=True, sink=sink)
    by_where = {}
    for (it, ans, kind, detail) in sink[1:]:
        if it["type"] == "IAM_POLICY":
            by_where[(it["current"], it["where"])] = (ans, kind, detail)
    prows = opal_naming_policyrole.policy_roles(root)
    n = role_n = with_role = overriding = missing = 0
    for pr in prows:
        n += 1
        hit = by_where.get((pr["name"], pr["where"]))
        if hit is None:
            missing += 1
            out("MISSING %s [%s]: the root's run has no line for this policy" % (pr["name"], pr["where"]))
            continue
        ans, kind, detail = hit
        res = ans.get("resolved") or {}
        basis = res.get("basis")
        printed = None
        if kind == "FIX":
            printed = detail.split("-", 1)[0]
        elif kind == "RIGHT":
            printed = pr["name"].split("-", 1)[0]
        try:
            slot = "{system}" in (opal_naming.grade(pr["name"], "IAM_POLICY")[1] or "")
        except opal_naming.RaiseDefect:
            slot = False
        exc = "none"
        if basis in ("exception", "exception-with-role"):
            exc = "%s(%s)" % (res.get("system"), basis)
        if printed is None:
            won = "nothing-printed"
        elif basis == "exception-with-role" and printed == res.get("system"):
            won = "exception-with-role"
        elif slot and basis == "exception" and printed == res.get("system") and printed != pr.get("role_system"):
            won = "EXCEPTION-WITHOUT-ROLE-OVERRIDES"
        elif printed == pr.get("role_system"):
            won = "role"
        else:
            won = "neither"
        if won == "exception-with-role":
            with_role += 1
        elif won == "role":
            role_n += 1
        elif won == "EXCEPTION-WITHOUT-ROLE-OVERRIDES":
            overriding += 1
        out("%s %s role=%s printed=%s role_system=%s exception=%s won=%s system_slot_filled_here=%s  [%s]" % (
            kind, pr["name"], pr["role_name"], printed or "-", pr["role_system"] or "-", exc, won,
            "yes" if slot else "no", pr["where"]))
    ok = missing == 0 and overriding == 0 and n == opal_naming_policyrole.text_count(root)
    out("ROOTCHECK-KEYS ok=%s root=%s policies=%d role=%d exception_with_role=%d exception_without_role_overriding=%d"
        % (ok, root, n, role_n, with_role, overriding))
    return 0 if ok else 1


HOLE_CLASSES = ("carded", "source_bucket", "event_rule", "unknown_word", "other")
_LINE_RE = re.compile(r"^(?P<kind>[A-Z-]+) (?P<type>\S+) (?P<cur>.*?) -> (?P<detail>.*?)  \[(?P<where>[^\]]*)\]$")


def hole_class(line_type, detail):
    """The class of a HOLE line, decided here and nowhere else: `carded` (the detail says a card skipped it and gave no
    name), `source_bucket` (a bucket of a root that serves more than one firm whose firm could not be filled), `event_rule`
    (an event rule whose on-{event} token is not ruled), `unknown_word` (a word in no vocabulary, an unresolved token, or a
    first segment that is neither a source nor a tier), else `other`."""
    d = str(detail)
    t = str(line_type)
    if "skipped by a card" in d and "the card gives no correct name" in d:
        return "carded"
    if t == "S3_BUCKET" and "this root serves more than one firm" in d and "could not fill {source}/{scope}" in d:
        return "source_bucket"
    if t == "EVENT_RULE" and "token is not ruled" in d:
        return "event_rule"
    if "is in no vocabulary" in d or "is an unresolved token" in d or "is neither a source nor a tier" in d:
        return "unknown_word"
    return "other"


def _split_line(line):
    """(kind, type, current, detail, where) of a printed item line, or None."""
    m = _LINE_RE.match(line)
    return None if m is None else (m.group("kind"), m.group("type"), m.group("cur"), m.group("detail"), m.group("where"))


def all_roots(map_path, out=print, run_one=None):
    """The run over every Terraform root: the denominator first (roots, mapped, each unmapped root by name with its name
    count from the scope), then each mapped root in sorted order (its ROOTCHECK line and COMPLETED or STOPPED), then the
    totals per kind and the holes per class; the last line is ALL-ROOTS. Returns 0 when ok (whatever the holes)."""
    run_one = run_one or check_root
    all_r = list(opal_naming_scope._roots())
    doc = opal_naming_rootmap.load_map(map_path)
    keys = sorted((doc.get("roots") or {}))
    covered, problems = set(), []
    for key in keys:
        try:
            covered.add(opal_naming_scope._map_key_root(key))
        except ValueError as exc:
            problems.append("map key %s: %s" % (key, exc))
    unmapped = [r for r in all_r if r not in covered]
    out("ROOTS total=%d mapped=%d unmapped=%d" % (len(all_r), len(keys), len(unmapped)))
    uncounted_all = 0
    for r in unmapped:
        try:
            r_items, r_unc, _st = opal_naming_scope.root_names(r, map_path)
            n, u = str(len(r_items)), str(len(r_unc))
            uncounted_all += len(r_unc)
        except Exception as exc:  # an unreadable count is printed and fails the run, never dropped
            n, u = "unread", "unread"
            problems.append("unmapped root %s: name count unread: %s: %s" % (r, type(exc).__name__, exc))
        out("UNMAPPED %s names=%s uncounted=%s" % (r, n, u))
    done, stopped, tot = 0, 0, dict((k, 0) for k in KINDS)
    cls = dict((c, 0) for c in HOLE_CLASSES)
    other_lines, stale_lines, items_all = [], [], 0

    def emit_uncounted(key):
        """One UNCOUNTED line per name the mapped root builds that its own files do not resolve (BF-v-4)."""
        nonlocal uncounted_all
        try:
            unc = opal_naming_scope.root_names(opal_naming_scope._map_key_root(key), map_path)[1]
        except Exception as exc:  # an unreadable root is printed and fails the run, never dropped
            problems.append("mapped root %s: uncounted names unread: %s: %s" % (key, type(exc).__name__, exc))
            return
        uncounted_all += len(unc)
        for u in unc:
            out(opal_naming_scope.uncounted_line(u))

    for key in keys:
        ent = doc["roots"][key]
        if opal_naming_rootmap.nothing_to_name(ent):
            # a root the map says has nothing to name: mapped; read against the scope, never skipped
            try:
                n = len(opal_naming_scope.root_names(opal_naming_scope._map_key_root(key), map_path)[0])
                why = None if n == 0 else NTN_STOP % (n,)
            except Exception as exc:
                n, why = -1, "%s: %s" % (type(exc).__name__, exc)
            if why is None:
                done += 1
                out("NOTHING-TO-NAME %s why=%s names=%d" % (key, ent.get("why"), n))
            else:
                stopped += 1
                out("ROOT %s | NOTHING-TO-NAME why=%s | STOPPED %s" % (key, ent.get("why"), why))
            emit_uncounted(key)
            continue
        lines, reason = [], ""
        try:
            run_one(key, map_path, out=lines.append, report_only=True)
        except Exception as exc:  # a stopped root is counted, never dropped
            reason = "%s: %s" % (type(exc).__name__, exc)
        last = lines[-1] if lines else ""
        if not reason and not last.startswith("ROOTCHECK "):
            reason = "no ROOTCHECK last line (last printed: %r)" % (last,)
        if reason:
            stopped += 1
            out("ROOT %s | %s | STOPPED %s" % (key, last or "-", reason))
            emit_uncounted(key)
            continue
        count = dict((k, 0) for k in KINDS)
        holes = []
        for ln in lines[:-1]:
            parts = _split_line(ln)
            kind = ln.split(" ", 1)[0]
            if kind in count:
                count[kind] += 1
            if STALE_MARK in ln:
                stale_lines.append("STALE-HINT %s || %s" % (key, ln))
            if kind == "HOLE" and parts is not None:
                holes.append(parts)
            elif kind == "HOLE":
                holes.append(("HOLE", "?", "?", ln, "?"))
        fields = dict(p.split("=", 1) for p in last.split()[1:] if "=" in p)
        items = int(fields.get("items", "-1"))
        if sum(count.values()) != items:
            problems.append("%s: the counts sum to %d, the last line says items=%d" % (key, sum(count.values()), items))
        done += 1
        items_all += items
        for k in KINDS:
            tot[k] += count[k]
        for (_k, typ, cur, detail, where) in holes:
            c = hole_class(typ, detail)
            cls[c] += 1
            if c == "other":
                other_lines.append("OTHER-HOLE %s || %s %s -> %s  [%s]" % (key, typ, cur, detail, where))
        out("ROOT %s | %s | COMPLETED" % (key, last))
        emit_uncounted(key)
    out("TOTALS completed=%d stopped=%d " % (done, stopped) + " ".join(
        "%s=%d" % (k.lower().replace("-", "_"), tot[k]) for k in KINDS))
    out("HOLE-CLASSES " + " ".join("%s=%d" % (c, cls[c]) for c in HOLE_CLASSES))
    for ln in other_lines:
        out(ln)
    for ln in stale_lines:
        out(ln)
    for p in problems:
        out("FAIL: " + p)
    ok = (len(keys) + len(unmapped) == len(all_r) and done + stopped == len(keys) and not problems
          and sum(cls.values()) == tot["HOLE"])
    out("ALL-ROOTS ok=%s roots_total=%d mapped=%d unmapped=%d completed=%d stopped=%d items=%d right=%d fix=%d "
        "not_asked=%d pattern=%d carded=%d refused=%d hole=%d carded_class_holes=%d source_bucket_holes=%d "
        "event_rule_holes=%d unknown_word_holes=%d other_holes=%d stale_hints=%d uncounted=%d"
        % (ok, len(all_r), len(keys), len(unmapped), done, stopped, items_all, tot["RIGHT"], tot["FIX"],
           tot["NOT-ASKED"], tot["PATTERN"], tot["CARDED"], tot["REFUSED"], tot["HOLE"], cls["carded"],
           cls["source_bucket"], cls["event_rule"], cls["unknown_word"], cls["other"], len(stale_lines),
           uncounted_all))
    return 0 if ok else 1


# ---------------------------------------------------------------------------------------------------------------
# place() -- the creation-time question (LGIC_BLANKFIX FWD-6, round 8 BF-w-1): where would the canon put THIS name, and if
# it cannot, who owes what. It is the root check's own decision (_root_state, _answer_fn, _decide_items, decide) asked for
# one name; nothing here decides a second time. Design: FWD6_DESIGN_round6.md (decision rule, owner table).
CRO = "4.0.0_SA_CRO"
CTO = "1.0.0_SA_CTO"
CREATOR = "the creator"
DEFAULT_MAP = "infra/logic/registry/root_map.json"

# Every text decide()/_collisions()/_ruling_of() can print under a HOLE has a row: (needle, owner, what is owed). The needle
# is a literal run of the text; a %s in the owed text is the root's map key. The order matters only for the frame (see owed_for).
HOLE_OWED = (
    ("several key rulings carry this key and no hint names this fi", CRO,
     "a declared_in hint on one key-ruling row that names the file (infra/logic/registry/key_rulings.json)"),
    ("one bucket per firm, and the registry holds no per-firm answ", CRO,
     "a per-firm key-ruling row for this key and its bucket variable (infra/logic/registry/key_rulings.json)"),
    ("so no key ruling is matched", CRO,
     "a key-ruling row for this key, or a literal bucket the reader can see (infra/logic/registry/key_rulings.json)"),
    ("it was skipped by a card; the card gives no correct name and", CRO,
     "the card's canonical form or its no_name_owed line (the card is a registry ruling)"),
    ("a brace remains that no per-firm answer admits", CRO,
     "the key-ruling row's per-firm answer for the brace (infra/logic/registry/key_rulings.json)"),
    ("has no such ending to rebuild", CREATOR,
     "a name that already ends in the schedule's word, or a schedule expression that agrees with the word the name carries"),
    ("the grader gave verdict", CTO,
     "nothing you can write: the grader gave a verdict and no form, which is a rule or registry defect"),
    ("{system}: the role's system is not resolved", CRO,
     "a root-map exception that names the role (infra/logic/registry/root_map.json), or a role the policy reader can place"),
    ("{system}: no map entry for this root", CRO,
     "a root-map entry for the root %s (infra/logic/registry/root_map.json)"),
    ("{system}: an inline policy takes its role's system; the root", CREATOR,
     "declare the inline policy under a role the policy reader finds in the root, so the role's system answers"),
    ("{system}: this root serves more than one firm; its map entry", CRO,
     "the map entry's fills for the system, for the root %s (infra/logic/registry/root_map.json)"),
    ("{cadence}: no cadence row for this name", CREATOR,
     "declare the name as a literal schedule or event-rule resource the cadence reader can see"),
    ("{cadence}", CREATOR,
     "a schedule expression the cadence reader can decide (the line prints its basis), or a name that already ends in the word"),
    ("{source}/{scope}", CRO, "a key-ruling row for this key, whose class is UNDECIDED (infra/logic/registry/key_rulings.json)"),
    ("a blank remains that no module fills", CTO,
     "nothing you can write: a blank no module has a rule for, which is a rule defect"),
    ("two resources cannot take one name, and nothing here says wh", CREATOR,
     "one of the two names; nothing here says which keeps it, so agree it with the owner of the older name"),
    ("the map says nothing to name", CRO,
     "the root's map entry says it has nothing to name, and a name was added: correct the entry (infra/logic/registry/root_map.json)"),
)
_FRAME = "could not fill "
_RAISED = ("is in no vocabulary", "is an unresolved token", "is neither a source nor a tier", "token is not ruled")


def owed_for(detail, root_key="", typ=""):
    """[(owner, what is owed)] for a HOLE detail, from HOLE_OWED. A frame ("partial form X; could not fill A; B") is owed by the
    clauses it carries: only the text after the frame is matched, and the cadence row of H14 applies only when H13 did not.
    A text no row matches is the grader's own raise: a vocabulary or event_rules.json row (CRO) when it names a missing word or
    token, else a rule defect (CTO)."""
    d = str(detail)
    body = d.split(_FRAME, 1)[1] if (d.startswith("partial form ") and _FRAME in d) else d
    out, seen, got13 = [], set(), False
    for needle, owner, what in HOLE_OWED:
        if needle not in body:
            continue
        if needle == "{cadence}" and got13:
            continue
        if needle == "{cadence}: no cadence row for this name":
            got13 = True
        what = what % root_key if "%s" in what else what
        if (owner, what) not in seen:
            seen.add((owner, what))
            out.append((owner, what))
    if not out:
        if any(w in d for w in _RAISED):
            out.append((CRO, "a vocabulary row or an event_rules.json row for the word or token the grader names "
                             "(infra/logic/registry/)"))
        else:
            out.append((CTO, "nothing you can write: the grader raised this text, which is a rule or registry defect"))
    return out


# --- reading a diff's post-image and HEAD's text through the same readers ----------------------------------------------
_OPEN_MODULES = (opal_naming, opal_naming_scope, opal_naming_cadence, opal_naming_policyrole, opal_naming_keyfill)
_MISSING = object()


def _rel_of(path):
    try:
        p = os.path.relpath(os.path.abspath(str(path)), opal_naming.REPO)
    except ValueError:
        return None
    return None if p.startswith("..") else p.replace("\\", "/")


def _clear_caches():
    opal_naming_scope._CACHE.clear()
    opal_naming_scope._SCAN_CACHE.clear()
    opal_naming_scope._PARSE_CACHE.clear()
    opal_naming_policyrole._CACHE.clear()


class texts_overlay(object):
    """With this in force, every module that reads a repository file reads {repo-relative path: text} first: the post-image
    of a diff, or HEAD's text of the same files. The readers are the five modules' own `open` names, so no reader is
    re-written. Caches that hold file text are cleared on entry and on exit. A path with no entry reads the disk."""

    def __init__(self, texts):
        self.texts = dict(texts or {})
        self._saved = []

    def _open(self, path, mode="r", *a, **kw):
        rel = _rel_of(path) if isinstance(path, (str, os.PathLike)) else None
        if rel is not None and self.texts.get(rel) is not None and "w" not in mode and "a" not in mode:
            text = self.texts[rel]
            if "b" in mode:
                return io.BytesIO(text.encode("utf-8"))
            return io.StringIO(text)
        return builtins.open(path, mode, *a, **kw)

    def __enter__(self):
        for m in _OPEN_MODULES:
            self._saved.append((m, m.__dict__.get("open", _MISSING)))
            m.open = self._open
        _clear_caches()
        return self

    def __exit__(self, *exc):
        for m, old in self._saved:
            if old is _MISSING:
                del m.open
            else:
                m.open = old
        self._saved = []
        _clear_caches()
        return False


# --- the root of a path, the root of a name ---------------------------------------------------------------------------
def root_of_path(path):
    """The Terraform root a repository file belongs to (a .tf file by folder; any other file by the scope's enumeration of
    names), or None. Reads the working tree, never a diff."""
    path = str(path).replace("\\", "/")
    r = opal_naming_scope._root_of_file(path)
    if r:
        return r
    items, _stats = opal_naming_scope._census()
    for it, a in zip(items, opal_naming_scope._assignment()):
        if a and opal_naming_scope._file_of(it) == path:
            return a
    return None


def roots_of_name(name, typ=None):
    """The sorted roots whose enumerated names include `name` (of type `typ` when given)."""
    items, _stats = opal_naming_scope._census()
    out = set()
    for it, a in zip(items, opal_naming_scope._assignment()):
        if a and it["current"] == name and (typ is None or it["type"] == typ):
            out.add(a)
    return sorted(out)


# --- place() ----------------------------------------------------------------------------------------------------------
_RANK = {"HOLE": 3, "FIX": 2}


def _fill_notes(ans, canon):
    """Where each blank of the grader's form was filled from, as plain words."""
    notes = []
    res, cad = ans.get("resolved"), ans.get("cadence")
    if canon and "{system}" in canon and res is not None and res.get("system"):
        notes.append('the system "%s" is read from the root map entry (%s)' % (res["system"], res.get("basis")))
    if canon and "{cadence}" in canon and cad is not None and cad.get("word"):
        notes.append('the cadence word "%s" is read from the schedule (%s)' % (cad["word"], cad.get("basis")))
    return notes


def _result(it, ans, kind, detail, st, found):
    graded = ans.get("graded")
    canon = graded[1] if graded else None
    res = {"kind": kind, "detail": detail, "name": it["current"], "type": it["type"], "where": it["where"],
           "root": st.root, "root_key": st.name, "mapped": st.entry is not None, "found": found,
           "form": None, "fills": [], "owed": []}
    if kind == "FIX":
        res["form"] = detail.split(" (", 1)[0]
        res["fills"] = _fill_notes(ans, canon)
    elif kind == "HOLE":
        res["owed"] = owed_for(detail, st.name, it["type"])
        m = re.match(r"partial form (.*?); could not fill ", detail)
        res["form"] = m.group(1) if m else None
    return res


def _hole_rows(decided):
    return [(it["type"], it["current"], detail, it["where"]) for (it, kind, detail) in decided if kind == "HOLE"]


def _place_run(root, map_path, wants, not_judged=None, key_rulings=None, name_rulings=None):
    """(results, hole rows, state). wants: [(name, type, where or None)]. The root's items are decided once, with the wanted
    names among them; a wanted name the scope does not list is added as an item at `where` (found=False in its result)."""
    st = _root_state(root, map_path, not_judged, key_rulings, name_rulings)
    if st.entry is not None and opal_naming_rootmap.nothing_to_name(st.entry):
        res = []
        for (name, typ, where) in wants:
            r = {"kind": "HOLE", "detail": "the map says nothing to name and a name was added: %s" % (name,), "name": name,
                 "type": typ, "where": where or "?", "root": st.root, "root_key": st.name, "mapped": True, "found": False,
                 "form": None, "fills": [], "owed": []}
            r["owed"] = owed_for(r["detail"], st.name, typ)
            res.append(r)
        return res, [], st
    items = list(st.items)
    idx, found = [], []
    for (name, typ, where) in wants:
        hits = [i for i, it in enumerate(items) if it["current"] == name and (it["type"] == typ or typ is None)]
        pref = [i for i in hits if where and items[i]["where"].rsplit(":", 1)[0] == str(where).rsplit(":", 1)[0]]
        if hits:
            idx.append(pref or hits)
            found.append(True)
        else:
            items.append({"plane": "repo", "type": typ, "current": name, "where": where or "?:0"})
            idx.append([len(items) - 1])
            found.append(False)
    answer_of = _answer_fn(st)
    decided, anss = _decide_items(items, answer_of, _schema_fourth())
    results = []
    for cand, f in zip(idx, found):
        best = max(cand, key=lambda i: _RANK.get(decided[i][1], 1))
        it, kind, detail = decided[best]
        results.append(_result(it, anss[best], kind, detail, st, f))
    return results, _hole_rows(decided), st


def place_many(root, map_path, wants, texts=None):
    """place() for several names of one root with one pass of the root's decisions: [(name, type, where or None)] -> [dict]."""
    if not texts:  # no post-image to read: the disk, and the scope's caches stay as they are
        return _place_run(root, map_path, list(wants))[0]
    with texts_overlay(texts):
        results, _holes, _st = _place_run(root, map_path, list(wants))
    return results


def place(name, typ, root, map_path=DEFAULT_MAP, where=None, texts=None, not_judged=None, key_rulings=None,
          name_rulings=None):
    """Where the canon places ONE name of a root: a dict with `kind` (one of KINDS), `detail` (the root check's own text for it),
    `form` (the name to use, FIX; the partial form, HOLE), `fills` (where each blank was filled from), `owed` ([(owner, what)]
    for a HOLE), `root`, `mapped` (the map has an entry for the root) and `found` (the scope listed the name). The decision is
    decide() on the answers check_root builds, so the kind is the one the root check prints for the same line. `texts`,
    {repo-relative path: text}, makes the readers see those texts (the post-image of a diff) instead of the disk."""
    if not texts:
        return _place_run(root, map_path, [(name, typ, where)], not_judged, key_rulings, name_rulings)[0][0]
    with texts_overlay(texts):
        results, _holes, _st = _place_run(root, map_path, [(name, typ, where)], not_judged, key_rulings, name_rulings)
    return results[0]


def refusal_text(res):
    """(form for the arrow, why text) of a name place() says is FIX or HOLE: what is owed and to whom."""
    if res["kind"] == "FIX":
        fills = ("; " + "; ".join(res["fills"])) if res["fills"] else ""
        return res["form"], ("NEW name the canon places as FIX. Owed: use %s%s. Build it with name() or edit the literal; "
                             "nothing else is owed." % (res["form"], fills))
    parts = ["%s -- from %s" % (what, owner) for owner, what in res["owed"]]
    return (res["form"] or "-"), (
        "NEW name the canon cannot place (HOLE): %s. Owed: %s. The name is placeable the moment that is done; the creator "
        "does not write the registry, so for a registry row hand its owner this line." % (res["detail"], "; ".join(parts)))


def place_root(root, map_path, wants, post_texts, head_texts, ratchet=True):
    """One root of a diff: the placement of each wanted name on the post-image, and the hole ratchet (post-image against
    HEAD, both run now). Returns {"results", "mapped", "root", "post_holes", "head_holes" (None when not ratcheted),
    "new_holes", "names_post", "names_head"}. An unmapped root is not ratcheted (the HOLEs it prints are largely its absent
    map entry); its name counts are returned for a notice."""
    with texts_overlay(post_texts):
        results, post_rows, st = _place_run(root, map_path, wants)
        names_post = len(st.items)
    out = {"results": results, "mapped": st.entry is not None, "root": st.root, "post_holes": len(post_rows),
           "head_holes": None, "new_holes": [], "names_post": names_post, "names_head": None}
    if not ratchet:
        return out
    with texts_overlay(head_texts):
        if st.entry is None:
            out["names_head"] = len(opal_naming_scope.root_names(st.root, map_path)[0])
        elif not opal_naming_rootmap.nothing_to_name(st.entry):
            _r, head_rows, _st2 = _place_run(root, map_path, [])
            out["head_holes"] = len(head_rows)
            have = {}
            for t, c, d, w in head_rows:
                have[(t, c, d)] = have.get((t, c, d), 0) + 1
            for t, c, d, w in post_rows:
                if have.get((t, c, d), 0) > 0:
                    have[(t, c, d)] -= 1
                else:
                    out["new_holes"].append((t, c, d, w))
    return out


def ratchet_text(root_res):
    """The refusal text of a root whose HOLE count grew: the new HOLE lines, each with what is owed and to whom."""
    lines = []
    for t, c, d, w in root_res["new_holes"]:
        owed = "; ".join("%s -- from %s" % (what, owner) for owner, what in owed_for(d, map_key(root_res["root"]), t))
        lines.append("HOLE %s %s -> %s [%s] Owed: %s" % (t, c, d, w, owed))
    return ("the unplaceable-name list grew in %s: %d HOLE line(s) now, %d at HEAD. New: %s"
            % (root_res["root"], root_res["post_holes"], root_res["head_holes"], " || ".join(lines) or "(same text moved)"))


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv and argv[0] == "keys":
        kp = argparse.ArgumentParser(description="the inline policies of a root and which system won")
        kp.add_argument("cmd")
        kp.add_argument("root")
        kp.add_argument("--map", required=True)
        ka = kp.parse_args(argv)
        return keys_check(ka.root, ka.map)
    if argv and argv[0] == "all":
        pp = argparse.ArgumentParser(description="the run over every Terraform root, denominator first")
        pp.add_argument("cmd")
        pp.add_argument("--map", required=True)
        pa = pp.parse_args(argv)
        return all_roots(pa.map)
    if argv and argv[0] == "lines":
        lp = argparse.ArgumentParser(description="run a root and check its own lines")
        lp.add_argument("cmd")
        lp.add_argument("root")
        lp.add_argument("--map", required=True)
        la = lp.parse_args(argv)
        return lines_check(la.root, la.map)
    ap =argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("root")
    ap.add_argument("--map", required=True)
    ap.add_argument("--report-only", action="store_true")
    a = ap.parse_args(argv)
    return check_root(a.root, a.map, report_only=a.report_only)


if __name__ == "__main__":
    sys.exit(main())
