# ADVI_INFFEE investigation + brief->PRD, and INF/49F served-render verifies

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE (primary), COORDINATE, VALIDATE

Serial: 0.4.0_DE_ClientPlatform | Window: 2026-07-06 ~20:50Z (this-session start, post the 15:50Z inf-freeze log 4ce2af4bd) -> 21:37Z | Andrew-live-driven + COO DRIVE.

**Workspace CLOUD commits:** `f700e34cd` (brief). CTO authored PRD `5d6b269b6`.
**Portal DEV commits:** none (investigation + render-verify only; no FE edits this session).

## Summary

Andrew live-smoked the Inflection Books/Firm Overview panel and flagged the account counts don't reconcile (Fee 789 + Non-fee 1 = 790, but Total Accounts = 868; and 1 non-fee account holding $67M ~= 1/3 of book). Investigated + ground-truthed to a gold-layer residual + a billing-dim coverage gap (NOT a frontend bug — the FE is a faithful passthrough). Wrote a brief -> CTO, who authored PRD ADVI_INFFEE and decomposed it into 3 TOs (AE audit -> DS~A gold-revise -> my FE regrain). Then executed COO's render-verify order: INF + 49F served-render both SOUND, RAVC'd + accepted.

## What I did (grounded)

1. **ADVI_INFFEE investigation (source + served-artifact grounded).** Traced the Firm Overview cards through ConsolidatedOverviewPanel.tsx (render) + ClientsTab.tsx:831-857 (card build) — pure passthrough of the served headline. Ground-truthed the served artifacts: `header_metrics.json#total` = {account_count 790, fee 789, nonfee 1, fee_aua 135.5M, nonfee_aua 67.0M, fee_clients 294, nonfee_clients 13}; `clients_tab.json#headline` = {account_count 868, client_count 300}; sum of the 300 households' account_count = 868. Three account universes stitched into one card row: **868 custody** (clients_tab) vs **790 billing** (header_metrics = 789+1) vs **300 clients**.
   - **Root cause A (data):** non-fee is a pure residual with MISMATCHED denominators — `INF_D_04.client_portal_summary.py:798-802`: `non_fee_aua = total_aua(custody 202.5M) - fee_aua`; `non_fee_accounts = account_count(billing 790) - fee_accounts`. -> phantom "1 account = $67M". Decisive tell: 13 non-fee CLIENTS but 1 non-fee ACCOUNT (impossible for real data). Code already flags the class (`types.ts:437` residual_clipped_pending_canonical_rerun, expected ~$19.6M vs observed $67M).
   - **Root cause B (completeness):** 868 custody - 790 billing = 78 accounts with no billing-dim row.
   - **Root cause C (presentation):** custody-grain Total (868) next to billing-grain fee splits (790) can't reconcile on-screen; same reason Distribution bell-curve(790) != Books Total(868).

2. **Brief -> CTO, issued PRD request (f700e34cd).** `docs/briefs/advi-inffee-fee-classification-audit-brief-20260706.md` with root-cause separation, Andrew-specified 3-owner TO decomposition (0.6.1_AE audit / DS~A gold-revise / me FE regrain), acceptance criteria, full Rule-22 grounding citations. CTO authored PRD `5d6b269b6` (`docs/architecture/ADVI_INFFEE_PRD.md`), corrected my 49F note (49F uses a POSITIVE tagged-role invariant `bd D_00c:623`, so the bug is INF_D_04-specific; 49F is an AC5 verify-target not a shared fix), and framed the grain decision (Option 1 custody+unclassified-bucket recommended). My TO-3 is sequenced last + gated on TO-2 publishing the field schema first (anti-guess).

