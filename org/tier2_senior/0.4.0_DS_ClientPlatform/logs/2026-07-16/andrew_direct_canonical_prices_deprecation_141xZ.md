# ANDREW-DIRECT: canonical-prices schema unnecessary on RPS-snapshot holdings; transaction-based pricing DEPRECATED; transactions stay for NNA

**Channel:** direct terminal message into the 0.4.0_DS_ClientPlatform~A session (mid-turn,
during the A4 F-AMT fix window) | **Time:** 2026-07-16 ~14:1xZ | **Received by:** 0.4.0_DS_ClientPlatform~A
**Recorded + broadcast same turn per org/XXX.md (COO + CTO + MSTR). SCOPE IS SURFACED, NOT
ADJUDICATED by this lane.**

## VERBATIM (message 1)

> "Yes also this is a key feature here. The concept of canonical prices as a whole only
> mattered because we had to reprice based on transactions so we needed to establish a
> historical price matrix. If we are moving to just .rps snapshots daily for holdings, that
> entire schema is unnecessary. This is part of the refactoring plan, where we can do this
> much more efficiently rather than being indebted to this transaction pricing schema"

## VERBATIM (message 2)

> "We do want transaction record to assist in NNA analysis, but any kind of transaction-based
> pricing framework is deprecated and we should not be doing that."

## Context at receipt (facts only, for the scope reading downstream)

- Arrived during the OPAL_GLDRNS.A4 window, immediately after the F-AMT fix chain landed
  (95b966545) -- the C_03/C_00 work it arrived beside uses dim_transaction for FLOWS ONLY
  (NNA/income/fees classification); in-kind transfer legs are valued row-price-else the
  POSITION STATEMENT's own closing_price (dim_position, RPS-derived) -- no historical price
  matrix in the new-runner graph today.
- Direct bearing to surface at the CTO gate: **A4 L3 (the M4 canonical-prices promotion --
  "builder becomes a NAMED C-group unit, pct_priced derives from its coverage")** and the
  M1/M6 signed cells' `pct_priced` references (WAVE3_SPEC 065e0e289); also casebook Entry 5's
  R3 "pricing + coverage -> M4 promotion" re-home line. Whether L3 is retired, reshaped to a
  statement-price coverage measure, or something else is the OWNER'S call, not this lane's.
