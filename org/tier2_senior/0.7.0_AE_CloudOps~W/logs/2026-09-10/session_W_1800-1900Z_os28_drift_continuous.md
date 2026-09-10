# 0.7.0_AE_CloudOps~W -- 2026-09-10 18:00-19:00Z -- NFRA_OUTSET `TO-OS-s-28`

**archetype:** BUILD + DEPLOY

## What this session was handed

A lane that **did not exist** an hour earlier. `2.0.0_SA_COO` spawned this seat at ~17:5xZ because
its 16:17:05Z GO on `TO-OS-s-28` had sat undrained in an unregistered lane inbox for ~1h40m (its own
row `NFRA_OUTSET-S45`). The GO was re-issued at 18:03:13Z with an explicit instruction: **read the
face at HEAD, not the copy quoted in the original GO**, because a CTO L4 ruling had landed inside
that window and withdrawn two of the three shapes the face offered.

## Outcome

**`TO-OS-s-28` TERMINAL. `O28-AC1` 6 arms / 6 HOLD / 0 FAIL, token printed, rc=0. `O28-AC2`
recorded for L9, not self-graded.**

The drift measure now publishes on a **recurring quarter-hour cadence with no human act**, proven by
two automatic publishes neither of which this seat started.

## The act

| | |
|---|---|
| before | daily calendar trigger @ 11:30Z, **no repetition**, Interactive principal |
| after | same trigger **+ `PT15M` indefinite repetition**, `--trigger scheduled` on the action |
| **not** changed | the principal -- **out of reach, see below** |

Re-registered from the task's **own exported XML** rather than via `Set-ScheduledTask`, because row
`NFRA_OUTSET-S39` measured that cmdlet silently reverting both battery flags on a laptop. A total
replace from a diffable source is auditable; a partial write is not.

## What I could not do, and did not route around

**The interactive-only principal.** Measured with a positive control on a *fresh* task, so the
denial cannot be "the existing task is locked":

| principal form | result |
|---|---|
| `Interactive` (**control**) | registers **OK** |
| `S4U` (both UserId forms) | `Access is denied` |
| `GroupId` | `Access is denied` |

The denial is specific to every "runs while logged off" principal. **One elevated line, stated
verbatim with its one-line rollback, is with Andrew.** I did not pick a weaker shape to make the
arms read better -- notably I refused a logon trigger, which would have closed the coverage gap
cheaply while making the cadence depend on a human habit the order kills by name.

## The bound I held

⛔ **No hand publish.** The artifact sat **18.3 h stale** and I let it. That staleness is precisely
what arm (a) rests on, and publishing by hand to keep the estate report green would have destroyed
the evidence while committing the act Andrew forbade.

## Compiler Tools

- **`comp-schedule`** -- DECLARED-NOT-APPLICABLE at the cut, and the face's own qualifier is the
  operative one: this cell's subject *is* a schedule, so a census at the cut describes the state the
  cell exists to change. The live reads went to the scheduled-task plane directly
  (`Get-ScheduledTask` / `Get-ScheduledTaskInfo` / `Export-ScheduledTask`), which is where a Windows
  task actually lives; comp-schedule does not model that plane.
- **`comp-iam`** -- DECLARED-NOT-APPLICABLE, not overridden. Nothing granted, nothing applied; arm
  (e) proves the role ARN, session name and key are byte-identical in source. The principal change
  identified here is a **Windows logon type**, not an IAM grant.
- **`comp-adversary`** -- DECLARED-NOT-APPLICABLE; arm (d) is the adversarial instrument, and it
  built its domain **by subtraction from a printed denominator of 18 live gating fields** rather
  than by recall.

## Surprise row filed

**`NFRA_OUTSET-S46`** -- `.tools/aws` is a bash script, so a Windows Python parent cannot exec it:
`OSError WinError 193`, which is **neither an aws error nor an empty result**. It killed exactly the
three battery arms that call the shim while the three that never touch it held.

⭐ **The diagnostic shape is the part worth keeping.** Three arms failed and three held, and the
split was not random -- a per-arm `try/except` had converted **one shared-dependency defect into
three independent-looking failures**. Reading what the *failing* arms had in common, instead of
debugging the first one, located it in a single step. That is Rule 22's shared-dependency blindness
seen from the other side.

## Carried forward

1. **Andrew's elevated line** -- until it runs, this device publishes nothing while nobody is logged
   on, and the report **should** say the device is silent.
2. `NFRA_OUTSET-S39` stays **ARMED**. This cell added the positive control it could not run but did
   not disarm it; the disarm is the line being run **plus a fire observed under the new principal**,
   since an S4U token carries no network credentials and that is untested on this box.
3. `TO-OS-s-22` and `TO-OS-s-23` remain untouched, waiting on their scheduled fire, not on this seat.
