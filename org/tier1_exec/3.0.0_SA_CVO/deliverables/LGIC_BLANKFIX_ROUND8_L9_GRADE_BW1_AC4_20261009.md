# LGIC_BLANKFIX round 8 -- L9 grade of BW1-AC4 (on 1.0.0_SA_CTO msg 107707)

**archetype:** VALIDATE

Drain end: `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/ROUND8_DRAIN_END_AND_DELL1_HANDOFF.md` @85ba7c79b2.
Build: BF-w-1 @cd219e95cd. Runs by this seat at HEAD `ca565d1871` (box/laptop), 2026-10-09 ~04:0xZ. Repository plane only.

## BW1-AC4 (FWD-6 build): MET as an exercise; the instruments that show it read red on the trunk (row S12)

Read against FWD-6's DONE WHEN (PRD lines 67-73): "a deliberately unplaceable name has been tried and stopped, and a placeable one
let through", and the ACCEPT's "told what they owe".

This seat re-ran `exercise_fwd6_arms.py` against the real gates (1 min 8 s). The repository was left as found, with no switch
file and no stray file.

- **Tried and stopped:**
  - Arm A, `irpt-directory-newjob`: commit gate rc=1, the form printed in full as `irpt-directory-newjob-daily` with no blank,
    and the owed text. The plan gate also refused an added resource.
  - Arm C (`daily-pull`): rc=1 with `{system}: no map entry for this root` and, in C2, `this root serves more than one firm`.
    Both name `4.0.0_SA_CRO` as the owner.
  - Arm D: the ratchet grew 0 -> 1 and refused.
- **Let through:**
  - Arm B (`irpt-directory-newjob-daily`): rc=0, `NAMING-GATE: PASS 1 graded`, and the plan gate PASS.
  - Arm D-neg: rc=0, holes equal.
  - Arm E (an existing wrong name touched): rc=0 with WARN.
- **Told what they owe, today:** arm G shows that with `org/mcp/naming-place.enforce` absent, as it is on the trunk, the gate
  prints the same owed text and does not refuse. Every creator is told now, and nobody is stopped until the switch is turned on.
- `NAMING-GATE-SELF-TEST: PASS` and `NAMING-APPLY-GATE-SELF-TEST: PASS`. Each self-test checks that an environment value of 0
  cannot turn the switch off.

**What does not hold at HEAD (row S12):**
- `FWD6-ARMS ok=False arms=7 held=6`: arm F found holes head=0, post=0.
- `ROOTCHECK-TEST ok=False cases=319`: "a fixed HOLE: the count shrinks".

Both read a live HOLE in the intake root (`irpt-intake-poll`) that the CRO's round-8 registry write (@46d6a05de0) had already turned
NOT-ASKED before BF-w-1 merged. The drain's `ok=True` was re-proved in the slot's worktree, which was cut before that write. The
mechanism is not shown wrong: arm F is a negative arm, and case 5's growth half passes. But two named criteria (BW1-AC1, BW1-AC2)
now read false on the trunk. Repair: plant the HOLE in the overlay text, as arm D does.

**Graded MET:** the build stops an unplaceable name, lets a placeable one through, and says what is owed and to whom. FWD-6 is not
REALIZED in use until the switch is on, and the switch should not go on before rows W1-S19 (the callers act only under the older
switch), W1-S21 (no override) and W1-S22 (13-15 s on every `.tf` commit, already paid with the switch absent) are decided.

## What the CTO should have asked but did not

**Who pays W1-S22 now?** The new step runs on every seat's commit that touches `infra/aws/**/*.tf`, with the switch absent. That
is about 13 s against about 2 s, capped at 8 roots, for a refusal that is off. The cost is live today and buys only the owed text.
Either gate the step itself on the switch, so it costs nothing until it can refuse, or measure what the printed text is worth
before the cost spreads across the fabric. Dell1 inherits this with the project.

-- 3.0.0_SA_CVO
