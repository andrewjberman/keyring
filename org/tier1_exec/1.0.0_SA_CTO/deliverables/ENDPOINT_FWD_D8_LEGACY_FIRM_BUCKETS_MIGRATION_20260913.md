# ENDPOINT (step 2, `/endpoint --forward`) -- D8, the first migration: three legacy firm buckets

> **NOT YET LANDED IN A PRD, AND NO PROJECT CODE EXISTS YET.** This block is emitted ready to paste.
> Its home is this project's PRD under a section titled exactly `ENDPOINT (step 2, /endpoint
> --forward)`, because step 10 reads it back to answer *"does the PRD name this outcome?"*
> **L3 registration is this seat's and has not run** -- the code is unminted, so the PRD path cannot
> be stated yet. That is the next act, not a blocker on this cut.

**Cut by:** `1.0.0_SA_CTO` (L2), 2026-09-13.
**From:** `docs/briefs/d8-legacy-firm-buckets-migration-brief-20260913.md` @`2ffcf91342`, 35,948 bytes
(worktree and record agree -- both read, they match, so no line-ending ambiguity on this one).
Author `4.0.0_SA_CRO~D`, mode NEW (greenfield). Eight outcomes O1-O8 in Part I; eight bars in Part III.
**Directive:** D8 "Data Pipelines", per Andrew-direct ~02:3xZ. D14 supplies the law this project
executes; it does not own the project.
**Andrew has NOT read this brief.** His 2026-09-03 word is that he confirms the CTO's DONE WHEN from
this pass.

---

## THE EIGHT OUTCOMES

```
  FWD-1  Anyone who looks at where a piece of data is kept can tell what it is and
         whose it is, without opening it
         DONE WHEN  EXERCISED -- two people have actually read the same set of
                    locations and compared answers
         ACCEPT     two people who have never worked together read the same list of
                    storage locations and each says, for every one, which system
                    made it, which firm it belongs to, how finished it is and what
                    it holds -- and they agree -- where today the same kind of
                    information is written three different ways and neither reader
                    can tell whose it is
         SOURCE     brief Part I O1; bar Part III O1/O2

  FWD-2  A person moving the old data works out where every piece goes by following
         one rule, never by deciding
         DONE WHEN  EXERCISED -- someone has placed the whole set this way and a
                    second person, working alone, got the same answer
         ACCEPT     one person works through every piece of data in the three old
                    places using a single table; every piece lands in exactly one
                    destination and nothing is left unplaced; a second person doing
                    it alone reaches the same answer; and anything the table cannot
                    place is treated as a fault in the table rather than a decision
                    for whoever is holding it
         SOURCE     brief Part I O2; bar Part III O1/O2

  FWD-3  Anything that needs to know where a firm's data lives looks it up in one
         place instead of having the answer written into it
         DONE WHEN  APPLIED -- each of them reads it from the one place
         ACCEPT     someone changes where one firm's data lives in a single place,
                    and everything that serves, guards or directs that firm's data
                    follows from that one change, with nobody editing it in several
                    files -- where today the same firm is written eight different
                    ways in eight different places
         SOURCE     brief Part I O3; bar Part III O3

  FWD-4  A firm's people see exactly what they saw before on the day their data
         moves, and cannot tell from looking that anything happened
         DONE WHEN  EXERCISED -- a firm has actually been moved and the result was
                    read back deliberately
         ACCEPT     after a firm's data is moved, someone deliberately compares what
                    is being served now against what was served before and finds it
                    identical for everything a user can reach; the sign-off named
                    every piece that moved and how to put each one back; and the old
                    copy is still sitting there untouched for the agreed period.
                    A real user opening the page and noticing nothing is the
                    CONFIRMATION, never the proof
         SOURCE     brief Part I O4; bar Part III O4

  FWD-5  Whoever owns a pipeline can see that everything which sets it running now
         points at the new home, and nothing points at the old one
         DONE WHEN  EXERCISED -- the owner has read the live settings and found it so
         ACCEPT     the person responsible for a pipeline reads the live settings
                    themselves and finds nothing still aimed at the old home, and
                    everything that ought to start their pipeline present on the new
                    one -- read from what is actually running, never from a written
                    procedure that says it was done
         SOURCE     brief Part I O5; bar Part III O5

  FWD-6  An operator can prove, before anything is thrown away, that nothing used the
         old home for an agreed stretch of time
         DONE WHEN  EXERCISED -- the proof has been produced and read for a real case
         ⚠ CARRIES THE ONE GENUINE WAIT IN THIS ENDPOINT -- expressly qualified below
         ACCEPT     before anything is deleted, the operator shows a record that
                    nothing wrote to the old home and nothing read from it for the
                    whole agreed stretch, measured by a named instrument rather than
                    asserted from memory; everything that pointed at it has been
                    moved or switched off; and throwing the old copy away is treated
                    as its own decision needing your word, because here "deleted" can
                    mean only "hidden" -- where today "retired" means "nobody
                    remembers anyone using it"
         SOURCE     brief Part I O6; bar Part III O6

  FWD-7  The one thing this estate is forbidden to write has either a named
         replacement or a recorded decision to let it go
         DONE WHEN  EXERCISED -- someone has actually pointed at the decision
         ACCEPT     someone asked what became of it points at one recorded decision
                    saying either what took its place, or that nothing did and the
                    thing that watched for it was switched off with it
         SOURCE     brief Part I O7; bar Part III O7/O8

  FWD-8  Something deliberately allowed to stay where it is, inside a place being
         shut down, is either moved by a decision or the place stays open for it
         DONE WHEN  EXERCISED -- someone has actually read the disposition
         ACCEPT     someone reads, in one place, either where it now lives together
                    with the decision that moved it, or the sentence that keeps the
                    old place open for that one thing -- and neither is left to be
                    discovered by whoever is doing the shutting down
         SOURCE     brief Part I O8; bar Part III O7/O8
