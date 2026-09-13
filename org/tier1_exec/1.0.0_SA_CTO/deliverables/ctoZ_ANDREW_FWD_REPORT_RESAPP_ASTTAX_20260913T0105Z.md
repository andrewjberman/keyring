# What was done on the site-Z box, outcome by outcome -- RESAPP and ASTTAX

**For Andrew.** Written 2026-09-13 01:05Z by the site-Z technology seat, which owns the outcome
list for both projects and takes the round-close grade on each. Answering, verbatim:

> *"have them report exactly what was done on their box so i can have an /exec-sum that shows the
> fwds for their respective two projects RESAPP and ASTTAX"*

Every outcome id you named is here. Where an outcome has never been graded, it says NEVER GRADED
rather than guessing one.

---

## THE SHORT ANSWER, BEFORE THE TABLES

**RESAPP: forty-six pieces of work are cut against fifteen outcomes and NOT ONE outcome is finished, because
fourteen of its fifteen outcomes can only be finished BY SOMEONE USING THEM.** When we wrote the
outcome list we set the bar for fourteen of fifteen at *someone has actually done this* -- an
analyst opened the page, Adam forwarded the pack, a figure was challenged and answered. **No
amount of code closes those. A person using it closes them.** Every one of the fifteen has had
work cut against it. Forty-three of the forty-six pieces are finished; three were cut tonight and
are running now. The page all of it feeds is not in front of anyone yet.

**ASTTAX is a different shape and the difference is the point: it cannot close without you.** Its
last round has been sitting at eleven of fifteen pieces done for hours, waiting on one decision of
yours. And a finding this seat is putting in front of you for the first time tonight: **two of its
six outcomes have never had a single piece of work cut against them in three rounds** -- the
colour rule and the "both screens agree" check. They were in the first plan and were not carried
into the second or third.

**The one thing that would move the most, tonight, is the ASTTAX decision you already hold.**

---

## RESAPP -- fifteen outcomes

Every one has had work cut against it. All of it is finished except three pieces cut tonight, which
serve FWD-14 and FWD-15 and are running now. **None of the fifteen is graded finished.**
The grade below is the round-close read this seat takes; it has been taken at every round and the
answer has been the same each time and is recorded as such.

| # | The outcome, in your terms | Bar | Graded | What was actually built | What it waits on |
|---|---|---|---|---|---|
| **FWD-1** | An analyst gets a first-draft pack for a covered name without opening a spreadsheet or a terminal | someone has done it | NOT REALIZED | The model block: the figures, the description, the segment breakdown, assembled behind one call | A person opening it |
| **FWD-2** | The same pack for a company we have never covered, by typing its ticker | someone has done it | NOT REALIZED | The on-demand pull, and the page saying it is fetching now rather than showing a save | A person typing a ticker |
| **FWD-3** | An analyst can defend every number on the page in a meeting | someone has done it | NOT REALIZED | Source, basis and as-of date carried beside every figure -- and this round, the corrected prices now carry their own provenance | A figure being challenged in a real meeting |
| **FWD-4** | An analyst reads what has recently been said about the company without leaving the page | someone has done it | NOT REALIZED | The commentary reader, ranked by recency and frequency, each item clickable | A person reading one and following it out |
| **FWD-5** | Adam forwards a printed pack without reformatting it | Adam has done it | NOT REALIZED | The print renderer against Adam's own template | **Adam forwarding one** |
| **FWD-6** | An analyst returning to a company can say what changed | someone has done it | NOT REALIZED | The version store exists and accumulates rather than overwrites | Someone comparing two versions |
| **FWD-7** | Adam can see which covered companies have gone stale | Adam has done it | NOT REALIZED | The freshness view over the covered list | **Adam using it to find a stale name** |
| **FWD-8** | The comparison block is about the company on the page | someone stopped distrusting it | NOT REALIZED | The peer set rebuilt; the old one was wrong on 48 of 54 names and that is fixed at the source | An analyst who distrusted it saying they no longer do |
| **FWD-9** | Machine-written prose is never mistaken for a firm view | **the marking is in place** | NOT REALIZED | The marking, sitting beside the evidence each sentence was drawn from | **The only one of the fifteen that does NOT need a person -- it needs the page served** |
| **FWD-10** | A figure that failed its check is visible as failed | someone saw a refusal | NOT REALIZED | The check face, and the rule that a failure shows as a marked value and never as a blank or a zero | A refusal being seen on screen |
| **FWD-11** | An analyst sees social discussion admitted by a written rule | someone read it and can point at why | NOT REALIZED | The admission rule, written and readable | A person reading the feed |
| **FWD-12** | An analyst can see where each input came from and re-run any one alone | one input re-run alone | NOT REALIZED | The input ledger, per source, with its own re-run | Someone re-running one |
| **FWD-13** | Everything on one page is about the same company | checked on an ambiguous name | NOT REALIZED | The identity layer across the three different keys -- ticker, symbol, investor page | A check on a name more than one business uses |
| **FWD-14** | The lists the page depends on do not rot in silence | a list rotted and someone was told | NOT REALIZED | **This round's work.** The fiscal figures now serve corrected prices with their provenance and refuse the unresolved ones; incomplete reads can no longer masquerade as absent history | A list actually going stale and the system saying so |
| **FWD-15** | A PM sees which covered names are worth looking at right now, ranked, and jumps straight to one | **a PM has done it** | NOT REALIZED | **This round's other work.** The ranked panel, the price and chatter crosses, the charts, the starred filter | **Adam or Lauren opening it cold** -- and the page is not published yet |

