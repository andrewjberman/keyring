# TO COMM_ASSIST.TO-CA-j-3 -- round 18 CA-j-3: deploy the ingress mark (the secret shell, its value out of band, then one targeted apply of module.ldo_001, pinned build, mode record)

<to_id>COMM_ASSIST.TO-CA-j-3</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.7.0_AE_CloudOps~CA</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>
<workstream>DEPLOY18</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-j-3` (`decompositions/COMM_ASSIST_DECOMP.round18.md`) | **outcome_ref:** FWD-7 |
**depends_on:** CA-j-1 (merged `0ca94ce0b6`), CA-j-2 (merged `38ce5a7981`); the GO waits on the CTO and CVO halves

---

## WORKER FACE

### GO

GO -- written by 2.0.0_SA_COO~CA 2026-10-14 ~04:4xZ. All three halves SIGNED on the pin `38ce5a7981`: COO (`NEVER_WIDEN_HALF_COO_COMM_ASSIST_R18_DEPLOY_20261014.md`, staged commit `41ef7071f7`), CTO (msg 109065, `1.0.0_SA_CTO/NEVER_WIDEN_HALF_CTO_COMM_ASSIST_R18_DEPLOY_20261014.md` @fa9ad4302e), CVO (`3.0.0_SA_CVO~L/NEVER_WIDEN_HALF_CVO_COMM_ASSIST_R18_DEPLOY_20261014.md` @29f8d9d49f).
The CTO's conditions bind: the secret value exists only in Secrets Manager (any appearance in a plan, log, ledger or message is a P1 BLOCKING row and an immediate rotation); step 3 runs only after `describe-secret` shows an `AWSCURRENT` version; after step 3 `check_j3_live.py` reads PASS and the ingress logs show `ingress_poll` and the mail step `polled` within 10 minutes, else roll back at once and file a BLOCKING row; `record` is the only mode this pair covers; never 20:00Z-21:45Z and no End of Day event in flight.
The CVO's half adds a watch, not a wait: the `ingress_poll` line does not show the text path, so the ISSUER reads Andrew's first real text after step 3 in the ingress log (routed, no secret error) and rolls back on a failure; you send no text to produce it. The CVO's carried limits (a Dell identity can read the key; a text more than 15 minutes old) are for the enforce pair CA-j-5 and are not grounds here.

The three halves BIND, and the COO half's Branch A / Branch B, rollback and conditions ARE the procedure. Read all three in full (all under `org/missions/D9/COMM/COMM_ASSIST/deliverables/`):
- COO `2.0.0_SA_COO~CA/NEVER_WIDEN_HALF_COO_COMM_ASSIST_R18_DEPLOY_20261014.md`
- CTO `1.0.0_SA_CTO/NEVER_WIDEN_HALF_CTO_COMM_ASSIST_R18_DEPLOY_20261014.md`
- CVO `3.0.0_SA_CVO~L/NEVER_WIDEN_HALF_CVO_COMM_ASSIST_R18_DEPLOY_20261014.md`

### THE CELL

`CA-j-3`. The same two Lambdas as your last order (`CA-i-14`, ledger `comm-assist-r17c-deploy`, CLOSED), now on `sWltfUwyJQpANEhbY+KFkszo8ScLKEIi7Lm4qyUNWrM=`. The trunk carries the ingress mark on top of that package (cell `CA-j-1`: `ingress_mark.py`, the producers in `tenant.py`, the `NAMES.json` row) and the Terraform for its secret shell, its read grant and `INGRESS_MARK_MODE` defaulting to `record` (cell `CA-j-2`). This cell ships them in three steps so no function ever runs the new code while the secret has no value.

### DO, IN THIS ORDER (the laptop, from the shared trunk at or after this order's GO)

1. `git worktree add --detach <scratch> 38ce5a7981` (outside every other worktree). Every build, test, init, plan, apply and re-plan below runs FROM that pinned worktree. Confirm `git -C <scratch> status --porcelain` is empty.
2. Open the ledger `comm-assist-r18-deploy` (`python .tools/deploy_ledger.py open ...` from the shared trunk), naming both functions and the secret. Commit the entry AND the sentinel BEFORE the first apply.
3. BEFORE reads, saved in your deliverables folder `org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/`: both functions' `CodeSha256` and `LastModified`; both functions' environment KEY NAMES (never values); the live zip with its sha256; `describe-secret` for `teams/global/ingress-mark` (expect not found).
   If the live hash is not `sWltf...`, or the secret exists, that is Branch B: another writer moved something. Stop and report.
4. Build in the pinned worktree: `bash infra/aws/lambda/teams-chat-assist/build.sh`. Run the import test on `infra/aws/lambda/teams-chat-assist/dist/pkg`. Record the built zip's base64 sha256. Then run AC1 below (`J3_PIN=38ce5a7981`): it must read `ok=True` BEFORE any apply.
5. `TF_DATA_DIR` = a NEW scratch directory outside every git tree. `init -input=false` against the declared backend; a migrate or reconfigure prompt means STOP.
6. **Step 1, the shell:** a saved, locked plan `-target=aws_secretsmanager_secret.ca_ingress_mark`, NO `-var`. Branch A exactly (`1 to add, 0 to change, 0 to destroy`, that one address) -> apply the saved plan through `bash .tools/safe-apply.sh`. Anything else -> Branch B: apply nothing, close the ledger as not-applied, report.
7. **Step 2, the value:** generate 32 random bytes as hex into a file OUTSIDE every git tree (for example `python -c "import secrets; open(PATH,'w').write(secrets.token_hex(32))"` run so the value is never printed), `aws secretsmanager put-secret-value --secret-id teams/global/ingress-mark --secret-string file://PATH`, delete the file, then `describe-secret` must show an `AWSCURRENT` version. Never read the value back; never print, log, commit or send it.
8. **Step 3, the code, the mode and the grant:** a saved, locked, targeted plan `-target=module.ldo_001`, NO `-var`. Branch A exactly (`0 to add, 3 to change, 0 to destroy`: handler, `ingress[0]`, `aws_iam_policy.exec`; environment differing only by the added `INGRESS_MARK_MODE = "record"`; the policy differing only by the new secret ARN; the after-hash equal to step 4's) -> apply that saved plan through `bash .tools/safe-apply.sh`. Anything else -> Branch B: apply nothing more, report (the shell and its value stay; nothing reads them).
9. Never between 20:00Z and 21:45Z.
10. AFTER: run AC2 below, then a targeted re-plan of `module.ldo_001` (expect no changes). Read log lines only, never message content. Ten minutes on, the ingress log still shows `ingress_poll` and the mail step `polled`.
11. Rollback on any AFTER failure: the COO half's rollback. File an ARMED row naming `2.0.0_SA_COO~CA`, and report.
12. Close the ledger and commit. Remove the pinned worktree. Send no test mail, text nobody and invoke nothing.

### RULES FOR THIS CELL

- Two targeted applies, in the order above: the secret shell, then `module.ldo_001`. Never untargeted, never bare `terraform`, never `aws lambda update-function-code`.
- No `-var`. No edit to any `.tf` or code file. Never push, `git stash`, rebase, `checkout --`, `clean`.
- The secret value is never visible anywhere (file, log, message, commit, ledger, plan, proof instance).
- No non-ASCII. `dist/` is never committed.
- Refuse a criterion you cannot satisfy as written. File a BLOCKING row with the measurement and stop; do not widen.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAj3-AC1" cell_refs="CA-j-3"><invocation>J3_PIN=38ce5a7981 python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r18/checks/check_j3_equiv.py"</invocation><expect>J3-EQUIV ok=True</expect></criterion>
`CAj3-AC1` -- the issuer's pre-flight check (read it; do not edit it), run BEFORE the apply with the pinned worktree built: the packaged-path diff from the deployed pin `abc5ad424a` carries the four round-18 files, the built `ingress_mark.py`, `tenant.py` and `NAMES.json` equal the pin's bytes, and the built package forms the same S3 addresses and considers the same mail parties as the package the live function serves (17 probes; one foreign registry file rides the package and is read there). It reads ok=False until the build exists.

<criterion id="CAj3-AC2" cell_refs="CA-j-3"><invocation>J3_PIN=38ce5a7981 python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r18/checks/check_j3_live.py"</invocation><expect>RESULT: PASS</expect></criterion>
`CAj3-AC2` -- the issuer's live check (read it; do not edit it). Both functions are on one new package, not `sWltf...`; the served zip hashes to it and its six files equal the pin's; both environments carry `INGRESS_MARK_MODE=record` and the other keys as recorded; the secret has a current version (value never read) and both roles may read it; the served code round-trips a mark, refuses a tampered one and parses the three modes. It FAILs at the base.

<criterion id="CAj3-AC3" cell_refs="CA-j-3"><invocation>bash "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r18/checks/check_j3_ledger.sh"</invocation><expect>RESULT: PASS</expect></criterion>
`CAj3-AC3` -- NEVER-2: the ledger `comm-assist-r18-deploy` is committed CLOSED at HEAD and its sentinel is gone. It FAILs at the base.
</proof_of_spec>

<expected_criteria>CAj3-AC1,CAj3-AC2,CAj3-AC3</expected_criteria>

Each invocation runs under `timeout 120`. Write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/COMM_ASSIST.TO-CA-j-3.ingress-mark-deploy.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> CAj3-AC1,CAj3-AC2,CAj3-AC3`, and flip `<status>` to `complete` only when all three PASS and the instance is VALID. Surprise rows are
`COMM_ASSIST-C18-S<k>`, fabric `laptop`, disarm_owner `2.0.0_SA_COO~CA`, `surfaced_at` = `date -u +%FT%TZ` at filing. Append lines only to the investigation file.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round18.md</decomp_doc>
<owned_cells>CA-j-3</owned_cells>
</decomp_ref>

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/comm-assist-r18-deploy.json
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-j-3.ingress-mark-deploy.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the act creates no schedule; the ingress keeps its 1-minute clock (module.ldo_001) and the End of Day window 20:00Z-21:45Z is a Branch B stop. No cron, alarm, monitor or notification is created.
comp-iam: RUN -- the one policy change is the module's `aws_iam_policy.exec` `Secrets` statement gaining the new secret's ARN (a read of ONE secret, `secretsmanager:GetSecretValue`, for the two functions' shared execution role); any other policy address, action or resource in the plan is Branch B. BLIND: the live grant is read by AC2's simulation per role, not predicted from the plan.
comp-adversary: RUN -- a second writer (NFRA_CTLPLN also deploys this module) moving the live hash before the act (step 3 -> Branch B); a package built from the moving trunk (pinned worktree, step 1); a foreign file riding the package (AC1 counts it and compares the S3 addresses and mail parties on both packages); the new code running before the secret has a value (the three steps put the value before the code); the secret value leaking into a file, log, plan or commit (condition 4; the generating file is deleted); the mode arriving as `enforce` (the plan pins `record` and AC2 reads it); an environment change other than the one key slipping into the plan (Branch B). BLIND: a real text from Andrew's phone through the ingress is the issuer's real run at close, not this seat's.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Base `38ce5a7981`: CAj3-AC1 base: PASS as measured only after the build exists (the issuer's own pre-flight build read `J3-EQUIV ok=True files=3 foreign=1 probes=17 same=17`); it reads ok=False until a detached worktree at the pin is built. CAj3-AC2 base: FAIL as measured (pre-state hash, secret not found, no `INGRESS_MARK_MODE`). CAj3-AC3 base: FAIL as expected (0 entries).
Source: CTO round-17 analysis item 1 and ruling `CTO_RULING_20261013_231xZ_COMM_ASSIST_SMS_FORGERY_AND_J290_DRAFTS.md`; COO half `NEVER_WIDEN_HALF_COO_COMM_ASSIST_R18_DEPLOY_20261014.md`; ledger precedent `comm-assist-r17c-deploy`.
