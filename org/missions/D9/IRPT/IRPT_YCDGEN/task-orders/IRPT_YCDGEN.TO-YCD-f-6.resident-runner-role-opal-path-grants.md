# IRPT_YCDGEN task order -- `YCD-f-6` -- ROUND 6 (THREAD): THE RESIDENT RUNNER ROLE'S GRANTS FOR THE OPAL PATH: ONE TARGETED resident.tf CHANGE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6F.md</decomp_doc>
<owned_cells>YCD-f-6</owned_cells>
</decomp_ref>
<to_id>IRPT_YCDGEN.TO-YCD-f-6.resident-runner-role-opal-path-grants</to_id>
<issued_to>0.9.0_WK_IRPT_YCDGEN~1</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE thread round; no schedule, trigger or EventBridge rule is added or read
comp-iam: DECLARED-NOT-APPLICABLE this cell DOES edit an IAM policy file (the resident runner role's inline policy), but the instrument cannot grade it: comp-iam models (action) not (action, resource) and fails green on a new resource, and the resident host's role is not a Lambda's. The live primitive is `iam simulate-principal-policy`, one resource per call with positive and negative controls, run by the issuer after the apply (CTO batch 273 condition 4)
comp-adversary: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches this surface
</preflight>

**Project:** IRPT_YCDGEN (D9/IRPT, fabric laptop) -- the Analysis report made in house, Opal-branded, with no YCharts call. **Round 6** builds one thread: Andrew submits a Cottonwood portfolio for an Overview and opens an Opal-made report. The first version carries no pricing (returns, risk, benchmark and risk-free print not available, reason `NOT_IN_THIS_VERSION`). No worker calls a vendor, writes the store, deploys or grants: the issuer makes every live act at close. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the round-6 decomposition)

### `YCD-f-6` -- the resident runner role's grants for the opal path: one targeted resident.tf change (hops release (IAM); FWD-1)
- `infra/aws/terraform/investor-reporting/ycharts/resident.tf`: R14 (1) to (5), and nothing else.
- The six checks `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round6/checks/f-6.check.py` (the issuer's; you run them and never edit them) are your acceptance; AC6 also proves nothing else moved.
- You edit and check offline. You run no `terraform plan` or `apply`, no AWS call: the issuer prints the plan, collects both halves and applies.

## 2. THE CONTRACTS YOU BUILD AGAINST (inlined from the decomposition and IRPT_BCKEND PRD v0.28)

**R14 The resident runner role's grants for the Opal path: exactly these, in `infra/aws/terraform/investor-reporting/ycharts/resident.tf` (RULINGS batch 273).** Add to `aws_iam_role_policy.runner_resident` (`irpt-ycharts-runner-resident-policy`): (1) a local `ycdgen_opal_report_prefixes`: for each firm `f` of `local.ycdgen_firms` (the research policy's firms, cottonwood only) the prefix `arn:aws:s3:::${local.resident_bucket}/${local.ycdgen_policy.source}/${local.resident_scopes[f].long}/${local.ycdgen_policy.families["YCHARTS_OPAL_REPORT"].tier}/${local.ycdgen_policy.families["YCHARTS_OPAL_REPORT"].table}/*` (derived from the registry exactly as `resident_write_prefixes` is; no bucket, firm or table name typed in it). (2) Statement `RetainTheOpalReportPdf`: `s3:PutObject`, `s3:GetObject`, `s3:GetObjectVersion` on `local.ycdgen_opal_report_prefixes`. (3) In the existing statement `ReportEncryptionViaS3ForResidentFamiliesOnly` the `kms:EncryptionContext:aws:s3:arn` StringLike list becomes `concat(local.resident_write_prefixes, local.resident_read_prefixes, local.ycdgen_opal_report_prefixes)`; nothing else about it changes. (4) Statement `ReadTheCanonicalClassificationTable`: Action exactly `["dynamodb:GetItem"]`, Resource exactly one ARN, `arn:aws:dynamodb:${var.aws_region}:${data.aws_caller_identity.current.account_id}:table/etf-classifications` (the form `generate.tf` writes). (5) Statement `ReadTheHeldFundCharacteristics`: Action `["s3:GetObject"]`, Resource `["arn:aws:s3:::opal-data-etfs/bbg/*"]`; and statement `ListTheHeldFundCharacteristicsFolder`: Action `["s3:ListBucket"]`, Resource `["arn:aws:s3:::opal-data-etfs"]`, Condition `{ StringLike = { "s3:prefix" = ["bbg/", "bbg/*"] } }`. The bucket name is typed in (5) because `layout_overview.HELD_BUCKET` types it and it is the shared market-data bucket, not a firm's; say so in a one-line comment. Every new statement carries a comment naming the SDK call it serves (file and line from the survey in section 3). No other line of the file changes, no other file changes, and the research principal and `ycdgen_host_families` are untouched. Each new statement is added to the Statement list in the order given, after `ReadFrozenCompositionAndNormalizedInput`.

