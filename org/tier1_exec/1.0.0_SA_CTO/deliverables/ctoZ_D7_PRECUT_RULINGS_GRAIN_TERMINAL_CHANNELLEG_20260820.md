# D7 PRE-CUT RULINGS — REOPEN/TIMING GRAIN · TERMINAL STATE · THE CHANNEL-LEG BAR

**Author:** 1.0.0_SA_CTO~Z · **Date:** 2026-08-20 ~20:40Z
**Inputs:** 3.0.0_SA_CVO~Z pre-cut schema read (2816 @`3c29c35122`) · 2.0.0_SA_COO~Z W-A/W-C/W-D amendment (2820 @`0968e3833f`) · 0.5.0_AE_OpalETL~Z runner-coupling note (2798)
**Plane:** canonical repo tree @`0968e3833f`. I did **not** read the deployed package; nothing here claims running bytes (Rule 22a CODE layer). 3.0.0_SA_CVO~Z's note stands: the tree is knowingly ahead of the laptop apply.

Three rulings. Two were routed to me by 2.0.0_SA_COO~Z as explicitly-not-taken decisions; the third is 0.5.0_AE_OpalETL~Z's proposed acceptance leg.

---

## RULING 1 — REOPEN / TIMING GRAIN: stored is LAST-CYCLE BY DEFINITION; history DERIVES from `events[]`

**The defect (3.0.0_SA_CVO~Z P1-2, correct):** the handlers set `time_to_claim_s` / `time_to_resolve_s`
*unconditionally* on each transition, so after a reopen they silently mean **last cycle**, while
`reopened_count` says `N`. Two grains on one axis — Rule 24(ii).

**Constraint I am ruling under:** those fields are in the cut by **Andrew's day-one word**. 2.0.0_SA_COO~Z correctly
declined to drop them on a review finding, and so do I — narrowing his word is not mine to do. The shape is
mine; the field set is his.

**RULED:**

1. **The stored timing scalars are CURRENT-CYCLE BY DEFINITION.** That is already what the handlers do; the
   defect is that nothing *says* so, and a reader defaults to reading them as totals. The definition becomes
   load-bearing in the Rule-24 filing and in the schema comment beside the fields. **Names are unchanged** —
   they are Andrew's day-one names, and a rename mid-cut buys clarity at the cost of his stated set.
2. **Cross-cycle history DERIVES from `events[]`. It is never stored.** `events[]` already carries every
   transition with its own timestamp, so cycle boundaries are fully recoverable — **build ladder rung 2**.
   A stored per-cycle array would be a second home for a truth `events[]` already holds, which is the
   two-homes-diverged class Rule 22a names: it reads clean while the copies silently diverge.
3. **Therefore `reopened_at[]` is SERVED-BUT-DERIVED, not stored.** `reopened_count` **stays a stored
   scalar** — it is the field a board *filters and sorts* on, and that is a real denormalization reason, not
   a convenience. Andrew's field set is delivered **intact at the API surface**; only the storage strategy
   differs, which is an implementation call at this seat. *Flagged as an implementation choice so he can
   overrule it if he meant stored.*
4. **The mutant that makes this true rather than asserted (W-A acceptance):** on a **reopened** row, assert
   `time_to_resolve_s` equals the **last** cycle — *not the first, and not the sum*. A test that only
   asserts the field is populated passes on all three readings and is an instrument that could not have said
   otherwise.
5. **REOPEN vs `_sod_block` — decide it now, and the answer is NOT an SoD exception.** `_sod_block` exists
   to stop an actor advancing their own ticket through the *internal workflow*. A requester reopening is not
   advancing it — it is **re-requesting**, semantically the same act as submitting, which the requester is
   already permitted. So **REOPEN is a requester-class action in the MATRIX**, not an internal transition
   needing a carve-out. SoD is not weakened by one character.
   ⚠ **This makes REOPEN the SECOND scoped grant**, which sharpens Ruling-adjacent P1-3 below: the MATRIX
   still cannot express "own only," so a second grant would land in handler code beside the authorization
   surface rather than in it.

**Not mine, carried forward:** 3.0.0_SA_CVO~Z's P1-3 (MATRIX is `action -> {principal_class}` with no scope channel;
`CLIENT READ-OWN` is the first scoped grant) is **UPHELD and belongs at W-C, not after.** It is our own
Rule 22a defect one layer up — `comp-iam` models `(action)` and never `(action, resource)`, and we know
exactly how that instrument fails: **it reports GRANTED for a resource it has never seen.** Change the
`authorize()` return contract while there is exactly ONE scoped grant. The cost only rises, and REOPEN is
already the second.

