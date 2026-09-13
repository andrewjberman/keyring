# POSN_ASTTAX -- what was actually done on this box, outcome by outcome

**For Andrew's /exec-sum.** Six outcomes were ratified for this project. **None of the six is
realized.** Every figure below was measured today from the project's own records, not carried
forward from a summary.

---

## THE ONE SENTENCE

**Every open piece of this project sits downstream of a single fact: the program that builds the
positioning data was repaired here, and the repaired version has never been put into service.**
The version actually running still fails outright the moment it meets one of the new class names.
So work that is finished in our code is invisible on the screen, and the one act that would make it
visible -- retagging the commodity and volatility holdings -- was deliberately refused, because a
measurement cut to decide whether that act was safe answered **no**.

**This is the difference worth seeing at a glance: the other project closed its round with nothing
left over. This one cannot close at all without your word.**

---

## THE SIX OUTCOMES

### FWD-1 -- Every holding is sorted into exactly one of five asset classes
**Grade: NOT REALIZED.** Its bar is the hardest kind -- someone must have actually re-sorted real
portfolios and seen every holding land in exactly one class.

**Done here:**
- The program that builds positioning data was rewritten to carry all five classes. Measured side
  by side on the same input: before the change, Commodities, Structured and Alternatives each came
  out as the literal word *Unknown* with a weight of 0.000; after it, each comes out under its own
  name with its real weight.
- It no longer swallows a class it does not recognise. Fed a made-up class, it now warns and names
  the value instead of silently adding it as zero.
- Two other programs that read the same data were tested hop by hop -- 88 of 88 places checked,
  **no silent drops**. A five-class value survives both.
- The classification list itself was made durable. It used to be silently reverted whenever the
  seeding script was re-run; the script now reads what is already there and merges rather than
  overwriting, proved with a before-and-after control against a scratch copy. **The live table was
  never opened.**

**Why it is still not realized:** none of that is in service, and the holdings have not been
retagged. Read live today, seven of the eight relevant tickers are still filed as *hedge* and one
as *equity*.

### FWD-2 -- Volatility and hedge products are shown apart from equities
**Grade: NOT REALIZED.** Same bar, same repaired program, same reason.

**Done here:** the safety question was answered properly rather than assumed. A measurement was cut
to decide whether the retag is safe *now*, against what is actually served. It re-derived the
affected set from scratch rather than trusting the seven tickers it was handed, and found
**eleven**, not seven. It then graded every combination of surface, holding and clause -- **836
checks, every one printed with its verdict and with how it was known.**

**The verdict was NO-GO**, and that is this round's most valuable output. The safety condition is
false at this vintage for **11 of 11** holdings, across **43 distinct surface-and-clause pairs**,
**473 failing checks of 836**. The most decisive single reading: the program that is actually
running fails on the new class names before any other check can even be reached.

The same work priced the fix: **ten groups of change would clear it, and five of those ten sit
behind the portal freeze.**

### FWD-3 -- The five classes always appear in the same order
**Grade: NOT REALIZED**, and we now know precisely why.

**Done here:** the front end was measured directly for the first time -- closing a gap an earlier
round had disclosed but could not close, because those files were outside what its instruments
could read.

**The front end collapses. It does not carry five classes.** Two separate places in the screen code
-- one on the Positioning holdings view, one on the Attribution selection view -- each contain a
hardcoded list naming only *Fixed Income* and *Equity*. A group carrying Commodities, Structured or
Alternatives **is never even looked at**. There is no ordering problem to fix yet, because three of
the five classes do not render at all.

### FWD-4 -- Each class has one color, the same everywhere
**Grade: NOT REALIZED, and nothing was done against it this round.** No cell in the current round
serves it. **This is the honest gap, stated rather than absorbed** -- the colour work is gated
behind the same screens that cannot yet show five classes.

### FWD-5 -- The classification is defined in one place and flows everywhere
**Grade: NOT REALIZED.**

