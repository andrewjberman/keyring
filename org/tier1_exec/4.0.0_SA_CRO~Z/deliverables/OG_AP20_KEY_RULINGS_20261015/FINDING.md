# OG-ap-20 s3:prefix literals -- key_rulings rows do NOT clear the naming gate (4.0.0_SA_CRO~Z, 2026-10-15 ~06:4xZ)

**archetype:** VALIDATE

Ask: 2.0.0_SA_COO~O msg 34363 -- land four key_rulings rows (G5A_KEY_RULINGS_FOR_CRO.json @9bafe2e9f9) so the naming gate
admits the ListBucket s3:prefix filter values gold/book/*, gold/holding/*, platinum/reports/*, silver/holdings/*.

## Measured (reproduction: `repro_s3prefix_literals.diff` in this folder; `python .tools/naming-gate.py --diff <it>`)

| registry state | gold/book/* | gold/holding/* | platinum/reports/* | silver/holdings/* | rivalfunds/etfs/gold/* |
|---|---|---|---|---|---|
| HEAD (no new rows) | REFUSE | REFUSE | REFUSE | REFUSE | CONFORMANT |
| + 4 rows, keys as proposed (`gold/book/` ...), canonical `etfs/global/<tier>/<table>/` | REFUSE | REFUSE | REFUSE | REFUSE | CONFORMANT |
| + 4 rows, keys as the literal (`gold/book/*` ...) | REFUSE | REFUSE | REFUSE | REFUSE | CONFORMANT |

The registry was restored to HEAD byte for byte after the test (no diff). NOTHING was committed to key_rulings.json.

## Why (from the contract and the gate)

key_rulings.json answers a path the grader CANNOT read (it RAISES: a first segment that is neither a source nor a tier).
These four begin with a TIER (gold, platinum, silver), so the grader reads them, refuses them as OUT-OF-PATTERN S3Key, and
never consults the rulings. The legacy_addresses rows already landed for the same prefixes (f636989b97) do not move the
verdict either. The `# naming-place-override:` line is documented as not affecting this older limb's REFUSE.

## Where the fix is (not this registry)

1. The gate owner: an IAM s3:prefix CONDITION VALUE is a filter, not an S3 key this code writes or reads; the S3Key grader
   should not grade it (2.0.0_SA_COO~O is raising this). This is the durable fix.
2. Or, until then, a deliberate departure: CLAUDE.md rule 30 -- "a deliberate departure is an R20 register entry Andrew
   acknowledges".
3. Or a restructure that avoids the literals: the applier rejected building them from an HCL expression (it would hide
   the literals from the gate, not answer them), and this seat agrees.

-- 4.0.0_SA_CRO~Z
