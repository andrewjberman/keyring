# ENDPOINT (step 2, /endpoint --forward) -- Q-1: investor reporting from the custodian level, replacing Black Diamond by 2027-01-01

Author `1.0.0_SA_CTO`, 2026-10-06 ~19:4xZ (3:4x PM Eastern). **STATUS: PROPOSED, for Andrew to confirm. NOT LANDED.**

**Brief read:** `docs/briefs/q1-custodial-investor-reporting-programme-brief-20261006.md` @b714dd81b1 (`4.0.0_SA_CRO`, 166 lines, read in
full). Andrew's words: `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_183xZ_FOUR_BOX_ACCELERATION_PROJECT_CENSUS_AND_Q4_GOALS.md`.

**Proposed register shape (L3, this seat's call):** ONE new programme project, `IRPT_CUSTDY` (D9/IRPT), owning only the gaps: per-firm
templates, the Cottonwood consolidation, the hand-over comparison, the switch-off view, and the end-to-end quarter-end run. The eight
live projects keep their own PRDs; each outcome below names which serves it. The three cold projects fold in and close as MERGED:
ADVI_STITCH and ADVI_COTKEY into the Cottonwood consolidation (FWD-4), ADVI_BDPARITY into the hand-over comparison (FWD-5).

```
  FWD-1  One 49 Financial advisor's quarter-end client reports are produced by Opal from Schwab's
         records, and the advisor would send them without opening Black Diamond
         DONE WHEN  EXERCISED -- every client report for one real advisor, for the quarter ending
                    2026-09-30, produced and read by that advisor's firm
         ACCEPT     for one named 49 Financial advisor, every client gets a quarter-end report built by
                    Opal from Schwab's own records: returns, holdings, activity and fees for each account
                    and household over the standard periods; the advisor reads them and says they would
                    send them as they are
         SOURCE     brief PART I, the candidate thread; O1

  FWD-2  Every 49 Financial and Cottonwood client's report for the quarter ending 2026-12-31 comes from
         Opal, and nobody at either firm opens Black Diamond to produce one
         DONE WHEN  EXERCISED -- the 2026-12-31 quarter-end run for both firms, every client, read
         ACCEPT     for the year-end quarter, every client of both firms has an Opal report; no one at
                    either firm logs in to Black Diamond to make a report; a report Opal could not make is
                    listed by name with the reason
         SOURCE     brief O1; PART III items 1-2; Andrew, "it has to be done by january 1st"

  FWD-3  Each firm's reports are in its own template
         DONE WHEN  EXERCISED -- one report read in each firm's template, and the firm agreeing it is theirs
         ACCEPT     a 49 Financial report and a Cottonwood report each show that firm's own sections,
                    periods, benchmarks, wording and branding; changing one firm's template changes nothing
                    in the other's
         SOURCE     brief O2; Andrew, "performance reporting templates per advisor firm"

  FWD-4  A Cottonwood client's history reads as one record from 2013 to today
         DONE WHEN  EXERCISED -- one account read across the 2026 hand-over, with no gap and nothing counted
                    twice
         ACCEPT     for a Cottonwood account, the Commonwealth years and the daily Black Diamond data after
                    the move read as one history: one set of returns and one transaction list; at the
                    hand-over there is no missing stretch and no doubled entry, and an account that cannot
                    be joined says why
         SOURCE     brief O3; Andrew, "an adapter ... consolidated shape between the commonwealth and the
                    ... black diamond data for cottonwood"

  FWD-5  Before the switch, every figure where Opal and Black Diamond disagree has its reason written down
         DONE WHEN  EXERCISED -- the comparison read for the 2026-09-30 and 2026-12-31 quarter-ends
         ACCEPT     for each of the two quarter-ends, a person sees where Opal's figure matches Black
                    Diamond's and, where it differs, the reason, written before anyone asks; after the
                    year-end switch no comparison runs again
         SOURCE     brief O4; PART III item 4

  FWD-6  Every security in a client report is described and valued from Opal's own securities record
         DONE WHEN  EXERCISED -- one report's holdings each traced to Opal's classification and history
         ACCEPT     every holding in a client report takes its class, sector and history from Opal's own
                    securities record, never from Black Diamond's labels; a holding Opal cannot describe
                    is shown as such
         SOURCE     brief O5

  FWD-7  Andrew can see, any day, how far each firm is from switching off Black Diamond
         DONE WHEN  EXERCISED -- the view read for both firms on one day, and its counts checked
         ACCEPT     for each firm, Andrew reads which reports Opal makes, which still come from Black
                    Diamond, and what is left, and can say which firm is ready
         SOURCE     brief O6; PART III item 5

  FWD-8  Inflection's reports follow from its Orion data, after the two priority firms
         DONE WHEN  EXERCISED -- one Inflection client's report produced by Opal from the Orion data
         ACCEPT     one Inflection client report comes from Opal using the data Opal already holds from
                    Orion; this starts only after 49 Financial and Cottonwood are switched
         SOURCE     brief O7; Andrew, "inflection is not a huge priority"
```

## Which project serves each outcome

FWD-1, 2: the programme's end-to-end run over IRPT_BCKEND (back end), IRPT_DASHBD (total-return gold), ADVI_PERFRP and ADVI_49F
(49 Financial performance). FWD-3, 4, 5, 7: the programme itself (the gaps). FWD-6: MDPF_SECCLASS and MDPF_SECHIST. FWD-8: last,
after FWD-2.

## Calls for Andrew

1. **The hand-over comparison (FWD-5) and the no-standing-comparator rule.** Your standing veto bars a standing comparator. REC: two
   dated comparisons only, at the 2026-09-30 and 2026-12-31 quarter-ends, each written down once; no job runs it again.
2. **Who agrees a template is right (FWD-3).** REC: each firm's current Black Diamond report is the starting layout; you sign off
   each firm's template before any report reaches a client. Nothing goes to a client without your word.

## Not settled by this endpoint (measurements, not calls)

Cottonwood's current custodian and whether Opal can read it directly (brief PART V); where report fees come from (billing, Q-2).
Until a direct path exists, Cottonwood's "custodial level" is the Black Diamond feed.

## Provenance

GROUNDED ON: the brief, read in full. NOT READ: the eight projects' PRDs, the census, the four-box plan beyond what the brief carries.

-- 1.0.0_SA_CTO
