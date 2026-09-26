# GOAL CLAUSE 1's RENDER OUTCOMES ARE UNGRADEABLE FROM THIS SEAT -- and the naive measurement PASSES a fence
`1.0.0_SA_CTO~Z`, 2026-09-26 ~06:5xZ

**Why I tried.** Goal clause 1 is *"visually polished Security Analysis application."* `AMGT_RESAPP`'s
Addendum B outcomes `FWD-21`..`FWD-26` are that clause, and **this seat has never graded them** -- the 20-of-20
coverage pass covered the earlier set. Their fences are DOM-level and the dev server was up, so a read-only
trace needed no word (`/closer`: *"A read-only TRACE needs no Andrew word"*).

**Result: NOT GRADED, and the attempt produced a finding worth more than the grade would have been.**

---

## 1. WHAT HAPPENED

`http://localhost:5174/security-analysis?security=BA_US_Equity` -- the navigate reported that URL. **By the
time the measurement ran, `location.href` read `http://localhost:5174/login`** and `document.body.innerText`
was **141 characters**. The app had redirected to an unauthenticated shell.

My probe returned:

| metric | value |
|---|---|
| `tabLabelsPresent` (Thesis/Exec Management/Peers/Model/Posture) | **[] -- none** |
| `elementsWithTitleAttr` | **0** |
| `titleAttrLongerThan80` | **0** |
| `citesAffordanceCount` | **0** |
| `darkWideBlocks` / `darkWideTopLevel` | **0 / 0** |
| `bodyTextLen` | 141 |

---

## 2. THE FINDING -- ONE OF THOSE ZEROS IS A FALSE PASS ON A REAL FENCE

**`FWD-23`'s fence** (`AMGT_RESAPP_PRD.md:678-682`) reads, in its own words:

> *"a sentence shows its PASS face and a 'cites N passages' affordance; opening it reveals the passage and
> accession line FROM THE DOM; **and a census prints ZERO passages carried in a native `title=` tooltip**"*

**My census printed ZERO.** Read against the fence's final clause, that is a PASS. **It is a zero produced by
the redirect, on a login page with no application DOM at all.**

> **A zero measured downstream of the bypass is produced BY the bypass.** The fence asks for an absence, so the
> instrument's own failure mode and the fence's success condition are THE SAME VALUE. There is no way to tell
> them apart from the number.

**This is the most dangerous shape a fence can have, and `FWD-23` has it:** a criterion whose success is an
absence cannot be graded by an instrument that can also return that absence for its own reasons. **A criterion
grading absence must grade presence too** -- here, the positive control is trivially available and was decisive:
`tabLabelsPresent` is empty and `bodyTextLen` is 141, so the page is not the application. **Without that
control I would have reported a PASS on `FWD-23`'s census clause.**

**`darkWideTopLevel: 0` is the mirror case.** `FWD-21` wants `bandContainersTopLevel == 1`. Zero is not 1, so
that one reads as a FAIL rather than a PASS -- **the same broken instrument produces a false PASS on one fence
and a false FAIL on another, from the same run.** Neither is a measurement.

---

## 3. THE BLOCKER, AND WHAT I WILL NOT DO ABOUT IT

The local dev server serves, and redirects an unauthenticated context to `/login`. **HTTP 200 on port 5174 is
therefore not evidence the application renders** -- it is evidence the server is up. I have been citing that
200 as a health check, which it is, and it does not reach this question.

**I did not and will not authenticate as Andrew.** I hold no credential of his, have requested none, and a
signed-in walk is not something to improvise inside a grading turn.

**The sanctioned route already exists** and is Andrew's own arm term 6 (`ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_SITEZ_DIRECTIVES_AS_A_WHOLE.md`
section 4): an agent performs the signed-in walk on a **bounded temporary principal** -- created, used inside
60 minutes, deleted and deletion VERIFIED with a positive control -- under a two-half sign-off, with any HAR
kept out of the repo and out of the broker. **That is its own act with its own halves, not a step inside this
one.** It is the correct next move for clause 1 and I am naming it rather than taking it here.

---

## 4. CONSEQUENCE FOR THE GOAL

| clause | measurable from this seat today? |
|---|---|
| 1. visually polished Security Analysis app | **NO -- `FWD-21`..`FWD-26` need an authenticated render** |
| 2. export, 2pg or rich text | **YES, and graded**: `FWD-30` NOT REALIZED on one clause of four (`74180574d5`) |
| 3. complete backfill through harvest channels | **YES, and graded**: one channel deep over 95 of 95 (`a370204f46` + A1/A2) |
| 4. close the projects | 0 of 18 `status: complete` |

**So clause 1 is the only clause of the four with NO instrument at this seat**, and that is a sharper statement
than "the render is not done." The render may well be further along than round 42's grades suggest -- rr-2's
AC4 passed ON THE RENDER, which means somebody does have a working instrument (the harness at portal DEV
`53ccbc52`, via `exportCompare.harness.cjs`). **The gap is that the harness lives with the executing seat and
this seat grades without one.** That is worth fixing on its own account: a grader that cannot see the plane it
grades is how three `AMGT_CORPUS` outcomes got self-graded MET on an s3api read tonight.

## 5. WHAT THIS ASKS FOR

1. **`FWD-23`'s census clause needs a stated positive control in the fence itself** -- "and the same run shows
   N > 0 application nodes" -- or its PASS is indistinguishable from an instrument that saw nothing. This is an
   L4 fence amendment at this seat, and it re-opens the half it touches.
2. **A grading path to the authenticated render for this seat**: either the bounded-principal walk under term
   6, or the executing seat's harness output committed as evidence I can read at a pin -- the same resolution
   that unblocked `FWD-30` this morning.

## Compiler Tools

`browser_evaluate` reporting `location.href` INSIDE the probe rather than trusting the navigate's echo, which
is the only reason the redirect was visible -- `tabLabelsPresent` and `bodyTextLen` carried in the same payload
as the fence metrics, so the positive control and the measurement could not be separated -- `curl` on 5174 kept
as a SERVER health oracle and explicitly not as a RENDER oracle -- the fence read at `:678-682` before
interpreting any zero.
