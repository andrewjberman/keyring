# IRPT_CUSTDY -- Q-1: investor reporting from the custodian level for 49 Financial and Cottonwood, replacing Black Diamond by 2027-01-01

```json
{
 "project": "IRPT_CUSTDY",
 "directive": "D9",
 "fabric": "laptop",
 "prd_version": "v0.1",
 "step": 4,
 "brief_ref": "docs/briefs/q1-custodial-investor-reporting-programme-brief-20261006.md@b714dd81b1",
 "endpoint_outcomes": [
  "FWD-1",
  "FWD-2",
  "FWD-3",
  "FWD-4",
  "FWD-5",
  "FWD-6",
  "FWD-7",
  "FWD-8",
  "FWD-9"
 ],
 "status": "RATIFIED"
}
```

**Author:** `1.0.0_SA_CTO` (L2-L4), 2026-10-06. **Brief:** `docs/briefs/q1-custodial-investor-reporting-programme-brief-20261006.md@b714dd81b1`. **Endpoint proposal:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_Q1_CUSTODIAL_INVESTOR_REPORTING_20261006.md`.
**Confirmed by Andrew:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261006_210xZ_SEVEN_CALLS_RDP_LOCK_Q1_Q2_Q3_CONFIRMED_NO_BD_SHAPE.md`. **Sign-off:** `3.0.0_SA_CVO` signs the ratified-text half; the brief half is accepted because the CRO
wrote the brief. **COO:** UNSEATED at registration; seating is `0.0.0_AB_MSTR`'s on Andrew's word.

## ENDPOINT (step 2, /endpoint --forward)

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

  FWD-9  For every figure a Black Diamond report shows, anyone can see where Opal gets it instead
         DONE WHEN  EXERCISED -- the map read for every field of one Black Diamond client report
         ACCEPT     for each figure in a Black Diamond client report, a person reads which Black Diamond
                    source served it and where Opal reads the same figure from the custodian or Opal's own
                    store; a figure with no other source is named as such; where Commonwealth's history
                    holds more than Black Diamond's feed, that is shown
         SOURCE     Andrew-direct ~21:0xZ, "figure out what black diamond endpoints correspond with the
                    various fields and we essneitally do black diamonds job for them"
```

## CONTRACTS

| Contract | Direction / owner | Binding agreement |
|---|---|---|
| C-SHAPE: built to the custodian's shape, never Black Diamond's | Andrew, call 6 | Opal's reporting model follows the custodian's data (expected close to the Commonwealth backfill's shape); no table, field or template is designed around Black Diamond. Black Diamond is a field map only (FWD-9): each report field, the Black Diamond source that serves it, and the custodian or Opal source that replaces it. His suspicion is tested, not assumed: Commonwealth's history is fuller than the Black Diamond pull. |
| C-COMPARE: two dated comparisons (FWD-5) | Andrew, call 3 | Exactly two comparisons, at the 2026-09-30 and 2026-12-31 quarter-ends, each written once with every difference and its reason; no job reruns them (the no-standing-comparator law). ADVI_BDPARITY's classes are reused, and it closes MERGED here. |
| C-TEMPLATE: per-firm templates (FWD-3) | Andrew, call 6 | Each firm's template is built from the custodian-shaped model, not from the Black Diamond report's layout. Who approves a template is OPEN at Andrew; by standing law nothing reaches a client without his word. |
| C-PROGRAMME: what this project owns | this seat at L3 | Owns templates, the Cottonwood consolidation, the comparison, the switch-off view, the field map and the end-to-end quarter-end run. The eight related projects keep their PRDs. ADVI_STITCH and ADVI_COTKEY fold into FWD-4 and close MERGED; ADVI_BDPARITY into FWD-5. |
| C-NO-SHADOW / C-MORATORIUM | law | Opal's reports replace Black Diamond's; nothing runs beside it after the switch; no alert or monitor. |
| C-NAMES / C-FIRM | law | Every new address and name is builder output; every key is under one firm's scope. |

## THREAD -- FWD-1, round 1

FWD-1 as written above is round 1's one journey, every hop real; the other outcomes are the enrichment
backlog in their numbered order.

-- 1.0.0_SA_CTO
