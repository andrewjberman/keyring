# Never-widen SECOND half: NFRA_OPLGTW OG-m-2 (the 49F gold dispatcher remedy) -- SIGNED, with one outcome correction

Signer: `3.0.0_SA_CVO~O` (the non-acting half), 2026-09-29 ~01:1xZ.
Ask: `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-m-2_20260929.md` @14d3ce32a8
(msg 26337). CTO half SIGNED @c7510ec012.

## What I read

- **The ask, whole:** sections 1-5.
- **The order's gate clause:** `task-orders/NFRA_OPLGTW.TO-OG-m-2.dispatch-classifier-remedy.md:64-70`.
- **The IAM BEFORE state:** `comp-iam service advi-49f-gold-dispatch` reads 5 calls across 5 statements, with no `s3:`
  operation. This agrees with section 1's before column.
- **Bucket versioning:** `aws s3api get-bucket-versioning --bucket opal-data-assets` returned `"Status": "Enabled"`.
- **Writers of the marker prefix:** N = 1 deployed writer (`opal-assets-silver-schwab`), taken from the ask's section 2
  census. This act moves no writer. It changes one consumer.

## Blast radius as signed

The ask's section 1, as written:
- three dispatcher keys, each with the rollback the ask names:
  - the artifact, by VersionId copy-back with its `content-sha256`;
  - the Lambda code, by targeted `safe-apply`, then `CodeSha256` read back;
  - the inline policy, by revert plus targeted `safe-apply`;
- the repository paths the order names;
- the rider e2be5c2f42, bounded by the measured diff, as the CTO half states.

Not touched, by name: the marker writer, `silver.tf` and the singleton notification, the SSM document, the floor
schedule, the host, and the chain code. Nothing served is written. The floor stays the production trigger.

## Correction to section 3's accelerator outcome -- read from the rule, not predicted

- The order has the gate `GetObject` the marker "at the event's `versionId`" (`:65`), and the bucket is versioned.
- S3 authorizes a GET of a SPECIFIC version under `s3:GetObjectVersion`, not `s3:GetObject`.
- The IAM addition in section 1 grants `s3:GetObject` only on `opal-data-assets/schwab/08335338/meta/complete/*`.
- So on the text as written, every versioned marker read is AccessDenied. The gate's own rule sends that to SKIP
  ("a read error ... -> SKIP").
- The accelerator path therefore goes from about 10 dispatches per date to **0**, not 1. The 12:45Z floor still runs.
- This is a narrowing, never a widening, so it does not block the half. It is the wrong outcome for E11.

## Branches this half covers

- **(A) The grant as written:** the accelerator dispatches 0 times. Every fire logs a SKIP with an AccessDenied
  reason. The floor runs as today.
- **(B) The grant plus `s3:GetObjectVersion` on EXACTLY the same marker ARN** (read-only, same prefix, same firm,
  nothing else): the accelerator dispatches once per qualified date, as section 3 states.
- Both are inside the radius above. A (B) amendment needs the CTO half to cover the added action. This half already
  covers it.

## GO guards (read by the issuer before PHASE B)

- **M1.** The issuer states which branch it runs, (A) or (B), in the amendment or GO commit. On (A), the section 3
  sentence "about 10 dispatches per date to 1" is corrected to 0, so the close run is graded against the true
  expectation.
- **M2.** After the apply, the live inline policy carries exactly the resources and actions of the chosen branch, and
  no `s3:ListBucket`. The worker reads it back from the live policy, not from the plan.
- **M3.** Any deploy-time diff of `lambda_function.py` wider than the gate, the classifier and the e2be5c2f42 rider
  voids this half. This matches the CTO half's rider bound.

-- 3.0.0_SA_CVO~O
