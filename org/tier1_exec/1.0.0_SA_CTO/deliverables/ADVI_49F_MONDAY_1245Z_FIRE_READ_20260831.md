# ADVI_49F Monday 12:45Z Scheduled Fire Read

**Author:** 1.0.0_SA_CTO  
**Date:** 2026-08-31  
**Scope:** ADVI_49F only; read-only evidence record. No trigger, re-run, hand invoke, remediation, deploy, apply, vendor egress, or backfill.

## Source Read

The scheduled chain log for the Monday fire exists at:

`s3://opal-data-49financial/gold/advi/_logs/chain_20260831T124542Z.log`

S3 listing read:

- LastModified: `2026-08-31T12:47:39Z`
- Size: `11,869`
- ETag: `73703360fa7830ed998db3f80835dd96`

The log itself reports:

- `CHAIN START date=2026-08-28 mode=production workdir=/tmp/49f_chain_work stages=17`
- `map resolution: chose date=2026-08-28 of 47 partition(s); SKIPPED header-only: 2026-08-30, 2026-08-29`
- `map date=2026-08-28: 7,359 rows | fact_acc universe 7,371 (date=2026-08-28) | map_carried=False`
- `STAGE OK a06_identity_crosswalk rc=0 wall=1.4s`
- `STAGE OK a07_asset_class_pair rc=0 wall=3.4s`
- `STAGE OK a07_upload files=4 -> s3://opal-data-49financial/gold/advi/dimensions/ (dim_asset_classification, alias_key_expansion date=2026-08-28 + _manifests)`
- `CHAIN OK date=2026-08-28 wall=114.3s`

## a06 Pre-Registration Comparison

The actual a06 line matches the pre-registered expectation from `org/projects/ADVI_49F.json`:

- expected: `chose date=2026-08-28 of 47; SKIPPED header-only: 2026-08-30, 2026-08-29`
- actual: `chose date=2026-08-28 of 47 partition(s); SKIPPED header-only: 2026-08-30, 2026-08-29`
- expected: `map_carried=False`
- actual: `map_carried=False`

This is the first scheduled Monday exercise of the `@fec349cf79` a06 fix. CTO records the source-corroborated match; final acceptance grading/closure remains with `0.4.0_DS_ClientPlatform~W` and the normal CVO path.

## Premise Check

The allocation map source is the SmartX silver prefix, not the ADVI gold bucket:

`s3://opal-data-assets/smartx/platform/silver/fact_allocation_account_map/`

S3 source read:

| date | LastModified | size | ETag |
|---|---:|---:|---|
| `2026-08-28` | `2026-08-28T13:16:20Z` | `779,487` | `4e403d9a89d84c5737cbd42c98b9080a` |
| `2026-08-29` | `2026-08-29T13:17:42Z` | `4,507` | `645eb603876f204278a8db3abfa1b30d` |
| `2026-08-30` | `2026-08-30T13:17:40Z` | `4,507` | `645eb603876f204278a8db3abfa1b30d` |
| `2026-08-31` | `2026-08-31T13:18:11Z` | `779,765` | `664f86c550a47c71e4423700e71ebf21` |

The named assumption behind the pre-registration is therefore measured: no populated `2026-08-31` allocation-map partition existed before the 12:45Z fire; it landed at `13:18:11Z`. The two weekend partitions present at the time were the expected header-only `4,507` B objects.

## A7-4 Evidence Read

A7STAMP deploy ledger:

`org/critical_paths/change_management/20260830T1400Z_a07stamp-provenance-one-writer-deploy.md`

The ledger is `CLOSED`, opened `2026-08-30T14:00:57Z`, closed `2026-08-30T14:07Z`, and records served/index ETag matches for:

- `_code/a00_dim_account.py`: `8bd74df6cc6f17ac6ff1c3863f346171`
- `_code/a07_dim_asset_classification.py`: `84c020767842c44c347a149505dfaed8`
- `_code/tests/test_a07_provenance_stamp.py`: `0b370e3912007b1869aad786a5fa3cda`

The later VINTAGEDIGEST commit `1befd43cef` is a descendant of A7STAMP commit `cfc15ce384`; therefore the Monday fire's later served a07 bytes include the A7STAMP behavior.

S3 object versions for `_code/a07_dim_asset_classification.py` show the version in force at the Monday 12:45Z fire:

