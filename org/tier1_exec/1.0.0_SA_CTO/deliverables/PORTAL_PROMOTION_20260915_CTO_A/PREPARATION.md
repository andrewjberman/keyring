# Portal promotion preparation — 2026-09-15

Author/executor seat: `1.0.0_SA_CTO~A`  
Status: **43f18c17 BLOCKED AS-IS BY CTO; AWAITING INTEGRATOR LOCKFILE FIX AND NEW-CANDIDATE PROOFS; PROMOTION NOT STARTED**

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

## MSTR integration update — notice 96987, 08:27:11 UTC

Exact notice `20260915T082711Z_0.0.0_AB_MSTR_Promote_prep__portal_integration_plan__l.md` was read and ACKed. MSTR explicitly states **nothing is merged into DEV yet and there is no GO**. The following branch publication observations are MSTR's reported `ls-remote` readbacks, not a new remote measurement by this seat:

- `laptop/dev-local` at `90d71d9e`, to move again when FE-s-49 drains; `laptop/d13-visual-elevation` at `46932888`.
- Site Z's optional `sitez/amgt-resapp-ri1` at `9aef37344c`; CTO~W recommends hold and inclusion requires Andrew's word.
- `sitez/posn-asttax-r6` will be published at the round-6 close head. Reported origin DEV remains `5b959f63ca`, PROD `b1389c8575`.

MSTR and MSTR~Z agree the integration sequence before either side merges: a fresh worktree from the final laptop DEV branch after FE-s-49 drains; merge the rebrand (reported disjoint `scripts/ui-smoke.mjs` conflict), then POSN, then AMGT only if separately approved. Typecheck and the whole suite run on the merged result. MSTR publishes that result as origin DEV, reads the IR gate there, and binds Site Z's POSN verdict to that leg before issuing GO.

MSTR reports 254 untracked evidence files in main DEV with zero tracked changes and will preserve them. He proposes using the fresh integration worktree, or main DEV tracked-only, for the Step 1 check; **he explicitly assigns confirmation of that interpretation to CTO**. This seat routed that confirmation to CTO at 08:28:05 UTC, recommending a clean integration worktree pinned to the exact published candidate plus a separate main-DEV tracked-state check. Until the owner confirms it, this remains a pending interpretation, not a silently relaxed gate. No evidence file is to be deleted or moved to satisfy it.

MSTR owns publication of the peer-owned DEV commits and the workspace CLOUD/gitlink leg. This supersedes any implication in the planned L5 leg above that this seat must itself move or commit the workspace pointer: bind the actual pointer action to MSTR's final integration plan and receipt. CTO~A's future authorized operation is the portal PROD promotion. All candidate pins and prerequisite proofs are re-read at the eventual explicit GO; neither this update nor the deadline starts deployment.

## CTO cleanliness ruling — notice 96988, 08:30:40 UTC

Exact notice `20260915T083040Z_1.0.0_SA_CTO_Re_96987_Step_1__RULED_--_check_the_fres.md` was read and ACKed. CTO confirms the governing purpose: no uncommitted or untracked byte reaches the promoted build. The check applies to the tree whose bytes are promoted.

1. The fresh integration worktree's printed HEAD must equal the exact candidate published to origin DEV, and `git status --porcelain --untracked-files=all` must print nothing: zero tracked changes and zero untracked files.
2. Main portal DEV must have zero tracked changes. Its untracked evidence remains untouched, outside the promoted build's byte path.
3. The ephemeral promotion worktree must also pass the all-files cleanliness check immediately before the build. Any dirty or mismatched release tree is a STOP.

CTO also wrote that the Step 4 promotion worktree's HEAD must equal the Step 1 DEV candidate. **One literal conflict was returned to CTO at 08:31:41 UTC:** the skill requires a `--no-ff` DEV-into-PROD merge, so the resulting merge commit cannot have the same commit hash as its DEV parent even when their file trees are identical. The proposed precise resolution is a clean promotion worktree whose HEAD equals the recorded PROD merge SHA, with its Git tree equal to the published DEV candidate's tree and an empty candidate-to-HEAD diff. That proposal remains pending the owner's explicit correction; it is not a silent substitute for the ruling. No merge or build has been started to work around the conflict.

MSTR's explicit GO and both merged-tree prerequisite PASS artifacts still bind. The ruling is preparation authority, not promotion GO.

## Investor Reporting candidate requirement — notice 96996, 08:58:43 UTC

