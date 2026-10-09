# TO COMM_ASSIST.TO-CA-d-2 -- round 12 CA-d-2: the FWD-4 mail deploy (one targeted apply of module.ldo_001) after r29

<to_id>COMM_ASSIST.TO-CA-d-2</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.7.0_AE_CloudOps~CA</issued_to>
<issued_by>2.0.0_SA_COO~ZZ</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>12</round>

**Directive:** D9 | **Fabric:** site-z | **Decomp cell:** `CA-d-2` (`decompositions/COMM_ASSIST_DECOMP.round12.md`) | **outcome_ref:** FWD-4 |
**depends_on:** NFRA_OPLGTW `TO-OG-ap-3` (creates `gateway/mail/commassist-bearer`)

---

## WORKER FACE

### GO -- TWO PHASES (amendment A2, CTO fold of UB-20261009T111212Z-f17d @02c84f1029)

**PHASE A runs when the issuer flips `<status>` to `pending`.** It applies nothing, opens no ledger, reads no secret and calls no
route. Do, in order: step 4 (BEFORE reads) and step 5 (both builds plus the import test) below. Then a SCRATCH preview: `TF_DATA_DIR`
set to a NEW scratch directory outside every git tree; `init -input=false` (a migrate or reconfigure prompt = STOP);
`terraform -chdir=infra/aws/terraform/transcripts plan -input=false -no-color -lock=false -target=module.ldo_001` with the variable
at its committed default `""` and the ONE foreign `-var` the A3 rule below permits. Save it as `PHASE_A_PLAN.txt` in your deliverables folder. **Expected: `0 to add, 2 to
change, 0 to destroy`, and both changes are the two functions' `source_code_hash`/`last_modified` only.** Any other reading (an
add, destroy, policy change, env change, address outside the module, failed import test, or a live hash other than `xWURpe/n...`)
-> file a BLOCKING row with the measurement and STOP. Then write `PHASE_A_READ.md` (one line per reading) and STOP. Do not
continue to step 1. The dependencies `-target=module.ldo_001` pulls in (`aws_kms_key.transcripts`, `aws_iam_role.second_reader` and
its policy) must read NO change; any change on them is "an address outside the module" -> STOP.

**A3 -- THE ONE PERMITTED `-var` (issuer ruling, row COMM_ASSIST-Z-S2 disarming Z-S1).** The shared root's NFRA_TRNSPT variable
`second_reader_trust_principal_arns` has no default by design. Pass it, and only it, as `-var` with the value READ at the act from
`aws iam get-role --role-name teams-global-transcripts-second-reader-role` (`AssumeRolePolicyDocument.Statement[].Principal.AWS`,
as a JSON list; it read `["arn:aws:iam::313476888478:user/Opal_Terminal"]` at 12:4xZ). Never type it from this order; never pass
any other `-var`. Our own `chat_assist_mail_bearer_secret_arn` is NEVER a `-var`: it is the committed default of step 2.

**PHASE A RE-RUN (A3):** re-take the scratch preview with that one `-var`, save as `PHASE_A_PLAN_2.txt`, append the readings to
`PHASE_A_READ.md`, report, and STOP.

**PHASE B runs only when the issuer writes `PHASE B GO` on the line below.** It is written once NFRA_OPLGTW `TO-OG-ap-3` is
complete with AC1 PASS (the secret exists and the gateway serves r29) AND (A4) NFRA_TRNSPT `TO-APPLY-s21` (the silver-only
reader role and its key-policy line) is complete, so a `-target=module.ldo_001` plan's dependencies read NO change. Phase B is
steps 1-9 below, re-reading step 4 at the act.
The three halves are committed and BIND: COO `org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~ZZ/NEVER_WIDEN_HALF_COO_COMM_ASSIST_R12_MAIL_DEPLOY_20261009.md`,
CTO `deliverables/1.0.0_SA_CTO~Z/NEVER_WIDEN_HALF_CTO_COMM_ASSIST_R12_MAIL_DEPLOY_20261009.md`, CVO
`deliverables/3.0.0_SA_CVO~Z/NEVER_WIDEN_HALF_CVO_COMM_ASSIST_R12_MAIL_DEPLOY_20261009.md` (all under `org/missions/D9/COMM/COMM_ASSIST/`).
Read all three. The COO half's Branch A / Branch B, rollback and conditions are the procedure.

PHASE B: NOT YET

### THE CELL

