# IRPT_CUSTDY decomposition -- ROUND 7 (issuer 2.0.0_SA_COO~K2; drafted 2026-10-07 ~15:3xZ, dell2)

**Status: ISSUED** (the issuance commit carries the `fanout:` line).

**Cut on:** the round-6 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_CUSTDY_ROUND_6_20261007.md` @881e552c2e
(`1.0.0_SA_CTO~DELL2` msg 749), section 2: E1-E3. receiving-check: UNCHECKED (no checker for a round analysis).

**Rule 24.** Domain: E1-E3, three cells, one per item. No item is dropped; two are gated, and each gated cell is cut the tick its gate opens,
in its own workstream (`~K2-E2`, `~K2-E3`), as rounds 3 and 4 did.

## Measured constraints (dell2, ~15:3xZ)

1. **E1 is already executing.** The CTO's review (msg 743) asked for this exact change on e355d193 before the analysis arrived; the issuer
   re-opened `IRPT_CUSTDY.TO-CU-f-1` as AMENDMENT 1 @c2b4cbb412 (criterion `CU16-AC3`, the mixed document refused by name, with the
   all-covered control), and worker `0.9.0_WK_IRPT_CUSTDY~14` is on it on portal `wk-IRPT_CUSTDY-14-portal` @e355d193. The analysis's E1
   control (2) also names the all-not-covered document: `CU16-AC2` (re-run under the amendment) is that control. So E1 is served by that
   order and no second order is cut for the same change (two orders on one write set would collide).
2. **E2 is gated on Andrew's word:** it executes after E1's template lands on portal DEV, which is Andrew's call (laptop 106221; CTO msg 749).
   Gate: `E1 on portal DEV`. Its risk is SERVED (it reads the served export).
3. **E3 has no input in the estate.** FWD-9 needs one real Black Diamond 49 Financial client report. Measured: the repo holds none
   (`comp-find -i 'black ?diamond.{0,40}client report|client report.{0,40}black ?diamond'`: 10 hits across 61,426 files, all prose or logs);
   `opal-data-bd` holds bronze endpoint pulls under `blackdiamond/49financial/bronze/` and no report (31 top-level prefixes read). Fetching a
   report from Black Diamond is a vendor call and a download: both need Andrew's word (vendor-API rule; msgs 633/642, no downloads). Gate:
   `one BD 49F client report on dell2` -- supplied by Andrew (laptop Taildrop, @50df0c2e97) or a per-use word for the pull. Card to
   `0.0.0_AB_MSTR~DELL2` for Andrew.

| cell | what | serves | status | placement | risk | chain / slot |
|---|---|---|---|---|---|---|
| `CU-g-1` (E1) | a mixed household refused by name; all-covered and all-not-covered controls render | FWD-1 | EXECUTING as `IRPT_CUSTDY.TO-CU-f-1` AMENDMENT 1 | dell2 | LOCAL | A, `~14` |
| `CU-g-2` (E2) | hop 5 served: one `CUSTODY_REPORT` export per household reaching READY; one report read against hop 3 (JUDGMENT, CVO) | FWD-1 | GATED: E1 on portal DEV (Andrew) | dell2 | SERVED | `~K2-E2`, cut at the gate |
| `CU-g-3` (E3) | the FWD-9 field map of one real BD 49F client report, every field mapped or MISSING with reason, denominator printed | FWD-9 | GATED: the report on dell2 (Andrew) | dell2 | LOCAL | `~K2-E3`, cut at the gate |

**Ordering and fan-out:** `fanout: 0 of 3 chains newly spawned this tick` -- A is already running under the amendment; E2 and E3 are gated.

## The issuer's acts

1. At E1's completion: drain, re-run the bun pair in the drained portal line, and send the new portal commit to `1.0.0_SA_CTO~DELL2` for PASS.
2. At each gate: cut its order the same tick (dry-run at the base first) and spawn.
