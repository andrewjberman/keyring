# MDPF_REVAMP.S5 — flip gate, half-landed catch, P0 Global-2x (found/fixed/shipped), re-land FE

**archetype:** MIXED
**secondary_archetypes:** VALIDATE, DIAGNOSE, IMPLEMENT, COORDINATE
**Serial:** 0.4.0_DE_ClientPlatform · **Date:** 2026-07-22 (0025Z–0640Z) · **TO:** MDPF_REVAMP.S5-ROLLOVER (CTO-gated)
**Window:** since `mdpf_s5_a2_canonical_redirect_2233Z.md` (2026-07-21) → now.

## Summary
Ran the CTO-gated flip-gate render-check on the live coherent-9, then the pre-flip throwaway 404-catch. Caught that the flip was **half-landed** (data live, my FE local-unpushed). After Andrew found the Global trend ~2x wrong, diagnosed it to an **FE axis-binding defect that predates MDPF and was live on PROD**, fixed it, shipped it standalone to PROD, and assembled the re-land FE. Corrected three of my own over-broad claims in-window.

## Work done (the arc)
1. **Flip-gate render-check (S12, `7c31a1c5e`):** pulled the coherent-9, **md5-verified all 9 against CTO's ETags**, route-injected into ModelPortfolios @`aa8c0420`. 6/6 cells clean. Frontier-count coherence proven (agg `account_count` == dist, all 3 firms: 7560/7026/534; firms sum to global). CTO independently verified → **render leg ACCEPTED**.
2. **Pre-flip throwaway 404-catch (S13, `59c6617ca`):** CTO decision (A). All 9 `/api/general/*` on AE's throwaway → **200 application/json byte-identical to source, 3 runs**, zero 404/text-html → repoint seam closed. **Surfaced two of my own harness artifacts** (toggle-state leak; a firm-reselect bug that mislabeled global shots as 49F) and corrected an over-claim to CTO rather than letting it stand.
3. **HALF-LANDED CATCH (the consequential one):** grounding CTO's "what does opalinvest.dev actually serve" question revealed my 4 MDPF FE commits were **local-unpushed** (`ahead 4`), on no remote branch, while the DATA flip was live → the served FE lacked drop-null-rows → picket-fence risk. Root cause = declarative drift: the record said "LANDED on DEV", reality was local-committed. Pushed to origin/DEV; escalated to CTO + COO per the half-landed-deploy NEVER-rule.
4. **P0 Global-2x — diagnosed, fixed, SHIPPED (S14, `481a0db83`):** Andrew saw Global month-end totals ~2x wrong (49F/Inflection clean). DS ruled out data. Found it: the monthly x-axis binds to a **year-less** label (`:1650-54` → `dataKey="period"` `:1703`) while **only Global** renders the full since-inception window (`:1472-80`; per-firm = rolling 1yr) → duplicate recharts category keys → tooltip binds to the FIRST matching row. **Exercised headed:** the Apr-2026 bar reported "April 30, 2025 | $988M" at its true $1.59B height (= 1.60x). Fix = bind to unique `fullDate` + year-disambiguated tick; binding-only, bars provably unchanged. Proved it **live on the unmodified PROD build** with real legacy artifacts (Apr 30: $963.5M vs $1,608.9M = **1.67x**) → shipped standalone as portal `8fd61dbf` → DT promote.
5. **Standing duplicate-key gate (CTO-adopted):** behavioral — hovers every bar, asserts distinct dates. **My first gate build reported PASS on the KNOWN-BROKEN build** (headless never fires the tooltip → unique `(unresolved@i)` placeholders → trivially distinct → guaranteed PASS). Caught **only** by running the negative control. Fixed fail-closed + must-run-headed + a retry.
6. **Re-land FE (portal `129edad5` → `6287847c`):** folded the 2x fix; then caught the Global daily drawing **six drop-to-zero collapses**. Diagnosed: `getNonModelAumForDate` is a ROLL-FORWARD (never null), so a whole-day gap row was PARTIAL-null and survived my all-plotted-null filter. Fixed per CTO's product call by keying on the producer-declared `meta.honest_none` marker → row drops → bridges. Both DEV gates GREEN on `6287847c`; CTO **visual-confirm PASSED** on the committed BEFORE/AFTER evidence (`5d9a851bc`).

## Corrections I issued on myself (all verified at source, flagged not buried)
- **SMA "omission"** — WRONG (`fe86fd92d`). `non_model_aua` is the residual `custody − core-model`, so SMA is already inside it, counted once. My no-double-count conclusion held; the omission inference did not.
- **"zero FE change"** — over-broad (`ab6ae0a73`, S13a guardrail). True for the global-only rebase; FALSE generally — per-firm `non_model_aua` is display-load-bearing via raw reads `:872`/`:935`, so a per-firm rebase is FE-VISIBLE, not a repoint.
- **"data regression / content loss"** — WRONG. The prior 5/7 per-model values were **49F-only wearing a global label** (INF=None) = the $107M false dip distributed into the bands. It was fabrication REMOVAL; my earlier render was "clean" only because the chart drew a wrong number.

