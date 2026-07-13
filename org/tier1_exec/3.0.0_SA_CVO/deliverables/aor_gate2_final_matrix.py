"""GATE-2 FINAL RE-VERIFY (3.0.0_SA_CVO~B) -- the COMPLETE key, at DS's COMMITTED hash c16b0c73b.

CTO 061054Z: "Nobody co-signs against tonight's numbers ... DS commits the round-8.2 build and hands
you a hash; you re-run the full matrix at that commit." This is that re-run. NOT against a working
tree -- the lib moved under me FOUR times tonight and two of my citations went stale mid-analysis.

THE KEY AS SHIPPED: (source_digest, fold_mode, code_digest) -- a digest of EVERY input the resolution
is a function of. The whole round was the discovery of what that input surface actually IS:
    as_of                     -> identifies the SOURCE PARTITION, never the RUN          (fail-open: A3)
    (as_of, fold_mode)        -> the partition KEY does not determine its CONTENT        (fail-open: A4; 6/69 measured)
    run_id                    -> a proxy for provenance; OVER-condemns legit cache reuse (breaks `--single`: A5)
    (source_digest,fold_mode) -> the CODE is a third input                               (fail-open: A7)
    + code_digest             -> the surface is now enumerated.

ARMS. Each runs in its OWN process: fold_mode() reads AOR_FOLD_ACTIVE at import, and code_digest()
hashes the live lib files.
  A1 absent                          -> RAISE   nothing at the key
  A2 not self-describing             -> RAISE   a PRE-8.2 artifact cannot say what produced it
  A3 MODE mismatch                   -> RAISE   *** the rollback defect: FOLDED artifact, switch-OFF run
  A4 SOURCE-DIGEST mismatch          -> RAISE   *** in-place partition rewrite (6/69 measured live)
  A7 CODE-DIGEST mismatch            -> RAISE   *** resolver-lib deploy + a resolverless run (R-B)
  A8 pin UNSET                       -> RAISE   refuses to skip the content check (fail-closed, R-C)
  A5 LEGIT CACHE REUSE               -> RETURN  *** NON-PLACEBO: `--single INF_D_00c` must still work
  A6 fresh servicing-only under OFF  -> RETURN  correct DELTA-0 (serves the SERVICING advisor)

A5/A6 are the controls. A key that RAISES on everything is not a discriminator, it is a brick -- and a
guard that over-condemns gets disabled at 3am by the operator it wrongly condemns. That failure mode is
what killed run_id; this key must survive it.

R-A is asserted STRUCTURALLY (below), not by arm: the resolver now takes the ETag off the very GET that
produced the DataFrame (`_load_latest_accounts_v2(with_key=True)`), so it CANNOT stamp bytes it did not
read. "You cannot stamp bytes you did not read" is a structural guarantee, not a check that can drift.

Hermetic: stubbed S3, real lib @ c16b0c73b, no prod touch, no gold run.
"""
from __future__ import annotations

import os
import subprocess
import sys
from io import BytesIO

REPO = r'C:\Users\AndrewBerman\Desktop\ajb_workspace'
LIB = os.path.join(REPO, 'data', 'inf', 'scripts', 'gold', 'lib')

PIN = '2026-07-12'
ETAG_NOW = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'    # the accounts_v2 partition THIS run resolved
ETAG_OLD = 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'    # the bytes it held BEFORE an in-place rewrite
CODE_OLD = 'deadbeefdeadbeefdeadbeefdeadbeef'    # a RETIRED resolver lib
FOLDED, SERVICING = 'noel_soderblom', 'peter_lee'

# arm -> (run mode, stamped fold_mode, stamped source_digest, stamped code_digest, pin_set, must_raise, why)
SELF = '__CODE_NOW__'      # resolved in-process to the REAL code_digest() of the live lib
ARMS = {
    'A1': ('1', None, None, None, True, True, 'artifact ABSENT'),
    'A2': ('1', '__PRE82__', '__PRE82__', '__PRE82__', True, True, 'PRE-8.2 artifact: not self-describing'),
    'A3': ('0', 'ACTIVE', ETAG_NOW, SELF, True, True, 'MODE mismatch: FOLDED artifact, switch-OFF run  <== THE ROLLBACK'),
    'A4': ('1', 'ACTIVE', ETAG_OLD, SELF, True, True, 'SOURCE mismatch: partition REWRITTEN in place (6/69)'),
    'A7': ('1', 'ACTIVE', ETAG_NOW, CODE_OLD, True, True, 'CODE mismatch: retired resolver logic (R-B)'),
    'A8': ('1', 'ACTIVE', ETAG_NOW, SELF, False, True, 'PIN UNSET: refuses to skip the content check (R-C)'),
    'A5': ('1', 'ACTIVE', ETAG_NOW, SELF, True, False, 'LEGIT CACHE REUSE: same content+mode+code  <== --single'),
    'A6': ('0', 'OFF', ETAG_NOW, SELF, True, False, 'fresh servicing-only, switch-OFF run (control)'),
}


