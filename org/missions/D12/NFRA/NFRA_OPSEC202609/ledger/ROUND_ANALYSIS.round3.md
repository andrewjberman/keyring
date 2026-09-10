# NFRA_OPSEC202609 -- ROUND 3 ANALYSIS + CLOSE GRADING (L10 answered)

**archetype:** SCRIBE (ledger) · **written by** `1.0.0_SA_CTO~Z` · **2026-09-10 ~21:3xZ**

| | |
|---|---|
| **Answers** | `[L10 SLUG] NFRA_OPSEC202609 round 3` @`b47b1b8697` from `3.0.0_SA_CVO~Z` (msg 21065) |
| **On Andrew's word** | *"tell CTO~Z to grade it and close it out"* -- 2026-09-10T21:23Z at the `2.0.0_SA_COO~Z` terminal, record @`9e1d2f700f` |
| **Grades** | `ledger/COMPLETION_GRADES.round3.json` -- the project's FIRST grades artifact |
| **Routes to** | `2.0.0_SA_COO~Z` (nothing to recut) · `0.0.0_AB_MSTR~Z` (the register) |

---

## 1. THE VERDICT: 16 of 19 REALIZED. THE PROJECT IS GRADED AND SETTLED, NOT FLAG-CLOSED.

35 of 35 orders terminal, 190 investigation items with 0 undispositioned, the CVO's L10 precondition
met on both limbs. This is a finished body of work. **Sixteen outcomes are REALIZED. Three are
NOT_REALIZED, and all three share one shape** -- see s.2.

⛔ **`dep_stage` STAYS `EXECUTING`, DELIBERATELY, AND THAT IS THE HONEST STATE.** The register's R6
gate refuses `CLOSED` while any grade is short of REALIZED, and it is right to. **"Close it out" is
satisfied by producing the grades and settling the outcomes -- not by forcing a flag the world has
not earned.** The three residues are live events, and the flag flips itself when they occur.

⚠ **GRADED AGAINST EACH CARD'S `DONE WHEN` STATE LINE, NOT THE COMPLETION REPORT'S COVERED CLAIM.**
The report marks all 19 COVERED and is correct -- a cell serves each outcome. But COVERED is not
met, and reading the bars directly caught three EXERCISED bars the coverage claim could not see.

---

## 2. THE THREE RESIDUES ARE ONE FINDING: A NOTIFICATION NO ARTIFACT CAN WITNESS

Screening all 19 bars, exactly three carry a limb outside the artifact plane -- a message delivered
to a human, or a measurement that needs elapsed time. **In every one the mechanism is built and
APPLIED; only the live event is missing.**

| outcome | bar | what is built | what the bar's last limb needs |
|---|---|---|---|
| `FWD-4` | EXERCISED | alarm + topic + **subscription now CONFIRMED** | a burst to fire a notification **that Andrew reads** -- and the staged burst (S6-AC2) fired when there were **0 subscriptions** (S6-AC3), so nothing was delivered |
| `FWD-15` | EXERCISED | the block mechanism, the one-email dedup path | an **automatic** block to fire **one email Andrew receives** -- the sentinel is WATCH-ONLY by design (`block_armed false`) |
| `FWD-19` | EXERCISED | the spam control, demonstrably flagging scripted submissions | the **volume delta** -- the after-window was ~32 min against a 0.217/day baseline (~1,660x too short), so "by how much it changed" is uncomputable until it fills |

⭐ **NONE OF THE THREE IS MISSING WORK. EACH IS WAITING ON TIME OR A LIVE EVENT.** FWD-4 and FWD-15
became reachable only this session (the subscription confirmed; the sentinel can now be armed).
FWD-19's control exists and works. **A round-4 that "built" anything here would re-buy working code**
-- what these need is a burst, an armed block, and a few days, in that order.

⛔ **AND THIS IS WHY GRADING BEFORE THE EVENTS WOULD HAVE BEEN A LIE.** The completion report's
COVERED is honest; a REALIZED on FWD-4 today would have cited an alarm that has never notified a
subscriber. The gap is in the world, not the build, and the grade says so.

---

## 3. FWD-19's GRAIN WAS ALREADY RULED, AND HALF THE BAR IS EXERCISED

`@c0003e75cf` ruled that "refused" is graded at the entry store, not the wire -- the scripted
submission WAS flagged spam with zero notifications while a real visitor's submission landed
unaltered. **That half is met.** What is not met is the *before/after volume* limb, which is the
temporal residue above. The grain ruling stands; the outcome is NOT_REALIZED only on the window.

---

## 4. WHAT IS OWED, BY WHOM

| owner | act |
|---|---|
| `2.0.0_SA_COO~Z` | **nothing to recut.** The three residues are not decomposition gaps; no round-4 cell would advance them. If Andrew wants the events forced (stage a burst, arm the sentinel), that is a small ops issuance, not a round. |
| `1.0.0_SA_CTO~Z` | ✅ grades written. **When the three live events occur, re-grade those rows to REALIZED and the register flips to CLOSED** -- no new round, just the second read against the same bars. |
| `0.0.0_AB_MSTR~Z` | the register stays `EXECUTING`; **do not force `CLOSED`.** R6 would refuse it and be right. |
| Andrew | **nothing owed.** He asked to close it out; it is graded and settled. The flag is not a decision he needs to make -- it is a fact three events have not yet produced. |

⚠ **THREE ITEMS STILL NAME THIS SEAT** (carried, not gated by the close): `Z-S170` (the to-pipeline
tag-grain defect -- same family as today's `TO_STATUS_RE` fix), `Z-S172` (FWD-19's grain, now ruled),
and `Z-S171` (the phantom Rule-27 citation). `Z-S172` is discharged; the other two are owned items on
no critical path.

**Push state:** LOCAL at write time; ancestry rather than a tip hash. `0.0.0_AB_MSTR~Z` pushes.
