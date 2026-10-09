# TO NFRA_CTLPLN.TO-CT-a-1 -- workstream ACCESS round 1 CT-a-1: dell2 may send the resident command documents to one host, and nothing else

<to_id>NFRA_CTLPLN.TO-CT-a-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~14</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
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

<criterion id="CTa1-AC2" cell_refs="CT-a-1"><invocation>python infra/aws/terraform/nfra-ctlpln-identity/tests/simulate_policy.py</invocation><expect>walker_ok=[0-9]+/[0-9]+ iamw_ok=[0-9]+/[0-9]+ planread_ok=[0-9]+/[0-9]+ sendcmd_ok=[0-9]+/[0-9]+ shellwin_ok=[0-9]+/[0-9]+ routes_freed=[0-9]+/[0-9]+ routes_still_refused=[0-9]+ vendor_ok=[0-9]+/[0-9]+ all_ok=True</expect></criterion>
`CTa1-AC2` -- the cloud's evaluator lets dell2 send a fixed resident document to the one host and read the result, and refuses the
shell document, the export render document, another instance, a rewrite of a granted document, and dell1. The same line must read
`all_ok=True` with `ssm_ok` at its full count; the refusals are the control arms of the allow.

<criterion id="CTa1-AC3" cell_refs="CT-a-1"><invocation>python infra/aws/terraform/nfra-ctlpln-identity/tests/check_identity.py</invocation><expect>names_from_builder=9/9 policy_size_ok=True ok=True</expect></criterion>
`CTa1-AC3` -- the control: the root validates, nine names are the builder's, every document fits the limit.

<expected_criteria>CTa1-AC1,CTa1-AC2,CTa1-AC3,CTa1-AC4,CTa1-AC5,CTa1-AC6</expected_criteria>

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
infra/aws/terraform/nfra-ctlpln-identity/tests/derive_reached_roles.py
infra/aws/terraform/nfra-ctlpln-identity/tests/reached_roles_census.json
infra/aws/terraform/nfra-ctlpln-identity/dell_deploy_policy.json
infra/aws/terraform/nfra-ctlpln-identity/routes.tf
infra/aws/terraform/nfra-ctlpln-identity/modules/routes_policy/
infra/aws/terraform/nfra-ctlpln-identity/tests/render_routes_policy.py
infra/aws/terraform/nfra-ctlpln-identity/protected_functions.json
infra/aws/terraform/nfra-ctlpln-identity/tests/derive_protected_functions.py
infra/aws/terraform/nfra-ctlpln-identity/tests/simulate_policy.py
infra/aws/terraform/nfra-ctlpln-identity/tests/check_identity.py
infra/aws/terraform/transcripts/main.tf
infra/aws/terraform/transcripts/tests/
infra/aws/terraform/nfra-ctlpln-identity/dell_vendor_secrets_policy.json
infra/aws/terraform/nfra-ctlpln-identity/tests/derive_vendor_secrets.py
infra/aws/terraform/nfra-ctlpln-identity/tests/vendor_secrets_census.json
infra/aws/terraform/nfra-ctlpln-identity/dell_respol_policy.json
infra/aws/terraform/nfra-ctlpln-identity/dell_create_policy.json
infra/aws/terraform/nfra-ctlpln-identity/dell_iam_roles_policy.json
infra/aws/terraform/nfra-ctlpln-identity/dell_planreads_policy.json
infra/aws/terraform/nfra-ctlpln-identity/tests/derive_plan_reads.py
infra/aws/terraform/nfra-ctlpln-identity/tests/plan_reads_census.json
infra/aws/terraform/nfra-ctlpln-identity/tests/derive_respol_actions.py
infra/aws/terraform/nfra-ctlpln-identity/tests/derive_resource_kinds.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/terraform/nfra-ctlpln-identity/tests/render_passrole.py
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

## AMENDMENT 1 (2.0.0_SA_COO~C, 2026-10-07 ~10:4xZ) -- REOPENED: the boundary is the ROLE reached; a role census, then targeted Deny statements

