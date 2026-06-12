# D5-FIX ORPHAN-AI+MISC (27 files) — LANDED; PORTALSWEEP fix-phase DONE
**archetype:** DIAGNOSE
**secondary_archetypes:** DEPLOY, COORDINATE
**serial:** 0.4.0_DE_ClientPlatform
**window:** ~2049Z -> 2109Z 2026-06-12

## Summary

Andrew put 0.4.2_RD_AdvisorIntelligence online to co-investigate the last orphan clusters
(true-orphan vs WIP). Joint DE+RD verdict: ALL ABANDONED, 0 paused-WIP. Andrew's partner-alternative
hypothesis DISPROVEN. Set expanded 19->27 via 2 census deltas. Andrew product-confirmed all 27 +
the v2.1.122 promote; applied on portal DEV (ab1c11b0), signaled DT. Closes the ENTIRE PORTALSWEEP
fix-phase.

## Investigation (Andrew-directed: explore logs/scenarios, rule out partner-alternative)

- Partner-alternative hypothesis DISPROVEN: AI orphans NEVER referenced in _partners/ (any firm/
  history); no firm-keyed registry / template-literal dynamic import; ALL 11 created in the SAME
  refactor commit 9423f71e as unwired scaffolding; live siblings (AdvisorBookAccountModal/
  ClientListPanel) are shared across all firms via AdvisorBookView.
- RD domain calls (5f38fd3f3): 11/11 ABANDONED, each from own git+roadmap+TO/PRD evidence.
  Resolved my one ambiguity (AdvisorBookAccountDetail :57 slot-comment = stale pre-modal docstring;
  modal is the live L4).
- 2 census deltas (RD + I both found AUATrendChart independently):
  - AUATrendChart: orphan->orphan (sole importer = orphan AssetIntelligenceTab) -> added.
  - Entire _shared/ClientDetail/ subtree: I verified resolved-path 9/9 0-external-inbound (the
    crude-grep types.ts=106 was stem noise) -> +7 new files. Old pre-AdvisorBook drill.
- MISC 8: my git archaeology = all abandoned (split-orphans / superseded / never-wired Tab2).

## Deployment sequence

1. Pulled clean DEV (HEAD==origin/DEV 73d2436a, behind 0, clean)
2. Re-verified 27 present + 0-inbound (AI 11+ClientDetail 9 [2 barrels overlap] + AUATrendChart + MISC 8)
3. git rm 27; tsc -b --force EXIT 0 + vite build EXIT 0 (14.25s); comp-transform schema-check AdvisorBookView PASS (Rule 20)
4. Commit ab1c11b0; push origin DEV -> VALGATE D-1 PASS; surface-check OK (27 files, no critical surface)
5. Signaled DT (origin/DEV HEAD ab1c11b0) for v2.1.122; pinged RD to rebase their 2 lane edits

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| comp-transform schema-check | AdvisorBookView | PASS | live AI surface unaffected by the deletions (Rule-20 pre-commit) |

What worked: ephemeral-worktree proof + resolved-path detector caught the ClientDetail stem-grep
FP (types.ts=106 was noise) and the AUATrendChart orphan->orphan; joint DE+RD dual-validation gave
Andrew a clean approve. D8 clean: dead _shared scaffolding are not registered critical surfaces.

## Files Modified

portal DEV ab1c11b0: 27 deletions (see commit message — AI 19 + MISC 8). No PROD (DT promotes).

## Blockers

None. ORPHAN-AI/MISC closed; v2.1.122 promote handed to DT.

## Current State

- portal DEV HEAD ab1c11b0 = origin/DEV. 27 abandoned orphan files removed.
- ENTIRE D5 PORTALSWEEP fix queue DONE: ORPHAN-PM (19, 5ad23559) + DC-01..07+ROUTE-01 (73d2436a) +
  ORPHAN-AI/MISC (27, ab1c11b0).
- DT promoting v2.1.122 (carries ESLINT-02 + DC/ROUTE + the 27 deletions to PROD).
- RD landing page_inventory.xml + AdvisorBookClientDetail:57 docstring concurrently (rebasing on ab1c11b0).
- Rule 19: main tree on DEV (only RD's concurrent edits in working tree, not mine).

## Next Steps

- [0.4.0_DT_ClientPlatform] promote v2.1.122 off current origin/DEV.
- [0.4.2_RD_AdvisorIntelligence] land page_inventory.xml refresh + docstring fix (rebased on ab1c11b0).
- [0.4.0_DE_ClientPlatform] PORTALSWEEP fix-phase complete; standing by. Banked: getPlatinumClientDetailStatic
  schema drift T1b (next portal pass).