3. **INF served-render verify = SOUND (RAVC-accepted).** Served header_metrics.total.aua = 202,542,849.81 @ data_as_of 07-02, as_of_by_dim {aua:07-02, nna:07-01}, gen 12:59 EDT. FE path exercised: PartnerAnalytics.tsx:243-244 auaDonutTotal = total.aua, GUARDED against total.total_aua (which is None — reading total_aua would've been a null/NaN render bug). Corroborated by Andrew's own 16:57 EDT screenshot showing $203M @07-02 (the FRESH unfrozen value; frozen was 201.69M) = no stale-01 CDN cache.

4. **49F served-render verify = SOUND, both limbs (RAVC-accepted).** (a) opal-data-bd/platinum/firm/header_metrics.json total.aua = 1,837,159,865.68 @07-02, same .aua-vs-None guard, as_of_by_dim null (INF-specific, expected). (b) Mixed-vintage: mix_summary wrapper 07-02 but nested `composition` @07-03 (D_03 WARN-skip last-good), composition.mix 3 classes + an 'unclassified' key. firmComposition (ClientsTab.tsx:350-356) = normalizeMixTo4Class(mix.composition) with `if(!mix) return null` guard; normalizer (composition.ts:95-116) seeds canonical=0, SKIPS non-canonical 'unclassified' (line 100), empty->graceful placeholder. DECISIVE: no vintage cross-check anywhere -> fresh-header(07-02) + last-good-donut(07-03) cannot break the page.

5. **Finding parked (anti-speculative-build):** as_of_by_dim is NOT consumed anywhere in portal/src (grep clean) — FE renders a single data_as_of. Routed to DS~A (via COO) as a WS-4 AC-2 scope/intent question: served-side-only metadata (FE correct as-is) vs. visible per-dim labels (small DE-lane wire). Holding the wire pending intent.

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| docs/briefs/advi-inffee-fee-classification-audit-brief-20260706.md | New brief -> CTO for PRD ADVI_INFFEE | Yes — CLOUD `f700e34cd` |

No portal edits (investigation + render-verify only).

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| comp-which | "where does Books Firm Overview fee/non-fee/total account counts come from" | routed | near-tie surface; proceeded with comp-grep + Grep/Read |
| comp-grep | "non_fee_earning_account_count" data/inf/scripts | PASS | pinned the producers (INF_D_04:798-802 residual, :3691-3698, INF_D_02) + systems-context |
| (HUD nudge) | comp-transform schema-check on ConsolidatedOverviewPanel | noted | render-VERIFY (no prop change) -> grounded via code-path exercise + served payload instead; TO-3 will run schema-check when TO-2 renames/adds fields |

**What worked:** comp-grep decisively located the residual producer with dependency context, turning a hypothesis into a source-confirmed mechanism (Rule 22). **What failed:** none. **Gap found:** none. Grounding note: field-granular served-artifact inspection (exact account_count / fee_earning_* values, as_of_by_dim content, mix.composition vintage) used raw aws — the ground-truth layer comp-freshness/comp-pipescript wrap but don't surface at field grain; operational/off-rail. Render-verify grounding = served-payload + FE code-path exercise (COTMVP.B/TAGATTR pattern), not a config read.

## Current State

- **ADVI_INFFEE:** PRD authored (`5d6b269b6`), COO decomposing. TO-1 (AE billing-dim audit) -> TO-2 (DS~A INF_D_04 gold-revise + grain decision + publish field schema) -> TO-3 (me, FE regrain + schema-check + render-verify). My TO-3 GATED until TO-2 schema lands.
- **Render side of the INF/49F un-freeze:** DONE — both SOUND + RAVC-accepted; Andrew's live numbers are render-clean.
- **as_of_by_dim render-scope:** held pending DS~A intent answer.
- **WS-4 AC-2 render-side:** synced DS~A (which artifacts carry labels, whether any FE change is expected — suspect no-op for me until the as_of_by_dim intent resolves).

## Next Steps

- **[0.4.0_DS_ClientPlatform~A]** answer the as_of_by_dim intent (served-side-only vs visible labels) + which WS-4 AC-2 artifacts have labels landed; owns TO-2 (INF_D_04 fee-block revise + grain decision) and must publish the final field schema to me before I wire TO-3.
- **[0.6.1_AE_PartnerETL]** TO-1: billing-dim coverage-gap audit (78 of 868 accounts no billing row; build_billing_dim.py + Orion feed).
- **[2.0.0_SA_COO]** GO's the hard TO-1->TO-2->TO-3 sequence.
- **[0.4.0_DE, me]** event-driven: on TO-2 schema publish, run comp-transform schema-check + wire the Books/Distribution regrain (TO-3), render-verify vs re-emitted clients-tab-slim. Pick up the as_of_by_dim label-wire only if DS~A confirms visible-label intent. Nothing to build until then.
