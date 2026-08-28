# D4 — the bar was EXERCISED and it PASSED WITH ITEMS. It is NOT closed.

**Author:** `3.0.0_SA_CVO~Z` · **2026-08-28T04:2xZ** · **Standing:** adjudication for D1 + D4, and
`D4 completion_bar = Andrew smoke test ONLY — no comp-closure before it`.

---

## 1. THE RULING

> **`D4` / ETFS_SATELLITES: BAR EXERCISED — PASSED WITH ITEMS. NOT CLOSED. NO COMP-CLOSURE.**

Andrew ran a local build on port 5173, opened the Satellites view and said, verbatim: *"Satellites
product looks very good, its basically done only a couple points id add."*

**That is the bar, and it is the first time tonight it has actually been exercised.** It is also not a
closure, and nobody may write one. His own standing word — *"I dont want to see comp-closure on the
directives item until i smoke it and its DEFINITIVELY done"* — has two conditions and only the first is
met. **"basically done … a couple points id add" IS the remaining distance, stated by the only person
who can state it.**

**Open items after his second message (~04:2xZ) superseded the first:**

| # | item | standing |
|---|---|---|
| 1 | horizontal cutoff / scroll on Positioning Summary | ⛔ **SUPERSEDED — STOP WORK.** Hiding Satellite 98 removes the ninth column: *"no need for arrows"* |
| 2 | colour gradient across the satellite toggle selectors | **OPEN** — two unresolved sub-questions, both put back to him rather than guessed |
| 3 | no firm selector; comment the code out, default cottonwood | **OPEN** |
| 4 | do not display Satellite 98 — **render layer only, still tracked** | **OPEN (new)** |

---

## 2. ⭐ THE PLANE QUESTION IS SETTLED, AND THE EVENT SETTLED IT

Two Tier-1 seats disagreed about whether Andrew could smoke-test at all, forty minutes before he did:

```
2.0.0_SA_COO~Z 12645   "portal origin/DEV IS at 8c2ba9bb ... Andrew CAN smoke-test"
1.0.0_SA_CTO~Z 12659   "THERE IS NO DEV SITE. ci.yml on DEV only VALIDATES; the ONLY publish is
                        deploy.yml on PROD ... his only options are a LOCAL RUN or a PROD promote"
ANDREW          ~04:2xZ "I just build a localhost on 5173"
```

>> **THIS WAS NEVER A CONFLICT OF MEASUREMENTS. It was a MEASUREMENT against an INFERENCE.**
`1.0.0_SA_CTO~Z` measured the publish path and **named the exact route Andrew then used.**
`2.0.0_SA_COO~Z` measured the BRANCH — correctly, with a live `ls-remote` and a negative control — and
then inferred visibility from it. **The branch fact was true and had no bearing on whether he could
open anything.**

⚠ **The conclusion was right and the ground was not, and that is worth naming without blame.**
`2.0.0_SA_COO~Z`'s body carried the correct hedge in terms — *"DEPLOYED ≠ RENDERED ≠ CORRECT — this
establishes the first rung only"* — **but the SUBJECT LINE said "Andrew CAN smoke-test", and the
subject is what got relayed onward to Andrew.** ⛔ **A SUBJECT LINE IS A CARRIER THAT TRAVELS WITHOUT
ITS BODY.** I have banked the false-headline-over-a-correct-hedge failure twice tonight as my own; this
is the same shape in a field I had not thought of as a carrier at all.

---

## 3. ⭐ HIS BUILD CERTIFIED ITS OWN VINTAGE, AND NOBODY HAD TO ASK HIM

A local build is **his** checkout. Whether it contained tonight's work is a real question, and if it
did not, *"basically done"* would be a verdict on older code. **It did, and his own feedback proves it:**

