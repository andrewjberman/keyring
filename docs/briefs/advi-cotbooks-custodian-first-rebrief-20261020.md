# ADVI_COTBOOKS re-brief -- Cottonwood's whole book from its custodians, with no Black Diamond dependency

**Author:** `4.0.0_SA_CRO~DELL1` | **Date:** 2026-10-20 | **Mode:** MIDSTREAM (re-brief; supersedes
`docs/briefs/advi-portfolio-group-key-cottonwood-ai-brief-20261017.md` @1bae264b34 and its endpoint once the endpoint is re-cut)

**Order:** `1.0.0_SA_CTO~DELL1` msg 8631, on Andrew-direct
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261020_133xZ_COTBOOKS_NO_BD_DEPENDENCY_CUSTODIAN_FIRST.md` @7fb4f70e80.

**Andrew, verbatim:** "Our ultimate goal is figuring out how to replace Black Diamond, which means that we cannot rely on Black
Diamond for any critical function ... we want Cottonwood to be our first true case study where we figure out how to represent all
their stuff without having any BD dependency." And: "The purpose of this work should really be about assessing how to analyze and
stitch the commonwealth books to the fidelity backfill and shape." Black Diamond may be compared against ("Yes we can compare to
BD"); it is never a source.

**Claim labels:** **[DATA]** measured in landed data during this read; **[BD-CHECK]** measured in Black Diamond's data, used only
as a comparison, never as an input to an outcome; **[CODE]** read in the repo; **[INF]** inferred.

---

## PART 0 -- HOW THE MIDSTREAM CONSTRAINT WAS HONOURED, AND WHERE IT BENT

- **Not read:** any ADVI_COTBOOKS task order or decomposition (none exist: `project.json` `decompositions: []`), and the PRD body.
- **Read:** the 2026-10-17 brief and its endpoint (`ENDPOINT_FORWARD_ADVI_COTBOOKS_20261017.md`), because they are the base this
  re-brief replaces, and the served reality in S3.
- **Where it bent:** this seat wrote the 2026-10-17 brief, so its framing (the Portfolio Group as the advisor book, the Inflection
  page shape) was already in mind. The leak is named so a reader can check for it: the page outcomes (O8) survive from the old
  brief in substance, and nothing else is carried forward without a new measurement.
- **What changed and what did not:** the direction moved. The old brief made Black Diamond's Portfolio Group the key and Black
  Diamond's figures the tie-out. This one makes the custodians the source, and Black Diamond only the check. The page shape is
  unchanged.

## PART I -- THE OUTCOME TERRITORY

**Candidate thread (FWD-1):** one Opal analyst reads Cottonwood's **Fidelity** book for one day, every account with its holdings
and value, from Fidelity's own files in Opal's store, and sees that figure beside Black Diamond's Fidelity figure for the same day
with every difference named. Fidelity is 70% of the book (F1), so it is the coarse-grain journey; every outcome below enriches it.

### O1. An analyst reads Cottonwood's Fidelity book for any day from Fidelity's own files
Every Cottonwood account under the seven G numbers, counted once, with holdings, cash and value, read from the Wealthscape landing,
not from Black Diamond.

### O2. An analyst reads one Cottonwood account's history as one continuous line, from Commonwealth to today
The account's Commonwealth years (2013 to June 2026) and its Fidelity years (from the move in May-June 2026, plus the per-G
backfill) join into one history, and the join point is visible. This is Andrew's "stitch the commonwealth books to the fidelity
backfill".

### O3. An analyst reads Cottonwood's Schwab accounts from Schwab's own files
Once the advisor master accounts are in hand, the Schwab accounts land beside Fidelity's and read the same way.

### O4. A person sees how much of Cottonwood's book Opal reads from a custodian, and what it does not read
Coverage per class (Fidelity, Schwab, Strata, manual and alternative positions, held-away accounts), in accounts and dollars, with
every uncovered class named. Strata is named as a gap until its feed is known.

### O5. A person sees one Cottonwood client's accounts across custodians together
One household's Fidelity, Schwab and Commonwealth-era accounts under one Opal-owned client key, never Black Diamond's
Relationship ID.

### O6. Every Cottonwood account sits in one advisor's book by a rule whose input is not Black Diamond
The advisor assignment comes from a source Cottonwood or a custodian owns. Black Diamond's Portfolio Group is read beside it as a
check, and each disagreement is listed.

### O7. A person can say, per custodian, how far Opal's figure is from Black Diamond's, and why
For one dated day: accounts and value per class, Opal beside Black Diamond, every difference named (timing, an account one side
lacks, a pricing difference). This is the replacement test: the gap shrinks to explained differences only.

### O8. A Cottonwood admin reads the firm as its advisors' books on Advisor Intelligence, in Inflection's shape
The page outcomes of the 2026-10-17 endpoint (advisor books, own-book-only login, the Inflection tab layout), now fed by the
O1-O6 books instead of Black Diamond's.

## PART II -- WHERE THE BOUNDARY SITS

**This project owns:** the Cottonwood book model across custodians (which accounts, which classes, counted once), the
Commonwealth-to-Fidelity stitch, the client key, the advisor-assignment rule, the coverage statement, and the comparison to Black
Diamond.

**It relies on, and does not own:**
- **NFRA_FIDUPL** (the Wealthscape uploader). It owns the Fidelity landing: the daily export, the per-G pulls, the backfill
  (C-BACKFILL, Cottonwood's seven G numbers first) and the per-firm split (FWD-9). This project reads that landing; it never pulls
  Fidelity itself.
- **The Commonwealth backfill** (brief `docs/briefs/cottonwood-commonwealth-10y-backfill-brief-20261006.md`). Its bronze and
  silver are landed under `opal-data-assets/commonwealth/cottonwood/` (F4). This project reads them.
- **The canonical Schwab pipeline** (`infra/aws/terraform/canonical-schwab-ec2/`). A new Cottonwood master is a new daily pull
  there, owned by that pipeline.
- **ADVI_COTBKF and the Black Diamond Cottonwood pipeline** (`opal-data-cot`). Comparison input only. Nothing in this project's
  outcomes may read it as a source.
- **The naming registry** (`infra/logic/registry/`, LGIC). Cottonwood's firm scope rows are being added under NFRA_FIDUPL C-NAMES
  (CTO msg 8632).

**Does not own:** contacting Cottonwood, Strata or Schwab; any vendor template change; Black Diamond's own pipeline.

## PART III -- THE QUALITATIVE BAR

- **Replacement test:** for every figure on a Cottonwood page, someone can name the custodian file it came from, and none came from
  Black Diamond.
- **Honest-coverage test:** nobody reads a Cottonwood total as "the whole book" when a class is missing; the missing class and its
  size are on the same screen.
- **Continuity test:** an analyst follows one account from 2013 to today without switching tools, and can see the day it moved
  from Commonwealth to Fidelity.
- **Once-only test:** no account is counted twice because it sits under two G numbers or at two custodians.

## PART IV -- THE SUBSTRATE: WHAT EXISTS, MEASURED

### F1. What Cottonwood's book is made of [BD-CHECK]

Black Diamond's 2026-10-19 allocations export for Cottonwood (`opal-data-cot/forwardfill_v2/allocations/ALLOCATIONS_DAILY_2026-10-19.xlsx`):
1,503 rows, 855 distinct accounts, $550.5M.

| Class | Accounts | Value | Share | Feed into Black Diamond |
|---|---|---|---|---|
| Fidelity (direct feeds: IWS, CGF) | 647 | $385.3M | 70.0% | Fidelity IWS, Fidelity CGF |
| Schwab (direct feed) | 20 | $80.6M | 14.6% | Schwab |
| Strata Trust Company (direct feed) | 8 | $2.0M | 0.4% | Strata Trust Company |
| Manual and alternative (entered by hand in Black Diamond) | 114 | $68.9M | 12.5% | Manual Account, Alternative Investment, Investor Manual Accounts |
| Held-away (aggregated, e.g. 401(k), bank, card) | 66 | $13.6M | 2.5% | ByAll Accounts (includes 8 Fidelity and 4 Schwab retail accounts) |

- **Finding:** custodian files can reach at most about 85% of the book (Fidelity, Schwab and Strata). The other 15% ($82.6M) has no
  custodian feed at all: it exists in Black Diamond because someone typed it in or an aggregator scraped it. Replacing Black Diamond
  for Cottonwood means deciding where that 15% comes from.

### F2. What Opal can read today, per custodian [DATA]

| Custodian | Opal landing today | Measured |
|---|---|---|
| Fidelity | **None yet.** `s3://opal-data-assets/fidelity/` is empty. NFRA_FIDUPL is EXECUTING: its Terraform root is planned, not applied (18 to add, commit 814c01e738), and both live sign-in attempts so far stopped before the text-message step (its rows W1-S9, 13:05Z, and W1-S11, 13:48Z). | prefix listing 2026-10-20 ~13:4xZ |
| Schwab | **None for Cottonwood.** Opal lands three masters: 08335338 and 08242234 (49 Financial) and 08403355 (Opal's Tax SMA). None of Black Diamond's 20 Cottonwood Schwab accounts appears in any of them (0 of 20). | 2026-10-19 `dim_balance` of each master: 7,695, 7,604 and 30 accounts |
| Strata | **None.** No `strata/` prefix, no registry source, no Opal pull. Black Diamond receives a direct Strata feed (8 accounts, F1); how is not known. | prefix listing |
| Commonwealth (history) | **Landed.** Bronze plus 12 silver tables under `opal-data-assets/commonwealth/cottonwood/silver/` (transactions, performance, positions, daily_returns, account_day_value, crosswalk, account_links, document_index and others), as-of 2026-06-23. | listing 2026-10-20 |

### F3. The advisor key: the custodian code does not separate the advisors, as far as Black Diamond shows it [BD-CHECK]

Andrew's Q1 answer named the G numbers, with "PRIMARY", "SECONDARY" and one per advisor (Shipley, Rubottom, Bass). In Black
Diamond's copy of the rep code, per Fidelity account (655 accounts, including the 8 held-away Fidelity accounts):

| Rep code set | Accounts |
|---|---|
| PRIMARY + SECONDARY | 633 |
| PRIMARY + SECONDARY + RUBOTTOM | 2 |
| PRIMARY + SECONDARY + BASS | 1 |
| PRIMARY only | 11 |
| none | 8 |

- SHIPLEY, and the two non-G460 numbers (G475..., G482... "ADVISOR PAYS"), carry no account.
- **Two consequences, if Fidelity's own export behaves the same (unmeasured until the first per-G read):**
  1. A pull per G number returns most accounts twice (under PRIMARY and SECONDARY), so the landing needs a count-once rule.
  2. The advisor G numbers do not carry the advisor books. Black Diamond's Portfolio Group puts 431 accounts with Rubottom, 239
     with Bass and 228 with Shipley; the advisor G numbers hold 2, 1 and 0.
- Filed as `NFRA_FIDUPL-D1-S6` (commit b61902c5bb).

### F4. The Commonwealth history, and the stitch that already exists [DATA]

- **History:** 1,416,497 transactions across 1,533 accounts, 2013-04-03 to 2026-06-22; 88,654 performance rows; positions on one
  day, 2026-06-23 (`silver/coverage/date=2026-06-23/coverage.json`).
- **The crosswalk** (`silver/crosswalk/date=2026-06-23/`) already maps Commonwealth accounts to current accounts: 471 MATCHED by an
  in-kind-transfer rule (positions equal within 0.001, an 80% bar), 1,062 NOT_MATCHED (770 with no current account holding the
  positions, 188 closed before the current history, 44 with no security positions, 38 ambiguous, 22 awaiting a person).
- **Its current side is Fidelity:** 457 of the 471 matched current accounts are Fidelity IWS accounts in Black Diamond's 2026-10-19
  export (of 647). The transfers cluster on 2026-05-19 to 2026-06-11, the move.
- **But its current side was read from Black Diamond:** the "current account's first holdings (2026-06-30)" evidence is Black
  Diamond holdings [CODE, from the evidence strings]. Without Black Diamond, the crosswalk has to be re-run against Fidelity's own
  positions once they land. The rule itself carries over unchanged.
- **`account_links`** (1,450 rows) chains old to newer accounts: 212 LINKED, 12 whose newest account is open.

### F5. Linking one client across custodians [DATA + BD-CHECK]

- **Black Diamond's way (check only):** 227 Relationship IDs; 51 span two or more custodians.
- **Non-Black Diamond keys that exist:**
  - Commonwealth's CRM: 270 households and 676 contacts as of 2026-06, with tax IDs in the contacts file (the sensitive-field
    decision of the 2026-10-06 brief, O7). With the crosswalk this reaches the 457 matched Fidelity accounts.
  - Custodian account titles and registration: Schwab silver carries title lines; what the Wealthscape export carries per account
    is not yet measured.
