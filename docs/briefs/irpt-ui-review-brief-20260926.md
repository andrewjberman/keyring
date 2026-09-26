# Investor Reporting -- the UI review of 2026-09-26: 49 findings, one register

**Mode:** `/brief-create --midstream DSGN_IRPTV1`. **Author:** 4.0.0_SA_CRO, 2026-09-26 ~21:1xZ, on Andrew-direct at
this terminal (verbatim at the end).
**The machine-readable register is the source of truth:** `docs/briefs/irpt-ui-review-findings-20260926.json`.
- It holds 49 findings. Each has an id (UIR-01..UIR-49), its screenshot, the observation, the outcome it belongs to, an
  owner project and seat, a known/new status with its earlier reference, the design rule it breaks, a cause marked
  `measured` or `inferred`, and a testable acceptance line.
- Every table in this file is generated from that register.

**Coverage rule (Andrew: "i dont want any of these slipping through the cracks"):**
- Every one of the 49 UIR ids must appear in the DSGN_IRPTV1 PRD addendum, with its FWD and criterion.
- The CVO grades each id.
- The check is `python docs/briefs/irpt-ui-review-coverage-check.py`. It prints "N of 49" with every missing id, and it
  exits 1 until all 49 are present. The register itself reads 49 of 49; the current PRD reads 0 of 49, as expected
  before the addendum.

---

## PART 0 -- How the blind constraint was honoured, and where it bent

- **Honoured:** no task order, `phase` or `blocking` field of DSGN_IRPTV1 was read for this brief. The findings come
  from Andrew's 10 screenshots of the page as served to him (the served reality) and from source lines read to
  explain a cause.
- **Where it bent:** this seat has read the PRD through v0.12 and wrote its ROUTE STRUCTURE section (C25, FWD-19). It
  also knows round 6 is cut from v0.12, and it graded or reviewed walk IVE20/IVE21/IVE23 earlier today. That
  knowledge shaped the known/new labels and the FWD citations. The six items marked `known` are ones that
  knowledge says are already queued; a reader should check that they really are, rather than trusting the label.
- **The outcomes are NOT unchanged.** O6 (every view shows every account), O9 (a legible securities map) and O10 (the
  figures are real) are not stated by any FWD this seat has read. The others sharpen FWD-2/3/9/12/13/15/16/18/19 at
  the grain an advisor sees.

## PART I -- The outcome territory

**Candidate thread:** one advisor, one Cottonwood client with two accounts (the one in the screenshots), on the page.
- Type the client's name and pick them first.
- Read who they are.
- Open Performance for each account in turn.
- Drill Holdings from the client total to each account's models and back.

That is FWD-1's thread, as it now runs through the client/account route structure.

### O1

An advisor types a client's name and the right client is the first thing they see, in a list nothing else on the page covers or competes with.

Findings: UIR-01, UIR-02, UIR-03, UIR-06, UIR-07, UIR-08, UIR-09, UIR-10, UIR-11.

### O2

An advisor reads who the client is and which firm it is in, in client language: no account number, token, code or double hyphen in the client's identity.

Findings: UIR-04, UIR-12, UIR-13, UIR-14, UIR-30.

### O3

An advisor tells every account of a client apart wherever accounts are listed, and every listed account opens.

Findings: UIR-15, UIR-17, UIR-24, UIR-26.

### O4

An advisor reads one account's performance (never a client blend), and when it cannot be shown reads the true reason in plain words, with no control offered that does nothing.

Findings: UIR-16, UIR-18, UIR-19, UIR-20, UIR-21.

### O5

An advisor moves from the client total down to one account and its models and back, always seeing where they are, with every percentage labelled with what it is a share of.

Findings: UIR-31, UIR-32, UIR-33, UIR-34, UIR-36, UIR-47, UIR-49.

### O6

Every holdings view shows every account of the client.

Findings: UIR-39.

### O7

One colour means one thing on the page: no two items in a chart share a colour, and the model palette and the asset-class palette never reuse each other's colours.

Findings: UIR-25, UIR-37, UIR-44, UIR-46.

### O8

The page shows client facts on its face and system facts one click away: one navy band, one date format, one money format, no raw codes or system words, no wrapped amounts, no duplicate totals.

Findings: UIR-05, UIR-22, UIR-27, UIR-28, UIR-29, UIR-35, UIR-38, UIR-40, UIR-45.

### O9

An advisor reads the securities map: each security once with its total, every tile legible, filters grouped by account.

Findings: UIR-41, UIR-42, UIR-43.

### O10

An advisor can trust the holdings figures: they are as of the last trading day, and model amounts are the positions actually held.

Findings: UIR-23, UIR-48.

## PART II -- Where the boundary sits

