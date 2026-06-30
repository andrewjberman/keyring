# 49F respawn: 23:00Z co-verify STAGED (penny-test to the cent) + allocations RETRY-NET design (CTO-blessed)

**archetype:** MIXED
**secondary_archetypes:** COORDINATE, VALIDATE, DIAGNOSE
**serial:** 0.6.0_AE_PartnerETL | **date:** 2026-06-30 | **window:** ~22:00Z (RESPAWN, prior session dropped ~21:46Z PID 22212) -> ~22:25Z | **checkpoint** (23:00Z verdict pending)

## Summary

RESPAWNED mid-49F (MSTR re-spawn per COO standing-hold). Re-armed reachability (watcher Monitor b3piybf3o), RAVC'd COO clean-resume, and STAGED my leg of the 23:00Z 49F served-flip penny-test to the cent with CTO + 0.7.0. Grounded the live served state (resolved the serve-vs-hold ambiguity with live artifacts), surfaced the serve-vs-hold fork to COO (now Andrew-gated), and got CTO sign-off on the durable allocations RETRY-NET design (option-a parameterize, implement post-serve).

## Co-verify staging (my leg = bd-side lineage + penny + gold-convergence)

GROUNDED against live artifacts (not self-report):
- **Served now** (platinum/firm/header_metrics.json gen 19:39Z; portal-origin gold/artifacts/summary/header_metrics.json): data_as_of=**06-26**, total.aua=**$1,816,267,427.27**, 2885 clients / 5937 accts / by_architect(10) intact. NO $0, NO stub. (0.7.0 independently penny-matched the same value off the CDN origin.)
- **Lineage penny-match (silver->cert->served), recomputed myself:** silver/allocations/2026-06-26 (6,807 rows) non-liability account_market_value sum = $1,816,267,427.27 == 06-26 cert.certified_aua == served, diff **+0.00**.
- **Exact expected values, both branches:** HOLD = $1,816,267,427.27@06-26 ; FLIP = **$1,831,666,360.06**@06-29 (silver/allocations/2026-06-29, 6,812 rows non-liab sum; gross $1,828,446,414.98 — non-liab > gross because liabilities are negative). DS~B independently replicated the flip value to the cent.
- **Mechanism (Rule 22, DS~B-grounded):** 23:00Z DEFAULTS to the FLIP — B_00 `--force-recent-days 14` (gold_dispatch.sh:84) auto-seals 06-29 over the max-sealed=06-26 watermark; D_00 serves as_of=perf.date.max(). So a flip needs no seal; a HOLD needs an active Andrew never-widen gate (COO->Andrew, in flight).
- **CTO Rule-22 deepening folded in:** tonight's penny-test also asserts the restored 23:00Z gold_aua CONVERGES toward the cert (the 19:3xZ gold = $1,626,516,968.05, 11.67% LOW, PREDATES the 21:39Z unrealized re-land; the 23:00Z gold must rebuild on it). Converges -> pipeline-break-fixed proven; still diverges -> ESCALATE (override may mask a hole).

**Penny-test harness staged** (scratchpad/penny_verify.py — one re-runnable command). Pre-run baseline: CK1 served==cert PASS (+0.0000), CK2 served==expected[06-26] PASS, CK3 no-$0 PASS, CK4 shape PASS; the two gates I OWN correctly still OPEN pre-run — CK5 gold-rebuilt-post-21:39Z FAIL (client_performance 19:36:03Z), CK6 convergence FAIL (gap still 11.67%). Both flip to PASS when the restored 23:00Z gold lands.

**Producer-side readiness:** the 23:00Z trigger = `bd-gold-nightly-fallback` EventBridge rule, state=ENABLED, cron(0 23 ? * MON-SAT *); today Tue -> WILL fire. No no-show risk.

## 3-way independence (settled w/ CTO + 0.7.0)

