# PRE-REGISTRATION -- the first POST-FIX scheduled fire (INF billing window + fee flag)

**Written 2026-08-12 ~13:26Z, BEFORE the evidence exists.** The interpretation table is fixed
here so the read cannot be rationalized afterward (the swallow-fix lesson: write the table
before the evidence). Andrew-direct: "wait for the fire and read both figures."

## What is being exercised

The 2026-08-11 deploys, verified still in place this morning (4/4 md5 TIE):
`build_billing_dim.py` 9a25fe0d · `lib/fee_classification.py` 52005d2b ·
`INF_D_04.client_portal_summary.py` eaae8fb4 · `validate_api_dims.py` 777c62ae.
No scheduled run has executed since they landed (last chain complete 08-11 14:59Z; deploys
~17:12Z). Today's run is the FIRST production exercise.

## PRE-FIX BASELINE (measured this morning on the 2026-08-11 partition, the last pre-fix run)

- `ending_mv_source` column: **ABSENT**
- `is_fee_earning` column: **PRESENT** (the retired one)
- ending_mv populated: **554 of 908** rows (354 absent -- the suppressed class)
- book sum: **$140,717,260.47**

## STRUCTURAL CHECKS -- deterministic, must hold EXACTLY (a miss is a FAIL, not a band)

| # | Check | PASS | FAIL means |
|---|---|---|---|
| S1 | `ending_mv_source` column present | present | the deployed code did not execute (runner used a different/cached copy) -- a DEPLOY-PATH defect, not a data defect |
| S2 | `is_fee_earning` column absent | absent | the flag retirement did not take; two derivation homes may be live again |
| S3 | ending_mv populated on ALL INFGRD rows, ZERO source-absent | N/N | the fix is PARTIAL -- the roster join missed rows; report the count, do not average it away |
| S4 | own tie-out: currentValue == retired windowed ending_mv on previously-populated rows | to the cent | the value path changed meaning, not just coverage |

## VALUE CHECKS -- BANDED (one trading day of market movement; exact equality is NOT expected)

| # | Quantity | Pinned reference (08-11 QA) | PASS band | The discriminator that actually matters |
|---|---|---|---|---|
| V1 | silver billing book | $209,476,279.36 | ~$205M-$214M (±~2%, one day) | **scale**: ~$209M vs the pre-fix ~$141M. A +49% jump IS the fix landing. Still ~$141M = fix did not take |
| V2 | served fee-earning AUA | $202,840,000 (approx pin) | ~$199M-$207M | must stay ~$200M-scale |
| V3 | served NON-fee-earning AUA | $6,290,000 (approx pin) | ~$6M-$8M | **Andrew's own figure was ~$8M.** A return to $60M+ = the coercion class is back and the flag consolidation did not take |

## NAMED FAILURE MODES (declared in advance so none gets discovered as a surprise)

1. **Chain does not fire** -> report a MEASURED non-fire with its denominator; do NOT infer a
   cause, do NOT fire an ad-hoc run as a substitute (ad-hoc is never production evidence).
2. **S1 fails** -> the code is deployed but not EXECUTING; the gap is the deploy path
   (which artifact the runner actually loads), and that is the finding, not the numbers.
3. **S3 partial** -> report the exact absent count; a partial coverage fix is a different
   defect from the one that was fixed.
4. **V3 returns to $60M+** -> the single-derivation-home consolidation failed; escalate as a
   regression of Andrew instruction #2, same turn.
5. **Values land in band but S1/S2 fail** -> COINCIDENCE, NOT CONFIRMATION. The structural
   checks are the oracle; the value bands alone cannot distinguish a working fix from a
   market move on the old code.

## Scope note

This reads the SCHEDULED run only. Silver book (V1) comes from the silver partition; V2/V3
come from the served artifact after the gold leg completes. If the silver leg lands but the
gold leg has not, V1 is readable and V2/V3 are NOT YET -- report them as pending, never as
absent.