### The two things this round found that change what those grades MEAN

**1. The work is right and the page cannot read it.** The corrected figures are produced correctly
-- 183 of 183 fiscal figures, ten corrected prices, every one carrying its provenance, and a
hundred-and-seven separate checks pass on the producing side. The page then matches **thirteen of
thirteen** header figures and **nought of a hundred and eighty-three** fiscal ones, because the two
sides name the same figure differently. This is not a near miss: it is arithmetic, and it will not
improve by itself. The round that just started is three pieces of work aimed squarely at it.
**Read plainly: we built the right thing and connected it to the wrong socket, and we found that
out by measuring rather than by a demo failing in front of someone.**

**2. The picture screen cannot tell "no data" from "we gave up trying".** Two genuinely different
states render identically. Also being fixed in the round that just started.

### What RESAPP is waiting on from you -- one thing

**The front end is finished on this machine and published nowhere, because you froze publishing.**
Two rounds of screen work -- the ranked panel and its charts -- exist only on this box, on working
branches, with no copy anywhere else. Nothing is lost and nothing is at risk today; it simply
cannot be opened by anyone but this machine, which is why **every screen outcome above reads NOT
REALIZED and structurally cannot read otherwise while the freeze holds.** That is the freeze doing
exactly what you asked it to do, and the cost is stated here rather than buried: **the fourteen
"someone has used it" outcomes cannot begin to close until the page is somewhere a person can open
it.**

---

## ASTTAX -- six outcomes

| # | The outcome, in your terms | Bar | Graded | What was actually built | What it waits on |
|---|---|---|---|---|---|
| **FWD-1** | Every holding sorts into exactly one of five asset classes | someone re-sorted real portfolios | NOT REALIZED | The five-class vocabulary in one place; the three disagreeing "unknown" defaults retired so an unrecognised holding shows as unclassified instead of being quietly called equity | The last four pieces, then a real portfolio re-sorted |
| **FWD-2** | Volatility and hedge products shown apart from equities | someone saw a portfolio stop folding them in | NOT REALIZED | The reassignment rules; the retag itself is one of the four pieces still open | **Your decision below** |
| **FWD-3** | The five classes always appear in the same order | the order is in place everywhere | NOT REALIZED | One definition of the fixed order; the screen hop measured | The last pieces, then a read of both screens |
| **FWD-4** | Each class has one colour, the same everywhere | the colour is in place everywhere | **NEVER GRADED -- AND NO WORK HAS EVER BEEN CUT AGAINST IT** | Nothing. It was in the first plan and was not carried into the second or third | Someone deciding it is in scope |
| **FWD-5** | The classification is defined in one place and flows everywhere | someone changed a boundary once and everywhere followed | NOT REALIZED | The single authoring source settled and built | A person changing a definition once and watching it flow |
| **FWD-6** | The two screens agree with each other | both read, no disagreement found | **NEVER GRADED -- AND NO WORK HAS EVER BEEN CUT AGAINST IT** | Nothing. Same as FWD-4: in the first plan, not carried forward | Someone deciding it is in scope |

### The finding this seat is raising for the first time

**Two of ASTTAX's six outcomes -- the colour rule and "the two screens agree" -- have had no work
cut against them across three rounds.** They were both in the original plan. The second and third
plans re-cut around the classification problem and did not carry them. Everything since has served
the other four.

