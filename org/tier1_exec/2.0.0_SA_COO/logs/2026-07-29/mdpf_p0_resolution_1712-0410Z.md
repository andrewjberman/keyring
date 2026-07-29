# 2.0.0_SA_COO -- MDPF P0 resolution: acceptance, flip, and the client-side clobber (2026-07-28 17:12Z -> 2026-07-29 04:10Z)

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE, TRACE

## Window

Continues `session_close_1258-1712Z_mdpf_p0_sweep_coordination.md` (@4e70e1c6d). Covers the
full MDPF end-to-end resolution: my acceptance diff, the DT flip, the client-side re-derivation
finding, the ETFS rebate exposure, and four Andrew-direct scope changes.

## What I did

### 1. The full-axis acceptance diff -- the gate that held the serve (PASS)

A = `json/mdpf/global/aggregate-aua-timeseries.json` ETag `5f758b47...` 254,419 B
B = `platinum/mdpf/global/aggregate-aua-timeseries.json` ETag `31e64570...` 200,059 B
Both downloaded and MD5-verified against their ETags BEFORE comparison.

DENOMINATOR: A n=447 (2024-11-01..2026-07-22), B n=450 (..2026-07-27), shared 447, A-only 0.
PREDICATE: exact equality of `opal_aggregate_aua` per shared date.

| criterion | result |
|---|---|
| 31 moved dates restored | **0 movers / 447 shared** |
| 3 frontier dates | 07-23 1,945,099,231.62 / 07-24 1,947,435,361.40 / **07-27 1,950,519,805.86** |
| the +136,978,678.52 seam @07-20/21 | **GONE** -- measured +13,083,893.86 |
| labels | point_class {measured 395, absent 24, interpolated_estimate 31}; cottonwood slot **45/2/3/400** -- DS's prediction exactly |

**THE FINDING THAT JUSTIFIED THE METHOD: the total was clean and the components were not.**
`model_aua` and `non_model_aua` each moved on 2025-11-03 and 2025-11-18 by +$0.01/-$0.01,
NETTING TO ZERO on the total. A total-only diff would have reported clean and been right by
luck. Also surfaced: `account_count_total` 41 diffs (40 = added coverage None->value; ONE
genuine mover, 07-22 8094->8099, Andrew-accepted as new holdings); `cohort_provenance` 447/447
differing but PURELY ADDITIVE (`as_of_by_partner` appended, partner labels byte-identical);
`meta.trading_day_calendar` changed hardcoded-fallback -> `pandas_market_calendars`
(Andrew-RATIFIED as wanted); `meta.composed_backfill` absent in BOTH sides = pre-existing, not
a regression.

### 2. Rulings issued

- **MDPF_INFACTUAL.001** @`991a04d761` -> DS~A: inflection ETF must use ACTUAL positions, not
  target weight. Later CLOSED AS MOOT (below).
- **CONSUME over recompute** for the ETF leg -- then SUSPENDED, then MOOT.
- **Catch-law (COO half, CTO-ratified):** *a fetcher's `catch` may return `null` or throw --
  NEVER a number.*
- **Carried-point idiom:** mark on PARTNER-LEG provenance, never rolled-up `point_class` (the
  3 frontier dates read "measured" globally while cottonwood is carried); visible WITHOUT
  interaction; three classes never collapsed; carried must NOT read as alarm.
- **Teardown-wave sequencing** + 4 constraints, all CTO-ratified. Load-bearing one: **the unit
  of retirement is the WRITE, not the PRODUCER** -- Stage 3/WS-A also feeds the gold-DDB accrual
  until 4c lands, so producer-level retirement would starve the emitter.

### 3. Grant landed (SoD)

`3a9c4bd3ab` -- `PUBLIC_DATA_ROUTER_DEPLOY`, full CLOUD_OPS_OR_ETL AE set (10) PRESERVED
verbatim + `0.2.0_DT`, scoped to `infra/aws/lambda-edge/public-data-router/**`. Machine-verified
no-AE-regression before commit (AE set is a strict subset; MISSING = []). **4th instance of the
identical DT-enumeration gap; the prior three each began with an audited override and closed the
lane afterward -- this one closed FIRST, so DT's deploy record carries zero overrides.**

### 4. Registry drift closed

