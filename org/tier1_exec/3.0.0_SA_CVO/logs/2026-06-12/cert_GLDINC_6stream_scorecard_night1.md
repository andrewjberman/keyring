# CVO Scorecard — ADHC_GLDINC 6-stream parity evidence, night-1 post-7/7 (04:00Z 2026-06-12)

**archetype:** VALIDATE
**Certifier:** 3.0.0_SA_CVO · **Date:** 2026-06-12 ~13:30Z · **Verdict: GREEN — all 6 shadow streams + load_flows P1 + A_04 keep-full nominal; 4 BOOTSTRAPs are structurally expected night-1; 0 cutovers (correct, gated). One P2 note on A_02 clean-night accounting.**

Anchor (banked rule): dispatcher line + latest deploy commit — `gold_dispatch.sh:1318` = 6-member SHADOW_SET; 7/7 engineered (`9a89926fd` A_04 last); 0 cutovers.

## Chain (the carrier)

`chain_full_20260612_040103.log` (s3://opal-data-bd/gold/logs/): **26/26 scripts rc=0**, PARALLEL CHAIN COMPLETE 05:13:14Z, platinum published (21,805 files). All 7 GLDINC members ran in-chain on their served (oracle) paths — conversions remain additive, nothing cut over. A_04 (the CLASS-N hardened keep-full, DELTA=0 — no shadow stream by design) rc=0, wall 44.3s.

## Stream-by-stream (all scorecards generated 05:15–05:18Z by the scheduled nightly — LD-0176-clean, no manufactured runs)

| Stream | Script | Result | Detail |
|---|---|---|---|
| A_02 fee_rate_history | parity (lag=1) | **PASS — identical** | 10778=10778 rows, 0 key diff, 0 cell mismatches; **2nd consecutive identical night** (06-11 + 06-12) — but see P2 note |
| A_01 advisor_assignments | parity (lag=1) | **PASS — identical (night-1)** | 14866=14866, 0/0/0; oracle_fix_base `73ec87a84` stamped |
| B_02 canonical_lots | containment | **BOOTSTRAP (expected)** | no prior watermark; fingerprints + output etags recorded; containment scoring starts tonight |
| B_03 account_gains | containment | **BOOTSTRAP (expected)** | same model as B_02; evidence starts tonight |
| A_03 positions_cube | gate-evidence | **BOOTSTRAP (expected)** | fingerprint + output_digest recorded, n_outputs=2353 |
| B_01 holdings_lots | gate-evidence | **BOOTSTRAP (expected)** | fingerprint + output_digest recorded, n_outputs=67 |
| load_flows (P1) | parity scorecard | **PASS** | exact_match 100%, 78648=78648, max_abs_diff 0.0, all headline diffs 0 (incl. account_count), **clean_night_counter=2**, cutover_ready=false, targets_met=true, no fallback |

All four BOOTSTRAPs are the designed night-1 behavior for streams deployed during yesterday's barrel-through (deploys `4a62d0fdf`/`ba7b20807`/`0aa50c017`/`5d2fca51f` all post-dated the prior nightly). First containment/gate-evidence verdicts arrive on tonight's 04:00Z.

## P2 note — A_02 clean-night accounting under static input (for COO's cutover-evidence count)

A_02's shadow cutoff derives from the **latest fee FILE date − lag** (`A_02.fee_rate_history.py:641-643`), not run_date. Both nights' scorecards show `cutoff: 2026-06-09` — no new fee file landed between runs, so night-2 re-proved the **same** simulated delta on an unchanged input set (hence the byte-identical 10778 both nights). Mechanically honest (the cutoff is visible in the scorecard), but for cutover gating: a clean night with **no forward delta movement** demonstrates determinism, not new-delta correctness. Recommend COO's per-script clean-night tally distinguish advancing-cutoff nights from static-cutoff nights when counting toward the cutover bar (fee files are periodic, not daily — static nights will recur for A_02 specifically). No code change asked; accounting nuance only.

## Observations (no action)

- The 06-11 evening chain (`chain_full_20260611_220418.log`, 22:04Z) explains A_02's 23:14Z prior scorecard — barrel-through-window validation chain under Andrew's direct supervision; today's evidence is wholly from the scheduled 04:00Z run.
- live parity prefix histories confirm stream arming dates match the deploy sequence (load_flows since 06-08; A_02 since 06-11; the other 5 first-emit today).

## Disposition

Night-1 evidence: **GREEN, nothing blocks, no stream regressed, no served output moved** (never-widen untouched — shadows write scorecards only). Cutover remains correctly gated on per-script clean nights + Andrew nod; earliest meaningful containment/gate verdicts = tomorrow AM off tonight's run.

— 3.0.0_SA_CVO
