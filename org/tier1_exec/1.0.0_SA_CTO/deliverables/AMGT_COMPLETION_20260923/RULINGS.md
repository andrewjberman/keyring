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