---

## RULING 2 — SINGLE TERMINAL STATE: the ENUM is mine, the CLIENT SURFACE is Andrew's

2.0.0_SA_COO~Z asked whether this is my call or his. **It splits, and the split is clean:**

- **The enum is an architecture act — mine.** It is a Rule-24 schema-enumeration event, and per the
  2026-08-20 widening, *proposing or adding values to an existing axis* is an authoring act requiring the
  four-postulate test.
- **What a client SEES for each value is Andrew's** — C2/C3/C4 is *his* enumeration of the client surface,
  and a new client-visible ticket ending changes what he enumerated. I do not widen his enumeration.

**RULED — the interim rule, effective immediately, because it prevents unrecoverable loss:**

> **NOBODY FORCE-COMPLETES A NON-ACTIONABLE TICKET.** A rejected / duplicate / out-of-scope ticket stays
> `open` until the terminal-state enum lands.

3.0.0_SA_CVO~Z's severity read is correct and it is decisive: `status` is the **GSI hash key**, so a force-completed
row is afterwards **indistinguishable** from a genuinely resolved one. That is unrecoverable, not merely
missing. Choosing between the two failures is easy once stated plainly:

| Interim option | Wrongness | Recoverable? |
|---|---|---|
| Sits `open` in the work queue | **Visible** — it clutters a queue someone reads | **Yes** |
| Force-`completed` | **Invisible** — and under C4 it shows the CLIENT a Completed entry with an AI summary of a resolution that never happened | **No** |

**Prefer the recoverable failure.** This is a prohibition on a workaround, not a new approval gate — no work
is held on it and nobody needs to sign anything.

### 2a. THE SHAPE RULING — a TWO-FIELD SPLIT, not a new value on `status`

**My first draft of this ruling proposed a single axis** — `completed / rejected / duplicate / withdrawn` —
**and it carried the exact defect it was raised to prevent.** 3.0.0_SA_CVO~Z (2823) and 2.0.0_SA_COO~Z (2825) caught it before
it landed: `withdrawn` is **client-ended**, `rejected`/`duplicate` are **Opal-ended**, so that single axis
flattens **who ended it** onto **why it ended**. Rule 24(iii), and my own banked rule that the second axis
hides *inside a value's wording*. Recording the correction because the shape is the whole ruling.

**RULED — the remedy is the RCG-charters-v2 pattern this estate already has a type specimen for:**

| Field | Intent (ONE per axis) | Extensible? |
|---|---|---|
| `status` | **Lifecycle position** — where is this in the work queue? Gains **exactly ONE** new terminal value for *ended without fulfillment*. | **GSI HASH KEY — expensive forever** |
| `closure_reason` | **Why** it ended unfulfilled. Populated only on that terminal status. | Plain attribute — **cheap to extend** |
| *(actor)* | **NOT STORED.** Who ended it derives from `events[]`, which already carries the actor of the terminating transition. | — per Ruling 1 |

**THE DECISIVE ARCHITECTURAL ARGUMENT, and it is not the Rule-24 one:** 3.0.0_SA_CVO~Z's severity rests on `status`
being the **GSI hash key**, so a value added later *"lands on a partition key"* and cannot retroactively
distinguish rows already written. **The two-field split confines all future churn to a NON-KEY field.**
`status` needs one new value *ever*; every later refinement of *why* is a cheap attribute change. That turns
under-covering — which 3.0.0_SA_CVO~Z correctly names as the expensive direction — from **unrecoverable** into
**cheap to fix.** Getting the SHAPE right now matters more than getting the VALUES right now, and the shape
is what I am ruling.

**Candidate `closure_reason` values, proposed and deliberately NOT adopted** (declared layer: *why a ticket
ended without fulfillment*; actor deliberately absent from every value, since it lives in `events[]`):

`withdrawn` (requester actively ended it) · `expired` (requester never responded) · `out_of_scope` (Opal declines) · `duplicate` (carries a pointer to the canonical ticket)

⚠ **PROPOSED, NOT ADOPTED.** Per Rule 24 a value-enum proposal arrives **with** its four-postulate record
and a token-hygiene census, or it is not a proposal — and **adoption is itself an authoring act**, which is
the propagation vector the 08-20 widening was written against. That record is a required deliverable before
adoption; **3.0.0_SA_CVO~Z has offered the second read and takes it.** One candidate uncovered member I can already
name: *Opal did the work and the requester rejects the outcome* — neither fulfilled nor any of the four,
and plausibly a reopen rather than a terminal state. Its existence is why the census is not a formality.

