"""GATE-2 RE-VERIFY (3.0.0_SA_CVO~B) -- does the round-8.2 (source_digest, fold_mode) key DISCRIMINATE?

THE ARM THAT KILLED IT IS THE ARM THAT CLEARS IT (base CTO, 054842Z). Same fixture, same
partition, resolver skipped -- and now it must RAISE.

This verifies the SHIPPED key against every state in the truth table its own docstring claims,
PLUS the two states that killed the previous three keys:
    A3  MODE mismatch     -- the defect I found (folded artifact consumed by a switch-OFF run)
    A4  DIGEST mismatch   -- the 6/69 in-place partition rewrite that killed (as_of, fold_mode)
and, critically, the state that would make this a CONDEMNATION INSTRUMENT if it fired:
    A5  LEGIT CACHE REUSE -- same content, same mode, resolver skipped. MUST RETURN.
        If A5 raises, `--single INF_D_00c` (the dispatch's OWN documented example, :18/:1205)
        hard-aborts, an operator hits it at 3am and reaches for the switch. A guard that
        over-condemns gets disabled by whoever it condemns.

A5 is the non-placebo control: a key that RAISES on everything is not a discriminator, it is a
brick. Run each arm in its own process -- fold_mode() reads AOR_FOLD_ACTIVE at import time.

Hermetic: stubbed S3 (get_object + head_object), real lib, no prod touch, no gold run.
usage: python aor_r182_key_verify.py <arm>     (driven by the __main__ loop below)
"""
from __future__ import annotations

import os
import subprocess
import sys
from io import BytesIO

REPO = r'C:\Users\AndrewBerman\Desktop\ajb_workspace'
LIB = os.path.join(REPO, 'data', 'inf', 'scripts', 'gold', 'lib')

# =================================================================================================
# >> SUPERSEDED -- AND IT WAS EMITTING A CONFIDENT FALSE *RED*, IN MY OWN VOICE. <<
# (3.0.0_SA_CVO~B, 2026-07-13. Self-caught while re-running the battery at HEAD.)
#
# This arm verifies the TWO-input key `(source_digest, fold_mode)`. Its fixtures stamp exactly those
# two fields (:68-69). The key that SHIPPED grew a THIRD axis -- `code_digest` (R-B: the CODE is an
# input too) -- so the chokepoint's third assertion legitimately RAISES on every one of this arm's
# unstamped fixtures. A5 and A6 (which demand RETURN) therefore came back RAISED, and this script
# concluded, at exit 1:
#
#       "VERDICT: DOES NOT DISCRIMINATE -- gate-2 stays RED. Do not ship this key."
#
# THAT VERDICT IS FALSE. The shipped 3-input key does NOT over-condemn: `aor_gate2_final_matrix.py`
# runs the SAME semantic arms with fixtures that stamp all THREE axes, and A5 (legit cache reuse)
# RETURNS. Two arms, one question, different fixture completeness -- and the one whose fixture matches
# the shipped key is the one that is right.
#
# THE LESSON, AND IT IS THE C_07 LESSON TURNED ON MY OWN INSTRUMENTS: this arm was CORRECT when it was
# written, and the GROUND MOVED UNDER IT. Nothing in it changed; the MEANING of what it measures
# changed. It now argues -- authoritatively, at exit 1, in my own voice -- against a key that is sound.
# **A stale arm that emits a confident false RED is worse than no arm**: a false FAIL's remedy is
# DESTRUCTIVE (block a good key, or teach the next reader to ignore RED verdicts).
#
# It is KEPT, not deleted -- it is the historical record of how the 2-input key was verified, and the
# A3/A4 arms in it are the ones that killed two earlier keys. But it MUST NOT render a verdict on the
# shipped key. It now detects that the key has grown past it and refuses.
#     LIVE REPLACEMENT: aor_gate2_final_matrix.py  (the 3-input key, 8/8 at HEAD)
# =================================================================================================
sys.path.insert(0, LIB)
try:
    from aor_resolution import RESOLUTION_COLS
    _shipped_axes = {c for c in ('source_digest', 'fold_mode', 'code_digest') if c in RESOLUTION_COLS}
except Exception as _e:                                    # noqa: BLE001
    print(f'INSTRUMENT BROKEN: cannot read RESOLUTION_COLS to check the key shape ({_e}). '
          'Refusing to render a verdict.')
    sys.exit(2)
if 'code_digest' in _shipped_axes:
    print('=' * 100)
    print('SUPERSEDED -- THIS ARM VERIFIES A KEY THAT NO LONGER SHIPS. NO VERDICT.')
    print('=' * 100)
    print("  this arm's key : (source_digest, fold_mode)          -- 2 axes, stamped at :68-69")
    print(f"  the SHIPPED key: {tuple(sorted(_shipped_axes))}  -- {len(_shipped_axes)} axes")
    print('\n  Its fixtures do not stamp `code_digest`, so the chokepoint raises on them CORRECTLY.')
    print('  Run unchanged, this script would report "A5/A6 OVER-CONDEMN -> do not ship this key" --')
    print('  a CONFIDENT FALSE RED against a sound key. It refuses instead.')
    print('\n  LIVE REPLACEMENT: aor_gate2_final_matrix.py (3-input key, 8/8 GREEN at HEAD).')
    sys.exit(2)