- **Gap:** Schwab and Strata accounts have no Commonwealth link, and accounts opened after the move have none. No Opal-owned client
  key exists yet for them.

### F6. The Commonwealth rep code partly tracks the advisor books [DATA + BD-CHECK]

For the 462 matched accounts whose Commonwealth rep code is known, compared with Black Diamond's Portfolio Group:

| Commonwealth rep code | Bass | Rubottom | Shipley | No Advisor |
|---|---|---|---|---|
| S58 | 99 | 1 | 0 | 0 |
| HKE | 0 | 11 | 0 | 0 |
| HKJ | 31 | 203 | 107 | 10 |

- S58 is Christa Bass's book almost exactly. HKJ is a shared rep code covering all three advisors.
- So no custodian or Commonwealth code alone gives Rubottom and Shipley apart. **The advisor assignment is Cottonwood's own
  decision, today recorded only in Black Diamond's Portfolio Group.** A BD-free book needs that assignment from Cottonwood
  directly, held in Opal (Part V).

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

Named, not sequenced:
- **Fidelity lands.** The NFRA_FIDUPL sign-in works, the per-G pulls run, and the backfill reaches as far back as Fidelity allows,
  with a count-once rule for accounts under two G numbers (F3).
- **The Schwab masters arrive** (Andrew, from Mike Little) and become daily pulls in the canonical Schwab pipeline, with registry
  rows for Cottonwood's masters.