Exact notice `20260915T085843Z_1.0.0_SA_CTO_Promote_Step_1_addition__the_candidate_m.md`, from CTO, was read and ACKed. It adds a mandatory two-part Step 1 test. The required Investor Reporting admin-gate commit is **`10c2f07d4da3795c0e404a92a8b9515259e42be7`** (FE-s-49 amendment 1). The earlier `90d71d9e1199d7bf5f666e68c8c58400333e6267` does not contain it and is not eligible by itself.

At the eventual GO, print and retain both checks against the **actual published, merged candidate**:

1. `git merge-base --is-ancestor 10c2f07d4da3795c0e404a92a8b9515259e42be7 <candidate>` must return 0. A bogus candidate hash must fail as the negative control. A nonzero exit for the real candidate, including an unreadable object, is a STOP.
2. Read `git show <candidate>:src/App.tsx` and `git show <candidate>:src/lib/firmAccess.ts`. In the candidate's own bytes, both `/investor-reporting` and `/investor-reporting/print` must carry `requireAdmin requireInternal`; the navigation item must carry `requiresAdmin: true` and `requiresTier: 'internal'`; the `49financial`, `inflection` and `cottonwood` allowlists must each omit `/investor-reporting`. Any failed or unreadable content check is a STOP even when ancestry passes, because a later merge can remove the guard.

The notice abbreviates the second source path as `lib/firmAccess.ts`. That literal root path was read at the cited commit and failed because it does not exist. A scoped filename search and `git ls-tree` resolve the canonical path unambiguously to **`src/lib/firmAccess.ts`**, which was then read from the same exact commit. This is an explicit source-path correction, not a substituted inbox notice or a concealed failed read.

Read-only preparation evidence, measured 2026-09-15T09:00:21Z and completed with the corrected path shortly afterward:

| Test | Result | Limit |
|---|---|---|
| Required commit ancestor of itself | exit 0 | Positive plumbing control, not a final candidate check |
| Required commit ancestor of old `90d71d9e...` | exit 1 | Old published DEV snapshot fails the new gate |
| Required commit ancestor of all-zero bogus commit | exit 128, invalid commit | Expected negative control; an invalid real candidate would also stop |
| `10c2f07d...:src/App.tsx` | Both route guards and the admin/internal navigation restriction present | Committed source inspection only |
| `10c2f07d...:src/lib/firmAccess.ts` | All three named partner sets omit the page | Committed source inspection only; no authenticated walkthrough claimed |

No final integrated candidate has been selected or graded by these preparation controls. Repeat the checks at GO, retain both prerequisite PASS artifacts, and apply the prior cleanliness and exact-byte requirements. The Step 4 no-ff merge commit/hash wording remains pending the explicit owner clarification already requested. No fetch, build, merge, push or deployment was performed for this notice.

## Published candidate precheck — notice 97008, 09:32:50 UTC

Exact notice `20260915T093250Z_0.0.0_AB_MSTR_Promote_candidate_43f18c17__laptop_integ.md`, from `0.0.0_AB_MSTR`, was read and ACKed at 09:33:37 UTC. It expressly says **no GO** and offers this head for the 96996 precheck: **`43f18c179cad01947e0f0a41a9889807301fd233`**, published as `laptop/integ-promote-20260915`. MSTR reports it combines gated DEV `10c2f07d`, d13 `46932888` and POSN round 6 `ebbee2e61a`; AMGT is excluded because its separate approval has not been given.

This seat independently measured the following against that exact commit at approximately **09:34–09:35 UTC**, using the existing portal Git object store and a read-only `ls-remote`. No checkout, fetch, install, build, merge or branch mutation was needed.

| Check | Measured result |
|---|---|
| `merge-base --is-ancestor 10c2f07d4da3795c0e404a92a8b9515259e42be7 43f18c179cad01947e0f0a41a9889807301fd233` | exit **0** |
| Same ancestry check with an all-zero candidate | exit **128**, invalid commit: expected negative control |
| Candidate `src/App.tsx` route entries | **2/2** named routes, `/investor-reporting` and `/investor-reporting/print`, have `ProtectedRoute requireAdmin requireInternal` |
| Candidate IR navigation item | **1/1** item has `requiresAdmin: true` and `requiresTier: 'internal'` |
| Candidate `src/lib/firmAccess.ts` partner allowlists | **3/3** named sets (`49financial`, `inflection`, `cottonwood`) omit `/investor-reporting` |
| Candidate tree | `f1afba420366a4f8645bbb6262db61ca4af9dab4` |
| Site Z trial `1a1e13ef1d7197c88499d010ebd4539a79270a0b` tree | Same tree `f1afba420366a4f8645bbb6262db61ca4af9dab4`; candidate-to-trial `git diff --exit-code` is empty, exit **0** |
| Live remote `refs/heads/laptop/integ-promote-20260915` | `43f18c179cad01947e0f0a41a9889807301fd233` |
| Live remote `refs/heads/DEV` | `5b959f63ca5e51214fe1e605b04b82b2bbf60ef4` |
| Live remote `refs/heads/PROD` | `b1389c85759511e65ec5d5b26ee96d63c91984c2` |

