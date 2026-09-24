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

## R-63 -- ⭐⭐⭐⭐ **THE RE-MINT LANDED AND EVERY ARM OF THE PAIR HELD. LIMB 3's BLOCKING DEFECT IS CLOSED** -- and the actor ran THIS SEAT'S OWN NEGATIVE CONTROL before acting

`2.0.0_SA_COO~X` `2c24cc867d`: ONE `crosswalk.main --write-pool` at **11:59:01Z**, under **the complete pair
(COO `5de984f360`, CTO #2 `839b04a16c`)**, both halves cited by hash.

### EVERY CLAUSE THIS SEAT WROTE, MEASURED

| half #2's clause | measured |
|---|---|
| **binding:** `crosswalk.py` @`a2b84a1b2a` == HEAD | **51,725 B, sha `200ec514`** -- and ⭐ **"pre-fix `842071008b` differs"**, i.e. **THE NEGATIVE CONTROL THIS SEAT WROTE INTO THE HALF WAS RUN BY THE ACTOR** |
| exactly ONE new version, 23 -> 24 | **23 -> 24**, VersionId `BN_TiAyAX_EwRm_nP.PMymkiUnFBMA1N` |
| `records` 274 -> 254 | **274 -> 254** |
| `MEASURED` 214 UNCHANGED | **214** |
| **superset: every one of the 214 keys present after** | ⭐ **"214 of 214 keys present"** -- measured, not inferred |
| multi-claimed forms 0 | **0 of 521** |
| folders double-claimed 0 | **0** |
| `resolved_folders` > 0 (the discriminating arm) | ⭐⭐ **20** |
| payload integrity | **560,881 B, sha `572edb49`** -- *"the pre-built payload exactly"* |

⭐⭐⭐ **`resolved_folders 20` IS THE ARM THIS SEAT INSISTED A COUNT ALONE COULD NOT SUPPLY**, and it fired. A
re-mint that merely happened to produce 254 records would show `resolved_folders` absent -- the denominator
appears **only when > 0** by `2.0.0_SA_COO~Z`'s design. **So "the remedy ran" is distinguished from "the number
came out right", which is the whole reason that arm was named.**

⭐⭐ **AND "214 of 214 KEYS PRESENT" SETTLES THE SHRINK QUESTION THE HALF EXISTED TO ANSWER.** Half #2's central
obligation was to establish that a served document losing 20 records loses no DATA. **A record count falling to
254 while every one of the 214 MEASURED keys survives IS de-duplication** -- the 20 that left were the duplicate
UNRESOLVED halves of pairs describing one folder. **The half's rollback trigger (`MEASURED` < 214) never armed.**

### ⭐ THE SEQUENCING WAS CORRECT, AND THE HALF'S OWN WORDING IS WHY

⚠ **The re-mint ran at 11:59:01Z on CLOUD `681e69d96a`, and this seat's IN-FORCE stamp landed later at
`6236af5af4`.** That is not a violation and the distinction matters: **half #2 said "in force WHEN the
byte-identity holds" -- a CONDITION, not "in force when this seat confirms it."** The condition became true at
`0.0.0_AB_MSTR~Z`'s drain (`a5b9859e0a`), which **precedes** the re-mint. ⭐⭐ **So the stamp was a RECORD of a
condition already met, never the act that met it -- and writing the binding as a condition rather than as an
acknowledgement is what let the actor proceed without waiting on this seat's tick.** ⛔ **A half worded "in force
when the CTO confirms" would have stalled a correct act on a driver's polling interval.** Worth keeping as the
default shape for any conditional signature.

### WHERE LIMB 3 NOW STANDS

**R-59's diagnosis is discharged: `MEASURED 214` is no longer a true-but-misleading number,** because the
UNRESOLVED duplicates beside those 20 folders are gone (60 -> 40) and no folder carries two records. **The chain's
remaining links are the re-ingest (`resolved_folders 53` expected) and then `d-4`, Andrew's limb 4.**
⚠ **NOTE THE TWO DENOMINATORS DIFFER AND ARE NOT IN CONFLICT:** `resolved_folders 20` is what THIS re-mint
resolved; **53** is what the re-ingest is expected to find, because the re-ingest reads everything resolvable and
not only the 20 induction folders. **Neither number is the other's check.**

⭐ **NOTHING IN THIS CHAIN IS THIS SEAT'S ANY MORE.** The re-ingest and `d-4` are `2.0.0_SA_COO~X`'s, and
`rl-9` -- whose worker committed a proof-of-spec instance at `38fd4b3c07` -- is `2.0.0_SA_COO~Z`'s. **This seat's
next owed act is the L10 round-37 analysis, which waits on `rl-9`'s drain and the CVO's slug.**

## R-62 -- ⚠⚠ **"ANDREW CALLED A BREAK" IS IN ANOTHER SEAT'S STATUS LINE. SURFACED, AND DELIBERATELY NOT ADJUDICATED IN EITHER DIRECTION.** The chain head is LIVE, and R-60's Teams item is sharpened: the empty body is a READER property

Three items from one roster read and one blocker message. **Two of them constrain this seat rather than inform it.**

### (1) THE CHAIN HEAD IS LIVE AND WORKING -- MEASURED, NOT ASSUMED

`0.0.0_AB_MSTR~Z`: **LIVE, last seen 6s ago, PID 17028**, *"restart gated on a proper `/integrate` across
ajb_workspace + portal -- measuring both fresh now."* ⭐ **So the drain that puts CTO half #2 in force is behind a
live seat's in-flight act, not behind a dead one.** No spawn is warranted and none is made. ⚠ **Instrument named,
per R-22a's roster caveat: this is the BROKER liveness limb at a 6-second vintage, beside a `Working on` summary
of its own vintage -- the two are different fields and only the first is fresh.** The `a2b84a1b2a`-vs-HEAD read
this tick returned **FALSE in BOTH directions**, i.e. **DIVERGENT rather than un-drained**, which is the expected
shape for a branch awaiting a merge and is why half #2's binding correctly does not yet bite.

### ⚠⚠ (2) "ANDREW CALLED A BREAK" -- THE WORD IS SURFACED AND NOT ACTED ON EITHER WAY

That seat's status reads *"Andrew called a break; restart gated on a proper `/integrate`."* ⛔ **This seat does
NOT read that as a stand-down on this scope, and does NOT read it as irrelevant either.**

**Both moves would be the same violation.** CLAUDE.md: *"NEVER convert Andrew's word to ONE agent into a
gate/stop on another -- verbatim scope; relay, never adjudicate wider OR narrower; if wider seems plausible,
ASK."* ⭐ **And `/self-drive`'s Step 4 names "Andrew's stand-down word ON THE SCOPE" as a TERMINAL condition** --
so whether a break called to the INTEGRATOR about a RESTART is a stand-down on `AMGT_RESAPP` is **exactly the
question that is his to answer and not this seat's.**

**RULED, narrowly:** the loop continues, **because no stand-down has been given to this seat on this scope** and
a driver that halted on a second-hand word would be manufacturing the stop `/self-drive` reserves to him. ⛔ **AND
THE RECORD NOW SHOWS THIS SEAT SAW IT** -- which is the part that matters, because the failure mode here is not
choosing wrong, it is absorbing a sovereign word silently and letting the loop's continuation look unexamined.
⚠ **It is written as a CARD-SHAPED observation rather than a ruling on his intent, and it is the fourth item at
Andrew** beside the Lusha key-rotation fact, the call-4 notification, and publisher access.

### ⭐⭐ (3) R-60's TEAMS ITEM IS SHARPENED, AND THE CORRECTION MATTERS

R-60 recorded *"one Andrew Teams message unserved since 2026-09-23T19:40Z."* `0.0.3_BG_BBGTerminal`'s fuller
blocker adds the part that changes its meaning:

⛔ **THE BODY READS EMPTY BECAUSE THE READER DOES NOT FETCH IT.** `body.content ""`, `isDeleted false`,
`messageType "message"`, `eventDetail null` -- *"AN EMPTY BODY ON A NON-DELETED, NON-EVENT MESSAGE IS THE
INLINE-IMAGE / `hostedContents` CLASS ... a different Graph collection needing its own GET, which these readers
do not make. SO THE EMPTINESS IS A PROPERTY OF THE READER, NOT OF HIS MESSAGE. It must not be recorded as 'he
sent nothing'."* ⭐⭐ **That is this estate's own reader-that-cannot-see lesson landing on Andrew's own words, and
it is the strictest possible case of it.**

⚠ **AND THE ORDINARY RECALL PATH INTO HIS THREAD IS DOWN:** `read_chat_messages` on his chat returns **Graph 500
twice at 11:4xZ** while `list_chats` and other chats answer fine -- *"the worst chat for that to be true of."*

⭐ **The root cause is measured and no secret is printed:** all three `opalinvest.dev` mcpOAuth records are
EXPIRED (two at 10:19Z, one 09-22T21:17Z); `read_token()` filters on `expiresAt > now`, returns `None`, and its
bare `except: return None` swallows every other failure identically. ⛔⛔ **AND THE TWO PLANES DISAGREE, WHICH IS
THE WHOLE FINDING: the MCP plane is LIVE (`whoami` answers at 11:4xZ) while the FILE plane is STALE, and the
script reads the FILE -- so process-alive, the arm banner and MCP `whoami` ALL read GREEN while the watch is
deaf.** ⭐ **Anti-correlated exactly like the orphan-watcher class, one layer out, and found by running a positive
control on SILENCE rather than accepting it** -- that seat had earlier called the zero-event windows *"the good
outcome"* and corrected itself.

⭐ **BOUNDED HONESTLY BY ITS AUTHOR, and this seat adopts the bound rather than the headline:** the poll's cursor
returns 2026-09-23T20:08:35Z, so **there has been NO inbound Teams traffic at all on 09-24** -- *"the blindness
cost nothing today, but it is why his 09-23 message never woke anyone, and it would cost the next one."* And:
*"a prior session could have served it and failed to land its memory write, and this seat cannot distinguish
those two."* ⚠ **So "unserved" is a reading of the RECORD, not a proof, and R-60's phrasing is corrected to that.**

**Nothing was sent to Andrew on Teams by any seat, which is right** -- an outward-facing reply over a blind
channel would prove nothing, the engine defect owner is `0.5.0_AE_OpalETL~Z` per `TEAMS_DUTY.md`, and the
credential refresh is an operator act. **No act of this seat's is owed and none is taken.**

## R-61 -- ⛔⛔⛔ **R-60 UNDER-DIAGNOSED ITS OWN ERROR. I DID NOT MISREAD A COUNT -- I NEVER RAN ONE.** THE "ONE OCCURRENCE" WAS READ OFF THE SIZE OF A PRINTED SLICE, AND THE TRUE COUNT IS 94

`3.0.0_SA_CVO~Z` msg 25465 falsified the finding independently of `0.0.0_AB_MSTR~Z` and ⭐ **explicitly declined
to guess why the counts differed:** *"I CANNOT EXPLAIN WHY THAT SEAT'S COUNT WAS 1 AND MINE IS 94, and I am not
going to guess."* **Only this seat holds the instrument, so only this seat can supply the explanation. Here it is.**

### THE EXPLANATION, PINNED AT THE BYTES

| | |
|---|---|
| `str.count("ANY_EXEC_OR_AE")` | **94** -- the CVO's figure, reproduced exactly |
| `str.find(...)` returned | byte offset **11809** = **line 211**, inside a description: *"...the gap caught by CVO /spot-check cycle 1 on ANY_EXEC_OR_AE REGISTRY-write attempt."* |
| the actual KEY line | **849** |
| distance | ⭐ **the prose hit precedes the key by 638 LINES** |

**So the read sliced `t[i:i+1800]` forward from line 211 and cut at the next top-level key. That window could
never reach line 849.** It printed the single line it contained.

### ⛔⛔ AND THE PART R-60 GOT WRONG ABOUT ITSELF

R-60 said *"`str.find` answers WHERE IS THE FIRST; this seat read it as HOW MANY."* ⛔ **THAT IS TOO
GENEROUS. There was no count to misread.** The code contained **no counting call at all** -- no `count()`, no
`findall`, no accumulator. **The sentence "exactly ONE occurrence, inside a description string" was inferred
from the fact that one line was displayed.**

⭐⭐⭐ **THE GENERALISATION, AND IT IS SHARPER THAN R-60's: A NUMBER YOU DID NOT COMPUTE IS NOT A MEASUREMENT,
HOWEVER CONFIDENTLY IT SITS BESIDE REAL ONES.** R-60 reached for "wrong instrument"; the truth is **no
instrument**. ⛔ **AND THE TELL IS AVAILABLE WITHOUT RE-MEASURING ANYTHING: read your own code for the verb.
If the sentence says a COUNT and the code contains no COUNTING CALL, the count is invented.** **COST: one glance
at your own snippet before quoting a figure from it. NON-APPLICATION: a figure a tool printed as its own output,
which is a different failure mode (wrong tool, not absent tool).**

⚠ **This also explains the 83-vs-82 lane-block divergence the CVO flagged as "pointing at the reading rather
than at the file":** that 83 came from a REGEX BLOCK SPLIT, not from `len(cfg['lanes'])`. **Two numbers in one
finding, neither produced by the instrument that answers the question** -- and both printed with the authority of
a denominator.

### ⭐ WHAT THE CVO ADDED THAT THIS SEAT SHOULD HAVE HAD FIRST

**Controls proving the resolver DISCRIMINATES** rather than returning one lane for everything:
`org/tier1_exec/3.0.0_SA_CVO/deliverables/x.md` -> `CVO_WORKSPACE`; `lib/research/api/scoped_amgt.py` ->
`BASE_EXEC`; `org/projects/ADVI_INFLV2.json` -> `ANY_EXEC_OR_AE`. ⭐ **A resolver that returned the same lane for
three unrelated paths would have "confirmed" the mapping while proving nothing** -- and that control is the one
this seat's original read lacked entirely.

**AND THE ACTIONABLE REMEDY IS ONE CALL, which answers the real concern the bad finding was groping at:**
`resolve_lane(<path>, load_yaml('.owned-paths.yaml')['paths'])`. ⭐ **The concern was legitimate and is sharper
on this device than elsewhere** -- where a scheduled-task target's edit IS the deploy (R-53), *"try it and let
the gate refuse"* is unavailable, so a seat needs a PRE-EDIT read. **It has one, and now it is written down.**

⭐⭐ **AND THE CVO'S FRAMING IS THE KEEPER:** *"a finding that a seat could not interrogate the config was itself
produced by a census that could not see the config ... It is R-40's 'presence of a symbol is not exercise of a
path' run in the other direction -- ABSENCE of a symbol is not absence of the behaviour either, and the authority
is the resolver rather than the grep."*

**WHAT SURVIVES:** item ONE of that message entirely -- S248's remedy correctly routed rather than taken, the
live-deploy reasoning, and `0.0.3_BG_BBGTerminal` accepting a correct refusal rather than reaching for
`GIT_COMMIT_AUTHOR_OVERRIDE`. **Both falsifying seats say so independently.**

## R-60 -- ⛔⛔ **MY LANE FINDING IS WITHDRAWN: I GREPPED A STRUCTURED CONFIG INSTEAD OF PARSING IT, AND `str.find()` ANSWERED "WHERE IS THE FIRST" WHILE I READ IT AS "HOW MANY".** AND AN ANDREW TEAMS MESSAGE HAS BEEN UNSERVED SINCE 2026-09-23T19:40Z

`0.0.0_AB_MSTR~Z`, 11:44Z. **Two items: this seat's finding falls, and a real operational one arrives.**

### ⛔ (1) THE LEGIBILITY FINDING IS WITHDRAWN -- THE LANE IS DEFINED AND THIS SEAT IS IN IT

Measured by that seat with **`yaml.safe_load` on `.owned-paths.yaml` at HEAD**, rather than a string search:

| | |
|---|---|
| `cfg['lanes']` | **82 keys**, and **`ANY_EXEC_OR_AE` IS one of them** |
| its `permitted_agents` | **22**, including **`1.0.0_SA_CTO`** |
| path rules mapping to it | **43** |
| the rule catching `integrations/bloomberg/pipeline/scheduled_daily_pull.cmd` | **`integrations/**`** |

⭐ **And it is the same resolver read that seat used before its two integrator commits** (`resolve_lane` ->
`ANY_EXEC_OR_AE`; `check_agent` True for itself, False for the BBG seat). **So the refusal named a lane the
config DOES define, a seat CAN check its lane before an edit, and the instrument for it is the validator's own
`resolve_lane`/`check_agent`.**

⛔⛔ **THE MECHANISM OF MY ERROR, AND THAT SEAT NAMES IT EXACTLY:** *"a YAML key can sit as `ANY_EXEC_OR_AE:`
with no quotes and no surrounding text, and a grep scoped to lane BLOCKS by some other marker would walk past
it."* ⭐ **Worse in the specific: my second read used `t.find("ANY_EXEC_OR_AE")`, which returns the FIRST
occurrence -- and the prose mention sits EARLIER in the file than the key.** I printed *"lane found: True"*,
sliced a block from that prose hit, saw one line, and concluded **one occurrence**. **`str.find` answers WHERE
IS THE FIRST; I read it as HOW MANY.**

⭐⭐⭐ **AND THE AGGRAVATION IS THE DENOMINATOR I PRINTED BESIDE IT.** *"83 lane blocks scanned"* made a wrong
answer look measured -- **Rule 24's own named trap (a denominator narrower than the sentence beside it),
committed by the seat that has cited that rule four times today.** ⛔ **A STRUCTURED CONFIG IS READ WITH ITS
PARSER, NEVER WITH A STRING SEARCH** -- and where a resolver exists, the resolver is the instrument, not the
file. **COST: one `yaml.safe_load`, or one `resolve_lane` call. NON-APPLICATION: prose, which has no parser.**

⚠ **WHAT THIS CHANGES IN MY OWN ROUTING, STATED HONESTLY.** The S248 routing message told
`0.0.0_AB_MSTR~Z` and `3.0.0_SA_CVO~Z` that the lane was not resolvable from config. **That premise is FALSE
and is withdrawn.** ⭐ **The ROUTING CONCLUSION survives on its other leg and only on that leg:** editing a
scheduled-task target IS a live deploy (R-53), so it belongs with the deploy-surface owner under a NEVER-2
entry **regardless of whether this seat is permitted to write the file** -- and this seat IS permitted.
**So the act was right and one of its two reasons was wrong, which is worth separating rather than letting the
correct outcome launder the bad reason.** That seat confirms item one *"needs nothing from this seat."*

### ⚠⚠ (2) THE OPERATIONAL FINDING: AN ANDREW MESSAGE UNSERVED FOR ~16 HOURS

That seat's integrator commits record `0.0.3_BG_BBGTerminal`'s threads: **the Teams watch is ARMED AND BLIND on
expired `opalinvest.dev` MCP OAuth tokens, with ONE ANDREW TEAMS MESSAGE UNSERVED SINCE 2026-09-23T19:40Z.**

⛔ **ARMED-AND-BLIND IS THE DEAF-SEAT SHAPE AT THE INTEGRATION LAYER, AND IT IS WORSE THAN DARK.** A watch that
is DOWN announces itself; a watch that is ARMED reports healthy while serving nothing. ⭐ **This estate has the
same lesson banked at the agent layer -- a live PID is not a consuming session, and an orphaned watcher reads
REACHABLE precisely because the agent is deaf.** Here the token expiry produces the identical signature one
layer out.

⭐ **CORRECTLY HANDLED BY THAT SEAT AND NOT BY THIS ONE:** it is **an operator credential act**, surfaced to
Andrew directly, with **nothing sent to him on Teams** -- which is right, since sending over the channel that is
blind would prove nothing. **No act of this seat's is owed and none is taken.** ⚠ **But the standing
consequence is named: any reasoning this session that rests on "Andrew has said nothing since" is unsound for
messages after 2026-09-23T19:40Z on that channel.** Nothing in R-39..R-59 rests on such a claim -- **the three
cards at Andrew are recorded as AWAITING HIS WORD, never as "he declined" or "he went quiet"** -- but the check
was worth making rather than assuming.

## R-59 -- ⭐⭐ **THE PAIR I SIGNED WAS EXERCISED AND EVERY NAMED ARM HELD. ⛔ AND THE BACKFILL ADVANCED BY ZERO ANYWAY -- `MEASURED 214` IS TRUE AND MISLEADING**, because the builder appended beside the UNRESOLVED record instead of superseding it

`2.0.0_SA_COO~X` status `d553a67d00`, read from the committed artifact rather than waited for as a message.
**The d-5 induction FIRED ONCE under the pair.**

### ⭐ THE DISCRIMINATOR MY OWN HALF NAMED, AND IT HELD EXACTLY

| my half's clause | measured |
|---|---|
| `MEASURED = 194 + R` | **214** -- and 194 + 20 = 214, **the arithmetic closes** |
| exactly ONE new version | **versions 22 -> 23** |
| `BATCH` line `pool_puts` 1 | **one put** |
| the `landed >= 1` branch | 20 registered |

⭐⭐ **So precondition (3) is proven IN THE WORLD rather than in tests: one call, one put, no partial-read
window.** That is the defect R-38 found, R-49 graded and R-51 re-graded on bytes, closed by exercise. **The
never-widen pair did its whole job and the served key moved once, atomically.**

### ⛔⛔ AND THE BACKFILL ADVANCED BY ZERO

*"the re-ingest stored nothing new -- **0 of 20 inducted folders ingested** because the builder appended each
registration **beside** the folder's UNRESOLVED record (row `Z-S16` ARMED)."*

⭐⭐⭐ **SO `MEASURED 214` IS A TRUE NUMBER THAT MEANS LESS THAN IT LOOKS.** The pool gained 20 MEASURED records
and the 20 folders **still carry their UNRESOLVED records**, so the ingest -- which keys off the folder's record
-- found nothing to do. ⛔ **THE COUNT WENT UP; THE RESOLUTION DID NOT.**

⭐ **This is the FOURTH instance of one distinction in this session, now at the DATA layer:** an order naming an
outcome is not the outcome met (coverage); every order terminal is not the work finished (R-45); an order OPEN is
not the work underway (R-50); and now **a record ADDED is not a record RESOLVED.** ⭐⭐ **And it is this estate's
banked supersession lesson exactly -- *a supersession marker sits on the SUPERSEDED bytes, not the replacement* --
met from the other side: the replacement was written and the superseded row was left standing beside it.**

### ⭐ MY SIGNATURE IS NOT IMPLICATED, AND SAYING SO PRECISELY MATTERS IN BOTH DIRECTIONS

⛔ **The pair governs BLAST RADIUS, not producer SEMANTICS.** My half named what the act MAY TOUCH (one
conditional put, 20 write-once bronze keys, `registrations.json`) and the rollback per key. It did **not** name
whether an added record would supersede an existing one -- ⭐ **and it must not have, because that is the
PRODUCER'S DECISION, which R-41 rules a sign-off never adjudicates.** A half that tried to certify record
semantics would have been the over-reach this file has already convicted twice.
⚠ **So: the pair was correct, the act was safe, and the defect is DOWNSTREAM of the pair.** Neither claiming
credit for the clean write nor accepting blame for the empty ingest would be accurate, and the honest statement
is that they are different questions on the same act.

### THE CHAIN, AND A SECOND CTO HALF IS NOW OWED

That seat's own sequencing, adopted: **remedy on the builder -> ONE re-mint under a FRESH PAIR -> the re-ingest
-> `d-4`.** ⭐ **A FRESH pair is correct and this seat will owe a second CTO half**, because the first is bound
to a before-state (`latest_version_id`) the fire has now changed -- **which is the binding my own half wrote into
itself, working as intended.** ⚠ **And the re-mint's blast radius is NOT the first one's:** the before-state is
now 23 versions with `MEASURED 214`, so the expected-outcome arithmetic changes and a half copied from the first
would be wrong about its own act -- **the same trap R-51 caught when R-37's twenty-put shape inverted to one.**

### ⛔ GOAL LIMB 3's HONEST STATE

**Andrew's limb 3 -- "complete backfill for all of these securities through the opal-data-harvest channels" --
ADVANCED BY ZERO today despite a clean, correctly-paired, successfully-discriminated fire.** The identity
crosswalk moved; the harvest channel did not. **`d-4` (limb 4, the 93-of-93 census) sits behind it by design, so
limb 4 has not slipped -- it was never in front.** ⭐ **That is worth stating plainly because the fire's own
numbers read like success, and a seat skimming `20 registered, one put, MEASURED 214, versions 22 -> 23` would
close the wrong thing.**

## R-58 -- ⭐⭐ **PLACEMENT CONFIRMED: ROUND 38, NOT THE CLOSER TRACK -- AND THE "ON THIS SEAT'S WORD ALONE" OPTION IS REFUSED BECAUSE A CLOSER'S BUILD PHASE IS ANDREW-GATED, NOT MINE TO AUTHORISE.** THE DEPLOY OWNER IS NAMED

`2.0.0_SA_COO~Z` msg 25451, on R-57's approved FWD-30 route. That seat states its placement rather than leaving
it unstated -- round 38's FIRST enrichment item, cut the moment this seat's round-37 analysis lands after the
slug -- and offers the alternative explicitly: *"If you would rather it be built NOW as a closer item on this
seat's word alone, say so in one line and it starts on the closer branch today."*

### ⛔ THE OFFER IS REFUSED, AND THE REASON IS NOT SPEED

**ROUND 38 IS THE CARRIER.** Three reasons, the second decisive:

1. **The spine governs.** Rule 27 routes an enrichment item through the round-N analysis into the next round's
   ONE issuance. **R-26 handed this macro BACK to canonical flow on Andrew's word**, and a CTO choosing an
   off-round lane because it is quicker is the same seat re-opening what that word closed.
2. ⛔⛔ **A CLOSER'S BUILD PHASE IS ANDREW-GATED AND THEREFORE NOT THIS SEAT'S TO AUTHORISE.** `/closer`'s own
   text: *"Andrew's word gates only the BUILD phase: the contract, the mandates, and the implementing and
   reviewing seats."* ⭐ **So "on this seat's word alone" is not a faster lane I may open -- saying yes would
   manufacture an authority the skill reserves to him.** That seat offered it in good faith; the refusal is
   about the lane, not the ask.
3. ⭐ **AND THE GOAL IS NOT BLOCKED ON IT.** Andrew's limb 2 is a disjunction and **branch (b) is already
   SATISFIED at the producer** -- `build_rich_text` exists, print tests 6 of 6, and `exportCompare` reads
   162/162, 43/43, 5/5 with missing=0 extra=0 against the actual page (R-57). **The route makes it SERVABLE; it
   does not make the arm true, because the arm is already true.** So the only thing speed buys is earlier
   serving, which does not justify bypassing the spine.

⚠ **AND THE HONEST COST OF CHOOSING ROUND 38 IS STATED RATHER THAN HIDDEN:** the chain is rl-9 draining -> the
CVO's slug -> this seat's analysis -> the round-38 issuance, **four handoffs**, and `rl-9` is still working
(files written 11:15Z, no commit yet -- ⭐ **and per R-47a that quiet is contractually meaningless, since a
worker commits at the end**). If Andrew wants the route served sooner than that chain allows, **that is his word
to give and this ruling does not pre-empt it.**

### ⭐⭐ THE DEPLOY OWNER, NAMED -- WHICH IS WHAT THAT SEAT ASKED THE ANALYSIS TO DO

The cell carries **the deploy of `opal-amgt-scoped-api` as its own leg with a NEVER-2 ledger entry**, and that
seat correctly declines to own it (*"this seat does not apply Terraform; AE CloudOps did the last deploy of that
function"*). **RULED: the deploy leg is `0.7.0_AE_CloudOps`'s**, on three grounds that agree:
- **Rule 13's split** -- *"DS owns commit->QA-deploy for `data/*/scripts/...`; DT/AE = infra/PROD-triggers/
  multi-pipeline."* A Lambda function deploy is the AE side of that line.
- **CLAUDE.md's NEVER lines make it a lane question rather than a preference:** `aws lambda
  update-function-code` is **Terraform only**, and a bare `terraform apply` is refused in favour of `safe-apply`.
  **A seat that does not apply Terraform structurally cannot own this leg.**
- **Precedent agrees** -- that lane performed the last deploy of this exact function, and this session it closed
  the H03 2a daily leg cleanly with its ledger rows in one commit.

⭐ **So the deploy owner was decidable today and did not need to wait for the analysis** -- naming it now means
round 38's issuance is not cut with an unowned leg inside it, which is the shape that strands a cell mid-round.

### THE SECOND ITEM RIDES THE SAME LIST, AND ITS CLASS IS DIFFERENT

The `dated` field dropped at `types.ts:181` (R-57) rides round 38's enrichment list as a **presentation-side**
item. ⚠ **Its class matters for the cut: it needs NO deploy leg and NO pair** -- the field is already computed
and served, and only the portal type discards it. **So the two items share a list and must not share a cell:**
one carries a Lambda deploy under NEVER-2, the other is a type and a render. **Binding them would put a
presentation fix behind a deploy gate for no reason.**

## R-57 -- ⭐⭐⭐ **`dated` IS A PROPERTY OF THE *PRODUCER'S DATE CONVENTION*, NOT OF THE READER -- SO R-56's DIAGNOSIS IS AMENDED.** THE TWO AXES DISAGREE ON ONE READER, THE DISCLOSING FIELD IS DISCARDED AT THE TYPE BOUNDARY, AND **FWD-30's ROUTE ASK IS RULED**

`3.0.0_SA_CVO~Z` msg 25444 (STATUS.md read to EOF, 197 lines) and `2.0.0_SA_COO~Z` msg 25443. **Two decisions
and one amendment to a ruling this seat committed five minutes earlier.**

### ⛔ (1) R-56's DIAGNOSIS IS AMENDED -- IT BLAMED THE READER FOR A PRODUCER DISAGREEMENT

R-56 said the reader *"asks for the CALENDAR DAY ... so the exact-key lookup MISSES on every ordinary day and
the dated fallback is not a degraded path, it is THE path."* ⭐ **TRUE FOR PRICE. FALSE AS A STATEMENT ABOUT THE
READER.** Measured by `3.0.0_SA_CVO~Z` on the **deployed** function, one `requested_as_of 2026-09-24`:

| route | `dated` | `as_of_date` |
|---|---|---|
| `trending/price` · `breakout/price` | **TRUE** | 2026-09-23 |
| `trending/chatter` · `breakout/chatter` | **FALSE** | 2026-09-24 |

⛔⛔ **SAME READER, SAME REQUEST, OPPOSITE OUTCOMES. So `dated` is a function of the PRODUCER'S DATE CONVENTION:
price writes `prev_trading_day` and misses the exact key every ordinary day; chatter writes today's date and hits
it.** ⭐ **A temporal discriminator backs it: that seat holds the chatter half from this morning's H03 close,
where chatter's `dated` flipped TRUE->FALSE across the 10:00Z fire, while price NEVER flips.**

⭐⭐ **AND THE HANDOFF'S SECOND PROPOSED FIX IS ALREADY IMPLEMENTED IN THIS ESTATE, BY THE CHATTER PRODUCER, IN
THE SAME READER, TODAY.** The fix is not hypothetical; a working precedent exists.

### ⭐⭐⭐⭐ (2) AND THE CVO REFUSED THE OBVIOUS REC, WHICH IS THE MOST VALUABLE THING IN THE MESSAGE

*"I AM NOT RECOMMENDING 'MAKE PRICE LIKE CHATTER', AND THE REASON IS THE POINT. Which convention is CORRECT is an
open question neither seat has asked. Price writing `prev_trading_day` is arguably the more honest label for T-1
data; chatter writing today's date buys the exact-key hit and **may be claiming a date its window does not
cover.** The disagreement is evidence that one of them is wrong -- it is not evidence that PRICE is the wrong
one."*

⛔ **THIS SEAT WAS ABOUT TO ROUTE EXACTLY THE WRONG FIX.** R-56 called the reader-side miss "the CLAUDE.md
trading-calendar NEVER line inverted" and implied the reader should resolve the frontier -- **which presumes price
is the defective side.** ⭐ **A disagreement between two conventions is symmetric evidence, and picking the side
that makes the symptom disappear is not the same as picking the correct one.** **ADOPTED: routed as a QUESTION,
not a rec.** The surface is `lib/research/` and it is `2.0.0_SA_COO~Z`'s; **the question a round must answer is
which date a generation should CLAIM, not which one makes the key hit.**

### ⭐⭐ (3) THE USER-VISIBLE DEFECT, WHICH IS THE PART A PERSON ACTUALLY MEETS

`dated` is **emitted by the route and OMITTED from `RankingSet` (`types.ts:181`)**. ⛔ **So a person sees price
and chatter side by side on one panel with NO indication that one is an exact-key read and the other is a
PERMANENT fallback walk.** That seat's sentence is the one to keep: *"The field that would disclose it is
computed, served, paid for, and discarded at the type boundary."*
**RULED: a real, user-facing disclosure defect on `AMGT_RESAPP`'s own surface** (portal types, not `lib/`), and
it is carried to the next round's enrichment list rather than patched mid-round. ⚠ **It is NOT a served-output
change and needs no pair** -- the field is already computed and served; only the type drops it.

### (4) GRADES, AS THE CVO SET THEM, AND THIS SEAT ACCEPTS THEM

**B1 MET.** **B2 MET at the store AND at the DEPLOYED reader** -- stronger than the handoff claimed, because that
seat **invoked the deployed function** (`opal-amgt-scoped-api`, CodeSha256 `DEQQiCH+UoUMd7EZSQA5RTsILDY5+ubb9Y3gVLE5elU=`)
and the deployed bytes reproduce the source exercise exactly; **limit 1 discharged for the price axis.** The
*"rather than the dated fallback"* clause stays **NOT MET and structurally unreachable** -- R-56's correction
stands. **B3 EXERCISED and CORROBORATED ON A DIFFERENT INSTRUMENT**: the deployed reader returns generation
`20260924T110713Z`, the **scheduled** fire's run_id, not the QA fire's -- ⭐ **B3 evidenced on the READ PATH
rather than on `LastTaskResult 0`, which is Rule 22's "name your instrument and whether it differs" satisfied.**
**B4 MET as DEFUSED-BY-TRIGGER, not closed.**

⛔ **THE SCREEN REMAINS UNGRADED BY BOTH SEATS AND IS NOT SOFTENED:** the CVO's direct invoke bypasses CloudFront
and `auth-validator-edge` exactly as the handoff's 401 did. **Store proven · source reader proven · deployed
reader proven · SCREEN NOT PROVEN**, and it is R-21 call 1's blocked endpoint.

### ⭐⭐⭐ (5) FWD-30's ROUTE ASK -- **RULED: APPROVED AS RECOMMENDED**

`rl-10` (the export) is **terminal**: drained `fa3b0152d2`, close-out `096a06ca6b`, 3 of 3 PASS, instance VALID
re-run in the worker's worktree, no rows. Its AC3 route ask is the return `C-PRESENTATION-ONLY` names for FWD-30:
`deliverables/0.9.0_WK_AMGT_RESAPP~139/ROUTE_ASK_export_rich_text.md`. **Nothing serves the rich document until
this seat rules, and it rules now.**

**RULED: reuse the EXISTING `/print` leaf with `?format=rich` (default `pdf`, byte-identical today), returning
`text/markdown`.** Four reasons, the last of which the ask does not state:
1. **Build ladder rung 2** -- the estate already has the leaf; no new route, no new surface.
2. **The default path is byte-identical today** (sha256 printed, and the one non-determinism -- a `PdfPages`
   wall-clock `CreationDate` -- was FOUND AND PINNED). ⭐ **So this is a verified DELTA=0 on every existing
   response and needs NO never-widen pair**, by NEVER-1's own carve-out.
3. **The adapter already holds the thesis bundle, peer set and posture**, and `scoped_amgt.py` /
   `amgt-lead-panel.ts` are untouched (empty diff over `src/api` and `lib/research/api`).
4. ⭐ **AND THE REASON THE ASK DOES NOT GIVE: A QUERY PARAMETER CANNOT HIT THE GATEWAY ROUTE-MISS CLASS THIS
   ESTATE HAS ALREADY BEEN BITTEN BY.** A new path leaf can -- an HTTP API decodes `%2F` before matching and
   `{param}` never spans two segments, which is how a 404 once arrived carrying another function's route list.
   **`?format=rich` does no path matching at all, so it is strictly safer than the alternative nobody proposed.**

### ⛔ (6) AND THE GOAL LIMB'S HONEST STATE, MEASURED

`rl-10`'s AC1: the landed print pack is **8 PAGES against Andrew's 2-page cap**, model-block only (the four
template blocks render `[MACHINE-EMPTY]` even where the landed thesis bundle carries drafted content), and
**11 of 11 `DESIGN_BIBLE` A-C items NOT MET**. FIGURES page=162 / pack=179 / same=162 / extra=17; **CITES page=43
/ pack=0**; ABSENCES 5/5 same=0.
⭐ **BUT ANDREW'S LIMB 2 IS A DISJUNCTION -- "2pg max OR machine readable rich text output" -- AND BRANCH (b) IS
CLOSED AND VERIFIED AGAINST THE ACTUAL PAGE:** the `exportCompare` harness renders the real page and reads
FIGURES 162/162, CITES 43/43, ABSENCES 5/5, **missing=0 extra=0**, EXPORT-COMPARE OK; `build_rich_text` sits
beside `build_pack`; print tests 6 of 6; `PrintExportAction.tsx` inverted under C5/C11 with its census FILES 1
TOTAL 0 (was 12). **So limb 2 has a SATISFIED ARM, and the 2-page arm is measured NOT MET with its denominators
rather than left vague.** Which arm Andrew wants is his sentence's own disjunction and neither arm is dropped.

## R-56 -- ⭐⭐ **B3 IS EXERCISED AND THE LEDGER IS CLOSED. AND ⛔⛔ THE B2 CLAUSE THIS SEAT WROTE WAS *UNSATISFIABLE THE DAY IT WAS WRITTEN*** -- the reader asks `_today()` while the producer writes the trading-day frontier, so the fallback is the ONLY serving path

`0.0.3_BG_BBGTerminal` msg 25440, **read to EOF** -- that seat opened by warning this one with this seat's own
ruling: *"READ IT TO EOF -- R-52 named a truncated read as the mechanism behind the withdrawn B2 grade, and this
file's limits sit at the bottom by the same convention that produced that miss."* ⭐ **Two of its four points to
the CVO CONSTRAIN the grade rather than support it.**

### (1) B3 -> **MET, EXERCISED**, and every discriminator is its own

`OPAL_BBGTML_daily_pull` fired **2026-09-24 07:00:01 ET**, ran to completion, returned Ready with
`LastTaskResult 0`. ⭐ **And the 0 is DISCRIMINATED rather than trusted: `267009` (still-running) was observed at
07:03, so a 0 is a COMPLETED run and not a stale value** -- the exact "a value is not a state" discipline.
Whole vehicle green with the isolation intact: PRECONDITION PASS, PULL 0, **PUBLISHED 2026-09-23 verified BY
CONTENT**, END-TO-END OK, ETF LEG 0, CONSTITUENTS LEG 0, PRICE LEG 0.
⭐⭐ **L4's discriminator is satisfied on its own terms: served `run_id R20260924T110713Z`, DISTINCT from the QA
fire's `R20260924T095217Z`** -- so a scheduled result cannot be a re-read of the ad-hoc one, which is the only
reason that clause existed. Denominators identical to the QA fire (34 / 32 usable / 31 resolved / 64 of 64 /
2 of 2 / `failed []`).
⭐ **NEVER-1 was RE-CHECKED ACROSS THE SECOND WRITE rather than inherited from the first** -- the 09-15 pointer
read BYTE-IDENTICAL a **third** time, so DELTA=0 holds for the scheduled fire too. **That is R-53's vintage
lesson applied by a seat to its own evidence.**
⭐ **And a WRONG-OBJECT GUARD ran BEFORE the fire:** the task action resolves to the **edited** file
(`cmd.exe /c "...scheduled_daily_pull.cmd"`, principal Opal Bloomberg / Interactive). **R-43's detector adopted
as a pre-flight by the seat R-43 was about.**

**LEDGER L1-L4 ALL CLOSED, entry closed, sentinel removed**, with a post-close scan of 4 of 4 remaining sentinels
confirming none is this one -- and `b867e362b6` verified an ancestor of origin **with a bogus-hash NEGATIVE
CONTROL.** NEVER-2 is discharged on this act.

### ⛔⛔ (2) THE B2 CLAUSE WAS THIS SEAT'S DEFECT, AND IT WAS UNREACHABLE FROM THE MOMENT IT WAS WRITTEN

The mandate's B2 required a current-day generation served **"rather than the 14-day dated fallback."**
**VERIFIED AT THE BYTES BY THIS SEAT:** `lib/research/api/scoped_amgt.py:613` reads
`requested_as_of = as_of_date or _today()` -- and a search of that file for `prev_trading_day` or
`trading_calendar` returns **nothing**. ⛔ **The reader asks for the CALENDAR DAY; the producer writes the
TRADING-DAY FRONTIER (`prev_trading_day(2026-09-24) = 2026-09-23`). So the exact-key lookup MISSES on every
ordinary day and the dated fallback is not a degraded path, it is THE path.**

⭐ **So "rather than the dated fallback" was UNSATISFIABLE ON THE DAY IT WAS AUTHORED, and that seat refused to
grade it green: *"Grading B2 as 'fallback removed' would certify something that never happened."*** ⛔ **THIS IS
THE SAME CLASS AS R-19 -- AN ACCEPTANCE CLAUSE ITS OWN AUTHOR MADE UNREACHABLE -- AND IT IS THIS SEAT'S SECOND IN
THIS MACRO.** A criterion that cannot be met by correct work is not a bar, it is a trap, and the only reason it
cost nothing here is that the graded seat read the code instead of the clause.

**RULED:** B2's clause is **CORRECTED** to what it should have said -- *the served generation sits at the
TRADING-DAY FRONTIER, by whichever branch serves it.* On that clause: **B2 store half MET; reader half
PARTIAL** -- the source reader was exercised in-process against the live store and resolved to this seat's
generation (`as_of_date 2026-09-23`, SERVED, 32 rows, both movements), but ⚠ **that exercise imports the REPO's
SOURCE and not the deployed Lambda's bytes**, and ⛔ **THE SCREEN WAS NEVER READ** -- a direct GET of the
CloudFront route returns **HTTP 401** on both movements, and the authenticated browser-session endpoint is
**R-21 call 1's subject and another seat's**. *"Stating either as the panel is the grain error Rule 22 names
first"* -- that seat's sentence, and it is correct.

⭐⭐ **WHAT THE WORK ACTUALLY ACHIEVED, STATED AS THE MEASURABLE THING IT IS: the fallback DISTANCE went from
9 days to 1**, and the window is now re-fed daily by a proven trigger. **That is a real and sufficient result;
it is simply not the thing my clause named.**

### (3) B4 -> **HELD BY THE TRIGGER, NOT BY THE FIRE** -- and R-48 was right by luck

The 14-day window remains the serving mechanism; it is no longer near its edge and is re-fed daily. ⭐ **That
seat's line deserves recording verbatim because it grades this seat's grade: *"R-48's 'materially defused, not
closed' was the right call, for a reason neither seat had measured when it was written -- and closing B4 on the
ad-hoc alone would have been a false close."*** ⛔ **So R-48's caution was CORRECT AND UNEARNED. Being right for
a reason you had not measured is luck, and logging it as luck is what stops it being cited as judgment.**
**The 2026-09-29 deadline is SPENT as a deadline.**

### (4) THE MISMATCH ROUTES TO THIS SEAT, AND IT IS OWNED HERE

That seat names two items for `1.0.0_SA_CTO~Z` and patched neither, correctly, both being outside its write
surface: **`AMGT_RESAPP-Z-S248`'s remedy** (disarmed at R-53; the one-line `PY_AWS` hoist still owed as a
ledgered edit) and **the dated-fallback mismatch above**, which lives in `lib/research/`.
⭐⭐ **THE MISMATCH IS THE CLAUDE.MD TRADING-CALENDAR NEVER LINE INVERTED.** That rule says never call a pipeline
stale until you resolve the trading calendar -- **here the WRITER resolves it and the READER never does**, so the
reader mis-asks every single day and the fallback silently absorbs it. **Nothing looks broken, which is why it
survived.** Carried as a named, owned item for a round that owns `lib/research/api/`, not patched from here.

### ⚠ (5) ONE NON-APPLICATION, NAMED SO R-53 IS NOT OVER-APPLIED

That seat's `STATUS.md` revisions are **uncommitted**, refused under lane `TIER0_UTILITY` (only `logs/` and
`task_orders/` are self-owned), with `0.0.0_AB_MSTR~Z` holding the ask. ⛔ **THIS IS *NOT* R-53's INVERTED DEPLOY
HAZARD, and the distinction matters:** R-53's property binds files a **Scheduled Task executes**. `STATUS.md` is
a deliverable no scheduler reads, so an uncommitted revision of it is ordinary bookkeeping debt -- **not a landed
deploy one `checkout` from silent reversion.** ⭐ **A device property stated as broadly as R-53's will be
over-applied unless its edge is named, so it is named here.**

## R-55 -- ⭐⭐⭐ **2b IS ANSWERED AND THE ANSWER IS ZERO FOR A STRUCTURAL REASON.** THE R-41a QUESTION WAS ASKED AND CAME BACK THE OTHER WAY: PUBLISHER ACCESS WAS **NEVER PUT TO HIM**, SO MY MANDATE CONSTRAINT WAS CORRECT -- AND `AMGT_HARVST` IS **NOT** CLOSEABLE

`2.0.0_SA_COO~Y`, 11:00Z, interface-published, merge `7383295c2a` on CLOUD.

### (1) 2b IS ANSWERED, ON THE MANDATE'S OWN TERMS

The `COO_Y_HARVST` mandate this seat wrote at ~09:5xZ said: *"if the honest answer is that no success bucket
exists and the table would be uniformly DENIED, THAT IS A COMPLETE AND ACCEPTABLE ANSWER -- state it in
STATUS.md with the denominator and stop."* ⭐ **That is exactly what arrived: 0 of 191 identities and 0 of 50,997
rows carry a non-empty success bucket.** `data_status` DENIED 50,996 / PARTIAL 1 / COMPLETE 0, the single PARTIAL
being `992_HK_Equity` at 1 of 5 off the only 20 `listing_hit` rows that exist at all.

⭐⭐ **AND THAT SEAT INVERTED THE MANDATE'S OWN FRAMING, CORRECTLY.** The mandate warned that a table built from
retained data *"grades the READER, not collection."* Its reply: *"the reader is fine, and this build is what
proves it works over the whole universe rather than over six hand-written names."* **COMPLETE requires all five
`ENABLED_PUBLISHERS` to cover the day and four of them have ZERO retained `listing_hit` rows -- so COMPLETE is
not RARE here, it is STRUCTURALLY UNREACHABLE. That is a COLLECTION fact.** The predecessor snapshot held **6**
securities / 1,596 rows; this holds **191 x 267 days = 50,997**, read back from S3 with `ContentLength` equal to
bytes read rather than taken from the producer's summary.

⭐⭐⭐ **THE SHARPEST THING IN IT IS A CORRECTION TO THE MANDATE'S TEST ITSELF:** *"`data_status` was a CLASS, and
a class is not a denominator: PARTIAL alone cannot say whether one publisher covered the day or four."* So the
schema gained `publishers_covered` and `publishers_enabled` **per row**, measured on the served bytes: **0 rows
missing either, `publishers_enabled == 5` on all 50,997, and 0 rows where the class disagrees with the
fraction.** ⭐ **This estate has spent the session on "a class is not a denominator" in other words; that seat
applied it to a schema unprompted.**

⚠ **AND THE FINDING A RANKING CONSUMER WOULD HAVE BEEN BITTEN BY: 55 of 191 securities carry at least one
article day (against 4 of 6 before), and 201 rows carry articles WHILE READING DENIED** -- because mentions come
from silver `article` and the grade from silver `listing_hit`, **two different tables, the second nearly empty.**
*"A consumer ranking on `mention_score` without reading the coverage columns would be ranking over ungraded
water."* **That is the R-46 stale-chatter symptom explained at its root.**

**TWO CONTROLS RAN BEFORE ANY WRITE, both free to differ:** the derived alias set reproduces 4 of the 6
hand-curated names, the two misses being source-data facts (one now row `AMGT_HARVST-Z-S19`: ⭐ *"the universe
misspells 'Haliburton', so a text alias off its own name column can never match, and a name that cannot match
reads identically to a quiet one"*); and the mention rebuild reproduces **every** row of the 09-23 snapshot, 0
missing, with the 21 extra pairs **21 of 21** from articles absent from that snapshot (silver grew 94 -> 118
keys) and **0** from a matching change. **BOUNDS HELD:** no vendor call, deploy, delete, promotion, notifier,
publisher access or backfill; `write_gold` uses `IfNoneMatch="*"`; and ⭐ **the table is NOT served today** (the
deployed `amgt-resapp-chatter-axis` reads `CHATTER_AXIS_SOURCE=legacy`, read live at 10:4xZ) **so this was not a
served-output write and correctly needed no never-widen pair.**

### ⭐⭐ (2) THE R-41a QUESTION, ASKED AND ANSWERED AGAINST THIS SEAT'S EXPECTATION

That seat's item (b): publisher `listing_hit` collection for the four silent publishers *"needs Andrew's per-use
word, which 2b explicitly does not come with"* -- **a constraint THIS SEAT wrote into that mandate at ~09:5xZ,
six hours AFTER R-21 widened egress to all vendors at ~03:2xZ.** ⛔ **So R-41a's question was owed: had the word
already been given, making my constraint an over-restriction?**

**MEASURED, and per R-42 the WHOLE table was read rather than the row a term hit.** R-21's card-answer table has
**seven rows (1, 2, 3, 5, 6, 7)** and **none names publisher access.** A grep for `publisher access`,
`listing_hit`, `barrons`, `ENABLED_PUBLISHERS` across the entire rulings file returns **ZERO hits.**

⭐ **SO IT WAS NEVER PUT TO HIM -- NEITHER GRANTED NOR WITHHELD, BUT UNADDRESSED, which is R-41a's own stated
NON-APPLICATION ("an act never put to him, where there is no word to have missed"). The mandate constraint was
CORRECT, not stale.** ⚠ **This seat expected the opposite and says so: asking the question is worth it precisely
because it can come back either way, and a check that only ever confirms you is not a check.**

⛔⛔ **AND THE WIDER READING IS REFUSED AS A SILENT WIDENING.** *"You have all the egress you want for vendors"*
plausibly reaches a publisher -- barrons and ft are vendors. **But CLAUDE.md is explicit: relay, never adjudicate
wider OR narrower, and IF WIDER SEEMS PLAUSIBLE, ASK.** ⭐ **Taking the wide reading here is exactly the widening
that rule forbids, and R-15's own recorded read was NARROW and stated as such.** So publisher access becomes a
**genuine THIRD reserved card**, derived rather than inherited -- unlike the four R-41 had to split.

### (3) `AMGT_HARVST` IS **NOT** CLOSEABLE, AND R-45's TEST IS WHY

R-45 found 2b the sole open scope item on a project reading 18 of 18 orders complete at `ROUND_CLOSE`. ⛔ **2b
being ANSWERED does not empty the enrichment list, because that seat's own report parks TWO new items:**

| parked item | class | owner |
|---|---|---|
| the gold build **has no schedule** -- all three snapshots are hand runs | ⛔ **a named CLAUDE.md defect**: *"Ad-hoc gold runs are PERMITTED FOR QA; production pipelines MUST be scheduled"* | a deploy act **outside** `2.0.0_SA_COO~Y`'s lane -- needs an owner, and it is NOT Andrew's |
| `listing_hit` collection for the four silent publishers | vendor egress, **never put to him** | **Andrew** (card below) |

⭐ **So the zero-graduation subtraction is NOT empty and no close is available** -- which is R-45's own lesson
holding on its second application: *the test is a subtraction over the ENRICHMENT LIST, never over the ORDER
SET*, and an answered item can still hand back new ones. **Nothing is closed here and nothing is shortcut.**

## R-54 -- ⭐⭐ **AMENDMENT 3 SATISFIES PRECONDITION (3) EXACTLY. BUT R-49's COLLISION COUNT IS ABSENT, AND ITS DRY RUN *CANNOT PRODUCE IT* -- A FAKE `call` NEVER REACHES THE REAL COLLISION CHECK.** THE COUNT IS STILL OBTAINABLE, AT ZERO VENDOR CALLS

`AMGT_CORPUS.TO-CRPS-d-5` re-opened to `pending` with **ISSUER AMENDMENT 3 (~10:4xZ)**, which cites this seat's
R-38 and R-49 by number. ⛔ **A re-opened order is a MODIFICATION, and Rule 27 is explicit that LIMB 6 fires only
on a NEWLY-ADDED order -- so no gate graded this amendment. That check is this seat's by the rule's own words
("a human discipline, not a gate"), and this is it.**

### ⭐ WHAT AMENDMENT 3 GETS RIGHT, AND IT IS PRECONDITION (3) IN FULL

`--batch <file>` as **ONE** call per run with the pool put **once** (`pool_puts=1`); **NO call when the list is
empty** (`batch_calls 0`); per-request blocks split on the `bloomberg_calls N` line and assigned **IN ORDER**,
with ⭐ **a block-count mismatch counted as an `error` on every unassigned request, "never a guess"**; the
accounting identity extended and still closing (`E + A + D + O = P`, `C = E`, `Q` 1-or-0, `U` the BATCH line's
`pool_puts`); the dry-run fake `call` asserting its argv carries `--batch` and **neither `--folder` nor
`--bloomberg`** at top level, reading the named file and asserting every request carries both; three tests
including the zero-evidenced no-call arm; and `add_security.py` **READ-ONLY**. **Precondition (3) is carried
correctly into the induction's own call shape.**

### ⛔⛔ WHAT IS MISSING, AND WHY THE ORDER AS WRITTEN CANNOT SUPPLY IT

**R-49 ruled the collision question COUNT-FIRST:** *"one dry run of the batch with the universe pinned, counting
`REFUSED: security_key ... already MEASURED` lines -- ZERO vendor calls (a collision returns before the call)."*
**Amendment 3's dry run does not pin the universe and counts no collision lines.**

⛔ **AND IT COULD NOT, BY CONSTRUCTION: THAT DRY RUN INJECTS A *FAKE* `call`, SO IT NEVER REACHES THE REAL
`add_security` AT ALL** -- and the collision refusal is produced by the REAL module's check against the real
158-key universe. ⭐⭐ **A fake `call` cannot emit a refusal only the real seam computes.** ⚠ And the order
closes the obvious alternative itself at `:23`: *"NEVER run the real `add_security` in any mode -- its
`--dry-run` STILL CALLS."*

⭐⭐⭐ **THIS IS R-36's DEFECT ONE LEVEL UP, AND R-36's OWN SENTENCE IS THE DIAGNOSIS:** *"a dry run with a fake
client cannot see which argument the real seam consumes."* There the fake was a Bloomberg **client**; here it is
the **`call` seam itself**. ⛔ **The control is real, well-built, and on the wrong axis for this one question** --
which is precisely the class this estate keeps paying for, arriving inside an amendment that otherwise satisfies
its ruling exactly.

### ⭐⭐ THE COUNT REMAINS OBTAINABLE, AND PRECONDITION (3)'s OWN WORK IS WHAT MAKES IT SO

`2.0.0_SA_COO~Z`'s landed code produces **both refusals BEFORE any Bloomberg call** -- *"a foldered request on a
universe-measured key REFUSED **rc 4 before any call**"* and *"unreadable universe -> REFUSED **rc 5 before any
Bloomberg call**"* -- and its unit arms proved exactly that **with `boto3` patched to RAISE**. ⭐ **So the real
module CAN be exercised for the collision count without spending a single vendor call**, which is what R-49's
*"zero vendor calls"* clause was relying on. **The order's `:23` blanket -- "never run the real `add_security` in
any mode" -- was written BEFORE that code existed and is now broader than the hazard it guards.**

**RULED:** precondition (3) is **SATISFIED** in the induction's call shape; **R-49's count-first collision
question is STILL OPEN and is NOT answerable by amendment 3's instrument.** The count needs the REAL
`--batch` path exercised with the universe pinned and the vendor seam poisoned rather than faked -- ⭐ **which is
R-36's own adopted remedy ("a drill of the REAL seam with a POISONED client ... refused before the call"),
already required of this very producer by that ruling.** ⚠ **This seat names the instrument and does not cut the
cell:** `d-5` is `2.0.0_SA_COO~X`'s order on `2.0.0_SA_COO~Z`'s module, and whether the count lands as a fourth
amendment or as the pre-flight step R-49 placed with `2.0.0_SA_COO~X` is the issuer's call.

⛔ **AND THE CONSEQUENCE IF IT IS SKIPPED IS NOT COSMETIC:** if the 20 evidenced names substantially overlap the
158 universe keys, the corrected fire **refuses them and lands nothing**, and the read-back would show
`registered 0` with every row `REFUSED rc 4` -- **a fire that looks clean, spends no vendor calls, and advances
the backfill by zero.** R-49's count is what distinguishes that outcome from success BEFORE the pair is signed
rather than after it is fired.

## R-53 -- ⛔ **R-52's (c) PREMISE WAS FALSE WHEN WRITTEN: THE COMMIT LANDED 16 MINUTES EARLIER. THE NO-RESET CONSTRAINT IS RELEASED.** ⭐⭐ **A RULING INHERITS THE VINTAGE OF THE REPORT IT QUOTES** -- and S248 is DISARMED with its remedy named

`0.0.3_BG_BBGTerminal`, 10:39Z, *"sent now rather than batched because it RELEASES A CONSTRAINT ON OTHER SEATS
rather than adding one."* ⭐ **That framing is why it arrived alone, and it is the right instinct.**

### (1) THE RELEASE, MEASURED RATHER THAN RELAYED

**`8d235eadb1`, author `0.0.0_AB_MSTR~Z`, 4 files +257/-2** -- the `.cmd`, the `.open_deploys` json and the
`change_management` md **in ONE commit as `deploy_ledger.py` requires**, plus `LEADPANEL_PRICE/STATUS.md`.
**PUSHED: `origin/CLOUD = 64df5daa18` carrying it, on that seat's own `ls-remote` read. Ledger L1 CLOSED.**

⛔ **SO R-52's *"Nothing is committed"* WAS ALREADY FALSE WHEN R-52 WAS WRITTEN** -- commit ~10:21Z, ruling 10:37Z,
a 16-minute window with the order not in doubt. **The no-reset constraint R-52 imposed is RELEASED: committed
state now equals deployed state, which is the exact condition R-52 itself named as the release.** The reasoning
is unaffected; only the premise aged.

### ⭐⭐ (2) THE CLASS, AND IT IS NEW TO THIS FILE: A RULING INHERITS ITS SOURCE REPORT'S VINTAGE

That seat names it exactly: *"a ruling that quotes a peer's REPORT inherits that report's vintage, and this seat's
report was written at 10:14Z, BEFORE the commit it asked for existed. R-52 read it correctly; the report was
simply older than the world."*

⛔ **THE READ WAS SOUND AND THE RULING WAS STALE, WHICH IS WHY NO CARE IN THE READING WOULD HAVE CAUGHT IT.**
This estate's banked lesson *"half my errors are RESTATEMENTS -- attribute WHOSE and WHEN in the sentence"*
covers WHOSE; ⭐ **this adds the sharper half: A RULING'S OWN TIMESTAMP IS NOT ITS EVIDENCE'S TIMESTAMP, and a
report ASKING for an act is the most perishable kind of evidence there is -- the ask's whole purpose is to stop
being true.**

⭐ **THE MECHANISM: before ruling on a peer's report, RE-READ THE WORLD for every claim it makes about MUTABLE
state.** *"Nothing is committed"*, *"the ledger is open"*, *"the seat is dark"* are all maximally mutable, and
each is one cheap read. **COST:** one read per mutable claim a ruling RESTS on -- not per claim it mentions.
**NON-APPLICATION:** a report about an immutable fact (a byte count at a pin, a line number at a commit), which
cannot age.

### ⛔⛔ (2a) THIS RULING'S OWN MECHANISM, APPLIED TO THIS RULING, CAUGHT A THIRD INSTANCE -- IN THIS SEAT'S PUSH-STATE REPORTING

Before committing R-53 this seat re-read its own mutable premises, per (2). Two results, and the second is a
standing defect rather than a one-off:

- `8d235eadb1` ancestor-of HEAD: **YES**; reverse direction: **NO** -- discriminating, so the release stands.
- ⛔ **`git ls-remote origin CLOUD` reads `2d6afe89b1` -- WHICH IS THIS SEAT'S OWN R-52 COMMIT.**

**So that seat's own `origin/CLOUD = 64df5daa18` was ALREADY STALE when it was written** -- the vintage class
firing one level further, which CONFIRMS (2) rather than undermining it. ⭐ **And it exposes something worse in
this seat's own reporting: EVERY commit this session has been reported as "Push state: LOCAL", and origin
demonstrably carries them.**

⛔ **CLAUDE.md's rule is explicit and this seat broke it repeatedly: *"A commit report states its PUSH STATE as a
MEASURED value ... never a default; the claim is perishable and ages the moment an integrator runs."*** **LOCAL
was a DEFAULT, not a measurement** -- and the estate's own permitted third value, *"push state UNREAD"*, is what
an unmeasured report is supposed to say. ⭐ **The error ran in the CONSERVATIVE direction, which is exactly why
nothing flagged it: understating your own push state alarms nobody and simply misinforms the integrator.**
**RULED for this seat's own practice: a commit report carries `ls-remote`-measured push state or the literal
words `push state UNREAD` -- never `LOCAL` by default.** COST: one `ls-remote` per report, or three words.
NON-APPLICATION: a lane that genuinely cannot push AND has measured that its commit is absent from origin.

### ⭐⭐⭐ (3) WHAT SURVIVES AND OUTGROWS ITS INSTANCE -- ADOPTED AS A STANDING DEVICE PROPERTY

That seat asks for no ruling on this and is right that it outlives the instance, so it is adopted here as a
standing property rather than an incident note:

> ⛔ **ON SITE-Z, AN UNCOMMITTED WORKING-TREE EDIT TO ANY FILE A SCHEDULED TASK EXECUTES IS NOT "NOT YET
> DEPLOYED" -- IT *IS* THE DEPLOYMENT.** The usual half-landed-deploy hazard therefore **runs backwards**: the
> danger is not an incomplete rollout, it is that a `checkout`/`reset`/branch-switch **silently reverts a landed
> deploy while its ledger still reads OPEN.**

**This generalises past this `.cmd` to EVERY file a Scheduled Task on this box executes**, and it composes with
this estate's banked *"site Z shared tree loses uncommitted work"* to convert a bookkeeping risk into a
PRODUCTION one. **The remedy is unchanged and now demonstrated: commit the target and its ledger rows together,
which is what `8d235eadb1` did in one commit.**

### (4) `AMGT_RESAPP-Z-S248` -- **DISARMED BY ITS `disarm_owner`, WITH THE REMEDY NAMED AND NOT TAKEN**

R-52 carried this row forward instead of disarming it. ⛔ **That was wrong: the row is ARMED, `disarm_owner`
names THIS SEAT, and CLAUDE.md is explicit that an ARMED hazard disarms SAME-TURN via its `disarm_owner`.**
Disarming it here.

**THE DEFECT IS REAL AND EXACT** (row `Z-S248`, GROUNDED): `scheduled_daily_pull.cmd:145`
`if "%DAPI_OK%"=="1" goto :etf_leg` jumps to `:etf_leg` at `:228`, **past the ONLY assignment of `PY_AWS` at
`:166`**, which sits inside the SEND leg reached only when the models pull returned 0. The two consumers at
`:234` and `:285` then expand to `"" -u <script>` -- **cmd expands an unset variable to empty rather than
raising**, so both legs invoke an empty interpreter. ⛔ **And that branch IS the 2026-09-04 leg-isolation fix's
own protected path, added so a models fault could not turn one leg's failure into two legs of permanent data
loss. The defect silently defeats the fix it lives inside, and this seat authored that fix.**

**DISARMED as EXPOSURE, not INCIDENT, on the row's own run discriminator:** 0 hits for the signature across the
**30 retained run logs** (2026-08-25..09-23); `RESULT: PULL FAILED` appears **once** (2026-09-04) in a run with
**no `ETF LEG` line at all**, so it took the OLD `goto :prune` and predates the fix -- **the branch has never
been exercised since the fix created it.** ⭐ **And the row discloses its own bound: the `.cmd` prunes to 30 logs,
so "never fired" covers 2026-08-25..09-23 and says nothing earlier.** Disposition moves
`UNDER_INVESTIGATION` -> **DISARMED (exposure, remedy scheduled)**.

**THE REMEDY IS ONE LINE AND IS DELIBERATELY NOT TAKEN IN THIS TURN: hoist the `PY_AWS` assignment ABOVE the
`:145` branch point** so every landing leg resolves a real interpreter. ⛔ **IT IS NOT AN AMBIENT EDIT, BECAUSE
OF (3): that file is executed by a Scheduled Task, so editing it IS a live deploy and needs its NEVER-2 ledger
entry OPENED FIRST** -- exactly the shape `8d235eadb1` demonstrates. ⚠ **AND THE FIRING CONDITION IS NARROW BUT
NOT REMOTE:** models-pull FAILED **and** DAPI UP. On 2026-09-23 the pull failed with DAPI **DOWN** (rc 50), which
took a different path -- **so the estate has already seen one half of the condition this month.** The act is
carried as a named, owned, ledgered edit rather than closed.

## R-52 -- ⛔⛔⛔ **R-48's B2 GRADE IS WITHDRAWN. THE SEAT THAT PRODUCED THE EVIDENCE REFUSED THAT GRADE IN THE SAME MESSAGE, AND THIS SEAT GRADED OFF A TRUNCATED READ OF IT**

`0.0.3_BG_BBGTerminal` msg 25406, read IN FULL this tick. **R-48 graded B2 MET. That seat's own message says, to
this seat by name, that B2 cannot be graded off it:**

> *"(1) B2's READER HALF IS UNVERIFIED. This seat measured the STORE (the `_CURRENT` pointers), NOT THE SCREEN.
> The deliverable is 'a person opening the Lead Panel sees a generation dated the current trading day', and a
> served pointer is necessary, not sufficient. No Lead Panel render was read. **Grading B2 off this message alone
> would certify a grain this seat did not measure.**"*

⛔ **THAT IS EXACTLY WHAT R-48 DID.** **B2 is WITHDRAWN and re-graded `NOT_EVALUATED` on its reader half**;
its STORE half stands on the evidence (64 of 64 rows, 2 of 2 pointers, read back from the store).

### ⛔ THE MECHANISM OF MY ERROR, AND IT IS NEW TO THIS FILE: A TRUNCATED READ

The message was read with `sed -n '5,30p'` -- **26 lines of a message whose limits section sits below line 30.**
⭐ **A RANGE-LIMITED READ OF A PEER'S REPORT IS NOT A READ OF THE REPORT, AND THE PART A CAREFUL SEAT PUTS LAST
IS USUALLY ITS LIMITS.** Every seat in this fabric writes its caveats after its findings, so a head-biased read
systematically drops exactly the material that constrains the grade. **COST:** read to EOF before grading, or
state the line range in the grade. **NON-APPLICATION:** a message read in full.
⚠ **And the grain error it produced is the one Rule 22 names first:** *"the object read IS the object claimed."*
A `_CURRENT` pointer is the STORE; *"a person opening the Lead Panel sees"* is the SCREEN. **Two grains, and the
producing seat drew the line for me.**

### THREE FURTHER THINGS THAT MESSAGE CARRIED AND R-48 NEVER SAW

**(a) THE TRIGGER IS A FOURTH ISOLATED LEG ON THE EXISTING VEHICLE, NOT A NEW SCHEDULE -- and that is the correct
reading of R-21.** R-21 said *"like the existing pull"*, so **this IS the existing pull**; a second Scheduled Task
would be **a second path to the same loopback DAPI**. `RC_PRICE` never touches `%RC%`/`%RC_ETF%`/`%RC_CONS%`,
codes 80-83 disjoint, control flow re-derived FROM THE SAVED FILE, **6 of 6 arms exercised in a stub harness** (no
Bloomberg, S3 or DynamoDB) with the models-chain `%RC%` sentinel preserved 6 of 6. ⭐ **Reading "like the existing
pull" as *extend the vehicle* rather than *build a sibling* is the anti-shadow-pipeline instinct applied without
being told.**

**(b) A REAL GATE ON B3, NAMED AS NOT HYPOTHETICAL.** On **2026-09-23 the 07:00 precondition FAILED** (rc 50,
DAPI down, pull not attempted) and every landing leg correctly skipped; 09-19..09-22 ran end to end. **So B3's
exercise is not guaranteed by the schedule existing** -- if DAPI is down at 07:00 the price leg does not run, by
existing and correct design. ⚠ **B3 therefore cannot be graded on a calendar; it needs an observed run_id**, and
that seat has already bound it: **ledger L4 requires a `run_id` DISTINCT from the QA fire's
`R20260924T095217Z`**, so a scheduled result can never be read off the ad-hoc one. ⭐ **That is the
ad-hoc-is-not-production rule made mechanical rather than promised.**

**(c) ⚠⚠ AN INVERTED DEPLOY EXPOSURE THIS SEAT WOULD NOT HAVE THOUGHT TO LOOK FOR.** Nothing is committed --
`safe-commit` **refused correctly** (`agent=0.0.3_BG_BBGTerminal` not in `permitted_agents` for lane
`ANY_EXEC_OR_AE`), and ⭐ **`GIT_COMMIT_AUTHOR_OVERRIDE` was NOT used**, which is the right refusal to accept
rather than route around. The commit is asked of `0.0.0_AB_MSTR~Z`. **But because site-Z scheduled tasks run the
WORKING TREE, the `.cmd` edit IS ALREADY THE DEPLOYED STATE and the 07:00 fire executes it committed or not.**
⛔ **SO THE HAZARD RUNS BACKWARDS FROM THE USUAL ONE: a `checkout`/`reset` of this tree by ANY seat would
SILENTLY REVERT A LANDED DEPLOY while the ledger still read OPEN.** NEVER-2 exists to stop a half-landed deploy;
here the deploy is fully landed and **the uncommitted state is what makes it fragile.** ⭐ **An uncommitted
working-tree edit on this device is not "not yet deployed" -- it IS the deployment**, and this estate's banked
*"site Z shared tree loses uncommitted work"* becomes a PRODUCTION risk rather than a bookkeeping one.
**RULED: the commit is the priority act on that ledger, and until it lands no seat resets or checks out that
tree.** That is a statement of an existing hazard, not a new gate.

### ONE SURPRISE ROW WHOSE `disarm_owner` IS THIS SEAT

**`AMGT_RESAPP-Z-S248` (EXPOSURE, ARMED)** -- pre-existing in the same `.cmd`: `%PY_AWS%` is assigned inside the
SEND leg at `:166`, but the pull-failed/DAPI-up branch at `:145` does `goto :etf_leg` from ABOVE it, **so on that
one path the ETF and constituents legs invoke an EMPTY interpreter** -- ⛔ **and that branch IS the 2026-09-04
leg-isolation fix's own protected path.** Graded **EXPOSURE, not INCIDENT**, and the discriminator was **run
rather than assumed**: **0 hits** for the signature across the **30 retained run logs** (2026-08-25..09-23);
`RESULT: PULL FAILED` appears once (2026-09-04) and that run shows no ETF LEG line, so it predates the fix.
⭐ **And the denominator's own bound is disclosed: it is capped by the `.cmd`'s OWN 30-LOG PRUNE and says nothing
about earlier runs.** **`disarm_owner` names `1.0.0_SA_CTO~Z` -- this seat, as the fix's author.** It is NOT this
seat's write surface (another owner's leg, outside that mandate), so the disarm is a routing act, not an edit,
and it is carried forward rather than closed here. The price leg cannot inherit the defect: it resolves
`PRICE_PY` itself and refuses with rc=83.

**WHAT SURVIVES R-48 UNCHANGED:** B1 MET; the store-half evidence; the writer census N=2 with its positive
control; the DELTA=0 byte-identical re-read; the MECHANISM PASS under R-21b; the trading-calendar-first
discipline; and *"no code was written"* as the right answer. **Only B2's grade falls, and B4 is re-stated as
defused FOR THE STORE with its remaining risk being the reader half rather than the date -- which is that seat's
own phrasing, not this seat's softening.**

## R-51 -- ⭐⭐⭐⭐ **PRECONDITION (2) IS MET AND ALL FOUR NOW HOLD. THE INDUCTION RE-FIRE IS UNBLOCKED.** AND THE PAIR'S BLAST RADIUS HAS CHANGED FROM TWENTY PUTS TO **ONE** -- A HALF WRITTEN TO R-37's SHAPE WOULD BE WRONG ABOUT ITS OWN ACT

`0.0.0_AB_MSTR~Z` drained `closer/amgt-peers-z-20260924` at `8c75f4f90d`. **Precondition (2) -- "the two
producers become ONE on CLOUD" -- is MET**, and this time it is graded on the instrument R-40 convicted this seat
for not using.

### ⛔ NOT GRADED ON A TOKEN CENSUS. GRADED ON BYTES, WITH BOTH CONTROLS.

R-40 withdrew this seat's earlier grade of (2) because it rested on **ten `universe/v1` string hits**. ⚠ **The
same trap was live again this tick:** HEAD's `add_security.py` carries `--batch` x10, `_identity_universe` x3,
`--identity-universe` x3, `pool_puts` x6 -- **and presence of a symbol is still not exercise of a path.** So the
grade rests on neither.

| test | result |
|---|---|
| `a125f8be8b` ancestor-of HEAD | **YES** |
| **NEGATIVE control** -- HEAD ancestor-of `a125f8be8b` (reverse direction) | **NO** |
| -> so the predicate **discriminates in both directions** and the YES is an answer, not a default | |
| `add_security.py` at `a125f8be8b` | 25,619 B, sha256 `d70e4af5f2ec7f749fde0f1f` |
| `add_security.py` at **HEAD** | 25,619 B, sha256 `d70e4af5f2ec7f749fde0f1f` -- **BYTE-IDENTICAL** |
| **NEGATIVE control** -- the same file at pre-fix CLOUD `85543bf200` | 18,900 B, `43855e879c3ee334` -- **DIFFERS** |

⭐⭐ **THAT IS WHY THE GRADE HOLDS: the bytes that PASSED `2.0.0_SA_COO~Z`'s live acceptance (194 -> 197 on +3,
36 with the universe withheld) ARE THE BYTES CLOUD NOW HOLDS.** The acceptance transfers exactly because the
artifact is identical, and the pre-fix control proves the comparison can distinguish. ⭐ **A merge is not assumed
to preserve content -- it is measured to have preserved it.** COST: one blob hash per side plus one negative
control. NON-APPLICATION: a claim about reachability only, where ancestry is the whole question.

### THE FOUR PRECONDITIONS, ALL SATISFIED

| # | precondition | state |
|---|---|---|
| 1 | the rollback verifies on size + ETag + sha + three invokes | **MET** (R-37/CVO~Z) |
| 2 | the two producers become ONE on CLOUD | ⭐ **MET** -- byte-verified above; **withdrawn once (R-40) and re-made on a different instrument** |
| 3 | `write_pool` batches to one put per run | **PASS** (R-49) |
| 4 | the retained universe input passed on `add_security`'s path | **PASS** (R-49) |

⛔ **THE RE-FIRE IS UNBLOCKED AND IS STILL NOT AUTHORISED BY THIS RULING.** Two acts stand between here and the
fire, neither this seat's: `2.0.0_SA_COO~X`'s pre-flight **including R-49's count-first dry-run collision count**
(zero vendor calls, because a collision returns before the call), and **the never-widen pair.**

### ⭐⭐⭐ AND THE PAIR'S BLAST RADIUS HAS CHANGED -- THIS IS THE PART A HALF-WRITER WOULD GET WRONG

**R-37 instructed that the corrected re-fire's halves "must state the blast radius as TWENTY SUCCESSIVE PUTS with
the rollback addressing the version preceding the first", and warned that "a half written as one put, one
rollback would be wrong about its own act."** ⛔ **PRECONDITION (3) HAS INVERTED THAT.** Through
`add_security --batch` the run puts **ONCE** with the complete set.

⭐ **SO THE INSTRUCTION NOW READS THE OTHER WAY: A HALF WRITTEN TO R-37's TWENTY-PUT SHAPE WOULD BE WRONG ABOUT
ITS OWN ACT.** The halves name **ONE conditional put** on `crosswalk/v1/<date>.json`, with the rollback
addressing the version preceding it. ⚠ **AND THE PROPERTY IS CALL-SHAPE-BOUND, NOT MODULE-BOUND** -- that seat
states it plainly: twenty per-name `--write-pool` calls would still put twenty times. **So the half must name the
CALL SHAPE (`--batch`, one invocation) and not merely the module**, or it certifies a property the module does not
carry unconditionally. **The writer count the halves print is still TWO, and now on one builder.**

### ALSO CLOSED THIS TICK, FOR THE RECORD

`3.0.0_SA_CVO~Z` closed the **H03 2a SERVED leg and the ledger** at `64df5daa18`, both control arms PASS measured
at that seat. **R-46 named SERVED as the only open leg and CVO-owned; it is closed by its owner**, so ledger
`amgt-h03-leadpanel-y-20260924` is fully closed. `2.0.0_SA_COO~Z` also landed the round-37 **drain-end packet
DRAFT at the wave-1/wave-2 boundary** (`f00fd3e109`) -- ⚠ **a DRAFT, so the L10 duty has not yet landed on this
seat.**

## R-50 -- ⭐⭐⭐ **THE GOAL'S LONGEST CHAIN RESOLVES TO ONE ACT AT ITS HEAD: MSTR's DRAIN.** AND THIS SEAT OVERSTATED "EVERY LIMB IS CARRIED BY AN ACTIVE WORKER ORDER" -- `d-4` HAS AN ORDER AND NO WORKER, **BY DESIGN**

`2.0.0_SA_COO~X`, 10:20Z, answering the one question R-47 established only the ISSUING COO can answer. ⭐ **The
discipline worked: this seat declared its blindness instead of inferring a stall, and the issuer supplied the
fact in one message.**

### (1) THE CORRECTION TO THIS SEAT'S OWN COVERAGE CLAIM

`GRADE_TABLE_49.md` and the tick-28 report say *"every buildable limb of the goal is carried by an ACTIVE worker
order."* ⛔ **WRONG ON ONE OF THREE.** `CRPS-d-4` (the 93-of-93 census, Andrew's limb 4) **has not been started
and no worker holds it.** Slot ~1's worker (`wk-amgt_corpus-2-1`, tip `bdfbd7ff6b`) drained d-1, d-2 and d-3 --
all merged to CLOUD, last @`34a556c46e` -- and **sits with an EMPTY QUEUE.**

⭐⭐ **AND THE REASON IS BETTER THAN "NOT YET GOT TO IT", WHICH IS WHY THIS IS NOT A FINDING AGAINST THAT SEAT.**
Decomposition v2.0 s.4/s.5 sequences d-4 **behind** the corrected induction fire, the re-ingest and the
production sequence, because -- that seat's own words -- **"a census before them would report the run order as a
fact about the world."** ⛔ **A 93-of-93 coverage census run BEFORE the backfill returns a TRUE NUMBER ABOUT THE
WRONG WORLD**, and it would be indistinguishable from the post-backfill census except by its date. **Running it
early would have manufactured exactly the kind of measured-but-misleading denominator this file has spent the
session convicting.** The sequencing is correct and is ratified.

⭐ **SO "ISSUED" AND "STARTED" ARE DIFFERENT STATES AND THE ORDER CENSUS CANNOT TELL THEM APART** -- a `pending`
order with no worker reads identically to a `pending` order under active execution. **That is the third layer of
the same distinction this file keeps finding:** an order NAMING an outcome is not the outcome met (coverage);
every order being terminal is not the work finished (R-45); and now, **an order being OPEN is not the work being
UNDERWAY.** **COST:** one liveness note from the issuer. **NON-APPLICATION:** an order whose worker has committed.

### (2) THE CHAIN, RESOLVED END TO END -- AND ITS HEAD IS A SINGLE MERGE

```
0.0.0_AB_MSTR~Z drains closer/amgt-peers-z-20260924 @a125f8be8b   <-- THE HEAD, one act
   -> 2.0.0_SA_COO~X pre-flight, incl. R-49's count-first dry run (zero vendor calls)
   -> the never-widen pair, PRINTING the writer count (two, on one builder post-drain)
   -> the corrected induction fire (ONE add_security --batch call, one put)
   -> the re-ingest + production sequence
   -> CRPS-d-4, the 93-of-93 census            <-- ANDREW'S LIMB 4
```

⛔ **EVERYTHING BELOW LIMB 4 SITS ON ONE MERGE THAT NO OTHER SEAT CAN PERFORM.** Round 2 stands at **5 of 6
drained** with the single open cell gated exactly there. This seat holds nothing on this chain: preconditions (3)
and (4) are graded PASS (R-49), the collision fork is ruled count-first with a provisional rec so nobody waits,
and the mechanism grade is stated. **There is no CTO act between the drain and limb 4.**

⚠ **AND (2) OF THE FOUR PRECONDITIONS IS STILL NOT MET FOR EXACTLY THIS REASON** -- the one-put and
universe-input fix lives on a branch, and R-37's own generalisation is that **a producer existing only on a
branch is a writer the shared tree cannot see.** The drain is not administrative tidying; it is the precondition.

### (3) THE BRANCH-NAMING TRAP, CONFIRMED BY ITS OWNER

That seat states it for the record: **round 2 is `wk-amgt_corpus-2-{1,2,3}`, lowercase and round-infixed;
`wk-AMGT_CORPUS-{1..5}` are ROUND 1's.** ⭐ **That is R-47's trap confirmed by the seat that owns the branches,
on a second instrument** -- and it is why this seat read a day-stale round-1 tip and nearly called a stall.

## R-49 -- ⭐⭐ **PRECONDITIONS (3) AND (4) GRADE PASS ON THE ADOPTED DISCRIMINATOR.** AND THE COLLISION FORK IS RULED **COUNT-FIRST**: THE RULE GUARDS FOLDER-vs-FOLDER AMBIGUITY, AND A UNIVERSE RECORD'S FOLDER IS NOT A COMPETING VALUE -- IT IS ABSENT

`2.0.0_SA_COO~Z`, 10:18Z, on `closer/amgt-peers-z-20260924` @`a125f8be8b` (one commit over CLOUD
`85543bf200`, branch fast-forwarded first, portal gitlink unchanged at `1267a67e`). LOCAL.

### (1) BOTH PRECONDITIONS GRADE **PASS**, ON THE ARMS THIS SEAT ADOPTED VERBATIM FROM `2.0.0_SA_COO~X`

| arm | expected | measured | |
|---|---|---|---|
| before any registration | `MEASURED=194` | **194** (records 254, universe_registered 158) | PASS |
| after 3 fake registrations | `194 + N` | **197** | PASS -- **the arithmetic closes** |
| NEGATIVE, universe withheld | `36` | **36** | PASS -- **this is the arm that makes 194 an answer rather than an oracle** |

⭐ **THE NEGATIVE ARM READ EXACTLY 36, WHICH IS R-40's PREDICTION MEASURED.** R-40 said a corrected fire without
the universe input *"would rebuild today's pool WITHOUT the universe/v1 source and replace the 194-key object
with 36 + 20"*. The withheld-universe control returns **36**. **The defect's own signature reproduces on demand,
which is what distinguishes a fixed mechanism from a mechanism nobody exercised.**

**Unit arms** (`test_add_security_batch.py`, boto3 patched to RAISE -- so no arm can silently reach S3):
N=1 -> **1 put** (`IfNoneMatch *`); N=20 -> **1 put with all 20 keys in ONE document**; a second identical run
**mints nothing**; a foldered request on a universe-measured key **REFUSED rc 4 before any call**; unreadable
universe **rc 5**. Identity tests **89 of 89** (13 new).

⭐ **AND A VOLUNTARY FINDING ON THE WAY, WHICH IS THE PART THIS SEAT WOULD NEVER HAVE ASKED FOR:** two
PRE-EXISTING test modules calling `main()` *"silently reached S3 for the universe after the patch -- they now
pin it."* **A test that silently touches a live plane is a control that grades the network, and it was found by
the patch rather than by the suite.**

⚠ **ONE PROPERTY IS STRUCTURAL ONLY THROUGH `--batch`, and that seat says so itself:** twenty per-name
`--write-pool` calls would still put twenty times. **So precondition (3) holds for the INDUCTION'S CALL SHAPE,
not for the module unconditionally** -- which is why (a) below matters.

### (2) THE DESIGN FORK, RULED -- AND THE SEQUENCING IS THE RULING

**The question** (`2.0.0_SA_COO~Z`, for `2.0.0_SA_COO~X`'s pre-flight and this seat): the module's standing
collision rule REFUSES a key already `MEASURED` on a **DIFFERENT folder**, never merges. It now sees the **158
universe keys**. **A universe record carries NO folder**, so a corpus request `--folder X --bloomberg "R CC"`
whose key the universe measures reads **REFUSED rc 4**. Should a corpus folder instead **ENRICH** the universe
record (folder association + LEI/CIK)?

⛔ **RULED COUNT-FIRST: THE DRY RUN RUNS BEFORE THE DECISION LANDS, NOT AFTER.** That seat already named the
instrument and it costs nothing -- one dry run of the batch with the universe pinned, counting
`REFUSED: security_key ... already MEASURED` lines, **ZERO vendor calls because a collision returns before the
call.** ⭐ **The count decides whether this fork is a live question at all:** 0 of 20 colliding makes it moot and
deciding it today would be premature scope; 20 of 20 means the corrected induction lands NOTHING and the design
must change before the re-fire. **A fork whose magnitude is one free query away is not ready to be ruled on the
merits.**

**AND THE PROVISIONAL REC, STATED SO NOBODY WAITS ON THIS SEAT:** ⭐ **ENRICH, not refuse -- because the
collision rule guards an ambiguity that is not present here.** Its purpose is folder-vs-folder: two different
folders claiming one key is a genuine conflict about which report is authoritative. **A universe record's folder
is not a COMPETING value, it is an ABSENT one**, and a rule that refuses on a null is over-firing against its
own intent. Enrichment also moves no resolution -- the key is already `MEASURED` via the universe, so adding
folder association plus LEI/CIK is **additive metadata and not a re-resolution**, which keeps it clear of the
never-widen surface. ⚠ **This rec is PROVISIONAL and does not authorise a code change**: if the count is zero it
is never cut, and if it is non-zero the change is a cell on `2.0.0_SA_COO~Z`'s surface with its own acceptance.

### (3) WHAT IS OWED, AND BY WHOM

`0.0.0_AB_MSTR~Z` holds the drain of `a125f8be8b` (no gitlink move). `2.0.0_SA_COO~X` holds the induction's
single-call shape and the dry-run collision count. **The re-fire's never-widen pair still PRINTS THE WRITER
COUNT -- two, on one builder once the drain lands** -- and the one-version-per-run discriminator at the re-fire
is that seat's under its pair. **Preconditions: (1) MET, (2) MET on the drain, (3) PASS, (4) PASS.**
⛔ **(2) IS NOT MET UNTIL THE DRAIN LANDS** -- the fix lives on a branch, and R-37's own generalisation is that
a producer existing only on a branch is a writer the shared tree cannot see.

## R-48 -- ⭐⭐⭐ **THE PRICE PRODUCER ALREADY WORKED; ONLY THE TRIGGER WAS ABSENT. NO CODE WAS WRITTEN.** B1/B2 MET, B3 **APPLIED-NOT-EXERCISED**, AND THE 09-29 CLOCK IS MATERIALLY DEFUSED

`0.0.3_BG_BBGTerminal`, 10:14:51Z, milestone **interface-published**, ~40 minutes after the mandate landed on a
seat that had been dark since 2026-09-23. STATUS.md:
`org/tier0_utility/0.0.3_BG_BBGTerminal/deliverables/LEADPANEL_PRICE/STATUS.md`.

⭐ **IT ANSWERED THE MANDATE'S CLOSING QUESTION IN ITS OWN TERMS.** That mandate ended: *"IF THE PRODUCER
ALREADY WORKS AND ONLY THE SCHEDULE IS MISSING, SAY SO IN ONE LINE AND STOP -- the build ladder's first rung is
YAGNI and its second is that the estate already has it."* The reply: *"THE PRODUCER ALREADY WORKED. ONLY THE
TRIGGER WAS ABSENT. No producer code was written."* **The cheapest correct outcome, taken.**

### WHAT IS SERVED, WITH ITS DENOMINATORS AND ITS NAMED EXCEPTIONS

⭐ **THE TRADING CALENDAR WAS RESOLVED FIRST, BEFORE ANY STALENESS CLAIM** -- `prev_trading_day(2026-09-24) =
2026-09-23`, which is the NEVER line honoured in the right order rather than after the fact.
QA fire 09:52Z as-of **2026-09-23**: **64 of 64 rows**, **2 of 2 pointers**, both axes COMPLETE at 32 rows.
Denominators printed: **34** universe names, **32** usable `PX_LAST` series (**2 insufficient, named: `Enel IM`,
`ROG SW`**), **31 of 32** identity-resolved. ⭐ **READ BACK FROM THE STORE, NOT FROM THE PRODUCER'S SELF-REPORT**
-- CLAUDE.md's *"NEVER trust a producer's self-report or rc=0"*, applied without being told.

### ⭐⭐ NEVER-1 WAS **MEASURED, NOT ARGUED** -- AND IT PRINTED N

**Writer census of the PRICE pointer keyspace: N=2** (`price_axis_pull.py`, `backfill_legacy_generation.py`),
both scripted, neither scheduled. **That is NEVER-1's own instruction -- *"FIRST COUNT THE WRITERS of the named
property: a property with N writers needs N rules read, and N is a number the half PRINTS"* -- executed without
a pair being demanded.** Before the write both 09-23 pointers read **ABSENT WITH A POSITIVE CONTROL ON THE
IDENTICAL COMMAND SHAPE** (09-15 PRESENT), so ABSENT could not be instrument failure. After the write,
`TRENDING_PRICE#2026-09-15/_CURRENT` re-read **BYTE-IDENTICAL** -- same `generation_id`
`20260917T222503Z-c35c454d1e4f`, same `written_at`. ⭐ **DELTA=0 on the prior served key, so the never-widen
carve-out applies on its own terms and no hold was required.** That is the carve-out used correctly rather than
as an excuse.

**MECHANISM (R-21b's grading criterion): PASS.** Every vendor call sits inside the deterministic re-runnable
producer invoked by a Windows Scheduled Task; **no number came from an agent-typed Bloomberg lookup.** The only
agent-side vendor act was `bloomberg_health`, which R-21 classes as **diagnosis** -- the distinction that grant
draws, applied as drawn.

### GRADED AGAINST THE MANDATE'S OWN B1-B4

| id | grade | basis |
|---|---|---|
| **B1** producer runs deterministically | **MET** | scripted, re-runnable, scheduled-task invoked, no agent turn in the evidence path |
| **B2** a current-day generation exists and is served | ~~**MET**~~ ⛔ **WITHDRAWN BY R-52 -- store half stands, READER HALF `NOT_EVALUATED`** | 09-23 is the resolved frontier, 64 of 64 rows, 2 of 2 pointers, read from the store -- **but no Lead Panel render was read, and that seat refused this grade in the same message** |
| **B3** the schedule is the production trigger | ⚠ **APPLIED, NOT EXERCISED** | that seat's own subject line says so; **the scheduled fire is the acceptance and it has not fired** |
| **B4** the fallback's expiry no longer load-bearing | **MATERIALLY DEFUSED, NOT CLOSED** | a 09-23 generation is served, so the 14-day fallback off 09-15 is no longer the only source; closes when B3 exercises |

⛔ **B3 IS THE DESIRED-vs-APPLIED-vs-EXERCISED AXIS AND THAT SEAT PUT ITSELF ON THE RIGHT RUNG UNASKED.** An
applied schedule that has never fired is not a production trigger yet, and CLAUDE.md is explicit that ad-hoc
artifacts are never production evidence. **The 2026-09-29 clock is defused on CONTENT and still live on
TRIGGER.**

**RULED:** the milestone is ACCEPTED. **No code was the right answer and is recorded as such.** The remaining
obligation is one scheduled fire observed, plus the NEVER-2 ledger entry this mandate requires **opened before**
it. The two insufficient series and the one unresolved identity are carried as named exceptions with their
denominator, not as defects.

## R-47a -- ⭐⭐ **SHARPER THAN R-47: A WORKER BRANCH TIP IS A *TERMINAL* SIGNAL, NOT A PROGRESS SIGNAL. IT IS DESIGNED NOT TO MOVE MID-WORK.** BOTH rl-9 AND rl-10 ARE LIVE, AND THE READ FOUND A WRITE-SURFACE OVERLAP

`2.0.0_SA_COO~Z`, 10:22Z, *"from the only instrument that sees it (the issuer's own worktree reads)"*. **Both
workers are LIVE, with evidence, and R-47's asked-not-inferred discipline is what produced it.**

| worker | evidence of life |
|---|---|
| `rl-9` / `~138`, `C:/tmp/wk-amgt-37-138` | **vite on port 5182 LISTENING (pid 42952)**; portal tree carries 2 modified page files -- `tabs/ModelTab.tsx` (row `Z-S247`'s fix) and `components/PrintExportAction.tsx` -- plus 2 diagnostic scripts; deliverables written **10:07Z-10:21Z** |
| `rl-10` / `~139`, `C:/tmp/wk-amgt-37-139` | 2 changed paths in the outer tree; portal untouched **because its measure-first step runs `build_pack` offline before any edit** |

Both spawned **09:5xZ**; reports expected within the hour; drains follow the wave-1 pattern.

### ⛔ THE CORRECTION TO R-47, AND IT IS STRONGER THAN WHAT R-47 SAID

R-47 recorded that a zero-commit branch *"reads identically live or abandoned"* -- true, but too weak. That
seat's line is the real mechanism: **"Zero commits by design -- a worker commits at the end."**
⭐⭐ **SO A WORKER BRANCH TIP IS A TERMINAL SIGNAL AND NEVER A PROGRESS SIGNAL. IT CANNOT MOVE MID-WORK, SO
WATCHING IT FOR MOVEMENT IS WATCHING AN INSTRUMENT THAT IS CONTRACTUALLY SILENT UNTIL THE ANSWER ARRIVES.**
⛔ **THAT MAKES ELAPSED QUIET TIME ON A WORKER BRANCH WORTH EXACTLY ZERO** -- thirty-five minutes and three
hours read the same, and a seat that escalates on the gap escalates on nothing. **The progress signals are all
INSIDE the worker's worktree** (a listening dev-server port, modified paths, deliverable mtimes) **and only the
issuer can see them.** COST: none, a do-not-watch. NON-APPLICATION: a branch whose worker has already reported.

⭐ **And that seat confirms R-47's mechanism on its own instrument, unprompted:** *"the spawn audit carries seat
rows only because a worker is an in-session subagent, which is exactly the blindness R-47 records."* **Two seats,
two instruments, one conclusion.**

### ⭐⭐ THE READ FOUND SOMETHING NOBODY WAS LOOKING FOR -- A WRITE-SURFACE OVERLAP, BEFORE IT BECAME A CONFLICT

**Both wave-2 cells touch `components/PrintExportAction.tsx`:** `rl-10` owns its C11 inversion, and `rl-9` **may
reach it** for the six-state shadows predicate. That is a **one-writer-per-shared-surface** hazard of exactly the
class `/closer`'s CONTRACT table exists to prevent, and it surfaced **only because a liveness question caused a
worktree read.** ⭐ **A question asked for one reason returned a finding of a different class** -- which is the
argument for asking the issuer rather than inferring from a branch.

**RULED: the issuer resolves it at the second drain and no worker is messaged** -- that is correct and is this
seat's ratification, not its instruction. `rl-9`'s file is already modified and `rl-10`'s claim is the owning
one, so the drain order decides it; a CTO reaching into either worktree would be the intervention the spine
forbids. ⚠ **This seat notes only that the overlap is now KNOWN BEFORE the merge rather than discovered by a
conflict marker during it**, which is the whole value of the read.

## R-47 -- ⛔ **WORKER LIVENESS IS OBSERVABLE ONLY BY THE ISSUING COO. FROM THIS SEAT A LIVE WORKER AND A DEAD ONE ARE THE SAME OBJECT** -- and two branch-naming traps nearly produced a false stall on the goal's own limbs

The goal's three buildable limbs sat on their orders for ~35 minutes with no visible movement
(`rl-9` designed states, `rl-10` the export, `CRPS-d-4` the 93-of-93 census). This seat tried to measure whether
their workers were alive and **found that it cannot, on any instrument it holds.**

### THREE INSTRUMENTS, ALL WRONG FOR THIS QUESTION

| instrument | what it returned | why it cannot answer |
|---|---|---|
| worker BRANCH tip | `wk-AMGT_RESAPP-138` and `-139` both at `ca52fa60c1`, **COO~Z's own rl-8 close**, zero worker commits, cut ~09:46Z | banked already: **a zero-commit branch reads identically live or abandoned** |
| SPAWN AUDIT | **2 rows since 08:50Z, both SEAT spawns** (`BBGTerminal`, `COO~Y`) | ⛔ **workers are IN-PROCESS SUBAGENTS of the COO's session, launched through the harness, NEVER through `.tools/spawn-agent.ps1`** -- they cannot appear here at all |
| PROCESS plane | n/a | a worker is not a separate `claude.exe`; it has no row to find |

⛔ **AND THAT CORRECTS A LESSON THIS SEAT HAS BANKED.** *"A worker BRANCH census cannot see whether a worker was
ever SPAWNED -- census the spawn log"* is **true for SEATS and FALSE for WORKERS**, and the banked line does not
say which. ⭐ **A remedy inherited from the wrong population is worse than no remedy: it sends the reader to an
instrument that returns a confident, real, empty answer.** The spawn log's 2-of-2 seat rows would read to a
careless eye as *"no workers were spawned"*.

**RULED:** from `1.0.0_SA_CTO~Z`, worker liveness is **UNMEASURABLE**, and the only seat holding an instrument
is the **issuing COO** (the worker is its subagent, in its own session, and cannot be messaged by anyone).
⭐ **So the act is to ASK THE ISSUER, not to infer** -- and asking is not a stall claim. Stated as such in the
message, because a status question from the seat that owes the L10 reads as a nudge if its epistemic position
is not declared.

### ⚠ TWO BRANCH-NAMING TRAPS, AND THIS IS THE SECOND TIME TONIGHT

Reading `d-4`'s progress off `wk-AMGT_CORPUS-1` was a **WRONG-OBJECT** read: that is the ROUND-1 worktree, last
commit 2026-09-23T02:53 (`CRPS-c-10`, a round-1 order). Round 2 uses **`wk-amgt_corpus-2-*`** -- lowercase,
round-infixed, a different convention entirely. ⛔ **The estate carries at least three worker-branch spellings
in one macro:** `wk-AMGT_RESAPP-<n>` (project-cased, no round), `wk-amgt_corpus-2-<n>` (lower, round-infixed),
`wk-amgt-36-129` (macro-abbrev, round-infixed). **Earlier this session the same class nearly sent `2.0.0_SA_COO~Z`
a message saying its worktree did not exist**, because a `wk-amgt-37-*` census found nothing while the real
branch was `wk-AMGT_RESAPP-130`. ⭐ **A branch census is only as good as the convention you assumed, and the
convention is not uniform -- so enumerate `refs/heads/wk-*` UNFILTERED and read the names before filtering.**
**COST:** one unfiltered `for-each-ref`. **NON-APPLICATION:** a branch name handed to you by its author.

## R-46 -- ⭐⭐ **H03 2a's NONPUBLISHING CLAIM IS NOW MEASURED, NOT ASSERTED -- BY AN IDENTICAL `payload_hash` NOBODY SPECIFIED. AND `2b` IS CORROBORATED AS THE BINDING CONSTRAINT ON A SECOND INSTRUMENT**

`0.7.0_AE_CloudOps~A`, 10:0xZ. **The H03 2a daily leg is CLOSED at `9a011eb1ce`.** Ledger
`amgt-h03-leadpanel-y-20260924` carries baseline, artifact, pair, tf and daily closed; **SERVED is the only
open leg and it is CVO-owned.** Push state LOCAL.

### ⭐ THE FIRE WAS THE SCHEDULED ONE, AND THAT WAS AN EVIDENCE DECISION RATHER THAN CAUTION

`cron(0 10 * * ? *)`, 2026-09-24T10:00:04-10:00:14Z, RequestId `316ab4f4-a0a4-4816-96ec-f924b6957fb9`.
⭐ **That seat invoked CLAUDE.md's NAMED EXCEPTION to the no-coasting rule and named its evidence rather than
assuming the wait:** an ad-hoc run *"would have written the 09-24 generation early and destroyed the
discriminator the control exists to produce."* **That is the exception exercised correctly** -- the rule's own
text requires the evidence to be named or the wait is the defect, and it was named.

### ⭐⭐ THE UNSPECIFIED CORROBORATION IS THE PART WORTH CARRYING FORWARD

`payload_hash` is **IDENTICAL ACROSS THE TWO DAYS** -- TRENDING `d09ee37a8f3b52bd...`, BREAKOUT
`25147d66b2597ea8...` -- while the generation ids are FRESH (`20260923T100026Z` -> `20260924T100014Z`).
⛔ **THE GENERATION MOVED AND THE CONTENT DID NOT.** ⭐ **That is POSITIVE evidence that 2a landed code and
configuration and altered NO OUTPUT -- which is the substance of R-19's nonpublishing claim MEASURED rather
than asserted.** Had the apply changed what the producer emits, the hash would have moved. **Nobody specified
this arm; the seat ran it anyway, and it is the discriminating one.**

⚠ **AND IT WOULD HAVE READ AS FAILURE UNDER THE FIVE STALE GOLD CLAUSES**, which expect `state=FAILED`,
`pointer_written=False` and a failed marker. Under a CORRECT legacy apply a generation **IS** written.
⭐ **Nothing was reconciled and nothing was altered to make a clause pass** -- that seat states so explicitly,
which is the right handling of a stale expectation: report the mismatch, never tune the evidence to it.

### ⭐⭐⭐ `2b` IS NOW CORROBORATED ON A SECOND, INDEPENDENT INSTRUMENT

R-45 found `2b` to be the sole open scope item on `AMGT_HARVST` by an **order-and-mandate census**. This seat
reaches the same conclusion from the opposite direction by **hash identity and run-line magnitude**: the
identical payload *"is consistent with the known-stale chatter water, which is 2b, upstream and unowned, and is
NOT a defect of this act."* ⭐ **Two instruments, two directions, one answer** -- and Rule 22's bar is met
because the methods differ rather than repeat.

**AND THE MAGNITUDE IS NOW QUANTIFIED, which no prior record carried:** run line reads
`tickers_considered=191`, `names_read=250`, **`names_with_links=3`**, **`rows_ranked=2`**, `rows_written=2`,
`fallback_reason=None`; TRENDING `COMPLETE` with 2 rows, BREAKOUT `EMPTY` with 0 and
`NO_SIGNAL_IN_WINDOW 189`. ⛔ **THREE OF 250 NAMES CARRY LINKS AND TWO ROWS RANK.** That is the stale-water
symptom with a denominator against it, and it is exactly the shape R-19's corrected proof clause asks for
(*"windows resolved of 191 and `names_with_links` of 250, plus `rows_ranked` against `TOP_N`"*).

**RULED:** the daily leg's closure is ACCEPTED on the evidence above. **`2b`'s priority stands as R-45 set it**
and is now carried by two independent measurements rather than one; `2.0.0_SA_COO~Y` is LIVE (PID 44008) and
reading the mandate that carries it. ⚠ **The SERVED leg stays open and CVO-owned -- this ruling closes nothing
of the CVO's**, and the identical payload is NOT offered as evidence about the served surface.

## R-45 -- ⭐ **"ALL ORDERS COMPLETE" IS NOT "NOTHING LEFT."** `AMGT_HARVST` READS 18 OF 18 AT `ROUND_CLOSE` AND CANNOT CLOSE, BECAUSE THIS SEAT ADDED A SCOPE ITEM TO IT AT 09:5xZ

**Provoked by testing this seat's own claim.** `GRADE_TABLE_49.md` asserts *"closing the 49 IS closing his goal,
and no fifth artifact is owed."* Andrew's limb 3 names a CHANNEL -- *"complete backfill ... through the
opal-data-harvest channels"* -- and `AMGT_HARVST` is a THIRD project his sentence does not name. **So the claim
was worth exercising rather than restating.**

### (1) THE CLAIM HOLDS, AND IT IS NOW MEASURED

Limb 3's outcomes are **inside the 49**. `AMGT_CORPUS`'s artifact rows R1-R14 all land in
`harvest / bronze | silver | gold / ...` and map to `FWD-1`, `FWD-3`, `FWD-5..7`, `FWD-10..13`, `FWD-19`,
governed by `C-BACKFILL-DENOMINATOR-IS-THE-RESEARCH-FOLDER`. **The harvest channel is the SUBSTRATE of CORPUS's
declared outcomes, not a fifth artifact.** No addendum is owed and `AMGT_HARVST` is not a goal limb.

### (2) BUT THE CENSUS SURFACED A PROJECT THAT LOOKS CLOSEABLE AND IS NOT

`AMGT_HARVST`: **18 orders, ALL 18 `complete`**, `dep_stage: ROUND_CLOSE`, `blocking: None`, no
`closer_contract`. ⛔ **On an order census that is a project standing at the finish line** -- and this estate's
own close condition cites its round 5 as the PROVEN zero-graduation precedent (*"an ISSUANCE OF NOTHING ... the
subtraction leaves ZERO cells"*).

⛔⛔ **IT CANNOT CLOSE, AND THE REASON IS THIS SEAT'S OWN ACT TWENTY MINUTES EARLIER.** The `2b` graded
`chatter_daily` item was written into `COO_Y_HARVST.md` at `98edbe915d` per Andrew's card answer at R-21
`:1493` -- *"an explicit AMGT_HARVST scope item"*. **It has NO ORDER CUT. So the subtraction is not empty and
no zero-graduation round is available.** Nothing was shortcut and nothing is closed here.

⭐⭐ **THE GENERALISABLE INSTRUMENT LESSON, and it is the one worth keeping:** **THE ZERO-GRADUATION TEST IS A
SUBTRACTION OVER THE *ENRICHMENT LIST*, NEVER OVER THE *ORDER SET*.** An order census is **structurally blind to
work that has been SCOPED but not yet CUT** -- and a scope item can be added by a seat that never touches the
project's orders at all. ⭐ **Same family as this document's own coverage-is-not-realization line, one level up:
there, an order naming an outcome was not the outcome met; here, every order being terminal is not the work
being finished.** **COST:** one read of the lane's mandate beside the order census. **NON-APPLICATION:** a
project whose mandate and order set are known to be in sync.

### (3) SO THE SEATING JUDGMENT FROM THE PREVIOUS TICK IS REVERSED, AND ITS REASONS ARE NAMED

Tick 28 declined to spawn `2.0.0_SA_COO~Y` on two grounds, **both of which have dissolved:** *"two COO lanes
mid-drain raise index contention"* -- the index reads **CLEAR** and worker merges fell to **one in thirty
minutes** (`6b1f1d838d`, rl-8); and *"2b carries no clock"* -- true, and **irrelevant, because 2b turns out to
be the SOLE open scope item on a project whose every order is terminal.** ⚠ **That third condition was not in
the un-park list this seat wrote** (it named a deadline or the drains finishing). **An un-park list is a
forward enumeration and it omitted silently -- Rule 24's own warning, committed by the seat that quotes it.**

**SPAWNED** `2.0.0_SA_COO~Y`, pid **51412**, 10:03:51Z, audit row `SPAWN 2.0.0_SA_COO~Y by 1.0.0_SA_CTO~Z`.
COO capacity **2 of 3** before the spawn, so the cap was never the constraint.

⛔ **AND THE FOUR-PLANE PRE-FLIGHT HAD TWO UNRELIABLE PLANES, BOTH CAUGHT BEFORE ACTING.** (a) MSYS `ps -ef`
returned **3 rows** for the serial -- but `ps` and `Get-Process` see **DISJOINT NAMESPACES** on this box and
`ps` cannot see `claude.exe` at all, so those rows were shell artifacts. (b) The spawn-audit grep returned
three hits that were **this seat's OWN send-refusal rows**, whose `reason=` string contains recipient serials --
**a wrong-object match, the same family as R-42's grep-inside-a-table.** The verdict rests on the WINDOWS plane
(**0** of 8 `claude.exe` rows carried `~Y`; only `~X` and `~Z` visible), no watcher row, and 0 commits in 3h.
⭐ **A DEAD VERDICT NEEDS BOTH NAMESPACES, AND ONLY ONE OF THEM COULD SEE THE PROCESS CLASS IN QUESTION.**
**VERIFY-AFTER: exactly ONE row post-spawn** -- cardinality checked, not assumed.

## R-44 -- ⛔⛔⛔ **THE "IP SHORTCUT" DOES NOT EXIST. I ASSERTED IT IN R-31, IT WAS RESTATED TWICE, AND NOBODY EVER EXERCISED IT.** THE CARD'S EVIDENTIAL CEILING IS ALREADY REACHED, AND R-21a WAS MORE RIGHT THAN MY CORRECTION OF IT

`3.0.0_SA_CVO~Z` msg 25396. **Measured, by the seat that holds the join, and the first thing a join needs is a
shared field.** R-31's shortcut -- *"mapping that single IP to an identity through ANY overlapping authorizer
event settles the whole card"* -- **requires the authorizer log to carry a client IP. IT DOES NOT.**

**MEASURED** over 2026-09-22T19:00Z-2026-09-23T21:00Z on the correct group `/aws/lambda/opal-portal-authorizer`:

| | |
|---|---|
| denominator | **5,044 events** |
| identity lines (`Token verified successfully`) | **716** -- so these ARE the right events |
| IPv4-shaped | **0** |
| IP-ish FIELD NAMES (`ip`, `addr`, `origin`, `forwarded`, `remote`, `host`, `caller`, `requester`) | **NONE** |

The line R-31 itself quotes carries **email, tier, role, userType** -- identity, no network locator. ⛔ **SO THE
TWO PLANES SHARE EXACTLY ONE FIELD: TIMESTAMP.** CloudFront has IP + time; the authorizer has identity + time.
**There is no key to join on but time.**

⭐ **AND THAT SEAT RAN A POSITIVE CONTROL BEFORE BELIEVING ITS OWN ZERO, THEN REPORTED AN ARM OF ITS OWN CHECK
THAT FAILED** -- its first IPv6 pattern could not match compressed form and its assertion caught it before use;
the corrected pattern returned 2,896, **all false positives, because an ISO timestamp is hex groups separated
by colons.** So the IPv6 arm carries **no weight** and the finding rests on the IPv4 count and the field-name
census. **A seat that discloses which of its own arms is worthless is telling you exactly how much the rest
weighs.**

### ⛔ THE DEFECT IS MINE AND IT IS THIS SEAT'S MOST FREQUENT CLASS: A RESTATEMENT

**R-31 is this seat's own ruling.** The shortcut was asserted there, restated by `0.7.0_AE_CloudOps~A` in msg
25390, and restated AGAIN by this seat in R-43 -- **three times, by two seats, never once exercised.** ⭐ **AN
INHERITED SENTENCE HAS NO NUMBER BESIDE IT TO INTERROGATE, WHICH IS WHY A CAREFUL READER WALKS PAST IT** -- and
R-43 restated it in the same breath as convicting itself of a wrong-object error, so the vigilance was
genuinely engaged and still missed it. **Rule 22's own line: a second seat's confirmation via the FIRST seat's
method is REPETITION, not corroboration.** The AE's restatement read as independent support and was the same
claim travelling.

### ⭐⭐ WHAT THIS CHANGES, AND IT INVERTS R-41/R-43's FRAMING RATHER THAN TRIMMING IT

R-41 said the read makes the card *"decidable one join away"*; R-43 said the narrowing *"reduces the work"*.
**It reduces nothing, because the join is not there.** ⛔ **THE TIMESTAMP CORRELATION IS NOT THE SLOW PATH TO A
SETTLEMENT -- IT IS THE ONLY PATH THAT EXISTS.** Therefore `0.7.0_AE_CloudOps~A`'s disclosed cache limit is
**not a temporary caveat pending better work; it is THE CARD'S PERMANENT EVIDENTIAL CEILING**, and no further
instrument in this estate lifts it.

**RULED:** the card is **NOT "decidable one join away".** It is decidable only as far as a cache-degraded
timestamp correlation allows, **which is exactly as far as it has already been taken**: one external client
domain present around all three 09-22 exposures at 300/600/1800s, two demonstrably-transacting firms absent at
every width up to 30 minutes (the discriminating negative), 09-23 internal at every width. **That IS the
evidence and there is no larger version of it.**

⭐⭐⭐ **AND THE OPERATIVE CONSEQUENCE IS THE SHARPEST SENTENCE ANY SEAT HAS WRITTEN TONIGHT:** *"waiting for a
better measurement before putting it to him would be waiting for an instrument that does not exist ... the
belief that more measurement is coming is itself a reason to defer."* **So this seat's framing was not merely
inaccurate, it was ACTIVELY HARMFUL** -- it implied Andrew should hold for a join that will never arrive, and
the authorizer log expires **2026-10-22** regardless.

### WHAT STANDS, WHAT FALLS, AND WHO WAS RIGHT

**R-31 PARTLY STANDS:** an instrument DID exist, it DOES retain 30 days, and reading it DID produce the
narrowing -- *"reconstructable from nothing"* was genuinely false. **R-31 FALLS on the join:** there is no key
but time, so *"settles the whole card"* was never true. ⛔ **AND `R-21a`'s ABSTENTION WAS MORE RIGHT THAN THIS
SEAT'S CORRECTION OF IT.** `3.0.0_SA_CVO~Z` declined to name a client because *"an IP is not an identity"*;
this seat read that as an evidence gap one query would close. **It was a STRUCTURAL fact about the two planes.**
The abstention is not merely undisturbed -- **its reason is now structural rather than circumstantial, which is
stronger than when it was written.** No firm is named as the client by any seat. The notification decision is
Andrew's by class, unrouted and unchanged, and it is **RIPE NOW** rather than pending.

## R-43 -- ⛔⛔ **THIS SEAT ROUTED THE WRONG LOG GROUP. BOTH EXIST, BOTH RETAIN 30 DAYS, AND A RE-RUNNER WOULD HAVE GOT A CLEAN WRONG ANSWER ON A CLIENT-NOTIFICATION CARD.** THE PERISHABLE HALF IS PRESERVED AND THE CARD IS NARROWED

`0.7.0_AE_CloudOps~A` msg 25388, record `R41_CALL4_AUTHORIZER_READ_20260924.md` @`95858f5cb4`. Read-only
throughout: no egress, no vendor call, nothing changed on any plane. **R-41's routed act is COMPLETE and the
perishable half of call 4 is preserved, which was the entire point of splitting the card.**

### THE DEFECT IS THIS SEAT'S AND IT IS THE MOST DANGEROUS SHAPE OF THE NIGHT

R-41's routing message (msg 25372) named **`/aws/lambda/opalinvest-auth-handler`**. R-31's measurement was
**`/aws/lambda/opal-portal-authorizer`**. ⛔ **BOTH GROUPS EXIST AND BOTH RETAIN 30 DAYS**, so a seat following
the routing text alone queries a real, live, plausible group and gets a **clean wrong answer** on a card that
feeds a decision about contacting a client.

⭐ **THE DISCRIMINATOR WAS AN INCIDENTAL MAGNITUDE NOBODY PLANNED AS A CONTROL.** R-31 mentioned *"3.75 MB"*
as colour. The authorizer reads **3,753,955** bytes; the auth-handler reads **3,160,776**. **So a throwaway
figure in an old record is what identified the right object.** ⭐ **AN INCIDENTAL SIZE, COUNT OR HASH IN A
CITATION IS A WRONG-OBJECT DETECTOR -- the one class Rule 21 states comp-read CANNOT catch** (*"WRONG-OBJECT
errors (comp-read cannot tell you that you handed it the WRONG FILE)"*). **COST:** one magnitude comparison
when two plausible resources exist. **NON-APPLICATION:** a record carrying no incidental magnitude -- there
the only remedy is the positive control.

⚠ **AND THE CAUSE IS NAMED BY THAT SEAT, NOT GUESSED: the auth-handler is the group it had been reading all
session on the UNRELATED SMS thread.** This seat pulled a resource name out of the wrong thread's context
while writing about a different incident. Two live threads, two similarly-named groups, one shared session.

### WHAT THE READ FOUND, AND ITS COVERAGE CONTROL CAME FIRST

Control before any zero was believed: 09-22T00Z-09-24T00Z, **7,046 events**, 1,574 on 09-22 and 5,472 on
09-23, **ten distinct identities across four domains** -- opalinvest.com 1716, inflectionwealth.com 204,
vmwealthpartners.com 54, cottonwoodmail.com 30. **That reproduces R-31's ten-identities-four-firms on an
INDEPENDENT read**, and it establishes that an empty window is a cache artifact rather than an absence.

**THE NARROWING, which only appeared past plausible authorizer cache TTL.** At +/-8s and +/-120s the three
09-22 windows are empty or internal-only -- **which is exactly where R-31 stopped.** At 300s, 600s and 1800s a
single EXTERNAL client domain appears around all three 09-22 exposures: **inflectionwealth.com**.
⭐ **AND THE NEGATIVE ARM IS WHAT MAKES IT EVIDENCE:** vmwealthpartners.com and cottonwoodmail.com appear at
**NO width up to +/-30 minutes around ANY of the three**, while both demonstrably transacted in the same
two-day window (54 and 30 events). **Their absence is informative rather than a coverage hole -- the evidence
would look different if the claim were false.** The 09-23 20:44:34 event is INTERNAL at every width tested,
consistent with R-31.

### ⛔ THIS IS NOT AN ATTRIBUTION, AND R-41a's SPLIT STILL HOLDS

That seat's own limit is adopted verbatim and is not softened here: **an API Gateway authorizer result is
CACHED, so the requester may have been authorized outside even a thirty-minute window and emitted no line at
all. Presence in a window is not a request; absence from one is not an exoneration.** Naming a firm as the
client on this evidence would be precisely the guess **R-21a** was written to prevent, and no firm is named as
the client -- by that seat or by this ruling. **The notification decision stays Andrew's, exactly where R-41
left it.** What changed is only that his half is now answerable on a narrowed candidate set instead of a fog.

**FOR `3.0.0_SA_CVO~Z`, whose join this is:** R-31's shortcut holds -- the exposure was ONE IP, so mapping
that single IP through ANY overlapping authorizer event settles the card. The candidate set it maps against is
narrowed to one external firm for the three 09-22 exposures, and the 09-23 exposure reads internal. **R-21a's
abstention was right on its facts and is not disturbed; the work is reduced, not substituted.**

**TWO HONEST GAPS, both that seat's own disclosures.** (1) The **+1 overlay response is UNDATED** in R-31, so
it is NOT covered by the window table and is not claimed to be. (2) PII: individual addresses were read but
are **not** in the committed record or the message -- firms and counts only, which is what R-31 says the
decision needs; address-level detail stays extractable from the live log until **2026-10-22** if the decision
genuinely requires it.

## R-42 -- ⛔⛔ **I GREPPED AN ANSWER TABLE, LANDED ON ROW 5, AND NEVER READ ROWS 2 AND 3 -- WHICH ANSWERED THE TWO QUESTIONS R-41 THEN ROUTED.** AND `rk-49`'s CARD HAS BEEN ASKING ANDREW THE WRONG QUESTION

`0.0.0_AB_MSTR~Z` msg (09:33Z) and this seat's own read. **Two findings, and the first explains the last
three hours of this file.**

### (1) THE ROUTING IN R-41 WAS UNNECESSARY. BOTH ANSWERS WERE ALREADY IN R-21, TWO LINES ABOVE ONE I READ.

R-41 routed *"who owns the price producer"* and *"who populates 2b chatter_daily"* to `0.0.0_AB_MSTR~Z` as
open seating questions. **Andrew answered both by card ~03:2xZ and this seat recorded both** in R-21's
card-answer table:

```
:1493  | 2 | who populates gold chatter_daily  | 2.0.0_SA_COO~Y, as an explicit AMGT_HARVST scope item...
:1494  | 3 | terminal-box schedule owner       | 0.0.3_BG_BBGTerminal -- it already runs OPAL_BBGTML_daily_pull
:1495  | 5 | Lusha / rk-49                     | WITHHELD for now -- the word buys nothing until hop 4 lands
```

⛔ **THIS SEAT READ `:1495` IN THIS SESSION, WHILE HUNTING THESE EXACT CALLS, AND WALKED PAST THE TWO ROWS
DIRECTLY ABOVE IT.** The mechanism is not carelessness and it is worth naming precisely: the read was a
**GREP FOR `lusha|rk-49`**, and only row 5 contains those tokens. ⭐ **A GREP BY TERM RETURNS THE ROWS THAT
MENTION YOUR TERM AND STRUCTURALLY CANNOT SHOW YOU A TABLE'S OTHER ROWS -- AND A TABLE OF ANSWERS IS EXACTLY
WHERE THE ANSWER TO THE ADJACENT QUESTION LIVES.** Every instrument behaved correctly; the grep had no way to
know it was standing inside an index of decisions.

⭐ **THE MECHANISM, and it is one line: WHEN A GREP HIT LANDS INSIDE A TABLE, READ THE WHOLE TABLE.**
**COST:** one adjacent-lines read, no re-search. **NON-APPLICATION:** a hit in ordinary prose, where the
neighbouring lines are not answers to sibling questions. This single check would have caught **three** of
this session's errors -- the price pull (R-41a), the chatter owner and the terminal owner (here).

### (2) `rk-49` HAS BEEN CARDED TO ANDREW AS THE WRONG QUESTION, AND THE ORDER SAYS SO ITSELF.

Three accounts of one blocker have been in circulation, all written by this seat:

| source | what it says blocks `rk-49` |
|---|---|
| `AMGT_CLOSE_CONDITION_20260924.md` | *"an external vendor API needs his explicit per-use word"* |
| R-21 `:1495` | *"the word buys nothing until hop 4 lands"* |
| **the ORDER, `TO-AMGT-rk-49` `:300`** | **"stays HELD, and its status stays open UNTIL ANDREW SAYS THE KEY IS ROTATED"** |

⛔ **THE ORDER WINS, BECAUSE THE ORDER IS THE ARTIFACT THAT MOVES.** Its own `:300` and this file's `:117-118`
agree: the ask is **a factual statement that the Lusha key has been rotated** -- not a grant of permission.
⭐ **THOSE ARE DIFFERENT QUESTIONS AND THE SECOND IS FAR EASIER TO ANSWER.** A card asking *"may we call
Lusha?"* invites a policy decision he has already itemised as withheld; a card asking *"has the key been
rotated?"* invites a one-word fact. **A card that asks the wrong question gets no answer, and the silence
reads as HIS delay rather than as this seat's mis-framing.**

**RULED:** the `rk-49` card is **RE-FRAMED** to the key-rotation question, and the close condition's exception
row for `rk-49` is corrected from *"HELD BY LAW ... needs that word"* to **"HELD pending Andrew's statement
that the Lusha key is rotated"**. It stays RESERVED -- ⭐ **and on a STRONGER citation than R-41 gave it: not
the generic vendor NEVER line, but Andrew's own all-vendors grant ITEMISING Lusha as WITHHELD by name
(R-21 `:1495`).** An exception named inside the grant that would otherwise cover it is the strongest form of
reservation this fabric recognises.

### WHAT IS OWED AND BY WHOM, AFTER THIS

`0.0.0_AB_MSTR~Z` spawned `0.0.3_BG_BBGTerminal` (LIVE PID 16952, 09:33Z) after measuring it **NOT
REGISTERED since 2026-09-23 11:30-11:50Z with R-21 unread in its inbox since 03:17Z**, and correctly states
that **the MANDATE is this seat's and did not exist.** It does now:
`BG_BBGTERMINAL_PRICE_PRODUCER.md`, beside this file -- the granted authority, R-21b's mechanism constraint as
the grading criterion, the **2026-09-29** expiry, B1-B4, and the NEVER-2 ledger requirement for the first
scheduled fire. **2b** needs no seating either; it is a **mandate update** to `COO_Y_HARVST.md`, not a routing.

⚠ **AND THE HONEST ACCOUNTING OF THE COST: six hours.** Andrew answered the terminal-box owner at ~03:2xZ.
That seat sat dark with the answer unread in its own inbox, this seat re-asked the settled question at
~09:2xZ, and the artifact that unblocks it -- a mandate R-21 explicitly said *"follows from this seat"* --
was written at ~09:4xZ against a **five-day** expiry. No gate failed and nothing alarmed, which is R-41a's
point about over-restriction arriving as silence.

## R-41 -- ⛔⛔ A CARD'S **RESERVED HALF** HAS BEEN RESERVING ITS **ADJUDICABLE PARTNER**. FOUR OF SIX CARDS AT ANDREW SPLIT, AND TWO INSTRUMENTS ARE AGING BECAUSE OF IT

**The standing instruction on this fabric is *"All open-calls on sitez fabric to be adjudicated by
`1.0.0_SA_CTO~Z` this session."* This seat has spent several ticks reporting "1 RESERVED in scope" while
SIX cards sat at Andrew.** `/self-drive`'s own ALL-RESERVED TELL says a uniformly-reserved queue is
presumptively an instrument artifact, and Andrew named this defect verbatim: *"somehow every single open call
falls under 'reserved' versus adjudicable ... it renders the skill useless if it cant get calls adjudicated
... In almost every single case i have ever seen i agreed with the rec outright."*

⛔ **BUT THE DEFECT IS NOT "I CALLED EVERYTHING SOVEREIGN." IT IS NARROWER, AND WORSE BECAUSE IT SURVIVES
THE CITATION TEST.** Each of these cards bundles **TWO ACTS**: one whose closure a NEVER line genuinely
reserves, and one that is nobody's but this seat's or `0.0.0_AB_MSTR~Z`'s. **The citation was tested against
the CARD and it passed -- because one of its acts really is his. So the adjudicable act inherited a
reservation it never earned.** ⭐ **A CALL'S RESERVED HALF DOES NOT RESERVE THE CALL.** Same shape as
NEVER-1's *"a sign-off names the act's BLAST RADIUS, never the producer's decision"*, and same shape as
R-40's *presence of a symbol is not exercise of a path*: the test was run one level above the thing it
governs.

⭐ **THE MECHANISM, and it costs one column: SPLIT EVERY CARD INTO ITS ACTS AND TEST THE CITATION AGAINST
EACH ACT.** A card is not a unit of authority; an act is.

| card | the act a NEVER genuinely reserves | the act that was never his | ruled |
|---|---|---|---|
| `rk-49` Lusha | the vendor call itself -- *"NEVER call an external vendor API without Andrew's explicit per-use word"* | none; the card is atomic | **RESERVED, whole.** The only close-condition exception he alone clears |
| Lead Panel price | ~~the **price PULL**~~ **NOTHING -- see R-41a; the pull is GRANTED** | the **producer's OWNER and RUN** (CRO brief item 4) -- a SEATING question | **ROUTED WHOLE** to `0.0.0_AB_MSTR~Z`; nothing on this card is his |
| call 4 (client notification) | the **notification decision** -- outward-facing, client-relationship, his by class | the **authorizer-log READ** that names the client -- a read-only query on Opal's own log | **SPLIT.** R-31 already ruled it decidable one join away and nobody ran the join |
| `2b` gold chatter table | **nothing.** No NEVER names it | populating an UNOWNED upstream gold table -- an OWNERSHIP question | **RE-ROUTED** to `0.0.0_AB_MSTR~Z`. It was never Andrew's |
| D12 SMS end state | **nothing.** The moratorium governs BUILDING a notifier, not retaining an existing guard | the keep-or-remove decision, with this seat's rec already written | **ADJUDICATED: KEEP** |
| SMS event destination | **nothing** | defer-or-build, and `0.7.0_AE_CloudOps~A` withdrew the premise that made it necessary | **ADJUDICATED: DEFERRED** |

**TWO OF THE SIX ARE ADJUDICATED HERE AND NEITHER NEEDED HIM.** D12 SMS end state: **KEEP** the guard --
it is `null`-returning at `sms.ts:81` under `ALLOW_UNVERIFIED` before the allowlist, the measured record is
13 of 14 codes ACCEPTED and 0 FAILED, and an accepted code is positive evidence of correct delivery rather
than absence of evidence of harm. Removing a guard on that record buys nothing and loses the arm. SMS event
destination: **DEFERRED** -- on that AE lane's own correction, the application already logs the destination
per message at 30-day retention, so a configuration set would add carrier-side DELIVERY confirmation, a
different and weaker question than the one that mattered.

⛔ **AND THE COST IS NOT HYPOTHETICAL -- IT IS BEING PAID ON A CLOCK, WHICH IS WHY THIS IS AN INCIDENT
RATHER THAN AN EXPOSURE UNDER RULE 22's NEGATIVE MIRROR.** Both split cards carry an **EXPIRING
INSTRUMENT**, and both expiries sit on the act that was never Andrew's:
- the Lead Panel price fallback stops finding the 2026-09-15 generations on **2026-09-29 -- five days** --
  after which a baseline cannot distinguish *"the producer never ran"* from *"the producer ran and found
  nothing"*, and the act that prevents that is SEATING a producer owner;
- the authorizer log carrying email / tier / role / `allowedFirmIds` retains **30 days, expiring
  2026-10-22**, and the act that preserves the answer is a READ.
**A reservation that parks a perishable read behind a non-perishable decision converts a recoverable
question into an unanswerable one, on a timer, silently.**

**WHAT DOES NOT CHANGE, stated so this ruling is not read wider than it is.** No NEVER is lifted and no
vendor call is authorized: the Lusha word and the Lead Panel price pull remain his, un-narrowed. The client
notification remains his -- ⭐ **and splitting the card is what makes his half ANSWERABLE, since R-31 already
measured that the decision turns on an identity the read supplies.** This seat is NOT deciding whether to
notify. ⚠ **Nor does this ruling relay his word wider or narrower** -- it touches no word of his; it corrects
this seat's own classification of acts he was never asked about.

## R-41a -- ⛔⛔ R-41 CALLED THE PRICE PULL RESERVED. **ANDREW GRANTED IT TWICE AND I RECORDED BOTH.** MY ERROR DIRECTION FLIPPED, AND THE RESTRICTIVE ONE IS INVISIBLE

`4.0.0_SA_CRO~Z` msg 25377, information only, no act asked. **It is correct and R-41's reserved list is
wrong.** ⛔ **THE FALSIFIER IS A RULING TWENTY-SIX NUMBERS EARLIER IN THIS SAME FILE, WHOSE HEADING SAYS THE
OPPOSITE OF WHAT R-41 CLAIMED -- AND THIS SEAT READ THAT HEADING IN THIS SESSION WHILE HUNTING FOR THESE VERY
CALLS.**

**R-15** @`884475c5a1`: *"ANDREW GRANTS EGRESS. The §5 refusal is **resolved BY HIS WORD**"*, Andrew-direct
~02:4xZ VERBATIM *"you have egress for whatever calls you want"*, and its recorded narrow read authorizes
**"(i) the price pull"** by name. **R-21** @`b390c36444`, ~03:2xZ VERBATIM: *"all recs approved, and you have
all the egress you want for vendors. Only thing I'd note is that the pull should be deterministic/scripted in
nature like the existing pull, i do not like the idea of relying on an agent for..."*

**SO THE PULL'S AUTHORITY IS GRANTED AND WHAT BINDS IS THE MECHANISM, WHICH R-21 ALREADY MADE A GRADING
CRITERION (R-21b).** Nothing on the Lead Panel price card is Andrew's. It is **ROUTED WHOLE** to
`0.0.0_AB_MSTR~Z` -- owner and run, under R-21's deterministic-scripted-producer constraint, before the
2026-09-29 fallback expiry. **The five-day clock was parked behind a call answered twenty hours earlier.**

⛔ **HOW I GOT IT WRONG, AND IT IS R-41's OWN DIAGNOSIS TURNED ON R-41.** There are two questions and I
answered the first while reporting the second: *"does the vendor NEVER line APPLY to this act?"* -- **YES,
and my earlier refusal of the brief's "no vendor word needed" was correct on exactly that ground.** *"Has
the word been GIVEN for this act?"* -- **YES, twice.** A rule applying and a word being absent are different
facts, and I carried the first forward as though it settled the second. ⭐ **THE TEST RAN ONE LEVEL ABOVE THE
THING IT GOVERNS -- which is the sentence R-41 itself is built on.**

⭐⭐ **AND THE GENERALISATION IS NEW, BECAUSE MY ERROR DIRECTION FLIPPED.** Earlier this session this seat
banked *"an existing narrow producer still needs Andrew's per-use vendor word -- my error ran in the
PERMISSIVE direction."* This one runs **RESTRICTIVE**: I withheld an act he had authorized. ⛔ **A SEAT THAT
ONLY EVER AUDITS ITSELF FOR OVER-PERMISSIVENESS WILL NEVER CATCH AN OVER-RESTRICTION -- AND OVER-RESTRICTION
IS STRUCTURALLY INVISIBLE, BECAUSE NOTHING FAILS. THE WORK SIMPLY DOES NOT HAPPEN, ON A CLOCK, AND EVERY
GATE READS GREEN.** The permissive error announces itself with a breach; the restrictive one announces
itself with nothing at all, which is why it needed a peer to say it out loud. **COST: one question per
reserved act -- *has the word already been given?* -- asked of the record, not of memory. NON-APPLICATION: an
act never put to him, where there is no word to have missed.**

⭐ **WHAT R-41 GETS RIGHT AND THIS STRENGTHENS:** the reserved list drops from three acts to **TWO** --
`rk-49` Lusha's vendor call and the call-4 client notification -- which is the direction R-41 argues. Its
ROUTING was right on every card; only its reservation of this one act was wrong. And `4.0.0_SA_CRO~Z`
offered the correction with *"if a later word narrowed it, this seat has not seen it and withdraws the
point"* -- a falsifiable form, which is why it was cheap to check rather than cheap to dismiss.

## R-40 -- ⛔⛔ PRECONDITION (2) IS WITHDRAWN AS VERIFIED. I GRADED IT ON A STRING CENSUS; AN IN-MEMORY BUILD FALSIFIES IT, AND THERE IS A **FOURTH** PRECONDITION

`2.0.0_SA_COO~X` msg 25355, on CLOUD @`54b277a086`. **This seat graded precondition (2) -- "the two producers
become ONE on CLOUD" -- as MET, on the strength of TEN `universe/v1` references in CLOUD's `crosswalk.py`.
That grade is WITHDRAWN. The references are real and the precondition is FALSE.**

**WHAT THE RIGHT INSTRUMENT FOUND.** `crosswalk.build_crosswalk("2026-09-24")` run IN MEMORY on CLOUD returns
`input_names 89, records 96, MEASURED 36` -- the 36-shape, **not** 194. At the bytes: the universe/v1 source is
an **EXPLICIT ARGUMENT**, `build_crosswalk(as_of, ..., identity_universe=None, identity_source=None)`
(`crosswalk.py:644-646`). The **CLI** loads and passes it (`:1171-1172`). But
`add_security._persist_registration_and_pool` calls `crosswalk.build_crosswalk(as_of, registrations=rows,
registrations_source=reg_path)` (`add_security.py:175`) **with no identity universe**, and `main`'s collision
check calls `build_crosswalk(args.as_of)` bare (`:392`). ⛔ **SO THE CORRECTED FIRE -- UNIFIED BUILDER,
BATCHED TO ONE PUT, PAIR SIGNED -- WOULD STILL REPLACE THE 194-KEY OBJECT WITH 36+20. THE SAME INCIDENT WITH
ONE PUT INSTEAD OF TWENTY.**

**WHY MY GRADE WAS WRONG, AND IT IS THE THIRD INSTANCE OF ONE CLASS IN ONE HOUR.** A census of the token
`universe/v1` answers *does this file MENTION the source*. The claim it was used to support was *does
add_security's CALL PATH consume it*. ⭐ **PRESENCE OF A SYMBOL IS NOT EXERCISE OF A PATH** -- Rule 22a's own
instruction for code, *"diff deployed bytes against the BUILD INPUT, never by filename"*, arriving from the
source direction. **And this seat NAMED the gap in its own precondition text (*"a string census is not a
build"*) and then graded the precondition anyway.** Writing the caveat is not running the control.
⚠ It joins R-39's token inversion and R-39a's two-axis glob: **three measurements this hour, one family --
a real instrument aimed one level off the claim.**

**THE FOURTH PRECONDITION, RULED.** `_persist_registration_and_pool` **and** the `:392` collision check load
and pass the retained universe/v1 identity input exactly as the CLI does (`load_identity_universe(None)` ->
latest retained), so an induction re-mint **ADDS** its registrations to 194 rather than replacing 194 with 36.

**ACCEPTANCE IS COO~X'S OWN AND IS ADOPTED VERBATIM, BECAUSE IT IS A DISCRIMINATOR AND NOT A COUNT:** an
in-memory `build_crosswalk` **through add_security's own path** prints `MEASURED 194` on the current inputs
BEFORE any registration is added, and `194 + N` after N fake registrations -- **with a negative control that
withholds the universe argument and reads 36.** The negative arm is what makes the 194 an answer rather than
an oracle, and it is the arm this seat's string census had no way to express.

**PLACEMENT: ONE CELL ON ONE SURFACE, NOT TWO.** Both clauses -- the one-put-per-run batching (R-38's third
precondition) and this universe-passing clause -- land on `add_security` / `crosswalk.py`, which is
`2.0.0_SA_COO~Z`'s surface. They are ONE cell. ⭐ **AND `2.0.0_SA_COO~Z`'s OWN PLACEMENT CALL IS CONFIRMED:
the Peers closer track (`closer/amgt-peers-z-20260924`), NOT round 38's enrichment list.** Round 37 is
mid-flight with its decomposition FROZEN and a presentation-only rectangle; parking a `lib/` edit in a
canonical round to make it look tidy would either break the freeze or delay the fix a whole round. The closer
track already carries the universe/v1 producer, so the fix lands where its own dependency lives.

⛔ **TWO DEFECTS IN THIS RULING'S OWN DELIVERY, ANNOTATED FORWARD RATHER THAN EDITED AWAY.**
**(a) R-40 AND R-39a SHARE COMMIT `5c19c11ed8`, WHOSE SUBJECT NAMES ONLY R-39a** -- both edits were in the
working tree when the merge cleared. A citation of R-40 by commit lands on a subject that does not mention
it. Same shape as this file's own header note about `a8a62f4f5c`, and recorded here for the same reason.
**(b) THE BROADCAST OF THIS RULING (msgs 25356-25359) CARRIED A FALSE ATTRIBUTION.** It said the commit was
blocked behind *"`0.0.0_AB_MSTR~Z`'s live drain of `wk-AMGT_RESAPP-132`"*. **It was `2.0.0_SA_COO~Z`'s drain
(`a8aa8bff17`).** ⭐ **`.git/MERGE_HEAD` HELD `65deef80be`, WHICH IS THE WORKER'S OWN L7 COMMIT -- SO THE
MERGE STATE NAMES THE BRANCH, NEVER THE ACTOR MERGING IT**, and this seat converted "whose branch" into
"whose act". The drainer is read off the RESULTING merge commit, and while the merge is still open the
honest answer is *owner UNREAD*. Caught by `0.0.0_AB_MSTR~Z`, which named it the same class as a pusher
attribution it corrected the previous night. ⚠ **A SIXTH INSTANCE THIS HOUR OF ONE FAMILY, AND THE FIRST
THAT TOLD THREE OTHER SEATS A FOURTH WAS HOLDING THEM UP.**

**THE RE-FIRE STAYS HELD, and the count is now FOUR: (1) rollback verified -- MET. (2) one producer on CLOUD
-- WITHDRAWN, re-graded NOT MET. (3) write_pool one put per run -- OPEN, taken. (4) the universe input passed
on add_security's path -- OPEN, same cell.** `2.0.0_SA_COO~X`'s refusal of its own re-fire pending both clauses
is CORRECT and is ratified: that seat has now twice refused an act it had authority to take, on its own
pre-flight measurement, and both refusals were right.

## R-39 -- THE CLOSE CONDITION DEMANDS A NUMBER NO INSTRUMENT CAN READ. THREE ATTEMPTS, THREE CONFIDENT WRONG ANSWERS, ONE OF THEM INVERTED

`AMGT_CLOSE_CONDITION_20260924.md` @`1ccf401cfd`, written by this seat, ends: *"THE SUBTRACTION IS PRINTED,
NOT ASSERTED -- the closing analysis states N of 49 REALIZED, names each exception with its reason, and the
two must SUM TO 49."* This seat then tried to measure N and **failed three times in a row, each time
producing a real number with a real denominator.**

**ATTEMPT 1 -- WRONG GRAIN.** A per-FILE co-occurrence join (does this file contain an `FWD-` id AND a grade
token) over 3,202 files returned 170 files, the top two being the PRDs themselves at 30 and 19 ids. Read as
*"the PRD carries the grades."* It does not. **A FILE-LEVEL JOIN CANNOT SUPPORT A PER-ROW SENTENCE**, and the
hits were prose: *"UNREALIZED at this bump"*, *"makes `FWD-17` gradeable"*.

**ATTEMPT 2 -- WRONG TOKEN, AND THE ERROR INVERTED A GRADE.** Re-run at line grain with an 80-character
proximity window, matching `REALIZED|NOT_REALIZED|PARTIAL`. It returned **3 of 49 REALIZED** and this seat
nearly published it. The round-11 analysis says, in bold, `**FWD-8 is NOT REALIZED.**` -- **with a SPACE.**
The regex tested `NOT_REALIZED` with an UNDERSCORE, found no match, then matched the substring `REALIZED`
inside `NOT REALIZED` and recorded FWD-8 as **REALIZED**. ⛔ **THE INSTRUMENT DID NOT MISS THE GRADE. IT
REPORTED THE OPPOSITE OF WHAT THE FILE SAYS, IN THE DIRECTION THAT FLATTERS THE CLOSE.**

**THE MEASURED SIZE OF THAT HAZARD**, word-boundary census over 604 AMGT `.md` files: **171 grade mentions in
FOUR token forms** -- `REALIZED` 129, `NOT_REALIZED` 21, `NOT REALIZED` 19, `UNREALIZED` 2. Under a
word-boundary positive match `\bREALIZED\b`, the underscore and `UN-` forms are correctly excluded (`_` and
`N` are word characters) and **the 19 space-separated ones invert.** So the vocabulary is not merely
inconsistent, it is inconsistent in the one way that converts a negative grade into a positive one.

**ATTEMPT 3 --** ~~**THE CARRIER IS ABSENT ON ONE WHOLE PROJECT.** `AMGT_RESAPP` has **35** `ROUND_ANALYSIS`
files; `AMGT_CORPUS` has **ZERO**, under any name, anywhere in its tree. So 19 of the 49 outcomes have no L10
grade carrier at all -- and **that is this seat's own debt**, because L10 is the CTO's step.~~
⛔ **WITHDRAWN BY R-39a BELOW, WHICH THIS SEAT WROTE FOUR MINUTES AFTER COMMITTING THE SENTENCE.**

**RULED, three parts.**

**(1) N IS UNMEASURED AND IS NOT MACHINE-MEASURABLE FROM WHAT EXISTS.** The grades live in free prose, in
bold sentences, across 35 documents, in four token forms. No published document has yet quoted an N, so by
Rule 22's negative mirror this is an **EXPOSURE, NOT AN INCIDENT** -- the discriminator being that the close
condition states the requirement and no closing analysis has been written against it. Nothing is re-opened.

**(2) THE GRADE TABLE IS THE CLOSING ANALYSIS'S FIRST SECTION, AND IT IS NOT A PRD EDIT.** Rule 27 freezes
the spec mid-round and both projects are EXECUTING, so appending a grade column to either ENDPOINT fence is
refused on its own terms. The table lands in the L10 closing analysis: one row per outcome, `FWD-<n>` and
**one controlled token from `{REALIZED, NOT_REALIZED, DEFERRED, HELD}`** -- underscored, never spaced, never
`UNREALIZED` -- plus the evidence coordinate. The controlled vocabulary is the whole mechanism: the
uncontrolled one has already fooled the seat that wrote the condition it serves.

**(3) THE 49 DENOMINATOR STANDS, AND IS NOW VERIFIED ON A SECOND INSTRUMENT.** Not from the headers'
self-declared `endpoint_outcomes` but by extracting distinct ids from the PRD bodies at HEAD: RESAPP 30
distinct, max 30; CORPUS 19 distinct, max 19 -- both contiguous, no gaps, no duplicates, 49 total. That is
the one number this seat published about the close, and it survives an instrument that does not trust the
header.

## R-39a -- ⛔⛔ R-39's ATTEMPT-3 CLAIM IS WITHDRAWN. THE CARRIER EXISTS; IT IS IN A DIFFERENT HOME UNDER A DIFFERENT NAME, AND THAT IS THE REAL REASON N IS UNMEASURABLE

**A FOURTH DEFECT, IN THE RULING THAT WARNS ABOUT THE FIRST THREE, COMMITTED TO THE RECORD AT `54b277a086`
BEFORE THIS SEAT CAUGHT IT.** R-39 said `AMGT_CORPUS` has ZERO L10 analyses "under any name, anywhere in its
tree" and called it this seat's own debt. **FALSE.** `2.0.0_SA_COO~X` cut round 2 *"on the round-1 analysis
@`031c3a3a3e`"* -- and that commit's own stat names the file:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_CORPUS_ROUND1_ANALYSIS_20260924.md`, 118 lines, **written by
this seat.**

**THE CENSUS MISSED IT ON BOTH AXES AT ONCE.** It globbed
`org/missions/D5/AMGT/AMGT_CORPUS/**/*ROUND_ANALYSIS*` -- the file is neither in that DOMAIN (it lives in CTO
deliverables) nor of that NAME (`ROUND1_ANALYSIS`, digit infixed, not `ROUND_ANALYSIS`). ⛔ **TWO
INDEPENDENT MISSES, SO FIXING EITHER ONE ALONE WOULD STILL HAVE RETURNED ZERO** -- which is why the zero felt
robust. And the sentence said "under any name, anywhere in its tree": a universal quantifier whose instrument
could only ever answer one name in one tree.

**MEASURED UNSCOPED, 42,116 tracked files, both axes dropped:**

| project | analysis files | home | name form |
|---|---|---|---|
| `AMGT_RESAPP` | **36** | `org/missions/D5/AMGT/AMGT_RESAPP/ledger/` | `ROUND_ANALYSIS.round<N>.md` |
| `AMGT_CORPUS` | **1** | `org/tier1_exec/1.0.0_SA_CTO/deliverables/` | `AMGT_CORPUS_ROUND<N>_ANALYSIS_<date>.md` |

**CORPUS IS AT 1 OF 1 AND OWES NOTHING.** Round 1 is its only closed round; round 2 is EXECUTING. There is no
debt, and R-39's "this seat's own debt" was a self-accusation manufactured by a bad glob.

**RULED, and it is a BETTER finding than the false one it replaces.** ⭐ **THE TWO PROJECTS IN ONE MACRO KEEP
THEIR L10 ANALYSES IN DIFFERENT HOMES UNDER DIFFERENT NAME FORMS.** That -- not a missing carrier -- is the
mechanical reason `N of 49` cannot be read by any instrument: the grades are in free prose (R-39), in four
token forms (R-39), across two incompatible carrier conventions (here). **The closing analysis therefore
NAMES ITS OWN CARRIER PATH for each project explicitly rather than globbing for it**, and R-39 part (2)'s
grade table is the single place both projects' 49 rows appear together.

⛔ **AND THE STANDING LESSON IS THE FOURTH ERROR ITSELF, NOT ITS CONTENT.** Four attempts at one number:
wrong GRAIN, wrong TOKEN, then wrong DOMAIN and wrong NAME simultaneously. Each returned a confident result
with a real printed denominator. **A ruling about measurement error is not protected from measurement error by
its subject** -- the only thing that caught the fourth was a PEER'S CITATION in an inbox message naming an
artifact this seat had written itself and then censused out of existence. `2.0.0_SA_COO~X` gets the catch.

**WHAT SURVIVES R-39 UNTOUCHED:** the grade-token inversion and its 171-mention four-form census; the
`NOT REALIZED`-contains-`REALIZED` mechanism; parts (1), (2) and (3) of its RULED section; and the verified
49 denominator. Only attempt 3's factual claim and its debt conclusion fall.

**WHAT THIS COSTS AND WHAT IT DOES NOT CLAIM.** ⛔ **UNGRADED IS NOT NOT-REALIZED.** 46 outcomes lacking a
grade says nothing about whether the work is done; it says the grade has not been written. The order counts
this seat has been reporting -- 182 of 201 complete on RESAPP, reading as 91 percent -- measure WORK DONE,
and the close condition measures ENDPOINT MET. Both numbers are real, they are not the same question, and
quoting the comfortable one against a condition written on the other is the error this ruling exists to stop.


## R-38 -- ⛔⛔ A **SECOND DEFECT UNDER THE FIRST**: A PER-RECORD PUT LOOP ON A SERVED KEY. "ONE PRODUCER" DOES NOT FIX IT

`3.0.0_SA_CVO~Z`, msg 25336, corroborated by `2.0.0_SA_COO~X` on a second instrument (boto3
`list_object_versions` + per-version `head_object`) and by `2.0.0_SA_COO~Z`'s own enumeration. **Three
instruments, one answer.**

⛔ **IT WAS NOT ONE OVERWRITE. IT WAS TWENTY WRITES IN EIGHTEEN SECONDS.** 21 versions of the key: ONE signed at
03:32:47Z, and **TWENTY between 08:02:37Z and 08:02:55Z** with sizes climbing **monotonically** -- 204,711 ·
206,139 · 207,592 · 209,042 · 210,458 · 211,838 · 213,346 · 214,766 · 216,254 · 217,698 · 219,080 · 220,492 ·
221,874 · 223,244 · 224,624 · 226,306 · 227,686 · 229,146 · 230,542 · 231,910. **~1.4 KB per write, about one per
second.** `write_pool` runs INSIDE each `add_security` call.

⛔⛔ **RULED: THIS IS A SECOND, INDEPENDENT DEFECT, AND R-37's "ONE PRODUCER BEFORE ANY RE-FIRE" IS NECESSARY BUT
NOT SUFFICIENT.** That seat's sentence is the operative one: *"even the CORRECT builder, running correctly through
the closer branch's `crosswalk.py`, would rewrite the served key N times on every run."* For the seconds of any
run, **a reader gets a PARTIAL crosswalk truncated at wherever the loop had reached** -- which **is** the
ASML/AAPL UNRESOLVED symptom, and it would **RECUR ON EVERY LEGITIMATE RE-FIRE rather than being spent once.**

⭐ **AND I SHOULD HAVE ASKED THE QUESTION THAT FINDS THIS, BECAUSE IT IS BANKED AT THIS SEAT:** *"the SECOND of two
stacked blockers is invisible to every instrument aimed at the route -- ask 'if blocker A vanished now, what would
change?'"* **If the two-writer problem vanished, the put loop would still break the served key on every run.** R-37
aimed its whole remedy at the writer count and never asked what remained.

## THE THIRD PRECONDITION ON THE RE-FIRE

**`write_pool` is called ONCE PER RUN with the complete record set, never once per name.** Until that holds, a
re-fire through the unified builder is still twenty successive served writes with a partial-read window in the
middle. ⚠ **THIS IS A CODE DEFECT, NOT A PROCESS ONE, AND NO PAIR MAKES IT SAFE** -- a never-widen half can name
twenty puts honestly and the partial-read window still exists between them.

**WHOSE SURFACE:** `add_security._persist_registration_and_pool` drives the loop and `crosswalk.write_pool`
(`lib/research/identity/crosswalk.py:998`) performs the put. `add_security` is **`2.0.0_SA_COO~Z`'s** surface
(R-16 V2's *"through `add_security`"*), so the batching change is that lane's or a coordinated cell -- **not
`2.0.0_SA_COO~X`'s to take**, exactly as that seat concluded when it DEFERRED item 3 rather than bypassing the seam.

⭐ **THE THREE PRECONDITIONS ARE NOW ORDERED AND NONE IS SKIPPABLE:** (1) the rollback VERIFIES on size + ETag +
sha + three invokes; (2) the two producers become ONE on CLOUD; (3) **`write_pool` batches to one put per run.**
**The re-fire's never-widen halves then FIRST print the writer count of the key -- two known -- which is
`2.0.0_SA_COO~X`'s own adoption of NEVER-1's instruction and is recorded as such.**

## ⭐ THE CONTAINMENT MEASUREMENT, WHICH IS THE GOOD NEWS AND WAS RUN AS A CONTROL

`crosswalk/v1/2026-09-22.json` is **UNTOUCHED at 203,327 bytes**, `LastModified 2026-09-22T17:21:29Z` --
**byte-length identical to the R-23 read.** ⭐ **So the blast radius holds on the pre-existing key and ONLY the
09-24 key moved.** The 194 peer objects are untouched, there are **0 delete markers**, and every noise version
stays addressable by `VersionId`. **The damage is one key, one day, fully reversible from the bucket's own
history.**

⚠ **AND THE OVERWRITE IS STILL LIVE AS OF THAT MEASUREMENT** (latest `dcPADuzd20vImHdtk4gq0k1H`, 231,910 b,
sha256 `037375929c02e26d`, 08:02:55Z) -- **the restore had not landed when this was written, and this ruling does
not assume it has.**

## ⭐ WHAT THE THREE SEATS DID, RECORDED BECAUSE IT IS THE REASON THIS IS RECOVERABLE

`2.0.0_SA_COO~Z` found the incident, measured it end to end, and **recorded its own half's undercount of writers
against itself.** `2.0.0_SA_COO~X` **held the re-fire, owned the before-state error in row `AMGT_CORPUS-Z-S13`
(ARMED, itself as `disarm_owner`), corroborated the enumeration on a second instrument, and REFUSED item 3** rather
than bypass another lane's seam. `3.0.0_SA_CVO~Z` **verified the signed sha ON FETCH rather than from a listing**
and found the defect underneath. ⛔ **Every one of the three reported a fault of its own in the same message as its
measurement, and the only grade that had to be withdrawn was mine.**

## R-37 -- ⛔⛔ R-36 IS WITHDRAWN. IT IS AN **INCIDENT**, AND MY GRADE RESTED ON A PEER'S BEFORE-STATE THAT MY OWN R-23 FALSIFIED

`2.0.0_SA_COO~Z`, msg 25330. **R-36's EXPOSURE grade is WITHDRAWN.** GO given on the same-window rollback, re-fire
HELD, at 08:2xZ -- **sent before this record was written, because a record arriving after a second overwrite is
worthless.**

**THE FACT R-36 MISSED: `crosswalk/v1/2026-09-24.json` EXISTED BEFORE THE FIRE.** `2.0.0_SA_COO~Z` published it at
03:32:47Z **under the never-widen pair** (COO @`4c7d0b2e7c`, **CTO @`429efcdf30` -- THIS SEAT'S OWN SIGNED HALF**):
523,207 bytes, `document-sha256 9bd953b9...`, **MEASURED 194**. The fire replaced it with **231,910 bytes**,
`records 116`, at 08:02:55Z.

**MEASURED SERVED EFFECT, on the deployed API at unchanged `CodeSha256`:** `ASML_US_Equity` **UNRESOLVED, basis
absent** (was MEASURED/absent/SERVED at 03:34Z) · `AAPL_US_Equity` **UNRESOLVED** (was derived 10 SERVED) ·
`CAT_US_Equity` still MEASURED derived 12. ⛔ **The hop-4 strand is BACK on the served route for the 158 keys
`universe/v1` registered, and R-24's route-layer PASS does not hold on the served stack.** **INCIDENT by Rule 22's
negative mirror: the defect's own signature -- served UNRESOLVED on a key that read MEASURED -- returns NON-ZERO.**

## ⛔ WHY MY GRADE WAS WRONG, AND IT IS THE WORST INSTANCE OF ONE CLASS TODAY

**I ACCEPTED A PEER'S BEFORE-STATE AS MEASURED.** msg 25324 said *"there was no 09-23 or 09-24 pool before; the
prior latest is 2026-09-22"*, and R-36 restated it as *"the object is NEW, and the prior latest was 2026-09-22."*
⭐ **Its denominators were REAL NUMBERS measured against THE WRONG BEFORE-OBJECT, which is exactly why they read as
evidence** -- `records 96 -> 116`, `MEASURED 36 -> 36`. A wrong-domain measurement arrives with a printed number.

⛔⛔ **AND THE FALSIFIER WAS IN MY OWN RULING HISTORY. I VERIFIED THAT OBJECT MYSELF AT R-23**, on an independent
instrument, hours earlier -- 523,207 bytes, MEASURED 194 -- `3.0.0_SA_CVO~Z` graded it PASS at R-24, and **I signed
the CTO half that published it.** ⭐ **So I did not lack the fact. I failed to bring my own prior measurement to a
peer's claim about the same key.** A restatement I could have falsified from my own record is worse than one I
could not, and the cheap guard is the one I keep writing down: **when a peer states a BEFORE-state on a key you
have touched, read your own prior measurement of that key before grading.**

## THE MECHANISM: TWO WRITERS OF ONE KEY, AND NOBODY'S BYTES WERE WRONG

`2.0.0_SA_COO~Z`'s producer (`crosswalk.py` with `universe/v1` as a SECOND registration source, 36 -> 194) lives on
`closer/amgt-peers-z-20260924`, **not on CLOUD**. The fire ran CLOUD @`a419df8f9d`, whose `build_crosswalk` knows
only `registrations.json` (8 rows at HEAD) -> 36 MEASURED. ⭐ **So `2.0.0_SA_COO~X` wrote CORRECTLY BY CLOUD'S
BYTES; the object it replaced was minted by a producer CLOUD does not have yet.** `write_pool`'s `IfMatch` branch
fired on a changed digest -- **the branch the CTO half's pre-flight condition existed to guard on the FIRST seat's
put, while the second writer had no pair at all.**

⛔ **THREE SEATS CONTRIBUTED, AND ONE OF THEM IS ME.** A never-widen half that **counted ONE writer** where NEVER-1
says *"FIRST COUNT THE WRITERS ... and N is a number the half PRINTS"* (recorded by `2.0.0_SA_COO~Z` against
itself) · a fire from a branch lacking the producer · **and a CTO grade built on an unverified before-state.**
⭐ **The seat whose signed object was destroyed is the one that found the incident, measured it end to end, and
recorded its own share of the cause.**

## THE RULING, THREE PARTS

**(1) HOLD THE RE-FIRE.** R-36's *"RE-MINT: YES"* is **rescinded** -- a re-mint from CLOUD's builder overwrites the
key again. The BUILD of amendment 2 is not held; only the pool write.

**(2) GO ON THE SAME-WINDOW ROLLBACK, AND NO NEW PAIR IS NEEDED.** The existing pair NAMES this key and its
rollback, so a restore to the bytes that pair signed **is that pair's rollback leg being exercised**, not a new
move. ⛔ **Requiring fresh sign-off to undo an unauthorised overwrite would leave the served route broken while
paperwork happened, and CLAUDE.md s.2 forbids manufacturing a gate nobody asked for.** VERIFY-AFTER: size 523,207
and `sha 9bd953b9...`, **then** the three invokes -- **a restore whose size matches but whose invokes do not is not
a restore.**

**(3) ONE PRODUCER BEFORE ANY RE-FIRE.** The closer branch's `crosswalk.py` must reach CLOUD (`0.0.0_AB_MSTR~Z`'s
drain of `closer/amgt-peers-z-20260924`, LOCAL @`dfe74daed6`) so the re-mint **ADDS 20 to 194** rather than
replacing 194 with 36+20. **That drain is now on the incident's critical path.**

⭐ **AND THE GENERALISATION IS SHARPER THAN "COUNT THE WRITERS": A PRODUCER THAT EXISTS ONLY ON A BRANCH IS A WRITER
THE SHARED TREE CANNOT SEE.** Both halves of the first pair could count writers correctly *by reading CLOUD* and
still miss the one living on a closer branch. **The writer census has to span the live worktrees, not the trunk** --
which is the same lesson NEVER-2 teaches about `.open_deploys/` reads during a worker deploy, arriving from the
other direction.

## R-36 -- ~~THE INDUCTION MISFIRE: ZERO VENDOR CALLS, BUT A NEW **LATEST** POOL OBJECT IS A SERVED MOVE~~ **WITHDRAWN BY R-37**

⛔ **THE EXPOSURE GRADE AND THE "RE-MINT: YES" INSTRUCTION ARE BOTH WITHDRAWN -- see R-37.** The text is kept
UNEDITED below as the superseded reasoning, per this estate's own correction pattern: the marker sits on the
superseded bytes rather than replacing them, so a reader meets the withdrawal before the argument.
⭐ **WHAT SURVIVES R-37 AND IS STILL TRUE:** the zero-vendor-call finding (`bloomberg_calls 0`, RAW landings 0, no
egress breach), R-21's mechanism holding, the poisoned-client control adopted as a requirement, and the observation
that **a new dated key is a served move when the consumer's selector is "newest"** -- which R-37 does not weaken but
*sharpens*, since the key was not even new.

`2.0.0_SA_COO~X` fired the scripted induction producer once at 08:01:43Z-08:02:54Z under R-16 V2 / R-21 /
`C-NO-VENDOR-CALL` v0.5, after `2.0.0_SA_COO~Z`'s no-objection (msg 25319). **It made ZERO Bloomberg calls** and
reported the misfire itself, with the discriminator measured.

**CAUSE, correctly attributed by that seat to itself:** the ORDER's call shape was
`["--folder", <folder>, "--as-of", ..., "--write-pool"]`, and `add_security._discover` **with `--folder` alone reads
the folder's ONE PAGER workbook** for the identifier -- never the report evidence the request row already holds.
**12 folders carry no ONE PAGER; 8 carry the template placeholder `AAPL US`.** All 20 returned UNRESOLVED before any
call. Its words: *"The fault is this seat's cut of the order, not the worker's build and not `add_security`."*

⭐ **R-21's MECHANISM HELD, AND THAT IS THE FIRST THING TO SAY.** The act was a **scripted deterministic producer**
fired once with an env guard, not an agent turn -- exactly what Andrew's *"deterministic/scripted in nature"* word
requires. **A misfire inside the right mechanism is a different class from data acquired by hand.**

## RULED, THREE PARTS

**(1) NO VENDOR-EGRESS BREACH. `bloomberg_calls 0` on all 20 rows, RAW landings 0.** R-16 V2 authorised up to one
`reference_data` call per name; **zero were spent.** Nothing to report to Andrew on egress.

**(2) ⛔ BUT MINTING `crosswalk/v1/2026-09-24.json` IS A SERVED-OUTPUT CHANGE, AND IT HAPPENED WITHOUT A NEVER-WIDEN
PAIR.** Not because a key was overwritten -- the object is NEW, and the prior latest was `2026-09-22` -- but because
⭐ **THE READER TAKES THE LATEST POOL DOCUMENT.** So the effective served document moved from 09-22 to 09-24 while
no existing key was touched. **A new dated key IS a served move when the consumer's selector is "newest".** That is
the shape a "did we overwrite anything?" check cannot see.

**GRADED EXPOSURE, NOT INCIDENT -- on that seat's OWN discriminator, which is the right one:**
`records 96 -> 116`, `UNRESOLVED 60 -> 80`, `registered 7 -> 27`, and ⭐ **`MEASURED 36 -> 36`, UNCHANGED.**
`MEASURED` is what a consumer resolves against, so **no served resolution moved**; the 20 added rows are UNRESOLVED
and resolve to nothing. **Noise in the latest document, not a wrong key.**
⭐ **AND WHAT KEEPS IT EXPOSURE IS THAT SEAT'S OWN FENCE**, raised before anyone asked: *"do NOT run the Peers batch
on the 2026-09-24 stamp as it stands."* **It identified the one consumer that would convert its noise into a wrong
answer and stopped it.**

⛔ **THE NOISE OBJECT STAYS. DO NOT DELETE IT.** An S3 delete of a served key is a heavier act than the mint was,
needs its own authority, and would replace a measurable exposure with an unmeasurable one. **It is superseded by the
corrected re-mint, not erased.**

**(3) ⛔ THE CORRECTED RE-MINT NEEDS THE NEVER-WIDEN PAIR, AND THAT IS THIS SEAT'S ANSWER TO THE QUESTION THAT SEAT
ASKED.** It offered: *"If you would rather this seat NOT re-mint today's pool at all, say so before the re-fire and
it will be routed to the CTO instead."* **RULED: RE-MINT, under the pair.** The reasoning is the rule's own text --
*"NEVER move served output without never-widen sign-off (CTO+COO); **verified DELTA=0 needs no hold**."*
⭐ **THE MISFIRE QUALIFIED FOR THE DELTA=0 CARVE-OUT ON `MEASURED`. THE CORRECTED FIRE DOES NOT** -- 20 real
registrations move `MEASURED` off 36 **by design**, which is the whole point of the act. **So the carve-out that
excuses the first write is exactly what obliges a pair on the second.**
This seat signs the CTO half at the pinned candidate; `2.0.0_SA_COO~X` signs the COO half. ⚠ **Both halves name the
blast radius and the rollback PER KEY, and `write_pool`'s branched condition (`IfMatch` on a changed digest,
`IfNoneMatch` on a first mint) is the rollback's mechanism rather than a promise.**

## ⭐ THE CONTROL THIS PRODUCER LACKED, AND IT GENERALISES PAST THIS PROJECT

That seat's own diagnosis is the most valuable line in its report: ⭐ **"a dry run with a fake client cannot see
which argument the real seam consumes."** The dry run PASSED because a fake client never exercised `_discover`'s
folder branch -- **the control was real and on the wrong axis**, which is the class this estate keeps paying for.

**Its remedy is adopted as stated and is now the requirement:** a drill of the REAL seam with a **POISONED client**
-- one that asserts the argv reaching `_discover` and **refuses before the call** -- so the argument shape is
exercised without spending egress. Amendment 2 carries it as a test.
⚠ **AND THE ESCALATION IS THE POINT: amendment 1 (the `AXMB`/`AMXB` refusal) was caught by the DRY RUN; amendment 2
was caught only by THE FIRE.** Two cut errors on one order in one round, both that seat's, both found by exercise
rather than by review -- **and the second was invisible to every instrument short of the real seam.**

## R-35 -- THE R-34 QUESTION IS ANSWERED: **15 CONTRACT AMENDMENTS WENT TO THE WRONG REVIEWER**, NOT TO NO REVIEWER

R-34 named this as owed and refused to guess it: *"whether any of those 37 was ever AMENDED while classifying
brief -- an amendment that escaped the ratified-half review is a different and worse thing than a definition that
was merely never bound."* **Measured now, over the PRD's full `--follow` history.**

**METHOD, because the number is only worth what the method is:** all **41** commits touching
`AMGT_RESAPP_PRD.md`, oldest first; at each commit every contract's DEFINITION BLOCK extracted (its bolded `C-`
line to the next definition or heading), hashed, and the section's half resolved by `half_of_section` **at that
commit**. A contract counts as AMENDED where its block hash changes; the half recorded is the half it sat in
**when the change landed**.

| | count |
|---|---|
| contracts ever defined in this PRD | **67** |
| never amended -- one text throughout | **29** |
| amended while **ratified-text** -- the CVO signature covered it | **23** |
| ⛔ amended while **brief** | **15** |
| | **SUM 67 of 67 -- the subtraction closes** |

**The most-amended, with distinct texts:** `C-SA-UNMEASURED` **6** · `C-NO-CONTACT` **4** ·
`C-HARVESTER-COMPUTE` **4** · `C-VERBATIM-GATE` **3** · `C-SERVER-SIDE-RANKING` **3** · `C-MODEL-FORECASTS` **3** ·
`C-AMGT-ARTICLES-STORE` **3** · `C-VALIDATION-NAMES` **3**.
⚠ **`C-VERBATIM-GATE` is a HARD guarantee** (every drafted sentence over its cited passage, no tooltip carrier) and
it has moved through three texts outside the CVO's half. **`C-MODEL-FORECASTS` carries Andrew's own words inline**
and has moved through three.

⭐⭐ **AND HERE IS THE PART THAT MAKES THIS NARROWER THAN IT FIRST READS, WHICH IS WHY IT IS STATED BEFORE THE
GRADE: THE BRIEF HALF IS NOT UNREVIEWED. IT IS REVIEWED BY THE CRO** (`prd-signoff status` reads
`brief SIGNED 4.0.0_SA_CRO~Z current`). ⛔ **So these fifteen amendments were NOT unseen -- they were seen by the
seat the spine does not assign to contracts.** The spine gives CONTRACTS to `3.0.0_SA_CVO` *"always"*; these were
routed to the BRIEF reviewer by a heading's first word.

**RULED: THIS IS AN INCIDENT IN THE NARROW AND EXACT SENSE -- A MISROUTED REVIEW, NOT AN ABSENT ONE.** Rule 22's
negative mirror says an incident *"ALSO requires RE-OPENING WHATEVER THE GAP ADMITTED"*, and what this gap admitted
is **fifteen contract amendments graded by the wrong reviewer.** ⛔ **THE REMEDY IS THEREFORE A CVO READ OF THOSE
FIFTEEN AT THEIR CURRENT TEXT -- NOT A RE-OPENING OF THE WORK BUILT ON THEM.** Nothing here says the contracts are
wrong; `3.0.0_SA_CVO~Z` read my nine and found them sound, and the CRO's reviews of the brief half were real
reviews. **Re-opening downstream work on this would be the exact over-correction Rule 22 warns of in its other
direction -- "re-opening work nothing ever harmed."**

⭐ **WHY THE NUMBER IS TRUSTWORTHY AND THE FIRST TWO ATTEMPTS WERE NOT.** Attempt 1 died on **cp1252** decoding the
PRD's non-ASCII and printed *"COMMITS SCANNED: 1 ... 0 amended while classifying BRIEF"* -- **a clean, confident
ALL-CLEAR produced by a crashed reader.** Attempt 2 printed the same `1`, because
⛔ **`git log --follow` DOES NOT COMPOSE WITH `--reverse`: together they collapse to ONE line, rc=0, empty stderr.**
Plain gives 40, `--follow` alone gives 41. **Both failures returned the REASSURING shape on the one question that
separates exposure from incident**, and only a positive control (`the --oneline --follow count is 41`) caught them.

⛔ **NOT FIXED IN THIS COMMIT** -- round 37 is in flight, Rule 27 freezes the spec, and the heading renames ride the
post-drain edit with F2, F3 and R-34. **The CVO read of the fifteen does NOT wait on that** and is routed now.

## R-34 -- ⛔ THE GUARD'S FIRST REAL RUN FOUND **37 CONTRACTS** OUTSIDE THE CVO SIGNATURE, AND NONE OF THEM IS MINE

`2.0.0_SA_COO~X` ROUTED the contract-half guard back to this seat as **not its project's cell** -- *"the defect and
the tool are yours ... one project's loop never writes another surface's fix"* -- with the rec to land it as this
seat's own mechanism *"with a negative control that re-heads one section and watches it fire."* **Correct, and
built: `.tools/prd-contract-half-check.py`.**

**IT IMPORTS `half_of_section` RATHER THAN RE-IMPLEMENTING IT** -- a second copy of that rule would be the very
two-carrier defect the guard exists to catch -- and it separates **DEFINITION** (a line OPENING with a bolded
`C-` id) from **MENTION**, because a naive grep over `C-` would be useless here: `AMGT_RESAPP` carries **295
mentions** against **4** defining sections.

⭐ **ITS FAILING ARM IS EXERCISED, NOT ASSUMED.** `--self-test` builds two in-memory fixtures and requires BOTH to
disagree with each other: a contract under `## B.4` MUST be refused, and the same contract under
`## CONTRACTS -- B.4` MUST pass while a mention-only section is NOT refused. **A checker whose failing arm was
never run reads identical to a real pass.** Historical control: the pre-rename vintage `1ffb156ecd` is REFUSED on
3 RESAPP sections + 1 CORPUS section, and `AMGT_CORPUS` at HEAD now **passes** -- so the instrument discriminates
across the fix rather than merely agreeing with it.

⛔⛔ **AND ON ITS FIRST RUN AGAINST HEAD IT REFUSED `AMGT_RESAPP` ON TWO SECTIONS THAT PREDATE MY ADDENDUM BY MANY
VERSIONS:**

| section (first word decides the half) | classifies | DEFINES |
|---|---|---|
| `## 3. CONSTRAINTS ON THE CUT` | **brief** | **34 contracts** -- `C-UNIT-MAP-MEASURED`, `C-MODEL-FORECASTS`, `C-VERBATIM-GATE`, **`C-VENDOR-EGRESS`**, `C-SERVER-SIDE-RANKING`, `C-DESIGN-SPEC-FIRST`, ... |
| `## 10. ADDENDUM v0.11 -- INSTANTIATING A NEW SECURITY` | **brief** | **3** -- `C-INSTANTIATION-ENTRY`, `C-PRODUCTION-HOME`, `C-VALIDATION-NAMES`, each marked *"(new, v0.11)"* |

**These are DEFINITIONS, verified by reading them rather than by counting matches:** the authoritative bolded form,
several carrying **Andrew-direct authority inline** (`C-MODEL-FORECASTS` quotes his *"I'd use Bloomberg as primary,
seeking alpha as a fallback"*). The properly-headed `## CONTRACTS -- v0.7 (ratified text; the reviewer is
`3.0.0_SA_CVO`, always)` classifies ratified and IS bound -- so the PRD has always had both kinds side by side.

⛔ **SO 37 CONTRACTS ON THIS PROJECT, INCLUDING A VENDOR-EGRESS CONTRACT, HAVE NEVER BEEN INSIDE THE BYTES THE CVO
SIGNATURE BINDS.** My addendum's four were a NEW instance of a defect that was already there at scale.

⭐⭐ **WHY NEITHER REVIEWER FOUND THESE, AND IT IS NOT A CRITICISM -- IT IS A STRUCTURAL LIMIT WORTH NAMING.**
`3.0.0_SA_CVO~Z` (row `Z-S11`) and `4.0.0_SA_CRO~Z` (first verdict REFUSE) each caught **my four**, independently,
on the same bytes. Both were reviewing **THE SPAN SINCE THEIR OWN LAST SIGNATURE** -- which is correct review
practice and is exactly what this estate asks of them. ⛔ **A SPAN-BASED REVIEW IS STRUCTURALLY BLIND TO A DEFECT
OLDER THAN ITS SPAN.** The 37 were never in anyone's delta, so no amount of care in the delta would surface them.
**That is what a whole-file guard buys that a diff review cannot, and it is the argument for the guard existing at
all rather than relying on reviewers.**

⚠ **EXPOSURE OR INCIDENT IS NOT ANSWERED HERE AND IS NOT GUESSED.** The discriminating question is whether any of
those 37 was ever **AMENDED** while classifying brief -- an amendment that escaped the ratified-half review is a
different and worse thing than a definition that was merely never bound. **That needs a per-contract history read
this seat has not done, and it is named as owed rather than assumed either way.**

⛔ **NOT FIXED IN THIS COMMIT, AND THE REASON IS THE SAME AS R-33's: ROUND 37 IS IN FLIGHT AND RULE 27 FREEZES THE
SPEC MID-ROUND.** Renaming two more headings would move bytes between halves for the third time today and
invalidate two signatures that have been current for under an hour. **It rides the post-drain edit WITH F2 and F3.**
⭐ **The guard is committed NOW and unblocked -- it refuses nothing at commit time yet, so landing it costs no seat
anything, and it is the durable form of the correction rather than a promise to remember.**

## R-33 -- TWO CORRECTIONS OWED ON `AMGT_RESAPP` v0.26, PARKED NOT APPLIED, BECAUSE ROUND 37 IS IN FLIGHT

`4.0.0_SA_CRO~Z`, stamping the brief half (`e8c94916ef`, review @`0175833900`), raised two items it explicitly
marked *"TWO CORRECTIONS OWED, not grounds, to ride whatever edit next opens the PRD after the freeze."*
**Both are real and both are PARKED HERE rather than applied.**

⛔ **WHY PARKED: RULE 27 FREEZES THE SPEC MID-ROUND** -- *"Mid-round the spec AND the decomposition are
FROZEN"* -- and `2.0.0_SA_COO~Z` has round 37 issued @`53793b671f` with `rl-1` RUNNING against these exact bytes.
⭐ **The byte freeze this seat imposed has SERVED ITS PURPOSE (all four halves SIGNED and current) and is
LIFTED; what holds now is a different and stronger constraint -- the round's own freeze, which is the COO's
round to unfreeze, not this seat's convenience.** That seat named the right landing slot before being asked.

**F2 -- `C-CLAUSE-CITED-REJECTION` OMITS `C2`, AND IT IS MATERIAL RATHER THAN COSMETIC.** The clause list at
`:2268` reads C1, C3, C5, C6, C8, C9, C10, C11, C12. **`FWD-22`'s own DONE WHEN requires TABULAR NUMERALS, which
is `C2`, and the walk brief's IV.2 carries a C2 finding.** ⛔ **So a reviewer rejecting a `FWD-22` candidate on
tabular numerals would be citing a clause the contract does not admit -- the rejection machinery and the outcome
disagree.** Remedy: add `C2`.

**F3 -- A LINE CITATION THAT NOW LANDS ON A DIFFERENT CONTRACT.** The preamble note at `:386` cites
`C-VERBATIM-GATE` *"at `:1107-1114`"*, which was true at `d8d2052388` (`:1113`); **at this pin those lines land on
`C-DEDUPE-BY-KEY`**, and the clause itself is at `:1234`. Remedy: **cite by NAME, not by line.**

⭐ **F3 IS CLAUDE.MD RULE 27'S OWN NAMED DEFECT, FOUND IN THIS SEAT'S PRD: *"A CITATION AGES SEPARATELY FROM THE
TEXT IT QUOTES -- re-reading the rule catches neither."*** The rule states the failure mode in the law this seat
edits; the PRD reproduced it anyway. ⛔ **AND THE AGED FORM IS WORSE THAN A DEAD LINK: it RESOLVES, to a REAL
contract that is the WRONG one** -- a reader following it gets a confident answer about dedupe when they asked
about the verbatim gate. **Citing by name cannot age.**

⭐ **ONE THING THAT SEAT DID WHICH IS WORTH THE RECORD: ITS FIRST VERDICT WAS *REFUSE*, ON THE SAME GROUND THE
CVO FOUND, REACHED INDEPENDENTLY ON THE SAME BYTES** -- B.4's four `C-` contracts hashing into the brief half,
*"zero occurrences in CONTRACTS :770-1140"*, while the ENDPOINT fence cited them as acceptance authority. **The
tool then refused that stamp because the half had already moved to `031c3a3a3e`, whose one change to this PRD is
that ground's cheapest remedy.** So two seats convicted the same defect on two instruments, and the refusal text
stays on record under a vintage note rather than being erased by the fix. ⚠ **Its own `L4R_REVIEW` file keeps the
`v0.25` label the request used while the bytes reviewed are v0.26's -- disclosed by that seat, and noted here so a
later reader does not treat the label as the vintage.**

**NO CORRECTION OWED ON `AMGT_CORPUS`** (stamp `9b17fd5d49`): ten carriage checks against the dossier brief at
`@328e17d5e5` all correct, including the numbering collision, the O7/F2 amendment, **all three stale passages with
two of them phrased as directives**, and *"backfill once at `:423` with `add_security` nowhere -- so `FWD-19` is
genuinely by subtraction."* ⭐ **That last line is an independent seat confirming the subtraction rather than
adopting this seat's word for it.** It also records that **the `CONTRACTS`-heading device is the fix the RESAPP
addendum lacked, since applied** -- the two PRDs now agree.

## R-31 -- ⛔ CALL 4 IS NOT UNDECIDABLE. THE IDENTITY IS IN A 30-DAY LOG, AND "RECONSTRUCTABLE FROM NOTHING" IS FALSE

**The card:** whether the AMGT incident's realised exposure -- four `BA_US_Equity` thesis responses
(09-22 19:15:35, 20:14:11, 20:21:40; 09-23 20:44:34) plus one overlay, **all to ONE client IP** -- warrants a client
notification. **It has sat at Andrew as structurally undecidable**, on `3.0.0_SA_CVO~Z`'s deliberate and
well-reasoned abstention (R-21a): *"it turns on who the client was, which this seat cannot determine and will not
guess"*, because *"per-firm attribution is reconstructable from nothing in this estate (R-11a) ... an IP is not an
identity."*

⛔ **THE UNIVERSAL IS FALSE, AND THE TELL WAS GRAMMATICAL BEFORE IT WAS MEASURED.** *"Reconstructable from
NOTHING"* is a NEVER-class quantifier, and the instrument behind it is a REPO-PLANE one. **A repo census can
answer "no mapping file exists here." It can never answer whether the AWS plane logged a principal.** That is a
different instrument, and it cost one query.

**MEASURED, 2026-09-24 ~05:4xZ, on the live plane:**
- `/aws/lambda/opal-portal-authorizer` **EXISTS**, retention **30 days**, 3.75 MB stored -- so the incident window
  is RETAINED, not aged out.
- Its events carry, verbatim: `Token verified successfully: { email, tier, role, userType }` and an
  `Authorization context: { email, tier, role, userType, allowedFirmIds }`. ⭐ **EMAIL, TIER, ROLE AND FIRM SCOPE,
  PER AUTHORIZATION.**
- ⭐ **COVERAGE CONTROL RUN BEFORE ANY ZERO WAS BELIEVED:** 2026-09-22 UTC holds **26+ events**, so the log has
  data that day. Across that day it distinguishes **TEN DISTINCT IDENTITIES ACROSS FOUR FIRMS** -- six internal
  `@opalinvest.com` authorizations and, on three EXTERNAL client domains, `vmwealthpartners.com` (16),
  `inflectionwealth.com` (52 across three people) and `cottonwoodmail.com` (9 across two).
  ⚠ **Individual addresses are deliberately NOT restated outside this file, and no broadcast carries them** -- the
  firms and the counts are what the decision needs; the addresses are client PII and naming them wider would be a
  second disclosure while adjudicating the first.

**RULED: CALL 4 IS RECLASSIFIED FROM "BLOCKED ON A FACT NOBODY HOLDS" TO "DECIDABLE, ONE JOIN AWAY." IT IS NOT
ADJUDICATED HERE, AND THE REASON IS NOT AUTHORITY.**

⛔ **WHAT THIS SEAT MEASURED DOES *NOT* CLOSE IT, AND THE LIMIT IS SPECIFIC: AN API GATEWAY AUTHORIZER RESULT IS
CACHED.** Of the four timestamps, three windows (+/-8s) returned **empty** and one (09-23 20:44:34) returned five
events, **all `andrew@opalinvest.com`, tier internal, userType Dev**. ⭐ **THE THREE EMPTIES ARE A CACHE ARTIFACT,
NOT AN ABSENCE** -- a served request can reuse a cached authorization minutes old and emit no authorizer line at
all, which is exactly why the coverage control mattered: the log HAS 09-22 data, so the empties cannot be read as
"nobody was authorized." ⛔ **AND FOR THE SAME REASON THE ONE HIT IS NOT AIRTIGHT EITHER** -- five events in a
12-second window is consistent with, but does not prove, that those events authorized THAT request.

⭐ **THE JOIN THAT WOULD CLOSE IT, NAMED SO THE NEXT SEAT DOES NOT RE-DERIVE IT:** `3.0.0_SA_CVO~Z` already parsed
**664 CloudFront access-log files, 19,114 rows**, and holds **the one client IP**. CloudFront carries IP+timestamp
per request; the authorizer carries email+firm+timestamp. **Neither alone attributes a request; together they do.**
⭐ **And there is a SHORTCUT that avoids the per-request join entirely: the exposure was ONE IP. Mapping that single
IP to an identity through ANY overlapping authorizer event settles the whole card** -- and that seat holds the IP
this seat does not.

⚠ **WHY THIS IS STILL NOT THIS SEAT'S CALL TO DECIDE, EVEN UNDER ANDREW'S "all open-calls ... adjudicated by
`1.0.0_SA_CTO~Z`" WORD.** His word supplies AUTHORITY. It does not supply the JOIN. ⛔ **Adjudicating now would
mean guessing which of ten identities it was -- converting a deliberate abstention into consent, which is the
precise error R-21a was written to prevent.** ⭐ **And the abstention was RIGHT ON ITS FACTS AND WRONG ONLY ON ITS
UNIVERSAL: the decision does turn on who the client was; that fact simply exists.**

**OWED, and it is a measurement rather than a decision:** `3.0.0_SA_CVO~Z` runs the IP-to-identity join against
this log group **before the 30-day retention wall**, which for the 09-22 events falls **2026-10-22**. ⛔ **THAT
DEADLINE IS REAL AND IT IS THE FIRST TIME THIS CARD HAS HAD ONE: today the fact exists, and on 2026-10-22 it stops
existing.** An undecidable card can wait; a decidable one with an expiring instrument cannot.

## R-32 -- ⛔ A RECORD WITH A HUMAN CARRIER AND A MACHINE CARRIER IS NOT WRITTEN UNTIL BOTH ARE. FOUR INSTANCES, MEASURED COST

Found while adjudicating the sitez open-call set, in **four** places in one stretch, **three of them this seat's**:

| # | the record | written | NOT written | who read it wrong, for how long |
|---|---|---|---|---|
| 1 | `closer_contract` (R-26a) | the GENERATED `org/projects/*.json` row | the DECLARED tree `project.json` | the generator would have ERASED it on the next `dep_stage` move |
| 2 | the twenty new `FWD` ids (R-27a) | the PRD header | the ENDPOINT section step 5 reads | the surface-manifest GATE caught it at commit |
| 3 | D12 ledger legs `A`/`V1` (`0.0.0_AB_MSTR`'s) | the markdown proof table, *"CLOSED 20260913T0629xxZ"* | the `.open_deploys/*.json` index the tool reads | **11 days** of two falsely-stranded legs |
| 4 | the v2.1.179 **PROD promote** (this seat's) | a prose `## Close-out`, *"LANDED AND VERIFIED ... Nothing half-landed"* | the `**Status:**` field | **8.2 days** of a RED `BYPASS: UNINDEXED OPEN LEDGER` on a production deploy |

⛔ **THE FAILURE IS SILENT IN BOTH DIRECTIONS AND SURVIVES A CAREFUL RE-READ OF WHAT YOU WROTE.** Write only the
human carrier and every automated read is wrong -- a false RED, for 8 days, on the one class where "half-landed"
is most expensive. Write only the machine carrier and every human read is wrong, and a generator deletes it.
⭐ **In case 4 the author had verified the world, the close-out was TRUE, and re-reading it would never have
surfaced the defect -- because what was written was correct. The defect was in what was NOT written.**

⭐ **THE TELL, AND IT IS CHEAP: IF A TOOL ENFORCES THE RECORD, THE TOOL'S READ IS THE RECORD.** After writing any
ledger, index or register entry by hand, run the tool that grades it and require the entry to CHANGE STATE.
**COST: one command.** **NON-APPLICATION: a record with exactly one carrier and no tool that reads it.**

**REPAIRED IN THIS COMMIT, with verify-after:** `V2` closed on its own clause measured verbatim
(`ACCOUNT_TIER=PRODUCTION`, `TEXT_MESSAGE_MONTHLY_SPEND_LIMIT EnforcedLimit=50`); `A` and `V1` closed by
**TRANSCRIBING** MSTR's existing markdown proof into the index, marked as transcription and not assertion, with `A`
re-verified live; the PROD promote given its `**Status:** CLOSED` field. **VERIFY-AFTER: the `BYPASS` and `RED`
lines are GONE and D12's stranded set went `['A','V1','V2','V3']` -> `['V3']`, denominator 5 of 5 sentinels.**

⛔ **`V3` IS LEFT OPEN DELIBERATELY AND ITS CLAUSE IS DEFECTIVE TWICE OVER.** It requires
*"`SMS_VERIFIED_DESTINATIONS` + `SMS_ALLOW_UNVERIFIED` re-read in a reviewed commit BEFORE or WHEN V2 lands"*, with
proof *"commit hash under `0.7.0_AE_CloudOps` author line"*. **(i) The re-read happened in
`0.4.0_DT_ClientPlatform`'s patch of 2026-09-17, a different lane, so the clause cannot be satisfied as written
unless the AE lane redoes another lane's work. (ii) "BEFORE or WHEN V2 lands" is already past.** ⭐ **This is the
same stale-clause class as H03's five gold clauses, and the discipline is the one this seat gave the AE seat
hours earlier, inverted: there the temptation was to change the ACT to make a clause pass; here it is to close a
LEG under a clause it does not satisfy. Both are the record bending to the checker.** The clause is re-cut, not
stretched.

## R-29 -- THE THIRD CROSSWALK SOURCE IS APPROVED, BOUNDED; AND ITS OWN RESEARCH NAMES A SIXTH BOUND IT DID NOT DRAW

**Closing the fork R-23a opened.** `4.0.0_SA_CRO~Z` researched it under `/self-drive`'s call routing -- *"If the
call specifically is a design fork, then you reach out to CRO agent to do research on past patterns ... and then
make the call with that info"* (Andrew-direct 2026-09-17 ~13:0xZ) -- and delivered
`AMGT_CROSSWALK_THIRD_SOURCE_RESEARCH_20260924.md` @`2ed4077666`. **The ruling is this seat's; that seat states
plainly that nothing in its research is an act.**

**RULED: APPROVED, as a registration source in the BUILDER, under the five bounds it drew PLUS a sixth below.**

**WHY IT IS NOT WHAT R-14 REFUSED, which is the whole question.** R-14 refused **the ROUTE trusting an artifact
while it is under resolution**. This is **the BUILDER minting registrations before any route reads anything** --
different actor, different moment, different failure mode. ⭐ **And the precedent argues FOR it rather than merely
permitting it:** `rk-4` widened the RANKER to 191 keys while the crosswalk carried 36, and **stranded 111 real peer
sets**. Deere is that same shape one hop down, so refusing here reproduces a defect this project already paid for.

**WHY "NEVER GUESSED" SURVIVES, measured rather than asserted.** The rule **REFUSES 1,812 of 2,851 member rows BY
CONSTRUCTION** and registers only the **1,039** whose OWN ROW states both an alpha ticker root and country United
States. The country is **read from the row**, not inferred from an exchange code; a non-US root carries no exchange
code and no country-to-exchange table exists, so it is refused rather than resolved. ⭐ **And the decisive
measurement is a NEGATIVE one: ZERO tickers appear under two countries**, so there is no collision to guess at.

**THE ALTERNATIVE IS PRICED, WHICH IS WHY THIS IS A CHOICE AND NOT A DEFAULT.** Posture naming only crosswalk
comparables puts **UNRESOLVED on the Posture tab's first line for every name whose comparable the builder never
heard of** -- and all eleven Boeing comparables plus `DE` are US alpha roots, so the visible cost lands on the
flagship name.

**THE FIVE BOUNDS ARE ADOPTED AS WRITTEN** (a) US alpha roots only, keyed `<ROOT>_US_Equity` from the row's own
country; (b) **EXISTING RECORDS WIN** -- the member source applies LAST and skips any key the coverage list or
`registrations.json` already holds, marking `also_in_scanner`; (c) alias forms are the canonical key and
`"<ROOT> US"` only, **NEVER the bare root**, which is what keeps it from colliding with the five pilot bare-root
aliases (`BA`, `COST`, `HAL`, `HD`, `VLO`); (d) the record carries `basis: scanner-member` with the scanner vintage
and universe ids **so a consumer can reject on it**, and nothing inducts from it; (e) the source re-mints when the
scanner vintage moves.

⭐ **BOUND (d) IS ALSO THE GRADER'S DISCRIMINATOR FOR BOUND (b), AND THAT IS WORTH STATING BECAUSE IT COSTS ONE
QUERY.** "Existing records win" is a claim about ORDER, which no snapshot shows. But a key that the coverage list or
`registrations.json` holds and that nevertheless carries `basis: scanner-member` **is the violation's own
signature** -- so the arm is: run that query over the registered set and print the denominator. **Zero is the pass.**

⛔ **THE SIXTH BOUND, WHICH THAT SEAT'S OWN "NOT MEASURED" SECTION IMPLIES AND DID NOT DRAW: THE COLLISION COUNT IS
A FLOOR, NOT A NUMBER.** It measured **9 minted US keys already crosswalk keys** against the
`crosswalk/v1/2026-09-22` object, and says so -- but the live object has moved. ⛔ **So a builder run re-measures
collisions against the CURRENT object before writing, and 9 is the LOWER BOUND, never the expected value.** A run
that finds more than 9 is finding the truth, not a regression, and must not be read as one. **A floor presented
beside a precise number reads as the number; that seat disclosed the limit and the disclosure is what makes this
bound cheap.**

⚠ **AND BOUND (e) COUPLES THIS TO A DIFFERENT PROJECT, WHICH IS NAMED SO NOBODY DISCOVERS IT LATER.** Re-minting on
scanner-vintage movement makes this source a CONSUMER of the FactSet screening refresh -- the `SSCN` scripted-refresh
brief @`3ed1c5e1f1`, whose own load-bearing unknown is whether Opal's entitlement admits a programmatic export at
all. **The peers ranker's `universe_vintage` already follows that vintage, so this is a SECOND consumer of one
unsettled upstream.** ⛔ **That does not gate this approval** -- the source works at a frozen vintage and re-mints
when one arrives -- but a stale scanner vintage now has two dependents, and the count belongs in the record.

**NOT AUTHORIZED BY THIS RULING:** no builder run, no pool write, no route change, no induction from this source
(bound d), and nothing about the 93 non-US roots.

## R-30 -- PEERS FAILURE CASE 3: THE GREEDY ROUTE IS APPROVED, AND SHIPPING IT ALONE IS REFUSED

**Two seats localised this independently, on different instruments, and reached the same place.** `3.0.0_SA_CVO~Z`
by direct lambda invoke, which BYPASSES the gateway: the decoded key `BP/_LN_Equity` returns **HTTP 200, identity
MEASURED, 12 members served from `peers/v1/BP/_LN_Equity/...`**, while the percent-encoded `BP%2F_LN_Equity`
returns **200 with identity UNRESOLVED and 0 members**. `2.0.0_SA_COO~Z` localised it to the **API Gateway route
table**, rec **one greedy route**. ⭐ **The handler, the crosswalk, the pool object and the engine are all FINE, and
the ten slash-key sets are NEITHER STRANDED NOR MALFORMED -- they are unreachable only through a URL path segment.**

**RULED: the greedy route is APPROVED. Shipping it WITHOUT the decode at the handler boundary is REFUSED.**

⛔ **THIS IS THE WHOLE RULING AND IT IS `3.0.0_SA_CVO~Z`'s FINDING, NOT THIS SEAT'S:** fixing the gateway alone
would **LOOK like progress and change nothing a user sees.** The request would stop 404-ing and start returning a
clean, confident **UNRESOLVED with zero members** -- which is the `peer_read {}` shape where *"could not read"* and
*"nothing to read"* are indistinguishable. **A user would see an empty peer set for a security whose 12-member
object exists and is readable.** ⭐ **So the gateway half converts a LOUD failure into a SILENT one, and a silent
wrong answer is worse than a 404.** Both layers land in ONE candidate or neither does.

⭐ **THE MECHANISM IS ALREADY BANKED ON THIS DEVICE AND CORROBORATES BOTH SEATS ON A THIRD INSTRUMENT:** an HTTP API
**decodes `%2F` BEFORE matching**, a `{param}` never spans two path segments, so the request falls through to
`$default` -- and **a 404 whose body lists ANOTHER function's routes is a gateway route miss, not a handler
defect.** Three independent arrivals at one answer.

**THE ACCEPTANCE ARM, and it must distinguish the two layers rather than pass on either:**
1. `BP%2F_LN_Equity` **through the gateway** returns **200 with 12 members** -- not 404, and not 200-with-zero.
2. ⛔ **THE DISCRIMINATOR: a key that genuinely does not exist must STILL answer UNRESOLVED-with-reason, not 12
   members.** A greedy route plus a permissive decode could make every malformed key resolve to something. `NOSUCHKEY`
   is the negative control and it was already the discriminator that made the Peers route grade honest.
3. The **nine other slash-key sets** reach 200 as well -- ten of ten, denominator printed, because one working name
   is a fix for one name.

⚠ **ONE DESIGN NOTE CARRIED FROM THAT SEAT, offered to the build and not imposed:** the object key itself contains
the slash (`peers/v1/BP/_LN_Equity/...`), **so the pool path and the URL path disagree about what a key is.** Any
fix that encodes at one boundary must decode at the other, and **the two boundaries are owned by different
surfaces -- which is exactly the split where an encode/decode pair goes missing.**

## R-28 -- H03 2a IS LANDED AND VERIFIED, AND THE OUTPUT DELTA OUTSIDE THE SIGNED RADIUS IS RULED INSIDE IT

**`0.7.0_AE_CloudOps~A`, RAVC2, commit `6fdfe5b25e` (LOCAL, measured by `ls-remote` with `f47642479c` as a
positive ancestry control).** Apply complete: **1 imported, 0 added, 3 changed, 0 destroyed** -- identical to the
plan and to the letter's prediction. `CodeSha256 Xdwp7Ir...` at 55,418,293 b, **512 MB / 120 s**,
`CHATTER_AXIS_SOURCE=legacy`, revision `e37b6030 -> 2c917823`. `terraform plan -detailed-exitcode` rc=0.
**NEVER-WIDEN HELD, COUNTED RATHER THAN ASSERTED:** exactly TWO `chatter_daily` entries across 4 statements and 21
resource/prefix entries, **gold-but-not-`chatter_daily` entries 0, removals 0**; log group tags-only,
`retention_in_days 0` unchanged. **Ledger leg `tf` CLOSED**; `daily` (the 10:00Z fire) and `served` (CVO-owned)
remain. ⭐ **The ledger was read across ALL 43 live worktrees and found in 3** -- NEVER-2 applied, where a
single-tree read would have returned a confident wrong answer.

⭐ **THE MEASUREMENT THAT DID NOT EXIST BEFORE THE ACT: `Max Memory Used 112 MB` AGAINST THE PRIOR 128 MB
CEILING.** The function was running at **87.5% of its limit**, so the 128->512 resize was **load-bearing, not
cosmetic** -- and nothing before this apply could have known that, because the figure is a product of the run.
**A resize that looked like packaging hygiene was 16 MB from an OOM.**

⭐ **AND THE R-15/R-17 REQUIRED ITEM IS DISCHARGED:** the one `dry_run` invoke (RequestId `10fbaa9c...`,
StatusCode 200, FunctionError null) is the **first target-runtime evidence of Arrow 15.0.2 reading
Arrow-24-written parquet**, clean. Zero-writes held on both products (`rows_written=0`,
`pointer_written=False`, `failed_marker_written=False`). ⚠ **And that seat guarded the exact misreading this
letter feared:** the dry-run `pointer_written=False` is the dry run writing nothing and is **NOT** evidence about
the 10:00Z fire, where a generation IS expected.

⭐ **THE FIVE STALE PROOF CLAUSES WERE REPORTED AND NOT RECONCILED, AND NOTHING WAS ALTERED TO MAKE ONE PASS.**
That was the single most important line in the letter and it came back in that seat's own words. **The half of the
pair an actor is best placed to "fix" is the half that stayed untouched.**

### R-28a -- THE `scoped_amgt_route_keys` OUTPUT DELTA: RULED INSIDE THE RADIUS, ON A WRITER COUNT

**BOTH `0.7.0_AE_CloudOps~A` AND `0.0.0_AB_MSTR~Z` CARRIED IT TO THIS SEAT RATHER THAN ABSORBING IT**, because the
letter's radius named three resources and no output while the plan added five keys (`freshness`, `lists`, `ledger`,
`versions`, `compare`). ⭐ **RAISING IT WAS CORRECT: a delta outside what a never-widen half NAMES is precisely what
that half exists to catch, and neither seat owns that surface.**

**RULED: THE SIGN-OFF HOLDS AND COVERS IT.** Measured on the never-widen rule's own instruction -- *"FIRST COUNT THE
WRITERS OF THE NAMED PROPERTY ... and N is a number the half PRINTS"*:

| | |
|---|---|
| **N = 1 WRITER** | `infra/aws/terraform/harvest/scoped-amgt-api.tf:387`, `output "scoped_amgt_route_keys" {` |
| **N = 0 CONSUMERS** | 15 hits across **72,224 files** scanned -- `SURFACED=1` (that declaration), `CONFIG=3`, `DOC=11`. Every non-declaration hit RECORDS a past plan or run; none is a reference |

⭐ **THE CENSUS IS DECISIVE RATHER THAN SUGGESTIVE BECAUSE OF HOW A CONSUMER MUST SPELL ITSELF:** reading an output
requires NAMING it -- `module.<x>.scoped_amgt_route_keys`, a `terraform_remote_state` lookup, or
`terraform output -json` in a script -- and **every one of those forms contains the string**, so the census that
found the declaration would have found the consumer. An output with one writer and no reader creates no AWS
surface, writes no served artifact and moves no key.

⭐ **AND TWO INDEPENDENT NEGATIVE CONTROLS FOR THIS EXACT DELTA WERE ALREADY IN THE CORPUS, NEITHER AUTHORED FOR
THIS ACT** -- which is better evidence than this seat's own reading: `AMGT-rk-59`'s `proof_of_spec` (`:74`),
*"only 'Changes to Outputs:' for scoped_amgt_route_keys, pre-existing/unrelated"*; and
`AMGT_EXPERIENCE/C1_EXECUTION.md` (`:11`), *"Exit 2 is only an update to the Terraform output
scoped_amgt_route_keys; no further apply was performed."* **Three seats have now met this delta on this stack and
dispositioned it identically.**

⚠ **THE LIMIT, STATED BECAUSE THE RULING READS WIDER THAN IT IS:** this covers **the five named keys on
`scoped_amgt_route_keys` and nothing else.** A delta on a DIFFERENT output, or a resource line where the plan read
`1 import / 0 add / 3 change / 0 destroy`, is **NOT** covered and returns here. **A ruling that a class of delta is
benign is not a ruling that deltas are benign.**

## R-27 -- BOTH ADDENDA CUT; THE EXPORT WAS IN NEITHER BRIEF, AND A GATE CAUGHT THE THIRD COORDINATE MISS

**Andrew-direct ~05:0xZ sets the goal and its completion test** (verbatim at
`ANDREW_DIRECT_20260924_050xZ_AMGT_GOAL_AND_COMPLETION_TEST.md`). `AMGT_CORPUS` v0.5 ADDENDUM A (`FWD-10`..`FWD-19`)
and `AMGT_RESAPP` v0.25 ADDENDUM B (`FWD-21`..`FWD-30`), both @`1ffb156ecd`.

⛔ **HIS FOUR CLAUSES MINUS WHAT WAS COVERED LEAVES AN EXPORT NEITHER BRIEF CARRIES.** The frontend brief's nine
outcomes are ALL render outcomes and its own Part VII lists *"the print action"* among what it did not capture; the
CORPUS brief never mentions an export. ⛔ **SO BOTH ROUNDS COULD HAVE BEEN CUT, DRIVEN AND GRADED COMPLETE WITH HIS
THIRD CLAUSE UNSERVED, AND EVERY ARTIFACT WOULD HAVE READ DONE.** It lands as `FWD-30`. ⭐ **Rule 24's subtraction
found it; reading his sentence for the parts that matched work already in flight would not have.**

⚠ **AND HIS COMPLETION TEST OVERTURNED A CONTRACT THIS SEAT HAD WRITTEN MINUTES EARLIER.**
`C-BACKFILL-DENOMINATOR-IS-THE-ESTATE'S-LIST` held that the 93 folders were *"the pool, not the population"*; he
said the folder IS the population. Replaced, and `K6` closed unworked. ⭐ **THE REASON IT COST NOTHING IS THAT THE
UNCERTAINTY WAS FILED AS A CARD RATHER THAN RESOLVED BY INFERENCE** -- one sentence from him closed it and nothing
had been built on the wrong domain. **Had this seat resolved it on its own reasoning, the round would now be
building an estate-wide backfill he never asked for, and the artifact would have looked measured, because its 93 was
real.**

### R-27a -- ⛔ THE THIRD COORDINATE MISS TONIGHT, AND THE ONLY ONE A GATE CAUGHT

The first cut of both addenda defined the twenty new outcomes in the HEADER and in the ADDENDUM section, and left
the **ENDPOINT section -- the surface step 5 reads -- without them.** The **step-4 PRD surface-manifest gate REFUSED
the commit** and named all twenty: *"the R3 monitor reads the header and step 5 reads the section, so this drift is
invisible to a reader and total to a consumer."*

⭐ **THREE INSTANCES OF ONE CLASS IN ONE STRETCH, ALL THIS SEAT'S:** R-26a (the field on the GENERATED row, not the
declared one) · A.2's stale O7 instruction in the brief this seat was cutting from · and this. ⛔ **AND THE
DIFFERENCE THAT MATTERS: the first two were found by READING, this one by a MECHANISM.** The gate could not be
talked past, cost one refused commit, and named every missing id. **A rule that depends on a reader noticing has a
failure rate; a gate does not** -- and the remedy here was to make the ENDPOINT fence the ONE carrier and turn both
addendum sections into pointers, rather than to keep two carriers in sync by discipline.

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
