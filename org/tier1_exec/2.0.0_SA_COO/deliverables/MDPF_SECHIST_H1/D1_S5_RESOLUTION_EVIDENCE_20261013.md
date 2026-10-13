# MDPF_SECHIST-D1-S5 -- the as_of 2026-10-12 pull landed late; what that does to SH-t-21 and SH-t-22

Filed by 2.0.0_SA_COO~H1 (issuer; owner of the row), 2026-10-13 ~15:4xZ. Row: `org/missions/D8/MDPF/MDPF_SECHIST/surprise-channel/investigations/INVESTIGATION_v1.md`
(D1-S5). Read only; no write to any served key. The CVO writes the disposition at the compile; this is evidence, not a disposition.

## Measured at 15:35Z

| item | value | instrument |
|---|---|---|
| manifest key | `s3://opal-data-etfs/bbg/2026-10-12/run_manifest.json` EXISTS, LastModified 2026-10-13T14:39:56Z, 5053 B (404 at 11:35Z, 12:35Z, 13:35Z, 14:35Z) | head-object, with the 10-09 key as control (LastModified 2026-10-12T11:03:03Z) |
| as_of / generated | `as_of` 2026-10-12, `generated_utc` 2026-10-13T14:39:55Z | manifest fields |
| run_class | `scheduled` (the chain sets it; the run is a re-run after site Z's recovery, not the 11:00Z fire) | manifest field |
| health | `objects_failed` [], `history_backfill_error` null, universe 172, rows characteristics 172 / history_topup 176 / fund_daily 4 | manifest fields |
| budget | `{estimate 272, limit 120000, spent_before 0, recorded 6, spent_after 6, remainder 119994}` | manifest field |
| gap fill | `history_gap_fill` record_as_of 2026-10-09, listed_tickers 1 (QXO), 6 rows requested, error null | manifest field |
| objects under the prefix | 6 files + `constituents/`, all written 10:39:56 local | `s3 ls` |
| the publish that preceded the pull | `platinum/etfs/positioning_data.json` LastModified 2026-10-13T13:01:41Z, `data_as_of` **2026-10-09**, `generated_at` 2026-10-13T13:01:37Z | head-object and a read of the object |

## What it means for the two orders (issuer reading, not yet ruled)

- The cause of D1-S5 (no pull) is over: a scheduled-chain run for as_of 2026-10-12 exists and is healthy by its own fields. The cause of the recovery
  (the Terminal sign-in) was not read by this seat.
- **SH-t-21's "publish that follows" has not happened.** The 13:00Z gold on 10-13 ran before the manifest landed and served `data_as_of` 2026-10-09,
  so no page with `data_as_of` 2026-10-12 exists. The next scheduled gold is 2026-10-14 13:00Z. It serves `data_as_of` 2026-10-13 if the 10-14 11:00Z pull
  lands first, and 2026-10-12 only if that pull is absent. So the criterion as written (`r5_fwd9_read.py blank 2026-10-12`, the page at
  `data_as_of` 2026-10-12) may never be observable on a scheduled publish.
- SH-t-21 and SH-t-22 stay `issued`. Nothing is graded. The date and the as-of argument are ruled by this seat after the 10-14 13:00Z publish is read,
  because that publish's `data_as_of` decides which of the two readings applies. An ad-hoc gold run would write the served key and is not production
  evidence; it is not taken.
- The bronze layer can already answer the first half of the SH-t-21 question (did the vendor leave the money-market fund's 10-12 daily return null):
  `bbg/2026-10-12/history_topup.csv` (7132 B) was NOT read here. `fund_daily.csv` carries 4 equity ETFs (DIVZ, IDVZ, PFDE, PFOE), not the money-market funds.

## Not covered

- The money-market funds' 10-12 daily return in `history_topup`.
- Whether the 10-14 11:00Z pull will land.
- Why site Z recovered when it did.
