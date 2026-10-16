#!/usr/bin/env python
"""R27 SC-e-108 ship check (Branch 1 of the E_18 ship pair): the served E_18 and gold_dispatch.sh are the built bytes.

Read-only (boto3 get_object, us-east-1). Run from the repo root:  python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R27_CHECKS/e108_shipped_check.py
For each of the two files under s3://opal-data-bd/code/gold/: the served md5 (computed over the downloaded body) equals the md5 of the repo file at HEAD;
the served E_18 names the old list nowhere (case-insensitive `bd-securities|BD_SECURITIES_TABLE|bd_securities|default_bd_securities_lookup`: 0 lines);
the served gold_dispatch.sh passes `bash -n` and holds the three chain assignments without B_01b.
Prints `E108-SHIPPED ok=<bool> e18=<served>|<repo>|MATCH/DIFF dispatch=<served>|<repo>|MATCH/DIFF e18_old_list_lines=<n> dispatch_syntax=<rc> chain=<ok>`; exit 0 ok, 1 not ok.
"""
import hashlib
import os
import re
import subprocess
import sys
import tempfile

BUCKET = 'opal-data-bd'
FILES = {'e18': 'E_18.detect_new_securities.py', 'dispatch': 'gold_dispatch.sh'}
GOLD = 'data/black_diamond/scripts/gold/'
PAT = re.compile(r'bd-securities|BD_SECURITIES_TABLE|bd_securities|default_bd_securities_lookup', re.I)
WANT = {'CHAIN_CANONICAL': 'B_00 B_01 E_18 B_02 B_03 C_00 C_01 C_02 C_04', 'CHAIN_HOLDINGS_SEED': 'B_01', 'GROUP_B': 'B_00 B_01 B_02 B_03'}


def main():
    import boto3
    s3 = boto3.client('s3', region_name='us-east-1')
    served, repo = {}, {}
    for k, name in FILES.items():
        served[k] = s3.get_object(Bucket=BUCKET, Key='code/gold/' + name)['Body'].read()
        out = subprocess.run(['git', 'show', 'HEAD:' + GOLD + name], capture_output=True)
        repo[k] = out.stdout
    md5 = {k: (hashlib.md5(served[k]).hexdigest()[:8], hashlib.md5(repo[k]).hexdigest()[:8]) for k in FILES}
    match = {k: md5[k][0] == md5[k][1] for k in FILES}
    old_lines = sum(1 for ln in served['e18'].decode('utf-8', 'replace').splitlines() if PAT.search(ln))
    with tempfile.NamedTemporaryFile('wb', suffix='.sh', delete=False) as f:
        f.write(served['dispatch'])
        tmp = f.name
    try:
        rc = subprocess.run(['bash', '-n', tmp], capture_output=True).returncode
    finally:
        os.unlink(tmp)
    text = served['dispatch'].decode('utf-8', 'replace')
    chain_ok = all((re.search(r'^%s="([^"]*)"' % k, text, re.M) or [None, None])[1] == v for k, v in WANT.items()) \
        and not re.search(r'^\s*run_background B_01b\b', text, re.M)
    ok = all(match.values()) and old_lines == 0 and rc == 0 and chain_ok
    print('E108-SHIPPED ok=%s e18=%s|%s|%s dispatch=%s|%s|%s e18_old_list_lines=%d dispatch_syntax=%d chain=%s' % (
        ok, md5['e18'][0], md5['e18'][1], 'MATCH' if match['e18'] else 'DIFF', md5['dispatch'][0], md5['dispatch'][1],
        'MATCH' if match['dispatch'] else 'DIFF', old_lines, rc, chain_ok))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
