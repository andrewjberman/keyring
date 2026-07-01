# CVO~B COMPPROOF.B2 -- B-01 blind-run judge verdict: PARTIAL (+ re-run flag + structural-reach-ceiling finding)

**archetype:** VALIDATE

**Serial:** 3.0.0_SA_CVO~B | **Date:** 2026-07-01 | **Window:** ~1508-1512Z
**TO:** NFRA_COMPPROOF.B2 (blind-run judge). First datapoint (validates the loop end-to-end; scales to 20).
**Incident:** B-01 = ADVI_BREAKS (sealed judge-view read as JUDGE). Independent judgment -- I re-audited the tool-log myself (not MSTR's cheat_check).

## VERDICT: **PARTIAL** (reach=narrowed / usability=usable / grounding-resilience=resist). NOT VOID. Isolation held. + RE-RUN FLAG + a structural-reach-ceiling finding.

## Gates (pre-scoring)
- **VOID-gate: NOT VOID (my independent tool-log re-audit).** All 20 tool-log entries audited vs the forbidden narrative/resolution set (org/critical_paths, debtscan, memory/, CLAUDE.md, org/**/logs, docs/**/postmortem) -> ZERO hits. Every call is comp-tool / live-AWS-served / SOURCE-read (the ALLOWED substrate): comp-which -> comp-freshness -> comp-platinum -> aws s3 (served) -> pipescript -> grep gold-SOURCE. Genuine graph-traversal, not answer-lookup. (Confirms MSTR's cheat_check, verified myself.)
- **Isolation-gate: HELD.** author ~D (isolation-barred) != solver (clean-room bare-launch) != judge (me).

## 3-axis (vs the sealed true root cause)
Sealed true RC (B-01): a 06-11 v2-txn cutover bundle STRANDED across 4 layers -- wrong bronze prefix / half-cutover quorum / silver->gold basename-collision SILENT-FATAL / eclipse cascade; the L3 FATAL was SILENT (on-instance, lock-held, no log/CW/SNS). Found by a HUMAN (Andrew, manual SSM).
- **REACH = narrowed.** The solver nailed the SYMPTOM (served inf header_metrics.json total.aua=$202,125,678 FROZEN at data_as_of 06-30), found the sibling header_metrics_fresh.json true $204,596,210 (source=bronze, bronze_date 06-12), localized to the INF_D_04 producer, and TOUCHED the cutover thread (bronze_date 06-12 == the stranded-deploy date). It did NOT reach the 4-layer stranded-deploy MECHANISM -- HALTED on an EXTERNAL API rate-limit (infra confound, NOT a substrate dead-end). So `narrowed`, not `no` (no substrate MISS).
- **GROUNDING-RESILIENCE = resist.** It characterized the $202M as FROZEN-BUT-FRESH and did NOT record it as truth (resisted the success-shaped-wrong trap) -- cross-checked against the sibling fresh.json. Plus 0 forbidden-narrative reads (grounded on live/source, not the resolution record).
- **USABILITY = usable.** 20 tool-calls, a clean rail-first 6-step traversal (comp-which first, then the right tools) -- a human could follow it. Not too-slow, not fell-back.
- `harness.score_run(reach=narrowed, usability=usable, grounding=resist)` -> **PARTIAL** (official).

## Two findings beyond the score
1. **RE-RUN FLAG (infra confound).** The reach was cut by an EXTERNAL API rate-limit (explicitly "not your usage limit"), not a dead-end. A clean re-run in a non-rate-limited window is needed for the CONCLUSIVE reach verdict -- do NOT bank this narrowed-reach as the substrate's ceiling on a confounded run.
2. **STRUCTURAL REACH-CEILING HYPOTHESIS (the deeper B-finding).** The true-RC L3 FATAL was SILENT -- on-instance, lock-held, NO log / CW / SNS. A failure that left NO trace in the observable substrate is likely UN-REACHABLE via graph/served/live tools -- which is precisely WHY a HUMAN had to manually SSM-ground it. So the reach-ceiling here may be STRUCTURAL (a real grounding-only-observable limit of the comp-tool substrate), not merely rate-limited. The re-run DISTINGUISHES "rate-limit cut it short" from "silent-FATAL is un-observable" -- either way it feeds Workstream-D as a genuine capability signal (the substrate cannot reach a trace-less failure; closing it needs a new signal, e.g. an on-instance FATAL-capture channel).

## Gap-charter (filed, per the 100%-MISS/PARTIAL AC)
`charter_for: B-01 / failure_class: stranded-half-landed-deploy / gap_axis: REACH-narrowed / proposal: graph-enrichment or new-comp-tool for the stranded-deploy class / feeds: Workstream-D` -- with the re-run + structural-ceiling note.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| corpus_loader.judge_view / incident_by_case_id (B-01) | read the SEALED true root cause (judge role) | PASS -- 4-layer stranded-deploy, silent L3 FATAL |
| independent tool-log audit (20 entries vs forbidden set) | the VOID-gate (my own, not MSTR's cheat_check) | PASS -- 0 forbidden-narrative reads; ALLOWED substrate only |
| harness.score_run + gap_charter | official 3-axis aggregate + charter | PASS -- PARTIAL; gap-charter filed |

What worked: re-auditing the tool-log MYSELF (not trusting MSTR's cheat_check) is the point of an independent judge -- 0 forbidden reads confirmed the run is a genuine graph-solve. Scoring reach=`narrowed` (not `no`) correctly avoided a false substrate-MISS on an infra-confounded halt. The deeper find -- a SILENT (trace-less) FATAL is structurally un-reachable via the observable substrate -- is the kind of capability-limit B is meant to surface (not just "did it solve," but "CAN the substrate solve this class"). Gap: the re-run (non-rate-limited window) is needed for the conclusive reach; flagged.

## Next Steps
1. **[2.0.0_SA_COO~B]** B-01 = PARTIAL (loop validated end-to-end: isolation + no-cheat + genuine traversal + independent 3-axis + gap-charter all fired). RE-RUN FLAG (rate-limit confound). Roll to the ledger; sequence a clean B-01 re-run for the conclusive reach; the structural-reach-ceiling (silent-FATAL un-observable) feeds Workstream-D. Then scale to B-02..B-20.
2. **[3.0.0_SA_CVO~B]** Judge B-02..B-20 as their solves land (same gate + 3-axis + charter). B-01 is the validated template.

-- 3.0.0_SA_CVO
