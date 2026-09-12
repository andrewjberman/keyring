# /self-drive AMGT_RESAPP & POSN_ASTTAX -- ticks 28-30

**seat:** `1.0.0_SA_CTO~Z` · **state:** ARMED · **device:** sitez · **2026-09-12T00:41Z**
Tick 27's log is `@ecc79fd`. Nine commits since. **The L10 read landed and round 7 is cut.**

---

## 1. THE ACT THE WHOLE LOOP WAS WAITING ON: the L10 read, delivered

`3.0.0_SA_CVO~Z` routed rounds 5 AND 6 in one commit (`bd523222a1`). The analysis
`@ac9b2e7e46` answers both; `ROUND_ANALYSIS.round6.md` is a pointer so nobody searching `round6`
finds a gap. **`2.0.0_SA_COO~ZZZ` cut round 7 off it at `c9b1fc5ed0` -- six cells.**

⭐ **AND THE REFUSAL TEN MINUTES EARLIER WAS VINDICATED BY MEASUREMENT, NOT BY LUCK.** At 23:55Z this
seat declined to grade `REMEDIATION_v6` because it was uncommitted. **The uncommitted file carried 9
rows; the committed one carries 10.** The bytes moved between the read and the route -- which is
`2.0.0_SA_COO~Z`'s rule (*an uncommitted file in a shared tree is not in hand*) proved on this seat's
own hesitation, three hours after this seat endorsed it about its OWN analysis.
⛔ **THE INSTRUMENT USED FOR THAT REFUSAL WAS STILL WRONG.** `git ls-files --error-unmatch` reads the
INDEX and cannot tell COMMITTED from STAGED; it would have flipped to TRACKED the moment the CVO
staged, minutes before anything routed. Right answer, wrong instrument, and the defect was already
banked in this seat's own memory by name. The right one is `git log -- <path>` with a positive
control.

## 2. THE FINDING IN THE ANALYSIS IS MINE

⛔ **THE MUTANT CONTROL I REQUIRED DESTROYED ~90 UNCOMMITTED LINES OF A WORKER'S WORK** (`Z-W10-S1`).
When I ruled `rd-8` SUPERSEDED I demanded an injected-error control and **never specified its restore
source**; the implementation restores from the INDEX, not the pre-test working bytes.
**A MUTATION CONTROL MUST SNAPSHOT THE WORKING TREE, NEVER THE INDEX** -- the index is the one copy
guaranteed not to hold a worker's in-flight edits. The control stays; `rd-8` shipped precisely
because its checks could not fail.

## 3. FOUR CORRECTIONS AGAINST THIS SEAT IN ONE HOUR, EACH CAUGHT BY A DIFFERENT SEAT

| # | what | caught by |
|---|---|---|
| 1 | **A PHANTOM GATE** -- my analysis said the recut waits on a CVO disposition pass. It does not: 65 of 65 items already dispositioned, 0 undispositioned (positive control POSN 24). | `3.0.0_SA_CVO~Z` |
| 2 | **AN UNMEASURED CONSEQUENCE** -- "blanks the page for four partner firms". `C-S52`: *"establishes an unsafe generation precondition; does not demonstrate live page blanking."* | `3.0.0_SA_CVO~Z` via `2.0.0_SA_COO~Z` |
| 3 | **THE REBINDING SUBJECT** -- body clean with `FOR <serial>` headers, subject read "Recut is yours". | `2.0.0_SA_COO~Z` |
| 4 | **A SELF-CONTRADICTING SPEC** -- I added the reversal as a new paragraph and left the one below saying the same mechanism was "NO LONGER OPERATIVE". | this seat, prompted by `4.0.0_SA_CRO~Z` |

⛔ **A PHANTOM GATE COSTS WHAT A BROKEN ONE COSTS**: a seat waits on a condition nobody will satisfy
and nothing announces it. Third instance tonight, after the unsent L4 notifier and the false LIMB 6
fence -- and this one I invented.
⛔ **AND #3 RECURRED 35 MINUTES AFTER ITS OWN CORRECTION, BECAUSE THE BANKED REMEDY SAID "IN THE
BODY".** I followed the rule correctly and shipped the defect one field over. **A REMEDY SCOPED TO
WHERE YOU LAST GOT CAUGHT LETS THE SAME DEFECT THROUGH ONE FIELD OVER** -- the same shape as #4, and
as my step-(2) bar being narrower than the hazard. Memory widened past the body.

## 4. THE ESTATE-LEVEL FINDING, and it is not mine

⭐ **`0.0.0_AB_MSTR~Z`'s line, which five seats then proved on themselves: CARE SPENT ON THE PREMISE
DOES NOT TRANSFER TO THE CONCLUSION DRAWN FROM IT, AND IT FEELS LIKE IT DOES.** The deploy gap was
verified on FOUR instruments -- worker, control plane, CVO reproduction, vintage comparison -- and
**not one seat asked what measured the page blanking. The answer was none.** The rigour on the first
half is exactly what made the second half feel carried.
It reached Andrew by **two independent paths** (MSTR's relay and this seat's `/open-calls` card),
which read as **corroboration rather than repetition** -- this estate's "a second seat's confirmation
via the first seat's method is REPETITION" arriving as a CONSENSUS, which is harder to see because
nothing looks repeated.
⭐ **AND `4.0.0_SA_CRO~Z` ENDED IT CORRECTLY:** *"the count has been corrected four times in twelve
minutes and the defect has been fixed zero times."* A hop count is a RECORD and does not decay; a
live spec line is a HAZARD. Line 16 was fixed in the next act rather than argued about.

## 5. SCOPE STATE / COMPLETION

```
OPEN CALLS IN SCOPE: 0 adjudicable · 3 RESERVED at Andrew · 1 CARRIED
  BLOCKING  deploy the 2026-08-18 generator (NEVER#1 class, four instruments)
  BLOCKING  POSN round 3 close with s-6/s-7 carried forward (LD-0521, his round-2 shape)
  BLOCKING  portal freeze scope -- EDIT vs PUSH/PROMOTE
  CARRIED   LIMB 6 widening; proxy vendor
COMPLETION TEST: NOT DONE -- 0 of 2 complete (denominator: 2 in scope)
  AMGT_RESAPP  active/EXECUTING  REACHABLE  ADMITTED; ROUND 7 CUT @c9b1fc5ed0, six cells
  POSN_ASTTAX  active/EXECUTING  REACHABLE  WITHHELD, brief owed (the 10th, one word)
  UNREACHABLE: 0     HELD-AT-STOP: not reached
```
⚠ **POSN's tenth re-sign is a WORD CHANGE and is worth it**: "blanks the page" reads as a live outage
and invites an emergency deploy; "an unsafe generation precondition" reads as a reason not to retag
until a deploy lands, on a deliberate schedule. Both fixes fold into the SAME outstanding signature,
so the cost stays at one review.

**Push state:** LOCAL. `0.0.0_AB_MSTR~Z` pushes origin/SITEZ.

## Compiler Tools

`prd-signoff.py status` · `_latest_dispositions` + `_open_tos_for_project` with positive controls ·
`git log -- <path>` (the routing instrument) · per-block JSON validation at the pin · `safe-commit` ·
native Grep.
