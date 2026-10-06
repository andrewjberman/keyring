# L1 BRIEF (MIDSTREAM) -- MDPF_SECCLASS: one table for all security classification, the legacy table consolidated and retired

- **Author:** `4.0.0_SA_CRO` (L1), 2026-10-05 ~21:2xZ (5:2x PM Eastern). **Mode:** MIDSTREAM on `MDPF_SECCLASS`.
- **Order:** Andrew-direct at the `4.0.0_SA_CRO` terminal, 2026-10-05 ~21:1xZ, verbatim in
  `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261005_211xZ_ONE_CLASSIFICATION_TABLE_CONSOLIDATE_BD_SECURITIES.md`:

  > I do not like using bd-securities and all these random tables, there should be one table for all classification
  > efforts. I could tell that bd-securities was being used for the Investor Reporting page because all the names
  > were all caps and not cleaned up nicely. If "Sector" inclusion can be managed surgically, and the gaps resolutely
  > filled in, this should be manageeable. [...] devise a plan to consolidate all the bd-securities info into the
  > ETFClassifier table, in a manner that does not break any of those surfaces.

- **Evidence base:** `docs/briefs/one-classification-table-consolidation-analysis-20261005.md` ("the analysis"; every
  count below is measured there, section cited).
- **Consumer:** `1.0.0_SA_CTO`, `/endpoint --forward` at L2.
- **Words:** "the shared list" = DynamoDB `etf-classifications`. "The legacy table" = DynamoDB `bd-securities`.

---

## PART 0 -- HOW THE BLIND CONSTRAINT WAS HONOURED, AND WHERE IT BENT

**Honoured.** No MDPF_SECCLASS task order was opened. The project's `project.json`, its `phase` and `blocking` fields,
its decompositions and its surprise channel were not read. The served reality was read directly: both tables scanned,
the three firms' live holdings snapshots and the Positioning ETF document read (analysis sections 2 and 3).

**Read, as the mode allows:** the PRD's header, its ENDPOINT block (FWD-1 to FWD-12), its provenance note and its
CONTRACTS table (`org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md` lines 1-186).

**Where it bent, four places:**
1. A search printed the PRD's section headings and the first line of each surface-manifest row (S01 to S20) and of the
   enrichment backlog. I used the manifest to say which components the PRD does NOT name (0.2 below). I did not use the
   backlog.
2. Source files carry project notes in their comments. `bd_securities_fallback.py`'s header says a chain of work is
   "HELD" and names its owner; `holdings_snapshot.py` cites a CTO ruling. Both were read while tracing code.
3. This seat's own prior session log, shown at startup, says one classifier piece "is not applied".
4. `1.0.0_SA_CTO` updated the PRD today from Andrew's words at another terminal (FWD-11, FWD-12). Reading the endpoint
   therefore showed today's branch tip for those two outcomes.

**The finding the mode exists to return: THE DIRECTION IS UNCHANGED.** Andrew's instruction today restates the
ratified endpoint. FWD-2 (one answer on every screen), FWD-4 (no second definition), FWD-5 (the legacy table gone) and
FWD-12 (sector on the shared list) already say it. What this brief adds is narrower: one outcome the endpoint lacks
(names, O2), one exception the endpoint permits that Andrew's words now close (O3), and surfaces the PRD does not name
(0.2). If the work has felt stuck, the cause is coverage and sequence, not direction.

### 0.2 Components traced today that the PRD's surface list does not name

| Component | Why it matters | Analysis |
|---|---|---|
| `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` + `bd_securities_fallback.py` | the Investor Reporting Holdings tab's producer and its fallback to the legacy table; the surface Andrew noticed | 4.1 B1 |
| `infra/aws/lambda/semantic-news-layer3-curation/lambda_function.py` | a live reader of the legacy table; blocks its deletion | 4.1 B4 |
| `portal/src/pages/Attribution/constants/etf-categories.ts`, `holdings-shared.tsx` | a second hardcoded list and fallback function | 4.5 F3 |
| `portal/src/lib/tickerRegistry.ts` | a hardcoded name-and-class registry | 4.5 F4 |
| `data/black_diamond/scripts/classification/resolve_tickers.py` | resolves which security a custody name is, from the legacy table's raw names | 4.2 R1 |
| the inline geography list in `yang-generate-positioning/lambda_function.py:95` | a class-like label with no home in the shared list | 4.3 A4 |

