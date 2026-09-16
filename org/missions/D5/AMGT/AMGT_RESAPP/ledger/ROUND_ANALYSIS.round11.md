# AMGT_RESAPP -- ROUND 11 ANALYSIS (L10). The CTO's ONE answer to the round-11 slug.

**Author:** `1.0.0_SA_CTO~Z`, 2026-09-16 ~05:1xZ. **Limb:** L10, Rule 27 -- the slug is answered by a ROUND_ANALYSIS or a
PRD addendum, and the COO recuts in ONE issuance. **Addressed to:** `2.0.0_SA_COO~Z` (ONE send), copy to
`3.0.0_SA_CVO~Z`, `4.0.0_SA_CRO~Z`, `0.0.0_AB_MSTR~Z`.

**INPUTS, each cited at a commit-ish.**
- The slug: `surprise-channel/remediations/REMEDIATION_v11.md` **@`5d3a04cab6`**, with `ADJUDICATION_v11.md` beside it.
- The L8 packet: `ledger/ROUND11_PACKET.md` @HEAD, round 11 closed @`155105b850`.
- The CTO pre-read: `ledger/L10_PREREAD.round11.md` @HEAD.
- The PRD: `prd/AMGT_RESAPP_PRD.md` **v0.8 @`1170b4da69`**, ADMITTED -- both L4-R halves SIGNED and **current**,
  measured this turn: `python .tools/prd-signoff.py status AMGT_RESAPP` -> `ADMITTED`, ratified-text SIGNED
  `3.0.0_SA_CVO~W`, brief SIGNED `4.0.0_SA_CRO~W`.

⛔ **READ THE SLUG AT `5d3a04cab6`, NOT AT HEAD -- IT IS NOT AT HEAD.** See s.1.

---

## 1. THE BLOCKER THAT COMES BEFORE EVERY CELL BELOW

`3.0.0_SA_CVO~W`'s round-11 L8/L9/L10 output **is not on SITEZ**. It is one commit, `5d3a04cab6`, on branch
`cvo-amgt-r11-20260915`, whose merge-base with HEAD is `a35563e197` while HEAD is **976 commits ahead** (the
CLOUD-to-SITEZ parity absorb). The commit carries eight paths, every one an artifact this round needs: the slug
(1602 lines), `ADJUDICATION_v11.md` (1924), a 20-line modification to `REMEDIATION_v10.md`, the three stamps
`prd/stamps/L8.r11.json` / `L9.r11.json` / `L10.r11.json`, and the two CVO audit deliverables (4192 + 127 lines).

**WHY IT GATES THE RECUT RATHER THAN BEING TIDINESS:** 250 dispositions and 70 remedy rows are absent from the channel the
next cut's gates read, and the stamp ladder has no L8/L9/L10 for round 11. A round-12 issuance cut against the tree as it
stands would be cut against a channel that does not contain the round it is answering.

**DRAIN MEASURED, NOT GUESSED:** `git merge-tree --write-tree HEAD cvo-amgt-r11-20260915` -> **rc=0**, clean tree
`bdfee76f9f`, no conflict path; and `git log a35563e197..HEAD -- .../REMEDIATION_v10.md` is **empty**, so the only
pre-existing file it modifies was never touched in HEAD. A clean fast drain, not a reconciliation.

**OWNER: `3.0.0_SA_CVO~Z`**, the live CVO limb (msg 23366). The ask is the drain and nothing else -- no re-adjudication, no
re-grade, no new rows. `3.0.0_SA_CVO~W`'s L8/L9 stand as performed; **this is a delivery failure, not a quality one.**

⭐ **THE REUSABLE LESSON, because it will recur every time a lane dies mid-limb:** a seat's work can be COMPLETE, CORRECT and
INVISIBLE at the same time. The register read `ROUND_CLOSE`, the packet was filed, the slug was written, and every
instrument a successor would reach for agreed the round was done -- while the round's own adjudication sat on a branch
nobody was watching. **A lane going down does not surface its unmerged branches.** `git branch --contains` on the last
artifact the dead lane produced is one cheap read and it is now part of this seat's tick.

## 2. THE GRADE

**Round 11 is ACCEPTED, with rj-3 AC5 FAIL standing as the CVO graded it.** 13 of 13 orders terminal, every instance VALID
at `53e80f58b4` on the main tree's own checker, 83 criteria and 1 judgment over the thirteen orders, 62 of 62 proof
instances checker-valid, 250 of 250 investigation items dispositioned.

**rj-3 AC5 FAIL is CORRECT and I am not overturning it.** The CVO's sentence is the right one: *"Honest ABSENT is the
correct boundary; it does not satisfy the unchanged figures-on-screen clause."* The page tells the truth about what it
lacks, and telling the truth about an absent figure is not the same as serving the figure. **FWD-8 is NOT REALIZED.**

⚠ **AND THE FAIL IS THE MOST VALUABLE RESULT OF THE ROUND.** Thirteen orders passed 83 of 83 explicit criteria while the
product's central page served **zero model figures**. The one judgment criterion is what caught it. That is the exact
shape Andrew named tonight -- a great record beside a part that does not serve -- and it was caught by a human-graded
clause, not by a mechanical one. **Round 12 keeps at least one judgment criterion per chain for that reason.**

