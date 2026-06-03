# ADHC_CMPAWS Phase-0 — S3 + IAM Census SHAPE (AE-side)

**archetype:** EXPLORE
**Author:** 0.7.0_AE_CloudOps
**Date:** 2026-06-03
**For:** 2.0.0_SA_COO (RAVC checkpoint) + 3.0.0_SA_CVO (hand-audit oracle)
**Status:** CENSUS SHAPE — enumeration done, schema proposed; full hand-audit + sub-compiler build deferred (capacity-fill, interruptible by keep-warm GO)

This is the "S3+IAM next" sub-compiler's Phase-0 census shape per ADHC_CMPAWS (PRD v0.1 d425e072f). The "recent operational pain" angle = bucket-policy Deny census (BMKAUD class) + comp-iam cross-ref. Establishes the census dimensions the sub-compiler will derive and CVO will hand-audit to 0-diff.

## S3 census (live, 2026-06-03; 31 buckets)

**Policy presence:** 9/31 have a bucket policy; 22/31 have none.
- WITH policy: opal-analytics-dashboard, opal-cloudtrail-logs-313476888478, opal-data-bd, opal-data-demo, opal-data-inf, opal-data-portal-v2, opal-data-schwab, opal-trade-recon-ui, opalinvest-portal.
- NONE: the rest (incl. all lambda-artifacts/layers/tf-state, most opal-data-* pipelines, market-data, runner-shared, trade-recon-{confirms,reports,requests}).

**Deny census (the operational-pain axis):** ONLY 1 bucket has Deny statements:
- **opal-data-schwab** — 2 Denies, both standard AWS best-practice (well-formed, Principal:* + condition-gated, NOT mis-scoped lockouts):
  - `DenyInsecureTransport`: Deny s3:* if `aws:SecureTransport=false` (TLS enforcement).
  - `DenyUnencryptedObjectUploads`: Deny s3:PutObject if `s3:x-amz-server-side-encryption != AES256` (SSE enforcement).
- **OPERATIONAL-PAIN MECHANISM (flag):** the SSE-enforcement Deny means any writer to opal-data-schwab that does NOT send `x-amz-server-side-encryption: AES256` on PutObject gets AccessDenied — a silent-write-failure footgun (the BMKAUD-class symptom: a Deny that blocks a legitimate operation when the caller omits an expected header/condition). Census must capture the Deny CONDITION so the compiler can flag every writer-role/path that could trip it.

## IAM census (comp-iam, current baseline)
- `comp-iam gaps` = clean: **76 IAM roles parsed, 137 services scanned, 0 permission gaps**. This is the IAM-vs-boto3 cross-ref baseline the sub-compiler diffs against.

## Proposed census SCHEMA (per-bucket node + IAM edges) — for sub-compiler + CVO hand-audit
```
S3 node: { name, has_policy:bool, statement_count, allow_count, deny_count,
           deny_shape:[{sid, action, condition_keys, principal}],
           encryption:{sse_default}, versioning:bool, public_access_block:{...},
           tf_managed:bool (declared in any infra/aws/terraform/*), tf_source }
IAM edge: { role -> bucket, effective:allow|deny, actions[], via:(role-policy|bucket-policy),
            condition_gated:bool }   # cross-ref comp-iam roles x bucket policies
DRIFT axis: declared(TF) vs live(AWS) vs on-disk(source) — per the ADHC_CMPAWS 3-source cert loop.
```

## Census shape findings (for the oracle)
1. Deny surface is tiny + standard (1 bucket, 2 best-practice Denies) — low blast radius, but the SSE-Deny writer-trip risk is the named operational-pain to certify against.
2. 22 policy-less buckets: the census should record WHY (relies on IAM-role grants + account-level Block Public Access rather than bucket policy) — distinguishing "intentionally no policy" from "missing policy" is a hand-audit judgment (the oracle's call).
3. comp-iam already covers the IAM-allow axis cleanly; the NEW value this sub-compiler adds = the bucket-policy Deny axis + the declared-vs-live drift on bucket policies (not currently compiled).

## Next (on COO go / as capacity allows; interruptible)
- Enrich the per-bucket census (encryption/versioning/PAB/tf_managed) across all 31 -> hand to CVO as the hand-audit fixture.
- CVO hand-audits the census -> diff-vs-compiler until 0-diff -> S3+IAM sub-compiler becomes source-of-truth (the ADHC_CMPAWS cert loop).
- TO authoring deferred to a focused pass (per PRD). Preempted if Andrew GOs keep-warm FIX2.
