"""opal_naming_cadence -- a schedule's own expression gives its cadence word, or the row is listed with the reason.

LGIC_BLANKFIX BF-t-4 (C-CADENCE). word_for() returns a word ONLY when the expression fires on exactly that word's
period with no other restriction; everything else is (None, <plain-words basis>). cadences(root) reads every EVENT_RULE
and SCHEDULE name the naming library's census_tf_names() finds in a root's .tf files and attaches the expression read
from the SAME resource block. Python 3.9, ASCII only, stdlib plus lib/opal_naming.py (read, not edited).

    python lib/opal_naming_cadence.py root ROOT
    python lib/opal_naming_cadence.py estate
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import opal_naming  # noqa: E402

TYPES = ("EVENT_RULE", "SCHEDULE")
_TF_ROOT = "infra/aws/terraform"

_RATE_RE = re.compile(r"^rate\(\s*(\d+)\s+(minute|minutes|hour|hours|day|days)\s*\)$")
_CRON_RE = re.compile(r"^cron\(\s*([^()]*?)\s*\)$")
_INT_RE = re.compile(r"^\d+$")
_STEP5_RE = re.compile(r"^(?:\*|0)/5$")
_DOW_NAMES = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
_WEEK_ALL = {"SUN-SAT", "MON-SUN", "1-7", "*", "?"}


def _vocab_words():
    return set(opal_naming._vocab().cadences)


def _give(word, basis):
    """Return (word, basis) only when the word is in the library's vocabulary; else None with the reason."""
    if word not in _vocab_words():
        return None, "%s: the library vocabulary has no word '%s'" % (basis, word)
    return word, basis


def _rate(m, expr):
    n, unit = int(m.group(1)), m.group(2).rstrip("s")
    minutes = {"minute": 1, "hour": 60, "day": 1440}[unit] * n
    if minutes == 1:
        return _give("1min", "%s: every minute" % expr)
    if minutes == 5:
        return _give("5min", "%s: every 5 minutes" % expr)
    if minutes == 60:
        return _give("hourly", "%s: every hour" % expr)
    if minutes == 1440:
        return _give("daily", "%s: every day" % expr)
    if minutes == 10080:
        return _give("weekly", "%s: every 7 days" % expr)
    if unit == "minute":
        return None, "every %d minutes: no cadence word for this period" % n
    return None, "every %d %ss: no cadence word for this period" % (n, unit)


def _dow_single(f):
    """The one day a day-of-week field names (0-6 with SUN=1 in AWS cron numbering), else None."""
    u = f.upper()
    if u in _DOW_NAMES:
        return u
    if _INT_RE.match(u) and 1 <= int(u) <= 7:
        return _DOW_NAMES[int(u) - 1]
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
    if dom != "?" and dow != "?" and not (dom == "*" and dow == "*"):
        return None, "day-of-month and day-of-week both set: not read"
    every_dom = dom in ("*", "?")
    # minute rules first: every minute / every 5 minutes
    if hr == "*" and every_dom and dow in _WEEK_ALL:
        if mi == "*":
            return _give("1min", "%s: every minute" % expr)
        if _STEP5_RE.match(mi):
            return _give("5min", "%s: every 5 minutes" % expr)
        if _INT_RE.match(mi):
            return _give("hourly", "%s: once an hour, every hour, every day" % expr)
        return None, "minute field %s: more than once an hour or not a single minute" % mi
    if not _INT_RE.match(mi):
        return None, "minute field %s: not a single minute" % mi
    if not _INT_RE.match(hr):
        if hr == "*":
            return None, "hour is every hour but days are restricted: not read as a cadence word"
        return None, "hour field %s: more than once a day" % hr
    # a single minute and a single hour: once a day at most
    if _INT_RE.match(dom):
        if dow in ("?", "*") and mon == "*":
            return _give("monthly", "%s: once a month, day %s" % (expr, dom))
    if dom in ("*", "?") and dow in _WEEK_ALL:
        return _give("daily", "%s: once a day, every day of the week" % expr)
    if dom in ("?", "*") and _dow_single(dow):
        return _give("weekly", "%s: once a week, on %s" % (expr, _dow_single(dow)))
    if dom in ("?", "*") and re.match(r"^[A-Za-z]{3}-[A-Za-z]{3}$|^\d-\d$", dow):
        return None, "%s days only: not every day" % dow.upper()
    if dom in ("?", "*") and "," in dow:
        return None, "several days a week (%s): no cadence word" % dow.upper()
    return None, "day rule dom=%s dow=%s: no cadence word" % (dom, dow)


def word_for(expression):
    """(word or None, basis). A word only for an expression firing on exactly that word's period, no other limit."""
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


def _repo_rel(path):
    return os.path.relpath(path).replace("\\", "/")


def _tf_files(root):
    return sorted(os.path.join(root, f) for f in os.listdir(root) if f.endswith(".tf"))


def _read(path):
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read().replace("\r\n", "\n")


def cadences(root):
    """One dict per EVENT_RULE or SCHEDULE name census_tf_names() finds in the root's .tf files."""
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
            if "schedule_expression" in attrs:
                expression = opal_naming._tf_literal(attrs["schedule_expression"][3])
                if expression is None:
                    word, basis = None, "expression is not a literal"
                else:
                    word, basis = word_for(expression)
            else:
                word, basis = word_for(None)
                if has_pat:
                    basis = "no schedule expression (event pattern only)"
            rows.append({"type": typ, "current": name, "where": where, "expression": expression, "word": word,
                         "basis": basis, "has_event_pattern": has_pat})
    return rows


def _independent_count(root):
    n = 0
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


def _main(argv):
    if len(argv) >= 2 and argv[0] == "root":
        root = argv[1].rstrip("/\\")
        rows = cadences(root)
        for r in rows:
            print(_line(r))
        dec = sum(1 for r in rows if r["word"])
        und = len(rows) - dec
        ok = len(rows) == _independent_count(root) and dec + und == len(rows)
        print("CADENCE-ROOT ok=%s root=%s rows=%d decided=%d undecided=%d" % (ok, root, len(rows), dec, und))
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
    print("usage: opal_naming_cadence.py root ROOT | estate")
    return 2


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
