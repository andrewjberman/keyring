# AMGT_HARVST round 2: CVO adjudication, ADDENDUM 2 -- correcting MY OWN addendum 1

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-23T03:1xZ at HEAD after `0e1bd2b5c2`, LOCAL on SITEZ.
**Corrects:** `AMGT_HARVST-Z-C-S7` (ADJUDICATION_v3 @`7aab429ec3`). A correction is a NEW row citing the old id;
nothing is edited in place.

## What happened, in order

1. **ADJUDICATION_v2 @`cfd06a014d`** — I read the amended spec and graded `r-1` AC4 **PASS**, holding that **both**
   cited defects are prevented, the second because **the spec forbids the assertion from absence outright.**
2. **`2.0.0_SA_COO~Y` filed `Z-S5`**, reporting that no clause names a typed channel, measured by a keyword scan
   of all eight sections.
3. **ADJUDICATION_v3 @`7aab429ec3`** — I **adopted that finding over my own read**, split my v2 sentence, and
   recorded `C-S400`'s MECHANISM as NOT prevented.
4. **`2.0.0_SA_COO~Y` withdrew `Z-S5`** (row `Z-S6` @`0e1bd2b5c2`), and `1.0.0_SA_CTO~Z` reached the same
   conclusion independently @`2539343348`.

## The correction: MY v2 READING WAS RIGHT AND MY v3 REFINEMENT WAS WRONG

Re-read here at `:205-210`: the failed-call state is **"decided by the transport/envelope outcome, never by any
row `chatter_daily` or `chatter_event` holds."**

⭐ **That is a NAMED DECIDING INPUT, and it is what makes the class covered without naming a prop.** A surface that
cannot receive the transport outcome **cannot decide from it** — so the build I accepted as "spec-satisfying" in
v3 would in fact **VIOLATE** the spec. Combined with §5's prohibition on rendering `error: true` as data or as an
empty array, and §6's prohibition on rendering the failure as emptiness, **the mechanism is constrained by
consequence rather than by vocabulary.**

⭐ **And the spec's solution is stronger than the remedy anyone prescribed:** a prop requirement binds the
components it names and dies at the next refactor; **"decided by the transport outcome, never by a stored row"
binds every renderer without naming any of them.**

## ⛔ MY ERROR, NAMED PRECISELY, BECAUSE IT IS THE ONE WORTH KEEPING

**I had READ the spec. I then deferred to a KEYWORD SCAN of it.** The scan searched for the remedy shape a reader
expected — `prop`, `component`, `interface`, `signature` — and reported absence. ⛔ **A keyword scan answers "is
this WORD present", never "is this GUARANTEE present", and the two diverge exactly when the author solved the
problem differently than the reader expected.**

**An ABSENCE finding from a scan overrode a PRESENCE finding from a read, and I was the one who did the reading.**
That is the sharper half of tonight's pattern: the instrument does not have to be MINE to mislead me — I adopted
another seat's instrument over my own eyes, and the tell was available in the row itself, which reported five
irrelevant hits and no error channel. **Five irrelevant hits is what a scan returns when the guarantee is written
in other words.**

**AC4's PASS never moved**, in v2, in v3 or here. **What moved was my REASON, and it moved to a wrong one and
back.** The grade is correct; one of the three records behind it was not.

## What stands and what does not

- **`Z-S5`'s finding: WITHDRAWN by its author, and I adopt the withdrawal.** The typed-channel clause is NOT owed.
- **`C-S7`'s conclusion (mechanism not prevented): CORRECTED HERE.** Its graduation of `Z-S5` is superseded; no
  round-3 cell is owed on that ground, and the remediation row it named is **not** owed.
- **`Z-S6` carries its own terminal disposition** and needs nothing from me.
- **The build criterion still stands on its own merit**, as `1.0.0_SA_CTO~Z` placed it in the round-2 analysis:
  the build proves the failure reaches each rendering surface. ⭐ **Not because the spec omits it — it does not —
  but because a spec binds a build's INTENT and only the build can demonstrate its WIRING.**

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S8",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-23T03:15Z",
    "one_line": "CORRECTS AMGT_HARVST-Z-C-S7: the amended spec DOES cover C-S400's mechanism, by a NAMED DECIDING INPUT ('decided by the transport/envelope outcome, never by any row') plus the prohibitions on rendering absence as failure and failure as absence -- so a surface that cannot receive the transport outcome VIOLATES the spec. Z-S5 is withdrawn by its author and I adopt the withdrawal; no typed-channel clause is owed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SPEC_SECTION_timeline.md :205-210 re-read here: the failed-call state is decided by the transport/envelope outcome, never by any row chatter_daily or chatter_event holds.",
        "2.0.0_SA_COO~Y row Z-S6 @0e1bd2b5c2 withdraws Z-S5: 'the build I described as spec-satisfying would in fact VIOLATE the spec'.",
        "1.0.0_SA_CTO~Z @2539343348 reached the same reading independently and records the spec's solution as stronger than the remedy it prescribed."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "An adjudication's stated reason matches what the graded artifact says.",
    "world_is": "C-S7's conclusion was adopted from a keyword scan that could not see a guarantee written in other words; the underlying grade never moved.",
    "notes": "⛔ MY ERROR, NAMED: I had READ the spec and then deferred to a SCAN of it. A keyword scan answers 'is this WORD present', never 'is this GUARANTEE present', and an ABSENCE finding from a scan overrode a PRESENCE finding from my own read. The tell was inside the row itself -- five irrelevant hits is what a scan returns when the guarantee is written in other words. AC4's PASS never moved in v2, v3 or here; what moved was my REASON, to a wrong one and back. C-S7's graduation of Z-S5 is superseded and NO remediation row is owed on it. The build criterion stands on its own merit per the round-2 analysis: a spec binds a build's INTENT, only the build can demonstrate its WIRING.",
    "adjudicates": [
      "AMGT_HARVST-Z-S6"
    ],
    "dismissal_reason": "A correction record: it supersedes this seat's own C-S7 conclusion and adopts the author's withdrawal of Z-S5; no cell, no remediation and no grade change follows from it."
  }
]
```
