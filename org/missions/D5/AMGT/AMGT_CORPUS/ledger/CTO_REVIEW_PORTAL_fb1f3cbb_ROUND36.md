# AMGT_CORPUS round 36 -- CTO product-file review of portal `fb1f3cbb` (al-2, the 49 V3 rows on the Model tab) -- REWORK

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-04 ~22:1xZ. **Ask:** `2.0.0_SA_COO~X` msg 29275 (branch `wk-AMGT_CORPUS-1-portal`, outer
drain @66edd940a7).

## What I read

- **Surface:** 3 files under `src/pages/SecurityAnalysis/`: `modelSheet.ts` +154, `tabs/ModelTab.tsx` +64, `types.ts` +3.
- **Base:** DEV `ec65c5d637`. origin/DEV is now `35a723bf`, **155 commits ahead** of that base.
- **Trial merge** (`git merge-tree --write-tree origin/DEV fb1f3cbb`): **CONFLICT in `tabs/ModelTab.tsx`**. `types.ts` auto-merges.
  The DEV side of the conflict is DSGN_AMGTV1's own Model-tab work:
  - `7598a3b2` AV-zg-5, "What changed leads the Model tab";
  - `28a1a16c` AV-zi-1, the rolling-window presets.
- The Model tab now has two writers in flight: CORPUS (FWD-20's rows) and DSGN_AMGTV1 (the page's design).

## Verdict: REWORK. Not reviewable as cut, because the reviewed bytes would not be the pushed bytes.

1. Merge current origin/DEV into the candidate branch (a merge, never a rebase). Resolve `ModelTab.tsx` by KEEPING DSGN's order
   ("What changed" leads, the presets stay) and adding the V3 rows where al-2 places them.
2. On the merge, re-run `al2_check` and the harness. Also run DSGN's `round29/checks/battery29.sh` and the round-34/35 checks, so
   that FWD-20's rows do not undo DSGN's reviewed design.
3. Re-ask with the merged commit. I review that diff against origin/DEV, and the DEV push stays Andrew's word.
4. Coordination: `2.0.0_SA_COO~D` is told that ModelTab has a second writer in flight, so DSGN's round 36 merges after this lands, or
   the other way round. Never two candidates cut on the same file at once.
