# POSN_ASTTAX — fifteen orders, zero outcomes, and the line between them

**The position-classification project.** Ordered by Andrew 2026-09-13 ~04:08Z: brief this project the
same way the research project was briefed. Three rounds, fifteen orders, eleven finished, four
carried forward on his word. **None of the six outcomes is realized.** This explains what the orders
were, what they actually changed, and — the part he asked for — **how that gets to the outcomes, and
exactly where the line stops today.**

---

## THE SHORT VERSION

**Three rounds bought one thing: the project now knows what is true.** It started on a premise that
turned out to be false, and most of the fifteen orders were spent finding that out and then building
against what is actually there.

**The single fact everything else hangs on:** the program that builds the positioning data was
repaired months of work ago, and **the repaired version was never put into service.** The version
running today still fails outright the moment it meets one of the new asset-class names. So work that
is finished and correct in our code is invisible on the screen.

**And a second, independent stop was found in round three:** the screens themselves can only display
**two** asset classes. Two separate places in the front-end code contain a hardcoded list naming only
*Fixed Income* and *Equity*. A group carrying Commodities, Structured or Alternatives is never even
looked at.

Two stops, one behind the other. Neither is a matter of working harder.

---

## WHAT EACH ROUND WAS FOR

**ROUND 1 — one question, asked properly.** A single order: *where does the classification actually
live, and does a change there flow anywhere?* The answer was a negative result, which is the useful
kind. It found that the obvious candidate could not be the answer, and it found the figure that cut
against its own conclusion rather than burying it. His own ruling then settled the question: the
classification is a **curated tagging list** a person extends as we acquire securities, not a
single-source-of-truth architecture. That corrected the frame the round had been measuring against,
and the correction was recorded in the open.

**ROUND 2 — seven orders, five run, two deliberately refused.** The round's most valuable output was
an order that **said no**. It was cut to verify that the allocation chain carried the five ratified
classes; it ran that verification and returned **NO**. A verification that returns no is the only
kind that can stop a bad act, and it stopped one.
⛔ **And the round's own founding premise was falsified in the process.** The project had been told
the old crash was "history, no longer operative." Measured: it is what runs in production. The
sentence describing today's behaviour actually describes our code; the sentence filed as history
describes the live system.

**ROUND 3 — seven orders: four measurements, one bar, two carried.** This is the round that stopped
guessing about the served system and went and read it.

---

## WHAT IS TRUE NOW THAT WAS NOT TRUE BEFORE — capability, not activity

1. **The program that builds positioning data carries all five classes.** Measured side by side on
   the same input: before, Commodities, Structured and Alternatives each came out as the literal word
   *Unknown* with a weight of zero; after, each comes out under its own name with its real weight.
2. **It no longer swallows a class it does not recognise.** Fed a made-up class, it warns and names
   the value instead of silently adding it as zero.
3. **The classification list survives a re-seed.** It used to be silently reverted whenever the
   seeding script ran; it now reads what is there and merges. Proved with a before-and-after control
   against a scratch copy — the live table was never touched.
4. **Two other programs that read the same data are proven to carry a five-class value** — every one
   of eighty-eight places checked, with no silent drops.
5. **The front end has been measured for the first time.** Earlier work had disclosed this gap and
   could not close it, because those files were outside what its tools could read. It is now read,
   and the answer is that it collapses to two classes.
6. **The retag is priced exactly.** Ten specific changes would make it safe. Which ones are ours,
   which belong to another project, and which sit behind the freeze is now a list, not a guess.
7. **The safety question has a measured answer instead of an assumption** — 836 individual checks,
   every one recorded with its verdict and with how it was known.

**None of that is visible to anyone yet. All of it is real.**

---

## THE LINE FROM THE ORDERS TO AN OUTCOME, AND WHERE IT STOPS

```
   finished orders  ->  repaired code  ->  [STOP 1: never deployed]  ->  served data
        ->  [STOP 2: screens read two classes]  ->  a person sees five classes  ->  outcomes close
```

