# Session log — 2.0.0_SA_COO (ws COO) — 2026-06-01 (~13:03Z → ~21:47Z)

Long /drive-driven session. 28 drive cycles. Headline: MDPF_SCOPED Schwab-canonical re-derive driven to verified-close; a bell-curve footer bug traced to a SCOPE-not-grain root + fixed (stopgap + durable); a real deployment-integrity hazard (smartx EC2 bundle 4.5mo-stale image) discovered, contained, and remediated; comp-aws registered as the Andrew-directed post-initial-group priority; 2 portal PROD promotes. Ended in a fully-converged Andrew-gated resting state.

## Startup
- /watcher self-heal + org/XXX.md + armed /drive (20m cron 8463e5d6). Answered Andrew "what agents for FIND_INSURE / ADVI_INFMVP / MDPF_SCOPED."
- Andrew priority: sort MDPF_SCOPED first (pod-4 RD+DE categorize FE↔BE linkage; 0.5.0+0.7.0 AE for FE/BE link certainty).

## MDPF_SCOPED — the spine arc (DRIVEN TO VERIFIED-CLOSE on data)
- **Schwab-canonical re-derive** (Andrew directive via RD: "use Schwab as catch-all total, parse the rest; not Black Diamond"). 49F 1/16–5/17 re-derived onto Schwab: the −$172M phantom BD→Schwab seam CLOSED (5/15 custody = $1,648,847,957 == 5/18 live, to the dollar). 1c interpolated+labeled. DE + CVO independent 5/5 PASS.
- **Global propagation gap** (caught by DE/CVO): TO-1a emit rewrote the 49F partner block but NOT the partition aggregate headline → global slice carried old full-book 49F (+$143M @4/15). DS~B re-aggregated → global headline +$93.6M clean (was −$62M cliff); DE+CVO verified to the dollar.
- **Inflection adjudication**: the global non_model band step looked like a third seam; DS~B initially read it as same-class re-derive → I caught the DS~B-vs-DE divergence, ran the arithmetic (model +93.6 / non_model −97.7 = −4.1 continuous total), DS~B ran the decisive total-continuity test (5/15 $203.8M → 5/18 $199.7M), CVO independently adjudicated: it's a genuine MODEL-FUNDING BREAKOUT (Inflection models funded 5/18), ACCEPT, NO TO-1c, no back-decompose (would fabricate pre-funding models). Prevented an unnecessary re-derive TO. §2 PRD whipsawed twice on crossed reads before settling (CTO logged the lesson: don't amend a classification before the methodology owner's decisive test converges).
- **Item-3** (12/27 anomaly): spurious Saturday partition deleted (Andrew-direct), rollup re-run, DE-verified clean on served timeseries.
- **pre-1/16 #3 artifact**: DS~B delivered (b3e627a75) — decisive finding the 1/16 boundary is ALREADY continuous (no cliff) so it's a labeling/provenance call, not a fix; rec B (flag-at-1/16). Routed to Andrew (#3, awaiting ruling).
- AC3 data-layer COMPLETE all 3 firms; durable-close gates on the smartx EC2 redeploy (below).

## MDPF bell-curve footer bug (6639)
- Andrew flagged Inflection footer "Excludes 6639 unfunded holdings." DE TO-A traced root cause SHARPER than the PRD: a SCOPE mismatch (footer = GLOBAL account-count 7039 − PER-FIRM distribution), not just grain — so EVERY per-firm footer wrong (49's "201" masked-wrong too; only Global's 14 correct). No per-firm accounts count existed → producer-emit NECESSARY.
- TO-C stopgap (RD~B 9b2fed2c): Global-only footer, all per-firm suppressed. TO-B durable (DS~B): per-firm + global producers emit accounts-grain excluded_unfunded_count + by_model; DE-verified all 3 firms (49F=2 / inf=5 / global reconciled). Producer = compute_per_firm/compute_account_distribution (NOT 09/INF_09 — corrected mid-flight).

