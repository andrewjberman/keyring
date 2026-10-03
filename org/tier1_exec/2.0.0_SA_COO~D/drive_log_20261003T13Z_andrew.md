# Drive log -- 2.0.0_SA_COO~D, 2026-10-03 13Z (host andrew)

| Time | Project | Limb | Act | Outcome |
|---|---|---|---|---|
| 12:5xZ-13:0xZ | DSGN_REBRND (FAST; IR lines still blocked: P-3/P-6 wait ~P's P-2 window, Case A waits ~Y) | round 3 E3, row W3-S4 | /portfolio-management: no computed zeros without a portfolio, one ERROR for a failed service: portal `c3e1d7b9` on origin DEV (ls-remote 13:04Z) | DRIVE FORWARD |
| 13:0xZ-13:1xZ | DSGN_REBRND (FAST; IR still blocked on ~P) | round 3 E3, row W3-S4 | /ticket-center says a failed load inside the board: portal `3d8cce99` on origin DEV (ls-remote 13:16Z) | DRIVE FORWARD |
| 13:1xZ-13:3xZ | DSGN_REBRND (FAST; IR still blocked on ~P) | round 3 E3, row W3-S4 | /data-refresh History and Emergency Rollback say a failed history read: portal `30f7fca1` on origin DEV (ls-remote 13:33Z) | DRIVE FORWARD |

## W3-S4 on /portfolio-management

- Re-measured on DEV 94c055e8 (ui-smoke on the restarted 5174, auth stubbed; netlog: `/api/private/portfolio/funds`
  and `.../autosave/PFDE/_` answered 401): every Optimized cell read 0.00 and nothing named the failure.
- Cause: with no portfolio loaded, `optimization.summary` is all zeros and the header drew them; the page read neither
  the fund list's nor the autosave read's `isError`. The fund picker's built-in fallback list is a designed fallback
  and is kept.
- Fix: the header shows the placeholder for every figure until a portfolio is loaded, and one PanelError (with a
  hint naming the fallback list and the unavailable resume) when either read failed.
- Pin `PortfolioManagement/components/summary-states.test.tsx` (negative control on HEAD: 0.00 x28, no error). Real run
  under the 401 and a live positive control (walk `20261003T130059Z`: no error line, Resume offered).
- An em dash typed into the pin's comment was replaced with words before commit (no non-ASCII added).

## W3-S4 on /ticket-center

- Re-measured on DEV c3e1d7b9 under the 401: a canvas error carrying the raw response body above a board reading "No
  open tickets.".
- Fix: the board's own `loadError`, one PanelError in the board (Try again; cause via innermostCause, `causeAt="data"`);
  the list is cleared on failure; the page-level error stays for actions. No pin (fetch effect); the 401 render and
  the live walk `20261003T131333Z` (served empty list, metrics of 11 tickets) are the checks.

## W3-S4 on /data-refresh

- Re-measured on DEV 3d8cce99 under the 401: History "No History Yet"; the same empty list drives Emergency Rollback's
  "No successful upload found in history -- there is nothing to restore to." (seen in code, then rendered after the
  fix in its error form).
- Fix: `historyError` in the page hook (the toast-only failure dropped); History and Emergency Rollback each show one
  PanelError with Try again; Rollback offers no restore without a target, as before; rollback logic untouched.
- 401 renders of both tabs and a live walk (`20261003T133002Z`, reads only) listing the real executions.

## Still open on W3-S4

- /advisor-intelligence (several of its files sit in 2.0.0_SA_COO~M's MDPF_SECCLASS lease).
- /market: a missing period change read as 0; RSIModal's own 50 defaults.