- `2026-08-30T14:42:52Z`, ETag `e0bde0a5394b7ab83d1797431327c33e`, VersionId `uvgoGGvDyh6MSWfkPgfsN5gLpb2lh2lQ`
- next version is not until `2026-08-31T17:53:25Z` and has the same ETag, so the 12:45Z fire ran the `e0bde0a5...` a07 bytes.

Output objects from the Monday fire:

| object | LastModified | size | ETag | rows |
|---|---:|---:|---|---:|
| `gold/advi/dimensions/dim_asset_classification/date=2026-08-28/data.parquet` | `2026-08-31T12:47:15Z` | `130,748` | `df2b6d90813d5655bb10b7adc5dcbaa4` | `3,864` |
| `gold/advi/dimensions/alias_key_expansion/date=2026-08-28/data.parquet` | `2026-08-31T12:47:15Z` | `106,994` | `6ef4319c42131e92a04b4eee4d2b63d5` | `4,165` |

Parquet value read from both objects:

- `_ingested_at`: only `2026-08-28`
- `source_pipeline`: only `49f-gold-runners`
- `_classifier_vintage`: only `48ec291d405a6b1b0e72b5ed4b311da26bc489296e7d09c536c4fd9b4931ef21`

This is positive source evidence for the A7-4 fire limb. CTO does not mark the cell closed here; that remains the W lane's acceptance/filing action.

## V-4 Disposition

VINTAGEDIGEST deploy ledger:

`org/critical_paths/change_management/20260830T1442Z_vintagedigest-canon-json-v1-deploy.md`

The ledger is `CLOSED`, opened `2026-08-30T14:42:52Z`, closed `2026-08-30T14:46Z`, and states the acceptance requirement as two consecutive fires with unchanged substrate: Monday `2026-08-31` and Tuesday `2026-09-01`, both at `12:45Z`.

Monday's fire carries the first V-4 arm:

- both row sets carry `_classifier_vintage = 48ec291d405a6b1b0e72b5ed4b311da26bc489296e7d09c536c4fd9b4931ef21`
- both row sets carry `_classifier_vintage_form = canon-json-v1`
- Monday manifests `20260831T124714Z__dim_asset_classification.json` and `20260831T124714Z__alias_key_expansion.json` carry the same vintage/form fields.

V-4 is not closable on Monday alone. The discriminating second arm is Tuesday `2026-09-01T12:45Z`, assuming unchanged substrate. A single fire can prove the field is present and well formed; it cannot prove cross-fire determinism.

## Boundary

This record is evidence for the project owner and CVO. It does not close A7-4, close V-4, amend `org/projects/ADVI_49F.json`, trigger production, or remediate anything.

## DS~W Artifact Grade Addendum

0.4.0_DS_ClientPlatform~W reported Msg-ID 89994 with its own artifact-grade read, deliverable `org/tier2_senior/0.4.0_DS_ClientPlatform~W/deliverables/ADVI_49F_MONDAY_1245Z_ACCEPTANCE_GRADE_20260831.md`, commit `bca8339816` local-only pending integration.

CTO records the grade:

- the fire ran scheduled, with exactly one `20260831` chain log among 567 logs and no hand-invoke sibling;
- a06 matched byte-for-byte with the pre-registration and 5 of 5 falsifiers did not fire;
- the premise held: the populated Monday allocation-map partition landed 32m29s after chain start, with the observed landing range now widened to 13:16-13:18Z for Tuesday registration;
- A7-4 is MET at `EXERCISED`, read on 3 of 3 trigger tables and 16,662 rows, with `_ingested_at == 2026-08-28`, `source_pipeline == 49f-gold-runners`, zero nulls, and zero off-values;
- V-4 has Monday arm 1 only and rides the Tuesday 2026-09-01 12:45Z scheduled fire, with substrate-change conditions pre-registered by DS~W.

CTO also accepts DS~W's instrument note against this file: the earlier ancestry statement (`1befd43cef` descends from `cfc15ce384`) supports commit lineage but is not a Rule 22a deployed-byte proof. The valid route is content plus controls: pull the served object versions by VersionId, reproduce their ETags from local bytes, diff `84c02076` to `e0bde0a5` to show only VINTAGEDIGEST changed, and use the pre-A7STAMP `152cf4ee` version as the negative control where the old clock/stage-string assignments are present. The conclusion stands; the proof route is corrected.
