# ADVI_TAGATTR leg-2/DS-2 resolution + COTMVP-B producer un-stall (coordination window)

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE
**Serial:** 0.4.0_DE_ClientPlatform - **Date:** 2026-07-01 - **Window:** ~1407Z (since log 9657ec07f) -> ~1516Z

**Workspace CLOUD commit:** `cf4d23f01` (ADVI_COTMVP.B-DS TO)
**Portal:** no code change this window (both TAGATTR follow-ons resolved to ZERO FE change).

## Summary
Continuation of the same-session 49F work. This window = coordination + grounding (no new FE code): drove the ADVI_TAGATTR follow-on legs to resolution and un-stalled COTMVP-B's producer end-to-end. Net: all three threads code-complete, event-gated on tonight's nightlies.

## Thread A -- COTMVP-B roster: producer UN-STALLED (stalled -> code-complete this window)
Proactively re-activated a gated project off a DS "no action" FYI. Ground-confirmed the gate still open (s3://opal-data-cot/platinum/firm/ has NO client_directory.json). COO owner-confirmed the emit onto base-DS (single-routed off the 06-30 base-COO/MSTR path). Wrote + GO'd `ADVI_COTMVP.B-DS` (TO `cf4d23f01`) with the EXACT schema CottonwoodClientsSection consumes ({households:[{household_id,display_name,aua}]}).
DS LANDED it in <15min: `build_client_directory()` in cot D_04.client_portal_summary.py (Step 11c), commit `bb2d62ef8` deployed+sha256-verified (cot-only, bd MATCH held). Offline-validated 218 households, all real names, sum $433.84M reconciles to clients_tab headline. **Accepted count = 218 (NOT 217)** -- 218 is the faithful clients_tab.headline.client_count; my TO's "~217" was an approximate from 06-30 memory; DID NOT filter to 217 (would fabricate a filter to match a stale number). Co-gated close on the cot nightly (DS comp-validate + my roster render + CVO count-verify 218). FE already live on PROD (07d5887f in v2.1.129) -> roster lights up on serve, zero FE change.

## Thread B -- ADVI_TAGATTR leg-2 (fees): landed, grounded, ZERO FE change
DS~A landed leg-2 (arch-gate-2 discharge, commit `3ba105354`): MIXED basis on employee_leaderboard.json -- AUA/NNA = aua_basis 'tagged_full_nonadditive'; FEE = fee_basis 'per_account_actuals_conserved_reconciled_to_c08_canonical'. CTO ADR resolved fees to CONSERVED (not full-tag) to avoid double-counting the C_08 billed total. Grounded the FE side: the leaderboard (AdvisorsTab) + Role Composition (RoleDonut) render NO fee-DOLLAR value (fee toggle only slices AUA, correctly non-additive); my only basis note (Role Composition helptext, a58ff3a7) is explicitly AUA-scoped (zero fee claim); fee-dollar panels (FeeSummary/FeeEfficiency/Income) source C_08 (unchanged). -> **Closed COO grounding-condition #2** (additive-safe, no mislabel). No FE change. DS~A owns condition #1 (DELTA=0 on the nightly).

## Thread C -- ADVI_TAGATTR DS-2 (total_aua no-infer): SHELVED
DS staged DS-2 (D_02/D_01 -> architect_no_infer, would drop advisor total_aua by House/impl-inferred AUA; commit 32d035b5b) then SHELVED it per Andrew (`bd40e393d`, low-usage surface + current number explainable). No FE watch needed for a number-move; dropped from my post-nightly pass. Hero/leaderboard/donut stay on the current inferred basis.

## Fee-basis Andrew alignment
Surfaced the mixed-basis (AUA full-tag / fees conserved) to Andrew as a possible deviation from his "fees all tagged" modal answer; DS~A clarified Andrew ALREADY ruled the account-level fee model live in their session (advisor's fee-% per account = conserved) -- so NOT a deviation, it's his call. Closed my own ask to Andrew (no action needed).

## Compiler Tools
No NEW comp-tool runs this window: pure coordination + grounding-by-code-read (RAVC on DS/DS~A landings + authored one TO). No portal-code change (leg-2 + DS-2 both resolved to zero FE change; COTMVP-B FE already shipped), so the DE schema-check/tsc gates rode the a58ff3a7 FE commit already logged in 9657ec07f. Grounding this window = native Read of CottonwoodClientsSection (schema extraction) + AdvisorsTab/RoleDonut (fee-render check) + aws s3 ls (cot client_directory absence).

## Blockers
None. All three threads event-gated on tonight's SCHEDULED nightlies (no-ad-hoc-gold GATE) -- not a stall.

## Current State
- 49F Advisors-tab boundary fix: LIVE PROD v2.1.129 (90322ba0). CVO PROD render-confirm pending.
- ADVI_TAGATTR: leg-1 (AUA/NNA full-tag, DS 0ab172d3f/fc8c18361) + leg-2 (fees conserved, DS~A 3ba105354) + FE (a58ff3a7, pushed DEV, rides 2nd promote) all landed. DS-2 SHELVED. Render-verify (leg-1) + DELTA=0 (leg-2, DS~A) on the bd nightly.
- COTMVP-B: producer landed (DS bb2d62ef8) -> cot nightly serves client_directory.json (218) -> roster renders on PROD (FE already live). TO cf4d23f01.

## Next Steps
- **[0.4.0_DE, me]** Post-bd-nightly: render-verify TAGATTR leg-1 (Travis architect full-tagged, donut center=dedup total ~$440M, tiles sum>center). Post-cot-nightly: verify CottonwoodClientsSection renders 218 clients sorted by $. RAVC COO at each.
- **[0.4.0_DS_ClientPlatform]** comp-validate Phase-3 on both post-nightly artifacts (TAGATTR leaderboard.json + cot client_directory.json); DELTA=0 (leg-2) -> RAVC COO+CTO.
- **[3.0.0_SA_CVO]** 49F Advisors-tab PROD render-confirm (v2.1.129) + count-verify 218 (cot roster) + TAGATTR leg-1 served-verify.
- **[0.4.0_DT_ClientPlatform]** 2nd promote carries a58ff3a7 -> PROD; hold portal/DEV pushes on the freeze signal.