PIN = '2026-07-12'                 # live: latest accounts_v2 partition
ETAG_NOW = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'    # the partition THIS run reads
ETAG_OLD = 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'    # the bytes it held BEFORE an in-place rewrite
FOLDED, SERVICING = 'noel_soderblom', 'peter_lee'

# arm -> (run's fold mode, artifact's stamped fold_mode, artifact's stamped digest, must_raise, why)
ARMS = {
    'A1': ('1', None, None, True, 'artifact ABSENT'),
    'A2': ('1', '__PRE82__', '__PRE82__', True, 'PRE-8.2 artifact: not self-describing'),
    'A3': ('0', 'ACTIVE', ETAG_NOW, True, 'MODE mismatch: FOLDED artifact, switch-OFF run  <== THE DEFECT'),
    'A4': ('1', 'ACTIVE', ETAG_OLD, True, 'DIGEST mismatch: partition REWRITTEN in place (6/69)'),
    'A5': ('1', 'ACTIVE', ETAG_NOW, False, 'LEGIT CACHE REUSE: same content+mode, resolver skipped'),
    'A6': ('0', 'OFF', ETAG_NOW, False, 'fresh servicing-only artifact, switch-OFF run (control)'),
}


def run_arm(arm: str) -> str:
    import pandas as pd
    sys.path.insert(0, LIB)
    from aor_resolution import RESOLUTION_KEY, load_resolution

    _mode, stamp_mode, stamp_digest, _mr, _why = ARMS[arm]
    if arm == 'A1':
        frame = None
    else:
        frame = pd.DataFrame({
            'account_id': [1, 2, 3],
            'advisor_key': [FOLDED if stamp_mode == 'ACTIVE' else SERVICING, 'peter_lee', 'patrick_scanlan'],
            'rep_bucket': ['individual'] * 3,
            'servicing_advisor_key': [SERVICING] * 3,
            'advisor_of_record_raw': ['Noel', '', ''],
            'explicit_aor': [True, False, False],
            'is_mover': [True, False, False],
            'as_of': [PIN] * 3,
        })
        if stamp_mode != '__PRE82__':          # A2 = the pre-round-8.2 artifact: columns simply absent
            frame['fold_mode'] = stamp_mode
            frame['source_digest'] = stamp_digest

    class StubS3:
        def get_object(self, Bucket, Key):
            if frame is None or Key != RESOLUTION_KEY:
                raise FileNotFoundError('NoSuchKey')
            b = BytesIO()
            frame.to_parquet(b, index=False, engine='pyarrow')
            b.seek(0)
            return {'Body': BytesIO(b.read())}

        def head_object(self, Bucket, Key):
            return {'ETag': f'"{ETAG_NOW}"'}    # the partition as it is RIGHT NOW

    try:
        res = load_resolution(StubS3(), 'opal-data-inf')
        return f'RETURNED|{res.advisor_key.iloc[0]}'
    except Exception as e:
        head = str(e).split(' -- ')[0][-58:]
        return f'RAISED|{head}'


if __name__ == '__main__':
    if len(sys.argv) > 1:                       # child: run ONE arm
        print(run_arm(sys.argv[1]))
        sys.exit(0)

    print('=' * 104)
    print('GATE-2 RE-VERIFY -- round-8.2 key (source_digest, fold_mode).  Does it DISCRIMINATE?')
    print('=' * 104)
    ok = True
    for arm, (mode, _sm, _sd, must_raise, why) in ARMS.items():
        env = dict(os.environ, INF_AOR_FOLD_ACTIVE=mode, INF_AOR_ASOF=PIN)
        p = subprocess.run([sys.executable, __file__, arm], env=env, capture_output=True, text=True)
        out = (p.stdout or p.stderr).strip().splitlines()[-1] if (p.stdout or p.stderr).strip() else 'NO-OUTPUT'
        got = out.split('|')[0]
        detail = out.split('|')[1] if '|' in out else ''
        good = (got == 'RAISED') == must_raise
        ok &= good
        verdict = 'ok' if good else ('*** FAIL-OPEN ***' if got == 'RETURNED' else '*** OVER-CONDEMNS ***')
        print(f'\n{arm}  switch={"ACTIVE" if mode == "1" else "OFF   "}  {why}')
        print(f'      demands {"RAISE " if must_raise else "RETURN"} -> got {got:<8} {verdict}')
        if detail:
            print(f'      {detail}')

    print('\n' + '=' * 104)
    if ok:
        print('VERDICT: THE KEY DISCRIMINATES.')
        print('  A3 (the defect that killed the previous key) now RAISES -- the rollback cannot re-serve the fold.')
        print('  A4 (the in-place partition rewrite, 6/69 measured) RAISES -- no other key saw this.')
        print('  A5 RETURNS -- legitimate cache reuse still works, so `--single INF_D_00c` is NOT hard-aborted.')
        print('     THIS IS THE NON-PLACEBO CONTROL: the guard is a discriminator, not a brick.')
        sys.exit(0)
    print('VERDICT: DOES NOT DISCRIMINATE -- gate-2 stays RED. Do not ship this key.')
    sys.exit(1)