## 3. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD at the issuance commit)

- Read first: `resident.tf` in full (the `locals` block at the top, `aws_iam_role_policy.runner_resident`, the existing `ReadFrozenCompositionAndNormalizedInput` and `ReportEncryptionViaS3ForResidentFamiliesOnly` statements, and the research-principal block below it that defines `ycdgen_firms`, `ycdgen_firm_prefixes`); `generate.tf` lines 210-228 (how the Lambda role writes the `etf-classifications` ARN); `iam.tf` (the role, and the comment that a second root attaches other inline policies by name: yours is `irpt-ycharts-runner-resident-policy` only).
- The SDK calls the statements serve (measured by a read of the producer path): `opal_producer.produce` -> the repository `artifacts.put` on the HOST s3 client (`reports/repository.py:465-479`: put_object IfNoneMatch, head_object on 412, get_object with VersionId); the classifier `ETFClassifier.get_classification` -> `dynamodb get_item` per ticker (`etf_classifications_dynamodb.py:56,72`); `layout_overview._read_characteristics` -> `s3 list_objects_v2` (Bucket opal-data-etfs, Prefix `bbg/`, Delimiter `/`) then `get_object` (`layout_overview.py:824,837`).
- The PDF is written by the runner role, NOT by the assumed research principal (`reports/resident_installed.py:319,336`), to the REPORTING bucket (`local.resident_bucket`), under policy `irpt-ycdgen-research-v1` family `YCHARTS_OPAL_REPORT` (tier `state`, table `ycharts_opal_reports`): `reporting_destination` returns the bucket of the policy's product scope.
- Run `terraform fmt` on the file before the checks (`terraform fmt infra/aws/terraform/investor-reporting/ycharts/resident.tf`; the formatter is the only tool you run on it besides the checks). The shell may need `terraform` from PATH; if it is absent say so in a surprise row.
- Encoding: ASCII only in HCL and comments.
- Module home and test layout: tests sit beside the code, no `conftest.py`, paths inserted at the top of each test file (as `ycharts/session/tests/test_resident_session.py:9`). Python tests run with `python -m pytest <file> -q -p no:cacheprovider` from your worktree root. Encoding: ASCII only in code and logs; no client figure and no secret in any committed file (C-FIRM, C-SECRET).

## 4. SURFACES AND BOUNDS

You READ (never edit): everything outside your `<paths>`, including `lib/`, `infra/logic/`, `docs/`, `org/missions/D9/IRPT/IRPT_YCDGEN/` (the PRD, the decompositions). NEVER: a vendor call (YCharts, Yahoo, Bloomberg or any other), an S3 or DynamoDB write, a live AWS call of any kind, a deploy, a Terraform command other than `terraform fmt` on your one file (no plan, apply, init or state read), a cookie, token or session value in any file, a figure value from a client file in any committed file, and none of another cell's files. A check you cannot satisfy inside your `<paths>` is a surprise row appended to `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (one `## <ROW-ID> -- <title>` section with a fenced json row; ids `IRPT_YCDGEN-W1-S<k>`, next unused k; `surfaced_at` the real UTC time), never an edit outside them.

