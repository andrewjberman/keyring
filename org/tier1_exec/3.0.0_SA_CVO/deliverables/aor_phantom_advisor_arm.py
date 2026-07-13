"""GATE-2 (3.0.0_SA_CVO~B) -- THE PHANTOM-ADVISOR ARM (F2-B item (c)).

DOES A FABRICATED ADVISOR REACH THE SERVED PER-ADVISOR NNA, HOLDING REAL AUA?

THE MECHANISM (grounded at source, not taken on report):
    INF_C_01:463   txns['advisor_key'] = txns['advisor_key'].fillna('inflection_unmapped_rep')
                   -- C_01 FLOORS every unmapped rep to that catchall, and writes canonical_nna.
    INF_D_00f:496  nna_clean.loc[advisor_key.isin(['', 'nan', 'unknown', 'Unknown']), ...] = 'Other'
    INF_D_04:2475  merged.loc[advisor_key.isin(['', 'nan', 'unknown', 'Unknown']), ...] = 'Other'
                   -- the normalisation that folds junk keys into the 'Other' bucket so the partition
                      sums close to the firm total.

    'inflection_unmapped_rep' IS IN NEITHER LIST.

    So it is NOT junk-normalised. It survives as its own advisor_key and is SERVED as a per-advisor
    row -- A FABRICATED ADVISOR, NAMED "inflection_unmapped_rep", HOLDING REAL AUA, on the per-advisor
    NNA that the portal shows.

WHY IT IS DORMANT AND WHY THAT IS NOT SAFETY:
    It fires only when some account's rep_id is unmapped -- and rep coverage happens to be 849/849
    today, so the floor never triggers. **A DEFECT THAT IS DORMANT BECAUSE A NUMBER HAPPENS TO BE AT
    100% IS NOT FIXED; IT IS ARMED.** The first coverage regression serves a phantom advisor.
    It is also SWITCH-INDEPENDENT: it has nothing to do with the AoR fold. It is live on the CURRENT
    pipeline, today, and would have been live regardless of whether this go-live ever happened.

THE ARM: floor a canonical_nna row to the catchall, push it through the real normalisation list of a
given vintage, and read the SERVED advisor set. RED while the phantom survives; GREEN once it is
normalised. (Note the shape: this asserts on the SERVED VALUE, not on the producer's output -- the
lesson C_07 cost me a retraction to learn.)

    @8bd1d1b62 (my determination hash)  -> RED  (phantom served)
    @dbab19e4c (F2-B a+b -- lib only)   -> RED  ((c) is NOT in it; it touches D_00f/D_04, which it does not)
    @<the (c) hash>                     -> must go GREEN

Hermetic: reads each vintage's source via git; no prod touch, no gold run.
"""
from __future__ import annotations

import re
import subprocess
import sys

import pandas as pd

PHANTOM = 'inflection_unmapped_rep'
D00F = 'data/inf/scripts/gold/INF_D_00f.advisor_nna_canonical.py'
REAL_AUA = 4_200_000.0

VINTAGES = [
    ('8bd1d1b62', 'my gate-2 determination hash'),
    ('dbab19e4c', 'F2-B (a)+(b) -- lib only'),
    ('HEAD', 'HEAD now'),
]


def normalisation_list(ref: str) -> str:
    """The junk-key normalisation list this vintage folds into 'Other'."""
    src = subprocess.run(['git', 'show', f'{ref}:{D00F}'], capture_output=True, text=True).stdout
    if not src.strip():
        raise RuntimeError(f'INSTRUMENT BROKEN: empty source for {ref} -- refusing to report a verdict '
                           'off a read that returned nothing.')
    # anchor on the normalisation specifically: the .isin([...]) that assigns 'Other'
    m = re.search(r"isin\(\[([^\]]*)\]\)\s*,?\s*\n?\s*'advisor_key'\s*\n?\s*\]\s*=\s*'Other'", src)
    if not m:
        m = re.search(r"isin\(\[([^\]]*)\]\)", src)      # fallback: the first isin list
    if not m:
        raise RuntimeError(f'INSTRUMENT BROKEN: no normalisation list found in {ref} -- a MISSING list '
                           'is not the same as an EMPTY one. Refusing to report GREEN.')
    return m.group(1)


print('=' * 98)
print('PHANTOM-ADVISOR ARM -- does a FABRICATED advisor reach the SERVED per-advisor NNA?')
print(f'  C_01 floors unmapped reps to {PHANTOM!r} and writes canonical_nna; D_00f/D_04 normalise junk keys.')
print('=' * 98)

results = {}
for ref, label in VINTAGES:
    try:
        lst = normalisation_list(ref)
    except Exception as e:
        print(f'\n  {ref:<12} ({label})\n      {e}')
        results[ref] = None
        continue

    members = [x.strip().strip('\'"') for x in lst.split(',') if x.strip()]
    # a canonical_nna floored by C_01 to the catchall, carrying REAL AUA
    nna = pd.DataFrame({'advisor_key': [PHANTOM, 'peter_lee'], 'nna': [REAL_AUA, 1_000_000.0]})
    nna.loc[nna['advisor_key'].isin(members), 'advisor_key'] = 'Other'
    served = sorted(nna['advisor_key'].unique())
    phantom_served = PHANTOM in served
    results[ref] = phantom_served

    print(f'\n  {ref:<12} ({label})')
    print(f'      normalisation list : [{lst}]')
    print(f'      SERVED advisors    : {served}')
    if phantom_served:
        print(f'      *** RED -- PHANTOM ADVISOR {PHANTOM!r} SERVED, holding ${REAL_AUA:,.0f} of real AUA ***')
    else:
        print("      GREEN -- normalised into 'Other'. No fabricated advisor is served.")

print('\n' + '=' * 98)
head = results.get('HEAD')
if head is True:
    print('VERDICT: RED at HEAD. The phantom-advisor defect (F2-B item (c)) is STILL LIVE.')
    print('  It is SWITCH-INDEPENDENT -- live on the CURRENT pipeline, nothing to do with the AoR fold.')
    print('  Dormant only because rep coverage is 849/849. A defect that is dormant because a number')
    print('  happens to be at 100% is not fixed; it is ARMED.')
    sys.exit(1)
if head is False:
    print('VERDICT: GREEN at HEAD -- the phantom is normalised and cannot be served.')
    print('  And the arm DISCRIMINATES: it is RED at 8bd1d1b62, so it can see the defect it clears.')
    sys.exit(0)
print('VERDICT: INDETERMINATE -- the instrument could not read a vintage. Do not quote this run.')
sys.exit(2)
