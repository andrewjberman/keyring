# Deploy Completion Record
**Date opened:** 2026-09-24T15:23:52.786979+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP rm-7: opal-amgt-scoped-api serves GET .../print?format=rich, pdf default unchanged
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | module.scoped_amgt_api.aws_lambda_function.this (opal-amgt-scoped-api) | CodeSha256 AFTER differs from BEFORE DEQQiCH+UoUMd7EZSQA5RTsILDY5+ubb9Y3gVLE5elU= |  | OPEN |
| L2 | verify | the default print path, GET /api/scoped/amgt/security/BA_US_Equity/print with no format | content-stream digest EQUAL to BEFORE 5f150ad66d00e76f5364058eda899723f0b1a9623af058ce558f974ac6c5d602, with CAT_US_Equity 7c017870dea741188c768a812637b10dd94b6d90ee1e10a7392a511c48d2025f DIFFERENT as the live negative control |  | OPEN |
| L3 | verify | the same route with format=rich and with format=xml | rich returns 200 text/markdown over 20 KB whose first line is a Markdown heading naming the security, and xml returns 400 |  | OPEN |

## Log

- 20260924T152352Z OPENED by 0.7.0_AE_CloudOps~A with 3 leg(s)

---

## THE ACT -- one function, one artifact write, one apply

**Order:** `AMGT_RESAPP.TO-AMGT-rm-7` (amendments 2 `@a2573d8540` and 3, issued by `2.0.0_SA_COO~Z`).
**Binding:** rm-4 on CLOUD, drain `3350abb022`, adapter commit `791806b1c9`. Verified at the store, not
the report: `git log -1 --format=%h -- lib/research/api/scoped_amgt.py` on CLOUD reads `791806b1c9`.
**Function:** `opal-amgt-scoped-api` only. **Terraform:** `infra/aws/terraform/harvest/scoped-amgt-api.tf`
through `safe-apply`. A plan showing any second resource move is a REFUSAL, printed and reported.

⛔ **THIS ENTRY IS OPENED BEFORE THE BUILD, NOT BEFORE THE APPLY.** The apply is not the act that moves
the code. `modules/yang-lambda` takes `source_code_hash` from the S3 artifact object's metadata, so the
irreversible step is the artifact WRITE; an apply on an unchanged object is a measured 0-diff. Opening at
the apply would have left the one destructive act outside the entry.

## BEFORE STATE -- measured immediately before the build

| what | value |
|---|---|
| `CodeSha256` deployed | `DEQQiCH+UoUMd7EZSQA5RTsILDY5+ubb9Y3gVLE5elU=` |
| artifact key | `s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip` |
| artifact `VersionId` | `ZacA2Kn0CWoJqOFLvTPe2kzZ4x_ctTYe` |
| artifact `LastModified` / size | `2026-09-23T21:58:26Z` / `807904` bytes |
| artifact `content-sha256` | `DEQQiCH+UoUMd7EZSQA5RTsILDY5+ubb9Y3gVLE5elU=` (identical to deployed) |

Served print reads, BA_US_Equity, three comparands each (`before_reads.json` carries the full record):

| read | bytes | raw sha256 | normalised | content-stream |
|---|---|---|---|---|
| no format | 77862 | `53c76f2170b5d423...` | `fab9a93f5b4bbc68...` | `5f150ad66d00e76f...` |
| `format=rich` | 77862 | `76d7cb6c31ca4b5c...` | `fab9a93f5b4bbc68...` | `5f150ad66d00e76f...` |
| `format=xml` | 77862 | `9e59bd9f9a138ae5...` | `fab9a93f5b4bbc68...` | `5f150ad66d00e76f...` |
| CAT_US_Equity, no format | 89537 | `7d2e36d36a294f0f...` | `999d6b2309d0528a...` | `7c017870dea74118...` |

All three BA reads return `application/pdf` and share ONE content digest: under the deployed bytes the
`format` parameter is ignored entirely, which is the behavioural confirmation that rm-4 is not deployed.

## L2's COMPARAND IS THE CONTENT-STREAM DIGEST, and why the other two are unusable here

Issuer amendment 3 (msg 25592), on this lane's measurement; rows `AMGT_RESAPP-Z-S253` / `-Z-S254`.

- **raw** -- the renderer stamps a wall-clock `/CreationDate`, so two IDENTICAL requests four seconds
  apart already differ (77862 bytes both, exactly one differing span). Always false; the order made a
  different sha the ROLLBACK trigger, so the diligent branch was the harmful one.
- **normalised** -- fixes the stamp but not this deploy: `render_pack.py:295` is
  `PdfPages(metadata={"CreationDate": None})`, which REMOVES the entry rather than fixing it, and dropping
  those bytes shifts every xref offset after them. Simulated on the live bodies: `77862 -> 77388`,
  `fab9a93f...` -> `9895fc74...`, SURVIVES **False**.
- **content-stream** -- page count plus each page's decoded content stream. Exercised on all three arms:
  identical across two invokes differing in the stamp; identical across the metadata strip; and DIFFERENT
  for CAT, so "equal" is still free to fail. A moved figure, changed number or dropped section all move it.

## ROLLBACK -- a re-point of the artifact plus a re-apply, never a rebuild

The artifact bucket has **versioning Enabled**, so the prior package is preserved by VersionId and needs
no backup copy. To roll back:

1. `aws s3api copy-object --bucket opal-313476888478-lambda-artifacts
   --key research/opal-amgt-scoped-api.zip
   --copy-source "opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip?versionId=ZacA2Kn0CWoJqOFLvTPe2kzZ4x_ctTYe"
   --metadata-directive COPY` -- restores the exact prior bytes AND their `content-sha256` metadata, which
   is what terraform reads.
2. `.tools/safe-apply.sh` on the same root -- the function returns to
   `CodeSha256 DEQQiCH+UoUMd7EZSQA5RTsILDY5+ubb9Y3gVLE5elU=`.
3. Re-read: L2's content digest must return to `5f150ad66d00e76f...` and `?format=rich` must serve a pdf
   again.

⛔ **The rollback is NOT a rebuild.** A rebuild from source would produce different bytes and would not
restore the state this entry records.

## BLAST RADIUS -- what this act may touch

ONE Lambda's code package. No IAM move, no route move (a query parameter does no path matching, and the
`/print` route key is unchanged), no dependency layer move (`print-deps-layer.tf` expected untouched; a
plan showing it move is the refusal), no DynamoDB or S3 data write, no schedule, no alarm. The portal
client action ships with the portal's own deploy and is not in this act.

**Reachability:** the function is portal-facing behind the CUSTOM authorizer, so the default `/print`
path is live for real users during the apply -- which is exactly what L2 exists to protect, and why L2 is
graded on a comparand that can actually express "unchanged".
