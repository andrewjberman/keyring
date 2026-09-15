# Portal promotion execution — 2026-09-15

Executor: `1.0.0_SA_CTO~A`. Status: **DEPLOYED; CI AND SERVED ARTIFACT VERIFIED; OWNER CLOSEOUT PENDING**.

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

## PROD execution and live artifact proof

- PROD pushed at **12:10:07 UTC**: `edf85ce503aad961b84b5ea3b2074eb84d416a16`. First parent/rollback `b1389c85759511e65ec5d5b26ee96d63c91984c2`; second parent `9adad7ce750742e9806c373a71f7ce900f3e22b2`; tree `d3db406c198b325fee48790a84205f0695c6d7c2`. The candidate diff was empty and all-files status clean immediately before the authorized push.
- Fresh PROD worktree baseline installation, merged frozen installation, typecheck and build passed under Bun 1.3.9. Pre-push provenance guard, VALGATE D-1 (no-op: no static partner adapters changed) and typecheck passed. The push command carried the same-command Andrew-direct override citing `02e9cb858c` and GO 97048.
- CI exact-head enumeration: **one workflow**, [Deploy to Production 34967303352](https://github.com/Opal-Capital/portal/actions/runs/34967303352), terminal **SUCCESS** at **12:12:00 UTC**. Build/typecheck, artifact upload/download, S3 static/index/JSON deployment, CloudFront invalidation and tag creation all succeeded. See `CI_34967303352.json`.
- Remote annotated tag **`portal-v2.1.178`**: tag object `968e6ab7e058e974cdc92a279cdb7a5ef5d1d63e`, peeled commit **`edf85ce503aad961b84b5ea3b2074eb84d416a16`**.
- At **12:16:00 UTC**, HTTP GET against `https://opalinvest.dev` matched **54/54 files byte-for-byte** to this exact run's downloaded `production-build`: `index.html` and all 53 JavaScript/CSS files in its assets root. Index SHA256 `7b70633fdc00be72f33bf5b43db1fe013aae141665df80617c9c52d2c19477e6`. Full bounded hash manifest: `SERVED_ARTIFACT_PROOF.json`. This proves served bundle identity; it does not assert dynamically fetched data freshness.

## Post-deploy behavior checks and remaining proof

The checked-in `portal/scripts/ui-smoke.mjs` exercised actual production JavaScript in fresh headless Edge at 1440x900, with its documented synthetic session claims and **no data fixtures**. Internal Opal admin reached `/investor-reporting` with its nav item present. A 49financial partner with both role=admin and firmRole=admin was redirected from that route to `/market`, with Investor Reporting absent from navigation. Positioning loaded the new page shell. Screenshots and network logs are private scratch evidence.

**Limit:** the harness's synthetic token is not a real bearer; protected APIs returned 401 as expected. The internal IR scope-error state and Positioning empty holdings under that synthetic token are **not** evidence that authenticated data works or that it is broken. No authenticated full data walkthrough is claimed. MSTR was notified at 12:17:19 UTC to provide the existing validation lane's authenticated served Positioning evidence and the separately owned vintage follow-up, alongside workspace pointer/publication and freeze-release receipts. The GO's dated vintage qualifier remains explicit.

Ledger L1-L3 are closed. L4-L7 remain open pending their specified actual proof. Main portal remains DEV; cleanup and canonical log follow before completion.

## Cleanup and additional gate checks

The same partner-admin synthetic session was redirected from `/investor-reporting/print` to `/market`. An internal Opal non-admin was also redirected from `/investor-reporting` to `/market`, with IR navigation absent. These are frontend identity-gate observations only.

Both owned worktree paths were resolved and verified inside the workspace `.runtmp/` directory and all-files clean before removal. `portal-candidate-20260915T115803Z` removal exited 0. `portal-promote-20260915T115803Z` removal exited 255 with Windows `Filename too long`; canonical `git worktree prune` followed, and neither owned path remains registered. The production skill explicitly permits this ignored physical residue. Peer worktrees were untouched. Main portal is verified **DEV at 9adad7ce**, and execution CWD is the workspace root. No workspace push occurred.