**STOP 1 — the deploy.** The repaired program is committed and passes on those bytes. The version in
service predates every repair. **He approved this deploy on 13 September, conditional on a two-seat
never-widen sign-off, and that condition is part of the approval.** The act moves served output to
four partner firms, so no sign-off means no deploy. This is the largest single item on the list and
the one that makes the other nine visible.

**STOP 2 — the screens.** Five of the ten priced changes are in the portal, which he has frozen and
restated as frozen twice. Until those change, three of the six outcomes cannot be reached no matter
what anyone builds.

⭐ **That is the whole answer to "how does this proceed to the outcomes."** Every finished order is
upstream of stop 1. Nothing the project has built is wasted; none of it can be seen.

---

## ⛔ THE TWO OUTCOMES WITH NO WORK CUT IN THREE ROUNDS

He asked that these be legible rather than absorbed. Measured across all three rounds' cell lists:

| outcome | orders cut against it in three rounds |
|---|---|
| FWD-1 — every holding in exactly one of five classes | many |
| FWD-2 — volatility and hedge shown apart from equities | four |
| FWD-3 — the five classes always in the same order | one, and only as a secondary |
| **FWD-4 — each class has one colour, the same everywhere** | **NONE** |
| FWD-5 — defined in one place and flows everywhere | one — it was the whole of round 1 |
| **FWD-6 — the places that show asset classes agree** | **NONE** |

**FWD-4 and FWD-6 have never had a single order cut against them.** That is not an oversight and it
is not laziness: **both live entirely inside the portal.** Colour is a screen property; cross-surface
agreement is a property of two screens. **The two outcomes nobody has worked are exactly the two that
are wholly behind the freeze** — so the freeze and the empty column are the same fact seen twice.

⚠ And FWD-6 carries a sharper detail: the two views **do** agree today. They agree because each
carries its own copy of the same wrong two-class list. **Agreement about two classes is not agreement
about five**, and an outcome graded on "do they agree" would read PASS on a broken system.

---

## WHY THE CRITERIA WERE SHAPED AS THEY WERE — the honest version

The research project's audit found that its orders could all pass while the page stayed wrong,
because the checks were satisfiable on the producer's own side. **The same is true of this project's
first two rounds and I am not going to claim otherwise:** those cells read our code, our files and
our tests.

**Round three is where that changed, deliberately.** The bar was written to read the **served
artifact** and the **deployed bytes** — not our repository. It downloaded the running program and
executed it. That single choice is why this project knows its generator is a month stale and its
screens carry two classes, and why it can price the fix to ten items.

⭐ **The lesson is not "our criteria were good."** It is that **a check run on the near side of a
boundary and claimed for the far side always passes**, and this project ran two rounds before one
order went and looked at the far side. When it did, the premise the whole project rested on inverted.

---

## WHAT WOULD CHANGE THE GRADES, AND WHAT EACH WAITS ON

| outcome | what it needs | whose |
|---|---|---|
| FWD-1, FWD-2 | the deploy, then the retag the bar currently refuses | **his**, and now approved subject to the sign-off |
| FWD-3, FWD-4, FWD-6 | the screens rendering five classes instead of a hardcoded two | **his** — inside the portal freeze |
| FWD-5 | both of the above, then someone actually changing a boundary once and watching it flow | **his**, downstream of the two |

**Nothing on this list is waiting on a seat.** Everything measurable has been measured. What remains
needs a release or a freeze lifted.

---

## WHAT THE PROJECT IS NOT ASKING FOR

Not a relaxation of the freeze — he has answered that twice and this brief does not reopen it.
Not a waiver of the sign-off on the deploy he approved; that condition is the control, not friction.
Not credit for the eleven finished orders. **He asked how it proceeds to the outcomes, and the honest
answer is that it proceeds through two acts that are his and one that is ours once he releases them.**
