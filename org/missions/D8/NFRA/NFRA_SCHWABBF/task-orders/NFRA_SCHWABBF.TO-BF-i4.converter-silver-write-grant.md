# TO NFRA_SCHWABBF.TO-BF-i4 -- the converter role may write the firm silver prefixes, enumerated per master (Terraform text only)

<to_id>NFRA_SCHWABBF.TO-BF-i4</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~5</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>keyform</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-i-4` (`decompositions/NFRA_SCHWABBF_DECOMP_R4.md`) |
**outcome_ref:** FWD-1, FWD-8 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`BF-i-4`, PRD v0.9 C-TIERS with the IAM shape of C-ALONGSIDE ("enumerated per master by the vendor file name's master prefix ... one statement entry per master, never a wildcard over the folder"). The silver converter writes the silver for every master of the schwab family. With the silver key on the firm form (cell `BF-s-4`), a firm-form master's silver is `schwab/{F}/silver/{T}/date={D}/{M}.parquet`. The converter role's silver WRITE grant is scoped to `schwab/<master>/silver/*` over `silver_source_scopes.schwab` and does not reach `schwab/49financial/silver/` or `schwab/cottonwood/silver/`: a firm-form conversion would be refused at its first write.
This cell edits Terraform TEXT and a test. It runs no `terraform init`, `plan` or `apply`, no `aws` command.

**What exists (read first).** `infra/aws/terraform/opal-assets/silver.tf` (round 2 merged `95b30c139f`): `local.silver_source_scopes` (about line 191) keys the three schwab master scopes; the per-family converter write grant is built from it at about lines 372-420 (`aws_iam_policy` "Converter grant: write + read-back-verify ONLY the ${each.key} silver/ + meta/ trees ... scoped to [...]", resources `arn:aws:s3:::${local.monolith_bucket}/${each.key}/${sc}/silver/*` and list prefixes `${each.key}/${sc}/silver/*`, and a similar block at about 474-488); and the round-2 inline policy `aws_iam_role_policy.silver_read_schwab_firm_prefix` (about 624-655) that gives the schwab converter role GetObject and ListBucket on `schwab/49financial/bronze/*` and `schwab/cottonwood/bronze/*`. Read these before editing; keep `silver_source_scopes`, every other family's grants and `silver_read_bronze` byte-identical.
The firm-form masters are 08403355 (`49financial`) and 08719286, 08134043, 08165601, 08480305 (`cottonwood`).

**Build.**
1. In `silver.tf` ADD a SEPARATE inline `aws_iam_role_policy` on the schwab converter role (the way round 2 did for the bronze read): `PutObject` (and `GetObject` and `ListBucket` for read-back verification, as the existing write grant does) on exactly these object resources, one entry per master: `arn:aws:s3:::${local.monolith_bucket}/schwab/49financial/silver/*/date=*/08403355.parquet`, and `.../schwab/cottonwood/silver/*/date=*/<master>.parquet` for each of 08719286, 08134043, 08165601 and 08480305; list prefixes `schwab/49financial/silver/*` and `schwab/cottonwood/silver/*` under an `s3:prefix` condition. NEVER a resource that ends `/schwab/49financial/silver/*` or `/schwab/cottonwood/silver/*` as the object resource. No `DeleteObject`. Do NOT touch `meta/` or `_ops/` (round 5). The old per-master silver grants STAY (the old silver keys exist until Andrew confirms their delete).
2. Rework or add tests in `data/canonical/schwab/tests/test_firm_prefix_grants.py` (the file exists with `iam_grants` and `event_rules` arms; do not change their meaning): new arms whose names contain `silver_write`: exactly one per-master resource for 08403355 under `schwab/49financial/silver/`, one per Cottonwood master under `schwab/cottonwood/silver/`, none for 08242234 or 08335338 under a firm silver prefix, no bare folder wildcard as an OBJECT resource, no `s3:DeleteObject`, the three old master-prefix silver resources still present, and `silver_source_scopes` unchanged.

### ACCEPTANCE

<criterion id="BF4-i4-AC1" cell_refs="BF-i-4"><invocation>python -m pytest data/canonical/schwab/tests/test_firm_prefix_grants.py -q -p no:cacheprovider --color=no -k silver_write</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF4-i4-AC1` -- the converter role's firm silver write entries per master, the absence of a folder wildcard and of delete, and the untouched old grants.

<criterion id="BF4-i4-AC2" cell_refs="BF-i-4"><invocation>python -m pytest data/canonical/schwab/tests/test_firm_prefix_grants.py -q -p no:cacheprovider --color=no -k "iam_grants or event_rules"</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF4-i4-AC2` -- the control: the round-2 and round-3 arms still pass (11 passed at the base).

<expected_criteria>BF4-i4-AC1,BF4-i4-AC2</expected_criteria>

Dry-run at the base: AC1 "deselected" (rc 5, no test named `silver_write`) -- FAIL as expected; AC2 `11 passed` -- PASS as expected (a control that must stay green).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named here you READ and never edit.
- **WORLD floor, nothing applied.** No `terraform init`, `plan` or `apply`, no `aws` command, no deploy (`terraform fmt -check` offline is fine). The apply is the NFRA CloudOps lane's act under `safe-apply` after the never-widen pair.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W5-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing; read `org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md` for the highest `W5-S<k>` and use the next), and do not weaken the test to pass.

<paths>
infra/aws/terraform/opal-assets/silver.tf
data/canonical/schwab/tests/test_firm_prefix_grants.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R4.md</decomp_doc> (round 4), cell `BF-i-4`.
<owned_cells>BF-i-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF4-i4-AC1, BF4-i4-AC2. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~5/NFRA_SCHWABBF.TO-BF-i4.converter-silver-write-grant.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> BF4-i4-AC1,BF4-i4-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** each statement and resource you added with its file and line, the pytest summary lines, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- Terraform text; no schedule.
comp-iam: RUN -- decomposition battery scanned silver.tf (the converter role: silver_read_bronze at ~561, the write grant over silver_source_scopes at ~372-420 and ~474-488, the round-2 firm read at ~624-655) and monolith-iam.tf, 2 Terraform files; this cell is the IAM edit (additive, per master, no folder wildcard, no delete); BLIND: the live IAM plane (0 roles read).
comp-adversary: DECLARED-NOT-APPLICABLE -- the singleton and other-family grants stay byte-identical (stated in the face).
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.9 C-TIERS, C-ALONGSIDE (IAM shape); decomposition round 4 cell BF-i-4; round-2 merge `95b30c139f`.
