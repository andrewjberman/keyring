# Card for Andrew -- MDPF_SECHIST: price history for Cottonwood client securities (two vendor pulls, sized)

**From:** `2.0.0_SA_COO~H1` (dell1), 2026-10-07 ~13:1xZ. **Carrier:** `0.0.0_AB_MSTR~DELL1`. **CTO ruling:** `1.0.0_SA_CTO~DELL1` msg 262.

## The two decisions

**A. Bloomberg, at site Z, paced inside the shared budget: 1,319 securities, 2,317,534 security-days.**
Run at site Z's terminal only, drawing on the one Bloomberg budget ledger (120,000 backfill rows a day after the 30,000 production reserve),
yielding to production. About 20 days if it had the whole backfill budget; longer while other backfills share it. **REC: yes.**

**B. Yahoo, a NEW vendor source: 3,226 securities, 5,773,776 security-days.**
Equities, ETFs, mutual funds, closed-end funds and unit trusts. Not admitted by the PRD today (contract C-PULL names Bloomberg at site Z only).
A yes here is followed by the CTO's PRD addendum before any task order names it. **REC: yes, once, scoped to this list** -- Bloomberg alone
would take months at the budget and the estate already holds Yahoo-sourced prices (bd `silver/historical_prices.parquet`). The addendum must say
which Yahoo field stands in for a total return.

## What the numbers are

- Source: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~27/PRICE_NEED_FOR_SECHIST.csv` @50a35d3ada (ADVI_COTBKF, read only,
  nothing fetched). Universe: every Cottonwood security from its first trade date to 2026-06-23; the window is an upper bound.
- 4,545 securities with any uncovered day; 8,091,310 security-days. 2,914 have no price anywhere; they are listed, never estimated.
- Earliest needed date 2013-04-03 (none before 2010, inside the corrected trading calendar).
- Where: round 2 of MDPF_SECHIST under FWD-2 ("a client's security shows performance for the whole time the client has held it").

## What nobody does without your word

No pull from either vendor, of any size. A yes on A alone starts the Bloomberg part; B waits for its own yes and the addendum.
