# TO NFRA_SCHWABBF.TO-BF-i2 -- IAM statements per master by file-name prefix, and the event rules, for the firm prefixes (Terraform text only)

<to_id>NFRA_SCHWABBF.TO-BF-i2</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~6</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>keyform</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-i-2` (`decompositions/NFRA_SCHWABBF_DECOMP_R2.md`) |
**outcome_ref:** FWD-1, FWD-6 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`BF-i-2`, the cloud half of PRD v0.5 C-KEYFORM. Andrew-direct 2026-10-20 ~14:3xZ: "schwab vendor and 49 firm for the 0840 and cottonwood firm for the various master accounts". Two things in Terraform match the OLD master prefix and so do not see the new keys:
the box role's grants, and the S3 event rules that wake the silver converter. This cell writes the Terraform TEXT and a test. It runs no `terraform` command against AWS, no `plan`, no `apply`: the apply is the NFRA CloudOps lane's release act under `safe-apply`.

**What exists (read before editing; the line numbers are from 2026-10-20).**
- `infra/aws/terraform/canonical-schwab-ec2/monolith-iam.tf`: the box role writes `schwab/{08242234,08335338,08403355}/bronze/*` (lines ~60-81: PutObject-class resources; a ListBucket-style statement with a prefix condition; `_ops` metadata), enumerated per master, never a wildcard over masters; the box has NO GetObject and NO DeleteObject on bronze (the write-only invariant, header lines ~19-25 and ~73). Lines ~179-196 are the one-time C3(a) remap role's statements. `infra/aws/terraform/canonical-schwab-ec2/iam.tf` may carry related statements; census it and edit it ONLY if it names `schwab/<master>/bronze`.
- `infra/aws/terraform/opal-assets/silver.tf`: `local.silver_event_rules` (lines ~241-244) holds `"schwab-08242234"`, `"schwab-08335338"`, `"schwab-08403355"`, each `{ family = "schwab", prefix = "schwab/<m>/bronze/", suffix = ".zip" }`, feeding the bucket's ONE `aws_s3_bucket_notification.monolith_bronze` (lines ~769-780, a singleton: a second notification resource would delete the others).
- The converter now takes the master from the file name (cell `BF-c-2`), so one rule per FIRM prefix serves all that firm's masters.
- The new key shape: `schwab/49financial/bronze/{type}/date=YYYY-MM-DD/{master}.CRS{YYYYMMDD}.{TYPE}.zip`, and `schwab/cottonwood/bronze/...` for the four Cottonwood masters.

**Build.**
1. `monolith-iam.tf`: ADD (do not remove) statements/resources so the box role may write the 49financial firm folder ENUMERATED PER MASTER by the vendor file name's master prefix: `arn:aws:s3:::opal-data-assets/schwab/49financial/bronze/*/date=*/08242234.*`, `.../08335338.*`, `.../08403355.*`, one entry per master, in the same statement(s) that carry the old per-master resources, and the matching list-prefix condition for `schwab/49financial/bronze/` if the old grant has one. NEVER a resource `schwab/49financial/bronze/*` over the whole folder (PRD C-ALONGSIDE: "never a wildcard over the folder"). Keep the write-only invariant: no Get, no Delete. The OLD master-prefix grants STAY (the old keys exist until Andrew confirms their delete).
   No cottonwood grant here: those masters belong to the Alongside box's own role (PRD C-ONEWRITER), a separate workstream. Say so in a comment at the statement.
2. `silver.tf`: ADD two entries to `local.silver_event_rules`: one for prefix `schwab/49financial/bronze/` and one for `schwab/cottonwood/bronze/`, each `family = "schwab"`, `suffix = ".zip"`. Keep the three old entries (the old keys exist until the delete). Use the map-key style the file uses; if the repo's naming gate or `infra/logic` registry refuses a hand-typed id, that is a missing registry row: file a surprise row, do not work around it.
3. Census the converter's execution role: name every statement that grants it GetObject on Schwab bronze (the `module.silver_converter` inputs or a role policy in `infra/aws/terraform/opal-assets/`), and state whether the firm prefix is already covered. If it is NOT covered and the grant lives in `silver.tf`, add the minimal read for `schwab/49financial/bronze/*` and `schwab/cottonwood/bronze/*` (the converter reads every master of the firm; it is not the writer); if it lives in a file outside your `<paths>`, do not edit it: file a row naming the file and line.
4. Test `data/canonical/schwab/tests/test_firm_prefix_grants.py` (reads the `.tf` files as TEXT; no terraform, no network):
   - GRANTS (name contains `iam_grants`): the three per-master firm resources exist in `monolith-iam.tf`; no resource equals `.../schwab/49financial/bronze/*` as a bare folder wildcard; the three old per-master resources are still present; no `s3:GetObject` or `s3:DeleteObject` was added to the box role's statements.
   - EVENT RULES (name contains `event_rules`): `local.silver_event_rules` has exactly the old three keys plus entries for the two firm prefixes, each family `schwab` and suffix `.zip`; the notification resource is still singular (exactly one `aws_s3_bucket_notification` for the monolith in the opal-assets root).
   - FMT: if `terraform` is on PATH, `terraform fmt -check` on the edited files exits 0; skip with a printed reason if it is not (no network, no init).

### ACCEPTANCE

<criterion id="BF2-i2-AC1" cell_refs="BF-i-2"><invocation>python -m pytest data/canonical/schwab/tests/test_firm_prefix_grants.py -q -p no:cacheprovider --color=no -k iam_grants</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF2-i2-AC1` -- the box role's per-master firm-prefix write entries, the absence of a folder-wide wildcard, and the untouched old grants.

<criterion id="BF2-i2-AC2" cell_refs="BF-i-2"><invocation>python -m pytest data/canonical/schwab/tests/test_firm_prefix_grants.py -q -p no:cacheprovider --color=no -k event_rules</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF2-i2-AC2` -- the event rules for the two firm prefixes beside the three old ones, and the singleton notification.

<expected_criteria>BF2-i2-AC1,BF2-i2-AC2</expected_criteria>

Dry-run at the base 2026-10-20: both "file or directory not found" (rc 4) -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named here you READ and never edit.
- **WORLD floor, nothing applied.** You run no `terraform init`, `plan` or `apply`, no `aws` command, and no deploy. The apply is the NFRA CloudOps lane's act under `safe-apply` after the never-widen pair; the order of "event rule first, then copy" is the cutover's choice, not yours.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W6-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test to pass.

<paths>
infra/aws/terraform/canonical-schwab-ec2/monolith-iam.tf
infra/aws/terraform/canonical-schwab-ec2/iam.tf
infra/aws/terraform/opal-assets/silver.tf
data/canonical/schwab/tests/test_firm_prefix_grants.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R2.md</decomp_doc> (round 2), cell `BF-i-2`.
<owned_cells>BF-i-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF2-i2-AC1, BF2-i2-AC2. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~6/NFRA_SCHWABBF.TO-BF-i2.firm-prefix-grants-and-event-rules.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> BF2-i2-AC1,BF2-i2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** each statement and map entry you added with its file and line, the converter-role census (statements named, covered or not), the pytest summary lines, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- Terraform text; no schedule edit.
comp-iam: RUN -- decomposition battery scanned 2 Terraform files (monolith-iam.tf, iam.tf) and 3 enumerated masters; this cell is the IAM edit (additive, per master, no folder wildcard, write-only invariant kept); BLIND: the live IAM plane (0 roles read), the converter's execution role (read by the worker from the Terraform at the cell, item 3).
comp-adversary: DECLARED-NOT-APPLICABLE -- decomposition findings 4 (no firm event rule means a firm-key day converts nothing; with it, once per object) and the singleton-notification hazard are inlined above.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.5 C-KEYFORM, C-ALONGSIDE (IAM shape), C-ONEWRITER; CTO round-1 analysis ruling 1 (IAM and event rules for the firm prefixes); decomposition round 2 cell BF-i-2.
