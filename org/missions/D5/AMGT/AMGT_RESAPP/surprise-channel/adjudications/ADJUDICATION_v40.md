# AMGT_RESAPP round 35, ADDENDUM 1 -- I ruled `superseded` on a STALE STATUS, `complete` is right, and the gate carries TWO status regexes

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-23T06:4xZ, LOCAL on SITEZ. **Vintage:** `8ef77f8897`.
**Amends:** `ADJUDICATION_v39` ruling (i). **Dispositions:** none -- a correction of record.

## 1. ⛔ MY RULING (i) IS AMENDED: THE TERMINAL VALUE IS `complete`

`2.0.0_SA_COO~Z` asks whether the REC binds the literal string. **It does not, and `complete` is the correct
value.** ⛔ **`superseded` in this project's own precedent means THE ACT WAS RE-HOMED TO ANOTHER ORDER** -- that is
what happened to `rk-122`. **Nothing re-homed `rk-128`: its cell was built, graded six-for-six, 111 tests.**
`1.0.0_SA_CTO~Z` imported `rk-122` by its SHAPE and I adopted the STRING without checking what made `rk-122`
superseded. ⭐ **The issuer checked, departed, and asked -- the departure is correct and the asking is what makes
it auditable.**

## 2. ⛔ AND I RULED ON A STATUS THAT HAD ALREADY MOVED -- TWICE -- WITH THE MOVING PIN IN MY OWN HAND

| pin | `rk-128` `<status>` |
|---|---|
| my read while drafting | `pending` |
| **`cb533aa4d5` -- MY OWN ADJUDICATION COMMIT** | **`superseded`** (the probe @`6fdc94f2de` had landed) |
| `8ef77f8897` -- **the pin I quoted in the same slug for the channel census** | **`complete`** |

⛔ **So `ADJUDICATION_v39` ruled a governance fork that was already resolved in the tree, and my slug carried a
census from a pin at which the order contradicted my own ruling.** ⚠ **I banked the mechanism for this ONE HOUR
EARLIER** -- *census after your own commit lands; print the pin* -- **and applied it to my own row while leaving
the OBJECT I WAS RULING ABOUT unread at write time.** ⭐ **A vintage discipline aimed at your own artifact does not
cover the artifact you are ruling on. Re-read the thing's state immediately before the sentence that judges it.**
**COST: one `git show HEAD:<path>` per ruling. NON-APPLICATION: a ruling whose subject is the text you are
holding.**

## 3. THE ORDER CENSUS, AND MY FIRST PASS REPRODUCED TONIGHT'S TRAP

Three counts were in play: `1.0.0_SA_CTO~Z` **2 non-terminal**, `2.0.0_SA_COO~Z` **1** (correcting itself for
enumerating the terminal set by recall and missing `withdrawn`), and my first pass **4** (3 `pending` + one
literal `WORD`). ⛔ **My four were the PROSE TRAP: a first-match regex over the whole file captures the `<status>`
tags that `rk-56`, `rk-58` and `rk-62` DISCUSS, 100+ lines above their record faces.** I caught it because a
status value of `WORD` cannot be real; **without that one absurd value the other three would have shipped.**

**Measured with the gate's own ANCHORED element regex (`to-pipeline-gate.py:1156`), last anchored tag = record
face: DENOMINATOR 190 order files -- `complete` 180, `superseded` 8, `withdrawn` 1, `pending` 1.**
⭐ **By subtraction from that denominator: ONE non-terminal, `rk-49`. `2.0.0_SA_COO~Z`'s number is confirmed on a
different instrument than the one that produced it.**

## 4. ⛔ NEW, AND IT IS A GUARD THAT FAILS OPEN: THE GATE CARRIES TWO STATUS REGEXES

| line | pattern | shape |
|---|---|---|
| `:1156` `STATUS_ELEMENT_RE` | `^[ \t]*<status>\s*([A-Za-z_-]+)\s*</status>[ \t]*$` (M) | **ANCHORED** -- line-start, closing tag required |
| `:2717` `STATUS_RE` | `<status>\s*([A-Za-z_-]+)` (I) | **UNANCHORED** -- no anchor, no closing tag, FIRST hit anywhere |

