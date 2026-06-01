# DS_ClientPlatform~B — Session Summary (2026-06-01)

Session arc: startup → MDPF_SCOPED inflection restore → BMKAUD WS-2 audit → Cohort-1c → MDPF 49F Schwab re-derive (TO-1a) + global fix + Inflection adjudication → **[session died ~67min; RESPAWNED]** → pre-1/16 disposition options artifact + TO-B bell-curve durable footer fix (3-firm) + re-derive staleness re-verification (2 angles). Worker (Tier-2 DS), lane COO 2.0.0_SA_COO. ~28+ work-cycles across both sessions. (Sections 1-7 = pre-respawn; "RESPAWN SESSION" block below = post-respawn.)

## 1. Startup + infra
- /watcher self-heal (was NOT REGISTERED → re-registered LIVE), tracked inbox-watcher relaunched. Armed /work 20m cron (later stopped by Andrew; switched to watcher-driven event loop).

## 2. MDPF_SCOPED inflection restore (FE↔BE linkage-audit data leg)
- FINDING: the 2026-05-29 backfill re-emit (build_mdpf_process_backfill.py, a 49F-only historical tool) was run over post-onboard dates 5/18-5/29, dropping the Inflection partner from 8 served artifacts → inflection per-firm panel empty, global understated by inflection 2a.
- FIX: re-emitted the 8 dates via canonical mdpf_aggregate_aua.py (both partners restored, S3-verified). CVO PASS 4/4.
- AE caught partition-fix != serving-fix → re-ran the ROLLUP (build_aggregate_aua_timeseries.py) so the FE timeseries/json slices refreshed (inflection trend non-null). CVO PASS #2.
- GUARDS shipped: onboard-date guard on the backfiller (a9352506f); version-monotonic write-guard on both partition writers (f304319f7, refuses downgrade methodology_version overwrite); rollup graceful-degrade on the json/mdpf dual-write (bf5d24861) + leg-1a rollup redeploy (durable FE-feed scheduling).
- 5/26=5/27 disposition: pre-existing upstream WS-C inflection feeder timing race (feeder 11:01 vs eclipse gold_complete 11:12) → chain-ordering, AE's Stage-0.5 gate.

## 3. BMKAUD WS-2 — benchmark/peers number validation (Andrew-direct audit)
- BENCHMARK: 360/360 cells reproduce exactly from canonical data_20260531_v1.pkl (HALF-A derivation-fidelity). 1M/1Q symptoms were pre-revert SmartX, now clean. HALF-B methodology = WS-3/CVO.
- PEERS: 30/30 reproduce; UST-1M traces exactly to the 20260531 xlsx → present+faithful (NOT a data bug; FE-side). Retracted my own "5-month-stale peers" error (real source was a fresh archived xlsx).
- 1M/1Q window both-ways evidence + end_date edge (jointly-BENIGN w/ WS-3) + p95==0.0 legitimate.
- HALF-A byte-verified vs the frozen evidence snapshot (md5 local==live==frozen). RAVC2-ACCEPTED + CLOSED.

## 4. Cohort label + meta fixes (Andrew/CTO canonical mapping)
- Cohort 1b/1c label comment fix in mdpf_aggregate_aua.py (22bb6f9bf) + rollup meta narrative (3af2911c7): canonical 1a=model, 1b=non-model PLUG, 1c=SMA (additive+disjoint). Values always correct (doc-only). Deployed to runner code bucket.

## 5. Item-3 — 12/27/2025 per-firm anomaly (Andrew visual-review flag)
- ROOT CAUSE: spurious Saturday partition (only Sat + only INF-null date in 402-series). Andrew-confirmed S3 delete of 2025-12-27.json (versioned/recoverable) + rollup → spike gone, INF null-dates=0, verified.

