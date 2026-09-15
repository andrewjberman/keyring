# Portal promotion preparation — 2026-09-15

Author/executor seat: `1.0.0_SA_CTO~A`  
Status: **PREPARATION COMPLETE; PROMOTION NOT STARTED; AWAITING MSTR GO**  
Prepared: 2026-09-15 08:14 UTC

## Assignment and authority boundary

Exact inbox notice: `20260915T080619Z_1.0.0_SA_CTO_Heads-up__you_execute_the_portal__prod-d.md`, Msg-ID 96978, from `1.0.0_SA_CTO`. Read and ACKed at 08:07:06 UTC. The body expressly says heads-up, NOT YET GO: prepare now, do not start.

Andrew's recorded instruction is **“Make sure portal is promoted by 9a eastern time”**: 13:00 UTC on 2026-09-15. The ruling is `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20260915_080xZ_PORTAL_PROMOTED_BY_9AM_EASTERN.md`. At the preparation read this was a staged, not yet committed file; its SHA-256 was `499b29653678b7a0cde6362f8c98927269f21c42706da812619f16da5f0ba49c`. Its future commit must be recorded in the execution ledger. This working-file digest is provenance for preparation, not a release approval or immutable commit pin.

CTO names this exact seat as the Andrew-directed non-DT executor. Start only on explicit `0.0.0_AB_MSTR` GO after both prerequisites PASS on the merged tree:

1. Site Z's real POSN_ASTTAX ad-hoc pull presents properly.
2. Investor Reporting's Opal-admin gate is on DEV, IRPT_FNTEND FE-s-49, owned by `2.0.0_SA_COO~F`.

CLOUD→SITEZ `/integrate` comes first, anticipated 11:00–12:00 UTC; promotion is anticipated 12:00–12:30 UTC. These are planning windows, not time-triggered authority. The deadline waives neither prerequisite. If either remains red near the deadline, MSTR owns the call to Andrew.

## Repository procedure reviewed

Read `.claude/skills/prod-deploy/SKILL.md` end to end, the Andrew-direct ruling, `.tools/deploy_ledger.py` usage, Gate 5 in the repository pre-tool hook, and the historical `org/critical_paths/change_management/20260901T0645Z_d12-portal-dev-to-prod-promote-v2.1.174_deploy.md` execution record. The historical record supplies a procedure example, not today's authority. Also inspected the current portal `.github/workflows/deploy.yml`.

The main portal checkout stays on DEV. Promotion uses an ephemeral worktree under the carried workspace root. The Codex startup/inbox branch continues to govern; no Claude consuming inbox helper is used. Retired `comp-surface-check` is not a gate and is not replaced by an invented check.

At GO, the audited `# never-override: Andrew-direct <date> <words>` must accompany the same portal push command, using the actual recorded authority. This exception is limited to the authorized portal operation. Workspace CLOUD push and CLOUD→SITEZ integration remain MSTR-owned. This seat can prepare and pathspec-commit the portal gitlink, then route its publication to MSTR; it must not extend the portal exception to workspace push/pull.

No freeze, deployment ledger/sentinel, DEV/PROD push, branch change, PROD ref update, promotion worktree, merge, gitlink update, or workflow dispatch has been started for this assignment.

## Measured preparation baseline

Read-only measurements at approximately 08:10–08:14 UTC; no fetch was performed. The remote-tracking refs below can be stale and are **not** the future release candidate or rollback selection.

| Item | Observation |
|---|---|
| Runtime identity | `OPAL_AGENT_SERIAL=1.0.0_SA_CTO~A` |
| Workspace root | `C:/Users/AndrewBerman/Desktop/ajb_workspace` |
| Main portal branch | DEV |
| Portal HEAD | `90d71d9e1199d7bf5f666e68c8c58400333e6267` |
| Recorded origin/DEV | `5b959f63ca5e51214fe1e605b04b82b2bbf60ef4` |
| Recorded origin/PROD | `b1389c85759511e65ec5d5b26ee96d63c91984c2` |
| DEV divergence from recorded origin/DEV | 113 ahead, 0 behind; peer-owned commits present |
| Tracked portal changes | None in `git status --porcelain --untracked-files=no` |
| Untracked portal entries | Present; clean-worktree gate not currently satisfied |
| Git | `C:\Program Files\Git\bin\git.exe` |
| Bun | `C:\Users\AndrewBerman\.bun\bin\bun.exe`, 1.3.9 |
| GitHub CLI | `C:\Program Files\GitHub CLI\gh.exe`, 2.87.0 |

MSTR must reconcile/publish peer-owned DEV work in the integration phase. This seat will not push those passenger commits, reset or rebase them, or remove untracked files to manufacture a clean checkout. Re-measure at GO and resolve the clean-worktree gate with the owning integrator before promotion.

