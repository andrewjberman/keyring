# OW-d-1 built and staged, then refused at the apply: dell2's cloudops principal cannot plan the trade-pipeline tree -- 0.7.0_AE_CloudOps~OW2

**Date:** 2026-10-09
**Task Order:** NFRA_OPSWKF.TO-APPLY-D1.trade-lambdas-ticket-bridge-ow2 (`org/tier2_senior/0.7.0_AE_CloudOps~OW2/task_orders/`, issued @a7dd8f7b6f)
**Status:** BLOCKED
**archetype:** DEPLOY

---

## Objective

Deploy ONE `safe-apply` of `infra/aws/terraform/trade-pipeline` at box/dell2 pin `71a1877db0`, covering the
code of `trade-submission-handler` and `trade-workflow-handler`, `TICKETS_TABLE` on both, and the two
`TicketBridgeOpalTickets*` statements on `trade-submission-policy` -- nothing else -- under the never-widen
pair (COO half @ad3f901e17, CTO half @a4c661373b), with this lane substituted as applier by CTO ruling
@5ff94852a6.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| to-check | `to-check.py --all --assignee 0.7.0_AE_CloudOps~OW2` | PASS | 1 active TO, exactly the one in the dispatch message; no phantom holdings |
| sequence-check | `sequence-check.py --project NFRA_OPSWKF` | PASS | PLACED, stage 3, dep_stage=EXECUTING |
| deploy_ledger | `open` / `close-leg L1` / `close-leg L2` / `hold` | PASS | the `hold` REFUSAL is the tool working: it will not HOLD an entry with open apply legs |
| safe-commit | 4 commits under this lane's author line | PASS | `-F` message files written by the Write tool, never `-m` |
| safe-apply | `-chdir=infra/aws/terraform/trade-pipeline apply <planfile>` | PASS (as a GATE) | exit 4, fail-closed, terraform never invoked -- the correct outcome, see Blockers |
| surprise-row-gate | at commit, 2 new rows | PASS | first attempt REFUSED on `/class` and `/disposition`; the enums are OBSERVATION/BLOCKING and UNDER_INVESTIGATION/GRADUATED/DISMISSED_WITH_REASON/DECOMP_INVALIDATING |
| comp-iam | not run | SKIPPED | the order's `<preflight>` declares it NOT-APPLICABLE at the cut; the live policy is graded by the step-5 simulate arms, which cannot run before the statements exist. Running it now would have hit the documented false-allow mode (an `allowed` against a statement that does not yet exist). |
| comp-rail | two denials | PASS | denied a `grep -rn` over two source dirs and a `grep` over a `*.tf` glob; both re-run as named-file reads, which answered |

**What worked:** `deploy_ledger`'s refusal to HOLD a half-landed entry, and `safe-apply`'s fail-closed
tagauthz limb, were the two instruments that produced the right answer against my intent to proceed.
`ow_checks.py i1-cond` answered CTO condition 1 in one call.
**What failed:** nothing produced a wrong answer.
**Gap found:** `safe-apply`'s comp-tagauthz limb cannot grade a TARGETED or planfile apply within the
permissions a targeted apply actually needs -- it re-plans the WHOLE tree, so one unreadable resource
anywhere in the tree blocks every apply to it. The naming limb already reads the caller's planfile
(`safe-apply.sh:285`); `:342` records the same reuse for tagauthz as DEFERRED. Recorded as row
`NFRA_OPSWKF-D2-S3`, not acted on.

---

## Work Completed

### 1. Startup and orientation

`/watcher` (registered, one watcher armed, re-armed once on its `[WATCHER-EXPIRED]` line -- Monitor tasks
`bj2qhd4e8` then `b4yaoy51c`), then `org/XXX.md` A.1/A.2/A.3/D/E and `/cloud-ops`. Identity cross-checked
against `org/mcp/liveness.json`: one row, this serial at PID 31552, no conflict. Message 2969 opened and
acked -- the only ackable row ever addressed to this lane.

