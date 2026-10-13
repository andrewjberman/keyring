# CTO ROUND-94 ANALYSIS -- IRPT_DASHBD (workstream B) -- the default performance report, on Andrew's baseline (2026-10-13 ~19:1xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** the round-93 drain (FWD-8 REALIZED WITH NAMED RESIDUE, accounts 1 and 6; laptop ruling @51f07538ea)
and Andrew-direct ~19:0xZ at this terminal:

> "Second to that, we need to get back on that IRPT_DSHBRD work here because I want to see how we're able to get a sample display with all this information as a baseline format for any given client at any firm. I have included the Black Diamond export here so you can have a baseline schema that we can work toward for the "performance" tab as well as the export."

**PRD addendum:** v0.14 adds **FWD-21**, the default performance report (an ENDPOINT change, so the CVO and CRO halves re-sign). The baseline is
`deliverables/1.0.0_SA_CTO~DELL2/BD_FINANCIAL_PERFORMANCE_REPORT_BASELINE_SCHEMA_20261013.md`, structure only; the PDF stays off the repo. Andrew's
export answers pivot-direction call 7 ("templates sent last week"): **the baseline is this Black Diamond 49 Financial Performance Report.**

**Priority (pivot direction):** second to O1 and O2. It takes no seat from IRPT_ANLREQ. The L7 ledger read (2026-10-14 11:41Z) stays carried;
none of the cells below touches the gold Lambda.

## ENRICHMENT LIST for round 94 (ONE issuance, all LOCAL or DEV-only)

1. **The Opal Shape for the report (contract first):**
   - One JSON contract, `IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json`, with one member per baseline table, column and row.
   - Each member names its Opal gold source (existing `account_return_daily`, `dim_return_method`, holdings and class tables, activity
     flows, realized gains) or carries `source: ABSENT` with its reason.
   - Vendor-agnostic: no member names a vendor (Andrew ~18:2xZ).
   - It folds in FWD-20's figure map where that map exists.
   - Output: the contract plus a gap table, counting baseline cells with an Opal source against those ABSENT.
2. **One sample, end to end, from gold:** one 49 Financial household (multi-account) built into the contract shape by a builder that reads
   gold and writes nothing served. Print the household value summary and the activity summary as the proof read. Every figure without a
   source reads ABSENT, never zero.
3. **The render, DEV only:** the Performance tab and the export (`ExportModal`) take the contract shape for that household, in the
   baseline's section order.
   - The export modal's width and the UNEXPECTED status-read failure (Andrew's smoke, msg 7142) are fixed in the same portal candidate.
   - FDRXX maps to CASH.
   - YTD is measured from the first measured day.
   - The portal candidate goes to this seat's review.
4. **Ledger leg L7**, carried.

Cottonwood and Inflection samples follow once 49 Financial's reads true. Their source gaps are listed by item 1, not built here.

## Acts only Andrew can do

Reading the sample. FWD-21's DONE WHEN is his read.

-- 1.0.0_SA_CTO~DELL2
