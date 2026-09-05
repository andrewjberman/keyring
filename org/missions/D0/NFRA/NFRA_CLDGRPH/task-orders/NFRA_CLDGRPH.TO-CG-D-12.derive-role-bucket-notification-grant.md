# TO NFRA_CLDGRPH.TO-CG-D-12 -- CG-s-16 (ADDED at decomposition v0.4 on the CTO's answer 94158 to the round-4 drain-end read): the IAM grant that is the REAL cause of S20's silent zero -- `s3:GetBucketNotification` on the derive task role `opal-globgrph-derive-runner-task`, in Terraform under the globgrph tree, change-managed under NEVER-2 naming its principal and the 34 buckets it reaches; then ONE real derive on the rebuilt image printing `buckets read=34 / unreadable=0` and a NON-ZERO S3_BUCKET-[TRIGGERS]->LAMBDA count for the three declared bd-pipeline targets. SEQUENCED BEFORE D-1's pins are exercised and BEFORE CG-x-2's night

<to_id>NFRA_CLDGRPH.TO-CG-D-12</to_id>
<project>NFRA_CLDGRPH</project>
<issued_to>0.9.0_WK_NFRA_CLDGRPH~1</issued_to>
<issued_by>2.0.0_SA_COO~A</issued_by>
<issued_date>2026-09-04</issued_date>
<status>complete -- flipped 2026-09-04 13:4xZ by `0.9.0_WK_NFRA_CLDGRPH~1` on a VALID proof-of-spec instance (`python .tools/proof-of-spec-check.py <instance> D12-AC1..D12-AC7` rc 0) whose six MECHANICAL rows all read PASS by output and whose one judgment row (D12-AC7) is recorded UNVERIFIABLE-BY-INSTRUMENT for `3.0.0_SA_CVO` at L9. The grant is APPLIED (`Apply complete! Resources: 1 added, 0 changed, 0 destroyed`), READ LIVE (`allowed 1`, with `implicitDeny` on the write twin as the control) and EXERCISED (`buckets read=34 / buckets unreadable=0`, TRIGGERS 171 served with bd-allocation-processor / bd-gold-trigger / bd-silver-merge at vintage 2026-09-04T12:55:59Z, a vintage tied to this order's derive by matching snapshot ids). Ledger CLOSED, 5 of 5 legs. TWO rows filed and BOTH matter to the next seat: `NFRA_CLDGRPH-W1-S9` -- the AccountWideReadOnly statement is in item2a.tf, outside this order's <paths>, so the action landed at its own address in the granted iam.tf (same role, same effect, `1 to add` instead of `1 to change`); `NFRA_CLDGRPH-W1-S10` -- the served-graph instrument returned a FALSE ZERO for every WHERE-filtered cypher and was repaired in this order's two scripts, so D12-AC4 passes on a REPAIRED instrument and TO-CG-D-1's D1-AC5 reading of `triggers:0` measured the instrument, not the graph. Previously: pending -- GO = the COO handing this order to slot ~1 by CONTINUING the same subagent (spine v3 L7), on a fresh worktree from CLOUD carrying the drains @329f61c687 and @33f93a5215 and this recut. ROUND 4 of NFRA_CLDGRPH continued on the CTO's answer 94158 (@1ff1d53fb5 the row gate's merge read; @68f22f74f5 the halt gate admits a worker holding a NON-TERMINAL order): ONE ADDED CELL, CG-s-16, cut by the issuer as the round's recut (spine L10 -> L6); slot ~1's next order, handed BEFORE the reopened TO-CG-D-1 so D-1's pins exercise (D1-AC5) can meet its TRIGGERS bar. Marked HARD by the issuer (a live IAM grant on a production role; opus). The assignee commits its own status flip after a VALID proof-of-spec instance whose mechanical rows ALL read PASS (worker.md @1ff1d53fb5); a FAIL row leaves the order open as the final report; the L8 seat reads the record.</status>

