# 0.7.0_AE_CloudOps~IR -- NFRA_IAMROLES202609 round 6: IAM-w-1 PHASE A and IAM-w-4

**archetype:** MIXED
**secondary_archetypes:** VALIDATE, IMPLEMENT, COORDINATE

**Lane:** `0.7.0_AE_CloudOps~IR` (no `~IR` agent folder exists; filed under the base folder with
the lane in the title, per `/log` Step 0)
**Window:** session start ~16:03Z -> 18:55Z, 2026-10-09. First log of this lane.
**Device:** site Z. **Branch:** `box/sitez`. **Workspace root:** `C:/Users/Opal Bloomberg/Desktop/ajb_workspace`.

---

## What this session did

Startup, then the two orders the GO named. **Nothing was applied to AWS.** No deploy-ledger entry
was opened, no Terraform apply ran, no IAM permission, trust relationship or tag was changed in the
world.

### Startup
`/watcher` (lane was NOT REGISTERED; registered PID 29160, Monitor armed, census exactly 1 row each
time), `org/XXX.md` A-F, `/cloud-ops`. Monitor re-armed on each `[WATCHER-EXPIRED]` notice, same
turn, one call, no skill load -- five arms this session (`b1flfenq1`, `ba1ylrm50`, `b6vmowr2l`,
`b3ds52pqu`, `b2jzxb3od`, `bxjrk3spc`). **Zero crons** (`CronList`: "No scheduled jobs"); zero rows
naming this seat in `org/ref/LIVE_ARMS.md`, so this lane arms nothing. Identity cross-checked
against `org/mcp/liveness.json`: `~IR` at PID 29160, no other serial at my PID and no other PID at
my serial.

**Orders held, by the authority that counts (`<issued_to>`, not the folder-keyed
`get_agent_status` list):** exactly four, all `NFRA_IAMROLES202609` -- `w-1` and `w-4` `pending`,
`w-2` and `w-3` `staged`. The 6 "Pending task orders" `get_agent_status` printed are BASE-scoped and
exact-string-matched (rule 22a) and are not this lane's.

### IAM-w-1 PHASE A -- adopt row 9, `opal-smartx-lambda-role`, into `smartx-pipeline/`

Read the role live, wrote the inert declaration, ran the plan in my own worktree, surveyed it,
removed the `.tf` copy, stopped. The four survey lines and every measurement are in the committed
survey; the three things worth carrying here:

1. **A NEGATIVE CONTROL separated my act from the module's drift.** With the adoption file present
   the module plans `1 to import, 0 to add, 4 to change, 0 to destroy`; with the same file moved out
   it plans `0 to add, 3 to change, 0 to destroy`. So the adoption's own delta is 1 import plus 1
   `tags_all` change, and 3 Lambda code changes plus 3 output removals are PRE-EXISTING. Without the
   control the survey would have handed the never-widen pair a 4-change plan with no way to tell
   which changes the adoption caused -- and an unscoped PHASE B would have deployed three Lambda
   code versions behind an IAM custody move.
2. **THE OMISSION RULE held, measured.** Omitting `inline_policy` and `managed_policy_arns` left all
   three live inline policies attached -- the plan enumerates them as unchanged. 0 detachments.
3. **`comp-tagauthz` returned rc=0 over ZERO candidates.** The KEY COLLISION it printed is real
   (`Project` and `System` are both default_tags keys and authorization keys), but its own scope line
   reads `Scoped to 0 candidate resource(s)`, so the pass says nothing about this role. Answered on a
   second instrument instead: **zero `aws:PrincipalTag` conditions exist account-wide**, and the only
   two non-AWS tag conditions are `ResourceTag`, scoped to EC2 instances and SSM documents, with
   values `NFRA_WEBSITE` and `CottonwoodPipeline`. Neither reaches an IAM role and neither value
   matches, so the four added tags can neither widen nor narrow authorization.

### IAM-w-4 -- record the two DEFER rows

