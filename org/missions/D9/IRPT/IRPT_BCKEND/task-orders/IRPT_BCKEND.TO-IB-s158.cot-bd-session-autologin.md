# TO IRPT_BCKEND.TO-IB-s158 -- The COT Black Diamond session auto-login succeeds again (row IRPT_BCKEND-S158)

<to_id>IRPT_BCKEND.TO-IB-s158</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.6.2_AE_PartnerETL~S</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-09-27</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>seat</worker_class>
<placeholders>NONE</placeholders>
<round>19</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 1.0.0_SA_CTO 101977 (on 101946) | **Decomp cell:** `IB-sr-1`
(IRPT_BCKEND decomposition, section 12 addendum) | **outcome_ref:** FWD-1 (the COT Performance hop) | **depends_on:** none

---

## WORKER FACE

### THE CELL

`IB-sr-1` -- disarm row `IRPT_BCKEND-S158`. The scheduled COT Black Diamond session refresh has failed every day since 09-24, so
`blackdiamond/cot/session` (AWSCURRENT created 2026-09-16) has aged out: a fresh Cottonwood Performance read now fails at the
provider (BDRequestFailed HTTPError, 2026-09-27 15:41:03Z).

What is measured (1.0.0_SA_CTO 101946):
- scheduler `cot-bd-session-daily-et` ENABLED, cron(30 7) America/New_York;
- SSM document `opal-cot-bd-session-fetch`: last Success 09-16; Failed 09-24, 09-25, 09-26, 09-27 (latest command 60650bfe, rc 1,
  output empty);
- in `C:/Users/AndrewBerman/Desktop/ajb_workspace/infra/aws/terraform/cot-pipeline/ssm.tf` lines 49-69 the step runs `set -e`, then
  `./run-bd-auto-login.sh > $LOG_FILE 2>&1`; a non-zero exit aborts the step before `tail` and the `aws s3 cp` log upload, so no log
  ever reaches `s3://opal-data-cot/logs/cot-exporter/session-fetch/`;
- the box keeps `/tmp/cot-session-autologin-*.log`; the deploy source is
  `C:/Users/AndrewBerman/Desktop/ajb_workspace/infra/aws/ec2/bd-cot-auto-login/` (S3 -> `/opt/bd-cot-auto-login` on the box).

**Build:**
1. Read the box's newest `/tmp/cot-session-autologin-*.log` files (read-only, through SSM on the auto-login instance) and name the
   failure cause in your deliverable, one line per failed day.
2. Change the document's step so the log is uploaded on failure too: capture the wrapper's exit code without `set -e` aborting
   first, `tail` and upload the log, then `exit` with the captured code. The document name is unchanged, so the
   `cot-session-complete` EventBridge rule still matches on Success.
3. Fix the named cause inside the grant, deploy through `safe-apply` (and the S3 -> box deploy the source already uses), and reach
   ONE Success of `opal-cot-bd-session-fetch`, fired by its scheduler or its existing trigger Lambda, that moves
   `blackdiamond/cot/session` AWSCURRENT.

**Vendor sign-in:** ONLY through the document (1.0.0_SA_CTO 101946, 101977). Nobody signs in by hand, and no other path writes the
session secret.

### ACCEPTANCE

