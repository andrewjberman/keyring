# CVO~A -- Andrew-direct: 14-cohort DAILY-AUM assessment -> blueprint COMMISSIONED as OPAL_ASSETS; source map reconciled; G6 validation staged

**archetype:** EXPLORE
**secondary_archetypes:** VALIDATE, COORDINATE

**Window:** 2026-07-12T23:32Z (the MSTR dispatch) -> 2026-07-13T00:23Z. 4 deliverable commits + 1 fixture-generator. All RAVC'd + accepted.

## Summary

Andrew-direct assignment (via MSTR): assess our automated DAILY AUM recording for Manav's 14 cohorts + author the plan to make all 14 bullet-proof before the manual weekly tracker retires. Sovereign clearance: the 49F/bd/Schwab ban LIFTED for me, THIS assessment, READ+PLAN only -- held throughout (zero writes to any firm pipeline; no external comms). The assessment became the BUILD BLUEPRINT Andrew commissioned as macro_project **OPAL_ASSETS** (CTO~B owns the PRD; my brief is the seed). Then grounded + reconciled Andrew's own source map: **convergence job CONFIRMED** -- 6/7 sources exist + run daily; only Schwab BD master 08335338 is missing.

## Deliverables (all committed + pushed, org/tier1_exec/3.0.0_SA_CVO/deliverables/)

1. **b2a17a7e3 -- the 14-cohort assessment + build blueprint** (commissioned as OPAL_ASSETS). Grades: 5 SOLID
   (4 ETFs fund-level + Inflection) / 8 PARTIAL (ONE root cause: the mdpf 49financial block ROLLED-FORWARD-STALE
   since 07-06 -- served aggregate_aua 07-10.json carries as_of=07-06) / 1 SILENT GAP (**Schwab BD master 08335338 =
   0 hits in 21,153 files; the entire ingest is hardcoded to SmartX 08242234**). Gap map G1-G6 with exact-build +
   owner-lane + clearance per gap. Honest interim: NOT yet a safe replacement for the manual backup until G1+G2 land.
2. **80bc2d51c -- the G6 validation protocol** (I validate; AE~A builds via COO): 6 assertions w/ falsifiers
   (fires-on-stale / silent-on-fresh / per-cohort-discrimination / rolled-forward-ages / missing-fails-LOUD-explicit-99
   / never-blocks-the-run), real-path method via the checker's env seam. Live baseline: the global alarm WORKS and is
   FIRING (staleness=2) -- G6 is additive; + a vintage discrepancy flagged (timeseries as_of_last=07-08 vs partition
   as_of=07-06) -> AE~A resolved per my finding (per-cohort OWN-field as_of).
3. **0b715fc9f -- the G6 fixture generator** (4 variants: fresh-all/one-stale/mixed/one-missing), co-authored to
   AE~A's LANDED parser (46d8be80d field-reads), dates computed vs the run day, shared-calendar caveat disclosed.
4. **e41c49683 -- Andrew's source map GROUNDED + RECONCILED**: TrueShares scrape (etf_netassets_watch/etf_probe.py,
   daily) / Pathfinder = FILEPOINT direct-CSV (PFOE/PFDE not on TrueShares; float floor 2026-05-18) / Orion = the INF
   gold chain (orion-gold-dispatch.sh) / Eclipse (opal-data-inf/gold/eclipse/, trading-daily) / Cottonwood
   (opal-data-cot/gold/positions_cube/, nightly, firm-separated) / SmartX SDD 08242234 (2.5yr daily CRS) / 08335338
   MISSING. **D1 divergence (the sharp catch): Andrew maps 49F ETF holdings to 08335338, but the HELD 08242234 RPS
   already carries ~$153M 49F DIVZ -- both-masters-dedup interim; the pull resolves.** D2: Filepoint 05-18 floor.
   D3: "already daily" is true at source, stale at the served rollup (G1 = freshness repair).

## Key rulings/decisions received

- Andrew commissioned OPAL_ASSETS (CTO~B PRD; my brief = seed; handed off + confirmed).
- Andrew GO'd the 08335338 investigation: 0.7.0 pulls (schwab-si2 REST); I ASSESS (look-back depth + contents).
- The LINCHPIN criterion (Andrew via MSTR+COO, refined): Schwab data is COMPLETE via files -- .rps=RPS positions
  (his recollection corrected from the estate: ".rds"=RLD realized lots; ".ult"=ULN unrealized + a real ULT too) --
  so grade PRESENCE+COMPLETENESS+LOOK-BACK of the CRS set for 08335338, constructability not endpoint-existence.
  PRE-ANSWERED from held artifacts: RPS IS direct PIT snapshot holdings; 08242234 holds the complete set daily since
  2024-01 -> the constructability thesis is CONFIRMED for the SmartX master; open = does the set FLOW for 08335338 +
  depth (2021 target; held for NEITHER master today).
- COO G6 ruling (a): the static EXPECTED_COHORTS taxonomy -> cohort-8 (08335338) alarms MISSING daily until G2 wires
  the pull (the alarm doubles as the G2 progress tracker). My sovereign-watch: the constant stays taxonomy-not-firm-data.

## Compiler Tools

| Tool | Run | Result |
|---|---|---|
| pipescript (mdpf/--list) | thread grounding | PASS -- mdpf-global-view = the core rollup |
| comp-grep (incl --include-held under the scoped clearance) | source/master/float greps | PASS -- the 08335338=0-hits finding |
| comp-freshness HUD rail | nudged raw s3-ls twice | complied via rail-checked markers (census-not-single-artifact reads) |
| aws (operational reads: s3 ls/cp, cloudwatch describe/get) | live artifact + alarm grounding | PASS -- the rolled-forward + alarm-firing evidence |

- What worked: grounding Andrew's map against held artifacts pre-answered half the linchpin before the pull.
- Gap found: none new (the assessment IS the gap census).

## Blockers

None. All remaining legs are event-gated externally (not blockers): 0.7.0's 08335338 pull -> my linchpin verdict
(incl D1); AE~A's TF alarms -> my G6 exercise; CTO~B -> scoping questions.

## Current State (handoff)

- OPAL_ASSETS commissioned; CTO~B has the brief (b2a17a7e3) + reconciliation (e41c49683) + D1/D2/D3 as PRD inputs.
- G6: AE~A's checker landed (46d8be80d, their commit); TF alarms building; my protocol (80bc2d51c) + fixture
  generator (0b715fc9f) ready -- exercise on their deploy ping. Cohort-8's alarm SHOULD read ALARM from day one
  (a standing live A5 until G2) -- if it reads GREEN before G2, that itself is a defect.
- 08335338: 0.7.0 pulling; my verdict rubric locked (CRS-set presence/completeness/2021-depth/constructability + D1
  both-masters resolution), FP-R1-classed per claim, to MSTR+COO+CTO~B on landing.
- Sovereign: the scoped clearance was used READ-only, exactly as leashed; the standing 49F ban holds everywhere else.

## Next Steps

- **[me]** exercise G6 on AE~A's deploy ping; verdict the 08335338 pull on 0.7.0's landing; answer CTO~B scoping.
- **[0.7.0_AE_CloudOps / ~A]** the 08335338 pull; the G6 TF alarms.
- **[1.0.0_SA_CTO~B]** the OPAL_ASSETS PRD (post AoR go-live).
