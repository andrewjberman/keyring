# /self-drive AMGT_RESAPP & POSN_ASTTAX -- tick 43 (covers ticks 42-43)

**seat:** `1.0.0_SA_CTO~Z` · **state:** ARMED · **device:** sitez · **2026-09-13T03:41:03Z**
Tick 41's log is `@ffd3e6b305`, committed `2026-09-12T22:27:18-04:00` (author time, not the filename).
Tick 42 was QUIET and wrote nothing. **Tick 43 is not: round 8 drained, a new Andrew-direct landed,
a standing CTO decision was taken, and a figure this seat put in front of Andrew turned out wrong.**

---

## 1. AMGT_RESAPP ROUND 8 IS FULLY DRAINED -- 46 OF 46, AND THE ROUND IS NO LONGER THIS SEAT'S

`rg-2` went terminal during tick 42/43. `2.0.0_SA_COO~ZZZ` closed the round at `@790607c9ef`:
`dep_stage` EXECUTING -> ROUND_CLOSE, **L8 packet compiled and handed to `3.0.0_SA_CVO~Z`**, whose
inbox carries it as of `03:14:45Z`. That seat is LIVE (18s at the read).

⛔ **THE L10 ORDER IS LOAD-BEARING AND THIS SEAT IS WAITING BY DESIGN.** The round-8
`ROUND_ANALYSIS` is owed only after the slug (`REMEDIATION_v8`) is cut; `v7` is the newest. Nothing
is pre-written. Measured: `.../remediations/` holds v1-v7; `ledger/` holds `ROUND_ANALYSIS.round1`
through `round7` plus `ROUND8_PACKET.md`.

## 2. ANDREW-DIRECT 22187 (03:21:46Z) -- A WORK DIRECTION, AND IT REACHES THIS LANE

VERBATIM, the part that binds here: *"they should get all of this stuff done now, RESAPP ASTTAX and
the RESAPP harvest publication backfill. Also I expect frontend for both RESAPP and ASTTAX to be
done too, despite not pushing to promote until a future date."* **NO PROMOTE, stated twice.** Nothing
in this tick touches the portal; `HEAD:portal e85f6eb84f`, unmoved.

**FIRST QUESTION THIS SEAT OWED ITSELF, BECAUSE IT IS THE L2/L4 OWNER: do the specifications
actually REACH "frontend done"?** They do, and it cost one read each -- so there is no L4 gap and no
addendum is needed. ASTTAX's frontend outcome is **FWD-6** ("the places that show asset classes
agree with each other"), mapped to surface **S3**, the two views that render. RESAPP's is **FWD-9**
plus round 8's three consumer-side cells. Both L4-R halves on both projects read SIGNED and current
(`AMGT_RESAPP v0.5 @932d83eb17`, `POSN_ASTTAX v0.5 @5840cc12ac`).

⛔ **AND THE COLLISION THAT ANSWER EXPOSES, WHICH IS THE USEFUL OUTPUT OF THIS TICK.** ASTTAX's
FWD-6 is **round-4 work**, and round 4 cannot be cut until round 3 reaches L10, and round 3 cannot
reach L10 while **4 of 15** orders are non-terminal -- the refuser counts open orders PER PROJECT,
never per round (LD-0521). **Those four are the carry-forward call that has sat with Andrew since
~01:0xZ.** So *"I expect frontend for both RESAPP and ASTTAX to be done"* **cannot be ordered for
ASTTAX at all** until he answers it. That is not a seat working slowly; it is one of his own open
calls standing directly in front of the thing he just said he expects, and it went to
`0.0.0_AB_MSTR~Z` for the one-pass list with a REC: **carry the four forward** -- all four sit
downstream of one undeployed generator and the retag is NO-GO, so they cannot run today under any
answer, and carrying them closes round 3 at no cost that is not already paid.

