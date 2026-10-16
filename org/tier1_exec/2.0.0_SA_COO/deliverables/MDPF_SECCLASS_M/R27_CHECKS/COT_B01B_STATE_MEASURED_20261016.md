# Cottonwood B_01b: what is measured about whether it runs (2.0.0_SA_COO~M1, 2026-10-16 ~07:2xZ)

Claim words: `measured` = read this session; `held` = cited from a record. Purpose: correct one word in the E_18 ship pair record. The CTO half (@d245ef138e) reads the cottonwood `B_01b` as "deployed and fired on 2026-10-15"; the request said only that the cottonwood gold stage wrote outputs that day and that whether B_01b ran in it was NOT measured. This note measures what can be measured.

## Measured

- **Deployed:** `s3://opal-data-cot/code/gold/B_01b.classify_new_securities.py`, LastModified 2026-10-07T07:09:42Z, 13,737 bytes. It names `bd-securities` and writes it (`data/cot/scripts/gold/B_01b.classify_new_securities.py:43,256,331`).
- **In the deployed dispatch:** `s3://opal-data-cot/code/gold/gold_dispatch.sh` (LastModified 2026-06-11T13:22:54Z, 58,520 bytes) holds `CHAIN_CANONICAL="B_00 B_01 B_01b B_02 B_03 C_00 C_01 C_02 C_04"` (line 139), `CHAIN_HOLDINGS_SEED="B_01 B_01b"` (132), `GROUP_B="B_00 B_01 B_01b B_02 B_03"` (151).
- **The cottonwood gold stage ran:** outputs were written 2026-10-15 ~11:37-11:40Z (`gold/canonical/holdings/2026-10-14.parquet`, `gold/views/firm_composition.json`, `platinum/firm/*`), after the `cot-exporter` instance launched at 11:30:16Z; the rule `cot-silver-complete` targets `cot-bd-session-trigger`.
- **B_01b leaves a watermark when it completes:** its `CLASSIFY_WATERMARK` is `gold/manifests/classify_watermark.json` (`lib/s3_layout.py:260`). **In `opal-data-cot` there is NO object under `gold/manifests/` at all** (the listing is empty) and the head of the watermark key is 404. The BD tree's own watermark reads LastModified 2026-10-11T05:05:19Z.
- **Per-run logs:** `opal-data-cot/gold/logs/` holds one file, dated 2026-06-26.

## What it supports and what it does not

- Supports: the cottonwood `B_01b` is DEPLOYED and NAMED in the deployed canonical chain. Not shown: that it has ever COMPLETED a run into this bucket (no watermark, no log), nor which chain the 10-15 cottonwood run was (the `cot-exporter` path may run a different step list).
- Therefore "scheduled writer: 1" in the request is a bound, not a measurement: the cottonwood copy CAN write the old list on any run that reaches it. The round-28 item (take cot `B_01b` out of the cot canonical chain) stands either way; its first act is to read the `cot-exporter` run's step list, which this note did not.
- No old-list row is attributable to a tree: the table carries no firm field. Rows written on 2026-10-04 (36) and 2026-10-11 (42) at 05:05Z fit the BD tree's weekly pattern (its watermark moved 10-11 05:05:19Z), not the cottonwood run time (11:3xZ).