`CA-d-2`. Andrew's Teams assistant is two Lambdas from `module "ldo_001"` in `infra/aws/terraform/transcripts/chat_assist.tf`:
`teams-global-chat-assist-handler-lambda` and `teams-global-chat-assist-ingress-lambda`. Both run round 7's package (`CodeSha256`
`xWURpe/nRkiZAc8Uui+arsJpSeVnUErNEHBWqtvrM5Q=`). The repo carries rounds 8-10's code (the mail poller among it) and round 11's variable
`chat_assist_mail_bearer_secret_arn` (default `""`; when set, `MAIL_BEARER_SECRET` joins both functions' environment and the value
joins the exec policy's secrets read). This cell sets the variable to the real secret and deploys.

### DO, IN THIS ORDER (site Z, `0.7.0_AE_CloudOps~CA`, from the shared trunk at or after this order's issuance commit)

1. `aws secretsmanager describe-secret --secret-id gateway/mail/commassist-bearer`: record `ARN` and nothing else. NEVER read the value.
   Absent = STOP, report.
2. Edit `chat_assist.tf`: the variable's `default = ""` becomes `default = "<that ARN>"`. That is the only change. Commit it alone
   through `safe-commit.sh`. It is committed, never passed as `-var`, because the root is shared.
3. Open the ledger `comm-assist-r12-mail-deploy` (`python .tools/deploy_ledger.py open ...`), naming both functions and
   `teams-global-chat-assist-policy`. Commit the entry AND the sentinel BEFORE the act.
4. BEFORE reads, saved in your deliverables folder: both functions' `CodeSha256`/`LastModified`, the live zip
   (`get-function` -> `Code.Location`) with its sha256, and the policy's default version id.
5. Build `bash infra/aws/lambda/transcripts-pull/build.sh` and `bash infra/aws/lambda/teams-chat-assist/build.sh` (the root does not
   load without both zips; building uploads nothing). Run the import test on `infra/aws/lambda/teams-chat-assist/dist/pkg` that the COO
   half's Branch B names.
6. `TF_DATA_DIR` = a NEW scratch directory outside every git tree; `init -input=false` against the declared backend (a migrate or
   reconfigure prompt = STOP). Take a saved, locked, targeted plan `-target=module.ldo_001` with the A3 `-var` only. Branch A exactly
   (`0 to add, 3 to change, 0 to destroy`; the two functions' code hash and env var, plus the policy's one ARN) -> apply that saved
   plan through `bash .tools/safe-apply.sh`. Anything else -> Branch B: apply nothing, close the ledger as not-applied, report.
   Never between 20:00Z and 21:45Z.
7. AFTER: run the criteria below, then a targeted re-plan (expect no changes). Within 5 minutes read the ingress log for
   `ingress_poll` lines with no `ingress_step_failed`, and for the mail step reporting `polled`, not `not-configured`. Read log lines
   only, never message content.
8. Rollback on any AFTER failure: the COO half's code rollback (saved zip over `dist/`, default back to `""`, same targeted apply).
   File an ARMED row naming `2.0.0_SA_COO~ZZ`, and report.
9. Close the ledger and commit. Send no test mail and invoke nothing.

### RULES FOR THIS CELL

- One targeted apply, `module.ldo_001` only. Never untargeted, never bare `terraform`, never `aws lambda update-function-code`.
- Never write, read the value of, rotate or delete the secret. No `-var` except the A3 one. Never push, `git stash`, rebase, `checkout --`, `clean`.
- No non-ASCII. `dist/` is never committed.
- Refuse a criterion you cannot satisfy as written. File a BLOCKING row with the measurement and stop; do not widen.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAd2-AC1" cell_refs="CA-d-2"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~ZZ/r12/checks/d2_live.py"</invocation><expect>RESULT: PASS</expect></criterion>
`CAd2-AC1` -- the issuer's live check (read it; do not edit it). The secret exists; `chat_assist.tf` at HEAD commits its ARN; both
functions carry the built package's hash (not round 7's) and `MAIL_BEARER_SECRET` = the ARN; the exec policy grants the read. It
FAILs at the base.

<criterion id="CAd2-AC2" cell_refs="CA-d-2"><invocation>bash "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~ZZ/r12/checks/d2_ledger.sh"</invocation><expect>RESULT: PASS</expect></criterion>
`CAd2-AC2` -- NEVER-2: the ledger `comm-assist-r12-mail-deploy` is committed CLOSED at HEAD and its sentinel is gone. It FAILs at
the base.
</proof_of_spec>

<expected_criteria>CAd2-AC1,CAd2-AC2</expected_criteria>

