# ANDREW-DIRECT 2026-09-04 ~12:1xZ -- "Recs 1 and 2 approved" on 0.0.0_AB_MSTR~Z's /open-calls (4 cards)

**Channel:** typed directly at the `0.0.0_AB_MSTR~Z` terminal (site Z), answering the four-card
`/open-calls` queue put to him minutes earlier. **Recorded by:** `0.0.0_AB_MSTR~Z`.
**Broadcast same turn:** MCP to `1.0.0_SA_CTO~Z`, `0.0.3_BG_BBGTerminal`, `2.0.0_SA_COO~Z`.

## His words, verbatim and entire

> Recs 1 and 2 approved

**He answered TWO of four.** Cards 3 (a mechanical pre-push refusal) and 4 (whether
`0.0.3_BG_BBGTerminal` stays permitted under the Tier-2 write gate) were NOT answered and stay in
the queue. This record does not treat silence on them as anything.

## CARD 1 -- the perishable Bloomberg capture. AUTHORISED AND DONE.

**CALL:** *Run today's ETF + constituents Bloomberg pull now?*
**REC (approved):** *Yes, run both today.* The grounds put to him: `READ_HERE.md:155` already states
the constituents leg runs even when a sibling fails, precisely because "there is no backfill, every
uncaptured day is gone permanently"; this morning's `.cmd` skipped both legs on the premise that a
failed models pull means Bloomberg is unreachable, and that premise was false today -- Bloomberg was
up and answering, and the pull died on a spreadsheet.

**THIS IS THE VENDOR-CALL WORD.** CLAUDE.md reserves an external vendor API call to his explicit
per-use word, which is why it was a card rather than an act.

**EXECUTED IMMEDIATELY, both legs, under the scheduled run class:**

```
ETF_RUN_CLASS=scheduled  <PY_AWS> -u integrations/bloomberg/pipeline/etf_daily_pull.py        rc=0
ETF_RUN_CLASS=scheduled  <PY_AWS> -u integrations/bloomberg/pipeline/etf_constituents_pull.py rc=0
```

**VERIFIED ON THE SERVED ARTIFACT, not on the runner's rc** (CLAUDE.md: never trust a producer's
self-report or rc=0). `list-objects-v2` on `opal-data-etfs`:

| leg | objects | written | as-of prefix |
|---|---|---|---|
| ETF daily | **7** | 2026-09-04T13:01:32Z | `bbg/2026-09-03/` |
| constituents | **9** | 2026-09-04T13:02:17Z | `bbg/2026-09-03/constituents/` |

All sixteen non-zero. **NEGATIVE CONTROL:** a bogus prefix (`bbg/2026-09-99/`) returns no `Contents`
at all, so the listings are real rather than an artifact of a query that matches anything.

**All four funds served on the constituents leg** -- DIVZ, IDVZ, PFDE, PFOE -- with sector and geo
allocations provided, holdings filled from the issuer/pathfinder channel at 29/44/90/24 rows.
`leg 1b` refused on entitlement for all four, which `READ_HERE.md` section 4 documents as the
EXPECTED refusal (BQL is refused identically for all four tickers); it is not a fault of this run.

⛔ **THE AS-OF IS `2026-09-03`, NOT `2026-09-04`, AND THAT IS CORRECT.** The pipeline lands under
`prev_trading_day` per `lib/trading_calendar`. The capture that was perishable was TODAY'S RUN of a
current-day-only source, not a file named for today.

## CARD 2 -- the INT template. APPROVED AS "BOTH, SHEET FIRST".

**CALL:** *The INT template fix: sheet, loader, or both?*
**REC (approved):** *Both, sheet first.* On 2026-08-18 merge **SPHY 0.0281 + 0.0275 -> 0.0556** and
**SPYM 0.1010 + 0.0150 -> 0.1160**; that preserves the 1.0 weight invariant, while
`drop_duplicates` breaks it to 0.9575 -- so these are intentional split lots, not a paste error.
Then a `groupby`-sum before the pivot so a legitimate split lot never breaks a run again.

**WHAT IS AUTHORISED AND BY WHOM:**
- **The loader hardening is authorised and is routed to `1.0.0_SA_CTO~Z`** as the pipeline
  work-order owner. It is code and it is that lane's.
- **The sheet edit is NOT taken by this seat.** `YC Intermediate Term template.xlsx` lives in
  Andrew's OneDrive (OCIO Models / 49 Models). The approved rec named the values but not the hand;
  a wrong edit to a live model-weight template is high-consequence and this seat holds no lane
  there. **ASSUMPTION STATED RATHER THAN ASSUMED SILENTLY: the sheet edit is his or OCIO's.** One
  word redirects it if he wants this fabric to make it.
- `0.0.3_BG_BBGTerminal` fires the models re-pull itself the moment the sheet is clean; it said so
  and it holds that leg.

⚠ **NOT DISCHARGED BY THIS RECORD:** models data stays at `data_as_of 2026-09-02` until the
template is de-duplicated and the re-pull runs. The ETF/constituents capture above is a DIFFERENT
leg and does not move the models figure.

## Root cause, for the record, measured by `0.0.3_BG_BBGTerminal` and not inferred

The 09-04 07:00 run died at `model_holdings.pivot(...)` with `ValueError: Index contains duplicate
entries`. Two duplicate `(date, ticker)` rows on 2026-08-18 in the INT template, present in the raw
sheet BEFORE any ticker rename -- which killed the first hypothesis (the `$:CASH->ICSH` /
`SPLG->SPYM` override collapsing two tickers). The file's mtime is 2026-09-03 10:50:25 ET, about
3h40m AFTER the 09-03 run finished green, so the 09-04 run was the first to read it. Control: of
the seven sibling templates in that directory, INT is the only one modified on 09-03.

## Still in the queue

Cards **3** (mechanical pre-push refusal) and **4** (`0.0.3_BG_BBGTerminal` permitted or blocked
under the Tier-2 write gate). Neither is blocking. Also NOT-MINE and still at him via
`2.0.0_SA_COO~Z`: the `opalinvest.com` apex decision, and the SNS confirmation click without which
the login-abuse alarm reaches nobody.

`0.0.0_AB_MSTR~Z`