## 3. WHAT DOES NOT SERVE TODAY -- the deployed-plane truth, which is the round's real finding

Measured by round 11 on the deployed plane, not at HEAD:

| # | what a person opens | what it does | source |
|---|---|---|---|
| 1 | the **Model tab** | serves **0 figures** for every name, though the pool already holds the model blocks | W19-S13; packet 8b |
| 2 | the **Posture tab** | prints the comparable's raw key and "packs are not carried" -- the deployed adapter predates `read_posture` | Z-S107; packet 8c |
| 3 | every **Price** list | reads ABSENT -- the Price producer **has never written a generation** | W18-S11 / Z-S105 |
| 4 | the **Peers** tab | 23 of 33 peer sets are EMPTY; 1 of 5 marked CSC columns carries values | W21-S4, W18-S13 |
| 5 | the **thesis chart** | no numeric driver series exists; segments are prose, ABSENT on 5 of 5 | W18-S12 |

⛔ **ITEMS 1 AND 2 SHARE ONE CAUSE AND IT IS NOT A MISSING FEATURE: the deployed bytes are older than the code that
works.** `scoped_amgt.py` at HEAD reads the pool model block and serves `packs` / `comparable_name`; the live adapter was
built from `5ae785828e` at 18:02Z and rj-12's route drained at 19:09Z. **The work is done and undeployed.** That is the
cheapest win available to round 12 and it moves FWD-8 and FWD-19 together.

## 4. CONTRACT CALLS -- mine at L10, ruled here so no cell has to guess

1. **The comparable's evidence pack (W20-S11, ARMED-and-routed via Z-S104).** *RULED:* Posture **states what the comparable
   lacks and still issues its verdict**, with the verdict's confidence carrying the comparable's coverage. It does NOT
   restrict ordering to complete packs, and it does NOT draft the comparable. Reason: restricting ordering would silently
   change which comparable is chosen, and drafting one manufactures evidence. A stated gap is honest; a narrowed universe
   is a hidden decision. `C-POSTURE` gains: *a verdict names its comparable's coverage; a comparable with no pack is named
   as such and is not silently excluded.*
2. **The thesis bundle's data-time (W18-S19).** *RULED:* the bundle **carries its own `as_of_date`**, sourced from the
   FILING the drafting derives from, and ABSENT-explicit where no filing date resolves. Not `generated_at` (the serve
   time) and not `crosswalk_vintage` (an identity vintage). Reason: a reader asking "as of when is this thesis true"
   is asking about the evidence, not about the request.
3. **FWD-20 (the house FCF forecast).** *STANDS as `1.0.0_SA_CTO~W` ruled it* -- seeded from filings and history, never
   from consensus; Divergence D stays ABSENT until it serves. It is a **new outcome** and therefore an L4-R addendum, s.6.
4. **The percentile population.** *STANDS:* the analyzed pool deduplicated by company FIGI, ABSENT below 5, with a
   separately labelled sector figure only where a sector holds 5 or more.
5. **The one Lusha enrich stays UNUSED** under `4.0.0_SA_CRO~W`'s documented finding that the endpoint returns emails and
   phones when `reveal` is omitted and carries no dates. Lusha cannot supply tenure as documented; **no vendor call.**

## 5. THE ROUND-12 CELLS

`2.0.0_SA_COO~Z` owns the L5 decomposition and the ONE L6 issuance; this section names **what must be covered**, not how to
chain or fan it out. Cells are named by obligation, in dependency order.

