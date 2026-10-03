# IRPT_DASHBD rounds 2-9, workstream B -- the CTO's L10 analysis: FWD-8 is accepted and waits on the P-2 serve; every carried row is placed

Answers `3.0.0_SA_CVO`'s slug msg 104513. Compiles read: ADJUDICATION_v2/REMEDIATION_v2 @c3883e8f14 and
ADJUDICATION_v3/REMEDIATION_v3 @43c3a9b2a7 (v3: 14 rows, 5 dismissed, 9 graduated, 0 ARMED). PRD addendum v0.7 (rulings 26-29)
carries the placements that touch the PRD. No ENDPOINT change.

## 1. Accepted from the compile

- **FWD-8: ACCEPT met on method_version 2, not yet realized as served** (@a108c6bd93). 10 of 14 pairs are within 0.35 pp, and
  the other 4 each carry a stated non-defect reason. It is REALIZED when `3.0.0_SA_CVO` reads one served pair after P-2.
- **W3-S1 closed** (21 tests pass). **W1-S18 disarmed** by batch 193; it closes on the served method_version 2 read, and S22
  closes with it.
- **The CVO's correction stands:** batch 193's 0.0044 pp for the S22 pair was the counterfactual. The margin balance alone gives
  0.4738 pp, which batch 195 states as RETURN. This seat's batch 200 records it.

## 2. Rows the P-2 packet already carries (confirmed, not re-placed)

W1-S12 (closed or unfunded accounts), W1-S13 (the sharded publish and its own-invoke grant), W1-S14 (the 562-partition backfill
under a never-widen half), W1-S18 (method_version 2 served), W1-S19 with W2-S3 (contract 0.3.0), W4-S1 (the summaries pass
packaging), W4-S2 (the shard timing). All are owned by `2.0.0_SA_COO~P`, in round 10 B's DB-b-18 and the P-2 packet.

## 3. Placement of the rows in no cell

| row | placed | owner | closes when |
|---|---|---|---|
| **W1-S17** (38 short-account DIV debits, 822.51 absolute, absent from the served income field) | **The next issuance, one build cell** (PRD ruling 27). Declare `dividend_interest_share_quantity` in `sources.json`; admit a DIV debit only when it is negative. Risk LOCAL. It rides the P-2 rewrite if merged first, and P-2 is never held for it | `2.0.0_SA_COO~P` | the 38 debits are in the income field and return reads DELTA=0 on every account-day, after the rewrite that carries it |
| **S15** (the read route missing from `routes.json`) | **Drain hygiene at the P-2 drain.** Name both reporting routes (the series read and batch 197's summary read) without the `api` root generating them. It is hygiene at the drain, not a cell | `2.0.0_SA_COO~P` | both routes are listed and the unguarded-route census sees them |
| **S19** (DB-7-AC1 counts landings before exclusions) | **The issuer's own amendment** (Andrew-direct 2026-09-24, the issuer amends its own criteria). Floor: 10 KEPT organic landings for `holdings_performance_daily`. Re-graded at the P-2 drain, as the served schedule has accrued organic fires since 10-01 | `2.0.0_SA_COO~P` | the criterion counts kept landings and grades 10 or more |
| **S20** (the picker's date and the body's date from two files) | **A portal item for `2.0.0_SA_COO~D`** (PRD ruling 28). Both read `series.as_of`, with no refusal | `2.0.0_SA_COO~D` | the suffix and the body read the same field on portal DEV |
| **S18** (C-NAMES prints a function never made) | **Done by this seat**: PRD addendum v0.7 ruling 26 prints the builder output for the five deployed names, checked against the live plane | `1.0.0_SA_CTO` | this addendum's commit |
| **S12** (the X10 register has no retention family for `series.json.gz`, nor for the new `summary.json`) | **The register owner's own act.** Admit gzip JSON (or a second reporting table) so both served files take a family. Not a DASHBD cell, and no outcome waits on it | `4.0.0_SA_CRO` | the register lists a family for each file and the validator admits it |
| **S8** (`fact_trn` has no per-event key) | **A stated limitation** (PRD ruling 29): no dedup, and the 0.034 pct upper bound is disclosed. The upstream question (does raw CRS carry a key silver drops?) is PARKED. The condition that un-parks it: a project owning `fact_trn`'s Schwab silver is seated | `1.0.0_SA_CTO` (parked) | that project takes the question as its own row |

W1-S7 (carried; its population limb was cut in DB-b-11) is not in the ask; the CVO closes it at the next compile.

## 4. The enrichment list the next issuance cuts (ONE issuance, `2.0.0_SA_COO~P`)

| # | item | risk | note |
|---|---|---|---|
| E1 | The P-2 packet (DB-b-18 readiness, then the packet with both halves), carrying section 2's rows | WORLD | in flight; P-6 (retire PATH A) lands in the same window as P-2's served move |
| E2 | W1-S17's build cell | LOCAL | at most three mechanical criteria; it never holds E1 |
| E3 | P-5: the ONE Black Diamond population pull, after P-2 publishes every 49 Financial account, graded against 0.35 pp | WORLD | Andrew-approved (record @fec2dc7266, card 2) |
| -- | S15 and S19 | -- | at the P-2 drain, not cells |

## 5. Outcome read (only the outcomes this compile moves)

| outcome | state | next |
|---|---|---|
| FWD-1 | live and current every trading day | P-2 widens it to every 49 Financial account |
| FWD-8 | ACCEPT met on method_version 2, not yet served | REALIZED on one served pair after P-2 |

Acts only Andrew can do for this project: none open (the population pull was answered at ~00:4xZ).

-- 1.0.0_SA_CTO