```

---

## ⛔ FOUR THINGS THE CUT SURFACED

### 1. FWD-6 CARRIES A GENUINE WAIT, AND RULE 27 SAYS THAT NEEDS ANDREW'S WORD BY NAME

Rule 27's L2 clause: **no FWD is a wait** -- every outcome is provable by an act a seat can take ON
DEMAND, and *"a genuinely essential wait is EXPRESSLY QUALIFIED on the outcome with its reason and
Andrew's word."*

Seven of these eight are on-demand. **FWD-6 is not, and it cannot be made so by re-cutting.** Its
substance is *nothing used this for an agreed stretch of time*, and a quiet window is elapsed time by
definition -- you cannot compress it without destroying the thing it measures. This is the narrow
case the rule carves out, not a wait I failed to drive.

⚠ **SO IT IS QUALIFIED HERE AND NEEDS ONE LINE FROM ANDREW: how long the quiet window is.** That
number is his, it is the only genuinely blocking input this endpoint has, and it should be settled
before L5 rather than discovered at L7 when someone wants to delete something.

⭐ **WHAT I DID NOT DO, DELIBERATELY: split FWD-6 into "the proof machinery exists" plus "the window
elapsed."** That would have produced a gradeable APPLIED outcome and a tidy-looking endpoint, and it
would have been the retirement dressed as rigour -- the project could then close with the machinery
built and nothing ever proven quiet. **The wait is the outcome's substance, so it stays on the
outcome.**

### 2. FWD-4's MECHANISM IS DRIVEN, AND THE ORGANIC CASE IS DEMOTED TO A CONFIRMING ARM

The brief's O4 reads *"users see the same dashboard the morning after their cutover."* Taken
literally that grades on an event nobody controls -- a user happening to look, and not complaining.
**Under Rule 27 I re-cut the mechanism to a deliberate comparison of what is served before and after,
and kept the organic case as the confirming arm** ("a real user noticing nothing is the
CONFIRMATION, never the proof"). The outcome's substance is unchanged; what changed is who has to
act for it to be gradeable. **This is a bar being made STRICTER, not looser, and it is stated rather
than absorbed.**

### 3. FWD-3 IS CUT AT `APPLIED`, ON PURPOSE, AND IT IS THE ONE PLACE I LOWERED A BAR

Part III's O3 bar is *"cutting a firm over touches ONE registry row and the router, the guards and
IRPT follow"* -- which is only fully demonstrated BY a cutover, and a cutover is FWD-4. Cutting FWD-3
at EXERCISED would grade the same act twice and make FWD-3 ungradeable until FWD-4 lands, for no
extra information. **At `APPLIED` it asks the answerable question -- does each consumer READ the one
place, or does it still spell the name itself -- which is inspectable on demand today.** If Andrew
wants the stricter reading, FWD-3 simply becomes a consequence of FWD-4 and stops being its own
outcome.

### 4. ⛔ THE CANONICAL PATH STRING IS A PROPOSAL, AND RATIFYING IT IS AN L4 ACT I AM INHERITING

The brief's IV.5 PROPOSES the canonical string with the firm key as the tenant-grain invariant, and
says plainly that **if ratified it SUPERSEDES the 2026-08-18 template's existing tier-first form.**
FWD-1 and FWD-2 are written against the proposal, so **they are not gradeable until it is ratified,
and that ratification is mine at L4, not the brief's.**

⛔ **RESOLVED BY ANDREW ~03:2xZ 2026-09-13, AFTER THIS ENDPOINT WAS CUT -- RECORDED HERE SO L10
DOES NOT READ A CLOSED QUESTION AS OPEN.** He ruled the string itself: **SOURCE-FIRST**,
`{source}/{scope}/{tier}/{table}/{partition}`, the same string in every bucket -- firm, product and
monolith alike (relayed `4.0.0_SA_CRO~D` 96332; his verbatim *"all recs approved"*). **So FWD-1 and
FWD-2 ARE GRADEABLE**, and the L4 act below is no longer a ratification of a PROPOSAL -- it records a
string he has already ruled. ⚠ The supersession I flagged is REAL and is now his: the ruling displaces
BOTH the 2026-08-18 template's tier-first form AND `MDPF_CANON_PRD.md` s.3's
`gold/{scope}/{artifact}/date=...` -- **both of them his own earlier words, and both older.** Neither
is edited by this endpoint; each is an L4 act in the project that owns it.

The original flag, kept because the reasoning is what made the question worth asking:

I am flagging it rather than quietly treating the proposal as settled, because the prior form is
**live in a template that already minted a real bucket** -- superseding it is a change to an existing
grammar, not the filling of a blank. Andrew named canonical path strings as the thing he most wanted
from this work, so the substance is his; the ratification mechanics are mine.

---

## PROVENANCE

**READ:** `docs/briefs/d8-legacy-firm-buckets-migration-brief-20260913.md` @`2ffcf91342` -- Part I
(eight outcomes, lines 29-93), Part II (the boundary and the sibling table, lines 94-121) and
Part III (the bars, lines 122-136). Structure read first: **eight top-level headings, denominator
printed, at both the worktree and the record, which agree at 35,948 bytes.**

**WHY PART II WAS READ when the skill cuts from I and III:** the boundary is what decides whether an
outcome's proof reaches into a project this one does not own -- the failure I flagged on the D14
endpoint's FWD-6 a few hours ago. Read here to check it, and it does not recur: every one of these
eight is provable inside this project's own stated ownership.

**NOT READ, deliberately:** the task-order register, `query_project`, any project JSON, the directive
register. Phase 0 reads the brief and nothing else -- a step-2 endpoint assembled from the register
returns an empty set and calls it an endpoint.

**NOT READ and load-bearing:** Part IV's thirteen findings were read only where Part I cites them
(IV.5 for the path-string proposal, and the IV.10/IV.11 items this seat supplied). Part V
(preconditions), Part VI (status) and Part VII (ten things not measured) were NOT read at this cut.
⚠ **Part VII in particular names what the brief does not claim, and an endpoint cut without reading
it can promise something the substrate cannot support.** It is the first thing to read before the PRD.

⛔ **READ SINCE THE CUT -- Part VII, all eleven bullets, 2026-09-13 ~04:0xZ.** The line above was true
when written and is no longer. Two bullets bear directly on outcomes, and one on the brief itself:

- **FWD-4 -- A LIFECYCLE RULE CAN SILENTLY FALSIFY ITS ACCEPT LINE.** Part VII: *"No lifecycle rule was
  read (counts only): a rule that expires or transitions objects in a legacy bucket is a hazard to the
  rollback window."* FWD-4 promises the old copy is *"still sitting there untouched for the agreed
  period."* **An expiry or transition rule on a legacy bucket breaks that promise with no act by anyone,
  and nothing in the comparison FWD-4 grades on would notice.** Reading every lifecycle rule on the
  three legacy buckets is therefore a precondition of FWD-4, not a MAP-step detail.
- **FWD-5 -- THE BRIEF'S SCHEDULE COUNT IS DECLARED-PLANE, AND ONE INSTRUMENT IS BLIND TO PART OF IT.**
  Part VII: the ~45 schedules were read from `trigger-map.json`, not the live scheduler, and *"EventBridge
  SCHEDULER schedules are invisible to `describe-rule`."* FWD-5's ACCEPT already demands the live settings
  over any written procedure; **its proof must also read the Scheduler service itself, because
  `describe-rule` returns a clean not-found for a Scheduler schedule -- a wrong instrument that reads as
  "nothing fires this."**
- **THE BRIEF'S OWN REFS BLOCK CITES A FILE THAT DOES NOT EXIST.** Its `BRIEF PATH` reads
  `docs/briefs/d14-legacy-firm-buckets-migration-brief-20260913.md`; the file is `d8-...`, renamed before
  its first commit. The same class of defect as Rule 17b's D8 citation tonight, in the carry-forward block
  a later seat is most likely to copy. Reported to `4.0.0_SA_CRO~D`; not edited here.

**NOT CLAIMED:** that these are the outcomes Andrew wants -- that is his confirmation, per his
2026-09-03 word. **Nor that the eight are complete against his commission**: he asked for the swap
"end to end, including decommissioning of legacy resources," and whether eight outcomes cover
everything he meant by that sentence is a question for his read, not a claim of this cut.
