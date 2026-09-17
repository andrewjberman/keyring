# AMGT_RESAPP -- WHAT STILL FAILS "WHAT WOULD A PERSON OPEN" AFTER CELLS A-L LAND

**Author** `4.0.0_SA_CRO~Z`. **Written** 2026-09-16 05:1x-05:3xZ at HEAD `1db70c8e87` (the L10 addendum 1). **Answers**
`1.0.0_SA_CTO~Z` msg 23388 s.4: *"which of the nineteen outcomes would still fail the 'what would a person open' test
after cells A-L land."* **Push state:** LOCAL (LD-0522).

**Method.** Cells A-L are taken at their text (`ledger/ROUND_ANALYSIS.round11.md` s.5 and A1.4 @`1db70c8e87`) and
projected onto each outcome's ACCEPT paragraph (PRD v0.8 @`1170b4da69`). The test is the CTO's own: what would a person
open, and does it answer. It is NOT the EXERCISED grade (a person's act, L9's). Every count is read from the pool or
the code at this vintage, never from a status. **Correction to the audit @`a10eece02e`, G2 row:** "4 of 89 covered
names" should read **3 of 89 covered names** (BA, BABA, SAP) **plus NVDA, which is NOT a covered name** -- it is the
one uncovered name pulled by ticker on 2026-09-11 (below, FWD-2). The 4-key count was right; its denominator was not.

---

## 0. THE ANSWER

**Cells A-L repair the PLANE -- deploy, wiring, surfaces. They do not touch the POPULATION.** After A-L, a person who
opens one of the pilot names gets a page whose tabs answer. A person who opens any OTHER covered name gets a page whose
tabs each say ABSENT, honestly. The residual is not one outcome; it is one axis that cuts across nine of them:

| residual class | what it means | outcomes it holds after A-L |
|---|---|---|
| **POPULATION** | the content exists for a pilot set and NO cell in A-L runs the producer over the coverage list or the union universe | FWD-1, 3, 5, 8, 9, 10, 16, 17, 18, 19 |
| **NO CELL** | the surface or mechanism is in no cell at all | FWD-6 (version compare), FWD-18's chart, FWD-12's re-run stages, FWD-11's feed |
| **SEAM** | the cell as ruled cannot reach the terminal | FWD-2 (K) |
| **RESERVED** | Andrew's decision by name; recorded, not a defect | FWD-4, 15, 16 (the feed), FWD-9/18 (filings batch activation), FWD-17 (the loop) |

**The producers, and who has run them over what** (the thing the round-12 cut should read AT THE CUT):

| producer | runs over | has run over | schedule | in A-L? |
|---|---|---|---|---|
| model block (`integrations/bloomberg/research/model_block_pull.py`, DAPI on this box) | one security per call | 3 covered (BA, BABA, SAP) + NVDA | none; terminal `ok:false` at 04:5xZ; sign-in budgeted | **NO** (A reads what exists; D pulls SCORE inputs, not the block) |
| filings analyzer + drafting (`lib/research/filings`, Claude API, USD ~1.1/filing) | the union universe (`filings.batch`) | 5 names | `OpalResearch-FilingsAnalyzer` DISABLED; rj-6 AC4: *"activation is Andrew's word"* | NO (RESERVED) |
| exec management (`lib/research/management`) | the union universe (`management.batch`) | 5 names | `OpalResearch-ExecManagement` DISABLED; rj-8: *"the production loop is the harvest estate's"* | NO (RESERVED) |
| posture (`lib/research/posture`, Claude API) | one pair per call | 2 (BA, BABA) | none | **NO** (A redeploys the READ; nothing produces more) |
| similarity ranker (`lib/research/peers`) | every name with a key | 33 (10 with members) | none | C repairs 23 empty subjects; **does not say the ranker re-runs over the names C newly resolves** |
| harvest (`lib/opal_data_harvest`) | publishers x names | 7 bodies / 3 names | `Opal Data Harvest - Local Publications` DISABLED | NO (RESERVED, R5) |
| chatter ranking (`amgt-resapp-chatter-axis`) | the pool | daily | cron 10:00Z ENABLED | served |
| Price producer | -- | never | -- | B |

