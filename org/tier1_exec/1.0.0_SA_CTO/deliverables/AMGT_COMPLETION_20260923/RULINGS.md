# AMGT CLOSER -- CTO RULINGS

`1.0.0_SA_CTO~Z`, site Z. **One file, appended.** `/closer`'s FILES OVER MAIL rule: *"CTO rulings append
to one `RULINGS.md` in the contract folder and go out as one message per batch, not one per ruling."*

Arming record: `ANDREW_DIRECT_20260923_193xZ_SELF_DRIVE_AMGT_ALL_THREE_CLOSER_LOOPS.md` @`a8a62f4f5c`.
⚠ **That commit's SUBJECT LINE MISDESCRIBES IT** -- it carries the acceptance-surface subject because this
seat reused a message-file path. The FILE is correct; the subject is wrong; a head-move to fix it was
correctly REFUSED by the repo guard and was not forced. Annotated forward here rather than edited in place,
which is this estate's own correction pattern.

---

## R-1 -- THE SHARED FIRST HOP HAS ONE OWNER: THE EXPERIENCE LANE, HELD BY `2.0.0_SA_COO~Z`

**The call.** `/closer`'s LIVE FIRST rule requires the shared first hop -- auth, scope, bootstrap -- to be
*"owned by ONE seat and proven live ... before any per-product offline closure counts toward an acceptance
ID."* It was unowned. **TWO seats independently named this as blocked on this seat**: `2.0.0_SA_COO~X`
(*"Shared auth/scope/bootstrap ownership: CTO `1.0.0_SA_CTO~Z` to name one owner"*, msg 25014) and
`2.0.0_SA_COO~Y` (*"assign shared first-hop owner"*, 19:45:28Z).

**RULED: the shared first hop belongs to the EXPERIENCE lane -- first-hop auth/scope/bootstrap plus all
mounted UI and client code -- and that lane is held by `2.0.0_SA_COO~Z`, the AMGT_RESAPP seat.**
One owner. **No committee ownership**, and no seat may treat a shared-hop edit as jointly held.

**Grounding, and it is not this seat's own measurement.** `4.0.0_SA_CRO~Z`, msg at 19:51:29Z, commissioned
as a DESIGN FORK under `/self-drive`'s call routing and answered inside four minutes:

> *"four tabs use the same getThesisBundle; Posture also shares getPeerSet with Peers. Eleven exports are 10
> request functions + one path helper; getCoverageSet has no mounted caller in inspected SecurityAnalysis
> tree. Six tabs/header therefore are not six independent vertical products."*

⭐ **THAT SENTENCE IS THE WHOLE RULING'S BASIS AND IT FALSIFIED THIS SEAT'S OWN PROPOSED DECOMPOSITION.**
The acceptance-surface record @`32dcce62d3` framed the product as **6 UI surfaces over 11 API functions**,
which invited a six-seat split by tab. Measured, the tabs are not independent: they share the request
functions, so a by-tab split would have put four seats inside one `getThesisBundle` contract and two inside
`getPeerSet`. **A split by SCREEN looked like a split by PRODUCT because the screens are the visible thing
and the shared client module is not.**

⛔ **AND THE DENOMINATOR IN THAT RECORD IS NOW CORRECTED: 11 exports is 10 REQUEST FUNCTIONS + 1 PATH
HELPER, and `getCoverageSet` HAS NO MOUNTED CALLER.** The record counted EXPORTS and called them
"functions the UI is backed by." An export census answers *"what does this module offer"* and never
*"what does the product call"* -- the same wrong-object shape as the `amgt`-in-`vite.config.ts` name census
that record itself was written to retire. **Two instances of one class in one document, caught by two
different seats within the hour.** COST: one mounted-caller read per exported symbol. NON-APPLICATION: a
module whose every export is known mounted.

## R-2 -- FOUR LOGICAL LANES, THREE ACTIVE SEATS; THE LANES ARE NOT THE SEATS

**RULED, adopting `4.0.0_SA_CRO~Z`'s proposed target:** four LOGICAL ownership lanes --
**EXPERIENCE** (first-hop auth/scope/bootstrap + all mounted UI/client) · **SERVED RUNTIME** (shared
API/report/generation/consumer contracts) · **CORPUS** · **HARVST**.

**Under the standing three-COO cap, LANES != SEATS.** Current personnel stand: `~X` CORPUS, `~Y` HARVST,
`~Z` RESAPP. **EXPERIENCE and SERVED RUNTIME are sequenced as two work packets INSIDE RESAPP at `~Z`**,
and a released producer slot rotates into EXPERIENCE once its bounded input contract is accepted.

⛔ **THE SEVEN-SEAT QUESTION IS NOT RULED HERE AND IS NOT THIS SEAT'S TO RULE.** Andrew floated
*"maybe UI frame and backend generalist, for 7 COOs, is the way to go."* `4.0.0_SA_CRO~Z`'s answer is
*"Prefer at most four concurrent COOs on merits, not seven"* and *"Three concurrent COOs remains the
planning cap; seven is an option to price, not an activation."* A verbatim standing Andrew-direct of
2026-09-14 ~07:0xZ reads *"We can only have 3 COOs running their respective projects/subagents at any one
time."* **A floated "maybe" does not repeal a verbatim standing cap, and reading it as repeal is the exact
silent widening CLAUDE.md forbids.** The delta is a card AT ANDREW: four lanes are wanted, three seats are
permitted, and he owns the difference.

## R-3 -- THE CRITICAL PATH IS ONE SENTENCE IN ONE CHAT, AND SAYING SO IS THE RULING

R-1 places the shared first hop at `2.0.0_SA_COO~Z`. That seat's own session bounds it: *"the direct user
instructions in this Codex session still restrict task work to an own-home COO order or named spine act;
this inbox relay does not itself replace them."* **That reading is accepted as CORRECT.**

**So the fabric's single critical path is now structural rather than technical: the OWNER of the hop every
other lane waits on cannot act until an operator sentence lands in its own Codex conversation.** That seat
wrote its own proposed unlock (msg 25016), offered as *"a proposal, not authority I am granting myself"*,
and it is carried to Andrew verbatim -- including its own final narrowing, that a review signature *"does
not authorize deployment, retained-object rewriting or gate bypass."*

⛔ **NO SEAT ROUTES AROUND THIS.** A broker relay cannot close a session-level restriction; this seat has
been wrong about that once already and is not repeating it. `send_override` exists and is NOT used here:
it forces a ROUTING gate, and this is not a routing gate.

## R-4 -- OFFLINE CLOSURES CONTINUE AND GRADE NOTHING UNTIL THE THREAD IS LIVE

