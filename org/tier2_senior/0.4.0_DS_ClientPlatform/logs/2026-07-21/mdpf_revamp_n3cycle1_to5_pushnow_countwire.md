# MDPF_REVAMP -- N=3 cycle-1 declared, TO-5 landed, streak-mechanics found, push-now account_count wired (DS)

**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE, VALIDATE
**Serial:** 0.4.0_DS_ClientPlatform | **Date:** 2026-07-21 | **Window:** ~15:53Z (prior log ce6cec9c9) -> ~18:28Z

## Summary
Drove MDPF_REVAMP from the staged-parity milestone to a live push-now cutover. N=3 STAGED-PARITY
cycle-1 declared by CTO (3 independent passes -- CTO S3 re-verify + DT date-joined parity + CVO
from-scratch re-derivation, all to the penny, 0 unexplained). Then: finalized the ledger (D-2+F2
composition + A4 ranges), delivered the cutover co-sign package, landed TO-5 (revamp-silver
source_vintage_last + NEVER#1 trading-day-aware status), grounded + flagged the STREAK-MECHANICS gap
(revamp is hand-staged, not scheduled), and -- on Andrew's rollback-armed PUSH-NOW GO -- wired
account_count to the real served counts (co-sign item 4). CTO ACCEPTED all; my DATA lane is COMPLETE +
Andrew-confirmed-correct. Cutover now HELD on a frontend-alignment roll-over (a DE agent owns the FE).

## Work done
- **N=3 cycle-1 (CTO-declared):** 3 passes agree to the penny -- axis 407/22/20, D-2 +$20,344,172.42
  exact, non_model +$21,647,872.00 (D-2+F2) NAMED, inflection EXACT, model F2 in-band, Nones all at
  feed-gaps. A4 named-delta PASS; account_distribution CVO-clean. CORRECTION absorbed: N=3 = 3 consecutive
  clean SCHEDULED cycles; hand-staged cycle-1 = a code-correctness pre-proof, not a streak cycle.
- **Ledger finalize (6026af46a):** non_model_latest notes name the D-2+F2 composition (+$21.65M = D-2
  $20.34M + F2 $1.30M) per CTO's re-verify item; locked ~A's A4 non_model_assets/global enterprise/
  non_model ranges (~A dry-run ties my aggregate to the cent).
- **Cutover co-sign package (2e9a118f8):** the 5 NAMED visible-correct changes (dual-read+$10-20M drift/
  TO-2, A4 pre-cutover passthrough boundary, 05-21 legacy-imputed null, account_count PRESERVE+seam,
  inflection 05-15 launch onset) + publish mechanics. FORMAL co-sign = cutover gate (CTO+COO+Andrew).
- **TO-5 (b) revamp-silver (7ef623e14 + 4d6dadd0e):** source_vintage_last = honest provenance of the
  revamp's OWN sources (model_aua=aum_daily/eclipse, partner_custody=rps_s2/orion), NOT legacy-feeder
  mirroring (false provenance). Grounded FE reads neither by_feeder nor .overall -> revamp-native shape.
  status = TRADING-DAY-AWARE (NEVER#1): trading_days_behind, T-1=current (no flat-hours Monday false-
  alarm); frontier fns inlined via the shim (no lib/ runner import). Both DATA-ARRAY-NEUTRAL proven.
- **TO-2 SCOPE (CTO-ruled, my FE trace):** grounded ModelPortfolios.tsx reads BOTH the revamp aggregate
  (getMdpfAggregateAUATimeSeriesByFirm) AND legacy getAUMTimeSeries/getAUMMetrics -> LIVE, not vestigial;
  TO-2 = later wave (replace the legacy reads, kills the dual-read + $10-20M drift). Parked for N=3.
- **STREAK MECHANICS (grounded finding):** the revamp producer is HAND-STAGED, NOT scheduled (source-map:
  publisher "EventBridge schedule DEFERRED"; no EC2 runner/trigger runs dim_mdpf; nightly runs the legacy
  producer). CTO ruled: WIRE it to a PARALLEL nightly schedule (= PRD S4 parallel-not-serving) -> streak
  accrues on scheduled runs; routed to AE via COO. My gold code is ready; the scheduler deploy is AE's.
- **PUSH-NOW account_count wire (82c4d1ec6, co-sign item 4):** Andrew GO'd a rollback-armed S5 cutover on
  the verified cycle-1 data. Wired account_count -> served-real: IMPORT served daily-snapshots date-joined
  (imported==served EXACT at all common dates, 0 non-tie all 3 firms), honest-None at published-only
  (un-derivable -> None, NO LOCF/gap-fill, CTO consistency point applied), other 6 arrays + model_value
  BYTE-IDENTICAL (streak-neutral), integer, seams clean; null_ok removed. Re-staged + landing-verified.
  05-15 asymmetry NAMED (0e82dae46, CTO ruled accept-the-import): model onsets 05-15 (Andrew) / imported
  count onsets 05-18 (served vintage, ties); no harness delta (None==None @05-15).

## MCP traffic
~40 messages, all base CTO (gate/rulings) + 0.2.0_DT (parity + 2 harness-bug fixes I surfaced) + 0.4.0_DS~A
(A4) + COO/CVO/MSTR (ACKs). Significant CTO rulings: N=3 cycle-1 declared; N=3=3-scheduled-cycle streak
(hand-staged=pre-proof); TO-5 (b) + status (b) trading-day-aware; TO-2 later-wave; WIRE revamp to parallel
schedule (routed AE); PUSH-NOW GO (Andrew, rollback-armed); account_count ACCEPTED; 05-15 accept-import;
push HELD on FE-alignment. DT: independent 3/3 NAMED_DELTA_PASS 0-unexplained vs final ledger; source_
vintage_last VALUE-exemption flagged (BUG-1 completion).

## Compiler Tools
| Tool | Run | Result | Note |
|---|---|---|---|
| DT mdpf_parity_check.compare() @e17a28141 | 3 firms, multiple | 0 UNEXPLAINED | ran DT's date-joined harness on count-wired + TO-5 artifacts; caught source_vintage_last VALUE-comparison gap (flagged DT) |
| safe-commit (surface-check + risk-reflex) | 6 commits | PASS | reflex clean each |
| commit-gate (py_compile+ds-precommit+ruff) | every .py edit | PASS | caught unused `latest` var + unused constant -> removed |
| comp-system-gate | 6 commits | OVERRIDE | audited system-current-override (build-alongside/ledger/docs, data-array-neutral or no data change) |
Grounding via boto3 data-plane (served/silver/DDB reads -- Rule 21 carve-out) + the canonical trading-day
shim (NEVER#1 status). DDB opal-assets-daily-aua grounded for TO-5 (used revamp-silver instead). Gap: DT
harness VALUE-comparison doesn't exempt source_vintage_last (flagged; BUG-1 completion).

## Files Modified
See commit messages: **6026af46a** (ledger D-2+F2 + A4 ranges), **2e9a118f8** (co-sign package),
**7ef623e14** (TO-5 source_vintage_last), **4d6dadd0e** (TO-5 trading-day-aware), **82c4d1ec6**
(account_count wired), **0e82dae46** (05-15 named). Files: data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_
timeseries.py + the named-delta ledger + the co-sign-package deliverable.

## Blockers
None on my side. My DATA lane is COMPLETE + Andrew-confirmed-correct (no producer schema changes). The
cutover is HELD on external gates: FE-alignment (a spawning 0.4.0_DE_ClientPlatform owns it), AE cutover
mechanics + the parallel-scheduler wiring, CTO's final pre-publish S3 re-verify, a render-check.

## Current State
- **RE-STAGED (count-wired, LIVE):** s3://opal-data-assets/gold/mdpf_revamp/{49financial,inflection,global}/
  aggregate_aua_timeseries.json (ETags 933318c2.../f3fd7af2.../53b732b2...). account_count real (ties served
  at common, honest-None published-only); other 6 arrays == the cycle-1 stage (streak-neutral).
- **Producer:** dim_mdpf_aggregate_aua_timeseries.py (--firm all): 3-firm serve-real; account_count imported
  from served (load_served_account_count + _account_count_series); source_vintage_last revamp-silver +
  trading-day-aware status (build_source_vintage_revamp + inlined _trading_days_behind). HAND-STAGED (not
  yet scheduled -- AE wires the parallel nightly).
- **Ledger (0e82dae46):** 3 firms date-joined 0-unexplained + A4 non_model_assets/global + 05-15 note; the
  account_count null_ok is REMOVED (counts tie).
- **A4 (~A):** dim_mdpf_non_model_assets.py staged gold/mdpf_revamp/global/non_model_assets.json (ETag
  d4802341...), ties my aggregate to the cent.
- **Co-sign package:** org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/MDPF_REVAMP_cutover_cosign_
  package_20260721.md (2e9a118f8).

## Next Steps
- **[1.0.0_SA_CTO]** final pre-publish S3 re-verify (account_count-tie + 6-array-byte-identical) at the
  cutover gate; drive co-sign (CTO+COO+Andrew).
- **[0.4.0_DE_ClientPlatform]** (spawning) FE alignment to the revamp model-only schema + render-check.
  I offered CTO a data-schema contract for the DE (I am the schema authority).
- **[0.7.0_AE_CloudOps / AE]** wire the revamp producer (dim_mdpf_aggregate + A4) to the PARALLEL nightly
  schedule (EventBridge/runner + source map + publisher schedule) so the streak accrues; + cutover mechanics.
- **[0.2.0_DT_PortfolioAnalytics]** complete BUG-1: exempt source_vintage_last from the VALUE comparison
  (provenance, not data).
- **[me / 0.4.0_DS_ClientPlatform]** event-driven: re-verify each scheduled cycle; write the DE schema
  contract on CTO's word; rollback support. DATA lane complete.
- Reachable, event-driven (Monitor bgszef4p4). No crons.
