# ADVI -- the Black Diamond "Portfolio Group" key, and why the Cottonwood Advisor Intelligence page is a flat list

**Author:** `4.0.0_SA_CRO~DELL1` | **Date:** 2026-10-17 | **Mode:** NEW (research brief; no portal or served-table change)

**Order:** `org/tier1_exec/2.0.0_SA_COO~C1/ANDREW_DIRECT_20261017_0145Z_CRO_PORTFOLIO_GROUP_KEY_AND_COTTONWOOD_ADVISOR_INTELLIGENCE.md`

**Andrew, verbatim:** "how they structure their 'Portfolio Group' key, because that's how we'll be able to run everybody's
book properly ... very wonky stuff going on with their Advisor Intelligence page ... should be taking on the Inflection
Shape visually. Namely how we are just listing all the accounts in a list on the first tab and it's generally all a mess."

**Claim labels on every finding:**
- **[V-API]:** vendor-observed through Black Diamond's own query catalog.
- **[DATA]:** measured in landed data during this read.
- **[CODE]:** read in the repo.
- **[INF]:** inferred.

Public SS&C documentation does not define the term. The vendor evidence is BD's query catalog as Opal's own scan read it.

---

## PART I -- THE OUTCOME TERRITORY

The candidate thread: one Cottonwood admin opens Advisor Intelligence and sees Cottonwood's three advisors as three
books, the way an Inflection admin sees Inflection's, and drills from an advisor to that advisor's clients.

### O1. A Cottonwood admin sees the firm as its advisors, not as one undifferentiated account list
Three named books (Jay Rubottom, Christa Bass, Stephen Shipley), plus an honest "unassigned" bucket. The single
synthetic advisor "Cottonwood Capital Advisors" goes away.

### O2. Every Cottonwood account belongs to exactly one book, by a stated rule
No account is counted twice, and none disappears. A two-book account shows in the book the rule names, and the page
says so.

### O3. The book totals match what the advisor sees in Black Diamond
An advisor or admin reads a book figure here that they would otherwise have opened Black Diamond's Business
Intelligence dashboard for, and the two agree.

### O4. An advisor who logs in sees their own book
This is the Inflection "Profile" path: a non-admin Cottonwood login resolves to its own advisor book, never another
advisor's.

### O5. The first tab reads like Inflection's: Advisors | Distribution | Books | Profile
The firm-level client roster is no longer stacked under Distribution as the first thing on the page.

## PART II -- WHERE THE BOUNDARY SITS

**Owns:**
- the definition of "book" for Cottonwood;
- the account-to-book rule;
- the data contracts the Inflection-shaped page needs from it.

**Relies on, does not own:**
- **ADVI_COTBKF.** The `silver/account_attributes` daily merge (round 106) and the `A_00` writer. Condition C-1 lives
  there.
- **The 49 Financial book work: ADVI_BDPARITY T2-DIMS** (`data/assets/scripts/gold/runners_49f/bd49f_dim_portfolio_group.py`).
  It already built `dim_portfolio_group` plus `bridge_group_account` for 49F, and it hit the same missing-primary-key
  wall (Part IV.1).
- **The portal Advisor Intelligence pages** (`portal/src/pages/AdvisorIntelligence/_partners/{cottonwood,inflection}`). The
  page work follows the normal route after Andrew reads this.
- **MDPF_CANON FWD-10, the Cottonwood gap diff** (`4.0.0_SA_CRO~DDD`). Adjacent; not touched here.
- **The client-to-model map** (BD rebalancer `fact_model_assignment`). A different axis: book is not portfolio (Part IV.2).

## PART III -- THE QUALITATIVE BAR

- **Advisor test:** a Cottonwood advisor looking at their book here does not have to say "that's not my number" against
  Black Diamond.
- **Single-membership test:** no account appears under two advisors, and none is hidden under "No Advisor" when it has a
  named advisor.
- **Admin test:** a Cottonwood admin can name, from the first screen, which advisor holds the most assets and the most
  clients, without scrolling an account list.

