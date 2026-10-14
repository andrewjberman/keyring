# TO COMM_ASSIST.TO-CA-j-8 -- round 18 CA-j-8: apply the resource policy that narrows the ingress-mark key (one targeted apply of aws_secretsmanager_secret_policy.ca_ingress_mark, no code)

<to_id>COMM_ASSIST.TO-CA-j-8</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.7.0_AE_CloudOps~CA</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>
<workstream>DEPLOY18KEY</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-j-8` (`decompositions/COMM_ASSIST_DECOMP.round18.md`, AMENDMENT 4) | **outcome_ref:** FWD-7 |
**depends_on:** CA-j-7 (merged `3af44d523b`), CA-j-3 (CLOSED @1daa4a97ce); the GO waits on the CTO and CVO halves

---

## WORKER FACE

### GO

GO -- written by 2.0.0_SA_COO~CA 2026-10-14 ~06:2xZ. All three halves SIGNED on the pin `3af44d523b`: COO (`NEVER_WIDEN_HALF_COO_COMM_ASSIST_R18B_KEY_DEPLOY_20261014.md`, staged commit `5346d2c2dd`), CTO (msg 109079, `1.0.0_SA_CTO/NEVER_WIDEN_HALF_CTO_COMM_ASSIST_R18B_KEY_DEPLOY_20261014.md` @9238cbd54c), CVO (`3.0.0_SA_CVO~L/NEVER_WIDEN_HALF_CVO_COMM_ASSIST_R18B_KEY_DEPLOY_20261014.md` @fc5530b470).
The CTO's conditions bind: after the apply, simulate `GetSecretValue` as `allowed` for `teams-global-chat-assist-role` and `explicitDeny` for both Dell agent users; within 10 minutes the ingress logs show `ingress_poll` and no `AccessDenied` for the function role on the mark secret (a `marks_seen` count advancing on a real text is the stronger proof and is the issuer's watch, not yours); ANY `AccessDenied` for the role means remove the policy at once (the Terraform destroy of the COO half's rollback, never a direct `delete-resource-policy`) and file a BLOCKING row; the mode stays `record`; never 20:00Z-21:45Z and no End of Day event in flight. The CTO half's rollback line also names a direct delete; THIS order and the COO and CVO halves allow only the Terraform destroy, and that is the procedure.
The CVO half adds nothing to the procedure: the carried limit (a text more than 15 minutes after its mark) is for the enforce pair CA-j-5.

The three halves BIND, and the COO half's Branch A / Branch B, rollback and conditions ARE the procedure. Read all three in full (all under `org/missions/D9/COMM/COMM_ASSIST/deliverables/`):
- COO `2.0.0_SA_COO~CA/NEVER_WIDEN_HALF_COO_COMM_ASSIST_R18B_KEY_DEPLOY_20261014.md`
- CTO `1.0.0_SA_CTO/NEVER_WIDEN_HALF_CTO_COMM_ASSIST_R18B_KEY_DEPLOY_20261014.md`
- CVO `3.0.0_SA_CVO~L/NEVER_WIDEN_HALF_CVO_COMM_ASSIST_R18B_KEY_DEPLOY_20261014.md`

### THE CELL

`CA-j-8`. The same two Lambdas as your last order (`CA-j-3`, ledger `comm-assist-r18-deploy`, CLOSED), now on `nX67q2k05fh77lG2gBLsNlp6HLAZeELPq85CJpWCVhA=` with the ingress mark live in `record` mode. The trunk now carries ONE Terraform resource more (cell `CA-j-7`): a resource policy on the mark's secret `teams/global/ingress-mark` that denies `GetSecretValue` to every principal except the assistant's execution role. This cell applies exactly that. No code, no package, no environment value, no identity policy moves.

### DO, IN THIS ORDER (the laptop, from the shared trunk at or after this order's GO)

1. `git worktree add --detach <scratch> 3af44d523b` (outside every other worktree). Every init, plan, apply and re-plan below runs FROM that pinned worktree. Confirm `git -C <scratch> status --porcelain` is empty. No build is needed (no code moves).
2. Open the ledger `comm-assist-r18-key-deploy` (`python .tools/deploy_ledger.py open ...` from the shared trunk), naming the policy resource and both functions. Commit the entry AND the sentinel BEFORE the apply.
3. BEFORE reads, saved in your deliverables folder `org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/r18b/`: both functions' `CodeSha256`, `LastModified` and environment KEY NAMES (never values); `get-resource-policy teams/global/ingress-mark` (expect no `ResourcePolicy`); `describe-secret` (expect a current version; never read the value).
   If the code hash is not `nX67q...`, the mode is not `record`, or a resource policy already exists, that is Branch B: another writer moved something. Stop and report.
4. BEFORE simulation: write the PLAN's policy text (the single Deny statement of the COO half) to a scratch file and run `aws iam simulate-principal-policy --resource-policy file://...` for the execution role (the function's `Role`) and `cloudops-dell1-agent-user` and `cloudops-dell2-agent-user`, action `secretsmanager:GetSecretValue`, resource the secret's ARN. The role must read `allowed` and both Dell users `explicitDeny`; any other read is Branch B.
5. `TF_DATA_DIR` = a NEW scratch directory outside every git tree. `init -input=false` against the declared backend; a migrate or reconfigure prompt means STOP. Take a saved, locked, targeted plan `-target=aws_secretsmanager_secret_policy.ca_ingress_mark`, with NO `-var`.
   - Branch A exactly -> apply that saved plan through `bash .tools/safe-apply.sh`. Branch A is `1 to add, 0 to change, 0 to destroy`: that one address and its single Deny statement, nothing else.
   - Anything else -> Branch B: apply nothing, close the ledger as not-applied, report.
   - Never between 20:00Z and 21:45Z.
