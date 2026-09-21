# /self-drive LGIC -- tick 165 (2026-09-20 ~23:0xZ-23:2xZ) -- A ROW THAT PREDICTED ITS OWN LEAK FOUR DAYS EARLY, AND ONE I DELIBERATELY DID NOT CLOSE

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260916_052xZ_LGIC_GOAL_AND_30M_SELF_DRIVE_ADJUDICATE.md`
**Scope:** `LGIC_NAMING, LGIC_ENFORCE, LGIC_CANON, LGIC_LGCTFM`. **Device:** laptop. **state: ARMED**

## ⭐ 1. `LGIC_CANON-S6` RULED AND DISARMED @`be57f7a17f`

### ⛔ A premise in the row was stale, and it changed the question
`S6`: *"NOTHING IS MID-FLIGHT: **CN-j-6 is HELD and unspawned**."* True on 09-16. **At HEAD the order reads
`status: complete`**, `issued_to 0.9.0_WK_LGIC_CANON~6`, proof-of-spec on disk. **THE CELL RAN.**

I came to rule on a **cut** and found a **completed experiment**. Caught only by checking the order's status
instead of trusting the row's sentence about it -- `LGIC_NAMING-S21`'s class, three hours old: **an armed row
is evidence about when someone last looked.**

### ⭐⭐ `2.0.0_SA_COO~G` called it exactly, four days early
Pre-spawn: *"`j6-noseverity` greps CN-j-6's **ORDER FILE** ... the check never looks at the canon, so it
certifies the arm intact while the arm is compromised."*

**At HEAD, `J6-AC3`:** criterion *"this order itself did not carry the severity order -- **the arm is
intact**"*; evidence *"the order names the phrase SEVERITY ORDER: False ... **PASS-J6-SEVERITY-WITHHELD**"*;
and in its own words *"**this criterion grades the task-order file itself, not this worker's artifact**."*
And `infra/logic/02_DOCTRINE.md` -- judge E's rule source, **no vintage pin** -- carries the scale at
**`:117-121`**, printed.

**The brief withheld it, the canon supplied it, and a criterion named *"the arm is intact"* returned PASS by
reading the brief.**

### ⭐ The consequence is bounded, and the bound is in the artifact
`declared_exclusions`, the worker's words: *"A severity ranking of the 7 planes or a single overall reading per
plane ... requires **RANKING axis verdicts against each other, which this cell does not do**."*

**Output = 7 rows × 5 axis verdicts with citations (`J6-AC1`/`AC2` PASS at 7 of 7), NOTHING RANKED.** The
worker met the scale and **did not use it**, because the order forbade the only operation that would have.
⭐⭐ **The contamination is REAL and the output is CLEAN, and those are not in tension: E's exposure was to the
ORDER; E produced only VOCABULARY.**

### RULED
**Reading TWO governs, on evidence** -- what was withheld is a BRIEF; the canon is where a judge finds the
scale. **With reading one's bound, now evidenced:** no reading of this round may be quoted as evidence the
severity **ORDER** is sufficient. **Hazard CONFIRMED, SPENT, cannot recur -> DISARMED** (clock is the CVO's).
**Remediation stays OPEN:** the round-3 per-plane **ROLL-UP** cell, not cut here.

### ⛔⛔ The keepable, still live in the fixed inputs
> **A CRITERION THAT GRADES THE BRIEF CANNOT CERTIFY THE ARM WHEN THE ARM'S INPUT IS A FILE THE BRIEF MERELY
> NAMES.** Withholding is a property of the **whole input closure** -- brief plus every document it points at
> -- so a check scoped to the brief returns PASS **at exactly the moment** the pointed-at document starts
> carrying the withheld thing. ⛔ **Its PASS is not weak evidence; it is evidence about a DIFFERENT OBJECT**,
> and its NAME converts that into a false assurance. **COST:** name the criterion for what it READS, or widen
> it to the closure. **NON-APPLICATION:** an arm whose inputs are all literal in the brief.

`check_canon_r2.py` is the issuer's fixed input; **I have not edited it** and do not widen the check.

## ⚠ 2. `LGIC_CANON-S22` READ AND **DELIBERATELY NOT CLOSED**

Its blocker is *"AT LEAST TWO; **DENOMINATOR UNMEASURED**"*, and the temptation was to call it discharged by
`S112`'s 462-over-3716.

**It is not, and the reason is a population difference I nearly papered over:** `S112` measured the **r8 census
corpus**; `S22` is about the **live census run** (2,231 live nodes / 1,852 to judge). And even within what I
did rule, **my own `S112`/`S113`/`S114` ruling covered ONE of EIGHT rule families and left 278 raises across
six families explicitly unowned.**

⭐ **So the honest answer is STAYS ARMED, and I am saying so rather than reaching for a disarm because it is
the last row on my list.** `MEMORY.md`: *when you hold a row's clock, the reading that CLOSES it is the one you
must not take yourself.* It gets a proper ruling next tick, with the two populations separated.

## STILL OWED -- one of `3.0.0_SA_CVO`'s six

`LGIC_CANON-S22` (and its answer is likely "armed, with the residual sized").

## Open calls at Andrew -- **2** · `MEMORY.md` 24.40 KB

## Compiler Tools

`git show HEAD:` on the order (status/`issued_to` -- the read that caught the stale premise) · `json.load` of
the proof instance with `acceptance`, `declared_exclusions`, `surprises` read in full · **bytes PRINTED at
`02_DOCTRINE.md:103-131`** with a `SEVERITY ORDER` census over all 668 lines (**2 hits: `:117`, `:666`**) ·
`git ls-files` for every `CN-j-6` artifact (**2**) · both `S6` and `S22` read in **investigation AND
remediation** carriers · 1 commit (`be57f7a17f`) · `send_message` x1 (3 delivered) · `Monitor` re-arm.

**PUSH STATE at write time:** `be57f7a17f` + this commit LOCAL; origin/CLOUD `146ad71831` (ls-remote read).
**state: ARMED**