Source inspection used `git show <candidate>:<path>`, not main DEV working files. The inspected blob IDs are `cb20bd3d2fe93988c4a759bf37add3b994bc4e6d` for `src/App.tsx` and `73cf302f0a48a876f548c943367ba326dc2ba804` for `src/lib/firmAccess.ts`. These results establish the requested source guards and ancestry on the named published branch. They do not establish authenticated runtime behavior, clean build worktrees, successful whole-suite execution, or admission of this candidate to origin DEV.

### Suite issues reported at the 09:35 precheck; corrected and ruled below

The notice reports **585 pass / 21 skip / 2 fail of 608** on intermediate tree `57c70a8e`, versus **586 / 21 / 1** on unmerged DEV `10c2f07d` at the same workspace-relative test location. Its final-candidate whole-suite run was still in progress. This seat has not rerun that suite or independently diagnosed those failures.

- **F25-AC8**, `fe-s-25 generator.test.ts:79`: the initial contract-drift/vintage diagnosis was **wrong**, corrected by MSTR 97014. The observed hashes differ because of CRLF versus LF raw checkout bytes; this is a test-instrument issue, not a contract-shape change. The independent reproduction and CTO disposition are below.
- **F49-AC8**, `fe-s-49 admin-gate.test.ts:582`: MSTR reports a merge-attributable pre-merge assertion that forbids two unrelated d13 hunks, which become expected after merging d13. The guard assertions reportedly still pass. CTO 97019 accepts this named failure for the exact candidate and assigns its later fix to COO~F.

The passing source precheck itself did not waive either failure. CTO's later explicit acceptance in 97019 governs the exact candidate; it does not turn the suite into a zero-failure run. Any amended candidate requires checks against its exact new SHA. This seat does not edit COO~F's tests or generated wire file.

### Next release inputs

MSTR targets GO around **11:30–12:00 UTC**, after Site Z's planned **11:1xZ 25-of-25 data recheck**. That is reported scheduling, not time-based authority. Final candidate/DEV publication, final suite evidence carrying the accepted failures, applicable prerequisite PASS records, clean integration/promotion trees, the Step 4 no-ff merge/hash clarification, freeze, and explicit MSTR GO remain release inputs. CTO 97019 resolves the test disposition and leaves the Step 4 clarification with **MSTR's GO**; the updates below supersede the earlier pending-CTO wording.

No deployment ledger or sentinel is opened for this precheck. The workspace gitlink and publication remain MSTR-owned. The result is routed to MSTR and CTO, then only the exact notice 97008 is archived.

## Corrected diagnosis, render evidence and CI read — notices 97014 and 97017

Read only the exact notices `20260915T093926Z_0.0.0_AB_MSTR_Correction__F25-AC8_is_a_line-ending_art.md` and `20260915T093956Z_0.0.0_AB_MSTR_CI_read_on_candidate_43f18c17__no_workfl.md`, both from MSTR. ACKs were sent at 09:40:05 and 09:40:52 UTC respectively.

**F25 correction:** MSTR explicitly withdraws both the cross-repository contract-drift diagnosis and the claim that COO~F's earlier green runs used an older workspace vintage. COO~F measured identical normalized schema content, with raw checkout line endings producing the two hashes. This seat independently reproduced that relationship at 09:41–09:43 UTC from `docs/contracts/investor-reporting/v1/StatusEnvelope.schema.json@58e387b4542cb8ce7c7c6a5bb4ebcb30980464c6`:

| Representation of the same schema | SHA-256 |
|---|---|
| Committed schema normalized to LF; also the current main workspace raw file | `f06c0029cd20ceb1cc08500f456cf3122a63dc9562f9df284b360f252895008a` |
| Same bytes with LF replaced by CRLF | `c83ce02d14c12044b7d627181ae8ef3fd07f96fe5c6ac7e2cfb0366d7deed380` |

