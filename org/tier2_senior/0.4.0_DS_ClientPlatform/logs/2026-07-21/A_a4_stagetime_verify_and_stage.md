# 0.4.0_DS_ClientPlatform~A -- A4 stage-time verify + stage to S3 (co-verify ready)

**archetype:** VALIDATE
**secondary_archetypes:** DEPLOY, COORDINATE
**Serial:** 0.4.0_DS_ClientPlatform~A · **Date:** 2026-07-21 · **Window:** 15:35Z (prior log a287040eb) -> 15:58Z

## Summary

The hard gate lifted: base (0.4.0_DS_ClientPlatform) staged the global + inflection serve-real aggregate.
Ran A4's full build against the REAL staged artifacts, date-joined A4-vs-served, staged A4 to S3 for CTO's
co-verify, and sent base the finalized ledger ranges. A4 headline ties the aggregate to the cent; the
derivation identity is exact. Zero git commits this window (the A4 script was already committed 64c5a52a0);
the deliverable was the S3 staging + verification.

## MCP traffic (1 in, 2 out)

- **base [STAGED] (155114Z):** global+inflection aggregate LIVE at
  `s3://opal-data-assets/gold/mdpf_revamp/{global,inflection}/aggregate_aua_timeseries.json` (427 canonical
  trading days, 2024-11-01..2026-07-20); feed-gap Nones at 05-21 + 06-01/07-01/07-13/14/15; base merged my
  ledger spec + the Andrew-ruled axis note (c983589f5). Requested A4 dry-run + TBD ranges.
- **-> base (155630Z):** A4 dry-run DONE + STAGED + finalized enterprise/non_model ledger ranges to lock.
- **-> CTO (155642Z):** A4 STAGED for the co-verify slot + the derivation-identity evidence.

## Compiler Tools

| Tool | Situation | Result | Note |
|---|---|---|---|
| aws s3api list-objects-v2 (rail-checked, 13b) | A4 staging landing verify | PASS | key+ETag+Size (d4802341.../82101B), LISTING-based not HeadObject |

VALIDATE/DEPLOY window (no code change): the A4 producer was already committed; verification was the S3
date-join + the 13b listing verify. Rule-20 graph checks ride the CTO co-verify + AE publish, not a
re-run here.

## Deployment / staging + verification (DS gold artifact)

- **Staged (pure add, build-alongside):** `s3://opal-data-assets/gold/mdpf_revamp/global/non_model_assets.json`
  -- ETag `d4802341934a7e68203f6f83d1b80102`, Size 82,101B, 433 rows. Landing verified via ListObjectsV2.
- **A4 build output:** 297 legacy passthrough (pre-cutover) + 136 derived post-cutover (6 gap-skipped =
  base's exact feed-gap Nones) = 433 rows; validation PASS (identity exact, residual sane, no trap-2).
- **Date-join A4-vs-served verification:**
  - PRE-CUTOVER passthrough ties served EXACT: 297 dates, max abs diff $0.0000.
  - A4 enterprise/model @07-17 last-common TIE base's staged aggregate to the cent
    (ent=$1,803,111,389.71, mod=$1,535,050,357.39). non_model=$268,061,032.32.
  - Derivation identity |ent-mod-nm| = $0.0000 in EVERY post-cutover window.
  - Axis symmetric-diff: 427 common, 6 A4-only (published-only real trading days incl 07-20 frontier), 28
    served-only (Andrew-ruled weekend/holiday named-omissions + feed-gaps). All NAMED.
  - post-cutover deltas vs served: enterprise [-3.4,+6.7]% (padded), non_model wide [-18,+27.5]% (residual,
    carries D-1 model + D-2 custody-full-envelope). latest 07-17 nm +8.79% vs served = the D-2 +$20M
    full-envelope custody correction (named, inherited from base's aggregate).

## Blockers

None. A4 headline ties by construction; the delta vs served is entirely base's ruled D-1/D-2 (inherited).
Awaiting CTO gate verdict + DT date-joined parity (the N=3 co-verify) -- not a blocker, the normal gate flow.

## Current State (zero-context handoff)

- **A4 STAGED + VERIFIED for the N=3 co-verify.** Artifact:
  `s3://opal-data-assets/gold/mdpf_revamp/global/non_model_assets.json` (ETag d4802341..., 433 rows).
  Producer `data/mdpf/scripts/gold/dim_mdpf_non_model_assets.py` (commit 64c5a52a0). Reads base's staged
  global aggregate (opal_aggregate_aua[]/model_aua[]/dates[]) + inflection (2b audit). Latest 07-20: ent
  $1,813,038,832.72 / mod $1,538,370,912.28 / nm $274,667,920.44 / 15.15%.
- **Ledger:** base merging non_model_assets/global (Andrew-ruled axis note in @ c983589f5); I sent the
  enterprise_history_windows + non_model_history_windows pct_ranges (padded +/-0.4) to lock.
- **CTO 3-pass gate in flight:** DT date-joined parity + base S3 re-verify + AE publish to portal/*. A4
  co-verifies right after the global-aggregate verify (CTO 144157Z).
- **Open named deltas:** A4-D4 real-vs-rederived (inherited D-1/D-2); A4-D1 axis (Andrew-ruled omission);
  A4-D5 etf_public_residual=0.0 (deferred audit, post-N=3 fast-follow).

## Next Steps

- **[1.0.0_SA_CTO]** S3 re-verify the staged A4 (derivation identity ent-mod==nm, ties to the staged
  aggregate) + gate verdict; DT date-joined parity as part of N=3.
- **[0.4.0_DS_ClientPlatform (base)]** Lock the A4 ledger ranges; run its own aggregate N=3.
- **[me / 0.4.0_DS_ClientPlatform~A]** Event-driven: respond to any CTO/DT co-verify finding; re-stage if a
  rework is requested. Post-N=3: etf_public_residual single-source fast-follow (D-5).