---

## PART I -- THE OUTCOME TERRITORY

### The candidate thread

The thread MDPF_SECCLASS already built is the Black Diamond chain (FWD-1). The thread THIS brief asks for is the surface
Andrew looked at: **one Cottonwood client's holdings on the Investor Reporting Holdings tab.** Every security on that
page shows a class, a sub-class and a clean name that the shared list holds, and the legacy table is never consulted.
Cottonwood is named because it is the firm furthest from the shared list today (analysis 3; holdings check 2.1).

### O1 -- An advisor opens any client's Holdings tab and every security's class and sub-class is the shared list's

No security on the page is labelled by the legacy table, by a match on its name, by a word in its name, or by the
shape of its ticker. A security the shared list does not hold reads as unclassified, by name. Today 1,671 of 3,334
distinct held securities are labelled some other way (analysis 3).

### O2 -- An advisor reads a properly written security name wherever holdings are listed

The name on the page is the shared list's clean, properly capitalized name, not the custody feed's capital-letter
string. This is the symptom Andrew named. Today the Holdings tab prints the custody description, 2,311 of 3,334 held
securities are served in all capitals, and the shared list holds a name for 338 of the 1,663 held securities it covers
(analysis 5.1). The current endpoint promises a clean name only for rows its AI classifier makes (FWD-11).

### O3 -- A reader finds no screen that still classifies from a second authority without Andrew having said so

