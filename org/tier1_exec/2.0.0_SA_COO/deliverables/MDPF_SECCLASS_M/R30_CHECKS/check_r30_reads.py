#!/usr/bin/env python
"""check_r30_reads.py -- MDPF_SECCLASS round 30 read checks (2.0.0_SA_COO~M1). READ-ONLY to workers.

Usage:
    python check_r30_reads.py s53-cause     grade S53_CAUSE.json (cell SC-e-118)
    python check_r30_reads.py selftest      a green arm and a negative arm per rule

What `s53-cause` checks (all mechanical, nothing graded on prose alone):
  1. every row of `dates` carries `residue` equal to the same date's `residue` in S48_RANGE_RECON.json (within 0.01);
  2. the per-class numbers of each row sum to its residue (within 1.00);
  3. at least 3 dates are Monday to Thursday with a non-zero residue and at least 2 dates are Friday to Sunday with a
     zero residue (the weekday is computed here from the date, never read from the file);
  4. `step.file` exists in the repo, `step.line` is inside it, and `step.quote` (12 characters or more) is on that
     line or within 2 lines of it;
  5. `calendar.file` exists and holds `def <calendar.function>`;
  6. `cause_named` is true, or false with a non-empty `not_read` list; `summary` has 80 characters or more.
The class numbers are NOT recomputed from S3 by this script: the issuer recomputes one Monday date by hand at the drain.
"""
import datetime
import json
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, *(['..'] * 5)))
CAUSE = os.path.join(ROOT, 'org', 'missions', 'D8', 'MDPF', 'MDPF_SECCLASS', 'deliverables',
                     '0.9.0_WK_MDPF_SECCLASS~106', 'S53_CAUSE.json')
RECON = os.path.join(ROOT, 'org', 'missions', 'D8', 'MDPF', 'MDPF_SECCLASS', 'deliverables',
                     '0.9.0_WK_MDPF_SECCLASS~103', 'S48_RANGE_RECON.json')


