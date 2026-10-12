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

## ADDENDUM 1 (2026-10-12 ~21:3xZ) -- DEV has grown since this breakdown; what changed for the smoke

Read at 21:3xZ (portal `git fetch`, origin/PROD..origin/DEV): **176 commits, 163 files**, up from 46 and 62 on 10-11. The files by page:

| Page | Files changed |
|---|---|
| Investor Reporting | 111 |
| Ticket Center | 19 |
| Security Analysis | 17 |
| Advisor Intelligence | 5 |
| Model Portfolios | 1 |
| shared `src/api`, `src/lib` and `src/components` | 6 |
| `package.json` and `bun.lock` | 2 |

**Added at the laptop CTO's ask (msg 108679, ruling `CTO_RULING_DELL2_29B7_IRPT_TILES_PROD_PUSH_NOT_YET_FOLDED_INTO_E7F2_20261012.md`):** `183860ba`, dell2's IRPT_BCKEND
value-facts tiles. The Investor Reporting adapter reads `value_facts.start_value` / `end_value`, and the market-value names stay for the Black Diamond path only. Investor
Reporting is OPAL-INTERNAL (gate admin + internal + Dev). It is folded into e7f2 as NOT YET until Andrew smokes the build.

**Client-facing changes since 10-11:** none to the Model Portfolios or Advisor Intelligence page files. Two SHARED changes reach every page:
1. **`53506d49`, `src/lib/firmAccess.ts`:** `FIRM_ALLOWED_PATHS`, the list of pages a partner login may open, is now generated. **Measured: the list is IDENTICAL on PROD
   and DEV** once comments and whitespace are ignored (615 = 615 characters, equal), so no partner gains or loses a page.
2. **`eba86eaf`:** the shared table no longer emits a whitespace text node inside its column group. This is a rendering fix seen on holdings tables. Glance at one
   partner-visible table during the smoke.

**The dependency files (`package.json`, `bun.lock`) changed.** That is the strongest reason to smoke the client-facing pages on the DEV build rather than trust page diffs.

**How to look:** unchanged from the section above, with the two client pages plus one holdings table.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 2 (2026-10-12 ~21:5xZ) -- the IRPT tiles line, as dell2's CTO states it

Per `1.0.0_SA_CTO~DELL2` msg 6599 (relayed by MSTR~DELL1 msg 4580). The source is `CTO_ROUND_ANALYSIS_IRPT_BCKEND_P_ROUND_168_20261012.md` section 3b, on
origin/box/dell2 and not yet on CLOUD. **`183860ba`, as corrected:** the opening and closing value tiles fill on the holdings-basis and Orion answers. **49 Financial is
unchanged: its page shows no tiles.** ADDENDUM 1's adapter description stands. Any earlier "three providers" wording for these tiles is wrong.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 3 (2026-10-12 ~23:3xZ) -- candidate `cf52fdbf` (dell2 DSGN_IRPTV1 round 31) appended

At the laptop manager's ask (bus 9626d218, MSTR~DELL1 msg 4585). DEV moved from `183860ba` to `cf52fdbf`: 11 files, approved by `1.0.0_SA_CTO~DELL2`, CI success, PROD
untouched. COO~D2's checks: typecheck 0, lint 0 errors, Investor Reporting suite 1,216 pass / 27 skip / 1 fail (F14-AC3, which COO~D2 names as the pre-existing base failure).
DEV is now **186 commits and 170 files** ahead of PROD (portal `git fetch`, 23:3xZ).

| change | page | class |
|---|---|---|
| IV-e-120: Total Assets shows its base inside the card | Investor Reporting holdings | OPAL-INTERNAL |
| IV-e-122: a vendor report's face carries its validation sentence and source line | Investor Reporting analysis | OPAL-INTERNAL |
| IV-e-121: rendered proof that an account row picked in the header starts Performance on it | tests only | none |

**One SHARED file:** `src/components/CategoryViewTree.tsx` (+19 lines), which Model Portfolios (client-facing) also renders. The change is an OPTIONAL `totalBase` prop. Absent
means no base line, and **`ModelPortfolios.tsx` on DEV passes `totalBase` 0 times**, so the Model Portfolios render is unchanged by this candidate.

-- 1.0.0_SA_CTO~DELL1