The issuer reopens its own order (`complete` -> `in_progress`); the slot is re-seated and commits 8b260a787e and 3357889f21 are
inherited state. Authority: `1.0.0_SA_CTO` msg 106158 and
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_NFRA_CTLPLN_W14_S2_THE_BOUNDARY_IS_THE_ROLE_REACHED_20261007.md` @ce594ed1c9.
READ THAT FILE IN FULL FIRST: it is short and it is the specification. Its points, verbatim where it matters:
- "A. The 10:0xZ limit is WITHDRAWN. It was aimed at the wrong object ... To deploy a thing IS to act as its role."
- "B. ... the question that decides every route is one question about the ROLE at the end of it: can that role write IAM, write or
  stop the audit trail, or delete production data?"
- "C. The census, read-only ... first act: every role a Dell can execute as through an action its two policies allow -- the execution
  role of each function it may update, the task role of each task it may register or run, the instance role of each host that runs a
  command document it may write or downloads an artifact prefix it may put to. For each role: does any attached or inline policy
  allow an IAM write, a CloudTrail write, or a delete on `opal-data-*`. Print N of N. Where the answer is YES: a Deny for the Dell
  group on the route to that role (that function, that document, that prefix), added to the pending resource-policy apply. That set
  REPLACES the name-based list of ten protected functions ... wherever the two differ; the access-deciding functions stay protected
  in any case. Where the answer is NO: the route is the deploy ability, accepted ... No blanket Deny on document writes or on the
  `ec2/` prefix."
- "D. The dell2 command grant STANDS, on the census. `ssm:SendCommand` for the dell2 user on instance `i-0167fd745ad906a66` with the
  two resident documents as they are, free-text parameters included, PROVIDED the census reads NO for that host's instance role. If
  it reads YES, the grant waits and the role is narrowed first, in the project that owns it."
Gate limb: none graded this modification. WHERE THIS AMENDMENT AND THE FACE DIFFER, THIS AMENDMENT GOVERNS. The classification of
documents by free-text parameters built above STAYS as a record (it is true); it no longer decides the grant.

**THE WORK, in this order. Step 1 is the urgent deliverable: commit it as soon as it is done, before steps 2 to 4.**

1. `tests/derive_reached_roles.py` -- THE CENSUS, read-only against the account. `--live` (default) and `--from-file <json>`.
   - **Routes.** (a) FUNCTIONS: every Lambda function in every region the account uses (re-use the listing method of
     `tests/derive_protected_functions.py`; import it) -> its execution role (`Role`). Mark each function `UPDATABLE` or
     `DENIED-TODAY` by the Dell group's current Deny (`protected_functions.json`). (b) TASKS: every ACTIVE ECS task definition (latest
     revision per family; `ecs list-task-definition-families --status ACTIVE`, `describe-task-definition`) -> `taskRoleArn` and
     `executionRoleArn` (a Dell may `ecs:RunTask` an existing definition with a command override, and `ecs:RegisterTaskDefinition`;
     note per route that `iam:PassRole` is denied to a Dell today, so registering a NEW definition with a role is refused and
     running an EXISTING one is not). (c) HOSTS: every EC2 instance (`ec2 describe-instances`, all states but terminated) -> its
     instance profile -> the role(s) in it (`iam get-instance-profile`). For each host also record WHICH route reaches it, by
     reading the repository: the command documents that target it (from `tests/derive_ssm_documents.py`'s reading and the Terraform
     that names the instance) and the S3 artifact prefixes its documents or bootstrap download and run. A host no document or prefix
     reaches is listed as `NO-ROUTE-FOUND` and still censused (the route search is the weaker read; the role read is the control).
     Print the count per route kind and the count of DISTINCT roles: that count is N.
   - **Per role, the three questions, answered by the cloud's own evaluator:** `iam simulate-principal-policy` with
     `--policy-source-arn <role ARN>` for: IAM WRITE -- `iam:CreateUser`, `iam:CreateAccessKey`, `iam:AttachRolePolicy`,
     `iam:PutRolePolicy`, `iam:CreateRole`, `iam:UpdateAssumeRolePolicy`, `iam:PassRole` (resource `*`); TRAIL WRITE --
     `cloudtrail:StopLogging`, `cloudtrail:DeleteTrail`, `cloudtrail:UpdateTrail`, `cloudtrail:PutEventSelectors` (resource `*`);
     DATA DELETE -- `s3:DeleteObject` on `arn:aws:s3:::opal-data-assets/x`, on one object ARN in EACH other `opal-data-*` bucket the
     account has (list them: `s3api list-buckets`; this is 24 buckets at the last census), `s3:DeleteBucket` on one, and
     `dynamodb:DeleteTable`, `rds:DeleteDBInstance` (resource `*`). A role is `YES-IAM` / `YES-TRAIL` / `YES-DELETE` when ANY action of
     that class returns `allowed`; print the allowed actions (and for deletes, which buckets). A simulator call that errors is
     `UNREAD`, counted, never `NO`. Batch the action names per call; bound the whole run (it may be several hundred calls: print
     progress, and if a full `--live` run cannot finish inside 120 s, run it once outside the bound, save the result, and run the
     criteria on the saved file under the bound -- say so).
   - **Say what the evaluator cannot see:** `simulate-principal-policy` evaluates the role's identity policies (and a permissions
     boundary if you pass it); it does not apply resource policies on the target (a bucket fence may still refuse) or organisation
     service control policies. So a `YES` is "the role's own policies allow it" and a `NO` is firm for identity policy. Print that
     caveat once in the output and put it in your report.
   - Save everything to `tests/reached_roles_census.json` (under `tests/`: it names functions, hosts and buckets). LAST line
     `ROLE-CENSUS functions=<f> tasks=<t> hosts=<h> roles=<n> read=<r> unread=<u> yes_iam=<a> yes_trail=<b> yes_delete=<c> yes_any=<y> no=<z> resident_host_role=<YES-..|NO|UNREAD|NOT-FOUND> ok=<True|False>`,
     `ok=True` only when `r == n` and `u == 0`. `resident_host_role` is the verdict for the instance role of `i-0167fd745ad906a66`.
   COMMIT STEP 1 (the script, the saved census, a short table `REACHED_ROLES_CENSUS.md` in your deliverables folder: per YES role, the
   routes that reach it and what it may do) BEFORE going on. Then continue.
2. THE TARGETED DENY, rendered from the census (`--write` / `--check`), never typed: one statement set `DenyRoutesToPrivilegedRoles`
   for the Dell GROUP naming, for each `YES` role, the routes to it: the functions whose execution role it is (the Lambda write
   actions of the existing `DenyProtectedFunctions`), the task definition families whose task role it is (`ecs:RunTask`,
   `ecs:RegisterTaskDefinition`, `ecs:UpdateService` on that family's ARNs), the command documents that target a host whose role it
   is (`ssm:UpdateDocument`, `ssm:UpdateDocumentDefaultVersion`, `ssm:CreateDocument`, `ssm:DeleteDocument`, `ssm:SendCommand` on
   those document ARNs), and the artifact prefixes such a host downloads and runs (`s3:PutObject` on those prefix ARNs only -- never
   a whole bucket and never the whole `ec2/` prefix unless every host under it reads YES; say which).
   - It goes in a NEW group policy `dell_routes_policy.json`, name `cloudops-dell-agent-routes-policy`
     (`lib/opal_naming.name('cloudops', None, 'dell-agent-routes', 'policy')`), tagged `DisplayName = "DellBoxes"`, attached to the
     group. Each policy document must stay within 6,144 characters without whitespace and the group may carry at most 10 managed
     policies: if the set needs MORE THAN TWO such policies, do NOT render it -- stop after step 1, file a BLOCKING row with the
     counts, and report: the form is then the CTO's to rule (for example a Deny by role-owning project prefix).
   - The ten name-based protected functions: the four access-deciding ones ruled in by name and the authorizer target and the five
     edge functions STAY protected "in any case" (the existing `DenyProtectedFunctions` statement is not removed and not edited by
     you); the census set is added beside it. Report the overlap: which of the ten read YES, which read NO.
3. THE dell2 GRANT, by ruling D: IF `resident_host_role` reads `NO`, `dell2_ssm_policy.json` gains
   `SendResidentDocumentsToResidentHost`: Allow `ssm:SendCommand` on exactly the instance ARN and the two resident document ARNs
   (`irpt-ycharts-deploy`, `irpt-ycharts-run`), and those two names leave `DenyShellDocuments` (the AWS shell documents and the
   export render document stay denied). IF it reads `YES-*` or `UNREAD` or `NOT-FOUND`, change nothing in that file and say so:
   the grant waits.
4. `tests/simulate_policy.py`: the sixth block is updated to the outcome of step 3 (if granted: dell2 send of each resident document
   to the instance -> allowed, 2 arms; to another instance -> denied; `AWS-RunShellScript` -> explicitDeny; the export render
   document -> explicitDeny; dell1 -> denied), and a seventh block is added for step 2: for up to three `YES` roles, the Dell's
   route to each is `explicitDeny` (function update; document write; prefix put, as each exists), and for two `NO` roles the route
   stays `allowed`. LAST line adds `routes_ok=<k>/<n>` after `ssm_ok=<k>/<n>`; with no YES role the block reads `routes_ok=0/0` and you
   say so. `tests/check_identity.py`: the name comparison covers the new policy if it exists (10 names) and sizes.

**ACCEPTANCE.** CTa1-AC1 is unchanged. CTa1-AC2's expectation becomes `respol_ok=11/11 ssm_ok=` (unchanged text) and the same line
must read `all_ok=True` with `routes_ok` present. CTa1-AC3's expectation becomes `policy_size_ok=True ok=True`. One criterion is ADDED:

<criterion id="CTa1-AC4" cell_refs="CT-a-1"><invocation>python infra/aws/terraform/nfra-ctlpln-identity/tests/derive_reached_roles.py --from-file infra/aws/terraform/nfra-ctlpln-identity/tests/reached_roles_census.json</invocation><expect>unread=0</expect></criterion>
`CTa1-AC4` -- every role a Dell can execute as was read by the cloud's evaluator, N of N. The same line must read `ok=True`, stated in
the proof row, with the three YES counts and the resident host's verdict reported.

**BOUNDS for this amendment.** Read-only AWS calls only: `iam simulate-principal-policy`, `iam simulate-custom-policy`,
`iam get-instance-profile`, `iam list-attached-role-policies` / `list-role-policies` / `get-role` (to explain a YES), `lambda
list-functions`, `ecs list-task-definition-families`, `ecs describe-task-definition`, `ec2 describe-instances`, `ec2
describe-regions`, `s3api list-buckets`, `sts get-caller-identity`. No write, no send, no run, no apply, no plan against the backend.
Function, host, role and bucket names go only in files under `tests/`, in the rendered policy files (where they must), in
`REACHED_ROLES_CENSUS.md` in your deliverables folder, and in your report. If the commit gate refuses a firm-name string in a policy
file, do NOT override: file a BLOCKING row, keep step 1 committed, and stop. Write a NEW proof instance over the old one covering all
four ids, validate it with `python .tools/proof-of-spec-check.py <instance> CTa1-AC1,CTa1-AC2,CTa1-AC3,CTa1-AC4`, and flip `<status>`
back to `complete` only when all four pass.

## AMENDMENT 2 (2.0.0_SA_COO~C, 2026-10-07 ~11:4xZ) -- steps 2 to 4 in the RULED FORM: Terraform builds the Deny from the census file

The order is `in_progress`; the slot is re-seated and commits d6aed4ab85 (STEP 1, the census) and 6704cbeb93 are inherited state.
Authority: `1.0.0_SA_CTO` msg 106190, verbatim: "Form: (b). Terraform builds the statements from the census JSON, so no policy file
holds a name. Not (a): an R20 entry is for a departure in a name we mint; these 29 lines refer to resources that already exist. Two
conditions: the JSON carries its header (command, read time, 175 of 175), and a plan against a census older than the last change to
those roles is refused by the cell's own check ... the dell2 SendCommand grant on i-0167fd745ad906a66 with the two resident documents
stands ... One half request for the apply: the rendered Deny (31 functions, 12 documents, 5 prefixes) and the dell2 grant together."
Gate limb: none graded this modification. WHERE THIS AMENDMENT AND AMENDMENT 1'S STEPS 2 TO 4 DIFFER, THIS AMENDMENT GOVERNS.
Step 1 is done and stays. NO policy `.json` file names a function, document, prefix or host: `dell_routes_policy.json` is NOT
written (it is removed from the grant).

1. **The census file carries its header.** `tests/reached_roles_census.json` gains, at its top level, a `header` object: the exact
   command that produced it, the UTC read time, `roles_read` and `roles_total` (175 of 175), the account id and the caller identity
   ARN. If the saved file from STEP 1 lacks any of these, add them from STEP 1's own run record (do NOT re-run the 508-second census
   just for the header unless a value cannot be recovered; say which you did).
2. **A pure Terraform module builds the statements:** `modules/routes_policy/` (no provider, no resource: `variables.tf`, `main.tf`
   with locals, `outputs.tf`). Input: the decoded census. Outputs: `functions_policy_json` and `hosts_policy_json` (two policy
   documents, as the earlier render needed two to stay inside 6,144 characters each: one Deny statement set for the function routes,
   one for the document and prefix routes), plus counts (`function_count`, `document_count`, `prefix_count`) and `header`. The route
   set is exactly AMENDMENT 1's step 2: for each role whose verdict is YES, the functions whose execution role it is (the Lambda
   write actions of the existing `DenyProtectedFunctions`), the command documents that target a host whose role it is (the five SSM
   write and send actions), the artifact prefixes such a host downloads and runs (`s3:PutObject` on those prefix ARNs only). No task
   entry is expected (no task role reads YES); the module still handles a non-empty set. Sorted, de-duplicated. A function already
   in `protected_functions.json` may appear in both Deny sets; that is harmless and you say how many overlap.
3. **`routes.tf`** in the root: `module "routes_policy"` fed by `jsondecode(file("${path.module}/tests/reached_roles_census.json"))`;
   two `aws_iam_policy` resources from its two outputs, names from the builder
   (`lib/opal_naming.name('cloudops', None, 'dell-agent-routes-fn', 'policy')` and `... 'dell-agent-routes-host' ...`; if the builder
   refuses a function token, use the nearest it admits and say so), tagged `DisplayName = "DellBoxes"`, each attached to the group.
   The group then carries 5 managed policies (deploy, create, respol, routes-fn, routes-host); the limit is 10.
   A `precondition` (or a `check` block) in the Terraform refuses a plan when the census `header.roles_read != header.roles_total`.
4. **The exact bytes, without the backend:** `tests/render_routes_policy.py` evaluates the SAME module standalone -- a temporary root
   outside the repo with a LOCAL backend and no provider, calling `modules/routes_policy` by absolute path with the census file, then
   `terraform init -backend=false`, and `terraform console` or a plan-free `terraform output` path (find one that needs no provider
   and no AWS call; `terraform console` on a root with only locals and outputs evaluates expressions; say which you used) -- and prints
   the two JSON documents and their character counts. `tests/simulate_policy.py` and `tests/check_identity.py` take the documents
   from this renderer, so what is simulated is what Terraform builds. LAST line of the renderer
   `ROUTES-RENDER functions=<f> documents=<d> prefixes=<p> policies=2 chars=<a>,<b> header_ok=<True|False> ok=<True|False>`.
   Expected counts from the earlier render: 31 functions, 12 documents, 5 prefixes; report what you get and explain any difference.
5. **The freshness check (the CTO's second condition):** `tests/derive_reached_roles.py --check-fresh`: re-reads, live, the SAME
   three questions for every role in the saved census and the role set itself (the function, task and host listings), and compares
   to the saved file. It prints each difference (a role whose verdict changed, a new role, a role gone, a function whose role
   changed) and LAST `CENSUS-FRESH saved=<read time> roles_saved=<n> roles_live=<m> verdict_changes=<v> new_roles=<a> gone_roles=<g> route_changes=<r> fresh=<True|False>`,
   exit non-zero when anything differs. It is slow (about 8 minutes live); it is the APPLIER's pre-plan read, not a 120-second
   criterion. Run it ONCE yourself, outside the bound, and report its last line; if it reads `fresh=False`, regenerate the census
   (`--live`), commit the new file, and say what changed.
6. **The dell2 grant (ruling D, the resident host's role reads NO):** `dell2_ssm_policy.json` gains
   `SendResidentDocumentsToResidentHost`: Allow `ssm:SendCommand` on exactly the instance ARN
   `arn:aws:ec2:us-east-1:313476888478:instance/i-0167fd745ad906a66` and the two resident document ARNs (`irpt-ycharts-deploy`,
   `irpt-ycharts-run`); those two names leave `DenyShellDocuments`; the AWS shell and session documents and the export render
   document stay denied. (These two names were already in this file and passed the naming gate in STEP 0's commit; if the gate
   refuses them now, do not override: file a BLOCKING row.)
7. **The simulation** (`tests/simulate_policy.py`): the sixth block becomes: dell2 send of each resident document to the instance ->
   allowed, 2 arms; dell2 send of a resident document to ANOTHER instance -> denied; `AWS-RunShellScript` to the instance ->
   explicitDeny; the export render document -> explicitDeny; dell2 `ssm:GetCommandInvocation` -> allowed; dell1 send -> denied.
   A seventh block, on the rendered routes documents added to the Dell group's set: for three YES roles chosen to cover the three
   route kinds that exist (a function update on a function of `lambda-execution-role`; an `ssm:UpdateDocument` on a document that
   feeds a YES host; an `s3:PutObject` on a YES host's downloaded prefix) -> explicitDeny each; for two NO roles (a function update on
   a function of a NO role; an `s3:PutObject` on the resident host's own artifact prefix) -> allowed each. LAST line:
   `POLICY-SIM allowed_ok=22/22 denied_ok=19/19 passrole_ok=5/5 protected_ok=8/8 respol_ok=11/11 ssm_ok=<k>/<n> routes_ok=5/5 all_ok=<True|False>`.
8. `tests/check_identity.py`: the name comparison covers the two new policies (11 names) and the sizes of the two rendered documents.
9. **One surprise row** (the CTO's ask: "File the gate's blindness (a reference read as a minted name) as a row for LGIC_BLANKFIX"):
   class OBSERVATION, INERT: the commit gate's naming limb refused 29 lines that REFER to resources that already exist (functions,
   command documents, S3 prefixes) as if they were newly minted names; owner named in the row as the LGIC_BLANKFIX project's COO.
   Give counts, not the names.

**ACCEPTANCE (same four ids; expectations as follows):**
- `CTa1-AC1` unchanged (`unresolved=0`, `ok=True`).
- `CTa1-AC2`: `respol_ok=11/11 ssm_ok=` and, on the same line, `routes_ok=5/5 all_ok=True`.
- `CTa1-AC3`: `policy_size_ok=True ok=True` (11 names).
- `CTa1-AC4` unchanged (`unread=0`, `ok=True`, from the saved file).

No firm, function, document, host or prefix name in any committed file outside `tests/` (the census) and your deliverables table,
except the two resident document names and the instance id in `dell2_ssm_policy.json`. If the commit gate refuses anything, do NOT
override: record the refusal lines, file a BLOCKING row, keep what is committed, and stop. Write a NEW proof instance covering the
four ids, validate it, and flip `<status>` to `complete` only when all four pass.

## AMENDMENT 3 (2.0.0_SA_COO~C, 2026-10-07 ~16:4xZ) -- REOPENED: the transcripts key admits the Dell agent users to DECRYPT (a widening; build and measure only)

The issuer reopens its own order (`complete` -> `in_progress`); the slot is re-seated in a fresh worktree; every earlier commit is
inherited state, merged and APPLIED. Authority: `1.0.0_SA_CTO` msg 106391, verbatim: "New cell, on Andrew's word at
4.0.0_SA_CRO's terminal ~16:1xZ, 'Yes Dell boxes can read all of that' (record
org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261007_161xZ_SIX_OPEN_CALLS_ANSWERED_TICKET_CENTER_AND_TRNSPT_ON_DELL2.md
@a3e5396e1e): the transcripts key policy admits the Dell agent users to decrypt. A widening: measure the plan, send one half
request." The record's item 5: the question was whether the dell2 agent user may read the transcripts store; his answer covers
the Dell boxes and the whole store, the raw tier included. Gate limb: none graded this modification. THE WORK below is the whole
of this amendment. YOU APPLY NOTHING: this pass builds the change and measures it; the apply is a separate act behind two halves.

THE WORD IS "READ". The key policy in `infra/aws/terraform/transcripts/main.tf` has one use statement, `NamedReadersUseTheKey`,
whose principals come from `var.reader_principal_arns` and whose actions include `kms:Encrypt`, `kms:ReEncrypt*` and
`kms:GenerateDataKey*`: adding a Dell user to that list would also let it WRITE under the key. Do NOT add them there.

1. THE FIRST READ, in `infra/aws/terraform/transcripts/tests/read_transcripts_access.py` (create the `tests/` folder), saved as
   `tests/transcripts_access.json`: (a) every statement of the key policy and of the bucket policy as the Terraform declares
   them, and which of them a READ by a Dell user meets (the bucket policy carries a TLS Deny and a write-key Deny and no reader
   list: confirm it); (b) what the two Dell users' OWN policies allow on this bucket and key, by the simulator against their
   LIVE attached policies (`s3:GetObject`, `s3:ListBucket`, `s3:PutObject`, `s3:DeleteObject` on the transcripts bucket, whose
   name you read from the registry scope row the root uses, never type; `kms:Decrypt`, `kms:Encrypt`, `kms:GenerateDataKey` on
   the key): a same-account key policy that names a user grants that user without an identity-policy statement, so the key policy
   is the control for decrypt, and the Dell users' existing S3 allows on the estate's bucket pattern decide whether the object
   read itself is already allowed; say which holds; (c) every other reader of the key today (the variable's default, any
   `.tfvars`, any other root or role that names the key: search `infra/aws/terraform/` for the key's alias and resource address).
   LAST line `TRANSCRIPTS-ACCESS key_statements=<k> bucket_statements=<b> dell_s3_get=<allowed|denied> dell_s3_put=<allowed|denied> dell_kms_decrypt_before=<allowed|denied> other_key_users=<n> ok=<True|False>`.
2. THE CHANGE, one statement added to the key policy and nothing else in the root: Sid `DellAgentUsersDecryptOnly`, Effect Allow,
   Principal the two Dell agent users' ARNs, Action exactly `kms:Decrypt` and `kms:DescribeKey`, Resource `*`. The two ARNs are
   NOT typed as strings: derive them the way this repository already names those users (read
   `infra/aws/terraform/nfra-ctlpln-identity/iam.tf` for how the names are built, and `lib/opal_naming.py name()`; in this root,
   build each ARN from the account id data source and the builder's name passed in as a variable with the builder's output as its
   default, or read the names from a file the identity root already owns; say which you chose and why, and if the commit gate's
   naming limb refuses the form you chose, do NOT override: file a BLOCKING row and stop). Do not touch
   `var.reader_principal_arns`, the bucket policy, or any other file of the root (`chat_assist.tf`, `mail_pull.tf`, `pull.tf`).
3. THE PROOF WITHOUT AN APPLY, in `tests/check_transcripts_dell_decrypt.py`: render the key policy document from the Terraform
   (a provider-less scratch evaluation of the same `jsonencode` expression with the data sources stubbed, as the fence cell did;
   `CHECKPOINT_DISABLE=1`; no backend, no AWS call from Terraform), then by `iam simulate-custom-policy` /
   `simulate-principal-policy` with that document as the resource policy: each Dell user `kms:Decrypt` on the key -> allowed;
   each Dell user `kms:Encrypt`, `kms:GenerateDataKey`, `kms:ReEncryptFrom`, `kms:ScheduleKeyDeletion`, `kms:PutKeyPolicy` ->
   NOT allowed; the existing reader unchanged (decrypt and encrypt allowed); an unlisted user `kms:Decrypt` -> not allowed; and
   the rendered document differs from today's by exactly the one added statement (parsed comparison). LAST line
   `TRANSCRIPTS-DELL-DECRYPT dell_decrypt=<a>/2 dell_write_refused=<r>/<n> reader_unchanged=<True|False> unlisted_refused=<True|False> statements_added=<k> ok=<True|False>`.
   Say plainly what the simulator cannot show (a real decrypt of a real object needs the apply and is another route's).
4. A plan note in your deliverables, `PLAN_NOTE_TRANSCRIPTS_DELL_DECRYPT.md`: what the apply would show by reading (one KMS key
   policy updated in place), exactly what the two Dell users gain (decrypt of every object in the transcripts store, the raw tier
   included, on Andrew's word) and do not gain (encrypt, write, key administration), whether the object read itself is already
   allowed by their own policies (from step 1), and the rollback. Do NOT run `terraform plan` against the backend: the issuer
   measures the plan.

**ACCEPTANCE.** One criterion is ADDED; the other four are unchanged and must still pass:

<criterion id="CTa1-AC5" cell_refs="CT-a-1"><invocation>python infra/aws/terraform/transcripts/tests/check_transcripts_dell_decrypt.py</invocation><expect>TRANSCRIPTS-DELL-DECRYPT dell_decrypt=2/2 dell_write_refused=8/10 reader_unchanged=True unlisted_refused=True</expect></criterion>
`CTa1-AC5` -- the same line must read `ok=True` with `statements_added=1`.

**BOUNDS.** Read-only AWS: `iam simulate-*`, `iam get-*`/`list-*` for the two Dell users' attached policies, `kms describe-key`,
`kms get-key-policy`, `sts get-caller-identity`. NO object read, NO listing of the transcripts bucket, NO decrypt call, no apply,
no plan against the backend, no download. Never print or save the content of a transcript.

## AMENDMENT 4 (2.0.0_SA_COO~C, 2026-10-07 ~17:4xZ) -- one issuer repair: CTa1-AC2's expectation no longer names another cell's count

`CTa1-AC2` expected `respol_ok=11/11 ssm_ok=`. The resource-policy block belongs to cell CT-d-5, whose amendment (merged
@aa6b587487, applied) moved it to 13 arms, so this cell's criterion failed on a number it does not own. The expectation is now
`ssm_ok=9/9 routes_ok=5/5 all_ok=True`: this cell's two blocks and the whole line's verdict. Nothing is weakened: `all_ok=True`
requires every block, the resource-policy one included. Gate limb: none graded this modification.
The worker re-runs the five criteria, rewrites the proof instance's `CTa1-AC2` row from that run (its `expect` field equal to the
new expectation, `status` from the match), validates the instance, and flips the order to `complete` when all five pass.

## AMENDMENT 5 (2.0.0_SA_COO~C, 2026-10-07 ~19:4xZ) -- REOPENED: the Dell group reads exactly the vendor secrets its placed projects need (measure first; build and measure only)

The issuer reopens its own order (`complete` -> `in_progress`); the slot is re-seated in a fresh worktree; every earlier commit is
inherited state, merged. Authority: `1.0.0_SA_CTO` msg 106535, verbatim: "Andrew's 18:3xZ item 4, 'The Dell Boxes have vendor
egress as needed'. dell1 is denied secretsmanager:GetSecretValue on astn/kimi/api-key, so it cannot make a vendor call he has
allowed it. Measure which vendor secrets the Dells' placed projects need, and send one half request granting the Dell group read
of exactly those." His words as recorded
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_183xZ_TWELVE_ITEMS_ANSWERED_INSTALLER_PUSH_VENDOR_EGRESS_STORE_OUTLOOK_LAW_LINE_D2_HOLD_LIFTED.md`,
item 4): "Vendor egress does not count as raw internet access; those are protected channels. The Dell Boxes have vendor egress
as needed." Gate limb: none graded this modification. YOU APPLY NOTHING AND YOU READ NO SECRET VALUE: no
`secretsmanager get-secret-value`, no `batch-get-secret-value`, by any identity, for any reason. Names, ARNs, tags, descriptions
and last-accessed dates only.

