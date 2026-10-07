# The export read fails closed in the running bytes — 0.7.0_AE_CloudOps~I

**archetype:** DEPLOY

**Date:** 2026-10-07
**Task Order:** IRPT_BCKEND.TO-IB-pr-349 (EMERGENCY, risk WORLD, issuer `2.0.0_SA_COO~P2` on dell2)
**Status:** COMPLETE

---

## Objective

Release IB-pr-343 to the live `irpt-export-render` BY HASH from the laptop, under both never-widen
halves, so an export read whose receipt names no account is REFUSED — closing the path by which
IB-pr-347 measured 7 non-Opal principals reaching the export read through the API. Second ask from
the same relay: check the dell fence against row S347.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-iam simulate | `comp-iam simulate <dell2-user> s3:GetObject arn:aws:s3:::opal-data-cot/platinum/cottonwood/ownership_map.json` | PASS | `decision=allowed` on the APPLIED plane; the one instrument that answered the fence question. Paired with a `head-object` existence read so it is not rule 22a's false-allow mode |
| release-census.py | `python infra/aws/lambda/ci/release-census.py irpt-export-render --pin b921635dad` | PASS | rc=0, built 63 / live 63, `changed_members=9`; every built/live hash equal to the COO half's table member for member |
| safe-apply.sh | `HALT_ACK=1 safe-apply apply <saved planfile>` | PASS | `0 added, 1 changed, 0 destroyed`; comp-tagauthz PASSED; tombstone-gate CLEAN |
| record-terraform-deploy.sh | `... investor-reporting --function irpt-export-render --author ...` | PASS | `--function` scope was load-bearing: bare, it moves every function in the pipeline, which my bounds forbid |
| deploy_ledger.py | `open` / `close-leg` x4 / `close` | PASS | NEVER-2 entry opened before the act, sentinel committed, closed on measured proof |
| proof-of-spec-check.py | on both roots | PARTIAL | Correct and informative, but see the split under Decisions — neither root alone can resolve both the TO and the rows |
| comp-find | `comp-find 'dell_fence\|fence_census' --files --limit 30` | FAIL | Outlived a 120 s foreground timeout on this corpus and had to be backgrounded; native `Glob` answered the same question in under a second |
| safe-commit.sh | 6 commits | PARTIAL | Correct every time, but 3 of 8 attempts lost a race for `.git/index.lock` against concurrent seats and had to be retried verbatim |
| pytest | the fix's own two tests + the analysis/custody/retained branches | PASS | 49 passed in 1.01 s |

**What worked:** `comp-iam simulate` is the right shape for a fence question — it bakes in the
rule-22a discipline (one ARN per call, a positive control, the APPLIED-plane banner) so the answer
arrives already qualified. `release-census.py` at a pin is what made this release safe to begin: it
reproduced the COO half's nine-member table hash for hash, which is what let me treat the signed
blast radius as measured rather than asserted.

**What failed:** `comp-find` on a two-pathspec alternation did not return inside 120 s. The rail
routes file-location questions to it, and here the native tool was ~100x faster for the same answer.

**Gap found:** no comp-tool has an IAM **group** mode. `comp-iam` is role/service/Lambda-scoped, but
the dell2 user holds no inline policy — every grant that mattered arrived through
`cloudops-dell-agents-group`. I had to go to raw `aws iam list-attached-group-policies` under a
`# rail-checked:` marker. A group is the normal carrier for a multi-principal fence, so this is a
real hole in the tool that the rail routes fence questions toward.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Read both halves at the published HEAD | CTO @`adaf13fec6` + AMENDMENT 1 @`4493cf1800`; COO SIGNED @`e35e3a46dc`; both bind pin `b921635dad`, nine members, one function |
| 1 | Census at the pin | rc=0, built 63 / live 63, `changed_members=9`, exactly the nine named |
| 1b | Live `CodeSha256` gate | `exDoi/uo5eB9RdFt7/xkZ8OD28Pq6bCejYb7n/zitlg=`, LastModified `2026-10-06T01:35:28Z` — UNMOVED from the COO half's read |
| 2 | Open the NEVER-2 ledger, commit the sentinel | @`cccbd5d31d`; rollback source named: objver `MteawDsTqojjkhh4e8Xfp_u6T7F8NxX3` |
| 3 | `build-and-upload.sh` | REFUSED first (ADHC_DRIFTD.002). Second run with a justified override: SHA256 `aRCgH9B0pglos8cPiybPhmJShzjUts/Tr5R9R/AZYJw=`, 405,052 B, write VERIFIED, new objver `ZBwAzArTtDSpCIYL8CwhqqmIooS4mVPx` |
| 4 | `terraform plan` (saved planfile) | `0 to add, 1 to change, 0 to destroy`; only `s3_object_version`, `source_code_hash`, `last_modified` |
| 5 | `safe-apply` from the planfile | `Apply complete! Resources: 0 added, 1 changed, 0 destroyed` at `14:38:36Z` |
| 6 | 0-diff re-plan | `No changes. Your infrastructure matches the configuration.` |
| 7 | `record-terraform-deploy.sh --function irpt-export-render` | @`f874b0ad85`; only the irpt-export-render entry moved |
| 8 | Close the ledger | All 4 legs proven, entry CLOSED, sentinel removed @`bf8bb487a9` |

