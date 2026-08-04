# DEPLOY LEDGER: Canonical-map portal DEV->PROD promote (pinned 0576ef22)

**Opened:** 2026-08-04T05:58Z by `0.2.0_DT_PortfolioAnalytics` (at deploy START, per NEVER#6)
**Status:** **OPEN -- promote in progress**

## Authorization
- Andrew-direct ~0545Z at the 0.4.0_DE terminal, verbatim committed @c6b19d7f67: *"deploy as soon
  as we're clean and clear on all frontend changes"* -- supersedes the {emitter landed + first
  clock-v3 fire green} sequencing (CTO formal discharge 055142Z; MSTR relay 055244Z).
- COO explicit GO 20260804T055352Z: promote 0576ef22 to PROD NOW; re-scoped conditions
  {frontend clean + gate-run green} both MET in COO's hand.
- Scope pin (COO 052920Z, CTO concurred 053007Z, DE concurred 052926Z): promote head =
  **0576ef22** (tree-identical to reviewed 7d544d27 + CI-parseable SURFACE_ACK). d32f5a52
  (kill-list row 15) is DELIBERATELY unpublished -- next cycle, own review chain. Local DEV
  sits one commit ahead of origin/DEV BY RULING; do not push it in this window.

## The change
- Portal PROD: c6f561b6 (tag portal-v2.1.155) -> merge of origin/DEV @0576ef22.
- Content = 7d544d27 (CANONICAL MAP realized, Andrew voice memo @7a585074e + CI-R6R T2/T3
  participation rendering) -- 0576ef22 is an empty ack-format commit, tree-identical.
- SEV1 surfaces touched (acked): model_portfolios.benchmark + model_portfolios.headline via
  src/pages/ModelPortfolios.tsx; ack audited 20260804T041944Z + CI-parseable on the pushed record.

## Pre-verified (before this ledger opened)
- [x] Typecheck: canonical `tsc -b --noEmit` at exactly 7d544d27 in an ephemeral worktree, true
      rc=0 (0576ef22 tree-identical => carries over). NOTE: skill Step 2's main-tree typecheck is
      DEVIATED-BY-RULING -- the main tree sits at d32f5a52 (held local), so a main-tree run would
      measure the WRONG tree; the artifact-binding checks are the pinned worktree run + the
      VALGATE pre-push tsc on the merged tree at push time.
- [x] CI on 0576ef22 by headSha: Build+Validate run 30880952307 SUCCESS (watched to conclusion) +
      Surface-Check Gate run 30880952383 SUCCESS (empty-range short-circuit DISCLOSED; COO
      adjudicated MET-WITH-DISCLOSURE 054422Z on composed evidence).
- [x] Ack extraction pre-exercised over the ACTUAL promote range origin/PROD..0576ef22 with the
      CI's exact sed: extracts the full reason; changed files = ModelPortfolios.tsx +
      pairedProvenanceRead.ts (expected set).

## Legs
- [ ] Step 3: local PROD re-asserted from origin (update-ref)
- [ ] Step 4: ephemeral worktree, foreground bun install, --no-ff merge of origin/DEV,
      parity gate `git diff origin/DEV HEAD` EMPTY
- [ ] COO ADDENDUM (adjudication 054422Z): BY-HAND comp-surface-check on the real merged tree in
      the worktree, output READ, verdict cited here -- the observed composition at the last
      reversible moment
- [ ] PROD push (integrator leg per standing -- MSTR push or audited-override with MSTR prior
      no-objection) + VALGATE/tsc pre-push gates PASS
- [ ] Step 5: deploy.yml run conclusion=success via `gh run view --json` (never watch); annotated
      tag peeled (`<tag>^{commit}` == PROD head)
- [ ] Step 6: workspace submodule pointer commit on CLOUD (integrator pushes)
- [ ] Step 7: worktree teardown + prune; main tree verified on DEV; end at workspace root
- [ ] Step 8: RAVC completion report to COO + CTO + MSTR (releases freeze); session log

**Close condition:** all legs checked, artifact table in the Step-8 report, this file flipped to
CLOSED with the completion timestamp. An unclosed ledger at session end = COO alarm (NEVER#6).
