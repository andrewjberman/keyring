# ANDREW-DIRECT 2026-09-30 ~18:3xZ at the 4.0.0_SA_CRO terminal -- MDPF_TAXSMA E2b: carry the last complete Tax figure on an unknown day; Tax enters the series from its first observed day

**Author:** 4.0.0_SA_CRO (Chief Research Officer)
**Channel:** Andrew typed at this seat's terminal, answering the two decisions this seat put to him (STATUS.md
Parked row @f40d20512d and the report that followed it).

## The two questions, as put

1. On a day Tax cannot be read (Gateway sign-in lapses, sheet unreadable): the contract's
   `categories.incomplete_rule` makes the 49 Financial and Global totals "unavailable" that day. This seat
   RECOMMENDED instead: show the last complete Tax figure, labelled with its date.
2. History: Tax enters the served series from its first observed day, with no backfill; the 49 Financial chart
   steps up by about $17M on activation day.

## Verbatim

> "Go with your recommendation on both, keep going"

## What the word does

- **Rule 1 (carry):** on a valuation date on or after Tax's first complete observation where Tax is not complete,
  the served 49 Financial and Global totals include the most recent COMPLETE Tax figure, and the Tax coverage
  says so: `value_status` stays the day's honest status, `last_complete_date` names the carried figure's date,
  `tax_value_basis` reads `CARRIED_LAST_COMPLETE`. This amends contract 0.6.0 `categories.incomplete_rule` for the
  served totals only; the Tax leaf still shows the day's own status.
- **Rule 2 (no backfill):** dates before Tax's first complete observation carry the pre-Tax base, with coverage
  `NOT_OBSERVED` / `BEFORE_FIRST_OBSERVATION`. No earlier date is reconstructed.

## Not authorized by this word

PROD promotion; the never-widen sign-off at activation (still CTO + COO halves); any served-key move.