<paths>
infra/aws/terraform/investor-reporting/ycharts/resident.tf
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- resident.tf is formatted (terraform fmt -check)
- **AC2** -- the Opal report prefix is derived from the registry and the research firms, and the retain statement has exactly its three actions
- **AC3** -- the KMS condition carries the write, read and Opal report prefix lists
- **AC4** -- the classification read is one GetItem on exactly the etf-classifications table
- **AC5** -- the held fund data is a Get on bbg/* and a List cut to the bbg/ prefix
- **AC6** -- nothing else moved: at most the one KMS condition line is replaced and no other file changes

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-f-6"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round6/checks/f-6.check.py AC1</invocation><expect>^f-6\.AC1 RESULT: PASS</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-f-6"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round6/checks/f-6.check.py AC2</invocation><expect>^f-6\.AC2 RESULT: PASS</expect></criterion>
  <criterion id="AC3" cell_refs="YCD-f-6"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round6/checks/f-6.check.py AC3</invocation><expect>^f-6\.AC3 RESULT: PASS</expect></criterion>
  <criterion id="AC4" cell_refs="YCD-f-6"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round6/checks/f-6.check.py AC4</invocation><expect>^f-6\.AC4 RESULT: PASS</expect></criterion>
  <criterion id="AC5" cell_refs="YCD-f-6"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round6/checks/f-6.check.py AC5</invocation><expect>^f-6\.AC5 RESULT: PASS</expect></criterion>
  <criterion id="AC6" cell_refs="YCD-f-6"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round6/checks/f-6.check.py AC6</invocation><expect>^f-6\.AC6 RESULT: PASS</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~1/IRPT_YCDGEN.TO-YCD-f-6.resident-runner-role-opal-path-grants.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-f-6.resident-runner-role-opal-path-grants`. Report once: each mechanical criterion's verdict line with the output above it; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Y):** round 6 cut from PRD v0.5 @e6a801f7f0 section 2 (the thread) and IRPT_BCKEND PRD v0.28 @3a8950aa20 items 29-31; CTO ruling msg 105387 (all cells in one issuance); decomposition round 6 revision 1.0 (`IRPT_YCDGEN_DECOMP_R6.md`). Chain `~1`, first order of addendum F (decomposition IRPT_YCDGEN_DECOMP_R6F.md), the implementation of the CTO's ruling batch 273 (msg 105464) on the branch B blockers. Item 5 settled before the cut: 81 of 153 held groups read opal-data-etfs/bbg/, so that read joins. The plan, the two halves, the apply (safe-apply), the 0-diff plan and the three simulate calls with the 49financial negative control are the issuer's acts after this cell merges. Risk WORLD: the gate's floor for infra paths and portal product files; nothing live moves inside the cell.

**DRAIN (2.0.0_SA_COO~Y, 2026-10-06 ~02:5xZ):** worker 0.9.0_WK_IRPT_YCDGEN~1 @461e1eeac3, merged 64611cd24b. The issuer read the whole diff of resident.tf (+44 -1): the local ycdgen_opal_report_prefixes (derived from resident_bucket, the research policy's source and families and resident_scopes, nothing typed), the statements RetainTheOpalReportPdf (PutObject, GetObject, GetObjectVersion), ReadTheCanonicalClassificationTable (dynamodb:GetItem on the etf-classifications ARN only), ReadTheHeldFundCharacteristics (s3:GetObject on opal-data-etfs/bbg/*) and ListTheHeldFundCharacteristicsFolder (s3:ListBucket on opal-data-etfs with s3:prefix bbg/ and bbg/*), and the one KMS StringLike list gaining local.ycdgen_opal_report_prefixes; no other line changed. **AC5 was recorded FAIL by the worker and is the ISSUER'S defect, not the cell's:** the check's findall for s3 actions also matched the required Condition key s3:prefix (row W1-S16). The check was fixed at 50ba89d585 (actions are read from the Action list only) and AC1-AC5 PASS on the merged tree; AC6 PASSES at the worker (against the branch point) and the file's diff since the branch point is byte-identical to the worker's (shown by hash); the worker's instance keeps its honest AC5 FAIL row, VALID by the checker, and this note is its disposition for the CVO's L9. NOTHING IS APPLIED: the plan, both halves, the apply, the 0-diff plan and the simulate controls are the issuer's next acts.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>6</round>
<workstream>R6F_ROLE_GRANTS</workstream>
<slot>~1</slot>
<fabric>laptop</fabric>
