"""GATE-2 (3.0.0_SA_CVO~B) -- DOES THE GO-LIVE SWITCH MOVE THE PHANTOM BUCKET?

THE QUESTION THIS ARM EXISTS TO ANSWER, AND WHY IT IS A GATE-2 QUESTION:
    My own phantom arm's docstring ASSERTS, in prose, that the phantom is "SWITCH-INDEPENDENT --
    live on the CURRENT pipeline, nothing to do with the AoR fold." **That claim was never
    exercised.** It is a comment, and a comment is a claim with no vintage and no test.

    It decides whether the phantom BLOCKS gate-2. If the switch cannot move the phantom bucket,
    the phantom is a separate, pre-existing SEV (already owned: CTO/COO/base-CVO chapter) and it
    does NOT block the AoR go-live. If the switch CAN move it, then going live silently changes a
    SERVED per-advisor number and it is a gate-2 blocker.

THE MECHANISM, SOURCE-CONFIRMED @ HEAD (not taken on report):
    INF_C_01:463   advisor_key.fillna('inflection_unmapped_rep')   <- the phantom is CREATED here
    INF_C_01:474   apply_resolution_fold(txns, load_resolution())  <- the fold runs AFTER, on those rows
    aor_resolution:775  movers = resolution[resolution['is_mover'] == True]
    aor_resolution:784  attach_advisor_key(df, movers, absent=None)
                        -> overwrites advisor_key for accounts PRESENT IN THE MOVERS FRAME;
                           absent=None leaves everyone else UNTOUCHED.

    So the fold overwrites the phantom key IF AND ONLY IF that account is a MOVER.
    A mover must be in the resolution; the resolution is built from accounts_v2 (the roster).
    => A ROSTER-ABSENT account can never be a mover => the fold cannot touch it.

TODAY'S DATA, GROUNDED LIVE (accounts_v2 snapshot_date=2026-07-12, 873 rows -- the denominator):
    accounts 560 / 703 / 1225 -- CTO's three rep_id=<NA> phantom accounts -- are ALL ABSENT from the
    roster. (Positive control: account 42 IS found, so "absent" is a real reading.)
    => TODAY: the fold cannot reach them. DELTA-0. The phantom is switch-independent RIGHT NOW.

BUT THAT IS A PROPERTY OF THE DATA, NOT OF THE CODE:
    "roster-absent" (accounts_v2) and "null rep_id on the txn row" (the transactions feed) are facts
    about TWO DIFFERENT SOURCES, and NOTHING COUPLES THEM. An account that sits in the roster while
    its txn rows carry a null rep_id is floored to the phantom AND is eligible to be a mover.
    For that account the switch MOVES money out of the phantom bucket.

    That is the same fallacy as "dormant because coverage is 849/849": a green that holds because a
    number happens to sit where it does today is ARMED, not FIXED.

THE ARM: drive the REAL apply_resolution_fold under OFF and ON over four accounts, and read the
phantom bucket on BOTH sides. Hermetic -- pure functions, no S3, no prod touch, no gold run.

CONTROLS THAT CAN FAIL (a control that cannot fail is not a control):
    PC1  a REAL mover MUST re-key under ON. If it does not, the fold never ran and a DELTA-0 on the
         phantom would be MEANINGLESS -- that is an INSTRUMENT BREAK, reported as such, never a pass.
    PC2  under OFF (zero movers) EVERY account must be untouched (the structural no-op contract).
    PC3  a real NON-mover must be untouched under ON (the movers-only contract).
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

REPO = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO / 'data' / 'inf' / 'scripts' / 'gold' / 'lib'))

from aor_resolution import apply_resolution_fold  # noqa: E402  (real lib, real function)

PHANTOM = 'inflection_unmapped_rep'
AOR = 'noel_soderblom'      # the advisor-of-record the fold re-keys movers to
SERVICING = 'peter_lee'     # the servicing rep the txn-side map yields

# account_id -> (starting advisor_key on the txn row, in-resolution?, is_mover?)
ACCOUNTS = {
    560:  (PHANTOM,   False, False),  # TODAY'S PHANTOM: rep_id=<NA> in silver AND roster-absent
    9001: (PHANTOM,   True,  True),   # THE REACHABLE ONE: rep_id=<NA> in silver but IN the roster
    42:   (SERVICING, True,  True),   # PC1 -- a real mover. MUST re-key under ON.
    77:   (SERVICING, True,  False),  # PC3 -- a real non-mover. MUST be untouched.
}


def txn_frame() -> pd.DataFrame:
    """One txn row per account, already floored by INF_C_01:463 where rep_id was null."""
    return pd.DataFrame({
        'account_id':  list(ACCOUNTS),
        'advisor_key': [v[0] for v in ACCOUNTS.values()],
        'rep_bucket':  ['firm' if v[0] == PHANTOM else 'individual' for v in ACCOUNTS.values()],
        'trans_amount': [52_604.80, 40_000.00, 1_000_000.00, 500_000.00],
    })


def resolution(mode: str) -> pd.DataFrame:
    """The canonical resolution. Under OFF it has ZERO movers -- that IS the definition of OFF."""
    rows = []
    for acct, (_, in_res, mover) in ACCOUNTS.items():
        if not in_res:
            continue                     # roster-absent -> never in the resolution
        is_mover = bool(mover) if mode == 'ACTIVE' else False
        rows.append({'account_id': acct,
                     'advisor_key': AOR if is_mover else SERVICING,
                     'rep_bucket': 'individual',
                     'is_mover': is_mover})
    return pd.DataFrame(rows)


def run(mode: str) -> pd.DataFrame:
    df, n = apply_resolution_fold(txn_frame(), resolution(mode))
    df['_n_folded'] = n
    return df


print('=' * 100)
print('PHANTOM x SWITCH ARM -- does the AoR go-live move money OUT of the phantom bucket?')
print('  real apply_resolution_fold @ HEAD; hermetic; no prod touch')
print('=' * 100)

off, on = run('OFF'), run('ACTIVE')
res = off[['account_id', 'advisor_key']].merge(
    on[['account_id', 'advisor_key']], on='account_id', suffixes=('_OFF', '_ON'))
res['MOVED BY THE SWITCH'] = res['advisor_key_OFF'] != res['advisor_key_ON']

print(f"\nfolded under OFF: {int(off['_n_folded'].iloc[0])}   folded under ON: {int(on['_n_folded'].iloc[0])}")
print('\n  account   advisor_key(OFF)              advisor_key(ON)               moved?')
print('  ' + '-' * 88)
for _, r in res.iterrows():
    mark = ' <<< THE SWITCH MOVED IT' if r['MOVED BY THE SWITCH'] else ''
    print(f"  {int(r['account_id']):<9} {r['advisor_key_OFF']:<29} {r['advisor_key_ON']:<29} "
          f"{str(r['MOVED BY THE SWITCH']):<6}{mark}")

# ---- the phantom bucket, on both sides of the switch --------------------------------------------
amt = txn_frame().set_index('account_id')['trans_amount']
ph_off = sum(amt[a] for a in ACCOUNTS if off.set_index('account_id').loc[a, 'advisor_key'] == PHANTOM)
ph_on = sum(amt[a] for a in ACCOUNTS if on.set_index('account_id').loc[a, 'advisor_key'] == PHANTOM)
print(f"\n  PHANTOM BUCKET under OFF : ${ph_off:>14,.2f}")
print(f"  PHANTOM BUCKET under ON  : ${ph_on:>14,.2f}")
print(f"  DELTA CAUSED BY THE SWITCH: ${ph_on - ph_off:>13,.2f}")

# ---- controls ----------------------------------------------------------------------------------
onx, offx = on.set_index('account_id'), off.set_index('account_id')
pc1 = offx.loc[42, 'advisor_key'] == SERVICING and onx.loc[42, 'advisor_key'] == AOR
pc2 = all(offx.loc[a, 'advisor_key'] == ACCOUNTS[a][0] for a in ACCOUNTS)
pc3 = onx.loc[77, 'advisor_key'] == SERVICING

print('\n  CONTROLS (could this arm have failed?)')
print(f"    PC1  a REAL mover re-keys under ON ...... {'PASS' if pc1 else 'INSTRUMENT BREAK'}"
      f"   ({offx.loc[42, 'advisor_key']} -> {onx.loc[42, 'advisor_key']})")
print(f"    PC2  OFF is a structural no-op ......... {'PASS' if pc2 else 'FAIL'}")
print(f"    PC3  a non-mover is untouched under ON . {'PASS' if pc3 else 'FAIL'}")

if not (pc1 and pc2 and pc3):
    print('\nINSTRUMENT BREAK -- the controls did not hold. NO VERDICT. Do not quote this run.')
    sys.exit(2)

print('\n' + '=' * 100)
reachable = bool(res.set_index('account_id').loc[9001, 'MOVED BY THE SWITCH'])
today = bool(res.set_index('account_id').loc[560, 'MOVED BY THE SWITCH'])

print('TODAY (accounts 560/703/1225 are ROSTER-ABSENT, grounded live on accounts_v2, 873 rows):')
print(f"  the switch moves the phantom? {today}  -> DELTA-0. The phantom does NOT block go-live.")
print('\nREACHABLE (an account IN the roster whose txn rep_id is null -- account 9001):')
print(f"  the switch moves the phantom? {reachable}"
      f"  -> the fold re-keys it to {onx.loc[9001, 'advisor_key']!r}, moving $40,000.00 out of the phantom.")

if today:
    print('\nVERDICT: RED -- the switch moves TODAY\'S phantom money. GATE-2 BLOCKER.')
    sys.exit(1)
if reachable:
    print('\nVERDICT: GREEN FOR GO-LIVE, ON THE DATA -- and that is exactly how precisely it must be said.')
    print('  The phantom is switch-independent TODAY because all 3 phantom accounts happen to be')
    print('  ROSTER-ABSENT. It is NOT structurally switch-independent: roster-presence and txn-rep_id')
    print('  nullity are facts about TWO DIFFERENT SOURCES and NOTHING COUPLES THEM. The first account')
    print('  that is roster-PRESENT with a null txn rep_id has its money MOVED by the switch.')
    print('  => Does NOT block gate-2. DOES belong in the determination as a DATA-DEPENDENT green,')
    print('     and in the phantom chapter as a reason the phantom must be fixed at the SOURCE.')
    sys.exit(0)
print('\nVERDICT: INDETERMINATE -- neither case fired. The arm did not exercise what it claims.')
sys.exit(2)