**THIS DOES NOT CONTRADICT THE RISK SEAT'S COUNT, AND THE DIFFERENCE IS WORTH ONE SENTENCE** --
both numbers will be in front of you. That seat measured the PLANS against the outcomes and found
all six covered, which is true and is the check it owns. This seat measured the WORK ACTUALLY CUT
and found four of six. **The plan covers all six; the work covers four. The gap between those two
numbers is the finding.**

⚠ **This is not a claim that they were forgotten deliberately, and it is not a criticism of the
seat that cut those rounds** -- each re-cut was answering a real defect that had just been found.
It is a statement that **the outcome list and the work list have drifted apart, and nothing in the
machinery would have said so.** This seat found it by counting the outcomes against the orders,
which is the check the round-close read exists to run -- and ASTTAX has not reached a round close
since the drift began.

**Nothing needs deciding tonight.** When ASTTAX's current round closes, this seat's read will
either put those two outcomes back into the work or record that they are out of scope -- and if it
is the latter, that is a scope decision and it comes to you rather than being taken here.

### What ASTTAX is waiting on from you -- the one decision that unblocks it

**Eleven of fifteen pieces are finished. Four are not, and all four sit behind one generator that
has not been deployed.** The question already in your queue is whether that round may close with
those four carried forward instead of finished. **Until that is answered the round cannot close,
the next round cannot be cut, and none of the six outcomes can move.** The recommendation from
both this seat and the operations seat is unchanged: **yes, carry them forward.**

---

## THE HONEST SUMMARY LINE

Across both projects: **twenty-one outcomes, none graded finished, and that is the correct grade
rather than a disappointing one.** Nineteen of the twenty-one can only be finished by a person
using the thing, and the thing is not yet in front of a person -- for RESAPP because publishing is
frozen, for ASTTAX because one decision is pending. **The building is not the bottleneck. Access
is.**

Two outcomes are the exception and neither is waiting on a person: **RESAPP's FWD-9** needs only
the page served, and **ASTTAX's FWD-4** needs only a decision that it is still in scope.

---

## ADDENDUM, 2026-09-13 02:52Z -- ANSWERING "43 WORKORDERS, 0 OUTCOMES"

**You asked how site Z has done 43+ work orders and achieved 0 outcomes.** The explanation brief is
the operations seat's to write and it is coming. This addendum carries only the two facts that are
this seat's to state, because the outcome list is this seat's artifact.

### 1. The bars were set BEFORE the work, and none has ever been weakened

An audit run at the laptop said, fairly, that it could not tell whether the "someone has actually
done this" bars were set up front or added afterwards. They were set up front. Measured:

```
2026-09-10 14:57   the outcome cards land: 14 bars -- 13 "someone has used it", 1 "it is in place"
2026-09-10 16:35   THE FIRST WORK ORDER IS CUT -- ninety-eight minutes later
                   (and the first commit is a literal ancestor of the second, with a control)
2026-09-11 08:36   the bars change ONCE: 14 -> 15. The added one is FWD-15, the Lead Panel,
                   from your own frontend walkthrough -- and it arrived with the same hard bar.
today             15 bars, unchanged since.
```
**No bar was ever lowered, swapped or quietly rewritten.** One outcome was added, on your word, and
it came in at the same standard as the rest.

### 2. The 43 and the 0 are measuring two different things, and both numbers are right

The work orders measure **what was built**. The outcomes measure **whether a person has used it**.
Nineteen of the twenty-one outcomes across both projects were written -- before any order existed --
to close only when an analyst, or Adam, or a PM actually does the thing. **No quantity of finished
orders can move them.**

⚠ **AND THERE IS A REAL FINDING UNDERNEATH, WHICH THIS SEAT IS NOT GOING TO SOFTEN.** The audit's
central point looks correct: the acceptance criteria were largely satisfiable on the *producing*
side, so orders could all pass while the page still could not read what they produced. Round 7
measured exactly that -- 107 producer-side tests passing, and the page joining **nought of 183**
figures. This seat's own round-close read named it as that round's whole lesson before the audit
existed, and the round now running is three pieces of work aimed squarely at it.

**So the honest answer to your question is two sentences.** The orders built the system and the
outcomes measure a person using it, which nobody can yet do because publishing is frozen and one
decision is pending. And separately, until this week our acceptance bar mostly stopped at the
producer's edge rather than at the screen -- that one is a real gap, it is being closed now, and it
is not what the 43-to-0 gap is made of.
