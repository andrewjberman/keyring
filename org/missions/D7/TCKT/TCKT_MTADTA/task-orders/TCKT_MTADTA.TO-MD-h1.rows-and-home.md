# TO TCKT_MTADTA.TO-MD-h1 -- registry rows, the R20 entry, targets regenerated, the bucket and key in Terraform (desired)

<to_id>TCKT_MTADTA.TO-MD-h1</to_id>
<project>TCKT_MTADTA</project>
<issued_to>0.9.0_WK_TCKT_MTADTA~1</issued_to>
<issued_by>2.0.0_SA_COO~S1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>

**Directive:** D7 | **Fabric:** dell1 | **Decomp cell:** `MD-h-1` (`decompositions/TCKT_MTADTA_DECOMP.md`) |
**outcome_ref:** FWD-1, FWD-7, FWD-8 | **depends_on:** none | **queue:** this slot's next order is `TO-MD-a1`

---

## WORKER FACE

### THE CELL

`MD-h-1`, HOME. Today the naming builder refuses everything this project needs (measured at the cut):

```
address('m365-metadata','trino','bronze','audit_events','date=20261016', object='events.json.gz')
  -> ValueError: source 'm365-metadata' is not a systems.json key
grade('opal-data-trino', 'S3_BUCKET') -> RaiseDefect: B2: 'trino' after opal-data- is no scope key
```

You add the two registry rows, regenerate the targets, write the R20 entry for a deliberate departure, and write the Terraform for the
bucket and its key. **You apply nothing and call no AWS API.** The bucket is for the eight operations team members' Microsoft 365 audit
metadata; Andrew's words: "I think all of this should be stored in a bucket called opal-data-trino", "its a product folder so follows
product rules", and (the departure) "all other domains/accounts should be dropped at the outset and not stored".

### BUILD

1. **`infra/logic/registry/scopes.json`** -- append this row to the `scopes` list in the file's existing key order (read the file's
   `_about` and the `transcripts` row first; add any field `validate` then demands, and nothing else):
   `{"key": "trino", "class": "PRODUCT", "long": "trino", "short": "trino", "tenancy": "GENERAL", "bucket": "opal-data-trino",
   "bucket_provisioned": false, "aliases": [], "note": "<one sentence: Opal-internal Microsoft 365 audit metadata for Andrew's eight operations team members (project TCKT_MTADTA); Andrew-direct 2026-10-16, 'its a product folder so follows product rules'; GENERAL tenancy: employee activity metadata, not client or partner custodial information (R4 narrowed 2026-09-18), the same shape as the transcripts row>"}`.
2. **`infra/logic/registry/systems.json`** -- append a VENDOR row `{"key": "m365-metadata", "class": "VENDOR", "long":
   "microsoft-365-metadata", "display_name": "Office 365 Management Activity API", "owner_directive": "D7", "owner_claim": "measured",
   "owner_basis": "<cite Andrew-direct 2026-10-16 ~06:0xZ 'let's get that brief refactored into this tckt center metadata project and kicked off on dell1', and that his folder word m365-metadata lands as the SOURCE segment of the ruled key grammar>"}` beside the `teams` and `outlook`
   rows. If `validate` refuses a class or token, the refusal text is your report and a surprise row; never bend the schema.
3. **`infra/logic/registry/root_map.json`** -- add a root entry `trino` (read `_about` and the `transcripts` entry as the template): default
   system `m365-metadata`, scope `trino`, source `m365-metadata`, evidence one sentence citing this order; exceptions for the three names the
   MD-a-1 order will create under system `globgrph`: `globgrph-trino-access-group` (type group), `globgrph-trino-access-lambda` (lambda),
   `globgrph-trino-access-role` (role). Add only what the file's own `_about` says an entry needs.
4. `python lib/opal_naming.py validate` -> exit 0.
5. `python lib/opal_naming.py generate --out .` and commit every file that changed; hand-edit none. At the cut, 8 of the 19 targets
   ALREADY differ from the generator before any new row (loaders.py, firm-config.mjs, generated_locals.tf, opal_name.tftest.hcl and four
   more): your regenerate restamps those for two reasons at once. Report the changed list and, for each, whether the diff is the hash/comment
   line only. If `portal/` files change and your worktree carries a portal checkout, commit them inside `portal/` on its nested branch and
   name that commit; if it carries none, say so in your report.
