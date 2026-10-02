# IRPT_DASHBD round 2, workstream B -- the CTO's L10 analysis: FWD-1 is live; round 3 makes it current every day

**Author:** 1.0.0_SA_CTO, 2026-10-02 ~06:4xZ (self-drive laptop directives). **Input:** `2.0.0_SA_COO~P` msg 104095 and its drain-end
record `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/IRPT_DASHBD_ROUND2_B_DRAIN_END_20261002.md` @fde5518653. PRD v0.6
@aabc054e89. Issuer `2.0.0_SA_COO~P`. Previous analysis: `CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_1_B_20261002.md` and its ADDENDUM 1.

## 1. Accepted from the drain

Both cells are terminal. **FWD-1 is LIVE end to end**: `2.0.0_SA_COO~D`'s signed-in walk on portal DEV `39b7a0fc` (06:26Z-06:28Z)
fetched one covered account's series and manifest through the served route (3 GETs, HTTP 200) and the page showed the figure with
"Data through September 28th, 2026" beside it. The route's controls held (V1 and an unauthenticated GET answered 401 with no
invocation). The thread is live but NOT current: the series is as of 2026-09-28 and nothing refreshes it (row S13). Round 3 is that.

DB-b-6 named the 1,498.38 USD residual on 0027265115 as a net of four offsetting classes; the fee leg matches to the cent.

## 2. The enrichment list round 3 cuts (ONE issuance, `2.0.0_SA_COO~P`)

| # | item | risk | ruled |
|---|---|---|---|
| E1 | **DB-b-7, the adapter's scheduled fire.** `account_return_daily.py` packaged unedited as a scheduled function on the holdings-performance pattern: its own root, its own ledger, its own clock, Monday to Friday by the trading calendar (`lib/trading_calendar.py`). Its fire time is read from its inputs' own landing times, never guessed, and falls before the publisher's 08:15 ET. Every new name is `lib/opal_naming.name()` output (rule 30, a new pipeline). | WORLD | YES, first. Acceptance: one scheduled fire lands the next T-1 partition with no seat starting it. |
| E2 | **The publisher root with its 08:15 ET schedule**, re-planned at a tree that carries the policy-selector fix (row S263), its own packet. | WORLD | YES, after E1 is served. Acceptance: the next morning the page reads "Data through" the new T-1 date with no seat starting either run. |
| E3 | **Foreign tax paid to internal** (ADDENDUM 1 A4): FTP/FC/WD and FTR/FC/WD move from EXTERNAL to internal (tax) in `4.0.0_SA_CRO`'s classification file; the served 49F engine's read moves under its own packet with both halves; the adapter's own override retires in the same act. | SERVED | YES, one cell with the CRO. |
| -- | **Margin interest** (DB-b-6: Opal classes INTR less S1INA internal, Black Diamond external, +10,724.31 USD on one account) | -- | RULED, NO CHANGE: Opal is right. Interest paid from the account is a cost of the portfolio and belongs in its return, not a client withdrawal (C-METHOD's `F_t` is the net EXTERNAL flow). The difference to Black Diamond is a stated methodology difference; the tie-out record names it. Not a cell. |
| -- | Hygiene (S15 the route named in `routes.json` without the `api` root generating it; IRPT_BCKEND-S260 the `UNEXPECTED` code) | -- | At the drain or the next change to `entry.py`; not cells. |
| -- | Like-day tie-out windows (PRD v0.6 ruling 23) | -- | CARRIED: Andrew's per-use vendor word. FWD-8's tolerance stays his. |

Each build order carries at most three mechanical criteria.

## 3. Rows placed at this seat

- **S16** (the seating lint truncates worker serials): the same defect as site Z's ETFS_RIVALS-S7, fixed @453c6430ec (`SERIAL_RE`
  admits an underscore) and on origin since the 2026-10-01 push. Answered; the CVO confirms it at the compile.
- **W1-S5**: accepted as the issuer's (a net-aware sum if the check is reused).

## 4. Outcome read

| outcome | state after round 2 | round 3 moves it to |
|---|---|---|
| FWD-1 | LIVE end to end, as of 2026-09-28 | live and current every trading day, no seat starting it (E1 + E2) |
| FWD-8 | not graded on agreement; the residual explained | unchanged; like-day windows wait on Andrew's vendor word |

Acts only Andrew can do, for this project: the like-day vendor pull; the recursive delete of `wk-irpt-dashbd-1` and its merged branch.

-- 1.0.0_SA_CTO
