# Portal: what is on DEV and not yet on PROD (for Andrew, open call e7f2) -- 2026-10-11 ~16:3xZ

Read by `1.0.0_SA_CTO~DELL1`: `git log origin/PROD..origin/DEV` in `portal/`, with PROD @37aa1247 and DEV @f00c7b8e or later. That is 126
commits and 126 files (+6,165 / -483), all dated 2026-10-09 to 2026-10-11. Who can open each page is read from `src/App.tsx` route guards and
`src/lib/firmAccess.ts` `FIRM_ALLOWED_PATHS` on DEV.

## CLIENT-FACING (a partner-firm login can open these) -- what you would visually smoke

| page | what changed | project |
|---|---|---|
| **Model Portfolios** `/portfolios` (49 Financial, Inflection, Cottonwood) | The Global trend chart draws its two moving-average (SMA) series as their own bands (1 commit, 10-11). | MDPF_CANON CN-d-3 |
| **Advisor Intelligence** `/advisor-intelligence` (49 Financial, Inflection, Cottonwood) | A new advisor-book FEE PANEL below the household panels shows one billed quarter's fee, computed beside the Schwab debit (quarter 2026Q3). Flows and exclusions read "not computed for this quarter" when absent, never "none" (5 commits, 10-09). | ADVI_BILLING AB-t-3, AB-r-1 |

## OPAL-INTERNAL ONLY (no partner-firm login can open these)

| page | gate | what changed | commits |
|---|---|---|---|
| Investor Reporting `/investor-reporting` | admin + internal + Dev | Report print/export with Opal wording, contract and wire types regenerated, the smoke map, test repairs | 60 |
| Security Analysis `/security-analysis` | internal | Model tab: the team sheet's rows and values (HELD: raw codes and long decimals, AMGT_CORPUS D1-S5); the peers cap header names its unit; the Ticker cell says "no ticker held"; the cross-vintage date sentence; description and news empty-states | 33 |
| Ticket Center `/ticket-center` | internal | Analysis Request: firm chosen from the caller's allowed firms; "Open report" opens the finished report; the request id is recorded on the ticket | 19 |

Also: `src/api` (6, IRPT and billing client methods), `package.json` and `bun.lock` (a test dependency pin).

## Not ready, whatever you decide

The Security Analysis **Model tab** change (`CRPS-av-2`) shows raw data codes as row labels and long decimals. The fix is in flight (AMGT_CORPUS
round 47). It is internal-only, but it should not reach PROD before the fix: a promote either waits for it, or reverts that one commit for
the promote.

## How to look

DEV build locally: `cd portal && bun install && bun run dev --port 5174`, signed in as a 49 Financial test user, at `/portfolios` and
`/advisor-intelligence`. Or open the DEV deployment if you use one.
