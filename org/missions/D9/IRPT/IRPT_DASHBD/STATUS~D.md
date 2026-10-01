# IRPT_DASHBD workstream F -- status of seat 2.0.0_SA_COO~D (FAST: /closer-drive under lease `IRPT_DASHBD~D`)

Seat `2.0.0_SA_COO~D` (CLAUDE). Contract: PRD `org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md` v0.4 @a8a65b9f62
(ENDPOINT unchanged since @2cb022f549; C-LEASE and ruling 6.7 place F's items on this seat). Reviewer `3.0.0_SA_CVO`
(grades each landed pin after the fact, as DSGN_IRPTV1 pins). Authority: Andrew-direct 2026-10-01 ~04:2xZ, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_042xZ_SELF_DRIVE_60M_LAPTOP_FABRIC_FINAL_SAY_CLOSER_DRIVE_IRPT_FIRST.md`
@c48af273cc (CTO 103442). **As of 2026-10-01T04:5xZ.** This file holds F's claims and next-list; the pins, the landed
table and the screen are in `org/missions/D13/DSGN/DSGN_IRPTV1/STATUS.md` (one seat, one portal checkout).

## Pins

| What | Value |
|---|---|
| Lease | FAST `IRPT_DASHBD~D` until 2026-10-01T12:32:19Z, surface `portal/src/pages/InvestorReporting/tabs/reporting`, `portal/src/pages/InvestorReporting/dashboard`; armed by this seat 04:32:19Z (`org/mcp/drive-mode.log`) |
| Landed for F | `dashboard/coverageWords.ts` (portal `57cf660e`, plan item 3) and `dashboard/windowMath.ts` (portal `63fb6318`, plan item 2); no page mounts either yet |
| Build plan | `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/item44/IRPT_DASHBD_HOP5_BUILD_PLAN.md` |
| Gold contract read | `org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json` 0.1.0 @10939bbfa4 (unchanged by PRD v0.4; the two members v0.4 names, FLOW_UNRECONCILED and NOT_MEASURABLE, are in the contract and in `coverageWords.ts`) |

## Live thread

State: NOT LIVE. FWD-1 hop 5 (the page) has no served file and no read route to read; "any hop fed by a fixture fails
the outcome", so no page is mounted against an invented shape.

## Write claims

- `2.0.0_SA_COO~D`: `portal/src/pages/InvestorReporting/dashboard/*`, `portal/src/pages/InvestorReporting/tabs/reporting/*`.
- Next claim: plan items 1 and 4 (`dashboard/seriesContract.ts`, `dashboard/DashboardPerformance.tsx`).

## Next (in order)

1. Plan item 1, the contract read with its named refusal. Waits on `org/standards/IRPT_DASHBD_SERIES_CONTRACT.json`
   (absent at 04:5xZ). Asked of `2.0.0_SA_COO~P` at 04:33Z: land the file ahead of DB-b-1's gold, since TO-DB-b-2
   `:54-58` already fixes its whole content and it reads no data.
2. Plan item 4, the Performance chart, the same tick item 1 lands.
3. Plan item 5, the per-account switch in `tabs/reporting/ReportingTab.tsx`, plus the one real signed-in run. Waits on
   a served `series.json.gz` and `manifest.json` (TO-DB-b-2) and the read route (TO-DB-b-4), both `pending`.

## Parked (one line each, owner + the condition that un-parks it)

- The FULL -> FAST boundary's one line to the CVO ("FAST from 04:32Z; pins graded after the fact"): owner this seat;
  un-parks when a `3.0.0_SA_CVO` session is live on the laptop (none registered at 04:50Z; a queued line is not a delivery).
- TO-DB-b-1's emit is held at `0.4.0_DS_ClientPlatform~S` pending `2.0.0_SA_COO~P`'s amendments (rows S4, S6, S7) and
  `1.0.0_SA_CTO` on S5: owners as named; it gates DB-b-2's served files, not the contract file.

## Limits

- No task order is cut for F while this lease lives; under FULL, F's orders name only the two paths above (C-LEASE).
- The page's time-to-paint and file-size measurement (PRD row S16) is taken on the real page with the real file, never
  estimated.
