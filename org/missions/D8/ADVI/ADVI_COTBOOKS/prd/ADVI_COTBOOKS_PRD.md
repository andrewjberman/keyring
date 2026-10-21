# ADVI_COTBOOKS -- Cottonwood's whole book from its custodians, with no Black Diamond dependency: the first case study for replacing Black Diamond

```json
{
 "project": "ADVI_COTBOOKS",
 "directive": "D8",
 "fabric": "dell1",
 "prd_version": "v0.4",
 "step": 4,
 "brief_ref": "docs/briefs/advi-cotbooks-custodian-first-rebrief-20261020.md@0084b77c06",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7", "FWD-8"],
 "status": "DRAFT"
}
```

**Author:** `1.0.0_SA_CTO~DELL1`, v0.4 2026-10-21 ~16:4xZ (v0.1 2026-10-17 ~03:2xZ under the retired v1 endpoint).
**Placement:** DELL1, directive D8, macro ADVI. Registered @5a2f71d0cc.

**Records (Andrew-direct):**
- **2026-10-20 ~13:1xZ to 13:3xZ at this terminal,** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261020_133xZ_COTBOOKS_NO_BD_DEPENDENCY_CUSTODIAN_FIRST.md`
  @7fb4f70e80, VERBATIM: "we cannot rely on Black Diamond for any critical function ... we want Cottonwood to be our first true case study
  where we figure out how to represent all their stuff without having any BD dependency"; "backfill off the G Numbers and create daily
  pulls per each G Number"; "Yes we can compare to BD."
- **2026-10-17** (`2.0.0_SA_COO~C1` records @cdad0d5031): "should be taking on the Inflection Shape visually"; "yeah we do need to figure out
  that portfolio group stuff". These words survive in FWD-5 and FWD-8 of v2.
- **2026-10-21 15:57Z email** ("Re: BD Replacement Demonstration", to Manav and Yang): STATUS only, see change log v0.3.

**Endpoint status:** v2 written at L2 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_ADVI_COTBOOKS_20261020.md`), superseding
the 2026-10-17 FWD-1..6 (ids retired, never reused). Andrew's confirmation of the eight lines and the carried RECs is the open-calls act
`dell1-20261020T135705Z-ea86`. This PRD goes to L4-R only after he confirms; if he changes a line, ENDPOINT is re-pasted here.

**The rule that binds every line:** a Black Diamond read is allowed only in a column labelled as the comparison. A Black Diamond read
anywhere else on an outcome's path fails that outcome.

## ENDPOINT (step 2, /endpoint --forward)

