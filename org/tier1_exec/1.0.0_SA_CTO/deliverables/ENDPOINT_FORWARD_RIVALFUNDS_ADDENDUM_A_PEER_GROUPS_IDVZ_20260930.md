# ENDPOINT ADDENDUM A (step 2, /endpoint --forward) -- ETFS_RIVALS: peer groups per Opal fund, the IDVZ group, income-clean trades -- `1.0.0_SA_CTO~Z`, 2026-09-30 ~15:5xZ

**Brief:** `docs/briefs/etfs-rivals-idvz-expansion-20260930.md` (midstream, `4.0.0_SA_CRO~Z`, msg 27235; 12,496 B, read to EOF).
**Andrew's words it rests on** (verbatim in `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/AMGT_RECONN_SOURCES_20260929/ANDREW_DIRECT.md`):
- *"this is simply an expansion on the initial tracked group"*;
- the IDVZ group from Adam (IDVZ, TXUE, BIDD, CGIC, INEQ, SCHY);
- the three views: *"trading outperformance/underperformance by sector and security; forward projected trading activity based on
  observable trends across sectors/securities; a 'hand-on-the-door wildcard analysis from the AI'"*;
- *"include the Opal Funds like IDVZ and PFOE into this list so we have them on the same analysis plane"*;
- *"did we already account for dividend/interest income? That should be covered"*;
- *"bbg is better for this group"*.
**Base endpoint:** `ENDPOINT_FORWARD_RIVALFUNDS_20260930.md` (FWD-1..9, landed in PRD v0.2).

**STATUS: PROPOSAL. Andrew confirms the DONE WHEN lines** (his 2026-09-03 word). Ids are permanent: amended outcomes keep their
numbers, and new outcomes take FWD-10, 11 and 12. **FWD-4, FWD-8 and FWD-9 are unchanged.**

---

```
  FWD-1  (AMENDED) Andrew opens one Opal fund's peer group on the live page
         and reads it, the Opal fund included, on one analysis plane
         DONE WHEN  EXERCISED -- one live trace: Andrew selects IDVZ on the
                    rival-funds page and reads IDVZ and its five peers side by
                    side (trade schedules, style reads, the views in FWD-6/7),
                    then follows one rival's trade back to the holdings reports
                    it was inferred from and to where they came from; selecting
                    PFOE shows its group the same way, PFOE included
         ACCEPT     every step shows real published holdings; a step fed by
                    sample data fails the outcome
         SOURCE     brief O1; Andrew point 3 (home funds on the same plane)

  FWD-2  (AMENDED: every fund in every group) Andrew sees how much real
         history each fund has, and never mistakes an old report for a fresh one
         DONE WHEN  EXERCISED -- for every fund in both groups, Andrew reads
                    which days carry a genuinely new report, which repeat an
                    older one, and which are gaps, back up to two years or the
                    fund's own start
         ACCEPT     as before; a fund that is in two groups is shown once, with
                    one history
         SOURCE     brief O2, IV.1

  FWD-3  (AMENDED: the source is chosen per fund) Fresh holdings arrive every
         trading morning with nobody downloading anything, from each fund's
         chosen source
         DONE WHEN  EXERCISED -- over several consecutive trading days, every
                    fund is collected each morning by its own source policy:
                    the IDVZ group from Bloomberg, the PFOE group from each
                    fund's own site with Bloomberg as the fallback; the page
                    names the source per fund and day
         ACCEPT     Andrew does nothing by hand; a fund's policy is a setting,
                    not code; a day a source fails says so plainly
         SOURCE     brief O2, IV.1-IV.2; Andrew "bbg is better for this group"

  FWD-5  (AMENDED: income and corporate actions) Andrew reads each fund's
         trade schedule: what the manager actually bought and sold, and when
         DONE WHEN  EXERCISED -- for every fund Andrew reads its trades
                    (entries, adds, trims, exits) with shares, window, estimated
                    price and size and confidence; on a fund and window that
                    contain a dividend, a split and a cash/currency line, none
                    of the three appears as a trade, and a purchase funded from
                    income reads as a trade labelled as income-funded
         ACCEPT     dividend and interest income, their currency conversion,
                    splits, bonus issues, spinoffs, stock dividends and rights
                    issues never read as a manager's decision; cash and
                    currency lines are the cash cross-check, not positions
         SOURCE     brief O3, IV.3; Andrew "did we already account for
                    dividend/interest income? That should be covered"

  FWD-6  (AMENDED: by sector and security) Andrew sees where each manager's
         trading helped or hurt, by sector and by security
         DONE WHEN  EXERCISED -- for one fund and period Andrew reads which
                    trades and trade clusters out- or under-performed afterwards,
                    summarised by sector and by security, each with its window
                    and denominator, including positions since sold
         ACCEPT     a holding with a missing price or sector is counted as
                    missing, never left out
         SOURCE     brief O5; Andrew view 1

  FWD-7  (AMENDED: projections and the wildcard) Andrew uses the AI to form
         views about a manager's behaviour, and can check them later
         DONE WHEN  EXERCISED -- for one fund Andrew reads (a) its projected
                    trading by sector and security if the observed trends
                    persist, each with what would contradict it, and (b) a short,
                    labelled wildcard section in which every item cites its rows
                    and says what would disprove it; a later account grades the
                    earlier projection against trades inferred after it
         ACCEPT     nothing invents a return, a trade or a motive; a later
                    grading cannot rewrite the earlier account
         SOURCE     brief O6, O7; Andrew views 2 and 3

  FWD-10 (NEW) Andrew sees whether each manager trades with discretion or by
         system, and why
         DONE WHEN  EXERCISED -- Andrew reads each fund's style read with its
                    evidence (timing concentration, breadth of the book touched,
                    trade size), and the group's index fund (SCHY) reads as
                    systematic on that same evidence
         ACCEPT     a count of trades alone is never the evidence; a label is
                    shown only after the control reads correctly
         SOURCE     brief O4, IV.3; Andrew "at a 20bps tolerance it's
                    immediately clear who is discretionary and who is
                    systematic"

  FWD-11 (NEW) Andrew compares an Opal fund with its rivals on the same
         measures
         DONE WHEN  EXERCISED -- Andrew reads IDVZ against its peers and PFOE
                    against its peers on the style read, the trading results and
                    the projections, computed by the same rules
         ACCEPT     Opal's own fund has no separate method and no special
                    treatment
         SOURCE     brief O8; Andrew point 3

  FWD-12 (NEW) Opal adds a peer group without a new pipeline
         DONE WHEN  EXERCISED -- a third group is added as a mapping entry
                    (the Opal fund, its rivals, each fund's source policy) and
                    flows through collection, the tables, the page and the
                    archive with no code change
         ACCEPT     a fund rivalling two Opal funds is stored once; adding a
                    group changes a mapping, not code
         SOURCE     brief O9, IV.4
```

---

## THE ONE PRD QUESTION, RULED AT L4 (not an endpoint line)

**Which single producer feeds the home funds (IDVZ, PFOE)?**
- The existing `integrations/bloomberg/pipeline/etf_constituents_pull.py` already pulls them.
- **Ruled: ONE writer per fund's holdings.**
- The PRD's first cell measures the existing producer's output: daily, share counts, and history depth.
  - If it meets FWD-2/3's grain, ETFS_RIVALS READS it.
  - If it does not, the home fund moves into ETFS_RIVALS' Bloomberg request, and the old pull stops writing that fund in the same
    window.
- Never two producers of the same holdings (CLAUDE.md, no duplicate output path).
