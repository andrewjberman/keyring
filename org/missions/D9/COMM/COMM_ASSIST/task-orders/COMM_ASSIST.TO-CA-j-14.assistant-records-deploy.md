# TO COMM_ASSIST.TO-CA-j-14 -- round 18 CA-j-14: deploy the assistant's mention record and mail log (one targeted apply of module.ldo_001, code only, pinned build)

<to_id>COMM_ASSIST.TO-CA-j-14</to_id>
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
<workstream>DEPLOY18REC</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-j-14` (`decompositions/COMM_ASSIST_DECOMP.round18.md`, AMENDMENT 8) | **outcome_ref:** FWD-13 |
**depends_on:** CA-j-12 (merged `ca76b8b225`), CA-j-5 (CLOSED @4dddae3aad), CA-j-17 (merged `0774100edc`); the GO waits on the CTO and CVO halves

---

## WORKER FACE

### GO

GO -- written by 2.0.0_SA_COO~CA 2026-10-14 ~15:4xZ. All three halves SIGNED on the pin `0774100edc`: COO (`NEVER_WIDEN_HALF_COO_COMM_ASSIST_R18E_RECORDS_DEPLOY_20261014.md`, staged commit `00cf6e5d86`), CTO (msg 109185, `1.0.0_SA_CTO/NEVER_WIDEN_HALF_CTO_COMM_ASSIST_R18E_RECORDS_DEPLOY_20261014.md` @82225b0fd9), CVO (`3.0.0_SA_CVO~L/NEVER_WIDEN_HALF_CVO_COMM_ASSIST_R18E_RECORDS_DEPLOY_20261014.md` @9395758c08).
The CTO's conditions bind: C1 this deploy lands BEFORE the first End of Day run under `enforce`, so the issuer attributes any End of Day failure by kind (a mark refusal belongs to the enforce flip; an exception or dead letter from the mention or mail writer belongs to this deploy; each rolls back ALONE, and this deploy rolls back from `8c5e0b278e` with the mode staying `enforce`); C2 your AFTER reads include the dead-letter queue `teams-global-chat-assist-dlq.fifo`: its `ApproximateNumberOfMessages` and `ApproximateNumberOfMessagesNotVisible` must read UNCHANGED from your BEFORE read (the issuer read 0 and 0 at ~15:3xZ; save yours in `r18e/` before and after); C3 the foreign registry row (`event_rules.json`, +6, from `4.0.0_SA_CRO~DELL1`) rides as counted: `check_k3_equiv`'s 17 of 17 probes are its proof, and you do not trim it.
The CVO's carried item is for the dell2 cell (CA-j-15), not for you. Timing: apply BEFORE 19:30Z, so it lands ahead of the End of Day window (20:00Z-21:45Z); if you cannot, do not apply until the window has closed and report. Rollback is a targeted apply from a detached worktree at `8c5e0b278e`, NEVER from `afa8752f44` (its default is `record`).

The three halves BIND, and the COO half's Branch A / Branch B, rollback and conditions ARE the procedure. Read all three in full (all under `org/missions/D9/COMM/COMM_ASSIST/deliverables/`):
- COO `2.0.0_SA_COO~CA/NEVER_WIDEN_HALF_COO_COMM_ASSIST_R18E_RECORDS_DEPLOY_20261014.md`
- CTO `1.0.0_SA_CTO/NEVER_WIDEN_HALF_CTO_COMM_ASSIST_R18E_RECORDS_DEPLOY_20261014.md`
- CVO `3.0.0_SA_CVO~L/NEVER_WIDEN_HALF_CVO_COMM_ASSIST_R18E_RECORDS_DEPLOY_20261014.md`

### THE CELL

`CA-j-14`. The same two Lambdas as your last orders (`CA-j-5`, ledger `comm-assist-r18-enforce-deploy`, CLOSED), on `/amW90t7TNsAAcx8Ap0t/eD7Jgk1HAOXJHCv8t8Mkho=` with the ingress mark in `enforce` mode. The trunk carries the assistant's two metadata-only records on top of that package (cell `CA-j-12`): `channel_mentions.py` (a mention record, written where a mention is texted), `mail_requests.py` (a considered-mail log) and the new `folder_records.py` (the scrub and the pruning), which the dell2 folder will publish to muse (FWD-13). This cell ships exactly that: code only. No environment value, policy, secret or Terraform resource moves; the trunk's Terraform default now reads `enforce`, equal to what is live.

### DO, IN THIS ORDER (the laptop, from the shared trunk at or after this order's GO)

1. `git worktree add --detach <scratch> 0774100edc` (outside every other worktree). Every build, test, init, plan, apply and re-plan below runs FROM that pinned worktree. Confirm `git -C <scratch> status --porcelain` is empty.
2. Open the ledger `comm-assist-r18-records-deploy` (`python .tools/deploy_ledger.py open ...` from the shared trunk), naming both functions (code only; no image). Commit the entry AND the sentinel BEFORE the act.
3. BEFORE reads, saved in your deliverables folder `org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/r18e/`: both functions' `CodeSha256`, `LastModified` and environment KEY NAMES (never values); the live zip with its sha256; the output of `python org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r18/checks/check_j5_obs.py` (it must NOT read `DIRTY`; the issuer's `probe:` row is counted apart).
   If the live hash is not `/amW90t7...` or the mode is not `enforce`, that is Branch B: another writer moved something. Stop and report.
4. Build in the pinned worktree: `bash infra/aws/lambda/teams-chat-assist/build.sh`. Run the import test on `infra/aws/lambda/teams-chat-assist/dist/pkg`. Record the built zip's base64 sha256. Then run AC1 below (`J14_PIN=0774100edc`): it must read `ok=True` BEFORE any apply. (The root needs both `dist` zips to plan: build `transcripts-pull` too if the plan asks for it, locally, uploading nothing.)
5. `TF_DATA_DIR` = a NEW scratch directory outside every git tree. `init -input=false` against the declared backend; a migrate or reconfigure prompt means STOP. Take a saved, locked, targeted plan `-target=module.ldo_001`, with NO `-var`.
   - Branch A exactly -> apply that saved plan through `bash .tools/safe-apply.sh`. Branch A is `0 to add, 2 to change, 0 to destroy`: the handler and `ingress[0]` only, changed keys within {`source_code_hash`, `last_modified`} and NEVER `environment`, the after-hash equal to step 4's.
   - Anything else -> Branch B: apply nothing, close the ledger as not-applied, report.
   - Never between 20:00Z and 21:45Z.
6. AFTER: run the criteria below, then a targeted re-plan (expect no changes). Read log lines only, never message content or the secret's value. Ten minutes on, the ingress log still shows `ingress_poll` and the mail step `polled`, and neither function log shows an error or `AccessDenied`.
7. Rollback on any AFTER failure: the COO half's rollback (the saved zip over `dist/`, then a targeted apply from a detached worktree at `8c5e0b278e`, NOT from `afa8752f44`, whose Terraform default would flip the mode to `record`). File an ARMED row naming `2.0.0_SA_COO~CA`, and report.
8. Close the ledger and commit. Remove the pinned worktree. Send no test mail, text nobody and invoke nothing.

### RULES FOR THIS CELL

- One targeted apply, `module.ldo_001` only. Never untargeted, never bare `terraform`, never `aws lambda update-function-code`.
- No `-var`. No edit to any `.tf` or code file. Never push, `git stash`, rebase, `checkout --`, `clean`.
- The secret's value is never read, printed, logged, committed or sent.
- No non-ASCII. `dist/` is never committed.
- Refuse a criterion you cannot satisfy as written. File a BLOCKING row with the measurement and stop; do not widen.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAj14-AC1" cell_refs="CA-j-14"><invocation>J14_PIN=0774100edc python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r18/checks/check_k3_equiv.py"</invocation><expect>K3-EQUIV ok=True</expect></criterion>
`CAj14-AC1` -- the issuer's pre-flight check (read it; do not edit it), run BEFORE the apply with the pinned worktree built: the packaged-path diff from the live pin `afa8752f44` carries the three CA-j-12 files, the built `channel_mentions.py`, `mail_requests.py` and `folder_records.py` equal the pin's bytes, and the built package forms the same S3 addresses and considers the same mail parties as the package the live function serves (17 probes; the Terraform file and one registry file from another seat are in the diff and are counted as foreign). It reads ok=False until the build exists.

<criterion id="CAj14-AC2" cell_refs="CA-j-14"><invocation>J14_PIN=0774100edc python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r18/checks/check_k3_live.py"</invocation><expect>RESULT: PASS</expect></criterion>
`CAj14-AC2` -- the issuer's live check (read it; do not edit it). Both functions are on one new package, not `/amW90t7...`; the served zip hashes to it and its eight files equal the pin's; both environments carry `INGRESS_MARK_MODE=enforce` and the other keys as recorded; the secret has a current version (value never read) and both roles may read it; the served code runs the mark checks, scrubs a snippet clean, and writes a mention record and a mail record with exactly the contracted keys. It FAILs at the base.

<criterion id="CAj14-AC3" cell_refs="CA-j-14"><invocation>bash "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r18/checks/check_k3_ledger.sh"</invocation><expect>RESULT: PASS</expect></criterion>
`CAj14-AC3` -- NEVER-2: the ledger `comm-assist-r18-records-deploy` is committed CLOSED at HEAD and its sentinel is gone. It FAILs at the base.
</proof_of_spec>

<expected_criteria>CAj14-AC1,CAj14-AC2,CAj14-AC3</expected_criteria>

Each invocation runs under `timeout 250`. Commit the deploy evidence FIRST, then write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/COMM_ASSIST.TO-CA-j-14.assistant-records-deploy.proof_of_spec.json`, pinning each artifact row to the commit that carried it, validate it with
`python .tools/proof-of-spec-check.py <instance> CAj14-AC1,CAj14-AC2,CAj14-AC3` AFTER your last commit, and flip `<status>` to `complete` only when all three PASS and the instance is VALID at the final head. Surprise rows are
`COMM_ASSIST-C18R-S<k>`, fabric `laptop`, disarm_owner `2.0.0_SA_COO~CA`, `surfaced_at` = `date -u +%FT%TZ` at filing. Append lines only to the investigation file.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round18.md</decomp_doc>
<owned_cells>CA-j-14</owned_cells>
</decomp_ref>

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/comm-assist-r18-records-deploy.json
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-j-14.assistant-records-deploy.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the act creates no schedule; the ingress keeps its 1-minute clock (module.ldo_001) and the End of Day window 20:00Z-21:45Z is a Branch B stop. No cron, alarm, monitor or notification is created.
comp-iam: DECLARED-NOT-APPLICABLE no policy moves: Branch A is the code hash only, and any iam address or environment key in the plan is Branch B.
comp-adversary: RUN -- a second writer (NFRA_CTLPLN also deploys this module; it has been told to hold and the hold was lifted at the CA-j-5 close, so it may apply again) moving the live hash or the mode before the act (step 3 -> Branch B); a package built from the moving trunk (pinned worktree, step 1); a foreign file riding the package (AC1 counts the Terraform file and the registry file and compares the S3 addresses and mail parties on both packages); an environment change or the mode leaving `enforce` in the plan (Branch B); a record writer failing inside the mention or mail handler (AC2's served-code probe runs both writers; the unit tests and `check_k1_records` read them at the merge); the secret value leaking (forbidden; never read). BLIND: a real @mention and a real considered mail are not in hand (Andrew's calls 44eb and e435), so the records are exercised by the probe and the tests until the dell2 pick-up and the FWD-13 exercise.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Base `0774100edc`: CAj14-AC1 base: PASS as measured only after the build exists (the issuer's own pre-flight build read `K3-EQUIV ok=True`, see the staging commit); it reads ok=False until a detached worktree at the pin is built. CAj14-AC2 base: FAIL as measured (the served package predates the records: the served-code probe cannot import `folder_records`). CAj14-AC3 base: FAIL as expected (0 entries).
Source: CTO ruling on call 608c (msg 109140); PRD v0.10 FWD-13; COO half `NEVER_WIDEN_HALF_COO_COMM_ASSIST_R18E_RECORDS_DEPLOY_20261014.md`; ledger precedents `comm-assist-r18-deploy`, `-key-deploy`, `-fresh-deploy`, `-enforce-deploy`.