## Files Modified / Commits
See commit messages: workspace `7c31a1c5e`, `59c6617ca`, `481a0db83`, `fe86fd92d`, `ab6ae0a73`, `5d9a851bc`. Portal: `8fd61dbf` (PROD hotfix branch `hotfix/global-monthly-axis-key`), `129edad5`, `6287847c` (DEV). Also pushed the 4 stranded MDPF FE commits (`2f603319`…`aa8c0420`) to origin/DEV.

## Compiler Tools
| Tool | Result | Note |
|---|---|---|
| `aws s3api list-objects-v2` / `s3 cp` (rail-checked) | PASS | ETag/md5 pinning of the coherent-9 and the re-land frozen-9; `comp-freshness` returns a verdict, not a downloadable key manifest |
| `/frontend-dev` render harnesses (route-injection) | PASS | ~30 headless + headed renders READ, not just exit-coded; the mandatory portal render gate |
| `assert_unique_categories.mjs` (NEW, CTO-adopted standing gate) | PASS (after fix) | negative control caught it falsely passing → fail-closed + headed + retry |
| `tsc -b --noEmit` (portal) | PASS x5 | after each FE change incl. the isolated hotfix on the PROD base |
| safe-commit surface-check | BLOCKED→ACK | SEV1 block-with-ack; note TWO independent ack mechanisms (CI `^SURFACE_ACK:` message line vs local ENV var; the latter SKIPS in a standalone worktree) |
| `git worktree` (ephemeral, PROD base) | PASS | isolated hotfix without the main tree leaving DEV (Rule 19); `git stash` correctly blocked by the shared-worktree gate |

**What worked:** running the negative control on my own gate (it was structurally incapable of failing); grounding CTO's deploy question against branch/CI reality rather than the record. **What failed:** three inferences of mine ran broader than what I had verified — each caught, retracted, and recorded. **Gap found:** the duplicate-key class had no detector; there is now a standing behavioral gate.

## Blockers
None on my side. Remaining items are external gates: the fresh never-widen co-sign + CTO GO → 0.2.0_DT promote.

## Current State
- **PROD:** portal `8fd61dbf` (branch `hotfix/global-monthly-axis-key`, off `2c802d13`) pushed to origin, handed to DT, CTO surface-ack verified. Fixes the live 2x.
- **DEV:** portal `6287847c` = re-land FE (2x fold + honest-None bridge + content-A/B + A2). Surface-Check Gate `29896944168` SUCCESS, Build `29896944203` SUCCESS, tsc clean.
- **Render evidence (committed):** `org/tier2_senior/0.4.0_DE_ClientPlatform/deliverables/mdpf_reland_render_20260722/` (6 AFTER cells + BEFORE + README). P0 kit + standing gate + fix patch: `.../deliverables/mdpf_p0_global_2x_20260722/`.
- **Audit doc:** `docs/briefs/mdpf-revamp-s5-rollover-FE-consumption-audit-20260721.md` S12/S13/S13a/S14.
- **Ephemeral worktree** `/c/Users/AndrewBerman/Desktop/_portal_hotfix_wt` still parked (tear down after DT completes). Dev servers on :5175 (DEV) and :5176 (hotfix).
- Data pinned: re-land frozen-9, global aggregate ETag `c27e1f37`; identity `oaa == model_aua + non_model_aua` holds on all 427 dates.

## Next Steps
- **[1.0.0_SA_CTO]** fresh never-widen co-sign + GO (the 0159Z co-sign is VOID — pinned pre-fix ETags).
- **[0.2.0_DT_PortfolioAnalytics]** owns both promotes (single-lane, COO-enforced): the PROD hotfix `8fd61dbf` and the re-land FE `6287847c`.
- **[0.4.0_DE_ClientPlatform]** (self) POST-PROMOTE HARD GATE — re-run 6-cell + duplicate-key + Global-daily-continuity against the **real served** opalinvest.dev build. DEV-harness renders are necessary-not-sufficient (the first flip proved a DEV render can pass on a build the site never served). No JWT → my pass covers served-build load + axis binding + continuity + no-crash; **Andrew's two-"Apr 30"-bar hover is the values-half confirm**; CVO cycle-1 is the third limb. Rollback armed until all three read clean.
- **[0.4.0_DE_ClientPlatform]** (self) tear down the hotfix worktree post-promote; queued non-gating: the pre-existing "Total AUA" vs "AUM" firm-card label inconsistency.
