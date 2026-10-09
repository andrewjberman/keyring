"""opal_naming_cadence -- a schedule's own expression gives its cadence word, or the row is listed with the reason.

LGIC_BLANKFIX BF-t-4 (C-CADENCE), BF-e-1 (one reader). word_for() returns a word ONLY when the expression fires on
exactly that word's period (NAMING_SCHEMA.json v1.16 block cadence: P1 daily on five or more days of the week, P2 the
{N}min / {N}h interval form); everything else is (None, <plain-words basis>). cadences(root) reads every EVENT_RULE and
SCHEDULE name the naming library's census_tf_names() finds in a root's .tf files and attaches the expression read from
the SAME resource block. carried_word() reads the word a NAME carries with the grader's own _cadence_slot, and
verdict_for() sets the two side by side. An event rule with no schedule takes its word from the ruled rows of
infra/logic/registry/event_rules.json (P3), never from a derivation. Python 3.9, ASCII only, stdlib plus lib/opal_naming.py.

    python lib/opal_naming_cadence.py root ROOT
    python lib/opal_naming_cadence.py contradicted ROOT
    python lib/opal_naming_cadence.py estate
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import opal_naming  # noqa: E402

TYPES = ("EVENT_RULE", "SCHEDULE")
_TF_ROOT = "infra/aws/terraform"
_EVENT_RULES = os.path.join(opal_naming.REGISTRY_DIR, "event_rules.json")  # the registry lane's file (row W1-S6)

_RATE_RE = re.compile(r"^rate\(\s*(\d+)\s+(minute|minutes|hour|hours|day|days)\s*\)$")
_CRON_RE = re.compile(r"^cron\(\s*([^()]*?)\s*\)$")
_INT_RE = re.compile(r"^\d+$")
_STEP_RE = re.compile(r"^(?:\*|0)/(\d+)$")
_DOW_NAMES = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]


def _vocab_words():
    return set(opal_naming._vocab().cadences)


def _give(word, basis):
    """Return (word, basis) only when the word is in the vocabulary (`values` or the interval token form)."""
    v = opal_naming._vocab()
    if word not in v.cadences and not v.cadence_token.match(word):
        return None, "%s: the library vocabulary has no word '%s'" % (basis, word)
    return word, basis


def _interval(minutes, expr, text):
    """The word for a FIXED interval of `minutes` (P2): {N}min 1-59, hourly, {N}h for 2-23 whole hours, daily."""
    if minutes < 60:
        return _give("%dmin" % minutes, "%s: %s" % (expr, text))
    if minutes == 60:
        return _give("hourly", "%s: %s" % (expr, text))
    if minutes % 60 == 0 and minutes // 60 < 24:
        return _give("%dh" % (minutes // 60), "%s: %s" % (expr, text))
    if minutes == 1440:
        return _give("daily", "%s: %s" % (expr, text))
    if minutes == 10080:
        return _give("weekly", "%s: %s" % (expr, text))
    return None, "%s: an interval of %d minutes has no cadence word" % (expr, minutes)


def _rate(m, expr):
    n, unit = int(m.group(1)), m.group(2).rstrip("s")
    if n == 0:
        return None, "%s: a zero interval is not a period" % expr
    minutes = {"minute": 1, "hour": 60, "day": 1440}[unit] * n
    return _interval(minutes, expr, "every %d %s%s" % (n, unit, "" if n == 1 else "s"))


def _dow_days(f):
    """The set of day numbers 0-6 (SUN=0) a day-of-week field names, or None when the field is not read."""
    def one(t):
        t = t.upper()
        if t in _DOW_NAMES:
            return _DOW_NAMES.index(t)
        if _INT_RE.match(t) and 1 <= int(t) <= 7:
            return int(t) - 1
        return None
    days = set()
    for part in f.split(","):
        if "-" in part:
            a, _, b = part.partition("-")
            x, y = one(a), one(b)
            if x is None or y is None:
                return None
            k = x
            days.add(k)
            while k != y:
                k = (k + 1) % 7
                days.add(k)
        else:
            x = one(part)
            if x is None:
                return None
            days.add(x)
    return days


def _step(field, period):
    """N of a `*/N` or `0/N` field when N divides `period` evenly (a fixed interval), else None."""
    m = _STEP_RE.match(field)
    if m and int(m.group(1)) > 0 and period % int(m.group(1)) == 0:
        return int(m.group(1))
    return None


def _cron(fields, expr):
    if len(fields) != 6:
        return None, "cron has %d fields, not 6: not read" % len(fields)
    mi, hr, dom, mon, dow, yr = fields
    if yr != "*":
        return None, "year is restricted (%s): not every year" % yr
    if mon != "*":
        return None, "month is restricted (%s): not every month" % mon
    # one of day-of-month / day-of-week is '?', the other carries the day rule
    if dom not in ("?", "*") and dow not in ("?", "*"):
        return None, "day-of-month and day-of-week both set: not read"
    every_dom = dom in ("*", "?")
    days = _dow_days(dow) if dow not in ("*", "?") else set(range(7))
    all_week = days is not None and len(days) == 7
    # a fixed interval of minutes, every hour, every day of the week
    if hr == "*" and every_dom and all_week:
        if mi == "*":
            return _interval(1, expr, "every minute")
        n = _step(mi, 60)
        if n is not None:
            return _interval(n, expr, "every %d minutes" % n)
        if _INT_RE.match(mi):
            return _give("hourly", "%s: once an hour, every hour, every day" % expr)
        return None, "minute field %s: more than once an hour or not a single minute" % mi
    if not _INT_RE.match(mi):
        return None, "minute field %s: not a single minute" % mi
    if not _INT_RE.match(hr):
        n = _step(hr, 24)
        if n is not None and n >= 2 and every_dom and all_week:
            return _interval(n * 60, expr, "every %d hours" % n)
        if hr == "*":
            return None, "hour is every hour but days are restricted: not read as a cadence word"
        return None, "hour field %s: more than once a day" % hr
    # a single minute and a single hour: once a day at most
    if _INT_RE.match(dom):
        if dow in ("?", "*"):
            return _give("monthly", "%s: once a month, day %s" % (expr, dom))
    if every_dom and days is not None:
        if len(days) == 7:
            return _give("daily", "%s: once a day, every day of the week" % expr)
        if len(days) >= 5:
            return _give("daily", "%s: once a day on %d days of the week (a weekday restriction is a calendar)"
                         % (expr, len(days)))
        if len(days) == 1:
            return _give("weekly", "%s: once a week, on %s" % (expr, _DOW_NAMES[next(iter(days))]))
        return None, "%s: once a day on %d days of the week: no cadence word" % (expr, len(days))
    return None, "day rule dom=%s dow=%s: no cadence word" % (dom, dow)


def word_for(expression):
    """(word or None, basis). A word only for an expression firing on exactly that word's period."""
    if expression is None:
        return None, "no schedule expression"
    expr = expression.strip()
    m = _RATE_RE.match(expr)
    if m:
        return _rate(m, expr)
    if expr.startswith("rate("):
        return None, "rate expression not read: %s" % expr
    m = _CRON_RE.match(expr)
    if m:
        return _cron(m.group(1).split(), expr)
    if expr.startswith("at("):
        return None, "one-time at() expression: not a period"
    return None, "expression form not read: %s" % expr


