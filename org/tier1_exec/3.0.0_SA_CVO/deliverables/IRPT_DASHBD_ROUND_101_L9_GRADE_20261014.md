# IRPT_DASHBD round 101 -- L9 grade of DB101-5-J1

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-14 ~04:3xZ. **Asked by:** msg 7518, packet
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND101_102_B_DRAIN_END_20261014.md` @4404620f0a.
**Criterion** (`task-orders/IRPT_DASHBD.TO-DB-b-191.section-by-section-check-of-the-49-financial-render.md:35`): each section's
`seen_in_render` faithfully reads the render against the baseline schema. That means the right section, the right members, the absent notes
as printed, and nothing claimed that the PDF does not show.
**Read by this seat:**
- the record `deliverables/0.9.0_WK_IRPT_DASHBD~156/SECTION_CHECK.json` (8 sections);
- the baseline schema `deliverables/1.0.0_SA_CTO~DELL2/BD_FINANCIAL_PERFORMANCE_REPORT_BASELINE_SCHEMA_20261013.md`;
- 8 of the 14 page images in the private folder (`.../fwd21_sample_r101_final/pages/r101/`): pages 1, 2, 4, 5, 7, 8, 11 and 14. These
  cover every section except the second pages of the multi-page ones.

No client figure is copied here.
**Result: PASS, with two notes.**

## Section by section, against the pages

| section | the record's claim | what the page shows |
|---|---|---|
| cover (p.1) | the report title is not printed; the household name and account list are absent beside long build notes; as-of in year-month-day form; footer "Household Performance Report" | Matches: "Not available yet" beside the two absent fields, as-of 2026-10-12, footer "Household Performance Report". See note 1 for the header. |
| portfolio overview (p.2) | chart headings print the absent form and draw nothing; long build notes | Matches on p.2: one chart heading, the absent form, no chart, and seven "Covers ..." build-note paragraphs. The table and fee-basis claims sit on p.3, which this seat did not open. |
| summary of accounts (p.4) | six column headings in the baseline's order; only ending value filled; "Account ending <last4>"; build notes above the charts | Matches exactly. |
| holdings (p.5) | a field list, not a table; window columns as rows; the class hierarchy not drawn, with a note naming Opal's seven classes | Matches. |
| taxable realized (p.7) | five columns in the baseline's order; three accounts, all absent; taxability not stated | Matches. Note 2 covers the heading. |
| account overview (p.8) | one table per account; benchmark rows absent; account-grain charts not drawn and silent; returns about 100x scale | Matches. Returns print 150.0%, 1120.0%, 1500.0% against net gains near 1.5%, 11% and 15% of value, so 100x is right. No chart and no note for the two baseline charts. |
| gain/loss review (p.11) | one row per account; four columns in order; realized absent; class rows not drawn | Matches. |
| disclosure (p.14) | one absent field with a long note naming the method field; the foot line on every page | Matches. |

Each section is the right section with the right members. The absent notes are quoted as printed ("Not available yet", plus the "Covers"
build text). No claim I checked is contradicted by its page.

## Notes

1. **An omission: "Sample Firm".** Every page I opened prints "Sample Firm / Performance Report" in the header, top right, where the
   baseline prints "49 Financial Performance Report". The record says the title "is not printed on the page or in any footer". That is true
   of the baseline title, but it omits that a placeholder firm name IS printed. That placeholder is a client-facing defect the ranked list
   does not carry. Add it to round 102's render-fix cell: the firm name must come from the firm, never a placeholder.
2. **A nit.** On p.7 the record calls the section heading "Taxable Realized Gain or Loss, Year To Date". That is the TABLE heading; the
   section heading reads "Taxable Realized Gain/Loss Summary, Year To Date", the baseline's wording. It does not change the reading.

Pages 3, 6, 9, 10, 12 and 13 were not opened by this seat. The issuer read pages 5 and 14 and agreed; the worker read all 14.

-- 3.0.0_SA_CVO
