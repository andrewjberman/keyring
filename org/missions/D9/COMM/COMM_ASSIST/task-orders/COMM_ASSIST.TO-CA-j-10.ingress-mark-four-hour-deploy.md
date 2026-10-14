# TO COMM_ASSIST.TO-CA-j-10 -- round 18 CA-j-10: deploy the four-hour ingress mark (one targeted apply of module.ldo_001, code only, pinned build)

<to_id>COMM_ASSIST.TO-CA-j-10</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.7.0_AE_CloudOps~CA</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-14</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>
<workstream>DEPLOY18FRESH</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-j-10` (`decompositions/COMM_ASSIST_DECOMP.round18.md`, AMENDMENT 6) | **outcome_ref:** FWD-7 |
**depends_on:** CA-j-9 (merged `afa8752f44`), CA-j-8 (CLOSED @df7f6f6c55); the GO waits on the CTO and CVO halves

---

## WORKER FACE

### GO

STAGED. The issuer flips `<status>` to `pending` and writes `GO` on the line below once all three halves are SIGNED on the pin `afa8752f44`. Until then, do nothing.

(no GO yet)

The three halves BIND, and the COO half's Branch A / Branch B, rollback and conditions ARE the procedure. Read all three in full (all under `org/missions/D9/COMM/COMM_ASSIST/deliverables/`):
- COO `2.0.0_SA_COO~CA/NEVER_WIDEN_HALF_COO_COMM_ASSIST_R18C_FRESH_DEPLOY_20261014.md`
- CTO `1.0.0_SA_CTO/NEVER_WIDEN_HALF_CTO_COMM_ASSIST_R18C_FRESH_DEPLOY_20261014.md`
- CVO `3.0.0_SA_CVO~L/NEVER_WIDEN_HALF_CVO_COMM_ASSIST_R18C_FRESH_DEPLOY_20261014.md`

### THE CELL

`CA-j-10`. The same two Lambdas as your last orders (`CA-j-3`, ledger `comm-assist-r18-deploy`, and `CA-j-8`, ledger `comm-assist-r18-key-deploy`, both CLOSED), now on `nX67q2k05fh77lG2gBLsNlp6HLAZeELPq85CJpWCVhA=` with the ingress mark live in `record` mode and its key narrowed. The trunk carries TWO more code changes on top of that package (cell `CA-j-9`): `ingress_mark.py` (a mark is valid for 4 hours, not 15 minutes) and `tenant.py` (the single-use record holds every mark inside that window, pruned by age; a refusal records the event's kind and tag). This cell ships exactly that: code only. No environment value, policy, secret or Terraform resource moves.

### DO, IN THIS ORDER (the laptop, from the shared trunk at or after this order's GO)

1. `git worktree add --detach <scratch> afa8752f44` (outside every other worktree). Every build, test, init, plan, apply and re-plan below runs FROM that pinned worktree. Confirm `git -C <scratch> status --porcelain` is empty.
2. Open the ledger `comm-assist-r18-fresh-deploy` (`python .tools/deploy_ledger.py open ...` from the shared trunk), naming both functions. Commit the entry AND the sentinel BEFORE the act.
3. BEFORE reads, saved in your deliverables folder `org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/r18c/`: both functions' `CodeSha256` and `LastModified`; both functions' environment KEY NAMES (never values); the live zip with its sha256.
   If the live hash is not `nX67q...` or the mode is not `record`, that is Branch B: another writer moved something. Stop and report.
4. Build in the pinned worktree: `bash infra/aws/lambda/teams-chat-assist/build.sh`. Run the import test on `infra/aws/lambda/teams-chat-assist/dist/pkg`. Record the built zip's base64 sha256. Then run AC1 below (`J10_PIN=afa8752f44`): it must read `ok=True` BEFORE any apply. (The root needs both `dist` zips to plan: build `transcripts-pull` too if the plan asks for it, locally, uploading nothing.)
5. `TF_DATA_DIR` = a NEW scratch directory outside every git tree. `init -input=false` against the declared backend; a migrate or reconfigure prompt means STOP. Take a saved, locked, targeted plan `-target=module.ldo_001`, with NO `-var`.
   - Branch A exactly -> apply that saved plan through `bash .tools/safe-apply.sh`. Branch A is `0 to add, 2 to change, 0 to destroy`: the handler and `ingress[0]` only, changed keys within {`source_code_hash`, `last_modified`} and NOTHING else (no `environment`), the after-hash equal to step 4's.
   - Anything else -> Branch B: apply nothing, close the ledger as not-applied, report.
   - Never between 20:00Z and 21:45Z.
6. AFTER: run the criteria below, then a targeted re-plan (expect no changes). Read log lines only, never message content or the secret's value. Ten minutes on, the ingress log still shows `ingress_poll` and the mail step `polled`, and neither function log shows an error for the mark secret.
7. Rollback on any AFTER failure: the COO half's rollback (the saved zip over `dist/`, then the same targeted apply). File an ARMED row naming `2.0.0_SA_COO~CA`, and report.
8. Close the ledger and commit. Remove the pinned worktree. Send no test mail, text nobody and invoke nothing.

### RULES FOR THIS CELL

- One targeted apply, `module.ldo_001` only. Never untargeted, never bare `terraform`, never `aws lambda update-function-code`.
- No `-var`. No edit to any `.tf` or code file. Never push, `git stash`, rebase, `checkout --`, `clean`.
- The secret's value is never read, printed, logged, committed or sent.
- No non-ASCII. `dist/` is never committed.
- Refuse a criterion you cannot satisfy as written. File a BLOCKING row with the measurement and stop; do not widen.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAj10-AC1" cell_refs="CA-j-10"><invocation>J10_PIN=afa8752f44 python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r18/checks/check_j10_equiv.py"</invocation><expect>J10-EQUIV ok=True</expect></criterion>
`CAj10-AC1` -- the issuer's pre-flight check (read it; do not edit it), run BEFORE the apply with the pinned worktree built: the packaged-path diff from the deployed pin `38ce5a7981` carries the two CA-j-9 files, the built `ingress_mark.py` and `tenant.py` equal the pin's bytes, and the built package forms the same S3 addresses and considers the same mail parties as the package the live function serves (17 probes; the one Terraform path in the diff is the already-applied CA-j-7 policy and is counted as foreign). It reads ok=False until the build exists.

<criterion id="CAj10-AC2" cell_refs="CA-j-10"><invocation>J10_PIN=afa8752f44 python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r18/checks/check_j10_live.py"</invocation><expect>RESULT: PASS</expect></criterion>
`CAj10-AC2` -- the issuer's live check (read it; do not edit it). Both functions are on one new package, not `nX67q...`; the served zip hashes to it and its six files equal the pin's; both environments carry `INGRESS_MARK_MODE=record` and the other keys as recorded; the secret has a current version (value never read) and both roles may read it; the served code round-trips a mark, refuses a tampered one, bounds a mark at 4 hours, holds marks by age and parses the three modes. It FAILs at the base.

<criterion id="CAj10-AC3" cell_refs="CA-j-10"><invocation>bash "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r18/checks/check_j10_ledger.sh"</invocation><expect>RESULT: PASS</expect></criterion>
`CAj10-AC3` -- NEVER-2: the ledger `comm-assist-r18-fresh-deploy` is committed CLOSED at HEAD and its sentinel is gone. It FAILs at the base.
</proof_of_spec>

<expected_criteria>CAj10-AC1,CAj10-AC2,CAj10-AC3</expected_criteria>

Each invocation runs under `timeout 250`. Commit the deploy evidence FIRST, then write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/COMM_ASSIST.TO-CA-j-10.ingress-mark-four-hour-deploy.proof_of_spec.json`, pinning each artifact row to the commit that carried it, validate it with
`python .tools/proof-of-spec-check.py <instance> CAj10-AC1,CAj10-AC2,CAj10-AC3` AFTER your last commit, and flip `<status>` to `complete` only when all three PASS and the instance is VALID at the final head. Surprise rows are
`COMM_ASSIST-C18F-S<k>`, fabric `laptop`, disarm_owner `2.0.0_SA_COO~CA`, `surfaced_at` = `date -u +%FT%TZ` at filing. Append lines only to the investigation file.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round18.md</decomp_doc>
<owned_cells>CA-j-10</owned_cells>
</decomp_ref>

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/comm-assist-r18-fresh-deploy.json
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-j-10.ingress-mark-four-hour-deploy.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the act creates no schedule; the ingress keeps its 1-minute clock (module.ldo_001) and the End of Day window 20:00Z-21:45Z is a Branch B stop. No cron, alarm, monitor or notification is created.
comp-iam: DECLARED-NOT-APPLICABLE no policy moves: Branch A is the code hash only, and any iam address or environment key in the plan is Branch B.
comp-adversary: RUN -- a second writer (NFRA_CTLPLN also deploys this module) moving the live hash before the act (step 3 -> Branch B); a package built from the moving trunk (pinned worktree, step 1); a foreign file riding the package (AC1 counts non-packaged paths and compares the S3 addresses and mail parties on both packages); an environment change or the mode arriving as `enforce` in the plan (Branch B); the held-marks code failing on a text (AC2's served-code probe runs `_held_marks` against a legacy string, a 3-hour and a 5-hour entry); the secret value leaking (forbidden; never read). BLIND: a real redelivered event after a real handler failure is read only live; muse's path is untouched and bounded by check_i13_fresh in the CA-j-9 order.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Base `afa8752f44`: CAj10-AC1 base: PASS as measured only after the build exists (the issuer's own pre-flight build read `J10-EQUIV ok=True files=2 foreign=1 probes=17 same=17`); it reads ok=False until a detached worktree at the pin is built. CAj10-AC2 base: FAIL as measured (the served code's bound is 15 minutes; the package is the CA-j-3 one). CAj10-AC3 base: FAIL as expected (0 entries).
Source: CTO ruling on call 847f (msg 109095); COO half `NEVER_WIDEN_HALF_COO_COMM_ASSIST_R18C_FRESH_DEPLOY_20261014.md`; ledger precedents `comm-assist-r18-deploy` and `comm-assist-r18-key-deploy`.