## PART IV -- THE SUBSTRATE: WHAT EXISTS AND WHETHER IT FITS

### IV.1 What Black Diamond's Portfolio Group is (Q1)

- **Place in the hierarchy [V-API].** BD's query type 6 ("BI Billing", the data model behind the Business Intelligence
  dashboard) exposes the level hierarchy **Date -> Team -> Relationship -> Client -> Portfolio Group -> Portfolio ->
  Account -> Holding**. Source: `org/tier1_exec/4.0.0_SA_CRO~A/deliverables/BD_PORTFOLIO_GROUP_KEYING_SCAN_20260819.md`
  section 3.
- **What it is used for [V-API + transcript].**
  - BD's Mike Little (Data Discussion, 2026-08-19): "portfolio group is like it is specific for the advisor ... his book,
    essentially".
  - Admin exports "come out divided up by portfolio group" (same file, section 1).
  - **It is the advisor book. It is not a strategy and not a portfolio.**
- **Cardinality: one account to MANY groups [DATA, V-API].**
  - At 49F: 201 groups and 6,155 accounts, with 5,579 accounts (90.6%) in 2 or more groups and up to 13. The groups
    overlap: advisor books, "X - Local Ops" views, division groups.
  - Summing across groups gives $8.25B against a $1.55B book (`bd49f_dim_portfolio_group.py` header).
- **What makes it a partition [V-API].** BD carries a separate dimension, **`Primary Portfolio Group` (dim id 436)**, which
  marks the ONE group that owns the account.
  - Membership is many-to-one; the primary is one-to-one.
  - Neither Opal pull selects dim 436:
    - the 49F template 390224 does not (`bd49f_dim_portfolio_group.py`: "THE PRIMARY KEY IS NOT IN THE FEED");
    - the Cottonwood template 270648 selects only `Portfolio Group, AccountID, Position Only, Account Supervised,
      Account Billable` (`data/cot/scripts/bronze/templates/account_attributes.json`) [CODE].
- **What a "multi-book" account means [INF from V-API + DATA].** It is an account that is a MEMBER of more than one
  group. At Cottonwood, almost every such account is an advisor's group plus "No Advisor" (IV.2). That reads as an
  assignment hangover, not a real co-ownership: an account still sitting in "No Advisor" after being added to an
  advisor's group. The primary dimension would say which group owns it, without guessing.

### IV.2 The key in Cottonwood's data today (Q2)

**Where it lives [CODE]:**
- BD datamining template 270648, landed daily as
  `s3://opal-data-cot/forwardfill_v2/account_attributes/ACCOUNT_ATTRIBUTES_DAILY_<date>.xlsx`;
- then `silver/account_attributes/`;
- then joined by `A_00` into `gold/dimensions/accounts_dimension_latest.parquet` as `portfolio_group`;
- `D_05` reads it for the supervised/book split.

**Measured on the 2026-10-15 pull, landed 2026-10-16 07:30 [DATA]:**

| | Count |
|---|---|
| Rows / distinct accounts | 1,127 / 1,004 |
| Distinct groups | 4 |
| Rows per group | Jay Rubottom 418, Christa Bass 239, Stephen Shipley 239, No Advisor 231 |
| Accounts in 2+ groups (multi-book) | **122** |
| ...of which advisor + No Advisor | 121 (Rubottom 91, Bass 19, Shipley 11) |
| ...in three groups (Rubottom + Shipley + No Advisor) | 1 |
| Accounts ONLY in No Advisor | 109 |

- **Cottonwood is far simpler than 49F.** It has 4 groups, and all of them are advisor books plus an unassigned bucket.
  There are no "Local Ops" or division groups. Its overlap is almost entirely "advisor + No Advisor".
- **First-row-wins is not only unstable; it is wrong today [DATA].**
  - `A_00` takes the first row in vendor file order for a multi-book account. The file is not sorted by group.
  - On the 10-15 pull, first-row picks for the 122 are Jay Rubottom 92, Christa Bass 19, **No Advisor 11**.
  - Those **11 are exactly Stephen Shipley's 11 shared accounts**. Shipley's book loses them to "No Advisor".
  - Day over day, the picks did not move (0 of 1,004 differ between the 10-14 and 10-15 pulls). The risk ADVI_COTBKF C-1
    names (a flip on reorder) is latent. The misassignment is present now.