```
  FWD-1  An analyst reads Cottonwood's Fidelity book for one day from Fidelity's own files
         DONE WHEN  EXERCISED -- on demand, for one stated business date, read from the
                    Fidelity landing under Cottonwood's own prefix: every account under
                    Cottonwood's G numbers counted once, with its holdings, cash and value;
                    the total printed beside Black Diamond's Fidelity figure for that date,
                    with every difference named
         ACCEPT     An analyst can say what Cottonwood holds at Fidelity on a given day, and
                    which Fidelity file each number came from, without opening Black Diamond
         SOURCE     brief Part I thread, O1, F3 (an account under two G numbers counts once)

  FWD-2  One Cottonwood account reads as one history, from Commonwealth to today
         DONE WHEN  EXERCISED -- one matched account's history is read end to end, from
                    2013 through the move to today. The Commonwealth-to-Fidelity link is
                    re-made against Fidelity's own positions, not Black Diamond's holdings,
                    and the join date shows
         ACCEPT     An analyst follows one client's account from Commonwealth into Fidelity
                    without switching tools, and can see the day it moved
         SOURCE     brief O2, F4; Andrew "stitch the commonwealth books to the fidelity
                    backfill"

  FWD-3  An analyst reads Cottonwood's Schwab accounts from Schwab's own files
         DONE WHEN  EXERCISED -- for one stated date, the Cottonwood Schwab accounts are read
                    from the canonical Schwab landing, beside Black Diamond's Schwab figure
                    for that date, every difference named.
                    QUALIFIED WAIT: the advisor master account numbers come from Alongside
                    (Andrew-direct 2026-10-20: "i am going to get those from Mike Little at
                    Alongside today"); the lane opens when they land
         ACCEPT     The Schwab part of the book reads the same way as the Fidelity part
         SOURCE     brief O3, F2 (0 of 20 in Opal's masters today)

  FWD-4  A person sees how much of Cottonwood's book Opal reads, and what it does not
         DONE WHEN  EXERCISED -- for one stated date, a coverage statement in accounts and
                    dollars for each class (Fidelity, Schwab, Strata, manual and
                    alternative, held-away), with every class Opal does not read named
                    beside its size on the same screen
         ACCEPT     No one mistakes a Cottonwood total for the whole book when a class is
                    missing
         SOURCE     brief O4, F1 (about 15% has no custodian feed); Strata a named gap

  FWD-5  Every Cottonwood account sits in one advisor's book, by an assignment Opal holds
         DONE WHEN  EXERCISED -- read on Opal's own advisor assignment for one date: every
                    account in exactly one book, none lost; Black Diamond's Portfolio Group
                    read beside it as the check, with each disagreement listed
         ACCEPT     The advisor books do not change if Black Diamond goes away
         SOURCE     brief O6, F3, F6 (no custodian or Commonwealth code separates
                    Rubottom from Shipley)

  FWD-6  One client's accounts across custodians are seen together
         DONE WHEN  EXERCISED -- one household with accounts at two custodians is read
                    under one Opal-owned client key, not Black Diamond's Relationship ID
         ACCEPT     A person sees a client's whole relationship in one place
         SOURCE     brief O5, F5

  FWD-7  Per custodian, the gap to Black Diamond is explained
         DONE WHEN  EXERCISED -- for one stated date, Opal beside Black Diamond for each
                    class, in accounts and value, with every difference given a named cause
                    (timing, an account one side lacks, pricing, a class Opal does not read)
         ACCEPT     The only differences left are ones someone can explain: the
                    replacement test
         SOURCE     brief O7, Part III replacement test

  FWD-8  A Cottonwood admin reads the firm as its advisors' books on Advisor Intelligence
         DONE WHEN  EXERCISED -- one live trace on a real admin login at a stated portal
                    commit: the first screen lists the advisors and their books, fed by
                    FWD-1 to FWD-5; one click reaches one advisor's clients; the page names
                    its books' date; an advisor login sees only its own book, and a request
                    for another's is refused; the tabs follow Inflection's layout
         ACCEPT     The Cottonwood page works like Inflection's, and every figure on it
                    traces to a custodian file
         SOURCE     brief O8 (the 2026-10-17 page outcomes); Andrew 10-17 "should be taking
                    on the Inflection Shape visually"
```

## CONTRACTS

