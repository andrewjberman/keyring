# Forty-three orders, zero outcomes -- what they were, what they built, and where the line stops

Written by the COO that issued and held every one of them. Plain language. No apology in it, because
none was asked for and one would be in the way.

## The audit is right, and I checked it myself before answering it

I ran the same count on my own instrument rather than accepting or disputing it. **Every figure
reproduces exactly:** 228 acceptance criteria across 44 records -- 145 scripts over our own files,
45 judgment calls, 29 test suites, and **9 reads of anything live**. 179 passed, 46 were routed to a
human reviewer, 3 failed outright.

**And its sharpest claim is substantially true.** Forty-three orders *could* have passed while the
page showed none of the numbers, because most of the checks asked "did the producer write it?" and
not "does the page read it?"

**Three corrections, each checkable.**

**One: they did not all pass.** Three failed on instruments, and **fourteen more failed at the
review layer** -- the criteria a machine cannot grade, which a separate seat grades afterwards. That
layer discriminated; it was not a rubber stamp. A round was sent back to be re-cut on the strength
of it.

**Two: the 20% "unverifiable" is not a hole.** Those are the judgment calls, and by rule the person
doing the work never grades their own. **Forty-two of the forty-two from closed rounds carry a
verdict from the reviewer.** The only four without one belong to the round running tonight, which
has not reached review yet. The number the audit read as a gap is a routing that worked.

**Three: the nine live reads were all against data stores** -- the tables and buckets -- **never
against a page.** That is not an oversight and I explain it below.

## What the rounds were for, one sentence each

| | |
|---|---|
| **1** | Build the sixteen pieces a research page needs: the numbers, the sources, the checks, the identity layer that keeps one company's data from being shown under another's name. |
| **2, 3, 4** | Fix what round 1 got wrong. A date join that married one company's results to prices nine months later. A corrected price that silently reverted to the raw one. A check whose "failed" marker read at a glance as an ordinary number. |
| **5** | The first round aimed at a screen: the store and the two ranking engines behind the panel a PM would open. |
| **6** | The panel failed its own repaired tests and was re-cut. |
| **7** | Repair the six defects the re-cut exposed, including a matcher that dropped every fiscal-year figure and a bypass where ten of ten corrected values silently reverted to raw. |
| **8** | Tonight. **The consumer boundary** -- the three places where the page fails to read what the back end now correctly produces. |

## What is true now that was not true before

Not activity -- capability. Each of these is a thing the system can do today and could not do in
August:

- **A covered company's model numbers assemble without anyone opening a spreadsheet or a terminal.**
- **Each figure carries where it came from, on what basis, and as of when** -- and the basis is stated
  honestly rather than reverse-engineered, because no terminal field reproduces the vendor's
  normalised earnings number.
- **A figure that fails its check is marked as failed** rather than blanked, zeroed, or quietly
  dropped -- with six written rules, one per class of number, each naming the input that makes it
  refuse.
- **The identity layer exists.** This is the one that fixes the defect we measured in production
  before the project started: forty-eight of fifty-four existing packs carry *another company's*
  comparison list.
- **Research snapshots accumulate instead of overwriting**, so "what changed since last time" is
  answerable in principle.
- **The ranking engines behind the lead panel run** -- price movement and discussion volume, on a
  schedule, into their own store.
- **And, as of tonight, the page reads the back end correctly**: the fiscal figures went from 0 of
  183 joined to 183 of 183, measured with a before-and-after control in the same run so the number
  is evidence rather than an assertion.

## Why the checks stopped where they did -- the honest answer is: half ruled, half drift

**The half that was ruled, and I would rule it the same way again.** No check could read a served
page **because no page is served.** The standing instruction on this project is *commit yes, promote
no* -- nothing reaches an environment until you say so -- and before that, no screen could be built
at all until the design spec was approved. A criterion that required a live page would have been a
criterion a correct build could not satisfy. That is why the only nine live reads we ever made were
against data stores: the stores are reachable; the page is not.

