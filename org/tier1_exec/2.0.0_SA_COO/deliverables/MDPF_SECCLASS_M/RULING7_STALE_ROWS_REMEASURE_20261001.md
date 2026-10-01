# MDPF_SECCLASS -- the six stale open rows, re-measured once each (round-6 ruling 7) and ruling 5's split

By `2.0.0_SA_COO~M`, 2026-10-01 07:4xZ, at CLOUD @cc7287f3d7, for `3.0.0_SA_CVO` to compile at its next slug
(`CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_6_20261001.md` @453c6430ec, rulings 5 and 7). A disposition below is this
seat's recommendation; the remediation rows stay the CVO's.

## Ruling 7 -- six rows

| row | measured today | recommended | owner and condition if it stays open |
|---|---|---|---|
| S1 (a third writer the PRD did not name) | The contract names it: `org/standards/MDPF_SECCLASS_CONTRACT.json` `fields.classified_by.definitions.constituents` cites `seed-etf-constituents.py` and its write condition; the PRD records the amendment (`MDPF_SECCLASS_PRD.md:271-272`, "C-FIELD and C-WRITER above are amended in place"; CTO ruling 103050) | CLOSE: remediated by the contract text | -- |
| S2 (the scheduled classification has no caller at two firms) | Callers of `etf_classification_scheduled` under `data/`: 2 of 3 firm trees -- `data/black_diamond/scripts/gold/E_18.detect_new_securities.py` and `data/cot/scripts/gold/E_18.detect_new_securities.py` (with `tests/test_e18_scheduled_caller.py`). Inflection has none. Neither E_18 has a scheduled trigger (row W10-S2). The Holdings refusal the row tied to it (IB-mr-251) is superseded by the narrowed release | STAYS OPEN, narrowed | `2.0.0_SA_COO~M`: the E_18 trigger cell (STATUS item 4) covers Black Diamond and Cottonwood; an Inflection caller is a new item behind it |
| W2-S3 (instrument_kind written to 10 of 167 constituent rows) | Live scan 07:42Z, 2,309 ticker rows: `instrument_kind` `single_security` 165, `fund` 138, absent 2,006 (classified_by scheduled 1,933, legacy 72, seed 1). The constituent rows now carry it (165). What is absent is the scheduled backfill's rows and 73 others | CLOSE as written: the 157 are filled. The 2,006 without a kind are a different population | The fill for scheduled rows waits on Andrew's open call (may a per-firm value fill an absent `instrument_kind` on an existing row; CTO 103218) |
| W3-S3 (a fourth classify site in D_04) | `D_04.client_portal_summary.py:2769-2780`: `build_advisor_positions` now calls `_classify_with_canonical`, and the comment reads "the ONE classify site for this file". Those bytes are the ones deployed today (ETag `ffcdc3620936e240a075e84cc9711273`) | CLOSE when BD_THREAD_R3 leg A1 passes: the served artifact `platinum/advisors/{id}/positions.json` has not been read | `2.0.0_SA_COO~M`, ledger `secclass-bd-thread-r3-m-20261001` |
| W5-S2 (`identifier_namespace` is also a wider field on the Investor Reporting wire contract) | Still two schemas, two value sets. One reader in the Investor Reporting tree now reads the TABLE's field: `ycharts/generate/comparison_catalogue.py` drops rows whose `identifier_namespace` is `CUSIP`, the table's own domain. No code reads both | CLOSE as an accepted shared name; no remedy is owed | -- |
| W6-S2 (the unconditional write grant on both tables) | Unchanged at HEAD: `infra/aws/terraform/shared-infra/main.tf:395-416` `aws_iam_policy.bd_securities_access` allows Scan, GetItem, PutItem, UpdateItem and BatchWriteItem on `bd-securities` and `etf-classifications`, attached to `bd-exporter-ec2-role` and `partners-lambda-role` | STAYS OPEN | `0.7.0_AE_CloudOps`, order TO-SC-e12 (`parked`); un-parks when an AE seat is live |

Denominator: 6 rows named by the ruling, 6 read; 4 recommended closed (one of them on a leg still open), 2 stay open
with an owner and a condition.

## Ruling 5 -- `.tools/test_safe_deploy.py`, row W10-S3

The same file was run twice in one harness (tool and test extracted with `git show` into a scratch folder):

| tool at | result | failing tests |
|---|---|---|
| `f136b6f559~1` (SC-e13's parent) | 7 failed, 7 passed | `test_pass_gold_deploy`, `test_fail_nodeploy`, `test_fail_partial`, `test_fail_sha_mismatch`, `test_serve_release_authorized_with_ack`, `test_author_enumeration_notice`, `test_no_regression_clean_deploy` |
| CLOUD HEAD | 7 failed, 7 passed | the same seven |

SC-e13 caused 0 of the 7. Four fail with `INDEX_MISSING` (the test's files sit outside the workspace, so they have no
index entry) and three with `TypeError: Strings must be encoded before hashing`. Both come from the change of
2026-08-30 (`3d9eb2931d`, the tool uploads the index blob and asserts its ETag); the test file was last changed on
2026-07-12 (`d7359a797e`). Nothing here is this seat's to fix under the ruling. Owner of the seven: the deploy
tool's owner lane (`0.7.0_AE_CloudOps`, dark); they un-park when an AE seat is live or the tool next changes.