- **The served dimension is stale [DATA].**
  - `accounts_dimension_latest.parquet` (rebuilt 2026-10-16 07:34) carries portfolio groups from the August silver
    partition: Rubottom 399, Bass 232, Shipley 230, No Advisor 81, **NULL 63** (of 1,005).
  - Silver `account_attributes` still holds only `2026-08-19.parquet`. ADVI_COTBKF round 106's fix first fires about
    2026-10-17 midday.
- **No other advisor field exists [DATA].**
  - The dimension's `architect` column is NULL for all 1,005 accounts.
  - `A_01` (advisor roles from transactions) therefore has nothing for Cottonwood, which is why the page shows ONE
    synthetic advisor (`cottonwood/index.tsx` header: "DS A_01 synthetic single advisor 'Cottonwood Capital Advisors'").
  - **Portfolio Group is the only advisor signal Cottonwood has.**
- **Book is not portfolio [DATA, prior CRO read].**
  - Each group spans 19 to 37 rebalancer strategies.
  - The client-to-model map is the BD rebalancer assignment (`fact_model_assignment`), joined on `external_id` =
    datamining `AccountID` (990 of 995), never on `account_id`.
  - Source: `org/tier1_exec/4.0.0_SA_CRO/deliverables/P3_COTTONWOOD_BACKEND_CENSUS_AND_PORTFOLIO_GROUP_20261014.md`.

**What must be true for it to be the unit of "everybody's book":**
1. **One owner per account, by the vendor's assertion.** Add `Primary Portfolio Group` (dim 436) to template 270648. Until
   that lands, use a STATED fallback rule: a named advisor beats "No Advisor"; and for the one three-group account,
   either name a pick or show it as "shared". Never use file order.
2. **Fresh daily.** Silver `account_attributes` must merge every day (ADVI_COTBKF round 106), so the book reflects the
   current pull, not August.
3. **Tied to BD's own number.** Each book's total ties out to BD's group-grain value (qt6, the "book-tie-out oracle",
   T1 in the 2026-08-19 scan). An overlap sum is never shown as a total.
4. **A login-to-advisor map.** Each Cottonwood portal user who is an advisor maps to one group name (the Inflection
   `advisorId` equivalent) for the Profile path.

### IV.3 How this produces today's page, and what the Inflection shape needs (Q3)

