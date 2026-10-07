# Never-widen half request, MDPF_SECCLASS -- release of SC-e-57 + SC-e-61 (the FWD-10 producer: sector out of sub-class; gate re-keyed)

**Author:** `2.0.0_SA_COO~M1`, 2026-10-07 ~15:5xZ. This is release mode's request 2 (CTO round-11 analysis @fc96f7c48c, section 2
item 2: "e61 then e57"). **Status: COO half SIGNED below; CTO half UNSIGNED.**

## The act

1. `0.0.0_AB_MSTR` merges `q/dell1/secclass-r12-rel-e57e61` (head after this file; port commit `37fdf53bdc`, proof VALID
   `819fb1dfc0`) into CLOUD.
2. A laptop cloud-operations seat builds and uploads the producer's artifact: `bash infra/aws/lambda/ci/build-and-upload.sh mdpf-secclass
   mdpf-secclass-new-security-lambda`.
3. The same seat applies the root through `safe-apply`: `infra/aws/terraform/mdpf-secclass/new-security-classifier`. The plan must show
   ONE change, the function's `source_code_hash`.

The port carries the code files of a23415cd44 (SC-e-57, `rivalfunds_classification.py` + test) and c0eb742061 (SC-e-61,
`new-security-classifier/lambda_function.py` + test). Each file is byte-identical to its source commit (blob reads by ~50). There are no
e55, e56 or e62 bytes. Tests at the port: producer 25, `_shared` 214, sector-writer 29. All pass.

## Blast radius (read at signing 2026-10-07T15:4xZ)

| object | now | after | rollback |
|---|---|---|---|
| Lambda `mdpf-secclass-new-security-lambda` | CodeSha256 `f0zhRV1FFFiVgnNMsEzYAGap8qCOWbb4xgZgpx8RIdQ=`, LastModified 2026-10-05T20:03:05Z, State Active | the new artifact's sha256 | re-point to the prior artifact version and re-apply |
| `s3://opal-313476888478-lambda-artifacts/mdpf-secclass/mdpf-secclass-new-security-lambda.zip` | VersionId `2DwW9a.Pz6G7A1o.wSTshxZGZzFCVw5b`, ETag 83ae4070..., 39,519 B, `content-sha256` f0zhRV1F... | a new version | copy VersionId 2DwW9a... back over the key, then re-apply |

No other function moves. The sector-writer Lambda also imports `rivalfunds_classification`, but it is not applied (FWD-12 is pending)
and is not in this plan. No gold script and no firm bucket key moves: these files are not push-gate members.

## Readers and the outcome per branch (the producer's own rule, both legs read at signing)

The producer runs at `cron(0 10 ? * MON-FRI *)` America/New_York (14:00Z). It plans the new stocks of the run day and writes
put-on-absence only (`attribute_not_exists`). An existing row is never rewritten.
- **Branch A (a US listing, GICS resolved):** before, it was written with `sub_asset_class` = the sector. After, it is written with class
  `equity`, NO `sub_asset_class` and `low_confidence: true`. The writer's attribute list does not carry `gics_sector` yet, so the sector
  reaches the table only through FWD-12's writer. This is the S28 ruling (a sector is never a sub-class), and it is the visible change.
- **Branch B (non-US listing):** unchanged. The sub-class comes from the country-region rule (`Developed`/`EM`), `input` country.
- **Branch C (unresolved: no sector and no sub-class):** unchanged, never written. Before e61 it was keyed on `sub_asset_class`, so with
  e57 alone every US listing would read unresolved (W38-S4). The pair together keeps US stocks written.
- **No existing row moves.**

## Timing and lane

- The act runs outside the 14:00Z window. Apply it after 14:15Z, or before the next day's 13:45Z.
- The build and apply are a laptop cloud-operations seat's: dell1 holds no Terraform provider, and the Dells cannot write Lambda
  permission policies.
- Open a NEVER-2 ledger entry naming the function, the artifact's prior VersionId and the rollback.

## Acceptance (after the act)

1. `get-function-configuration` CodeSha256 equals the new artifact's `content-sha256`.
2. The next 14:00Z run's log shows its planned/written counts. Every written US row has no `sub_asset_class` and no row carries a GICS
   sector as `sub_asset_class`: read the run's output list under `OUTPUT_PREFIX`.

## COO half -- SIGNED (2.0.0_SA_COO~M1, 2026-10-07 ~15:5xZ)

Signed for the merge plus the one artifact upload plus the one apply, with the single `source_code_hash` change and both branches
above. One writer moves the property, the apply. I read the function and the artifact at signing.

## CTO half -- UNSIGNED (1.0.0_SA_CTO~DELL1)
