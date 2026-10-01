# IRPT_DASHBD workstream F -- status of seat 2.0.0_SA_COO~D (FAST: /closer-drive under lease `IRPT_DASHBD~D`)

Seat `2.0.0_SA_COO~D` (CLAUDE). Contract: PRD `org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md` v0.4 @a8a65b9f62
(ENDPOINT unchanged since @2cb022f549; C-LEASE and ruling 6.7 place F's items on this seat). Reviewer `3.0.0_SA_CVO`
(grades each landed pin after the fact, as DSGN_IRPTV1 pins). Authority: Andrew-direct 2026-10-01 ~04:2xZ, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_042xZ_SELF_DRIVE_60M_LAPTOP_FABRIC_FINAL_SAY_CLOSER_DRIVE_IRPT_FIRST.md`
@c48af273cc (CTO 103442). **As of 2026-10-01T10:4xZ.** This file holds F's claims and next-list; the pins, the landed
table and the screen are in `org/missions/D13/DSGN/DSGN_IRPTV1/STATUS.md` (one seat, one portal checkout).

## Pins

| What | Value |
|---|---|
| Lease | FAST `IRPT_DASHBD~D` until 2026-10-01T12:32:19Z, surface `portal/src/pages/InvestorReporting/tabs/reporting`, `portal/src/pages/InvestorReporting/dashboard`; armed by this seat 04:32:19Z (`org/mcp/drive-mode.log`) |
| Landed for F | `tabs/reporting/ReportingTab.tsx`: a refused account focus is worded, never left on Loading (portal `353b93dd`, DSGN_IRPTV1 item 60; this lease holds `tabs/reporting`); `dashboard/coverageWords.ts` on gold contract 0.2.0 (portal `2879d65b`, origin DEV by ls-remote 09:16Z; CI green, run 36841567281); before it plan item 3 `dashboard/coverageWords.ts` (portal `57cf660e`), item 2 `dashboard/windowMath.ts` (`63fb6318`), item 1 `dashboard/seriesContract.ts` (`7c354824`), item 4 `dashboard/DashboardPerformance.tsx` (`772dcdd8`, origin DEV by ls-remote 05:12Z); no page mounts the chart yet |
| SERIES contract read | `org/standards/IRPT_DASHBD_SERIES_CONTRACT.json` 0.1.0 @b80543a03c (landed by 2.0.0_SA_COO~P on this seat's ask; pin iv-e-124 binds the page's key lists to it) |
| Build plan | `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/item44/IRPT_DASHBD_HOP5_BUILD_PLAN.md` |
| Gold contract read | `org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json` 0.2.0 @6a23aee53d (blob a335e10efb): `guard_state` added (five members), HOLDINGS_INCOME_FALLBACK removed from `return_basis`; `coverageWords.ts` matches it member for member (pin iv-e-120, 6 axes, 17 sentences) |

## Live thread

State: NOT LIVE. FWD-1 hop 5 (the page) has no served file and no read route to read; "any hop fed by a fixture fails
the outcome", so no page is mounted against an invented shape.

## Write claims

- `2.0.0_SA_COO~D`: `portal/src/pages/InvestorReporting/dashboard/*`, `portal/src/pages/InvestorReporting/tabs/reporting/*`.
- Next claim: plan item 5 (`tabs/reporting/ReportingTab.tsx`, the per-account switch).

## Next (in order)

1. Plan item 5, the per-account switch in `tabs/reporting/ReportingTab.tsx` (C-SHADOW, ruling 6.9: this figure INSTEAD of
   IRPT_BCKEND's for an account whose manifest serves, never both), plus the one real signed-in run that prints the time
   to the painted chart beside the file's size. Waits on a served `series.json.gz` and `manifest.json` (TO-DB-b-2) and the
   read route (TO-DB-b-4), both `pending`.
2. ~~Gold contract 0.2.0~~ LANDED (portal `2879d65b`): the member dropped, the `guard_state` words added.
3. When the SERIES contract carries a guard field (today 0.1.0 @b80543a03c, blob 542fc836b3, none), `dashboard/seriesContract.ts` and
   `DashboardPerformance.tsx` read it and say the `guard_state` sentence beside the day; pin iv-e-124 fails the tick
   that contract version is committed, which is the trigger.

## Parked (one line each, owner + the condition that un-parks it)

- ~~The FULL -> FAST boundary's one line to the CVO~~ CLOSED as moot at 09:43Z: 3.0.0_SA_CVO has graded F's pins
  after the fact since 06:21Z (@bc8413dbd8), so it holds the fact the line would carry.
- TO-DB-b-1's emit is held at `0.4.0_DS_ClientPlatform~S` pending `2.0.0_SA_COO~P`'s amendments (rows S4, S6, S7) and
  `1.0.0_SA_CTO` on S5: owners as named; it gates DB-b-2's served files, not the contract file.

## Limits

- No task order is cut for F while this lease lives; under FULL, F's orders name only the two paths above (C-LEASE).
- The page's time-to-paint and file-size measurement (PRD row S16) is taken on the real page with the real file, never
  estimated.
