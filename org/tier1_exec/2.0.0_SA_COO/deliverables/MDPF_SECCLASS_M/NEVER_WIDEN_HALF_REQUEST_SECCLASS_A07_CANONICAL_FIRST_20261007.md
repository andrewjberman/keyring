# Never-widen half request, MDPF_SECCLASS FWD-5 SC-e-42 -- a07 (the Advisor Intelligence classification dim) reads the canonical table first

**Author:** `0.9.0_WK_MDPF_SECCLASS~32` (worker, TO-SC-e42), 2026-10-07. **For:** `2.0.0_SA_COO~M1` to sign and send. **Status: UNSIGNED. Nothing is deployed, nothing is pushed.**
The candidate lives on branch `wk-MDPF_SECCLASS-32` at commit `88c7018366` (base `b55059ee33`). The edited file is in a shipped shared home
(`data/assets/scripts/gold/runners_49f/`), so the branch stays off every pushed range until both halves sign.

## The act

Upload the changed a07 from the candidate commit, by the issuer, through `.tools/safe-deploy.sh` (a shared repo home: the S3-membership guard applies) after both halves sign:

| repo path (at `88c7018366`) | S3 key |
|---|---|
| `data/assets/scripts/gold/runners_49f/a07_dim_asset_classification.py` | `s3://opal-data-49financial/_code/a07_dim_asset_classification.py` |

(`file_to_s3_target` and `second_targets_for` read at the worktree: bucket `opal-data-49financial`, key `_code/a07_dim_asset_classification.py`, label `advi`; no second target, no bundle member.)

What the file does after the upload: a07 scans `etf-classifications` at build time, in the same one sanctioned scan site as `bd-securities` (consistent read, a paginated scan of `ticker` and `asset_class`),
and takes each held key's class from the canonical row when one exists, resolved in this order: the bare ticker, then `CUSIP:<9>`, then `BBG:<ticker>:<exch>` (a07's population carries no exchange, so the BBG
form matches on the ticker part and is used only when every BBG row for it agrees). Only a key with no canonical row falls to the old-list maps; a key in neither stays on a07's existing regex / ticker-shape fallback.
Six classes only: a canonical row outside them is not honored (0 of 3,507 today). `--no-canonical` restores the old path. The dim's columns, the alias-key-expansion join surface and the vintage form are unchanged;
`classification_source` gains the labels `canonical-ticker`, `canonical-cusip`, `canonical-bbg`, `canonical-variant`.

**IAM (read at 2026-10-07):** a07 runs on the chain role `bd-exporter-ec2-role`. Its attached customer policy `bd-securities-access` allows `dynamodb:Scan, GetItem, PutItem, UpdateItem, BatchWriteItem` on BOTH `table/bd-securities`
and `table/etf-classifications`, so the new read needs no grant. Nothing in the act changes IAM.

Worker's proof: `python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py data/assets/scripts/gold/runners_49f/tests/test_a07_canonical_first.py` prints `PYTEST-OK ... 7 passed`;
the two existing a07 test files (vintage digest, provenance stamp) read 12 passed.

## Blast radius

**The candidate diff.** `git diff b55059ee33 88c7018366` = 4 files, 38,649 insertions, 13 deletions; the one shipped file is a07 (102 insertions, 13 deletions of the 115 changed lines). No table, trigger, IAM grant, Terraform file or other script changes.

**What the switch changes** (a local build of a07's own population: 49F dim_position 2026-10-06, Inflection positions_mv 2026-10-07, Cottonwood fact_holdings 2026-10-06; nothing uploaded; the held set is `inferred`, not the served mix bytes, which the firm
buckets deny this device -- row W25-S1). Denominator 4,136 distinct held keys, listed one by one in `A07_SWITCH_BEFORE_AFTER_20261007.json`:

| source of the class after the switch | keys |
|---|---|
| canonical (1,946 bare ticker, 396 `CUSIP:`, 4 `BBG:`) | 2,346 |
| old list (no canonical row, an old-list map hit) | 775 |
| neither (a07's regex / ticker-shape fallback 993, UNCLASSIFIED-LOUD 22) | 1,015 |

**164 of the 4,136 keys change class** (every changed key is a canonical-sourced key; no old-list key and no neither-key moves). Dollars are each firm's own market-value column summed over the changed keys on the dates above (signed; 49F `market_value_settled_unsettled`,
Inflection `current_value`, Cottonwood `Market Value`). These are the per-firm dollars the Advisor Intelligence mix would re-bucket on the next a07 run:

| class move | keys | 49financial $ | cottonwood $ | inflection $ |
|---|---|---|---|---|
| equity -> fixed_income | 118 | 4,702,859 | 4,773,956 | 2,885 |
| alternatives -> structured | 9 | 21,350,476 | 4,172,141 | 2,036,247 |
| alternatives -> commodities | 8 | 978,876 | 20,427,481 | 0 |
| equity -> alternatives | 7 | 229,650 | 103,330 | 896,331 |
| fixed_income -> equity | 6 | 2,902,706 | 3,140,032 | 0 |
| equity -> structured | 5 | 3,718,359 | 1,706,603 | 0 |
| alternatives -> equity | 5 | 1,143,287 | 267,155 | 15,262 |
| UNCLASSIFIED-LOUD -> equity | 4 | 638,371 | 0 | 0 |
| equity -> commodities | 2 | 1,400 | 0 | 3,935 |
| **all 164** | **164** | **35,665,983** | **34,590,699** | **2,954,660** |

The largest single keys: VXX alternatives -> structured (49F $20.65M, Cottonwood $1.98M, Inflection $2.04M); EVSM equity -> fixed_income (Cottonwood $10.25M); GLD alternatives -> commodities (Cottonwood $9.29M, 49F $0.31M); PHYS alternatives -> commodities
(Cottonwood $8.34M); CASH equity -> fixed_income (Cottonwood -$5.48M, 49F $0.01M); CEMIX fixed_income -> equity (Cottonwood $3.14M); PSLV, SPYI, JEPI, `CUSIP:06745PR94`, `CUSIP:89602HGC5`, AAETX follow. Each move is the canonical table's class for the key, read live (`issuer_check_sc_e42.py` re-reads every canonical key).

**What does not move.** Served bytes do not change at the upload: a07 is a build-time script, so the `dim_asset_classification` and `alias_key_expansion` partitions already served stay until the next scheduled chain run rebuilds them with the new code;
the d06 (49F) and d08 (COT) mix artifacts read the rebuilt dim after that. The classifier vintage digest does not cover the canonical substrate (row `MDPF_SECCLASS-W32-S3`): a canonical-only change would not move `_classifier_vintage`; the class changes above do show in the dim's own rows.

**Parity control, stated honestly.** `--parity-control` diffs the port against `lib/etf_classifier.py`, which since SC-t-1 (`206b90e359`) is a canonical-ticker-only reader, so with the switch OFF the control already reports 1,690 mismatches at the base
(row `MDPF_SECCLASS-W32-S1`); it was dead before this edit. With the switch ON it reports 1,282 unsanctioned mismatches (against the same lib) and 447 `canonical-*` deltas, whose key set contains all 164 changed keys and 283 more (keys whose before and after class agree; the lib answers UNCLASSIFIED-LOUD for all 283, 273 of them
resolved by a `CUSIP:` row the ticker-only lib never reads): the parity's changed set does NOT equal the before/after's; before/after is a strict subset (0 keys only in before/after, 283 only in parity). The face's equality could not be met; a07's
parity code was kept (never removed or loosened to a pass), with the switch's `canonical-*` deltas printed in full beside it.

## Rollback per key

Rollback per key: one key, `s3://opal-data-49financial/_code/a07_dim_asset_classification.py`. Restore it by copying its previous `VersionId` back over the key, then re-run a07 for the affected date so the served dim partition is rebuilt on the old path.
**The live VersionId was NOT read:** `head-object` answers 403 and `list-object-versions` answers `AccessDenied` (`s3:ListBucketVersions`) to this device's agent identity `cloudops-dell1-agent-user` on `opal-data-49financial` (row `MDPF_SECCLASS-W32-S4`). The deploying
seat reads it with `aws s3api list-object-versions --bucket opal-data-49financial --prefix _code/a07_dim_asset_classification.py` BEFORE the upload and writes the IsLatest VersionId into its ledger entry; the act does not proceed on an unread rollback key. The last ETag
on record (VINTAGEDIGEST proof) is history, not the live read. Code-level rollback: `git revert 88c7018366` on the merge.

## Both halves UNSIGNED

**COO half (`2.0.0_SA_COO~M1`):** UNSIGNED. Reads: the act (one key, safe-deploy, after the CTO half); the blast radius (164 keys, $35.67M 49F / $34.59M Cottonwood / $2.95M Inflection re-bucketed on the next a07 run, inferred held set);
the rollback key's VersionId read by the deploying seat before the act; the parity set difference above.
**CTO half (`1.0.0_SA_CTO`):** UNSIGNED. Reads: that SC-e-42 is the a07 row of FWD-5; that the stale parity control and the vintage gap are rows, not blockers of this switch.
**Conditions to propose:** (1) a change-management ledger entry opens before the upload and names the one key and its VersionId; (2) the upload runs under `.tools/safe-deploy.sh`, never a bare copy; (3) branch `wk-MDPF_SECCLASS-32`'s code commit reaches a pushed
range only after both halves sign; (4) the first chain run after the upload is read for the dim's `A5-A07-SOURCE-CENSUS` line (canonical-* labels present) and the d06/d08 mix totals still sum to the firm's value.
