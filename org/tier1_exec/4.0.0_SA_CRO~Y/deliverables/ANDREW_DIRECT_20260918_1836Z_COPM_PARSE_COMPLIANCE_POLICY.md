# ANDREW-DIRECT 2026-09-18 ~18:36Z -- COPM parsing solution, Desktop/compliance_policy

**Channel:** Claude Code terminal, seat `4.0.0_SA_CRO~Y`, mid-turn user message during startup.
**Recorded:** 2026-09-18 18:36Z (the message landed ~35 min earlier, during /watcher).

## Verbatim

> "C:\Users\Opal Bloomberg\Downloads\Opal Capital COPM_12.11.2025.pdf" I want you to come up with a parsing solution for this document so we can adequately chunk it
> in a folder on desktop we'll call compliance_policy.

## Scope as read (surfaced, not adjudicated)

A deliverable request to this seat: a reusable parser for the Compliance and Operating Procedures
Manual PDF, and its chunked output in `C:\Users\Opal Bloomberg\Desktop\compliance_policy`.
No fabric project, no register row, no other seat's lane touched. The output folder is OUTSIDE the
repo corpus (Desktop), so nothing is committed except this record.

## Delivered

- `C:\Users\Opal Bloomberg\Desktop\compliance_policy\parse_copm.py` -- PyMuPDF parser (no other dependency).
- `chunks/` (431 markdown chunks with YAML front matter), `chunks.jsonl`, `sections.json`,
  `toc.json`, `COPM_full.md`, `manifest.json` (source SHA-256 `ae5928e2bfca...`), `README.md`.
- Validation (in manifest.json): TOC entries found 377 of 377, each on the printed
  page the TOC claims; chunk chars vs body chars EQUAL; oversize chunks
  0; verdict OK.

## Source-document findings (for Andrew / the CCO; not parser defects)

- Section 19 ETF Rule 6c-11: summary box has the five labels and no values.
- Section 17.1.4 Board Reporting: only the sub-label "Adviser Responsibility", no text.
- 14.8.6.3 Maintenance of Records is mis-numbered (it sits under 14.5.6).
- Appendix G Fee Billing Audit Spreadsheet (printed p.230) is blank: title only.
