# 49F Advisors-tab boundary fix (LIVE PROD) + ADVI_TAGATTR full-tagged advisor attribution (diagnosed -> routed -> FE)

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, IMPLEMENT, COORDINATE
**Serial:** 0.4.0_DE_ClientPlatform - **Date:** 2026-07-01 - **Window:** session start (~1244Z) -> ~1405Z

**Portal DEV commits:** `90322ba0` (49F Advisors boundary + Exec-Summary rename) -> `a58ff3a7` (ADVI_TAGATTR FE follow-on)
**Workspace CLOUD commits:** `0517a8397` (ADVI_TAGATTR.DS-1 TO) -> `ee396d9a0` (TO amend: CTO gates)
**Shipped to PROD:** `90322ba0` rode /prod-deploy v2.1.129 (`eb049b7e`, CI 28521963790 success) with `07d5887f` + `ad97d915`.

## Summary
Andrew-resume session, two live 49F AdvisorIntelligence issues Andrew surfaced directly:
1. **49F Advisors tab BLANK** (period-boundary) -- diagnosed with CVO, fixed, CVO-GREEN, now LIVE on PROD.
2. **Advisor AUA attribution inconsistency** ($440M vs $358M for Travis Penfield) -- Andrew ruled advisor AUA/NNA/fees must be FULL-TAGGED (not split-weighted). Source-grounded the mechanism, wrote+routed the producer TO to DS, folded CTO's 2 arch-gates, DS landed leg-1, I built the FE follow-on. Render-verify co-gated on tonight's nightly.