### 2. Pre-act reads (all measured, no step skipped)

| Check | Result |
|---|---|
| STOP 1 -- `git diff --name-only 71a1877db0 HEAD` over the two surfaces | EMPTY. Positive control: 932 files differ pin..HEAD repo-wide, so the pathspec is not silently matching nothing |
| OW-d1-AC1 -- `ow_checks.py i1-cond` | **MET**: `OW-I1-COND-OK GetItem stmt + UpdateItem stmt conditioned to ['events', 'linked_submission_id', 'status', 'ticket_id']; env on 2 functions`. The checker is byte-identical pin..HEAD |
| CTO condition 1, read a second way from the CODE | The only `opal-tickets` writers are `bind_ticket` (SET linked_submission_id, events), `unbind_ticket` (REMOVE linked_submission_id) and `sync_ticket` (SET events, optionally status). Union = {linked_submission_id, events, status} + key ticket_id = exactly the conditioned list. No `updated_at`, which the half named as a candidate. Nothing needed widening |
| Built handler sha256 | Equal to the objective at the working tree AND at the pin's blobs, for both files |
| COO half bytes | Packet blob at ad3f901e17 is `a921977542de220111ca88b5524f51fecccd7637`; `git hash-object` of the HEAD file is the same, so the signed text has not drifted |
| Pre-existing ledger | NONE. Swept `.open_deploys/` by `ls-tree` AND `ls -a` across every live worktree: 0 of 43 carry a trade/opswkf entry, positive control 41 of 43 carry an `irpt` entry. Corroborates the withdraw @7199703ea1 |

### 3. Legs L1 and L2

**L1 (BEFORE reads).** Rollback pins recorded: `trade-submission-handler.zip` =
`S4xlyU0kBjVqTfqywTwhAb6nHmuSK4Fs`, `trade-workflow-handler.zip` = `nGDl6NWpkMdQLwcCSIE92YRuh71vabEO`.
Each function's live `CodeSha256` equalled its artifact's `content-sha256`, so the baseline had no
stale-running-bytes hazard. Env on both: `[DASHBOARD_URL, EMAIL_FROM, SUBMISSIONS_TABLE]`.
`trade-submission-policy`: 5 statements, zero `opal-tickets`.

**L2 (build + upload).** Built PER FUNCTION, never the whole-pipeline form -- `s3_object_version` is a
`data.aws_s3_object` read at plan time, so a pipeline-wide build would have moved
`trade-dashboard-api.zip` and `trade-parquet-batch-export.zip` and pulled their functions into the plan,
which is branch B. Verified after upload that only the two intended keys moved (dashboard still
@2026-07-21, parquet-batch still @2026-07-14). New versions `UfDVwCjbt.EJrkTBv9.Ei2_2b4Eg2VNR` and
`0xtFDu9OOdfXnl_3qPCcUgMT_EmUnvfS`; zip-content sha256 `Mw5sshdjyyuObV6J1tcbz4sSnD5yoNQUh9Bp2HW3Ifs=` and
`uWqGvRL/HfP6crogFOCkjRVfkNTxOH4jab/g+atRXzQ=`. Handler hashes verified by EXTRACTING each uploaded zip
and hashing the file inside, not by filename; each zip's own sha256 independently recomputed.

### 4. The plan, and the refusal

`jwt_secret` was hydrated into the gitignored `secrets.auto.tfvars` per the tree's README, from the live
`trade-auth-handler` env -- precisely so the other four functions show no spurious drift. The value was
never printed (length 64, sha256 prefix `6e8c7046b929`).

Untargeted plan: rc=1. It rendered `Plan: 0 to add, 3 to change, 0 to destroy` over exactly the three
OW-d-1 resources -- **branch A** -- and then errored 403 on refreshing
`aws_ses_configuration_set.trade_pipeline`. Targeted plan over the three resources: rc=0, clean,
same 0/3/0, with the policy's `UpdateItem` conditioned to exactly
`[ticket_id, linked_submission_id, events, status]` and each function moving FROM its recorded rollback
pin TO the version I uploaded.