The main file and pinned schema are identical after LF normalization. The exact portal candidate's `src/pages/InvestorReporting/contracts/wire/StatusEnvelope.ts` header contains the CRLF hash above; its `src/pages/InvestorReporting/__tests__/fe-s-13/gen-wire.ts` `sha256Of` function hashes its text argument directly. The abbreviated root path `contracts/wire/StatusEnvelope.ts` initially failed to resolve; the scoped filename result supplied the full path above, which was read at the same candidate. No checkout line endings, schema, generated wire file or generator were modified. This reproduction supports the corrected hash diagnosis; it is not a newly executed bun-suite result.

**Site Z render:** MSTR 97014 relays `0.0.0_AB_MSTR~Z` bus `04b0586c` at 09:36 UTC: final render **PASS** on exact candidate `43f18c17`, zero tracked changes, served against six keys pinned by VersionId. Reported Satellite 15 and Satellite 80, selected by exact name, both views: **272/272 cells each, zero mismatches**; zero values with 3+ decimals, zero markers, and zero `font-mono` under Positioning. This is attributed relayed evidence, not a browser walkthrough independently executed by this seat. The notice does not provide the six VersionIds or replace the scheduled later data recheck.

**CI:** MSTR 97017 reports all three candidate workflow files run on `ubuntu-latest`, with none invoking `bun test`: DEV `ci.yml` runs the provenance guard, bare `tsc --noEmit`, and build; PROD `deploy.yml` runs the correct `bun run typecheck` and build; manually triggered `promote-to-prod.yml` runs bare `tsc --noEmit` and build. The branch trigger in the last file is commented out. This seat subsequently read the two files assigned for its later fix and independently read candidate `package.json`: `typecheck` is **`tsc -b --noEmit`**, and `test:provenance-guard` is **`node scripts/provenance-read-guard.mjs`**. It does not invoke the bun suite. This is workflow/source evidence, not successful CI execution. CTO's acceptance below relies on the stated flip condition being false.

## CTO test disposition and deferred work — notice 97019, 09:41:12 UTC

Exact notice `20260915T094112Z_1.0.0_SA_CTO_RULING__43f18c17_PROCEEDS_with_F25-AC8__.md` from CTO was read and ACKed at 09:42:15 UTC. Its original ruling was to proceed with exact candidate `43f18c179cad01947e0f0a41a9889807301fd233`, name F25-AC8 and F49-AC8, and not fix those tests first. **CTO 97030 below supersedes permission to promote that candidate as-is because of the separate stale-lockfile defect. The F25/F49 exceptions still stand.** No test count is rewritten as green, and no unlisted failure is accepted by implication.

CTO says the raw hash difference is not caused by its `58e387b454` pin correction, which changed provenance metadata rather than shape. It accepts F49's pre-merge invariant failure on the correctly merged d13 tree. MSTR's workflow census and CTO's independent package-script read establish that neither named bun-test failure enters the promotion gate. The **Step 4 no-ff merge SHA versus DEV SHA clarification remains with MSTR's GO**. This ruling is not that GO. The planning window remains ~11:30–12:00 UTC, deadline 13:00 UTC.

Deferred ownership is explicit:

- **COO~F:** one IRPT_FNTEND order after promotion for generator LF normalization plus header regeneration, and an F49 carried-hunks arm keyed to whether `c29a8b86` is an ancestor of HEAD. It may build behind the freeze; DEV publication waits for freeze release.
- **This seat, CTO~A:** two-line portal workflow fix after promotion: change the typecheck command in `.github/workflows/ci.yml` and `.github/workflows/promote-to-prod.yml` to `bun run typecheck`. `deploy.yml` already uses the correct command and is outside this fix.

The exact proposed change is prepared as **`POST_PROMOTE_TYPECHECK.patch`**, based on candidate `43f18c17`, SHA-256 **`2caf55e1756d56472a99d2eea57816a5f0b37e0e8a21eefada39d4fc95fe88d9`**. It changes exactly one command in each named workflow. `git apply --check` passed against isolated copies of those two candidate files in private scratch. This is an unapplied preparation artifact: no portal source, index, branch or candidate was changed. Reconcile against the actual post-promote DEV head, perform the applicable validation, and land/publish only after promotion and freeze release. The deferred patch is not part of this release.

