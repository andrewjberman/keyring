# Andrew-direct 2026-10-13 ~13:5xZ -- brief request to the CRO: how per-box portal DEV work is handled today, and the strategy Andrew describes

**Relayed by:** `2.0.0_SA_COO~C` (laptop), at Andrew's word, to `4.0.0_SA_CRO` (laptop). **Not a decision:** nothing here is implemented; no gate is built (CLAUDE.md section 2, no inferred gates).

## 1. Andrew's words, VERBATIM

Question: *"Is the work from your box and all the other boxes all on DEV? What should be happening moving forward is that each Box has its own worktree and it must get approval on before merging forward to DEV. that way we can do PROD promotes with only approved DEV features."*

Instruction: *"i want you to relay this to CRO on this box and have them draft a brief covering how per-box DEV work is currently handled and what i am suggesting. Their brief should analyze what needs to happen to move this over to the strategy im describing."*

## 2. What the COO measured (portal repository `Opal-Capital/portal`, fetched 2026-10-13 ~13:3xZ; counts, not a full audit)

- `origin/DEV` is 200 commits ahead of `origin/PROD` (196 files, about 16,300 lines added, client-facing `src/pages/TicketCenter/` among them). `origin/PROD` is 32 commits ahead of `origin/DEV` (the `AV-zzs-1` work, e.g. 37aa1247ee), merge base 2d42e9b733: PROD has taken work that did not pass through DEV.
- Authors of the 200 PROD..DEV commits (top): `2.0.0_SA_COO~D2` 30, `0.9.0_WK_IRPT_ANLREQ~51` 14, `2.0.0_SA_COO~Y2` 12, `0.9.0_WK_DSGN_IRPTV1~49` 12, `~53` 10, `0.9.0_WK_AMGT_CORPUS~2` 10, then more DSGN_IRPTV1 workers. Nothing on DEV records whether a commit was approved.
- Remote branches ahead of DEV (not yet on it), examples: `cand-dell1-secclass-e53-r9` +4, `cand-dell1-secclass-e59-r10` +2, `irpt-dev-candidate-3-20260924` +3, `irpt-dev-candidate-7-20260924` +1, `irpt-opal-scope-p-portal-20260923` +1, `q/dell2/wk-IRPT_BCKEND-167-portal/r1` +2, `sitez/merge-trial-20260915` +2; many `wk-*-portal` branches exist too (ownership not checked).
- One NFRA_CTLPLN commit is on DEV: `53506d49` (the generated `firmAccess.ts` carrier, worker `0.9.0_WK_NFRA_CTLPLN~70`), landed by the integrator after CTO review, with no approval step from Andrew. It is the only DEV commit touching `src/lib/firmAccess.ts` since PROD.

## 3. What the brief is asked to cover

1. How per-box portal DEV work is handled TODAY: where each box (laptop, dell1, dell2, sitez) works (worktree, nested portal checkout, `wk-*-portal`, `cand-*`, `q/<box>/...` branches), who may push DEV and PROD (`.tools/hooks/never-rules-gate.sh`, `/prod-deploy`, the CLAUDE.md portal rules), what review exists before DEV, and how a PROD promote is cut now. Cite the files and the gate lines read.
2. The strategy as Andrew states it: each box has its own worktree/branch; a feature needs approval before it merges forward to DEV; PROD promotes carry only approved DEV features. Say what "approval" would need to mean in practice (who, where recorded, per feature or per commit), without inventing an answer where Andrew has not given one.
3. The gap and what has to happen to move over: the existing 200-commit DEV/PROD gap and the 32-commit PROD-only set; the unmerged candidate branches; the tools, gates, skills and law text that would change and their owners; a migration order; the risks.
4. Open decisions for Andrew, each with a recommendation.

Out of scope for the brief: building any gate or tool (Andrew has not asked for one to be implemented).
