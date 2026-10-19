# Andrew-direct 2026-10-19 ~14:2xZ -- promote all dell2 portal work to PROD

**Received at:** `1.0.0_SA_CTO~DELL2` terminal. **VERBATIM:**

> "I want to make sure that all the work that has been done on this device on the opalinvest.dev portal repo is actually
> pushed to PROD, we need to make sure that the portal is updated with all work that has been done on this device, as I
> just went into our CFO office to demo the ticket center analysis request flow, and it is not the most recent version.
> Let's get that done now."

This is his word for a client-facing PROD push (CLAUDE.md, Agent Autonomy, portal PROD exception).

## Measured at receipt (portal, fetched ~14:2xZ)

origin/DEV is f7074536 and origin/PROD is d729ee6d (portal-v2.1.235). The content diff PROD to DEV under `src` is 53 files
(+7,630 / -488). It splits as follows:

| group | files | device | in his word? |
|---|---|---|---|
| **Ticket Center analysis request** (`AnalysisRequestParts.tsx`, `analysisRequest.ts`) | 0 differing | -- | already equal on PROD |
| Ticket Center meeting request (`MeetingRequestParts.tsx`) | 0 differing | -- | already equal on PROD |
| **Investor Reporting** (Performance tab template, performance report and export, holdings panels, chart breaks; IRPT_DASHBD DB-b-176 to DB-b-316) | 43 (code and tests) | dell2 | **YES**: promote |
| **Trade Request form** (`TradeRequestParts.tsx`, `tickets.ts` upload door, `TicketCenter.tsx` wiring, trade tests) | 5 | dell2 (TCKT_VNEXT) | **HELD BY NAME**: his 2026-10-17 hold, "we should not push this til we actually have a functioning channel for that". This word does not name it, so it is not lifted; asked. |
| MDPF_CANON (`cottonwoodTrend.ts`, `trendGrouping.ts`, `ModelPortfolios.tsx`), AMGT_RESAPP harness | 5 | dell1 | NO: not this device's work |

Also not on DEV or PROD: `cand/dell2/anlreq-commentary-always-requested`. It stays off PROD until a commentary PDF opens
(ruling `RULING_COMMENTARY_GAP_TWO_CAUSES_20261017.md`). Shipping it now would give every new ticket a commentary link that
refuses. He is told so plainly.

## Acts

1. `2.0.0_SA_COO~D2` (the IRPT_DASHBD issuer) cuts ONE PROD-based recut branch carrying the Investor Reporting set
   (cherry-picks onto origin/PROD; no Trade Request, no dell1 file). Its gates:
   - typecheck 0;
   - eslint 0;
   - the Investor Reporting and Ticket Center tests no worse than DEV;
   - the vite build green;
   - a payload check listing every file and its source commit.
2. The approval row is closed on THIS record (`--ruled-by andrew`).
3. `0.4.0_DT_ClientPlatform~DELL2` promotes it by `/prod-deploy`, then runs the standing tree-equal fold of PROD into
   DEV (0 files).
4. The receipt names the pages changed and their class: Investor Reporting > Performance tab, client-facing.