Each invocation runs under `timeout 120`. Write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/COMM_ASSIST.TO-CA-d-2.mail-deploy.proof_of_spec.json`. Validate
it with `python .tools/proof-of-spec-check.py <instance> CAd2-AC1,CAd2-AC2`. Flip `<status>` to `complete` only when both PASS and
the instance is VALID. Surprise rows are `COMM_ASSIST-Z-S<k>` (the gate grammar; A3), fabric `site-z`, disarm_owner `2.0.0_SA_COO~ZZ`, `surfaced_at` =
`date -u +%FT%TZ` at filing. Append lines only to the investigation file.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round12.md</decomp_doc>
<owned_cells>CA-d-2</owned_cells>
</decomp_ref>

<paths>
infra/aws/terraform/transcripts/chat_assist.tf
org/critical_paths/change_management/
org/critical_paths/.open_deploys/comm-assist-r12-mail-deploy.json
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- the act creates no schedule; the ingress keeps its existing 1-minute clock (module.ldo_001 S15); the End of Day window 20:00Z-21:45Z is a Branch B stop. No cron, alarm, monitor or notification is created.
comp-iam: RUN -- live `iam get-policy teams-global-chat-assist-policy` at the cut: default v3. The act adds exactly ONE ARN (gateway/mail/commassist-bearer) to the existing secrets-read statement; round 11's PLAN_SET (`0.9.0_WK_COMM_ASSIST~5`) showed that statement as the only policy change. BLIND: a cross-account secret would also need a resource policy; the secret is created in 313476888478 by OG-ap-3.
comp-adversary: RUN -- the variable passed as `-var` (unwired by the next apply of the shared root; committed default instead); a package built from a tree carrying a packaged-path change not in the half (Branch B); the secret's value entering any artifact (never read); an apply inside the End of Day window (Branch B). BLIND: what the registry's additive rows resolve to at run time is guarded only by the import test, not by a live call.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

**ISSUER NOTES:**
- Pre-cut (base `b1b8f5b4fe`): `CAd2-AC1` base FAIL as expected (secret absent, both functions at `xWURpe/n...`, no env var, no
  grant). `CAd2-AC2` base FAIL as expected (0 entries). The ledger reader's positive control on `teams-r7-code-laptop-20261008`
  reads CLOSED=yes, PASS.
- A1 (issuer, 2026-10-09 ~09:5xZ): re-addressed `0.7.0_AE_CloudOps~Z` -> `0.7.0_AE_CloudOps~CA` (fresh lane assigned by
  `0.0.0_AB_MSTR~Z` msg 32641; rule 27 seating: `~Z` holds open orders on 4 other projects, gate2 ANNOUNCE at `f8b46c5aa5`). Same
  class, same box. The three signed halves bind the act, not the lane letter, and are unchanged. Graded by no gate limb as a
  modification (placeholders NONE; a re-address never trips the seating lint).
- A2 (issuer, 2026-10-09 ~11:3xZ, on `1.0.0_SA_CTO~Z`'s fold of UB-20261009T111212Z-f17d @02c84f1029, msg 32712): the order splits
  into PHASE A (BEFORE reads, builds, import test and a scratch `""`-variable preview plan, expecting 0/2/0 with the code hash
  only; it applies nothing) and PHASE B (the act, behind the `PHASE B GO` line, unchanged in substance). Phase A runs once the
  fold is signed by `3.0.0_SA_CVO~Z`. No criterion changed. Graded by no gate limb as a modification (placeholders NONE).
- A3 (issuer, 2026-10-09 ~12:5xZ, on 0.7.0_AE_CloudOps~CA's Phase A STOP, msg 32751, row Z-S1): one foreign `-var`
  (`second_reader_trust_principal_arns`) is permitted at its LIVE value, read at the act; the readers dependencies must read no change;
  the Phase A preview is re-run; the row-id line follows the gate grammar. NFRA_TRNSPT a18 applied it at 09:55Z (role CreateDate). Branch A
  and the halves' blast radius are unchanged. Disarm row COMM_ASSIST-Z-S2. Graded by no gate limb as a modification (placeholders NONE).
- A4 (issuer, 2026-10-09 ~13:1xZ, on PHASE_A_PLAN_2.txt, 13:09Z): the re-run reads `1 to add, 3 to change`. Two of the changes are
  outside the module: `aws_iam_role.silver_reader` (create) and `aws_kms_key.transcripts` (policy update), NFRA_TRNSPT TR-r-21's
  built-but-unapplied silver reader, pulled in as dependencies because module.ldo_001 takes the key's id and ARN. Branch A is
  correctly not met. OG-ap-3 is complete (fab015fa54). PHASE B GO now also waits on NFRA_TRNSPT TO-APPLY-s21 (pending, laptop
  0.7.0_AE_CloudOps~TRL). Carried to round 13: decouple module.ldo_001 from the key RESOURCE (read it by data source), so that no
  other project's pending key change blocks a COMM deploy again. Graded by no gate limb (placeholders NONE).
- The analysis's done-when also names the real mail run. That run is the issuer's at close, not this order's (an applier sends no
  test mail).

Source: PRD `prd/COMM_ASSIST_PRD.md` v0.2 (ADMITTED, `805fec22c5`), FWD-4, C-MAIL, C-PACKAGE; round-11 analysis @4c14e95965.