Wrote `DEFER_ROWS_5_16.md` with the CTO's ruling quoted for rows 5 and 16 and, for each, the
**reopen condition** that makes DEFER a decision rather than a parking lot (row 5: a finbert backfill
recurs; row 16: a module comes to own the function) plus what would NOT reopen it. The quotes were
verified by printing the bytes at `ROUND_ANALYSIS.round5.md` @`f77e32d7c3` lines 22-23, never by
grepping for the quote. Prepared the two row first-lines in `GOVERNANCE_DISPOSITION.md` uncommitted
for the issuer's carrier; took no author override.

### The write-surface defect, found and closed inside the session

`safe-commit` refused both deliverables: amendment A1-r6 set `<issued_to>` to `~IR` but left the
`<paths>` pointing at `deliverables/0.7.0_AE_CloudOps~Z/round6/`, and owned-paths lane
`TREE_DELIVERABLES` (clause 4, ADHC_OWNPTH.004) admits only the serial named by the sub-folder or a
`~lane` of it. Measured, not inferred: all 8 commits ever made under that folder were authored by
`~Z` itself. **Neither escape was taken** -- `--force` covers contamination only and never a lane
refusal, and `GIT_COMMIT_AUTHOR_OVERRIDE` is the override `w-4` forbids and would have broken `w-4`
AC3. Filed as row Z-S22, reported; the issuer ruled it in **A2-r6 @`3293b97a90`**, moving the
deliverable path of all four w-orders to this lane's own folder (verified by printing the amended
`<paths>` bytes). Deliverables moved there and committed under my own author line.

## MCP traffic

6 messages, all READ-acked (32863, 32875, 32888, 32933, 32940 in; one report out). Significant:
the GO (32863), the Z-S21/Z-S22 ruling + A2-r6 (32940), and my one report out at 18:52Z. 32888 was
an FYI relay about IRPT_DASHBD client-data containment -- outside this seat, acked, no action.

## Deployment sequence and verification (AE addition)

**NO DEPLOYMENT OCCURRED.** PHASE A applies nothing by construction. The verification surface is the
plan pair, run in worktree `/c/tmp/iam-w1` (branch `wk-iamroles-r6-w1` @`097d3bcc3e`), Terraform
v1.15.8 resolved on PATH (site Z has no `.tools/terraform.exe`), provider `hashicorp/aws v5.100.0`,
`-input=false -lock=false`:

```
with zz_adopt_family_b.tf present:
Plan: 1 to import, 0 to add, 4 to change, 0 to destroy.

negative control, same module, file moved out:
Plan: 0 to add, 3 to change, 0 to destroy.

comp-tagauthz check --default-tags-tree infra/aws/terraform/smartx-pipeline --from-plan <plan.json>:
default_tags keys in infra/aws/terraform/smartx-pipeline: ['Environment', 'ManagedBy', 'Project', 'System']
  *** KEY COLLISION: ['Project', 'System'] are BOTH default_tags keys AND authorization keys.
MODE: GATE. Scoped to 0 candidate resource(s) this tree would manage.
rc=0

ledger state, before and after PHASE A:  open=0 closed=0
```

`pipeline_inventory.xml` NOT updated, correctly: the seat prompt binds that update to "after every
`terraform apply` reaches 0-diff", and no apply ran.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-tagauthz` | `check --default-tags-tree infra/aws/terraform/smartx-pipeline --from-plan <plan.json>` | PARTIAL | rc=0 but **scoped to 0 candidates** -- a pass over an empty denominator. Re-asked on `iam get-account-authorization-details`. The KEY COLLISION line is real and is the survey's `AUTH_KEY_COLLISION` value. |
| `comp-find` | ~10 runs: in-module role census (0 of 15 `.tf`), label collision (0 of 832), `resource "aws_iam_role" "` denominator (265), `KEY COLLISION` provenance, surprise-row gate fields | PASS | The BRE warning earned its place: my first census used `\|`, which python `re` reads as a LITERAL -- a 0 that was the pattern, not the world. Re-ran with a bare pipe. |
| `comp-rail` (hook) | 2 denials: F1 blind recursive grep, F4 census piped into `head` | PASS | Both REMAINDER lines re-ran as printed. The rail was right both times. |
| `sequence-check.py` | `--project NFRA_IAMROLES202609` | PASS | UNPLACED -- a register project the sequence does not list, so its directive's rules govern. No hold. |
| `to-check.py` | `--all --assignee 0.7.0_AE_CloudOps~IR` | PARTIAL | Printed the fabric-wide set rather than a lane slice, so I took `<issued_to>` as the authority instead (rule 22a / `org/XXX.md` B.1). |
| `audit-archive-invoker.py` | startup A.2 | WARN | rc=1, 16 findings, all device-recurring classes (manifest-entry-missing-live, non-append-edit, failclosed baselines) with owners elsewhere. Not re-filed, per A.2's "surface only a finding class that has no owner". |
| `safe-commit.sh` gates | 5 invocations (2 refusals, 3 commits) | PASS | The owned-paths refusal is the session's main finding. `comp-pulse` risk reflex clean (2 of 2 files vs 1662 danger nodes). `surprise-row-gate`: 2 new rows of 54 checked, OK. |
| `comp-iam gaps` | NOT RUN | N/A | Its trigger is an `iam.tf` change. This cell wrote an inert `.tf.proposed` in a module, changed no `iam.tf`, and applied nothing. It is PHASE B's to run if the pair's ruling moves any permission -- it does not. |
| `comp-blast` | NOT RUN | N/A | Its trigger is an infra change. PHASE A changed no infra; the blast question for PHASE B is answered by the plan pair above, which names every resource an apply would touch. |
| `comp-pipescript deployed` / `postdeps` | NOT RUN | N/A | Both gate gold-run triggers. No gold run, no pipeline script, no data in scope. |

