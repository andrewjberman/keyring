# Never-widen half, MDPF_SECHIST round 6 -- Positioning gold carries the last vendor day for a closed-market security (SH-t-24, FWD-9)

**Author:** `2.0.0_SA_COO~H1` (dell1), 2026-10-14 ~13:4xZ. **For:** `1.0.0_SA_CTO~DELL1` (the CTO half); applier `0.7.0_AE_CloudOps~DELL1`.
**Status: COO half SIGNED at pin `87a0dcf14d` (the SH-t-24 drain merge on `box/dell1`; LOCAL, push state unread at signing).** No deploy before the CTO half.
Basis: CTO round-5 ADDENDUM 2 (`org/missions/D8/MDPF/MDPF_SECHIST/ledger/ROUND_ANALYSIS.round5.md` @d3206f14a8, msg 5564), which asked for this pair.

## The act

The `etf-positioning-producer` Lambda is re-packaged from git AT THE PIN (`infra/aws/lambda/etfs-pipeline/etf-positioning-producer/build_package.py --pin 87a0dcf14d`, deterministic zip,
per-member sha256 manifest) and applied by `0.7.0_AE_CloudOps~DELL1` through Terraform (`safe-apply`, never `update-function-code`), under a ledger entry opened first.
Live now: `CodeSha256 YEYdzIZd2KQp3NngjJ5anv8RfTcsB8MqG21yRvCKVhM=` (read 2026-10-14 13:41Z, LastModified 2026-10-09T20:08:21Z) -- the rollback target.

