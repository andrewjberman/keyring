# TO COMM_ASSIST.TO-CA-f-1 -- round 14 CA-f-1: deploy the round-13 package (one targeted apply of module.ldo_001, code only, pinned build)

<to_id>COMM_ASSIST.TO-CA-f-1</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.7.0_AE_CloudOps~CA</issued_to>
<issued_by>2.0.0_SA_COO~ZZ</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>14</round>

**Directive:** D9 | **Fabric:** site-z | **Decomp cell:** `CA-f-1` (`decompositions/COMM_ASSIST_DECOMP.round14.md`) | **outcome_ref:** FWD-3, FWD-4 |
**depends_on:** none (the GO waits on the CTO and CVO halves)

---

## WORKER FACE

### GO

The issuer flips `<status>` to `pending` and writes `GO` on the line below once all three halves are SIGNED. Until then, do nothing.

GO -- written by 2.0.0_SA_COO~ZZ 2026-10-11 ~01:5xZ. All three halves SIGNED on the pin `2fd32e12c2`: COO `3d80c80db2`, CTO
`7e2efbe4eb`, CVO `942155dfc1`. The CVO half's carried point 2 binds: a pre-state hash other than `SFSTGBQX...` at step 3 is
Branch B (refuse; never re-baseline). Outside 20:00Z-21:45Z.

The halves BIND, and the COO half's Branch A / Branch B, rollback and conditions ARE the procedure. Read all three in full
(all under `org/missions/D9/COMM/COMM_ASSIST/`):
- COO `deliverables/2.0.0_SA_COO~ZZ/NEVER_WIDEN_HALF_COO_COMM_ASSIST_R14_DEPLOY_20261011.md`
- CTO `deliverables/1.0.0_SA_CTO~Z/NEVER_WIDEN_HALF_CTO_COMM_ASSIST_R14_DEPLOY_20261011.md`
- CVO `deliverables/3.0.0_SA_CVO~Z/NEVER_WIDEN_HALF_CVO_COMM_ASSIST_R14_DEPLOY_20261011.md`

### THE CELL

`CA-f-1`. Andrew's Teams assistant is two Lambdas from `module "ldo_001"` in `infra/aws/terraform/transcripts/chat_assist.tf`:
`teams-global-chat-assist-handler-lambda` and `teams-global-chat-assist-ingress-lambda` (us-east-1). Both run the package
`SFSTGBQX3r49t2YXSrN+6t6Ekmz1NrpxkjX09VHLZEM=`, deployed 2026-10-09 23:03Z by another project (NFRA_CTLPLN `TO-APPLY-31`) and built
at `bde0c0fc90`. The trunk carries two merged COMM changes on top of it: `mail_requests.py` (only five named parties are
considered) and `channel_mentions.py` (a failing channel poll names its error and raises). This cell ships exactly that, code only.

### DO, IN THIS ORDER (site Z, from the shared trunk at or after this order's issuance commit)

1. `git worktree add --detach <scratch> 2fd32e12c2` (outside every other worktree). Every build, test, init, plan, apply and re-plan
   below runs FROM that pinned worktree. Confirm `git -C <scratch> status --porcelain` is empty.
2. Open the ledger `comm-assist-r14-deploy` (`python .tools/deploy_ledger.py open ...` from the shared trunk), naming both functions.
   Commit the entry AND the sentinel BEFORE the act.
3. BEFORE reads, saved in your deliverables folder `org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/`:
   - both functions' `CodeSha256` and `LastModified`;
   - the live zip (`get-function` -> `Code.Location`) with its sha256.

   If the live hash is not `SFSTGBQX...`, that is Branch B: another writer moved it. Stop and report.
4. Build in the pinned worktree: `bash infra/aws/lambda/transcripts-pull/build.sh` and `bash infra/aws/lambda/teams-chat-assist/build.sh`
   (the root does not load without both zips; building uploads nothing). Run the COO half's import test on
   `infra/aws/lambda/teams-chat-assist/dist/pkg`. Record the built zip's base64 sha256.
5. `TF_DATA_DIR` = a NEW scratch directory outside every git tree. `init -input=false` against the declared backend; a migrate
   or reconfigure prompt means STOP. Take a saved, locked, targeted plan `-target=module.ldo_001`, with the ONE permitted `-var`
   `second_reader_trust_principal_arns` read live at the act:
   `aws iam get-role --role-name teams-global-transcripts-second-reader-role`, the `Principal.AWS` list as JSON.
   - Branch A exactly -> apply that saved plan through `bash .tools/safe-apply.sh`. Branch A is `0 to add, 2 to change,
     0 to destroy`: the handler and `ingress[0]` only, keys within {`source_code_hash`, `last_modified`}, and the after-hash
     equal to step 4's.
   - Anything else -> Branch B: apply nothing, close the ledger as not-applied, report.
   - Never between 20:00Z and 21:45Z.
