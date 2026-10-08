# IRPT_CUSTDY -- Q-1: investor reporting from the custodian level for 49 Financial and Cottonwood, replacing Black Diamond by 2027-01-01

```json
{
 "project": "IRPT_CUSTDY",
 "directive": "D9",
 "fabric": "laptop",
 "prd_version": "v0.4",
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

## 1. The arc

**Start.** Black Diamond produces every quarter-end client report for 49 Financial and Cottonwood. Opal already holds 49
Financial's Schwab records (brief F1), computes 49 Financial performance on its own method (F4), and serves holdings and an
export from IRPT_BCKEND; it has no per-firm template (F6) and no report an advisor would send. **End.** On 2027-01-01 every
client report of both firms comes from Opal on the firm's own template, built from the custodian's shape, with the two
dated comparisons written and the switch-off view read.

## 2. THREAD -- FWD-1, round 1

FWD-1 is round 1's one journey: one named 49 Financial advisor's quarter-end reports for 2026-09-30, every hop real.

1. **The advisor and the client list.** One 49 Financial advisor is named. That advisor's accounts and households are read
   from the firm's advisor-ownership map (row W1-S1: a directory entry carries no advisor). The map's address is builder
   output once its naming-registry row lands; until then the read is routed under laptop decision 106087. The IRPT_BCKEND
   directory (`directory_runner.py`, `irpt-directory-search`) supplies only names and households for the accounts the map
   assigns. Output: the account and household list the run covers, its count printed.
2. **Schwab's records for those accounts.** Positions, balances, transactions and realized lots for the quarter are read
   from Schwab silver under `opal-data-assets/schwab/<master>/` (producer `data/assets/scripts/silver/schwab_conversion.py`),
   never from Black Diamond. Output: per account, the custodian rows for 2025-09-30 to 2026-09-30 (the longest standard period
   the quarter report shows is read at L5 from the 49 Financial template).
3. **The figures.** Returns per account and household over the standard periods, holdings, activity and fees, computed by
   Opal: returns and holdings from the holdings-based gold (IRPT_DASHBD `account_return_daily` and IRPT_BCKEND
   `data/assets/scripts/gold/investor_reporting/holdings_49f.py`); activity from the transaction rows of hop 2. Fees: the
   source is not measured (brief PART V, Q-2); round 1 reads the fee rows Schwab's transactions carry and names every
   account where that is not the billed fee.
4. **The securities.** Every holding takes its class, sector and history from Opal's securities record: the one classification
   table (MDPF_SECCLASS; reader `infra/aws/lambda/v2_portal/_shared/etf_classification.py`) and MDPF_SECHIST. A holding Opal
   cannot describe is shown as such (FWD-6 starts here, on one advisor's holdings only).
5. **The report.** Hops 3 and 4 are laid into the 49 Financial template and rendered per client on the IRPT_BCKEND export path
   (`infra/aws/terraform/investor-reporting/export/b2_render.tf`, function `irpt-export-render`). The template is new (F6):
   round 1 builds the 49 Financial one only, from the custodian-shaped model (C-SHAPE, C-TEMPLATE).
6. **The read.** The advisor's firm reads every report of the run and says whether it would send it as it is. A report it would
   not send is listed with the reason. Nothing reaches a client (C-TEMPLATE: Andrew's word).

Round 1 does not touch Cottonwood, Inflection, the comparison or the switch-off view.

## 3. ENRICHMENT BACKLOG (ordered)

1. FWD-9: the field map for one Black Diamond client report (feeds every later template and the comparison).
2. FWD-5, first comparison: the 2026-09-30 quarter-end, written once, ADVI_BDPARITY's classes reused.
3. FWD-6 widened: every holding in every 49 Financial report from the securities record.
4. FWD-3: the Cottonwood template; one report read in each firm's template.
5. FWD-4: the Cottonwood consolidation over ADVI_COTBKF's history and the Black Diamond `z09` daily feed (ADVI_STITCH and
   ADVI_COTKEY fold in here).
6. FWD-7: the per-firm switch-off view.
7. FWD-2 dry run, then FWD-5 second comparison at 2026-12-31, then FWD-2 itself (the year-end run, both firms).
8. FWD-8: Inflection from Orion, after both firms are switched.

## 4. WORKSTREAMS AND OWNERS

- One workstream in round 1; COO lane `2.0.0_SA_COO~K2` (seated by `0.0.0_AB_MSTR~DELL2`; placement dell2).
- Gold and silver scripts are DS-lane work under rule 13; Lambda and Terraform changes are DT/AE work through `safe-apply`.
- IRPT_BCKEND, IRPT_DASHBD, ADVI_PERFRP, ADVI_49F, MDPF_SECCLASS, MDPF_SECHIST and ADVI_COTBKF keep their PRDs; a hop that
  needs their change is a CONSUME against their served artifact, or a request to their COO, never a write into their paths.
- **fabric:** the header keeps `"fabric": "laptop"`; the box is carried by `placement` (control-plane brief section 3: two
  readers know only two fabrics).

## 5. Rulings closed at L4

1. Round 1 is one 49 Financial advisor at the 2026-09-30 quarter-end (FWD-1), the only real quarter-end before the switch.
2. Fees in round 1 come from Schwab's transaction rows, labelled as such, until billing (Q-2) names the fee source.
3. Every new address and name is `lib/opal_naming.py` output; none is typed here (builder output owed at L5).
4. Black Diamond is read only for the field map and the two comparisons; no hop reads it to make a figure.

## 6. SURFACE MANIFEST (step 4 -> step 5)

| id | outcome_ref | surface | claim | verb | depends_on | bound |
|---|---|---|---|---|---|---|
| S01 | FWD-1 | the advisor's accounts from the firm advisor-ownership map (address: builder output owed; registry row asked of the laptop, laptop decision 106087), names and households from `directory_runner.py` / `irpt-directory-search` | measured (row W1-S1; ~K2 round 1) | consume | -- | one advisor, count printed |
| S02 | FWD-1 | Schwab silver for those accounts under `opal-data-assets/schwab/<master>/` (`schwab_conversion.py`) | held (brief F1) | consume | S01 | custodian rows only |
| S03 | FWD-1 | holdings-based returns: IRPT_DASHBD gold `account_return_daily`; IRPT_BCKEND `holdings_49f.py` | unmeasured (served state per those projects) | consume | S02 | standard periods |
| S04 | FWD-1 | fee rows from Schwab transactions, labelled; the billed-fee source (Q-2) | unmeasured | measure | S02 | every unmatched account named |
| S05 | FWD-1, FWD-6 | securities record: `infra/aws/lambda/v2_portal/_shared/etf_classification.py` (MDPF_SECCLASS) and MDPF_SECHIST | held | consume | -- | six classes only |
| S06 | FWD-1, FWD-3 | the per-firm template model (NEW; address and name builder output owed at L5) | unmeasured (brief F6: none exists) | build | S03, S04, S05 | custodian-shaped |
| S07 | FWD-1 | the render on the IRPT_BCKEND export path (`export/b2_render.tf`, `irpt-export-render`) | held | wire | S06 | one report per client |
| S08 | FWD-1 | the advisor firm's read of every report, written down | unmeasured | measure | S07 | nothing to a client |
| S09 | FWD-9 | the Black Diamond field map (NEW; builder output owed at L5) | unmeasured | build | -- | every field of one report |
| S10 | FWD-5 | the two dated comparisons (ADVI_BDPARITY classes) | unmeasured | measure | S07, S09 | written once each |
| S11 | FWD-4 | the Cottonwood consolidation over ADVI_COTBKF silver and `opal-data-assets/blackdiamond/cottonwood/` | held (brief F2) | build | ADVI_COTBKF | no gap, no double count |
| S12 | FWD-7 | the switch-off view (NEW; builder output owed at L5) | unmeasured | build | S07 | per firm |
| S13 | FWD-8 | Inflection from `opal-data-assets/orion/inflection/` | held (brief F3) | consume | FWD-2 | after the switch |

## 7. BRIEF COVERAGE

| Brief heading | Carried | Consuming sections |
|---|---|---|
| PART I, thread and O1-O7 | the thread; seven outcomes plus FWD-9 | ENDPOINT; section 2 |
| PART II, boundary | owns templates, consolidation, comparison, switch-off view; relies on eight projects | C-PROGRAMME; section 4 |
| PART III, bar | sent without question; no Black Diamond login; no seam; reasons written first; readiness any day | FWD-1, FWD-2, FWD-4, FWD-5, FWD-7 |
| PART IV, F1-F6 | Schwab data held; Cottonwood via Black Diamond; Orion; Opal's method; securities rebuild; no template | sections 2 and 6 |
| PART V, must be true | the date; Cottonwood's custodian (unmeasured); fees (Q-2); the cold projects; capacity; no shadow | FWD-2, S04, S11, C-PROGRAMME, C-NO-SHADOW |

-- 1.0.0_SA_CTO

## v0.2 (1.0.0_SA_CTO~DELL2, 2026-10-07) -- L4 surfaces on `2.0.0_SA_COO~K2`'s hand-back (msg 4)

Added sections 1-7: the THREAD's six hops, the ENRICHMENT BACKLOG, owners, the L4 rulings, the SURFACE MANIFEST and BRIEF
COVERAGE. The ENDPOINT and CONTRACTS are not edited, so the ratified-text half does not re-open.

## v0.3 (1.0.0_SA_CTO~DELL2, 2026-10-07) -- hop 1's source corrected on row W1-S1

Hop 1 and S01 now name the firm advisor-ownership map as the advisor's account source. The directory only names the
accounts. Neither the ENDPOINT nor the CONTRACTS changed.

## v0.4 (1.0.0_SA_CTO, 2026-10-08) -- a wording addendum: the product is the "Performance client statement"

Andrew-direct ~21:2xZ at the `1.0.0_SA_CTO~DELL2` terminal, VERBATIM: "Yeah the issue with the custody report is that it really
sounds like its just a performance report, I dont see the differnce between what youre discussing for that purpose with what will
end up being on the performance tab" and "if the functions youre building out are additive and currently dont exist on the
performance tab, then that is great, but lets refer to it accoridngly" (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_212xZ_CUSTODY_REPORT_IS_PERFORMANCE_ADDITIVE_REFER_ACCORDINGLY.md`
@b15e76c232, dell2).

- Wherever this PRD says "custody report", read **"Performance client statement"**: the quarterly client-facing export of the
  Performance report, with the added holdings, activity and fees sections, rendered in each firm's template, sourced from the
  custodian. "Custody report" is retired as a product name.
- The work continues; it is additive to the Performance tab.
- Code identifiers in flight stay (`CUSTODY_REPORT`, `irpt-custody-x10-v1`, `custody-report-read`, `custody_write.py`), each
  documented as the Performance client statement where it is defined.
- Wording only. FWD-1 to FWD-9, the ENDPOINT and the CONTRACTS are unchanged in substance; no half re-opens.
