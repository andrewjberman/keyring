"""GATE-2 (3.0.0_SA_CVO~B) -- THE PHANTOM-ADVISOR ARM, v2. ASSERT AGAINST THE ROSTER, NOT A NAME.

>> WHY v1 WAS REBUILT: ITS *GREEN* CONDITION REWARDED THE ONE FIX THAT IS FORBIDDEN. <<

v1 read INF_D_00f's junk-key normalisation list from source and asked one question:
    "does the string 'inflection_unmapped_rep' survive the .isin([...]) -> 'Other' normalisation?"
So v1 went GREEN the moment anyone ADDED the catchall to that list -- i.e. folded the residual into
the 'Other' bucket. **That is precisely the fix CTO's ruling (i) FORBIDS:**

    "SUPPRESSING it silently is FORBIDDEN -- silently dropping a residual is how a reconciliation
     stops reconciling."

and after the grounding INVERTED (`1d0bf952c`), it is worse than forbidden -- it is FALSE. That money
is not unattributable: it is a REAL ADVISOR'S. Renaming it 'Other' would be a false statement on a
served field. **My own arm would have certified it.** A control that can pass for the wrong reason is
not a control -- and this one would have passed for the exact wrong reason.

v1 also ASSERTED, in prose, that the phantom is "SWITCH-INDEPENDENT ... nothing to do with the AoR
fold," and never tested it. That claim is now EXERCISED in a separate arm
(`aor_phantom_switch_arm.py`) and it is TRUE ONLY OF TODAY'S DATA: the 3 phantom accounts happen to
be ROSTER-ABSENT, so the fold cannot reach them. A roster-PRESENT account with a null txn rep_id
would be moved by the switch. A comment is a claim with no vintage and no test.

>> WHAT v2 ASSERTS, AND WHY IT IS THE DURABLE SHAPE <<
CTO's durable ruling: "the producer must assert EVERY KEY IN `advisors` RESOLVES TO A REAL ADVISOR ON
THE CANONICAL ROSTER, and RAISE otherwise -- a one-time removal fixes today; the next residual walks
back in under a different name."

So v2 asserts membership in the CANONICAL ROSTER, derived from source, and is blind to the name:
    canonical roster = values(_INF_REP_ID_TO_ADVISOR_KEY)   # INF_C_01, the rep_id -> advisor map
                     u {the AoR advisor keys}               # the advisor-of-record SSOT
A key the map cannot PRODUCE is not an advisor -- whatever it is called.
    'inflection_unmapped_rep' -> not producible -> RED   (it comes from a .fillna() FLOOR, not the map)
    'Other'                   -> not producible -> RED   (the FORBIDDEN fix does NOT green this arm)
    <any future residual>     -> not producible -> RED   (the "different name" case, closed by shape)

GROUNDED ON THE SERVED ARTIFACT, not on a source simulation (v1's fatal shape -- it asserted what the
normalisation WOULD do, then called itself a served-value check):
    s3://opal-data-inf/platinum/firm/advisor_nna_canonical.json   (READ-ONLY. No re-derive: the
    [STOP] b7bce51bd forbids RE-DERIVATION of canonical_nna, not reading it.)

CONTROLS (a control that cannot fail is not a control):
    M0  the LIVE served artifact                       -> must be RED   (the phantom is live TODAY)
    M1  the FORBIDDEN fix: residual renamed 'Other'    -> must STAY RED (v1 went GREEN here)
    M2  the LEGITIMATE fix: restored to a real advisor -> GREEN
    M3  a NEW residual under a DIFFERENT name          -> RED  (shape, not string)
    M4  POSITIVE CONTROL: a clean artifact             -> GREEN (proves it CAN go green -- else the
                                                          arm is a brick that says RED to everything)
"""
from __future__ import annotations

import json
import re
import subprocess
import sys

