# TO COMM_ASSIST.TO-CA-d-2 -- round 12 CA-d-2: the FWD-4 mail deploy (one targeted apply of module.ldo_001) after r29

<to_id>COMM_ASSIST.TO-CA-d-2</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.7.0_AE_CloudOps~CA</issued_to>
<issued_by>2.0.0_SA_COO~ZZ</issued_by>
<issued_date>2026-10-09</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>12</round>

**Directive:** D9 | **Fabric:** site-z | **Decomp cell:** `CA-d-2` (`decompositions/COMM_ASSIST_DECOMP.round12.md`) | **outcome_ref:** FWD-4 |
**depends_on:** NFRA_OPLGTW `TO-OG-ap-3` (creates `gateway/mail/commassist-bearer`)

---

## WORKER FACE

### GO -- this order is `staged`; act only when the issuer flips it `pending`

The issuer flips it once all three hold: (1) NFRA_OPLGTW `TO-OG-ap-3` is complete with AC1 PASS, so the secret exists; (2) a CTO
half and (3) a CVO half are committed beside the COO half
`org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~ZZ/NEVER_WIDEN_HALF_COO_COMM_ASSIST_R12_MAIL_DEPLOY_20261009.md`.
**The halves BIND**: read all three first. The COO half's Branch A / Branch B, rollback and conditions are the procedure.

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
   reconfigure prompt = STOP). Take a saved, locked, targeted plan `-target=module.ldo_001`. Branch A exactly
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
- Never write, read the value of, rotate or delete the secret. Never `-var`. Never push, `git stash`, rebase, `checkout --`, `clean`.
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
the instance is VALID. Surprise rows are `COMM_ASSIST-Z-AE-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~ZZ`, `surfaced_at` =
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
- The analysis's done-when also names the real mail run. That run is the issuer's at close, not this order's (an applier sends no
  test mail).

Source: PRD `prd/COMM_ASSIST_PRD.md` v0.2 (ADMITTED, `805fec22c5`), FWD-4, C-MAIL, C-PACKAGE; round-11 analysis @4c14e95965.
