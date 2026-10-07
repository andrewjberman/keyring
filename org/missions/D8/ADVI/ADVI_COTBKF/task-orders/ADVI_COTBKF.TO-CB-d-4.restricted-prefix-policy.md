# TO ADVI_COTBKF.TO-CB-d-4 -- round 4 CB-d-4: C-RESTRICTED -- the Cottonwood bucket's restricted-prefix statements and the break-glass role, planned and simulated

<to_id>ADVI_COTBKF.TO-CB-d-4</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~15</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>~C</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `CB-d-4` (`decompositions/ADVI_COTBKF_DECOMP.round4.md`) | **outcome_ref:** FWD-7 |
**depends_on:** none (R20 X15 landed @3d5dd4bf52; CTO ruling msg 105951; lane ADVI_COTBKF_C granted @b573ddee69)

---

## WORKER FACE

### THE CELL

`CB-d-4`, FWD-7: "tax numbers, dates of birth, driver's license and passport numbers exist only where Andrew said they may; anyone can list
those places and who can read each; a person without that right who tries is refused." The CRM zip that carries them goes to ONE prefix of
the Cottonwood firm bucket, and no byte is written before that prefix's policy is live. You write the Terraform for that policy and the
break-glass role, and prove both with a targeted plan and AWS's own policy simulator. You APPLY NOTHING: the apply is the file's owner's,
under a never-widen pair.

**Fixed by the record (never re-derived, never typed beyond these):**
- **The key** (R20 X15, `infra/logic/06_CONFORMANCE_LEDGER.md` section 6): `s3://opal-data-cottonwood/commonwealth/cottonwood/bronze/crm/date=2026-06-23/CRM_CottonwoodCapitalAdvisors.zip`;
  the RESTRICTED PREFIX is `commonwealth/cottonwood/bronze/crm/` -- which is `lib/opal_naming.key('commonwealth', 'cottonwood', 'bronze',
  'crm', ...)`'s prefix with only the bucket departing. It is empty today.