---

## 1. OUTCOME BY OUTCOME, AFTER A-L

Denominators: universe 256 (89 coverage, 170 holdings, 3 both); keyed 33 today (C widens toward 164 of 170 holdings);
pilot set BA / BABA / COST / HD / SAP; model blocks 3 of the 5 (COST and HD have none).

| FWD | ACCEPT, in one line | after A-L a person opening a PILOT name gets | ... opening any OTHER covered name gets | residual |
|---|---|---|---|---|
| 1 | model numbers, description, segments already on screen | figures for BA / BABA / SAP; ABSENT for COST / HD | Model tab ABSENT | POPULATION -- no cell runs the block pull over the 89 |
| 2 | type an uncovered ticker, get the page, told it is fetching now | "fetching now" and a queued request | same | SEAM -- see s.2 |
| 3 | defend every number from the page | provenance beside each served figure (3 names) | nothing to defend | POPULATION (rides FWD-1) |
| 4 | recent commentary on the page | 2-3 items for BA / COST / HD; none for BABA / SAP | an honest empty feed | RESERVED (harvest) |
| 5 | Adam forwards the printed pack unchanged | a PDF for the 3 names with a block (J) | print REFUSED, no block | POPULATION (rides FWD-1); the forward is a person's act |
| 6 | return, say what changed, name the earlier version | NO surface -- the store holds 4 stamps for BA and the page shows one | same | **NO CELL** -- A-L carry no version-compare surface |
| 7 | Adam sees which covered names are stale | the freshness view (L) over the 89 | the same view -- most rows say never refreshed | served after L |
| 8 | the comparable list is about THIS company | peers for the 33 keyed (10 with members) | "absent with a reason" for the unkeyed; after C, keyed but with NO R-1 object unless the ranker re-runs | POPULATION unless C's text says the ranker runs over the widened set |
| 9 | machine prose marked, beside its evidence | drafted sections for the 5 | Thesis tab ABSENT | RESERVED (filings batch activation is Andrew's word) |
| 10 | a failed check visible as failed | check badges on the served figures (3 names) | nothing to check | POPULATION (rides FWD-1) |
| 11 | social discussion admitted by a written rule | the server's status sentence, no items (G classifies) | same | NO CELL builds the feed (measure-then-build, by design) |
| 12 | see each input's source / last run / outcome, re-run any ONE alone | the ledger surface (L) over 4 ledgers dated 09-11; **re-run does nothing** -- `ledger.py` `CLASSES` carries `stage: None` for 6 of 6 classes | an empty ledger | **NO CELL** wires a stage; K may give `market_data` one, leaving 5 of 6 |
| 13 | everything on the page is the same company | identity MEASURED, crosswalk vintage shown | UNRESOLVED stated honestly; after C, resolved for the holdings | served after C |
| 14 | owned lists, told when they rot | the register + rot signal (L) | same | served after L |
| 15 | a ranked list, click through to a name | Trending x Chatter 10 rows over 7 bodies; Price after B | same list | served; thin by RESERVED |
| 16 | description + today's items above the tabs | description (from D-1) for the 5; items for 3 | description ABSENT (D-1 is the source); empty feed | POPULATION + RESERVED |
| 17 | who runs it, how long, vs the pool average | roster for the 5; tenure from the filing; Lusha 11 of 48, no dates | Exec tab ABSENT | RESERVED (the loop) + POPULATION |
| 18 | filings read for the analyst + the ONE chart | prose for the 5; **the chart ABSENT for 5 of 5** (W18-S12: no driver series matches a model series) | Thesis tab ABSENT | **NO CELL** for the chart; RESERVED for the batch |
| 19 | better or worse than the most similar name on the other side | posture for BA and BABA only | "no posture" | POPULATION -- nothing in A-L produces a posture beyond the 2 |

**Count:** after A-L, for a person opening a NON-pilot covered name, **10 of 19 outcomes answer ABSENT** (1, 3, 5, 8, 9,
10, 16, 17, 18, 19). For a pilot name, **5 of 19 still fail even for the best-served name** (2, 6, 11, 12, 18's chart).
The ten are one axis, not ten defects.

---

## 2. THREE THINGS IN A-L AS RULED THAT WILL NOT PRODUCE WHAT THEY NAME -- stated so the cut does not inherit them

**K (R3): "the consumer becomes an event-source-mapped Lambda" cannot reach the terminal.** `pull_consumer.py` calls
`model_block_pull.stage_pull`, which is the Bloomberg DAPI at `127.0.0.1:8194` on THIS box (PRD s.5, first bullet: "the
Bloomberg interface is local to one device ... any design must say how a browser request reaches it"). A Lambda consumer
would drain the queue and fail every message at `bloomberg_health`. The seam's own design (`sqs.tf` header; `pull_consumer.py`
docstring) is a BOX-side poller under the operator's identity, "never a persistent service" (BOUNDS G-20). ⭐ **And it
has worked exactly once, end to end:** `packs/NVDA_US_Equity/status.json` reads `state: LANDED`, requested 2026-09-11T00:53:58Z,
landed 00:54:02Z, raw and derived keys named -- NVDA is not a covered name, so that is FWD-2's own case, exercised by a
person running the poller. So K's honest shape is: wire the page to the enqueue route (the adapter's 501 goes away), keep
the consumer box-side, and the page's "fetching now" resolves only when a person runs the poller or Andrew activates a
cadence on this box -- which is the same reserved-class decision as the harvest (@`187f003998`, "local on this device with
some kind of local cron job"). A card at Andrew, not a Lambda.

**L (R4) gives FWD-12 a surface over a ledger that cannot re-run anything.** `lib/research/ledger/ledger.py` `CLASSES`:
`market_data`, `filings`, `news`, `social`, `web`, `sa` -- every one `"stage": None`. "Re-run any one alone" has no stage
to invoke for 6 of 6 classes. A surface over that ledger shows four rows dated 2026-09-11 and a re-run button that records
SKIPPED. The cell should either wire stages (the model-block pull for `market_data`; the filings analyzer for `filings`; the
harvest worker for `news`) or state the surface serves the ledger READ only and the re-run is round 13.

**A closes the deployed-plane FAIL for the names that have a block, and the judgment criterion will still read
ABSENT for 86 of 89.** "Does the page a person opens now show the figures" is the right criterion; the cut should name
WHICH page -- BA -- and print the block count read from `derived/model_block/` at the cut beside it, so the 3-of-89 is
carried as data and not rediscovered by the CVO.

---

## 3. WHAT WOULD MAKE THE POPULATION MOVE -- each with its gate, none of them this seat's to cut

| act | gate | class |
|---|---|---|
| the model-block pull over the 33 keyed coverage names (then the rest as C resolves them) | a signed-in terminal on this box; the two-phase budgeted sign-in (`integrations/bloomberg/READ_HERE.md`); the Bloomberg-terms question the PRD carries as OPEN | a DECISION (budget + terms), not reserved by name |
| the filings analyzer + drafting batch over the union universe | rj-6 AC4: "activation is Andrew's word"; USD ~1.1 per filing (about USD 100 for the 89) | RESERVED |
| the exec-management batch | rj-8: the harvest estate's loop | RESERVED |
| posture over every keyed name | Claude API per pair; the comparable needs the OTHER side's pack (C-POSTURE) -- so it follows the two above | a cell, after the batches |
| the ranker over the names C resolves | none -- a re-run | a cell (C's text should say so) |
| the harvest over the union universe | @`9db2a36cdc` | RESERVED |

Until at least the first two move, the product is five names. That is a true sentence about the artifact and it is the
sentence the round-12 COMPLETION_REPORT will have to write unless the population is cut or carded now.

---

## 4. NOT CLAIMED

No grade. No view on fan-out or sequencing (the COO's). The five-name pilot set is read from the pool, not from a plan;
if a cell in A-L is intended to run a producer over the universe and this seat missed it in the text, the cell's own
denominator will say so at the cut. Vintage: pool read 04:4xZ and 05:2xZ; analysis @`1db70c8e87`; `ledger.py` at HEAD.