`5f51f7ebb8` -- committed the uncommitted tail of Andrew's 07-14 renames (`PFMG_TAXSMA` ->
`OPAL_TAXSMA`, `TCKT_CENTER` -> `OPAL_TICKET`). Verified both successors present with real
content and REGISTRY rows before landing the deletions.

### 5. Memory index restored under the load cap

`MEMORY.md` was **17,733 B against a 17,408 B cap -- 325 B already silently not loading.** Now
17,346 B, entire file loads (positive control: last line inside the window). Added the Aug-1
clock + the ETFS rebate exposure; compacted the tail browse-index (auto-recall unaffected).

## The two findings that mattered most

**(a) THE CLIENT-SIDE RE-DERIVATION.** Twelve hours of route/bucket tracing never found it
because it was in the browser. The page ignored the canonical `opal_aggregate_aua` and rebuilt
its own total: `trendLastPoint.aum (7 non-SMA by_model legs, 1,672,708,163.51) +
getNonModelAumForDate(non_model_assets.time_series) (232,313,972.65) = 1,905,022,136.16`
rendered, vs the artifact's own 1,950,519,805.86. GAP 45,497,669.70 = platinum non_model
277,811,642.35 - legacy 232,313,972.65. **Andrew had named this exact drift at ~1743Z the
previous day; we kept looking for it server-side.**

**(b) ETFS_AVGCAP IS A PARTNER-REBATE BASIS AND JUNE SHIPPED MISLABELED.** June 2026 went out
`partial=false` on 17/30 written days, tail carried from 06-24 (~13% of basis weight).
**BOTH guards are structurally blind:** AC6 reports the OLDEST input, so a dead-tail month is
byte-identical to a healthy one; and `partial` keys off CALENDAR coverage, which carry-forward
satisfies by construction. July would have been 3 real days / 28 carried on a $521,948,667.35
basis. Root cause of the dead 49F leg: **never scheduled BY DESIGN** -- TF landing commit
`349c91e35b` says verbatim *"NO event trigger (S-D2 monthly batch, rides next Schwab batch)"* --
and the last hand-fire (07-14) walked to the then-frontier 07-06 during an RPS freeze and nobody
re-fired after the unfreeze. Coherent design that expired when the source went daily and the
purpose became a rebate.

## Corrections I made against myself

1. **Asserted live state across an unmeasured event.** Told CTO "AWS untouched / serve
   byte-identical" ~15 min after the flip had applied. Retracted; DT surfaced it.
2. **Source-read lost to runtime.** Claimed the scope-less fetcher was the headline from
   `portal-proxy.ts:497-507`; DT's runtime capture showed ZERO component callers. My acceptance
   diff covered the right artifact after all -- but I said so nowhere at the time.
3. **Wrong attribution passed to DE** ("another agent's in-flight edits blocking your push") --
   measured false; it was pre-existing tree debt.
4. **Manufactured a false dilemma on the as-of stamp.** Turned Andrew's expected RESULT (07-27)
   into a TARGET, creating a phantom conflict with "derive from the data" and an escalation path
   for a non-problem. Andrew: *"IT IS NOT VERY COMPLICATED."* Struck it.
5. **Over-dramatized the audit-attribution defect.** Andrew: *"dont be so dramatic... its not an
   existential crisis."* Correct -- it is a bug MSTR will fix.