22202 answered his four sovereign items minutes later. **None of the four touches this lane** --
they are harvest/backfill and are `4.0.0_SA_CRO~Z`'s. Read, not acted on.

## 3. A STANDING CTO DECISION TAKEN RATHER THAN HELD -- `Z-C-S55`, row `Z-S42` `@9d7b09987f`

Tick 41 scheduled this act to POSN's L10. **His direction reaches it and the scheduling reasoning
did not survive contact:** the reason to wait was that opening a PRD mid-round is a disruption --
but that is a reason to defer the *edit*, never the *decision*, and the decision had simply not been
made. It is made now.

**THE RULING:** the additional ETF publisher is **OUT of POSN's WRITE scope and IN its DISCLOSURE
scope.** Three facts from `Z-C-S55`'s own text decide it and they point different ways: it *copies*
gold holding class values and emits a four-key book allocation at its lines 469-472, so a retag
reaches it and the PRD's closed two-sibling set is **wrong as written**; its live artifact carried
189 rows over four books and **zero candidate members**, so its current bytes cannot exercise
post-retag loss; and it belongs to another project, which **forecloses a write outright**. The only
live question was whether POSN may stay silent about a surface it cannot touch. **It may not** --
Rule 24's subtraction is over the surfaces a retagged value REACHES, not the surfaces this project
may EDIT, and a list that drops members for belonging to someone else is a subtraction over the
wrong domain that still prints a denominator.

⚠ **AND THE ZERO IS NOT SAFETY.** Zero candidate members is a STATE, not a property; it flips the
first time a candidate member appears in any of those four books. So the disclosure carries its own
falsifier -- the measured zero WITH the condition that ends it. A zero recorded without its expiry
is the same shape as a criterion that returns the same answer in both worlds.

**Carrier:** one line in PRD s.4, which sits inside the ratified half. POSN is mid-round-3, so it
lands in the round-3 L10 addendum. **The decision is not deferred** -- `2.0.0_SA_COO~Z` read the row
off the commit and executed it as a ruling within four minutes, without a message, which is the
doctrine working.

## 4. `Z-W10-S1`'s ACTUAL DANGER CLOSED WITHOUT TOUCHING THE FROZEN SPEC

Its formal disarm is a PRD edit this seat will **not** make mid-round: Rule 27 freezes the spec, both
halves are signed and current, and re-opening the ratified half would block round 4's cut. But the
danger does not need the edit. PRD s.4 states the live mechanism as *"no else in the allocation
if/elif chain, so a Commodities value renders Unknown AND its weight accumulates to 0.000."* **The
weight half is false at HEAD** -- `AT2-s-1` added the else to all three chains and the served
allocation reads 2.5. The real loss sits at the five-class served view and at the delta and spread
rows, which were ABSENT rather than zero.

⛔ **WHY IT COULD NOT WAIT:** the next cell to read that sentence is **`AT3-s-5`, the bar that GATES
the retag.** A bar built on *"confirm the weight zeroes in the allocation dict"* returns **the same
answer pre- and post-retag** -- a gate that cannot fire, on the exact act Andrew is holding. The
corrected reading went to the round owner so the bar is cut right whenever it is cut. **The text
still gets fixed at L10; the hazard is closed today.**

## 5. A FIGURE THIS SEAT PUT IN FRONT OF ANDREW WAS WRONG -- `Z-S61`, corrected `@5d688b925d`

The FWD addendum said the outcome bars were set **"ninety-eight minutes"** before the first order.
**Wrong.** Over every commit touching the RESAPP PRD:

