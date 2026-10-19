#!/usr/bin/env python
"""R30 SC-e-117 ship check (READ-ONLY): the served E_18 and the served shared module are the built bytes, E_18 carries the April-table
candidacy block, the shared module writes `resolved_via`, both compile, and gold_dispatch.sh is untouched.

Run from the repo root:  python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R30_CHECKS/e117_shipped_check.py
Compares, under s3://opal-data-bd/code/gold/: the served E_18.detect_new_securities.py md5 with the built md5 (b844297d...), the served
lib/_shared/etf_classification_scheduled.py md5 with the built md5 (3adc5b1b...), the marker lines in each body, that both compile as Python, and
that gold_dispatch.sh still equals the base md5 165933f6dd0068a649f9757d9b86f303.
Prints `E117-SHIPPED ok=<bool> e18=<served>|b844297d|MATCH/DIFF shared=<served>|3adc5b1b|MATCH/DIFF block=<n> field=<n>
compiles=<bool> dispatch=<served>|165933f6|MATCH/DIFF`; exit 0 ok, 1 not ok. `selftest` runs a green arm and six negative arms.
"""
import hashlib
import sys

BUCKET = 'opal-data-bd'
E18_KEY = 'code/gold/E_18.detect_new_securities.py'
SHARED_KEY = 'code/gold/lib/_shared/etf_classification_scheduled.py'
DISPATCH_KEY = 'code/gold/gold_dispatch.sh'
BUILT_E18 = 'b844297dea8d05bddf5692c9863a44a4'
BUILT_SHARED = '3adc5b1b6b40e0e191cfbcb32e36ff63'
DISPATCH_BASE = '165933f6dd0068a649f9757d9b86f303'
BLOCK = 'Entered candidacy through the April table'
FIELD = '"resolved_via"'
NL = chr(10)


def _compiles(raw, name):
    try:
        compile(raw.decode('utf-8', 'replace'), name, 'exec')
        return True
    except SyntaxError:
        return False


def grade(e18, shared, dispatch, built_e18=None, built_shared=None, dispatch_base=None):
    be, bs, bd = built_e18 or BUILT_E18, built_shared or BUILT_SHARED, dispatch_base or DISPATCH_BASE
    me, ms, md = hashlib.md5(e18).hexdigest(), hashlib.md5(shared).hexdigest(), hashlib.md5(dispatch).hexdigest()
    block = sum(1 for ln in e18.decode('utf-8', 'replace').splitlines() if BLOCK in ln)
    field = sum(1 for ln in shared.decode('utf-8', 'replace').splitlines() if FIELD in ln)
    compiles = _compiles(e18, 'E_18') and _compiles(shared, 'shared')
    ok = me == be and ms == bs and block >= 1 and field >= 1 and compiles and md == bd
    line = 'E117-SHIPPED ok=%s e18=%s|%s|%s shared=%s|%s|%s block=%d field=%d compiles=%s dispatch=%s|165933f6|%s' % (
        ok, me[:8], be[:8], 'MATCH' if me == be else 'DIFF', ms[:8], bs[:8], 'MATCH' if ms == bs else 'DIFF',
        block, field, compiles, md[:8], 'MATCH' if md == bd else 'DIFF')
    return ok, line


def selftest():
    e = ("print('%s')" % BLOCK + NL).encode()
    s = ('_WRITE_FIELDS = ("ticker", "resolved_via")' + NL).encode()
    d = b'x'
    fe, fs, fd = hashlib.md5(e).hexdigest(), hashlib.md5(s).hexdigest(), hashlib.md5(d).hexdigest()
    green = grade(e, s, d, fe, fs, fd)[0]
    noblock = ("print('none')" + NL).encode()
    nofield = ('_WRITE_FIELDS = ("ticker",)' + NL).encode()
    broken = e + ('def (:' + NL).encode()
    neg = [
        grade(e + b'#', s, d, fe, fs, fd)[0],
        grade(e, s + b'#', d, fe, fs, fd)[0],
        grade(noblock, s, d, hashlib.md5(noblock).hexdigest(), fs, fd)[0],
        grade(e, nofield, d, fe, hashlib.md5(nofield).hexdigest(), fd)[0],
        grade(broken, s, d, hashlib.md5(broken).hexdigest(), fs, fd)[0],
        grade(e, s, b'y', fe, fs, fd)[0],
    ]
    ok = green and not any(neg)
    print('E117-SHIPPED-SELFTEST green: %s negatives refused: %d of 6' % (green, sum(1 for n in neg if not n)))
    return 0 if ok else 1


def main():
    import boto3
    s3 = boto3.client('s3', region_name='us-east-1')
    get = lambda k: s3.get_object(Bucket=BUCKET, Key=k)['Body'].read()  # noqa: E731
    ok, line = grade(get(E18_KEY), get(SHARED_KEY), get(DISPATCH_KEY))
    print(line)
    return 0 if ok else 1


if __name__ == '__main__':
    if sys.argv[1:2] == ['selftest']:
        sys.exit(selftest())
    sys.exit(main())
