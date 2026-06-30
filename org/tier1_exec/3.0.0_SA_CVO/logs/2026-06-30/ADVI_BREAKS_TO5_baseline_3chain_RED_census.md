# ADVI_BREAKS TO-5 — CVO independent BASELINE RED census (inf / 49F / COT served chains)

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, TRACE
**Agent:** 3.0.0_SA_CVO | **Date:** 2026-06-30 | **Window:** ~12:43Z startup -> ~12:57Z (P0 override engaged immediately at startup)

## Context
Andrew-sovereign P0 (CTO PRD d2cae58f9, COO TO-5 GO 20260630T125339Z): DATA_ANALYTICS + DATA_SSOTMG HELD until inf/49F/COT served chains validate GREEN + CVO independent confirmation (TO-5) + prevention alarm (TO-6). CVO owns the gate-release verdict. Phase 1 = independent RED baseline (do NOT take DS/CTO findings as given). Phase 2 = re-sweep + per-pipeline GREEN/AMBER/RED after fix legs (TO-2 inf / TO-3 49F / TO-4b COT).

## Baseline — ALL THREE RED, THREE DISTINCT MECHANISMS (grounded vs LIVE served + S3 list-object-versions)

### INF — RED (stub-clobber + stale)
- served `opal-data-inf/platinum/firm/header_metrics.json` = **132B STUB** `{firm_id,generated_at,data_as_of,total_aua,client_count}`, total_aua **$202.58M**, generated_at **06-29T22:07:10Z**. Missing ~15 portal-required keys (by_architect, radial_12m, account_distribution, dates, ytd_nna, total{}). Rich header = 28830B.
- **NO 06-30 write** => served NOT following Orion 06-30 08:36ET $202.13M (Andrew anchor). Stale at 06-29 AND degraded shape.
- MECHANISM (version-history grounded): 132B-then-28830B two-writer interleave goes back to **>=06-24 (PRE-Friday)** — every prior day the rich landed SECOND and won. 06-28 CLEAN. Regression = stub re-fired **3x on 06-29 EVE (21:29:20 / 21:40:30 / 22:07:10Z)** AFTER the rich 14:34Z write -> stub is last-writer = served. `inf-portal-publisher` = 1 invocation/day (CW one stream/day) so it is NOT the late writer; late writes are off-cadence (manual / canonical re-run).
- CORRECTS CTO's "NEW emitter from Friday 06-26 work" — emitter is OLD; the NEW behavior is the evening re-fire. Exact emitter INFERRED per Rule 22 = TO-1.
- Confirmed source: `INF_D_00.portal_aggregates.py:898` writes the RICH header (no stub path); `INF_D_04` writes the gold/artifacts/summary/ 28830B artifact (different key). Thin emitter is a THIRD writer.

### COT — RED (as_of-pin)
- served `opal-data-cot/platinum/firm/header_metrics.json` = **728B**, RICH shape, file **REGENERATES DAILY** (latest 06-30T02:19:27Z — healthy cadence) BUT **data_as_of FROZEN at 2026-06-26**. total.aua **$432.46M**, client 217, account 805.
- Producer runs; the DATA as_of is pinned 4 days stale. Distinct from INF (file fresh, CONTENT stale).
- SMELL FLAGS: nna_qtd==nna_ytd==nna_12m all == $396,987,695.43 (q1/q2/q3 all 0.0 — collapsed into q0); by_architect 100% "Unassigned".

### 49F — RED (stopped-publisher)
- served `opal-data-bd/platinum/firm/header_metrics.json` (firm_id 49financial; bucket = **opal-data-BD** per Andrew) = **1648B**, RICH shape, total.aua **$1.745B**, client 3047, account 6685, data_as_of 2026-06-24.
- **FROZEN since 06-26T05:00:19Z** — ZERO writes 06-27/28/29/30. Publisher STOPPED after Friday 06-26. No `_fresh` key exists.
- Distinct again — not a stub, not a pin; the publisher just stopped.

## Common thread
All three onset at/after **Friday 06-26 canonical/SSOT work** -> blast radius CONFIRMED across all 3 firms, 3 different break modes. Independently corroborates Andrew's "Friday changed PROD"; refutes a single-emitter framing.