<criterion id="IBS158-AC1" cell_refs="IB-sr-1"><invocation>python -c "import json;d=json.load(open('C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier2_senior/0.6.2_AE_PartnerETL/deliverables/IRPT_BCKEND_S158_CAUSE_20260927.json'));r=d.get('failed_days') or [];ok=bool((d.get('structural_cause') or {}).get('one_line')) and len(r)==4 and all(x.get('command_id') and (x.get('quoted_failing_line') or (x.get('cause_claim')=='absent' and x.get('why_unmeasurable'))) for x in r) and (d.get('absence_proof') or {}).get('carriers_checked',0)>=1;print('CAUSE-NAMED' if ok else 'MISSING')"</invocation><expect>CAUSE-NAMED</expect></criterion>
`IBS158-AC1` (AMENDED 2026-09-27 by the issuer, 2.0.0_SA_COO~P, on 0.6.2_AE_PartnerETL~S 102034) -- the failure cause is named
at the grain the carriers allow: the STRUCTURAL cause measured (why no log survived), and one row per failed day (09-24..09-27)
with its command id and EITHER the quoted failing line OR `cause_claim: absent` with why it is unmeasurable, beside an absence
proof over every carrier checked with its denominator. Why amended: the order's premise that "the box keeps
/tmp/cot-session-autologin-*.log" was false -- /tmp is tmpfs and the box stops between runs, so the four days' logs were
destroyed before this order was cut, and the reproduction after the log-on-failure fix SUCCEEDED. The original test asked for
bytes no carrier holds; the amendment grades what was measurable, and a per-day cause stays `absent`, never inferred.

<criterion id="IBS158-AC2" cell_refs="IB-sr-1"><invocation>aws ssm get-document --name opal-cot-bd-session-fetch --query Content --output text</invocation><expect>the live document's step captures the wrapper's exit code without set -e aborting before the log upload, uploads the log, then exits with the captured code</expect></criterion>
`IBS158-AC2` -- the LIVE document uploads its log on failure (read from AWS, not from the repo).

<criterion id="IBS158-AC3" cell_refs="IB-sr-1"><invocation>aws secretsmanager list-secret-version-ids --secret-id blackdiamond/cot/session --query "Versions[?contains(VersionStages,'AWSCURRENT')].CreatedDate" --output text</invocation><expect>an AWSCURRENT CreatedDate later than 2026-09-27T17:00:00Z, with one opal-cot-bd-session-fetch command Status Success at or before it</expect></criterion>
`IBS158-AC3` -- one Success of the document that moves the session secret's AWSCURRENT.

<expected_criteria>IBS158-AC1,IBS158-AC2,IBS158-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **Deploy discipline.** A ledger entry opened before the first write (`.tools/deploy_ledger.py`), `safe-apply` for Terraform, and
  the S3 -> box deploy the source already uses. The change is WORLD: it moves live infrastructure and the live COT session.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not
  weaken the test to pass.

<paths>
infra/aws/terraform/cot-pipeline/ssm.tf
infra/aws/ec2/bd-cot-auto-login/run-bd-auto-login.sh
infra/aws/ec2/bd-cot-auto-login/secret-ids.env
org/tier2_senior/0.6.2_AE_PartnerETL/deliverables/IRPT_BCKEND_S158_CAUSE_20260927.json
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 12 addendum (round 19), cell `IB-sr-1`.
<owned_cells>IB-sr-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBS158-AC1, IBS158-AC2, IBS158-AC3. Instance at `org/tier2_senior/0.6.2_AE_PartnerETL/deliverables/IRPT_BCKEND.TO-IB-s158.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IBS158-AC1,IBS158-AC2,IBS158-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** one message to `2.0.0_SA_COO~P` naming the cause, the ledger slug, the Success command id and the new AWSCURRENT
version id; surprise rows in the investigation file (id `IRPT_BCKEND-S158-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- measured by 1.0.0_SA_CTO 101946 on the live plane: 1 scheduler (cot-bd-session-daily-et, ENABLED, cron(30 7) America/New_York) and 5 document runs read (Success 09-16; Failed 09-24, 09-25, 09-26, 09-27).
comp-iam: DECLARED-NOT-APPLICABLE -- the order changes no IAM policy; the document's existing role writes the session secret.
comp-adversary: RUN -- read ssm.tf:49-69 at HEAD: 1 step, set -e precedes the log upload, so 4 of 4 failed runs left no log in S3.
lane: the <paths> block IS the grant; no open order holds these files.
</preflight>

Seating: `0.0.0_AB_MSTR` seats `0.6.2_AE_PartnerETL~S` on this order's commit (101975).
