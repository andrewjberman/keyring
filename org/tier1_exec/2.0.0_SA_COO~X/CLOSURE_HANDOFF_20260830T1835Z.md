# CLOSURE HANDOFF -- `2.0.0_SA_COO~X` -- 2026-08-30T18:35Z

Written on Andrew's ~18:2xZ edict, **for a successor with zero context**. His words as other seats
recorded them were *"these continued works"*: **the edict closes a CONTEXT, not the work.** Nothing below
is cancelled, completed early, or narrowed, and no project is marked done on the strength of it.

⛔ **I NEVER RECEIVED THE EDICT DIRECTLY.** No frame carrying it reached this seat's inbox. I acted on it
because the git trunk — the channel of record — carries three seats' closure commits citing it at 18:28Z,
and because the broker's known return-path defect makes a missing frame entirely ordinary today. **A
successor should treat the edict's exact wording as second-hand from this seat and read it at its source.**

Every abbreviation is expanded and no message id is load-bearing. Read the sections in order.

---

## 1. WHAT THIS SEAT IS

`2.0.0_SA_COO~X` — the laptop COO lane running two cron-fired loops, both armed on Andrew's own word:

- **`/drive NFRA_C3MATERIALIZE`** — scope is that one project. "Completing" means the PRD's section-6
  falsification tests, never milestones.
- **`/drive D11`** — the ACTUATE half of a DRIVE PAIR with `1.0.0_SA_CTO~X`'s `/self-drive D11`. Scope is
  the D11 register predicate re-resolved each tick from `org/missions/DIRECTIVES.yaml`
  (currently `NFRA_SUBSTRATECARDING` + `NFRA_C3MATERIALIZE`). **An empty tick is LEGAL here** — that is
  the designed exception, not a lapse.

**Both clauses were LIVE at this write** (`org/XXX.md`, the COO row and the CTO row). A successor re-arms
from those rows and nowhere else. The stop condition is the clause struck or the project reading
`status: complete`.

## 2. WHAT IS DONE, with the pin and the instrument that closed it

| Thing | Pin | Closed by |
|---|---|---|
| sec-7b FACE 1 (the MEASUREMENT unit) | `36846ac64d` | joint FINAL FACE PASS ON ORIGIN, CRO 16:48:37Z + CVO 16:50:48Z |
| sec-7b certified record | `97ccacce00` | joint FINAL PASS ON ORIGIN, 16:42:35Z / 16:44:54Z |
| `NFRA_SUBSTRATECARDING.TO-CARD-R-COO` | `0de7268029` | joint proof close ON ORIGIN; **uncarded_20 class CLOSED 20 of 20** |
| sec-7a THE BRIDGE DETERMINATION, whole 14(e) round | `b48dfbbd19` | JOINT RECORD CLOSE ON ORIGIN, CRO 18:18:42Z + CVO 18:19:00Z |

The sec-7a round in one line: c0 `7e3a5168ef` (17 cells, 4 planes) -> seal `8249f5fb3e` -> **two
independent blind nominations 28 s apart, both correct, each naming its instrument** -> SCORE **HIT**
`6cda40124f` -> separate CRO + CVO artifact PASS -> joint close -> certified record.

## 3. WHAT IS IN FLIGHT, AND EXACTLY WHERE IT STOPS IF NOBODY TOUCHES IT

**THE 7A DETERMINATION FACE — `NFRA_C3MATERIALIZE.TO-L3S7A-CCY.determination`, committed `91c71a475f`,
status `pending`, NOT DELIVERED.** It sits with `3.0.0_SA_CVO~X` and `4.0.0_SA_CRO~X` for certification.
The repair contract they wrote says **certification precedes delivery to the seat**. If nobody touches it:
the face stays `pending`, `0.8.0_AE_CloudComp~Y` stays idle with nothing owed, and no measurement happens.
**The successor's act is: read the certifiers' verdict, then deliver — do not deliver before it.**

**What that unit is for, since the name misleads:** it is called the DECLARATION unit in the allocation,
but the ruling makes its deliverable a **DETERMINATION with three legal outcomes** — `OUTCOME_A`
(declarable), `B-NO-DECLARED-RELATION-YET` (closable, the store's owner), `B-REFUSED-BY-1-OR-4` (not
closable inside D11, a scope question). ⛔ **ACCEPTANCE IS ON THE MEASUREMENT AND THE TYPING, NEVER ON
WHICH OUTCOME APPEARS.** A face whose acceptance is "a declaration exists" pays for outcome A and a seat
paid for outcome A will find one. **Do not let anyone re-word that line.**

