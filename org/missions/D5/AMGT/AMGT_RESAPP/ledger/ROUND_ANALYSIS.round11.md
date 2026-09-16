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