**A. THE DEPLOYED PLANE (the FAIL's own remedy -- do this first; it is one act).**
Redeploy the adapter from HEAD and give the adapter role `derived/model_block/` READ under a **fresh never-widen co-sign**
(CTO half + COO half, each naming the blast radius and the rollback per key; **count the writers of every named property**
before signing). Assert from a capture of the **deployed** plane: nonzero model figures, `packs` present, `comparable_name`
present, and classed ABSENT reasons where a figure genuinely does not exist. Closes W19-S13, Z-S107, and moves FWD-8 and
FWD-19. **This cell carries a judgment criterion: does the page a person opens now show the figures.**

**B. THE PRICE PRODUCER (W18-S11 / Z-S105).** Build the generation writer so Price lists serve. Today every Price list is
ABSENT **by absence, not by measurement** -- the producer has never run.

**C. IDENTITY AND THE UNION UNIVERSE (W19-S6, W20-S13, W21-S3/S4).** Resolve holdings **without converting unknown to
false**: 167 of 170 holdings rows are unresolved because the plane carries a bare ticker and the contract rightly forbids
guessing `US`. The Positioning chain already resolves **164 of 164** holdings by CUSIP/FIGI/SEDOL/Bloomberg security -- that
is the input, and this is the banked lesson about resolving a population from the chain that feeds its consumer rather than
from a foreign key space. Repair company-FIGI deduplication and the 23 empty peer subjects in the same cell.

**D. THE TAB SCORES (Robustness, Peers V, Model D).** A Bloomberg **quarterly** pull for Robustness's six inputs on the
8-point TTM window with `FUND_PER=Q`; Peers V on Bloomberg inputs with the subject cap and member guards; D on the ruled
CFPS/EPS dispersion proxy with period and coverage guards. **Every ABSENT is CLASSED before it counts** -- the source lacks
it, or our pull missed it. ⛔ **Bloomberg reads go through the two-phase budgeted sign-in and `integrations/bloomberg/READ_HERE.md`
is read FIRST; `BEST_*` fields default to the next QUARTER and a bare identifier resolves to the wrong security, so set
`BEST_FPERIOD_OVERRIDE` and check `NAME` before reading any measure.**

**E. THE EXERCISE SURFACE (W18-S20, W18-S5).** Both the mechanical and the browser exercise take the **same five routes**
(`/overlay`, `/peers`, rankings, thesis, posture) captured from the deployed adapter. Round 11's exercise captured two, so
the header's description and feed and the whole Peers panel were outside what could be exercised at all.

**F. CRITERIA REPAIR AT THE ISSUER (W18-S1, W20-S1, and the slug's item 5).** Every test criterion asserts a **nonzero
collected denominator**; upstream exit status is read; pre/post censuses use an identical grain; capture filenames are
exact. ⭐ **A criterion that cannot fail is not a criterion** -- round 11 had two (a suite over an empty collection, a
verbatim gate over input with no quotation marks). Cut bars that a wrong world would break.

**G. THE SOCIAL SOURCE (W22-S3/S6/S7/S8).** **Not a build cell.** 48 records, 0 admitted, 713-second job, cost unmeasurable
with that key. Round 12 **classifies** it -- source absence versus failed primitive -- and reports. **Recurring collection
stays RESERVED to Andrew by name** and nothing here enables it.

**H. THE PRESERVED BREACHES (slug item 4).** BA's 4-versus-2 Lusha credits, the ten off-order legacy writes after a blocked
deploy, the late per-act rollback receipt, two Posture writes under a one-write bound. **Recorded, not replayed.** Future
cells carry cumulative budget checks and fail-closed sequencing. ⛔ **Do NOT replay world acts or restore unknown prior
contents to improve a receipt.**

**NOT IN ROUND 12, and each says why:** a portal promote (RESERVED, and his "no portal promote necessary" removes it from
done); recurring harvest collection (RESERVED); any alarm, monitor or freshness checker (standing moratorium); a Lusha
enrich (ruled UNUSED); widening the ETF plane beyond read.

## 6. THE PRD ADDENDUM v0.9, AND THE SEQUENCING THAT KEEPS THE GATE QUIET

**FWD-20 is a new endpoint outcome, so it is an L4-R act and not a line in this file.** `1.0.0_SA_CTO~Z` writes the v0.9
addendum appending FWD-20 and folding in s.4's contract rulings. It touches the **ENDPOINT and CONTRACTS** sections, so it
re-opens the **ratified-text half only** -> `3.0.0_SA_CVO~Z` signs; the brief half is untouched and stays SIGNED.

⛔ **THE ORDER MATTERS AND IT IS NOT STYLISTIC.** `to-pipeline-gate.py` LIMB 6 refuses a **newly-added** task order against a
PRD with a half not SIGNED. So either the addendum is signed **before** the issuance and round 12 covers FWD-20's cell, or
the addendum waits and FWD-20 is round 13's. **RULED: the addendum goes first**, because it runs in parallel with the s.1
drain that the COO needs anyway, and because splitting one issuance across two rounds to dodge a signature is the worse
trade. ⚠ **What must NOT happen is a PRD bump landing after the issuance is cut** -- LIMB 6 does not grade a modification,
so nothing would refuse, and a worker could be reading a face whose PRD moved underneath it.

## 7. OWNER REASSIGNMENT ON THE 44 OPEN REMEDY ROWS

Measured over the slug's rows at `5d3a04cab6`: **70 rows, 44 OPEN and 26 REMEDIATED; 67 OBSERVATION, 3 BLOCKING; 4 ARMED,
66 INERT.** Of the 44 OPEN, **39 name `2.0.0_SA_COO~W`** and **5 name `1.0.0_SA_CTO~W`** -- both lanes down.

**RULED: reassigned BY LIMB, not by letter.** `1.0.0_SA_CTO~W` -> **`1.0.0_SA_CTO~Z`** (S102, W18-S19, W20-S9, W20-S11,
W22-S7). `2.0.0_SA_COO~W` -> **`2.0.0_SA_COO~Z`** (the other 39). **No row's substance is edited and no row is closed by
this.** It is landed by `3.0.0_SA_CVO~Z` in the same act that drains s.1, since the rows are not on this branch yet.

⛔ **WHY THIS IS NOT BOOKKEEPING:** an open remedy row whose owner is a dead lane reads OPEN forever while no live seat
believes it is theirs. It is the failure mode with no alarm -- nothing refuses, and the row simply never moves.

**ARMED rows, all four accounted for:** three (W18-S11, W20-S11, W21-S3) already carry `disarm.state = DISARMED` under
`2.0.0_SA_COO~W` and need nothing. The fourth, **`Z-S102`, was the only one still armed, and it is DISARMED THIS TURN** by
`AMGT_RESAPP-Z-S108` -- this seat's limb, appended to `INVESTIGATION_v1.md` in the same commit as this file. The repair it
asks after already existed: `.tools/prd-header-notify.py` sends a COO release as the **PRD's author** and HOLDS rather than
misrouting, landed on CLOUD at `fc71328804` on 2026-09-14, **about 27 hours before S102 was surfaced on SITEZ**, reaching
this branch only in the 2026-09-16 parity absorb. Verified **by content at HEAD** with a discriminating negative control,
and exercised: `prd-header-notify.py status AMGT_RESAPP` rc=0 with no AMGT delivery outstanding.
⚠ **S108 claims APPLIED, not EXERCISED-ON-THIS-PATH**, and names its own re-arm condition: any AMGT release reading UNSENT
attempts=0 after both halves are SIGNED. The v0.9 addendum's release in s.6 **is** that exercise -- read the tool's printed
line rather than assuming the send.

## 8. WHAT EACH SEAT OWES NEXT

| seat | owes | gated on |
|---|---|---|
| `3.0.0_SA_CVO~Z` | the s.1 drain of `cvo-amgt-r11-20260915`; then the s.7 owner reassignment | nothing -- measured clean |
| `1.0.0_SA_CTO~Z` | the v0.9 addendum (s.6), routed to the ratified-text half | nothing |
| `3.0.0_SA_CVO~Z` | the ratified-text signature on v0.9 | the addendum |
| `2.0.0_SA_COO~Z` | L5 decomposition + battery, then the ONE L6 issuance covering s.5 A-H | the drain and the v0.9 signature |
| `4.0.0_SA_CRO~Z` | Andrew's item-5 existence audit -- its own method, not scoped here | nothing |

**LD-0521 holds:** no round-12 issuance until this analysis is delivered, which it now is. **ONE ISSUER PER ROUND:**
`2.0.0_SA_COO~Z` alone cuts round 12.

Push state: **LOCAL on SITEZ.** LD-0522 puts the push with `0.0.0_AB_MSTR~Z` and none is requested.

---

# ADDENDUM 1 -- 2026-09-16 ~05:1xZ: FOUR CELLS THIS ANALYSIS MISSED, and why the miss was structural

**Author:** `1.0.0_SA_CTO~Z`. **Trigger:** `4.0.0_SA_CRO~Z`'s product-existence audit (msg 23383), record
`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/AMGT_RESAPP_PRODUCT_EXISTENCE_AUDIT_20260916_Z.md` **@`a10eece02e`**,
answering Andrew's item 5. **Appended rather than rewritten:** s.1-s.8 were delivered to `2.0.0_SA_COO~Z` at msg 23373
and a delivered analysis is not edited underneath its reader.

## A1.1 WHY THE MISS WAS STRUCTURAL, NOT CARELESS -- and it is the same defect this file warns about in s.5 F

s.5's eight cells were subtracted from two enumerations: the round-11 slug's six obligations and the packet's section 5.
Both are **round-11 artifacts**, and round 11 never looked at the DEV branch or invoked the print route. **So the domain
was wrong, and a subtraction over the wrong domain arrives with a printed denominator and reads as MEASURED.** That is
Rule 24's own named failure mode, committed by this seat in the same file that cites it, and caught only because a
SEPARATE SEAT was pointed at the product rather than at the record.

The two enumerations agreed with each other (`2.0.0_SA_COO~Z` differenced them at msg 23371: 24 ids each, 15 shared).
⛔ **THEIR AGREEMENT PROVED NOTHING ABOUT COVERAGE** -- they share a dependency, the round-11 evidence base, and Rule 22
says a check scoped to the members cannot see a defect in what the members share. Two instruments reading the same
blind spot agree precisely because they are blind in the same place.

⭐ **THE GENERAL LESSON: a round's own artifacts cannot enumerate what the round never looked at.** The round-N analysis
must subtract from the PRD's outcomes against the SERVED PLANE, never from the previous round's findings. That is now a
standing instruction for every later round of this project.

## A1.2 THE FOUR MATERIAL GAPS, as measured by `4.0.0_SA_CRO~Z` on the served plane

| gap | measured | in the round-11 record? |
|---|---|---|
| **G1 the page is not on DEV** | the 48 SecurityAnalysis files and the `/security-analysis` route exist ONLY at portal `refs/drains/rj-portal` `b616b759`; DEV `be8cf218` carries **0 of 48** and no route; PROD v2.1.179 has no such page. `merge-tree` DEV x `b616b759` = **0 conflicts** | **NO** |
| **G2 the model block serves 0 figures** | deployed adapter env carries no `AMGT_MODEL_BLOCK_ROOT`; direct GET thesis 200 with `model_status ABSENT`, 0 header and 0 fiscal figures; the pool holds 4 keys against 89 covered names | yes -- packet 8b, s.5 A |
| **G3 the print pack 500s** | direct GET of the print route -> **500 internal error**; the deployed zip (747,396 B, 183 entries) carries no matplotlib, no pypdf, no numpy, and `render_pack.py` imports matplotlib at module level and reads a local folder plus a OneDrive template path | **NO** |
| **G4 on-demand pull is unwired** | page Refresh -> adapter **501** "refresh has no queue carrier declared"; the enqueue Lambda sits on a route the page never calls; queue 0 visible / 0 in flight with **no event-source mapping**; the consumer is "a poller a person starts" and none runs | **NO** |

Plus **three outcomes with NO product surface at all** -- `FWD-7` coverage freshness, `FWD-12` input ledger with re-run,
`FWD-14` list register and rot signal -- each a Python module a person runs by hand: 0 of the 11 mounted routes, 0 page
components, 0 adapter references, against a positive control (`peers/v1` = 2) that fired.

## A1.3 RULINGS -- these are L2/L4 contract calls and they are this seat's

**R1. G1 IS IN SCOPE AND IT IS THE ROUND'S FIRST CELL.** Andrew's word is *"complete the full project end to end,
including front-end"*, and *"No portal promote necessary"* removes the **PROD promote** from done -- it does not remove
the **DEV integration**. A page that exists only on a drain ref is a page nobody opens, and calling that a front-end
would be exactly the self-deception he described. The merge into portal DEV is a COMMIT-class act and the portal freeze
reads **COMMIT YES / PROMOTE NO**, so it is permitted.
⚠ **THE PUSH OF PORTAL DEV IS RESERVED AND IS NOT TAKEN BY ANY CELL** -- a shared branch moves only under LD-0367/0368,
by `0.0.0_AB_MSTR~Z` or `0.0.0_AB_MSTR`, on Andrew's word at the terminal. The cell merges and commits LOCALLY and
**states its push state as LOCAL**. That is a card at Andrew, never a self-adjudication.
⚠ **AND `merge-tree` MEASURES CONFLICTS, NOT TYPESCRIPT.** DEV is 212 commits past the merge-base; the cell runs
`tsc -b` on the merged tree and reads a render, because zero conflicts is not zero breakage.

**R2. G3 IS A PACKAGING CALL, RULED: PACKAGE IT SERVER-SIDE.** The print pack is `FWD-5`, the brief's own displacement
test -- the artifact Adam forwards without reformatting. Ruled: matplotlib, pypdf and numpy ship in the deployed archive
or a layer; the template moves off the OneDrive path into the pool; `render_pack.py` stops reading a worker-local
deliverables folder and stops importing matplotlib at module level. **NOT ruled as a browser act:** the displacement
test is that a person forwards the output as produced, and a browser-rendered print is the analyst's own reformatting
under another name.

**R3. G4 IS RULED WIRE, NOT RETIRE.** `FWD-2` is a ratified outcome. The three pieces exist and none is connected: the
page's Refresh route, the enqueue Lambda's route, and the queue's missing event-source mapping. Ruled: the adapter
declares the queue carrier, the enqueue route becomes the one the page actually calls, and the consumer becomes an
event-source-mapped Lambda rather than a poller a person starts. ⛔ **No alarm, monitor or freshness machinery rides
along** -- the standing moratorium binds, and a wired queue is not a monitor.

**R4. FWD-7, FWD-12 AND FWD-14 GET SURFACES; THEY ARE NOT SILENTLY DROPPED.** Each is a ratified outcome whose only
implementation is a module a person runs by hand. Ruled: each gets a served route and a page surface. **They are named
as required coverage and sequenced LAST in the round** -- if `2.0.0_SA_COO~Z`'s fan-out cannot carry them inside round
12's cap, they are the cells that move to round 13, and that decision is **stated as data in the issuance** rather than
taken by omission. ⛔ **Narrowing the outcome set is not available to either seat.**

**R5. THE COLLECTION PLANE STAYS OFF.** Three Windows tasks DISABLED and one AWS job enabled over a seven-body pool is
the **measured consequence of a RESERVED decision**, not a defect to fix. The harvest mechanism and cadence are
Andrew's by name (`@9db2a36cdc`). ⛔ **No cell enables collection**, and the seven-body pool is the honest denominator
every count bar in round 12 is cut against -- **read the pool AT THE CUT**, which is the defect round 11 filed as
W19-S8.

## A1.4 THE ROUND-12 CELL SET, RESTATED WHOLE

s.5's eight stand unchanged: **A** deployed plane (model block read plus the posture redeploy under a fresh never-widen
co-sign), **B** Price producer, **C** identity and union universe, **D** tab scores, **E** five-route exercise surface,
**F** criteria repair at the issuer, **G** social source classified, **H** preserved breaches.

Four are ADDED: **I** the DEV integration of the page (R1, FIRST), **J** the print pack packaged so `FWD-5` serves
(R2), **K** the on-demand pull wired (R3), **L** surfaces for `FWD-7` / `FWD-12` / `FWD-14` (R4, sequenced last).

⭐ **AND CELL I CHANGES WHAT CELL E CAN EVEN MEAN:** round 11's browser half exercised a **local vite serve** of portal
`0e153399`. Once the page is on DEV, the exercise runs against the integrated branch, and that is the first time the
front-end and the deployed adapter are read together on the plane a person would actually use. **Cell E is therefore
chained after cell I, not beside it.**

## A1.5 WHAT IS REAL, recorded so the gaps are not read as "nothing works"

The adapter is deployed, edge-authorized and answering: identity MEASURED, description SERVED from D-1, a publisher feed
SERVED, on `4.0.0_SA_CRO~Z`'s own GET invoke. The daily chatter ranking serves keyed rows. The pool carries the
crosswalk, the union universe (256 names), filings 5, drafting 5, peers 33, management 5, posture 2. **The page code is
whole** -- header, five tabs, print action, harnesses -- **and merges into DEV with zero conflicts.** The distance from
here to a product a person opens is real work, and it is a great deal less than the distance already travelled.

---

# ADDENDUM 2 -- 2026-09-16 ~05:2xZ: A-L REPAIR THE PLANE, NOT THE POPULATION. Three rulings corrected, one cell added, two cards to Andrew.

**Author:** `1.0.0_SA_CTO~Z`. **Trigger:** `4.0.0_SA_CRO~Z`'s residual projection (msg 23389), record
`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/AMGT_RESAPP_POST_ROUND12_RESIDUAL_PROJECTION_20260916_Z.md`
**@`1d5454312a`**, answering this seat's own question at msg 23388 s.4.

## A2.1 THE FINDING, AND IT IS THE ONE THAT DECIDES WHETHER THIS IS A PRODUCT

**Cells A-L repair the PLANE -- deploy, wiring, surfaces. NOT ONE OF THEM RUNS A PRODUCER OVER THE COVERAGE
LIST.** After all twelve land, a person opening a **pilot** name (BA, BABA, COST, HD, SAP) gets a page whose
tabs answer. A person opening **any other covered name** gets tabs that each say ABSENT -- honestly, correctly,
and uselessly.

**Measured: 10 of 19 outcomes still ABSENT for a non-pilot covered name after A-L** (`FWD-1, 3, 5, 8, 9, 10,
16, 17, 18, 19`). And 2 of the 5 pilots fail four more, because COST and HD have no model block at all.

⭐ **THAT IS ONE AXIS ACROSS TEN OUTCOMES, NOT TEN DEFECTS** -- and it is invisible to every per-outcome check,
because each outcome's own cell is correctly built. It is Rule 22's shared-dependency blindness one level above
the cells: **A-L share a dependency they do not name, which is that somebody has run the producers.**

The producer census, read from the pool rather than from any status:

| producer | has run over | schedule | in A-L? |
|---|---|---|---|
| model block | **3 covered names** (BA, BABA, SAP) + NVDA, which is NOT covered | none; terminal `ok:false` | **NO** -- A reads what exists; D pulls SCORE inputs, not the block |
| filings analyzer + drafting | 5 names | task DISABLED | RESERVED |
| exec management | 5 names | task DISABLED | RESERVED |
| posture | 2 names | none | **NO** -- A redeploys the READ |
| similarity ranker | 33 (10 with members) | none | C repairs the empties but does not say the ranker RE-RUNS |
| harvest | 7 bodies / 3 names | DISABLED | RESERVED (A1.3 R5) |
| Price | **never** | -- | B |

**`4.0.0_SA_CRO~Z`'s correction to its own earlier audit is accepted and recorded:** G2's "4 of 89 covered
names" should read **3 of 89 plus NVDA, which is not covered**. The key count was right and its denominator was
not -- the exact shape Rule 22 reserves the word COVERAGE for.

## A2.2 THREE RULINGS CORRECTED -- each was wrong as written, and the correction is this seat's

**C1. R3 (cell K) WAS WRONG. An event-source-mapped Lambda CANNOT reach the terminal.** `pull_consumer.py`
calls `model_block_pull.stage_pull`, which is the Bloomberg DAPI at `127.0.0.1:8194` **on this box**. A Lambda
consumer would drain the queue and fail every message at `bloomberg_health`. The seam is **box-side by its own
design** and the code says so (`sqs.tf` header; the poller is "never a persistent service").
⭐ **AND IT HAS WORKED ONCE, END TO END:** `packs/NVDA_US_Equity/status.json` reads `LANDED`, requested
2026-09-11T00:53:58Z, landed 00:54:02Z, with its raw and derived keys named. `FWD-2`'s own case, exercised by a
person running the poller. **The outcome is not unbuilt; it is unwired at the page and unactivated at the
cadence.**
**CORRECTED RULING:** cell K wires the page's Refresh to the enqueue route so the 501 disappears, and the
adapter declares its queue carrier. **The consumer STAYS ON THE BOX.** Its cadence is the same reserved-class
activation as the harvest -- Andrew's word, "local on this device with some kind of local cron job"
(`@187f003998`) -- and is **a card, not a cell**. ⛔ No Lambda consumer is built.

**C2. R4 (cell L) FOR `FWD-12` WAS INCOMPLETE.** `ledger.py`'s `CLASSES` carries `stage: None` for **6 of 6**
classes, so a surface over it would record SKIPPED for every re-run and the button would be a decoration.
**CORRECTED RULING:** cell L **binds the stages that exist** -- `market_data` to the block pull, `filings` to
the analyzer, `news` to the harvest worker -- and the re-run control **refuses with a NAMED REASON** where
activation is reserved, rather than silently recording SKIPPED. A control that cannot act says why. If the
binding cannot be cut inside round 12's fan-out, the surface ships as **READ-ONLY with the re-run stated as
round 13 in the issuance data** -- never as a button that does nothing.

**C3. A's JUDGMENT CRITERION WAS UNGRADEABLE AS WRITTEN.** "Does the page a person opens now show the figures"
reads ABSENT for **86 of 89** covered names, so a grader could call it PASS or FAIL honestly.
**CORRECTED:** the criterion **names the page (`BA_US_Equity`)** and **prints the block count from
`derived/model_block/` at the cut beside it**, so "3 of 89" travels as data with the grade instead of being
discovered later. ⭐ A judgment criterion still needs a printed denominator; judgment is about the verdict, not
about the evidence being vague.

## A2.3 ONE CELL ADDED

**M. THE RANKER RE-RUNS OVER THE NAMES CELL C NEWLY RESOLVES.** C repairs 23 empty peer sets and the
company-FIGI dedup, but nothing in its text says the similarity ranker runs again over the identities C
creates. Without that, C's own output is a better crosswalk feeding the same 10 populated peer sets. **Cell M
is a re-run, not a rebuild**, and it is chained after C.

## A2.4 TWO CARDS AT ANDREW -- RESERVED, AND NOT SELF-ADJUDICATED

Both move the POPULATION, both are his by a named class, and **this seat is not taking either**. Each carries
this seat's recommendation, which is what a card owes him.

**CARD 1 -- THE MODEL-BLOCK PULL OVER THE 33 KEYED COVERAGE NAMES.** Today: 3. Gate: a signed-in terminal, the
two-phase budgeted sign-in (`integrations/bloomberg/READ_HERE.md`), and **the Bloomberg-terms question this PRD
itself holds OPEN**. Class: **vendor use** -- `CLAUDE.md` is explicit that availability is not authorization and
that an external vendor call needs his per-use word. **RECOMMENDATION: YES, and it is the single highest-value
act available to this project** -- it converts the Model tab, the thesis figures and the Posture comparables
from "correct and empty" to populated across the coverage list, and it moves the most outcomes per unit of
work of anything in round 12. The terms question is his to close and it is the reason this is a card.

**CARD 2 -- THE FILINGS AND DRAFTING BATCH OVER THE UNION UNIVERSE.** Today: 5 names. Gate: his word
(`rj-6 AC4`, "activation is Andrew's word") and **cost, roughly USD 100 for the 89** at the measured
~USD 1.1 per filing. Class: **reserved by name, and money**. **RECOMMENDATION: YES for the 33 keyed names
first, not the 89** -- the unkeyed names cannot render an identity-joined page anyway, so spending on them buys
nothing until cell C widens resolution. That is roughly USD 36 for the population that can actually display.

⚠ **WHAT HAPPENS IF NEITHER CARD IS ANSWERED, stated plainly so nobody discovers it at the close: the product
is FIVE NAMES.** Round 12 would land twelve cells, every criterion could pass, and the
`COMPLETION_REPORT` would have to say that a person opening the 84 other covered names sees an honest ABSENT on
every tab. ⛔ **That sentence is the one this project must not write by accident**, and it is exactly the class
of thing Andrew asked `4.0.0_SA_CRO~Z` to catch.

## A2.5 WHAT IS NOT CHANGED BY THIS ADDENDUM

Cells A, B, D, E, F, G, H, I and J stand as written in s.5 and A1.4. The v0.9 PRD (`@44269d0515`) is untouched:
none of these corrections changes ratified text -- K, L and M are **cut-level shape**, and the two cards are
decisions that belong to Andrew rather than to the PRD. `3.0.0_SA_CVO~Z`'s pending ratified-text signature is
**not re-opened by this file** and the half hash `88e330dea809` still stands.

---

# ADDENDUM 3 -- 2026-09-16 ~05:4xZ (self-drive tick 2): the FIT contract ruled, the social cost ruled, and round 11's five open slug rows dispositioned

**Author:** `1.0.0_SA_CTO~Z`, adjudicating in its own lane per Andrew's ~04:3xZ word. **Why this exists:** the
tick's first question is *what is waiting on THIS seat*, and three channel rows reassigned to the CTO limb at
`Z-S109` carried no ruling, while **the FIT is named in the slug's obligation 2 and is covered by NO cell in
A-M.** A gap between a named obligation and the cell set is the thing this loop exists to catch.

## A3.1 THE FIT -- RULED (settles `W20-S9` and `W20-S10`, which are ONE defect in two places)

**What is measured.** `W20-S9`: card 3 carries the DIVZ and PFOE presets as **counts and weights, not as factor-code
lists** -- DIVZ names 7 of its 13 codes, PFOE **0 of its 16**, so **22 of the 29 preset slots have no code to
read**. `W20-S10`: R-1's rows carry **no scanner factor values at all** -- the ranker's loader keeps the 284-code
set and **drops the numbers by design** -- so every fit score is ABSENT, 0 of 13 and 0 of 16, for all four names
of the QA pair.

⭐ **THESE ARE NOT TWO FINDINGS. The fit needs a CODE to read and a VALUE to read for it, and both ends are
missing** -- so repairing either alone moves nothing and would grade as progress. Naming the 22 codes against
rows that carry no values still yields ABSENT; retaining values for codes the preset never names still yields
ABSENT. **A cell that fixes one end and passes its criterion is the failure mode here.**

**RULED: the fit is made COMPUTABLE, in ONE cell that carries BOTH ends, or it is not cut at all.**
1. The presets name **every** factor code they score under -- 13 of 13 for DIVZ, 16 of 16 for PFOE, the printed
   denominator beside each.
2. The ranker's loader **retains the factor values for exactly those codes** on the R-1 rows. Not the 284-code
   set: the named codes, so the retention is bounded by the presets rather than by the scanner's width.
3. The fit score is ABSENT **with a classed reason** wherever a named code has no value for a name -- the source
   lacks it, or our pull missed it (A1.3's classing rule, applied here).
4. **Its criterion asserts a NONZERO factor count on a real name**, not the absence of an error. A fit that
   renders ABSENT everywhere satisfies "the tab renders" and proves nothing.

⛔ **NOT RULED: retiring the fit.** It is part of the surface Andrew approved (PRD s.3b, "Recs approved"), and
retiring a ratified surface element is an endpoint change, not a cut-level call. If the fit proves uncomputable
on measured grounds, that is a card at Andrew with the measurement, never a quiet drop.

**CELL N** (round 12): the fit made computable, both ends in one cell. Chained after **C** and **M**, because
the codes are read against the peer rows those two repair.

## A3.2 THE SOCIAL COST -- RULED (settles `W22-S7`)

**What is measured:** cost cannot be read with the key on any route probed -- the progress payload carries no
cost field, the snapshots listing carries none, and the balance route refuses the key **403, "Your API key lacks
the required permissions for this action."** So `S-1 cost.usd` is null with claim `absent`, and the only USD
figure in the record is the **pre-call estimate**, claim `held`.

**RULED, and it is a claim-discipline ruling rather than a build one:** the cost field stays **ABSENT with its
reason recorded** -- *the key lacks billing permission* -- and the pre-call estimate is REPORTED as `held`,
**never promoted to `measured`.** ⛔ **The estimate must not be allowed to drift into the measured slot**, which
is precisely what an unenforced provenance field does: an estimate sitting where a measurement belongs reads as
a measurement to every later consumer. This is `A_VALUE_MUST_CARRY_ITS_CLAIM` at its narrowest and most literal.

**A key with billing permission is a CREDENTIAL act and is NOT taken tonight.** It is not carded either: the
social source is already unproven as a feed (cell G classifies it), and asking for a credential to measure the
cost of a feed we have not decided to run inverts the order. **If cell G's classification says the feed is worth
running, the billing key rides with that decision and not before.**

## A3.3 ROUND 11's FIVE OPEN SLUG ROWS -- DISPOSITIONED

`3.0.0_SA_CVO~Z` read these as the analysis's to disposition (msg 23377) and it is right. `project.json`'s
`blocking` field names them as round 11's open five. Each is dispositioned here against the artifact, not the
prose:

| row | disposition | grounding |
|---|---|---|
| `Z-S95` ranked click lacks the canonical key | **REMEDIATED in round 11** | rj-1 landed the canonical key on the ranked click; rj-10's served capture carries **10 of 10** rows with a `security_key`; the slug records the repair and updates its clock in v10 |
| `C-S196` no drafted sections, evidence tooltip-only | **REMEDIATED in round 11** | rj-2 serves validated D-1 with **38 of 38** sentences carrying passages, and the browser half read **48 evidence blockquotes, 0 tooltips** |
| `W17-S4` / `W17-S5` issuer criteria | **CARRIED into cell F**, not closed | they are the criteria-repair class the slug's obligation 5 addresses AT THE ISSUER; cell F owns them and they close when round 12's orders assert nonzero collected denominators |
| `Z-S96` two article stores | **RESOLVED by `C-ONE-STORE`**, disarm row already filed by `1.0.0_SA_CTO~W` | the contract settled the question; no further act |

⚠ **`W17-S4`/`W17-S5` are the only two still open, and they are open BY DESIGN** -- a criteria-repair obligation
cannot be closed by a ruling, only by the next cut writing better criteria. **They are NOT a blocker on the
round-12 issuance** and `project.json`'s `blocking` field is corrected in this commit to say so, because it
currently reads as though all five gate the round.

## A3.4 WHAT THIS TICK MEASURED AND DID NOT ACT ON

- **Zero unmerged branches.** `git branch --no-merged HEAD` returns **0** -- the round-11 stranded-slug class is
  clear, and this check is now standing.
- **`2.0.0_SA_COO~Z` is WORKING, not stalled.** Zero commits in the shared tree, but plane 3 shows its own
  worktree `C:/tmp/coo-amgt-r12` on `coo-amgt-r12-20260916` at `06378dd3bd` -- Rule 14b isolation for a
  multi-file commit, created off the latest addendum. **No nudge.** ⭐ A zero-commit count in the shared tree is
  the EXPECTED reading for a correctly-isolating seat, and nudging on it would punish the right behaviour.
- **`3.0.0_SA_CVO~Z` is mid-review** of the v0.9 ratified-text half, with `Z-S109` landed. The signature is the
  last gate on the L6 issuance and nothing else waits on it.
- **The deployed plane was NOT re-measured this tick.** `4.0.0_SA_CRO~Z` measured it at ~05:0xZ and ~05:1xZ and
  nothing has deployed since; re-running it would burn the context the next adjudication needs and could not
  change an act. **Re-measure when a deploy lands, not on a timer.**
