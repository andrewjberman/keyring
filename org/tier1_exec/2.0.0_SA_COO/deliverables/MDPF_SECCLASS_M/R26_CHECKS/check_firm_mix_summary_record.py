#!/usr/bin/env python
"""R26 SC-e-105 check: the firm_mix_summary writer-and-readers record is complete and its decision follows from its rows.

Usage: python check_firm_mix_summary_record.py <record.md>   (run from the repo root)
Record lines the check reads:
  WRITER: <repo path>:<line>          -- the line must contain `mix_summary.json`
  | <repo path>:<line> | ORDER-DEPENDENT: yes|no | <one line why> |     -- one row per reader file
  DECISION-FIRM-MIX-SUMMARY: SORT-UNDER-PAIR | NO-ORDER-DEPENDENT-READER
Census (the denominator): files tracked by git in data/ infra/ lib/ (and portal/src via `git -C portal`) whose text matches
`firm/mix_summary|mix_summary\\.json`, minus test files, markdown and the writer file. Every census file must have a row;
a row for a file outside the census is `extra`. The decision must be SORT-UNDER-PAIR iff some row says yes.
Prints `FIRMMIX-RECORD ok=<bool> ...`; exit 0 ok, 1 not ok, 3 record absent.
"""
import os
import re
import subprocess
import sys

PAT = r'firm/mix_summary|mix_summary\.json'


def _grep(cwd, paths):
    r = subprocess.run(['git', 'grep', '-l', '-I', '-E', PAT, '--'] + paths, cwd=cwd, capture_output=True, text=True)
    return r.stdout.splitlines()


def census(writer_file):
    files = set(_grep('.', ['data/', 'infra/', 'lib/']))
    if os.path.isdir('portal/src'):
        files |= {'portal/' + f for f in _grep('portal', ['src/'])}
    keep = set()
    for f in files:
        base = os.path.basename(f)
        if not f.endswith(('.py', '.ts', '.tsx', '.js', '.jsx', '.sh', '.tf', '.yaml', '.yml')):
            continue
        if '/tests/' in f or base.startswith('test_') or '/__tests__/' in f or '.test.' in base or '.spec.' in base:
            continue
        if f == writer_file:
            continue
        keep.add(f)
    return keep


def main():
    if len(sys.argv) < 2 or not os.path.isfile(sys.argv[1]):
        print('FIRMMIX-RECORD ok=False record=ABSENT')
        return 3
    text = open(sys.argv[1], encoding='utf-8').read()
    w = re.search(r'^WRITER:\s*(\S+?):(\d+)\s*$', text, re.M)
    writer_ok, writer_file = False, None
    if w:
        writer_file = w.group(1)
        try:
            line = open(writer_file, encoding='utf-8').read().splitlines()[int(w.group(2)) - 1]
            writer_ok = 'mix_summary.json' in line
        except (OSError, IndexError):
            writer_ok = False
    rows = {}
    for m in re.finditer(r'^\|\s*(\S+?):\d+\s*\|\s*ORDER-DEPENDENT:\s*(yes|no)\s*\|\s*(.+?)\s*\|\s*$', text, re.M):
        rows[m.group(1)] = m.group(2)
    cen = census(writer_file)
    missing, extra = sorted(cen - set(rows)), sorted(set(rows) - cen)
    d = re.search(r'^DECISION-FIRM-MIX-SUMMARY:\s*(SORT-UNDER-PAIR|NO-ORDER-DEPENDENT-READER)\s*$', text, re.M)
    consistent = bool(d) and ((d.group(1) == 'SORT-UNDER-PAIR') == ('yes' in rows.values()))
    ok = writer_ok and not missing and not extra and consistent and bool(cen)
    print('FIRMMIX-RECORD ok=%s writer_ok=%s census=%d rows=%d missing=%s extra=%s decision=%s consistent=%s' % (
        ok, writer_ok, len(cen), len(rows), missing, extra, d.group(1) if d else None, consistent))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