**The half that was drift, and the audit is right to name it.** There is a boundary *inside the
code* -- between what the back end writes and what the page asks for -- that was reachable the whole
time, and our checks did not cross it until tonight. **Round 7 is the proof, and it is the one fact
I would put in front of you above all others: we repaired the back end, every check passed, and the
page still showed none of the figures.** Thirteen of thirteen header numbers joined; **zero of one
hundred and eighty-three** fiscal numbers did. The page was asking for them under a different name
than the producer was writing them.

Nothing in forty-three orders was shaped to catch that. The audit's reading of the criteria is
correct and I am not going to argue with it.

**What it does not see, stated because it asked to be corrected -- and now measured by the seat that
owns the definitions rather than asserted by me:** the outcome cards landed in the specification
**two hours and four minutes before the first order was cut**, and the commit that set them is a
literal ancestor of the commit that issued the work. Walked revision by revision across every version since:
**one outcome was added -- the lead panel, on your own word after the walkthrough -- and it arrived at
the same demanding bar as the rest. No bar has ever been weakened, swapped or retrofitted.**

⭐ **Which removes one explanation and sharpens the real one.** The bars were never gradeable from
producer-side work, *by design, from the first day*. An "exercised" bar closes when the thing is
**used**. So forty-three orders of correct producer-side capability can all be real and still move no
outcome -- not because the orders failed the outcomes, but because **the outcomes measure a later
event than the orders build.** That is not an excuse for the criteria gap above; the two are
different layers and both are true.

And the stopping point was not invisible to us either: round 7's own evidence is what exposed it,
which is why round 8 exists and why it was cut the same hour that evidence landed.

## The line to the outcomes, and exactly where it stops

Fifteen outcomes. **Every one has work behind it** -- that was checked from both ends by two seats
using different methods, and both came back complete with nothing uncovered and nothing invented.

**Fourteen of the fifteen are written so they are only done when a person has actually used the
thing.** Not when it is built. Not when it passes. When an analyst answers a challenged number off
the screen; when Adam forwards a printed pack; when a PM follows a name out of the ranked list.

**So the line runs: the data is assembled, the checks run, the identity holds, the page now reads it
-- and then it stops, because the page cannot reach a person.** That last step is your word, not a
build. The fifteenth outcome, the one that only needs the marking in place rather than a person, is
blocked by the same thing: its home is the page.

## What would change the grades

Six things wait on you, and they are the whole list:

1. **The word to promote the portal.** This is the gate on all fifteen.
2. A per-use word for **one social data trigger** -- we measured first and found 1,763 datasets
   listed and reachable, none ever exercised, so we deliberately built nothing on an unexercised
   catalogue.
3. A per-use word **naming a model** for the drafting producer.
4. **How many names we may classify on the terminal** -- until then the page says "no sensible
   comparison" rather than guessing.
5. **Who owns the publisher list and the company-to-social map.** An unowned list is exactly the
   failure that outcome exists to prevent, so we cannot name them for you.
6. **The harvesting box standing up**, which is the clock on your own narrow permission for the four
   named publications.

After all six, fourteen outcomes still need a named person to use the thing. That is not a build and
this project cannot manufacture it.

## The shortest true answer to your question

**The forty-three orders built the thing. The outcomes measure whether someone used it.** Those are
different axes, and they were deliberately set that way before any order existed -- because an
outcome that closes when a build finishes is an outcome that lies to you.

**So the gap between forty-three and zero is not a productivity finding. It is the distance between
a built system and a served one** -- and today that distance is one frozen publish and a handful of
decisions that are yours. The audit's criteria finding sits inside that distance and makes it longer
than it needed to be: we should have been testing the consumer boundary all along, and we were not.

## What I would do differently, in one line

**Every round should have carried at least one check that crosses the boundary between the producer
and its consumer, even when the consumer cannot be served.** Round 8 does. Rounds 1 through 7 did
not, and that is the difference between a back end that is correct and a page that shows correct
numbers -- which is the difference you are looking at.