def _num(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def grade_s53(doc, recon, root):
    problems = []
    rrows = {r.get('date'): r.get('residue') for r in (recon.get('rows') or [])}
    dates = doc.get('dates')
    if not isinstance(dates, list) or not dates:
        return ['dates is missing or empty']
    weekday_nonzero = 0
    other_zero = 0
    for row in dates:
        d = row.get('date')
        if d not in rrows:
            problems.append('date %r is not in S48_RANGE_RECON.json' % (d,))
            continue
        res = row.get('residue')
        if not _num(res) or abs(res - rrows[d]) > 0.01:
            problems.append('%s residue %r != recon %r' % (d, res, rrows[d]))
            continue
        classes = row.get('classes')
        if not isinstance(classes, dict) or not classes or not all(_num(v) for v in classes.values()):
            problems.append('%s classes is not a non-empty map of numbers' % d)
        elif abs(sum(classes.values()) - res) > 1.0:
            problems.append('%s classes sum %.2f != residue %.2f' % (d, sum(classes.values()), res))
        wd = datetime.date.fromisoformat(d).weekday()
        if wd <= 3 and abs(res) > 1.0:
            weekday_nonzero += 1
        if wd >= 4 and abs(res) <= 0.01:
            other_zero += 1
    if weekday_nonzero < 3:
        problems.append('fewer than 3 Monday-to-Thursday dates with a non-zero residue (%d)' % weekday_nonzero)
    if other_zero < 2:
        problems.append('fewer than 2 Friday-to-Sunday dates with a zero residue (%d)' % other_zero)
    step = doc.get('step') or {}
    sf = step.get('file')
    if not isinstance(sf, str) or not os.path.isfile(os.path.join(root, sf)):
        problems.append('step.file does not exist: %r' % (sf,))
    else:
        with open(os.path.join(root, sf), encoding='utf-8', errors='replace') as fh:
            lines = fh.read().splitlines()
        ln, q = step.get('line'), step.get('quote')
        if not isinstance(ln, int) or not 1 <= ln <= len(lines):
            problems.append('step.line %r is outside the file (%d lines)' % (ln, len(lines)))
        elif not isinstance(q, str) or len(q) < 12:
            problems.append('step.quote is under 12 characters')
        elif q not in ' '.join(lines[max(0, ln - 3):ln + 2]):
            problems.append('step.quote is not within 2 lines of step.line')
    cal = doc.get('calendar') or {}
    cf, fn = cal.get('file'), cal.get('function')
    if not isinstance(cf, str) or not os.path.isfile(os.path.join(root, cf)):
        problems.append('calendar.file does not exist: %r' % (cf,))
    else:
        with open(os.path.join(root, cf), encoding='utf-8', errors='replace') as fh:
            if not isinstance(fn, str) or ('def %s' % fn) not in fh.read():
                problems.append('calendar.function %r is not defined in %s' % (fn, cf))
    named = doc.get('cause_named')
    if named is not True and not (named is False and doc.get('not_read')):
        problems.append('cause_named must be true, or false with a non-empty not_read list')
    if not isinstance(doc.get('summary'), str) or len(doc['summary']) < 80:
        problems.append('summary is under 80 characters')
    return problems


def _good(tmp):
    os.makedirs(os.path.join(tmp, 'lib'))
    with open(os.path.join(tmp, 'lib', 'trading_calendar.py'), 'w', encoding='utf-8') as fh:
        fh.write('def expected_last_trading_day(x):\n    return x\n')
    with open(os.path.join(tmp, 'step.py'), 'w', encoding='utf-8') as fh:
        fh.write('a = 1\nb = 2\nc = 3\nd = 4\ne = 5\nf = drop_rows_where(weekday_flag == 1)\ng = 7\n')
    recon = {'rows': [{'date': '2026-10-05', 'residue': -32073.92}, {'date': '2026-10-06', 'residue': -32000.0},
                      {'date': '2026-10-07', 'residue': -31900.0}, {'date': '2026-10-09', 'residue': 0.0},
                      {'date': '2026-10-10', 'residue': 0.0}]}
    dates = [{'date': r['date'], 'residue': r['residue'], 'classes': {'cash': r['residue']}} for r in recon['rows']]
    doc = {'dates': dates, 'step': {'file': 'step.py', 'line': 6, 'quote': 'drop_rows_where(weekday_flag == 1)'},
           'calendar': {'file': 'lib/trading_calendar.py', 'function': 'expected_last_trading_day'},
           'cause_named': True, 'summary': 'x' * 90}
    return doc, recon


def selftest():
    arms = []
    with tempfile.TemporaryDirectory() as tmp:
        doc, recon = _good(tmp)
        arms.append(('green', grade_s53(doc, recon, tmp) == []))
        def neg(name, mutate):
            d, r = json.loads(json.dumps(doc)), json.loads(json.dumps(recon))
            mutate(d, r)
            arms.append((name, grade_s53(d, r, tmp) != []))
        neg('residue-off', lambda d, r: d['dates'][0].update(residue=-1.0))
        neg('classes-do-not-sum', lambda d, r: d['dates'][0]['classes'].update(cash=5.0))
        neg('quote-missing', lambda d, r: d['step'].update(quote='this text is nowhere in the file'))
        neg('line-far-from-quote', lambda d, r: d['step'].update(line=1))
        neg('function-missing', lambda d, r: d['calendar'].update(function='no_such_function'))
        neg('unnamed-without-not-read', lambda d, r: d.update(cause_named=False))
        neg('too-few-weekdays', lambda d, r: d.update(dates=d['dates'][:2] + d['dates'][3:]))
        neg('short-summary', lambda d, r: d.update(summary='short'))
    ok = all(a[1] for a in arms)
    print('R30-SELFTEST ok=%s arms=%s' % (ok, ','.join('%s:%s' % (n, 'ok' if v else 'FAIL') for n, v in arms)))
    return ok


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    if argv[1] == 'selftest':
        return 0 if selftest() else 1
    if argv[1] == 's53-cause':
        if not os.path.isfile(CAUSE):
            print('R30-s53-cause ok=False problems=%r' % (['no file at ' + CAUSE.replace(ROOT, '').lstrip(os.sep)],))
            return 1
        with open(CAUSE, encoding='utf-8') as fh:
            doc = json.load(fh)
        with open(RECON, encoding='utf-8') as fh:
            recon = json.load(fh)
        problems = grade_s53(doc, recon, ROOT)
        print('R30-s53-cause ok=%s%s' % (not problems, '' if not problems else ' problems=%r' % (problems,)))
        return 0 if not problems else 1
    print('unknown mode %s' % argv[1])
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv))
