# ENDPOINT (step 2, `/endpoint --forward`) -- comp-heat and the tooling at the outset of the Semantic Estate Pipeline

**Seat:** `1.0.0_SA_CTO` (L2; the only seat that cuts the endpoint). **Phase 0** -- runs BEFORE the PRD and before any task
order. **Written:** 2026-09-04 ~14:1xZ.

**INPUT, the only thing read for this phase (Step F1):**
`docs/briefs/comp-heat-and-the-semantic-estate-pipeline-outset-tooling-brief-20260904.md` @`bc52eb658d`
(334 lines, 27,139 bytes; `4.0.0_SA_CRO`, measured 12:55Z-13:50Z; no `generated` line -- its Part VI carries a clock per row).

**STATUS: NOT YET LANDED.** No PRD exists for this work (the brief's own `PROJECT: NONE-YET`), so the block below is emitted
ready to paste and lives nowhere else yet. Its home is the section titled **`ENDPOINT (step 2, /endpoint --forward)`** in the
project's PRD at its tree home -- `org/missions/D<n>/<MACRO>/<CODE>/prd/<CODE>_PRD.md` -- and the directive, macro and code
are fixed at **L3 (register), which has not run.** An endpoint that lives only in a terminal is the carrier problem this
phase exists to close; this file is the carrier until L3 and L4 land.

**AWAITING:** Andrew's confirmation of the `DONE WHEN` lines (his own standing ruling, 2026-09-03 ~05:2xZ: *"i will confirm
CTO's DONE WHEN from their /endpoint --forward, but after that point ... I want the canonical loop to be able to keep cycling"*).
Nothing downstream moves until he reads these eight.

---

## The block, ready to paste

```
  FWD-1  Someone asks how cold or how busy a part of the estate is, and gets a
         bounded answer they can act on
         DONE WHEN  EXERCISED -- someone has asked and been answered
         ACCEPT     a person asking "what here has gone quiet" or "what have I
                    written and not saved" gets an answer that says how much of
                    the estate it looked at and when it looked, comes back
                    inside the time they allowed it, and can be asked about one
                    corner rather than the whole place; and a person who does
                    not know the thing exists is pointed at it when they ask the
                    question in their own words -- where today they read the
                    history by hand
         SOURCE     brief O1; Part IV F1, F3 (nothing routes the question), F4
                    (no bound today)

  FWD-2  Someone asks one question that spans the code and the live estate, and
         never has to know how it is answered
         DONE WHEN  EXERCISED -- someone has asked and been answered
         ACCEPT     a person asks, in their own words, which things are busy in
                    one place and idle in the other, and gets a single answer
                    that says which sources it put together and when each was
                    last built -- without writing a query by hand and without
                    knowing that anything was started in the cloud to answer it
         SOURCE     brief O2; Part IV F2 (it already works and nobody has used
                    it; the answer carries no age today)

  FWD-3  A reader of the daily report can follow any fact back to what produced
         it and get the same answer again
         DONE WHEN  EXERCISED -- a reader has followed one line back and
                    reproduced it
         ACCEPT     a reader who doubts a line in the day's report can find what
                    produced it, ask that thing again, and get the same line;
                    where today the report's own workings are the only account
                    of where its facts came from
         SOURCE     brief O3, bar B2; Part IV F7 (the report computes its own
                    facts and names the tools only in passing)

  FWD-4  Andrew decides a day's proposals on evidence he can argue with
         DONE WHEN  EXERCISED -- one day has been decided that way
         ACCEPT     at a sitting each proposal points at the finding it came
                    from, so the argument is about whether that finding is right
                    -- never about whether the thing proposing it had looked at
                    the estate at all
         SOURCE     brief O4, bars B4 and F8; the standing condition on the
                    deferred days (LD-0522 Amendment 1), of which this is the
                    gradable form

  FWD-5  Anyone can see which of the things feeding the daily analysis worked
         today, and one that failed says so
         DONE WHEN  EXERCISED -- the working order has been read from one place
                    on a real day
         ACCEPT     a person can tell in one look which of the things that feed
                    the day's analysis answered and which did not; one that
                    could not answer says so in its own words and says how much
                    it did manage to look at, and never leaves a blank space
                    that reads like a clean result
         SOURCE     brief O5, bar B3

  FWD-6  The things at the front of the pipeline fit together, and nothing is
         measured twice
         DONE WHEN  APPLIED -- the one account of how they fit is written and
                    nothing does another's job over again
         ACCEPT     someone can put two or three of these questions together --
                    is this busy, is it drifting, has it shipped -- and get an
                    answer without anyone building a new thing to do it; and no
                    two parts of the estate work the same measurement out in
                    their own way, or where one must, it says plainly which
                    other one it is standing in for
         SOURCE     brief O6, bar B5; Part IV F7 (the same measurement exists
                    twice today, and the second one says so)

  FWD-7  Something people already read gets its numbers from this tool
         DONE WHEN  EXERCISED -- a run shows a reader's own material carrying
                    them
         ACCEPT     a thing people already look at takes its figures from this
                    tool, shown by a run that anyone can repeat, so "nothing
                    uses it" stops being true because of evidence and not
                    because someone connected it and said so
         SOURCE     brief O7; Part IV F3 (the one thing that names it gives up
                    before reaching it)

  FWD-8  "Is this safe to put away?" is answerable, advisory, and never acts on
         its own
         DONE WHEN  EXERCISED -- someone has asked and got a list they could
                    argue with
         ACCEPT     a person asking what is safe to put away gets a ranked list
                    with the reason for each line, can disagree with any of
                    them, and nothing is ever removed by the tool itself
         SOURCE     brief O8; Part IV F5 (the parts that would answer it are
                    built and reachable from nothing), P8 (never auto-delete)
```

---

## Notes the PRD carries, and why they are NOT outcomes

- **Discoverability is a limb of FWD-1, not its own outcome.** The brief puts the routing row at P9 (a precondition), and a
  tool nobody can find fails FWD-1's own acceptance -- so it is graded there rather than minted as a ninth id.
- **The deferred days are not an outcome.** Their release is the CONSEQUENCE of FWD-4 and FWD-5 holding; an outcome that
  says "the deferral lifts" would grade itself on someone else's decision.
- **The consumption seam's SHAPE is not an outcome** (brief F7, P5: outputs shipped to the host, or a host that can run the
  tools). FWD-3 and FWD-6 say what must be TRUE either way; which shape buys it is the PRD's and the decomposition's.
