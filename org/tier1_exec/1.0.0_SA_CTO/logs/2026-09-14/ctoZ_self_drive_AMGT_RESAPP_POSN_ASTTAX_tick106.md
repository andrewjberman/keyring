# /self-drive AMGT_RESAPP & POSN_ASTTAX -- tick 106 -- STEP 0.7 RUNS FOR THE FIRST TIME, AND THE TEST THAT ENDS THIS LOOP IS MEASURED UNRELIABLE

**seat:** `1.0.0_SA_CTO~Z` · **state:** ARMED · **device:** sitez · **2026-09-14T08:5xZ**
Tick 105's log is `@920c6c357f`. Delta-driven; the floor would not fall until tick 111.

> **The merge brought this skill a new Step 0.7 and it binds from this tick. Running it surfaced that
> the relayed workaround does not cover this scope -- and a routine reconciliation two steps later
> found that `/self-drive`'s own completion test rests on a field that is measurably wrong on a
> sibling project in the same directive.**

---

## 1. STEP 0.7 -- THE SEQUENCE, FIRST LIVE RUN

Andrew-direct ~01:xxZ ties this loop to `org/missions/SEQUENCE.yaml` every tick, device-agnostic. The
document and its reader arrived on the CLOUD->SITEZ leg; **this is the first tick that could run it.**

```
sequence-check | SEQUENCE.yaml | file last commit d65f700ae0 | enforcement: TRACK | stage enum: OK
  --project AMGT_RESAPP ... projects: 0    FLAGS (denominator 0 projects): none    rc=0
  --project POSN_ASTTAX ... projects: 0    FLAGS (denominator 0 projects): none    rc=0
```

### ⛔ The relayed workaround does not discriminate for THIS scope

`22561` carries the laptop CTO's fix (taken as proposed, 17/17 self-test, `c90fb962c6`) **and the
operational half: the fix is LOCAL on the laptop, so site Z still passes a typo silently.** Its interim
guidance is *read the printed project ROW, not the exit code.* Measured here:

| code | `sequence-check` | register file |
|---|---|---|
| `LGIC_NAMING` (placed) | `projects=1` | PRESENT |
| `AMGT_RESAPP` | `projects=0` | PRESENT |
| `POSN_ASTTAX` | `projects=0` | PRESENT |
| `LGIC_NAMNIG` (typo) | `projects=0` | ABSENT |
| `ZZZZ_NOSUCH` | `projects=0` | ABSENT |

⛔ **The workaround separates PLACED from everything else. It does NOT separate UNPLACED from TYPO --
and BOTH scoped projects are UNPLACED**, so it cannot discriminate exactly the two cases in front of
this loop. **Interim discipline adopted, a READ and no tool edit** (the tool is another fabric's, minutes
old, and this session is scope-bound):
```
projects>0                                  -> PLACED
projects=0 AND org/projects/<CODE>.json      -> UNPLACED, drive normally, no sequence constraint
projects=0 AND no register file              -> UNKNOWN CODE, drive nothing
```
Exercised on five codes, positive and negative arms both firing.
⚠ **VINTAGE STATED AS UNVERIFIED, NOT ASSUMED:** the readable file here is **v1 `@d65f700ae0`**. v2
`@089ba2d431` (reported to add COO capacity) is local on the laptop. **Whether v2 places anything in
this scope cannot be read from this device**, and a relay summary is not a read. Neither project is
placed in the readable version; the sequence is TRACK, so the tick raises and refuses nothing.

## 2. ⭐ THE RECONCILIATION THAT FOUND SOMETHING -- `POSN_ASTTAX-Z-S56` @`59edbe21f9`, ARMED

The register reports D4 `open_tos=6`; POSN_ASTTAX has 4 non-terminal. **Rather than explain the gap,
every member was measured:**
```
ETFS_CANON 0 | ETFS_POSITIONING 2 | ETFS_INGEST 0 | ETFS_SATELLITES 0 | POSN_TENANCY 0 | POSN_ASTTAX 4
                                                                                          TOTAL 6
```
**The register's count is exactly right and reconciles.** The two numbers measure different sets and
were never in conflict -- **and the defect appeared only because the reconciliation was performed
instead of narrated, in the member nobody was looking at:**
```
org/projects/ETFS_POSITIONING.json .. status='complete'  AND  dep_stage='EXECUTING'   no completed_at
non-terminal orders ................. 2 -- TO-13-DS (0.4.0_DS_ClientPlatform~Y)
                                           TO-14-AE (0.7.0_AE_CloudOps~N), own status text:
                                           "AC1 + AC2 + AC3 PASS -- 3 of 4"
```
>> ⛔ **`/self-drive` STEP 4 ENDS THIS LOOP ON `status: complete`, READ FROM THE REGISTER. STEP 4 GUARDS
   AGAINST THE DRIVER DECLARING ITS OWN DONE -- NOT AGAINST THE FIELD BEING WRONG.** Reading rather
   than declaring removes the driver's INCENTIVE to be wrong; it does not make the field TRUE, and a
   single-field oracle has no discrimination by construction. On DONE this loop writes a final log,
   `CronDelete`s itself, **strikes the `org/XXX.md` carrier clause and stands down its paired `/drive`
   half.** The last two reach another seat and none of it is cheap to reverse. <<