```
c0b5636ea9  2026-09-10T14:32:06-04:00  THE PRD'S FIRST COMMIT -- all fourteen FWD ids, and at
                                       line 49 the literal "BAR DISTRIBUTION: 13 of 14 are
                                       EXERCISED; only FWD-9 is APPLIED"
8019bf6433  2026-09-10T14:57:00-04:00  the SAME line, unchanged, at line 215
908880f6d1  2026-09-10T16:35:57-04:00  first issuance
                                       TRUE GAP 2h03m51s, not 98 minutes
```
Negative control fired: `git show c0b5636ea9~1` on that path returns *"exists on disk, but not in
`c0b5636ea9~1`"*, so the birth commit is genuinely first. What actually changed between the two
commits: the token `EXERCISED` goes **3 -> 16** in the body and the file **269 -> 483** lines.
`8019bf6433` is where each bar was written out **on its own row**; the bar regime never moved.
**Rule 22 GRAIN -- this seat read the token's SHAPE becoming visible as the claim's OBJECT arriving,
the fourth instance of that exact shape it has recorded tonight.**

⭐ **THE PART WORTH MORE THAN THE FIGURE: the error made this seat's OWN case WEAKER, and an error in
that direction does not trip the reflex that catches one making it stronger.** It surfaced only
because `4.0.0_SA_CRO~Z` measured the same fact from a different commit, unprompted, on its own limb,
and the two numbers disagreed in the open. **That seat was right and this one was not.**

**Corrected in this seat's own artifact**, with a note stating what the line used to say. **Not
corrected by this seat:** `2.0.0_SA_COO~ZZZ`'s explanation brief carries the old figure at its own
line 88 in its own voice -- that document is not this seat's, its author has the measurement, and
the brief already discloses both figures and says they are stated rather than averaged.

## 6. AN INSTRUMENT FAULT FOUND WHILE SENDING, AND IT IS THE DANGEROUS KIND

This seat's broker send **refused six times reporting an EMPTY body while a body was supplied.** Two
probes bisected it: a ~250-character body delivers; ~420 and above refuses, single-line or not,
single recipient or a list, with or without quotes. **So a long substantive send silently loses its
body, and the only thing standing between that and a delivered empty message is the send guard's
own refusal.** The guard is correct and it is the sole reason this was visible. Work routed to the
durable carrier instead -- which is the right answer anyway.

## 7. OPEN CALLS / COMPLETION

```
OPEN CALLS IN SCOPE: 0 adjudicable · 3 RESERVED · NO PITCH (unchanged; CVO-confirmed at tick 31)
  the ALL-RESERVED tell does NOT fire: the queue is 0 adjudicable, not all-reserved
COMPLETION TEST: NOT DONE -- 0 of 2 complete (denominator: 2 projects, 2 of 14 live directives)
  AMGT_RESAPP  ROUND_CLOSE  REACHABLE  0 OPEN of 46 -- round 8 drained; L8 packet at the CVO
  POSN_ASTTAX  EXECUTING    REACHABLE  4 OPEN of 15 -- round 3; L10 held on Andrew's four-order call
  UNREACHABLE: 0     HELD-AT-STOP: not reached
```
Register agrees with the gate on both directives (D4 6=6, D5 0=0 -- D5 moved 1 -> 0 this tick).
**Push state:** `origin/SITEZ 649b7ed1f2`, local ahead 1 at the read. `HEAD:portal e85f6eb84f`,
unmoved. No TO cut, no dispatch, no apply, no merge, no promote.

## Compiler Tools

`to-check.py`'s `find_all_to_files` + `parse_to_file` driven directly for a per-project open census
over a 2593-file denominator with `ZZZZ_NOSUCH` as the negative control · `git log --reverse` over a
single PRD path with `git show <commit>~1` as a birth-commit control · a token census (`EXERCISED`
3 -> 16, lines 269 -> 483) as the discriminator separating presentation from regime ·
`prd-signoff.py status` on both projects · the fence-line channel reader admitting both bracket and
brace blocks · `git status --porcelain` on each channel path before appending · `date -u` measured
at the write, not before it · post-write verify with a `Z-S99` negative control and `git show
HEAD:<path>` as the oracle after commit · two deliberate send probes to bisect the empty-body fault ·
`safe-commit.sh -F` with the message file written by a non-shell writer.
