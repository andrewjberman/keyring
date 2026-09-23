# AMGT_RESAPP round 35, ADDENDUM 4 -- blocker B CORROBORATED on my own instrument; the GRADE stands and my CAUSAL SENTENCE does not

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-23T06:5xZ, LOCAL on SITEZ. **Vintage:** `c56cc0c48c`.
**Corrects:** `ADJUDICATION_v39`'s causal sentence. **Grade impact:** none, and that is a RULING, not a waiver.

## 1. ⭐ BLOCKER B, MEASURED HERE -- NOT ADOPTED

`2.0.0_SA_COO~Z` reports a second blocker none of the three of us named. **I ran it myself rather than take it:**

| claim | my read |
|---|---|
| `_hk_national_regulator` cannot win on ANY branch | **5 return paths, 5 carrying `"passed": False`** -- `:1281`, `:1292`, `:1303`, `:1316`, and **`:1333`, the branch where the search SUCCEEDS**, which carries `"seeds": seeds` |
| the seeds have no reader | `seeds = []` at `:1441`; passed **by reference into STEP 4's lambda** at `:1449`; **step 5 runs at `:1451`, after it**; `run_battery` appends step 5's seeds at `:1460-1462` -- **into a list whose only consumer has already executed** |
| a win cannot propagate | winner set only on a passing step (`:1463`), so the run falls to `:1473`/`:1476` and the object is built from `attempts` alone |

⛔ **CONFIRMED on a different instrument than the one that produced the claim. The route has TWO stacked blockers
and every one of us reported the first as the whole cause.**

## 2. RULING: NO CRITERION'S PASS IS FALSIFIED -- ROUND 35'S GRADE STANDS

⛔ **This is mine to decide, not the issuer's to waive, and I decide it per criterion rather than accept the
frame:** AC2 asked for HERMETIC dispatch and the declared return shape -- **the adapter does dispatch and does
return it**; AC3 exercised test (c) on the acceptance path with a fixture -- **unreached by B**; AC4 bounded ONE
live fetch with counters -- **unreached by B**. ⭐ **Blocker B makes no PASS wrong. The cell was cut to build a
dispatching, guarded, negative-controlled route and it built one.**

⚠ **What IS wrong is the CAUSAL SENTENCE, and mine carried it:** `ADJUDICATION_v39` wrote *"the route is built,
dispatches correctly ... and it returns nothing for Lenovo"*, attributing the failure to the search alone. **That
sentence is struck. The route returns nothing for Lenovo AND could not have won had the search returned records.**

## 3. ⭐ THE CLASS, AND THE PART I ADD TO IT

`2.0.0_SA_COO~Z`'s form is right: **when a route fails at the FIRST of two stacked blockers, the second is
invisible to every instrument aimed at the route, because the route never reaches it.** Rule 22's
shared-dependency blindness rotated -- not a defect BENEATH the members, but one DOWNSTREAM OF THE STOP.

⛔ **AND THE HALF THAT MAKES IT WORSE HERE: BLOCKER B WAS DECLARED IN THE GRADED ARTIFACT'S OWN DOCSTRING**
(`:1267-1272`: *"this order's egress bound is ONE live HKEX fetch, already spent on the search ... and no branch
here ever wins"*). ⭐ **The worker implemented the bound correctly and SAID SO. Three seats read that file -- one
to write the packet, one to write the analysis, one to grade -- and none of us read that sentence.** ⚠ **Once a
MEASUREMENT exists (`recordCnt=0`), attention goes to the number and a plain declaration a few lines away stops
being read: it is not hidden, it is UNATTENDED.** **Remedy: when an artifact carries both a measurement and prose,
read the prose for what it says about the NEXT step, not for what it says about the measurement.**
**COST: one read past the failure point. NON-APPLICATION: a route with a single failure mode already proven
exhaustive.**

⭐ **Round 36's `AC5` -- the win must PROPAGATE, deliberately not implied by `AC4` -- is the correct mechanical
answer and it is already cut. I will grade it on exactly that separation.**

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S410",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-23T06:58Z",
    "one_line": "CORROBORATES blocker B on this seat's own instrument (5 of 5 return paths in _hk_national_regulator carry passed False, including the search-success branch at :1333; its seeds go to a list whose only reader, step 4, has already run) and RULES that no round-35 criterion's PASS is falsified -- AC2 asked for hermetic dispatch and the declared shape, AC3 and AC4 are unreached by B -- so the grade stands while ADJUDICATION_v39's causal sentence, which attributed the failure to the search alone, is STRUCK.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "battery.py _hk_national_regulator :1252-1340: 5 return statements, 'passed': False at :1281, :1292, :1303, :1316 and :1333 (the search-success branch, carrying 'seeds': seeds).",
        "run_battery: seeds = [] at :1441, passed by reference into step 4's lambda at :1449, step 5 invoked at :1451 after it, step 5's seeds appended at :1460-1462 with no later consumer; winner set only at :1463, so the run falls to :1473/:1476.",
        "The round-35 deliverable's own docstring at :1267-1272 declares that the egress bound is one fetch already spent and that no branch here ever wins."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "A packet's causal sentence names every blocker on the path it describes.",
    "world_is": "The route carries two stacked blockers; all three seats reported the first as the whole cause, and the second was written in the graded artifact's own docstring.",
    "notes": "THE ADDED HALF, mine: the second blocker was not hidden, it was UNATTENDED -- once a MEASUREMENT exists (recordCnt=0) attention goes to the number and a plain declaration a few lines away stops being read. Remedy: read an artifact's prose for what it says about the NEXT step, not about the measurement. COST one read past the failure point; NON-APPLICATION a route with a single failure mode already proven exhaustive. THE GRADE IS A RULING, NOT A WAIVER: I decided it per criterion rather than accept the issuer's frame, and round 36's AC5 (the win must PROPAGATE, not implied by AC4) is the correct mechanical answer and is already cut.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W128-S1"
    ],
    "dismissal_reason": "A correction-of-record row: it strikes this seat's own causal sentence, corroborates the second blocker on an independent instrument, and rules that no criterion's PASS moves."
  }
]
```
