# Session log — CN-P1 + RA-P1 post-rerun validator pass

**Agent:** 0.4.0_DS_ClientPlatform~D
**Date:** 2026-04-15
**Task orders:**
- `ADVI_ROLLUP.CN-P1.ds-nna-atomic-shadow-write.md` (in_progress -> complete)
- `ADVI_ROLLUP.RA-P1.ds-role-aua-shadow-write.md` (in_progress -> complete)

## Summary

A->D rerun chain closed by AE at 19:35Z. Both shadow artifacts present in S3; both validators PASS on `2026-04-13.parquet`. Flipping CN-P1 + RA-P1 to COMPLETE; CN-P2 (~D) and RA-P2 (~C) consumer-cutover TOs are now unblocked from the shadow-emit dependency.

## Artifacts validated

| Artifact | S3 key | Mtime ET | Size | Rows |
|---|---|---|---|---|
| nna_atomic | `s3://opal-data-bd/gold/canonical/nna_atomic/2026-04-13.parquet` | 14:42 | 331 KB | 9,559 |
| role_aua | `s3://opal-data-bd/gold/canonical/role_aua/2026-04-13.parquet` | 15:05 | 18 KB | (n/a — not surfaced by validator) |

## Validator runs

### `validate_nna_atomic.py --artifact /tmp/nna_atomic_2026-04-13.parquet`

```
[OK] INV1 PASS: daily identity holds on all 9,559 rows
[OK] INV2 PASS: cumulative identity holds on all 9,559 rows
[OK] INV3 SKIPPED: no --prior-artifact supplied
[OK] INV4 PASS: firm daily_inflow=4011250.06, daily_outflow=9156462.81, nna_txn=-5145212.75 (consistent)
[OK] INV5 PASS: fee partition (billable + non_billable == total) holds per date across all flow columns
RESULT: ALL INVARIANTS PASS
```

INV3 (period-rollup vs prior-artifact) is the only skipped invariant; will be exercised at CN-P2 consumer-cutover when prior-day comparator becomes part of the standard run.

### `validate_role_aua.py --artifact /tmp/role_aua_2026-04-13.parquet`

```
OK: I1 fee-bucket partition (aua_fee_paying + aua_no_fee == aua)
OK: I2 equal-split sum reconciliation (sum_role(aua) == aua_tagged_total per (date, advisor))
SKIP: I3 cross-advisor additivity -- --cross-check not provided
SKIP: I4 certified AUA bound -- --certified not provided
OK: I5 primary key uniqueness ((date, advisor, role) unique)
OK: I6 role enum membership

role_aua validation: 6/6 invariants passed
```

I3 and I4 are optional cross-checks that require external comparators (account_performance.total_aua, certified_aua reference). Both will be enabled at RA-P2 consumer-cutover where those comparators are part of the wired flow.

## Compiler Tools

| Run | Expect | Observed | Pass/Fail |
|---|---|---|---|
| `aws s3 ls s3://opal-data-bd/gold/canonical/nna_atomic/` | At least one shadow parquet present | `2026-04-13.parquet` 14:42 ET 331KB | **PASS** |
| `aws s3 ls s3://opal-data-bd/gold/canonical/role_aua/` | At least one shadow parquet present | `2026-04-13.parquet` 15:05 ET 18KB | **PASS** |
| `validate_nna_atomic.py --artifact ...` | Exit 0; INV1/2/4/5 PASS | All PASS, INV3 skipped (no prior artifact) | **PASS** |
| `validate_role_aua.py --artifact ...` | Exit 0; I1/I2/I5/I6 PASS | 6/6 PASS, I3/I4 skipped (optional) | **PASS** |

## Acceptance check

CN-P1:
- Shadow write to `gold/canonical/nna_atomic/{date}.parquet` from C_01: artifact present, conforms to CN-P0 ratified 22-column schema (validator passes invariants on it).
- Atomic-rollback property: pre-fire commit pairing preserved (bf9651b8 + afd553d4 both pre-rerun).

RA-P1:
- Shadow write to `gold/canonical/role_aua/{date}.parquet` from D_02 pre-pass: artifact present, conforms to RA-P0 schema (validator 6/6).
- Scope deferrals (aua_fee_paying=0, aua_no_fee=aua, txn columns=0.0) intact for P2 promotion.

## Next

- Flip both TOs to complete in same commit as this log.
- MCP COO with shadow-emit close + validator pass + downstream unblock notice.
- CN-P2 (~D) consumer cutover: pickup candidate after WP-11 49F delta lands or per COO sequencing.
- RA-P2 (~C) consumer cutover: notify ~C lane unblocked.
- INV3 will be wired at CN-P2 with `--prior-artifact` comparator path.

## Risks / flags

- Single-day shadow artifact only (`2026-04-13`). If A->D rerun was supposed to backfill multiple days, AE should confirm the date scope. Validator passes on the day present; multi-day backfill verification deferred.
- INV3 (period-rollup) and I3/I4 (cross-checks) remain SKIP — not blocking for shadow phase but mandatory at consumer cutover phases.
