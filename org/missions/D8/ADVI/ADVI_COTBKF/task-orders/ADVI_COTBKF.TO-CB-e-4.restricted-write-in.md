# TO ADVI_COTBKF.TO-CB-e-4 -- round 5 CB-e-4: the C-RESTRICTED apply write-in, one valid role request and its note

<to_id>ADVI_COTBKF.TO-CB-e-4</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~19</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-e-4` (`decompositions/ADVI_COTBKF_DECOMP.round5.md`) |
**outcome_ref:** FWD-7, FWD-4, FWD-2 (row S7) | **depends_on:** none

---

## WORKER FACE

### THE CELL

`CB-e-4`: the CRM records of the Commonwealth delivery may land only behind **C-RESTRICTED**: a restricted prefix in the Cottonwood
firm bucket that only Andrew's console user and one break-glass role may read or write. The policy and the role are written and merged
in `infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf` (lines 177-275: statements `DenyRestrictedReadExceptReaders`,
`DenyRestrictedListExceptReaders`, `DenyRestrictedWriteExceptBreakglass` on prefix `commonwealth/cottonwood/bronze/crm/`; role
`cloudops-cot-restricted-breakglass-role` built by module `opal_name_restricted_breakglass`, trust = the console user only; inline policy
`restricted-prefix-get-put-list`). **Nothing is applied.** This box (dell2) never creates, edits or attaches a role or a bucket policy:
it WRITES IN, and the laptop applies.

You write that write-in, two artifacts:

1. **One role request on dell2** with the estate's writer, `org/devices/role_request.py` (run `python org/devices/role_request.py write --help`
   and read the module's header first). Run it with `AGENTBUS_DEVICE=dell2` and `OPAL_AGENT_SERIAL=0.9.0_WK_ADVI_COTBKF~19`, project
   `ADVI_COTBKF`, Terraform root `infra/aws/terraform/shared-infra`, the resource the break-glass role, and one `--permission` per action
   of the role's inline policy and of the bucket statements, each tied to its line in `s3-lgic-firm-buckets.tf` as
   `<action>,<arn>,<path>:<line>`. The real `write` (not `--dry-run`) records the request under `org/devices/role_requests/dell2/` and
   sends one bus line to the laptop; that send is the write-in's purpose. Run `--dry-run` first until it prints no REFUSED line.
2. **The note** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~19/C_RESTRICTED_WRITE_IN.md`: the request id and path;
   the bucket and the prefix; the role; the three bucket statements and the role policy, each with its file line; and the command the
   laptop must run immediately before the apply, `python infra/aws/terraform/shared-infra/tests/check_restricted_prefix.py` (the CB4d4-AC1
   check; it needs terraform and the real backend, which dell2 lacks -- row S7); and the order of acts: policy applied, check re-run,
   then the single CRM landing by Andrew through the role on his word.

**If the writer refuses a shape** (for example, an assuming principal that is a user rather than a service): do NOT edit the writer or
its schema (they are NFRA_CTLPLN's). Write the request as close as the writer admits, put the gap in the note, and file a surprise row.

### ACCEPTANCE

<criterion id="CB5e4-AC1" cell_refs="CB-e-4"><invocation>python "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/checks/check_e4_write_in.py"</invocation><expect>E4-WRITE-IN request_valid=True cites_policy_file=True note_carries_ac1=True</expect></criterion>
`CB5e4-AC1` -- the request validates through the writer's own validator, cites the policy file, and the note carries the pre-apply check.

<expected_criteria>CB5e4-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **No AWS call, no terraform, no IAM or S3 act.** The writer makes none; you make none.
- **Refusal clause.** If the criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-W19-S<k>`), and do not weaken the check.

<paths>
org/devices/role_requests/dell2/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round5.md</decomp_doc> (round 5), cell `CB-e-4`.
<owned_cells>CB-e-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB5e4-AC1. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~19/ADVI_COTBKF.TO-CB-e-4.restricted-write-in.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB5e4-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the request id and path, the validator's line, the E4-WRITE-IN line, any writer refusal and how the note carries it, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-time write-in.
comp-iam: RUN -- the request names 1 role and 3 bucket statements from the merged file; denominator: the policy statements at s3-lgic-firm-buckets.tf:177-275; BLIND: the live bucket policy and live IAM (not applied; read by the laptop at apply).
comp-adversary: RUN -- the writer and schema are another project's and are not edited; the bus send is the designed mechanism; BLIND: the laptop's answer (mark-applied/refused).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-4 analysis @e363a194ed, E4; row S7; laptop ruling 1 of 07:4xZ (access by write-in).
