# TO NFRA_TRNSPT.TO-TR-i1 -- hop 1's clock and the writer principal, DESIRED ONLY (Terraform plan clean, no apply)

<to_id>NFRA_TRNSPT.TO-TR-i1</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~1</issued_to>
<issued_by>2.0.0_SA_COO~T</issued_by>
<issued_date>2026-09-30</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>transcripts</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `TR-i-1` (`decompositions/NFRA_TRNSPT_DECOMP.md`) |
**outcome_ref:** FWD-1 | **depends_on:** TR-t-1 (drained; `pull.run()` exists on your branch)

---

## WORKER FACE

### THE CELL

`TR-i-1`: the SCHEDULE of hop 1 and the principal that runs the pull job, written as Terraform in the transcripts root and
proven by a clean `plan`. **NOTHING IS APPLIED IN THIS ORDER.** The apply is a later release act under CTO+COO halves with a
change-management entry, after site Z lands the gateway tools (S04) and the stored sign-in's lifetime is measured (S05).

PRD section 4 engines: "the pull jobs: scheduled Python on an EventBridge clock, one per source ... each schedule its own
clock." C-MORATORIUM: a schedule on its own clock, never "on success of upstream"; no alarm, no SNS, no SES. C-READERS: "A
pipeline role that WRITES is a third principal and is named in the round's halves; the writer cannot be a reader by accident."
Rule 30: every resource name is `lib.opal_naming.name()` output; a builder refusal is a missing registry row, never a typed name.

**Measured at the cut:** `name('teams','global','transcripts-pull','lambda')` -> `teams-global-transcripts-pull-lambda`
(a PRODUCT scope is refused in the scope slot: "this slot takes FIRM/GLOBAL/MASTER"; the product rides the function slot).
`infra/aws/terraform/transcripts/main.tf` (READ, never edit) declares the bucket, the KMS key (alias `alias/opal-data-transcripts`,
use granted to `var.reader_principal_arns`), the TLS-only and key-only bucket policies, and the S3 backend
`opal-313476888478-terraform-state` key `transcripts/tfstate`.

**Build (DESIRED; WORLD by path, no apply):**
1. `data/transcripts/scripts/teams/NAMES.json`: one row per resource `{"<logical>": {"system":"teams","scope":"global",
   "function":"transcripts-pull","kind":"<kind>","qualifier":null,"name":"<name() output>"}}` for the Lambda, its role, its
   policy, its log group, the EventBridge rule and the gateway-bearer secret. Compute each with `name()`; where the builder
   refuses a kind, record the refusal text in your report and use the kind the builder admits (read `org/standards/NAMING_SCHEMA.json`
   resource kinds). Never hand-type a name.
2. `infra/aws/lambda/transcripts-pull/handler.py`: `lambda_handler(event, context)` reads env `TRANSPORT` (`gateway` default,
   `fixture` for tests), `FIXTURE_DIR`, `KMS_KEY_ALIAS`, builds the transport and an S3 client, calls
   `data.transcripts.scripts.teams.pull.run(..., apply=True, with_silver=True)` and returns the run record as JSON. Import the
   job from the packaged tree (`build.sh` copies `data/transcripts/scripts/`, `lib/opal_naming.py`, `org/standards/NAMING_SCHEMA.json`
   and `infra/logic/registry/*.json` into `infra/aws/lambda/transcripts-pull/dist/` and zips it to
   `dist/transcripts-pull.zip`; `pyarrow` comes from the existing layer `pandas-pyarrow-layer:1`, READ `infra/aws/lambda/lambda-layer-map.json`
   for its ARN form, never typed).
3. `infra/aws/terraform/transcripts/pull.tf`: the Lambda (python3.12, the zip, `source_code_hash`, the layer, timeout 300 s,
   env `TRANSPORT=gateway`), its IAM role and policy (s3 Get/Put/List on the bucket's `teams/transcripts/*` keys; kms
   Encrypt/Decrypt/GenerateDataKey on the key via `aws_kms_grant` for the role -- a grant, not an edit of the key policy;
   `secretsmanager:GetSecretValue` on the bearer secret name), the log group (30-day retention), the EventBridge rule
   `cron(0 13-22 ? * MON-FRI *)` with its target and `aws_lambda_permission`. Names from `NAMES.json`. No alarm, no SNS, no SES.