6. **Mis-imported an acceptance bar**: put a bias constant measured on the 49F RPS leg into an
   INFLECTION acceptance test (-1..-3%); measured drift was -13.1%. A correct check aimed at the
   wrong population -- the third instance that night, and mine.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-grep` | `ETFS_AVGCAP` | PASS | found the whole prior-art estate Andrew pointed at (PRD + 3 per-partner producers + avgcap engine) |
| `git grep -ril avgcap` | denominator 172 files | PASS | printed the denominator beside the verdict |
| `comp-surface-check` | auto in safe-commit x3 | PASS | "no critical surface" on all three commits |
| `comp-pulse` (risk-reflex) | auto, pre-commit | PASS | DENOMINATOR 2 files vs 1568 danger nodes -- a measured clean, not a default |

**What worked:** `comp-grep` on `ETFS_AVGCAP` returned the entire parallel ETF-ownership pipeline
in one call -- the finding that reframed the whole ETF lane.
**What failed:** the `aws` PATH shim, all session. `~/bin/aws` strips `/c/Users/.../bin` from PATH
before re-invoking, but this shell's PATH carries the `/cygdrive/c/...` form, so the strip fails,
the shim re-finds itself, and a bash script gets executed through Python. Worked around via the
awscli Python entry point directly. Same mount-form class as MEMORY-13's `mount -f C: /c`.
**Gap found:** no comp-tool answers "which served artifact does this rendered figure come from" --
that question cost this estate twelve hours and two wrong answers tonight, and it was finally
answered by a runtime DOM capture, not by any instrument.

## Blockers

None held by me. All open items are gated on scheduled events or other lanes.

## Current State (zero-context handoff)

- **MDPF flip is LIVE.** PROD `1f363956`, tag `portal-v2.1.149` (peeled-verified), CI success,
  parity gate 0 bytes. Edge router v6 maps `/api/general/mdpf/` -> `/platinum/mdpf/`.
- **Global headline is a FIELD READ** of `opal_aggregate_aua`, renders $1.95B. Forced-failure
  control: em-dash + entire trend panel absent (graceful-degrade branch DELETED, not unused).
- **As-of stamps DERIVED** -- footer "July 27th, 2026, 5:00p ET" from `as_of_last`, with
  per-element vintages named beside it ("Model detail as of 2026-07-23 - Client Holdings as of
  2026-07-23"). Nothing forced.
- **Carried points render distinguishably** -- band + heavier border + label (daily), date-exact
  slate outline on the Jul-27 bar, legend chips both charts, tooltip names leg + as-of.
- **D4's COO half CLOSED** on DEV `f6c11812`. Remaining: DT's Oracle-1 on the served bundle.
- **bd-49f writer LIVE** + backfilled (floor `cron(45 10)`). **ETFS CSV patch deployed**
  (`etfs-reports-v1.1.0`), QA-invoke exercised on the deployed runtime BOTH directions, 3 days
  ahead of the Aug-1 shot. **`non_model_assets` retired at the WRITE** and objects deleted
  ~03:52Z -- consumer removed first (PROD 03:31Z), correct order, verified.
- **ETF decomposition: no consumers AND no mandate.** Provenance from git: born
  `7c09fccf1b` 2026-05-18 11:52 as an internal WS-A implementation detail; 49F's leg replaced
  with measured RPS actuals `8d93255582` SEVEN HOURS LATER the same day; inflection left on the
  estimate citing materiality (~$18mm, grew to ~$58mm). Andrew: *"I never asked for
  target-weight ETF Decomposition."* Deletion rides the teardown wave -- **`identity_2` is a
  live gate computed FROM the block; preserve-or-replace FIRST, and pin the unexplained
  daily-advance mechanism before any edit.**

## Next Steps

- **[2.0.0_SA_COO]** Teardown wave, post-fires, gates 0-4. **C6 (Q-cell `enterpriseQ ??
  metricsData.priorLevel` -- a live fallback that ACTIVATES on canonical failure and shifts
  Q2 $1.77B -> $1.76B) is TOP-RANKED**, above the four stale chart routes. Then C7
  (`getNonModelAssets()` aimed at a deleted object).
- **[2.0.0_SA_COO + 1.0.0_SA_CTO]** Benchmarks/peers have NO canonical platinum location --
  design ruling, and it does not get solved by pointing them at the nearest artifact.
- **[0.7.0_AE_CloudOps~A]** 10:45Z 49F first-fire acceptance; 15:15Z no-regen check; 4c after
  the 17:15Z fire. **Aug 1 10:00 ET CSV deadline -- named owner.**
- **[0.4.0_DE_ClientPlatform]** FactorTilts zero-weighting (recommended pulled FORWARD of the
  wave -- it silently weights AGG on an empty map when `getAUMMetrics` catches, a wrong ANSWER
  rather than a wrong picture).
- **[ANDREW]** June rebate disclosure to the partner; whether `/prod-deploy` authoring promotes
  under his personal identity is intended.
- **ALL LANES: today's 15:00Z / 16:15Z / 17:15Z unattended fires are the ONLY evidence any of
  this holds on a schedule. Every run in this window was a hand-run.**