- **This brief owns** (DSGN_IRPTV1, 2.0.0_SA_COO~D; 45 findings): everything the page renders and every call it
  makes, under PRD v0.12's ROUTE STRUCTURE.
- **It relies on, and routes to, IRPT_BCKEND** (2.0.0_SA_COO~M; 4 findings):
  - UIR-03, directory display names that are registration titles;
  - UIR-23, the served Holdings as of 2026-09-22, where the R4 scheduled publication is not on;
  - UIR-26, account labels repeating, which the own-mask half @`c412578ede` fixes on the next scheduled publication;
  - UIR-48, model amounts equal to exact target percentages.
- **Shared, the CTO to rule:** UIR-07, search ranking. It is server-side (the IRPT_BCKEND directory search) or
  client-side (the portal re-ranks without filtering).
- **Out of scope:** the Analysis tab (not in these screenshots) and Export's rendering (Export appears only as UIR-20,
  enabled with nothing to export).

## PART III -- The qualitative bar

- An advisor finds a client by typing the client's name and never scrolls past a list of other people's registrations
  to reach them.
- An advisor never sees two accounts that look the same, two chart slices that share a colour, or one colour that
  means a model in one chart and an asset class in the next.
- An advisor never reads a percentage without knowing what it is a share of, and never loses which account they are
  in while drilling.
- A figure the page cannot give comes with the true reason, never "temporarily" when it will not clear by itself.
- Nothing on the page's face is a token, a code, a system word or a second copy of a figure shown elsewhere.

## PART IV -- The substrate: findings with what was measured

The full register, generated from the JSON. The "Outcome" and "Owner" columns are the routing.

