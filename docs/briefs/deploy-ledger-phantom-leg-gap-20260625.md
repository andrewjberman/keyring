# deploy_ledger.py `--pipeline` phantom-leg gap (LOW-PRI tooling TO)

**Filed:** 2026-06-25 by 0.7.0_AE_CloudOps (COO-requested, post-ETFS-W3).
**Severity:** LOW. **Tracked:** COO backlog item (2.0.0_SA_COO).
**Tool:** `.tools/deploy_ledger.py` (deploy-completion ledger; NEVER-law gate per CLAUDE.md "never leave a confirmed deploy half-landed").

## Problem

`deploy_ledger.py open --slug X --pipeline inf` auto-expands the ledger into ALL of
the pipeline's canonical S3-code-prefix legs (for `inf`: `inf-bronze`, `inf-gold`,
`inf-silver`, + 5 `inf-aux-*`). When the actual deploy is a **single Lambda TF
apply** (not an S3-code-prefix deploy), none of those legs corresponds to the work,
yet `close` REFUSES until every phantom leg is "proven":

```
REFUSED: ledger 'etfs-inf-backfill-datetarget' has unproven leg(s):
['inf-bronze','inf-gold','inf-silver','inf-aux-bronze-runner', ...]
```

### Impact
- **Noise + false-half-landed risk on the NEVER-law gate**: 8 phantom legs blare as
  "unclosed/stranded" when the real deploy (the lambda) is fully landed + verified.
- Forces the operator to close-leg each phantom leg with an N/A-with-proof note
  (what I did for `etfs-inf-backfill-datetarget` on 2026-06-25) -- honest but a
  manual workaround that pollutes the ledger with not-in-scope legs.

## Repro
1. `deploy_ledger.py open --slug test --title "single lambda" --author X --pipeline inf`
2. Deploy ONE lambda (e.g. `inf-etf-ownership-daily`) via TF apply.
3. `deploy_ledger.py close --slug test` -> REFUSED on 8 phantom S3-code legs.

## Workaround (current, proven)
Open with an explicit single leg instead of `--pipeline`:
```
deploy_ledger.py open --slug X --title "..." --author Y \
  --leg "fn-name|verify|module.resource|TF apply 0-diff + verify-on-served"
```
`--leg` format = `id|kind|target|proof_required`; allowed kinds =
`activation | ec2-baked-asset | git | s3-prefix | verify`. Used cleanly for
`etfs-w3-cot-producer` (single `verify` leg) the same day -- no phantom legs.

## Proposed fix (either is sufficient)
1. **Leg-kind detection at `--pipeline`**: when the deploy is a Lambda/TF-resource
   (not an S3-code-prefix push), do not auto-add the S3-code-prefix legs; add a
   single `verify`/`tf-lambda` leg instead. Could key off the source-map
   (`tf_resource` present + `artifact_s3_key` under `{pipeline}/` vs an
   `s3://.../code/{tier}/` prefix).
2. **`--pipeline-scope` flag** (or honor an explicit `--leg` overriding the
   auto-expand): let the opener declare "lambda-only / single-resource" so
   `--pipeline` does not expand the full S3-code leg set.

Add `tf-lambda` (or reuse `verify`) as a first-class leg kind so a single-Lambda
deploy has a natural, non-phantom home.

## Notes
- Both ETFS deploys this session (`inf-pipeline-v1.7.75`, `cot-pipeline-v0.4.4`)
  are fully landed + verified-on-served + tagged; the inf ledger's phantom legs were
  closed N/A-with-proof, the cot ledger used the `--leg` workaround. No deploy was
  actually half-landed.
- Project home: TBD (COO to slot under the appropriate NFRA tooling project).
