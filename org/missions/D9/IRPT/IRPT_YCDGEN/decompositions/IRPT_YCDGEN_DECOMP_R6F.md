# IRPT_YCDGEN -- DECOMPOSITION, ROUND 6 ADDENDUM F: the resident runner role's grants for the Opal path (one targeted resident.tf change)

```json
{
 "project": "IRPT_YCDGEN",
 "round": 6,
 "addendum": "F",
 "prd_ref": "org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md (v0.6; ENDPOINT unchanged since v0.5 @e6a801f7f0)",
 "prd_version": "v0.6",
 "endpoint_outcomes": ["FWD-1"],
 "round_scope": ["FWD-1"],
 "author": "2.0.0_SA_COO~Y",
 "cells": 1,
 "chains": 1,
 "join_cells": 0,
 "frozen": true,
 "revision": "1.0",
 "parent_decomp": "org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6.md",
 "ruling": "org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md batch 273 (msg 105464)",
 "cell_ids": ["YCD-f-6"]
}
```

**Why an addendum.** Branch B (Andrew's principal on the allow list) cannot run on the resident host as installed. Measured 2026-10-06 ~01:5xZ with `iam simulate-principal-policy` (one resource per call, positive controls
read `allowed`) on `irpt-ycharts-runner-role`: PutObject and GetObjectVersion on the `ycharts_opal_reports` prefix, `dynamodb:GetItem` on `etf-classifications`, and `s3:GetObject` / `s3:ListBucket` on
`opal-data-etfs/bbg/` all `implicitDeny`. The CTO ruled (batch 273, msg 105464): one targeted `resident.tf` apply, plan first, both halves; conditions 1 to 5 recorded below. Item 5 was settled before this cut
(condition 2): of the Overview map's 153 distinct held-data groups, **81 read the Bloomberg characteristics parquet under `opal-data-etfs/bbg/`** (not price-based: expense ratio, region exposure, dividend yield),
3 read `etf-classifications`, 69 have no rule; the producer loads rows for every held group regardless of pricing (`opal_producer.py:229-232`), so the no-pricing version DOES reach `bbg/`. The bucket has no bucket
policy and encrypts with AES256 (no KMS grant is needed for it); its latest dated folder is `bbg/2026-10-02/` of 31.

## Cell

| cell | hop | writes | reads | depends on |
|---|---|---|---|---|
| `YCD-f-6` | release (IAM, resident role) | `infra/aws/terraform/investor-reporting/ycharts/resident.tf` | `iam.tf`, `generate.tf`, the registry | none open |

**Writer read.** A scan of 4,246 task-order files (both roots) for a non-terminal order whose `<paths>` names `investor-reporting/ycharts/resident.tf` found 0; four orders name the root as a directory, all four
`complete`. This order is its only writer. The file's own comment names it as the `~Y` lane's resident grants.

**Contract R14 (exactly what the CTO's ruling allows, and nothing else).** Add to `aws_iam_role_policy.runner_resident` (`irpt-ycharts-runner-resident-policy`) four things, each derived from the registry or the
SDK calls, never typed except where named:
1. A local `ycdgen_opal_report_prefixes`: for each firm of `local.ycdgen_firms` (the research policy's firms, cottonwood only), the prefix
   `arn:aws:s3:::${local.resident_bucket}/${local.ycdgen_policy.source}/${local.resident_scopes[f].long}/${local.ycdgen_policy.families["YCHARTS_OPAL_REPORT"].tier}/${local.ycdgen_policy.families["YCHARTS_OPAL_REPORT"].table}/*`.
   (The existing `ycdgen_firm_prefixes` is the firm-bucket form for the research principal; this is the reporting-bucket form the repository writes: `reporting_destination` returns the product bucket.)
2. Statement `RetainTheOpalReportPdf`: `s3:PutObject`, `s3:GetObject`, `s3:GetObjectVersion` on `local.ycdgen_opal_report_prefixes`.
3. The KMS statement `ReportEncryptionViaS3ForResidentFamiliesOnly`: its `kms:EncryptionContext:aws:s3:arn` StringLike list gains `local.ycdgen_opal_report_prefixes` (`concat(write, read, opal)`); nothing else about it moves.
4. Statement `ReadTheCanonicalClassificationTable`: `dynamodb:GetItem` only, on exactly the `etf-classifications` table ARN (as `generate.tf` writes it: `arn:aws:dynamodb:${var.aws_region}:${data.aws_caller_identity.current.account_id}:table/etf-classifications`).
5. Statements `ReadTheHeldFundCharacteristics` (`s3:GetObject` on `arn:aws:s3:::opal-data-etfs/bbg/*`) and `ListTheHeldFundCharacteristicsFolder` (`s3:ListBucket` on `arn:aws:s3:::opal-data-etfs`
   with `Condition = { StringLike = { "s3:prefix" = ["bbg/", "bbg/*"] } }`). The bucket name is typed because `layout_overview.HELD_BUCKET` types it and the bucket is the shared market-data home, not a firm's; a comment says so.
No other line of any file changes; `ycdgen_host_families` and the research principal are untouched (the PDF is written by the runner role through the repository, not by the assumed principal).

**CTO conditions carried (batch 273).** (1) Exactly the opal report prefix (write, read, KMS) and `GetItem` on the table ARN, nothing else moves; with condition 2 the `bbg/` read joins because v1 reaches it (above).
(3) The playwright environment line rides the branch B install, not this apply. (4) After the apply: a 0-diff plan; the three simulate calls read `allowed`; a negative control (a 49financial `ycharts_opal_reports`
key) still `implicitDeny`. (5) For branch B's half: a request under a firm other than cottonwood refuses at the research policy; shown there. Conditions 4 and 5 are the issuer's acts, not the cell's.

## Edges and fan-out

M = 1, no dependency. The cell edits and checks offline; the plan, both halves, the apply, the 0-diff plan and the tag are the issuer's (`safe-apply`, ledger).
fanout: 1 of 1 chain, cap 8, reason: one IAM cell.

## Four-postulate record (Rule 24)

MECE: the four measured denials (prefix write/read, KMS, the table read, the bbg read) are each one numbered part of R14; the renderer's environment line is deliberately OUT (condition 3). Same grain: one policy resource.
Intent: one outcome (the Opal path's calls are granted and no other). State: no existing statement changes except the one KMS list; the research principal and the assumed-role grants do not move; negative control stays denied.

## Battery

`comp-iam` is DECLARED-NOT-APPLICABLE as the instrument (its blindness, stated: it models `(action)` not `(action, resource)` and cannot see the resident host's role as a Lambda); the live primitive is `iam simulate-principal-policy`,
one resource per call, run by the issuer after the apply with the controls above. comp-schedule and comp-adversary DECLARED-NOT-APPLICABLE.