6. **`infra/logic/06_CONFORMANCE_LEDGER.md`** -- read section 4 (the entry schema) and section 6 (the register). Add ONE R20 entry,
   status as the schema's acknowledged value, covering two departures:
   - **A1 INGESTION / R9.** Bronze for source `m365-metadata` holds only the events of Andrew's eight named accounts, after the field
     levers, not the raw blob Microsoft ships; every other account is dropped before the first write and never stored. Reason, VERBATIM:
     "all other domains/accounts should be dropped at the outset and not stored" (Andrew-direct 2026-10-16 ~05:4xZ, record
     `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_054xZ_SPINE_BECOMES_TCKT_MTADTA_OPS_EIGHT_DROP_AT_OUTSET_GLOBGRPH_ROLE_ONLY.md`).
     Acknowledger: Andrew, by that same word. Kind: PERMANENT (his word names no condition; he may reverse it). State the consequence in
     one line: a population or field error cannot be repaired from bronze, and the source keeps 7 days.
   - **A3 NAMING.** The KMS key of bucket `opal-data-trino` has no builder kind (`name(..., 'key')` -> ValueError: kind 'key' is neither a
     NAMING_SCHEMA.json kind nor a cadence). The key's alias follows the `transcripts` root's alias form. Do NOT edit `NAMING_SCHEMA.json`.
   - The entry text must contain the strings `m365-metadata`, `dropped at the outset`, `R9`, `Andrew-direct`, `opal-data-trino`, `PERMANENT`, `KMS`.
7. **`infra/aws/terraform/trino/main.tf`** -- model it on `infra/aws/terraform/transcripts/main.tf` lines 1-135 (read them): the
   `terraform {}` block and S3 backend (state key `trino/tfstate`), the provider, `data "aws_caller_identity" "current"`, the scope row read
   by the root's directory name (`local.scope_row`, `local.bucket` -- the bucket name is NEVER a literal in the file), and exactly these
   resource labels, which the next order depends on: `aws_s3_bucket.trino`, `aws_s3_bucket_server_side_encryption_configuration.trino`
   (SSE `aws:kms`, bucket key on, the key below), `aws_s3_bucket_public_access_block.trino` (all four true), `aws_kms_key.trino`
   (symmetric, `enable_key_rotation = true`, 30-day deletion window, **no inline `policy`**: the access order attaches the one policy
   with `aws_kms_key_policy`), `aws_kms_alias.trino`. Add a header comment stating how privacy is held: by the key and the
   single-principal policies of `access.tf`, not by this file. **This file declares NO bucket policy, key policy, role, group or
   Lambda.** No SNS, alarm or notification resource of any kind.

### ACCEPTANCE

<criterion id="MD1-h1-AC1" cell_refs="MD-h-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R1_CHECKS/r1_check_h1.py rows</invocation><expect>H1-ROWS-OK</expect></criterion>
`MD1-h1-AC1` -- `validate` passes, the builder emits the ruled address, name and both grades, and a fresh generate is byte-identical to the committed targets.

<criterion id="MD1-h1-AC2" cell_refs="MD-h-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R1_CHECKS/r1_check_h1.py ledger</invocation><expect>H1-R20-OK</expect></criterion>
`MD1-h1-AC2` -- the R20 entry exists with its required strings.

<criterion id="MD1-h1-AC3" cell_refs="MD-h-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R1_CHECKS/r1_check_h1.py tf</invocation><expect>H1-TF-OK</expect></criterion>
`MD1-h1-AC3` -- `main.tf` declares the bucket, its SSE-KMS default, the public-access block and the rotating key, and nothing of the access policies.

<expected_criteria>MD1-h1-AC1,MD1-h1-AC2,MD1-h1-AC3</expected_criteria>

