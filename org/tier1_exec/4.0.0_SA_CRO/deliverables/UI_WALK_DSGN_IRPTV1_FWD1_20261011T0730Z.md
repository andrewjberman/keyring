# UI walk -- DSGN_IRPTV1 FWD-1 on portal DEV -- 2026-10-11 07:30Z

Order: 1.0.0_SA_CTO msg 108248, relayed by 0.0.0_AB_MSTR msg 108249; for dell2 2.0.0_SA_COO~D2 / 1.0.0_SA_CTO~DELL2
(dell2 msg 4374). Walker: 4.0.0_SA_CRO, `/ui-walk --client "anna thiessen" --performance-state`.
Not acceptance evidence (the /ui-walk skill grades nothing). Hop outcomes only; no client figure is written here.

## Build walked

- Running bundle: `bun run dev:live --port 5174` from worktree `C:/tmp/portal-5174`, detached at origin/DEV
  `ab697ba120a6452bdcb634038d8114b88f18e4a9` (fetched 07:2xZ). Live data and auth through CloudFront; real login.
- Firm selector stayed at its default `Global (All)`.

## Hop outcomes (FWD-1, PRD lines 44-48)

| # | Hop | Outcome | Evidence |
|---|---|---|---|
| 1 | Sign in | PASS | logged in, landed on /market |
| 2 | Open Investor Reporting | PASS | route loaded |
| 3 | Search the client by name | PASS | first match and answer at 1,444 ms (`search-timings.json`) |
| 4 | Pick her Cottonwood brokerage account | PASS | account picker offers `****9237 / Brokerage`; identity card names Cottonwood Capital Advisors |
| 5 | Header identity card | PASS | who, firm, holdings total, as-of date (2026-10-08) and "2 accounts" all render from live reads |
| 6 | Performance: YTD return and spread to benchmark | FAIL | picker label reads "YTD unavailable"; tab state `refusal` at 3,457 ms with the sentence "Performance is not available for this client yet. It becomes available once Opal Capital computes performance for this account." API: `performance/sel_*` -> UNAVAILABLE `OBJECT_NOT_COVERED` (both accounts); `reporting/client/<id>/summary` and `reporting/<acc>/manifest` -> UNAVAILABLE `FIRM_BINDING` |
| 7 | Holdings: Models / SMAs / Client split | PARTIAL | default face splits the total by ACCOUNT (Trust / Brokerage), not by category; the category split (models, SMA, Client) is reached one layer in, by opening an account tile; the Client category dialog renders with its derivation text |
| 8 | Holdings: security list | PASS | securities table with asset-class summary renders for All and for the Brokerage account; sleeve filter lists the Opal models, DIVZ SMA and Client |

FWD-1 verdict from this walk: the thread breaks at hop 6. Performance for this client is refused on the served
reporting/performance reads (`OBJECT_NOT_COVERED`, `FIRM_BINDING`), so YTD return and spread are not on the screen.

## Guard and walk health

- `guard.tsv`: EMPTY -- 0 guard aborts (no write attempted by the page).
- 16 telemetry calls stubbed locally; 7 API issues (all listed in hop 6); 3 console errors (two 401s at login
  before the session was set, one React whitespace-in-table warning on Holdings).
- Walk void: no. Account disarmed at 07:32:57Z; a login with the walk password after disarm was REFUSED (HTTP 401).

## Local artifacts (laptop only, gitignored, never sent)

`C:\Users\AndrewBerman\Desktop\ajb_workspace\tmp\ui-walk\20261011T072958Z\` -- `findings.json`, `guard.tsv`,
`performance-state.json`, `search-timings.json`, `netlog.tsv`, `summary.md`, 25 screenshots. The walker captures
every step automatically, so the screenshots do show client figures; they stay on this laptop.
