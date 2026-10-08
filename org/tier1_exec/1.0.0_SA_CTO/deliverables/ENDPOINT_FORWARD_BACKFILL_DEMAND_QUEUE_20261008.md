# ENDPOINT (step 2, /endpoint --forward) -- the market-data backfill demand queue

- **Author:** `1.0.0_SA_CTO~DELL1`, L2, 2026-10-08 ~20:3xZ.
- **Status: RATIFIED by Andrew ~22:4xZ ("1.) Yes."); the two readings settled below.** No project is registered yet. The block goes into the PRD under the
  section title `ENDPOINT (step 2, /endpoint --forward)` once it is registered (L3).
- **Proposed code:** `MDPF_DEMQUE` (macro MDPF, directive D8; no collision in `org/projects/`). Not registered.
- **Inputs (both briefs, both read in full):**
  - Organisation-wide L1 brief: `docs/briefs/bbg-backfill-demand-queue-brief-20261008.md` @91f5c90ec2 (`4.0.0_SA_CRO~Z`, 284 lines).
    Andrew's record: `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20261008_18xxZ_BACKFILL_DEMAND_QUEUE_PROJECT_BRIEF_TO_DELL1.md`
    @f81483f292.
  - Cottonwood research: `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261008_COTTONWOOD_YAHOO_PRICE_BACKFILL_STRUCTURE.md`
    @e112184d3b (`4.0.0_SA_CRO~DELL2`, 148 lines). Andrew's record:
    `org/tier1_exec/2.0.0_SA_COO~C2/deliverables/ANDREW_DIRECT_20261008_191xZ_DELL_YAHOO_EGRESS_AND_PRICE_BACKFILL_STRUCTURE_TO_CRO.md` @489e1cd24c.
  - Placement: `0.0.0_AB_MSTR~DELL1` record @cf7005c305 ("All of this needs to get wrapped up into a registered project which will be
    run on this device").
- **NOT READ:** the project register, any project JSON, any open task order, the evidence files the brief cites (its measured figures
  are the brief's, not re-derived here). Phase 0 reads the briefs only.

## Outcomes

```
FWD-1  A new Cottonwood client security gets its price history onto the client's page without anyone running a pull
       DONE WHEN  EXERCISED -- one real security, traced from arrival to the page
       ACCEPT     a named security a living Cottonwood client holds, with no history before, shows its daily prices on that client's
                  pages; those prices agree with the prices the client actually traded at; and no person ran a pull by hand
       SOURCE     site Z brief I.0 (the candidate thread); dell2 research s.1 (lock against trade prices), s.6 (living client first)

FWD-2  Anyone can see, in cells, what every daily job pulls, from which vendor, for which page
       DONE WHEN  EXERCISED -- a real day read back
       ACCEPT     for a chosen day, a person reads every recurring market-data pull on every box, how many cells (one row times one
                  field) it drew from each vendor, which page it fed, and which of the pulled fields no page uses; the day's figures
                  can be checked against what the jobs actually received
       SOURCE     site Z brief O1, O8; Andrew "counting off the basis of cells", "where that quota is going"

FWD-3  A backfill can never stop a production pull
       DONE WHEN  EXERCISED -- shown on purpose
       ACCEPT     a person can read, per vendor channel, today's fixed daily load, what backfills have used, and what is left above a
                  reserve kept for production; a backfill big enough to reach the reserve stops at it, and the next morning's
                  production pulls all run
       SOURCE     site Z brief O2, Part III (the 2026-10-05 block); Andrew "developing our reserves"

FWD-4  A request for history is priced and scheduled before it runs, including a new client's onboarding
       DONE WHEN  EXERCISED -- one real request
       ACCEPT     someone asks for history on a set of securities, fields and dates, and is told before anything runs what it costs
                  and the day it will finish; the same is shown for a new firm or large account before its onboarding starts; and
                  what the run then uses is close to what was quoted
       SOURCE     site Z brief O3, O9

FWD-5  Each security is identified once, and what cannot be identified is listed with its reason and the dates it covers
       DONE WHEN  EXERCISED -- one real run read
       ACCEPT     a security arriving from a custodian, a fund or a client file is matched to one identity before anything is pulled
                  for it, and every page asking for it uses that one identity; a security that cannot be matched, or is matched only
                  for part of the time it was held, appears on a list with its reason and the dates still open
       SOURCE     site Z brief O4; dell2 research s.2, s.5; Andrew "resolution of the ticker ... how that can be locked in", "a process
                  of securities that cannot be mapped", "unresolved indexing on time period(s)"

FWD-6  Each page's history comes from a stated vendor by a stated rule
       DONE WHEN  APPLIED -- the rule is written and in force
       ACCEPT     for each page, a person can read which vendor supplies which figure (Bloomberg, Yahoo Finance, or the custodian's
                  own file), why, and what is used when that vendor fails; a figure a cheaper source already supplies is not taken
                  from Bloomberg
       SOURCE     site Z brief O5; Andrew "whether we go to BBG or YFinance and associated methodology per surface"

FWD-7  Yahoo Finance is used gently and reliably, and its prices stay right through splits and mergers
       DONE WHEN  EXERCISED -- a multi-day run read
       ACCEPT     every Yahoo request follows one shared pace, stops for the day when Yahoo pushes back and resumes where it stopped;
                  a refused or empty answer is reported as a failure, never shown as real prices; and a split or merger, including
                  one Yahoo records later, leaves a held position valued at the price it actually traded at
       SOURCE     site Z brief O7; dell2 research s.3, s.4; Andrew "be gentle with it", "corporate actions ... particularly
                  retroactively"

FWD-8  The same history is pulled once and shared
       DONE WHEN  EXERCISED -- shown on purpose
       ACCEPT     when two pages need the same security's prices over the same dates, it is pulled once and both pages show it, and
                  unchanged history is not pulled again the next day
       SOURCE     site Z brief O6, IV.1a (overlap measured)

FWD-9  What is pulled first follows how much it matters
       DONE WHEN  EXERCISED -- one real day's order read
       ACCEPT     when there is not enough room for everything, the securities that matter most to clients we still serve are pulled
                  first; an unmatchable fund held only by a client who is gone, by name and by account, is not pursued; and a person
                  can see the order and why each item sits where it does
       SOURCE     Andrew (Yahoo record) "we keep a 'ranking' on the importance ... that is not a priority to get"; dell2 research s.6
```

## Rulings at L2 (this seat)

1. **The unit is the cell (one row times one field), on every vendor ledger.** Andrew ~18:3xZ: "counting off the basis of cells".
   This supersedes the interim "returned records" unit of the standing ruling (msg 31939, as the site Z brief cites it). Every producer
   on the ledger changes unit together at build time; none changes alone.
2. **One project, run on dell1.** The Yahoo price backfill agreed for MDPF_SECHIST (dell2 msg 1456, my reply via msg 1072) folds in here,
   on Andrew's placement word. MDPF_SECHIST keeps the Bloomberg pull and supplies its price-need file as an input. ADVI_COTBKF's ranked
   need list is an input contract: a file at a fixed path with its key namespace stated. Yahoo egress runs under Andrew's record
   @489e1cd24c.
3. **Identity:** the existing resolvers (`etf-classifications`, the Black Diamond resolver, the override lists, AMGT's crosswalk) are
   inputs, not replaced. For client securities, the lock against the client's own trade prices (dell2 research s.1) is the proof that
   locks a mapping. A mapping is locked per date range, and a lock with no trade prices to check carries the claim `held`, not
   `measured`.
4. **Prices are stored as traded,** with splits and dividends kept apart, so a later correction is re-derived and never re-pulled (dell2
   research s.3).
5. **Bloomberg capacity is unknown** (site Z brief Part VII). FWD-3's reserve starts from the measured floor (2.92M BQL cells on
   2026-10-05) and is re-measured. Nothing in this project buys capacity or entitlement; that is Andrew's spend decision.
6. **The queue schedules and accounts; producers keep their own code.** Changing the model notebooks' daily re-pull is the owner's
   change. The queue reports its cost and proposes an incremental pull.
7. **Across boxes:** site Z holds the Bloomberg Terminal, so Bloomberg draws run there. Every box that calls Bloomberg or Yahoo reports to
   the one ledger. The ledger's home is chosen at L4 with builder-named addresses (CLAUDE.md rule 30).
8. **Pilot first:** a 50-security living-client pilot (dell2 research s.7 item 3) measures the error rate, the tolerance band and
   Yahoo's response before the first full session.

## Settled by Andrew (~22:4xZ, at the dell1 CTO terminal)

VERBATIM: "1.) Yes. 2.) Production daily pulls includes ETF Positioning. Then Current clients and new client onboarding. Then rival
funds history (which I think we can handle on BBG even if it takes a week or two of daily little jobs to get the majority of it out of
the way). Then research pages. Then finally former clients last. 3.) Only BBG and Yahoo for now."

1. The DONE WHEN lines FWD-1..9 are CONFIRMED as written.
2. **The priority order (FWD-9) is:**
   1. production daily pulls, which INCLUDE ETF Positioning;
   2. current clients and new-client onboarding;
   3. Rival Funds history, on Bloomberg, as small daily jobs over a week or two until the majority is done;
   4. research pages;
   5. former clients last.
3. **The queue meters Bloomberg and Yahoo only for now.** Other vendors stay named as sources in each page's vendor rule (FWD-6).