| Id | Shot | Surface | Observed | Outcome | Owner | Status |
|---|---|---|---|---|---|---|
| UIR-01 | 165424 | search | The client dropdown opens on an EMPTY query and lists the firm's entries A-Z, acting as a browse list rather than a search. | O1 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-02 | 165424 | search | The PERFORMANCE tab strip draws ON TOP of the open dropdown, cutting it between the first and second option. | O1 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-03 | 165424 | search | Options are account registrations, not clients: 'A HARE CUST FOR' appears three times with three account tails; every row shows one account's tail and a raw type code ('S1', 'FB'). | O1 | IRPT_BCKEND (2.0.0_SA_COO~M) | new |
| UIR-04 | 165424 | search | The firm prints as a token chip ('49financial', 'cottonwood') on every row, inline on some rows and wrapped to its own line on others. | O2 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | known; walk IVE23-AC4 FAIL, org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/prod-uiwalk-20260926.md |
| UIR-05 | 165424 | page | Behind the dropdown: 'Choose a client to confirm its firm and accounts in Resolution.' uses the system word 'Resolution'. | O8 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-06 | 165424 | page | Before any client is chosen, the Performance area shows a figure ('VS BENCHMARK +2.00%') from the illustrative sample panel. | O1 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-07 | 165438 | search | Typing 'anna thiessen' matches on 'anna' only and lists alphabetically; the real match 'Thiessen, Anna' (Cottonwood) is LAST. Name order differs by firm ('ANNA GARCIA' vs 'Thiessen, Anna') and search does not adjust. | O1 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-08 | 165438 | search | The tab strip again covers part of the list: 'ANNA BOROWINSKI' is cut off under it. | O1 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-09 | 165438 | search | Browser spell-check underlines the typed client name. | O1 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-10 | 165438 | search | In Global mode the list mixes all three firms with no grouping and no result count. | O1 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-11 | 165446 | page | 'Illustrative sample -- not a client's data.' shows through behind the search list. | O1 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-12 | 165515 | identity | WHO reads 'Thiessen, Anna ****9237 / BROKERAGE': a two-account client is labelled with one account's tail and type. | O2 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-13 | 165515 | identity | 'cottonwood -- Client': the lower-case firm token and an ASCII double hyphen show on the page. | O2 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | known; walk IVE23-AC4 FAIL |
| UIR-14 | 165515 | header | The Firm menu still says 'Global (All)' after a Cottonwood client is chosen. | O2 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-15 | 165515 | performance | The account picker lists '****9237 / BROKERAGE' twice, with no value beside either. | O3 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | known; own-mask labels half CRO @c412578ede (publishes with the next scheduled Holdings publication); PRD v0.12 C25 label + value |
| UIR-16 | 165515 | performance | The Performance account picker offers 'All accounts', although Performance is per account. | O4 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-17 | 165530 | identity | 'Over what' expands to two identical '****9237 / BROKERAGE' lines, neither clickable. | O3 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-18 | 165515 | performance | 'Performance for this account is temporarily unavailable right now.' is not true for Cottonwood: it needs a one-use Black Diamond plan per account and will not clear by itself. The raw code DEPENDENCY_UNAVAILABLE shows under Details. | O4 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-19 | 165515 | performance | The refusal renders as an amber-tinted block. | O4 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-20 | 165515 | header | Export is enabled while there is no report to export. | O4 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-21 | 165515 | performance | The 'Account:' label and picker float on the page canvas outside any panel; the period controls sit in a separate panel. | O4 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-22 | 165515 | identity | 'About this scope' is a system word on the face. | O8 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-23 | 165515 | data | Holdings are as of 2026-09-22 on Saturday 2026-09-26: three trading days behind Friday 2026-09-25. | O10 | IRPT_BCKEND (2.0.0_SA_COO~M) | new |
| UIR-24 | 165611 | holdings | Both pie slices are labelled 'Unknown' while the table beside them names the accounts. | O3 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | known; walk IVE20-AC4 FAIL item 1 |
| UIR-25 | 165611 | holdings | Both account slices and both legend dots are the same cyan. | O7 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-26 | 165611 | holdings | The two account rows carry identical labels ('****9237 / BROKERAGE'). | O3 | IRPT_BCKEND (2.0.0_SA_COO~M) | known; own-mask labels half CRO @c412578ede; row IRPT_BCKEND-S146 |
| UIR-27 | 165611 | holdings | Supervision and Advisory read 'withheld' on every row: system facts on the face. | O8 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-28 | 165611 | holdings | The summary card shows 'Unique accounts', 'Model coverage' and 'Source dates Business/Observed' on the face, in two date formats. | O8 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-29 | 165611 | holdings | Money is 'USD 46,009,147.02' here and '$46,009,147.02' in the identity card, and the client total appears twice. | O8 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-30 | 165611 | holdings | The 'cottonwood' token chip at the top right. | O2 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | known; walk IVE23-AC4 FAIL |
| UIR-31 | 165641 | holdings | After drilling into account 1 the account filter still says 'All accounts': the drill and the filter do not know about each other. | O5 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-32 | 165641 | holdings | The breadcrumb skips the account level, and the drilled row reads 'Rebalancer strategy: Anna *9238', a different tail from the account's '****9237'. Masking switches between one and four asterisks. | O5 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-33 | 165641 | holdings | The pie shows 100.00% while the table shows 57.17% for the same row: two bases, neither labelled. | O5 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-34 | 165641 | holdings | A one-slice grey pie carries no information. | O5 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-35 | 165641 | holdings | Amounts wrap onto two lines ('USD / 26,303,302.17'). | O8 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-36 | 165650 | holdings | For the same model the pie says 60.70% and the table 34.70%, with different bases and no label. | O5 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-37 | 165650 | holdings | The colour systems collide: blue is an Opal model in this pie but Equity on the securities map; orange is a model here but Alternatives there; Opal Fixed Income is grey, the 'unknown' colour. | O7 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-38 | 165650 | holdings | The 'Primary', 'Custom' and 'Opal model' chips are jargon, and 'Opal model' breaks across two lines. | O8 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-39 | 165743 | holdings | Allocation shows ONE bar (57.17%) and drops the second account's 42.83%. | O6 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-40 | 165743 | holdings | At least four dark navy bands on one page (Allocation and Securities Map headers and footers). | O8 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-41 | 165743 | securities map | The filter chips repeat each model once per account and mix models, sleeves, strategies and 'DIVZ SMA', with no account grouping. | O9 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-42 | 165743 | securities map | The right third of the treemap collapses into unreadable hairline slivers. | O9 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-43 | 165743 | securities map | One security splits into several tiles, one per model (SPHY x3, JAAA x2, JPST x2), so its total cannot be read. | O9 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-44 | 165743 | securities map | The legend's Cash green is almost the same as Fixed Income green; no Cash tile shows; grey and white slivers have no legend entry. | O7 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-45 | 165743 | page | Three date formats on one page ('September 22nd, 2026, 5:00p ET', '2026-09-22', 'September 24th ... 2:02a ET'); 'Source: Opal Capital Analysis.' is vague. | O8 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-46 | 165932 | holdings | DIVZ SMA and Opal Fixed Income are both grey, so two slices look the same. | O7 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-47 | 165932 | holdings | Pie and table percentages use different bases again (36% against 15.42%). | O5 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |
| UIR-48 | 165932 | data | Model amounts are EXACT percentages of the account: 36.0000 / 33.0000 / 21.0000 / 7.0000 / 3.0000% (account 2) and 60.7 / 20.0 / 16.0 / 3.3% (account 1), including 'Client (residual, not in a model)'. Real positions would not land on round numbers; this looks like target weight x account value. | O10 | IRPT_BCKEND (2.0.0_SA_COO~M) | new |
| UIR-49 | 165932 | holdings | The account filter still says 'All accounts' while drilled into account 2; the breadcrumb again skips the account. | O5 | DSGN_IRPTV1 (2.0.0_SA_COO~D) | new |

