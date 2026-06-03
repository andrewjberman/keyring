# 0.6.0_AE_PartnerETL session log — 2026-06-03 work_1510Z

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, DEPLOY

## Context — Andrew assigned bd-pipeline owner; routed in for advisor-timeseries dual-writer fix

Session start: registered, watcher armed (Monitor task `basfjgeza`), `/work 20m` cron `23b8bca2`. No pending TOs at start. Within first cycle, COO routed me in (Andrew-assigned bd-pipeline owner) for two asks (144339Z + CTO 144709Z/144951Z + 0.7.0 handoff 145059Z).

## (A) ADHC_BDTSCLB.001 — D_02 sole writer of advisor timeseries — SHIPPED bd-v2.25.0

**Problem:** served `platinum/advisors/{id}/timeseries.json` <- D_04 pass-through of gold `gold/entities/advisors/{id}/timeseries.json`, which had TWO writers — D_02 (RICH: per-role aua, fee splits incl `total_aua_fee_paying` + `nna_canonical_fee_paying`, canonical NNA) and `bd-portal-advisor-publisher.build_advisor_timeseries` (SIMPLE subset, via GLDRST `_dual_write_key` :74-75 onto D_04's read key). Async fan-out every publish (bd-portal-publisher:1965). Masked only by cascade ordering; any reorder wipes the rich fields = breaks shipped 49F NNA-mode toggle + incoming W2b AUM split.

**Superset proof (CTO hard gate) — MET:**
- FIELD: publisher per-row {date,total_aua,cum_inflows,cum_outflows,nna} strict-subset of D_02 (D_02:2053-2113 emits all 5 + rich). 0.7.0 empirical (live abby_horton, 763 rows/32 keys) + my code-read agree. No unique publisher field.
- COVERAGE: publisher groups `architect`-only; D_02 melts all 5 roles -> superset advisor set. D_04 serves from D_02 set.
- CONSUMER CHECK: 3 live readers of the entities key all consume D_02's superset; publisher's legacy `gold/advisors/{id}/timeseries.json` primary write has ZERO live readers (grep + comp-blast no node).

**Fix:** removed `build_advisor_timeseries` call (:1147) + fn + Step-5/7 prints + dead `_dual_write_key` timeseries branch. KEPT `build_advisor_mix_timeseries` + book dual-writes. INF untouched (separate `inf-portal-advisor-publisher`, sole builder there). Also cleared pre-existing in-file ruff debt (zero behavior change): `from __future__ import annotations` (FA102 on `str|None`), drop unused numpy, `# noqa: E712` on intentional pandas-mask comparisons, drop F541 f-prefixes.

**Deploy chain:** ds-commit-gate exit 0 -> commit `99ade9b65` -> build-and-upload (sha `RBnudmPq...`) -> tf plan (1 in-place, only bd_portal_advisor_publisher) -> safe-apply (HALTGT pass) -> 0-diff verified -> comp-iam no delta -> pipeline_inventory `58b1165` -> record-terraform-deploy `bd61d75e2` -> tag `bd-v2.25.0` + push --follow-tags (pre-push HALTGT pass).

**AC status:** AC1/2/3/5 DONE. AC4 (CVO served-parity, CTO mandatory close-gate) OPEN — rides the W2b run output. RAVC2 to COO/CTO/DS sent (150753/150800Z); all 3 accepted (COO 150934Z spawning CVO, CTO 150851Z deployed-pending-AC4).

## (B) W2b D_02->D_04 run — BLESSED path + run-mechanism owned; fork surfaced

Blessed DS's path (D_02 --upload -> D_04 --upload). Took run-mechanism option (b): I drive on bd-gold-layer-runner (own the EC2). Prepped scoped cascade `infra/aws/ec2/bd-gold-layer-runner/adhoc/bdtsclb001_w2b_d02_d04_cascade.sh` (commit, uploaded to `s3://opal-data-bd/code/adhoc/`); D_02 + D_04 deployed = MATCH (runner S3 has DS W2b commit 5a7fb9417).

**Fork surfaced to COO/DS/CTO:** the boot systemd auto-runs `gold_dispatch.sh --chain full` (full publish). The scoped "no publisher between" path was needed ONLY to dodge the clobber — now removed at bd-v2.25.0. So a normal full incremental publish (boot default) would land W2b + serve as the natural AC4 full-publish parity test, zero interleave risk. Routed the scoped-vs-full decision to COO/DS (data owner) before firing a PROD cascade. Held pending their call (promote held on Andrew's smoke = no urgency).

## Compiler Tools
| Tool | Result |
|---|---|
| `comp-platinum reverse gold/entities/advisors/{id}/timeseries.json` | served URL + AdvisorAnalytics consumer; producers D_02/D_03 |
| `comp-blast build_advisor_timeseries` / `gold/advisors/{id}/timeseries.json` | no other consumer of removed write; legacy key = no graph node (zero readers) |
| `comp-iam service bd-portal-advisor-publisher` | 4 S3 ops GRANTED, no delta (removal only) |
| `comp-pipescript deployed D_02 + D_04` | both MATCH (runner S3 has W2b commit) |

## Next
Await COO/DS ruling on scoped-vs-full W2b publish path; execute the run; ping DS to served-verify (total_aua_fee_paying present + reconciles); route CVO for AC4 served-parity; RAVC2 the run + CVO verdict to close ADHC_BDTSCLB.001.
