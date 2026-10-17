# ENDPOINT (step 2, /endpoint --forward) -- ADVI_COTBOOKS: Cottonwood's advisor books on the Advisor Intelligence page (`1.0.0_SA_CTO~DELL1`, 2026-10-17 ~03:1xZ)

**Brief:** `docs/briefs/advi-portfolio-group-key-cottonwood-ai-brief-20261017.md` @1bae264b34 (`4.0.0_SA_CRO~DELL1`, 235 lines, measured
2026-10-17 01:5xZ to 02:1xZ).
**Orders:** Andrew-direct ~01:45Z (`org/tier1_exec/2.0.0_SA_COO~C1/ANDREW_DIRECT_20261017_0145Z_CRO_PORTFOLIO_GROUP_KEY_AND_COTTONWOOD_ADVISOR_INTELLIGENCE.md`):
"how they structure their 'Portfolio Group' key, because that's how we'll be able to run everybody's book properly ... should be taking on the
Inflection Shape visually"; and ~03:00Z (`.../ANDREW_DIRECT_20261017_0300Z_PORTFOLIO_GROUP_WORK_GO.md` @cdad0d5031): "yeah we do need to figure out
that portfolio group stuff".
**Standing order of work** (CTO msg 7116, C-1 of `ADVI_COTBKF/ledger/NEVER_WIDEN_R106_ACCOUNT_ATTRIBUTES_CTO_HALF.md`): the account-to-book rule
lands before any page reads the book.

```
  FWD-1  A Cottonwood admin opens Advisor Intelligence and sees the firm as its
         advisors' books, then opens one advisor and sees that advisor's clients
         DONE WHEN  EXERCISED -- one live trace on the real login, real data and real
                    services: the admin's first screen lists the advisors and an
                    unassigned group, and one click reaches one advisor's clients.
                    Every step is a real call; a step fed by sample data fails
         ACCEPT     A Cottonwood admin can say from the first screen which advisor
                    holds the most assets and the most clients, and can open any
                    advisor to see who that advisor's clients are, without scrolling
                    a list of every account in the firm
         SOURCE     brief Part I (candidate thread), O1, Part III admin test

  FWD-2  Every account in Cottonwood's supervised book belongs to exactly one
         advisor's book, chosen by a rule anyone can read
         DONE WHEN  EXERCISED -- read on the served book data for one dated pull:
                    no account sits in two books, none is lost, and an account Black
                    Diamond lists under more than one group shows the book the rule
                    picked and that it is shared
         ACCEPT     No supervised client is counted twice and none goes missing, and when an
                    account could belong to two advisors the page says which one it
                    shows and why, the same way every day
         SOURCE     brief O2, IV.2 item 1, Part III single-membership test

  FWD-3  Each advisor's book total matches what that advisor sees in Black Diamond
         DONE WHEN  EXERCISED -- for one dated pull, each advisor's total read on the
                    page beside Black Diamond's own figure for that advisor's group,
                    every difference named
         ACCEPT     An advisor looking at their book here does not have to say
                    "that's not my number" against Black Diamond, or the page says
                    plainly by how much and why it differs
         SOURCE     brief O3, IV.2 item 3, Part III advisor test

  FWD-4  An advisor who logs in sees their own book and no one else's
         DONE WHEN  EXERCISED -- one advisor login reaches its own book on the live
                    product, and a request for another advisor's book from that
                    login is refused
         ACCEPT     A Cottonwood advisor sees their own clients when they log in, and
                    cannot see a colleague's
         SOURCE     brief O4, IV.2 item 4

  FWD-5  The Cottonwood page reads like Inflection's
         DONE WHEN  EXERCISED -- the live page at a stated portal commit shows the
                    tabs Advisors, Distribution, Books and Profile in Inflection's
                    arrangement, and the first tab is not a list of every account
         ACCEPT     Someone who knows the Inflection page finds the Cottonwood page
                    laid out the same way, and the clutter of the first tab is gone
         SOURCE     brief O5, IV.3; Andrew ~01:45Z "should be taking on the
                    Inflection Shape visually"

  FWD-6  The books show today's assignments, not old ones
         DONE WHEN  EXERCISED -- a deliberate check on demand: the book an account
                    shows equals its group in the newest Black Diamond pull, and the
                    page names that pull's date
         ACCEPT     When Cottonwood moves a client to another advisor in Black
                    Diamond, the page shows the move with the next day's data, and
                    says which day its books are from
         SOURCE     brief IV.2 item 2, Part VI (the served dimension carries August
                    groups)
```

**NOT READ:** the task-order register and the ADVI_COTBKF orders (Phase 0 reads the brief only).

**Carried to the PRD, not outcomes:**
- Whether to add `Primary Portfolio Group` (dim 436) to Black Diamond template 270648 is a vendor-side pull change. Until Andrew words it, the rule
  in FWD-2 is the stated fallback: a named advisor beats "No Advisor", and the one three-group account is named. File order is never the rule.
- The Cottonwood user roster for FWD-4 is a new input, and its source is the PRD's to name. Nobody contacts Cottonwood.

-- 1.0.0_SA_CTO~DELL1