## Residual unknowns (carried into fix legs)
1. INF exact thin-emitter file + why it re-ran 06-29 eve (TO-1, ~A).
2. COT: is 06-26 the latest as_of Schwab provides, or is upstream fresher and the pin is a bug? base-DS must ground the as_of SOURCE (TO-4). + nna-collapse / Unassigned-architect smells.
3. 49F: what stopped the BD publisher after 06-26T05:00 (TO-3, ~B).
4. Custodian PARITY numbers (served-vs-source AUA delta) not yet compared per firm = the GREEN-gate measurement for Phase 2; baseline RED rests on staleness+shape (already decisive).

## Compiler Tools
| Tool | Run | Result | Note |
|---|---|---|---|
| comp-freshness chain inf | INF upstream silver/gold | PASS (mostly) | upstream fresh 06-29; the defect is at the SERVED platinum key, downstream of these |
| comp-pipescript io INF_D_00 / INF_D_04 | header_metrics writers | PASS | INF_D_00:898 = rich served-key writer; INF_D_04 = gold-artifact writer (different key) |
| pipescript advi-inf --resource | producer map | PASS | shared-advisor-router serves platinum/firm/* per firm bucket |
| live aws (s3api list-object-versions / cp, CW describe-log-streams) | the version-history forensics on all 3 served keys | PASS | rail-checked; the decisive ground (clobber/stale/stopped pattern per chain) |

**What worked:** version-history (list-object-versions size-over-time) was the decisive tool — it dissolved CTO's "new Friday emitter" lead into "old emitter, evening re-fire" for INF, and cleanly separated the 3 mechanisms (clobber / pin / stopped). Ground-before-accept held: did not take the DS/CTO framing as given.
**Gap:** exact INF thin-emitter not yet pinned (Rule-22 INFERRED) — handed to TO-1 with a sharpened hunt (what re-ran 06-29 21:00-22:10Z emitting the thin shape).

## Addendum (post-baseline) — 49F CHANGE-EVENT C REFUTED + bucket confirmed (source-grounded)
- 49F TRUE served key = **opal-data-BD**/platinum/firm/header_metrics.json (per Andrew + grounding). The opal-data-INF header_metrics_fresh.json (324B/06-29) is INF's own _fresh (INF_D_00e), NOT 49F. Served writer = `data/black_diamond/scripts/gold/D_00.portal_aggregates.py:725`.
- CHANGE-EVENT C (Schwab-SSOT canonical interfering with 49F) — REFUTED as the freeze cause (Rule 22 source-confirm): canonical-schwab DOES write opal-data-bd (co-tenancy: `build_canonical_daily.py:48` + all `canonical/schwab/gold/*` BUCKET=opal-data-bd), BUT `build_gold_portal_aggregates.py` is explicitly **"NOT served"** (L132,137), writing an isolated `canonical/schwab/gold/.../date=/data.parquet` partition — NOT the served JSON key. Decisive negative: 49F served has ZERO writes after 06-26T05:00 (a clobber would show writes). => 49F freeze = **CHANGE-EVENT A only** (BD bronze dark 06-19 SS&C MFA -> D_00 ran on frozen silver -> froze 06-26). Fix = ADVI_BDAPIMIG.
- LATENT risk banked for TO-6/SSOT: if a future canonical change ever re-points build_gold_portal_aggregates at the served key, 49F inherits INF's exact two-writer failure.

## Phase-2 rubric (locked to PRD §4 A-F)
Per-pipeline GREEN only when ALL pass vs SERVED/custodian: A(chain map) / B(single-writer) / C(freshness: data_as_of==true date AND advances daily) / D(custodian parity within tol) / E(schema: all portal keys present) / F(trigger health). INF additionally must pass the TO-2 size/shape gate. ALL-GREEN x3 + TO-6 alarm live = CVO gate-release.

## Blockers
None for the baseline (delivered). Phase-2 GREEN/AMBER/RED verdict is event-gated on the fix legs TO-2/3/4b landing.

— 3.0.0_SA_CVO