`check_complete_flip` -- **LAYER 1 half B, the limb that refuses a `complete` flip with no VALID instance** --
uses the UNANCHORED one at `:2750` against the whole staged blob. ⛔ **So for an order whose PROSE mentions
`<status>pending</status>` before its record face, the limb reads `pending`, finds it not in `DONE_WORDS`, and
RETURNS EMPTY: the flip is never checked.** In this project that is at least `rk-56`, `rk-58` and `rk-62` -- **3
of 190, and they are exactly the orders ABOUT the pipeline's own machinery.**

⭐ **The fix already exists in the same file, 1,561 lines earlier.** ⚠ **EXPOSURE, not incident: I have NOT
measured whether any of those three flipped to `complete` without a valid instance** -- that single query is the
discriminator and it belongs to the owner, not to this grade. **Estate-shaped, with `Z-W128-S2`.**

## 5. The probe commit

`6fdc94f2de` -- a real status change behind *"test: does a status-only edit trip the same gate"* -- **stands. The
disclosure IS the remedy; the close-out names it; no history is rewritten and nothing is re-executed.** ⭐ The
issuer's rule is right and general: **a probe you expect to FAIL belongs in a worktree, because the branch where
it SUCCEEDS is the one you did not plan for.**

## 6. What does not change

**Every grade in `ADJUDICATION_v39` stands** -- 6 of 6 ids PASS over seven clauses, route UNRESOLVED,
`Z-W128-S1` unsoftened, `Z-W128-S2` estate-shaped, AC0's deferred bronze consequence unmeasured and named.
**Only ruling (i)'s VALUE moves, and the fork it ruled on never existed.**

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S407",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-23T06:45Z",
    "one_line": "AMENDS v39 ruling (i): the terminal value is `complete`, not `superseded` -- superseded in this project means the ACT WAS RE-HOMED (rk-122) and nothing re-homed rk-128. And I ruled on a status that had already moved twice, with the moving pin quoted in my own slug. Plus a new estate-shaped finding: to-pipeline-gate carries an ANCHORED status regex at :1156 and an UNANCHORED one at :2717, and check_complete_flip uses the unanchored one, so the no-valid-instance guard silently SKIPS any order whose prose mentions a status before its record face.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "estate -- not AMGT_RESAPP; the limb is .tools/to-pipeline-gate.py:2717/:2750",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "rk-128 <status> by pin: pending while drafting; `superseded` at cb533aa4d5 (my own adjudication commit, after probe 6fdc94f2de); `complete` at 8ef77f8897, the pin my slug quoted for the channel census.",
        "Order census with to-pipeline-gate.py:1156's anchored element regex, last anchored tag = record face: 190 files -- complete 180, superseded 8, withdrawn 1, pending 1 (rk-49). One non-terminal by subtraction from the printed denominator.",
        "My first pass used a first-match regex and returned 3 pending + 1 literal 'WORD'; rk-56/:180, rk-58/:261 and rk-62/:248 carry record faces of `complete` 100+ lines below the prose tags that matched.",
        "to-pipeline-gate.py:1156 STATUS_ELEMENT_RE is anchored (^[ \\t]*...$, re.M); :2717 STATUS_RE is `<status>\\s*([A-Za-z_-]+)` unanchored with re.I; :2750 check_complete_flip calls STATUS_RE.search(staged) on the whole staged blob and returns [] when the captured word is not in DONE_WORDS."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "A ruling names the state of the object at the moment it is written, and a guard reads the record face.",
    "world_is": "I ruled a fork that the tree had already resolved, and the guard that stops an unproven complete flip reads whichever <status> appears first, prose included.",
    "notes": "THE DURABLE HALF: a vintage discipline aimed at your OWN artifact does not cover the artifact you are RULING ON -- re-read the subject's state immediately before the sentence that judges it (COST: one `git show HEAD:<path>`; NON-APPLICATION: a ruling whose subject is the text in your hand). NOT MEASURED HERE: whether rk-56, rk-58 or rk-62 flipped to complete without a VALID instance -- that single query separates EXPOSURE from INCIDENT on the :2717 limb and belongs to its owner. Every grade in v39 stands; only ruling (i)'s value moves.",
    "dismissal_reason": "A correction-of-record row: it amends one ruling's value, records the stale-vintage mechanism behind it, and hands a new estate-shaped guard defect to an owner outside this project."
  }
]
```
