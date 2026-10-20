# NFRA_SCHWABBF decomposition -- ROUND 6, the RELEASE of 08403355 on all three tiers (2026-10-20, issuer 2.0.0_SA_COO~SB, workstream `release-0840`)

Source: `deliverables/2.0.0_SA_COO~SB/RELEASE_PLAN_R5_0840_ALL_TIERS.md` (COO half signed; CTO half `org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_SCHWABBF_R5_0840_ALL_TIERS_CTO_HALF_20261020.md` @e7d8af9d1c, msg 110003), the fence pair (`ledger/NEVER_WIDEN_BF5_STATE_FENCE_COO_HALF.md`, CTO half @4b0036c6cb), PRD v1.0. Andrew-direct (relayed by the CTO): one cutover, same-day rollback, no side-by-side, the old keys deleted only on his confirmation; "I want ... the 0840 tax sma account sorted out"; "this needs to go through the same full bronze/silver process that the other masters go through."
**The window:** 2026-10-21 12:00-20:00Z (CTO msg 110003). **CTO conditions:** no pull fire between R4c and R5; if R5 cannot finish by 21:30Z stop after R4b; the cutover does not start until the gateway pair (R3c, `2.0.0_SA_COO~O`, `0.7.0_AE_CloudOps~NFRA1`) is signed and ready; the pin is on origin before R5; any failure rolls back in the same window; order inside the window: fence apply, converter deploy, puller upload.

## The rectangle (round 6)

| cell | item | release act | placement | risk | executor | depends on |
|---|---|---|---|---|---|---|
| `BF-k-6` | the schwab converter build pin in `silver.tf` moves to the commit whose vendored modules the package dir equals (row W5-S5), with a byte-equality test | R3 (pin) | laptop | WORLD (`infra/` floor; nothing applied) | worker | -- |
| `BF-j-6` | the schwab converter role leaves the shared one-way fan-in fence for a schwab-only variant that leaves the 15 enumerated firm state resources writable (row `NFRA_SCHWABBF-S4`: the shared fence's belt 1 denies every S3 mutation outside `opal-data-assets`) | R3b (identity) | laptop | WORLD (`infra/` floor; nothing applied) | worker | `BF-k-6` (same file) |
| `BF-r-1` | open the change-management entry naming the legs, the families that read Schwab bronze and the state readers; confirm the copy identity; take stock before the window | R1 | laptop | WORLD | `0.7.0_AE_CloudOps~NFRA1` | -- |
| `BF-r-3` | the fence apply (3 rows, `shared-infra`), THEN the converter package and identity apply (`opal-assets`, `canonical-schwab-ec2`) under `safe-apply` | R3a, R3b | laptop | WORLD | `0.7.0_AE_CloudOps~NFRA1` | `BF-k-6`, `BF-j-6`, `BF-r-1`, gateway pair ready |
| `BF-r-4` | copy and verify the three tiers of 08403355 (state, silver, bronze LAST) with the move tool | R4a-R4c | laptop | WORLD | `0.7.0_AE_CloudOps~NFRA1` | `BF-r-3` |
| `BF-r-5` | push the pin, extend the entry to name `_monolith_bronze.py`, upload the puller | R5 | laptop | WORLD | `0.7.0_AE_CloudOps~NFRA1` | `BF-r-4` verified |
| `BF-r-8` | FWD-1: the oldest served day of 08403355 through the new writer, the event path, the trace | R8 | laptop | WORLD | `0.7.0_AE_CloudOps~NFRA1` | `BF-r-5` |

Not in this rectangle: R0 (the served-floor re-read belongs to the backfill round, FWD-2; the cutover does not depend on it), R3c (the gateway, `2.0.0_SA_COO~O`'s), R6 (`equal_sample.py compare --form firm`, the COO's own act after `BF-r-5`), R7 (the old-key delete, HELD FOR ANDREW).
**Chains (M = 2; fan-out 1 of 2 workers + 5 staged CloudOps orders).** Chain K: `BF-k-6` -> `BF-j-6` (one worker, slot ~1, one branch: both edit `silver.tf`). Chain R: `BF-r-1` -> `BF-r-3` -> `BF-r-4` -> `BF-r-5` -> `BF-r-8` (one lane, `0.7.0_AE_CloudOps~NFRA1`, one at a time; each is `staged` until the issuer writes its GO).
**Write sets (disjoint).** `BF-k-6`: `infra/aws/terraform/opal-assets/silver.tf`, `data/canonical/schwab/tests/test_schwab_build_pin.py` (new). `BF-j-6`: `infra/aws/terraform/opal-assets/silver.tf`, `data/canonical/schwab/tests/test_converter_fan_in_fence.py` (new). The CloudOps orders write only their deliverables folder `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/`, the change-management ledger and the investigation file.

## Rule 24 record (the cell set is a schema)

- **MECE over a declared domain.** Domain: the writes the PRD v1.0 cutover makes to S3, Lambda, IAM, bucket policy and the box's code home for 08403355 (census: RELEASE_PLAN section 2, nine acts R0-R8 plus R3c) = six cells here + R0 (moved), R3c (COO~O), R6 (COO), R7 (Andrew). Remainder: none.
- **Same grain.** One cell per act-group that must finish before the next may start. **Intent coherence.** Each cell has one stop condition. **State coherence.** A failure inside a cell rolls back that cell's legs in the same window; the old keys are never touched before R7.

## Battery (round 6)

- `comp-schedule`: RUN by reading. The pull fires 09:45, 10:15, 10:45, 21:45, 22:15, 22:45Z; the window 12:00-20:00Z sits between the 10:45 and 21:45 fires; CTO: no fire between R4c and R5.
- `comp-iam`: RUN. The copy identity is CloudOps's own (never the box); the fence rows admit the box role and the converter role for the state prefixes only; the converter role has no delete; versioning is ON on the monolith (read at R1 for the two firm buckets).
- `comp-adversary`: findings inlined into the orders: (1) the `opal-assets` and `shared-infra` plans may carry other projects' pending changes: apply only the named resources by `-target`, and stop if the plan shows anything else; (2) a push before R4 verifies would deploy `_monolith_bronze.py` early (the deploy gate holds it only while no OPEN entry names it): the entry names it at R5, not before; (3) the bronze copy fires the converter 6,074 times by design (event-order branch, plan section 2).