**RULING, binding on this loop and nothing else.** When either scoped project's `status` first reads
`complete`, the loop does **not** terminate on that field alone: it corroborates `dep_stage` reads
`CLOSED` and the non-terminal order count is **ZERO with its denominator printed**, records all three
in the final log, and **stays ARMED** on any disagreement, raising it to `0.0.0_AB_MSTR~Z` as register
writer. No gate on any other seat; it constrains only this driver's own terminal act -- the one act
Step 4 leaves entirely to the driver's reading.
**NEGATIVE CONTROL** (so this is a defect, not the schema's normal state): AMGT_RESAPP reads
`active / ROUND_CLOSE / 0 of 47`, POSN_ASTTAX `active / EXECUTING / 4 of 19` -- both coherent.
⛔ **NO DISPOSITION ON `ETFS_POSITIONING`**: outside scope, neither order addressed to a serial this
seat holds, no register edit. Raised to the register writer and the two issuing lanes as an observation
with its measurement, no act requested.
**Filed now rather than at the flip** -- the tick where the oracle would end the loop is the tick with
the least appetite for a new question.

## 3. `Z-S82` RULED -- AND THE RULING DECLINES A LAW EDIT

`2.0.0_SA_COO~ZZZ` filed a THIRD instrument of one shape: plane (b) of the nudge rung reads
`org/tier1_exec/<BASE>/deliverables/` unscoped, returning **MOVING at 53 min** on an artifact authored
by the BASE serial about another project, while the queried lane's own newest is **COLD at 1658 min**.
**Sharper than `Z-S79`**: an inflated count gets argued with, but **MOVING is the branch that ENDS the
probe** -- the wrong reading is the one nobody follows up.
**NOT a duplicate**, confirmed: different directory, different instrument, different consumer.

⛔ **RULED: NO `CLAUDE.md` EDIT.** The filer says it itself -- Rule 22 already names the class (*a check
scoped to the members cannot see a defect in what the members share*). **A law line restating a rule the
file already carries is the ratchet the change-policy forbids**, and this seat has edited that file
twice in the past hour, both to correct its own numbers.
⛔ **And the `ROSTER` clause deliberately does NOT widen to cover it.** ROSTER names ONE TOOL. Annexing a
skill's filesystem probe to a clause about a broker call would make the clause false about its own
subject and unfindable from the surface that has the defect.
⭐ **The actionable defect is the RUNG'S WORDING.** `"<BASE serial>"` is exactly right at what it was
written for and reads as though the base home ANSWERS FOR the lane. Fix: scope plane (b) by AUTHOR, with
the base serial's newest as the positive control -- **which is the COO loop's rung, so this is a REC, not
an edit to another seat's skill.**
**Three instruments, one session, one shape -- a SHARED CONTAINER read as a PER-SERIAL fact:** the broker
task-order limb, the broker log limb, the probe's deliverables plane. Recorded without a law line.

## 4. STATE AND COMPLETION

```
SCOPE  D4 + D5 -> AMGT_RESAPP, POSN_ASTTAX   device SITEZ   (denominator: 2 of 15 live directives)
AMGT_RESAPP  ROUND_CLOSE  active  47 of 47 COMPLETE, 0 OPEN   round 9 at L9, bound adjudicator
POSN_ASTTAX  EXECUTING    active  15 COMPLETE / 4 ACTIVE of 19 round 4 at L9
             denominator 2618 tree+flat orders · ZZZZ_NOSUCH control = 0
next slug    REMEDIATION_v9 / _v4 / ROUND_ANALYSIS.round4 ABSENT; v8 / v3 controls PRESENT
portal       gitlink e85f6eb84f == submodule checkout -- freeze intact
SEQUENCE     both projects UNPLACED (register-corroborated); file v1 @d65f700ae0; v2 UNREADABLE here
OPEN CALLS   0 adjudicable · 2 RESERVED · NO PITCH  (all-reserved tell does not fire: 0 adjudicable)
COMPLETION   NOT DONE -- 0 of 2 (denominator: 2 projects, 2 of 15 live directives)
             REACHABLE 2 · UNREACHABLE 0 · HELD-AT-STOP NOT REACHED
```
⚠ **DENOMINATOR CORRECTION: live directives is 15, not the 14 this seat has printed in prior logs** --
it moved with the merge and was carried forward unre-read. Corrected here rather than quietly updated.

**Push state:** HEAD `59edbe21f9`, `origin/SITEZ 959e8aa375` (ls-remote) -- **LOCAL**, the integrator's
to carry. **No TO cut, no dispatch, no apply, no promote, no gitlink move.**

## Compiler Tools

`sequence-check --project` run on FIVE codes including a one-letter typo and an impossible code, with
the register file as the independent discriminator the local tool lacks · the D4 open-TO count
reconciled MEMBER BY MEMBER rather than explained, which is what found `Z-S56` · prior-round
`REMEDIATION`/`ROUND_ANALYSIS` files as PRESENT controls so an ABSENT verdict discriminates ·
`ZZZZ_NOSUCH` zero control on the order census · `to-check.py` on `status_class` (**there is no
`status` key**) · the POSN channel append targeting the FINAL close via `rfind` with an `endswith`
assert, because **that channel is 40 fenced blocks, not one**, plus post-edit asserts that the block
count held at 40, rows went 87 -> 88, and **no block but the last differs byte-for-byte** ·
`safe-commit.sh -F` with a message file written by a non-shell writer · `ls-remote` for push state.
