# ENDPOINT (step 2, /endpoint --forward) -- ADVI_COTBOOKS v2: Cottonwood's whole book from its custodians, with no Black Diamond dependency (`1.0.0_SA_CTO~DELL1`, 2026-10-20 ~14:0xZ)

**Brief:** `docs/briefs/advi-cotbooks-custodian-first-rebrief-20261020.md` @fcb2c7cbaf (`4.0.0_SA_CRO~DELL1`).

**Order:** Andrew-direct, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261020_133xZ_COTBOOKS_NO_BD_DEPENDENCY_CUSTODIAN_FIRST.md`
@7fb4f70e80, VERBATIM: "we cannot rely on Black Diamond for any critical function ... we want Cottonwood to be our first true case
study where we figure out how to represent all their stuff without having any BD dependency."

**Supersedes:** `ENDPOINT_FORWARD_ADVI_COTBOOKS_20261017.md` (FWD-1..6). Those ids are retired and never reused. These are new
outcomes, numbered from FWD-1 under the v2 brief.

**The rule that binds every line:** a Black Diamond read is allowed only in a column labelled as the comparison. A Black Diamond
read anywhere else on an outcome's path fails that outcome.

```
  FWD-1  An analyst reads Cottonwood's Fidelity book for one day from Fidelity's own files
         DONE WHEN  EXERCISED -- on demand, for one stated business date, read from the
                    Fidelity landing under Cottonwood's own prefix: every account under
                    Cottonwood's G numbers counted once, with its holdings, cash and value;
                    the total printed beside Black Diamond's Fidelity figure for that date,
                    with every difference named
         ACCEPT     An analyst can say what Cottonwood holds at Fidelity on a given day, and
                    which Fidelity file each number came from, without opening Black Diamond
         SOURCE     brief Part I thread, O1, F3 (an account under two G numbers counts once)

  FWD-2  One Cottonwood account reads as one history, from Commonwealth to today
         DONE WHEN  EXERCISED -- one matched account's history is read end to end, from
                    2013 through the move to today. The Commonwealth-to-Fidelity link is
                    re-made against Fidelity's own positions, not Black Diamond's holdings,
                    and the join date shows
         ACCEPT     An analyst follows one client's account from Commonwealth into Fidelity
                    without switching tools, and can see the day it moved
         SOURCE     brief O2, F4; Andrew "stitch the commonwealth books to the fidelity
                    backfill"

  FWD-3  An analyst reads Cottonwood's Schwab accounts from Schwab's own files
         DONE WHEN  EXERCISED -- for one stated date, the Cottonwood Schwab accounts are read
                    from the canonical Schwab landing, beside Black Diamond's Schwab figure
                    for that date, every difference named.
                    QUALIFIED WAIT: the advisor master account numbers come from Alongside
                    (Andrew-direct 2026-10-20: "i am going to get those from Mike Little at
                    Alongside today"); the lane opens when they land
         ACCEPT     The Schwab part of the book reads the same way as the Fidelity part
         SOURCE     brief O3, F2 (0 of 20 in Opal's masters today)

  FWD-4  A person sees how much of Cottonwood's book Opal reads, and what it does not
         DONE WHEN  EXERCISED -- for one stated date, a coverage statement in accounts and
                    dollars for each class (Fidelity, Schwab, Strata, manual and
                    alternative, held-away), with every class Opal does not read named
                    beside its size on the same screen
         ACCEPT     No one mistakes a Cottonwood total for the whole book when a class is
                    missing
         SOURCE     brief O4, F1 (about 15% has no custodian feed); Strata a named gap

  FWD-5  Every Cottonwood account sits in one advisor's book, by an assignment Opal holds
         DONE WHEN  EXERCISED -- read on Opal's own advisor assignment for one date: every
                    account in exactly one book, none lost; Black Diamond's Portfolio Group
                    read beside it as the check, with each disagreement listed
         ACCEPT     The advisor books do not change if Black Diamond goes away
         SOURCE     brief O6, F3, F6 (no custodian or Commonwealth code separates
                    Rubottom from Shipley)

  FWD-6  One client's accounts across custodians are seen together
         DONE WHEN  EXERCISED -- one household with accounts at two custodians is read
                    under one Opal-owned client key, not Black Diamond's Relationship ID
         ACCEPT     A person sees a client's whole relationship in one place
         SOURCE     brief O5, F5

  FWD-7  Per custodian, the gap to Black Diamond is explained
         DONE WHEN  EXERCISED -- for one stated date, Opal beside Black Diamond for each
                    class, in accounts and value, with every difference given a named cause
                    (timing, an account one side lacks, pricing, a class Opal does not read)
         ACCEPT     The only differences left are ones someone can explain: the
                    replacement test
         SOURCE     brief O7, Part III replacement test

  FWD-8  A Cottonwood admin reads the firm as its advisors' books on Advisor Intelligence
         DONE WHEN  EXERCISED -- one live trace on a real admin login at a stated portal
                    commit: the first screen lists the advisors and their books, fed by
                    FWD-1 to FWD-5; one click reaches one advisor's clients; the page names
                    its books' date; an advisor login sees only its own book, and a request
                    for another's is refused; the tabs follow Inflection's layout
         ACCEPT     The Cottonwood page works like Inflection's, and every figure on it
                    traces to a custodian file
         SOURCE     brief O8 (the 2026-10-17 page outcomes); Andrew 10-17 "should be taking
                    on the Inflection Shape visually"
```

**Carried to Andrew with a REC, not outcomes:**
1. **Where the roughly 15% with no custodian feed comes from.** This is $82.6M of manual, alternative and held-away holdings, per
   Black Diamond on 2026-10-19.
   REC: v1 shows it as a sized "not read" line under FWD-4. The source (an Opal manual upload, an aggregator of our own, or leaving it
   out) is decided after FWD-1 to FWD-7 are read.
2. **Seeding the advisor assignment.** Today only Black Diamond's Portfolio Group records it.
   REC: seed it once from Black Diamond as a one-time import. Cottonwood confirms it, and from then on Opal holds and maintains it.
   Black Diamond is then a check, not a source.
3. **Strata.** Andrew: "We need to clarify that." It is a named gap (8 accounts, $2.0M) until then.

**Finding routed to NFRA_FIDUPL (surprise row D1-S6):** in Black Diamond's copy, most accounts sit under both PRIMARY and SECONDARY.
The advisor G numbers hold only 3 accounts. So the per-G pulls need a count-once rule, and the G numbers do not give the advisor
books; FWD-5 does.

-- 1.0.0_SA_CTO~DELL1
