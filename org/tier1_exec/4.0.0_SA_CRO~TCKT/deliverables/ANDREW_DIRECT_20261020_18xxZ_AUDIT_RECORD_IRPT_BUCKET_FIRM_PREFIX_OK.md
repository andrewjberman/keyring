# ANDREW_DIRECT 2026-10-20 ~18:2xZ -- the audit record may live in the IRPT bucket under the firm prefix

Channel: Claude Code session, seat 4.0.0_SA_CRO~TCKT (box dell2), Andrew's answer to a single-choice question this seat
asked after CTO msg 11486 (PRD v0.28 @ea3014a892).

Question, verbatim as shown to him:

> The audit record (one structured file per analysis request) was going to live in each firm's own bucket, as you said.
> The CTO has moved it to the shared Investor Reporting bucket, in a separate folder per firm
> (opal-data-irpt/irpt/<firm>/platinum/analysis_audit/). Its reason: the server that generates reports is blocked from
> writing to firm buckets, and every other report file already lives this way. Is that OK?

Options shown:
- "OK, per-firm folder (Recommended)": each firm keeps its own folder inside the shared Investor Reporting bucket,
  alongside the report PDFs and the other report files. Nothing new to unblock.
- "No, each firm's own bucket": the record must sit in each firm's own bucket. This needs a new permission for the
  report server to write there, plus the usual signed change, which delays the audit record.

**His answer, verbatim:** "OK, per-firm folder (Recommended)".

Effect: his earlier "an analysis-report folder in each firm's bucket" (@f2581e90b9) is satisfied by
`opal-data-irpt/irpt/<firm>/platinum/analysis_audit/` at a builder-made address (C-AUDIT-RECORD, PRD v0.28).