**Done here, and this one genuinely advanced:**
- Your own ruling settled a question the first round had got wrong. That read had judged the
  classification list against a single-source-of-truth architecture and concluded neither end
  qualified. Your purpose ruling -- that it is a curated tagging list a person extends as we
  acquire securities -- **corrected the frame, and the correction was recorded in the open rather
  than quietly absorbed.** The one place does exist: it is the table. The old code list is a
  retired input.
- That one place was then made durable, as described under FWD-1.

**Why it is still not realized:** the bar asks that someone *change a class boundary once and watch
everywhere update by itself*. Nobody has, and nobody can while the screens read a fixed two-class
list.

### FWD-6 -- The places that show asset classes agree with each other
**Grade: NOT REALIZED.**

**Done here:** both views were read at source and compared. **They do agree -- and that is the
problem.** They agree because each carries its own copy of the same hardcoded two-class list.
Agreement about two classes is not agreement about five. And nobody has yet opened both views and
read them, which is what this outcome's bar actually requires.

---

## WHAT HAS NEVER BEEN GRADED, stated plainly

The last formal read of this project graded **0 of 6 realized**, and said that was correct for what
that round contained. **Everything described above from the current round came after that read and
has never been graded at all** -- the round has not been submitted for judgment, because it cannot
be while items remain open.

Five questions sit unanswered as a direct result. Each finished piece of work deliberately recorded
its readings and **offered no verdict**, leaving the judgment to the reviewer. The sharpest of them
bears directly on what FWD-1 and FWD-6 would even mean:

> Is the set of screens and files we checked genuinely the set a retagged value *reaches* -- or
> merely the set our instruments could see?

That is not rhetorical. The instrument the criterion itself named could read about **one file in
nine** of the working copy; **29,824 files were unreadable to it**, and the three most consequential
things eventually found -- a second place that writes the registry, a second live producer, and a
class-rewriter -- **all lived in the part it could not see.** They were found only because a second,
differently-built instrument was constructed to go looking. **A grade taken on the first
instrument's evidence would have read cleaner and been worth less.**

---

## THE FOUR ITEMS CARRIED FORWARD, and which outcomes they touch

Fifteen pieces of work have been cut on this project; eleven are finished. **Four are open**, and
they are the reason the round cannot close:

| the open item | touches |
|---|---|
| the additive five-class reconciliation | FWD-1, FWD-2 |
| the hedge-predicate reconciliation (carried from the earlier round) | FWD-1 |
| the retag itself | FWD-1, FWD-2 |
| the hedge-predicate reconciliation (its successor) | FWD-1 |

**All four touch FWD-1; two also touch FWD-2. None of them touches FWD-3, FWD-4, FWD-5 or FWD-6**
-- those four are blocked by the screens, not by these items.

**All four are one gap seen four times, not four separate stalls.** Each sits downstream of the same
undeployed program.

---

## WHAT EACH OUTCOME WAITS ON, AND WHOSE WORD MOVES IT

| outcome | waits on | whose |
|---|---|---|
| FWD-1, FWD-2 | putting the repaired program into service, then the retag that is currently refused | **yours** for the release; the refusal lifts on its own once the surfaces can carry five classes |
| FWD-3, FWD-4, FWD-6 | the screens rendering five classes instead of a hardcoded two | **yours** -- it is inside the portal freeze |
| FWD-5 | both of the above, and then someone actually changing a boundary and watching it flow | **yours**, downstream of the two |
| the round closing at all | whether it may close with **four items unfinished, not two**, carried forward with reasons named | **yours** -- already in front of you |

**Nothing here is waiting on a seat on this box.** Everything measurable has been measured; what
remains needs either a release or a freeze lifted, and both are yours.

---

## WHERE THIS DEPARTS FROM THE SHAPE I WAS ASKED FOR

Two late findings were suggested for inclusion where they bear on a grade. Both belong to the other
project's round rather than this one, so importing them would misattribute them. **This project's
own version of the same lesson is recorded above**: the measurement that mattered most was invisible
to the instrument the work itself had named, and was recovered only by building a second one.
