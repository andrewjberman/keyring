# S19 drain -- verdicts for the 13 NFRA branches (1.0.0_SA_CTO~O, 2026-09-28 ~18:0xZ)

**For:** `0.0.0_AB_MSTR~Z`'s worksheet, `org/tier0_exec/0.0.0_AB_MSTR/deliverables/mstrZ_S19_POSTPURGE_DRAIN_STATE_AND_PROPOSAL_20260928.md`
@f10abae456, section 6.
**Split:** by `1.0.0_SA_CTO~Z` (msg 173242Z). The NFRA `rel-*`, `rb-*` and `wk-NFRA_OPALAI-*` branches are this seat's.
- The worksheet counts 13 NFRA rows; CTO~Z's message says 14.
- 13 are ruled here, and 11 + 13 = 24 closes the worksheet.

**Method.** No merge. Each check was run against the pre-rewrite CLOUD @c31d4ef7fb, which is the local trunk at the
time of measurement:
1. `git merge-base --is-ancestor` of each branch against the newest release tip `rel-nfra-oplgtw-sprint-owner`
   (6a98a0553a). Positive control: email-deny is inside sprint-owner.
2. `git cherry CLOUD <tip>` for patch identity.
3. A three-way blob compare per touched file: merge-base 1764e54a16 against the tip against CLOUD.
4. For the files BOTH sides changed, reverse-apply `git diff MB TIP` against a throwaway index read from CLOUD
   (`GIT_INDEX_FILE`). The shared index was never touched.
5. Every worktree's uncommitted files, read.

## Verdicts

| branch | verdict | basis |
|---|---|---|
| `rel-nfra-oplgtw-sprint-owner` | **SUPERSEDE** | Newest gateway release, live on the host. `git cherry`: 6 of 13 commits patch-equivalent on CLOUD, including its own 6a98a0553a. See the note below for the other 7. |
| `rel-nfra-oplgtw-email-deny` | **SUPERSEDE** | Ancestor of sprint-owner. |
| `rel-nfra-mcpindex-r2-gateway` | **SUPERSEDE** | Ancestor of sprint-owner. |
| `rb-nfra-mcpindex-r2-base` | **SUPERSEDE** | Ancestor of sprint-owner. |
| `rel-nfra-opalai-portal-grant-gateway` | **SUPERSEDE** | Ancestor of sprint-owner. |
| `rb-nfra-opalai-portal-grant-base` | **SUPERSEDE** | Ancestor of sprint-owner. |
| `rel-nfra-opalai-zs18-gateway` | **SUPERSEDE** | Ancestor of sprint-owner. |
| `rb-nfra-opalai-zs18-base` | **SUPERSEDE** | Ancestor of sprint-owner. |
| `rel-nfra-mcportal-r2-gateway-2` | **SUPERSEDE** | Ancestor of sprint-owner. |
| `rel-nfra-opalai-r1-gateway` | **SUPERSEDE** | Ancestor of sprint-owner (no worktree). |
| `rel-nfra-mcportal-r2-gateway` | **SUPERSEDE** | The ABANDONED first cut of MP-d-1, re-cut FRESH as `-gateway-2` (5e24a559f6, inside sprint-owner). Its 2 commits: f1f0fc6780 is inside sprint-owner, and c97839d7c8's files are SAME/CONTAINED on CLOUD against the live release. |
| `wk-NFRA_OPALAI-1` | **HOLD** | See the note on the two HOLD rows below. |
| `wk-NFRA_OPALAI-3` | **HOLD** | See the note on the two HOLD rows below. |

**Why sprint-owner's other 7 commits are superseded.** Across the union of files the 7 touch:
- 31 of 35 files are byte-identical on CLOUD and the release tip;
- config.py and server.py are CONTAINED on CLOUD;
- test_entitlement_admin.py differs in comments only; CLOUD carries INDEX_TOOLS, the by-name pin and `== 51`;
- EC2_MANIFEST.json is AHEAD on CLOUD: CLOUD's gateway `deployed_commit` is 6a98a0553a, the tip's is 2bcade5f5c.
So nothing in the chain is missing from the trunk.

**The two HOLD rows.** Both carry REAL round-1 work that is carried to round 2 behind Andrew's cutover gates
G-ACCT/G-AUTH/G-PUSH. COO~O superseded OA-t-1 and OA-t-3 for the round @4ce47993e4.
- `wk-NFRA_OPALAI-1` (OA-t-1, product files into opal_ai): 6 commits not upstream. Its submodule commit opal_ai
  2e48f7b sits on local branch `wk-NFRA_OPALAI-1-opal_ai`, clean, in `C:/tmp/oa-1`.
- `wk-NFRA_OPALAI-3` (OA-t-3, runtime setup and the launch-gate fence): 3 commits not upstream. Its submodule commit
  opal_ai 803f699 is on `wk-NFRA_OPALAI-3-opal_ai`, clean, in `C:/tmp/oa-3`.
- Both nested submodule commits exist ONLY in these worktrees, so DO NOT remove `C:/tmp/oa-1` or `C:/tmp/oa-3`.
- When landed, cherry-pick the build and move commits only. Drop each branch's final status flip to complete: the
  trunk reads SUPERSEDED-for-round, and the round-2 re-cut owns the status.

## Uncommitted files in the 11 SUPERSEDE worktrees -- read, all disposable

- `infra/aws/ec2/EC2_MANIFEST.json`, in 6 worktrees: 658/658 lines raw, but only 4+/4- with `--ignore-cr-at-eol`. It
  is the release's own deploy stamp. The newest stamp (6a98a0553a) is already on CLOUD; the older ones are superseded.
- `mcportal/`: a clean detached clone of the portal repo at a3bff71 (dirty = 0), the release build input.
- `.scratch/`: commit-message text files.

## After the re-sync

- The 11 SUPERSEDE branches may be deleted once this file is cited as the examined-commits record.
- `C:/tmp/oa-1` and `C:/tmp/oa-3` stay until OA-t-1/OA-t-3 re-cut in round 2 lands their content by cherry-pick.
