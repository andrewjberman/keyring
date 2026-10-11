# ADVI_COTBKF decomposition -- ROUND 55 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-11 ~03:4xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** the ROUND-54 ANALYSIS of `1.0.0_SA_CTO~DELL2` @0ac41554df (msg 3985), read after round 54 (CB-bb-1) was issued.

**Rule 24.** Domain: the four items of the analysis's section 4 -> one row each in the first table; one new cell.

`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_54_20261011.md` section 4 is the rectangle of rounds 54 and 55.

| list item | where it lands |
|---|---|
| 1. restore the manifest and fix the sweep (D2-S80) | `CB-bb-1`, drained @05b0f0b2f2. The issuer's close: the section-2 pattern reads 0 hits in 87,054 files; the manifest's 3,325 `sha256` values equal the round-47 local files 3,325 of 3,325. The ruling's "every sha256 field asserts 64 hex" test is in `CB-bc-1`. |
| 2. remove the device default (D2-S77) | `CB-bc-1`, below. |
| 3. the `return_basis` / `method_version` vocabulary value (D2-W66-S1) | NOT a cell here: it is IRPT_DASHBD's, asked of `2.0.0_SA_COO~D2` by message. The re-stamp cell of this project is cut when that value lands. |
| 4. the CB-al-2 re-cut pair | an issuer act, after 1 and 3. |

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-bc-1` | the private sweeps config path comes from `COTBKF_SWEEPS_CONFIG` alone (no device default; the same named error when absent); every `sha256`-named field of a tracked `ard_*manifest.json` is 64 lower-case hex | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~82` |

**Fan-out:** `1 of 1 chains, cap 8`. Round 54 was ONE issuance (@fe72dab7c4, CB-bb-1), cut before the analysis arrived; the
rest of the analysis's list is this round, because to-pipeline-gate admits one issuance per round. DIRECT-ACT cell (one cell, under 300 product lines, LOCAL).