`~X` and `~Y` are NOT blocked from building. `/closer`: *"Offline closures are allowed; they grade nothing
until the thread is live."* Both seats have already stated their own next proofs and both are independently
takeable -- `~X` a corpus payload check for an already-resolved `IMB_LN_Equity`, `~Y` a read-only
reachability probe for Lenovo. **Those proceed. What neither may do is count an offline closure toward an
acceptance ID, or edit a shared surface it does not own** (`~X` said so itself: *"C cannot independently
edit their shared surfaces"*).

## R-5 -- TWO REGISTRY ROWS ARE STALE AND THE STALENESS READS AS AN ANSWER

`org/projects/AMGT_RESAPP.json`'s `blocking` string asserts `AMGT-rk-49` is *"the project's ONLY
non-terminal order of 189."* **Measured at HEAD by this seat: 5 non-terminal of 191 order files** --
`rk-49` pending, `rk-58` pending, `rk-62` pending, `rk-56` status `word`, `rk-26` withdrawn. Even
discounting `rk-26` as terminal-in-substance, the row understates by at least three.

The sibling was measured independently on AMGT_CORPUS: its `project.json` phase field still reads
*"6 of 11 drained"* with five later commits landed.

⛔ **A STALE `blocking` STRING IS WORSE THAN AN EMPTY ONE: it is PROSE, it names a specific id, and it
reads as a measurement.** A driver that trusts it drives one order and believes the rest closed. Registry
rows are MSTR-written; **routed to `0.0.0_AB_MSTR~Z` as a register fix, not corrected here.** COST: one
order census per project per tick. NON-APPLICATION: a row whose `blocking` is empty or absent, which
claims nothing.

---

## R-6 -- ⛔ R-5 IS WITHDRAWN IN ITS FIRST HALF. THE REGISTRY ROW WAS RIGHT AND THIS SEAT'S PARSER WAS BROKEN

**R-5 asserted that `AMGT_RESAPP.json`'s `blocking` string understated the open-order count -- "5
non-terminal of 191" against its claim of one. THAT WAS WRONG. The row's claim is CORRECT.**

**Measured with an ANCHORED parser, `^<status>\s*([A-Za-z_]+)\s*</status>\s*$` over all 191 order files:
`complete` 181 · `superseded` 8 · `withdrawn` 1 · `pending` 1. NON-TERMINAL = 1, and it is `rk-49`** --
exactly what the row says, and exactly what `rk-49`'s own file says of itself (held by design pending
Andrew's Lusha key-rotation word).

**WHY R-5 GOT 5.** Its parser was `<status>\s*([^<]*)</status>` -- UNANCHORED -- and took the FIRST
match anywhere in the file. Exactly THREE files disagree between the two parsers, and all three
disagree for the same reason:

| order | anchored (true) | first unanchored match | loose matches in file |
|---|---|---|---|
| `rk-56.status-element-at-issuance` | `complete` | `word` | **10** |
| `rk-58.direct-act-minted-order` | `complete` | `pending` | 2 |
| `rk-62.gate-x-direct-act-exemption` | `complete` | `pending` | 3 |

⛔ **THE FILE THAT BROKE IT IS NAMED `status-element-at-issuance` -- A TASK ORDER WHOSE SUBJECT IS THE
`<status>` ELEMENT ITSELF, so it quotes ten of them in prose and its real one is the eleventh match.**
An unanchored parser reads a DOCUMENT ABOUT a record face as though the prose were the record face.
The two orders about direct-act minting and a gate exemption fail the same way for the same reason:
orders that DISCUSS order mechanics are exactly the orders that quote order tags.

⛔ **AND THE FAILURE WAS NOT SILENT-LOOKING -- IT PRODUCED A CONFIDENT, PLAUSIBLE, DENOMINATOR-BEARING
NUMBER THAT CONVICTED A CORRECT ARTIFACT.** R-5 then used it to route a "register fix" to
`0.0.0_AB_MSTR~Z` for a row that needed none, and the whole batch went to six seats. ⭐ **The tell
available at the time and not taken: `rk-56` read `word`, which IS NOT A STATUS VALUE IN ANY ENUM.**
A value outside the enum is the parser announcing it read the wrong object, and it was printed in this
seat's own output and passed over.

⛔ **THE GENERAL RULE, and it is the third instance of ONE class in this seat's session:** an
unanchored match over a document that may DESCRIBE its own format lands on the description. The
siblings were the `amgt`-in-`vite.config.ts` name census (a name census answering a coverage
question) and the 11-export count read as 11 mounted callers. **All three read a real number off the
wrong object, and all three arrived with a denominator.** COST: anchor the pattern to a full line, and
treat any value outside the declared enum as a parser failure rather than a finding. NON-APPLICATION:
a machine-written file with one occurrence by construction -- though that is a property to verify by
counting matches, not to assume.

**WHAT SURVIVES OF R-5, narrowed and re-attributed.** `AMGT_RESAPP.json`'s `phase`/`blocking` ARE
stale, but in a DIFFERENT WAY than R-5 claimed and on another seat's measurement, not this seat's:
**they describe ROUND 35 while ROUND 36 has since closed** (`ledger/ROUND_ANALYSIS.round36.md`:
*"ROUND 36 IS CLOSED, and the project's canonical phase closes with it"*). The AMGT_CORPUS half of R-5
-- `phase` reading *"6 of 11 drained"* with five later commits landed -- was measured by a separate
instrument and is ATTRIBUTED, not re-derived here.

**So the ask to `0.0.0_AB_MSTR~Z` is REPLACED, not merely reduced:** nothing is owed on the
non-terminal count, and what is owed is a round-vintage refresh on two rows. ⚠ **A correction that
only shrank the number would have left MSTR~Z hunting a defect that does not exist in the field this
seat named.**

## R-7 -- `lib/research/price/**` MOVES TO `2.0.0_SA_COO~Y`, BOUNDED AND REVERSIBLE

**The contract's own breaking-change rule is the authority: "one exchange between the peers, then
`1.0.0_SA_CTO~Z` rules."** The exchange happened and returned nothing to integrate.

**MEASURED STATE.** `2.0.0_SA_COO~Y` implemented C-GEN-TERMINAL at `621bf1d5d7`, advanced to
`56621b4949`, and its combined run reads **199 PASS / 9 FAIL -- all nine the unmigrated Price
callers**, with 158 metrics/coverage and 24 API passing. It sent `2.0.0_SA_COO~Z` a pinned Price
proposal with nine compute cases passing in memory. `2.0.0_SA_COO~Z` replied at 20:47:33Z that its
session closer exception has not arrived: **review NOT_STARTED, no consumer migration pin, no
integration.** That lane's own words: *"The nine Price failures are therefore an explicit cross-seat
blocker, not a pending ACK."*

⭐ **AND `2.0.0_SA_COO~Y` DID THE RIGHT THING, WHICH IS WHY THIS RULING EXISTS RATHER THAN A REPRIMAND:**
*"H will not edit Z surfaces or route around it."* **A lane that refuses to cross a boundary it was given
is not the problem to solve; the boundary is.**

**RULED: `lib/research/price/**` transfers to `2.0.0_SA_COO~Y` as sole writer, TEMPORARILY.** Named
files, measured rather than guessed: `axis.py`, `generation.py`, `backfill_legacy_generation.py`,
`__init__.py` and `tests/`. `backfill_legacy_generation.py` is the estate's ONLY live
legacy-republisher definition (comp-find, band DEF, 5 of 1424 hits, the other four being `.scratch`
copies and two rendered daily reports).

**FIVE BOUNDS, and the transfer is void without them:**
1. **NAMED FILES ONLY.** Anything outside `lib/research/price/**` stays SERVED RUNTIME's. A ninth
   failure needing a file outside that tree is a new blocker, not an extension.
2. **REVERTS ON ACTIVATION.** The moment `2.0.0_SA_COO~Z` can act, the surface returns to SERVED
   RUNTIME and `2.0.0_SA_COO~Y` hands a pin rather than keeping the tree. This is a loan.
3. **THE EXISTING PINNED PROPOSAL IS THE BASIS.** `2.0.0_SA_COO~Y` applies the migration it already
   designed and tested; it does not redesign the Price contract under cover of a grant.
4. **NO SERVED-OUTPUT WRITE, NO DEPLOY.** The never-widen pair still binds every served write, and
   nothing here touches the AMGT Lambda repair or its cutover.
5. **STILL NO ACCEPTANCE CREDIT.** LIVE FIRST is unchanged: `H1`-`H4` grade nothing until `E0` is
   graded. This unblocks WORK, not CREDIT.

⚠ **THE CANDIDATE BASE PREDATES THE MERGE.** `2.0.0_SA_COO~Y` states `56621b4949`'s base predates
`0e9ed7b1d8`, which landed 996 CLOUD commits. **That branch is carried forward before the Price work
integrates**, or the integration is graded against a tree the estate no longer has.

⛔ **WHY NOT SIMPLY WAIT: the thing being waited for is not in any seat's gift.** `2.0.0_SA_COO~Z`'s
restriction lifts only in its own operator's chat. **A dependency whose owner cannot act is not a
dependency, it is a stop** — and leaving nine tested failures parked behind it buys nothing and costs a
working lane its momentum. ⭐ **The reversibility is what makes this cheap: a loan that reverts on
activation risks a re-merge, where waiting risks the work.**

## R-8 -- THE GENERATION EXPOSURE IS MEASURED AND STAYS AN EXPOSURE

C-GEN-TERMINAL @`52ec61680d` named a discriminator and **deliberately did not run it**: committed
pointers reading `COMPLETE` with `row_count == 0`, the signature of a laundered non-determination.

**`2.0.0_SA_COO~Y` ran it, on the surface it owns: 305 items scanned, 22 current pointers (12
`COMPLETE` / 10 `EMPTY`), ZERO `COMPLETE` with `row_count` 0, zero ungraded `COMPLETE` counts.**

**RULED: the classification HOLDS. EXPOSURE, not incident. Nothing is re-opened.** The guard was
unreachable and there is no measured instance of it having been reached. ⚠ That lane states no
historical or causal conclusion is drawn, and none is drawn here: **22 CURRENT pointers is not the
file's whole history**, so this closes the forward question and not every question.

⭐ **This is Rule 22's negative mirror working as designed, and the cost was one query.** The remedy
stayed single — build the guard — instead of doubling into re-opening work nothing ever harmed.

## R-11 -- THE INCIDENT'S REACH IS MEASURED. CAPACITY IS NOT REACH, AND TWO CALLS GO TO ANDREW

`3.0.0_SA_CVO~Z`, msg 25116, record @`65132a45c7`. **The second half of the double remedy is MEASURED.**
⭐ **This seat named it as owed while the deploy was green; that seat measured it within the hour.**

**REACH, over 664 hourly CloudFront access-log files, 2026-09-19T00:00Z to the 21:58Z cutover:**
**521** `/api/scoped/amgt*` requests -- **423 REFUSED 401 at the edge and served nothing**, 98 served.
The auth-validator-edge gate did most of the containing.

**THE INTERSECTION THAT BOUNDS IT:** a response can carry a no-span sentence only if the security HAS
drafted sections -- one of the 12 objects under `drafting/v1/`, the complete set measured during C4. Of
21 served thesis responses, Lenovo (12), `992_HK_Equity` (4) and `DE_US_Equity` (1) are **NOT in the
corpus and carried no drafted prose at all.** **`BA_US_Equity` (4) IS.**

**REALISED EXPOSURE: four responses** -- 09-22 19:15:35, 20:14:11, 20:21:40 and 09-23 20:44:34 -- **all
`BA_US_Equity`, all from ONE client IP**, the only distinct IP across every served thesis response, plus
**one** in-corpus overlay response. **At most ~21 no-span sentences, repeated, to a single client.**

⛔ **"179 SENTENCES SERVED" DESCRIBES THE DEFECT'S CAPACITY, NOT ITS REALISED REACH.** 179 is what the
corpus WOULD have served had every security been requested; **only `BA_US_Equity` ever was.** Both
numbers are true about different things. ⭐ **A remediation that conflated them would re-open ELEVEN
SECURITIES' worth of work that nothing ever touched -- which is the negative-mirror failure from the
OTHER side of its ledger.** The rule guards against closing a guard-task on "nothing went wrong"; it
guards equally against re-opening on a number that was never realised. COST: one log census. NON-
APPLICATION: a defect whose every instance is known to have been requested.

⭐ **AND THE ZERO WAS CAUGHT BY A POSITIVE CONTROL.** The first parse read **zero** -- these files carry
a bare space-separated header rather than a `#Fields` line. **19,114 rows parsed** is what made the
eventual zeros absence rather than a broken parser. **A census of a log format you did not write starts
with a positive control or its zero means nothing.**

## R-26 -- HAND-BACK TO CANONICAL FLOW ON ANDREW'S WORD; and `closer_contract` WAS ON THE CARRIER THE GENERATOR ERASES

**Andrew-direct 2026-09-24 ~04:3xZ, VERBATIM:** *"I think we're positioned here to get back to canonical
flow. I want you to essentially clean up any residue laying about, and essentially spec out a new analysis
that can be handed off to new rounds for development on AMGT_CORPUS ... AMGT_RESAPP ... Then you can have
COO~X take CORPUS and COO~Z take RESAPP."* Full text and the two round specs:
`HANDBACK_TO_CANONICAL_20260924.md`.

**RULED.** `AMGT_CORPUS` -> `2.0.0_SA_COO~X`, `AMGT_RESAPP` -> `2.0.0_SA_COO~Z`, both back to canonical
enrichment rounds. `AMGT_HARVST` STAYS IN CLOSER -- 2a is mid-apply with the AE mandate issued, ledger
`amgt-h03-leadpanel-y-20260924` OPEN, and the never-widen pair closed against one patch hash.
**Closer work in flight completes under its own spec** (Rule 27): Peers consumer-2, failure case 3, the 2a
apply and the `DE_US_Equity` fork are closer items, not round cells.

⚠ **AND THE ANSWER TO HIS CONDITIONAL IS NO: DATA IS NOT THE ONLY THING MISSING FROM RESAPP.** Beyond
CORPUS's reach: the 5-column render (needs the `1ec5446c` portal deploy), consumer 2 UNGRADED so every
Peers case is half-graded, 0 of 3 failure cases exercised, `dated` absent from `RankingSet`, and the price
producer on a fallback **expiring 2026-09-29**. **The frontend walk is necessary and NOT sufficient**, so
the RESAPP round carries the non-data items too or it closes on a false completion.

### R-26a -- ⛔ THIS SEAT PUT `closer_contract` ON THE **GENERATED** ROW. THE GENERATOR ERASES IT, AND NOTHING WOULD HAVE SAID SO

Found while removing the field, which is the only reason it was found at all.

1. ⛔ **WRONG CARRIER.** I wrote it to `org/projects/*.json` -- the GENERATED index.
   `org/standards/PROJECT_TREE.contract.json:121`: *"an index entry carrying `home` is GENERATED from the
   tree row at `home`/project.json and **is never hand-edited**"*. `closer_contract` is not among the
   eleven `index.fields` (`:100-110`) at all.
2. ⛔ **AND IT IS ERASED ON THE FIRST WRITE.** `.tools/missions-tree-index.py:356` is a FULL OVERWRITE with
   `compose_index(t)`, built from the TREE row; `:352-354` skip that write only while all six
   `compared_fields` match -- `directive, macro_code, fabric, `**`dep_stage`**`, `**`status`**`, name`.
   **The field survived only because nothing had moved yet, and `dep_stage`/`status` are exactly what a
   closer changes.** The HARVST skip I believed I had installed was one `derive --write` from vanishing.
3. ⭐ **THE DISCRIMINATOR IS A CLEAN INVERTED PAIR AND IT SETTLES WHICH FILE IS RIGHT.** `IRPT_BCKEND` /
   `IRPT_FNTEND` -- the precedent that CREATED this field -- carry it in the **tree** row
   (`org/missions/D9/IRPT/*/project.json:41,43`) and **ABSENT** from their generated rows. AMGT carried it
   in the **generated** row and **ABSENT** from the tree. **Exactly inverted; mine is the outlier**, and the
   skills' own words are *"a project whose `project.json` carries..."*, which is the tree file.
4. ⚠ **`missions-tree-index.py check` reads `RESULT: 0 violation(s)` BOTH BEFORE AND AFTER**, over 25 tree
   projects and 374 index rows: an extra key in a generated row is not INDEX-DRIFT, which grades only the
   six compared fields. **The instrument that exists for this file could not see it.**
5. ⛔ **THE FIELD HAS NO MECHANICAL CONSUMER AT ALL.** Census: **49 hits across 72,197 files** --
   `SURFACED=4` (three of them my own comp-rail log lines), `CONFIG=5` (the `project.json` rows),
   `DOC=40` (skills + spine). **Not one `.py` or `.sh` reads it.** So the skip is a READING rule, not a
   gate -- the law-stronger-than-tool shape this seat has ruled on four times tonight, asserted as
   mechanical in this very hand-back's first draft.

**REMEDIED IN ONE COMMIT:** off all three generated rows, onto the `AMGT_HARVST` **TREE** row, appended
exactly as `IRPT_BCKEND` does. ⭐ Side effect: the three generated rows are now byte-canonical to what the
generator writes (`indent=1, ensure_ascii=True`), where my earlier hand-edit had reformatted them to
`indent=2` -- **so the next `derive --write` is a no-op instead of a diff**; the tree row keeps its
hand-authored `indent=2`, making its diff 3 insertions / 2 deletions instead of 139 lines of churn.
⭐ **THE GENERALISATION, WHICH IS THE PART WORTH KEEPING: A FIELD WRITTEN TO A DERIVED ARTIFACT READS BACK
CORRECTLY FOR EXACTLY AS LONG AS NOTHING REGENERATES IT** -- every read passes, the checker passes, and the
erasure is triggered by the very state change the field exists to survive. **Before writing a field, ask
which file DECLARES it and which file is DERIVED from that one.**

### R-26b -- THE RESIDUE SPLIT IS PUBLISHED WITH ITS DEFINITION, BECAUSE TWO RIGHT NUMBERS DISAGREE

**67 local branches = `CLOUD` + 53 fully merged + 13 carrying unique commits.** ⚠ `git branch --merged
CLOUD` reads **54 because it counts `CLOUD` itself**; 54 + 13 = 67 and the deletable set is **53**. Both
numbers are correct under different definitions, so the definition is printed beside the number.
⛔ **THIS SEAT DELETES NEITHER A WORKTREE NOR A BRANCH IT DOES NOT OWN, INCLUDING THE 53 "SAFE" ONES** --
43 worktrees, 0 prunable, each a live seat's workspace; three of the 13 unmerged were written in the last
90 minutes; and **a branch census cannot see whether a worker was ever spawned**, so a zero-commit `wk-*`
reads identically live or abandoned. Routed to `0.0.0_AB_MSTR~Z` as an integrator decision with the
denominator printed. `.runtmp_*`/`.scratch` regrowth: **0** -- the earlier ~38 MB sweep held.

## R-25 -- 992_HK CLOSED NOT-A-DEFECT ON ARITHMETIC, and an enrichment item was STRUCK BECAUSE IT ALREADY EXISTS

**`2.0.0_SA_COO~Z` supplied the measured cause; `3.0.0_SA_CVO~Z` VERIFIED IT ARITHMETICALLY rather than
accepting it** (msg 25227), re-reading both payloads it already held:

| | before | after |
|---|---|---|
| SUBJECT cap | 419,619.12 | 456,118.54 |
| **all 11 common members' caps** | **BYTE-IDENTICAL, 11 of 11** | |
| every surviving member's `cap_ratio_to_subject` | scaled by **exactly 419619/456118** (AMAT .9980->.9182, CSCO 1.1354->1.0446, NFLX .7312->.6727) | |
| `BYXXXJ` cap 87,129.7 | ratio .20764 | **87129.7/456118.54 = .19102 -- BELOW the 0.2x floor** |

⭐ **THE UNIFORM SCALING IS THE DISCRIMINATOR AND IT IS DECISIVE: A PURE SUBJECT-CAP MOVE PREDICTS EVERY MEMBER
RATIO SCALING BY ONE COMMON FACTOR. A MEMBER-DATA MOVE COULD NOT PRODUCE THAT.** `BYXXXJ` left because the
SUBJECT grew past it, not because member data changed. **992_HK is CLOSED as NOT A DEFECT -- the ranker's
intended output on moved inputs.** ⭐ **A cause that PREDICTS a pattern and is then measured against it is
worth more than a cause that merely explains the observation.**

### ⛔ R-25a -- THE FIELD THE ENRICHMENT ITEM WOULD HAVE ADDED WAS ALREADY THERE AND ALREADY CORRECT

That seat wrote *"the SUBJECT cap's vintage is carried nowhere on R-1."* **IT IS CARRIED, at
`subject.cap_vintage`, AND IT MOVED:** `2026-09-16T20:18:16Z` -> `2026-09-22T20:12:18Z` -- **exactly the two
model-block partitions the cause names.** **Enrichment (a) "R-1 carries `subject.cap_vintage`" is STRUCK, not
implemented.** Caught because that seat went to check whether the proposed field already existed **before
anyone built it**.

⭐ **AND THE HONEST READING IS SHARPER THAN A MISSING FIELD: THE OBJECT WAS ALREADY ATTRIBUTABLE. A consumer
comparing `cap_vintage` across the two objects would have seen the subject input move and known why membership
changed. NOBODY LOOKED** -- not the producing seat, and not the grader until it went to check. **"The
attribution was not absent; it was UNREAD."**

⛔ **THAT IS A FOURTH MEMBER OF R-22's CLASS, AND THE SHARPEST ONE, BECAUSE IT INVERTS THE OTHER THREE.** In
`peer_read {}`, `K3` and the `task-orders` path, the instrument **could not see** what was there. **Here the
instrument saw it perfectly and NOBODY ASKED IT.** ⭐ **So the class is wider than blind readers: BEFORE
PROPOSING A FIELD THAT WOULD ANSWER YOUR QUESTION, QUERY THE PAYLOAD FOR IT** -- the cheapest fix is the one
already shipped. **COST: one read of the object you are about to extend.**

⭐ **ENRICHMENT (b) STANDS AND THE DISTINCTION IS EXACT: a MEMBER-SET DIGEST on R-1 so a consumer watching
identity/basis/count/status can see membership move. `cap_vintage` does NOT cover it -- `cap_vintage` says an
INPUT moved, a digest says the OUTPUT did, AND EITHER CAN MOVE WITHOUT THE OTHER.** Worth building; (a) is not.

### ⭐ R-25b -- R-24a IS ACCEPTED AND **SHARPENED**: a no-regression claim has TWO ARMS, not one

R-24a said: pick a control that COULD have regressed. `3.0.0_SA_CVO~Z` records the stronger form and binds
itself to asking for both:

> **"A NO-REGRESSION CONTROL MUST BE A CASE THE ACT REGENERATES AND THAT WAS FREE TO DIFFER. A case that could
> not have changed proves the act did not CORRUPT it, and proves NOTHING about FIDELITY when inputs move."**

⭐ **SO THERE ARE TWO ARMS AND THEY ANSWER DIFFERENT QUESTIONS: an UNTOUCHED case proves NON-CORRUPTION; a
case FREE TO DIFFER proves FIDELITY. R-24a asked for the second and implied the first was worthless -- it is
not, it is simply a different claim.** BA was a sound non-corruption control and a void fidelity control, and
the defect was citing it for the second. **Both arms are required; this seat's ruling is amended to say so.**

**UNCHANGED:** consumer 2 ungraded · the three failure cases unexercised · `BP%2F_LN_Equity` 404 OPEN as
failure case 3. **The route/data PASS stands and 992_HK is closed on cause.**

## R-24 -- PEERS ROUTE LAYER **PASS**, and the grade found a SILENT MEMBER SWAP no summary field can see

**`3.0.0_SA_CVO~Z`** graded `f12263b4e7` on deployed bytes **against its OWN pre-build baseline
(`99f8d35d37`, 02:3xZ) rather than against the handoff's figures** (record @`bb4d36e32c`).
**ROUTE/DATA LAYER: PASS.** `CodeSha256` UNCHANGED, so **every change is attributably the POOL PUBLICATION
and not a code deploy** -- the cleanest possible attribution.

| selection | before | after |
|---|---|---|
| `BA_US_Equity` | MEASURED/derived/12/SERVED | same |
| `992_HK_Equity` | MEASURED/derived/12/SERVED | same *(summary fields)* |
| **`ASML_US_Equity`** | UNRESOLVED/absent/0/(none) | **MEASURED/absent/0/SERVED** |
| **`CAT_US_Equity`** | MEASURED/absent/0/ABSENT | **MEASURED/derived/12/SERVED** |
| `NOSUCHKEY_ZZ` | UNRESOLVED/absent/0 | same |

⭐ **THE DISCRIMINATOR, IN THAT SEAT'S WORDS: "EXACTLY THE TWO THE MANDATE SAID WOULD MOVE, MOVED; THE
NEGATIVE CONTROL DID NOT. That is what separates 'the fix worked' from 'everything now resolves', and only
the second would also show NOSUCHKEY resolving."** A fix that resolved the negative control would have been a
widening, not a repair. Also graded sound: ASML's reason **names the missing model_block, cites F2/G-24, and
records that NO NEW BLOOMBERG CALL was made** -- consistent with R-21's mechanism ruling; CAT's 12 members are
security-scoped with a distinct payload hash; and 992_HK's FX caveat (*"NO FX rate is applied and none is
invented"*) is **refusing to invent a rate, which IS the criterion, met.**

### ⛔ THE FINDING: 992_HK's SUMMARY FIELDS ARE UNCHANGED AND ITS MEMBERS ARE NOT

```
BEFORE  BFZ7XB B7GJP7 BLN7Y2 BMZNGH  BYXXXJ  AMAT ORCL LRCX CSCO INTC BMMV2K NFLX
AFTER   BFZ7XB B7GJP7 BLN7Y2 BMZNGH  CSCO AMAT ORCL INTC LRCX BMMV2K  B929F4  NFLX
```

**`BYXXXJ` LEFT, `B929F4` ARRIVED, plus reordering -- while identity MEASURED, basis derived, count 12 and
status SERVED are IDENTICAL ACROSS THE CHANGE.** ⭐ **SO EVERY SUMMARY FIELD THE ROUTE SERVES IS INVARIANT
UNDER A MEMBERSHIP CHANGE. A consumer watching identity/basis/count/status cannot detect it.**
⭐ **AND BA IS THE CONTROL: its member list is BYTE-IDENTICAL IN THE SAME ORDER across the same republish**, so
this is specific to 992_HK and **not** an artifact of regenerating every object.

⛔ **NOT A DEFECT CLAIM, and that restraint is correct.** A regenerated set may legitimately differ on fresher
inputs. **BUT `universe_vintage` is UNCHANGED at 2026-08-06, so the universe did not move.** **OPEN, and it
needs ONE SENTENCE FROM THE PRODUCING SEAT, not an assumption from a grader: why did `BYXXXJ` leave and
`B929F4` arrive, and is that the ranker's intended output on 2026-09-24 inputs? THE CASE CANNOT GO TO FULL
PASS UNTIL THAT IS ANSWERED.** Relayed to `2.0.0_SA_COO~Z`.

### ⭐ R-24a -- THE CONTROL THE BUILDER CHOSE WAS THE ONE CASE THAT COULD NOT REGRESS

⛔ **THE STRUCTURAL POINT, offered with no suggestion of concealment and worth more than the swap itself: the
handoff's post-act instrument list names AAPL, CAT, 6861_JP, ASML, BA and NOSUCHKEY -- NOT 992_HK -- and cites
BA as the NO-REGRESSION evidence. BA IS THE SELECTION THAT DID NOT CHANGE.**

⭐ **RATIFIED AS A STANDING TEST: A NO-REGRESSION CONTROL MUST BE A CASE THAT *COULD* HAVE REGRESSED.** BA was
already derived/12/SERVED with unchanged inputs, so it had no room to move; citing it proves the act was
survivable for cases the act does not touch, which is **not** what "no regression" claims. **The case that can
regress is one the act DOES regenerate and whose content is free to differ** -- 992_HK.
⚠ **A seat reasonably reports its own working set, and 992_HK sits in the CVO's mandate's five, not the
builder's.** ⭐ **THIS IS PRECISELY THE GAP AN INDEPENDENT BASELINE EXISTS TO CLOSE, BECAUSE THE AFTER-STATE
ALONE LOOKS PERFECTLY HEALTHY** -- and it is the third time tonight that grading against a
*separately-captured* before-state beat grading against a report. **COST: pick the control by asking what it is
free to do, not by whether it passed.** NON-APPLICATION: an act with a single affected case, where control and
subject coincide.

**NOT REACHED AND NOT IMPLIED (that seat's own limits, kept):** **CONSUMER 2 IS UNTOUCHED, so every case is
HALF-GRADED by the mandate's own rule** and it will not credit one on the Peers side alone · nothing rendered
(no column states, no "5 present / 12 absent of 17", no P/E 2026 label) · the three failure cases unexercised ·
the trace folders and receipt are LOCAL on a branch and are **attributed, not verified** · and **direct invoke
bypasses the edge, so a `/market` redirect is undetectable by that instrument.**
**Standing findings acknowledged rather than worked around:** `BP%2F_LN_Equity` 404 is **mandate failure case 3
and is OPEN**; `DE_US_Equity` UNRESOLVED (R-23a, routed to CRO~Z).

## R-23 -- PEERS B04/P1 IS PUBLISHED. The signed act held its blast radius, VERIFIED BY THE SIGNER on an independent instrument

**Act executed 03:33Z by `2.0.0_SA_COO~Z` under both halves** (COO @`4c7d0b2e7c`, CTO @`429efcdf30`).
**Receipt:** `PEERS_CANDIDATE_20260924T0310Z/PUBLICATION_RECEIPT.json` @`f12263b4e7`.

⭐ **THE BRANCH-B PRE-FLIGHT CONDITION WAS HONOURED IN-PROCESS, AND WIDER THAN THIS SEAT REQUIRED:**
`head-object crosswalk/v1/2026-09-24.json` -> **404**, with the `2026-09-22` control at **200**, **plus peer
keys 0 of 194 present** -- a check the half did not ask for. **Branch A confirmed AT PUT TIME, not at signing
time, which is the whole point of the condition.** Then `publish_peers_candidate.py` put the exact signed
bytes, sha-checked per file: **UPLOADED 194 of 194 + 1 crosswalk; READ-BACK 195 of 195.**

⭐ **VERIFIED AT THIS SEAT ON AN INDEPENDENT INSTRUMENT, because a signer who never checks the act it
authorized has signed nothing:** `crosswalk/v1/2026-09-24.json` = **523,207 bytes**, LastModified
**2026-09-24T03:32:47Z**, `document-sha256 9bd953b9...`. ⭐ **AND THE BLAST-RADIUS PREMISE HELD: the PRIOR key
`crosswalk/v1/2026-09-22.json` is STILL 203,327 bytes at LastModified 2026-09-22T17:21:29Z -- byte-length
identical to this seat's pre-signature read and dated two days before the act. NOTHING PRE-EXISTING WAS
TOUCHED**, measured rather than inferred from the producer's promise.

**POST-ACT ON THREE INSTRUMENTS (that seat's):** (1) pool -- `load_crosswalk` answers from the new key,
`resolve()` over the 191 prior pool keys = **191 MEASURED** (proof obligation 2, met). (2) deployed function,
direct invoke, **`CodeSha256` UNCHANGED** -- `AAPL` derived 10 SERVED with `price`/`ev`/`ey` on members, `CAT`
derived 12, `6861_JP` derived 4, **`ASML` SERVED with `basis: absent` and its "no classification" reason**
(the hop-4 strand, resolved), `BA` derived 12 with carried fields, `NOSUCHKEY` UNRESOLVED. (3) served stack,
signed-in re-walk 03:34Z against the 03:20Z before-state under **the same identity, bundle and function -- the
only thing that moved between them is the pool publication.**

⚠ **ONE THING CORRECTLY NOT CLAIMED: the counts line still reads "1 column(s) carry"** because the served
bundle carries the OLD column map. **The 5-column render lands with the PORTAL DEPLOY of `1ec5446c`, which is
MSTR's merge and Andrew's word -- NOT this act.** That seat scoped it rather than letting a pool publication
appear to close a render.

### R-23a -- THE `DE_US_Equity` CALL: a THIRD crosswalk source is NOT what R-14 refused, and this is a DESIGN FORK

⭐ **`2.0.0_SA_COO~Z` CORRECTED ITS OWN INFERENCE, UNPROMPTED, WITHIN ~15 MINUTES.** Its 03:22Z handoff said
`DE_US_Equity` *"is among the 158 the candidate registers"*. **It is NOT.** Deere is a scanner **MEMBER**, never
a `universe/v1` **SUBJECT**, so no registration source carries it and Posture reads it UNRESOLVED after the act
on **both** the browser and the direct invoke. Its own words: *"That sentence was inferred, not measured."*
⚠ **This seat did NOT relay that inference** -- the never-widen reply carried the OBSERVATION (Posture returned
UNRESOLVED) and not the explanation, which is the only reason the error stopped at one seat.

**THE CALL:** the comparable key space is the **scanner candidate universe, 2,851 rows** -- **14x wider than
the 194 subject keys** -- and R-1's member identity block already says UNRESOLVED for such members.
**Its REC:** register scanner-row tickers carrying an exchange code as a **THIRD crosswalk registration source**
under the same refusal rules. **Alternative:** Posture names only comparables inside the crosswalk.

⛔ **AND THE FIRST THING TO SETTLE IS THAT THIS IS NOT WHAT R-14 REFUSED, OR A LATER READER WILL THINK THIS
SEAT CONTRADICTED ITSELF.** R-14 refused **the ROUTE accepting a landed peers object's own identity block** --
a resolver trusting the artifact it is resolving. **This proposes a new REGISTRATION SOURCE IN THE BUILDER,
under refusal rules** -- which is *converging up to the producer*, the thing R-14 explicitly ENDORSED. **Same
direction, different surface, and the distinction is the builder-versus-resolver line.**

**RULED: this is a DESIGN FORK, and it is routed to `4.0.0_SA_CRO~Z` for pattern research before this seat
decides** -- per the call-routing table, a design fork gets research first and the decision the tick it lands.
**It is NOT blocking:** enrichment list, separate act, no build started. **The question to research is one
sentence: does registering a 2,851-row member space under refusal rules preserve the crosswalk's "never
guessed" property, or does it approach the make-any-key-resolvable state R-14 refused?** ⚠ **And the cost of
the alternative is user-visible: Posture would render UNRESOLVED for legitimate comparables on a real screen**,
so "do nothing" is not the safe default here -- both branches have a price.

**PARKED at that seat under their own words:** the 60-name induction (**scripted and deterministic per R-21,
never an agent turn**) and the slash-key route shape. **Standing findings handed to `3.0.0_SA_CVO~Z` to grade
AGAINST rather than around:** the `BP%2F_LN_Equity` gateway 404 (10 slash-key objects unreachable), the
`DE_US_Equity` UNRESOLVED, and the 5-column render pending the portal deploy.

## R-22 -- THE CORPUS WAS NEVER THE PROBLEM: `O7` IS SMALL BECAUSE **THE ABSENCE WAS IN THE READER**

**`4.0.0_SA_CRO~Y`** (msg 25203, package `PDF_EXTRACTABILITY_20260924/`, register row `RCN-0016`) on
Andrew's word *"Begin with PDF Extractibility"* (record `32a7b8aa5e`). **This is input to the `AMGT_CORPUS`
dossier addendum R-18 puts at this seat -- not the L1 brief itself.**

⛔ **CORRECTION, AND IT IS THE FOURTH INSTANCE OF ONE CLASS TONIGHT. THIS RULING FIRST SAID THE L1 BRIEF WAS
"STILL OWED FROM THAT SEAT". IT WAS ALREADY DELIVERED** -- `docs/briefs/amgt-corpus-dossier-fold-brief-20260924.md`,
committed **`be09d62ef7`** (Parts 0-VII), amended `5ef3e9a89b` (Part VIII), and handed to this seat as **msg
25189 at ~03:04Z**, about 35 minutes before this ruling was written. `4.0.0_SA_CRO~Y` corrected it (msg 25210).

⭐ **AND THE SHARPEST DETAIL IS NOT THAT THE MESSAGE SAT UNREAD -- IT IS THAT THIS SEAT PRINTED THE COMMIT
HASH OF THE ARTIFACT IT THEN CALLED ABSENT.** Tick 17's own Step-0 output reads `HEAD: be09d62ef7`. **That is
the brief's commit.** The shared tree's HEAD *was* the brief, this seat echoed the hash in its own tool output,
and then wrote a sentence denying the artifact existed. ⛔ **The evidence was not merely in the inbox; it was in
this seat's own printed measurement, one screen up.**

**The class, now four for four: the laptop scope limit ("not measured" while the answer sat in this inbox 90
minutes) · the LEG-OUTSTANDING gate · step 2's sufficiency · this.** ⭐ **Every one is a claim about ANOTHER
PARTY'S STATE made without reading what this seat already held** -- and the remedy is the same each time and
costs one read: **before writing "X is owed / X does not exist / X was not measured", check your own
holdings.** ⚠ **A statement about a peer's obligations is a measurement, not a courtesy.**

⚠ **CONSEQUENCE FOR THE ADDENDUM, stated as a named condition rather than a vague wait: `4.0.0_SA_CRO~Y` is
AMENDING the brief's `O7` and Part IV-F2 right now to cite this package, and will send the hash when it lands.
Writing the L4 addendum against bytes mid-amendment would build on a read about to be superseded, so the
addendum is cut at the AMENDED hash** -- which is one message away, not an open-ended hold.

⭐ **THE HEADLINE INVERTS THE LEAD PANEL'S. There, the pipes worked and the water was missing. HERE THE WATER
WAS ALWAYS THERE AND THE PIPE WAS BLIND:** of the 30 PDF-only folders, **26 carry a full research pack** -- 26
pillars, 27 recommendation lines, 27 risks, 26 management, 26 all three cases, 24 thesis summaries, 24 company
descriptions, 15 "Why we own" -- and **29 of 30 carry pillars or "Why we own"**. The single empty one is
**QXO** (an investor Q&A PDF only). **`O7` is therefore SMALL, and it was a READER defect, not a corpus gap.**

**THE POSITIVE CONTROL IS WHAT MAKES THAT RELIABLE:** 56 docx+pdf pairs of the same stem; of the 19 whose docx
carries pillars under the ruled continuation rule, **17 FULL, 1 PARTIAL (Alibaba -- the PDF finds one MORE),
1 NONE (Michelin, a blank template docx)**, and ⭐ **99 of 99 docx pillars recovered from the PDF.** The PDF
path recovers everything the docx path finds and occasionally more. Population read: **157 top-level PDFs, 0
zero-text, 0 read failures, 0 placeholders hydrated**, with 71 docx as the control side. ⚠ **28 further PDFs
in one Copa subfolder were NOT read** -- a stated denominator gap, not a silent one.

⛔ **THE CAUSE, AND IT IS A CLASS THIS SESSION HAS NOW MET THREE TIMES: `extract.py`'s `K3` heuristic looks for
a STANDALONE LARGE/BOLD SHORT LINE, and the PFOE author's packs label their sections with INLINE BOLD LEADS.
K3 sees NONE of them.** That is why K3 read **33 of 52** and why the scan filed those packs as "PDF-only
unknowns". **The labels were present the whole time, in a shape the detector could not perceive** --
`RECOMMENDATION`, `COMPANY DESCRIPTION`, `Long-term growth algorithm`, `INVESTMENT THESIS`, `RISKS`
(Pre-mortem first), `Ownership`, `Management and capital allocation`, `Special items`, and on updates
`Headline results`, `Positives`, `Negatives`, `Segment highlights`, `Guidance`, `Why we own`.

⭐ **THE CLASS, NAMED BECAUSE THREE INDEPENDENT SURFACES HIT IT TONIGHT: AN INSTRUMENT THAT CANNOT
DISTINGUISH "I CANNOT SEE IT" FROM "IT IS NOT THERE" REPORTS THE SECOND.** (i) `peer_read {}` -- a STRANDED
set, an object that exists whose key will not resolve, is byte-identical in the response to a security that
never existed (`3.0.0_SA_CVO~Z`, 111 sets). (ii) `K3` -- inline-lead sections reported as absent sections.
(iii) This seat's own `task_orders` vs `task-orders` path, which returned a clean confident `0 of 0`.
**In all three the world was fine and the reader was narrow, and in all three the output was a CONFIDENT
NEGATIVE rather than an error.** ⛔ **So: when a census returns "absent", ask what SHAPE the instrument
requires and whether the data is obliged to take it.**

**TWO MORE MEASURED CAUSES, both cheap to fix:** the team's PDF headings carry a **trailing colon** and
**"Valuation" is a PILLAR lead, not a section**; and a PFOE pillar lead can sit alone on its line with the
colon in a **non-bold span**. ⭐ **And one candidate cause is RULED OUT by measurement rather than left
hanging: the docx regex's 80-character lead cap is NOT a limit -- a 140-char variant gives identical counts.**

**WHAT THE ADDENDUM WILL TAKE (that seat's recommendation, adopted as the shape to write):** `extract.py`
gains the inline-lead section rule and the PFOE name set; `continuation.py`'s pillar rule gains a **PDF
branch** carrying the three rules **with the docx branch KEPT AS THE CONTROL**; the dossier gains
`thesis_summary`, `company_description`, `growth_algorithm`, `ownership`, `special_items`, `why_we_own`,
`positives`/`negatives`, **each CITED or explicitly ABSENT**.

⚠ **LIMITS CARRIED INTO THE ADDENDUM RATHER THAN DROPPED AT THE GOOD NEWS:** PFOE pillar recall has **no docx
twin to control against** (2 per pack across 24 packs is self-consistent, **not controlled**); management,
risks and cases are measured as **block presence, not typed fields**; the 28 unread Copa PDFs; and **nothing
under the library root was written.**

⚠ **AND THE FOLD CONSTRAINT FROM R-18 STILL BINDS THIS:** *"i wouldnt change AMGT_RESAPP page layout
architecturally"*, and *"Peers largely stays as it is"* -- so a richer dossier feeds the EXISTING tabs and
does not reshape them.

## R-21 -- ALL RECS APPROVED, EGRESS WIDENED TO ALL VENDORS -- AND THE GRANT IS BROAD ON **AUTHORITY**, NARROW ON **MECHANISM**

**Andrew-direct 2026-09-24 ~03:2xZ at the `1.0.0_SA_CTO~Z` terminal, VERBATIM:** *"all recs approved, and you
have all the egress you want for vendors. Only thing I'd note is that the pull should be
deterministic/scripted in nature like the existing pull, i do not like the idea of relying on an agent for
something a script can do way better."*

**CLOSED BY "all recs approved" -- 6 of the 7 `/open-calls` cards:**

| # | call | ruling |
|---|---|---|
| 1 | browser session endpoint | CDP on a signed-in admin+Dev browser, or he runs the readout. **NOT credentials.** |
| 2 | who populates gold `chatter_daily` | **`2.0.0_SA_COO~Y`**, as an explicit `AMGT_HARVST` scope item, NOT a rider on H03 |
| 3 | terminal-box schedule owner | **`0.0.3_BG_BBGTerminal`** -- it already runs the `OPAL_BBGTML_daily_pull` family |
| 5 | Lusha / `rk-49` | **WITHHELD for now** -- the gate's purpose is unmet regardless; the word buys nothing until hop 4 lands |
| 6 | FX for the 0.2x-5x band | Bloomberg DAPI spot at the universe vintage, pulled with the existing refresh |
| 7 | wider Bloomberg field set | **AUTHORIZED**, scoped to the landed universe, once per refresh |

⛔ **CALL 4 IS **NOT** CLOSED, AND SAYING SO IS THE POINT.** Its REC was *"None offered"* -- there was nothing
to approve. **"All recs approved" cannot decide a card that carried no recommendation**, and the underlying
decision (notify, or not, on the FINAL set of 4 thesis + 1 overlay to one client IP) **remains his alone**,
because per-firm attribution is reconstructable from nothing in this estate (R-11a). ⭐ **A blanket approval
must not be allowed to absorb the one card it structurally cannot answer** -- that is R-15's
"generous-answer-to-one-question" discipline applied to its own author.

### R-21a -- THE ABSENCE OF A REC ON CALL 4 WAS **BY DESIGN**, and only `3.0.0_SA_CVO~Z` could confirm it

⭐ **THIS SEAT SAID "there was nothing to approve." THAT IS TRUE AND WEAKER THAN THE REAL REASON.** That seat
(msg 25200) supplies the confirmation only its author could: **it DELIBERATELY DECLINED to recommend and said
so at the time**, VERBATIM -- *"whether that warrants a notification is ANDREW'S CALL, not this seat's, because
it turns on who the client was, which this seat cannot determine and will not guess."*

⭐ **SO THE ABSENCE OF A REC IS ITSELF THE FINDING. It is not a GAP in the card; it is what the card
CONCLUDED.** A rec would have required **guessing the one fact the decision turns on** -- per-firm attribution
is reconstructable from nothing here (R-11a), the set is FINAL at four thesis plus one overlay to ONE client
IP, and **an IP is not an identity.** ⛔ **Treating it as decided would CONVERT A DELIBERATE ABSTENTION INTO
CONSENT -- the shape of every implied-pass error this thread has corrected tonight.**

### R-21b -- THE MECHANISM CONSTRAINT IS NOW A **GRADING CRITERION**, stated before any candidate exists

`3.0.0_SA_CVO~Z` has bound itself, in its own words:

> ⛔ **"A CANDIDATE WHOSE EVIDENCE DEPENDS ON A VENDOR CALL MADE IN AN AGENT TURN IS A FAIL ON MECHANISM, EVEN
> IF THE DATA IS CORRECT."**

Its test is the boundary drawn below: **does the call's output land in an artifact, a table or a screen?** Yes
-> it must come from a deterministic, re-runnable, scheduled producer. A one-off reachability probe that lands
nowhere is diagnosis and passes. ⭐ **AND IT WILL SAY "MECHANISM" RATHER THAN "DATA", SO A BUILD SEAT DOES NOT
RE-MEASURE SOMETHING THAT WAS ALREADY RIGHT** -- a FAIL that names its own axis saves the re-cut it forces.

⭐ **ON WHY THE RETROACTIVE DISCLOSURE MATTERED, and it is that seat's line, not this one's: "A RULE WHOSE
AUTHOR CARVES OUT THEIR OWN PRIOR ACT TEACHES THE CARVE-OUT, NOT THE RULE."** Naming this seat's own R-15
`bloomberg_health` probe as the constrained class -- rather than exempting it as read-only and diagnostic -- is
what makes the boundary usable by anyone else.

⚠ **And that seat checked its OWN conduct rather than assuming it: every vendor-adjacent act it made tonight
was a READ of this estate's own planes** -- lambda invoke, `s3api`, CloudWatch, git. **NO VENDOR API WAS CALLED
BY THAT SEAT AT ANY POINT**, so it has nothing to re-cut. Checked, not asserted.

## THE MECHANISM CONSTRAINT -- the most consequential thing in his message

⭐ **THE GRANT IS BROAD ON AUTHORITY AND NARROW ON MECHANISM, and those are separate axes.** *"You have all
the egress you want for vendors"* widens **WHO MAY BE CALLED** past R-16's V1/V2 enumeration to **all
vendors**. *"The pull should be deterministic/scripted in nature like the existing pull"* constrains **HOW**.

⛔ **RATIFIED: EVERY VENDOR CALL ON THIS ESTATE LIVES IN A DETERMINISTIC, SCRIPTED, RE-RUNNABLE PRODUCER --
NOT IN AN AGENT TURN.** His reason, verbatim: *"i do not like the idea of relying on an agent for something a
script can do way better."* The model he names is the **existing** pull (`price_axis_pull.py` + `generation.py`
+ a scheduled trigger).

**HOW IT BINDS THE THINGS JUST APPROVED:**
- **Call 6 (FX):** a **field added to the universe-refresh script**, not an agent fetching rates. The caveat
  becomes a computation, which is only true if a script computes it.
- **Call 7 (wider field set):** a **field LIST in the existing puller**, extended once. ⛔ **NOT an agent
  calling DAPI per missing column** -- that is the exact shape he refused.
- **Call 2 (gold population):** a producer with a trigger, not an agent-run backfill.
- **Call 3:** already this shape -- **it is the reference implementation**, which is why he pointed at it.
- **`rk-49`/Lusha, if ever granted:** scripted induction through `add_security`, never an agent-typed lookup.

⚠ **AND IT BEARS ON THIS SEAT RETROACTIVELY, STATED RATHER THAN QUIETLY DROPPED.** At R-15 this seat made an
**agent-side** vendor call -- `bloomberg_health` -> `ok: true`, `127.0.0.1:8194`, `//blp/refdata`. It was
read-only, diagnostic, and it did de-risk the pull. ⭐ **But it is exactly the class his note constrains, and
the honest line is the boundary, not an excuse: a ONE-OFF REACHABILITY PROBE is diagnosis; ACQUIRING DATA a
producer should acquire is the thing a script does better.** Going forward at this seat: **diagnostics may be
agent-side and ad hoc; any call whose OUTPUT lands in an artifact, a table or a screen goes through a
script.** ⛔ **A scheduled producer still needs the condition HELD, not probed once (R-15's grain note), which
is a second reason the probe was never a substitute for the script.**

⭐ **AND THE CONSTRAINT IS A GIFT TO THE RECORD, NOT A LIMIT ON IT:** a scripted pull is re-runnable, has a
digest, lands in a ledger and can be graded on deployed bytes. **An agent-side call is unattributable from
git by construction** -- the same class as R-12's untracked deletion. **His preference and this estate's
evidence law point the same direction.**

**STILL GATED AND NOT LIFTED BY ANY OF THIS:** the deploy ledger for a first scheduled fire · the never-widen
pair on any served-output move · production scheduling · and ⛔ **the calls-not-picks line from R-16 stands:
`3.0.0_SA_CVO~Z`'s standing ruling on ambiguous names (`AXMB`/`AMXB`) is untouched, because a word that
permits ASKING a vendor never permits DECIDING which identity the answer belongs to.**

## R-20 -- THIS SEAT'S *REPLACEMENT* PROOF CLAUSE IS ALSO DEFECTIVE. `names_with_links` CHANGES MEANING ON GOLD

⛔ **R-19 withdrew one unreachable proof clause and replaced it with another defective one, inside the same
ruling.** The replacement said: *prove the INPUT, measured as windows resolved of 191 and **`names_with_links`
of 250***. `3.0.0_SA_CVO~Z` (msg 25194, grade @`d8f0251c85`) carries `2.0.0_SA_COO~Y`'s warning that
**handler `store_item_count`-based `names_with_links` CHANGES MEANING ON GOLD**, so a displayed **6/250 would
not prove link improvement**.

⭐ **THAT IS A UNIT CHANGE HIDING UNDER A STABLE FIELD NAME: same metric, same label, same screen, DIFFERENT
POPULATION after the source switch. A reader comparing 3/250 before to 6/250 after reads an improvement that
is A CHANGE OF SUBJECT.** ⛔ **So my replacement clause would have CREDITED a moved denominator as a better
numerator** -- the exact failure the clause was written to prevent, one level down.

**RULED, and this is the third form of the clause:** any `names_with_links` figure offered as evidence
**STATES THE POPULATION COUNTED AND THAT IT IS UNCHANGED**, or it is not evidence. **A bare before/after pair
is REFUSED.** `3.0.0_SA_CVO~Z` has bound itself to the same test: *"a moved denominator is not a better
numerator, and I will refuse a PASS on a bare before/after pair."* ⚠ **The durable lesson is not about this
metric: A PROOF CLAUSE MUST NAME THE POPULATION, NOT ONLY THE NUMBER, whenever the act being proved could
change what is counted.**

⭐ **AND THE CROSS-CHECK NEITHER LANE CLAIMED IS THE STRONGEST ITEM IN THE PACKET.** The preflight reports the
gold snapshot as **1,596 rows: 1,595 DENIED + 1 PARTIAL**. **That is EXACTLY the migration scope ratified in
`C-HV-DAILY-STATUS`** -- *"1,595 of 1,596 rows, COMPLETE/PARTIAL untouched"* -- **which `3.0.0_SA_CVO~Z`
signed at half hash `fa4257b65ca7`.** ⭐ **TWO INDEPENDENT MEASUREMENTS OF THE SAME POPULATION, HOURS APART, BY
DIFFERENT SEATS FOR DIFFERENT PURPOSES, AGREEING TO THE ROW, NEITHER DERIVED FROM THE OTHER.** So the
1,596/1,595 figure is not a coincidence of reading -- it is the same population the HARVST amendment ratified,
which is why R-19's conclusion is safe to act on.

⭐ **ARTIFACT IDENTITY CORROBORATED ON TWO ROUTES, which is what makes "ZIP unchanged" RELIABLE rather than
BELIEVED:** that lane **hashed the ZIP** -> hex `23a7a2b5c688b73a914e5554694485f861b3ae93431e79fbd482e4d6f2068c76`;
this CVO **read the Lambda API's `CodeSha256`** -> base64 `I6eitcaItzqRTlVUaUSF+GGzrpNDHnn71ILk1vIGjHY=`, which
**base64-decodes to that exact hex**, `CodeSize 669924` both. **A configuration read versus hashing the bytes --
different instruments, same object.**

⭐ **THE CLEANEST STATEMENT OF WHY H03 CANNOT FIX THE WATER, and it is that seat's:** *"the relabel changes what
a row is CALLED, never whether a publisher covered the day. 1,595 uncovered days remain 1,595 uncovered days
under any name ... a seat hoping the source switch would raise admissibility was hoping a rename would create
data."* ⚠ **The 0/191 replay is graded NOT_EVALUATED (that seat did not re-run it) and the CONCLUSION IS
ENDORSED on facts it did verify** -- the honest split between what was measured and what follows.

⭐ **CLAUSE 6 IS OBSERVED WORKING IN THE REPLAY:** `denied=0`, `no_coverage=173`, `partial=5557`. **`denied=0` IS
clause 6 behaving as ratified** -- legacy gold `DENIED` reads as `no_coverage`, so the denied counter is
reserved for a genuine refusal and reads 0 **by construction**. And `2.0.0_SA_COO~Y`'s own line -- *"DENIED
means uncovered spans here, not an observed authorization denial"* -- is **amendment 1's finding restated from a
different direction by a seat that did not write it.**

**The role-name catch is confirmed independently:** `amgt-resapp-chatter-axis-lambda-role`, and ⛔ **"a build
step typing the mandate's spelling would reference a role that does not exist."**

⚠ **ONE STANDING HAZARD, FLAGGED AND OWNED: THE DEPLOY LEDGER IS OPEN** --
`.open_deploys/amgt-h03-leadpanel-y-20260924.json` plus a `change_management` entry at the same pin. **NEVER-2
requires it closed at completion or rolled back.** It is `2.0.0_SA_COO~Y`'s to close, and that lane reports the
hold helper refuses unapplied activation legs. ⭐ **"An open entry outlives the conversation that opened it"** --
so it is recorded here rather than left in an inbox, and it is the first thing to check when 2a closes.

## R-19 -- THE H03 CUTOVER DOES **NOT** FIX THE CHATTER WATER, AND THIS SEAT'S PROOF CLAUSE WAS UNREACHABLE BY THE PRODUCER'S OWN DESIGN

**`2.0.0_SA_COO~Y` preflighted step 2 before building it and refused to proceed** (blocker, evidence
`LEADPANEL_PREFLIGHT.md` @`de0487e9fe`, fresh read 02:53Z). **It is right on every count and this ruling
corrects the mandate, not the seat.**

⛔ **THE FINDING THAT MATTERS: THE GOLD INPUT IS ALSO EMPTY.** Latest gold carries **1,596 rows for SIX
securities -- 1,595 DENIED, 1 PARTIAL.** A **real reviewed reader/producer replay with `write_fn=None`
resolves 0 OF 191 required windows**; both products come back `FAILED` / `INCOMPLETE_GOLD_INPUT`, zero rows,
no pointer. ⭐ **That seat's sentence is the whole ruling: "six gold day-record-bearing names are not six
publication links."**

⛔ **SO THE PREMISE OF STEP 2 IS FALSIFIED. Legacy gives `names_with_links=3 of 250`; GOLD gives 0 of 191
windows. NEITHER SOURCE HAS THE DATA.** The cutover is **NECESSARY AND NOT SUFFICIENT** -- it wires a correct
reader to an input that is itself unpopulated for this universe. ⚠ **AND THIS FALSIFIES WHAT THIS SEAT TOLD
ANDREW:** the proposal called step 2 *"the only step that changes what a user actually sees in the list."*
**It cannot, yet.** The real gap is **upstream of H03: the graded `chatter_daily` gold table is not populated
for the AMGT universe.**

⛔ **AND THIS SEAT'S OWN PROOF CLAUSE WAS UNREACHABLE BY CONSTRUCTION.** The mandate demanded *"`row_count` on
the order of the universe, not 2."* **The producer carries `TOP_N=10`, so `row_count` CAN NEVER EXCEED 10 no
matter how good the input is.** ⭐ **A PROOF CLAUSE THE PRODUCER'S OWN DESIGN CANNOT SATISFY IS A DEFECT IN
THE MANDATE, NOT A FAILURE OF THE BUILD** -- and a seat that had simply obeyed it would have chased an
impossible bar or quietly redefined it. **WITHDRAWN.** Replaced: the proof is about the **INPUT**, measured as
**windows resolved of 191** and **`names_with_links` of 250**, plus `rows_ranked` **against `TOP_N`** -- never
against the universe.

**RE-SCOPED, and step 2 is now TWO items:**
- **2a (buildable now, `2.0.0_SA_COO~Y`):** land the cutover as a **CODE and PACKAGING** improvement -- reader
  wired, the missing **Arrow/naming dependencies** added to the canonical package, the **S3-metadata artifact
  form** adopted (R-17/CVO's durable-artifact reason), and the reviewed safeguards at **`4dc4b667f3`** carried
  onto CLOUD coherently. ⛔ **THIS DOES NOT CLOSE STEP 2's ACCEPTANCE AND MUST NOT BE REPORTED AS CLOSING IT.**
- **2b (NEW, upstream, UNOWNED):** populate the graded `chatter_daily` gold table for the AMGT universe.
  **Until 2b lands, Trending x Chatter cannot show a real ranking from any source.** ⚠ **Surfaced to Andrew as
  a scope item, not silently absorbed into 2a.**

⛔ **AND A NONPUBLISHING CUTOVER IS NOT AUTHORIZED AS A CLOSURE.** That seat asked for *"explicitly
nonpublishing cutover intent"* as one branch. **RULED: 2a is explicitly NONPUBLISHING -- it lands code and
package, it does NOT write a generation or move a pointer, and it claims no acceptance ID.** ⭐ Its refusal to
bypass the hold is correct: *"canonical hold REFUSED unapplied activation leg; no sentinel bypass or
fabricated completion."* **The ledger `amgt-h03-leadpanel-y-20260924` stays OPEN until 2a closes on its own
terms.**

**FOUR MANDATE CORRECTIONS THIS SEAT OWES, all that seat's measurements:**
1. **The role is `amgt-resapp-chatter-axis-lambda-role`**, not `amgt-resapp-chatter-axis-role` as the mandate
   wrote it (corroborated by `3.0.0_SA_CVO~Z`'s baseline ARN).
2. **`DEFAULT_SOURCE` is CLI-ONLY.** The mandate offered *"an env var the function does not carry today"* as a
   route -- **that route does not exist**; the source is a CLI argument, so a Lambda invocation cannot set it
   without a code change.
3. **The canonical package lacks Arrow/naming dependencies** -- a rebuild from HEAD can fail at import, so the
   package change is part of 2a rather than an afterthought.
4. **TF uses local `filename`/`filebase64sha256`**, confirming the no-durable-artifact condition.

⭐ **AND THE SEATING QUESTION THIS SEAT RAISED IS ANSWERED BY THAT SEAT, IN ITS FAVOUR:** *"This Codex instance
remains AMGT; separate Claude IRPT instance is not adopted."* **The AMGT `~Y` and the IRPT `~Y` are DIFFERENT
INSTANCES, so there is NO Rule 27 one-project-per-Tier-2-instance collision.** The flag was worth raising and
is now closed on measurement rather than assumption.

⚠ **A PATTERN AT THIS SEAT, NAMED BECAUSE IT IS NOW THREE FOR THREE TONIGHT: this seat's claims about WHAT
EXISTS have held up, and its claims about WHAT A FIX WILL ACHIEVE have been falsified every time a seat
measured them** -- the shared-fetch premise, the LEG-OUTSTANDING gate, and now step 2's sufficiency. **The
remedy is not more caution in prose; it is preflighting a proof clause against the producer's design before
issuing it, which is exactly what that seat did and this seat did not.**

## R-16 -- THE VENDOR-WORD REGISTER: THREE GRANTS, TWO TERMINALS, TEN MINUTES, AND ONE EXPLICIT EXCLUSION

⛔ **"VENDOR EGRESS APPROVED" HAS NOW BEEN SAID TWICE IN UNDER TEN MINUTES, AT TWO DIFFERENT TERMINALS, ABOUT
TWO DIFFERENT POPULATIONS -- WITH A THIRD BLOOMBERG PULL EXPLICITLY DEFERRED.** That is the exact setup in
which a seat makes an unauthorized call in good faith, believing it is covered. **Enumerated here so no seat
reads one grant as another.**

| # | word | terminal / time | SCOPE -- what it authorizes |
|---|---|---|---|
| **V1** | *"you have egress for whatever calls you want"* | `1.0.0_SA_CTO~Z`, ~02:4xZ (R-15) | the **price pull**, the **Refresh proof to LANDED**, and this seat's **read-only** vendor checks |
| **V2** | *"Vendor egresss approved."* | `4.0.0_SA_CRO~Y`, 02:47Z (`57485eaae8`) | the **60 UNRESOLVED backlog names** the universe carries -- **ONE `reference_data` call each, ONCE**, through `AMGT_RESAPP`'s `add_security` |
| **V3** | the Model tab's Bloomberg figure pull | same word, item 3 | ⛔ **NOT AUTHORIZED. A DESIGN STATEMENT ONLY.** `4.0.0_SA_CRO~Y` states it plainly: *"its per-use word is asked AT THE CUT, not read from item 1."* |

⛔ **V2 AUTHORIZES THE CALLS, NOT A PICK.** `3.0.0_SA_CVO~Z`'s standing ruling on ambiguous names (America
Movil `AXMB`/`AMXB`) is **UNTOUCHED**. ⭐ **A word that permits you to ASK a vendor does not permit you to
DECIDE which of two candidate identities the answer belongs to** -- the first is egress, the second is
adjudication, and they are different authorities that happen to arrive in the same sentence.

⛔ **AND V1 DOES NOT COVER V2's POPULATION, NOR V2 V1's.** Neither is a standing fabric-wide grant. **A
Bloomberg call outside V1 and V2 needs its own word, and V3 is named here precisely because it LOOKS covered
by V2 and is not.** ⚠ This register is additive: a fourth word extends the table; nothing in it widens by
reading.

## R-17 -- LEAD PANEL STEP 3 IS CLIENT-SIDE ONLY. The route already serves what the screen needs

**`3.0.0_SA_CVO~Z` (msg 25178) measured the `dated` gap in the perishable pre-10:00Z window, and the mechanism
is sharper than the proposal's -- which makes the step CHEAPER, not larger.**

**MEASURED ON DEPLOYED BYTES 02:39:48Z:** `trending/chatter` -> HTTP 200 with **`dated: TRUE`**,
`requested_as_of: '2026-09-24'`; `breakout/chatter` -> 200 with `dated: FALSE`; and
`gainers/securities` -> **HTTP 400** *"movement must be one of TRENDING, BREAKOU..."* -- **a real refusal, so
the instrument discriminates rather than answering 200 to everything.**

⭐ **THE ROUTE EMITS BOTH FIELDS AND THE CLIENT TYPE DROPS THEM.** The served payload carries `dated`,
`requested_as_of`, `as_of_date`, `coverage_vintage`, `empty_reason`, `generation_id`,
`generation_row_count`, `payload_hash`, `ranking_reason`, `ranking_status`, `read_attempts`, `resolution`,
`row_count`, `rows_read`, `run_id`, `state`. `types.ts:181` `RankingSet extends Partial<GenerationFields>`;
neither declares `dated` or `requested_as_of`, and a repo-wide search over **986 files** finds no
ranking-payload use of either name.

⛔ **SO THE GAP IS AT THE TYPE BOUNDARY, NOT ON THE WIRE. THE INFORMATION A READER NEEDS IN ORDER NOT TO BE
MISLED BY A FRESH TIMESTAMP IS ALREADY BEING COMPUTED, SERVED AND PAID FOR, AND IS DISCARDED BECAUSE THE
CLIENT NEVER MODELS IT.**

**RULED, and it corrects this seat's own proposal:** step 3 is **CLIENT-SIDE ONLY** -- extend the type and
render. The proposal called it *"two portal-and-adapter changes"*; **no adapter or route change is required.**
⭐ **CONSEQUENCE THAT MATTERS: step 3 therefore does NOT move served output, so it does NOT carry the
never-widen pair, and the 2026-09-29 expiry can be made VISIBLE without touching anything that serves.**
Cheaper, lower-risk, and available before the deadline.

⚠ **THAT SEAT SCOPED ITSELF AND THE LIMIT IS KEPT:** it measured (a) the deployed route emits both fields and
(b) the type declarations at HEAD omit them. It did **NOT** trace the adapter or the panel, so it has **NOT**
shown the panel would render them if the type carried them, nor that the type is the **only** place they are
lost. **ROUTE-PROOF IS NOT RENDER-PROOF and this is not render evidence.** The build seat confirms the render
path; the type fix is necessary and not proven sufficient.
⭐ **One useful adjacency:** `empty_reason` **IS** in `GenerationFields`, so the `189 of 191`
`NO_SIGNAL_IN_WINDOW` reason **CAN** reach the client even though `dated` cannot -- worth holding when the
hour-axis case is graded.

## R-18 -- THE DOSSIER IS AN `AMGT_CORPUS` ADDENDUM, AND THE ADDENDUM IS THIS SEAT'S TO WRITE

**Andrew-direct at the `4.0.0_SA_CRO~Y` terminal 02:47Z, item 2, VERBATIM: *"Rec approved."*** -- the rec being
**dossier as an `AMGT_CORPUS` ADDENDUM, NOT a new `AMGT_DSSIER` project.** ⭐ **No project is registered**; the
earlier relay was explicit that *"any project or addendum that follows is `1.0.0_SA_CTO~Z`'s to register on his
further word"*, and this is that word.

**Item 3, VERBATIM and load-bearing on the fold:** *"I would try to bend the best content pieces into the
AMGT_RESAPP panel/tab structure from the existing corpus, but i wouldnt change AMGT_RESAPP page layout
architecturally ... 'Peers' I think largely stays as it is. 'Model' I think we have to use the model ratio
selections/design from the corpus and try to fill those in via Bloomberg for the figures. 'Posture' is still
up to us."*
⛔ **"I WOULDNT CHANGE AMGT_RESAPP PAGE LAYOUT ARCHITECTURALLY" IS A CONSTRAINT ON THE ADDENDUM, NOT A
PREFERENCE** -- the dossier is **one channel among equals**, not the page's primary shape. ⚠ **And "Peers
largely stays as it is" means the live Peers closer is NOT re-scoped by this** -- `COO~Z` keeps building the
four steps already mandated.
**OWED AT THIS SEAT:** the L4 addendum, once `4.0.0_SA_CRO~Y`'s `--midstream` L1 brief lands (the dossier
artifact plus the per-tab fold contract). Measured beside it: 93 folders -- 46 docx+pdf, 30 pdf-only prose, 6
docx-only, 10 workbook-only, **1 empty**.

## R-15 -- ANDREW GRANTS EGRESS. The §5 refusal is resolved BY HIS WORD, the recorded read is NARROW, and egress authorizes NO OTHER GATE

**Andrew-direct 2026-09-24 ~02:4xZ at the `1.0.0_SA_CTO~Z` terminal, VERBATIM: *"you have egress for whatever
calls you want"*** -- answering `CLOSER_PROPOSE_LEADPANEL_20260924.md` §4(c) and §5.

⭐ **THIS IS THE MECHANISM WORKING, NOT AN EXCEPTION TO IT.** This seat refused `4.0.0_SA_CRO~Z`'s reading
that the price pull needed no vendor word, on the ground that *"availability is not authorization"* and the
question was **AUTHORITY, not magnitude**. The remedy named was his word. **He gave it.** The refusal stands as
correct and is now satisfied -- which is the difference between a gate and an obstacle.

⛔ **THE RECORDED READ IS THE NARROW ONE AND IS STATED AS SUCH.** It authorizes: (i) the **price pull** on the
terminal box, (ii) the **Refresh proof to `LANDED`**, and (iii) this seat's own read-only vendor checks. ⚠ **His
sentence admits a WIDER reading -- "whatever calls you want" is not scoped to those runs -- and TAKING THE WIDER
ONE SILENTLY IS THE EXACT WIDENING CLAUDE.md §2(b) FORBIDS** (*relay, never adjudicate wider OR narrower; if
wider seems plausible, ASK*). **A vendor call outside those three comes back to him.** ⛔ **AND THIS SEAT HAS
ALREADY WIDENED A RELAY ONCE TONIGHT** -- MSTR's push sentence, carried one hop to three Tier-2 seats -- so the
narrow record here is not caution for its own sake, it is the second application of a correction this seat
earned four hours ago.

⛔ **EGRESS IS NOT A DEPLOY AUTHORIZATION, AND THE OTHER GATES ARE UNTOUCHED. A VENDOR WORD ANSWERS *WHO MAY
CALL*, NEVER *WHAT MAY BE SCHEDULED OR SERVED*.** Still required and NOT covered by this grant:
- **The deploy ledger** (`org/critical_paths/change_management/`) for the price producer's **first scheduled
  fire** -- a production schedule, opened before and closed after.
- **The never-widen sign-off pair** (CTO + COO halves) on step 2's deploy, because it **moves served output**.
- **An owner for the terminal box's schedules** -- still unowned; the grant does not name a seat.
- **`.owned-paths.yaml` / contract ownership** -- unchanged.
⭐ **A generous answer to ONE question must not read as an answer to THREE.** Of the proposal's three asks, he
has answered the vendor word; **the browser session endpoint and the terminal-box owner REMAIN OPEN.**

**MEASURED WITH THE GRANT, immediately and read-only:** `bloomberg_health` -> **`ok: true`, endpoint
`127.0.0.1:8194`, service `//blp/refdata`.** That **closes the brief's `bloomberg_session_state UNKNOWN`** for
reachability and de-risks the price pull before any seat runs it.
⚠ **GRAIN, stated: this is a MOMENT, not a PROPERTY.** It proves the refdata service was reachable from this
process at ~02:4xZ. It does **not** prove the session will be up when a scheduled task fires later, that the
puller's own entitlements work, or that `//blp/refdata` covers `PX_LAST` across the whole landed universe. **A
one-time check on a standing condition answers a moment**, and a scheduled producer needs the condition held,
not observed once.

## R-14 -- PEERS CLOSER GO: the peers grant, the hop-4 identity ruling, and a `closer_contract` gap that was open all session

**Andrew-direct 2026-09-24 ~02:2xZ, VERBATIM: *"granted, spawn 2.0.0_SA_COO~Z. Then yes, go."*** answering
`CLOSER_PROPOSE_PEERS_20260924.md`. Three things land, and one instruction is HELD.

**(a) `lib/research/peers/**` -> `2.0.0_SA_COO~Z`, as a CONTRACT ownership row and NOTHING ELSE.**
⭐ **EXERCISED, not inferred:** `resolve_lane("lib/research/peers/engine.py")` -> **`BASE_EXEC`**;
`check_agent("2.0.0_SA_COO~Z", ...)` -> **True**; **negative control** `org/tier0/ledger/x.md` -> lane
`TIER0_MSTR`, **False**, so the instrument can refuse; **sibling control** `scoped_amgt.py` (a row already
relied on) -> identical `BASE_EXEC` / True. ⛔ **AND A NARROW LANE ROW WOULD HAVE BEEN WORSE THAN REDUNDANT:
paths resolve LONGEST-MATCH-FIRST, so a `~Z`-only `lib/research/peers/**` row DISPLACES `lib/**` ->
`BASE_EXEC` and REVOKES base CTO/COO/CVO access to the module.** The grant file itself warns of this at
`:194-196` (*notes that "trained a new lane to ask for a grant it already held"*) and `:200` (*a tilde lane
cannot be given LESS than its base*). **The word "granted" is satisfied by the table row.**

**(b) ⛔ THE SPAWN IS HELD, AND THE HOLD IS THE MEASUREMENT: `2.0.0_SA_COO~Z` IS ALREADY LIVE** -- last seen
14 s before the read, **PID 22020**, *"READY: codex seat bound"*. **Spawning over a live serial is an identity
conflict**, so the instruction's premise is falsified and the act is not performed. ⚠ **AND THE TRAP THAT
NEARLY HID IT: `get_agent_status` returned IRPT logs under that serial, which read as "wrong project".** Per
Rule 22a the **`Latest logs` limb is BASE-scoped** -- those were `~M`'s and `~Y}`'s -- while liveness / PID /
`Working on` are **per-LANE**. **The lane-scoped limb is the one that answers "is this serial live", and it
said yes.** A reader who graded the base-scoped limb would have spawned a duplicate onto a live PID.

**(c) HOP-4 CONTRACT QUESTION, RULED HERE rather than carded** (the brief routed it to this seat because it
changes which names get a set at all): **the ranker KEEPS its identity fall-through; the CROSSWALK widens to
meet it. Converge the route UP to the producer, never trim the producer down.** The fall-through is why 191
keys and **111 real derived sets** exist; deleting it would destroy landed work to make two resolvers agree.
⛔ **REFUSED on the brief's own ground: the route must NOT accept a landed peers object's own identity block
as a third surface** -- it makes ANY pool key resolvable and is the guess the crosswalk's ratified text
forbids. ⭐ **A resolver that trusts the artifact it is resolving has no authority left.**

**(d) ⚠ A GAP THIS SEAT LEFT OPEN SINCE v1.0, found while executing (c): NONE of the three D5 project rows
carried `closer_contract`.** `/closer` requires it *"in the same commit as the contract"*, and
`/canonical-drive` **skips** a row that carries it. **So for this entire session, canonical-drive could have
recut or issued against three projects under a live closer, and nothing would have refused it.** Landed now on
all three (`AMGT_RESAPP`, `AMGT_HARVST`, `AMGT_CORPUS`). **EXPOSURE, NOT INCIDENT** -- no recut is known to
have occurred, and per Rule 22's negative mirror that distinction is not a technicality: the remedy for an
exposure is the guard, and re-opening work nothing touched would be the opposite error.

**NO new contract, no task orders, no rounds:** Peers was already **B04 / P1** inside `CONTRACT.md` v1.0. The
delta is one ownership row, two MANDATEs (`COO_Z_PEERS.md`, `CVO_Z_PEERS.md`), and the three row fields.

## R-13 -- THIS SEAT REPORTED `LEG-OUTSTANDING` AS A FAILED GATE ALL NIGHT, AND THE PROTOCOL FORBIDS EXACTLY THAT

⛔ **EVERY TICK LOG TONIGHT CARRIED THE SENTENCE "THAT GATE IS NOT MET: `origin/CLOUD` unchanged at
`b475b96309`, SITEZ 1,09x ahead / 0 behind" -- AND IT WENT TO ANDREW IN EVERY REPORT.** The `/integrate`
skill @`d7454b855a` (2026-08-27, `0.0.0_AB_MSTR~Z`) says in terms: ⛔ **"`LEG-OUTSTANDING` still means what
it said -- one YES and one NO -- but it is a STATE DESCRIPTION, not a defect, and IT MUST NOT BE REPORTED
AS A FAILURE or drive further legs on its own."**

**ANDREW RETIRED THE FIXED POINT AS A GOAL, VERBATIM (2026-08-27 ~23:2xZ):** *"parity is foundationally
never going to happen unless work is stopped, which is not happening, the gist of it is that i want both
fabrics to be updated with each others work, the big reason for this right now is that i need to run a
/daily-sprint with the full render but i dont want to do it until we have all the info in from sitez."*
**THE OBJECTIVE IS MUTUAL UPDATEDNESS ON A PRACTICAL CADENCE, NOT A FIXED POINT** -- both `is-ancestor`
reads returning YES means the refs are EQUAL, and two live fabrics cannot hold that longer than it takes
someone to commit. The skill also forbids asking a fabric to hold pushes to manufacture a both-YES read.

⭐ **THE PROTOCOL'S OWN INSTRUCTION IS THE ONE THIS SEAT SKIPPED: "ASK WHAT THE INTEGRATION IS FOR, AND
MEASURE THAT INSTEAD. A one-directional need has a one-directional test."** This seat never asked what the
integrate was FOR. It reached for `rev-list --count`, got a real number, and reported the number as a
verdict -- **an unasked-for denominator answering a question nobody had framed.** The 08-27 precedent is
explicit that the satisfying read there was ONE direction alone and the other *"was irrelevant to the need
and would have cost a push-hold to obtain."*

**MEASURED STATE, 2026-09-24 ~01:3xZ, stated as a STATE and not as a grade:**
- **PORTAL REPO: COMPLETE.** branch `DEV`, local `10141b6d` == `origin/DEV` == the parent's gitlink, **0
  dirty paths** -- three reads agreeing, and the gitlink read matters because merging a gitlink never moves
  what it points at.
- **LEG CLOUD -> SITEZ: COMPLETE**, `is-ancestor(origin/CLOUD -> HEAD) = YES`, landed `da77d3365b`
  **00:52:42Z -- AFTER Andrew's ~22:32Z break word**, merging `origin/CLOUD @69e36619ae` (the laptop CTO's
  00:47:10Z commit carrying his own ~00:4xZ *"all recs approved"*, one rec of which was a CLOUD push).
- **LEG SITEZ -> CLOUD: OUTSTANDING**, 1,104 commits, `is-ancestor(HEAD -> origin/CLOUD) = NO` (negative
  control run in both directions). ⚠ **This is the direction that carries THIS fabric's work to the laptop,
  which is the direction his 08-27 word cared about** -- so it is genuinely wanted, and it is **HELD AT BOTH
  MSTRs FOR HIS WORD** by their own report, not stalled. **The merging act is the LAPTOP's** (`laptop leads
  the push, SITEZ merges`), so it is not this fabric's to drive and the device guard keeps it that way.

⛔ **AND A TERMINOLOGY COLLISION WORTH MORE THAN THE STATE IT DESCRIBES: `0.0.0_AB_MSTR~Z` CALLS
CLOUD -> SITEZ THE "FORWARD LEG" (`da77d3365b`, `0e9ed7b1d8`, both) WHILE THIS SEAT HAS BEEN CALLING
SITEZ -> CLOUD FORWARD.** Two seats using *forward* in **opposite senses about one operation**, in commit
subjects that outlive every conversation. **A seat reading "forward leg done" can conclude the wrong
direction landed, and nothing in either sentence looks ambiguous.** ⭐ **RATIFIED: name the direction
explicitly -- `CLOUD -> SITEZ` / `SITEZ -> CLOUD` -- and never `forward` or `reverse`, in any integrate
report, commit subject or log at this seat.** COST: two extra words. NON-APPLICATION: a context where only
one direction exists.

**THE CORRECT REPORT FORM, which this seat owes going forward:** name each leg by direction with its
`is-ancestor` read and the act that satisfied it; say what the integration is FOR when that is known; and
report an outstanding leg as a STATE with its owner, never as a failed gate. **Reporting it as a failure
told the operator his own retired goal was blocking his restart.**

COST: one read of the skill before quoting a gate. NON-APPLICATION: a gate whose definition this seat
authored and holds.

### R-13a -- THE DEFECT PROPAGATED ONE HOP TO THE OPERATOR, AND THE COLLISION WAS TWO SEATS AGAINST ONE

⛔ **A SECOND INSTANCE, VOLUNTEERED BY `3.0.0_SA_CVO~Z` (msg 25150), THAT THIS SEAT COULD NOT HAVE KNOWN
ABOUT: THAT SEAT RESTATED THE DEFECTIVE FRAMING TO ANDREW.** Its status report carried *"Cross-fabric
integrate -- not met; origin/CLOUD at `b475b96309`, SITEZ ~1,100 ahead"* -- **taken from tick 12 and passed
on unchecked.** So the framing did not stop in this seat's logs: **it propagated one hop, to a DIFFERENT
AUDIENCE, through a seat holding no independent basis for it.** A wrong framing in a log is a record
defect; the same framing restated by a peer is a fabric defect.

⭐ **AND THAT SEAT'S OWN SHARPEST POINT IS THE FROZEN COORDINATE, WHICH IS NEW: "the verdict word was
wrong AND the hash beside it was stale, and THE HASH IS WHAT MADE THE SENTENCE LOOK MEASURED. A stale pin
inside a restated claim is WORSE THAN NO PIN: it supplies the APPEARANCE OF GROUNDING to a sentence the
restating seat never grounded."** `b475b96309` was stale **by a whole merge** -- `origin/CLOUD` had moved
to `69e36619ae` and the CLOUD -> SITEZ leg had landed at 00:52Z. Three defects in one restated sentence: a
state reported as a failed gate, a superseded coordinate quoted as current, and **an undifferentiated
"integrate" that HID THAT ONE LEG WAS COMPLETE** -- the half a reader most wants.

⛔ **AND THE COLLISION WAS NOT SYMMETRIC: IT WAS TWO SEATS AGAINST ONE, AND THIS SEAT WAS THE OUTLIER.**
`0.0.0_AB_MSTR~Z` reports (msg 25151) that laptop `0.0.0_AB_MSTR` used the same `forward = CLOUD -> SITEZ`
sense in every frame tonight. ⭐ **SO THREE PARTIES WERE EACH INTERNALLY CONSISTENT AND THE MINORITY HOLDER
GOT NO SIGNAL -- which is the real reason no sentence looked ambiguous.** A private convention does not
feel private; **it feels like the convention.** The remedy is unchanged and is now adopted at all three
seats: name the endpoints.

⭐ **ONE MITIGATION THIS SEAT'S RULING OVERSTATED, and `0.0.0_AB_MSTR~Z` is right to name it:** both
commit subjects carrying *"forward leg"* (`0e9ed7b1d8`, `da77d3365b`) **also name the direction explicitly
in the same line** -- *"merge `origin/CLOUD @<sha>` into SITEZ"* -- so a reader of the subject alone still
gets the direction. **Nothing is rewritten and the hazard was latent rather than realised.** R-13 implied
those subjects were actively misleading; they are not.

⚠ **AND THE VINTAGE RULE DEMONSTRATED ITSELF INSIDE THIS EXCHANGE: that seat measured the outstanding leg
at 1,105 and this seat at 1,104**, because `b2f8ea91a7` landed between the two reads. Neither is wrong.
**Two seats, ten minutes, one commit of difference** -- exactly the drift R-12's vintage clause names, and
the reason an integrate count must never be quoted without its read time.

The outstanding leg is held at both MSTRs for **Andrew's A/B word**; both seats have stated they will not
report it as a blocker again.

## R-12 -- A TEARDOWN'S VERIFY-AFTER IS A **WORKTREE** READ, NEVER A **HISTORY** READ

⚠ **RULED IN A MESSAGE AND A TICK LOG FIRST, WHICH WAS THE WRONG CARRIER.** A log is a journal; a
STANDING OBLIGATION belongs here, by this seat's own reasoning at R-11a -- the reader who needs it is
running a teardown months from now and will not read tonight's inbox. Landed here on `3.0.0_SA_CVO~Z`'s
refinement (msg 25130, `AMGT_RESAPP-Z-S241` @`4eee2d0317`).

**THE HAZARD, measured 2026-09-23:** five untracked `.tf` files declaring **40 resources, every one an
alarm/monitor/watchdog under the standing moratorium**, sat in a plannable position for **three months**.
Two teardowns (`858554332d`, `dd7d2da955`, both 2026-07-17) removed them from **git** and left them on
**disk** -- the file mtimes are 2026-07-10, **predating both teardowns by seven days**, so nothing
resurrected them. **An INCOMPLETE TEARDOWN, not a restore event.**

⛔ **AND IT SURVIVED BECAUSE THE INSTRUMENT THAT CONFIRMS A TEARDOWN COULD NOT SEE WHAT MADE IT
INCOMPLETE.** `git log`, `git show` and a branch census all correctly report the files gone -- gone from
**history**. **TERRAFORM READS THE FILESYSTEM.** So a teardown verified on the history plane passes while
the working tree still declares every resource, and the two planes disagree with nobody looking.

**RATIFIED:** a teardown that removes a `.tf` from git **removes it from the working tree**, and its
**verify-after is a WORKTREE read** -- `ls`, `terraform plan`, or **`git status --porcelain
--untracked-files=all`** -- **never a HISTORY read.**

⭐ **THE WIDER FORM IS `3.0.0_SA_CVO~Z`'s CORRECTION OF THIS SEAT AND IS ADOPTED.** This seat first ruled
*"never a git read"*, which banned the TOOL CLASS when the defect is the PLANE: `git status -uall` **is**
a git read and **reads the working tree**, so it catches this hazard exactly as `ls` does. ⭐ **AND THE
CORRECTED FORM IS CHEAPER, WHICH IS WHY IT MATTERS PRACTICALLY RATHER THAN PEDANTICALLY:** an `ls` needs
to know WHICH directory and verifies ONE teardown, while one `git status -uall` filtered to `*.tf` covers
**every** terraform directory at once **with a printed denominator** -- one command instead of 77, cheap
enough to run on a cadence rather than only after a teardown.

**THE CLASS IS MEASURED AND CLEAN: 477 tracked `.tf` across 77 directories, signature query ZERO** --
and ⭐ **the zero is CONTROLLED, not assumed: a probe was planted, the query returned 1, the probe was
removed.**

⛔ **AND THE PLANE IS PER-WORKING-TREE, WHICH MAKES R-12 WIDER THAN EITHER THIS SEAT OR
`3.0.0_SA_CVO~Z` FIRST WROTE IT: "THE WORKING TREE" IS NOT SINGULAR ON THIS ESTATE.** Rule 14b puts every
worker in its **own linked worktree**, so a verify-after read in the shared tree covers the shared tree
and **nothing else** -- and each of the others is an independently plannable position. Measured by
`0.0.0_AB_MSTR~Z` (msg `20260923T230041Z`): **site Z has 41 worktrees**; 26 carry an
`infra/aws/terraform` directory and every one reads **0** untracked `.tf`; 15 are sparse cones with no
such directory, ⭐ **correctly reported as `NO-TF-DIR` rather than as 0, because a read there is
inconclusive by construction** (terraform cannot be applied from a tree lacking the directory either).
Each row printed its own `rev-parse --show-toplevel`, so no husk read the parent repo. **One false hit
was disclosed and correctly excluded** -- a `' M'` tracked modification at
`infra/aws/terraform/yang-pipeline/etf-classifications.tf`.

⛔ **THE EXCLUSION WAS RIGHT AND THE REASON THIS RULING FIRST GAVE FOR IT WAS WRONG.** This ruling said
it was *"that seat's live work"*. **NO EDIT EXISTS.** `3.0.0_SA_CVO~Z` (`AMGT_RESAPP-Z-S242`
@`63c3dfde02`) measured the working file and `HEAD`'s blob **BYTE-IDENTICAL** -- 2,815 bytes, 82 CRLF
each, raw-identical and not merely normalised-identical -- and touched no terraform file this session.
`.gitattributes` sets `eol=lf` for the path while the committed blob **has carried CRLF since
`39810307ce` (2026-02-19, seven months earlier)**, so the clean filter normalises to LF and compares
against a CRLF blob, which can never match; `update-index --refresh` does not clear it. **14 sibling
worktrees hold the identical bytes and read CLEAN**, because git short-circuits the content comparison
while the index stat matches -- so the mismatch is LATENT in all 15 and visible only where something
touched the mtime. `0.0.0_AB_MSTR~Z` corrected its own report in the same terms: it **attributed a
tracked-file `' M'` to the worktree's holder BY PATH** and dated it from an mtime, one status code away
from its own census text saying an untracked file is attributable by name and content **but never by
path**.

⛔ **AND THAT IMPOSES A LIMIT ON R-12 THAT A READER WILL OTHERWISE OVERRUN: `git status` ON A TRACKED
FILE IS NOT A CONTENT CHECK.** Its verdict follows the **stat cache**, so it can report CLEAN on a file
that differs from its blob and MODIFIED on one byte-identical to it -- **both happened in this single
sweep.** R-12 is sound for the **UNTRACKED** signature it governs, and soundly so by construction: an
untracked file has **no index entry**, hence no stat cache to short-circuit and no clean filter to
disagree with. **Extending R-12 from "detects untracked `.tf`" to "tells me whether tracked terraform
matches git" is NOT ratified and is not true.**

⭐ **THE CLASS IS MEASURED AND IT IS 46, NOT 1** (this seat, `git ls-files --eol`, denominator **41,741
tracked files**, **8,048** carrying an `eol=lf` attribute, **46** of those with a CRLF/mixed blob against
it; discriminating control PASSED -- the instrument finds the file `3.0.0_SA_CVO~Z` measured). **FIVE ARE
`.tf` AND THEY ARE A KNOWN FALSE-POSITIVE SET ON THE VERY SWEEP R-12 MANDATES:**
`terraform/yang-pipeline/etf-classifications.tf`, `terraform/nfra-agentbus-alyssa01/{main,iam}.tf`,
`terraform/seeking-alpha/main.tf`, `lambda/ec2-auto-shutdown-enforcer/main.tf`. **Each will read MODIFIED
in any worktree where something touches its mtime, with no edit behind it** -- so a seat running R-12's
verify-after should expect them and chase nothing. The remedy is re-committing each with LF so the blob
matches its own attribute (pure line-ending normalisation, no semantic change); that is a content commit
under `infra/aws/`, routed and NOT done here.

⚠ **AND THIS SEAT'S OWN CENSUS NEARLY PUBLISHED A ZERO FROM A BROKEN PARSE.** The first pass reported
**0 files carrying `eol=lf`** -- against `3.0.0_SA_CVO~Z`'s direct measurement that one does -- because
`git ls-files --eol` renders the field as `attr/text eol=lf` **with a space**, and an `\S*` capture
truncated it, dropping **8,050 of 41,741 rows (19%) into an "unparsed" bucket that silently HELD THE
ENTIRE POPULATION.** ⛔ **A POSITIVE CONTROL WAS RUN AND IT PASSED ON THE WRONG AXIS:** it confirmed the
corpus contains CRLF blobs (744) and **never tested the attribute parse**, which was the half that was
broken. **The contradiction with a peer's measurement is what caught it, not the control.** ⭐ **THE
CONTROL MUST EXERCISE THE CLAIM'S OWN JOIN -- here, a file KNOWN to satisfy BOTH halves** -- and the
corrected run carries exactly that. COST: one named positive per census. NON-APPLICATION: a
single-predicate census, where any positive exercises the whole join.

⭐ **46 IS CORROBORATED ON AN INDEPENDENTLY-WRITTEN INSTRUMENT AND IS A TOTAL, NOT A FLOOR.**
`3.0.0_SA_CVO~Z` re-derived it by `git cat-file --batch` over every HEAD-tree blob then `check-attr` over
only the CRLF-bearing paths -- **a different method, same 46** (41 `.py`, 5 `.tf`). ⛔ **AND IT NAMED THE
SHARED DEPENDENCY BOTH PASSES RESTED ON rather than letting two agreeing numbers read as settled: both
trusted `eol=lf` as the only attribute shape producing the mismatch, so a `text=auto` path with no
explicit `eol` would have been INVISIBLE TO BOTH.** Measured here and it is **ZERO**: of **851**
CRLF-bearing blobs, **805 carry NO text attribute at all** and **46 carry `text eol=lf`**; the widened
signature (any text-normalisation, not just explicit `eol=lf`) returns **the same 46**, and
`core.autocrlf=false` means the 805 are stored as authored with no clean filter to disagree -- **not
exposed, and correctly so.** Rule 22's shared-dependency clause, run rather than noted.

⚠ **EVERY DENOMINATOR IN THIS RULING CARRIES A VINTAGE AND IS ONLY TRUE AT IT: 41,741 tracked / 851
CRLF-bearing / 46, read 2026-09-24 ~00:5xZ around `0e7cfdd669`.** ⛔ **A CENSUS OF A LIVE REPO IS A
PERISHABLE FIGURE AND NEITHER THIS SEAT NOR `3.0.0_SA_CVO~Z` STATED ONE AT FIRST.** That seat's own two
passes, an hour apart, read **41,741 / 3,147** then **41,851 / 3,151** -- four files that look like a
discrepancy and are simply other seats committing, this one included. **Only the JOIN held still (46 and
851 both stable across both runs), which is the reason the conclusion survives and the intermediates must
not be quoted bare.** COST: one pin per census sentence. NON-APPLICATION: a census of a frozen ref.

⚠ **THE TWO PASSES AGREE AT 46 AND THEIR INTERMEDIATE DENOMINATORS DO NOT -- 851 here versus 3,147 there
-- AND BOTH ARE RIGHT ABOUT DIFFERENT POPULATIONS.** ⭐ **RECONCILED EXACTLY BY `3.0.0_SA_CVO~Z` rather
than left as an explanation: splitting ITS raw set by THIS instrument's classification gives 2,300 in the
`-text` bucket and **851** on the text plane -- **2,300 + 851 = 3,151**, this seat's number reproduced to
the unit.** `ls-files --eol` **CLASSIFIES** (and buckets 2,497
paths as `-text`, excluding them); `cat-file` **COUNTS RAW BYTES** across all 41,739 blobs including
binaries that contain a CR-LF sequence incidentally. **The join agrees because the `eol=lf` set is small
and unambiguous; the intermediates are not the same measurement and must not be quoted as though one
confirms the other.**

⭐ **AND THE ROOT `.gitattributes` ALREADY NAMES THIS EXACT HAZARD AT `:3`** -- *"without an eol rule a
CRLF checkout makes terraform files read as MODIFIED against an LF index"* -- with `*.tf text eol=lf` at
`:10`. **So the RULE is in place and correct; the 46 are blobs committed with CRLF before or despite it.**
That makes the remedy precisely a re-commit under the rule that already governs them, and it means this
class is closed-going-forward and open only as a backlog of stragglers.

⭐ **THREE SEATS MISJUDGED THE CARDINALITY OF THIS SAME PLANE INSIDE ONE HOUR, EACH IN A DIFFERENT
DIRECTION** -- `0.0.0_AB_MSTR~Z` and this seat read "the working tree" as one when site Z has 41;
`3.0.0_SA_CVO~Z` inferred "every worktree" from the blob mechanism and measured 1 of 15, correcting
itself before reporting; and this seat's class census read 1 file as 0 and then as 46. **The plane was
right every time and its COUNT was assumed every time.**

**COVERAGE IS NOW COMPLETE AND NO NAMED POPULATION REMAINS OPEN** (closed @`00:35Z`, laptop
`0.0.0_AB_MSTR`'s own instrument via `0.0.0_AB_MSTR~Z`, agentbus `7d6a11d2`): **shared trees 0 and 0;
site Z 26 of 26 worktrees carrying the directory read 0** (15 without it, `NO-TF-DIR`); **laptop 12 of 12
carrying it read 0** (2 without it, same treatment). Per-worktree denominators printed throughout.

⭐ **AND THE REMAINDER CLOSED *BECAUSE* THIS RULING NAMED IT.** The prior line said the laptop's 14 worker
worktrees were unswept and would be swept **after the reverse merge**; naming them as the open population
got them swept within minutes instead. **A NAMED REMAINDER IS ACTIONABLE; A SCOPE ADJECTIVE IS NOT** --
*"site-Z only"* gives no reader anything to close, while *"the laptop's 14 worker worktrees"* names an act
and an owner. That is the practical case for preferring the named remainder, and it was demonstrated here
rather than argued.

⛔ **THIS RULING SHIPPED THE SENTENCE "site-Z only, the laptop is not measured" WHEN THE LAPTOP ANSWER HAD
BEEN IN THIS SEAT'S OWN INBOX FOR ~90 MINUTES.** `3.0.0_SA_CVO~Z` wrote that limit truthfully -- it did
not hold the laptop message -- and **this seat, the only seat holding BOTH halves, RESTATED the peer's
limit instead of closing it.** ⭐ **A PEER'S SCOPE LIMIT IS A CLAIM ABOUT *THEIR* COVERAGE, NEVER A CLAIM
ABOUT THE POPULATION** -- and it arrives already sounding careful, which is exactly why it gets carried
forward unexamined. **Before restating an inherited limit, check it against your OWN holdings; the seat
that can falsify it is usually the one relaying it.** COST: one inbox read against one sentence.
NON-APPLICATION: a limit on an instrument only the peer can run.

⛔ **ONE CONSEQUENCE FOR ANY FUTURE AUDIT OF THE FIX ITSELF, and it is the same blindness one level on:
the five were UNTRACKED, so deleting them produced NO COMMIT AND LEFT NO GIT RECORD. THE DELETION IS
UNATTRIBUTABLE FROM GIT BY CONSTRUCTION** -- evidenced only by the actor's report plus a filesystem read.
⭐ **So THE SURPRISE ROW IS THE AUDIT RECORD HERE, not a supplement to one.** Confirmed by a seat that
did not perform the deletion, which is the only confirmation worth having on one.

**COST:** one worktree read per teardown, or one repo-wide one on a cadence. **NON-APPLICATION:** a
teardown executed in a fresh clone or ephemeral worktree, where no working tree survives the act.

## R-11a -- A STANDING LIMIT ON EVERY FUTURE ADJUDICATION ON THIS SURFACE

⛔ **AN IP IS NOT AN IDENTITY, AND PER-FIRM ATTRIBUTION IS UNAVAILABLE FROM ANY INSTRUMENT IN THIS
ESTATE.** Measured: the firm header is injected by `auth-validator-edge` **DOWNSTREAM of the access
log**; API Gateway access logging is **NOT declared**; and the Lambda log carries only START/END/REPORT
plus error lines, **with no route and no firm on a successful request.**

**RATIFIED: an incident on this surface can have its ROUTE and its CLIENT IP reconstructed and NEVER its
FIRM. No seat promises firm attribution in a future adjudication.** Recorded here rather than left in a
message, because the seat that needs it is the one writing a blast radius months from now.

## R-11b -- ONE CALL AT ANDREW (was two; the second was never his), NOT URGENT

1. **NOTIFICATION.** Four responses over ~25 hours to one client. `3.0.0_SA_CVO~Z` recommends **no
   re-processing of the eleven untouched securities** and states the notification question **turns on
   who the client was, which it cannot determine and will not guess.** ⛔ **This seat does not guess
   either, and does not decide it: it is outward-facing and reputational.**
2. ⛔ **WINDOW -- WITHDRAWN AS A CALL. IT WAS NEVER ANDREW'S, AND CARDING IT WAS THIS SEAT'S
   OVER-RESERVATION.** Closed by `3.0.0_SA_CVO~Z` (msg 25125, record @`8e5612576b`) by MEASURING it.

   > ~~The census covers 09-19 to cutover ONLY ... pre-09-19 requests are NOT measured -- and ARE
   > measurable, the logs running to 2026-09-03. Widening is one re-run of the same method.~~

   ⭐ **THAT SEAT'S REASONING IS THE CORRECTION AND IT IS ACCEPTED WITHOUT RESERVATION:** *"one turns on
   who the client was and is genuinely his. The other was a QUESTION, NOT A DECISION -- it needed no
   authority, cost one read-only census, and carding it would have handed him a choice where a fact was
   available for the asking."*

   ⛔ **THIS IS THE OVER-RESERVATION DEFECT `/self-drive` NAMES BY NAME, COMMITTED BY THE SEAT RUNNING
   `/self-drive`.** Andrew's own words, which this seat had quoted back to him hours earlier: *"somehow
   every single open call falls under 'reserved' versus adjudicable which needs to be assessed better
   because it renders the skill useless if it cant get calls adjudicated."* ⭐ **THE TEST THIS SEAT
   FAILED TO APPLY: does closing this need AUTHORITY, or does it need WORK? Authority is reserved. Work
   is not a call.** A question whose answer is one read-only census is never a sovereign decision, and
   dressing it as one spends the operator's attention on something a tool could answer.
   **COST: none -- it removes a card.** **NON-APPLICATION: a measurement that is itself an outward-facing
   act, or one whose instrument needs a grant.**

   **THE MEASUREMENT: 2026-09-03 to 09-18, 2,222 hourly files, positive control 52,242 rows parsed. 82
   `/api/scoped/amgt*` requests, 21 thesis/overlay served, and ZERO IN-CORPUS.** A response for a
   security with no drafted sections cannot serve a no-span sentence, so **realised exposure over the
   complete measurable history is EXACTLY the five responses already reported.**

   ⭐ **AND IT IS EXHAUSTIVE RATHER THAN MERELY WIDER, which is the part worth keeping: the CloudFront
   logs begin 2026-09-03, which PREDATES the Lambda's earliest artifact version at 2026-09-15 across 30
   versions. THE LOG HISTORY PRECEDES THE FUNCTION'S OWN DEPLOYABLE HISTORY, so there is no earlier
   period in which this surface could have served anything at all.** The window cannot be widened
   further, and widening it to its limit changed the answer by zero. **"We looked further and found
   nothing" and "there is nowhere further to look" are different claims, and this is the second.**

   **Recommendation against re-processing the eleven untouched securities is STRENGTHENED: over the full
   history, eleven of the twelve were never served even once.**

⚠ **NOT URGENT AND DELIBERATELY NOT ESCALATED MID-BREAK:** the guard is deployed and the exposure is
closed forward. These are retrospective questions. **The incident CLOSES when the remediation act is
done and recorded -- the measurement is not the act.**

⚠ **LIMITS CARRIED, not softened:** response bodies were not captured, so "could carry no-span prose" is
inferred from corpus membership TODAY and the per-response count is an **UPPER BOUND, not a reading.**

## PARKED -- OFF THE AMGT THREAD, NAMED SO NOTHING DRIFTS (`/closer` NO SIDE-QUESTS)

**Two `opal_ai` items now sit at this seat and NEITHER is being worked while AMGT is armed.** Recorded
with owner and un-park condition, because an un-parked item is the one that gets lost.

| item | owner | un-park condition |
|---|---|---|
| **opal_ai L1 brief RCN-0014** @`2c4a813784`, delivered by `4.0.0_SA_CRO~X` (msg 25011) as intake for this seat's L2 | `1.0.0_SA_CTO~Z` | AMGT stands down, or Andrew re-scopes |
| **opal_ai GitOps split spec** -- Andrew-direct ~22:0xZ at the `4.0.0_SA_CRO~X` terminal, record @`bd282e03e9`: *"figure out what needs to happen to properly split this off in GitOps from ajb_workspace ... same structure as the portal where it is contained in the monolith, but it has its own git submodule"*. That seat writes the spec; this seat is its intake | `4.0.0_SA_CRO~X` writes it; `1.0.0_SA_CTO~Z` receives it | the spec lands AND AMGT stands down or is re-scoped |

⛔ **HIS WORD WENT TO `4.0.0_SA_CRO~X`, NOT TO THIS SEAT, AND IS NOT READ AS RE-TASKING IT.** CLAUDE.md:
a word to one agent is never converted into a gate or a re-tasking of another -- **relay, never adjudicate
wider or narrower.** It commissions a SPEC from that seat. The AMGT scope armed at
`a8a62f4f5c` stands until Andrew says otherwise, and `/self-drive` §6 makes the armed scope the only work
this fabric does. ⭐ **The temptation to read a nearby Andrew-direct as a scope change is exactly what the
verbatim-scope rule exists to stop** -- and the GitOps spec is interesting enough to be a real pull.

⚠ **ONE THING WORTH FLAGGING NOW rather than at intake, because it bears on a hazard already measured
tonight:** a portal-shaped submodule inherits the portal's properties, and two of those bit this evening
-- **a commit inside a gitlink can land on a DETACHED HEAD with every gate green** (surprise row
`AMGT_RESAPP-Z-S237`), and **`.owned-paths.yaml` rows for a submodule path bind by READING ONLY because no
hook evaluates a commit made inside it** (CONTRACT §3, upheld by `3.0.0_SA_CVO~Z`). **A second submodule
doubles both.** Not an objection to the design -- an input the spec should answer rather than discover.

## R-10 -- ANDREW SUSPENDS THE L4-R SIGNATURE AS A BAR FOR AMGT. THE REVIEW IS KEPT; THE RITUAL IS NOT

**Andrew-direct 2026-09-23 ~21:2xZ at this terminal, VERBATIM: *"agreed with your rec"*,** answering this
seat's recommendation in these words: *"keep the reviewing and drop the ritual"* -- specifically, **KEEP**
`3.0.0_SA_CVO~Z` grading pinned candidates plus the never-widen pair and cutover review, and **SUSPEND**
the L4-R PRD half-signature **as a bar** while AMGT runs under closer mandates.

**THE MEASURED BASIS, which is why this is not merely tidying.** The L4-R half-signature feeds
`to-pipeline-gate` LIMB 6, which refuses a **NEWLY-ADDED TASK ORDER** against a PRD with an unsigned
half. ⛔ **CLOSER MODE CUTS NO TASK ORDERS** (`/closer`: *"No task orders, no rounds, no recuts for
in-scope fixes"*), and Andrew's word to `2.0.0_SA_COO~Z` was *"We are moving off of the canonical flow
for this project."* **So the door LIMB 6 guards is one nobody walks through, and two signature cycles
were spent tonight on a lock with no traffic behind it.**

⛔ **WHAT IS SUSPENDED IS NARROW AND THE SCOPE MATTERS MORE THAN THE SUSPENSION.** SUSPENDED: the
half-signature as a **BAR on progress** for AMGT PRDs under closer mode. **NOT SUSPENDED, and none of
this is touched:** `3.0.0_SA_CVO~Z`'s REVIEW of ratified text and the binding force of its findings on
this seat · its grading of every pinned candidate · **the never-widen pair on any served-output write**
· the cutover review · every deploy gate. **No tool, gate or hook is edited. Nothing is removed from the
repo.** This is a ruling about what this seat treats as a blocker, not a change to a mechanism.

⭐ **AND THE EVIDENCE MOVED AGAINST THIS SEAT'S OWN REC BETWEEN PROPOSING IT AND EXECUTING IT, WHICH IS
RECORDED RATHER THAN QUIETLY DROPPED.** The rec was sent at ~21:1xZ. `3.0.0_SA_CVO~Z`'s R8 (msg 25069)
arrived at 21:17Z and **caught a live self-contradiction in the ratified text this seat had just
written** -- amendment 4 asserted both that the 221-file census IS the denominator and that 221 *"appears
in no denominator here"*, so a worker quoting the stale bullet would have carried a RETRACTED FIGURE into
the build as ratified text. **That catch came OUT OF the cycle being suspended.**

⛔ **SO THE HALVES ARE NOT INTERCHANGEABLE AND THE DISTINCTION IS THE WHOLE RULING: THE REVIEW FINDS
DEFECTS; THE SIGNATURE GATES A DOOR NOBODY USES.** Suspending the review to save the ceremony would have
traded a working control for a dead one. **R8's defect is fixed in amendment 4's next hash REGARDLESS of
the suspension, because a self-contradicting spec is a defect whether or not anything gates it** --
un-gating text does not license shipping text that contradicts itself.

⚠ **NON-APPLICATION, stated so this is not read wider than it is:** any project NOT under a closer
mandate; any PRD from which task orders ARE cut; and the laptop fabric, which this ruling does not reach.
**REVERSION: the moment AMGT cuts a task order from a PRD, LIMB 6 has traffic again and the bar is back
without a further ruling.** COST: none -- it removes a step. `3.0.0_SA_CVO~Z` may pitch against the scope
of this ruling as a governance fork.

## R-9 -- R-7's LOAN IS TERMINATED. THE PEERS AGREED FIRST, SO THIS RATIFIES RATHER THAN RULES

**`2.0.0_SA_COO~Z` IS ACTIVE.** Andrew authorized it directly in its own conversation, recorded at
`568f2f0c88:org/tier1_exec/2.0.0_SA_COO/deliverables/AMGT_EXPERIENCE/AUTHORITY.md` (pin verified here
against a negative control). His words, verbatim: *"Yes there is no need to be held up here. We are
moving off of the canonical flow for this project because we need to move faster."* and *"You have
explicit insturction from CTO on your brief and expectations, you should have received documents that
qualify this in great detail"*.

⭐ **THAT SEAT'S OWN RECORD NARROWS IT CORRECTLY AND THIS SEAT ADDS NOTHING:** *"A review signature is
evidence-bound and is not deployment, retained-object rewrite, vendor-egress or gate-bypass
authorization."* **The session restriction is resolved. The DEPLOY GATES ARE NOT TOUCHED.** Anyone
reading the activation as deploy authorization is reading it wider than both the operator and the
authorized seat did.

**RULED: R-7's Price loan TERMINATES on that activation. `lib/research/price/**` returns to SERVED
RUNTIME at `2.0.0_SA_COO~Z`.** R-7's bound 2 said *"reverts on activation ... this is a loan"*, and it
does.

⭐ **AND BOTH LANES REACHED THE HANDBACK BEFORE THIS RULING EXISTED, INDEPENDENTLY.** `2.0.0_SA_COO~Z`:
*"R7 activation returns price ownership to this seat; coordinating Y handback before edits"* and
*"activation does not justify concurrent writers."* **So this entry RATIFIES a peer agreement rather
than imposing a decision, which is the lighter and correct act** -- `/closer` sends a breaking change to
the CTO only after one exchange between the peers, and here the exchange converged. **A CTO that rules
where its peers already agree adds a step and subtracts nothing.**

**THE HANDBACK, stated once so neither lane has to guess, and covering BOTH branches because which one
holds is not measured here:**
- **NO CONCURRENT WRITERS.** `2.0.0_SA_COO~Y` does not begin new Price edits; `2.0.0_SA_COO~Z` does not
  edit that surface until the handback lands.
- **IF `~Y` APPLIED the migration under R-7:** it finishes to a PIN and hands that pin over. The work is
  not abandoned and is not re-derived.
- **IF `~Y` HAD NOT STARTED:** `~Z` applies the pinned proposal `~Y` already designed and tested -- nine
  compute cases passing in memory -- rather than authoring a second design.
- ⛔ **EITHER WAY THE NINE FAILURES' FIX SURVIVES THE OWNERSHIP CHANGE.** A surface transfer that loses
  the tested work would be worse than the stop R-7 was written to clear.
- ⚠ **`~Y`'s candidate base predates the merged `0e9ed7b1d8`** (996 CLOUD commits). Carried forward
  before integration, by whichever lane integrates.

**WHAT IS NOW UNBLOCKED AND WHAT IS NOT.** The never-widen PAIR is completable for the first time today:
this seat's half is signed (`97d9e537d4`, pin-bound `83e9f90be5`, rollback corrected `3b4083a685` after
`2.0.0_SA_COO~Z` found it restored the known incident), and that seat reports its half and an
independent `dd91fd3126` exact-package review UNDERWAY. ⛔ **The pair is still not the deploy:**
`3.0.0_SA_CVO~Z`'s cutover review comes after it and that seat has stated the review is IN ADDITION to
the pair and never in place of it. **Three controls, in order, none skipped.**

---

**What these rulings do NOT do.** R-1 through R-6 landed no CONTRACT; **R-7, R-8 and R-9 postdate it** --
CONTRACT v1.0 and three MANDATES are issued at `0e33cea24b`. **R-7 REASSIGNS ONE NAMED SURFACE** and
no other; `~X`, `~Y` and `~Z` otherwise hold what they held. No task order, no spawn, no cap widening,
no deploy, no vendor call, no entitlement change, and no lift of any seat's session restriction.
