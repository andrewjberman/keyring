# ANDREW-DIRECT 2026-09-11 ~22:25Z -- resume after the reboot: drive both IRPT lanes

**Received at:** the 1.0.0_SA_CTO terminal, in-session, 2026-09-11 ~22:25Z (this seat's launch turn).
**Channel:** Andrew directly, typed into this session.
**Recorded by:** 1.0.0_SA_CTO. **Broadcast:** same turn, per `org/XXX.md`.

## VERBATIM AND ENTIRE

> "load up and get /canonical-flow driving for COO~B (IRPT_BCKEND) and COO~F (IRPT_FNTEND)."

Preceded in the same session by the launch line, quoted for completeness:

> "1.0.0_SA_CTO
>
> FIRST: run /watcher to self-heal inbox-watcher + broker registration. THEN: org/XXX.md startup protocol."

## SCOPE IS NOT ADJUDICATED HERE -- what is surfaced, not decided

1. **The managed wind-down of ~17:1xZ is over as a POSTURE for these two lanes.** MSTR 95993/95994
   carried Andrew's "let workers finish, START NOTHING NEW, /log + commit, reboot follows". The reboot
   has landed (this device is back up; 2.0.0_SA_COO~B, 2.0.0_SA_COO~F, 0.0.0_AB_MSTR and this seat are
   all at session start). His sentence above is a live instruction to START, and it names the two lanes.
   **What it does NOT say** is that any other hold is lifted. This seat does not widen it.
2. **PORTAL STAYS FROZEN.** Andrew-direct, still standing and NOT touched by the sentence above:
   *"nobody does any portal promotes until i say so is the takeaway here."* IRPT_FNTEND works IN the
   portal repo and commits to local DEV; it does not push DEV and does not bump the workspace gitlink.
3. **The push cadence on CLOUD is unchanged** -- 0.0.0_AB_MSTR on Andrew's word (LD-0522). Both lanes
   commit LOCAL.
4. **"/canonical-flow driving"** is read as: each lane runs `/canonical-flow <CODE>` to measure its limb
   from artifacts rather than from its own recollection after a session turnover, and then proceeds
   through the normal L6/L7 gates. It is NOT read as authorization to re-cut a decomposition or to
   re-open a PRD mid-round; both rounds are FROZEN mid-round per Rule 27.

## STATE AT THE MOMENT OF THE DIRECT (measured, not recalled)

- Workspace `CLOUD` HEAD `aaaba07abc` local; `origin/CLOUD` `aa484f6b62` (`git ls-remote`, 22:32Z) --
  the tree is AHEAD of origin and single-copy until Andrew calls a push.
- **IRPT_BCKEND** (2.0.0_SA_COO~B): round 2 EXECUTING. Complete and merged: IB-rt-1, rt-3, rt-4, rt-5,
  rt-7, rt-8. Open: IB-rt-2 (~2), IB-rt-9 (~3), IB-rt-10 (~4, pending and unhanded), IB-rt-6 (~2,
  staged), IB-rt-11 (~3, staged), IB-rtb-1 (~1, staged). All worker subagents died with the reboot;
  their BRANCH state survives on disk. Handoff:
  `org/tier1_exec/2.0.0_SA_COO~B/logs/2026-09-11/session_close_1210-1835Z.md`.
- **IRPT_FNTEND** (2.0.0_SA_COO~F): round 2 EXECUTING. Complete and drained: FE-s-12, s-13, s-14, s-17.
  Not seated: FE-s-15, FE-s-16, FE-s-18 (all read `<status>blocked` = NOT SEATED, not a hard blocker).
  Named next act in its own handoff: seat FE-s-15 (slot ~1, port 5181) and FE-s-16 (slot ~3, port 5183)
  in parallel from HEAD / portal DEV `84a86c10`, FE-s-18 last; FE-s-15's face carries the v1 re-pin
  (`@d9c940244a` or later) that the six red consumer tests turn on. Handoff:
  `org/tier1_exec/2.0.0_SA_COO~F/logs/2026-09-11/session_cooF_1735Z_MANAGED_WINDDOWN_successor_handoff.md`.

## STILL OWED TO ANDREW AND NOT ANSWERED BY THIS DIRECT

**W4-S20 (IRPT_BCKEND, carried by 2.0.0_SA_COO~B via msg 96005):** `opal-data-ycharts` has versioning
ENABLED, so the four synthetic-export deletes wrote DELETE MARKERS. Every ordinary read and every
production reader now finds nothing, but the four noncurrent versions remain retrievable by `VersionId`
to a principal with `s3:GetObjectVersion`. The per-version delete is UNRECOVERABLE and was not taken on
a one-line "yes on synthetic exports". **The question, exactly: do the four noncurrent versions go too?**
Until answered, any statement that the four PDFs are "gone" carries that qualifier.

## THIS SEAT'S ACT ON THE DIRECT, SAME TURN

Directive sent to 2.0.0_SA_COO~B and 2.0.0_SA_COO~F (their own lane inboxes), each carrying the verbatim
sentence, the three non-lifted holds above, and the lane's own measured next act. Broadcast to
0.0.0_AB_MSTR. 2.0.0_SA_COO (base) is NOT live at this instant, so nothing was addressed to it -- a base
serial with no base session is a silent hole.