- **comp-heat's place on the marquis list is not here** -- it is downstream of the tool working (the ratification's own
  words, and the brief's Part II).
- **Eight outcomes, eight territory items.** The brief's O1-O8 map 1:1 to FWD-1..FWD-8 in order. That is the brief's cut,
  not a coincidence: this seat tested for a ninth (discoverability, the deferral, the seam's shape) and each collapsed into
  an existing outcome or into a precondition, above.
- **`FWD-n` ids are permanent and never reused** from the moment this block lands in a PRD; a retired outcome leaves its
  number vacant.

---

## Provenance (Step F5)

- **BRIEF:** `docs/briefs/comp-heat-and-the-semantic-estate-pipeline-outset-tooling-brief-20260904.md` @`bc52eb658d`,
  334 lines / 27,139 bytes, read whole at this seat before writing a line of the block.
- **EVERY OUTCOME TRACED:** each `SOURCE` above names the brief's own Part I item and the Part IV finding or Part III bar it
  rests on. No outcome was invented from the topic string; no number was invented anywhere.
- **NOT READ, deliberately (the phase is defined by what it refuses):** the task-order register and every task order; any
  project row or `project.json`; the sibling PRDs (`NFRA_FEDOBS`, `NFRA_CLDGRPH`, `NFRA_COMPDRIFT`, `NFRA_COMPDIFF`,
  `NFRA_DEBTSCAN`); the estate-report runner's source; `/estate-pull` and the manifest contract; the Kimi half.
  **Stated precisely because a false "not read" is worse than a read:** this seat read `NFRA_COMPEFFICACY`'s PRD s.4.4
  EARLIER TODAY, for that project's own FWD-10 grade, and did NOT re-read it for this phase -- the inherited bar reaches
  this endpoint through the brief's citation of it (Part II, P4), not through a fresh read.
- **NOT DONE:** no PRD written, no project registered, no cell, no task order. L3 and L4 follow Andrew's confirmation.

**Push state:** LOCAL on commit; origin/CLOUD @`351f309e0a` (this seat's `ls-remote` read at 12:40Z; a push window is
approved and lands with `0.0.0_AB_MSTR`, after which this claim ages).
