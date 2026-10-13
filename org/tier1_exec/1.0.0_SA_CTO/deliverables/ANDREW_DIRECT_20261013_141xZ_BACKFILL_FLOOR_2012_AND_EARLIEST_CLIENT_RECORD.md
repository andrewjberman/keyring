# Andrew-direct, 2026-10-13 ~14:1xZ (10:1x am ET), at the `1.0.0_SA_CTO~DELL1` terminal

**Verbatim:**

> We don't need anything prior to the earliest record of a client in the system, which generally would be 2020, in the case of Cottonwood Backfill could be as early as 2012. I think it is important to note that any backfill is thereby cut at 2012.

**Context:** MDPF_SECHIST CARD-A Bloomberg client history (1,319 names, about 2.4M cells as filed; `2.0.0_SA_COO~Q1` msg 4873). This seat ruled per-security windows, with P1 living-client
names first.

**Recorded as law for EVERY backfill (any vendor, any project, any box):**
1. **The start of a security's backfill window is the EARLIEST CLIENT RECORD in the system** that holds it: the client's (or the firm's) first date on our plane, generally
   2020.
2. **A HARD FLOOR of 2012-01-01:** no backfill request reaches before 2012-01-01, whatever a record says. Cottonwood's backfill may reach as early as 2012, and never earlier.
3. **The window a request may ask for** is therefore `[max(earliest client record for that security, 2012-01-01), today]`, intersected with the dates the security was actually
   held (this seat's per-security ruling). A request that asks for earlier dates is refused at the queue, not trimmed silently.

**Who it reaches:** the dell1 backfill and history owners (MDPF_DEMQUE `~Q1`, MDPF_SECHIST `~H1`), and, by relay, every box's backfill work, ADVI_COTBKF above all (dell2).

-- recorded by 1.0.0_SA_CTO~DELL1

## ADDENDUM 1 (2026-10-13 ~14:1xZ) -- the same session, verbatim

> for many needs, like rivalfunds, we only need 365 days back from the point of the need.

**Recorded:** a backfill window is set by its NEED, never by "everything available".
- **Client-history needs** (holdings, performance, client reporting): `[max(earliest client record, 2012-01-01), today]`, as above.
- **Non-client needs** (rival funds, ETF positioning, research, any market-context series): **365 days back from the point of the need,** that is, from the date the need first
  requires the data, not from the earliest record.
- **The 2012-01-01 floor binds both.**
- **Every queue request DECLARES its need class and its window start.** A request that does not declare them, or asks beyond its class's window, is REFUSED at the queue.
  Current requests are re-priced on these windows before their next draw.

-- recorded by 1.0.0_SA_CTO~DELL1

## ADDENDUM 2 (2026-10-13 ~14:2xZ) -- the same session, verbatim, and this seat's rulings applying it

> This is why we need to actually go through each queue item in DEMQUE and qualify the rules, priority order, and backfill depth per item.

> because I do not see us needing even more than 2 weeks of BBG daily quota if done correctly here.

**Recorded:**
1. **Every MDPF_DEMQUE queue item is QUALIFIED, one by one, before its next draw** (19 request files at `2.0.0_SA_COO~Q1`'s scan). Each row states:
   - the request id and its owning project;
   - the CONSUMER: the served page or product that reads it, named, or "none found";
   - the need class (client history or non-client);
   - the window start and end, under this record;
   - the securities count and the fields;
   - the cells;
   - the priority rank, under Andrew's queue order (open call 7328: production, then current clients including onboarding, then ETF Positioning, then rival funds in
     slices, then research, then former clients);
   - the days of Bloomberg daily quota it takes;
   - a recommendation: keep, trim (to what) or drop (why).
   **The target, Andrew's: the whole qualified queue fits in about 2 WEEKS of Bloomberg daily quota.** A request that cannot fit is trimmed or dropped by its consumer's need,
   never by silent truncation.
2. **Andrew reads the table before the queue draws again on anything not already in flight.**
3. **In flight, `DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS`** (research, start 2021-10-01, 15,120 cells, about 75 pct drawn): it is NOT grandfathered beyond its class.
   - Rows already drawn are kept; nothing is deleted.
   - Only the remainder inside 365 days of its need date may be drawn.
   - Anything older is cancelled.
4. **`etf_daily_pull.py` depth backfill (MDPF_SECHIST, `~H1` msg 4888):** the law REACHES it. It is a non-client need, so its window is 365 days back from the need, not the
   earliest client record.
   - Its `DEPTH_START_DAYS = 372` exceeds 365 by 7, so it becomes 365, with the trading calendar resolving the first business day.
   - It declares its class at the queue.

-- recorded by 1.0.0_SA_CTO~DELL1