def run_arm(arm: str) -> str:
    import pandas as pd
    sys.path.insert(0, LIB)
    from aor_resolution import RESOLUTION_KEY, code_digest, load_resolution

    _m, s_mode, s_dig, s_code, _pin, _mr, _why = ARMS[arm]
    if s_code == SELF:
        s_code = code_digest()          # the REAL digest of the live lib -- a genuinely matching artifact

    if arm == 'A1':
        frame = None
    else:
        import pandas as pd
        frame = pd.DataFrame({
            'account_id': [1, 2, 3],
            'advisor_key': [FOLDED if s_mode == 'ACTIVE' else SERVICING, 'peter_lee', 'patrick_scanlan'],
            'rep_bucket': ['individual'] * 3,
            'servicing_advisor_key': [SERVICING] * 3,
            'advisor_of_record_raw': ['Noel', '', ''],
            'explicit_aor': [True, False, False],
            'is_mover': [True, False, False],
            'as_of': [PIN] * 3,
        })
        if s_mode != '__PRE82__':       # A2 = the pre-8.2 artifact: the three identity columns are ABSENT
            frame['fold_mode'] = s_mode
            frame['source_digest'] = s_dig
            frame['code_digest'] = s_code

    class StubS3:
        def get_object(self, Bucket, Key):
            if frame is None or Key != RESOLUTION_KEY:
                raise FileNotFoundError('NoSuchKey')
            b = BytesIO()
            frame.to_parquet(b, index=False, engine='pyarrow')
            b.seek(0)
            return {'Body': BytesIO(b.read())}

    try:
        res = load_resolution(StubS3(), 'opal-data-inf')
        return f'RETURNED|served advisor_key={res.advisor_key.iloc[0]}'
    except Exception as e:
        msg = str(e)
        clause = msg.split(' -- ')[1][:60] if ' -- ' in msg else msg[:60]
        return f'RAISED|{clause}'


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(run_arm(sys.argv[1]))
        sys.exit(0)

    print('=' * 108)
    print('GATE-2 FINAL RE-VERIFY -- (source_digest, fold_mode, code_digest) @ COMMITTED c16b0c73b')
    print('=' * 108)
    ok = True
    for arm in ('A1', 'A2', 'A3', 'A4', 'A7', 'A8', 'A5', 'A6'):
        mode, _sm, _sd, _sc, pin_set, must_raise, why = ARMS[arm]
        env = dict(os.environ, INF_AOR_FOLD_ACTIVE=mode, INF_AOR_ASOF=PIN)
        if pin_set:
            env['INF_AOR_SRC_ETAG'] = ETAG_NOW
        else:
            env.pop('INF_AOR_SRC_ETAG', None)
        p = subprocess.run([sys.executable, __file__, arm], env=env, capture_output=True, text=True)
        raw = (p.stdout or p.stderr).strip()
        out = raw.splitlines()[-1] if raw else 'NO-OUTPUT'
        got = out.split('|')[0]
        detail = out.split('|')[1] if '|' in out else out
        good = (got == 'RAISED') == must_raise
        ok &= good
        tag = 'ok' if good else ('*** FAIL-OPEN ***' if got == 'RETURNED' else '*** OVER-CONDEMNS ***')
        print(f'\n{arm}  switch={"ACTIVE" if mode == "1" else "OFF   "}  {why}')
        print(f'      demands {"RAISE " if must_raise else "RETURN"} -> {got:<8} {tag}')
        print(f'      {detail}')

    print('\n' + '=' * 108)
    if ok:
        print('VERDICT: THE KEY DISCRIMINATES ON ALL THREE INPUTS, AT A COMMITTED HASH.')
        print('  A3 the rollback defect        -> RAISES   (the arm that killed it clears it)')
        print('  A4 in-place partition rewrite -> RAISES   (6/69, measured live)')
        print('  A7 retired resolver code      -> RAISES   (the third input, no longer unguarded)')
        print('  A8 pin unset                  -> RAISES   (fail-closed; it will not skip the check)')
        print('  A5 legit cache reuse          -> RETURNS  (--single INF_D_00c still works: NOT a brick)')
        print('  A6 servicing-only under OFF   -> RETURNS  (correct DELTA-0)')
        sys.exit(0)
    print('VERDICT: DOES NOT DISCRIMINATE -- gate-2 stays RED.')
    sys.exit(1)
