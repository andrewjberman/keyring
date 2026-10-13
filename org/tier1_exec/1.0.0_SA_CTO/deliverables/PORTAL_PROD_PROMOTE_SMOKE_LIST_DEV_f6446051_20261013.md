# Portal PROD promote -- the smoke list for Andrew's localhost read (card 9, 2026-10-13)

**Build:** portal `origin/DEV` @`f6446051`, detached worktree `C:\dev\portal-smoke-5174`, `bun run dev --port 5174 --strictPort`,
http://localhost:5174 answers 200 (this seat's curl). The API calls proxy to the same CloudFront the DEV portal uses (`vite.config.ts:64`).
**Delta:** `origin/PROD` @`37aa1247` -> DEV is 163 commits, all of which `/prod-deploy` ships. Files under `src/`, by page:
InvestorReporting 143, TicketCenter 19, SecurityAnalysis 17, AdvisorIntelligence 5, api 3, lib 2, ModelPortfolios 1, components 2.
**Order:** `ANDREW_DIRECT_20261013_122xZ_ANSWERS_TO_NINE_DELL2_CARDS.md` card 9; the promote is open call `dell1-20261011T033643Z-e7f2`.

Sign in as yourself. Each line: where, what to do, and PASS when.

## 1. Investor Reporting (client-facing; 143 files)

1. **Holdings value tiles** -- pick an Inflection client. PASS: the start and end value tiles show figures, and Holdings names the
   account it covers. 49 Financial: no value tiles, which is expected and unchanged.
2. **Account pick carries over** -- pick an ACCOUNT in the header, open Performance, then Holdings. PASS: both open on that account.
   Holdings shows its Models / SMAs / Client split.
3. **Holdings table footnote** -- PASS: one sentence says how much of the total sits in sleeves the table does not itemise.
4. **No firm selected** -- clear the firm in the header. PASS: "No firm is selected in the header" (not a mismatch error).
5. **Vendor (Black Diamond) report** -- open one. PASS: every card has a plain title, never a raw code; a vendor-only card shows one
   plain sentence of reason; the validation sentence and source line sit on the face.
6. **Opal report print/export** -- print one. PASS: no vendor wording appears.
7. **Six asset classes** -- PASS: the class breakdown shows six classes and no "multi_asset".
8. **Added 17:4xZ: search by an account's last four digits** (IB-pr-515, live on the shared search function since 17:35Z). In the
   header's client search, type the last four digits of an account you can see. PASS: that account itself appears as a result,
   showing its masked number, and picking it opens on that account. Two accounts sharing the digits show as two results.

## 2. Ticket Center (client-facing; 19 files)

1. **Queue** -- PASS: each waiting ticket shows its age in hours (up to 72h).
2. **Analysis Request form** -- open it. PASS: the firm answer is a list of the firms you may use, and the Opal models appear as
   checkboxes plus an "Other ETFs" field. Do not submit.
3. **Upload answer** -- PASS: a refused upload shows words (for example SHEETS_NOT_READ explained), raw codes only inside a closed
   Details.
4. **Open report** on a finished ticket -- PASS: it opens the finished report in Investor Reporting's layout, not the request record.
5. **Trade Request form** -- PASS: it is present for the trade_request type. Do not submit.
6. **Final commentary** -- PASS: the ticket shows who sent it.

## 3. Advisor Intelligence (client-facing; 5 files)

1. **Amended 13:4xZ.** Andrew's smoke found the new 2026Q3 fee panel empty ("Fee detail is not available for this quarter"). Its
   mount is reverted in candidate `f6ef1d25` (branch `cto-dell2-revert-29b18a8c`), which the 5174 build now serves; the component
   stays. Open an advisor's book client detail. PASS: no new fee panel, and the existing Fee Summary shows its figures.

## 4. Model Portfolios (client-facing; 1 file)

1. Global trend. PASS: the two SMA series draw as their own bands.

## 5. Security Analysis (Opal-internal; 17 files)

1. Open any name. PASS: the empty-state card shows one plain line; the Model tab opens on a summary; the news list shows each headline
   once; the timeline draws a price line; the peers table has readable tickers.

## Grading

Any line that errors, shows a raw code outside Details, or shows another firm's data is a FAIL: reply with the line number, and the
promote waits. All PASS: reply "pass", and this seat routes `/prod-deploy` to the DT seat under call e7f2 (it merges all 163).

-- 1.0.0_SA_CTO~DELL2
