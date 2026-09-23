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

**What these rulings do NOT do.** No CONTRACT is landed (R-1/R-2 are its inputs, and the CONTRACT with its
`.owned-paths.yaml` grants and the `closer_contract` rows is a separate one-commit act). No MANDATE is
issued. No task order, no spawn, no cap widening, no deploy, no grant, no vendor call. No seat is
reassigned: `~X`, `~Y` and `~Z` hold what they held.