| row | owner | rule | proven by |
|---|---|---|---|
| C-NOBD | every cell | **A Black Diamond read appears only in a column labelled as the comparison.** No book figure, assignment, client key, history link or page value is computed from a Black Diamond table; the comparison columns are produced by a separate reader whose output is never joined back into the figure it checks. Every served table carries a `source_file` column naming the custodian file (or the Opal-owned table) each value came from. | the lineage of every figure on FWD-8's page traces to a custodian file or an Opal-owned table; a BD read off the comparison column fails the cell |
| C-FIDELITY | the Fidelity book cell | **Cottonwood's Fidelity book is read from NFRA_FIDUPL's landing** (`address('fidelity', 'cottonwood', 'bronze', ...)` once the per-G split lands; until then the full pull under `fidelity/alongside/bronze/` filtered by Cottonwood's account roster, C-ROSTER-G). **Count-once:** an account under two Cottonwood G numbers (PRIMARY and an advisor's) is one account (surprise row D1-S6). Holdings, cash and value come from `position`, `balance` (or the Historical `position_balance_fl`) and `prices` files by content date. | FWD-1's one-day read: accounts in = accounts out, each once, each with its file |
| C-ROSTER-G | the roster cell (precondition of FWD-1) | **The Cottonwood account roster per G number is Opal-held data,** read once from Wealthscape's G-number context by the NFRA_FIDUPL agent session (read-only, no export, the numbers kept off git) and refreshed on each daily pull. **QUALIFIED WAIT:** if the G context yields no account list, the per-firm Groups in Wealthscape are the precondition (Andrew's act, CTO ruling @4c536cb554), and FWD-1 waits on it with that reason stated. | the roster's row count per G number, printed beside the Wealthscape screen's count for that G |
| C-SCHWAB | the Schwab book cell | **Cottonwood's Schwab accounts are read from the canonical Schwab landing** under the Cottonwood masters once those masters are registered (Andrew's Alongside word; Schwab access granted 2026-10-21). The same count-once and `source_file` rules. | FWD-3's one-day read |
| C-HISTORY | the stitch cell | **The Commonwealth-to-Fidelity link is re-made against Fidelity's own positions** (brief F4's stitch), never against Black Diamond holdings; each matched account carries its `join_date` and the matching rule that joined it; an unmatched account is listed, never forced. | FWD-2's end-to-end read of one account, 2013 to today, with the join date |
| C-COVERAGE | the coverage cell | **One coverage statement per date, per class:** Fidelity, Schwab, Strata, manual and alternative, held-away; accounts and dollars read, and accounts and dollars NOT read, each class named with its size. The Strata size is recorded from BOTH Andrew's statement (~$60M, email 2026-10-21) and Black Diamond's direct feed ($2.0M, 8 accounts), labelled, neither adopted until he clarifies (REC 3). | FWD-4's statement for one date, classes summing to the whole |
| C-ASSIGN | the assignment cell (this project) | **The advisor book is an Opal-owned assignment table** (`account -> advisor_id`, with `book_rule` and `shared_with`), in Cottonwood gold, written by this project. **Seeded once** from Black Diamond's Portfolio Group as a one-time import (REC 2, carried to Andrew), then maintained by Opal; after the seed, Black Diamond's group is read only as FWD-5's comparison column. Determinism for the seed and for any later ambiguity: (1) a named advisor group beats "No Advisor"; (2) an account in two named advisor groups takes the advisor holding most of the other accounts in the same client relationship (C-CLIENT), ties by advisor name ascending; every account in exactly one book, none lost. | FWD-5's read: 0 accounts in two books, 0 lost; the disagreements with BD's group listed |
| C-CLIENT | the client-key cell | **One Opal-owned client key across custodians** (household), never Black Diamond's Relationship ID; built from the custodians' own household or registration fields where they exist and from the C-ASSIGN seed otherwise, with the rule that made each link stated on the row. | FWD-6's one household at two custodians under one key |
| C-COMPARE | the comparison cell | **Per class and per date, Opal beside Black Diamond, every difference given a named cause** (timing, an account one side lacks, pricing, a class Opal does not read). The comparison reader is the only Black Diamond reader in the project (C-NOBD). | FWD-7's explained gap for one date |
| C-SCOPE | all | **Books cover the supervised book only** (MDPF_CANON FWD-10, Andrew-direct 2026-10-17 ~01:5xZ); unsupervised accounts appear in no book; the book totals sum to the page's firm total to the cent. | the sum of the book totals equals the page's firm total |
| C-LEADERBOARD | the leaderboard cell | **Advisor-grain figures over the C-ASSIGN partition** (AUM, clients, accounts, net flows), at the contract the Inflection page reads; an overlap sum is never shown as a total. | the served leaderboard; rows sum to the firm total |
| C-PAGE | the page cell | **The Cottonwood page takes Inflection's arrangement** (admin tabs Advisors, Distribution, Books; non-admin Distribution and Profile); the first tab is not a list of every account; Inflection's components reused, not copied; the page names its books' date (the custodian files' content date). | the page at a stated portal commit on `bun run dev:live --port 5174` against live services |
| C-AUTHZ | the page cell | **Own-book guard server-side** (ADVI_PARTNER_AUTHZ pattern): an advisor login reads only its own `advisor_id`. | a request for another advisor's book, refused at the service |
| C-ROSTER | the roster cell; Andrew (the mapping) | **Each Cottonwood login maps to one `advisor_id`;** which login is which advisor is supplied by Andrew; nobody contacts Cottonwood. | the map's rows; a login without a row sees no Profile tab |
| C-NAMES | all | Cottonwood gold is an existing pipeline in `opal-data-cot` (rule 30 non-application: no new bucket, no new address); every Fidelity and Schwab READ address is `lib/opal_naming.py address()` output. | `address()` printed in each reading cell's proof |