4. `terraform -chdir=infra/aws/terraform/transcripts init -input=false` then `plan -no-color -input=false -lock=false`: only
   ADDS; `0 to change, 0 to destroy` (the bucket and key must not move). `terraform fmt` clean.
5. Tests `data/transcripts/scripts/tests/test_pull_handler.py`: with `TRANSPORT=fixture` and the TR-t-1 fixture dir, the handler
   returns a run record with `no_person` true and makes no network call (fake S3 injected through an env-selected factory or
   monkeypatch).

### ACCEPTANCE

<criterion id="TR1-i1-AC1" cell_refs="TR-i-1"><invocation>terraform -chdir=infra/aws/terraform/transcripts plan -no-color -input=false -lock=false</invocation><expect>0 to change, 0 to destroy</expect></criterion>
`TR1-i1-AC1` -- the desired schedule and principal plan as pure additions; the bucket and key are untouched.

<criterion id="TR1-i1-AC2" cell_refs="TR-i-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T/R1_CHECKS/r1_names_check.py</invocation><expect>NAMES-CONFORMANT</expect></criterion>
`TR1-i1-AC2` -- every name in `pull.tf` is the builder's output for the recorded slots.

<criterion id="TR1-i1-AC3" cell_refs="TR-i-1"><invocation>python -m pytest data/transcripts/scripts/tests/test_pull_handler.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
`TR1-i1-AC3` -- the handler wraps the job over the fixture transport with no network.

<expected_criteria>TR1-i1-AC1,TR1-i1-AC2,TR1-i1-AC3</expected_criteria>

Dry-run at the base 2026-09-30 14:0xZ: AC1 "No changes" (no pull.tf; the expectation string absent), AC2 NAMES-BAD unreadable, AC3 "no tests ran" -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **NEVER `terraform apply`, never `safe-apply`, never touch `main.tf`.** This order produces a plan, not a deploy; it opens
  no change-management entry because nothing lands. If `init` needs a provider download that fails, that is a surprise row,
  not a workaround.
- **The bearer secret is NAMED, not created**: its value is site Z's to mint when the headless route exists.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `NFRA_TRNSPT-W1-S<k>`), and do not weaken the test to pass.

<paths>
infra/aws/lambda/transcripts-pull/handler.py
infra/aws/lambda/transcripts-pull/build.sh
infra/aws/lambda/transcripts-pull/dist/
infra/aws/terraform/transcripts/pull.tf
infra/aws/terraform/transcripts/.terraform.lock.hcl
data/transcripts/scripts/teams/NAMES.json
data/transcripts/scripts/tests/test_pull_handler.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. Do not commit `dist/` contents (add them
to your report by hash; `dist/` is a build product).

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP.md</decomp_doc> (round 1), cell `TR-i-1`.
<owned_cells>TR-i-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR1-i1-AC1, TR1-i1-AC2, TR1-i1-AC3. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~1/NFRA_TRNSPT.TO-TR-i1.schedule-and-principal-desired.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR1-i1-AC1,TR1-i1-AC2,TR1-i1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the NAMES rows and any builder refusal, the plan summary line (adds by resource), the layer ARN source, the pytest line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; the schedule here is DESIRED (plan only); applied on a later release under halves.
comp-iam: RUN -- the writer role is the third principal C-READERS names; drafted as an aws_kms_grant plus a scoped S3 policy, unapplied; the halves at release name it.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round.
lane: the <paths> block IS the grant; infra/aws/** is the AE lane at APPLY, which this order never reaches.
</preflight>

Source: PRD v0.1 section 2 hop 1 (the schedule), section 4 engines, C-READERS, C-MORATORIUM; decomposition round 1 cell TR-i-1.
