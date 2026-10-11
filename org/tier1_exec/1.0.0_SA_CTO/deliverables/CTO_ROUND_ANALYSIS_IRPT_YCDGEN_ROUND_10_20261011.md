# CTO ROUND-10 ANALYSIS -- IRPT_YCDGEN -- answering the round-9 L10 slug (2026-10-11 ~08:3xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/remediations/REMEDIATION_v8.md`
@dafae769e6 (3.0.0_SA_CVO msg 4489), on `deliverables/2.0.0_SA_COO~G2/r9/ROUND9_DRAIN_END_READ_20261011.md` @9982fb211e.
**Prior:** `CTO_ROUND_ANALYSIS_IRPT_YCDGEN_ROUND_9_20261011.md` @eeb799ce72. **No PRD addendum.**

## 1. Where the project stands

**FWD-1 is NOT MET and has not been run as written.** Round 9 fixed the stored reason in the tree and measured the data. Nothing
is deployed. What the measurements say, all 2.0.0_SA_COO~G2's and 2.0.0_SA_COO~C2's reads of positions dated 2026-05-06:

| measure | value |
|---|---|
| Cottonwood securities with a characteristics row | 72 of 826 by count; 23.01% of PRICED value |
| position rows carrying no value | 6,122 of 10,090; by source, not by date or build (row ADVI_COTBKF-D2-S100) |
| unpriced by kind | Fixed Income 184 of 184; Mutual Fund 89 of 113; Cash Equivalent 55 of 57; Equity 68 of 294; ETF 24 of 134 |
| accounts with positions | 744; all priced and symbolled: 59 |
| of those 59, at 90% coverage or more | 1 today; 41 after a 14-symbol addition |
| size of those 41 | 23 hold one position, 17 hold two to five, ONE holds six or more |
| the 70 elements with no rule | PARTIAL 52, NOT_SEEN_IN_REPO 18, by repo evidence |

## 2. The sitting: NOT ASKED in round 10. The decision and its reason

An Overview Andrew could open today for a real Cottonwood portfolio would read "not covered" for most of what the account
holds, and, once this round's release lands, it would say so truthfully. That is not what FWD-1 asks him to look at. The
accounts that would read well after the 14 symbols are almost all one-to-five-position accounts, where an Overview shows
little whatever the coverage.

**The sitting is asked when ONE Cottonwood account holding six or more positions reads 90% or more covered on a regenerated
report whose page sentences are true, measured by a seat.** One such account exists on paper after the 14 symbols. Round 10
finds out whether it exists in fact.

Two things bound that, and neither is this project's to fix:
- **Cottonwood's unpriced positions.** 685 of 744 accounts hold one. Fixed income is unpriced entirely. A report cannot value
  what the holdings table does not value. This is ADVI_COTBKF's source question (row D2-S100, 2.0.0_SA_COO~C2).
- **The 70 rule-less elements** are FWD-14's scope and are enrichment after the thread runs.

## 3. Ruling on the row

| row | ruling |
|---|---|
| **D2-S44** (OBSERVATION, INERT; owner 2.0.0_SA_COO~G2): the page prints one sentence for both causes and appends the stored string | As ruled in msg 4477 and as the slug states it: two sentences, one per cause, no raw string, in the same resident release as the reason fix. The close is the rendered page, read by the reviewer. |

## 4. ENRICHMENT LIST for round 10 (ONE issuance, in this order)

1. **The page sentence** (D2-S44). LOCAL build.
2. **Can the store's source describe the 14?** Read-only, NO pull: on the store's existing 172 securities, by kind, how many
   mutual funds, ETFs and cash symbols carry a country and a sector today. If funds read empty where equities read full, the
   source does not describe funds and a pull of fund symbols buys nothing.
3. **The one account.** For the account of six or more positions: its position count, and its coverage by value today, after
   the 14, and after only those of the 14 that item 2 says the source can describe. Counts and percentages; no account id, no
   figure.
4. **The resident release:** the reason fix and the page sentence, under one never-widen pair, then the census re-run on a
   regenerated report. This is the first deploy of the project in three rounds.
5. **The data request, written and not sent:** the describable subset of the 14, as the request the Bloomberg queue takes, by
   a seat that has read `integrations/bloomberg/READ_HERE.md` first. Adding rows to the store moves served data, so it is sent
   only under its own pair, in round 11.
6. **Carried cells e and f** (D2-S38's status read; S16's generation hop from TCKT_VNEXT's run 3).

Items 1, 2 and 3 are independent. Item 4 follows item 1. Each build order carries at most three mechanical criteria.

## 5. Acts only Andrew can do

- **The FWD-1 sitting.** Citation: PRD FWD-1 ACCEPT, "Andrew, signed in as himself". Not asked; section 2 states when.

## 6. What this analysis did not measure

Every number in section 1 is another seat's read, as filed, on one date. This seat read no positions, no store and no layout
code. "One account of six or more positions" is a count from 2.0.0_SA_COO~G2's per-account read @e64d4e4418; nothing about that
account is known here beyond the count.

-- 1.0.0_SA_CTO~DELL2
