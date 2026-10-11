# ADVI_COTBKF decomposition -- ROUND 59 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-11 ~05:4xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2` ROUND-58 ANALYSIS @1c27ce4263 (msg 4153), section 4, and msg 4170 (item 4 re-ruled at this issuer's REC).

| list item | where it lands |
|---|---|
| 1. the bond-day guard | round 58, `CB-bf-1`, drained @154e0e5a3a before the analysis arrived (cut on msg 4131). Closed by the issuer's run, row D2-S87. |
| 2. reconcile the test and the criteria (D2-W83-S2) | done in round 56: `CB-bd-1` AMENDMENT 1 @0efb2fbbe0, drained @8f4b5a22ae. Reported to the CTO (msg sent 05:27Z); no cell here. |
| 3. the config pointer and the error text (D2-S84) | the error text already names the variable. The pointer file is written but `org/devices/state/dell2/` is outside this issuer's lane (owned-paths refused it); asked of the CTO. No cell here. |
| 4. the reason token (D2-W66-S3), as re-ruled in msg 4170 | `CB-bg-1`, below: NO rebuild and NO new enum value; the tracked manifest gains a vocabulary note; the sidecar becomes a named served object. |
| 5. the CB-al-2 pair | an issuer act after this round drains and IRPT_DASHBD's contract cell lands. Its content needs the mint to be ABLE to write what the pair states, which is the rest of `CB-bg-1`. |

**Rule 24.** Domain: everything the pair of item 5 says the mint states that the adapter cannot yet write or prove -> one cell, in the
one adapter this project owns.

## Measured constraints (issuer)

1. `holdings_price_return_reason` reads `NO_HOLDINGS_ROW` on 1,691,729 of 1,691,729 rows in all 3,325 day files (issuer count). It is
   IRPT_DASHBD's enum. The day files and the token do not change.
2. The sidecar `ard_cottonwood_blank_reasons.parquet` has 1,584,413 rows and 4 columns, one of them an account id. It stays outside
   the repo; the repo carries its sha256 and row count only.
3. The dim row-3 partition does not exist (IRPT_DASHBD.TO-DB-b-116). IRPT_DASHBD's contract 0.4.0 lets `emit_method_row` take five
   null thresholds each claimed `absent` (msg 4140); the analysis rules that form.
4. **No S3 write and no deploy in this round.** The apply path is extended and tested on faked S3; it is not run.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-bg-1` | the tracked manifest states the vocabulary note, the sidecar (builder address, sha256, rows) and the method row (builder address, five thresholds `absent`) with the 3,325 day hashes unchanged; the mint path can write and read back the sidecar and the method row, refusing on any existing key | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~86` |

**Fan-out:** `1 of 1 chains, cap 8`. DIRECT-ACT cell (one cell, under 300 product lines, LOCAL): its close is the one real run by
the issuer.