- ME: bd-side silver->cert->served lineage + penny + gold->cert convergence + gold-freshness gate.
- 0.7.0: served portal/CDN end-to-end (origin penny-matched; cache-gap RESOLVED — publish invalidates /advisor-intelligence/* per live invalidation IDs).
- CTO: gold/cert + the Orion-to-the-cent bar (the real GREEN-vs-Orion is the 06-29 flip = tomorrow's definitive verify -> 2-of-3 GREEN). Tonight = rescued/clean/safe (hold or flip, NOT a freeze, NOT $0).

## Allocations RETRY-NET design (durable, CTO-blessed, implement POST-serve)

Root cause grounded: the BD DataMining allocations export on T-1 timing returns a ~4,592B header-only XLSX; `download_export` only rejects <100B and `ingest_table` guards completeness only for table=='holdings' -> the stub landed over the good partition -> silver stub -> C_02 would certify $0. **Allocations is unprotected.** Fix = generalize the existing CTO-blessed holdings DATEMODE-B retry-net (completeness floor + reject-don't-land + write-after-land sidecar + valued-re-pull sweep + e2 alarm) to allocations. CTO ruled **option (a) parameterize-by-table** (one source of truth, all 4 tables) with the HARD GATE: holdings path byte-identical (extend test_retry_net.py with a holdings no-regression case + an allocations row-count-floor case, both green pre-deploy). Concurrency-governor grounded N/A for 49F (4 sequential single-report exports, no serial fan-out — CTO thread closed). Shared cot/bd code -> coordinate the touch with the cot lane (0.4.0 + 0.7.0, retry-net co-authors); deploy to BOTH opal-data-cot/code/bronze/ + opal-data-bd/code/bronze/ after the serve. Brief: docs/briefs/bd-49f-allocations-retry-net-design-20260630.md (2202c3355).

## Compiler Tools

| run | result | note |
|---|---|---|
| comp-freshness chain bd | PASS | grounded all 4 BD silver PASS (alloc 19:18Z restored, unrealized 21:39Z) + the full gold canonical chain advanced ~19:1x-19:3xZ; the producer-side freshness map for the co-verify |
| comp-grep (certified_aua / D_00 keys / cot_bronze_ingest / 390224) | PASS | located the C_02 cert producer + D_00 served resolver + the shared ingest + its invokers; carried SYSTEMS-CONTEXT |
| comp-blast cot_bronze_ingest | NOT-FOUND | bronze script not in the gold trace-graph; fell back to comp-grep for the invoker/consumer set (test_retry_net.py + cot-exporter user-data + bd-49f-runner) |
| comp-glob (pull*alloc* / cot_bronze_ingest / bd-49f-runner) | PASS/0-hit | located the shared ingest + the runner Lambda |
| comp-which (gold trigger arming) | ROUTED-no-fit | no comp-tool covers EventBridge schedule arming -> rail-checked raw `aws events list-rules` |

What worked: comp-freshness chain bd is the single best producer-side readiness lens (silver+gold+ddb in one call). comp-grep SYSTEMS-CONTEXT routed me straight to the C_02/D_00 cert chain. What failed: comp-blast can't see bronze scripts (gold-graph only). Gap: no comp-tool for (1) reading an S3 JSON artifact's VALUE for a penny-test (comp-freshness gives status not value -> rail-checked aws cp), (2) EventBridge schedule/state arming.

## Blockers

None. The 23:00Z run is a legitimate external-event gate (NEVER#4 — verify on the scheduled run); the serve-vs-hold is an Andrew never-widen decision in flight via COO. Not assumption-blocks.

## Current State (handoff)

- **Reachability:** registered LIVE PID 28704; watcher Monitor task **b3piybf3o** persistent.
- **Penny-test:** scratchpad/penny_verify.py (one command) — re-run when the 23:00Z run publishes (DS~B will ping on gold-rebuild+platinum-republish; I ping DS~B+COO if gold canonical LastModified < 21:39:59Z). Expected: HOLD $1,816,267,427.27@06-26 OR FLIP $1,831,666,360.06@06-29, to the cent, + CK5/CK6 -> PASS.
- **Serve-vs-hold:** Andrew-gated (COO relaying). Default mechanism = FLIP (--force-recent-days 14). Covered to the cent on both.
- **Retry-net:** design committed 2202c3355, CTO-blessed option-a; implement + extend test_retry_net.py + deploy both code paths POST-serve, after cot-lane (0.4.0+0.7.0) signoff.
- **Pending TOs (unchanged):** ADHC_GLDINC.SS4c.ae-periodic-oracle-revalidation; ADVI_BDAPIMIG.P1.ae-productionize-runner (retry-net is part of this); ADVI_COTETL.L4-GUARD.

## Next Steps

- **[0.6.0_AE_PartnerETL]** (me) on 23:00Z run completion: run penny_verify.py -> RAVC verdict to CTO + reply DS~B; then POST-serve pick up the allocations RETRY-NET (option-a parameterize + test extension + 2-path deploy) after cot-lane signoff.
- **[2.0.0_SA_COO]** relay Andrew's serve-vs-hold ruling.
- **[1.0.0_SA_CTO]** gold/cert + Orion-to-the-cent leg; tomorrow's definitive clean-flip verify -> 2-of-3 GREEN.
- **[0.4.0_DS_ClientPlatform~B]** served-side 5-tie|HOLD verify on the 23:00Z outcome; cot-lane retry-net signoff (post-serve).
- **[0.7.0_AE_CloudOps]** served/CDN leg verdict at flip-time.