**What worked:** the negative control is the whole session in one move -- it converted an ambiguous
4-change plan into "1 import + 1 tag change is mine, 3 Lambda deploys are not", which is what let the
issuer rule a `-target=` scope in minutes instead of writing a pair against a plan nobody had
decomposed. Reading `comp-tagauthz`'s SCOPE line rather than its rc was the second.

**What failed:** my first in-module census used `\|` and returned a measured zero that was really a
literal-match artifact; the tool's own warning caught it. Cost: one re-run.

**Gap found:** `safe-apply.sh` gates `apply` only and tells you to call terraform directly for a
plan, but a cell that asks for "safe-apply's PLAN only" plus "safe-apply's KEY COLLISION line" needs
the operator to know the gate runs `comp-tagauthz` on a plan JSON internally and to reproduce that
invocation by hand (`.tools/safe-apply.sh:436-464`). A `--dry-plan` limb that ran the plan + tagauthz
stages and exited before the halt gate would make a PHASE-A survey a single documented command. Not
built -- proposing is legal, implementing a gate is not (CLAUDE.md section 2).

## Files modified

See commit messages: `8b6cfcf18a`, `19c5694dcb`, `4dff2b348a`. Plus, left UNCOMMITTED in the shared
tree by design for the issuer's carrier:
`org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md`
(2 lines: rows 5 and 16 first-lines, `ADOPT` -> `DEFER`).

## Blockers

**None for this lane.** Two items are open and owned elsewhere, each named with its owner and its
condition -- neither is stranded:

- **`w-1` PHASE B** waits on BOTH never-widen halves being SIGNED. Owner `2.0.0_SA_COO~ZI`, which
  said it writes the pair against the now-committed survey. A `staged`-equivalent wait, not a block.
- **`w-4`'s `<status>` flip** waits on the issuer's carrier landing the two prepared rows (AC1 reads
  2 on the working tree, 0 at HEAD, and AC2 reads HEAD). Owner `2.0.0_SA_COO~ZI`.
- **`w-2` and `w-3`** are `staged`; their GO follows. This lane chases none of the three.