Dry-run at the base 2026-10-16 ~06:5xZ: AC1 `H1-ROWS-REFUSED builder: source 'm365-metadata' is not a systems.json key`, AC2
`H1-R20-MISSING [...]`, AC3 `H1-TF-REFUSED no main.tf` -- each FAIL as expected. Run the check files from the repository (worktree) root.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else you READ and never edit.
- **WORLD by the gate's path floor (`infra/`); NOTHING is applied.** No `terraform apply`, no `terraform init` against the remote
  backend, no AWS call, no S3 access, no Microsoft call. `terraform fmt -check` on your file is welcome; it needs no network.
- No alert, alarm, SNS or notification resource anywhere (standing moratorium).
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `TCKT_MTADTA-D1-W1-S<k>`, in the investigation file below, fields `spec_asserts` and `world_is`), and do not weaken a check to pass it.
- Commit only through `.tools/safe-commit.sh` with `--author "0.9.0_WK_TCKT_MTADTA~1 <0.9.0_WK_TCKT_MTADTA~1@opal.agent>"`, `-F` a message
  file you write with the Write tool, and `-- <paths>`.

<paths>
infra/logic/registry/scopes.json
infra/logic/registry/systems.json
infra/logic/registry/root_map.json
infra/logic/06_CONFORMANCE_LEDGER.md
infra/aws/terraform/trino/main.tf
data/firm_registry.json
data/assets/scripts/gold/investor_reporting/directory_runner.py
data/assets/scripts/gold/investor_reporting/holdings_snapshot.py
data/assets/scripts/gold/runners_49f/perfrp_firm_pin.py
data/black_diamond/scripts/bronze/_asset_dim_rest_pin.py
data/black_diamond/scripts/gold/lib/platinum_dest_view.py
data/mdpf/config/bronze_homes.json
.tools/ds-precommit-check.py
infra/aws/lambda-edge/_shared/firm-config.mjs
infra/aws/lambda/investor-reporting/_authz/loaders.py
infra/aws/lambda/exec-summary-generator/platinum_dest_view.py
infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/platinum_dest_view.py
infra/aws/lambda/portal_data_proxy/firm_page_access.py
infra/aws/terraform/modules/opal_name/generated_locals.tf
infra/aws/terraform/modules/opal_name/tests/vectors.json
infra/aws/terraform/modules/opal_name/tests/opal_name.tftest.hcl
portal/src/lib/firmAccess.ts
portal/src/pages/InvestorReporting/header/firmDisplayNames.generated.ts
portal/src/pages/InvestorReporting/header/vendorDisplayNames.generated.ts
org/missions/D7/TCKT/TCKT_MTADTA/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_MTADTA/decompositions/TCKT_MTADTA_DECOMP.md</decomp_doc> (round 1), cell `MD-h-1`.
<owned_cells>MD-h-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: MD1-h1-AC1, MD1-h1-AC2, MD1-h1-AC3. Instance at `org/missions/D7/TCKT/TCKT_MTADTA/deliverables/0.9.0_WK_TCKT_MTADTA~1/TCKT_MTADTA.TO-MD-h1.rows-and-home.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> MD1-h1-AC1,MD1-h1-AC2,MD1-h1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the two rows verbatim, the validate line, the changed-target list with the diff nature of each, the three check lines, the
R20 entry's heading line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; no schedule is applied.
comp-iam: DECLARED-NOT-APPLICABLE for this cell -- it declares no principal; the policies are MD-a-1's, and `comp-iam gaps` runs at the drain over the merged root.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; the restamp hazard is the issuer's at the drain (decomposition ruling 7).
lane: the <paths> block IS the grant; infra/logic/** is PLATFORM_LOGIC_DOCS (CRO lanes) -- the worker grant admits the order's paths, per the NFRA_TRNSPT TO-TR-g1 precedent (rows prepared on a branch, landed by merge, the restamp named to its owners at the drain).
</preflight>

Source: PRD v0.2 C-HOMES, C-ACCESS (the key), DECISIONS 1 and 4, SURFACE MANIFEST R1 C1; decomposition round 1 cell MD-h-1.