- **Members:** the same 14 as the 2026-10-09 deploy (the builder's `PACKAGE` already lists `etf_positioning_gold.py` and `etf_positioning_publisher.py`). Two member bytes change; no member is added or removed.
- **IAM:** NO change. A plan showing ANY IAM, schedule, env or layer change is a STOP.
- **Pre-apply gate:** the import smoke of the 2026-10-09 pair on the unzipped package: `import etf_positioning_gold, etf_history_gap_record; print(etf_history_gap_record.record_address('2026-10-12'))`, plus `etf_positioning_gold.frontier_returns` importable.
- **Second family, NOT rebuilt:** `cot-satellites-characteristics-producer` vendors an older `etf_positioning_gold.py` (09408b19e5, row MDPF_SECHIST-D1-S6); it does not carry this change. Its windows for a closed-market security stay blank there. Not widened by this act.

## What changes (read from the code at the pin)

1. `frontier_returns(tkr, as_of, hist, gap_record)`: a reading ON as_of (a NULL counts) returns `compute_returns` at as_of, frontier = as_of. No row on as_of: carry the last vendor day `f` only when `as_of - f` <= 4 calendar days AND the gap record carries the security with `absent_count` 0; windows anchored on `f`. Otherwise blank. `compute_returns` is byte-identical.
2. `build_tables`: each holding row gains the column `return_frontier` (the frontier date, or null). New gold partitions only; no historical partition is rewritten.
3. Publisher: a holding gets `returns_frontier` ONLY when its frontier differs from the book's `data_as_of`; a book gets `returns_frontier_holdings` ONLY when one of its holdings carried. Neither key is added to `HOLDING_KEYS` / `BOOK_KEYS`. With nothing carried, the served JSON is the same keys and values as today.

## Both branches (per security, per book as_of)

- **Reading on the book's as_of** (every ordinary day, every security with a session): unchanged. Measured: 339 of 339 (ticker, book as_of) pairs with a reading equal `compute_returns` (`R6_CHECKS/r6_closed_market_real.py`, AC2 of SH-t-24).
- **No vendor day, within 4 days, `absent_count` 0:** the windows are the frontier day's, labeled. Measured set at the book as_of 2026-10-12: SALXX (frontier 2026-10-09), KCDMY and UNVGY (2026-10-08); only SALXX is held in a served book.
- **No vendor day, beyond 4 days or `absent_count` > 0 or no gap-record entry:** blank, as today.
- **A NULL reading on as_of (C-MMF):** blank, unchanged (FXFXX at 2026-10-12: frontier 10-12, all windows None).

## Writers counted

Served `platinum/etfs/positioning_data.json` per-security windows: N = 1 rule (`frontier_returns` over `compute_returns`), one producer (`etf-positioning-producer`). The new holding column and the two served keys: N = 1 writer each (this producer). `gold/holding/date=<asof>/`: N = 1 writer (this producer).

## Dry run at the pin (ONE, read only; `R6_CHECKS/r6_pin_dryrun_diff.py 2026-10-13`)

New gold + publisher code at HEAD (which carries the pin) run with `publish=False` through a read-only S3 client, document built in memory, diffed key by key against the page served 2026-10-14T13:01:42Z (data_as_of 2026-10-13):

- 188 holdings compared; **2 changed**: `DIVZ/SALXX` and `IDVZ/SALXX` (books as_of 2026-10-12), each with all 8 windows `None` -> the 2026-10-09 values (1D 0.0389, WTD 0.0777, MTD 0.1166, 1M 0.326, QTD 0.1166, 1Q 0.8897, YTD 2.645, 1Y 3.5329) and a new `returns_frontier` "2026-10-09". 16 changed cells.
- The two books gain `returns_frontier_holdings` = `[{"ticker": "SALXX", "frontier": "2026-10-09"}]`. Nothing else differs, no key dropped, no holding added or removed.
- BLIND: the publish step (not executed), the gold parquet write (the new column, exercised at the first scheduled run), readers of `gold/holding/` other than this publisher (not censused here), and the portal rung below.

## Blast radius

From the first scheduled run after the apply: `platinum/etfs/positioning_data.json` (windows move ONLY for a holding whose market has no vendor day on its book's as_of; on the dry-run inputs, SALXX in DIVZ and IDVZ), and `gold/{book,holding}/date=<asof>/` (the new column). No historical partition is rewritten; no pull, schedule or IAM changes.

## Rollback

Re-apply the prior package (`CodeSha256 YEYdzIZd2KQp3NngjJ5anv8RfTcsB8MqG21yRvCKVhM=`, read at the apply); re-run gold + publisher for the latest as-of with the prior code (the served key returns to blank for SALXX on a closed-market book). The new gold column in already-written partitions is inert to the old publisher (it reads named columns). No S3 delete is needed.

## Acceptance (the first scheduled gold run after the apply)

- No `ImportError`; the run logs the book labels as before.
- On an ordinary as_of (all books on session days): the served document has the same keys and values as the day's dry run without the change (the dry-run diff on that as_of prints `changed_holdings=0`).
- On the next closed-market as_of for a held security (the bond-market holiday, Veterans Day 2026-11-11, is the next one; SALXX in the TrueShares books): the holding carries `returns_frontier` and the book `returns_frontier_holdings`.

## Open at the CTO half (one question)

The portal reads the served page through an allowlist adapter (`portal/src/pages/Positioning/shared/etfAdapter.ts`, `toCurrentHolding`) that drops keys it does not name. After this deploy the JSON carries the label and the page does not show it, so a carried Friday number would read as Monday's on a closed-market book until the adapter passes `returns_frontier` through (a portal rung, another seat's). **REC: deploy any time** (the served change is zero on session days and the next closed-market day with a held security is 2026-11-11), **and cut the adapter rung before 2026-11-11**; if the CTO wants the label on the page first, sequence the deploy after that rung.

## AMENDED 2026-10-14 ~19:1xZ (2.0.0_SA_COO~H1) -- the pin narrows to exactly the two members this half names

The applier's step-3 comparison (CloudOps ~SH1, msg 5734, evidence `org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.7.0_AE_CloudOps~SH1/evidence/frontier_member_comparison_20261014.txt`) found that a build at `87a0dcf14d` moves 8 members, not the 2 this half and the CTO half sign for: also `lib/opal_naming.py` (+841 lines between the pins), four `infra/logic/registry/*.json` files and `data/firm_registry.json`. The act is NOT widened. The pin is `11dc6a2161` on the scratch branch `pin/sechist-frontier-20261014`: the live pin `09b6a7d580` with `etf_positioning_gold.py` and `etf_positioning_publisher.py` taken byte-equal from `87a0dcf14d`. The two signed members' bytes are unchanged by this; the other 12 members stay byte-identical to the live package. The dry run above (HEAD code) is unaffected for the two members; its use of the newer naming library is not part of the act. The six other moved members ride the next ordinary rebuild of this Lambda, under its own pair.