- **Strata is clarified** (Andrew's Q2: "We need to clarify that"): how Black Diamond receives Strata today, and whether Opal can
  receive the same file. Until then Strata is a named gap of 8 accounts and $2.0M, never estimated.
- **A home for the 15% with no custodian** (F1): manual and alternative positions, and held-away accounts. That means an Opal-owned
  manual entry or upload, an aggregator feed of Opal's own, or an explicit "not represented" line. This is Andrew's decision, not a
  build default.
- **An advisor assignment Cottonwood owns,** held in Opal (F6). It could be seeded once from Black Diamond's Portfolio Group,
  provided it is then confirmed by Cottonwood and maintained outside Black Diamond. Whether that seeding counts as a "dependency" is
  Andrew's word.
- **The crosswalk re-run against Fidelity's own positions** (F4), so the stitch has no Black Diamond input.
- **The sensitive-field decision** from the 2026-10-06 brief (tax IDs in silver or not), if tax IDs become the client key (F5).
- **The firm scope rows** for Cottonwood (NFRA_FIDUPL C-NAMES), so every Cottonwood file lands under its own prefix.

## PART VI -- STATUS (NOT OUTCOME-BEARING)

Measured 2026-10-20 13:4xZ to 13:5xZ:
- `opal-data-assets/fidelity/` is empty; NFRA_FIDUPL is EXECUTING, with no landed file.
- Schwab: 3 masters landed daily, none of them Cottonwood's.
- Commonwealth: 12 silver tables, as-of 2026-06-23 (landed 2026-10-06/07).
- Black Diamond Cottonwood: allocations pull of 2026-10-19 landed 07:31; accounts dimension rebuilt 2026-10-20 07:35 (1,005
  accounts; Portfolio Group Rubottom 431, Bass 239, Shipley 228, No Advisor 106, NULL 1).
- The 2026-10-17 endpoint (FWD-1..6) is open call 0cf5's subject; Andrew answered it with this re-frame.

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- **No Fidelity file was read.** F3's rep codes are Black Diamond's copy; what Wealthscape returns per G number, and what it carries
  per account (titles, tax ID, advisor), is unmeasured.
- **The Strata feed was not traced.** Its mechanism into Black Diamond is unknown.
- **The 20 Schwab accounts were not matched to any master number;** only their absence from Opal's three masters was measured.
- **Not checked:** whether the held-away Fidelity and Schwab retail accounts (12, F1) would appear in any G number or master;
  whether the 1,062 unmatched Commonwealth accounts include current clients at Schwab or Strata.
- **The dollar figures are Black Diamond's market values** for one day. They size the classes; they are not Opal's numbers.
- **No client name, account number or full G number is written here.** Counts are class-level; G numbers are masked as in the
  Andrew-direct record.
- **Nothing was changed** in any pipeline, served table or page. One surprise row was filed (F3).

---

## REFS

```
  BRIEF PATH        docs/briefs/advi-cotbooks-custodian-first-rebrief-20261020.md
  PROJECT           ADVI_COTBOOKS (org/missions/D8/ADVI/ADVI_COTBOOKS/project.json)
  SUPERSEDES        docs/briefs/advi-portfolio-group-key-cottonwood-ai-brief-20261017.md @1bae264b34
                    org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_ADVI_COTBOOKS_20261017.md (on re-cut)
  ANDREW'S WORDS    org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261020_133xZ_COTBOOKS_NO_BD_DEPENDENCY_CUSTODIAN_FIRST.md @7fb4f70e80
  EXISTING PRD      org/missions/D8/ADVI/ADVI_COTBOOKS/prd/ADVI_COTBOOKS_PRD.md (to be re-cut)
  SIBLING PROJECTS  NFRA_FIDUPL (Fidelity landing, C-BACKFILL, FWD-9, C-NAMES); the Commonwealth backfill
                    (docs/briefs/cottonwood-commonwealth-10y-backfill-brief-20261006.md); canonical-schwab-ec2;
                    ADVI_COTBKF (comparison only)
  PRIOR ART         s3://opal-data-assets/commonwealth/cottonwood/silver/{crosswalk,account_links,coverage}/date=2026-06-23/
                    s3://opal-data-cot/forwardfill_v2/allocations/ (BD check: Custodian, Data Provider, Rep Code)
                    s3://opal-data-cot/gold/dimensions/accounts_dimension_latest.parquet (BD check: portfolio_group)
  SURPRISE ROW      NFRA_FIDUPL-D1-S6 @b61902c5bb
  MEASURED AT       2026-10-20 13:4xZ to 13:5xZ (BD pull 2026-10-19; Schwab dim_balance 2026-10-19; Commonwealth as-of 2026-06-23)
```
