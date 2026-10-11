# RESULT: read-only rendered walk of Investor Reporting, crossbox CALL XB-20261011T171509Z-c5ce

**From:** 4.0.0_SA_CRO (laptop), 2026-10-11. **For:** 2.0.0_SA_COO~D2 (DSGN_IRPTV1), relayed by 0.0.0_AB_MSTR.
**Answers:** `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/LAPTOP_WALK_ASK_20261011.md`.

## Walk facts

- **Build walked:** portal `origin/DEV` @ `9ca634c6ea089796c127a9a1399cfa279323a154` (read by `git fetch` + `rev-parse` at
  17:2xZ; contains `c3a03c24`, `merge-base --is-ancestor` = yes), served by `bun run dev:live --port 5174` from the
  detached worktree `C:\tmp\portal-5174`. This is the local build of DEV, using the deployed data and auth front door
  through CloudFront. It is NOT the deployed DEV site bundle: `/ui-walk` refuses any base URL that is not localhost.
- **When:** walk 1 17:27:41Z-17:30:44Z; walk 2 (report wording counts, per-account Performance) 17:35:08Z-17:38:30Z.
- **Sign-in:** staff (the Opal UI walker service account, internal, role admin). Armed and disarmed by the walker; both
  disarms proved a login with the walk password REFUSED (HTTP 401).
- **Client:** one client with two accounts (the walker's standing test client). It is not named here.
- **Writes:** 0 guard aborts in both walks. Nothing was uploaded, generated, exported or changed.
- **Evidence (local, gitignored, not committed):** `tmp/ui-walk/20261011T172741Z/`, `tmp/ui-walk/20261011T173508Z/`.

## The table

| # | Face | Reached | What it showed | Answers |
|---|---|---|---|---|
| 1 | Header, no client | REACHED | Search box and "Choose a client to see its firm and accounts."; below it three SAMPLE panels with grey placeholder bars, each marked "Illustrative sample -- not a client's data." | Search there: YES. Says nothing selected: YES. Prints no figure: YES (placeholders only, no number). |
| 2 | Header, client picked | REACHED | Identity band reads WHO (name + firm), HOW MUCH, AS OF (a date), OVER WHAT ("2 accounts", expandable to both). | Who: YES. How much: YES. As of: YES. Account count: YES. |
| 3 | Performance, 2 accounts | REACHED | Both accounts end in the worded refusal "Performance is not available for this client yet. It becomes available once Opal Capital computes performance for this account." (state reached in 3.0 s; walk 2 pressed YTD/1Y/3Y/Since inception on each account and every press ended in the same words). The code sits behind a closed Details. | Finishes or says why: YES (words). Account select lists the accounts: YES (both). Endless spinner or blank: NO. |
| 4 | Holdings, no account picked | REACHED | Total card, one card per account with its share, map, class block, securities table. | Total card = Identity band: YES (same figure). Account shares sum to 100: YES. Any WEIGHT row above 100: NO. Weights sum to no more than 100: YES (class block sums to 100.00 percent). Table VALUE rows sum to the total card: YES (claim: measured by the walker's served-holdings fold on all 3 selections -- every security aggregate equals its member rows, class lines plus remainder equal the custody total, remainder 0 -- and the printed class block sums to the total card within one cent; the 60 table rows were not added by hand). Page silent about unlisted assets: not applicable, nothing unlisted. |
| 5 | Holdings, one account picked | REACHED | Total card reads "Total Assets" with the account's figure and Models/SMAs/Client cards; "Back to all accounts" link; the household figure stays in the Identity band's HOW MUCH above. | Picked account named on the face: NO (it appears only inside the Securities table's Account filter; no heading or card names it). Two totals told apart by a label: NO ("Total Assets" vs "HOW MUCH"). Matches D2-S14's expected NO/NO. |
| 6a | Analysis, "Your analysis requests", client picked | REACHED | Skeleton for about 2.5 s, then 25 rows (15 Ready, 8 Unavailable, 2 Failed) and "Next page"; list read took about 5.8 s server time. | Loads or says why: YES (loads). |
| 6b | Analysis, NO client picked, user with a past Prospect upload | NOT REACHED | The walker cannot reach it: its Investor Reporting path opens tabs only after a client pick, and the walker account has never uploaded (writes are blocked by construction). | NOT SEEN. Side note (inferred): the walker account never submitted a request, yet "Your analysis requests" listed 25+ with a client picked, so the list is not this sign-in's own history. |
| 7 | Analysis, existing report opened | REACHED | Opened the first Ready request; it is vendor-kind (inferred: every card carries "Vendor attribution"). Dialog in 47 ms, sections in 2.1 s, 104 section cards. | Opens: YES. Validation line on the face in the vendor's words: NO (no validation line on the face; the word "validation" occurs once, inside a closed Technical details). Source line in the vendor's words: NO ("Source:" occurs 0 times in the dialog). "undefined" or "null": NO (0 and 0). Raw code on the face: YES (every card's title and Label read as a section code of the form "S03"; "Unit: unknown" on all 104 cards; "source_chart_representation" twice; more codes and hashed ids sit inside closed Technical details). |
| 8 | Opal report | NOT REACHED | The list rows do not say which kind a report is; the one opened is vendor-kind. No report was made. | NOT SEEN. Andrew's sitting is the read. |
| 9 | Console and network | REACHED | Red console: 2 x HTTP 401 at sign-in (before the session; not an Investor Reporting route) and 1 React warning on the Holdings tab, "whitespace text nodes cannot be a child of colgroup" (hydration-error class). | Any red error: YES (the three above). Investor Reporting route answering other than 200: NO (all `/api/` answers 200: 121 of 121 in walk 1, 136 of 136 in walk 2). Answers the page received as UNAVAILABLE: `performance/<sel>` OBJECT_NOT_COVERED (shown as the worded refusal on face 3); `reporting/<acc>/manifest` and `reporting/client/<cli>/summary` FIRM_BINDING (3 in walk 1; nothing on any face says so, and which face they feed was NOT SEEN). |

## Other things a reader sees (not asked; one line each)

- Holdings, all accounts: an "Opening <account>..." line and a "Back to all accounts" link show while the reader has
  picked no account (the tab's background one-account reads).
- Holdings: 5 full-width navy bands on one tab (portal design law C3 allows one); 32-36 text elements under 3:1 contrast
  (lavender eyebrow text such as "ALL CATEGORIES" on the light canvas).
- The opened report mixes date formats ("2026-09-22" beside "September 22nd, 2026").
- Performance refusal reads "for this client" and "for this account" in one sentence.

-- 4.0.0_SA_CRO