THE WORD IS "VENDOR". A secret that holds a vendor's API key or sign-in is in scope. A secret that holds anything else (a
database password, a signing key, a session secret, a portal user store, another firm's credential that is not a vendor call) is
NOT in scope and must not ride in on a wildcard. The Dell group holds no `secretsmanager:GetSecretValue` today (issuer's read of
the three group policies: create, update, tag, describe and list only).

1. THE CENSUS, in `tests/derive_vendor_secrets.py`, saved as `tests/vendor_secrets_census.json`:
   - (a) every secret in the account by NAME (`secretsmanager list-secrets`, auto-paginated, counted client-side; the region the
     estate uses, and say which regions you read): name, ARN, description, tags, last accessed date, last changed date; never a value;
   - (b) every reference to a secret name or a `secretsmanager` call in the repository (the Grep tool; a shell `grep -r` is
     blocked): the file, the secret named, and which project root or pipeline it belongs to (the directory under
     `infra/aws/terraform/`, `data/`, `lib/` or `portal/` and, where a project row names it, the project code);
   - (c) which projects are placed on a Dell. NO register lists this (the directive register names DELL2 for D7 only; project
     rows carry laptop or site-z). Read what the repository does record: `org/missions/DIRECTIVES.yaml` placements naming a Dell;
     task orders whose `<issued_to>` or `<issued_by>` serial ends in a lane that the device register or today's relay files tie to
     a Dell (lanes ending `1` on dell1 and `2` on dell2 by the fabric's convention, for example `~M1`, `~G1`, `~C2`, `~P2`, `~Y2`:
     confirm the convention from `org/devices/DEVICES.json` or the relay files under
     `org/tier0_exec/0.0.0_AB_MSTR/deliverables/` before using it; if you cannot confirm it, say so and mark placement INFERRED).
     Print each Dell-placed project with the evidence line that places it;
   - (d) the join: for each Dell-placed project, the secrets its code references; each classified VENDOR (names the vendor and the
     call it serves, from the code or the secret's description), NOT-VENDOR (says what it is), or UNSURE (counted, listed, NOT
     granted). The one secret the CTO names, `astn/kimi/api-key`, must appear with its project and class.
   - LAST line `VENDOR-SECRETS secrets=<n> referenced=<r> dell_projects=<p> placement_inferred=<True|False> vendor=<v> not_vendor=<x> unsure=<u> granted=<g> ok=<True|False>`
     (`ok=True` when both listings completed and every referenced secret of a Dell-placed project has exactly one class;
     `granted` equals `vendor`).
