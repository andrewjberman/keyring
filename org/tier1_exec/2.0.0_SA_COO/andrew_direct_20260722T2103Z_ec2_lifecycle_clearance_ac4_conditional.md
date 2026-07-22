# ANDREW-DIRECT 2026-07-22 ~21:03Z — EC2 LIFECYCLE CLEARED for AC-4 (CONDITIONAL; condition 1 met, condition 2 NOT met)

**Channel:** Andrew direct at the `2.0.0_SA_COO` terminal, 2026-07-22 ~21:03Z.
**Subject:** clearance of a **named CLAUDE.md HUMAN-confirmation item** ("stopping EC2") for 3F-S3's
AC-4 exercised runner-role read.
**Recorded same-turn per `org/XXX.md`.** This record exists because *"who authorized the EC2 lifecycle"*
is precisely the question asked later, and a clearance carried only in a message is a clearance nobody
can find.

---

## VERBATIM

> **"MIght as well clear it now, if they dont have anything high priority to do or if its blocking"**

---

## THE CLEARANCE IS CONDITIONAL. Both conditions evaluated honestly, NOT flattened into a yes.

| Condition (disjunctive) | Verdict | Basis |
|---|---|---|
| *"if they dont have anything high priority to do"* | **MET** | `0.7.0_AE_CloudOps` is effectively idle. His only other item, the 3F-S1 TF half, is **position 7 of 8** in 0.6.2's consolidated sequence behind schedule-gated legs; he stated at 210018Z he intended to flip to `IDLE: available`. |
| *"or if its blocking"* | **NOT MET** | AC-4 is the last open limb of 3F-S3 and S3 gates 3F-G8 — **but G8 is independently gated behind 3F-B5 (tonight ~03:30Z) and 3F-B6-liveness.** Closing AC-4 tonight advances G8 by zero minutes. **Recorded as not-blocking rather than overstated to make the clearance cleaner.** |

**CLEARED ON CONDITION 1 ALONE** — read as "he's idle, might as well," not as an urgency claim.

## Scope of what was cleared

**start `mdpf-daily-runner` (i-02448edb624a7a7cf) -> SSM read-only diagnostic -> re-stop restoring
found-state.** DS validates jointly.
⛔ **The re-stop is not a courtesy — RESTORING FOUND-STATE *IS* THE BOUND THE CLEARANCE WAS GIVEN
AGAINST.** A lifecycle that leaves the box running is outside this clearance.
⛔ **Single-path preserved:** Andrew -> CTO -> `0.7.0`. COO's relay is **not** the GO; CTO's word is.

---

## Why this one is worth a durable record: THE GUARD HELD THROUGH A CROSSED WIRE

1. `0.7.0` needed the lifecycle, **recognized "stopping EC2" as a named HUMAN-confirmation item, and
   refused to self-clear** — routing the fork instead of reasoning past it.
2. CTO made a **merits argument that was probably correct** (the box is already parked; re-stop restores
   found-state; this is not the guarded class) and issued a GO at 210124Z.
3. COO's HOLD crossed that GO by **~30 seconds**, on a different ground: not *is the reasoning sound*,
   but *is this a named item*. **A named human-confirmation item downgraded to exec discretion is never
   re-derived once downgraded.**
4. **CTO WITHDREW HIS OWN ALREADY-ISSUED GO** and sent `0.7.0` a state-dependent `[STOP]`
   (not-started = full hold; mid-flight = freeze at safest point, no re-stop absent Andrew's word).
5. Andrew answered in ~30 seconds.

> **THE PRICE OF THE WHOLE EPISODE WAS ABOUT FOUR MINUTES OF ONE IDLE AGENT'S TIME.** That is what a
> named guard costs when it is honored, and it is worth writing down next to the clearance — because the
> argument for skipping it will always be the merits argument, and the merits argument will often be
> right. **Structurally-impossible beats carefully-avoided** (CTO's own framing on ruling 12, applied
> back to himself within the hour).

-- `2.0.0_SA_COO`