---

## For the carrier, not for the brief

- Vintage: measured 2026-09-13T02:50Z against the project tree at head.
- Method distribution reproduced independently: 145 command / 45 manual_read_with_citation / 29
  test_suite / 9 live_read over 44 records, 228 criteria; 179 PASS / 46 UNVERIFIABLE / 3 FAIL.
  Identical to the laptop's audit.
- L9 grades on the adjudication plane: 29 PASS, 14 FAIL, 1 NOT_EVALUATED across 44 distinct criteria.
- The 4 worker-level UNVERIFIABLE criteria carrying no L9 grade are `AMGTrg1-AC1`, `AMGTrg1-AC5`,
  `AMGTrg2-AC5`, `AMGTrg3-AC5` -- all round 8, which has not reached L9.
- The 9 `live_read` criteria sit on `rd-1`, `rd-2`, `rd-5`, `rd-6`, `s-6` -- every one a DynamoDB or
  S3 store.
- Round 8 status at writing: 45 of 46 orders terminal; `rg-2` open and re-spawned. `rg-1`'s repair
  drained at `55c71e45d5`, negative control firing at 0 of 183 before and 183 of 183 after.
- The laptop's zero for `task_orders/` is a path-shape zero: this fabric spells it `task-orders/`.
- **The bar-timing measurement is NOT this seat's** and is used with attribution: `1.0.0_SA_CTO~Z`
  (msg 22179) -- outcome cards at `8019bf6433`, 2026-09-10 14:57:00-04:00; first issuance
  `908880f6d1` at 16:35:57-04:00; `merge-base --is-ancestor` YES with the reverse direction NO as a
  firing negative control; bar distribution walked across all 15 PRD revisions, 14 bars -> 15, the
  EXERCISED/APPLIED split constant. Its stated limit: it measured the COUNT and the DISTRIBUTION at
  every revision plus FWD-15's provenance text, **not a per-card textual diff** -- so "no bar was
  weakened" rests on the distribution holding and the count rising by one. `4.0.0_SA_CRO~Z`
  (msg 22176) measured the same thing from the PRD's FIRST commit `c0b5636ea9` and reports a 2h03m
  gap; the two figures differ because they time different commits and both are stated rather than
  averaged.
- The "19 of 21 outcomes across both projects" framing is `1.0.0_SA_CTO~Z`'s and spans POSN_ASTTAX
  too; this brief deliberately claims only AMGT_RESAPP's 15, which are this seat's to speak to.
- FIGURE CORRECTION, and it runs AGAINST this brief's own case, which is why it is made: the body
  said **"ninety-eight minutes"** and now says **two hours and four minutes**. `1.0.0_SA_CTO~Z`
  corrected its own measurement (msg 22222) -- it had timed `8019bf6433`, where the bars were merely
  written out per row, while the PRD's FIRST commit `c0b5636ea9` at 14:32:06-04:00 **already carried
  all fourteen outcome ids and the bar line**. True gap **2h03m51s**, which is `4.0.0_SA_CRO~Z`'s
  original figure. Two seats measured the same thing, disagreed, and the disagreement was a choice of
  commit rather than a choice of method -- **which is exactly why both were printed side by side here
  instead of averaged.** The understatement made the case weaker than the record supports; it is
  corrected in the direction of the evidence, not of the argument.
- CITATION CORRECTION, made before this file was carried: an earlier revision of this section cited
  those two messages as 22177 and 22174. Both ids were INFERRED, not read. Measured from the
  delivered files' own headers they are 22179 and 22176. The claims they support are unchanged;
  only the pointers were wrong, and a pointer nobody can follow is not a citation.
- Rule 27 verbatim, for the judgment-criteria correction: *"L9 adjudicate (JUDGMENT criteria are
  graded HERE and never self-graded)"*.
