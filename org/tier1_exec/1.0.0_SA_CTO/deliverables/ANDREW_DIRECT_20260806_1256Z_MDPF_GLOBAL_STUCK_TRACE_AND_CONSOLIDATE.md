# ANDREW-DIRECT — 2026-08-06 ~1256Z, CTO terminal (base 1.0.0_SA_CTO)

## VERBATIM

> "THe first thing we need to do for this session is trace the path/publishing of the "Global"
> scope of the Model Portfolios page. The global aggregate is stuck on July 30th, despite it being
> August 6th. All the firm scopes (49, inflection, cottonwood) are all stuck at August 3rd. I need
> you to assess where in the chain we are breaking, checking the gold-level files, any
> publishers/emitters between silver gold and platinum, and come up with a plan to streamline and
> consolidate this on schedule once and for all. Once that is done, I need you to orchestrate an
> ad hoc publishing to bring everything up to schedule as of August 5th."

Channel: CTO terminal, direct message mid-startup. Recorded + broadcast same turn per XXX.md.

## SCOPE READ (addressed seat = CTO base; no wider gate manufactured)

1. TRACE: Model Portfolios page "Global" scope publishing path. Global aggregate vintage stuck
   2026-07-30; firm scopes (49f, inflection, cottonwood) stuck 2026-08-03. Find the break(s) in
   the chain: gold files, publishers/emitters between silver -> gold -> platinum.
2. PLAN: streamline + consolidate MDPF publishing ON SCHEDULE, once and for all. This is the
   sovereign appetite already ruled 08-05 ~2235Z (@c52d9bdb0): ONE mdpf-gold-lambda carrying every
   responsibility ACTUALLY NEEDED — the owed needed-subset determination folds in here.
3. EXECUTE: ad-hoc publishing to bring everything current to 2026-08-05 (= the T-1 frontier for a
   Thursday 08-06 session; consistent with the trading-calendar default).

Note: ad-hoc catch-up publish is explicitly Andrew-ordered here (and the standing rule already
permits ad-hoc runs; the production path still needs the SCHEDULE — that is deliverable 2).

## TRACE FINDINGS (CTO base, measured 2026-08-06 1300-1355Z — grounded, each line cites its read)

**F1 — THE PRIMARY BREAK IS THE TRIGGER LAYER, upstream of gold->platinum. The publish hop is ALIVE.**
`opal-data-inf/gold/meta/pipeline-complete.json` (Door-6, the mdpf-daily-trigger's ONLY firing
event) LastModified **Fri 2026-07-31 14:56:49Z** (head-object 1352Z) — the marker never landed
again during the INF outage, so the MDPF daily chain (feeders -> WS-A -> Stage-6 spine +
cottonwood 6d legs) has not had a scheduled fire since 07-31. This is the exact CLAUDE.md
no-schedule defect class ("a pipeline whose only trigger is another pipeline's success has no
schedule"), measured live for the second time (first: 07-18, six-day freeze).

**F2 — Measured data ends 08-03 because exactly ONE chain run happened in the window:** an
ad-hoc run 08-04 ~21:59Z (platinum partition `aggregate_aua/2026-08-04.json` LastModified) that
resolved T-1=08-03 from sources. INF's eclipse leg kept producing during the outage
(`gold/eclipse/2026-08-05/_meta/gold_complete.json` exists, 08-05 14:51Z) — only the FULL-spine
completion marker was blocked. Hence 49f+inflection "measured" through 08-03, nothing after.

**F3 — The ~13:33-13:50Z daily hop (accrual bridge -> publisher path) fired BOTH 08-05 and
08-06** — gold `_aggregate_aua/2026-08-06.json` written 13:33:57Z today, platinum hyphen surface
(all four scopes) rewritten 13:50:50Z today — but it re-publishes the frozen gold: served
`as_of_last` stayed **2026-08-03** after today's write (content read 1353Z). Gold->platinum
carries; it has nothing new to carry.

**F4 — GLOBAL 07-30 IS NOT A PUBLISHER BREAK — it is the complete-data-frontier clamp (Andrew's
own 08-04 edict, ModelPortfolios.tsx:405-429) working as designed.** Served cohort_provenance:
cottonwood last "carried_at_declared_cadence(as_of=2026-07-27)" on 07-30, "absent" from 07-31 on.
The Global view clamps to the last EVERY-partner-present date = 07-30. Firm views do not clamp =
08-03. One display rule, two vintages, both honest.

**F5 — The cottonwood absence is a GOLD-LEG break with FRESH silver:** BD silver
`blackdiamond/cottonwood/silver/fact_model_assignment/` has partitions through **08-06**, but the
cottonwood slice legs (6d: dim -> pair -> slice -> global re-stage) run ONLY inside the dead
daily chain. Slice artifacts under `gold/mdpf_revamp/cottonwood/` were last rewritten by the
08-05 13:35Z hop with stale content (provenance still reads absent-from-07-31).

**F6 — Desired-vs-applied fork to fold into consolidation:** repo
`infra/aws/terraform/opal-assets/mdpf_portal_publisher.tf` locals still declare write_prefixes
`json/mdpf/*` + `json/portfolios/*` while the WO-2 header block + the live-verified CF v6 rewrite
(`/api/general/mdpf/*` -> `/platinum/mdpf/*`, portal-proxy.ts F4 @b48634789a) say the live serve
is `opal-data-portal-v2/platinum/mdpf/*` on the egress role. The repo file self-contradicts
across eras; reconcile at consolidation.

**F7 — Retired-twin residue (already ruled, not a break):** underscored
`platinum/mdpf/{,scope/}aggregate_aua_timeseries.json` (LastModified 07-31) are the RETIRED
Stage-4 twins — portal reads hyphen only; the 4 twin objects await deletion under CTO GO.

**IMPLICATION FOR THE CONSOLIDATION PLAN (supports the transcript's goals 4-6):** the fix that
closes F1 permanently is Andrew's canonical requirement itself — the MDPF chain gets ITS OWN
SCHEDULE (INF-marker as accelerator at most, never the only trigger), every firm on the same
pattern/schedule/design, cottonwood's legs promoted into the same spine cadence as 49f/inflection.
The catch-up to 08-05: one chain run (RUN_DATE=today resolves T-1=08-05) + the publish hop, with
cottonwood legs included so the Global frontier un-clamps.

## CONTEXT BINDINGS

- INF v1.7.99 acceptance run ~13:47Z today is causally coupled: mdpf-daily-refresh-trigger has
  ScheduleExpression: None and fires only on INF completion marker (`gold/meta/pipeline-complete.json`,
  DOOR 6) — the exact no-schedule defect CLAUDE.md's ad-hoc-runs rule names, measured 07-18.
- W-1a re-point RULED: `gold/mdpf_revamp/_aggregate_aua/{date}.json` (underscore form).
- Promotion-hop finding: spine-writes-canonical-grammar may kill the 09:40 accrual hop.
- MDPF json/mdpf/* teardown PARKED; hyphenated `account-distribution.json` is a LIVE SERVED
  PORTAL BELL — not to be treated as abandoned during this work.