6. AFTER: run the criteria below, then a targeted re-plan (expect no changes). Read log lines only, never message content.
7. Rollback on any AFTER failure: the COO half's code rollback (the saved zip over `dist/`, then the same targeted apply).
   File an ARMED row naming `2.0.0_SA_COO~ZZ`, and report.
8. Close the ledger and commit. Remove the pinned worktree. Send no test mail and invoke nothing.

### RULES FOR THIS CELL

- One targeted apply, `module.ldo_001` only. Never untargeted, never bare `terraform`, never `aws lambda update-function-code`.
- No `-var` except the one above. No edit to any `.tf` or code file. Never push, `git stash`, rebase, `checkout --`, `clean`.
- No non-ASCII. `dist/` is never committed.
- Refuse a criterion you cannot satisfy as written. File a BLOCKING row with the measurement and stop; do not widen.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAf1-AC1" cell_refs="CA-f-1"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~ZZ/r14/checks/d1_live.py"</invocation><expect>RESULT: PASS</expect></criterion>
`CAf1-AC1` -- the issuer's live check (read it; do not edit it). Both functions are on one new package, not `SFSTGBQX...`. The
served zip hashes to it. The served zip's two round-13 files equal the pin's. The served code refuses a sixth firm. It FAILs at
the base.

<criterion id="CAf1-AC2" cell_refs="CA-f-1"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~ZZ/r14/checks/d1_errorfield.py"</invocation><expect>RESULT: PASS</expect></criterion>
`CAf1-AC2` -- the live `channel_poll` step is no longer silent after the deploy. Either its `error` field is readable and
`ingress_step_failed[channels]` appears, or it is healthy. Run it 5-10 minutes after the apply. It FAILs at the base (60 of 60
failed, 0 with an error).

<criterion id="CAf1-AC3" cell_refs="CA-f-1"><invocation>bash "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~ZZ/r14/checks/d1_ledger.sh"</invocation><expect>RESULT: PASS</expect></criterion>
`CAf1-AC3` -- NEVER-2: the ledger `comm-assist-r14-deploy` is committed CLOSED at HEAD and its sentinel is gone. It FAILs at the base.
</proof_of_spec>

<expected_criteria>CAf1-AC1,CAf1-AC2,CAf1-AC3</expected_criteria>

Each invocation runs under `timeout 120`. Write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/COMM_ASSIST.TO-CA-f-1.round13-package-deploy.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance> CAf1-AC1,CAf1-AC2,CAf1-AC3`, and flip `<status>` to `complete`
only when all three PASS and the instance is VALID. Surprise rows are `COMM_ASSIST-Z-S<k>` (the gate grammar), fabric `site-z`,
disarm_owner `2.0.0_SA_COO~ZZ`, `surfaced_at` = `date -u +%FT%TZ` at filing. Append lines only to the investigation file.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round14.md</decomp_doc>
<owned_cells>CA-f-1</owned_cells>
</decomp_ref>

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/comm-assist-r14-deploy.json
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-f-1.round13-package-deploy.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- the act creates no schedule; the ingress keeps its 1-minute clock (module.ldo_001); the End of Day window 20:00Z-21:45Z is a Branch B stop. No cron, alarm, monitor or notification is created.
comp-iam: RUN -- no policy moves: Branch A is the code hash only; the round-12 policy v4 (+1 commassist ARN) is unchanged by this act.
comp-adversary: RUN -- a second writer (NFRA_CTLPLN deploys the same module) moving the live hash before the act (step 3 -> Branch B); a package built from the moving trunk (pinned worktree, step 1); the ~60 ingress_step_failed lines an hour read as a regression (named in the COO half as intended); message content entering an artifact (log lines only). BLIND: whether the gateway serves the channel routes is NFRA_OPLGTW's; this act only makes the failure readable.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Base `2fd32e12c2`: CAf1-AC1 base: FAIL as expected (pre-state hash; both round-13 files differ from the pin; the served code
admits `sixthfirm`). CAf1-AC2 base: FAIL as expected (60 channel_poll, 60 failed, 0 with error, 0 step_failed). CAf1-AC3 base:
FAIL as expected (0 entries).
Source: CTO round-13 analysis `ledger/ROUND_ANALYSIS.round13.md` @08b06f5d33, ruling 1 and D1.
