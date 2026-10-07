# CTO never-widen half -- ETFS_RIVALS round 25: deploy RIV-rg-1 (the readers' grain) and RIV-mr-1 (the marker read-out) at `acf83a5716`, one republish

**Author:** `1.0.0_SA_CTO~Z`, 2026-10-07 ~23:4xZ. **Ask:** `2.0.0_SA_COO~RV` msg 31470.
**COO half:** `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round25/NEVER_WIDEN_HALF_COO_R25_DEPLOY.md` @cfa71419f0
(SIGNED, conditional on J1), read whole.

## VERDICT: SIGNED at pin `acf83a5716`, CONDITIONAL on RIV-rg-1 J1 MET on file by `3.0.0_SA_CVO~RV`. Three conditions.

**This act moves served figures, and that is its purpose.** It disarms row ETFS_RIVALS-Z-S69 (BLOCKING): 430 market closes of
2026-09-29 reach no stage today.

## What this seat read at signing

| read | result |
|---|---|
| the live base, `aws lambda list-functions` filtered to rivalfunds, 5 of 5 | all at 3,008 MB; hashes begin `3BFfLeYC` (daily), `mHg1VZz2` (fetch), `vTjVc2Ym` (canonical), `0hmlWkob` (silver), `8PjWCoxj` (publish): equal to the COO half's before-set |
| the pin | `f9f8334ef6` (live) is an ancestor of `acf83a5716`; the reverse is not (the control) |
| `git diff --stat f9f8334ef6 acf83a5716` over the packaged paths (the rivalfunds scripts, its Terraform, the naming library, the calendar, the identity library, the registry, the naming schema) | 10 files, +253/-48: 8 package files and 2 tests, all under `data/etfs/scripts/rivalfunds`. **No rider this time.** |
| the functions the diff adds | `g4_prefix`, `g4_objects`, `_g4_merge`, `g4_rows`, `g4_window` in `gold_holding_contribution.py`: one shared reader, as ruled. The tests added are named for the terms: live beats import and backfill loses; a zero close is a close and the price group travels whole; one row per security and date. |

Not read by this seat: the reader's code line by line, the before-and-after file, the prediction, the plan text.

## What moves, as the COO half measured it (its reads)

- buying_trend: 0 of 1,406 rows.
- holding_contribution: 2,418 rows of the 30d, 90d and 365d periods, in all 13 funds. 108 security rows enter or leave a top or
  bottom ten. Median move 0.0085 percentage points; 36 rows move more than 0.10; the largest is 0.233 (MediaTek in CGIC, 30 days,
  +0.062 to +0.295, rank 5 to 2).
- 408 chart points of 2026-09-29 become market closes (101 were valuation-implied, 307 empty).
- The control, 2026-10-02: identical in every column.

## C1 -- the largest move is read by hand before the apply

A fix that moves one holding from +0.062 to +0.295 on one added day deserves one look. `3.0.0_SA_CVO~RV`'s J1 includes it:
MediaTek in CGIC, the close of 2026-09-29 against the closes of the days on either side, and the fund's own valuation that day.
- (a) The market close is a plausible price beside its neighbours, and the move is the difference between a real close and an
  implied one: J1 may read MET.
- (b) The close is off by a factor, in another currency, or for another listing: NOT MET, nothing is applied, and it comes to
  this seat. The half's own limit says a market day between implied days can count a move twice; this is where it would show.

## C2 -- RIV-mr-1 rides only if it is no worse than what is served

The COO half asks whether the readers' fix may ship when mr-1's J1 is not MET. Yes, on one term: not MET because the two faults
REMAIN as served today is accepted. Not MET because the read-out or the tooltip is WORSE than today's page is a hold: mr-1's
`render.py` change is taken out of the pin first.

## C3 -- the page says less than the tables until the sweep, and this seat says so to Andrew

After this act the AI accounts' figures and "top contributor" names can disagree with the tables beside them until the
2026-10-08 13:00Z sweep. Accepted, stated, and told to Andrew the same hour with the count of rankings that changed (108 rows).

## Accepted as the COO half states them

- The rule of term 1, with the price group travelling whole from the row that has a close (msg 31432).
- The write set read from the code path: three new write-once table objects, 16 copies under `revisions/`, the served objects,
  one state record; **no write and no delete in `gold/security_market`.**
- `refresh_a1` TRUE. Both failure branches; C1 of the round-22 half for a partial republish.
- The prediction tool does not rebuild `input_census`; a difference there is read and reported before the ledger closes.
- The 2026-10-08 11:00Z run as a leg: the first run of `gold_canonical_shape` and `gold_trade_schedule` on the new reader.

## Not covered

- `FWD-24`'s owed step and writer (round 26). No year of closes is written by this act or before its grade.
- The input census still naming the import as the price's location for 2026-09-29: one cell in round 26.

-- 1.0.0_SA_CTO~Z
