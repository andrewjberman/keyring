# ANDREW-DIRECT 2026-10-01 ~16:1xZ at the 1.0.0_SA_CTO terminal -- device too slow: every seat writes a reboot brief, the CTO writes the reboot doc, the seats are relaunched with their briefs

**Verbatim:** "Device is getting too slow, I need you to assess current state, what agents are on what projects and their state.
Every agent should write a brief on what theyre doing and where theyre at and report them to you, then you write a reboot doc
with who needs to be spawned and we launch them with their briefs."

**Follow-up words, same terminal, ~16:2xZ, verbatim:** "yes they can proceed to the next easy checkpoint" and "i do not want
them cut off mid-stream."

So no seat is stopped mid-act: each finishes the work in hand to its next easy checkpoint (a commit, a closed leg, a
completed read, a sent reply), then writes its brief. The brief is written at that checkpoint, not before it.

## What it orders

1. `1.0.0_SA_CTO` assesses the current state: which seat is on which project, and in what state.
2. EVERY live seat writes a reboot brief in the form of
   `org/tier1_exec/1.0.0_SA_CTO/deliverables/REBOOT_20261001/BRIEF_TEMPLATE.md`, in its own deliverables folder, commits it,
   and reports its path to `1.0.0_SA_CTO`.
3. `1.0.0_SA_CTO` writes the reboot doc, `org/tier1_exec/1.0.0_SA_CTO/deliverables/REBOOT_20261001/REBOOT_DOC.md`: who is
   respawned, on what, with which brief, in what order.
4. The seats are launched with their briefs after the reboot ("we launch them": the launch is Andrew's with this seat).

## What it does not change

- No open deploy is left half-landed (CLAUDE.md NEVER-2): a seat mid-act finishes it or rolls it back before it stops, and its
  brief names every ledger entry it holds open and why it is safe to hold over a reboot.
- No new vendor attempt, deploy or apply starts between the broadcast and the reboot.
- The ten acts listed for Andrew stand; nothing in this order answers any of them.
- The live seats at the order (process census 16:17Z, ten `claude.exe`): `0.0.0_AB_MSTR`, `1.0.0_SA_CTO`, `2.0.0_SA_COO~D`,
  `2.0.0_SA_COO~M`, `2.0.0_SA_COO~P`, `2.0.0_SA_COO~Y`, `3.0.0_SA_CVO`, `4.0.0_SA_CRO`, `4.0.0_SA_CRO~X`,
  `0.4.0_DS_ClientPlatform~S`.

Recorded by `1.0.0_SA_CTO`; broadcast the same turn to the nine other live seats.
