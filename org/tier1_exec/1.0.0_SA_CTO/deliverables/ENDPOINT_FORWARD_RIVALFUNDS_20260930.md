# ENDPOINT (step 2, /endpoint --forward) -- rivalfunds (rival ETF holdings) -- `1.0.0_SA_CTO~Z`, 2026-09-30 ~04:2xZ

**Brief:** `docs/briefs/etf-holdings-research-20260929.md`, revision 2 (September 29 ~23:5x ET), 20,570 B, read to EOF.
**AMENDED ~04:4xZ to brief revision 3** (@2a1f275a78, CRO~Z msg 26910), on Andrew's reply to the nine outcomes: *"Yeah this is
pretty good but i have one idea that may be foundatinal ... We need to reverse engineer their actual trades ... a gold table for
each active etf that is effectively their trade schedule ... one really, really clear signal on competitive intelligence"*.
Outcomes amended in place, with ids unchanged because none had landed: FWD-1 (the thread leads with trades), FWD-5 (the trade
schedule is the foundation), FWD-6 and FWD-7 (built on the trade schedule). FWD-2, 3, 4, 8 and 9 are unchanged. The DONE WHEN
lines are still unconfirmed.
**Author:** 4.0.0_SA_CRO~Z (msg 26900). **Andrew's rulings:** `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/AMGT_RECONN_SOURCES_20260929/ANDREW_DIRECT.md`
(12,243 B, read to EOF), including the 14-item gap-pass rulings and *"S9 looks fine, add the registry row and send to CTO"*.

