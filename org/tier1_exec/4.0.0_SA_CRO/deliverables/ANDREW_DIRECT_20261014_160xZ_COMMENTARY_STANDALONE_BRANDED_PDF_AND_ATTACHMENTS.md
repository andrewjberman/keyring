# ANDREW DIRECT -- the commentary is a standalone branded PDF; the holdings file and the form selections are each an attachment (2026-10-14 ~16:0xZ)

**Channel:** Andrew, at the dell2 terminal, in the session of `4.0.0_SA_CRO~DELL2`. He was answering this seat's question R2 (review
`L4R_REVIEW_IRPT_ANLREQ_v0.6_BRIEF_HALF_20261014.md`@6f40d4010f). The question had two parts:
- (1) is the commentary attachment a standalone branded Opal PDF, or the package PDF (the Opal report with a commentary page inside)?
- (2) does "the form as filled" stay as an attachment?

He also approved this seat's offer of a read-only price-coverage read.

**Verbatim:**

> 1.) Yes it should be a standalone branded PDF. If you mean the original holdings csv as the "form" then yes that is an attachment. If you mean the results from the form selection on the ticket issuance, yes that is also a standalone attachment. 2.) Yes do it.

## What it sets (surfaced, not adjudicated)

The AI investment commentary is a **standalone branded Opal PDF**. It is not the package PDF with a commentary page inside, and not a
text draft. The open ticket's attachments are four standalone items:
1. the advisor's original holdings CSV/XLSX;
2. the form selections made at ticket issuance;
3. the YCDGEN-generated Opal report;
4. the AI commentary as a standalone branded Opal PDF.

## What it touches

- IRPT_ANLREQ PRD v0.9:
  - FWD-1 item (4), "the AI commentary draft";
  - the line "the branded Opal PDF with the commentary inside is a later enrichment, not FWD-1";
  - BRIEF COVERAGE row 8;
  - backlog item 6;
  - FWD-3.
- The /closer trace @6766f4486d, hops 15 and 19:
  - no standalone commentary PDF renderer exists (the drafter writes JSON text; `opal_packager.py` renders only the combined package
    PDF);
  - the ticket page has no commentary reader.

-- recorded by 4.0.0_SA_CRO~DELL2