This corrected record and proposed patch are routed to CTO/MSTR, then only notices 97014, 97017 and 97019 are archived. Promotion remains unstarted; no ledger/sentinel, freeze, merge, push or workflow dispatch is created by these notices.

## DEV publication and Step 4 clarification — notice 97024, 09:47:44 UTC

Exact notice `20260915T094744Z_0.0.0_AB_MSTR_Portal_origin_DEV_fast-forwarded_to_the_.md`, from MSTR, was read and ACKed at 09:48:34 UTC. MSTR reports the authorized DEV fast-forward and expressly states **GO is still pending**. The freeze prohibits other portal DEV pushes and main-DEV merges until promotion lands. Worker branches needing current DEV start from `43f18c17`; the deferred changes remain outside this release.

Independent readback at **09:48:56 UTC**:

| Surface | Measured value |
|---|---|
| Live `refs/heads/DEV` | `43f18c179cad01947e0f0a41a9889807301fd233` |
| Live candidate branch `refs/heads/laptop/integ-promote-20260915` | Same `43f18c179cad01947e0f0a41a9889807301fd233` |
| Live `refs/heads/PROD` | `b1389c85759511e65ec5d5b26ee96d63c91984c2` |
| Main portal branch / HEAD | `DEV` / `43f18c179cad01947e0f0a41a9889807301fd233` |
| Main portal HEAD tree | `f1afba420366a4f8645bbb6262db61ca4af9dab4` |
| Main portal tracked-state check | `git status --porcelain --untracked-files=no` empty |

These reads confirm candidate publication and main tracked cleanliness. They do not measure the future promotion worktree's all-files cleanliness, and no untracked evidence was removed or moved.

**Step 4 is clarified by MSTR:** the no-ff PROD merge commit will differ from DEV's commit hash. Its file tree must equal the candidate tree; MSTR also offers the recorded second-parent condition. This executor uses the **tree-equality condition**, records the actual PROD merge SHA and its parents, and retains the skill-required empty candidate-to-merge diff plus clean worktree check. Second-parent ancestry alone does not replace file-tree parity. This resolves the literal HEAD-equality ambiguity without changing the required merge procedure. Bind the clarification and candidate pin to the eventual GO message, which MSTR says will state it again.

The remaining planned data input is Site Z's **25-of-25 recheck after the ~11:05 UTC models publish**, targeting ~11:30 UTC. Publication is not deployment authority; no GO was issued by 97024.

## Exact-candidate DEV CI failure — independently measured after publication

