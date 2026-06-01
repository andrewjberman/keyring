# DS_ClientPlatform~B — Session Summary (2026-06-01)

Session arc: startup → MDPF_SCOPED inflection restore → BMKAUD WS-2 audit → Cohort-1c → MDPF 49F Schwab re-derive (TO-1a) + global fix + Inflection adjudication. Worker (Tier-2 DS), lane COO 2.0.0_SA_COO. ~23 work-cycles.

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