## Thread 1 -- 49F Advisors tab blank (period-boundary)
Root cause (CVO-triaged, DE-confirmed vs live `s3://opal-data-bd/platinum/firm/leaderboard.json`): windows.QTD entry_count=0 (data_as_of 06-29 predates Q3/Jul-1) while YTD/MAX/1Y/3Y=156 each. `AdvisorsTab` defaulted to `period='qtd'`; `resolveWindow`'s `??` only falls back on MISSING windows, not present-but-EMPTY -> whole tab blank on load, recurs every month/quarter turn.
**Fix (`90322ba0`):** default `period` 'qtd'->'ytd' (Andrew-direct) + derive `effectivePeriod` (auto-advance off an empty selected window to the freshest POPULATED PERIOD_OPTION while the user hasn't manually toggled; honest -- toggle highlights the shown window; recurs-proof; no-op when default populated). Also Andrew-direct: `AdvisorPublicProfile` panel title 'Executive Summary'->'Summary' + matching AdvisorAnalytics helptext xref.
CVO VERIFIED GREEN (all 5 bar cases + the `entries.length>0` linchpin + schema-check). LIVE on PROD v2.1.129.

## Thread 2 -- ADVI_TAGATTR full-tagged attribution
**Diagnosis (source-grounded):** `total_aua` = tagged dedup ($439.97M, correct) vs `sum(role_breakdown[*].aua)` = split-weighted ($358.34M). `D_00c.portal_leaderboard.py` applied `split_pct` "three-case" weighting to role_breakdown (~876-931); the FE Role Composition donut showed the role-sum as the center total = the $440M-vs-$358M mismatch Andrew saw.
**Andrew ruling:** advisor tagged to an account in a role -> FULL account AUA to that (advisor,role); an account counts fully under EACH role held; roles are NON-ADDITIVE (sum > dedup total). Applies to AUA+NNA+fees.
**Routed:** wrote TO `ADVI_TAGATTR.DS-1` (`0517a8397`), routed to DS via COO spawn (DS was offline). CTO GO'd direction + set 2 semantic gates -> folded into TO (`ee396d9a0`): (1) non-additive labeling (FE never sums advisors to firm total -- DE-VERIFIED: firm total is client-sourced from PartnerAnalytics, the lone cross-advisor sum AdvisorsTab summary.total_aua is unrendered); (2) fee-blast on C_08/E_23 before landing fees.
**DS leg-1 LANDED** (`0ab172d3f` D_00c + `fc8c18361` D_04, comp-pipescript deployed MATCH): role AUA/NNA/flows full-tagged; total_aua untouched; gate-1 labels (`aua_basis: tagged_full_nonadditive`) emitted + rescued from D_04's whitelist trim. DS correctly ground-truthed my TO hypothesis -- the canonical `aua_tagged_total` is a disabled `if False` ~5x-underscaled shadow (CTO STAUDT.FIX1), so recomputed from the trusted account_team melt. Leg-2 (fees) escalated to CTO ADR (full-tagging rebases C_08 billing total).
**FE follow-on (`a58ff3a7`):** Andrew chose "keep donut, center = true Total". Extended the existing clients/accounts dedup-center pattern to AUA/NNA (now required -- full-tagging makes them non-additive like counts): donut CENTER = `entry.total_aua`/`entry.nna` (dedup) for all metrics; tiles = per-role full-tagged; % pill = share of dedup Total (book, can sum >100%); honest helptext killing the false "reconciles to Total AUM"; non-additive guard comment on the unrendered AdvisorsTab summary rollup. Robust to both pre-nightly (split-weighted, tiles sum under) and post-nightly (full-tagged, tiles sum over) -- keys on dedup-center behavior, not the `aua_basis` label.

## Files Modified
See commit messages: DEV `90322ba0` (AdvisorsTab.tsx effectivePeriod + AdvisorPublicProfile/AdvisorAnalytics text), `a58ff3a7` (AdvisorPublicProfile RoleDonut center/helptext + AdvisorsTab summary guard); CLOUD `0517a8397`/`ee396d9a0` (DS-1 TO + gates).

## Compiler Tools
| Tool | Target | Result |
|---|---|---|
| `comp-transform schema-check` | AdvisorsTab (90322ba0); AdvisorPublicProfile + AdvisorsTab (a58ff3a7) | PASS -- all rendered fields match; no consumer sums role_breakdown as firm total (CTO gate-1) |
| `bun run typecheck` (tsc -b --noEmit) | portal, both fixes | exit 0 |
| `bunx eslint` | 3 files (90322ba0) + 2 files (a58ff3a7) | clean |
| `aws s3 cp` (leaderboard.json) | ground Travis AUA + per-window entry_count | operational grounding: QTD=0/YTD=156; total_aua 439.97M vs role-sum 358.34M |
| Grep/Read (native) + `git show PROD:` | D_00c split mechanism + FE consumer trace | source-grounded the mechanism (rule 22) |

**What worked:** served-artifact grounding independently confirmed CVO's boundary triage + pinned the attribution mechanism at source before proposing a fix (falsified my own TO's aua_tagged_total hypothesis -- DS caught it too). schema-check confirmed CTO gate-1 (no firm-total summation) airtight.
**Gap found:** the AdvisorPublicProfile Role Composition helptext CLAIMED "roles reconcile to Total AUM" -- false under both the old split-weight ($358M) AND the new full-tag; declarative drift, now fixed.

## Blockers
None. ADVI_TAGATTR render-verify is nightly-gated (my own no-ad-hoc-gold-run GATE) -- co-gated with DS comp-validate on the post-nightly served artifact; leg-2 fees held for CTO ADR. Not a stall.

## Next Steps
- **[0.4.0_DE, me]** Post-nightly: render-verify the Travis drilldown (center=$440M, architect tile full-tagged, tiles sum >total) on the regenerated served leaderboard.json; RAVC COO. Live-render the 49F Advisors tab on PROD (or hand CVO).
- **[0.4.0_DS_ClientPlatform]** comp-validate Phase-3 on the post-nightly artifact (co-gated close with me); re-emit fees if CTO ADR returns full-tag (ping me only if a rendered fee field changes).
- **[1.0.0_SA_CTO]** fee-basis ADR (leg-2): full-tag fees vs keep the C_08-coupled split basis.
- **[0.4.0_DT_ClientPlatform]** push `a58ff3a7` to DEV (COO-routed) -> rides the 2nd promote to PROD.
- **[3.0.0_SA_CVO]** 49F Advisors-tab live-render confirm on PROD v2.1.129.