`gh -R Opal-Capital/portal run list --commit 43f18c179cad01947e0f0a41a9889807301fd233 --limit 100` returned **one run**: [CI - Build & Validate, 34954379962](https://github.com/Opal-Capital/portal/actions/runs/34954379962), push-created **09:46:39 UTC**, status **completed**, conclusion **failure**. The exact head SHA matches the candidate. Subsequent job and failed-step reads identify:

- Job **104332756669**, **Lint, Type Check & Build**, failed step **6, Install dependencies**, at 09:46:59 UTC.
- Command: `bun install --frozen-lockfile`; CI's `BUN_VERSION: latest` resolved to **Bun 1.4.2 (`744846f84`)**.
- Error: **`lockfile had changes, but lockfile is frozen`**, process exit **1**.
- ESLint, provenance guard, typecheck, build and artifact upload were all **skipped**. The separate Build Summary job succeeded, which does not make the workflow successful.

This is a distinct install failure, not either accepted F25-AC8 or F49-AC8 bun-suite failure. It is not accepted by implication from CTO 97019. MSTR and CTO received the initial red result at **09:49:24/26 UTC** and the exact failed-step diagnosis at **09:50:10/12 UTC**.

Candidate `deploy.yml` independently read at the same SHA pins **Bun 1.3.9** and also uses `bun install --frozen-lockfile`. The earlier version-causality question is now resolved by **CTO 97030**: the same stale pair fails the frozen-lockfile check on pinned Bun 1.3.9. **43f18c17 must not promote as-is.** MSTR must provide the one-commit lockfile repair and the new-candidate proofs below. This replaces the former pending-disposition statement; it does not claim the repair already exists or has passed. No lockfile regeneration, dependency installation, workflow rerun, candidate alteration or CI fix was performed by this seat. The two-line post-promote patch remains unchanged and unapplied.

The preparation record is committed and routed before archiving only exact notice 97024. Promotion has not started; no deployment ledger, sentinel, PROD merge/push, or workflow dispatch was created by this seat.

## Blocking amendment and replacement-candidate requirements — CTO 97030, 10:06:12 UTC

Read only exact notice `20260915T100612Z_1.0.0_SA_CTO_AMENDS_97018__43f18c17_must_NOT_promote_.md` from `1.0.0_SA_CTO`; ACK sent at **10:07:08 UTC**. It amends the earlier PROCEED ruling: **do not promote `43f18c179cad01947e0f0a41a9889807301fd233` as-is**. The separate F25-AC8/F49-AC8 test disposition remains in effect.

CTO's reported diagnosis is a stale manifest/lock pair. d13 commit `19be39c1` removed seven dependencies from `package.json` without regenerating `bun.lock`: `@nivo/core`, `@nivo/radar`, `@visx/scale`, `apexcharts`, `framer-motion`, `phosphor-react`, and `react-apexcharts`. The old lock's root workspace block still contains them; CTO reports no lockfile change between gated DEV `10c2f07d` and `43f18c17`.

CTO independently tested a scratch copy of the exact candidate's `package.json` and `bun.lock` with **Bun 1.3.9**, matching PROD's pinned version:

- Original pair: `bun install --frozen-lockfile --lockfile-only` **exit 1**, frozen-lockfile mismatch.
- Regeneration: `bun install --lockfile-only` **exit 0**, reported 450 packages; diff **103 removed / 4 added lines**.
- Regenerated pair: frozen-lockfile-only check **exit 0**.

These are CTO's attributed scratch measurements, not a full clean installation/build run by this seat. They establish why the original candidate is blocked before any PROD push. The only four added resolutions are reported hoists of existing identical version/sha512 entries: `@types/d3-array@3.2.2`, `@types/d3-interpolate@3.0.4`, `d3-format@3.1.0`, and `d3-time-format@4.1.0`. No remaining package resolution is to change.

**Integrator action:** MSTR commits the regenerated **`bun.lock` only**, as one commit on top of `43f18c17`. CTO explicitly allows this candidate repair through the existing DEV freeze. That allowance belongs to the integrator's repair; it does not release unrelated DEV pushes or authorize this seat to edit the candidate. CTO reports no committed fix and no portal mutation by its own seat in the notice. No new candidate SHA has been supplied here.

**Required proof before GO on the replacement candidate:**

1. Diff from `43f18c17` names **`bun.lock` only**; inspect the actual diff for deletions and exactly the four stated hoists, retaining their previous versions and integrity hashes.
2. On a clean checkout, **Bun 1.3.9** runs full `bun install --frozen-lockfile`, then `bun run typecheck`, then `bun run build`: **all exit 0**. A lockfile-only check does not substitute for these full checks.
3. The replacement SHA's DEV CI run **passes Install**. CTO expressly anticipates the already-existing lint failure described below; capture the actual run and steps rather than relabeling it green or assuming any red result is accepted.
4. Site Z's planned **25-of-25 data recheck after the ~11:05 UTC models publish runs on the new SHA**, not the blocked candidate.
5. Rebind this seat's required gate-commit ancestry, exact IR source checks, publication/cleanliness checks and eventual MSTR GO to that new candidate. The final promotion tree must equal the **new candidate's tree**, with an empty diff; old tree `f1afba42` is historical and cannot be used as the replacement release's parity target.

**Named DEV lint disposition:** CTO identifies `src/pages/InvestorReporting/__tests__/fe-s-5/alias-probe.test.ts:16:20`, ESLint `no-constant-binary-expression` on `cn('a', false && 'b', 'c')`, as present since DEV `5b959f63` (reported run `34562328385` on 09-11) and still present on `43f18c17`. CTO accepts that specific existing DEV-only lint failure for this promotion because PROD `deploy.yml` runs install/typecheck/build, not lint. Its fix belongs to the IRPT_FNTEND round-8 work alongside F25/F49. This is attributed history/disposition, not an independent reread of the earlier run. Additional failures are not accepted by implication, and required PROD workflow success remains mandatory.

MSTR's GO window remains ~11:30–12:00 UTC with the 13:00 UTC deadline. This amendment supplies a blocking decision and a repair/proof path, not deployment GO. The amended preparation is committed and routed to CTO/MSTR before archiving exact notice 97030. No deployment ledger, sentinel, dependency installation, source edit, merge, push or workflow dispatch is started by this seat.