- **Readers (CTO ruling msg 105951):** IAM user `Andrew_Berman_Console` (Andrew's human console identity: console login, 0 access keys) and
  ONE new break-glass role, name `name('cloudops', <cottonwood scope>, 'restricted-breakglass', 'role')` ->
  `cloudops-cot-restricted-breakglass-role` (compute it through `infra/aws/terraform/modules/opal_name`, never typed), whose trust policy
  admits ONLY `Andrew_Berman_Console`, with an identity policy allowing get/put/list on the restricted prefix only. The single landing write
  goes through that role, by Andrew, on his word.
- **Refused:** IAM user `Andrew_Berman` -- every agent shell on the laptop runs as it -- and every other principal.

**The file** `infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf` (read it whole first): `aws_s3_bucket_policy.lgic_firm` is ONE
for_each policy over `local.lgic_managed_firm_buckets` (today `inflection` and `cottonwood`) with one statement, `DenyForeignFirmPrincipals`;
the live `opal-data-cottonwood` policy holds that same one statement. Add, for the COTTONWOOD row ONLY (the inflection policy's rendered JSON
must not change by a byte):
1. `DenyRestrictedReadExceptReaders` -- Deny, `Principal *`, `s3:GetObject*` (and `GetObjectVersion*`, `GetObjectAttributes`,
   `GetObjectTagging`) on `<bucket arn>/commonwealth/cottonwood/bronze/crm/*`, condition `ArnNotLike aws:PrincipalArn` = [the console
   user's ARN, the break-glass role's ARN].
2. `DenyRestrictedListExceptReaders` -- Deny `s3:ListBucket*` on the bucket with `StringLike s3:prefix` the restricted prefix, same
   `ArnNotLike` condition.
3. `DenyRestrictedWriteExceptBreakglass` -- Deny `s3:PutObject*`, `s3:DeleteObject*`, `s3:RestoreObject` on the prefix, condition
   `ArnNotLike aws:PrincipalArn` = [the break-glass role's ARN] only.
Select the cottonwood row from the registry data the file already reads (`scopes.json`), not by a typed firm token if the naming gate
refuses one (say which you used). The role (`aws_iam_role` + its policy) goes in the same file. Read the console user's ARN with a
`data "aws_iam_user"` lookup.

**The check** `infra/aws/terraform/shared-infra/tests/check_restricted_prefix.py`:
- runs `terraform -chdir=infra/aws/terraform/shared-infra init -input=false` (the real backend, read-only) and
  `terraform plan -input=false -lock=false -no-color -out=<tmp> -target=aws_s3_bucket_policy.lgic_firm -target=<the role and its policy>`,
  then `terraform show -json <tmp>`; counts add / change / destroy; asserts the changed policy is the cottonwood row only
  (`other_buckets_changed` = how many other bucket policies' rendered JSON differ);
- takes the planned cottonwood policy JSON and calls `iam.simulate_custom_policy` (read-only) with an allow-all identity policy and the
  bucket policy as `ResourcePolicy`, `CallerArn` = an IAM USER ARN, and `ContextEntries` setting `aws:PrincipalArn` (the simulator takes
  only a user as `CallerArn`; the role is simulated through the context key): `Andrew_Berman` read (GetObject) and write (PutObject) on a
  key under the prefix -> denied; `Andrew_Berman_Console` read -> allowed; the break-glass role read and write -> allowed; `Andrew_Berman`
  read of a key OUTSIDE the prefix -> allowed (the difference control: the statements bind the prefix, not the bucket);
- prints as the LAST line exactly:
  `RESTRICTED-CHECK agent_read=<denied|allowed> agent_write=<..> console_read=<..> breakglass_read=<..> breakglass_write=<..> agent_read_outside=<..> other_buckets_changed=<k> plan_change=<c> plan_destroy=<d> plan_add=<a>`.

### ACCEPTANCE

<criterion id="CB4d4-AC1" cell_refs="CB-d-4"><invocation>python infra/aws/terraform/shared-infra/tests/check_restricted_prefix.py</invocation><expect>RESTRICTED-CHECK agent_read=denied agent_write=denied console_read=allowed breakglass_read=allowed breakglass_write=allowed agent_read_outside=allowed other_buckets_changed=0 plan_change=1 plan_destroy=0</expect></criterion>
`CB4d4-AC1` -- the agents' identity is refused on the prefix and only there, the two readers are admitted, only Cottonwood's policy changes.

<criterion id="CB4d4-AC2" cell_refs="CB-d-4" judgment="true"/>
`CB4d4-AC2` -- JUDGMENT, graded by `3.0.0_SA_CVO` at L9: a person can list, from the policy and the role, every principal that can read the
CRM prefix (FWD-7's "anyone can list those places and who can read each").

<expected_criteria>CB4d4-AC1,CB4d4-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Terraform's `.terraform/` and plan files stay
  uncommitted.
- **No apply, no `terraform apply`, no state verb, no IAM write.** AWS calls allowed: the plan's reads and `iam:SimulateCustomPolicy`.
- **The inflection policy must not change**, and no statement may touch a key outside the restricted prefix.
- **Never write to the restricted prefix**, and never read a CRM byte.
- **Refusal clause.** If a criterion cannot be met as written (for example the shared-infra plan shows drift on a targeted resource you did
  not cause), stop, write the plan output in your report and a surprise row (id `ADVI_COTBKF-W15-S<k>`), and do not weaken the check.

<paths>
infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf
infra/aws/terraform/shared-infra/tests/check_restricted_prefix.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round4.md</decomp_doc> (round 4), cell `CB-d-4`.
<owned_cells>CB-d-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB4d4-AC1, CB4d4-AC2 (judgment: UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO; never PASS or FAIL).
Instance at `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~15/ADVI_COTBKF.TO-CB-d-4.restricted-prefix-policy.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB4d4-AC1,CB4d4-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the `RESTRICTED-CHECK` line, the plan summary with every targeted address, the three statements and the role's trust and
identity policies in brief, how the cottonwood row was selected, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule.
comp-iam: RUN -- denominator: 2 principals admitted of the 7 IAM users and every role in the account (list-users read 04:0xZ: agentbus-alyssa01-fleet-alyssa-user, Andrew_Berman, Andrew_Berman_Console, github-actions-portal, opal-portal-dashboard, Opal_Terminal, one external user); adds one role (trust: one human user) and deny statements on one prefix of one bucket; simulated, not applied. BLIND: the account root user (a bucket policy cannot bind it) and service principals.
comp-adversary: RUN -- the agents run as Andrew_Berman (measured 04:0xZ, sts get-caller-identity), so "Andrew alone" = the console user; the difference control (read outside the prefix allowed); other firm's policy byte-identical; BLIND: the account root user (a bucket policy cannot bind it) -- named in the report.
lane: the <paths> block IS the grant (worker RULING 1); lane ADVI_COTBKF_C @b573ddee69.
</preflight>

Source: PRD C-RESTRICTED, C-SENSITIVE; R20 X14/X15 (@3d5dd4bf52); CTO msgs 105948, 105951, 105964; decomposition round 4 (measured constraint 6).