C01 = 'data/inf/scripts/gold/INF_C_01.canonical_nna.py'
BUCKET = 'opal-data-inf'
KEY = 'platinum/firm/advisor_nna_canonical.json'
SERVED = f's3://{BUCKET}/{KEY}'
PHANTOM = 'inflection_unmapped_rep'
AOR_KEYS = {'noel_soderblom'}          # the advisor-of-record SSOT's new advisor


def canonical_roster() -> set[str]:
    """The advisor keys the rep_id -> advisor map can PRODUCE, read from source at HEAD."""
    src = subprocess.run(['git', 'show', f'HEAD:{C01}'], capture_output=True, text=True).stdout
    if not src.strip():
        raise RuntimeError('INSTRUMENT BROKEN: empty source for INF_C_01 -- refusing to report a '
                           'verdict off a read that returned nothing. (A zero is the one result a '
                           'retrieval can produce for reasons that have nothing to do with the estate.)')
    m = re.search(r'_INF_REP_ID_TO_ADVISOR_KEY[^=]*=\s*\{(.*?)\}', src, re.S)
    if not m:
        raise RuntimeError('INSTRUMENT BROKEN: could not find _INF_REP_ID_TO_ADVISOR_KEY in INF_C_01. '
                           'A MISSING map is not an EMPTY one. Refusing to report GREEN off an absent '
                           'symbol -- that is exactly how a renamed clobber looks identical to a fix.')
    keys = set(re.findall(r":\s*'([a-z_]+)'", m.group(1)))
    if not keys:
        raise RuntimeError('INSTRUMENT BROKEN: the map parsed to ZERO advisor keys. If the roster is '
                           'empty, EVERY key is a phantom and this arm would report a spectacular, '
                           'meaningless RED. Refusing.')
    return keys | AOR_KEYS


def served_advisor_keys() -> tuple[list[str], dict]:
    """READ-ONLY. boto3, not the `aws` CLI: `.tools/aws` is a Git-Bash SHIM, and a Windows Python
    subprocess cannot resolve it (FileNotFoundError WinError 2). Note the failure mode that did NOT
    happen: had this been wrapped in a bare `except: return []`, a FAILED READ would have produced an
    EMPTY advisor list and this arm would have printed a triumphant GREEN -- "no phantoms!" -- off an
    artifact it never read. A failed read is NOT an empty advisor list. Fail closed."""
    import boto3
    body = boto3.client('s3').get_object(Bucket=BUCKET, Key=KEY)['Body'].read()
    if not body.strip():
        raise RuntimeError('INSTRUMENT BROKEN: the served artifact read back EMPTY. That is not an '
                           'empty advisor list -- it is a read that told us nothing. Refusing GREEN.')
    d = json.loads(body)
    if 'advisors' not in d:
        raise RuntimeError("INSTRUMENT BROKEN: no 'advisors' key in the served artifact. A MISSING "
                           'collection is not an EMPTY one. Refusing GREEN.')
    return list(d['advisors'].keys()), d


def verdict(keys: list[str], roster: set[str], label: str) -> bool:
    """True == RED (a served key that the canonical roster cannot produce)."""
    phantoms = [k for k in keys if k not in roster]
    print(f'\n  {label}')
    print(f'      served advisors : {sorted(keys)}')
    if phantoms:
        print(f'      *** RED -- NOT ON THE CANONICAL ROSTER: {phantoms} ***')
    else:
        print('      GREEN -- every served key resolves to a real advisor on the canonical roster.')
    return bool(phantoms)


print('=' * 100)
print('PHANTOM-ADVISOR ARM v2 -- does the SERVED per-advisor NNA carry a key that is NOT AN ADVISOR?')
print('=' * 100)

roster = canonical_roster()
print("\n  CANONICAL ROSTER (from INF_C_01's rep_id->advisor map @ HEAD, + the AoR SSOT):")
print(f'      {sorted(roster)}   (denominator: {len(roster)})')
print('  A key this map cannot PRODUCE is not an advisor -- whatever it is called.')

