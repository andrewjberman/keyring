# 0.4.0_DT Log: ADVI_49PUSH.048 -- opal-partners-data firm bucket cache deploy
**Date:** 2026-04-09
**Agent:** 0.4.0_DT_ClientPlatform
**Tag:** partners-api-v1.15.5
**TO:** ADVI_49PUSH.048

## Change

Added module-level `_bucket_cache: dict = {}` at line 76 of lambda_function.py.
Modified `get_firm_bucket()` (line 164) to return cached bucket on warm hits
before calling DynamoDB. Only calls `users_table.get_item()` on first request
per firm_id per Lambda instance.

Lines changed:
- Line 76 (added): `_bucket_cache: dict = {}`
- Lines 173-186: early-return + cache-write logic in get_firm_bucket()

Call sites unchanged: lines 1283 and 1355.

## Compiler Tools

| Tool | Command | Result |
|------|---------|--------|
| grep | `grep -n "get_firm_bucket\|_bucket_cache" lambda_function.py` | 1 def, 2 call sites, cache dict confirmed |
| py_compile | `python -m py_compile lambda_function.py` | PASS |

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Read lambda_function.py | get_firm_bucket at line 161 (pre-change), no existing cache |
| 2 | Apply code change | _bucket_cache dict + early-return in get_firm_bucket |
| 3 | py_compile | PASS |
| 4 | git commit (source) | f3a5f003 perf(opal-partners-data): cache get_firm_bucket... |
| 5 | build-and-upload.sh partners-api opal-partners-data | SHA: SIaoy8Xmtwe2+g1cl6OXYZnY5OfDRzR19n58dOKyZKk= |
| 6 | git commit (source map) | da59aa38 ci: upload opal-partners-data artifact [skip ci] |
| 7 | terraform plan | 1 change: s3_object_version + source_code_hash |
| 8 | terraform apply | Apply complete: 0 added, 1 changed, 0 destroyed |
| 9 | 0-diff plan | No changes. Infrastructure is up-to-date. |
| 10 | record-terraform-deploy.sh | a8c25841 (CHANGELOG.json parse error non-critical, source map OK) |
| 11 | git tag | partners-api-v1.15.5 |
| 12 | git push --follow-tags | CLOUD: d08746df..a8c25841 + tag pushed |

## Deployment Tags

| Pipeline | Tag | Commit |
|---------|-----|--------|
| partners-api | partners-api-v1.15.5 | a8c25841 |

## Verification

Source hash before: `pTH3UMOAh//7IWRSFBA0Skag0ta9m+irPYM3N0kkf18=`
Source hash after:  `SIaoy8Xmtwe2+g1cl6OXYZnY5OfDRzR19n58dOKyZKk=`
S3 version: `mMWuJwVJmlxrju8DQahFbWJULvDRyKeu`

CloudWatch verification: next warm L2/L3 Books invocation for same firm_id
should NOT show a DynamoDB get_item call for FIRM#{firm_id}/META.
(Requires live traffic to confirm cache hit path -- no test invoke run this session.)

## Infra Note

build-and-upload.sh bun path resolution: do NOT set TMPDIR="C:/Windows/Temp" when
bun is the JSON tool. Bun cannot load scripts via Windows-style C:/ paths.
Run without TMPDIR override -- bun resolves /tmp/ correctly via MSYS2 conversion.
MSYS_NO_PATHCONV=1 still required for terraform.exe calls (separate export).

## Current State

- partners-api-v1.15.5 live
- opal-partners-data: _bucket_cache active, warm L2/L3 hits skip DynamoDB

## Next Steps

- CloudWatch confirm: first Books tab L2 load -> DynamoDB call present (cache miss). Second load same firm -> no DynamoDB call (cache hit).
- ADVI_49PUSH.016 (auth audit + book scoping): still pending, needs assessment.
- deployment_map.md TO: still pending -- background work.
