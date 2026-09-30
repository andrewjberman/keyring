# ENDPOINT (step 2, /endpoint --forward) -- the client reporting dashboard (backend + frontend, one project)

**Author:** 1.0.0_SA_CTO, 2026-09-30 ~14:0xZ. **Phase 0 of `/endpoint`, run on the CRO's two L1 briefs, which are one
product read from two sides and are cut here as ONE project with TWO workstreams** (Andrew: "two COOs at once, COO~P on
the backend and bucketing and COO~D on the frontend, so we could run this whole function in concert"). The IRPT lesson
this shape answers: fifteen frontend and eighteen backend rounds with no journey working end to end because no outcome
owned the seam. Here FWD-1 owns the seam.

**Briefs read (F1):**
- `docs/briefs/reporting-dashboard-backend-brief-20260930.md` @`0ee065b116`, 4,145 words (backend: gold shape, total
  return, serving).
- `docs/briefs/reporting-dashboard-frontend-brief-20260930.md` @`0ee065b116`, 2,457 words (frontend: the views).
- Andrew's words, verbatim, in `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260930_06xxZ_REPORTING_DASHBOARD_TWO_BRIEFS_SCOPE_ANSWERS.md`
  (six messages: the request, five scope answers, gold is the Opal shape, total return on a conservative GIPS
  methodology, the fee rail, the two-methodology question).

**Proposed registration (L3, the CTO's next act, not yet landed):** code `IRPT_DASHBD` under D9 / macro IRPT, laptop;
workstream B (backend, `2.0.0_SA_COO~P`) and workstream F (frontend, `2.0.0_SA_COO~D`), disjoint write surfaces from
the PRD's writer table. NOT YET LANDED anywhere but this file; the PRD carries this section verbatim at L4.

## Andrew's rulings the endpoint records (verbatim sources in the CRO record)

1. Net worth, held-away accounts and liabilities are OUT ("scratch it", "forget this view"). The activity summary
   does not toggle to net worth.
2. Account grain is what matters; household and client are aggregates of accounts.
3. 49 Financial first; Cottonwood's Black Diamond backfill arrives later, so the shape is firm-agnostic now.
4. Performance is TOTAL RETURN on a conservative GIPS methodology: external flows enter because they change the
   weighting, under rules that keep a flow from distorting the return; income on cash receipt; GROSS of advisory fees
   and labelled so; a fee rail designed now and left unused.
5. **This NARROWS the 2026-09-28 holdings-only ruling** ("cash movements should not matter at all"; IRPT_BCKEND PRD
   v0.19 "the only inputs are end-of-day asset holdings values"). For THIS project flows re-enter as a weighting input,
   never as an unguarded return term. IRPT_BCKEND's holdings-basis gold is unchanged by this and becomes the guard rail
   (FWD-8) rather than the headline. Recorded here so the L4 PRD and IRPT_BCKEND's next addendum both cite one source.
6. Gold is the one Opal shape and the adapter layer (annex 17c, `1fef5f680e`): bronze raw, silver typed in the source's
   shape, gold coalesced into one shape; firm-specific columns do not survive into gold.

## The outcomes

```
  FWD-1  An advisor opens one 49 Financial account on the live portal, sees its daily total-return
         history, picks any start and end date, and the answer is on screen in about two seconds,
         with nobody having run anything that day
         DONE WHEN  EXERCISED -- one live trace: custodian file -> silver -> the Opal-shape gold ->
                    the served series file -> the signed-in page -> the drawn curve and headline number
         ACCEPT     Andrew picks an account and two dates the next morning and sees the curve without
                    waiting; changing the dates makes the page wait on nothing; every hop is the real
                    thing (a hop fed by a fixture fails this outcome)
         SOURCE     backend brief O1 and Part VI; frontend brief F1 and Part VI; Andrew "49 Financial
                    should be the first", COO~P record "under 2 s"

  FWD-2  Any account of any firm the gold covers loads the same way, and nothing on the page or in
         the file says which firm's plumbing produced it
         DONE WHEN  EXERCISED -- an Inflection account and a Cottonwood account each shown on the same page
         ACCEPT     a reader cannot tell from the page or the file which firm the account came from;
                    where a firm lacks a piece of data the page says so in words, never with a
                    firm-specific layout
         SOURCE     backend brief O2, Part V.1-2; Andrew message 3 ("gold is the adapter layer")

  FWD-3  A person sees how each asset class performed over the window and how the mix moved
         between two dates, in Opal's canonical classes
         DONE WHEN  EXERCISED -- a real account's window read by a person
         ACCEPT     a person says in one sentence which class drove the window and how the mix moved,
                    without reading a table; the classes add up to the account; unclassified holdings
                    show as their own class and are never folded away
         SOURCE     backend O3, Part V.4; frontend F2, F3; Andrew "asset allocation relying on Opal
                    canonical ETF-Classifier asset classes"

  FWD-4  A person sees realized gain, unrealized change and income for a window, and an activity
         summary whose figures agree with the transactions for the same window
         DONE WHEN  EXERCISED -- summed by hand from the transactions list and matched
         ACCEPT     beginning value, contributions, withdrawals, gain split three ways, and ending value
                    are on one screen beside a chart of value against contributions, and a deposit
                    reads as a deposit, not as performance; an account whose custodian gives no lot
                    detail says so instead of showing zero
         SOURCE     backend O4, Part V.4; frontend F4, F5; Andrew "unrealized gain + realized gain
                    over the given period", "activity summary view"

  FWD-5  A person browses the transactions for any account and window, filters, sorts and exports them
         DONE WHEN  EXERCISED -- a real window browsed and exported
         ACCEPT     date, asset, action, type, symbol, units, price, amount and custodian are shown in
                    Opal's own words for the action and type, not the custodian's codes; a long window
                    scrolls without the page stalling
         SOURCE     backend O5; frontend F6; Andrew "we should be able to show transactions"

  FWD-6  At the deepest drawdown in the chosen window, a person sees the topics that were trending
         then, as a cloud they can read at a glance
         DONE WHEN  EXERCISED -- Andrew reads one
         ACCEPT     the topics around the trough are ones a person who lived that week recognises; the
                    view says plainly they are market-wide, not filtered to the portfolio; a drawdown
                    before the news history begins says there is no topic history, never an empty cloud
         SOURCE     backend O6, Part V.7; frontend F7; Andrew "wherever the biggest drawdown is should
                    absolutely have a snapshot of the topic cloud phrases", "a signature view"

  FWD-7  A household or a client is the same page over more accounts, built from the account grain
         DONE WHEN  EXERCISED -- one real household shown
         ACCEPT     an "all accounts" choice shows the household with no new concept on the page; its
                    figures follow the same rules as one account's; accounts with different histories
                    are shown honestly, not averaged into a longer one
         SOURCE     backend O7, Part V.6; frontend F9; Andrew "Account level is all that matters, I
                    don't mind aggregating for household/client level"

  FWD-8  A return figure a person can defend: total return, before advisory fees and labelled so,
         and a day the data cannot support says so instead of showing a plausible wrong number
         DONE WHEN  EXERCISED -- the 49 Financial figure tied out against Black Diamond's own return
         ACCEPT     for an account and window the two returns agree within a tolerance Andrew accepts
                    and every day they disagree carries a stated reason; a misdated or missing deposit
                    can never show up as a huge gain or a total loss; the old "time-weighted, net of
                    fees" label is gone everywhere the new figures show
         SOURCE     backend O8, Part V.3 (the guard against hyper-exaggeration), Part IV.4; frontend
                    F8, Part IV.7; Andrew messages 4-6 (conservative GIPS, gross of fees, "avoid flows
                    having hyperexaggerated effects")

  FWD-9  The reporting gold is one Opal shape for every firm, with a written contract per table and
         one adapter per firm, and the fee rail is reserved and unused
         DONE WHEN  APPLIED -- the tables, their contracts and the three adapters exist and agree
         ACCEPT     the same table from any two firms has the same columns and meanings; the only place
                    a firm's own codes appear is inside that firm's adapter; a fee field exists,
                    carries nothing, and no net-of-fee figure is produced anywhere
         SOURCE     backend Part V.1, V.2, V.5; Andrew message 3 and message 5 ("a rail for fees")

  FWD-10 A person can always tell what they are looking at: where the data starts, which days could
         not be measured, when a figure is a fallback, and how current the data is
         DONE WHEN  EXERCISED -- read from the screen alone
         ACCEPT     a partial-history account, a day that could not be measured, a fallback day and a
                    window before the news data starts are each explained on screen in a sentence;
                    no state is hidden inside an average
         SOURCE     backend Part V.1 (the coverage vocabulary), V.3; frontend F8, Part V.3
```

## Thread order and the seam

FWD-1 is the thread and round 1 decomposes over its hops: silver -> the first gold table with its contract ->
the served series and manifest files -> the page reading them -> the curve with custom bookends and the honest
label. Workstream B owns the hops up to the served file; workstream F owns the page; the seam (the file's fields the
page needs) is a named contract in the PRD with ONE writer (B) and the page as its only reader. Every later round
enriches: FWD-3, FWD-4, FWD-5, FWD-6, then FWD-2 (Inflection, then Cottonwood), then FWD-7, with FWD-8 and FWD-10
graded on every round's served figures and FWD-9 applied as each table lands.

## Carried into the PRD, not decided here (the CRO's Part VII, both briefs)

Day-count convention; the reconciliation tolerance and the large-flow share (proposed from the 49F data's own
distribution); flow-timing convention decided by the round-1 tie-out (start, end, midpoint); reuse of the retiring
flow engine's parity work or a rebuild inside the adapter; where the household union-find lands; registering the
`reporting` table family and its platinum publisher under the tenancy rules; the presets; the benchmark overlay's
round; whether the allocation-change view replaces the Holdings Allocation panel (AD-03); how a household aggregate
with uneven histories is indicated. None blocks round 1. No vendor call is in any outcome; a new Black Diamond or
Orion pull is Andrew's per-use word (CLAUDE.md, vendor egress).

## Provenance (F5)

READ: the two briefs at `0ee065b116`; the CRO's Andrew-direct record (six messages); annex 17c at `1fef5f680e`;
IRPT_BCKEND PRD v0.21 lines 38-42 (the holdings-only rule this endpoint narrows for its own project).
NOT READ, on purpose (Phase 0): the directives register, any task order, any project JSON, the portal tree, any
parquet or served object. The two-second figure is Andrew's target and COO~P's estimate, not a measurement.

-- 1.0.0_SA_CTO