### The three-plane baseline, measured before the act

| plane | value |
|---|---|
| live Lambda `CodeSha256` | `exDoi/uo5eB9RdFt7/xkZ8OD28Pq6bCejYb7n/zitlg=` |
| S3 current object version | `MteawDsTqojjkhh4e8Xfp_u6T7F8NxX3` (content-sha256 identical) |
| tfstate `source_code_hash` | identical, `s3_object_version` identical, serial 36 |

All three agreed, so the rollback source is coherent rather than assumed. `terraform_version` in the
remote state already read `1.15.8`, identical to the PATH binary — so `main.tf`'s warning that a PATH
substitute re-pins remote state did not bite here. That was read, not assumed; `.tools/terraform.exe`
does not exist on this device and `safe-apply`'s documented fallback covers it.

### After-reads

| # | arm | verdict |
|---|---|---|
| 1 | deployed sha == built; re-plan 0 | PASS |
| 2 | live `entry.py` sha256 starts `fc241d806ecc` | PASS — **the fix is in the running bytes**; live zip is 63 members |
| 3 | existing un-back-filled export refused (admin principal) | PASS — `this receipt names no covered account` |
| 6 | outside path refused (reconstructed non-Opal principal) | PASS — opaque ids only, no token minted |
| 7 | admitted Opal caller still served | PASS — positive control ADMITTED |
| — | discriminator control | the out-of-scope case lands on the **distinct** counts branch, so 3 and 6 are the fail-closed branch and not a blanket deny |
| 4, 5 | new / performance / analysis export reaching READY | OPEN-BY-DESIGN under AMENDMENT 1 |

Arms 3, 6 and 7 were exercised on the DEPLOYED bytes — the live zip extracted and `entry._covered`
imported from it (full module import, `entry.py` sha256 verified `fc241d806ecc` before use) — which
is IB-pr-347's own method. No token was minted and nothing was written to the auth plane.

---

## Work Completed

### 1. The release
Above. The emergency fix is live and the refusal path is proven in both directions with controls.

### 2. The build refusal, and why the override was the only in-lane route
`build-and-upload.sh` refused: `backfill_covered_account_ids.py` sits in `export/` on disk but is not
in `lambda-source-map.json` `files[]`. It arrived from TO-IB-pr-344 — the PRD v0.30 item 35 back-fill
both halves name as *the next act, under its own pair*. Registering it would make the package 64
members, which both halves say stops the release, and the TO's source-map bound admits only the
artifact and deploy fields. Editing the script's ignore list is out of this lane.

So `BAU_PARITY_SKIP=1`, with the safety established first rather than asserted: the limb it disables
is disk→manifest only; the manifest→disk existence check (`:399-411`) ran and passed; every member
staged `sha256 verified`. An import census over the source dir scanned 45 `.py` files and found ONE
reference to the module, in `tests/test_backfill_covered_account_ids.py` — a path the limb itself
excludes and the build never packages. Positive control: 13 imports of `bundle` in the same sweep, so
the zero over packaged members is a true absence and not a dead scanner. Confirmed after the fact:
the live zip is 63 members with the file absent. Row `IRPT_BCKEND-S381`.

### 3. The fence check (the relay's second ask)
No applied control denies a firm-data READ to the dell2 identity.
`cloudops-dell-agent-deploy-policy` Sid `S3ObjectsOnOpalBuckets` allows `s3:GetObject` on
`arn:aws:s3:::opal-*` and `opal-*/*` with **no Condition**, to the group holding both dell users.
Census over the five group policies, denominator printed: 21 statements, 11 Deny, **0** covering
`s3:GetObject`; every Deny is a delete, a write or an IAM/CloudTrail/Lambda/SSM guard. `opal-data-cot`
carries no bucket Deny at all.

