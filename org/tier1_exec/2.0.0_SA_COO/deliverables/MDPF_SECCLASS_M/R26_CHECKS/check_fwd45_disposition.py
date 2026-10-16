#!/usr/bin/env python
"""R26 SC-e-103 check: the B_01b / E_18 disposition record covers every live reference to the old list.

Usage: python check_fwd45_disposition.py <record.md>   (run from the repo root)
The record must carry, as markdown table rows, one row per live line of B_01b.py and E_18.py that names the old list
(`bd-securities`, `BD_SECURITIES_TABLE`, `bd_securities`, case-insensitive): `| <file>:<line> | <class> | <replacement> |`,
class in CLASSES and a non-empty replacement; plus the three lines
  DECISION-B_01b: RETIRE-FROM-CHAIN | REPOINT-TO-ETF-CLASSIFICATIONS | OTHER:<text>
  DECISION-E_18: REPOINT-TO-ETF-CLASSIFICATIONS | OTHER:<text>
  B_02-READS-BD-SECURITIES: yes | no
Prints one line `FWD45-DISPOSITION ok=<bool> ...`; exit 0 ok, 1 not ok, 3 record absent.
"""
import os
import re
import sys

FILES = ['data/black_diamond/scripts/gold/B_01b.classify_new_securities.py',
         'data/black_diamond/scripts/gold/E_18.detect_new_securities.py']
PAT = re.compile(r'bd-securities|BD_SECURITIES_TABLE|bd_securities', re.I)
CLASSES = {'DOC', 'DEAD', 'READ-KNOWN-SET', 'READ-NAME-PREFIX', 'READ-LOOKUP', 'WRITE'}


def live():
    out = set()
    for f in FILES:
        with open(f, encoding='utf-8') as fh:
            for i, line in enumerate(fh, 1):
                if PAT.search(line):
                    out.add((os.path.basename(f).split('.')[0], i))
    return out


def main():
    if len(sys.argv) < 2 or not os.path.isfile(sys.argv[1]):
        print('FWD45-DISPOSITION ok=False record=ABSENT')
        return 3
    text = open(sys.argv[1], encoding='utf-8').read()
    rows, bad = set(), []
    for m in re.finditer(r'^\|\s*(B_01b|E_18)(?:\.[A-Za-z_.]+)?:(\d+)\s*\|\s*([A-Z-]+)\s*\|\s*(.+?)\s*\|\s*$', text, re.M):
        key = (m.group(1), int(m.group(2)))
        rows.add(key)
        if m.group(3) not in CLASSES or not m.group(4).strip('- '):
            bad.append(key)
    lv = live()
    missing, extra = sorted(lv - rows), sorted(rows - lv)
    d1 = re.search(r'^DECISION-B_01b:\s*(RETIRE-FROM-CHAIN|REPOINT-TO-ETF-CLASSIFICATIONS|OTHER:\S.*)$', text, re.M)
    d2 = re.search(r'^DECISION-E_18:\s*(REPOINT-TO-ETF-CLASSIFICATIONS|OTHER:\S.*)$', text, re.M)
    b2 = re.search(r'^B_02-READS-BD-SECURITIES:\s*(yes|no)\s*$', text, re.M)
    ok = not missing and not extra and not bad and bool(d1 and d2 and b2) and bool(lv)
    print('FWD45-DISPOSITION ok=%s live=%d rows=%d missing=%s extra=%s bad=%s decisions=%s' % (
        ok, len(lv), len(rows), missing, extra, bad, bool(d1 and d2 and b2)))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