Andrew, 2026-10-05 ~20:4xZ: "I do not want holdings being displayed from any other table or going through any other
process." The endpoint's FWD-6 lets a screen keep a different authority if it is written down. Two are written down
today (the Holdings tab's fallback; the Schwab firm composition) and the Positioning ETF view was a third until FWD-12.
After this outcome, a declared exception exists only where Andrew has agreed to that one by name.

### O4 -- A person filling the shared list knows, for every held security without a row, that it is missing, and sees the count reach zero

The list of held securities with no row is something a person can pull on demand, per firm, with its total. It reads
1,671 today across three firms. "Resolutely filled" is that list reading zero and staying there as holdings change
(the staying-there half is the existing FWD-7).

### O5 -- An analyst opens the Positioning page's ETF view and reads each holding's sector from the shared list

Already FWD-12. Carried here for one reason: the shared list has two fields that hold sector-like words, `sector`
(179 rows of segment words) and `sub_asset_class` (which is where single stocks' sector names live today). A person
maintaining the list must be able to say which field a sector goes in (analysis 5.2). Measured on the ETF view: 166 of
its 167 holdings have a row; class agrees for all 166; 57 holdings that are blank on the page today would show a sector.

### O6 -- Anyone looking at a mix by asset class on any screen can say how the shared list's six classes became that screen's buckets

The legacy table has four classes and two quiet folds; the shared list has six. The 49 Financial data, the partner feed
and the Black Diamond mix each show three or four buckets (analysis 4.1 B2, B3; 5.3). One stated mapping per screen,
readable by the person looking at it. Among securities in both tables, 55 change class when a reader switches.

### O7 -- A developer opens the portal and finds no list of tickers with classes or names in it

Three hardcoded lists and two copies of one fallback function exist today (analysis 4.5 F1 to F4). After this, a page
shows what it is served; a missing label shows as missing.

### O8 -- Anyone can show that nothing reads or writes the legacy table, and it is then deleted on Andrew's word

Already FWD-5. Carried because today's trace found readers and writers the surface list does not name: the news
curation function, three writers that still add AI-classified rows every day, and the identity resolver that depends on
the legacy table's raw names (analysis 4.1 B4, 4.2). The job of working out which security a custody name is keeps a
home after the table is gone.

---

## PART II -- WHERE THE BOUNDARY SITS

**MDPF_SECCLASS owns:** the shared list's content and shape (class, sub-class, sector, fund-or-single, name, key
forms); the fill of missing rows; the mechanism that adds new ones; the proof that no second definition remains; the
legacy table's export and deletion.

**It relies on, and does not own:**

- **IRPT_BCKEND (the Holdings workstream, `2.0.0_SA_COO~M`)** -- owns `holdings_snapshot.py`, the fallback module and
  the published `HoldingsSnapshot` contract (`docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json`),
  including the `asset_class_basis` field. O1 and O2 land on its producer and its contract. This is the boundary most
  likely to be re-argued: the shared list is MDPF_SECCLASS's, the page's producer is IRPT's.
- **DSGN_IRPTV1 / the portal Investor Reporting page** -- renders the name and the basis field (analysis 4.5 F5, F6).
- **ETFS_POSITIONING / ETFS_CANON** -- own the ETF gold producer that reads Bloomberg's sector today (O5).
- **The Positioning and Attribution pages' producers (the yang pipeline)** -- already read the shared list; own their
  copies of the client module.
- **The firm data chains** -- Black Diamond, Cottonwood, Inflection, 49 Financial, each in its own firm tree. A cell in
  one firm's tree never writes another's.
- **The partner feed and the news pipeline** -- own the two Lambdas that read the legacy table.
- **Rival Funds** -- out of scope on Andrew's word today ("rivalfunds is an internal product and not related"). Its
  626 rows in the shared list (FWD-9) are not touched by this brief.

**It does not own:** security measurements. Andrew, recorded in FWD-12: characteristics are not handled in this table.
Fees, yields, durations, prices and returns stay where they are.

---

## PART III -- THE QUALITATIVE BAR

1. Andrew opens a Cottonwood client's Holdings tab and cannot find a security name he would want cleaned up.
2. Asked "why is this security in this class?", a person answers from one row in one table, and the answer is the same
   on every screen that shows it.
3. No number on any page moves at a switch without that security having been named beforehand as one that would move.
4. A security nobody has classified is visibly unclassified. It is never quietly called equity because its ticker is
   short.
5. The person who deletes the legacy table can show who last read it, and that the answer is nobody.

---

## PART IV -- THE SUBSTRATE: what exists, measured

- **F1. The direction is already ratified.** PRD v0.6, status RATIFIED, twelve outcomes; FWD-11 and FWD-12 were added
  today from Andrew's words at another terminal (PRD lines 133-155).
- **F2. One client module exists and most producers use it.** `etf_classifications_dynamodb.py`. The Black Diamond and
  Cottonwood gold libraries, the Positioning models producer and the satellite producers read only it (holdings check
  2.3, 2.4, 3). Four tracked copies of the client or its seed list sit beside it (analysis 4.4).
- **F3. A mechanism for adding rows exists.** `etf_classification_scheduled.py` writes a row only where none exists
  and reads a legacy row only as an input, on Andrew's rule of 2026-09-29 that the shared list is never overwritten
  from the legacy table. 3,045 of the shared list's 3,493 rows are its work (analysis 2).
- **F4. The legacy table is mostly not in use.** 10,873 rows; 2,053 label something held today (analysis 1, 3).
- **F5. The legacy table cannot be copied across.** Four classes against six; 9,939 rows written by an outside AI
  model; 55 class disagreements among the 2,378 securities in both; sub-class words the shared list does not use
  (analysis 2).
- **F6. 187 of the missing securities are not missing.** They have a row keyed `CUSIP:<symbol>` that the Holdings
  producer's lookup does not try (analysis 3).
- **F7. No portal page calls a classification table.** Every non-canonical label on a page is a hardcoded list in the
  portal or a served field (analysis 1, 4.5).
- **F8. The all-caps names come from the custody feed, not from the legacy table** (analysis 5.1). Andrew's reading of
  the cause differs from the measured cause; his reading of the symptom is right.
- **F9. Two other tables that sound related are not classification tables** (`trade-security-identifiers`,
  `opal-harvest-security-metrics`; analysis 2).

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

- **The legacy table stops growing.** Three writers add rows to it daily (analysis 4.2). Until they stop, every count
  ages and the deletion check cannot reach zero.
- **The sector field question is answered once** (O5; analysis 5.2), under the taxonomy law (CLAUDE.md rule 24):
  one axis, one intent.
- **A key form exists for a security with no ticker and no CUSIP.** The legacy table uses `NAME::<slug>`; the shared
  list has plain tickers and `CUSIP:` keys only (analysis 2). 58 held securities have no symbol.
- **Every switch of a reader is a served move:** the securities that change are listed before and read after, with the
  two sign-off halves (PRD contract C-SERVED; CLAUDE.md never-widen).
- **Outside-model use has Andrew's word per use.** FWD-11 records his approval of the AI classifier for securities
  nothing else can place. Whether that word covers the 668 securities labelled by ticker shape today is for the CTO to
  confirm against FWD-11's text, not for this brief to assume.
- **The published Holdings contract changes with its consumer first.** The portal validates a closed set of fields; a
  field the page does not know refuses the whole response (`holdings_snapshot.py:660-664`).
- **Firm trees stay separate.** The shared list is reference data; each firm's chain reaches it through its own cells.
- **The legacy rows are exported and kept before deletion**, and the deletion is Andrew's act (PRD contract C-DELETE).

---

## PART VI -- STATUS (NOT OUTCOME-BEARING)

Measured 2026-10-05 ~20:5xZ to ~21:2xZ; holdings figures are for business date 2026-10-02.

- Shared list: 3,493 rows. Legacy table: 10,965 rows.
- Held across three firms: 3,334 distinct securities; 1,663 with a row in the shared list; 1,671 without.
- Share of holdings value labelled from the shared list: Cottonwood 77.3 percent, 49 Financial 97.3 percent,
  Inflection 98.6 percent.
- Positioning ETF view: 167 holdings, 166 with a row.
- The PRD is v0.6. Its task orders and status were not read (Part 0).

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- **It does not know what MDPF_SECCLASS already has in flight.** Some of O1 to O8 may be partly built. Blindness is the
  mode's rule; the CTO reconciles at L2.
- **It does not say how many of the 1,671 any one source can classify.** No fill was tested.
- **"Has a row" is by symbol,** against one day's snapshots. A blank or odd symbol may hide a security that is covered.
- **The live access grants were not read**, only the Terraform files naming the legacy table (analysis 4.6).
- **Not traced:** the client-portal and advisor pages, exports, `lib/research/identity/positioning_chain.py`, the
  Inflection composition scripts, whether the four client-module copies equal the home file (analysis 7).
- **No page was rendered.** O2's "names look right" was measured as letter case in served data, not read on a screen.
- **It proposes no order of work.** The analysis's section 6 is a sketch Andrew asked for; sequencing is L5's.
- **It does not decide O3 for the Schwab composition.** Andrew's words of today reach it as written; whether he means
  that screen too is a question for him, put by the CTO if the endpoint needs it.

---

## REFS

```
  BRIEF PATH        docs/briefs/mdpf-secclass-one-classification-table-midstream-brief-20261005.md
  PROJECT           MDPF_SECCLASS (org/missions/D8/MDPF/MDPF_SECCLASS/)
  EXISTING PRD      org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md (v0.6, RATIFIED; FWD-1..FWD-12)
  ORIGINAL BRIEF    docs/briefs/canonical-security-table-brief-20260929.md @87ad6973f3
  ANALYSIS          docs/briefs/one-classification-table-consolidation-analysis-20261005.md
  EARLIER CHECK     docs/briefs/holdings-surfaces-canonical-classifier-check-20261005.md
  ANDREW'S WORDS    org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261005_204xZ_HOLDINGS_SURFACES_ONLY_CANONICAL_ETFCLASSIFIER_TABLE.md
                    org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261005_213xZ_CANONICAL_TABLE_CARRIES_SECTOR.md
                    org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261005_211xZ_ONE_CLASSIFICATION_TABLE_CONSOLIDATE_BD_SECURITIES.md
  SIBLING PROJECTS  IRPT_BCKEND (Holdings workstream); DSGN_IRPTV1; ETFS_POSITIONING / ETFS_CANON; the yang pipeline;
                    the firm data chains; the partner feed; the news pipeline. Rival Funds: out of scope.
  PRIOR ART         the one client module; the scheduled classifier; the 425 CUSIP-keyed rows; the contract file
                    org/standards/MDPF_SECCLASS_CONTRACT.json; PRD contracts C-SERVED, C-DELETE, C-WRITER
  OPEN FOR ANDREW   NONE put by this brief. Two the CTO may need: whether O3 reaches the Schwab composition; whether
                    FWD-11's word covers the ticker-shape securities.
  MEASURED AT       2026-10-05 ~20:5xZ to ~21:2xZ (tables scanned; snapshots for business date 2026-10-02)
```
