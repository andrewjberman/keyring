# Never-widen half, MDPF_SECHIST rounds 3-4 -- Positioning gold gains blank-over-gap, the money-market rule and the gap-record producer (SH-t-7 + SH-t-15)

**Author:** `2.0.0_SA_COO~H1` (dell1), 2026-10-09 ~16:0xZ. **For:** `1.0.0_SA_CTO~DELL1` (the CTO half); applier `0.7.0_AE_CloudOps~DELL1`.
**Status: COO half DRAFTED, NOT SIGNED.** Signed only AFTER SH-t-8 is taken at site Z and its first scheduled run carries a non-null
`TOT_RETURN_INDEX_GROSS_DVDS` for SALXX / FXFXX (cell SH-t-17); gold first would blank those two funds. No deploy before both halves.

## The act

The `etf-positioning-producer` Lambda's package is built from git AT A PIN (`infra/aws/lambda/etfs-pipeline/etf-positioning-producer/build_package.py`,
`--pin` required, deterministic zip, per-member sha256 manifest) and applied by `0.7.0_AE_CloudOps~DELL1` through Terraform (`safe-apply`,
never `update-function-code`). The pin is a box/dell1 commit carrying SH-t-7 (@e8d83d658a), SH-t-15 (@7478ba71ca) and the silver module
`data/etfs/scripts/silver/etf_history_gap_record.py` (SH-t-6, @f81aac3c45) -- the package member list must include that module, which the
builder does not list today (a package edit in this act). ONE IAM act rides it (disarm ruling @912e4704b0): `s3:PutObject` on
`arn:aws:s3:::opal-data-etfs/bloomberg/etfs/silver/history_gaps/*` for the producer's role, applied by dell1 (Step F) and reported after
the fact to `0.0.0_AB_MSTR~DELL1` by name and grant; the three IAM-parity conditions ride the order.

**Second family:** `infra/aws/lambda/cot-pipeline/cot-satellites-characteristics-producer/build_package.py` also vendors
`etf_positioning_gold.py`. It is NOT rebuilt by this act; its next build would carry the change, so its owner is told at the pair.

## What changes (read from the code at the pin)

1. `run()` builds the day's gap record (`produce_gap_record`: `load_partitions` -> `build_gap_record`), writes it with `write_record` to
   `record_address(as_of)` when publishing, and passes the same record to `compute_returns`. A build failure falls back to the old read;
   a write failure is logged `WRITE FAILED` and the run continues.
2. `compute_returns`: a window containing a listed day serves blank; a counted absent day the record could not date blanks every window
   wider than 1D; a security with no listed day reads exactly as today.
3. SALXX / FXFXX daily return comes from `TOT_RETURN_INDEX_GROSS_DVDS` (level / previous level - 1); no level -> blank.

## Both branches (per security)

- No listed gap, not a money-market fund: unchanged (pinned by the existing gold tests at the drain).
- Listed gap: the windows spanning it turn blank where they showed a compounded number -- the FWD-5 move.
- SALXX / FXFXX: windows from the level series; blank where the level is missing (why SH-t-8 must be live first).

## Writers counted

Served `platinum/etfs/positioning_data.json` per-security windows: N = 1 rule (`compute_returns`). The new key
`bloomberg/etfs/silver/history_gaps/as_of=<d>/gap_record.json`: N = 1 writer (this run).

## Blast radius

From the first run after the apply: `gold/{book,holding}/date=<asof>/` and `platinum/etfs/positioning_data.json` (windows blank over
listed gaps; money-market windows from the level), and one new object per as-of under `history_gaps/`. No historical partition rewritten.

## Rollback

Re-apply the previous package pin (the function's prior `CodeSha256`, read at the apply); delete the `history_gaps/as_of=<d>/` objects
written since (an S3 delete -- Andrew's confirmation per CLAUDE.md); re-run gold + publisher for the latest as-of. The IAM grant is
removed by reverting its Terraform.

## Acceptance (the first scheduled run after the apply)

The record object exists at `record_address(<as_of>)` with no `WRITE FAILED` line; a security with no gap reads as the day before; SALXX
and FXFXX show windows from the level series.

## AMENDED to PRD v0.3 (2.0.0_SA_COO~H1, 2026-10-09 ~16:3xZ)

- "What changes" item 3 and branch "SALXX / FXFXX" are replaced: the money-market daily return reads `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS`;
  a null day serves BLANK (never estimated, never the level); the next pull re-requests that day from the gap record, and the same day
  serves filled on the following run. Code: round 5 repair cell SH-t-19 (staged @ffd76f8b9d); the pin is a commit carrying it.
- The status line's sign condition (a non-null level, cell SH-t-17) is VOID; SH-t-17 is carried and void (@93f6c1d5a6). The half signs
  after SH-t-19 drains and SH-t-8 (as repaired) is taken at site Z.
- Acceptance adds the FWD-9 read (CTO msg 2791): a first-day null served blank on 2026-10-12, served filled on the 2026-10-13 run.

## R1 (round-4 analysis, msg 2828) -- the ONE IAM statement this pair carries

- Role `etf-positioning-producer-role` today grants PutObject on `gold/*` only (CVO measurement, REMEDIATION_v3 D1-W14-S1).
- Added, in the same deploy, through `safe-apply` by 0.7.0_AE_CloudOps~DELL1: ONE statement, `s3:PutObject` on
  `arn:aws:s3:::opal-data-etfs/bloomberg/etfs/silver/history_gaps/*` -- the prefix `lib/opal_naming.address("bloomberg", "etfs", "silver",
  "history_gaps", ...)` builds (read 2026-10-09: `s3://opal-data-etfs/bloomberg/etfs/silver/history_gaps/as_of=2026-10-12/gap_record.json`).
  No wildcard beyond that prefix.
- A plan showing ANY other IAM change is a STOP. Rollback: re-apply the prior policy (read at the apply). Reported after the fact to
  0.0.0_AB_MSTR~DELL1 by name and grant (Step F); the three IAM-parity conditions ride the order.
- Pin: a box/dell1 commit carrying SH-t-7, SH-t-15 and SH-t-19 (round 5, decomposition @e3b4308e1b); written here at SH-t-19's drain.
