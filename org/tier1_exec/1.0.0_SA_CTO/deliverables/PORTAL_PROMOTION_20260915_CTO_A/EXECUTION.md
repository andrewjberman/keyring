# Portal promotion execution — 2026-09-15

Executor: `1.0.0_SA_CTO~A`. Status: **STARTED; PROD NOT YET MOVED**.

## Authority and exact release

MSTR's explicit **GO 97048**, exact root-level inbox notice at 11:52:03 UTC, was read and ACKed at 11:53:01 UTC. The verbatim message is preserved in `GO_97048.md`. It designates this exact seat as the Andrew-directed non-DT executor and binds the audited portal-push override to Andrew's deadline ruling. Authority records: `4524cc2466` (~07:4xZ merge/promote) and `02e9cb858c` (`ANDREW_DIRECT_20260915_080xZ_PORTAL_PROMOTED_BY_9AM_EASTERN.md`). Deadline: **13:00 UTC / 09:00 Eastern**.

- Admitted DEV candidate: **`9adad7ce750742e9806c373a71f7ce900f3e22b2`**.
- Required candidate tree: **`d3db406c198b325fee48790a84205f0695c6d7c2`**.
- GO-time live PROD / proposed rollback base: **`b1389c85759511e65ec5d5b26ee96d63c91984c2`**, to re-read before the merge.
- Required merge: no-ff, **second parent = admitted DEV SHA AND tree = admitted tree**, plus empty candidate-to-merge diff. Literal merge-HEAD equality to DEV is not required.
- AMGT is excluded. No other DEV pushes or main-tree merges are permitted during the active MSTR freeze.
- Runtime procedure: `.claude/skills/prod-deploy/SKILL.md`, read end to end at execution start; Codex exact-seat inbox/runtime rules supersede its Claude inbox helper examples. MSTR retains workspace pointer/publication ownership.

## Accepted proof and limitations

The prior source, lockfile and CI checks are pinned in `PREPARATION.md@323e1fdd75`. GO binds the IR gate (2 routes, 1 nav item, 3 partner exclusions) to the candidate. The required `10c2f07d4da3795c0e404a92a8b9515259e42be7` ancestor and candidate source checks are re-read at execution.

MSTR accepts presentation proof with a **named vintage qualifier**: Site Z reports 544/544 cells equal served values, mutation discrimination and no unrounded values; Satellite 15 and 80 render checks were 272/272 each on Positioning source identical to the candidate. At 11:51 UTC, `characteristics.json` still has reported VersionId prefix `PXyBGaqn`, published 08:10:03 UTC, with 23 positioning-data-sourced holdings dated 2026-09-11, while `positioning_data.json` reports 2026-09-14 since 11:06:20 UTC. **This execution does not call those vintages aligned.** The page reads the data key live; MSTR explicitly owns post-promotion verification after the third driven re-serve or the 12:30 UTC organic run. GO permits promotion with this qualifier and replaces the earlier wait for an unqualified new-SHA data recheck.

Known exceptions remain named: F25-AC8 line-ending instrument issue; F49-AC8 pre-merge invariant; all five lint errors adjudicated by CTO 97040 (two unused SentimentGauge imports, unused pre-envelope PERFORMANCE_KEY, ExportButton DOM/hook immutability diagnostic, historical alias-probe constant expression). DEV CI **34957141198** passed Install, failed lint, and skipped later checks. It is not green. Separate clean Bun 1.3.9 install/typecheck/build and the manual provenance-guard proof are attributed as in preparation. Required PROD deployment workflow success is not waived.

## Complete deployment ledger

Opened before execution mutations at 11:55 UTC:

- Ledger: `org/critical_paths/change_management/20260915T1155Z_portal-prod-promote-20260915-0900et_deploy_completion.md`.
- Sentinel: `org/critical_paths/.open_deploys/portal-prod-promote-20260915-0900et.json`.
- Seven declared legs: L1 admission/preflight; L2 PROD merge/push; L3 deployment/tag; L4 served artifact/behavior; L5 MSTR-owned workspace pointer/publication; L6 cleanup/report/freeze release/session log; L7 MSTR-owned characteristics vintage follow-up.

Every leg closes only against its actual proof. A still-pending MSTR follow-up stays visible rather than being represented as complete. After a failed PROD push/deploy, surface the exact failure to MSTR/CTO immediately; no unilateral revert or repush is authorized by the prepared rollback SHA.

## Execution observations

At **11:53:52 UTC**, independent `ls-remote` showed DEV at the admitted candidate and PROD at the recorded base. Main portal was DEV at that candidate with zero tracked changes. Bun resolved through PATH and printed **1.3.9**. Existing peer integration worktree remained on `43f18c17`; it will not be altered. The executor uses its own fresh candidate checkout for all-files cleanliness and a separate ephemeral PROD worktree; main portal stays DEV. No PROD branch, merge, push or installation has occurred at this initial record.

Further evidence and exact results are appended as execution proceeds.