**Today [CODE]:**
- `cottonwood/index.tsx` has two tabs, **Distribution** and **Books** (admin-only).
- Distribution stacks `DistributionTab` and then `CottonwoodClientsSection`, the firm-level client roster ("firm-level
  client relationships, advisor-independent"). **That roster is the long account list on the first tab.**
- Books renders the shared advisor drill over ONE synthetic advisor, so the advisor level carries no information.
- The page reads no `portfolio_group` at all (ADVI_COTBKF CTO half: "No portal or gateway reader").

**Why [INF, strongly supported]:**
- When the Cottonwood page was built, there was no advisor key the page could trust: `architect` was empty and
  `portfolio_group` was unmerged, stale and first-row-ambiguous.
- So the page fell back to "one firm, all clients": a synthetic advisor plus a flat roster.
- **The flat list is the visible symptom of the missing book key.**

**Inflection's shape [CODE]:**
- Admin tabs: Advisors | Distribution | Books. A non-admin gets Distribution | Profile, with Profile only when the login
  resolves to an `advisorId`.
- It reads `getFirmLeaderboard` (advisor-grain) and the platinum partner analytics.
- It enforces the own-book-only rule (ADVI_PARTNER_AUTHZ).

**What the Inflection shape needs from the key, as data contracts:**

| Contract | Grain | Must carry | Comes from |
|---|---|---|---|
| Advisor entities | One row per book | `advisor_id` (stable), display name, and an "unassigned" bucket marked as such | `Portfolio Group` values |
| Account-to-book partition | One row per account | Exactly one `advisor_id`, the rule that chose it, and a `shared_with` list for multi-book accounts | `Primary Portfolio Group`, or the stated fallback (IV.2 item 1) |
| Advisor leaderboard | One row per advisor | AUM, clients, accounts, flows, sums that equal the firm total, and a tie-out to BD's group value | Gold, over the partition |
| Book drill | Advisor -> relationship -> account | Relationships (225 today) under their advisor | `relationship_id` in the accounts dimension |
| Login-to-advisor | One row per portal user | The `advisor_id` for the Profile tab and the own-book guard | Cottonwood user roster (new) |

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

These are named, not sequenced:
- the dim-436 addition to the BD template (vendor-side pull change);
- the daily silver merge (ADVI_COTBKF);
- a deterministic `A_00` rule. ADVI_COTBKF C-1 already says a consumer appearing triggers an `A_00` cell first, and this
  page would be that consumer;
- a Cottonwood advisor-entity producer in place of the synthetic `A_01` one;
- the leaderboard at advisor grain;
- the login-to-advisor roster;
- the qt6 tie-out read.

## PART VI -- STATUS (NOT OUTCOME-BEARING)

Measured 2026-10-17 01:5xZ to 02:1xZ:
- the forwardfill pulls 10-13 to 10-15 land daily;
- silver `account_attributes` holds the 2026-08-19 partition only;
- the accounts dimension was rebuilt 2026-10-16 07:34, with August groups (63 NULL);
- ADVI_COTBKF round 106's first scheduled silver fire is about 2026-10-17 midday.

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- **No SS&C public documentation defines "Portfolio Group".** The hierarchy and dim 436 are as BD's query catalog exposed
  them to Opal's scan on 2026-08-19, not a vendor manual.
- **Not verified:**
  - that dim 436 is populated for Cottonwood's tenant;
  - which group BD marks primary for the 122 multi-book accounts;
  - that "No Advisor" plus an advisor is a hangover rather than an intended state. Ask Cottonwood or BD.
- **Not read:**
  - BD's Business Intelligence app endpoints;
  - the Cottonwood user roster;
  - the Inflection gold producers behind `getFirmLeaderboard`.
- **No client names or account numbers were printed or kept.** Counts are group-level.
- **No change was made to any portal file, served table or pipeline.**

---

## REFS

| Item | Pointer |
|---|---|
| Brief path | `docs/briefs/advi-portfolio-group-key-cottonwood-ai-brief-20261017.md` |
| Project | NONE-YET (adjacent: ADVI_COTBKF, ADVI_BDPARITY) |
| Existing PRD | NONE for this page shape |
| Sibling projects | ADVI_COTBKF (silver merge, `A_00`, C-1); ADVI_BDPARITY T2-DIMS (49F group dim); MDPF_CANON FWD-10 (`4.0.0_SA_CRO~DDD`) |
| Prior art | `org/tier1_exec/4.0.0_SA_CRO~A/deliverables/BD_PORTFOLIO_GROUP_KEYING_SCAN_20260819.md`; `org/tier1_exec/4.0.0_SA_CRO/deliverables/P3_COTTONWOOD_BACKEND_CENSUS_AND_PORTFOLIO_GROUP_20261014.md`; `data/assets/scripts/gold/runners_49f/bd49f_dim_portfolio_group.py`; `data/cot/scripts/bronze/templates/account_attributes.json`; `data/cot/scripts/gold/A_00.accounts_dimension.py`, `A_01.advisor_assignments.py`, `D_05.supervised_split.py`; `org/missions/D8/ADVI/ADVI_COTBKF/ledger/NEVER_WIDEN_R106_ACCOUNT_ATTRIBUTES_CTO_HALF.md` (C-1) |
| Pages | `portal/src/pages/AdvisorIntelligence/_partners/cottonwood/index.tsx`; `.../inflection/index.tsx` |
| Measured at | 2026-10-17 01:5xZ to 02:1xZ (pulls 2026-10-14 and 2026-10-15; dimension 2026-10-16 07:34) |
