# TO NFRA_SCHWABBF.TO-BF-g5 -- the box role and the converter role may write the firm buckets' state prefix, enumerated per master (Terraform text only)

<to_id>NFRA_SCHWABBF.TO-BF-g5</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~4</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>keyform</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-g-5` (`decompositions/NFRA_SCHWABBF_DECOMP_R5.md`) |
**outcome_ref:** FWD-1, FWD-6, FWD-8 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`BF-g-5`, PRD v1.0 C-TIERS with the IAM shape of C-ALONGSIDE ("enumerated per master by the vendor file name's master prefix ... one statement entry per master, never a wildcard over the folder"). The state tier of a firm-form master lives in the FIRM bucket (`opal-data-49financial`, `opal-data-cottonwood`), not in `opal-data-assets`. Neither the box role (the puller's run records) nor the converter role (the completion marker, the conversion manifest, the backfill status) can write there today: the first state write of a firm-form master would be refused.
This cell edits Terraform TEXT and a test. It runs no `terraform init`, `plan` or `apply`, no `aws` command.

**The objects (fixed in `decompositions/NFRA_SCHWABBF_DECOMP_R5.md`).** For firm-form master M (08403355 under `49financial`, bucket `opal-data-49financial`; 08719286, 08134043, 08165601, 08480305 under `cottonwood`, bucket `opal-data-cottonwood`): `schwab/{F}/state/{table}/date={D}/{M}.{name}` with tables `complete`, `conversions`, `pulls`, `backfill_status`, `daily_pull`.
- The BOX role (the 49F box) writes, for 08403355 only: the `pulls` and `daily_pull` tables (PutObject). The Cottonwood masters belong to the Alongside box's own role (not this cell; CTO msg 109915 and PRD C-ONEWRITER).
- The CONVERTER role (`aws_iam_role.silver["schwab"]`) writes AND reads back, for 08403355 and the four Cottonwood masters: tables `complete`, `conversions`, `backfill_status` (PutObject; GetObject and ListBucket for the read-back, the closure verdict and the "newest partition" read of the backfill status).

**What exists (read first).** `infra/aws/terraform/canonical-schwab-ec2/monolith-iam.tf`: the box role's statements (`MonolithSchwabWrite`, `MonolithSchwabList`, and the `_ops` and `meta/pulls` grants for the three masters around lines 86-96; round 3 left the firm-prefix bronze write for 08403355 only). `infra/aws/terraform/opal-assets/silver.tf`: the converter role; round 4 added `aws_iam_role_policy.silver_write_schwab_firm_silver` (about lines 668-704; PutObject and GetObject on five per-master silver resources, ListBucket under `s3:prefix`, no delete) and round 2 added `silver_read_schwab_firm_prefix` (bronze read). Use the same local names for the monolith bucket (`local.monolith_bucket`); the firm buckets are named in the registry (`infra/logic/registry/scopes.json`, each firm row's `bucket`): read how other roots in `infra/aws/terraform/` reference `opal-data-49financial` and `opal-data-cottonwood` (a data source, a variable or a literal) and follow that, never retype a bucket where a reference exists. Read the firm buckets' own Terraform (bucket policy, encryption: the puller sends `--sse AES256`) and name in your report anything that would refuse these writes (a deny statement, a required KMS key); you do NOT edit that Terraform (it is outside your `<paths>`).

**Build.**
1. `monolith-iam.tf`: ADD (do not remove anything) a statement on the box role: PutObject only, on `arn:aws:s3:::opal-data-49financial/schwab/49financial/state/pulls/date=*/08403355.*` and `.../state/daily_pull/date=*/08403355.*`. No Get, no Delete, no wildcard over the folder. The old `_ops`/`meta/pulls` grants in `opal-data-assets` STAY (the old keys exist until Andrew confirms their delete).
2. `silver.tf`: ADD a separate inline `aws_iam_role_policy` on the schwab converter role with PutObject and GetObject on `arn:aws:s3:::opal-data-49financial/schwab/49financial/state/{complete,conversions,backfill_status}/date=*/08403355.*` and `arn:aws:s3:::opal-data-cottonwood/schwab/cottonwood/state/{complete,conversions,backfill_status}/date=*/<master>.*` for each of the four Cottonwood masters (one resource entry per master and table), and ListBucket on each firm bucket under an `s3:prefix` condition of `schwab/49financial/state/*` and `schwab/cottonwood/state/*` respectively. No DeleteObject. The existing grants and `silver_source_scopes` stay byte-identical.
3. Tests: new arms in `data/canonical/schwab/tests/test_firm_prefix_grants.py` whose names contain `state_write`: the box statement has exactly the two 08403355 resources and PutObject only; the converter policy has one resource per (master, table) as above in the right bucket, no entry that ends `/state/*` as an OBJECT resource, no `s3:DeleteObject`, the bucket names come from the same source the repo uses elsewhere (or equal the registry's `bucket` for each firm); every earlier arm stays green (`silver_write`, `iam_grants`, `event_rules`: 18 passed at the base).

### ACCEPTANCE

<criterion id="BF5-g5-AC1" cell_refs="BF-g-5"><invocation>python -m pytest data/canonical/schwab/tests/test_firm_prefix_grants.py -q -p no:cacheprovider --color=no -k state_write</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF5-g5-AC1` -- the state-tier write entries per master in the right bucket, PutObject-only on the box, no folder wildcard, no delete.

<criterion id="BF5-g5-AC2" cell_refs="BF-g-5"><invocation>python -m pytest data/canonical/schwab/tests/test_firm_prefix_grants.py -q -p no:cacheprovider --color=no -k "silver_write or iam_grants or event_rules"</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF5-g5-AC2` -- the control: the round-2 to round-4 arms still pass (17 selected at the base).

<expected_criteria>BF5-g5-AC1,BF5-g5-AC2</expected_criteria>

Dry-run at the base: AC1 "deselected" (rc 5, no test named `state_write`) -- FAIL as expected; AC2 passes (a control that must stay green).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named here you READ and never edit.
- **WORLD floor, nothing applied.** No `terraform init`, `plan` or `apply`, no `aws` command, no deploy (`terraform fmt -check` offline is fine). The apply is the NFRA CloudOps lane's act under `safe-apply` after the never-widen pair.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W4-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing; read the investigation file for the highest `W4-S<k>` and use the next). Append the row to `org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md` at the BYTE level (do not use the Edit tool on that file: it mixes CRLF and LF; insert before the closing `]` and keep the file's own line endings; verify `git diff --numstat` shows only added lines). Do not weaken the test to pass.

<paths>
infra/aws/terraform/canonical-schwab-ec2/monolith-iam.tf
infra/aws/terraform/opal-assets/silver.tf
data/canonical/schwab/tests/test_firm_prefix_grants.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R5.md</decomp_doc> (round 5), cell `BF-g-5`.
<owned_cells>BF-g-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF5-g5-AC1, BF5-g5-AC2. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~4/NFRA_SCHWABBF.TO-BF-g5.iam-state-tier-firm-bucket.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> BF5-g5-AC1,BF5-g5-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** each statement and resource you added with its file and line, what the firm buckets' own Terraform says about writes (deny, encryption), the pytest summary lines, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- Terraform text; no schedule.
comp-iam: RUN -- decomposition battery scanned silver.tf (converter role: silver_read_bronze at ~561, the write grant at ~372-420, the round-2 bronze read at ~624-655, the round-4 silver write at ~668-704) and monolith-iam.tf (box role), 2 Terraform files; the firm buckets' own policies are read by the worker at the cell (item above) and were not before; this cell is the IAM edit (additive, per master, no folder wildcard, no delete); BLIND: the live IAM plane (0 roles read).
comp-adversary: DECLARED-NOT-APPLICABLE -- decomposition finding 1 (a different bucket) is the cell; the singleton and other-family grants stay byte-identical.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v1.0 C-TIERS, C-ALONGSIDE (IAM shape); CTO msgs 109915, 109966, 109970; decomposition round 5 cell BF-g-5; round-4 merge `16d4ae3ea0`.
