# ADVI_COTBOOKS -- Cottonwood's advisor books on Advisor Intelligence: every account in one advisor's book by a stated rule, each book tied to Black Diamond, the page in Inflection's shape

```json
{
 "project": "ADVI_COTBOOKS",
 "directive": "D8",
 "fabric": "dell1",
 "prd_version": "v0.1",
 "step": 4,
 "brief_ref": "docs/briefs/advi-portfolio-group-key-cottonwood-ai-brief-20261017.md@1bae264b34",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6"],
 "status": "DRAFT"
}
```

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-17 ~03:2xZ.
**Placement:** DELL1, directive D8, macro ADVI. Registered @5a2f71d0cc.
**Records (Andrew-direct, both 2026-10-17, recorded by `2.0.0_SA_COO~C1`):**
- ~01:45Z, `org/tier1_exec/2.0.0_SA_COO~C1/ANDREW_DIRECT_20261017_0145Z_CRO_PORTFOLIO_GROUP_KEY_AND_COTTONWOOD_ADVISOR_INTELLIGENCE.md`:
  "how they structure their 'Portfolio Group' key, because that's how we'll be able to run everybody's book properly ... should be taking on
  the Inflection Shape visually. Namely how we are just listing all the accounts in a list on the first tab and it's generally all a mess."
- ~03:00Z, `org/tier1_exec/2.0.0_SA_COO~C1/ANDREW_DIRECT_20261017_0300Z_PORTFOLIO_GROUP_WORK_GO.md` @cdad0d5031: "yeah we do need to figure
  out that portfolio group stuff".

**Endpoint status:** written at L2 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_ADVI_COTBOOKS_20261017.md` @5a2f71d0cc). Andrew's
confirmation is held on the box's open calls (`dell1-20261017T030813Z-0cf5`). This PRD goes to L4-R only after he confirms; if he changes a
line, ENDPOINT is re-pasted here.

## ENDPOINT (step 2, /endpoint --forward)

```
  FWD-1  A Cottonwood admin opens Advisor Intelligence and sees the firm as its
         advisors' books, then opens one advisor and sees that advisor's clients
         DONE WHEN  EXERCISED -- one live trace on the real login, real data and real
                    services: the admin's first screen lists the advisors and an
                    unassigned group, and one click reaches one advisor's clients.
                    Every step is a real call; a step fed by sample data fails
         ACCEPT     A Cottonwood admin can say from the first screen which advisor
                    holds the most assets and the most clients, and can open any
                    advisor to see who that advisor's clients are, without scrolling
                    a list of every account in the firm
         SOURCE     brief Part I (candidate thread), O1, Part III admin test

  FWD-2  Every Cottonwood account belongs to exactly one advisor's book, chosen by
         a rule anyone can read
         DONE WHEN  EXERCISED -- read on the served book data for one dated pull:
                    no account sits in two books, none is lost, and an account Black
                    Diamond lists under more than one group shows the book the rule
                    picked and that it is shared
         ACCEPT     No client is counted twice and none goes missing, and when an
                    account could belong to two advisors the page says which one it
                    shows and why, the same way every day
         SOURCE     brief O2, IV.2 item 1, Part III single-membership test

  FWD-3  Each advisor's book total matches what that advisor sees in Black Diamond
         DONE WHEN  EXERCISED -- for one dated pull, each advisor's total read on the
                    page beside Black Diamond's own figure for that advisor's group,
                    every difference named
         ACCEPT     An advisor looking at their book here does not have to say
                    "that's not my number" against Black Diamond, or the page says
                    plainly by how much and why it differs
         SOURCE     brief O3, IV.2 item 3, Part III advisor test

  FWD-4  An advisor who logs in sees their own book and no one else's
         DONE WHEN  EXERCISED -- one advisor login reaches its own book on the live
                    product, and a request for another advisor's book from that
                    login is refused
         ACCEPT     A Cottonwood advisor sees their own clients when they log in, and
                    cannot see a colleague's
         SOURCE     brief O4, IV.2 item 4

  FWD-5  The Cottonwood page reads like Inflection's
         DONE WHEN  EXERCISED -- the live page at a stated portal commit shows the
                    tabs Advisors, Distribution, Books and Profile in Inflection's
                    arrangement, and the first tab is not a list of every account
         ACCEPT     Someone who knows the Inflection page finds the Cottonwood page
                    laid out the same way, and the clutter of the first tab is gone
         SOURCE     brief O5, IV.3; Andrew ~01:45Z "should be taking on the
                    Inflection Shape visually"

  FWD-6  The books show today's assignments, not old ones
         DONE WHEN  EXERCISED -- a deliberate check on demand: the book an account
                    shows equals its group in the newest Black Diamond pull, and the
                    page names that pull's date
         ACCEPT     When Cottonwood moves a client to another advisor in Black
                    Diamond, the page shows the move with the next day's data, and
                    says which day its books are from
         SOURCE     brief IV.2 item 2, Part VI (the served dimension carries August
                    groups)
