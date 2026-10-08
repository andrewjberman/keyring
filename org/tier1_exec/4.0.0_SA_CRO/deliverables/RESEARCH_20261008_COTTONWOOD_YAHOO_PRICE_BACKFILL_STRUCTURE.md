# RESEARCH -- the Cottonwood Yahoo price-backfill structure: resolution, unmappables, corporate actions, schedule, unresolved index, ranking

**archetype:** EXPLORE
**Author:** 4.0.0_SA_CRO~DELL2, 2026-10-08
**Ask:** 2.0.0_SA_COO~C2 msg 1454; Andrew-direct ~19:1xZ, record
`org/tier1_exec/2.0.0_SA_COO~C2/deliverables/ANDREW_DIRECT_20261008_191xZ_DELL_YAHOO_EGRESS_AND_PRICE_BACKFILL_STRUCTURE_TO_CRO.md` @489e1cd24c.
**Scope:** the YAHOO share of the Cottonwood price-need file
(`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~27/PRICE_NEED_FOR_SECHIST.csv`): 3,226 securities,
5,773,776 security-days (upper bound). Not decided here: who builds it (the record leaves that open; MDPF_SECHIST's C-SERIES
is where the prices land).

## 0. Four measurements that shape the design (read 2026-10-08, this seat)

Source: the bronze ClientDelivery transactions file (1,416,494 records parsed), joined to the need file and to the silver
crosswalk (`commonwealth/cottonwood/silver/crosswalk/date=2026-06-23/`, 1,533 accounts).

| # | measurement | value | why it matters |
|---|---|---|---|
| M1 | Yahoo-need securities carrying a `Symbol` in Commonwealth's own rows | 3,101 of 3,226 (125 with none; 0 with two different symbols) | most tickers come from the delivery itself; Yahoo search is needed for only about 4% |
| M2 | Commonwealth trade prices available to check against (`by`/`sl`/`dvr` rows with quantity and amount) | 481,060 observations; median 4 per security; 148 securities with none | a mapping can be **proved** against prices the client actually traded at, not trusted by symbol |
| M3 | Days actually held vs the need file's upper bound | about 2.14M weekdays held (first to last transaction per account, to 2026-06-23 if still held; inferred) vs 5.77M | the real gap is about 37% of the stated need; measure coverage against held periods |
| M4 | Securities by whether any holder is still a Cottonwood client (crosswalk) | P1 living client 1,714 (2.64M upper-bound days); P2 match still open 64; P3 gone 1,448 (3.04M) | nearly half the need sits in Andrew's "not a priority" class |

**The schedule turns on a fifth fact:** Yahoo returns a security's whole daily history, with its splits and dividends, in ONE
request. The cost is per **security**, not per security-day. The Yahoo leg is about 3,300 requests in total, not millions.

## 1. Ticker resolution, and how a mapping is locked in

**Candidates, in this order:**
1. Commonwealth's own `Symbol` for the CUSIP (M1).
2. Opal's identity tables by CUSIP: the MDPF_SECCLASS key table, then Black Diamond's `ticker_resolution` (as rules, not as a
   read of another firm's bucket).
3. A Yahoo search on the security description, for the 125 with no symbol and for any candidate that fails step 4.
4. Mutual-fund share-class rules (five-letter tickers ending in X; the class in the description).

**Lock rule (the proof).** A candidate becomes LOCKED for a date range only when:
- Yahoo's **as-traded** close (see section 3) is within tolerance of Commonwealth's implied trade price `|Amount / Quantity|`
  on at least `min(3, available)` trade dates, AND at least one of those dates falls in the earliest third of the range;
- tolerance: 0.5% for mutual funds (NAV trades at NAV), 2% for listed equity, ETF and closed-end funds (intraday vs close);
- Yahoo's instrument type agrees with Commonwealth's `Asset_Type`.

**The lock record** (one row per CUSIP and date range, append-only; a change is a new row that names the row it supersedes):
`cusip, yahoo_symbol, valid_from, valid_to, method (C1-C4), observations_checked, observations_passed, median_abs_error,
locked_at, run_id, supersedes`.
Prices are pulled only for LOCKED rows. The lock is keyed by **date range**, not by CUSIP alone, because:
- a CUSIP can trade under different tickers over time (ticker changes);
- a ticker can name a different company today (recycled tickers). A recycled ticker fails the price check on the old dates, so
  the check guards against it on its own.

Securities with no trade prices (148, M2) cannot be proved this way. They may lock on method C1 or C2 alone, with
`observations_checked = 0`, so a consumer can refuse them (claim = held, not measured).

## 2. Securities that cannot be mapped

Every Yahoo-need security sits in exactly one state:

| state | meaning | next act |
|---|---|---|
| CANDIDATE | has a symbol, not yet checked | pull and check |
| LOCKED | proved for a date range | price pulled; any days outside the range go back to the index (section 5) |
| REJECTED:PRICE_MISMATCH | Yahoo's prices disagree with the trade prices | try the next candidate; after the last, UNRESOLVED |
| UNRESOLVED:NO_CANDIDATE | no symbol from any source | search once more by description at P1 only, else stop |
| UNRESOLVED:YAHOO_NO_DATA | Yahoo returns nothing (typically delisted or merged away; Yahoo drops much delisted history) | the fallback ladder |
| UNRESOLVED:PARTIAL_RANGE | Yahoo history starts after the held period | the fallback ladder for the uncovered period only |
| PARKED:LOW_PRIORITY | P3 and not resolved by step 1 or 2 | nothing; kept in the index |

**Fallback ladder for UNRESOLVED, P1 and P2 only:**
1. Bloomberg at site Z, inside `bbg_budget.py` behind the production reserve (it can price delisted CUSIPs Yahoo cannot).
2. Commonwealth's own trade prices as a sparse series: priced on trade dates only, blank between (C-GAP, no interpolation),
   with claim `inferred`.
3. UNPRICED, kept in the index with its reason.

## 3. Corporate actions, including retroactive ones

**Store prices as traded, never adjusted.** yfinance's `Close` is split-adjusted after the fact: a 2-for-1 split in 2024
halves every 2016 close. Pull with `auto_adjust=False, actions=True` and store four things apart: the close as served, the
split events, the dividend events, and the as-traded close derived from them (close times the product of the later split
ratios). Commonwealth's quantities are as traded, so only the as-traded price values them correctly.

**Thread Commonwealth's own events in.** The delivery carries its corporate actions: `lica`/`loca`/`licar` (contribution and
withdrawal on a corporate action), `QA` quantity adjustments, `acca`/`accal` cost adjustments, `CAF`, and `CA_Event_Id`.
- **Splits:** every Yahoo split on a held security should meet a Commonwealth quantity change on the same date in the
  accounts holding it. A split with no matching quantity change, or the reverse, raises a flag. This also proves the lock
  across the event.
