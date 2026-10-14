# TO COMM_ASSIST.TO-CA-i-4 -- round 17 CA-i-4: deploy the round-17 package (one targeted apply of module.ldo_001: code and one environment value, pinned build)

<to_id>COMM_ASSIST.TO-CA-i-4</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.7.0_AE_CloudOps~CA</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>17</round>
<workstream>DEPLOY17</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-i-4` (`decompositions/COMM_ASSIST_DECOMP.round17.md`) | **outcome_ref:** FWD-7, FWD-8, FWD-4 |
**depends_on:** CA-i-2, CA-i-6, CA-i-7, CA-i-8, CA-i-9 (all merged, pin `b19849b51c`); the GO waits on the CTO and CVO halves

---

## WORKER FACE

### GO

The issuer flips `<status>` to `pending` and writes `GO` on the line below once all three halves are SIGNED on the pin. Until then, do nothing.

GO -- written by 2.0.0_SA_COO~CA 2026-10-14 ~00:1xZ. All three halves SIGNED on the pin `b19849b51c`: COO (`NEVER_WIDEN_HALF_COO_COMM_ASSIST_R17_DEPLOY_20261014.md`, issuance commit `e93a7913ee`), CTO `d7cd346166`, CVO `d2c7360c00`. The CTO's conditions bind: pre-state still `nIQW...` at the act; `check_i4_equiv` `ok=True` re-run on the package being uploaded; after the act `check_i4_live` PASS plus `ingress_poll`/`polled` within 10 minutes, else roll back and file a BLOCKING row; never 20:00Z-21:45Z. The CVO half's carried point binds on the NEXT act, not this one: a signed answer can be replayed (row `COMM_ASSIST-C-S5`, ARMED, disarm owner the issuer); nothing here installs a forwarder. The halves BIND, and the COO half's Branch A / Branch B, rollback and conditions ARE the procedure. Read all three in full (all under `org/missions/D9/COMM/COMM_ASSIST/`):
- COO `deliverables/2.0.0_SA_COO~CA/NEVER_WIDEN_HALF_COO_COMM_ASSIST_R17_DEPLOY_20261014.md`
- CTO `deliverables/1.0.0_SA_CTO/NEVER_WIDEN_HALF_CTO_COMM_ASSIST_R17_DEPLOY_20261014.md`
- CVO `deliverables/3.0.0_SA_CVO~L/NEVER_WIDEN_HALF_CVO_COMM_ASSIST_R17_DEPLOY_20261014.md`

### THE CELL

`CA-i-4`. Andrew's Teams assistant is two Lambdas from `module "ldo_001"` in `infra/aws/terraform/transcripts/chat_assist.tf`: `teams-global-chat-assist-handler-lambda` and
`teams-global-chat-assist-ingress-lambda` (us-east-1). Both run the package `nIQW+3XvvaFNJQfwX5lrI99XSexESb68Pd1uLldlTgI=` (deployed 2026-10-11 ~02:17Z, pin `2fd32e12c2`, entry
`comm-assist-r14-deploy`). The trunk carries COMM round 17 on top of it: the receiver that verifies muse's signed answers, the agent-bus sender stamp, the mail-draft loop, and one
Terraform variable that sets `MUSE_ANSWER_PUBKEY` (muse's public key). This cell ships exactly that: code and that one environment value.

### DO, IN THIS ORDER (the laptop, from the shared trunk at or after this order's issuance commit)

1. `git worktree add --detach <scratch> b19849b51c` (outside every other worktree). Every build, test, init, plan, apply and re-plan below runs FROM that pinned worktree. Confirm
   `git -C <scratch> status --porcelain` is empty.
2. Open the ledger `comm-assist-r17-deploy` (`python .tools/deploy_ledger.py open ...` from the shared trunk), naming both functions. Commit the entry AND the sentinel BEFORE the act.
3. BEFORE reads, saved in your deliverables folder `org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/`: both functions' `CodeSha256` and `LastModified`; both functions'
   environment KEY NAMES (never values); the live zip (`get-function` -> `Code.Location`) with its sha256. If the live hash is not `nIQW...`, that is Branch B: another writer moved it. Stop and report.
4. Build in the pinned worktree: `bash infra/aws/lambda/transcripts-pull/build.sh` and `bash infra/aws/lambda/teams-chat-assist/build.sh` (the root does not load without both zips; building uploads
   nothing). Run the import test on `infra/aws/lambda/teams-chat-assist/dist/pkg`. Record the built zip's base64 sha256. Then run AC1 below: it must read `ok=True` BEFORE any apply.
5. `TF_DATA_DIR` = a NEW scratch directory outside every git tree. `init -input=false` against the declared backend; a migrate or reconfigure prompt means STOP. Take a saved, locked, targeted plan
   `-target=module.ldo_001`, with NO `-var` (the required root variable is supplied by the committed `readers.auto.tfvars`).
   - Branch A exactly -> apply that saved plan through `bash .tools/safe-apply.sh`. Branch A is `0 to add, 2 to change, 0 to destroy`: the handler and `ingress[0]` only, changed keys within
     {`source_code_hash`, `last_modified`, `environment`}, the `environment` diff EXACTLY one added key `MUSE_ANSWER_PUBKEY` with every existing key unchanged, and the after-hash equal to step 4's.
   - Anything else -> Branch B: apply nothing, close the ledger as not-applied, report.
   - Never between 20:00Z and 21:45Z.
6. AFTER: run the criteria below, then a targeted re-plan (expect no changes). Read log lines only, never message content. Ten minutes on, the ingress log still shows `ingress_poll` and the mail step `polled`.
7. Rollback on any AFTER failure: the COO half's rollback (the saved zip over `dist/`, then the same targeted apply with `-var chat_assist_muse_answer_pubkey=` as the one permitted `-var`). File an ARMED row
   naming `2.0.0_SA_COO~CA`, and report.
8. Close the ledger and commit. Remove the pinned worktree. Send no test mail, text nobody and invoke nothing.

### RULES FOR THIS CELL

- One targeted apply, `module.ldo_001` only. Never untargeted, never bare `terraform`, never `aws lambda update-function-code`.
- No `-var` except the rollback's one. No edit to any `.tf` or code file. Never push, `git stash`, rebase, `checkout --`, `clean`.
- No non-ASCII. `dist/` is never committed.
- Refuse a criterion you cannot satisfy as written. File a BLOCKING row with the measurement and stop; do not widen.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAi4-AC1" cell_refs="CA-i-4"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i4_equiv.py"</invocation><expect>I4-EQUIV ok=True</expect></criterion>
`CAi4-AC1` -- the issuer's pre-flight check (read it; do not edit it), run BEFORE the apply with the pinned worktree built: the four round-17 files in the built package equal the pin's bytes, and the built package forms the same S3 addresses and considers the same mail parties as the package the live function serves (17 probes). It reads ok=False until the build exists.

<criterion id="CAi4-AC2" cell_refs="CA-i-4"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i4_live.py"</invocation><expect>RESULT: PASS</expect></criterion>
`CAi4-AC2` -- the issuer's live check (read it; do not edit it). Both functions are on one new package, not `nIQW...`. The served zip hashes to it and its four round-17 files equal the pin's. Both environments carry muse's key (fingerprint as recorded) with the mail secret and the SMS origination unchanged. The served code routes `muse.reply`, accepts a real signature, refuses another key and stamps `ldo-001`. It FAILs at the base.

<criterion id="CAi4-AC3" cell_refs="CA-i-4"><invocation>bash "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i4_ledger.sh"</invocation><expect>RESULT: PASS</expect></criterion>
`CAi4-AC3` -- NEVER-2: the ledger `comm-assist-r17-deploy` is committed CLOSED at HEAD and its sentinel is gone. It FAILs at the base.
</proof_of_spec>

<expected_criteria>CAi4-AC1,CAi4-AC2,CAi4-AC3</expected_criteria>

Each invocation runs under `timeout 120`. Write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/COMM_ASSIST.TO-CA-i-4.round17-package-deploy.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> CAi4-AC1,CAi4-AC2,CAi4-AC3`, and flip `<status>` to `complete` only when all three PASS and the instance is VALID. Surprise rows are
`COMM_ASSIST-C4-S<k>`, fabric `laptop`, disarm_owner `2.0.0_SA_COO~CA`, `surfaced_at` = `date -u +%FT%TZ` at filing. Append lines only to the investigation file.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round17.md</decomp_doc>
<owned_cells>CA-i-4</owned_cells>
</decomp_ref>

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/comm-assist-r17-deploy.json
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-i-4.round17-package-deploy.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the act creates no schedule; the ingress keeps its 1-minute clock (module.ldo_001) and the End of Day window 20:00Z-21:45Z is a Branch B stop. No cron, alarm, monitor or notification is created.
comp-iam: DECLARED-NOT-APPLICABLE no policy moves: Branch A is the code hash and one environment key, and any iam address in the plan is Branch B. The assistant policy (teams-global-chat-assist-policy) is not read or changed by this act.
comp-adversary: RUN -- a second writer (NFRA_CTLPLN also deploys this module) moving the live hash before the act (step 3 -> Branch B); a package built from the moving trunk (pinned worktree, step 1); foreign files riding the package (lib/opal_naming.py and eight registry files; AC1 reads them where they act, because the plan cannot); a key pinned that is not muse's (AC2 compares the fingerprint to the record); a changed mail secret or origination (AC2 pins both); message content entering an artifact (log lines only). BLIND: whether muse can reach the new receiver end to end is cell CA-i-5 and the FWD-7 grade, not this act; a muse answer is refused until the forwarder is installed.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Base `b19849b51c`: CAi4-AC1 base: FAIL as expected (no built package at the pin; the stale main-tree package carries the pre-round-17 files). CAi4-AC2 base: FAIL as expected (pre-state hash; the served code has no muse_verify; no MUSE_ANSWER_PUBKEY). CAi4-AC3 base: FAIL as expected (0 entries). AC1 green arm: PASS as measured (17 of 17) on the issuer's real pre-flight build of the pin; AC2's probe green on that same build (route, accept, refuse, stamp).
Source: COO half `NEVER_WIDEN_HALF_COO_COMM_ASSIST_R17_DEPLOY_20261014.md`; CTO round-16 analysis @6e9e2fc1ff; ledger precedent `comm-assist-r14-deploy` (CA-f-1).
