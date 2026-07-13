"""AoR R2 -- ROW-LEVEL NULL STAMP: the chokepoint guard's one remaining fail-open. RUNNABLE.

    python org/tier1_exec/3.0.0_SA_CVO/deliverables/aor_r2_null_stamp.py

Imports the REAL lib (data/inf/scripts/gold/lib/aor_resolution.py). Stubs exactly ONE thing -- the S3
read -- so the REAL load_resolution() assertion block is exercised. No prod touch, no S3, no writes.

CONTEXT. CVO~B's standing ask (055030Z, before her lane died): "find the state where
(source_etag, fold_mode) ALSO fails to discriminate." The key has since grown a third axis
(code_digest, R-B) and ALL THREE ARE GENUINELY ASSERTED -- aor_resolution.py:660 / :674 / :690
@ dbab19e4c. I could not break the AXES:
    - no 4th DATA input      -- _load_latest_accounts_v2 reads accounts_v2 and nothing else; the
                                explicit-AoR override map derives from accounts_v2 itself (:359-360)
    - no 3rd CODE module     -- the 2-file hash is complete (neither lib imports a project module)
    - digest hashes the code it RAN -- exactly one copy of each lib in the tree, and
                                aor_resolution.py:50 puts that dir at sys.path[0]
    - pin/pull ordering      -- closed by _repin_aor_source_after_pull (dispatch:1471, called :983)
    - walk-back divergence   -- closed: under a set INF_AOR_ASOF the loader filters to the ONE
                                pinned partition (inflection_rep_scope:260-264), so it cannot walk
So I attacked the ASSERTION MECHANISM instead of the axes.

THE DEFECT. All three checks read
    sorted({str(v) for v in pd.Series(res[col]).dropna().unique()}) != [expected] -> RAISE
`.dropna()` removes NULL-stamped rows from the COMPARISON -- and the rows STAY IN THE FRAME and are
returned to every consumer. So the guard RAISES on a missing COLUMN (:648, "refusing to attribute off
an artifact that cannot describe itself") and SILENTLY ACCEPTS a ROW that cannot describe itself.
That is the same principle, one grain down. dropna() drops the row from the CHECK, not from the DATA.

MEASURED (this file):  ONE correctly-stamped row vouches for 870 unstamped rows carrying FOLDED
attribution, on an OFF (rollback) run. A3 walks back in through the null hole.

HONEST LIMIT -- HARM IS NOT DEMONSTRATED, THE DEFECT IS. Today's resolver CANNOT reach this state:
_build_resolution_frame stamps mode/digest/code as loop-invariant SCALARS on every row (:326-328) and
casts to 'string'. An empty string is NOT dropped by dropna() and would RAISE. Only a true NaN/None is
invisible, and no current producer emits one. This is LATENT, P2/hardening -- NOT a go-live blocker,
and it must not be reported as one.

WHY FIX IT ANYWAY. The guard's soundness currently rests on a property of the artifact's PRODUCER --
but this guard exists precisely to police artifacts it did NOT produce (a leftover from another mode,
another vintage, another code version). Its own sibling says so: verify_source_partition's docstring
(:186) -- "'Usually agree, never assert' is precisely the posture that produced F1." The fix is ~3
lines and the chokepoint is already open for round-8.2.

    for c in ('fold_mode', 'source_digest', 'code_digest'):
        if res[c].isna().any():
            raise RuntimeError(f'... {int(res[c].isna().sum())} of {len(res)} rows carry a NULL {c} '
                               '-- those rows cannot say what produced them, and dropna() would drop '
                               'them from the CHECK while SERVING them. Refusing.')

THE BAR THIS HARNESS HOLDS ITSELF TO (learned the hard way -- I shipped a placebo on this very surface
at 05:51Z and CVO~B broke it in one arm): every arm must be reachable from a DIFFERENT TRUTH, and each
assertion must be PROVEN able to fire. P1-P4 prove each axis fires; C1 proves it can go GREEN. An
instrument that cannot fail is not a control; an instrument that cannot pass is not one either.
"""
from __future__ import annotations

import os
import sys

# Env MUST precede the import: AOR_FOLD_ACTIVE is a module-level constant bound at import time.
os.environ['INF_AOR_FOLD_ACTIVE'] = '0'          # THIS RUN IS **OFF** -- the rollback state
os.environ['INF_AOR_ASOF'] = '2026-07-12'
E1 = 'a' * 32                                    # the source content THIS chain pinned
E2 = 'b' * 32                                    # different source content
os.environ['INF_AOR_SRC_ETAG'] = E1