def _ruled_event_rules():
    """{(name, type): row} from infra/logic/registry/event_rules.json."""
    with open(_EVENT_RULES, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    return {(r["name"], r["type"]): r for r in data.get("rules", [])}


def _event_token(canonical):
    """The on-{event} tail of a canonical name, or None when it has none."""
    toks = canonical.split("-")
    if "on" in toks[:-1]:
        return "-".join(toks[toks.index("on"):])
    return None


def carried_word(name, type):
    """The cadence word the current NAME already carries, read with the grader's own _cadence_slot; else None."""
    v = opal_naming._vocab()
    try:
        toks = opal_naming._res_tokens(name, v, "a resource name")
        if not toks:
            return None
        _sysv, out, _scope, _ph = opal_naming._slots(name, toks, type, v)
        func = [opal_naming._r3_spell(toks, i, v) for i in range(len(toks)) if i not in out]
        _f, last, blank = opal_naming._cadence_slot(func, v)
    except opal_naming.RaiseDefect:
        return None
    return None if blank else last


def verdict_for(row):
    """One cadences(root) row -> {"word", "carried", "agrees", "canonical"}; agrees is None when either is missing."""
    word = row.get("word")
    carried = carried_word(row["current"], row["type"])
    agrees = None if (word is None or carried is None) else word == carried
    ruled = _ruled_event_rules().get((row["current"], row["type"]))
    return {"word": word, "carried": carried, "agrees": agrees,
            "canonical": ruled["canonical"] if ruled else None}


def _repo_rel(path):
    return os.path.relpath(path).replace("\\", "/")


def _tf_files(root):
    return sorted(os.path.join(root, f) for f in os.listdir(root) if f.endswith(".tf"))


def _read(path):
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read().replace("\r\n", "\n")


def _walk(sc, scope, label, exprs, extra, call_anchor=None):
    """Read every EVENT_RULE / SCHEDULE resource of one scope (then its module instances) with the scope's own evaluator
    (opal_naming_scope: locals, variables and tfvars). exprs gets {resource block where: schedule_expression text} for the
    block whose expression the evaluator resolves; extra gets one tuple per name the census cannot read as a literal and
    the evaluator resolves: (type, name, where, expression or None, has event_pattern, states an expression). `where` is
    the line the scope gives the name (the same line root_names() puts on the item), so the root check finds the row."""
    for res in scope.f.resources:
        if res["type"] not in scope.attr_map:
            continue
        typ, attr = scope.attr_map[res["type"]]
        if typ not in TYPES:
            continue
        row = sc._name_expr(res, scope, attr, None)  # None when the name is one literal (the census counts it)
        anchor = call_anchor or "%s:%d" % (res["path"], res["line"])
        b = scope.bindings(res)
        if isinstance(b, sc.Unk):
            continue
        erow = res["attrs"].get("schedule_expression")
        for bk, bv in b[1]:
            env = sc._Env(scope, each=({"key": bk, "value": bv} if b[0] == "for_each" else None),
                          count=(bk if b[0] == "count" else None))
            expr = None
            if erow is not None:
                v = sc._run(erow[0], res["path"], erow[1], env)
                expr = str(v) if isinstance(v, str) else None
            if row is None:
                if call_anchor is None and expr is not None:
                    exprs.setdefault(anchor, expr)
                continue
            val = sc._run(row[0], res["path"], row[1], env)
            if isinstance(val, str) and val:
                item = (typ, str(val), sc._where_of(val, label, anchor), expr, "event_pattern" in res["attrs"], erow is not None)
                if item not in extra:
                    extra.append(item)
    for name in sorted(scope.f.modules, key=lambda n: scope.f.modules[n]["line"]):
        call = scope.module_call(name)
        if call.folder is None:
            continue
        pairs = call.pairs()
        if isinstance(pairs, sc.Unk):
            continue
        anchor = call_anchor or "%s:%d" % (call.block["path"], call.block["line"])
        for bk, bv in pairs[1]:
            _walk(sc, call.make((pairs[0], bk, bv)).scope, label, exprs, extra, anchor)


def _scoped(root):
    """(exprs, extra) of _walk over the root's folder: the names and schedule expressions that are built in locals,
    variables or modules (row W4-S3). ({}, []) when the folder cannot be read by the scope."""
    exprs, extra = {}, []
    try:
        import opal_naming_scope as sc
        folder = sc._Folder(os.path.abspath(root), _repo_rel(root))
        sc._FOLDERS.clear()
        _walk(sc, sc._Scope(folder), _repo_rel(root), exprs, extra)
    except (OSError, ValueError, KeyError, AttributeError):
        return {}, []
    return exprs, extra


def _decide_row(typ, name, where, expression, has_pat, stated, ruled):
    """One cadences row from what is known of a resource: the expression text (None when it is not a literal or
    not stated), whether an event pattern is declared, whether a schedule_expression is stated."""
    if stated:
        if expression is None:
            word, basis = None, "expression is not a literal"
        else:
            word, basis = word_for(expression)
    elif has_pat:
        row = ruled.get((name, typ))
        tok = _event_token(row["canonical"]) if row else None
        if tok is not None:
            word, basis = tok, "event rule: ruled %s (%s)" % (row["canonical"], row["evidence"])
        else:
            word, basis = None, "event rule: its on-{event} token is not ruled"
    else:
        word, basis = word_for(None)
    return {"type": typ, "current": name, "where": where, "expression": expression, "word": word,
            "basis": basis, "has_event_pattern": has_pat}


def cadences(root):
    """One dict per EVENT_RULE or SCHEDULE name census_tf_names() finds in the root's .tf files, then one per such name
    built in a local, a variable or a module that the scope's evaluator resolves to a literal (row W4-S3); an expression
    that is a variable or local the evaluator resolves is read like a literal."""
    ruled = _ruled_event_rules()
    exprs, extra = _scoped(root)
    rows = []
    for fp in _tf_files(root):
        path = _repo_rel(fp)
        text = _read(fp)
        names, _ = opal_naming.census_tf_names(path, text)
        wanted = {}
        for typ, name, where in names:
            if typ in TYPES:
                wanted[where] = (typ, name)
        if not wanted:
            continue
        blocks = {}
        for it in opal_naming._tf_items(text, 0, len(text)):
            if it[0] == "block" and it[1] == "resource" and len(it[2]) == 2:
                blocks["%s:%d" % (path, opal_naming._line_of(text, it[3]))] = it
        for where in sorted(wanted, key=lambda w: int(w.rsplit(":", 1)[1])):
            typ, name = wanted[where]
            it = blocks.get(where)
            attrs = {}
            if it is not None:
                attrs = {a[1]: a for a in opal_naming._tf_items(text, it[4], it[5]) if a[0] == "attr"}
            expression, has_pat = None, "event_pattern" in attrs
            stated = "schedule_expression" in attrs
            if stated:
                expression = opal_naming._tf_literal(attrs["schedule_expression"][3])
                if expression is None:
                    expression = exprs.get(where)  # a variable or local the scope resolves
            rows.append(_decide_row(typ, name, where, expression, has_pat, stated, ruled))
    seen = set((r["type"], r["current"], r["where"]) for r in rows)
    for typ, name, where, expression, has_pat, stated in extra:
        if (typ, name, where) not in seen:
            seen.add((typ, name, where))
            rows.append(_decide_row(typ, name, where, expression, has_pat, stated, ruled))
    return rows


def _independent_count(root):
    """The literal EVENT_RULE and SCHEDULE names of the root's .tf files, counted without cadences(), plus the names the
    scope resolves from locals, variables and modules (counted by _scoped, the scope's own evaluator)."""
    n = len(set((t, nm, w) for t, nm, w, _e, _p, _s in _scoped(root)[1]))
    for f in os.listdir(root):
        if f.endswith(".tf"):
            names, _ = opal_naming.census_tf_names("x/" + f, _read(os.path.join(root, f)))
            n += sum(1 for t, _n, _w in names if t in TYPES)
    return n


def _line(r):
    return "%s %s %s expr=%s word=%s basis=%s" % (r["where"], r["type"], r["current"],
                                                 r["expression"] if r["expression"] is not None else "-",
                                                 r["word"] if r["word"] else "NONE", r["basis"])


def _roots():
    out = []
    for r, ds, fs in os.walk(_TF_ROOT):
        ds[:] = sorted(d for d in ds if d != ".terraform")
        if any(f.endswith(".tf") for f in fs):
            out.append(r)
    return sorted(out)


def _contradicted(rows):
    out = []
    for r in rows:
        v = verdict_for(r)
        if v["agrees"] is False:
            out.append((r, v))
    return out


def _main(argv):
    if len(argv) >= 2 and argv[0] == "root":
        root = argv[1].rstrip("/\\")
        rows = cadences(root)
        for r in rows:
            print(_line(r))
        dec = sum(1 for r in rows if r["word"])
        und = len(rows) - dec
        ok = len(rows) == _independent_count(root) and dec + und == len(rows)
        print("CADENCE-ROOT ok=%s root=%s rows=%d decided=%d undecided=%d contradicted=%d"
              % (ok, root, len(rows), dec, und, len(_contradicted(rows))))
        return 0 if ok else 1
    if len(argv) >= 2 and argv[0] == "contradicted":
        root = argv[1].rstrip("/\\")
        rows = cadences(root)
        bad = _contradicted(rows)
        for r, v in bad:
            print("%s %s %s expr=%s schedule_word=%s carried=%s" % (r["where"], r["type"], r["current"],
                                                                  r["expression"], v["word"], v["carried"]))
        ok = len(rows) == _independent_count(root)
        print("CADENCE-CONTRADICTED ok=%s root=%s rows=%d contradicted=%d" % (ok, root, len(rows), len(bad)))
        return 0 if ok else 1
    if argv[:1] == ["estate"]:
        rows_n = dec = und = indep = 0
        for root in _roots():
            rows = cadences(root)
            for r in rows:
                print(_line(r))
            rows_n += len(rows)
            d = sum(1 for r in rows if r["word"])
            dec += d
            und += len(rows) - d
            indep += _independent_count(root)
        ok = rows_n == indep and dec + und == rows_n
        print("CADENCE-ESTATE ok=%s rows=%d decided=%d undecided=%d" % (ok, rows_n, dec, und))
        return 0 if ok else 1
    print("usage: opal_naming_cadence.py root ROOT | contradicted ROOT | estate")
    return 2


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