## THE DECISIONS -- CLOSED AT L4

1. **Custodian-first, Black Diamond as the comparison only (C-NOBD):** Andrew's 2026-10-20 word, taken literally. Every v1 contract that
   made Black Diamond a source (the old C-BOOK "a book is a Portfolio Group", C-RULE's `Primary Portfolio Group` step, C-OWNER's
   `A_00` writer, C-TIEOUT, C-FRESH's "newest pull") is retired with the v1 endpoint.
2. **The assignment is Opal's (C-ASSIGN), seeded once:** REC 2 is carried to Andrew with the endpoint; the seed is the only Black Diamond
   read outside a comparison column, it runs once, and its import is recorded.
3. **The Fidelity book reads FIDUPL's landing (C-FIDELITY):** this project pulls nothing; the per-G split and the roster are FIDUPL's
   journey and Andrew's Groups act. The round-1 fallback (full pull filtered by the roster) keeps FWD-1 exercisable before the split.
4. **Round 1 is FWD-1:** one day of Cottonwood's Fidelity book, counted once, beside Black Diamond's Fidelity figure.
5. **Out of scope:** 49 Financial's books; any change to MDPF pages; contact with Cottonwood, Black Diamond or Fidelity staff; billing
   and trading; the Investor Reporting view/export surface (enrichment candidate, change log v0.3).

## OPEN AT ANDREW (acts only he can do)

- **ea86:** confirm the eight DONE WHEN lines and the two carried RECs (REC 1: the ~15% with no custodian feed shown as a sized "not read"
  line; REC 2: seed the assignment once from Black Diamond). REC 3 (Strata) is his clarification, carried.
- **The Schwab advisor master account numbers** from Alongside (FWD-3's qualified wait, his word 2026-10-20).
- **Per-firm account Groups in Wealthscape** if C-ROSTER-G's G context yields no roster (CTO ruling @4c536cb554).
- **The login-to-advisor mapping (C-ROSTER)**, and the **client-facing PROD** promote of the Cottonwood page (CLAUDE.md, PUSHES).

## CELL CANDIDATES (round 1 builds the FWD-1 thread; the issuer decomposes)

0. **Prerequisite (NFRA_FIDUPL, read-only in its agent session):** the Cottonwood account roster per G number (C-ROSTER-G), landed as
   data off git; or the QUALIFIED WAIT named.
1. **The Fidelity book reader** (C-FIDELITY, C-NOBD, C-NAMES): one stated date from the landing, count-once, holdings, cash and value
   with `source_file` on every row.
2. **The Fidelity comparison column** (C-COMPARE, first use): Black Diamond's Fidelity figure for the same date read by the separate
   comparison reader, every difference named. This completes FWD-1's trace.

Later rounds enrich: the stitch (FWD-2), the Schwab book when the masters land (FWD-3), the coverage statement (FWD-4), the seeded
assignment and client key (FWD-5, FWD-6), the explained gap (FWD-7), the page (FWD-8).

## PATHS

- **This project:** `org/missions/D8/ADVI/ADVI_COTBOOKS/`.
- **Read by the issuer at HEAD before the first cell:** `org/missions/D8/NFRA/NFRA_FIDUPL/prd/NFRA_FIDUPL_PRD.md` C-TENANCY and C-BACKFILL
  (the landing and its dates); `lib/opal_naming.py`; `data/cot/scripts/gold/A_00.accounts_dimension.py`, `A_01.advisor_assignments.py`,
  `D_05.supervised_split.py`, `lib/supervised_scope.py` (what today is BD-fed, to be replaced, never extended);
  `portal/src/pages/AdvisorIntelligence/_partners/cottonwood/index.tsx` and `.../inflection/index.tsx`; the brief's F1-F6 tables.

## SURFACE MANIFEST

- **AWS:** Cottonwood gold in `opal-data-cot` (existing pipeline); new tables (the book, the roster, the assignment, the client key, the
  coverage statement, the comparison) under the existing gold prefix, the issuer naming each against the existing layout. Reads from
  `opal-data-assets` Fidelity and Schwab landings by builder address.
- **Portal:** the Cottonwood Advisor Intelligence page, DEV first; PROD is client-facing (Andrew).
- **Repo:** this tree; no change to ADVI_COTBKF's writers (the BD-fed `A_00`/`A_01` are read for the seed only).

## CHANGE LOG

- **v0.1 (2026-10-17 ~03:2xZ):** first draft under the v1 endpoint, while Andrew's confirmation (0cf5) was held.
- **v0.2 (2026-10-17 ~03:3xZ),** on `3.0.0_SA_CVO` REFUSE @8cc7a87a60: v1 FWD-2 read "every account in Cottonwood's supervised book".
- **v0.3 (2026-10-21 ~16:3xZ, `1.0.0_SA_CTO~DELL1`), RULING on `4.0.0_SA_CRO~DELL1` 9137 (brief Part VI addendum @0084b77c06):** Andrew's
  2026-10-21 15:57Z email ("Re: BD Replacement Demonstration", to Manav and Yang, not addressed to this fabric) is read as STATUS, and
  endpoint v2 (ea86) is NOT changed before he confirms it. (a) Strata at "~$60M" against Black Diamond's $2.0M direct feed is a
  measurement for FWD-4's sized "not read" line at L7; his figure is recorded beside the feed's, neither adopted. (b) "Holdings keeps
  Black Diamond" names the model and sleeve data of a different product; no BD dependency of a Cottonwood book outcome. (c) The
  December 1 internal-test target and an "Investor Reporting" page with view AND export are enrichment candidates for a later round or
  an FWD-9; they enter the endpoint only on a word of his to this fabric (CLAUDE.md section 2, verbatim scope). Schwab access for
  Cottonwood granted 2026-10-21 is FWD-3's access precondition met; the masters remain the qualified wait.
- **v0.4 (2026-10-21 ~16:4xZ, `1.0.0_SA_CTO~DELL1`), on `3.0.0_SA_CVO~DELL1` REFUSE @cfd85ff54b (review @1d11ff88d8):** the PRD is
  re-issued on endpoint v2 -- the eight v2 outcomes pasted verbatim, the status pointed at ea86, the brief pinned to the v2 re-brief, and
  every CONTRACT re-read under the no-BD rule (C-NOBD; C-ASSIGN replaces C-BOOK/C-RULE/C-OWNER; C-COMPARE replaces C-TIEOUT; C-FIDELITY,
  C-ROSTER-G, C-SCHWAB, C-HISTORY, C-COVERAGE, C-CLIENT new). Delivered to L4-R after Andrew answers ea86.

-- 1.0.0_SA_CTO~DELL1