The deployment workflow builds and typechecks with Bun 1.3.9, deploys through S3/CloudFront, and creates an annotated `portal-v*` tag after deployment. Local tool presence does not establish GitHub authentication, successful CI, current AWS authorization, or live application correctness. Those execution checks remain outstanding. Running typecheck on this preliminary tree would not prove the later merged candidate; candidate typecheck is required at GO.

## Execution sequence at GO

1. Read the exact MSTR GO. Record its immutable provenance, the final integration/DEV pin, both prerequisite PASS artifacts and their applicability to that merged tree, and the active DEV-push freeze. Use the canonical exact-seat Codex inbox path for new messages. If any prerequisite or the clean-worktree gate is unresolved, return that concrete issue to MSTR before mutation.
2. Open the canonical change-management ledger with its complete leg manifest at deployment START, before the first deployment mutation. Proposed unopened slug: `portal-prod-promote-20260915-0900et`. Record executor, MSTR-owned legs, rollback base, approval references, and evidence locations. The proposed slug is not an existing deployment record.
3. Carry the workspace root forward. Recheck main DEV and cleanliness; fetch current portal refs as prescribed. Do not push peer-owned ahead commits. Any needed publication or integrator-only pull is MSTR's leg. Resolve Bun and run `bun run typecheck` against the admitted DEV candidate; zero errors required. Do not install dependencies in the main checkout.
4. Reassert local PROD from current origin/PROD as prescribed, capture that exact SHA as rollback base, create the timestamped promotion worktree under `.runtmp`, and perform any required Bun install there in the foreground. Main portal remains on DEV. Do not set `MSYS_NO_PATHCONV=1` for portal Git operations.
5. Merge current `origin/DEV` with `--no-ff` in the promotion worktree. Record DEV pin, PROD base, rollback base, and author in the merge message. Require an empty `git diff origin/DEV HEAD` and the skill's applicable gates before the authorized PROD push. Do not run the retired surface checker. Attach the exact audited Andrew-direct override to the portal push command.
6. Use explicit `gh -R Opal-Capital/portal` on every GitHub query. Enumerate all workflows for the exact pushed head SHA and explicitly inspect each run's `status` and `conclusion`; all required runs must finish successfully. A silent watch is not success. An empty filtered list requires the repository/unfiltered positive control. Fetch the resulting annotated tag and compare its peeled `^{commit}` to the deployed SHA.
7. Verify the served application artifact and the actual affected ASTTAX and Investor Reporting behavior. Record the live evidence; neither a tag nor a proxy availability check substitutes for the exercised application behavior. Record the workspace portal gitlink with an exact-path local commit, and route the CLOUD publication/integration leg to MSTR.
8. Remove only the verified exact promotion worktree path within this workspace, prune its Git registration as prescribed, and verify the main portal remains DEV with the execution cwd returned to the workspace. Report a Windows long-path cleanup residual if encountered; do not force broad filesystem cleanup. Close ledger legs only against their evidence, then close the ledger only when every leg is evidenced. Send the prescribed closeout to COO/MSTR, release the freeze through its owner, and write the canonical session log.

## Planned complete change-management legs

The actual ledger must bind these to the final approved pins and evidence at start. If the admitted plan changes, update its manifest before taking the new action.

| Leg | Owner | Required completion proof |
|---|---|---|
| L1 — Admission and DEV candidate | MSTR for integration/publication; CTO~A for execution preflight | MSTR GO, both merged-tree prerequisite PASS artifacts, DEV freeze, clean checkout, published candidate SHA, zero-error typecheck |
| L2 — PROD merge and push | CTO~A under recorded Andrew-direct exception | Current PROD rollback SHA, candidate/merge SHA, empty DEV parity diff, passed push gates, exact remote PROD receipt |
| L3 — Deployment and tag | Portal CI; CTO~A verifies | Every exact-SHA workflow terminal success, deploy result, annotated tag peeled to that SHA |
| L4 — Served behavior | CTO~A, with prerequisite owners supplying application evidence where needed | Actual production artifact and affected ASTTAX/Investor Reporting walkthrough results |
| L5 — Workspace portal pointer | CTO~A local commit; MSTR publishes/integrates | Exact gitlink commit plus MSTR's publication/integration receipt; a local commit alone does not close publication |
| L6 — Cleanup and closeout | CTO~A; freeze owner for release | Main DEV confirmed, worktree cleanup result, canonical log, COO/MSTR closeout and freeze-release receipt |

## Stop and recovery boundaries

Red typecheck, VALGATE, unresolved merge conflict, failing CI, missing authority, or unproven prerequisites prevent completion. Before PROD push, leave the remote release unchanged and report the concrete failure. After a push, a failing deployment or live verification is immediately surfaced to COO and CTO/MSTR with the captured rollback SHA and evidence. The rollback SHA is a prepared recovery input; this assignment does not grant unilateral revert or repush authority.

The approved MDPF Cottonwood cents hotfix remains a separate open deployment. This seat still owns its scheduled 13:30 UTC Gold and 13:50 UTC publisher evidence check. No manual invocation is authorized by this promotion preparation.