`safe-apply` with that saved planfile: **exit 4, fail-closed, terraform never invoked.** Its comp-tagauthz
limb runs its own untargeted `terraform plan` over the whole tree and takes neither `-target` nor the
caller's planfile, so the same 403 makes the gate unable to evaluate.

### 5. Disposition

Rows `NFRA_OPSWKF-D2-S2` and `NFRA_OPSWKF-D2-S3` appended @`d8056d8c7f`. One report sent to
`2.0.0_SA_COO~O2` (msg delivered 09:54Z). The ledger entry stays OPEN/RED by design.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Build per function, not per pipeline | `s3_object_version` is a plan-time data-source read, so moving the other two artifact keys would have widened the plan into branch B. The narrower form was the only one consistent with the signed write set |
| Apply a SAVED plan file rather than re-planning inside the apply | The apply then does exactly the diff I read, closing the read-then-apply window on the three resources |
| Did NOT use `TAGAUTHZ_OVERRIDE` | `safe-apply` says in terms that it "is not the remedy for this error" and "Do not bypass a gate to work around your own toolchain". Self-granting a bypass to land one's own deploy is the shape the no-manufactured-friction law exists to prevent |
| Did NOT grant this lane's own principal the missing permission | The principal is defined in `infra/aws/terraform/nfra-ctlpln-identity/`; this lane is seated for NFRA_OPSWKF only, and the grant sits outside the signed blast radius |
| Did NOT roll back the two S3 uploads | There is nothing in the world to roll back: both functions still pin their prior `s3_object_version`, so the new versions are unreferenced. An S3 delete also needs human confirmation, and the next applier wants these artifacts |
| Did NOT run step 5(d) early as a probe | An unauthenticated `POST /api/general/trades/submit` that unexpectedly succeeded would have created a real trade submission. The order sequences it after the apply, and running it now would not change the blocked state |
| Left the ledger OPEN/RED rather than forcing a HOLD | `deploy_ledger hold` refused it with apply legs open; the RED is the designed signal to the issuer |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/critical_paths/change_management/20261009T0922Z_nfra-opswkf-ow-d1-trade-lambdas-20261009_deploy_completion.md` | NEVER-2 entry opened, L1 and L2 closed with proof | Yes -- `ca366778d4`, `240024a9f9`, `a57eab7482` |
| `org/critical_paths/.open_deploys/nfra-opswkf-ow-d1-trade-lambdas-20261009.json` | the sentinel | Yes -- same three |
| `infra/aws/lambda/ci/lambda-source-map.json` | two `artifact_sha256` values (the builder's own write) | Yes -- `a57eab7482` |
| `org/missions/D9/NFRA/NFRA_OPSWKF/surprise-channel/investigations/INVESTIGATION_v1.md` | rows D2-S2 and D2-S3 appended | Yes -- `d8056d8c7f` |
| `infra/aws/terraform/trade-pipeline/secrets.auto.tfvars` | hydrated from the live value per the tree's README | No -- gitignored by `infra/aws/terraform/.gitignore:5`, verified with `git check-ignore -v`. It holds a live signing secret at rest on this device; disclosed here rather than left as a silent artifact |

Nothing under `infra/aws/terraform/trade-pipeline/*.tf` or `infra/aws/lambda/trade-pipeline/` was edited.
The code being deployed was already merged at the pin.

---

## Blockers

- **BLOCKED on an UNASSIGNED grant, routed to `2.0.0_SA_COO~O2`:** `cloudops-dell2-agent-user` needs
  `ses:DescribeConfigurationSet`. Per the Blocker Verification Protocol this is the AMBIGUOUS class, not
  the BLOCKED-on-a-seat class -- no agent's log or task order corroborates the dependency because it is
  not yet owned by anyone -- so it was escalated rather than parked on a serial.
  **Evidence:** row `NFRA_OPSWKF-D2-S3` @`d8056d8c7f`; `safe-apply.sh:424-427` and `:342`; the 403 named
  `aws_ses_configuration_set.trade_pipeline`, `ses.tf:19`.
  **Natural home of the fix:** `cloudops-dell-agent-plan-reads-policy`, whose stated purpose IS the reads
  terraform needs at plan time and which today carries only two `ssm:GetParameter` statements
  (`get-policy-version` v2, 09:45Z). Defined in `infra/aws/terraform/nfra-ctlpln-identity/`.
  **Honest limit:** that this ONE grant suffices is INFERRED, not measured. The failing plan surfaced one
  error and still rendered a summary, but anything downstream of the failed resource may have been skipped
  rather than read, so a second SES read may surface once the first lands.

- **NOT blocking, pre-existing, owner-less in this lane:** row `NFRA_OPSWKF-D2-S2` --
  `trade-workflow-handler`'s `parquet_exporter.py` imports pyarrow at module top level while the function's
  only layer is `openpyxl-layer:3` at 817,805 bytes. The import at `workflow_handler.py:529` is lazy, so
  the path is dormant rather than broken, and this act changes no layer and no packaged file.

---

## Current State

NFRA_OPSWKF OW-d-1 is BUILT AND STAGED BUT NOT APPLIED, and the live world is byte-identical to its
pre-session state, measured after the refusal: `trade-submission-handler` and `trade-workflow-handler` are
still at `CodeSha256` `AaR7TiZ0qAGfzozoKmd+JFgvdBvQEcymjP/T+Yfzp50=` and
`ChlY4kHsBjueRP2tGawZgXRZ0Qpzx4P48vTdPyRlFYY=` with `LastModified 2026-09-25T17:19:52Z`, env still the three
prior keys with no `TICKETS_TABLE`, and `trade-submission-policy` still 5 statements with zero occurrences
of `opal-tickets` in the live document. The two new artifact versions
(`UfDVwCjbt.EJrkTBv9.Ei2_2b4Eg2VNR`, `0xtFDu9OOdfXnl_3qPCcUgMT_EmUnvfS`) sit in
`opal-313476888478-lambda-artifacts` unreferenced, because both functions still pin their prior
`s3_object_version` -- so nothing is half-landed and the ledger's rollback pins remain valid. The ledger
entry `nfra-opswkf-ow-d1-trade-lambdas-20261009` is OPEN/RED with L1 and L2 closed-with-proof and L3/L4/L5
open. The task order stays `pending`. Push state: LOCAL @`d8056d8c7f`, origin `box/dell2` @`933e33667e`
(`git ls-remote` read) -- this seat does not push a shared branch; `box-sync` carries it.

---

## Next Steps

1. **[2.0.0_SA_COO~O2] Route the `ses:DescribeConfigurationSet` grant to the NFRA_CTLPLN identity owner** --
   it is the single thing standing between a clean branch-A targeted plan and the apply. Asked in the 09:54Z
   report; this lane does not chase it and will not grant itself the permission.
2. **[0.7.0_AE_CloudOps~OW2] On the grant landing: re-plan, confirm rc=0 and branch A still reads 0/3/0
   against the SAME two uploaded object versions, then `safe-apply` and run step 5 (a) to (e)** -- including
   the CTO's negative arm, an `UpdateItem` naming `answers` DENIED. The rollback pins and both built sha256
   values are already in the ledger, so the act resumes without rebuilding. If a second SES read surfaces,
   it goes back to the same owner, not around the gate.
3. **[2.0.0_SA_COO~O2] Decide whether OW-d-1 should instead be re-seated on a device whose principal can
   plan the tree** -- the alternative to the grant. CLAUDE.md rule 26 forbids ferrying the apply, so this is
   a re-seating call for the issuer, not a workaround this lane can take.
4. **[owner of `safe-apply.sh`, via 1.0.0_SA_CTO] Consider letting the tagauthz limb read the caller's
   saved planfile** the way the naming limb already does at `:285` -- `:342` records it as DEFERRED. Surfaced
   in row D2-S3; proposing is legal, implementing is not this lane's act.
