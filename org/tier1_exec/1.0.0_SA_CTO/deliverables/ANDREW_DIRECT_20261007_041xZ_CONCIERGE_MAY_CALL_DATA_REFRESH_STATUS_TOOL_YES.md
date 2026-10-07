# ANDREW-DIRECT 2026-10-07 ~04:1xZ -- the Teams concierge identity may call the read-only data-refresh status tool

**Channel:** typed at the `1.0.0_SA_CTO~O` terminal (site Z), ~04:1xZ, answering this seat's `/open-calls` card
(CALL 1 of 1, ~04:1xZ).

## The card, as put

"May the Teams concierge identity call the new read-only status tool? (yes/no)"

REC: "yes. It only issues GETs and fires nothing. Without it the caller confirms a send by reading the portal's
displayed date, which works but is slower. On a yes, one allowlist row is added in a later release."

## Verbatim

> rec approved

## Applied as (verbatim scope, no wider)

- **Authorizes:** one allowlist row. The scoped Teams concierge identity may call `opal_data_refresh_status`, the
  read-only tool that release r25 adds (NFRA_OPLGTW OG-up-1, CTO R33).
- **Does NOT authorize:** any other tool for that identity, any other identity, a grant or state-store write, or a
  change to release r25. The halves on `240ac2fe5a` stand as signed, and condition 6 of the CTO half is met by this
  record for a LATER release only.
- **Route:** `2.0.0_SA_COO~O` cuts the row as one cell and ships it in the release after r25, under the usual three
  halves. The tool maps to no Graph scope, so the concierge's 9-scope consent does not change.
- **Until that release is live,** the concierge's caller confirms a send from the portal's displayed date.

-- 1.0.0_SA_CTO~O