**`NFRA_SUBSTRATECARDING` W4-COX** — `0.7.0_AE_CloudOps~X` is at card 4 of 7 (cards 1-3 jointly closed).
The class close is the ISSUER's act at 7 of 7 and is not due yet. Three subjects remain after card 4:
`cse_test_24458e6c`, `cse_test_bb57a916`, `ms_heat_snap`.

## 4. WHAT THIS SEAT OWES, BY SERIAL

**Nothing, as of this write.** Every dispatch fired is answered or is with a certifier. The only
outstanding obligation is the successor's: deliver the 7A face to `0.8.0_AE_CloudComp~Y` **after** the
certifiers rule, and close the `w4_remote` class at 7 of 7.

## 5. WHAT IS CLOCK- OR EVENT-GATED

- **sec-6 tests 6.1 / 6.2 / 6.5: OUTSTANDING, all on L4 identity existing.** ⛔ **6.2 is the only one
  whose cost is NIGHTS rather than work** — it needs N >= 20 SCHEDULED nightly runs, N declared in the PRD
  **at the L4 cut, before the first run** (a bar set after its data is a fit). Earliest sec-6 completion is
  therefore (L4 cut date) + N nights, and **every day L4 slips, that slips with it.**
- **The `after-bridge-declared` gate is OPEN and only OUTCOME_A moves it.** A typed refusal closes the
  UNIT and leaves the GATE open. **Do not plan a follow-on cut of the four consumer cells contingent on
  the determination unit closing** — they are contingent on the gate DISCHARGING, and a plan written the
  other way sits there as an act that silently never fires.
- **The gate is blocked on a store-side capability that does not exist** (`declared_by_store` NO over
  16,397 portal edges, none targeting a Module) — portal-graph work **outside D11's scope with no owner
  inside it.** That is a programme fact, not a task.

## 6. WHAT IS UNVERIFIED, AND WHERE I WAS WRONG

A closure log that reads uniformly clean is the one to distrust. Mine does not.

**Four errors of mine today, each self-found or peer-found and each corrected:**
1. I wrote a **FALSE CLAIM into my own scorer** — that its digest had been pre-published to the certifiers
   when it never was — and removed it before the scorer ran. A claim about my own rigour that the rigour
   did not cover.
2. A drive log of mine claimed a cut was "unblocked" when the unit had **no cell basis at all**; found by
   trying the cut, not by re-reading my sentence.
3. A **negative control was contaminated** — my "bogus" hex probe is a live test fixture, returning 1
   where 0 was required.
4. My cutter **hardcoded a verdict AND made the selftest require it**, so it went stale on the joint close
   and its own check passed. `3.0.0_SA_CVO~X` caught it before any face was written.

**THREE MUTANTS OF MINE WENT BLIND TODAY** when the artifact's format moved past their anchors — each
mutated nothing and **reported as a PASS**. A battery cannot tell you an arm has stopped biting. If you
inherit any battery of mine, **re-verify that each mutant still changes the text** before trusting a count.

**Other unverified things:** both dead-seat verdicts today rest on ONE seat's process-table instrument.
The broker's return path lies (writes land, the caller is told they failed) — **never record "not
delivered" from a return value; read the store.** And this seat's `[STUCK]` at 18:12Z was answered by the
integrator taking the fault on itself; a successor should not read that as a standing entitlement to
escalate at 3 ticks without re-measuring.

## 7. THE TWO PROCESS RULES I ADDED TODAY — keep them or kill them deliberately

- **The scorer pre-commitment is a GATE, not a habit.** `seal_7A.py` REFUSES unless the scorer exists, and
  stamps its digest into the seal record, so a scorer cannot be shaped to a nomination. Adopted from
  `1.0.0_SA_CTO~X`: *"nobody should have to want it."*
- **A certified rendering goes to its own file, never over the authoring draft** — that removes the
  feedback path that grew a 7B file from 165 to 437 lines, rather than guarding against it.

**Placement, MEASURED:** origin/CLOUD `89edf8efc1`. This log and `91c71a475f` are LOCAL and ride the next
integration window. Push is the integrator's act, never this seat's.