**Directive:** D0 · **Fabric:** laptop · **PRD:** `org/missions/D0/NFRA/NFRA_CLDGRPH/prd/NFRA_CLDGRPH_PRD.md` v0.4 @`25c66d3358` (FWD-2, FWD-4) · **Decomp cell:** `CG-s-16` (decomposition v0.4, this recut; the cell text inlined below) · **Lane:** `infra/aws/terraform/globgrph/iam.tf` (the derive task role's inline policy), the change-management ledger + its sentinel · **Rule 27 seating:** `0.9.0_WK_NFRA_CLDGRPH~1`, a spine-v3 worker subagent of `2.0.0_SA_COO~A`.

---

## STANDING LAW (inlined; the worker face is your whole context)

- **Serial:** `0.9.0_WK_NFRA_CLDGRPH~1`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_NFRA_CLDGRPH~1;`. Commit only on your worktree branch via `bash .tools/safe-commit.sh --author "0.9.0_WK_NFRA_CLDGRPH~1 <0.9.0_WK_NFRA_CLDGRPH~1@opal.agent>" -F <msgfile> -- <files>`, `<msgfile>` written with the Write tool. Never push, merge, rebase, `checkout --` or `clean`. Push state is LOCAL and you say so.
- **Your write surface is exactly the PATHS block below plus `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/`.** A path you need that the block lacks is a BLOCKING row on that criterion, never an override.
- **Scratch:** `<your worktree>/.scratch/` only (worker.md @1ff1d53fb5; sibling workers share the parent session's scratchpad and overwrite each other there -- your own row W1-S6).
- **Surprise = ONE ROW, never a message.** Append to `org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md` a new `## <id> -- <title>` section with a fenced json array holding one object (the shape of your own W1 rows); id `NFRA_CLDGRPH-W1-S<k>`, `<k>` the next unused within W1 (W1-S1..S8 exist at HEAD; start at S9); restate the header denominator line; never edit an existing row; keep working.
- **Every criterion invocation runs under `timeout 120`**; rc 124 IS the recorded output, retried once at most. Deliverable steps that are not criterion invocations (the derive task wait, the chain wait) may use `timeout 600` and are polled with bounded reads.
- **THE HALT GATE NOW ADMITS YOU** (`.tools/halt-gate-check.sh` @68f22f74f5): a worker is a real principal while a NON-TERMINAL order under NFRA_CLDGRPH at HEAD is issued_to it, and the gate scans your ISSUER's inbox for a [STOP]. `bash .tools/safe-apply.sh` resolves for you now; if it still returns rc=3, that is a BLOCKING row quoting its whole output, never a retry with an escape.
- **NEVER:** `terraform apply` bare (use `bash .tools/safe-apply.sh` -- read its header first; targeted on exactly the address you name); widen the grant beyond `s3:GetBucketNotification` (no `s3:*`, no new managed policy, no other principal); write the marker, the pointer or any `projection/` object; delete any S3 object; touch a firm data bucket; an alarm/SNS/monitor; non-ASCII in code/logs/AWS; `2>/dev/null` a read whose emptiness carries a verdict; bare `git commit`.
- **NEVER-2 (deploy ledger) BINDS:** `python .tools/deploy_ledger.py open ...` BEFORE the apply with the complete leg manifest; **an IAM act NAMES ITS PRINCIPAL AND THE BUCKETS IT REACHES (34) in the entry** (the CTO's ruling, 94158); close every leg with proof; close the entry. The sentinel `org/critical_paths/.open_deploys/<slug>.json` is TRACKED and in your PATHS block: commit it with the entry.
- **Search rail:** `python .tools/comp-read <file> --for "..."` / `--enumerate '<regex>'`; `python .tools/comp-find '<pattern>' <pathspec>`; raw recursive grep/find in Bash is refused; a `cmd | grep` receiver is free. AWS CLI = `.tools/aws`. Region us-east-1, account 313476888478.

## THE CELL (decomposition v0.4, this recut, s.1a; added on the CTO's answer 94158 over your own row NFRA_CLDGRPH-W1-S7)

> **CG-s-16** | the derive task role `opal-globgrph-derive-runner-task` GRANTED `s3:GetBucketNotification` (the API that yields every S3_BUCKET-[TRIGGERS]->LAMBDA edge), in Terraform (`infra/aws/terraform/globgrph/iam.tf`, an inline statement beside the role's existing account-wide read grants), change-managed under NEVER-2 with the principal and the 34 buckets named; then ONE real derive on the rebuilt image | FWD-2, FWD-4 (acc 2, 4) | claim: measured (row W1-S7 @33f93a5215: the role holds GetBucketPolicy, GetBucketVersioning, GetBucketLocation, ListAllMyBuckets, GetObject, PutObject, DeleteObject, ListBucket and NOT GetBucketNotification -- absent from its four inline policies, no attached managed policy, absent from all 495 .tf files; the ad-hoc derive on the rebuilt image printed `buckets read=0 / buckets unreadable=34` and named all 34) | status: OPEN -- ROUND 4 (recut) | lane `0.7.0_AE_CloudOps` | placement laptop | depends_on: CG-s-15's image (DONE: `:latest` = sha256:1b89853f..., the fix's bytes) | **closes on:** the grant APPLIED and read live (`simulate-principal-policy`, ONE ARN per call, `allowed` with a matched statement); a real derive on the rebuilt image printing `buckets read=34 / unreadable=0`; the served projection at the post-derive vintage answering TRIGGERS > 0 with bd-pipeline's three Lambda targets present; the ledger CLOSED naming the principal and the 34 buckets. S20 and S28 DISARM on this proof (the CVO reads it at L9), never on the rebuild alone

## MEASURED BY THE ISSUER (and by you, in D-1), so you do not spend a discovery step on it

- **The role:** `opal-globgrph-derive-runner-task` (its ARN `arn:aws:iam::313476888478:role/opal-globgrph-derive-runner-task`); its inline policies live in `infra/aws/terraform/globgrph/iam.tf` -- your W1-S7 row names the `Sid AccountWideReadOnly` grants as the statement to extend (`comp-read infra/aws/terraform/globgrph/iam.tf --for "the derive runner task role's inline policy documents, the AccountWideReadOnly statement, and every s3: action it grants"`). Add `s3:GetBucketNotification` to THAT statement (resource `*`, matching the sibling read actions' scope) -- ONE action added, nothing else. If the statement carries a Condition, say so before applying: a conditioned grant reads `implicitDeny` on simulate with `MissingContext` (a FALSE deny) and the criterion below cannot grade it -- that is a row, not a workaround.
- **The apply set is ONE address:** `aws_iam_role_policy.<the resource that carries that document>` -- name it from the file; `safe-apply -target` on exactly it; expect `0 to add, 1 to change, 0 to destroy`. ONE unscoped `terraform plan` saved and asserted BY ADDRESS LIST to contain none of yours beyond the known foreign items (the same control as your D-1 run; the seven stale root outputs of W1-S3 are NFRA_GLOBGRPH's and are named, not touched).
- **The derive's run shape** (your D-1 record): family `globgrph-derive-runner` (still revision 6 on `:latest`, which is now the fix's image sha256:1b89853f... -- the pins are D-1's, after this order), subnet `local.subnet_id`, SG `sg-0f6cedf53107c6f8c`, public IP ENABLED; log group `/ecs/globgrph/derive-runner`. **Ad-hoc runs are PERMITTED FOR QA** (CLAUDE.md s.5): ONE ad-hoc `run-task` after the grant; the 02:00Z scheduled fire stays the acceptance the L9 seat reads later.
- **The chain and the read** (your D-1 record): the derive stamps the marker -> the Pipe launches the projection worker -> the pointer advances -> the serving service swaps; `triggers_query.sh` in your deliverables folder at HEAD (`org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/triggers_query.sh`) already sends the TRIGGERS query from the gateway host by SSM and prints the response whole -- reuse it; write a sibling `bd_targets_query.sh` for `MATCH (a:CloudNode)-[e:CloudEdge]->(b:CloudNode) WHERE e.edge_type='TRIGGERS' AND a.node_id CONTAINS 'opal-data-bd' RETURN b.node_id AS target ORDER BY target`.
- **The 34 buckets:** the derive's own log enumerates them (`unreadable=[...]` in your D-1 run); the ledger entry lists them by name as the buckets this grant reaches.

## DELIVERABLE -- in this order

1. **Open the ledger** (`cldgrph-cgs16-derive-role-bucket-notification`, author your serial) with FIVE legs and the principal + 34 buckets in its manifest: L1 activation = the Terraform edit committed on your branch; L2 activation = `safe-apply` targeted on the one address (`0 add / 1 change / 0 destroy` quoted) + the unscoped plan control by address list; L3 verify = the live read: `simulate-principal-policy` one ARN per call -> `allowed` with a matched statement, PLUS the negative control on the same principal for an action it must NOT hold (e.g. `s3:PutBucketNotification`) -> `implicitDeny`; L4 exercise = ONE ad-hoc derive on the rebuilt image exits 0 with `buckets read=34 / buckets unreadable=0` in its log; L5 verify = the served projection at the post-derive vintage answers TRIGGERS > 0 and the three bd-pipeline targets. Write the entry's path to `ledger_entry_d12.txt` and the derive's log group/stream to `derive_log_group_d12.txt` / `derive_log_stream_d12.txt` in your deliverables folder (the criteria read them).
2. **The edit:** one action in one statement; `terraform fmt -check`; the targeted plan saved; the apply through `safe-apply.sh`; the unscoped plan control.
3. **The live read + the negative control** (L3), one ARN per call, separate invocations.
4. **The derive** (L4) and the chain (L5): poll bounded (at most 30 x 30 s) until the pointer advances past the derive's start; then the two queries from the gateway host.
5. **The deliverable** `CG-s-16.derive-role-bucket-notification.result.md`: one fenced JSON block (the statement before/after, the address, the plan/apply lines, the two simulate results, the derive task ARN + exit + the denominator line, the post-derive vintage, the TRIGGERS count and the three targets, the 34 buckets) then prose. Close the ledger (5 of 5). Then the proof instance, validate, and -- ONLY if every mechanical row is PASS -- flip and commit (instance, deliverables, the ledger entry + its sentinel, the flip together).

## ACCEPTANCE (v3 grammar: one clause per criterion; every mechanical invocation bounded)

<criterion id="D12-AC1" cell_refs="CG-s-16"><invocation>.tools/aws iam simulate-principal-policy --policy-source-arn arn:aws:iam::313476888478:role/opal-globgrph-derive-runner-task --action-names s3:GetBucketNotification --resource-arns arn:aws:s3:::opal-data-bd --query 'EvaluationResults[0].[EvalDecision,length(MatchedStatements)]' --output text</invocation><expect>^allowed\s+[1-9]</expect></criterion>
`D12-AC1` -- THE GRANT IS APPLIED AND READ LIVE: `allowed` with at least one matched statement, one ARN per call (a batched multi-ARN simulate poisons verdicts; a conditioned grant would read implicitDeny -- if it does, the deliverable quotes `MissingContext` and this row is FAIL with a surprise row, never a re-read with a wider call).

<criterion id="D12-AC2" cell_refs="CG-s-16"><invocation>.tools/aws iam simulate-principal-policy --policy-source-arn arn:aws:iam::313476888478:role/opal-globgrph-derive-runner-task --action-names s3:PutBucketNotification --resource-arns arn:aws:s3:::opal-data-bd --query 'EvaluationResults[0].EvalDecision' --output text</invocation><expect>^implicitDeny$</expect></criterion>
`D12-AC2` -- THE NEGATIVE CONTROL: the WRITE twin of the granted action stays denied on the same principal and resource (the grant is one read action, not a widening).

<criterion id="D12-AC3" cell_refs="CG-s-16"><invocation>.tools/aws logs filter-log-events --log-group-name "$(cat org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/derive_log_group_d12.txt)" --log-stream-names "$(cat org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/derive_log_stream_d12.txt)" --filter-pattern "unreadable" --query 'events[].message' --output text</invocation><expect>buckets read=3[0-9] .*unreadable=0\b</expect></criterion>
`D12-AC3` -- THE CLOUD DERIVE READS EVERY BUCKET: `read=34 / unreadable=0` on the real principal (the number that was 0/34 in D-1).

<criterion id="D12-AC4" cell_refs="CG-s-16"><invocation>bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/triggers_query.sh</invocation><expect>"triggers":\s*[1-9][0-9]*</expect></criterion>
`D12-AC4` -- TRIGGERS NON-ZERO ON THE LIVE GRAPH at a vintage LATER than this order's derive start (both timestamps in the deliverable); S20's zero is gone.

<criterion id="D12-AC5" cell_refs="CG-s-16"><invocation>bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/bd_targets_query.sh</invocation><expect>bd-allocation-processor[\s\S]*bd-gold-trigger[\s\S]*bd-silver-merge</expect></criterion>
`D12-AC5` -- THE THREE DECLARED bd-pipeline TARGETS are present as TRIGGERS edges (CG-s-14's closes-on, met in the cloud).

<criterion id="D12-AC6" cell_refs="CG-s-16"><invocation>grep -c '^\*\*Status:\*\* CLOSED' "$(cat org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/ledger_entry_d12.txt)"</invocation><expect>^1$</expect></criterion>
`D12-AC6` -- THE LEDGER ENTRY CLOSED (read from the entry's own Status line -- `deploy_ledger.py list` cannot print CLOSED, your row W2-S5's sibling finding), naming the principal and the 34 buckets.

<criterion id="D12-AC7" cell_refs="CG-s-16" judgment="true"/> `D12-AC7` -- THE GRANT'S SCOPE READ: account-wide `s3:GetBucketNotification` on `*` beside the role's existing account-wide reads versus a 34-bucket enumeration -- which you chose, why, and the blast radius (the derive role only; no other principal moved). A reading act; NO verdict; graded by `3.0.0_SA_CVO` at L9.

<expected_criteria>D12-AC1, D12-AC2, D12-AC3, D12-AC4, D12-AC5, D12-AC6, D12-AC7</expected_criteria>

## SURFACES

`infra/aws/terraform/globgrph/iam.tf` (the ONE edit) · `infra/aws/terraform/globgrph/item2a.tf` (READ: the derive task's run shape) · `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/{CG-s-15.shared-image-digest-pins.result.md, triggers_query.sh, targeted_plan.txt}` (READ: your own D-1 record; the SSM query shape) · the W1-S7 row at HEAD (READ) · the ledger you open.

## BOUNDS

- **ONE action in ONE statement on ONE role.** No other IAM change, no managed policy, no other principal, no bucket policy.
- **`safe-apply` targeted on the one address; the unscoped plan is a control, never applied.**
- **One ad-hoc derive**; a non-zero exit is read, filed as a row, reported -- never retried blind. No pins (D-1's, after this order), no serving restart, no marker/pointer write, no S3 delete.
- A spec-vs-world divergence is a ROW. Certifier != author.

<paths>
infra/aws/terraform/globgrph/iam.tf
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D0/NFRA/NFRA_CLDGRPH/task-orders/NFRA_CLDGRPH.TO-CG-D-12.derive-role-bucket-notification-grant.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CLDGRPH/decompositions/NFRA_CLDGRPH_DECOMP.md</decomp_doc> v0.4 (this recut; v0.3.1 @7a3f99759f), cell CG-s-16 (s.1a; ADDED on the CTO's answer 94158 to the round-4 drain-end read 94157, over row NFRA_CLDGRPH-W1-S7 @33f93a5215).
<owned_cells>CG-s-16</owned_cells>
Read-dependencies, NOT claimed: CG-s-15 (the rebuilt image, DONE at the digest; its pins ride the reopened TO-CG-D-1 AFTER this order), CG-s-14 (DONE at source). Downstream, NOT yours: TO-CG-D-1's D1-AC5 (needs this grant), CG-x-2 (the night after this grant and the pins).
</decomp_ref>

<preflight>
comp-schedule: RUN -- 2026-09-04 06:2xZ at the round's cut: GATES ARMED 21 across 5 carriers (C1 21 -> 5, C2 4, C3 12, C4 20, C5 337); NEEDS-READ 138 prose fields (a reading list, never counted); at this recut two more ledgers are OPEN on this project (cgs15, cgd2 -- the reopened orders close them); the C3 moratoria bind this face's BOUNDS.
comp-iam: RUN -- the worker's own D-1 read (row W1-S7 @33f93a5215): opal-globgrph-derive-runner-task holds 8 s3 actions across four inline policies, no attached managed policy, GetBucketNotification absent from the role and from all 495 .tf files (positive control passing); comp-iam cannot answer "is this denied?" -- the APPLIED read is D12-AC1/AC2's own act, one ARN per call. Run `python .tools/comp-iam refresh-census` before any APPLIED census read (24 h TTL).
comp-adversary: DECLARED-NOT-APPLICABLE -- composed at L5 on the decomposition (rc 0 @07288006e5, 22/22 cited commits VERIFIED); the deliverable's validator context is the L9 seat's compose.
comp-denytest: DECLARED-NOT-APPLICABLE -- the change is a single ALLOW action on one role; the denial-side lens has no population (the negative control D12-AC2 is the live read).
</preflight>

<proof_of_spec>
Criterion ids minted at the recut by the issuer: `D12-AC1`..`D12-AC7`. The ASSIGNEE fills a `org/standards/PROOF_OF_SPEC.schema.json` instance at
`org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/NFRA_CLDGRPH.TO-CG-D-12.derive-role-bucket-notification-grant.proof_of_spec.json`
and validates it with `python .tools/proof-of-spec-check.py <instance> D12-AC1,D12-AC2,D12-AC3,D12-AC4,D12-AC5,D12-AC6,D12-AC7` BEFORE the complete flip; the flip requires rc 0 AND every mechanical row PASS (worker.md @1ff1d53fb5) -- a FAIL row leaves the order open and is your final report. `D12-AC2` (the denied twin), `D12-AC3` (unreadable=0) and `D12-AC4` (non-zero) are the controls that must be able to FAIL. `D12-AC7` is `judgment="true"`: recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; **`PASS` or `FAIL` on it is INVALID.**
</proof_of_spec>

<compiler_tools_mandate>
BEFORE EDIT: `python .tools/comp-read infra/aws/terraform/globgrph/iam.tf --for "the derive runner task role's inline policy documents, the AccountWideReadOnly statement, every s3: action it grants, and any Condition on it"`. BEFORE COMMIT: `terraform fmt -check infra/aws/terraform/globgrph/iam.tf`; no `.py` is edited by this order.
</compiler_tools_mandate>

**THE REPORT IS YOUR FINAL MESSAGE, ONCE, IN THE `WORKER REPORT` SHAPE.** You cannot send a message and nobody can send you one.

**GO = the hand-off (the COO continues this subagent on a fresh worktree from CLOUD).**