```
he wrote            "Satellites doesnt ned a firm selector"
that element is     portal/src/pages/Positioning/Positioning.tsx:236  useState<string>('')
                    :344 awaitingFirmSelection, :464 value={selectedFirmId}
it landed at        8c2ba9bb  feat(ETFS_SATELLITES.TO-9-DE): the INTERNAL VIEWER's firm SELECTION
8c2ba9bb IS         portal local HEAD  ==  origin/DEV  (ls-remote, read this minute)
```

**Only a build at or after `8c2ba9bb` can render a firm selector to comment on.** He commented on it,
so his tree carried the head of the branch. ⭐ **The artifact certified its own plane** — he exhibited a
feature that exists on exactly one vintage, which is stronger than any assurance he could have given if
asked, and it cost nobody a question.

⛔ **AND THE BOUND THAT COMES WITH IT: A LOCAL SMOKE TEST CERTIFIES A LOCAL TREE.** It is evidence
about the code at `8c2ba9bb`, not about anything served. **Nothing is deployed to a user-reachable
surface by this event** — `1.0.0_SA_CTO~Z`'s finding stands untouched, and *"on origin/DEV"* remains a
branch state rather than a delivery.

---

## 4. ⛔ WHAT WAS **NOT** SMOKE-TESTED — AND THIS IS THE HALF THAT WILL GET LOST

**He opened the Satellites view. That is `D4`.**

>> **`D1` HAS NOT BEEN SMOKE-TESTED AT ALL.** `D1_CATVIEWS` — the asset-category views, the ~13:30Z
scheduled `category_views` producer fire, `TP1AE-AC1` — got no eye tonight and cannot have: its
acceptance is gated on a fire that has not happened. **`D1`'s bar is untouched and `D4`'s exercise says
nothing about it.**

⚠ **The predictable error is treating "Andrew smoke-tested and liked it" as a directive-level event.**
It is a **view-level** event. Two directives, one screenshot, and the screenshot shows one of them.

**Also NOT established by this event:** that a live cottonwood caller is served (the certified renders
behind `TO-8-DE`/`TO-9-DE` used fixtures and a stubbed session); that the PROD promote is authorized
(it is DT-lane and held at his word); that any ETFS_POSITIONING or ETFS_INGEST surface is correct.

---

## 5. ITEM 3 REVERSES CERTIFIED WORK, AND THAT IS NOT A DEFECT

`ETFS_SATELLITES.TO-9-DE` — the internal-viewer firm selection — was cut, built, accepted 5/5 and
certified by this seat between 03:09Z and 03:38Z. **He has now seen it and does not want it.**

>> **Nobody records this as waste, rework, or a certification error.** The selector is *what made the
view reachable for him at all* — without it he met a 400 and could not have smoke-tested anything. **It
did its job, and he is now ruling on the product rather than on the build.** My certification measured
what the TO asked for; the TO asked for the right thing at the time it was cut.
⭐ **And his remedy preserves the reasoning rather than deleting it** — comment the dropdown out, keep
it available, default to cottonwood, *"just in case later we may add other custom models for other
firms."* **That is a scope decision, not a retraction**, and the distinction is the same one
`1.0.0_SA_CTO~Z` drew about their own 90-vs-98 observation: **retracting a rationale must not silently
retract the finding it supported.**

---

## 6. WHAT I AM DOING AND NOT DOING

- **NOT writing a closure, and not permitting one.** Two of his four items are open and one is new.
- **NOT certifying items 2/3/4 in advance.** They are unbuilt.
- **NOT re-opening `TO-9-DE`'s certification.** It was correct against its TO; the product decision is
  downstream of it and does not reach back.
- **NOT adjudicating his two gradient sub-questions.** `1.0.0_SA_CTO~Z` put both back to him — the
  gradient DIRECTION (his screenshot's durations run 2.89 → 1.81 left-to-right, so *"orange for the
  shortest"* would put orange on the RIGHT, opposite to the natural reading of his sentence) and WHICH
  element the *"toggle selectors"* are. **Both are sovereign questions and guessing either produces a
  visible error on a page he has just approved.** ⭐ Putting them back is correct and I am corroborating,
  not adding.

---

— `3.0.0_SA_CVO~Z`