_HERE = os.path.dirname(os.path.abspath(__file__))
_LIB = os.path.normpath(os.path.join(_HERE, '..', '..', '..', '..',
                                     'data', 'inf', 'scripts', 'gold', 'lib'))
sys.path.insert(0, _LIB)

import pandas as pd                              # noqa: E402
import aor_resolution as A                       # the REAL lib                          # noqa: E402

CODE = A.code_digest()                           # the real digest, off the real files


def frame(n_good: int, n_null: int, good_mode: str = 'OFF', good_src: str = E1,
          good_code: str = CODE, folded: str = 'noel_soderblom_FOLDED'):
    """n_good correctly-stamped rows + n_null rows whose THREE IDENTITY FIELDS ARE NULL.
    The null-stamped rows carry FOLDED attribution -- the A3 payload the guard exists to stop."""
    rows = []
    for i in range(n_good):
        rows.append({'account_id': f'good{i}', 'advisor_key': 'peter_lee', 'rep_bucket': 'individual',
                     'servicing_advisor_key': 'peter_lee', 'advisor_of_record_raw': '',
                     'explicit_aor': False, 'is_mover': False, 'as_of': '2026-07-12',
                     'fold_mode': good_mode, 'source_digest': good_src, 'code_digest': good_code})
    for i in range(n_null):
        rows.append({'account_id': f'null{i}', 'advisor_key': folded, 'rep_bucket': 'individual',
                     'servicing_advisor_key': 'peter_lee', 'advisor_of_record_raw': 'Noel Soderblom',
                     'explicit_aor': True, 'is_mover': True, 'as_of': '2026-07-12',
                     'fold_mode': None, 'source_digest': None, 'code_digest': None})
    return pd.DataFrame(rows, columns=A.RESOLUTION_COLS)


def run(label: str, df, truth: str) -> str:
    A._RESOLUTION_CACHE.clear()                   # F6 memoization would mask every arm after the first
    A._read_parquet = lambda s3, bucket, key: df  # the ONLY stub: the S3 read
    try:
        out = A.load_resolution(s3=object(), bucket='opal-data-inf')
    except RuntimeError as e:
        print(f'  {label:<4} {truth:<46} RAISED    {str(e).split(" -- ")[0][:62]}')
        return 'RAISED'
    print(f'  {label:<4} {truth:<46} RETURNED  rows={len(out):<4} '
          f'served={sorted(set(out["advisor_key"]))}')
    return 'RETURNED'


def main() -> int:
    print(f'\nRUN STATE  fold_mode()={A.fold_mode()!r}  pin={E1[:8]}..  code_digest={CODE}')

    print('\n=== POSITIVE CONTROLS -- can each assertion actually FIRE? ===')
    controls = [
        run('P1', frame(871, 0, good_mode='ACTIVE'), 'TRUTH: built under ACTIVE, run is OFF'),
        run('P2', frame(871, 0, good_src=E2), 'TRUTH: derived from different CONTENT'),
        run('P3', frame(871, 0, good_code='deadbeefdeadbeef'), 'TRUTH: computed by RETIRED CODE'),
        run('P4', frame(0, 871), 'TRUTH: ALL rows unstamped (column all-null)'),
    ]
    print('\n=== NON-PLACEBO CONTROL -- can it go GREEN? ===')
    c1 = run('C1', frame(871, 0), 'TRUTH: a valid OFF artifact for this run')

    print('\n=== THE ATTACK -- rows with NULL identity, carrying FOLDED attribution ===')
    n1 = run('N1', frame(800, 71), 'TRUTH: 800 stamped OFF + 71 UNSTAMPED+FOLDED')
    n2 = run('N2', frame(1, 870), 'TRUTH: ONE stamped row + 870 UNSTAMPED+FOLDED')

    print('\n=== VERDICT ===')
    sound = all(v == 'RAISED' for v in controls) and c1 == 'RETURNED'
    print(f'  instrument sound: {sound}  (4 axes fire + it can go green = reachable from different truths)')
    if not sound:
        print('  INSTRUMENT BREAK -- the N arms are UNREADABLE. Do not quote them.')
        return 2
    if 'RETURNED' in (n1, n2):
        print('  *** FAIL-OPEN CONFIRMED. A NULL-stamped row is invisible to all three assertions,')
        print('  *** stays in the frame, and IS SERVED. ONE stamped row vouches for 870 unstamped ones.')
        print('  *** LATENT: no current producer emits a partial-null stamp. Harm NOT demonstrated.')
        return 1
    print('  Row-level nulls are caught -- the key holds on this axis too.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
