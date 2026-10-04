# Drive log -- 2.0.0_SA_COO~D, 2026-10-04 00:3xZ-01:2xZ (host andrew)

| Time | Project | Limb | Act | Outcome |
|---|---|---|---|---|
| 00:3xZ-01:0xZ | IRPT_BCKEND Y-5 (~Y 104829) | Aproxy after the cents fix (136ee09e9f) | after site Z's DISARMED: run 1 stopped before any write (the search box was not drawn in 30 s); run 2: UP-58dc023f... NEEDS_CORRECTION -> NORMALIZED, submit REQ-6be454cbb317d96a6e4ba5f8 RECEIVED; the row read LOADING, then UNAVAILABLE from 00:56Z to the 20-minute ceiling; ~Y asked to read the server state | DRIVE FORWARD (routed) |
| 00:3xZ-00:4xZ | DSGN_REBRND W3-S5 (FAST) | /investor-reporting's bare lines | request list loading / failed / empty and the export preview's loading are the designed states; pin request-list-states (DEV fails every arm); signed-in walk `20261004T010454Z` shows the list's LOADING | DRIVE FORWARD |
| 00:4xZ-00:5xZ | DSGN_REBRND W3-S5 (FAST) | /valuations | page loading -> LOADING; Risk Premium failure -> ERROR (it drew white text on the canvas, "Data source: /data/risk_premium_data.json" and the raw error); pin valuation-states; ui-smoke --dist renders looked at | DRIVE FORWARD |
| 00:5xZ-01:0xZ | DSGN_REBRND W3-S5 (FAST) | /valuations' Range panel | "Backend needs to generate ranges data..." (with an emoji) -> EMPTY in words; "(pending)" -> "(no range yet)"; pin arm (e); render looked at | DRIVE FORWARD |
| 01:0xZ-01:1xZ | DSGN_REBRND W3-S5 (FAST) | /correlations | loading -> LOADING; one ticker -> EMPTY inside the matrix panel, whose header keeps the selectors (the tinted notice had removed the only controls); pin correlation-states; renders looked at | DRIVE FORWARD |
| 01:1xZ | both (FAST) | landing | portal DEV `c35c66db` (ls-remote): 8071b59b, e2f89bd9, 7a12098c, c35c66db; pins handed to the CVO | DRIVE FORWARD |
| 01:2xZ-01:3xZ | DSGN_REBRND W3-S5 (FAST) | /data-refresh | the amber "Could not load current data state" band -> PanelError with a retry; that panel and Upload History load as PanelLoading; pin data-refresh-states (DEV fails every arm); ui-smoke render with the manifest forced to a 503 looked at; LANDED portal DEV `a403f466` (ls-remote) | DRIVE FORWARD |
| 01:4xZ-01:5xZ | DSGN_REBRND W3-S5 (FAST) | /security-scanner | three tabs' grey "Loading ... data..." lines -> PanelLoading; pin scanner-loading-states (DEV fails all three arms); ui-smoke render with the factor read held looked at; LANDED portal DEV `a9b7427e` (ls-remote) | DRIVE FORWARD |

## Notes

- DSGN_REBRND's lease surface was widened by the seat (re-arm, same CTO batch 165 authority) to `portal/src/pages/Valuation`
  and `portal/src/pages/Correlation`.
- Every walker use this hour sent ARM and DISARMED to 0.0.0_AB_MSTR. Background runs now use a 30-minute shell limit,
  so the walker's own finally-disarm always runs.

## Open

- W3-S5: /advisor-intelligence and /login spinners; the demo page's silver copy. /portfolios stays parked under MDPF_TAXSMA's lease.
- REQ-6be454cb's server state: ~Y.
- The print's bundle reference on the face: put to Andrew.
