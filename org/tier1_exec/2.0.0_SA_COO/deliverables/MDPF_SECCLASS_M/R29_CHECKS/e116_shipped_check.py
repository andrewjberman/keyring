#!/usr/bin/env python
"""R29 SC-e-116 ship check (READ-ONLY): the served E_18 is the built bytes, shows the held-out display, still names the old list nowhere, and
gold_dispatch.sh is untouched.

Run from the repo root:  python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R29_CHECKS/e116_shipped_check.py
Compares, under s3://opal-data-bd/code/gold/: the served E_18.detect_new_securities.py md5 with the md5 of the repo file at HEAD; the served body holds the
display line `Held out by the resolution table` and compiles as Python; it names the retired list nowhere; the served gold_dispatch.sh md5 equals the base
value 165933f6dd0068a649f9757d9b86f303 (unchanged by this ship).
Prints `E116-SHIPPED ok=<bool> e18=<served>|<repo>|MATCH/DIFF display=<n> compiles=<bool> old_list_lines=<n> dispatch=<served>|165933f6|MATCH/DIFF`; exit 0 ok, 1 not ok.
"""
import hashlib
import re
import subprocess
import sys

BUCKET = 'opal-data-bd'
E18 = 'E_18.detect_new_securities.py'
GOLD = 'data/black_diamond/scripts/gold/'
PAT = re.compile(r'bd-securities|BD_SECURITIES_TABLE|bd_securities|default_bd_securities_lookup', re.I)
DISPATCH_BASE = '165933f6dd0068a649f9757d9b86f303'
NL = chr(10)


def grade(served_e18, repo_e18, served_dispatch, dispatch_base=None):
    base = dispatch_base or DISPATCH_BASE
    se = hashlib.md5(served_e18).hexdigest()
    re_ = hashlib.md5(repo_e18).hexdigest()
    text = served_e18.decode('utf-8', 'replace')
    display = sum(1 for ln in text.splitlines() if 'Held out by the resolution table' in ln)
    try:
        compile(text, E18, 'exec')
        compiles = True
    except SyntaxError:
        compiles = False
    old = sum(1 for ln in text.splitlines() if PAT.search(ln))
    sd = hashlib.md5(served_dispatch).hexdigest()
    ok = se == re_ and display >= 1 and compiles and old == 0 and sd == base
    line = 'E116-SHIPPED ok=%s e18=%s|%s|%s display=%d compiles=%s old_list_lines=%d dispatch=%s|165933f6|%s' % (
        ok, se[:8], re_[:8], 'MATCH' if se == re_ else 'DIFF', display, compiles, old, sd[:8], 'MATCH' if sd == base else 'DIFF')
    return ok, line


def selftest():
    fake = hashlib.md5(b'x').hexdigest()
    good = ("print('Held out by the resolution table')" + NL).encode()
    green, _ = grade(good, good, b'x', fake)
    bad_syntax = good + ('def (:' + NL).encode()
    old_list = good + ("x = 'bd-securities'" + NL).encode()
    nodisplay = ("print('no display')" + NL).encode()
    neg = [
        grade(good, good, b'y', fake)[0],
        grade(nodisplay, nodisplay, b'x', fake)[0],
        grade(bad_syntax, bad_syntax, b'x', fake)[0],
        grade(old_list, old_list, b'x', fake)[0],
        grade(good, good + ('#' + NL).encode(), b'x', fake)[0],
    ]
    ok = green and not any(neg)
    print('E116-SHIPPED-SELFTEST green: %s negatives refused: %d of 5' % (green, sum(1 for n in neg if not n)))
    return 0 if ok else 1


def main():
    import boto3
    s3 = boto3.client('s3', region_name='us-east-1')
    se = s3.get_object(Bucket=BUCKET, Key='code/gold/' + E18)['Body'].read()
    sd = s3.get_object(Bucket=BUCKET, Key='code/gold/gold_dispatch.sh')['Body'].read()
    repo = subprocess.run(['git', 'show', 'HEAD:' + GOLD + E18], capture_output=True).stdout
    ok, line = grade(se, repo, sd)
    print(line)
    return 0 if ok else 1


if __name__ == '__main__':
    if sys.argv[1:2] == ['selftest']:
        sys.exit(selftest())
    sys.exit(main())
