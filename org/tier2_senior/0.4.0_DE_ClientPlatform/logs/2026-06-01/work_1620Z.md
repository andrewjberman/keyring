# /work — 0.4.0_DE_ClientPlatform — 2026-06-01 1620Z (respawn + dispatch)

**archetype:** VALIDATE
**secondary_archetypes:** TRACE, COORDINATE

## Startup (respawn)
- Prior session dead ~2.9h (broker-LIVE was phantom pinned to broker-daemon PID; COO confirmed = its "DE wedged" diagnosis, 416220942).
- /watcher self-heal: killed prior-session orphan watcher (259580) + auto-respawn copy (278266); re-registered LIVE (PID 5512); tracked watcher running (task b6ckquzmf, PROCESS-OK). MSTR startup-hint absorbed (= spawn directive).
- Step 1b admin: session-serial file, owned-paths hook present, headmove guard present, comp-graph context set. `/work` 20m cron armed (job 758a61a5, 8,28,48).
- Ground-truth: most DE TOs complete; only externally-blocked ADVI_49PUSH stragglers + cancelled INFGRO. Checked in with COO; got redirect.

## Dispatch (COO [SYNC] 161304Z)
1. MDPF_SCOPED P1 = CLOSED + shipped PROD (portal-v2.1.105) — my BE-fit leg accepted, RD~B merged matrix, Performance/Peers classification resolved (COO ruled (b)-label). Dropped the stale matrix-reconcile (verified BEFORE doing it — no wasted work).
2. REDIRECT: Cohort-1c serving-data continuity verify (pairs RD~B trend rollup fix).

## Work done — Cohort-1c serving-data continuity verify
Read live S3 `json/mdpf/{49financial,global}/aggregate-aua-timeseries.json` (gen 13:34Z today). Reconciled the decomposition to the dollar and characterized the 5/18 boundary.

**Verdict: CONDITIONAL.** The ~$25M SMA(1c) is real & present so RD has a correct number to surface, BUT:
- **SMA(1c) is model-stack space, not non_model.** `by_model` = 5 `cohort_class='model'` + 2 `cohort_class='sma'` sleeves; `sma_aua = Σ sleeves` (to-the-$), additive alongside `model_aua`, NOT inside `non_model_aua`.
- **non_model (1b) is NOT continuous across 5/18:** 49f -$172M (largest non_model step in the 402-date series); `nm+sma` still -$147M; partner_custody_total -$156M. Global non_model -$270M but headline `opal_aggregate_aua` only -$62M (series-max is -$142M on 4/03). = documented **methodology seam** (historical <=5/17 v0.8/Ruling-2; >=5/18 live v0.9). Adding ~$25M does NOT close it.
- **SMA series crosses the boundary null -> $24.9M** (recent live region 4/28-5/15 = null; historical = flat ~$19.67M = the .032-probe seam value).
- **Narrative-vs-data tension:** meta says "1c non-additive sub-slice of 1b" but serving by_model treats SMA as separate additive `cohort_class='sma'`. Flagged to DS~B.

**FE implication:** correct fix = RD~B's already-flagged **F5** (per-firm by_model key-set drives trend model iteration => SMA sleeves stacked => post-5/18 ~$25M gap closes). NOT a non_model fold (mis-attributes SMA; adds nothing pre-5/18).

## Commits
- CLOUD `<pending>` — docs/briefs/mdpf-cohort-1c-serving-continuity-verify-20260601.md + this log

## Comms
- RAVC2 -> COO (2.0.0_SA_COO) + CTO (1.0.0_SA_CTO), CC DS~B (0.4.0_DS_ClientPlatform~B): finding + recommendation.

## Next
- [COO/CTO] Awaiting verdict on the CONDITIONAL + GO for RD~B F5 (vs a non_model fold).
- [DS~B] meta-narrative vs by_model reconciliation + pre-5/18 sma null-gap confirm.
- Free for next portal-data-path item after; flagged COO. /work cron live (next ~20m).