**STATUS: NOT YET LANDED IN A PRD.** No project code or PRD exists. This block goes, unchanged, into the L4 PRD under the section
titled `ENDPOINT (step 2, /endpoint --forward)`. **Andrew confirms the DONE WHEN lines** (his 2026-09-03 word: *"i will confirm
CTO's 'DONE WHEN' from their /endpoint --forward"*). Until he does, this is a proposal.

The outcome ids are permanent from the moment they land. A new outcome takes the next unused number. A retired outcome leaves its
number vacant, and nothing is ever renumbered.

---

```
  FWD-1  Andrew opens one rival fund's day on the live page, reads what it
         traded, and traces a trade back to what the fund itself published
         DONE WHEN  EXERCISED -- one live trace: Andrew opens the rival-funds
                    page on the Opal site, picks BASG, reads its most recent
                    trades first, and follows one trade back through the two
                    holdings reports it was inferred from to the fund's own
                    published files
         ACCEPT     every step Andrew takes shows real holdings the fund
                    published; the page he reads is the one kept for that day,
                    and the list of past days shows it; a step fed by made-up
                    or sample data fails the outcome
         SOURCE     brief O1 (the candidate thread); Part V H1-H7 (each hop
                    crossed once for BASG); ANDREW_DIRECT item 4 (/rivalfunds,
                    archive by day)

  FWD-2  Andrew sees how much real history each fund has, and never mistakes
         an old report for a fresh one
         DONE WHEN  EXERCISED -- Andrew reads, for each of the six funds, which
                    days carry a genuinely new report, which are weekly or
                    quarterly, which are gaps and which repeat an older report,
                    back up to two years or the fund's own start
         ACCEPT     for any fund and day Andrew can tell whether the holdings
                    were actually published that day or carried over from an
                    earlier report; a fund's start as an ETF is not blurred
                    with any earlier fund it came from
         SOURCE     brief O2, IV.2; ANDREW_DIRECT scope clarification ("as much
                    as we can up to that threshold ... weekly, fine")

  FWD-3  Fresh holdings arrive every trading morning with nobody downloading
         anything, and Bloomberg is used only when the fund's own site fails
         DONE WHEN  EXERCISED -- over several consecutive trading days, each
                    fund's holdings are collected from its own site each
                    morning; on a day a fund's site fails, Bloomberg fills it
                    if it carries that fund, and the page says plainly when it
                    cannot (GQGU)
         ACCEPT     Andrew does nothing by hand on an ordinary day; on any day
                    he can see which source supplied each fund, and a fund that
                    was covered from its own site shows that Bloomberg was not
                    asked
         SOURCE     brief O3, Part V H6; ANDREW_DIRECT items 9 and 12

  FWD-4  Andrew compares any fund against any other in one common format,
         without learning six different file layouts
         DONE WHEN  EXERCISED -- Andrew reads two funds that came from
                    different sources side by side in the one master format,
                    with each position's source and dates shown
         ACCEPT     every position a fund disclosed appears, including cash,
                    derivatives and anything that could not be identified; a
                    detail the fund published but the master format has no
                    place for yet is kept, not thrown away
         SOURCE     brief O4, Part III (cash and unidentified visible);
                    ANDREW_DIRECT item 14 and L1 direction point 1

  FWD-5  Andrew reads each rival fund's trade schedule: what the manager
         actually bought and sold, and when
         DONE WHEN  EXERCISED -- for each of the six funds Andrew reads its
                    trades (entries, adds, trims and exits) with the shares
                    traded, the window they happened in, an estimated price and
                    size, and how sure the inference is
         ACCEPT     a price move, a dividend, a change of identifier or the
                    fund simply growing or shrinking never shows up as a trade;
                    a trade too small to tell from noise is not shown as one;
                    where reports are days apart the trade is placed in that
                    wider window, never invented on a single day
         SOURCE     brief rev 3 O5 (the foundation); ANDREW_DIRECT "reverse
                    engineer their actual trades ... a gold table for each
                    active etf that is effectively their trade schedule";
                    trade floor 0.2% and dividends from Bloomberg (same file)

  FWD-6  Andrew sees where a manager's holdings and choices helped or hurt
         DONE WHEN  EXERCISED -- Andrew reads, for one fund and period, its
                    best and worst holdings by return and by contribution, and
                    how the trades in its trade schedule have done since,
                    including positions it has since sold
         ACCEPT     every ranking says what it ranks, over what window and out
                    of how many holdings; a holding with a missing price is
                    counted as missing, not quietly left out
         SOURCE     brief O6, Part III (rankings state their window and
                    denominator)

  FWD-7  Andrew uses the AI to form views about a manager's behaviour, and
         can later check those views against what the manager actually did
         DONE WHEN  EXERCISED -- one AI account of a fund's process, built
                    from its trade schedule, is saved, and a later account
                    grades it against trades inferred after it was written
         ACCEPT     every claim in the AI account points to the figures it came
                    from, separates what was seen from what is guessed, and
                    says what would prove it wrong; a later grading cannot
                    rewrite what the earlier account said
         SOURCE     brief rev 3 O7 (starting from the trade schedule), Part III
                    (the AI does not manufacture returns or intent; one clear
                    signal, not a data dump); ANDREW_DIRECT L1 direction point 3

  FWD-8  An Opal researcher can rebuild the research from the kept raw files
         and add a new fund without changing what anything means
         DONE WHEN  EXERCISED -- a rebuild from the kept raw files reproduces
                    the published figures for one day, and running the same
                    day again adds no duplicate positions
         ACCEPT     a researcher can show where every figure came from, and a
                    rerun never silently replaces an earlier day's record
         SOURCE     brief O8, Part V H2-H3 (backfill by replay)

  FWD-9  A day's page never publishes figures that failed their checks
         DONE WHEN  EXERCISED -- on a day where a check is made to fail on
                    purpose, the page either says what failed or is not
                    published, and it never shows the failed figures as normal
         ACCEPT     Andrew can never read a quietly wrong page; when something
                    is missing or failed, the page tells him what
         SOURCE     brief Part III ("nothing publishes past a failed
                    guardrail"); Part V H7; ANDREW_DIRECT item 10
```

---

## FOR THE PRD (carried, not outcomes)

- **Round 1 builds FWD-1's thread over BASG**, crossing H1-H7 once. Later rounds widen to all six funds and enrich FWD-2 to FWD-9.
  This follows spine v3.16-3.18 and the brief's own Part V.
- **Vendor use:**
  - OpenAI for the analyses is authorized by Andrew's word (ANDREW_DIRECT item 4).
  - Bloomberg for the backfill and enrichment rests on items 7 and 13, under R-21's scripted-only mechanism. The brief itself
    says "each pull remains subject to Andrew's per-use vendor word", so **the L4 PRD states which is in force**, and this seat
    reads it before any pull is cut.
- **LGIC:** the registry change has landed (brief IV.5, @d451070fb1). The PRD cites builder output for every address and name
  (CLAUDE.md rule 30).
- **Unresolved, carried to L4:**
  - the unattended-Excel validation for the Bloomberg leg (brief IV.3);
  - issuer publication times (item 12, several days of observation);
  - AWS reachability of the six sites (item 11, the first test).

- **One clear signal, not a data dump** (brief rev 3 Part III): the page leads with what each rival traded, and a table no reader
  or analysis consumes is not built. This is a PRD constraint on the table set, not an outcome.
- **Dividends** come from Bloomberg's per-holding dividend calendar, an enrichment input under the vendor question above.

## PROVENANCE

**GROUNDED ON:**
- the brief, revision 2 (read to EOF, 20,570 B);
- `ANDREW_DIRECT.md` (read to EOF, 12,243 B);
- the endpoint skill, Phase 0 (F1-F5).

**NOT READ:**
- `GOLD_TABLES_AND_PROMPTS.md` (37,095 B). It is the supporting specification, and it is L4 material: the PRD's contracts cite
  it. The endpoint is drawn from the brief's outcome territory, as Phase 0 requires.
- the task-order register and any project JSON. None exists, and Phase 0 must not read them.
- `DAILY_COVERAGE_CENSUS.md`, `BBG_EXCEL_ACCESS_VERIFIED.md`.