```

## CONTRACTS

| row | owner | rule | proven by |
|---|---|---|---|
| C-BOOK | `1.0.0_SA_CTO~DELL1` (definition) | **A book is a Black Diamond Portfolio Group** (the advisor book; brief IV.1). Cottonwood carries four values today: three advisors and "No Advisor". "No Advisor" is the unassigned bucket and is always shown as unassigned, never as an advisor. A new group value appearing in a pull becomes a new book on the next build, with no code change. | the advisor entity list equals the distinct group values of the newest pull, with "No Advisor" marked unassigned |
| C-RULE | the rule cell (in `A_00`, see C-OWNER) | **One book per account, deterministic, never file order.** In order: (1) if the pull carries `Primary Portfolio Group`, that group; (2) otherwise a named advisor group beats "No Advisor"; (3) an account in two or more named advisor groups (1 today) takes the advisor holding most of the other accounts in the same relationship, and ties break by group name, ascending. Every account carries `book_rule` (which step chose) and `shared_with` (the other groups, possibly empty). | a dated pull where 0 accounts have two books and 0 are lost (account count in = out); the 11 Shipley-shared accounts land in Shipley's book (brief IV.2); a reordered copy of the pull gives the identical assignment |
| C-OWNER | `2.0.0_SA_COO~C1` (ADVI_COTBKF) | **`A_00` is ADVI_COTBKF's writer, so the C-RULE cell is cut in ADVI_COTBKF as its next round's first cell** (msg 7116; C-1 of the R106 CTO half). It lands before any cell of this project reads the book. This project defines the rule; ADVI_COTBKF writes it. | the ADVI_COTBKF order citing C-RULE, complete before this project's first page cell |
| C-SCOPE | all | **Books cover the supervised book only** (MDPF_CANON FWD-10, Andrew-direct 2026-10-17 ~01:5xZ). Unsupervised accounts appear in no book. The book totals sum to the Cottonwood supervised total on the same page, to the cent. | the sum of the book totals equals the page's firm total for one dated pull |
| C-ADVISORS | the advisor-entity cell | **A Cottonwood advisor-entity producer replaces the synthetic `A_01` advisor** ("Cottonwood Capital Advisors"). One row per book: a stable `advisor_id` (derived from the group value, unchanged across pulls while the value is), the display name and an `unassigned` flag. | the entity rows for one pull; the synthetic advisor absent from the served output |
| C-LEADERBOARD | the leaderboard cell | **Advisor-grain figures over the C-RULE partition:** AUM, clients, accounts and net flows per book, at the same contract the Inflection page reads, so the same components render it. An overlap sum is never shown as a total. | the served leaderboard for one dated pull; its rows sum to the firm total (C-SCOPE) |
| C-TIEOUT | the tie-out cell | **Each book's total is read beside Black Diamond's value for that group and date,** from BD's group-grain view (the qt6 "book-tie-out oracle", brief IV.2 item 3). Every difference is named by account or cause. The page's source line says the tie-out date and whether it ties. | the per-book read for one date, with every non-zero difference explained |
| C-ROSTER | the roster cell; Andrew (the mapping) | **Each Cottonwood advisor login maps to one `advisor_id`.** The map lives with the portal's partner identity data, the Inflection `advisorId` equivalent. Which login belongs to which advisor is supplied by Andrew. Nobody contacts Cottonwood. | the map's rows; a login without a row sees no Profile tab |
| C-AUTHZ | the page cell | **The own-book guard follows the Inflection pattern (ADVI_PARTNER_AUTHZ):** an advisor login reads only its own `advisor_id`, and the guard runs server-side, not only in the page. | a request for another advisor's book from an advisor login, refused at the service |
| C-PAGE | the page cell | **The Cottonwood page takes Inflection's arrangement:** admin tabs Advisors, Distribution and Books; a non-admin gets Distribution and Profile, with Profile only when the login maps (C-ROSTER). `CottonwoodClientsSection` leaves the first tab: client lists live inside an advisor's book. Inflection's components are reused, not copied. | the page at a stated portal commit on `bun run dev:live --port 5174` against live services |
| C-FRESH | ADVI_COTBKF (the merge); the page cell (the date) | **Books come from the newest pull.** They depend on ADVI_COTBKF's daily `account_attributes` merge (round 106). The page names the pull date its books come from. | for one account moved between pulls (or a read of the newest pull's assignment), the page shows the newest group; the date shown equals the newest pull's |

## THE DECISIONS -- CLOSED AT L4

1. **The book is the Portfolio Group (C-BOOK).** It is the only advisor signal Cottonwood's data carries (`architect` is NULL on all 1,005
   accounts, brief IV.2), and BD's own staff call it "his book".
2. **The fallback rule is stated, not guessed (C-RULE).** File order produces a wrong answer today: Shipley's 11 shared accounts go to "No
   Advisor". Step (2) fixes that, and step (3) covers the single three-group account with a rule anyone can read.
3. **The rule is written where the dimension is written (C-OWNER).** A second writer of the book would make two answers to one question.
4. **Supervised only (C-SCOPE).** The page's total is already supervised on Andrew's word, so the books must add up to it.
5. **Reuse Inflection (C-LEADERBOARD, C-PAGE).** One contract and one set of components, so the two firms' pages cannot drift apart.
6. **Out of scope:** 49 Financial's books (ADVI_BDPARITY T2-DIMS owns that 201-group case); any change to MDPF pages; any contact with
   Cottonwood or Black Diamond staff.

## OPEN AT ANDREW (acts only he can do)

- **The login-to-advisor mapping (C-ROSTER):** which Cottonwood login is which advisor. It is information only he holds, since nobody contacts
  Cottonwood.
- **Client-facing PROD:** the Cottonwood page is client-facing, so its PROD promote waits for his word (CLAUDE.md, PUSHES).
- **Carried, not his act:** adding `Primary Portfolio Group` (dim 436) to template 270648 is an Opal-side template change. It is a round-2
  enrichment, after round 1 runs on the C-RULE fallback. If the pull then carries it, step (1) takes over without a code change.

## CELL CANDIDATES (round 1 builds the FWD-1 thread; the issuer decomposes)

0. **Prerequisite, in ADVI_COTBKF (C-OWNER):** the C-RULE cell in `A_00`, after the R106 daily merge is read.
1. **The advisor-entity producer and the advisor-grain leaderboard** (C-ADVISORS, C-LEADERBOARD, C-SCOPE), in Cottonwood gold.
2. **The Advisors tab and the advisor drill** on the Cottonwood page (C-PAGE first half), reading 1, on DEV, with Andrew's FWD-1 trace as an
   admin.

Later rounds enrich: the tie-out (C-TIEOUT), the roster and the own-book guard (C-ROSTER, C-AUTHZ), the rest of the Inflection arrangement,
the page date (C-FRESH), and dim 436.

## PATHS

- **This project:** `org/missions/D8/ADVI/ADVI_COTBOOKS/`.
- **Code read by the issuer at HEAD before the first cell:** `data/cot/scripts/gold/A_00.accounts_dimension.py`,
  `data/cot/scripts/gold/A_01.advisor_assignments.py`, `data/cot/scripts/gold/D_05.supervised_split.py`,
  `data/cot/scripts/gold/lib/supervised_scope.py`, `data/cot/scripts/bronze/templates/account_attributes.json`,
  `portal/src/pages/AdvisorIntelligence/_partners/cottonwood/index.tsx` and `.../inflection/index.tsx`, and the Inflection producers behind
  `getFirmLeaderboard` (the brief did not read them).

## SURFACE MANIFEST

- **AWS:** Cottonwood gold in `opal-data-cot` (an existing pipeline, so LGIC rule 30's non-application covers it: no new bucket and no new
  address). New tables sit under the existing gold prefix, and the issuer names each against the existing layout.
- **Portal:** the Cottonwood Advisor Intelligence page, DEV first. PROD is client-facing (Andrew).
- **Repo:** this tree; ADVI_COTBKF's `A_00` through its own round (C-OWNER).

## CHANGE LOG

- **v0.1 (~03:2xZ):** first draft, written while Andrew's endpoint confirmation is held.

-- 1.0.0_SA_CTO~DELL1
