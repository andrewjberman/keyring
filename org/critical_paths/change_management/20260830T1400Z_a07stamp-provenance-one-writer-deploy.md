# Deploy-completion ledger: ADVI_49F.c02-A07STAMP -- the Atom-9 provenance pair gets ONE writer

**Status:** CLOSED
**Opened:** 2026-08-30T14:00:57Z (the push-gate deploy, first object write) | **Closed:** 2026-08-30T14:07Z (running-artifact read)
**Operator:** 0.4.0_DS_ClientPlatform~N | **Deploy executed by:** the pre-push deploy gate at the 14:00Z integration window (0.0.0_AB_MSTR)

**Authority:** cell `C02-g-10` of `ADVI_49F_DECOMP_AMENDMENT_c02_REEMISSION_20260830.md`, WIDENED to a00 by
`2.0.0_SA_COO` 87531 on `1.0.0_SA_CTO`'s rec 87523. A7-4 amended by the issuer at 87680: because the
14:00Z window's gate deploys this commit's files, **A7-4 is a READ of the served ETags plus this ledger on
that read, NOT a second upload.** Gate acceptance of A7-1..A7-3: 87732. Grader: 87746.

## Scope
Commit `cfc15ce384` (ON ORIGIN; `origin/CLOUD` @ `5850d0f9ee33e7aea62909507f0934b1aab2ae77`, ls-remote read
14:02Z, `merge-base --is-ancestor` YES with a passing positive control on `b6dad1f773`).

- `a07_dim_asset_classification.py` -- `:351-352` and `:499-500` -> `rc.stamp_provenance(...)`
- `a00_dim_account.py` -- `:353-354` -> `rc.stamp_provenance(...)`
- `tests/test_a07_provenance_stamp.py` -- new, 5 arms

## This is an intentional served-value change on TWO of three tables
`_ingested_at` stops being a wall clock and becomes the partition date; `source_pipeline` stops being the
stage string `canonical-dims/a07_dim_asset_classification` and becomes the pipeline identity
`49f-gold-runners` (`1.0.0_SA_CTO` 87446: one field, one intent, all 16 tables).

Measured before the bytes moved, paired pre-fix/post-fix runs at D=2026-08-28 into scratch roots:

| table | column denominator | movers |
|---|---|---|
| `dim_asset_classification` | 10 | 2 (`_ingested_at`, `source_pipeline`) |
| `alias_key_expansion` | 8 | 2 (the same two) |
| `dim_account` | 38 | **0** -- a00's hand-rolled values were already value-identical |

`content_hash` identical across pre / post / served on both a07 tables (`e9703f0a...`, `efd49051...`), so the
classified content did not move. **`_classifier_vintage` also moves, and is NOT this change** -- it is
non-deterministic per process (a DynamoDB string SET stringified into a digest); excluded by name by the
issuer at 87525 and cut as its own cell C02-g-13.

**CONSUMER CENSUS before the change: ZERO code readers of the stage-valued string.** Repo 15 hits / 135,504
files scanned (corpus=all; 71,560 ephemeral-floor, 4,161 binary, 15 unreadable excluded and printed), bands
TEST=1 + DOC=14, no CODE band. Portal swept as its own repo: 0 hits, positive control 13,332 occurrences
across 717 files.

## Identity read -- the evidence, under the index-blob rule (Rule 22a)

Deployed by CONTENT, never by filename. Served ETag vs the git blob at `cfc15ce384`:

| object (`s3://opal-data-49financial/_code/`) | served ETag | index blob md5 | size | LastModified | verdict |
|---|---|---|---|---|---|
| `a00_dim_account.py` | `8bd74df6cc6f17ac6ff1c3863f346171` | `8bd74df6cc6f17ac6ff1c3863f346171` | 21,721 B | 14:00:57Z | **MATCH** |
| `a07_dim_asset_classification.py` | `84c020767842c44c347a149505dfaed8` | `84c020767842c44c347a149505dfaed8` | 30,047 B | 14:01:02Z | **MATCH** |
| `tests/test_a07_provenance_stamp.py` | `0b370e3912007b1869aad786a5fa3cda` | `0b370e3912007b1869aad786a5fa3cda` | 7,477 B | 14:01:08Z | **MATCH** |

Denominator: 82 objects under `_code/`. Corroborated independently by `3.0.0_SA_CVO` at 14:0xZ (87746).

**⚠ THE CRLF LIMB, AND IT WAS NOT AUTOMATIC.** `a07_dim_asset_classification.py` is one of **9 of 82** tracked
runner `.py` files whose WORKING TREE is CRLF while its index is LF, and the pre-push deploy gate uploads
WORKTREE bytes. Shipping the worktree would have put `dcac63966a0c7c1eef18ba1d65d1cce2` (30,604 B, 557 CRs) on
a key whose established identity is the index blob -- the pre-fix object `152cf4ee65de9331a9d50ce5d589fa85` is
byte-equal to the pre-fix INDEX blob and not to that content rendered CRLF, which is how the convention was
established rather than assumed. `0.0.0_AB_MSTR` hand-normalised the 557 CRs before the push (87703). **The
normalisation was a manual act, so it is not a property this key can be assumed to keep on the next deploy.**

## Chain of custody -- the object read IS the object that runs
Verified at source, not inferred from the bucket name:
1. EventBridge Scheduler `advi-49f-gold-floor` -- **ENABLED**, `cron(45 12 * * ? *)` UTC
2. -> Lambda `advi-49f-gold-dispatch` (`{"run_class":"production"}`), `SSM_DOCUMENT_NAME=advi-49f-chain-dispatch`, `HOST_INSTANCE_ID=i-01003b035d2988dfb`
3. -> SSM document `advi-49f-chain-dispatch` v3, **Active**:
   `aws s3 sync s3://opal-data-49financial/_code/ /tmp/advi_49f_code/ --delete` then
   `python3 chain_49f_entrypoint.py --production`

`--delete` mirrors the prefix, so no stale local copy survives the sync. A same-named
`a00_dim_account.py` exists at `s3://opal-data-inf/code/gold/runners_inf/` (4,439 B, 08-12) -- a **different
pipeline's** file sharing a basename, not a second home for this one; a07 has zero objects there.

## Named fire (the acceptance, NOT this ledger)
**Monday 2026-08-31, 12:45Z.** Today is Sunday and today's fire already ran at 12:47Z, so Monday's is the
first fire these bytes can meet. Chain date from the calendar, not arithmetic:
`prev_trading_day(2026-08-31) = 2026-08-28` (control: `prev_trading_day(2026-09-01) = 2026-08-31`, so Monday
is itself a trading day). That fire's a07 outputs AND `dim_account` are to be read **from the S3 objects**,
carrying `_ingested_at == 2026-08-28` and `source_pipeline == 49f-gold-runners`.

The same fire carries the separately registered a06 map-vintage line (87710): two named skips
(`2026-08-30`, `2026-08-29`) to `2026-08-28`, `map_carried=False`.

## Rollback (stated BEFORE the fire)
`git revert cfc15ce384`, then the reverted bytes reach `_code/` by the same push-gate path (LF-normalised).
No data is moved or deleted -- three source files change, so reversal is a redeploy, not a restoration.
Already-served partitions are not rewritten by a revert; the boundary is the next fire either way.
**Trigger:** Monday's fire emitting `_ingested_at` as a clock, or `source_pipeline` not equal to
`49f-gold-runners`, on any of the three tables; or any a0* stage aborting where it did not abort on
2026-08-29.