6. AFTER: run the criteria below, then a targeted re-plan (expect no changes). Read log lines only, never message content or the secret's value. Ten minutes on, the ingress log still shows `ingress_poll` and the mail step `polled`, and neither function log shows `AccessDenied` for the mark secret.
7. Rollback on any AFTER failure: the COO half's rollback (a targeted destroy of that one resource through Terraform, never a direct `delete-resource-policy`). File an ARMED row naming `2.0.0_SA_COO~CA`, and report.
8. Close the ledger and commit. Remove the pinned worktree. Send no test mail, text nobody and invoke nothing.

### RULES FOR THIS CELL

- One targeted apply, `aws_secretsmanager_secret_policy.ca_ingress_mark` only. Never untargeted, never bare `terraform`, never `aws lambda update-function-code`, never a direct `put-resource-policy`.
- No `-var`. No edit to any `.tf` or code file. Never push, `git stash`, rebase, `checkout --`, `clean`.
- The secret's value is never read, printed, logged, committed or sent.
- No non-ASCII.
- Refuse a criterion you cannot satisfy as written. File a BLOCKING row with the measurement and stop; do not widen.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAj8-AC1" cell_refs="CA-j-8"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r18/checks/check_j8_live.py"</invocation><expect>RESULT: PASS</expect></criterion>
`CAj8-AC1` -- the issuer's live check (read it; do not edit it). The secret's resource policy has exactly one statement (Deny, `*`, `GetSecretValue`, exception for the execution role only); simulated against the LIVE policy the execution role is `allowed` and both Dell users `explicitDeny`; management acts (`PutSecretValue`, `DescribeSecret`, `PutResourcePolicy`) stay open to them; the code hash, the mode `record` and the secret's current version did not move. It FAILs at the base (no policy).

<criterion id="CAj8-AC2" cell_refs="CA-j-8"><invocation>bash "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r18/checks/check_j8_ledger.sh"</invocation><expect>RESULT: PASS</expect></criterion>
`CAj8-AC2` -- NEVER-2: the ledger `comm-assist-r18-key-deploy` is committed CLOSED at HEAD and its sentinel is gone. It FAILs at the base.
</proof_of_spec>

<expected_criteria>CAj8-AC1,CAj8-AC2</expected_criteria>

Each invocation runs under `timeout 120`. Write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/COMM_ASSIST.TO-CA-j-8.ingress-mark-key-policy-deploy.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> CAj8-AC1,CAj8-AC2` AFTER your last commit, and flip `<status>` to `complete` only when both PASS and the instance is VALID at the final head. Surprise rows are
`COMM_ASSIST-C18K-S<k>`, fabric `laptop`, disarm_owner `2.0.0_SA_COO~CA`, `surfaced_at` = `date -u +%FT%TZ` at filing. Append lines only to the investigation file.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round18.md</decomp_doc>
<owned_cells>CA-j-8</owned_cells>
</decomp_ref>

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/comm-assist-r18-key-deploy.json
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-j-8.ingress-mark-key-policy-deploy.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the act creates no schedule; the ingress keeps its 1-minute clock and the End of Day window 20:00Z-21:45Z is a Branch B stop. No cron, alarm, monitor or notification is created.
comp-iam: RUN -- the one policy moved is a RESOURCE policy on ONE secret that only DENIES the value read to every principal except the execution role; it grants nothing and no identity policy moves (any iam address in the plan is Branch B). Measured by the issuer with `simulate-principal-policy` and this exact policy supplied (denominator: 3 principals): execution role `allowed`, `cloudops-dell1-agent-user` and `cloudops-dell2-agent-user` `explicitDeny`; management acts allowed for both Dell users. BLIND: the live evaluation by the real functions on a cold container is read only by the first real text (the issuer's watch), not by a simulation.
comp-adversary: RUN -- the policy locking out the assistant itself (refused: the exception is the live function Role; step 4 and AC1 simulate it `allowed`); a second writer (NFRA_CTLPLN also deploys the ldo module) moving the code or mode before the act (step 3 -> Branch B); a plan that touches more than the one address (Branch B); a direct put-resource-policy that leaves Terraform state wrong (forbidden by RULES; rollback is a Terraform destroy); the secret's value read to verify (forbidden; AC1 reads the policy and simulates). BLIND: an administrator can still rewrite the policy (a recorded management write; the residual stated in the COO half and the PRD addendum).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Base `3af44d523b`: CAj8-AC1 base: FAIL as measured (no resource policy; the code, mode and version checks read true). With the intended policy text supplied in place of the live read, the check's real simulations read PASS (role allowed, both Dell users explicitDeny, management allowed). CAj8-AC2 base: FAIL as expected (0 entries).
Source: CTO ruling `CTO_RULING_20261014_052xZ_COMM_ASSIST_INGRESS_MARK_KEY_NARROWED.md` (msg 109075); CVO half of CA-j-3 (AMENDMENT 3); COO half `NEVER_WIDEN_HALF_COO_COMM_ASSIST_R18B_KEY_DEPLOY_20261014.md`; ledger precedent `comm-assist-r18-deploy`.
