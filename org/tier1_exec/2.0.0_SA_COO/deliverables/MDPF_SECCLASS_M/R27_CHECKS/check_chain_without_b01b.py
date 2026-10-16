#!/usr/bin/env python
"""R27 SC-e-108 check: gold_dispatch.sh runs the canonical chain without B_01b.

Usage: python check_chain_without_b01b.py [path]   (run from the repo root; reads data/black_diamond/scripts/gold/gold_dispatch.sh)
Asserts: CHAIN_CANONICAL == "B_00 B_01 E_18 B_02 B_03 C_00 C_01 C_02 C_04"; CHAIN_HOLDINGS_SEED == "B_01";
GROUP_B == "B_00 B_01 B_02 B_03"; no `run_background B_01b` line remains; E_18 is still dispatched (`run_background E_18`)
and still a NONFATAL_IDS member; `bash -n` accepts the file.  The registry row `B_01b|...` may stay (the script file stays).
Prints `CHAIN-NO-B01B ok=<bool> ...`; exit 0 ok, 1 not ok.
"""
import re
import subprocess
import sys

F = sys.argv[1] if len(sys.argv) > 1 else 'data/black_diamond/scripts/gold/gold_dispatch.sh'
WANT = {'CHAIN_CANONICAL': 'B_00 B_01 E_18 B_02 B_03 C_00 C_01 C_02 C_04',
        'CHAIN_HOLDINGS_SEED': 'B_01',
        'GROUP_B': 'B_00 B_01 B_02 B_03'}


def main():
    text = open(F, encoding='utf-8').read()
    got, problems = {}, []
    for k, v in WANT.items():
        m = re.search(r'^%s="([^"]*)"' % k, text, re.M)
        got[k] = m.group(1) if m else None
        if got[k] != v:
            problems.append('%s=%r' % (k, got[k]))
    if re.search(r'^\s*run_background B_01b\b', text, re.M):
        problems.append('run_background B_01b remains')
    if not re.search(r'^\s*run_background E_18\b', text, re.M):
        problems.append('E_18 no longer dispatched')
    m = re.search(r'^NONFATAL_IDS="([^"]*)"', text, re.M)
    if not m or 'E_18' not in m.group(1).split():
        problems.append('E_18 not NONFATAL')
    r = subprocess.run(['bash', '-n', F], capture_output=True, text=True)
    if r.returncode != 0:
        problems.append('bash -n rc=%d %s' % (r.returncode, r.stderr.strip()[:120]))
    print('CHAIN-NO-B01B ok=%s problems=%s' % (not problems, problems))
    return 0 if not problems else 1


if __name__ == '__main__':
    sys.exit(main())