## smartx DEPLOYMENT-INTEGRITY hazard (discovered + contained + remediated)
- AE found the smartx daily EC2 job runs a DIVERGENT Docker-bundle copy; deployed ECR image = Jan-14 (4.5mo stale) < Feb-20 bundle < canonical (THREE-state staleness). Recent data/smartx edits never reached prod. The 202606 "spurious 7025@June" served-global was an artifact of this (June genuinely $0/unvalued end-of-period; corrected to 6838@May, −187).
- CONTAINED: CTO blast-radius = daily-run DAG clean post-AE-sync (the scary diffs are non-DAG retired/manual); no other silent daily drops.
- REMEDIATION: §3c interim drift-guard SHIPPED (AE 79568df53 — fails on canonical-vs-bundle divergence at push); §2 per-firm wired into the DAG+bundle (CTO ruled option-a + guardrail-1 fail-soft-on-missing-eclipse, AE 0b1e80d69); daily trigger HELD (0.5.0, removes the 14:16Z revert deadline — safe, monthly-grain). §3a/b durable env-aware sync (Dockerfile COPY-from-canonical + env-detecting config.py — config is intentionally EC2-specialized) FOLDS INTO comp-aws EC2 scope.
- **re-derive code-vintage confirm**: CTO flagged the stale image's undeployed Jan-21 "CRITICAL AUM smoothing" fix could touch the verified re-derive. DS~B's 3-step check → STAYS CLOSED: 49F 1a reads RAW SmartX daily-export CSVs directly, bypasses the aggregation layer where the undeployed fixes live + independent F4 point-in-time. Re-derive confirmed clean on BOTH angles (Mar/Apr-empty + code-vintage); §10 annotation 844921778.
- OPEN (deadline-free, safe-held): the smartx-exporter Docker rebuild (durably fixes the staleness + makes the global/per-firm fixes permanent). Gated on a Docker host — AE envs have no daemon, no CodeBuild path. Surfaced to Andrew as push-vs-ride (#8): ride-safe default vs push-tonight (needs MSTR CloudOps respawn + Andrew Docker Desktop).

## Portal (2 PROD promotes, Rule 19)
- v2.1.107 (DT 456d134e): canonical FE model names + disclaimer removal + Cohort-1c SMA fold (Andrew-smoked).
- v2.1.109 (DT a810bbef, Andrew-direct full DEV→PROD): INF blend colors + Macro YYYY-MM fix + HoldingsTab canonical names + DE FE-slim ETF_NAME_FALLBACKS retire. Schwab re-derive renders on this build (data-layer). + RD~B blend-sandwich ordering + footer stopgap on DEV (ride next promote).

## Other projects
- **comp-aws (ADHC_CMPAWS)**: REGISTERED (f915aca3c) — Andrew-directed MAJOR. CTO PRD d425e072f. Andrew directive: redirect fabric to comp-aws ONCE the initial group (FIND_INSURE+MDPF_SCOPED+ADVI_INFMVP) clears. EC2-edge scope richly anchored by this session's smartx hazard (three-state image/bundle/canonical reconcile, cross-pipeline edge, env-aware-not-naive, standalone-MDPF-pipeline end-state). Memory: project_comp_aws_post_initial_group_priority.
- **comp-lambdamap**: Phase-1 + Phase-2d shipped (drift-detect; reproduced+superseded CVO's manual audit, caught 3 wrong-source_dir + a bonus seeking-alpha TF bug). Subsumed as comp-aws Lambda sub-module.
- **FIND_INSURE**: active work done+RAVC2'd; A/B universe brief delivered (#2, lean B-core + formalize WM sidecar). DS~C reconciled 7 stale ADVI TOs (queue→0).
- **Positioning A+**: deployed yang-v2.4.11, DE-verified (0 all-caps, 22 clean); FE-slim shipped v2.1.109. Pending Andrew visual.

## Liveness / process incidents
- **DS~B WEDGED** (~67min): broker phantom-LIVE pinned to the daemon PID (4812 = python server.py); MSTR respawned (fresh PID 1040). My diagnosis cited the telemetry-is-truth pattern; MSTR folded it to standing discipline. (memory: reference_broker_phantom_live_pinned_to_daemon_pid.)
- **AE pod session-wrap** (0.5.0 f5c64a9ca): intentional session-end; CTO flagged so I didn't burn re-ping cycles → surfaced push-vs-ride to Andrew instead of unilateral respawn.
- Recurring `cd portal` cwd-drift bit the safe-commit twice (cycle 17, 20) — fixed by resetting to root; lesson: subshell portal checks.

## Andrew decision-stack at session end (the binding constraint — fabric fully converged)
1. Durability TF apply-ratify (BMKAUD smartx-retirement destroy + portal-v2 import+Deny).
2. FIND_INSURE universe A/B (brief delivered).
3. pre-1/16 Schwab disposition (artifact delivered, rec B).
4. MDPF visual smoke (v2.1.109 build — 49F + Global trend continuous).
5. comp-aws kickoff = AUTO on initial-3-clear.
6. footer+blend promote-timing (ready on DEV).
7. owned-paths confirm (let DS co-own 2 smartx distribution files — CTO-surfaced).
8. push-vs-ride on the 2 AE-gated deploys (bell-curve Docker rebuild + yield-curve fix) — ride-safe default; push = MSTR CloudOps respawn + Andrew Docker Desktop.

## State at handoff
Fully converged + Andrew-gated. MDPF re-derive CLOSED (both staleness angles); bell-curve data-complete + safe-held (durable redeploy deadline-free, trigger held, data correct); portal current; FIND_INSURE done; comp-aws staged for post-initial-group redirect. AE pod wound down. Watcher healthy (PROCESS-OK). /drive 20m cron live. No COO-actionable work until Andrew acts on the stack.
