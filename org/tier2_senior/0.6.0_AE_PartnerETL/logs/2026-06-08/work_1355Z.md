# 0.6.0_AE_PartnerETL session log — 2026-06-08 work_1355Z (GLDINC P1 design-review -> GO -> build, co-dev w/ DS)

**archetype:** IMPLEMENT
**secondary_archetypes:** DESIGN, COORDINATE, REVIEW

Continues work_1313Z (P0+W2a validated-live & RAVC-closed; P1 staged). This tick: P1 design review -> CTO GO -> full AE-lane build, co-developed with 0.4.0_DS.

## P1 design review -> GO (4 byte-identity traps closed before any code)
The plumbing-proof's "zero-correctness" claim hinged on getting the cache boundary exactly right. Four traps, all surfaced + resolved in the design-of-record (commits 1002a5491 -> 50a8df3de -> de437b3c0 -> 8dde33353) BEFORE building:
1. **Per-event grain** (CTO): garbage filter is per-event (nna_flows.py:250->259->280) BEFORE the :285 groupby; daily-aggregated cache can't reproduce per-event exclusion.
2. **Dedup-over-union** (AE): composite dedup :145-149 is trade_date-keyed but watermark is file-date -> a cross-boundary twin survives per-block dedup.
3. **Order-stability** (AE): :128/:148 keep='last' is row-order-dependent -> union must re-sort by source_order_key to the oracle's sorted(keys) concat order.
4. **Raw pre-:128/pre-dropna** (DS): oracle dedups (:128) BEFORE dropna (:132), so a null-field row can win the dedup then be dropped, net-suppressing its non-null twin; a post-dropna cache loses that winner. CTO independently verified + made binding.
Resolution: cache the TRULY-RAW per-event rows (post-:122-124 concat, pre-:128) incl. null-key rows + source_order_key; run the WHOLE transform from :128 over the union each night. CTO principle banked for P2+: **cache boundary must sit UPSTREAM of every cross-event / current-state op.** CTO GO 133416Z (deploy-class confirm).

## Build (Option A split, co-dev w/ DS — both endorsed)
- **DS (0.4.0, gold-.py deploy domain + reconcile-correctness):** owns lib/nna_flows.py — `_transform_events_to_daily()` extraction (oracle byte-unchanged) + `load_flows_from_transactions_windowed(wm)->(daily,pending_state)` (PURE, no writes) + `read_load_flows_watermark()` + `write_load_flows_state(pending)` + restatement detect-and-fallback. Commits + S3-deploys all P1 gold .py (incl. the harness — owned-paths correctly blocked AE from committing gold/*.py). API LOCKED 134749Z.
- **AE (0.6.0, GLDINC infra lead):** authored `gldinc_p1_shadow.py` (shadow harness + §4b scorecard: key_set_symmetric_diff/row_count_delta/exact_match_rate/within_epsilon+max_abs/rel/headline_metric_diffs/clean_night_counter/restatement_fallback; writes ONLY gold/_parity+_state, never served; SINGLE harness-gated cache advance on clean-OR-fallback; non-fatal). GATED clean, pure ASCII, from __future__. Wired gold_dispatch.sh post-chain invoke (chain:full only, NON-FATAL, kill-switch GLDINC_P1_SHADOW) — **committed 0cd1812f2**, deploy-held until DS's .py bundle lands. IAM verified CLEAR (opal-data-bd/* wildcard covers _state+_parity, no TF change).
- **clean_night_counter semantic (AE call, flagged DS+CTO):** HOLD on fallback (full-scan didn't exercise the incremental read), INCREMENT on clean-&-not-fallback, RESET on divergence -> ">=5 clean nights" = 5 nights the INCREMENTAL path actually matched.

## Open / next
- DS commits+deploys lib+harness bundle -> AE deploys gold_dispatch.sh (sequenced) BEFORE tonight's ~23:00Z nightly -> first scorecard on the scheduled run (ZERO ad-hoc).
- Confirms pending: DS on API names + counter-hold semantic; CTO on counter-hold (he set the >=5 gate).
- Freeze epsilon off night-1's actual max_abs_diff (expect ~0). RAVC2 CTO+COO with first scorecard. COO /drive daily-watch attests scorecard.json through 2026-07-05.
- P0 resume==fresh empirical residual folded to P2 AC (per COO ruling); relevant to DS's P2 A_03 draft.

## Compiler Tools
| Tool | Result | Note |
|---|---|---|
| ds-commit-gate.sh | PASS (gldinc_p1_shadow.py) | py_compile + ds-precommit (undefined-name; caught a leftover `clean` ref) + ruff (caught E402 from future-before-docstring) — all fixed, clean. |
| bash -n | PASS (gold_dispatch.sh) | post-chain shadow-invoke wiring. |
| comp-iam (manual read of bd-pipeline/iam.tf) | CLEAR | runner role opal-data-bd/* wildcard covers gold/_state + gold/_parity; no TF change. |
| comp-pipescript io (P1 build mandate) | DEFERRED to cutover | P1 is shadow-only (no served-key change); io/feeds run before the consumer cutover (later Andrew-gated phase), not the shadow. |
