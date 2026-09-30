# One canonical per-security table for every holdings surface -- L1 brief, 2026-09-29

**Mode:** NEW (greenfield project; the substrate exists, the project does not). **By:** 4.0.0_SA_CRO on the CTO's placement
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_PLACEMENT_20260929_182xZ_ONE_CANONICAL_SECURITY_TABLE.md`, part (c): "Retiring
`bd-securities` and the ~15 copies is a NEW PROJECT, through the canonical workflow. L1 brief by `4.0.0_SA_CRO`, from the census
in the record."). **Andrew's words** (verbatim, recorded by 2.0.0_SA_COO~D,
`org/tier1_exec/2.0.0_SA_COO~D/deliverables/ANDREW_DIRECT_20260929_175xZ_ONE_CANONICAL_SECURITY_TABLE_FOR_ALL_HOLDINGS.md`
@099316efdd):

> "the table that feeds positioning should feed ALL HOLDINGS. Which means that is our canonical table for all holdings info, so
> that is where we feed in a row per security, including asset class, sub asset, and so on"

> "Better to use that table as a shared source for this kind of thing so we dont have duplicated tables and rules laying around.
> thats why i call it 'Canonical'"

**Consumer:** `/endpoint --forward` at L2 (1.0.0_SA_CTO). Every outcome below is numbered and citable; status lives in Part VI and
is not outcome-bearing.

**Not in this brief (placed elsewhere by the CTO, same record):** (a) Investor Reporting's producer reading the canonical table
now, as an IRPT_BCKEND ~M cell; (b) the PHYS row through the seed source, same cell; (d) the portal half (single stocks ordered
after the last ETF class), 2.0.0_SA_COO~D. This project starts at L1 now and does not block (a).

---

## PART I -- THE OUTCOME TERRITORY

The canonical table is DynamoDB `etf-classifications` (hash key `ticker`; `asset_class`, `sub_asset_class`, `sector`, `name`,
`management_style`), seeded from `infra/aws/lambda/v2_portal/_shared/etf_classification.py` by
`infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py`, read through
`infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py`. The project's territory is every OTHER place a ticker is
assigned an asset class or sub-asset, and the fork table `bd-securities` those places grew around.

### O1 -- The candidate thread (FWD-1): Black Diamond's own holdings surfaces answer from the canonical table

A Black Diamond reader (the advisor-facing composition artifacts and the client portal summary that the BD gold chain serves)
opens a client's holdings and sees the class and sub-asset the canonical table holds for each ticker -- GLD and PHYS as
Commodities / Metals, VXX as Structured / Hedge -- with no `bd-securities` read anywhere on that chain. **Why this thread:**
`bd-securities` is Black Diamond's fork (seeded from the canonical table by `seed_bd_securities.py`, then drifted); the BD chain
is where the copies are densest (classifier library, assets dim, composition artifacts, new-security detection and
classification, canonical prices); one firm, one served surface, the default as-of day. Round 1 builds it end to end; the other
outcomes are enrichment rounds.

### O2 -- A person asks "what class is ticker X in Opal's holdings?" and gets ONE answer, anywhere they look

Whether they open Investor Reporting Holdings, Positioning Models or Satellites, a Black Diamond, Cottonwood or Inflection
composition artifact, the 49F asset dimension, a partner's data feed, the market overview, or holdings attribution, the class
and sub-asset for a ticker are the canonical row's. A ticker that has no row is shown as unclassified BY NAME, never silently
folded into a class by a local rule.

### O3 -- A person corrects or adds a security in ONE place and every surface follows

Adding or changing a row happens in the seed source, the seed path writes the table, and every surface in O2 shows the new
value after its next run. Nobody edits a second file, a second table, or a hand `put-item`. The PHYS row (placed in cell (b)) is
the first proof of this path; the project makes it the only path.

### O4 -- An engineer can prove there is no second definition

A census over the repo for ticker-to-class assignments outside the canonical package reads zero (the pattern `lib`'s `ids.py`
already sets for account ids: "ONE DEFINITION. The grammar lives HERE and nowhere else. A census ... outside this package reads
0"). The census is a repeatable instrument with a printed denominator, run at each round's close, not a one-time list.

### O5 -- `bd-securities` is gone, and its going is provable

The table has no reader (the O4 census plus the live IAM grants that name it), its last readers were moved under never-widen
halves with a before/after read of every served figure that moved, and the table is deleted on Andrew's confirmation as the
destructive act it is -- with the seed-and-drift record kept, so the drift's values are recoverable if a figure is disputed.

### O6 -- A rule that must differ from the canonical table is declared, not hidden

Where a surface legitimately classifies from another authority (Positioning's ETFs mode reads Bloomberg GICS fields; the Schwab
gold reads Schwab as security master), that departure is written down with an owner and a reason, and a reader can tell "canonical
row" from "declared departure". A fold like the classifier's `hedge -> alternatives` or a lambda's `VXX = equity` is not a
departure; it is a copy, and it goes.

### O7 -- A security that appears in a day's holdings gets its canonical row without a person noticing it first

When a new ticker lands in any firm's holdings (a day-over-day draw), the canonical table gains its row -- asset class and
sub-asset -- on a scheduled path, so no surface shows "Other" or "unclassified" for longer than the schedule's own gap; a
one-off backfill of today's "Other" rows is the QA run that proves the path, and the scheduled run is the acceptance. Andrew,
walk 2 of 2026-09-29 (transcript `tmp/ui-guidance/20260929/IRPT WALK 2_2309.txt` l.94-96, [564-609 s]): "we will need to add a
new row in that canonical table and draw from that canonical table ... not only run an ad hoc run, but also likely structure a
continuous pipeline as new securities become apparent in day-over-day draws so that the table ... can have representations that
are accurate for the sub-asset classes for the incoming securities." Where that classification calls a vendor model, the call is
Andrew's per-use word at the PRD, never a default of the pipeline.

### O8 -- A reader can tell an ETF from a single security from the canonical row itself, and a table orders them accordingly

The canonical row carries whether the instrument is an ETF (or fund) or a single security, so a holdings table can keep one
sub-asset gradient for ETFs and place single securities after the last ETF class without a second rule in the portal. Andrew,
same walk (l.102-105, [648-677 s]): "individual securities should be marked as such. That likely should be a field in that
DynamoDB table. If it is an ETF or an individual security, individual securities are always secondary ... And that is then we can
reuse the same gradient logic with regard to the sub-asset taxonomy." The ORDER is the portal half's (placement (d)); the FIELD
is this project's.

Expect these eight; O1 is the thread and O2-O8 are what the enrichment rounds serve. Decomposition into cells is L5's, not this
brief's.

---

## PART II -- WHERE THE BOUNDARY SITS

**This project owns:** every ticker-to-class assignment outside the canonical package (the copies), the `bd-securities` table and
its IAM grants, the O4 census instrument, and the declared-departure register of O6.

**This project relies on, and does not own:**
- **The canonical table, its seed source and client** -- POSN_ASTTAX's product (closed 2026-09-15; C-ONE-SOURCE, C-FIVE-CLASSES),
  extended here from two Positioning surfaces to every holdings surface. A change to the table's SHAPE is POSN_ASTTAX's
  successor, not this project.
- **Cell (a)+(b): Investor Reporting's producer onto the canonical table and the PHYS row** -- IRPT_BCKEND, 2.0.0_SA_COO~M, landing
  before the COT holdings re-point (S173). This project starts after or beside it and never re-does it.
- **The portal half** -- DSGN_IRPTV1 / 2.0.0_SA_COO~D: `SecurityList.tsx` reads the served sub-asset; single stocks ordered after the
  last ETF class. The portal's own ticker constants (`etf-categories.ts`, `HoldingsBreakdownTable.tsx`) are IN this project's
  territory as copies; the display order is NOT.
- **Each firm's pipeline tree** -- the CTO's (c): "Reference data shared across firms is not firm data, so the cross-firm rule does
  not bar it. Every pipeline still keeps its own firm tree." Each copy reaches the canonical table through that pipeline's own cells,
  never as a rider on another project (the shadow-migration shape the law forbids).
- **Bloomberg-sourced classification** (Positioning ETFs mode) and the **Schwab security master** -- named in O6 as candidate
  declared departures; whether either joins the canonical table is the CTO's call at L2, not scoped here.

**Sibling projects named:** POSN_ASTTAX (closed), IRPT_BCKEND (cells (a)+(b)), DSGN_IRPTV1 (portal half), ETFS_CANON / ETFS_POSITIONING
(Bloomberg-side classification), the D14 LGIC migration projects (names and homes; see Part V).

---

## PART III -- THE QUALITATIVE BAR

- **One answer:** a developer asked "where does ticker X's class come from on surface Y" names one table and one seed file, and is
  right for every surface -- they do not open a second file to check.
- **One edit:** an engineer who corrects a row does not open a pull request in a second repository tree to keep a copy in step, and
  no surface shows the old value after its next scheduled run.
- **Zero by census, not by belief:** the O4 census is what says "none left"; a sentence with NEVER or EVERY in it cites the
  census's denominator.
- **A moved figure is read, not predicted:** for each surface moved, the classes that change are listed by ticker before the move
  and read back after it on the served artifact.
- **Nothing silently folds:** a ticker without a row reads as unclassified on the face, in words a reader understands.

No numbers are set here. Counts of copies and files are measurements (Part VI), not targets.

---

## PART IV -- THE SUBSTRATE: is this in a canonical pattern?

Findings, each with what was measured:

1. **The canonical table and its ONE-SOURCE rule already exist and are ratified.** POSN_ASTTAX (`org/missions/D4/POSN/POSN_ASTTAX/project.json`,
   status closed, dep_stage CLOSED) owns "the five-class taxonomy ... one central source that flows ... every surface reads that one
   classification rather than re-deriving it" -- for the two Positioning surfaces. Live rows read by ~D's trace 2026-09-29: GLD =
   commodities / Metals (sector Gold); VXX = structured / Hedge; PHYS no row. This project is the same rule at estate width.

2. **The fork is measured and its drift is measured.** ~D's record: `bd-securities` was seeded from the canonical table
   (`data/black_diamond/scripts/classification/seed_bd_securities.py:21-22`) and now holds GLD, PHYS = alternatives / Gold and VXX =
   alternatives / Volatility; the classifier folds `hedge` into `alternatives` (`data/black_diamond/scripts/gold/lib/etf_classifier.py:99,108`).
   A second seeder, `seed_canonical_securities.py`, writes BOTH tables and sets VXX = equity / Volatility -- three values of one ticker
   across three writers.

3. **The copies are enumerated with file:line (~D's census, the CTO's "~15"), and this seat's own token census bounds them.** ~D lists:
   `bd-securities` readers (BD and COT `etf_classifier.py`, `runners_49f/a07_dim_asset_classification.py:58,220`, `build_bd_assets_dim.py:154`,
   `D_03.composition_artifacts.py:116`, `seed_canonical_securities.py`); Lambda copies (`partners/lambdas/opal-partners-data/etf_classification.py:230,235`
   with VXX = equity and GLD = other, and its `etf_classifier.py:9`; `yang-generate-etf-returns/etf_classification.py:115`;
   `yang-generate-holdings-attribution/etf_classifications_dynamodb.py`, a second client copy; `market-overview-tiered-generator/lambda_function.py:67`;
   `yang-generate-positioning/lambda_function.py:324`, an alias map); `lib/research/identity/positioning_chain.py:163`; front end
   `portal/src/pages/Positioning/constants/etf-categories.ts:11-66` (UVXY = Equity / Volatility) and `portal/src/components/holdings/HoldingsBreakdownTable.tsx:69,129`;
   deliberately separate `data/canonical/schwab/gold/build_gold_firm_composition.py:7`. This seat's token census (native grep, code
   files only, tokens `bd-securities|etf_classifier|etf_classification`, 2026-09-29 18:4xZ): `data/` 44 files / 151 hits, `infra/` 46 / 111,
   `portal/src` 6 / 16 (with `etf-categories|getSubAssetClass`), `lib/` 2 / 4. The token census is wider than the copy list (it counts
   the canonical package, tests, manifests and terraform too); it is the denominator the O4 instrument will subtract from, not the copy count.

4. **The ONE-DEFINITION pattern with a census that reads zero is already built for another key.** `lib`'s `ids.py` (shipped in the
   investor-reporting artifacts) states it as its contract: "ONE DEFINITION. The grammar lives HERE and nowhere else. A census of the
   grammar outside this package reads 0." O4 reuses the pattern, not the code.

5. **Copies live in three serving shapes, and each is deployed differently:** scheduled Python gold/silver pipelines per firm (BD, COT,
   INF, 49F, assets), Lambda artifacts with vendored module copies (yang-pipeline positioning / portfolios / holdings attribution,
   partners, market overview) whose deployed bytes are diffed against their build input (source maps under `infra/aws/lambda/ci/`), and
   the portal bundle. A "port" therefore has three mechanics, which is why the CTO placed it as a project with cells per pipeline rather
   than one edit.

6. **Retirement is a served move at every step.** Each copy's replacement moves served figures (at least GLD, PHYS, VXX on every
   surface that shows them), so every cell is a never-widen act with halves, a before/after read on the served artifact, and a
   rollback per key -- the same discipline cell (a) is landing under now.

7. **Naming and homes.** `etf-classifications` predates the LGIC canon; `infra/logic/registry/resources.json` carries both table names.
   An existing table reaches conformance through its own migration project (rule 30, R19), never as a rider here; a NEW resource this
   project creates (none is proposed) would take its name from the builders.

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

Dependencies and preconditions, named and not ordered:

- Cell (a)+(b) landed: Investor Reporting reads the canonical table, and the PHYS row exists through the seed path (proves O3's path
  before this project widens it).
- The seed source is the reproducible authority: the table's live rows equal a seed run's output, or the difference is listed (the
  live table has taken retag writes under POSN_ASTTAX; the seeder guard there is the prior art).
- The O4 census instrument exists before the first copy is retired, so "done" has a denominator from round 1.
- For each pipeline: the dependency graph read before the change (rule 20), a never-widen half pair, the list of tickers whose class
  moves on that surface, and the before/after read.
- The live IAM grants that name `bd-securities` (bd-pipeline `iam.tf`, and any others the live census finds) are read before the table
  is touched; a Deny or a delete is the last act, after the reader census reads zero.
- Andrew's confirmation before the table is deleted (destructive, unrecoverable), and the DONE WHEN he confirms at L2.
- The single-stock ordering question (Andrew's open lean: restart the order and place single stocks after the last ETF-class asset)
  is answered in the portal half; this project's surfaces carry whatever the canonical row says and do not invent a second order.

---

## PART VI -- STATUS, MARKED NOT-OUTCOME-BEARING

Measured, with clocks. Nothing here is an outcome.

- **2026-09-29 ~17:4xZ (~D's read-only trace):** canonical rows GLD commodities / Metals, VXX structured / Hedge, PHYS absent;
  `bd-securities` GLD and PHYS alternatives / Gold, VXX alternatives / Volatility; the fold `hedge -> alternatives` in the classifier;
  the copies as listed in Part IV.3.
- **2026-09-29 18:2xZ (CTO placement @c3c3f414dc):** (a)+(b) placed as an IRPT_BCKEND ~M cell before S173; (c) this project; (d) the
  portal half with ~D.
- **2026-09-29 18:4xZ (this seat's token census):** 98 code files carry one of the three tokens across `data/`, `infra/`, `portal/src`
  and `lib/` (44 + 46 + 6 + 2). Not a copy count.
- **Investor Reporting today:** classifies through `bd-securities` (`holdings_snapshot.py:828-873`), and the portal discards the served
  sub-asset (`SecurityList.tsx:149`), so GLD / PHYS / VXX render as Alternatives / Other on the Holdings tab (Andrew's screenshots of
  2026-09-29, `holdings_8.png`, and this seat's walk register). Both are being moved by cells (a) and (d), not by this project.

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- It did not re-read the live tables or the deployed Lambda bytes; Part IV cites ~D's trace for every live value and file:line. Its own
  measurement is the token census, which is a denominator, not a copy list.
- It did not check whether every copy is still reachable from a scheduled run (a dormant copy is retired the same way, but its
  before/after read is empty by construction; the census, not a belief, decides).
- It does not decide whether Positioning's ETFs mode (Bloomberg GICS) or the Schwab security master join the canonical table; O6 names
  them as candidate declared departures for the CTO.
- It does not order the pipelines. Which firm goes after the thread is L5's.
- It does not propose a new table, name or address; if the CTO's endpoint needs one, the builders name it (rule 30).

---

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/canonical-security-table-brief-20260929.md
  PROJECT           NONE-YET (CTO placement (c): new project; L2/L3 by 1.0.0_SA_CTO)
  EXISTING PRD      NONE (prior art PRD: org/missions/D4/POSN/POSN_ASTTAX/prd/POSN_ASTTAX_PRD.md, closed)
  SIBLING PROJECTS  POSN_ASTTAX (closed; owns the taxonomy and the one-source rule for Positioning), IRPT_BCKEND (cells (a)+(b), ~M),
                    DSGN_IRPTV1 (portal half, ~D), ETFS_CANON / ETFS_POSITIONING (Bloomberg-side), D14 LGIC (names and homes)
  PRIOR ART         DynamoDB etf-classifications + infra/aws/lambda/v2_portal/_shared/etf_classification.py (seed source) +
                    yang_pipeline/seed-etf-classifications.py (seed path) + _shared/etf_classifications_dynamodb.py (client);
                    lib ids.py ONE-DEFINITION census pattern; POSN_ASTTAX seeder guard (retag writes preserved)
  ANDREW'S WORDS    org/tier1_exec/2.0.0_SA_COO~D/deliverables/ANDREW_DIRECT_20260929_175xZ_ONE_CANONICAL_SECURITY_TABLE_FOR_ALL_HOLDINGS.md @099316efdd
  CTO PLACEMENT     org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_PLACEMENT_20260929_182xZ_ONE_CANONICAL_SECURITY_TABLE.md @c3c3f414dc
  MEASURED AT       ~D trace 2026-09-29 ~17:4xZ; CTO placement 18:2xZ; this seat's token census 18:4xZ
```