## 6. TO-1a — 49F Black-Diamond→Schwab canonical re-derive (the big seam fix)
- SCOPE-FIRST: empirically validated the Schwab restriction is computable EXACTLY (4/15 $1,556.2M vs full-book $1,699.3M via BD silver/allocations ∩ fees crosswalk). Surfaced the exact-vs-estimate map (CTO hard-honesty gate) before emit.
- APPLIED: re-derived 49F 1/16-5/17 onto Schwab canonical (1b = Schwab_custody − 1a − 1c) via WS-E production compute; 82 partitions; holiday/raw-schema custody roll-forward; 1c linear-interp across the null-gap (Andrew's calculated-daily ruling), labeled estimate. Dry-validated 82/0-err before --apply.
- PROVENANCE: per-date cohort_provenance + meta.basis_provenance in the served feed (rollup enhanced, 120652cb6) — DE AC3 estimate-labeling.
- RESULT: 49F 5/15→5/18 custody step $0 (was −$172M). SEAM CLOSED. DE + CVO both PASS 5/5.
- GLOBAL FIX (my emit gap, caught independently + by DE/CVO): the partition aggregate block wasn't recomputed from the corrected 49F → global slice stale. Fixed in-place (re-apply recomputes aggregate from partners) + rollup → global headline 5/18 step now +$93.6M clean (was −$62M cliff), 4/15 $1,556.2M Schwab. DE re-verify PASS + CVO axis-1 CLEARED.

## 7. Inflection adjudication (corrected my own over-framing)
- I initially framed the global −$89M non_model residual as needing a same-class Inflection re-derive (TO-1c). DE + COO reconcile + my verification of the decisive total-continuity test (Inflection total −$4.1M across 5/18) corrected it: it's a model-funding BREAKOUT (models funded 5/18, $93.6M moved out of non_model into model; total continuous), NOT a basis re-measurement. NO TO-1c re-derive. The Inflection band step is honest; only an optional Andrew display preference remains.

## Honesty discipline (banked to memory)
Made several over-framings this session — peers-5mo-stale, sma-null-pre-5/18, sma-not-reconstructable, Inflection-as-re-derive, the aggregate-block scope — each caught by a peer's independent read or my own re-check BEFORE reaching Andrew. Lessons: verify against the actual SERVED/consumed artifact + ALL producers, not a partial proxy (memory feedback_verify_against_served_artifact_not_partial_proxy); partition-fix != serving-fix, run comp-pipescript postdeps (memory feedback_mdpf_partition_reemit_needs_rollup_postdep).

## Open (Andrew decisions / scoped follow-ons — none silently wrong)
- Pre-1/16 (#3): back-cast-estimate / flag-at-1/16 / start-at-1/16 (TO-1b artifact to draft for Andrew).
- Inflection 5/18 display: accept honest breakout (recommended) vs cosmetic smoothing.
- AC6 add-days 2/2,3/2,4/1,5/1 (custody OK, need 1a/by_model scoping) — follow-on.
- MDPF leg-1 (json/mdpf daily scheduling) verify on AE's runner IAM grant.

## Key commits
a9352506f, f304319f7, bf5d24861 (MDPF guards/rollup); 22bb6f9bf, 3af2911c7 (cohort labels/meta); 120652cb6 (rollup provenance); TO-1a partition emits (S3, via .runtmp/bmkaud/to1a_emit_v2.py); BMKAUD WS-2 + Cohort-1c + Item-3 evidence docs under this logs dir.

---

# RESPAWN SESSION (2026-06-01 ~1948Z+) — dispatches #1, #2 + re-derive staleness re-verify

Prior session died ~67min (broker phantom-LIVE pinned to broker-daemon PID 4812; MSTR [STUCK] respawn). Picked up 2 unprocessed ws COO dispatches + handled 2 CTO/COO closed-work-verification asks.

## 8. Respawn recovery
- /watcher self-heal: re-registered LIVE (was phantom 4812), killed prior-session orphan watcher (auto-respawn loop), launched tracked watcher. Armed /work 20m cron (fd526b5c).
- Recovered BOTH dispatches from `~B/read/` — the dead session's orphan watcher had swallowed them (top-level + check-inbox empty; found via grep). Lane-subdir vs concatenated-path: COO addressed `0.4.0_DS_ClientPlatform/~B/`.

## 9. Dispatch #1 — pre-1/16 disposition OPTIONS artifact (DONE, arms Andrew #3)
`docs/briefs/mdpf-49f-pre-1-16-disposition-options-20260601.md` (b3e627a75). 3 options (A back-cast estimate / B flag-at-1/16 / C start-at-1/16), each with what-Andrew-sees + honesty posture + data implications + AC6-dates (12/30,12/31,1/2) handling + rec.
- DECISIVE empirical finding (pulled served 49F timeseries): the 1/16 boundary is ALREADY numerically continuous (1/15 $1,409.3M → 1/16 $1,412.9M, +$3.6M, no cliff) — the full-book→Schwab divergence only opened April→5/17. Reframes the decision as PROVENANCE/labeling, not a visible jump.
- REC = Option B (flag-at-1/16, keep pre-1/16 labeled legacy): A buys ~nothing visible while adding a widening error band; C discards real continuous growth history (Nov'24 ~$776M→Jan'26 ~$1.4B). CTO CONCURRED strongly (rejected A as fabricated-precision-for-zero-change). Routed to Andrew #3. **AWAITING Andrew ruling.**

## 10. Dispatch #2 — TO-B bell-curve durable footer fix (3-firm, all served+verified)
The footer "Excludes N unfunded holdings" was an FE cross-scope subtraction `metrics.account_count(7039 GLOBAL) − distribution.account_count(per-firm)` = 6639 garbage for inflection. Durable fix = emit the excluded-unfunded count DIRECTLY in the producer.
- PRODUCER-CORRECTION (material): DE/COO cited INF_09/09.generate_partner_analytics as the emit-target — WRONG (those publish partner_analytics.json/NNA). The real producer of `json/mdpf/{firm}/account-distribution.json` is `compute_per_firm_account_distribution.py` (+ `compute_account_distribution.py` global). Proved by shape+source+period match.
- EMITTED total + by_model `excluded_unfunded_count` for all 3 firms (49F=2, inflection=5, global=2), each self-consistent (excl=active−funded) + reconciled (Σ by_model = total). by_model per CTO ruling 29b310e4f. Triple-verified: DS data-layer + DE serving-verify (1a026099c) + CVO cert (bf244cac1 inflection / bfd43a981 global). LD-0012 cross-scope-subtraction defect eliminated.
- ANTI-REGRESSION GUARD + LATEST-FUNDED-PERIOD selection: dry-run-before-upload caught that re-running 49F would regress 6838→0 (smartx June 202606 is an unvalued $0 shell — AE confirmed genuine end-of-period, the served 7025@June was a spurious transient). Guard refuses to upload a 0-account distribution; latest-funded selection skips the $0 shell. Global -187 correction (7025@June→6838@May) COO-approved as a correction, AE re-emitted.
- OWNED-PATHS: `data/smartx/**` = AE OpalETL lane; my DS serial can't commit → handed AE the diffs (did NOT --force). AE committed (4ffb21d7b, cfc278f38, 9dfb66dcb). §2 finding: the per-firm producer is MANUAL-ONLY (not in the smartx daily DAG/Docker bundle/Lambda) → recommended + AE wiring it into the daily DAG + bundle on the same pending Docker rebuild.
- DURABLE-CLOSE GATE: the smartx-exporter EC2 daily run (~14:16Z) runs a DIVERGED old bundled copy → would re-clobber to the anomaly until AE's Docker rebuild. So data-correct NOW, durable-close = AE Docker rebuild (CVO conditional cert + DE re-verify gate on the post-deploy daily run) + RD FE cutover. **In AE/RD hands.**

## 11. Re-derive staleness re-verification (both angles CLEAN — closed work stays closed)
Two staleness angles raised against the verified-closed TO-1a re-derive (CTO blast-radius):
- Angle 1 (Mar/Apr near-empty smartx-allocations): 1a from a SEPARATE populated daily source; not affected (served Mar/Apr 1a ~$1.2B, 0 nulls/82 dates). COO-accepted.
- Angle 2 (stale Jan-14 smartx-exporter image, missing d621311b5 Jan-21 AUM-smoothing + feca94a1f + May-13): 49F 1a INSULATED — reads raw SmartX daily-export CSVs directly (build_mdpf_process_backfill.py historical; wsb_49f_smartx_model_aua.py REST-API live), bypassing the exporter aggregation layer where the fixes live (d621311b5 is in aggregate_smartx_by_transaction_dates.py = global AUM timeseries, a different pipeline) + independent point-in-time F4 logic; current-code-consistent by construction. COO-accepted.
- Annotated the re-derive close record §10 (844921778, COO-directed).

## Open / gated (none silently wrong)
- **pre-1/16 #3** — Andrew ruling (artifact delivered + CTO-concurred rec B).
- **TO-B durable close** — AE Docker rebuild (per-firm DAG wiring + global daily-run) gated on Andrew push-vs-ride + wound-down AE pod; then DE/CVO post-deploy re-verify + RD FE cutover.
- (From prior session, still tracked:) Inflection 5/18 display preference; AC6 add-days 2/2,3/2,4/1,5/1; MDPF leg-1 scheduling.
- Fabric converged/Andrew-gated at session end; holding armed-quiet keep-warm.

## Respawn-session key commits
b3e627a75 (pre-1/16 options artifact); 4ffb21d7b + cfc278f38 + 9dfb66dcb (AE-committed TO-B producers); 1308043ab + 844921778 (re-derive staleness verify + §10 annotation); work logs work_1955Z/2014Z/2039Z/2053Z/2109Z/2138Z under this dir. Served emits: json/mdpf/{49financial,inflection}/account-distribution.json + json/portfolios/account-distribution.json (all 3 with total+by_model excluded_unfunded_count).