live_keys, doc = served_advisor_keys()
print(f'\n  SERVED ARTIFACT: {SERVED}')
print(f'      generated_at={doc.get("generated_at")}  data_as_of={doc.get("data_as_of")}')
print('      (FROZEN by the bronze STOP -- and note this is NOT a V4: it PREDATES the AoR code and')
print('       was produced under switch-OFF. It grounds the PHANTOM; it says nothing about the fold.)')

m0 = verdict(live_keys, roster, 'M0  THE LIVE SERVED ARTIFACT')
if m0:
    amt = doc['advisors'][PHANTOM]['windows']['MAX']['nna']
    firm = doc['firm']['windows']['MAX']['nna']
    tot = sum(doc['advisors'][k]['windows']['MAX']['nna'] for k in live_keys)
    print(f'      the phantom holds ${amt:,.2f} of REAL money on the served spine')
    print(f'      sum(advisors)=${tot:,.2f}  firm=${firm:,.2f}  DELTA=${tot-firm:,.2f}')
    print('      >> AND THE RECONCILIATION TIES *BECAUSE* THE PHANTOM IS COUNTED AS AN ADVISOR. <<')
    print('         An identity that is GREEN in the defective state is not a detector. (It also stays')
    print('         green through the DELETION mode of the STOP -- both sides lose the money at once.)')

# ---- the mutants: can this arm pass for the WRONG reason? ---------------------------------------
m1 = verdict(['Other', 'peter_lee', 'joe_brandenburg'], roster,
             "M1  THE FORBIDDEN FIX -- residual folded into 'Other' (v1 went GREEN here)")
m2 = verdict(['patrick_scanlan', 'peter_lee', 'joe_brandenburg'], roster,
             'M2  THE LEGITIMATE FIX -- restored to a real advisor on the roster')
m3 = verdict(['inflection_residual_v2', 'peter_lee'], roster,
             'M3  A NEW RESIDUAL UNDER A DIFFERENT NAME (the "walks back in" case)')
m4 = verdict(['peter_lee', 'joe_brandenburg', 'patrick_scanlan', 'inflection_wealth_management'],
             roster, 'M4  POSITIVE CONTROL -- a clean artifact (proves the arm CAN go green)')

print('\n' + '=' * 100)
sound = (m1 is True and m2 is False and m3 is True and m4 is False)
print('  INSTRUMENT SOUNDNESS')
print(f"    M1 forbidden fix STAYS RED ...... {'PASS' if m1 else 'FAIL -- the arm rewards suppression'}")
print(f"    M2 legitimate fix goes GREEN .... {'PASS' if not m2 else 'FAIL -- the arm is a brick'}")
print(f"    M3 renamed residual caught ...... {'PASS' if m3 else 'FAIL -- the arm keys on a STRING'}")
print(f"    M4 clean artifact goes GREEN .... {'PASS' if not m4 else 'FAIL -- says RED to everything'}")
if not sound:
    print('\nINSTRUMENT BROKEN -- the mutants did not behave. NO VERDICT. Do not quote this run.')
    sys.exit(2)
print('    -> the arm is reachable from DIFFERENT TRUTHS, and it does NOT reward the forbidden fix.')

if m0:
    print('\nVERDICT: RED on the SERVED artifact. The phantom advisor is LIVE.')
    print('  NOT a gate-2 blocker: exercised switch-independent on TODAY\'s data (all 3 phantom')
    print('  accounts are ROSTER-ABSENT, so the fold cannot reach them -- aor_phantom_switch_arm.py).')
    print('  It is a SEPARATE, PRE-EXISTING defect on the current pipeline, and its FIX IS BLOCKED by')
    print('  [STOP] b7bce51bd (no canonical_nna re-derivation until the silver rep_id NULL is fixed).')
    sys.exit(1)
print('\nVERDICT: GREEN -- no phantom on the served spine.')
sys.exit(0)