Causes measured at source, beyond the screenshots:
- **UIR-39:** `AllocationBars.rootOf` returns the FIRST node with `parentRef === null`
  (`portal/src/pages/InvestorReporting/tabs/holdings/AllocationBars.tsx:64-65, 138-139`). A two-account snapshot has two
  parentless ACCOUNT nodes (PROD walk HAR entries 98 and 256), so only the first account renders. `slices.ts:148`
  `rootNode` has the same shape, so every view built on it may drop accounts; a census of its callers is owed.
- **UIR-16:** `AccountFilter` always adds "All accounts" (`AccountFilter.tsx:99-100`), and Performance mounts it.
- **UIR-12:** WHO is the search option label (`IdentityCard.tsx:343`), which is the name plus one masked tail
  (`header/search.ts:94-96`).
- **UIR-48:** account 2's model amounts divided by its value give 36.0000%, 33.0000%, 21.0000%, 7.0000% and 3.0000%;
  account 1's give 60.7%, 20.0%, 16.0% and 3.3%. This was computed by this seat from the screenshot figures.

## PART V -- What must be true, without scoping it now

- The own-mask account labels (UIR-15, UIR-26, UIR-32) publish with the next scheduled Holdings publication (R4
  enable, whose second half this seat owes). Until then, every account list shows the value beside the label (C25
  v0.12).
- Cottonwood per-account Performance needs a one-use Black Diamond plan per account, so UIR-18's honest copy depends
  on that gate as it stands.
- UIR-48 needs 2.0.0_SA_COO~M's reading of how model amounts are formed, before any view presents them as held
  positions.
- The firm catalogue's display names (UIR-04, UIR-13, UIR-30) must be available to the page, not only the tokens.

## PART VI -- Status (NOT OUTCOME-BEARING)

- **Build observed:** localhost:5174 dev build (address bar in 165743). The running bundle's commit was not recorded.
  The shared portal working copy read `fdccc6e6`, origin DEV `1e02be40`, PROD `36a37afc` (21:0xZ).
- **Counts** (from the register):
  - by outcome: O1 9, O2 5, O3 4, O4 5, O5 7, O6 1, O7 4, O8 9, O9 3, O10 2;
  - by owner: DSGN_IRPTV1 45, IRPT_BCKEND 4;
  - by status: new 43, known 6;
  - by cause claim: inferred 10, measured 39.

## PART VII -- What this brief does not claim

- The 10 `inferred` causes are not checked in code: UIR-01, 02, 06, 07, 08, 09, 24, 25, 46, 48. Each acceptance line
  stands whatever the cause turns out to be.
- UIR-48 is a pattern in the numbers, not a proven cause. Whether model amounts are targets or holdings is 2.0.0_SA_COO~M's
  to state.
- Only one Cottonwood client and the 49financial/Global search lists were reviewed. Other firms' and clients' pages
  may carry more.
- The screenshots stay on this laptop (`C:\Users\AndrewBerman\Pictures\Screenshots\`). They show client names and
  amounts and are NOT committed. Each finding's text stands alone.
- The `known` labels rest on this seat's reading of earlier records (PART 0).

## Refs to carry

```
  BRIEF PATH        docs/briefs/irpt-ui-review-brief-20260926.md
  REGISTER          docs/briefs/irpt-ui-review-findings-20260926.json   (49 findings, schema_version 1.0)
  COVERAGE CHECK    docs/briefs/irpt-ui-review-coverage-check.py        (exit 0 only when all 49 ids are cited)
  PROJECT           DSGN_IRPTV1 (owner of 45); IRPT_BCKEND (owner of 4)
  EXISTING PRD      org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md (v0.12)
  SIBLING PROJECTS  IRPT_BCKEND (2.0.0_SA_COO~M: UIR-03, 23, 26, 48)
  PRIOR ART         route structure @713a49f7b8 (C25); walk grades prod-uiwalk-20260926.md (IVE20/21/23);
                    own-mask labels half @c412578ede; R4 enable first read @707490f568
  MEASURED AT       2026-09-26 ~20:5xZ-21:1xZ (screenshots 16:54-16:59 local)
```

## Andrew-direct request -- verbatim record

Channel: the 4.0.0_SA_CRO terminal, 2026-09-26 ~21:0xZ.

> "I want to do another fronteend analysis to point out all these things i dont like. [10 screenshot paths] lets start
> with these and you point out the issues you see with each and ill add others if you miss any"

> "you got pretty much everything, i think you can just write the brief now"

> "need it very structured, make sure every single point is covered in machine-readable form, because i dont want any
> of these slipping through the cracks."

> "so there are 49 issues you caught, all of them should be included."