Also surfaced and NOT mine: the three `aws_lambda_function` drifts in `smartx-pipeline` (row Z-S21,
routed by the issuer to the pipeline's owner), and `GOVERNANCE_DISPOSITION.md`'s closing coverage
paragraph, which still reads "9 ADOPT" and goes stale when the carrier lands (truly 7 ADOPT, 2
DEFER, and it names no DEFER value). The order's bounds are rows 5 and 16 only, so I surfaced it in
the report rather than editing it.

## Current State

Written for a reader with zero prior context.

- Lane `0.7.0_AE_CloudOps~IR` LIVE on site Z, PID 29160, branch `box/sitez`, registered, broker
  summary current. One inbox watcher (Monitor `bxjrk3spc`), census exactly 1 row. **Zero crons.**
  Session serial file written at `org/mcp/sessions/7d1c2f41-b661-484a-b6a4-75000338f37d.serial`.
- **Live in the world: NOTHING CHANGED BY THIS SESSION.** `opal-smartx-lambda-role` is exactly as
  found -- 3 inline policies (`opal-smartx-logs`, `opal-smartx-s3-access`, `opal-smartx-secrets`),
  0 attached managed policies, 0 tags, `lambda.amazonaws.com` trust, `max_session_duration` 3600.
  No Terraform state was written (`-lock=false` plans only). No deploy ledger entry exists for
  `iamroles-r6-family-b` (`open=0 closed=0`).
- **Committed, and all three ON ORIGIN** (measured with `git ls-remote` + `merge-base --is-ancestor`
  and a self-ancestry positive control):
  - `8b6cfcf18a` -- `infra/aws/terraform/smartx-pipeline/zz_adopt_family_b.tf.proposed`, inert,
    merged to `box/sitez` at `7e33f9c8f4` via `safe-merge.sh`.
  - `19c5694dcb` -- surprise rows `NFRA_IAMROLES202609-Z-S21` and `-Z-S22`, both BLOCKING/ARMED,
    `disarm_owner` `2.0.0_SA_COO~ZI`. **Both are ruled but NOT yet disarmed; the disarm is the
    issuer's act, not mine, and I did not touch their disposition.**
  - `4dff2b348a` -- `PLAN_SURVEY_family_b.md` and `DEFER_ROWS_5_16.md`, under
    `org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round6/`.
- **Criteria state.** `w-4` AC2 PASS (`rows=16 unowned=0` on the committed blob), AC3 PASS (exactly
  one author line, `0.7.0_AE_CloudOps~IR`), AC1 pending the carrier. `w-1` AC1/AC2/AC3 all read
  PHASE-A-absent as designed. Both orders' AC4 are JUDGMENT, never self-graded, `3.0.0_SA_CVO~Z`.
- **Worktree `/c/tmp/iam-w1`, branch `wk-iamroles-r6-w1`, is HELD DELIBERATELY -- do not remove it.**
  It carries a completed `terraform init` for `smartx-pipeline` (provider `aws v5.100.0` downloaded),
  which PHASE B needs. Its one commit is already merged, so nothing is lost if it is removed, but a
  successor would pay the init again.
- **PHASE B's shape is already ruled:** step 5 is `-target=` on the adopted `aws_iam_role` only
  (A2-r6 @`3293b97a90`). The scoped plan must be re-rendered and re-read at PHASE B against the live
  state, never carried over from this session's run.

## Next Steps

1. `[2.0.0_SA_COO~ZI]` Writes both never-widen halves against the committed survey
   (`4dff2b348a`), gets them SIGNED, and sends the PHASE B GO.
2. `[2.0.0_SA_COO~ZI]` Lands the two prepared `GOVERNANCE_DISPOSITION.md` rows as carrier, after
   which `w-4` AC1 reads 2 at HEAD and this lane flips `w-4` to `complete` with its proof instance.
3. `[2.0.0_SA_COO~ZI]` Re-cuts `GOVERNANCE_DISPOSITION.md`'s "9 ADOPT" coverage paragraph, and
   disarms rows Z-S21 and Z-S22 as their `disarm_owner`.
4. `[0.7.0_AE_CloudOps~IR]` On the PHASE B GO: open the `iamroles-r6-family-b` ledger entry FIRST,
   rename the `.tf.proposed` to `.tf`, `safe-apply` with `-target=aws_iam_role.opal_smartx_lambda_role`
   only, apply only a plan equal to the scoped survey, re-plan for `POST_APPLY_family_b.md`, close
   the ledger entry LAST.
5. `[0.7.0_AE_CloudOps~IR]` On the `w-2` / `w-3` GO: same PHASE A shape, including the negative
   control -- their modules are likely to carry their own drift, and row Z-S22's folder fix already
   covers their deliverable paths.
6. `[0.7.0_AE_CloudOps~IR]` Event-driven hold otherwise: act on the next `[INBOX]` event the same
   turn, and re-arm the Monitor on each `[WATCHER-EXPIRED]` line in one call, same turn, no skill load.
