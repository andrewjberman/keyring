#!/usr/bin/env python
"""R26 SC-e-104 check: E_25's load_mix_summary_latest reads the REAL shape of mix_daily_summary.json.

Loads data/black_diamond/scripts/gold/E_25.aua_decomposition_audit.py by path and calls load_mix_summary_latest with a stub
S3 client that serves the committed copy of a real C_06 body (SC1's leg P body, 2,297 firm dates). No AWS call.
Prints `E25-REAL ok=<bool> ...`; exit 0 ok, 1 not ok.  Run from the repo root.
"""
import importlib.util
import io
import json
import sys

E25 = 'data/black_diamond/scripts/gold/E_25.aua_decomposition_audit.py'
BODY = 'org/tier2_senior/0.7.0_AE_CloudOps~SC1/deliverables/E102_LEGP_mix_daily_summary_BODY.json'


class _Stub:
    def __init__(self, raw):
        self._raw = raw

    def get_object(self, Bucket=None, Key=None, **kw):
        return {'Body': io.BytesIO(self._raw)}


def main():
    raw = open(BODY, 'rb').read()
    firm = json.loads(raw)['firm']
    latest = max(firm)
    spec = importlib.util.spec_from_file_location('e25_under_test', E25)
    mod = importlib.util.module_from_spec(spec)
    sys.path.insert(0, 'data/black_diamond/scripts/gold')
    spec.loader.exec_module(mod)
    res = mod.load_mix_summary_latest(_Stub(raw))
    err = res.get('error')
    classes = sorted(k for k in firm[latest] if k != 'total')
    ok = (err is None and res.get('date') == latest and abs(res.get('total', 0) - round(firm[latest]['total'], 2)) < 0.01
          and set(res.get('classes', {})) >= set(k for k in classes if firm[latest][k]))
    print('E25-REAL ok=%s error=%s date=%s want_date=%s total=%s classes_served=%s of_nonzero=%d' % (
        ok, err, res.get('date'), latest, res.get('total'), sorted(res.get('classes', {})),
        len([k for k in classes if firm[latest][k]])))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
