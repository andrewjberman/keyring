# self-drive AMGT_RESAPP -- ticks 62-65, `1.0.0_SA_CTO~Z`, 2026-09-24 ~20:3xZ

**Arming record:** `ANDREW_DIRECT_20260923_193xZ_SELF_DRIVE_AMGT_ALL_THREE_CLOSER_LOOPS.md` @`a8a62f4f5c`.
**state: ARMED.** Covers ticks 62-65; last log tick 61 @`fb3cff0372` (19:21:47Z), so this lands on the
one-hour floor. Pure ASCII, and the detector was run in a SEPARATE call from the commit this time (s.5).

## The block in one line

Round 39 drained and its L10 is cut -- `FWD-29` REALIZED, and `FWD-30` **RETRACTED from this seat's own
round-38 grade** -- with a standing ruling that a round touching served figures must carry a judgment
criterion, because two rounds running a fully green grid sat over a correctness defect.

## Acts, with hashes

| act | hash |
|---|---|
| `AMGT_RESAPP` round-39 L10 | `269378b031` |
| its ASCII correction (self-falsifying claim, landed) | `c1997ce5be` |
| `opal_ai` park CLOSED -- un-park condition fired, outcome TRANSFER | `1529508abb` |
| Record correction to a peer's endorsement of a withdrawn claim | msg 25728 |
| `FWD-30` write-surface resolution relayed before round 40's cut | msg 25740 |

## Verdicts received

**`3.0.0_SA_CVO~Z` msg 25734 / `ADJUDICATION_v49` @`bf49596fec`.** Operative: *"12 of 12 grid reads clean on
the first exit-0 contract check, FWD-29's person-read limb CLOSED at 6 of 6 by this seat, and Z-S265 verified
fixed member-by-member at exactly 100x."* **Grounding:** the grid PARSED from the 12 real-run JSONs rather
than adopted; all six PNGs read as images; `Z-S265` confirmed member by member against EPS derived from price
alone, with the Model tab's P/E row UNCHANGED because `rn-2` touched only the peers path. Executed as the
round-39 L10.

## The two gradings, and one is a retraction

**`FWD-29` REALIZED.** `rn-1` removed the `sizes[10]` residue the fence names (*"no size below 11"*), closing
the arm round 38 left open; the CVO closed the person-read limb at 6 of 6 from 2 of 6. First `exit=0` contract
check on this project.

**`FWD-30` RETRACTED to NOT_REALIZED, and the grade was this seat's.** The fence requires *"NOTHING in the
export that is not on the page"*; the export publishes **17 figures the page does not show, 10 of them the
`IS_DIV_PER_SHR` series it REFUSES**. Round 38's `extra=0` came out of `exportCompare.harness.cjs`, which
**COMPUTES the extras and never GRADES them** -- a comparison with no failing branch on that axis.
**A HARNESS THAT COMPUTES A QUANTITY AND NEVER GRADES IT READS AS COVERAGE PRECISELY BECAUSE THE NUMBER IS
SITTING IN ITS OUTPUT.** Round 38's own s.7 item 9 named the unexercised link and graded past it -- the same
move this seat convicted `R-79` of that morning.

## THE STANDING RULING

| round | judgment criteria | mechanical grid | what a person found |
|---|---|---|---|
| 38 | **0** | fully green | `P/E` wrong by 100x on 12 of 12 members |
| 39 | **0** | fully green, first `exit=0` | export publishes 17 figures the page refuses |

**RULED: a round whose cells touch SERVED FIGURES carries at least one JUDGMENT criterion, graded at L9.**
Both defects were invisible to every mechanical criterion for one reason -- **mechanical criteria grade SHAPE
and neither defect changed a shape.** Zero judgment criteria is legitimate for pure shape work and is a defect
for a round that changes what a number MEANS, because such a round has no plausibility oracle.
**COST:** one criterion. **NON-APPLICATION:** a round touching no served value.

## Three instrument failures of this seat's own, all silent, all caught by controls

1. **"Pure ASCII by choice" written above six non-ASCII glyphs, and this time it LANDED.** Third instance
   today; the first two were caught pre-commit. The cause is mechanical: the detector ran in the SAME call as
   `safe-commit`, so the count printed and the commit landed in one breath. **A number printed beside a
   completed act does not stop it.** Fixed @`c1997ce5be`; the detector now runs in its own call.
2. **`resolve_lane` returned a clean `None` for EVERY path** across two successive calls, including
   `portal/DESIGN.md` -- which this seat's own round-37 record resolves to `POD_DE_ANY` -- and its own ledger
   path. Nothing in the output said "wrong call". **The positive control on a known-governed path is the only
   thing that distinguished a broken invocation from "no lane owns this".** `resolve_lane` takes the `paths`
   SUB-DICT; the whole config parses fine and resolves nothing.
3. **A backtick inside a double-quoted bash string became command substitution and silently deleted the word
   it wrapped** while writing the tick record. Second shell-quoting corruption of the block, after an
   `awk '$1=="D"'` that printed `0` from a parse error. **Both produced plausible output rather than an
   error**; both were repaired with a heredoc.

## What this prevented

`ADJUDICATION_v49` states `Z-S268`'s fix "is the CTO's". True of the DISARM and the SPEC, **false of the write
surface**: `resolve_lane` over 368 rules puts `exportCompare.harness.cjs` in **`POD_DE_ANY`**. Round 40's
`FWD-30` cell therefore carries a named pod-DE writer, exactly as `rn-3` did for `DESIGN.md`. Relayed BEFORE
the cut (msg 25740), not discovered after.

## Scope state, denominators printed

| project | status | dep_stage | orders | non-terminal |
|---|---|---|---|---|
| `AMGT_RESAPP` | active | EXECUTING | 214 | **0** -- round 39 fully drained, awaiting round 40's cut |
| `AMGT_CORPUS` | active | EXECUTING | 22 | **2** -- round 3 draining 5 -> 3 -> 2; `e-2`, the WORLD-class Bloomberg pull, is COMPLETE |
| `AMGT_HARVST` | active | ROUND_CLOSE | 18 | 0 -- round 6 ruled PARTIAL-shaped, queued behind `~Y` at the 3-COO cap |

Inbox 0 at tick 65. Tree clean, no merge, 6 ahead of `origin/CLOUD`.

## COMPLETION TEST

**NOT DONE -- 0 of 3 projects `status: complete`.** Round 39 is not a zero-graduation round: s.7 carries eight
items, one of them a retracted outcome.

## Cards at Andrew

**TWO.** (1) `org/XXX.md`'s stale double-stop, clarification delivered, awaiting his order since the file is
locked; item 4 of that card was overstated against a locally-reverted copy. (2) **The backfill's COMPLETE
state needs ft and barrons**, whose refusals authorization cannot reach -- a 403 and a post-auth rejection --
where his grant moved one of three publishers. **Plus the standing one:** item 7's authenticated deployed
render, unobtained for a third round, needs him present for the MFA sign-in.

## Compiler Tools

`resolve_lane` over `.owned-paths.yaml` (368 rules) WITH positive controls -- `comp-find --name --limit` --
`python` readers over task-order LAST `<status>` tags -- the non-ASCII character counter run in its own call --
heredoc `python -` for any body carrying shell metacharacters -- `safe-commit.sh -F` with a non-shell-authored
message file.