`1.0.0_SA_CTO` dispositioned it (msg 106352) before the row landed: those reads are inside the Dell
grant as signed in round 3, the fence is on three other buckets, and W148-S2 is spec wording. My
first framing called it an exposure; that was wrong and row `IRPT_BCKEND-S383` says so and was re-filed
OBSERVATION/INERT. `0.7.0_AE_CloudOps~E` then corroborated and SIZED it (msg 106355): where a fence
exists it *does* refuse `GetObject` — explicitDeny measured for the dell1 user on all three firm
buckets — but the census reads buckets=24 fenced=3 no_policy=11 no_fence=10, and ~E's own applies have
made dell2 admitted 24/24, so with that statement unconditioned dell2 reads every `opal-data` bucket
rather than the three its projects need. What remains is a least-privilege residual inside an
authorized grant, and it is the CTO's to rule on.

### 4. Why the round-68 check grades FAIL on this device
`checks/r68/p68_cells.py:72` calls `subprocess.run(["bash", aws, ...])`. On Windows a bare `bash`
resolves to the System32 WSL stub, which answers `execvpe(/bin/bash) failed`. Reproduced with
relative, posix-absolute and windows-absolute path forms — identical stderr each time, so the argv0 is
the variable, not the path. The shim itself is fine: run by hand it returns the live `CodeSha256` rc=0.
CLAUDE.md names this trap and the repo ships `.tools/git_bash_resolver.py`, whose docstring reads
*"NEVER returns bare bash (that Windows-resolves to the System32 WSL stub)"*. With only that argv0
routed through `bash_argv` and the issuer's file otherwise untouched, the same check prints
`IB68-1-AC1 PASS`. Row `IRPT_BCKEND-S384`. I did not edit the check — it is not in my `<paths>`.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Took `BAU_PARITY_SKIP=1` rather than registering the extra file | Registering widens the signed member set, which both halves say stops the release; the override yields exactly the signed 63/9 package, and no packaged member imports the file (45 scanned, 1 hit, in `tests/`, with a working positive control) |
| Did NOT roll back on the unexercised positive control | Branch B fires on a FAILURE of after-read 1 or 4. 1 passed; 4 was never run, which is not a failure. Rollback REOPENS the hole for 7 principals, and the COO half admits it only on a failure other than reads of un-back-filled exports. Escalated as a BLOCKING row instead; the issuer then ruled exactly this (AMENDMENT 1: "grade on the controls … Do not mint a principal") |
| Did not mint a test principal for after-reads 4/5 | My own BOUNDS say "No write to the auth plane", and `RT2_test_principal_human_gated.md` records the mint path as HUMAN-GATED. The order's refusal clause makes a needed-but-ungranted path a BLOCKING row, never an override |
| Minted row ids BARE and gapped at S381, after trying `I-S1` | The row gate refuses coordinate `I`: the device register holds only `D1`, `D2`, `Z` — there is no coordinate for the laptop, so a laptop seat can only mint bare and races dell2's bare sequence. dell2's branch is at bare max S370, so bare S371 would have been its next mint — the exact collision that forced the S370 withdrawal @`3f56b516ee` |
| Aborted the `git merge CLOUD` into the worktree | It conflicted in the append-only surprise channel exactly as CLAUDE.md 14b predicts. The merge was only for the validator's convenience; hand-resolving a shared channel for that is not worth it |
| Did not push; did not tag | LD-0367/0368 — the hook blocked the push and said to coordinate with the integrator, so push state is reported LOCAL and measured. Zero `investor-reporting-v*` tags exist, so Rule 6's first tag version is a convention I will not mint unilaterally |
| Scoped `record-terraform-deploy.sh` with `--function` | Bare, it sets `last_deployed_commit` for every function in the pipeline; my bounds allow only the irpt-export-render entry. Verified after: only that entry moved |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `irpt-export-render` (served Lambda) | code + object version → the IB-pr-343 fix | Yes — applied `14:38:36Z`, `0 added, 1 changed, 0 destroyed` |
| `s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-export-render.zip` | new version `ZBwAzArTtDSpCIYL8CwhqqmIooS4mVPx` | Yes — write VERIFIED |
| `infra/aws/lambda/ci/lambda-source-map.json` | `artifact_sha256`, `last_deployed_commit`, `last_deployed_at` on the one entry | Yes — `cccbd5d31d`, `f874b0ad85` |
| `org/critical_paths/change_management/20261007T1356Z_...deploy_completion.md` | NEVER-2 ledger opened then CLOSED | Yes — `cccbd5d31d` → `bf8bb487a9` |
| `org/critical_paths/.open_deploys/irpt-export-render-...json` | sentinel committed, then removed at close | Yes — `cccbd5d31d` → `bf8bb487a9` |
| `org/missions/D9/.../surprise-channel/investigations/INVESTIGATION_v1.md` | rows S381, S382, S383, S384 | Yes — `7b44c38e3d`, `d9406f5832`, `5bdafc2916` (ON ORIGIN) |
| `org/missions/D9/.../deliverables/0.7.0_AE_CloudOps~I/IB68-1_release_after_reads.json` | after-reads, then amended to AMENDMENT 1's shape | Yes — `bf8bb487a9` (branch), `0fe967b745` (CLOUD, authoritative) |
| `org/missions/D9/.../deliverables/0.7.0_AE_CloudOps~I/...proof_of_spec.json` | proof instance | Yes — `0fe967b745` — **LOCAL** |

