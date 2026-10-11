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

## ADD-ON: faces 10 and 11, IV-e-106 (MSTR msgs 108372 and 108373)

- **Builds walked:** walk 3 at portal DEV `ca23f110a25f43f952392054117c5b40942ad85f` (17:43:07Z-17:49:34Z); walks 4 and 5
  at portal DEV `3ebc35ebf2ef7d95318333b95b50657d861d9f20` (17:52:12Z-18:01:21Z, 18:03:01Z-18:05:58Z). Each head was
  read by `git fetch` + `rev-parse` before the walk and served from the same local `dev:live` worktree. `3ebc35eb` over
  `ca23f110` changes only Ticket Center files and `src/api/endpoints/investor-reporting.ts`. Same sign-in kind and the
  same client; every disarm REFUSED a login; 0 guard aborts; every `/api/` answer 200 (122, 90, 119).

| # | Face | Reached | What it showed | Answers |
|---|---|---|---|---|
| 10a | Holdings, one account in scope | REACHED | Above the total card: "Account: <masked label>" in bold and "Total Assets below: this account"; the card's Total Assets is that account's figure and the class block beneath sums to it. | Line seen: YES. Matches the card: YES (the masked label is the same account the card and the table's Account filter show). |
| 10b | Holdings, all accounts in scope | NOT REACHED | In every walk on these heads the Holdings tab opened on ONE account: the account the Performance tab's Account select last held (the walker's select loop ends on the second account). The walker does not press "Back to all accounts". | "All N accounts" / "Total Assets below: all N accounts": NOT SEEN. |
| 10c | Identity band base | REACHED | Under HOW MUCH: "all 2 accounts", beside OVER WHAT "2 accounts". | Seen: YES. Matches: YES. |
| 11 | Header search, ACCOUNT row picked (walk 5, a fresh session) | REACHED | Typing the account's last four digits offered one option ("1 matched across firms"): the client's name with that account's masked label and the firm beneath it (inferred to be the account row; it is the only row offered). After the pick the search box reads the client's name and the Identity band shows the whole client ("all 2 accounts"). | Performance's Account select starts on the picked account: NO (it starts on the client's OTHER, larger account; refusal words in 3.4 s). Holdings opens on the picked account: NOT SEEN as a clean read (it did open on the picked account, but the walker's Performance select loop had just left that same account selected, so the header pick and the carry-over cannot be told apart). Consistent with CTO~DELL2's note that the account-row case "is held by a test and nothing rendered". |
| 106 | IV-e-106, report reader carries retained_ref | REACHED | The same Ready report reopened at `ca23f110`: 104 section cards, 94 coverage items, "Job status: Ready", as at `9ca634c6`. "retained" and "sha256" occur 0 times in the dialog. | Unchanged face: YES (as the commit says, no page prints it). |

New observation (walks 1, 3, 4, 5): **the Holdings tab inherits the account last chosen in Performance's Account select.**
A reader who looks at one account's performance and then opens Holdings sees that one account, not the client. At
`9ca634c6` it showed mid-flight ("Opening <account>..." over the all-accounts figures); from `ca23f110` on, the new line
names the account, so the reader is at least told.

-- 4.0.0_SA_CRO
