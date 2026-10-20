# Report to Andrew: the Ticket Center Analysis Request flow, closed out end to end on production (2026-10-20)

**From:** 1.0.0_SA_CTO~DELL2. **Answers:** your order relayed at 2026-10-20 01:05Z ("Close out the ticket center analysis request
ops ... Report to the ms inbox when the flow is closed out end to end, including what was verified live").
**Evidence:** the final run's receipt is `org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_commentary_e2e7d/A_E2E7D.txt`,
RUN-DONE PASS. Times are US Eastern.

## The headline

At 5:57 PM, a synthetic Opal staff user with nothing set up in advance (no advisor, no directory row, no firm list) filed an
Analysis Request through the production Ticket Center page. By 5:59 PM the still-open ticket carried all four items:
1. the holdings upload;
2. the form as filed;
3. the Opal report;
4. the AI commentary as its own PDF.

Both PDFs then opened from the ticket's own routes:
- the report: 39 pages, 231,470 bytes;
- the commentary: 2 pages, 45,182 bytes.

Nobody touched anything after Submit.

## What was verified live (run 7d, production)

| step | result |
|---|---|
| The form | Opens with the Advisor pre-filled with the filer and required, no report type, no commentary choice, no date field, the three firms, the five Opal models |
| Filing | Ticket TCK-20261020-7d5b0bf1 created at 5:57:05 PM |
| The report | Built by the Opal producer and READY within 30 seconds; the commentary was drafted and stored |
| The package | Attached at 5:59:09 PM; complete at 5:59:18 PM with all four items held |
| Open report | Shows the report face, not the construction log |
| Report PDF | Opens from the ticket route: a real PDF, 39 pages |
| Commentary PDF | Opens from the ticket route: a real PDF, 2 pages |

The two PDFs were opened through the same routes the ticket page calls. A person clicking them in a browser is the next thing to
see; your own sample filing is that check.

## What it took today (all on production)

1. **5:28 AM:** the new form went live, but it could not request the analysis. A field was missing from the page's own check.
   - Found by an offline test before any filing was affected: zero filings were hit.
   - Fixed at 10:26 AM.
2. **12:37 PM:** your walkthrough changes went live: the Advisor pre-filled and required, no date field, ETF chips, no Variant or
   commentary rows. The Advisor became required because the ticket service refuses a blank one.
3. **2:33 PM:** the ticket service was given permission to read the stored Opal report PDF.
4. **5:33 PM:** two bugs that stopped either PDF opening from the ticket were fixed. The commentary check compared the wrong
   fingerprints, and the report route looked for the PDF where it is never written.

Each release was checked before and after, and none needed a rollback.

## What is still open

- **Report content:**
  - 100 sections, 13 with values; the other 87 say "not available". Most are the comparison content of a Multi-Comp.
  - The Core comparison work you approved (FWD-10) fills them. It is built and signed, and ships next as one release.
  - That release also adds the Overview price pages and the audit record you approved.
- **Your Overview review (FWD-9):**
  - Today's Overview is saved for you at `C:\dev\andrew_samples\Opal_Overview_sample_E2E7D.pdf`. It is synthetic data, 39 pages,
    and kept outside the repository.
  - The next release adds the price pages to the Overview, so the version to judge against the YCharts sample is one filed after
    that release. I will send it when it exists.
- **Not exercised today:**
  - an unknown ticker that gets a proxy (the backend proposal step is being wired);
  - deliberately failed steps showing on the ticket;
  - another firm being refused.
  These are the project's other outcomes and come in the next rounds.
- **Your own filing:** you can file a real sample now. Everything above works on production.

-- 1.0.0_SA_CTO~DELL2
