# UI walk -- DSGN_IRPTV1 FWD-1 on portal DEV -- 2026-10-11 09:45Z (re-walk)

Order: dell2 2.0.0_SA_COO~D2 msg 4592, relayed by 0.0.0_AB_MSTR msg 108283 (acked). Walker: 4.0.0_SA_CRO,
`/ui-walk --client "anna thiessen" --performance-state`, the same client and flags as the 07:30Z walk
(`UI_WALK_DSGN_IRPTV1_FWD1_20261011T0730Z.md`). The walk ran once and made one fresh request; nothing was repeated.
Not acceptance evidence (the /ui-walk skill grades nothing). Hop outcomes only; no client figure is written here.

## Build walked

- Running bundle: `bun run dev:live --port 5174` from worktree `C:/tmp/portal-5174`, detached at origin/DEV
  `ff4189475984dc8ba0b8039cddf2eb2eb58e2f24` (fetched 09:4xZ; `bun install` run for the package.json delta). Live data
  and auth through CloudFront; real login.
- The firm selector stayed at its default, `Global (All)`.

## Hop outcomes (FWD-1)

| # | Hop | Outcome | Change vs 07:30Z | Evidence |
|---|---|---|---|---|
| 1 | Sign in | PASS | same | logged in, landed on /market |
| 2 | Open Investor Reporting | PASS | same | route loaded |
| 3 | Search the client by name | PASS | same | first match at 849 ms, answered at 1,258 ms (`search-timings.json`) |
| 4 | Pick the Cottonwood brokerage account | PASS | same | the picker offers `****9237 / Brokerage` |
| 5 | Header identity card | PASS | same | who, firm, holdings total, as-of date (2026-10-08) and "2 accounts" render |
| 6 | Performance: YTD return and spread to benchmark | PARTIAL | was FAIL | see below |
| 7 | Holdings: Models / SMAs / Client split | PARTIAL | same | the default view still splits the total by ACCOUNT (Trust / Brokerage); the Models / Client category split appears only after opening an account tile |
| 8 | Holdings: security list | PASS | same | the securities table and asset-class summary render; the sleeve filter lists the Opal models, DIVZ SMA and Client |

### Hop 6 detail

- Tab state: `body` at 5,250 ms (was `refusal` at 3,457 ms). The account picker now prints a YTD figure for BOTH
  accounts (it read "YTD unavailable" before).
- The fallback the code predicts is now OBSERVED. `reporting/<acc>/manifest` is still refused for both accounts and
  `reporting/client/<id>/summary` is still refused (`UNAVAILABLE FIRM_BINDING`). The tab then renders from
  `performance/sel_*`, which answers `PARTIAL PERFORMANCE_PARTIAL` (2 GETs per selection, both PARTIAL). Report details
  read "Partial -- Qualified answer, not a complete report", with the source given as Black Diamond.
- YTD return: ON SCREEN, but it covers the wrong window. YTD requested 2026-01-01..2026-10-08, but the source answered
  2026-05-29..2026-10-08, and the page says so ("The source answered a different window from the one requested").
  The figure on screen is a return since May 29, not a calendar-year YTD.
- Spread to benchmark: NOT ON SCREEN -- "No benchmark supplied for this window. Spread not supplied for this window."
- 'Vs benchmark' tile: renders as "Vs benchmark: not supplied". Ending value and beginning value are also "not
  supplied", and the accounts table prints Account and Ending value as "not supplied".
- Typed vendor refusal: NONE. Nothing indicates a stale stored session.
- Trust account: the body was read in full (the cumulative-return chart and a 92-observation daily series). Brokerage
  account: the picker shows its YTD and its API read answered PARTIAL, but the walker's screenshot caught the body
  still at "Loading", so the Brokerage body was not seen.
- Noted, not chased: on the Holdings tab, the same `performance/sel_9fd8...` selection that answered PARTIAL on the
  Performance tab answered `UNAVAILABLE OBJECT_NOT_COVERED`.

FWD-1 verdict from this walk: hop 6 no longer breaks. A return now reaches the screen through the /performance
fallback. Hop 6 is not met as written, though: the window is May 29 onward rather than YTD, and the spread and the 'Vs
benchmark' tile are "not supplied". Hop 7 is unchanged (PARTIAL).

## Guard and walk health

- `guard.tsv`: EMPTY -- 0 guard aborts (1 byte, no rows).
- 13 unique findings from 54 observations, 26 screenshots, 16 telemetry calls stubbed, 7 API issues (all listed under
  hop 6, plus the Holdings item), 3 console errors (two 401s at login before the session was set, and the same React
  whitespace-in-colgroup warning on Holdings).
- Walk void: no. The account was disarmed at 2026-10-11T09:47:58Z; a login with the walk password after the disarm was
  REFUSED (HTTP 401).

## Local artifacts (laptop only, gitignored, never sent)

`C:\Users\AndrewBerman\Desktop\ajb_workspace\tmp\ui-walk\20261011T094454Z\` -- `findings.json`, `guard.tsv`,
`performance-state.json`, `search-timings.json`, `netlog.tsv`, `summary.md`, 26 screenshots. The screenshots show
client figures and stay on this laptop.