2. THE GRANT, built from the census and nothing typed twice: `dell_vendor_secrets_policy.json`, one statement
   `ReadNamedVendorSecrets`, Effect Allow, Action exactly `secretsmanager:GetSecretValue`, Resource the EXACT ARNs of the VENDOR
   class (a secret's ARN ends in a random suffix: use the full ARN from the listing, or the name followed by `-??????`; no `*`
   that could match a second secret; say which form you used and prove it matches exactly one secret each). No `kms:Decrypt`
   unless a listed secret is encrypted under a customer-managed key (read each secret's `KmsKeyId`; a secret under the
   account's default key needs none); if one is, STOP and report it rather than widening a key policy. Add the policy and its
   group attachment to `iam.tf` beside the others, its name from the builder as the others are (a sixth managed policy on the
   group; the limit is ten).
   If the commit gate's naming limb refuses the secret names in a `.json` outside `tests/` (it refused function names before),
   do NOT override: keep the census committed, file a BLOCKING row, and report -- the CTO ruled the earlier case by having
   Terraform build the statement from the census file under `tests/`; say whether the same form would serve here.
3. THE PROOF WITHOUT AN APPLY: extend `tests/simulate_policy.py` with an eighth block on the group's set plus the new document:
   each Dell user `secretsmanager:GetSecretValue` on each VENDOR secret -> allowed; on one NOT-VENDOR secret -> not allowed; on
   one secret outside every Dell project -> not allowed; `secretsmanager:PutSecretValue` on a VENDOR secret -> as today (report
   what today is: the create policy allows it; this cell does not change it, and you say so plainly in the plan note).
   The last line gains `vendor_ok=<a>/<n>`.
4. `PLAN_NOTE_DELL_VENDOR_SECRETS.md` in your deliverables: what the apply would show (by reading: one policy and one attachment
   created), the table of secrets granted with the project and vendor each serves, the NOT-VENDOR and UNSURE lists, how placement
   was established, and what the grant does NOT do (it lets a Dell READ the key; whether a given vendor call is one Andrew
   allowed for a given project stays the rule seats follow).

**ACCEPTANCE.** One criterion is ADDED; the other five are unchanged and must still pass (`CTa1-AC2`'s line gains `vendor_ok=`):

<criterion id="CTa1-AC6" cell_refs="CT-a-1"><invocation>python infra/aws/terraform/nfra-ctlpln-identity/tests/derive_vendor_secrets.py --from-file infra/aws/terraform/nfra-ctlpln-identity/tests/vendor_secrets_census.json</invocation><expect>VENDOR-SECRETS secrets=</expect></criterion>
`CTa1-AC6` -- the census was taken and saved; the same line must read `ok=True`. The live listing may exceed 120 seconds and is
run once outside the bound with `--live`.

**BOUNDS.** Read-only AWS: `secretsmanager list-secrets`, `describe-secret`, `iam simulate-*`, `iam get-*`/`list-*` for the Dell
group's policies, `sts get-caller-identity`. NEVER a secret's value. No apply, no plan against the backend, no download.

## AMENDMENT 6 (2.0.0_SA_COO~C, 2026-10-07 ~22:3xZ) -- two issuer repairs to expectations (rows W14-S9, W14-S10); no code change

1. `CTa1-AC2`: AMENDMENT 5 made the simulation's line gain `vendor_ok=` before `all_ok`, and left the expectation as contiguous
   text that the new field splits. It is now `ssm_ok=9/9 routes_ok=5/5 vendor_ok=[0-9]+/[0-9]+ all_ok=True`.
2. `CTa1-AC5`: the transcripts key change was APPLIED today (order NFRA_CTLPLN.TO-APPLY-9, complete). The check's `ok` includes a
   pre-apply guard that the LIVE key policy equals the pre-edit render, which is false after the apply by construction, so the
   line now ends `ok=False`. The criterion's expectation names the four results the cell proves and no longer the `ok` word:
   `TRANSCRIPTS-DELL-DECRYPT dell_decrypt=2/2 dell_write_refused=10/10 reader_unchanged=True unlisted_refused=True`. The proof row
   says in its evidence that the invocation exits non-zero for that stated reason.
Gate limb: none graded this modification. The worker re-runs the six criteria, rewrites the two proof rows from that run with
their new `expect` fields, validates the instance, and flips the order to `complete` when all six match.

## AMENDMENT 7 (2.0.0_SA_COO~C, 2026-10-07 ~23:5xZ) -- REOPENED, PRIORITY: the OpenAI key comes OUT of the grant; one client session secret comes IN by ruling

The issuer reopens its own order (`complete` -> `in_progress`); the slot is re-seated in a fresh worktree; the earlier commits are
inherited state on the trunk (merged @22c49c71e2; NOT applied). Authority, `1.0.0_SA_CTO`:
- msg 106620: "CTO half SIGNED FOR THREE, not four ... openai-api-key is out: the whitelist line scopes it to one project, need
  is not shown, and a read is undone only by rotation. ... nothing applies until the counterpart is amended to three and the
  plan and simulator re-run with the OpenAI key as a refused arm."
- msg 106631: a Dell run "aborted BEFORE any vendor call: AccessDenied on secretsmanager:GetSecretValue for
  blackdiamond/49f/session (cloudops-dell2-agent-user)" (IRPT_DASHBD's read-only Black Diamond pull). "It enters the census as
  needed by a Dell-placed project, for dell2 only if the census can scope by box, otherwise for the group; it rides the same
  amended plan as the three, as a fourth ARN ... Its sibling sessions for other firms do not enter by likeness."
- msg 106634: this goes ahead of everything else; do it in the simplest form that is correct.
Gate limb: none graded this modification. YOU APPLY NOTHING AND YOU READ NO SECRET VALUE, exactly as AMENDMENT 5 bound.

1. THE CENSUS (`tests/vendor_secrets_census.json`, through `tests/derive_vendor_secrets.py`, never by hand-editing the JSON if the
   script regenerates it: give the script a small RULINGS table, data in its head, that overrides a derived class by secret
   name with the ruling's message id and reason):
   - `openai-api-key`: class `EXCLUDED-BY-RULING` (CTO msg 106620), not granted;
   - `blackdiamond/49f/session`: class `GRANTED-BY-RULING` (CTO msg 106631; needed by IRPT_DASHBD, placed on dell2; a refused
     run named it), granted;
   - no other secret changes class: assert that the set of names whose class differs from the committed census is exactly
     those two, and print the before and after counts. The other session secrets stay UNSURE.
   Re-take nothing live unless the script cannot apply the rulings to the saved listing; if it must re-list, the listing is
   still names only.
   Read `blackdiamond/49f/session`'s `KmsKeyId` from the saved listing: if it is not the account's default key, STOP at that
   secret (leave it out, say so) and deliver the three.
2. SCOPE BY BOX, if it costs no more than a small, clean change: the session secret is needed by a dell2 project only. Prefer a
   SECOND statement carried on dell2's own user policy (the root already attaches one per-user policy to the dell2 user:
   read `iam.tf` and `dell2_ssm_policy.json` for the pattern, and build this one the same way the group's vendor statement is
   built, from the census, so no policy file holds a name) and keep the three vendor keys on the group. If scoping by box
   cannot be done cleanly in this pass (for example it needs a new managed policy that the naming builder refuses), put the
   fourth ARN on the group's statement instead and SAY which you did and why. Either way each resource entry is an exact ARN
   matching exactly one listed secret.
3. THE SIMULATION (`tests/simulate_policy.py`, eighth block): the three vendor keys allowed for both Dell users;
   `openai-api-key` REFUSED for both (it was allowed before: this arm flips); `blackdiamond/49f/session` allowed for dell2 and,
   if you scoped by box, REFUSED for dell1; one sibling session secret (for example the same vendor's session for another
   firm) refused for both; the not-vendor, UNSURE and unrelated arms as before. Report the new `vendor_ok=<a>/<n>`.
   `tests/check_identity.py`: update the count it asserts only if a policy name was added.
4. The plan note `PLAN_NOTE_DELL_VENDOR_SECRETS.md` in your deliverables: rewrite its first section to the amended grant
   (which secrets, on which principal, what the apply would show by reading), and keep the UNSURE list.

**ACCEPTANCE.** The six criteria and their expectations are unchanged (`CTa1-AC6`'s line will read `granted=4` with the two
ruled classes counted: say how your line counts them; if you add fields, add them at the end of the line). Write a NEW proof
instance covering the six ids, validate it, and flip the order to `complete` when all six match.

## AMENDMENT 8 (2.0.0_SA_COO~C, 2026-10-08 ~00:2xZ) -- SUPERSEDES AMENDMENT 7's items 1 and 2: the grant WIDENS to every secret a Dell-placed project's own code reads by name

Authority: `1.0.0_SA_CTO` msg 106646, on Andrew-direct ~00:0xZ ("I think we need to start giving dell boxes more permissions.
Their entire point is to be work horses and laptop is control plane."; record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_000xZ_DELLS_ARE_THE_WORK_HORSES_MORE_PERMISSIONS_LAPTOP_IS_CONTROL_PLANE.md`,
which may not be in your worktree yet). The CTO's ruling, verbatim: "the grant widens to every secret a Dell-placed project's
own code reads by name, vendor or internal, from the census already taken; openai-api-key stays out; this supersedes 'three'
and my 23:35Z input. One amended half, one plan." Gate limb: none graded this modification. WHERE THIS AMENDMENT AND
AMENDMENT 7 DIFFER, THIS ONE GOVERNS. AMENDMENT 7's items 3 and 4 and its bounds stand. YOU APPLY NOTHING AND READ NO SECRET VALUE.

1. THE GRANT SET, derived from the saved census and nothing typed: every listed secret for which the census holds at least one
   reference that is A PROGRAM of a Dell-placed project reading the secret BY NAME (the census's own distinction, made in the
   earlier pass: a program that fetches the value, as against a Terraform grant, a registry, a manifest, a fixture or a
   document that merely names it). Vendor or internal makes no difference now. `openai-api-key` is EXCLUDED-BY-RULING and stays
   out. A secret named only in a project's documents, or only in registries, is NOT in the set. A secret no Dell-placed
   project's program reads is NOT in the set, whatever its class was. `blackdiamond/49f/session` is in the set if and only
   if the rule above puts it there (a program of IRPT_DASHBD reads it by name: check); it is no longer a special case.
   Keep the earlier class column (VENDOR, NOT-VENDOR, UNSURE) as information and add a boolean `granted` with the reader
   program's file and line as its evidence. If the saved census does not record, per reference, whether it is a program
   reading by name, re-derive that from the repository (names only) and say so.
   For each granted secret read `KmsKeyId` from the saved listing: one under a customer-managed key is left OUT, listed as
   blocked-by-key, and reported (no key policy is touched).
2. ONE STATEMENT ON THE GROUP (the simplest correct form; the per-box scoping of AMENDMENT 7 item 2 is dropped by the ruling's
   "one plan"): `ReadSecretsDellProjectsReadByName`, Allow `secretsmanager:GetSecretValue`, the exact ARN of every granted
   secret, built by Terraform from the census as before. Keep the document inside the 6,144-character managed-policy limit: if
   it does not fit, split by a stable rule into two policies and say so; a precondition already refuses an oversize document.
3. In the simulation's eighth block: every granted secret allowed for both Dell users (you may sample when the set is large:
   then test ALL of them once outside the 120-second criterion and record the full result in the plan note, and keep a fixed
   sample of at least eight in the criterion's run, chosen to include a vendor key, an internal bearer token, a signing key if
   one is granted, and a session secret); `openai-api-key` REFUSED; one secret that only documents name REFUSED; one secret no
   Dell project's program reads REFUSED; one unrelated secret REFUSED; a granted name with a wrong suffix REFUSED.
4. THE PLAN NOTE must list, by name, EVERY granted secret with its class, its project, its reader program (file and line) and
   one plain sentence on what holding its value lets a box do: this is the list two people sign, and it will include internal
   credentials. Put first, under their own heading, any granted secret that is a SIGNING KEY, a seed, an administrator
   credential or a token that lets its holder act as the firm or as a user (for example a JWT private key, an admin seed, a
   gateway bearer token), so that the widening is read for what it is. Do not soften or omit one; if the rule puts it in the
   set, it is in the set and it is named.

**ACCEPTANCE.** The six criteria and their expectations are unchanged; `CTa1-AC6`'s line reads `granted=<n>` with the new count.
Write a NEW proof instance covering the six ids, validate it, and flip the order to `complete` when all six match.

## AMENDMENT 9 (2.0.0_SA_COO~C, 2026-10-08 ~01:0xZ) -- REOPENED, PRIORITY, SUPERSEDES AMENDMENTS 7 AND 8 ON SCOPE: three changes to the Dell identity root in ONE plan, on Andrew's word lifting three limits

Authority: Andrew-direct ~00:4xZ, "lets start with lifting 1 2 3 6", answering a numbered list (record, read its rulings section:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_004xZ_LIFT_FOUR_DELL_LIMITS_SECRETS_FIRM_DATA_RESOURCE_POLICIES_PUSH.md`),
and `1.0.0_SA_CTO` msg 106669: "1. Secrets: the Dell group reads every vendor credential and every client-firm or custodian
session in the store. Out only: signing keys, seeds, bearer tokens. openai-api-key is IN. ... 3. The resource-policy Deny (the
75 actions) comes off the Dell group. The routes Deny stays. IAM creation stays with the laptop. Also in:
iam:SimulatePrincipalPolicy on self, and dell2's SSM parameter once named. ASK: one half request per root, fewest applies that
are honest; secrets first." Gate limb: none graded this modification. WHERE THIS AMENDMENT AND AMENDMENTS 7 OR 8 DIFFER, THIS ONE
GOVERNS. A previous pass on this branch built AMENDMENT 8's wider set (a secret is granted when a Dell project's program reads
it): keep its tooling, replace its RULE. YOU APPLY NOTHING AND READ NO SECRET VALUE.

A. **SECRETS, the new rule, over ALL listed secrets (114 at the last listing), by NAME, description, tags and the code that
   uses it; whether a Dell project's code names it today no longer matters.** Each secret gets exactly one class:
   - `VENDOR-CREDENTIAL`: a key or sign-in for an outside vendor's service (model providers, market-data and custodian
     platforms' API keys, proxy providers, messaging providers). GRANTED. `openai-api-key` is in this class and GRANTED.
   - `CLIENT-SESSION`: a client firm's or a custodian's login or captured session used to pull that firm's data (the
     `blackdiamond/*`, `orion/*`, `smartx/*`, `ycharts/session/*`, `seeking-alpha/session` kind). GRANTED.
   - `PLATFORM-KEY`: a secret whose holder can act AS Opal's own platform: signing keys (any `jwt` private or public key pair's
     private half and any shared signing secret), seeds, administrator credentials, and bearer tokens for Opal's own gateway or
     services. The CTO named `opal/auth/jwt-private-key`, `opal/auth/irpt-render-jwt-private-key`, `opalinvest/jwt-secret`,
     `opalinvest/admin-seed` and the gateway bearer tokens, "and any like them the cell finds". NOT granted.
   - `OTHER`: anything that is none of the three, or that you cannot place by name, description and use (configuration
     bundles with no description, a public key, an origin-verify value, the firm's own directory app credential, a secret
     scheduled for deletion). NOT granted; listed with the reason, for a person to rule. When in doubt between a granted class
     and OTHER, it is OTHER. When in doubt between PLATFORM-KEY and anything else, it is PLATFORM-KEY.
   Rulings table in the derive script's head (name, class, message id) for the named ones. A secret under a customer-managed
   key is left OUT of the grant whatever its class, listed as blocked-by-key (no key policy is touched).
   One statement on the group as before, exact ARNs, no wildcard, built by Terraform from the census; split into two managed
   policies by a stable rule if the document would pass 6,144 characters (count it; say which).
B. **THE RESOURCE-POLICY DENY COMES OFF.** Remove from the root: `aws_iam_policy.dell_agent_respol` and its group attachment in
   `iam.tf`, `dell_respol_policy.json`, and the checks that exist only to prove that Deny (`tests/derive_respol_actions.py`; the
   resource-policy block of `tests/simulate_policy.py` becomes its mirror: the same actions for a Dell user now read as the
   create policy and the other statements leave them, with at least `s3:PutBucketPolicy`, `kms:PutKeyPolicy`,
   `lambda:AddPermission` and `sqs:SetQueueAttributes` each reported by its decision, not asserted to be allowed: REPORT what
   each reads once the Deny is gone, because an action no Allow covers stays refused, and say so). The ROUTES Deny
   (`routes.tf`, `modules/routes_policy/`), `DenyPassRoleExceptNamed`, `DenyProtectedFunctions` and `DenyApiKeyReads` STAY
   untouched: assert the routes and protected-function arms read exactly as before. `tests/check_identity.py`'s name count
   moves accordingly. Keep `tests/read_queue_attribute_writers.py` and its saved file (a read, harmless).
C. **SELF-SIMULATE.** Add `iam:SimulatePrincipalPolicy` for each Dell user ON ITS OWN USER ONLY: one statement in the group's
   read statement set (`dell_create_policy.json`'s read statement, or a new small statement there), Resource
   `arn:aws:iam::<account>:user/${aws:username}` (the policy variable, so one statement serves both users and neither can
   simulate the other or any role). Add two arms to the simulation: a Dell simulating itself allowed; simulating the other
   Dell or a role refused.
D. dell2's SSM parameter read is NOT in this pass (its name has not arrived).
E. THE PLAN NOTE (`PLAN_NOTE_DELL_VENDOR_SECRETS.md`, renamed in its title to cover all three changes): what the ONE apply
   would show by reading (expected: the secrets policy and attachment created, the resource-policy policy and attachment
   destroyed, one policy updated in place for the self-simulate), then: every GRANTED secret by name with its class; every
   PLATFORM-KEY by name with one plain sentence on what holding it lets a box do; every OTHER by name with the reason; and,
   for B, the list of what a Dell can newly do once the Deny is gone, by action, from the simulation, with the plain note that
   a Dell changing a resource policy does so under its own box's never-widen pair.

**ACCEPTANCE.** `CTa1-AC1`, `AC3`, `AC4`, `AC5` unchanged. `CTa1-AC2`'s expectation is unchanged
(`ssm_ok=9/9 routes_ok=5/5 vendor_ok=[0-9]+/[0-9]+ all_ok=True`): keep those three fields adjacent and in that order; the
resource-policy field may change its name and count, and a `selfsim_ok=<a>/<n>` field goes BEFORE `ssm_ok`. `CTa1-AC6` unchanged
(`VENDOR-SECRETS secrets=`; the line reads `ok=True` with the new counts, and add `platform_key=<n> other=<n>` at its end).
Write a NEW proof instance covering the six ids, validate it, and flip the order to `complete` when all six match.

## AMENDMENT 10 (2.0.0_SA_COO~C, 2026-10-08 ~04:0xZ) -- REOPENED, PRIORITY: item B needs the ALLOW, not only the Deny removed

AMENDMENT 9's pass (commits `ab4bfecd59`, `943d8eee65` on this branch) is accepted as built: 66 of 114 secrets granted, 28
platform keys and 19 unplaced withheld, 1 blocked by its key; the resource-policy Deny removed; self-simulate added. Its own
measurement found that removing the Deny frees ONE action (`sqs:SetQueueAttributes`): 71 of the 75 stay refused because no Allow
covers them. `1.0.0_SA_CTO` msg 106731, ruling 1: "Andrew lifted 'change who may reach a resource: bucket policies, key
policies, Lambda permissions, queue policies'. Removing the Deny while 71 of 75 actions stay refused for want of an Allow
delivers one action, not that. The identity plan grants the Dell group those resource-policy actions as an Allow, in the same
plan. Out of the Allow: every iam: action (item 4 is not lifted) and anything that is the routes-host policy's subject (item 5
is with Andrew). The half states how many of the 75 the Allow covers and names the ones left out." Gate limb: none graded this
modification. YOU APPLY NOTHING, RUN NO PLAN AGAINST THE BACKEND, AND READ NO SECRET VALUE.

1. **THE ALLOW.** One new managed policy on the group, name from the builder as the others are, holding the resource-policy
   actions of the former Deny list (recover the list of 75 from this branch's history: `git show c7c6d13b85:infra/aws/terraform/nfra-ctlpln-identity/dell_respol_policy.json`),
   as an Allow, MINUS the exclusions below. Keep the list as DATA in a JSON document with, per action, `in_allow` true or
   false and the reason when false, and build the policy from it.
2. **EXCLUSIONS, each stated in the data with its reason:**
   a. every `iam:` action (the CTO's ruling; item 4 is not lifted);
   b. any action that is the subject of the routes Deny (`routes.tf`, `modules/routes_policy/`): read that policy's action
      list and exclude the intersection, printing it (it may be empty);
   c. the actions the statements that STAY already deny explicitly (`cloudtrail:PutResourcePolicy`,
      `cloudtrail:DeleteResourcePolicy`, and any other the simulation shows as explicitDeny): leave them out of the Allow so
      the document does not carry a dead grant;
   d. **the ISSUER'S exclusion, for the CTO to confirm or overrule in its half: the Secrets Manager resource-policy actions
      (`secretsmanager:PutResourcePolicy`, `secretsmanager:DeleteResourcePolicy`, and any other secretsmanager action in the
      list).** Reason: in one account a resource policy on a secret that names the Dell user is enough to let it read that
      secret, so this action would let a Dell grant itself the 28 platform keys the same plan withholds. Mark these
      `in_allow: false, reason: "would undo the secrets carve-out of this plan (issuer; CTO to confirm)"`.
   e. Do NOT invent further exclusions. But REPORT, without excluding, every other way the Allow could undo a limit that
      stays: at least (i) `kms:PutKeyPolicy` / `kms:CreateGrant` on a key that encrypts a withheld secret (the one
      blocked-by-key secret; say which key and whether the withheld secrets use the default key, where a key policy is not
      settable); (ii) `lambda:AddPermission` on the ten protected functions (expect the explicit Deny that stays to win: show
      it); (iii) `s3:PutBucketPolicy` on the three firm-fence buckets and on the Terraform state bucket (a Dell could rewrite a
      fence or the state bucket's policy: say what the simulation reads); (iv) anything touching the transcripts key's policy.
      These go in the plan note under a heading "What this Allow can undo", for the people who sign.
3. **RESOURCE SCOPE.** `Resource: "*"` unless an action cannot take it; no condition invented. If the document would pass
   6,144 characters, split by a stable rule and say which; the group then holds at most 7 managed policies (quota 10): print the
   count.
4. **SIMULATION.** The `freed_ok` block becomes: every action with `in_allow: true` reads `allowed` for both users on a
   representative resource of its service; every excluded action reads its stated decision (implicitDeny, or explicitDeny with
   the statement that denies it); the ten protected functions still read explicitDeny for `lambda:AddPermission`; the routes
   arms read exactly as before. Print `freed_allowed=<a>/<n> freed_excluded=<e>` inside the POLICY-SIM line BEFORE `selfsim_ok`
   (replacing `freed_ok`); the three adjacent fields `ssm_ok=9/9 routes_ok=5/5 vendor_ok=<a>/<n> all_ok=True` stay last and in
   that order.
5. **PLAN NOTE** (same file): the expected plan by reading (now 3 or more to add: the secrets policy and attachment, the new
   Allow policy and attachment; 1 to change; 2 to destroy), the count of the 75 the Allow covers, EVERY excluded action by name
   with its reason, and the "What this Allow can undo" section.
6. `tests/check_identity.py`'s name count moves again; the proof row for `CTa1-AC3` keeps the expectation
   `policy_size_ok=True ok=True` (the issuer accepts row W14-S13's reading that the count moves).

**ACCEPTANCE.** The six ids as in AMENDMENT 9, `CTa1-AC2` matching `ssm_ok=9/9 routes_ok=5/5 vendor_ok=[0-9]+/[0-9]+ all_ok=True`.
Rewrite the proof instance from your runs, validate it, and flip the order to `complete` when all six match.

## AMENDMENT 11 (2.0.0_SA_COO~C, 2026-10-08 ~06:0xZ) -- REOPENED, PRIORITY, SHORT: one public SSM parameter read, by exact ARN (it leads plan 2)

AMENDMENT 10's pass is accepted and merged (@31dc118504). One grant is added to the same plan. `1.0.0_SA_CTO` msg 106743:
dell2's seat is refused `ssm:GetParameter` on
`arn:aws:ssm:us-east-1::parameter/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64` (an AWS PUBLIC parameter:
note the empty account field), which blocks a release that gates Andrew's own retry of a report run; msg 106757: "Plan 2 leads
with dell2's SSM parameter by exact ARN." The root holds no `ssm:GetParameter` grant today. Gate limb: none graded this
modification. YOU APPLY NOTHING AND RUN NO PLAN AGAINST THE BACKEND.

1. Add ONE statement to the Dell group's read statement set (in `dell_create_policy.json`, beside `SimulateOwnPolicyOnly`):
   Sid `ReadPublicAmiParameter`, Effect Allow, Action `ssm:GetParameter` ONLY (not `GetParameters`, not `GetParametersByPath`),
   Resource exactly the ARN above. No wildcard, no second ARN, no account id inserted.
2. First find WHY the seat needs it, by reading: search the repository for `al2023-ami-kernel-default-x86_64` and
   `ami-amazon-linux-latest` and report the file and line that reads it (a Terraform `data "aws_ssm_parameter"` in the root
   dell2 is applying is the expected shape). If that code reads the parameter with a DIFFERENT action (Terraform's data source
   calls `ssm:GetParameter`; if you find `GetParameters` or a path read instead, say so and add exactly the action that code
   uses, naming the file and line as the reason). If other public AMI parameters are read by Dell-placed roots, LIST them in
   your report and do NOT add them.
3. Simulation: two new arms in `tests/simulate_policy.py`, counted inside the existing `ssm_ok` field (which becomes
   `ssm_ok=<n>/<n>` with n = 9 plus your arms): `ssm:GetParameter` on the exact ARN allowed for both users; `ssm:GetParameter`
   on a different public parameter (`.../al2023-ami-kernel-6.1-x86_64`) and on an account parameter
   (`arn:aws:ssm:us-east-1:<account>:parameter/anything`) refused. Count the create policy's characters against 6,144.
4. Plan note: add the statement to the expected plan (the create policy's in-place change now adds two statements).

**ACCEPTANCE.** The six ids as before; `CTa1-AC2`'s expectation becomes
`ssm_ok=[0-9]+/[0-9]+ routes_ok=5/5 vendor_ok=[0-9]+/[0-9]+ all_ok=True` (the issuer changes the criterion's `<expect>` in this
order by this amendment; write the proof row's `expect` equal to it). Rewrite the proof instance from your runs, validate,
flip the order to `complete`.

## AMENDMENT 12 (2.0.0_SA_COO~C, 2026-10-08 ~06:4xZ) -- REOPENED, PRIORITY, SHORT: three explicit Deny statements by resource, so the Allow cannot undo three limits that stay

AMENDMENT 11's pass is accepted. Your AMENDMENT 10 report and row NFRA_CTLPLN-W14-S15 found routes by which the new Allow undoes
limits that stay. `1.0.0_SA_CTO` msg 106781 ruled three of them OUT, "Each as an explicit Deny by resource ARN, in plan 2":
"1. lambda:AddPermission on the ten protected functions: OUT. Same class as the signing keys: a way to act as the platform.
2. s3:PutBucketPolicy on the CloudTrail log bucket: OUT. No Dell project owns the audit trail. 3. sqs:AddPermission and
SetQueueAttributes on the four agentbus queues: OUT. Receive-only-own-queue is how the boxes are kept apart." Gate limb: none
graded this modification. YOU APPLY NOTHING AND RUN NO PLAN AGAINST THE BACKEND.

1. **PROTECTED FUNCTIONS.** The existing statement `DenyProtectedFunctions` (in `dell_deploy_policy.json`) lists the ten
   functions and the actions it denies. Add to the Deny, for the SAME ten function ARNs (reuse the statement's own resource
   list; do not retype it), every action of the new Allow's list whose service is `lambda` (at least `lambda:AddPermission`
   and `lambda:RemovePermission`; take the set from the Allow's data document, print it). Either widen that statement's
   action list or add a sibling statement `DenyProtectedFunctionPermissions` in the same document: choose the one that keeps
   the existing `protected_ok=8/8` arms unchanged, and say which.
2. **THE AUDIT-TRAIL BUCKET.** A new Deny statement `DenyAuditTrailBucketPolicy`: every `s3` action of the Allow's list
   (bucket policy, ACL, public-access-block and the like: take the set from the data document, print it) on
   `arn:aws:s3:::opal-cloudtrail-logs-313476888478` and `arn:aws:s3:::opal-cloudtrail-logs-313476888478/*`. Take the bucket
   name from where your last pass found it; if the repository names the trail's bucket in Terraform, cite the file and line.
3. **THE AGENTBUS QUEUES.** A new Deny statement `DenyAgentbusQueuePolicy`: every `sqs` action of the Allow's list (at least
   `sqs:AddPermission`, `sqs:RemovePermission`, `sqs:SetQueueAttributes`) on the four agentbus queue ARNs. Take the four ARNs
   from the repository (the agentbus Terraform or `org/devices/`), cite the file and lines, and do not match by wildcard
   unless the four share an exact prefix no other queue has: if you use a prefix pattern, list every live queue name it would
   match from the repository's own records and show it is exactly the four. A Dell must still be able to RECEIVE from and
   SEND on the queues exactly as today: add arms showing `sqs:ReceiveMessage` on its own queue and `sqs:SendMessage` read as
   they did before this amendment.
4. Put statements 2 and 3 where they fit the 6,144-character limits (print each touched document's count); if a document
   would overflow, a new small managed policy named by the builder is acceptable (the group then holds 7 of 10: print it).
5. **SIMULATION.** A new field `undo_denied=<a>/<n>` in the POLICY-SIM line, placed BEFORE `selfsim_ok`: for both users,
   each denied action on each named resource reads `explicitDeny` with the new statement matched; and the controls: the same
   actions on a NON-protected function, on another bucket (`opal-data-assets`) and on a non-agentbus queue still read
   `allowed`. `freed_allowed` stays 70/70 on its representative resources (if a representative resource is now one of the
   denied ones, move the representative, do not drop the action). The last four fields stay
   `ssm_ok=15/15 routes_ok=5/5 vendor_ok=<a>/<n> all_ok=True`.
6. **PLAN NOTE:** the expected plan by reading, as ONE list for the people who sign plan 2 (what plan 2 adds on top of plan
   1, assuming plan 1 is applied first: the Allow policy and its attachment created; the create policy changed in place for
   the parameter read; the deploy policy and any other touched policy changed in place for the Denies), and update "What this
   Allow can undo": the three ruled routes now read refused; the four accepted routes (a firm fence's policy, the state
   bucket's policy, a key policy, the transcripts key) and the object-ACL finding stay as reported.

**ACCEPTANCE.** The six ids, expectations as AMENDMENT 11 left them. Rewrite the proof instance, validate, flip to `complete`.

## AMENDMENT 13 (2.0.0_SA_COO~C, 2026-10-08 ~07:5xZ) -- REOPENED, PRIORITY, VERY SHORT: seven more actions into the audit-trail bucket's Deny, and the Allow behind a switch

AMENDMENT 12's pass is accepted. Two changes, both small. `1.0.0_SA_CTO` msg 106838: "1. In. Add the seven (lifecycle, logging,
notification, encryption, versioning, ownership controls, public-access block) to DenyAuditTrailBucketPolicy in plan 2. A
lifecycle rule that expires the audit log is the same harm as a rewritten policy ... 3. ... the Denies step applies BEFORE plan
1 ... So: Denies, then plan 1 (targeted at its five), then the Allow." and msg 106820: "From now, a resource that must not apply
yet stays behind a count of 0 until its pair is signed." Gate limb: none graded this modification. YOU APPLY NOTHING AND RUN NO
PLAN AGAINST THE BACKEND.

1. **THE SEVEN.** Your row NFRA_CTLPLN-W14-S16 found that the create policy already lets both Dells change the audit-trail
   bucket's lifecycle, logging, notification, encryption, versioning, ownership controls and public-access block. Add to
   `DenyAuditTrailBucketPolicy` the WRITE actions for exactly those seven (the `s3:Put...` action of each, and the
   `s3:Delete...` action where the service has one, for example the lifecycle and encryption deletes and the public-access
   block delete: take the exact action names from the create policy's own Allow list and from the simulator, list each with
   the one of the seven it belongs to, and do not add reads). Same two resources. Count the document against 6,144.
2. **SIMULATION.** Extend `undo_denied` with an arm per added action on the bucket for both users (explicitDeny, the new
   statement matched) and a control per added action on `opal-data-assets` (still as it read before: report the decision; do
   not assert allowed where an older Deny already refuses it).
3. **THE ALLOW BEHIND A SWITCH.** `aws_iam_policy.dell_agent_respol_allow` and its attachment exist today whenever the data
   document renders (`count = respol_policy_count`, `respol_json == null ? 0 : 1`). Add a variable
   `apply_respol_allow` (bool, default `false`) in the root and make both counts
   `var.apply_respol_allow && <the existing condition> ? 1 : 0` (keep the existing condition as it is). With the default, a
   plan of the root contains NEITHER resource. The simulation and static checks must still test the Allow's document (they
   read the rendered JSON, not the count): show `freed_allowed=70/70` unchanged. Say exactly how the applier turns it on for
   the last step (`-var apply_respol_allow=true` on plan and apply) and that nothing else in the root reads the variable.
   `terraform validate` passes with the default and with the variable true.
4. **PLAN NOTE, section E, rewritten as THREE STEPS** for the people who sign, by reading: STEP A (the Denies step, a
   targeted apply of the two policies changed in place: `aws_iam_policy.dell_agent_create` gains `SimulateOwnPolicyOnly`,
   `ReadPublicAmiParameter`, `DenyAuditTrailBucketPolicy`, `DenyAgentbusQueuePolicy`; `aws_iam_policy.dell_agent_deploy`'s
   `DenyProtectedFunctions` gains four actions; nothing created, nothing destroyed); STEP B (plan 1's remaining four
   resources: the secrets policy and attachment created, the old Deny policy and attachment destroyed); STEP C (the Allow and
   its attachment, with the variable true). Say what each step would show if the previous one is applied.

**ACCEPTANCE.** The six ids, expectations unchanged. Rewrite the proof instance, validate, flip to `complete`.

## AMENDMENT 14 (2.0.0_SA_COO~C, 2026-10-08 ~12:3xZ) -- REOPENED, VERY SHORT: the Allow's variable defaults to TRUE, so a plain plan cannot destroy it

Steps A and B of this root are APPLIED (09:19:39Z, 11:33:48Z). Step C, the Allow, is signed by both seats and with the applier
now, applied with `-var apply_respol_allow=true`. Once it is applied, the variable's default of false becomes a hazard: any
plan or apply of this root by any seat WITHOUT the variable would plan to DESTROY the Allow and its attachment. `1.0.0_SA_CTO`
msg 106915: "Condition 6 is tightened: the cell that makes the variable's default true is cut the same hour as the apply, and no
other seat plans this root in between." Gate limb: none graded this modification. YOU APPLY NOTHING AND RUN NO PLAN AGAINST THE
BACKEND. THE ISSUER HOLDS THIS BRANCH OFF THE TRUNK UNTIL THE APPLIER REPORTS STEP C APPLIED.

1. In the root, change `variable "apply_respol_allow"`'s default from `false` to `true`, and rewrite its description to say:
   the Allow was applied on 2026-10-08 under order NFRA_CTLPLN.TO-APPLY-13; the variable remains as the one-line way to take
   the Allow off (`-var apply_respol_allow=false` plans its removal, which is a never-widen act needing its own pair); it was
   false until that apply so that no plan could carry the Allow before its pair was signed. Change nothing else in any `.tf`.
2. `terraform validate` passes. The static check and the simulation read as before (they read the rendered document, not the
   count): report both last lines.
3. Add ONE static check, in `tests/check_identity.py` (or the nearest existing static test of the root): the variable's
   default is `true`, read from the `.tf` text; a default of `false` fails the check with a line naming this amendment. This
   is what stops a later edit from quietly re-arming the hazard.
4. Plan note: one closing paragraph in section E saying step C is the last step, the default is now true, and how the Allow
   is taken off.

**ACCEPTANCE.** The six ids, expectations unchanged. Rewrite the proof instance, validate, flip to `complete`.

## AMENDMENT 15 (2.0.0_SA_COO~C, 2026-10-08 ~13:5xZ) -- REOPENED, PRIORITY: item 5 is lifted -- the routes Deny comes off both Dells (step D)

Authority: Andrew-direct 2026-10-08 ~13:2xZ at the `1.0.0_SA_CTO` terminal, verbatim and entire in the record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_132xZ_TEN_ANSWERS_LIFT_ITEMS_5_AND_4_WIDEN_BOTH_GRANTS_DELL2_RETRIES_DELL1_INSTALLS.md`
(read its table and its "One consequence" section): "1.) lIFT ITEM 5. 2.) LIFT ITEM 4. 3.( WIDEN THE TWO GRANTS, YES. ...".
`1.0.0_SA_CTO` msg 106945: "Three cells, each under its own pair ... (1) Item 5, first: remove the Deny in
cloudops-dell-agent-routes-host-policy for both Dells. dell1 measures s3:PutObject on the cot and bd code prefixes
explicitDeny; three dell1 deploys wait. (2) Item 3 widened ... (3) Item 4 ...". THIS AMENDMENT IS CELL (1) ONLY. Cells (2) and
(3) follow as later amendments, each merged only after the one before it has applied; do NOT start them. Gate limb: none
graded this modification. YOU APPLY NOTHING AND RUN NO PLAN AGAINST THE BACKEND.

1. **FIND THE WHOLE OF ITEM 5 FIRST, by reading, and print it.** The routes Deny is built in `routes.tf` through
   `modules/routes_policy/`. Report: every managed policy it creates (names from the builder; the CTO names
   `cloudops-dell-agent-routes-host-policy`; say whether there is a second document, as earlier passes spoke of "the two routes
   Deny documents"), every attachment (group or per user), every statement in each with its actions and resources in plain
   words (what a Dell is refused today: command documents, task definitions, the code prefixes of which buckets, and so on),
   and which statements a DIFFERENT file of this root holds that also refuse a deploy route (name them; for example
   `DenyPassRoleExceptNamed`, `DenyProtectedFunctions`, `DenyApiKeyReads`, `DenyS3DeletesOnProductionData`, `DenyEveryIamWrite`).
2. **REMOVE ONLY THE ROUTES DENY**: the policy or policies and attachments that `routes.tf` creates. Do it so that a plan of
   the root shows exactly those resources destroyed and NOTHING else changed: the module also renders the secrets policy and
   the Allow's data (`respol_policy_count` and the like), so do NOT delete the module; remove or zero the routes resources
   only, and keep every other output of the module rendering exactly as it does (assert the secrets policy and the Allow
   documents are byte-identical before and after your change, from the module's rendered JSON).
   The statements named at the end of item 1 that live in OTHER files STAY in this cell, untouched: they are cells (2) and (3)
   or not lifted at all. If dell1's measured refusal (`s3:PutObject` on the cot and bd code prefixes) is caused by a statement
   that is NOT in the routes policy, STOP and report which statement refuses it: removing the routes policy would then not
   deliver what was asked, and the issuer must know before a half is signed.
3. **SIMULATION.** The `routes_ok` block becomes its mirror: for both users, each action and resource the routes Deny
   refused is REPORTED by its decision once the Deny is gone (allowed, or still refused and by which statement), not asserted
   to be allowed. Include, as named arms: `s3:PutObject` on a key under the Cottonwood code prefix and under the Black Diamond
   code prefix (find the exact prefixes the routes policy names); writing an SSM command document; registering a task
   definition; and whatever else item 1 found. Print the field as `routes_freed=<allowed>/<n> routes_still_refused=<k>` in
   place of `routes_ok=5/5`, and list each still-refused arm with its statement. The fields after it stay
   `vendor_ok=<a>/<n> all_ok=True`, last.
4. **STATIC CHECK**: names from the builder and the group's attachment count move; report both. `allow_default_true=True`
   stays.
5. **PLAN NOTE**: a new section F, "STEP D -- the routes Deny removed (item 5)": the expected plan by reading (resources
   destroyed, by address, so the applier can TARGET them), what each Dell can newly do, in plain words, and what still
   refuses a deploy route after this step and why.

**ACCEPTANCE.** The six ids. `CTa1-AC2`'s expectation becomes, by this amendment,
`routes_freed=[0-9]+/[0-9]+ routes_still_refused=[0-9]+ vendor_ok=[0-9]+/[0-9]+ all_ok=True` (the issuer changes the criterion's
`<expect>` in this order; write the proof row's `expect` equal to it). Rewrite the proof instance, validate, flip to `complete`.

## AMENDMENT 16 (2.0.0_SA_COO~C, 2026-10-08 ~16:3xZ) -- REOPENED, PRIORITY: item 3 -- widen the two grants (cell 2, step E)

Authority: Andrew-direct 2026-10-08 ~13:2xZ, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_132xZ_TEN_ANSWERS_LIFT_ITEMS_5_AND_4_WIDEN_BOTH_GRANTS_DELL2_RETRIES_DELL1_INSTALLS.md`
row 3: "WIDEN THE TWO GRANTS, YES" to "the 28 platform keys, the audit trail and its bucket, the portal's protected functions
and the four cross-box queues"; "Not named and so not widened by this: the 19 unplaced secrets, and the one custodian
session behind its own key". `1.0.0_SA_CTO` msg 106945 cell (2); msg 106987: cell 2 goes FIRST, cell 1 after it applies;
`org/tier1_exec/1.0.0_SA_CTO/deliverables/FAST_FIX_RULINGS_20261008_162xZ.md` graph F1: `opal/mcp/graph-read-token` is one of
the 28 and ships here. AMENDMENT 15 (cell 1, the routes Deny) is NOT on this branch: it is parked on branch
`wk-NFRA_CTLPLN-14` and is not part of this pass. Do not touch `routes.tf` or the routes arms. Gate limb: none graded this
modification. YOU APPLY NOTHING, RUN NO PLAN AGAINST THE BACKEND, AND READ NO SECRET VALUE.

THE ISSUER'S READING (the CTO half confirms or widens it): "the two grants" are the SECRETS read grant and the
RESOURCE-POLICY Allow. What comes in is what those two grants held out on the four named things. Nothing else moves:
`DenyEveryIamWrite` (cell 3), `DenyPassRoleExceptNamed`, `DenyApiKeyReads`, `DenyS3DeletesOnProductionData`,
`DenyTableAndDatabaseDeletes`, the protected functions' ten DEPLOY actions, and the routes Deny all stay as they are.

1. **SECRETS: the 28 PLATFORM-KEY secrets are GRANTED.** In `tests/derive_vendor_secrets.py` the class PLATFORM-KEY becomes
   a granted class (record this amendment as the rule's source in the script's head). OTHER (19) and BLOCKED-BY-KEY
   (`schwab/sdd/session`) stay NOT granted. Re-derive the census from the saved listing (or `--live`, names and metadata
   only, never a value) and print the class counts; expected granted 66 + 28 = 94. The grant stays exact ARNs, no
   wildcard, built by the module from the census. The document will pass 6,144 characters: SPLIT by a stable rule (one
   managed policy per granted class is the rule `iam.tf` already names), names from the builder, each with its group
   attachment; print each document's characters and the group's managed-policy count (expected 7 of 10). Keep the existing
   policy's name and address for one of the parts so it updates in place rather than being destroyed and re-created.
   Name `opal/mcp/graph-read-token` in your report as granted.
2. **THE AUDIT TRAIL: `cloudtrail:PutResourcePolicy` and `cloudtrail:DeleteResourcePolicy` come into the Allow.** In
   `dell_respol_policy.json` flip both to `in_allow: true` (summary 72 of 75 in the Allow). `DenyCloudTrailWrites`
   (`dell_deploy_policy.json`) denies them today through `cloudtrail:Put*` and `cloudtrail:Delete*`: rewrite that statement
   so it no longer denies those TWO actions and still denies every other CloudTrail Stop/Delete/Update/Put action. Take the
   full action list of those four prefixes from the AWS service reference or the simulator, print it, and write it
   explicitly (or use a `NotAction`-free form you show is equivalent); show by simulation that `cloudtrail:StopLogging`,
   `DeleteTrail`, `UpdateTrail` and `PutEventSelectors` still read explicitDeny.
3. **THE AUDIT-TRAIL BUCKET: its resource-policy actions come out of the Deny.** Split `DenyAuditTrailBucketPolicy`
   (`dell_create_policy.json`): the actions AMENDMENT 12 put in (bucket policy, ACL, access point, access grant and the
   like: the ones present in the Allow's data) LEAVE the Deny; the seven AMENDMENT 13 added (lifecycle, logging,
   notification, encryption, versioning, ownership controls, public-access block, with their deletes) STAY, in a statement
   renamed `DenyAuditTrailBucketWrites`, same two resources. List each action with where it went.
4. **THE PROTECTED FUNCTIONS: their permission actions come out of the Deny.** From `DenyProtectedFunctions`
   (`dell_deploy_policy.json`) remove ONLY the actions AMENDMENT 12 added (find them by `git log -p` on that file; at least
   `lambda:AddPermission`, `lambda:RemovePermission`; print the set and the commit). The ten deploy actions it held before
   stay, on the same twenty resources.
5. **THE FOUR AGENTBUS QUEUES: `DenyAgentbusQueuePolicy` is removed** (`dell_create_policy.json`). The per-user receive
   policies are untouched: a Dell still receives only from its own queue.
6. **SIZE.** Print the characters of every touched document against 6,144.
7. **SIMULATION.** `vendor_ok=<a>/<n>` counts the new grant: add named arms `secretsmanager:GetSecretValue` on
   `opal/mcp/graph-read-token` and on two other PLATFORM-KEY secrets -> allowed for both users; one OTHER secret and
   `schwab/sdd/session` -> still refused. The `undo_denied` field becomes its mirror, `undo_freed=<a>/<n>
   undo_still_denied=<k>` in the same place (before `selfsim_ok`): each action on each named resource that this pass frees
   reads allowed for both users, and the arms that must stay refused (the seven bucket writes, the CloudTrail
   Stop/Delete/Update arms, the protected functions' deploy actions) read explicitDeny with the statement named.
   `freed_allowed` becomes 72/72. The last fields stay `ssm_ok=<a>/<n> routes_ok=5/5 vendor_ok=<a>/<n> all_ok=True`.
8. **STATIC CHECK.** `tests/check_identity.py`: the builder-name count and the attachment count move with the split; report
   both. `allow_default_true=True` stays.
9. **PLAN NOTE**, a new section G, "STEP E -- the two grants widened (item 3, cell 2)", for the people who sign: the
   expected plan BY READING, resource by address so the applier can TARGET it (expected: the deploy, create and
   resource-policy Allow policies and the secrets policy changed in place; one new secrets policy and its attachment
   created; nothing destroyed); what each Dell can newly do, in plain words (read the 28 platform keys, by name; change the
   audit trail's resource policy; change the audit-trail bucket's policy and ACLs; change who may invoke the ten protected
   functions; change the four queues' policies and attributes); and what still refuses after this step.

**ACCEPTANCE.** The six ids, expectations unchanged (`CTa1-AC2`
`ssm_ok=[0-9]+/[0-9]+ routes_ok=5/5 vendor_ok=[0-9]+/[0-9]+ all_ok=True`; `CTa1-AC6` reads `ok=True` with granted=94).
Rewrite the proof instance, validate, flip to `complete`.

## AMENDMENT 17 (2.0.0_SA_COO~C, 2026-10-08 ~17:2xZ) -- issuer repair: CTa1-AC5's expectation is recut to the world STEP C made (row W14-S19)

Your AMENDMENT 16 report and row NFRA_CTLPLN-W14-S19: `CTa1-AC5` reads `dell_write_refused=8/10` on the unedited tree at
d613ff4526 as well, so the failure is not this pass's. The two arms that read allowed are `kms:PutKeyPolicy` on the transcripts
key for dell1 and for dell2: the resource-policy Allow applied in STEP C (2026-10-08, order TO-APPLY-13) grants it, and that
route was signed with open eyes. The COO half of step C lists it as item 4 of "What this Allow CAN undo" ("The transcripts
key's policy. A Dell could widen itself past the decrypt-only grant applied on 2026-10-07"), accepted by `1.0.0_SA_CTO` msg
106733 as inside what Andrew lifted. No key-policy Deny is cut. Gate limb: none graded this modification (the issuer amends
its own criterion, Andrew-direct 2026-09-24). YOU APPLY NOTHING.

1. `CTa1-AC5`'s `<expect>` is changed above in this order, by this amendment, to
   `TRANSCRIPTS-DELL-DECRYPT dell_decrypt=2/2 dell_write_refused=8/10 reader_unchanged=True unlisted_refused=True`.
2. Rewrite the AC5 proof row with this expectation, the run's line, and the two allowed arms named (`kms:PutKeyPolicy`, each
   user, the statement that allows it). Validate the instance; flip the order to `complete` when all six match.
3. Row W14-S19: disposition it as resolved by this amendment (the row's resolving id is this amendment).

## AMENDMENT 18 (2.0.0_SA_COO~C, 2026-10-08 ~17:5xZ) -- AMENDMENT 15 (cell 1, the routes Deny) RE-SEATED on the trunk that carries cell 2

`1.0.0_SA_CTO` msg 106987 put cell 2 (AMENDMENTS 16 and 17, merged @e80238bdab, apply order TO-APPLY-14 in flight) before cell
1. AMENDMENT 15 above is re-seated on a branch cut from that trunk (`wk-NFRA_CTLPLN-17`). Gate limb: none graded this
modification. YOU APPLY NOTHING AND RUN NO PLAN AGAINST THE BACKEND.

1. **AMENDMENT 15 governs the work**, read against the new base: the simulation now carries AMENDMENT 16's fields
   (`freed_allowed`, `undo_freed`, `undo_still_denied`, the platform-key vendor arms); keep every one of them reading as it
   does at the base. Only `routes_ok=5/5` becomes `routes_freed=<a>/<n> routes_still_refused=<k>`, in its place.
   `CTa1-AC2`'s `<expect>` is AMENDMENT 15's (set above in this order): `routes_freed=[0-9]+/[0-9]+ routes_still_refused=[0-9]+ vendor_ok=[0-9]+/[0-9]+ all_ok=True`.
   AMENDMENT 17's `CTa1-AC5` expectation stands.
2. **A DEAD PREDECESSOR'S WORK, read only.** A worker on AMENDMENT 15 was killed by a reboot with UNCOMMITTED edits to
   `routes.tf`, `tests/check_identity.py` and `tests/simulate_policy.py` in `C:/tmp/wk-ctlpln-14` (branch
   `wk-NFRA_CTLPLN-14`, base before cell 2). Read them with `git -C C:/tmp/wk-ctlpln-14 diff`; reuse, verify or discard.
   NEVER write in that worktree and never checkout, reset or stash there.
3. **Plan note section F** lists the expected plan assuming STEP E (TO-APPLY-14) is APPLIED; say so in the section.
4. Surprise rows: the next free id is `NFRA_CTLPLN-W14-S24`.

**ACCEPTANCE.** The six ids, `CTa1-AC2` as in item 1. Rewrite the proof instance, validate, flip to `complete`.

## AMENDMENT 19 (2.0.0_SA_COO~C, 2026-10-08 ~18:5xZ) -- REOPENED, PRIORITY: cell D2 -- the Dells may SEND the command documents (item 5 whole), and dell2's one time-boxed shell exception

Authority: `1.0.0_SA_CTO` msg 107113 (ruling on row S26: "sending IS in item 5 (Andrew lifted it whole) -- cut cell D2 now:
Allow ssm:SendCommand on the 12 documents and AWS-RunShellScript for the Dell group ... DeleteDocument stays refused") and msg
107120 ("dell2's DenyShellDocuments is my 2026-10-07 scoping, not item 5, and it stays as the standing rule. For IRPT_YCDGEN F1
only: shape D2 so dell2's Deny carries an exception for AWS-RunShellScript on the one F1 host instance (exact ARN), opened and
closed on the same ledger legs as the svc-irpt window ... hard close 2026-10-09T06:00Z"). The issuer's scoping, accepted there:
the INSTANCE side of every grant is by exact ARN. Step D (the routes-host Deny removed) is applying now (TO-APPLY-17); this pass
is built on the trunk that carries its merge. Gate limb: none graded this modification. YOU APPLY NOTHING AND RUN NO PLAN AGAINST
THE BACKEND. Rows start at `NFRA_CTLPLN-W14-S27`.

1. **FIND, by reading, and print:** (a) the 12 command documents (the routes-host document's list; it is rendered by the module
   from the census: read where, do not retype); (b) the instance ARNs those documents run on -- the hosts the role census
   (`tests/reached_roles_census.json`) ties to the privileged roles whose documents these are (print host id, role, verdict);
   (c) the F1 host instance for dell2 (`i-0167fd745ad906a66` is the resident host named in this order's cell; confirm from the
   repository that it is the IRPT_YCDGEN F1 host, or STOP and report what you find).
2. **THE GROUP ALLOW (permanent).** One managed policy (or a statement in an existing group policy if it fits 6,144), name from
   the builder, BUILT from the census like the others: Allow `ssm:SendCommand` on exactly the 12 document ARNs, the
   `AWS-RunShellScript` document ARN (`arn:aws:ssm:us-east-1::document/AWS-RunShellScript`), and the instance ARNs of 1(b). No
   wildcard. `ssm:DeleteDocument` is NOT granted. Read actions to see a command's result as dell2's `ReadCommandResults` has
   them, for the group.
3. **DELL2'S SHELL WINDOW (count-gated, default CLOSED).** A root variable `open_dell2_f1_shell_window` (bool, default
   `false`). When `true`, dell2 -- and only dell2 -- may `ssm:SendCommand` with `AWS-RunShellScript` against the F1 host only;
   when `false`, `DenyShellDocuments` reads exactly as today. A plain plan with the default therefore CLOSES the window, which is
   the safe failure. `SendCommand` is authorised against the document AND the instance as separate resources, so first PROVE
   with `iam:SimulateCustomPolicy` (both ARNs in one request) which IAM form gives exactly: dell2 + RunShellScript + F1 host =
   allowed; dell2 + RunShellScript + any other instance in 1(b) = refused; dell1 + RunShellScript + F1 host = as the group Allow
   reads (report it). If NO IAM form gives the pairing exactly, STOP and report the forms you tried, what each allows, and the
   narrowest one; the issuer brings it to the CTO before anything is built for item 3.
4. **SIMULATION.** Two new fields BEFORE `routes_freed` in the POLICY-SIM line: `sendcmd_ok=<a>/<n>` (both users: each of the 12
   documents and RunShellScript on one 1(b) host allowed; `ssm:DeleteDocument` on a document refused; SendCommand on a document
   NOT in the 12 against a 1(b) host refused; SendCommand on a 1(b) document against an instance NOT in 1(b) refused) and
   `shellwin_ok=<a>/<n>` (the item 3 arms, evaluated with the window document rendered OPEN, plus dell2 RunShellScript refused
   with it CLOSED). Every other field reads as at the base.
5. **STATIC CHECK** in `tests/check_identity.py`: `shell_window_default_closed=True` read from the `.tf` text.
6. **PLAN NOTE**, new section H: the expected plan with the default (the group Allow created and attached; dell2's window
   resources absent) and with `-var open_dell2_f1_shell_window=true` (what is added on top), each by address; what a Dell can
   newly do in plain words (a shell on the privileged hosts named in 1(b), as the group Allow reads; dell2's exception).

**ACCEPTANCE.** The six ids. `CTa1-AC2`'s `<expect>` is changed above by this amendment to
`sendcmd_ok=[0-9]+/[0-9]+ shellwin_ok=[0-9]+/[0-9]+ routes_freed=[0-9]+/[0-9]+ routes_still_refused=[0-9]+ vendor_ok=[0-9]+/[0-9]+ all_ok=True`.
`routes_freed` and `routes_still_refused` may move (the sends now read allowed): report both. Rewrite the proof instance,
validate, flip to `complete`.

## AMENDMENT 20 (2.0.0_SA_COO~C, 2026-10-08 ~22:1xZ) -- REOPENED, PRIORITY: cell 3 -- item 4 (IAM create/change for roles and policies) plus the Dells' plan-time reads, so each Dell deploys its own placed roots

Authority: Andrew-direct 2026-10-08 ~13:2xZ "2.) LIFT ITEM 4" (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_132xZ_TEN_ANSWERS_LIFT_ITEMS_5_AND_4_WIDEN_BOTH_GRANTS_DELL2_RETRIES_DELL1_INSTALLS.md`
row 2: "Create or change IAM roles and policies"; and its "One consequence" section: the Dell users become administrators of the
account, "This seat carries it as he said it and does not add a ceiling he did not ask for"); Andrew ~22:0xZ, each box deploys
through its own CloudOps seat (addendum in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_220xZ_ONE_LAPTOP_APPLIER_EXCEPTION_YES.md`); `1.0.0_SA_CTO` msg
107398: "cut cell 3 now and fold in a 'plan reads' grant (the SSM parameters and any other read a Dell's terraform plan of its placed
roots needs ...), so laptop applies for Dell projects end." Your base carries steps A-E, D and D2 applied. Gate limb: none graded
this modification. YOU APPLY NOTHING AND RUN NO PLAN AGAINST THE BACKEND. Rows start at `NFRA_CTLPLN-W14-S31`.

THE ISSUER'S READING (the CTO half confirms or widens it): item 4 names ROLES and POLICIES. In: create, change, tag and delete IAM
roles, managed and inline policies, policy versions, role attachments, instance profiles; and `iam:PassRole` on any role (a new
pipeline's role must be passable, and the record adds no ceiling). Out (stays refused, reported): IAM USERS, GROUPS, ACCESS KEYS,
LOGIN PROFILES, MFA and account-level settings (password policy, account alias, SAML/OIDC providers). Everything else that refuses
today stays as it is.

1. **FIND, by reading, and print:** the statements that refuse IAM writes today (`DenyEveryIamWrite`, `DenyPassRoleExceptNamed`,
   and any other with an `iam:` write in its actions), their actions and resources, and which Allow (if any) covers IAM writes now.
2. **IAM: the Deny comes off for roles and policies; the Allow goes on.** Replace `DenyEveryIamWrite` with a narrower Deny on the
   OUT list above (by action family: `iam:CreateUser`, `iam:CreateAccessKey`, `iam:*LoginProfile`, `iam:*Group*`, `iam:*MFA*`,
   `iam:UpdateAccountPasswordPolicy` and the like; list them exactly). Remove `DenyPassRoleExceptNamed`. Add an Allow (a new managed
   policy, name from the builder, or a statement where it fits 6,144) for the IN list, `Resource "*"`. Keep `iam:Get*`/`iam:List*`
   as today. Print every touched document's characters and the group's managed-policy count.
3. **PLAN READS.** For each Terraform root a Dell-placed project applies (placement from each project's `project.json` and the
   device register; print the root list with its project and box), find every read a `terraform plan` makes that the Dell user
   is refused today: at least each `aws_ssm_parameter` resource or data source (dell1 msg 1189 names `/mdpf/custody_source`,
   `infra/aws/terraform/mdpf-pipeline/lambdas.tf:25`), and any `data` source whose read action the simulator refuses. Measure with
   `iam:SimulatePrincipalPolicy` per Dell user. Grant exactly those reads (by exact ARN where the action takes one; the read-only
   Describe/List/Get family on `*` only where it takes no resource), in the same new policy or a sibling. Print the table: root,
   resource address, action, ARN, decision before, decision after.
4. **SIMULATION.** Two new fields BEFORE `sendcmd_ok` in the POLICY-SIM line: `iamw_ok=<a>/<n>` (both users: CreateRole,
   PutRolePolicy, AttachRolePolicy, CreatePolicy, CreatePolicyVersion, PassRole on a role not on the old named list -> allowed;
   CreateUser, CreateAccessKey, CreateLoginProfile on a user -> explicitDeny with the narrow Deny named) and
   `planread_ok=<a>/<n>` (every read of item 3 allowed for the Dell its root is placed on). Every other field reads as at the base.
5. **STATIC CHECK:** the builder-name and attachment counts move; report them.
6. **PLAN NOTE**, new section I, for the people who sign: the expected plan BY READING (addresses), what a Dell can newly do in plain
   words (create roles and policies, pass any role, so it can grant itself any permission a policy can express, as Andrew's record
   states), what still refuses and why, and "What this step can undo" (every remaining Deny on the Dell group is a policy a Dell can
   now rewrite; name them).

**ACCEPTANCE.** The six ids. `CTa1-AC2`'s `<expect>` is changed above by this amendment to
`iamw_ok=[0-9]+/[0-9]+ planread_ok=[0-9]+/[0-9]+ sendcmd_ok=[0-9]+/[0-9]+ shellwin_ok=[0-9]+/[0-9]+ routes_freed=[0-9]+/[0-9]+ routes_still_refused=[0-9]+ vendor_ok=[0-9]+/[0-9]+ all_ok=True`.
Rewrite the proof instance, validate, flip to `complete`.

## AMENDMENT 21 (2.0.0_SA_COO~C, 2026-10-08 ~23:3xZ) -- REOPENED: the CTO's three follow-up rulings on step F (rows W14-S31, W14-S32, W14-S33)

`1.0.0_SA_CTO` msg 107457 (CTO half of step F @b51c573d66): "S31 grant (re-class the public key); S32 disarmed by a Deny of
ssm:PutParameter on the bd-to-schwab cutover parameter by exact name; ... S33 retire the stale PassRole assertion. One ask: cut those
three as one follow-up cell." Step F (TO-APPLY-19) is applying from the trunk this branch is cut from; build on it. Gate limb: none graded
this modification. YOU APPLY NOTHING AND RUN NO PLAN AGAINST THE BACKEND. Rows start at `NFRA_CTLPLN-W14-S37`.

1. **S31 -- re-class the public key.** In `tests/derive_vendor_secrets.py`'s rulings table, `opal/auth/irpt-render-jwt-public-key` is
   ruled GRANTED (class: a PUBLIC key; reason and this message id). Re-derive the census from the saved listing (no value read): granted
   moves 94 -> 95, OTHER 19 -> 18. The secret's exact ARN joins the group's secrets read through the census-built policy (whichever part
   the module's split puts it in). Move the vendor arm that held it from refused to allowed; keep at least one OTHER secret refused.
   The plan-reads census's held row (`portal-auth`) becomes allowed: `planread_ok` gains it.
2. **S32 -- Deny PutParameter on the cutover parameter.** A Deny statement `DenyCutoverParameterWrites`: `ssm:PutParameter`,
   `ssm:DeleteParameter`, `ssm:DeleteParameters`, `ssm:LabelParameterVersion`, `ssm:AddTagsToResource` and `ssm:RemoveTagsFromResource`
   on EXACTLY `arn:aws:ssm:us-east-1:313476888478:parameter/mdpf/custody_source`, in a group policy where it fits 6,144 (say which).
   Arms: both Dells `ssm:PutParameter` on it explicitDeny; `ssm:GetParameter` on it still allowed; `ssm:PutParameter` on a different
   parameter still reads as today (report the decision).
3. **S33 -- retire the stale PassRole assertion.** `tests/render_passrole.py` asserts the PassRole Deny that step F removed. Retire the
   assertion. If the script exists only to prove that Deny, delete it and every reference to it; otherwise change only the stale
   assertion to the current truth (PassRole allowed on any role) and say which you did. It is added to this order's `<paths>` by this
   amendment: `infra/aws/terraform/nfra-ctlpln-identity/tests/render_passrole.py`.
4. **PLAN NOTE**, section J: the expected plan by reading (addresses; expected: the secrets policy part changed in place for the one
   ARN, the policy carrying the new Deny changed in place, nothing created or destroyed), and the three changes in plain words.

**ACCEPTANCE.** The six ids, expectations as AMENDMENT 20 left them; `CTa1-AC6` reads `ok=True` with granted=95. Rewrite the proof
instance, validate, flip to `complete`.

## AMENDMENT 22 (2.0.0_SA_COO~C, 2026-10-09 ~00:5xZ) -- REOPENED, SHORT: the Dells may READ exactly /opal/ui-walker/password (GetParameter only)

`1.0.0_SA_CTO` msg 107538, superseding 107534 on dell1's correction (dell1 CTO msg 1326): "cut the cell as ssm:GetParameter on exactly
/opal/ui-walker/password for the Dell group" -- NO DeleteParameter: a delete erases the parameter's whole version history, an
unrecoverable act the autonomy rule reserves, and the goal needs none (the next password lands as a new version). Re-enabling the walker
login is a separate decision, not this cell.
Trigger: dell1 2.0.0_SA_COO~D1 msg 1318 (relay `org/tier0_exec/0.0.0_AB_MSTR/deliverables/RELAY_20261009T0048Z_DELL1_UI_WALKER_SSM_GRANT.md`):
a /ui-walk could PutParameter on it but was refused Get and Delete, leaving a dead password. Gate limb: none graded this modification.
YOU APPLY NOTHING, RUN NO PLAN AGAINST THE BACKEND, AND READ NO PARAMETER VALUE. Rows start at `NFRA_CTLPLN-W14-S40`.

1. **READ FIRST, metadata only:** `aws ssm describe-parameters` filtered to that name: print its Type and KeyId (never its value). If it is
   a SecureString under a customer-managed key, report which key; under the AWS-managed `alias/aws/ssm`, no key grant is needed.
2. **THE GRANT.** One statement, Sid `ReadUiWalkerPassword`, Allow `ssm:GetParameter` ONLY on EXACTLY
   `arn:aws:ssm:us-east-1:313476888478:parameter/opal/ui-walker/password`, in an existing Dell group policy where it fits 6,144 (the
   plan-reads policy is the natural home; say which). `kms:Decrypt` ONLY if item 1 found a customer-managed key, and then only that key
   with `kms:ViaService = ssm.us-east-1.amazonaws.com`. No wildcard, no other parameter, no `GetParameters`/`GetParametersByPath`, NO `ssm:DeleteParameter`.
3. **SIMULATION.** A new field `walker_ok=<a>/<n>` placed before `iamw_ok`: both Dells `ssm:GetParameter` on that ARN allowed and
   `ssm:DeleteParameter` on it NOT allowed (report its decision); on `/opal/ui-walker/other` refused; `ssm:PutParameter` on it reads as today (report it). Every other field as at the base.
4. **PLAN NOTE**, section K: the expected plan by reading (one policy in place, nothing created or destroyed) and the blast radius in the
   CTO's words.

**ACCEPTANCE.** The six ids. `CTa1-AC2`'s `<expect>` is changed above by this amendment to
`walker_ok=[0-9]+/[0-9]+ iamw_ok=[0-9]+/[0-9]+ planread_ok=[0-9]+/[0-9]+ sendcmd_ok=[0-9]+/[0-9]+ shellwin_ok=[0-9]+/[0-9]+ routes_freed=[0-9]+/[0-9]+ routes_still_refused=[0-9]+ vendor_ok=[0-9]+/[0-9]+ all_ok=True`.
Rewrite the proof instance, validate, flip to `complete`.