- **Mergers and CUSIP changes:** a `loca` on the old CUSIP and a `lica` on a new CUSIP in the same account on the same date
  form a **succession edge**. The old CUSIP's range closes and the new one's opens on that date, each locked separately.
  This is how a merged-away security keeps its history up to the merger and stops at it.

**Retroactive changes.** Because the stored close is as served and the events are stored apart, a split Yahoo adds or
corrects later is applied by re-deriving the as-traded series. Nothing is re-pulled. Any new event on a security
re-runs its lock check for the affected range, so a lock that the new event breaks drops back to CANDIDATE. A periodic
pass (for example monthly, while the backfill is live) re-requests events only for LOCKED securities still held at the end
of the window (80 securities).

## 4. Call structure and a gentle schedule

**Requests:** one security per request (no multi-ticker download; one failure then costs one security). Each request asks for
the whole daily history with actions. Total: about 3,100 history requests, about 200 searches, plus retries and re-checks;
call it 4,000.

**Pacing (recommended, to be tuned on the first day's run):**
- one request every 8-12 seconds with random jitter, single-threaded, from one box;
- a daily cap of about 400 requests, run in one window each day (for example off US market hours);
- stop for the day at the first 401, 403 or 429 response, double the gap next day, and return to normal after a clean day;
- a checkpoint after every request (state per security, last attempt, outcome), so a stopped day resumes exactly.

**Duration:** about 10 sessions for the first pass, in P1 then P2 then P3 order, plus 2-4 sessions of retries and re-checks.
That is two to three weeks at a gentle pace, in line with Andrew's "multi-week" expectation; the cap could be raised if Yahoo
stays clean. P1 (1,714 securities) finishes in about the first five sessions.

The existing `data/black_diamond/scripts/silver/backfill_yahoo_prices_safe.py` already has the checkpoint and stop-on-429 pattern
(20 per batch, 5 s sleep). The build ladder says reuse its pattern, not a new fetcher; its batch size should drop to one.

## 5. Unresolved index, by time period

One row per **(CUSIP, held period)**, not per CUSIP, so a partial resolution leaves only the uncovered period open:
`cusip, period_start, period_end, accounts_affected, priority (P1/P2/P3), score, state (section 2), reason, next_act,
attempts, last_attempt, source_tried`.
Held periods come from the transactions: the union of each holding account's first to last transaction, extended to the end
of the window when the account still held the security (M3). Coverage is reported against these periods (about 2.14M days),
not against the 5.77M upper bound. Reported as a denominator: periods covered / periods open / periods parked, by priority.

## 6. Importance ranking

**Tier (from the crosswalk, M4):**
- **P1, living client** -- at least one holding account is MATCHED to a current Cottonwood account. 1,714 securities.
- **P2, match open** -- no MATCHED holder, but a holder is AMBIGUOUS or AWAITING_PERSON. 64 securities.
- **P3, gone** -- every holder is NO_CURRENT_ACCOUNT_HOLDS_POSITIONS, CLOSED_BEFORE_CURRENT_HISTORY or NO_SECURITY_POSITIONS.
  1,448 securities. This is Andrew's example class: unresolvable and held only by a client who no longer exists is not pursued.

**Within a tier, a score:** held days times the number of accounts, weighted by the largest single purchase amount, so a large
long-held position outranks a tiny one-account lot.

**Gap to close before relying on P3:** the crosswalk matches by **account** (rule R2, in-kind transfer). Andrew's test is "by name
**or** account". A name match against the Black Diamond client set is not yet in the crosswalk (`AWAITING_PERSON` is the
closest state). Until it is, P3 may hold some living clients. Recommend P3 securities still get step-1 resolution (it costs
nothing beyond the request), and only the fallback ladder is withheld from them.

## 7. Recommendations

1. Adopt sections 1-6 as the structure. The lock-by-trade-price rule (section 1) is the core answer to "how it is locked in".
2. Build it as an addendum to the project that owns the pull (MDPF_SECHIST, C-PULL), not a second fetcher. The owner is the
   CTO's call.
3. Before the first session: run one 50-security P1 pilot to measure the real error rate, the tolerance band and Yahoo's
   response to the pacing.
4. Add a name match to the crosswalk (C-CROSSWALK) before P3 is treated as final.

Working files: session scratchpad only; no client data in this file (counts only).