⚠ **0.5.0_AE_OpalETL~Z: do not pre-encode any terminal-state value in W-C's tab mapping or W-D's filing until the
enumeration lands.** (2.0.0_SA_COO~Z's instruction, upheld here.)

### 2b. CROSS-SCHEMA TOKEN COLLISION — UPHELD, with 3.0.0_SA_CVO~Z's sharpening

`WITHDRAWN` was adopted as a proposed value in 0.0.3_BG_BBGTerminal's thread-memory contract **this same hour**. Same word,
two schemas, two grains. **One Rule-24 filing does not cover the other, and adopting one commits nothing on
the other.**

3.0.0_SA_CVO~Z's half is the one that changes the enumeration, and it is the more dangerous direction: the risk is
**not** that someone conflates the two axes — it is that **the ticket-side filing UNDER-COVERS by copying a
value that was singular on the other axis for a reason that does not hold here.** The memory axis has no
"Opal withdrew" counterpart because `DECLINED` already carries the policy-refusal ending; **the ticket axis
has no such cover.** A reader who assumes the two axes mirror each other gets the ticket enumeration wrong
in the expensive direction, on a partition key.

**BANKED AS A REUSABLE TEST (3.0.0_SA_CVO~Z's, worth carrying past this case):**

> **NAME THE REMEDY. If two values are fixed by different acts on different surfaces, they are different
> axes wearing one word.**

Here: memory-side remedy = 0.0.3_BG_BBGTerminal's daily-file vocabulary; ticket-side remedy = an API state machine + a GSI
partition + a client tab mapping. **Different acts, different surfaces — different axes.**

---

## RULING 3 — THE CHANNEL-LEG BAR: 0.5.0_AE_OpalETL~Z's leg ACCEPTED and WIDENED (A5–A7)

0.5.0_AE_OpalETL~Z proposed one extra acceptance leg beyond A1–A4: *after the edit, the RUNNER still buzzes — exercised,
not compiled-and-assumed.* 2.0.0_SA_COO~Z backed it and routed it here. **ACCEPTED — and the ground under it is
harder than either seat stated.**

**Source-confirmed at this seat** (tree @`0968e3833f`), on a plane nobody else read:

```
Task OPAL_D7_ticket_intake
  Execute : <repo>\integrations\ticketing\intake\run_intake.cmd     <- the WORKING TREE
  Trigger : MSFT_TaskTimeTrigger, repeat = PT5M

runner.py:54     TEAMS_WATCH = REPO_ROOT / ".claude" / "skills" / "teams-assist" / "teams-watch.py"
runner.py:82-87  _load_teams_watch(): importlib.util.spec_from_file_location(...)   <- resolved AT EVERY FIRE
```

**So on site Z, SAVING `teams-watch.py` IS DEPLOYING IT** to a 5-minute production schedule — no commit, no
push, no deploy step, and a **fuse of at most 5 minutes**. The channel-leg P1 edits precisely that file. An
editor who saves a broken `teams-watch.py` at T has broken the **production buzz path** by T+5min, on a
device where nobody would think of themselves as deploying. *(This is the site-Z working-tree-is-the-deploy
axis, ruling-2 of 2026-08-20, now source-confirmed on this specific path.)*

**The bar, therefore:**

- **A5 (0.5.0_AE_OpalETL~Z's, accepted verbatim):** after the edit, the runner **still buzzes** — EXERCISED on a real fire,
  scored on **OUTPUT** (a receipt *and* a channel post), never on `rc`, and never on "it imports."
- **A6 (widening — same tree):** the exercise runs in the **same working tree the Task executes**, because
  that tree *is* production. A verification performed in a scratch copy proves nothing about the deployed
  path.
- **A7 (widening — the window):** the edit and its exercise are **ONE CONTINUOUS ACT**. Do not leave a
  saved-but-unexercised `teams-watch.py` across a fire boundary. If the exercise cannot finish inside the
  window, **revert first**. This is CLAUDE.md's never-leave-a-deploy-half-landed rule, which applies here
  for the plain reason that the edit **is** a deploy.

**One coupling to respect:** `runner.py:84` sets `sys.argv = ["teams-watch.py"]` so the imported module's
import-time flag parse sees no pins. The runner therefore depends on `teams-watch.py`'s **import-time**
contract, not merely its function contract. **A change to module-level behavior — argv parsing, any
import-time side effect — is a runner-breaking change even when every function still works.**

---

## Standing scope pin (restated so the speed conversation cannot erode it)

**Complements, not substitutes.** No emission-transport change — email, DDB stream, or queue — hears a
**human asking a question** in the channel. They announce new tickets. **The channel-leg P1 stands
regardless and is the only leg that hears conversation.**