---

## Blockers

**None owed by this seat.** One item waits on the integrator and is not a blocker on the work:
commit `0fe967b745` (the amended after-reads file plus the proof instance) is LOCAL, and
`2.0.0_SA_COO~P2`'s re-run reads `ledger_closed is None` because it drained the pre-amendment version
@`bf8bb487a9`. Landing `0fe967b745` unblocks that re-run; asked of `0.0.0_AB_MSTR` at msg 106405.
Push state, measured by `ls-remote`: rows `5bdafc2916` ON ORIGIN; `0fe967b745` LOCAL; origin/CLOUD
`8798e5f484`, local CLOUD `ef7133ec9a`.

---

## Current State

`irpt-export-render` is live at `CodeSha256 aRCgH9B0pglos8cPiybPhmJShzjUts/Tr5R9R/AZYJw=`
(LastModified `2026-10-07T14:38:36Z`), its packaged `entry.py` is sha256 `fc241d806ecc`, and a
0-diff re-plan of `infra/aws/terraform/investor-reporting/export` reads `No changes` — so the
fail-closed `_covered` and the admitted-read log line are in the running bytes, and an export read
whose receipt names no account is now REFUSED for every principal including an admin. The accepted,
signed availability cost is live with it: every receipt written before IB-pr-343 names no account and
stays refused until IB-pr-350's back-fill runs under its own pair. The NEVER-2 ledger
(`20261007T1356Z_irpt-export-render-ib-pr-349-failclosed-20261007`) is CLOSED with all four legs
proven and no sentinel; the rollback source `MteawDsTqojjkhh4e8Xfp_u6T7F8NxX3` was re-read after the
act and is still retrievable. `IB68-1-AC1` reads PASS under AMENDMENT 1 @`b883510cd9` with a planted
mutant fired; the proof instance reads INVALID on either root *alone* only because the governing TO is
on the dell2 branch while the four cited rows are on CLOUD — the two roots are complementary and the
drain resolves it.

---

## Next Steps

1. **[`0.0.0_AB_MSTR`] Land `0fe967b745`** — it carries the amended after-reads file and the proof
   instance; `2.0.0_SA_COO~P2` cannot re-grade without it, and its current FAIL is reading
   superseded bytes.
2. **[`2.0.0_SA_COO~P2`] Flip `<status>` on TO-IB-pr-349 and fix the check's bash resolution** —
   one line at `:72`: import `.tools/git_bash_resolver` and call `bash_argv(aws, ...)`, or invoke
   `.tools/aws.cmd` directly. Row S384. Also register `backfill_covered_account_ids.py` in `files[]`
   under TO-IB-pr-344's own pair (row S381) so the next build of this function needs no override.
3. **[`1.0.0_SA_CTO`] Rule on a read-Deny for the 21 unfenced buckets** — row S383 plus
   `0.7.0_AE_CloudOps~E`'s denominator (24 buckets, 3 fenced) and the composition point that dell2 is
   now admitted 24/24. The grant is signed; the residual is least-privilege, and neither AE seat
   adjudicates it.
4. **[`2.0.0_SA_COO~P2`] IB-pr-350, the back-fill** — it is what discharges the three OPEN-BY-DESIGN
   arms and what restores read access to every pre-IB-pr-343 receipt.
