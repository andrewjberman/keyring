# TO NFRA_CTLPLN.TO-CT-a-1 -- workstream ACCESS round 1 CT-a-1: dell2 may send the resident command documents to one host, and nothing else

<to_id>NFRA_CTLPLN.TO-CT-a-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~14</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>ACCESS</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-a-1` (`decompositions/NFRA_CTLPLN_DECOMP.access1.md`) | **outcome_ref:** FWD-10 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`CT-a-1`, the CTO's ruling (msg 106138; `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULINGS_FOR_THE_DELLS_20261007_1000Z.md`
section 1), verbatim: "The dell2 user gets `ssm:SendCommand` on instance `i-0167fd745ad906a66` alone, with the resident command
documents alone, plus the read actions that return a command's result. Not the AWS shell-script document, not the export render's
documents, no other instance." And what the signature must be able to say: "a command sent to a host runs as the host's own role.
Scoped to documents whose text is fixed in the repository, the dell2 user can run what those documents run and nothing else; a
document that takes a free-text command parameter is a shell on that role and is OUT of the grant. The cell's first read is each
resident document's parameters." You write the policy and prove it by derivation and simulation. You APPLY NOTHING and SEND NOTHING.

**What exists:** the Terraform root `infra/aws/terraform/nfra-ctlpln-identity/` (the two Dell users; per-user bus policies
`dell1_bus_policy.json` / `dell2_bus_policy.json` attached with `aws_iam_user_policy_attachment`; group policies; `tests/simulate_policy.py`
with five blocks today, LAST line `POLICY-SIM allowed_ok=22/22 denied_ok=19/19 passrole_ok=5/5 protected_ok=8/8 respol_ok=11/11 all_ok=True`;
`tests/check_identity.py`, `names_from_builder=8/8`). SSM command documents are declared as `resource "aws_ssm_document"` in several
roots; under `infra/aws/terraform/investor-reporting/` there are `ycharts/ssm.tf` (2 documents) and `export/ssm.tf` (1). The instance
id occurs in `investor-reporting/ycharts/resident.tf`.

**FIRST READ -- `tests/derive_ssm_documents.py` (it is the half of the deliverable a senior seat signs on):**
- List EVERY `aws_ssm_document` declared under `infra/aws/terraform/` (print the count; 16 in 9 files at the cut). For each: its
  Terraform address, its resolved `name` (literal, or resolved from locals in the same root; `UNRESOLVED` is counted), its
  `document_type`, where its content comes from (inline, `file()`, `templatefile()`), and its PARAMETERS parsed from the content:
  each parameter's name, type, default, `allowedValues` / `allowedPattern` if any.
- Find where each parameter is USED in the document's steps. A parameter is `FREE-TEXT-COMMAND` when its value is interpolated into a
  shell or PowerShell command line, a script body, a `commands` / `runCommand` list, an interpreter argument, a path that is then
  executed, or an environment variable a fixed script evaluates, AND it is not constrained by `allowedValues` or by an
  `allowedPattern` that excludes shell metacharacters and spaces. A parameter that only selects among fixed branches, or is a
  constrained identifier (a date, a firm code from an enumerated list, a digest), is `CONSTRAINED`. When you cannot tell, the
  parameter is `UNSURE` and the document is treated as free-text (OUT). Print your reasoning in one line per parameter, quoting the
  step line (file:line).
- Classify each document: `RESIDENT-FIXED` (it targets the resident host's work -- declared in `investor-reporting/ycharts/`, or its
  name or description says resident -- AND it has no `FREE-TEXT-COMMAND` or `UNSURE` parameter); `RESIDENT-FREE-TEXT` (resident, but
  it takes a free-text command: OUT, named in your report); `EXPORT-RENDER` (declared in `investor-reporting/export/`: OUT by the
  ruling); `OTHER` (every other document: OUT).
- Also read which documents the instance is the declared target of (associations, EventBridge targets, Lambda code that calls
  `send_command` with a document name: search the investor-reporting root and `infra/aws/lambda/investor-reporting/` for
  `DocumentName` / `send_command`), and print any document sent to that instance today that your classification did NOT call resident.
- LAST line `SSM-DOCS declared=<n> unresolved=<u> resident_fixed=<a> resident_free_text=<b> export_render=<c> other=<d> unsure_params=<p> in_policy=<k> ok=<True|False>`,
  `ok=True` only when `u == 0`, `a + b + c + d == n`, and the policy of step 2 names EXACTLY the `RESIDENT-FIXED` documents (`k == a`).

**Build:**

1. Nothing in the three group policy files changes.
2. `dell2_ssm_policy.json` -- a per-user managed policy, name `cloudops-dell2-agent-ssm-policy`
   (`lib/opal_naming.name('cloudops', None, 'dell2-agent-ssm', 'policy')`), tagged `DisplayName = "DellBoxes"`, attached to
   `cloudops-dell2-agent-user` ONLY (an `aws_iam_user_policy_attachment`, as the bus policy is). Statements:
   - `SendResidentDocumentsToResidentHost`: Allow `ssm:SendCommand` on EXACTLY these resources: the instance ARN
     `arn:aws:ec2:us-east-1:313476888478:instance/i-0167fd745ad906a66` and one document ARN per `RESIDENT-FIXED` document
     (`arn:aws:ssm:us-east-1:313476888478:document/<name>`). No wildcard in any resource. (`ssm:SendCommand` is authorised against
     BOTH the document and the target; an Allow that names only the instance would permit any document.)
   - `ReadCommandResults`: Allow `ssm:GetCommandInvocation`, `ssm:ListCommandInvocations`, `ssm:ListCommands` on `*` (these actions do
     not support resource-level scoping; say so in a comment-free way in your report, since JSON has no comments) and
     `ssm:DescribeInstanceInformation` on `*`.
   - `DenyShellDocuments`: Deny `ssm:SendCommand` and `ssm:StartSession` on
     `arn:aws:ssm:*::document/AWS-RunShellScript`, `arn:aws:ssm:*::document/AWS-RunPowerShellScript`,
     `arn:aws:ssm:*::document/AWS-RunRemoteScript`, `arn:aws:ssm:*::document/AWS-StartInteractiveCommand`,
     `arn:aws:ssm:*::document/AWS-StartNonInteractiveCommand`, `arn:aws:ssm:*::document/AWS-StartSSHSession` and
     `arn:aws:ssm:*::document/AWS-StartPortForwardingSession*`; and Deny `ssm:SendCommand` on every `EXPORT-RENDER` and
     `RESIDENT-FREE-TEXT` document's ARN by name.
   The document list in the policy is RENDERED by the derive script (`--write`), never typed; `--check` compares.
   The create policy already lets a Dell `ssm:UpdateDocument`: a Dell that can rewrite a resident document's text can run anything
   through this grant. Add to THIS policy a `DenyRewriteOfGrantedDocuments` statement: Deny `ssm:UpdateDocument`,
   `ssm:UpdateDocumentDefaultVersion`, `ssm:DeleteDocument`, `ssm:ModifyDocumentPermission` and `ssm:CreateDocument` on the
   `RESIDENT-FIXED` document ARNs. File ONE surprise row saying that the same hole is open for dell1 through the group's create policy
   and for both Dells on the instance's other inputs you can name (for example an S3 script a fixed document downloads and runs:
   check each `RESIDENT-FIXED` document for a script fetched at run time and name the object and whether a Dell can write it).
3. `iam.tf`: the policy resource and its one attachment.
4. `tests/simulate_policy.py` -- a sixth block, evaluated for DELL2's effective set (the group policies, `dell2_bus_policy.json` and
   `dell2_ssm_policy.json` in one call) and, for the negative arm, DELL1's (which lacks the new policy):
   dell2 `ssm:SendCommand` with resources [instance ARN, one `RESIDENT-FIXED` document ARN] -> allowed (one arm per fixed document,
   at most three; say how many exist); dell2 `ssm:SendCommand` with [instance ARN, `AWS-RunShellScript`] -> explicitDeny; dell2 with
   [instance ARN, the export render document] -> denied; dell2 with [ANOTHER instance ARN, a fixed document] -> denied; dell2
   `ssm:GetCommandInvocation` -> allowed; dell2 `ssm:UpdateDocument` on a fixed document -> explicitDeny; dell1 `ssm:SendCommand` with
   [instance ARN, a fixed document] -> denied. Print one line per arm. LAST line keeps the five existing fields and adds
   `ssm_ok=<k>/<n>`: `POLICY-SIM allowed_ok=22/22 denied_ok=19/19 passrole_ok=5/5 protected_ok=8/8 respol_ok=11/11 ssm_ok=<k>/<n> all_ok=<True|False>`.
   (`simulate-custom-policy` takes one resource ARN per evaluation for most actions; for `ssm:SendCommand` pass both ARNs in
   `ResourceArns` and read the per-resource results. If the simulator cannot evaluate the two-resource form, evaluate each resource
   separately, require BOTH allowed for an allowed arm, and say so.)
5. `tests/check_identity.py`: the name comparison covers the new policy (9 names) and its size.

### ACCEPTANCE

<criterion id="CTa1-AC1" cell_refs="CT-a-1"><invocation>python infra/aws/terraform/nfra-ctlpln-identity/tests/derive_ssm_documents.py --check</invocation><expect>unresolved=0</expect></criterion>
`CTa1-AC1` -- every declared command document was read and classified, and the policy names exactly the fixed resident ones. The same
line must read `ok=True`, stated in the proof row, with `unsure_params` reported.

<criterion id="CTa1-AC2" cell_refs="CT-a-1"><invocation>python infra/aws/terraform/nfra-ctlpln-identity/tests/simulate_policy.py</invocation><expect>respol_ok=11/11 ssm_ok=</expect></criterion>
`CTa1-AC2` -- the cloud's evaluator lets dell2 send a fixed resident document to the one host and read the result, and refuses the
shell document, the export render document, another instance, a rewrite of a granted document, and dell1. The same line must read
`all_ok=True` with `ssm_ok` at its full count; the refusals are the control arms of the allow.

<criterion id="CTa1-AC3" cell_refs="CT-a-1"><invocation>python infra/aws/terraform/nfra-ctlpln-identity/tests/check_identity.py</invocation><expect>names_from_builder=9/9 policy_size_ok=True ok=True</expect></criterion>
`CTa1-AC3` -- the control: the root validates, nine names are the builder's, every document fits the limit.

<expected_criteria>CTa1-AC1,CTa1-AC2,CTa1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No apply, no `terraform plan` against the backend, no IAM write, no `ssm send-command`, no session, no call that touches the
  instance.** AWS calls allowed, read-only: `iam:SimulateCustomPolicy`. The documents are read from the REPOSITORY (the Terraform and
  the files it loads), not from the account: say plainly in your report that the live documents were not compared.
- If NO document classifies `RESIDENT-FIXED`, do not widen the rule: write the policy with the read statement and the Deny statements
  only, file a BLOCKING row with the table, and report. A grant of nothing is the correct result of that read.
- Do not type a firm's name into any file outside a `tests/` directory. If a document's name carries one and the commit gate refuses
  the policy file, do not override: file a BLOCKING row and stop.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_CTLPLN-W14-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or the
  expected value.

<paths>
infra/aws/terraform/nfra-ctlpln-identity/dell2_ssm_policy.json
infra/aws/terraform/nfra-ctlpln-identity/iam.tf
infra/aws/terraform/nfra-ctlpln-identity/tests/derive_ssm_documents.py
infra/aws/terraform/nfra-ctlpln-identity/tests/simulate_policy.py
infra/aws/terraform/nfra-ctlpln-identity/tests/check_identity.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit: the three group policy files, the bus policies, every `.tf` and loaded
script under `infra/aws/terraform/` and `infra/aws/lambda/investor-reporting/`, `lib/opal_naming.py`.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.access1.md</decomp_doc> (workstream ACCESS, round 1), cell `CT-a-1`.
<owned_cells>CT-a-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CTa1-AC1, CTa1-AC2, CTa1-AC3. Instance at `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~14/NFRA_CTLPLN.TO-CT-a-1.dell2-sendcommand-grant.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CTa1-AC1,CTa1-AC2,CTa1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the three last lines; THE DOCUMENT TABLE (address, name, class, each parameter with its class and the step line that
decided it); the documents in the policy; every document sent to the instance today that is not in it; any run-time script a granted
document fetches and who can write it; each arm of the sixth simulation block with its decision; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule.
comp-iam: RUN at the cut by the simulation criterion (CTa1-AC2), a sixth block with five refusal arms; base read `POLICY-SIM allowed_ok=22/22 denied_ok=19/19 passrole_ok=5/5 protected_ok=8/8 respol_ok=11/11 all_ok=True` (the round-4 drain's read of CT-d-5); `comp-iam gaps` after the apply is the issuer's.
comp-adversary: RUN -- a shell on the host's role through a free-text parameter (every parameter classified with the step line that uses it; UNSURE is OUT); the AWS shell documents (explicit Deny by name); a grant that names only the instance and so admits any document (both resources named, no wildcard, and the other-document and other-instance arms); rewriting a granted document and then sending it (Deny on update, delete and permission changes of the granted documents; the same hole for dell1 and for run-time scripts rowed); dell1 gaining the grant (per-user attachment; the dell1 arm); BLIND: the live documents were not compared to the repository, and the host role's own reach is not read here -- both go in the half request.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: CTO msg 106138; `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULINGS_FOR_THE_DELLS_20261007_1000Z.md` section 1 (read in
the working tree at the cut; its commit was pending); decomposition ACCESS round 1. Base dry-run at the cut: CTa1-AC1 base FAIL as
expected (no script); CTa1-AC2 base FAIL as expected (no `ssm_ok`); CTa1-AC3 base FAIL as expected (8/8 at the base).
