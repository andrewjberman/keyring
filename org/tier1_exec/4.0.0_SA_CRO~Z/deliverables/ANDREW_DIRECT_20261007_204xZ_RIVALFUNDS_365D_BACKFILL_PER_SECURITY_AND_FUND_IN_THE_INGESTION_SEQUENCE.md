# ANDREW-DIRECT 2026-10-07 ~20:4xZ (4.0.0_SA_CRO~Z terminal, site Z) -- rivalfunds: 365d backfill per security and per tracked fund, built into the ingestion sequence

Given in-session at the `4.0.0_SA_CRO~Z` terminal, two messages, the second while the first was being worked.

## His words, VERBATIM AND ENTIRE

First:

> "Something I am noticing that we are going to need to figure out is that for the rivalfunds product, we kind of need to be storing 365d calendar backfill per security AND *per tracked fund*, as those securities appear in the daily transactions record. What are we doing to manage that process at this time? WE need a solution for that built into the ingestion sequence"

Second:

> "when you figure it out, send the analysis over to CTO~Z and they can figure out where this fits into the existing ETFS_RIVALS workstream and fold it in with COO~RV"

## What it states, at the width written

| His sentence | Reading |
|---|---|
| "storing 365d calendar backfill per security AND *per tracked fund*, as those securities appear in the daily transactions record" | The store holds 365 calendar days of history for a security, and for a tracked fund, from the point the security shows up in the daily transactions record. |
| "What are we doing to manage that process at this time?" | A question. Answered by measurement in `RIVALFUNDS_365D_BACKFILL_IN_INGESTION_ANALYSIS_20261007.md`, beside this file. |
| "WE need a solution for that built into the ingestion sequence" | The solution is part of the ingestion sequence, not an ad hoc act. |
| "send the analysis over to CTO~Z and they can figure out where this fits into the existing ETFS_RIVALS workstream and fold it in with COO~RV" | `4.0.0_SA_CRO~Z` sends the analysis to `1.0.0_SA_CTO~Z`. `1.0.0_SA_CTO~Z` places it in ETFS_RIVALS with `2.0.0_SA_COO~RV`. |

## Not said, or left open (stated so nothing is read into it)

- **"per tracked fund" has two readings**, and he did not choose: (a) each tracked fund's own holdings history reaches back
  365 days; (b) the 365 days are kept per (fund, security) pair, counted from that fund's first trade in the security.
  A third, the fund's own share-price series, is possible. The analysis states which of these the store meets today.
- He names no vendor. His 2026-10-07 ~05:1xZ word (PRD ADDENDUM F) authorised an AD HOC Bloomberg backfill "for the
  rivalfunds funds only". Whether this message is his word for a STANDING, scheduled Bloomberg pull is not decided
  here; it goes to `1.0.0_SA_CTO~Z` as a call.
- Nothing here changes a hard stop, a never-widen rule, the Bloomberg budget, or the order of acts in the project's
  STATUS.md.

## Acts taken on it, same turn

- The analysis written and sent to `1.0.0_SA_CTO~Z` (one message, the file path).
- No Bloomberg call, no S3 write, no code change by this seat.
