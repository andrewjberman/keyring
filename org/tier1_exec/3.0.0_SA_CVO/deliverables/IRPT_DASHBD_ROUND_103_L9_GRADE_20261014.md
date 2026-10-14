# IRPT_DASHBD round 103 -- L9 grade of DB103-1-J1

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-14 ~05:4xZ. **Asked by:** msg 7552, packet
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND103_B_DRAIN_END_20261014.md` @571a22eeee.
**Criterion** (`task-orders/IRPT_DASHBD.TO-DB-b-193.*.md:45`), two clauses:
- the holdings table is in the baseline's orientation, with its class hierarchy as the baseline draws it, in tab and export;
- every client-facing unavailable-figure line reads as plain words a client would understand.

**Read by this seat:**
- the baseline's Holdings Overview: rows are the class hierarchy (class, then sub-class); columns are Ending Value | Allocation | Net Gain
  and Return for L12M, YTD, QTD, MTD and Since inception; "a class with no holding prints —";
- pages 1, 3, 5, 6 and 14 of the issuer's final render (`.../fwd21_sample_r103_final/pages/`);
- the holdings table's headers and row heads parsed from `FWD21_TAB_49F_SAMPLE.html`.

No client figure is copied here.
**Result: FAIL on the wording clause; the orientation clause is met.**

## Clause 1, orientation -- MET

- **Export (p.6):** rows are Household, then Cash, Fixed Income, Equity, Structured, Alternatives, Commodities, Unclassified. Columns are
  Ending Value, Allocation, then Net Gain and Return for Last 12 Months, Year To Date, Quarter To Date, Month To Date and Since inception,
  in the baseline's order. Nothing is transposed now.
- **Tab:** the same column headers in the same order, and the same row heads (parsed from the HTML). Both are built from one view model.
- **The class hierarchy:** the baseline's own groups (US, INTL, Taxable, Non-Taxable, Real Estate, Cash, and their sub-classes) have no
  contract member. Opal's seven classes are drawn as the class level, and the sub-class level says in words "Sub-class rows: not available
  yet". That is the hierarchy the data allows, stated honestly. I accept it on the condition that the sub-class rows follow once a member
  exists.

## Clause 2, plain words -- NOT MET, on two counts

1. **A class the household does not hold reads "Not available yet".** On p.6, Alternatives, Commodities and Unclassified print "Not
   available yet" in the Allocation column. The round-101 render's own note said these classes have no holding on the as-of date. The
   baseline prints a dash for a class with no holding. A client reading "Not available yet" would believe Opal lacks the figure, when the
   true answer is that the household holds none. The words are plain, but what they tell the client is wrong.
2. **Section notes with no referent.** On pages 1, 5, 6 and 14, the section opens with stacked sentences: "This figure needs more history
   than is available yet." / "This figure is not available yet." / "This figure does not apply." None of them says WHICH figure. On p.6 all
   three print together above a table with absent cells of different kinds. A client cannot tell which figure "does not apply". The
   reason now lives only in an attribute, invisible on the page.

**Remedy (one small render cell):**
- a class with no holding prints the baseline's dash (or 0.0%), never "Not available yet";
- each kind note either names its figures ("Returns before July 2024 need more history than is available yet") or sits beside the
  cells it explains.

The chart-title defect the issuer saw on p.3 belongs in the same cell. The chart is titled "Household performance, last 12 months, with
benchmark lines", but it draws only the four benchmark lines.

## Seen and in order

- The header reads "49 Financial / Performance Report" on every page I opened; the placeholder is gone.
- No build language is visible.
- Percent values print at their stored scale.
- The benchmark chart draws four series.
- The Portfolio Value Summary is filled for beginning value.

-- 3.0.0_SA_CVO
