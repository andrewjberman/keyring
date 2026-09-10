# CHANGE: `OpalOutsetDriftLaptop` -> CONTINUOUS (15-minute repetition) + trigger disclosure

**archetype:** DEPLOY · **state:** CLOSED — LANDED AND VERIFIED (opened before the act, per NEVER-2)

| | |
|---|---|
| **Actor** | `0.7.0_AE_CloudOps~W` |
| **Opened** | 2026-09-10 ~18:20Z |
| **Order** | `NFRA_OUTSET.TO-OS-s-28` (re-cut @`32b730ae79`), criterion `O28-AC1` |
| **Authority** | Andrew-direct 2026-09-10 ~15:3xZ, VERBATIM: *"no this should be a continuously stitched function, maybe every 15 min."* and *"no hand-drawn anything, no manual trigger anything for something like this"* |
| **Resource** | Windows scheduled task `\OpalOutsetDriftLaptop` on THIS device (laptop) |
| **Also** | `infra/aws/ec2/outset-drift-device/publish_drift.py` (trigger-disclosure fields) |

## THE ACT — TWO PARTS, ONE OF WHICH I CANNOT PERFORM

### Part 1 — THE INTERVAL (mine, no elevation needed)

| | |
|---|---|
| before | `CalendarTrigger` daily @ `2026-09-09T07:30:00` local, **no repetition** |
| after | same daily trigger **plus** `Repetition` every **PT15M**, duration **indefinite** |
| action arg | `--trigger scheduled` appended, so the artifact discloses what started it |
| unchanged | principal · settings block · command · working dir · `--out-prefix` |

### Part 2 — THE PRINCIPAL (**NOT MINE — Andrew's one elevated line**)

The task's principal is `LogonType=InteractiveToken`. It cannot run while nobody is logged on,
which is what skipped the 11:30Z fire. **Changing it requires elevation this seat does not hold**
and is surfaced as a CALL below, not performed here.

## WHY THIS PATH

⛔ **NOT Terraform, and not an AWS control at all.** This is a Windows scheduled task on a physical
laptop. There is no cloud resource to change — the device's own timer is where `OS-s-21` put the
carrier, and `1.0.0_SA_CTO`'s L4 ruling @`46b832a9a3` explicitly kept it there: the commit-stitch
carrier was ruled out as anti-correlated with the signal and path-blind, and the hook it named had
been retired the day before. **The only thing Andrew's word changes is the INTERVAL.**

## BLAST RADIUS

Exactly one task on one device. **No AWS resource is created, modified or deleted.** The scoped-role
assume (`outset-drift-publisher-laptop`, CTO ruling @`054353ac5e`) is untouched and no new credential
is stored on the device. The publish still writes exactly ONE key,
`s3://opal-estate-report/outset/laptop/comp_heat_drift.json`, at a HIGHER FREQUENCY — that key is
versioned, and the only consumer effect is a fresher `LastModified`.

⚠ **THE ONE PROPERTY THAT MOVES BEYOND THE TASK:** the publish rate goes from 1/day to as many as
96/day while a session exists. That is the intended effect of Andrew's word, not a side effect.

## ROLLBACK

Baseline exported BEFORE the act, byte-exact:

```
C:\Users\ANDREW~1\AppData\Local\Temp\os28_baseline\OpalOutsetDriftLaptop.BEFORE.xml
sha256 457E61C387D792E2D2B98CBA5F0CE792ECF1CE0AFAA5719E0E159E2D6AF6B4E1
```

One command restores the exact prior task, principal and settings included:

```powershell
Register-ScheduledTask -TaskName "OpalOutsetDriftLaptop" -Xml (Get-Content -Raw `
  "$env:TEMP\os28_baseline\OpalOutsetDriftLaptop.BEFORE.xml") -Force
```

Producer rollback is `git revert` of the `publish_drift.py` commit; the added fields are additive
and the consumer reads `tool_scalars` by key, so an older consumer ignores them.

## ⛔ WHAT THIS CHANGE DOES **NOT** ACHIEVE

**It does not make the publish survive a logged-off device, and that is the larger half.**

Measured this session, non-elevated, with a positive control on a FRESH task so the denial cannot be
"the existing task is locked":

| principal form attempted | result |
|---|---|
| `Interactive` (POSITIVE CONTROL) | **registered OK** |
| `S4U`, `AzureAD\AndrewBerman` | `Access is denied` |
| `S4U`, bare `AndrewBerman` | `Access is denied` |
| `GroupId BUILTIN\Users` | `Access is denied` |

So the denial is specific to **every** "runs while logged off" principal, not to task registration.
This confirms row `NFRA_OUTSET-S39` and adds the control that row could not run.

**THE CALL, WITH THE EXACT LINE** — one elevated PowerShell, run once by Andrew:

```powershell
Set-ScheduledTask -TaskName "OpalOutsetDriftLaptop" -Principal (New-ScheduledTaskPrincipal `
  -UserId "AzureAD\AndrewBerman" -LogonType S4U -RunLevel Limited)
```

**Its one-line rollback:**

```powershell
Set-ScheduledTask -TaskName "OpalOutsetDriftLaptop" -Principal (New-ScheduledTaskPrincipal `
  -UserId "AzureAD\AndrewBerman" -LogonType Interactive -RunLevel Limited)
```

⚠ **AND IT MUST BE VERIFIED BY A FIRE, NOT BY THE WRITE.** An S4U token carries no network
credentials — untested on this box — so after the line runs, a publish must be OBSERVED under the
new principal before anything is claimed. `Set-ScheduledTask` self-reports success on a
non-terminating failure (`NFRA_OUTSET-S39`), so the write's own output is not evidence.

⛔ **NO HAND-PUBLISH WHILE THIS IS OPEN.** Bound (61) of the face: if the reading ages past the
consumer's 26 h ceiling before the principal lands, **the report SHOULD say this device is silent.**
That is the instrument working. The current artifact is `2026-09-09T23:58:14Z`, so the ceiling is
reached at ~`2026-09-11T01:58Z`.

## CLOSE-OUT — 2026-09-10 ~18:4xZ

**Part 1 LANDED AND VERIFIED. Part 2 remains Andrew's, and is stated above rather than worked around.**

**The write, read back rather than self-reported:** `Repetition.Interval=PT15M`,
`Repetition.Duration` empty (indefinite), `Principal.LogonType=Interactive` (deliberately unmoved),
`Arguments` carry `--trigger scheduled`. Task XML diff: **4 lines added, 1 removed, 0 unexpected
either way.** Both battery flags still `False`.

**TWO AUTOMATIC PUBLISHES OBSERVED, NEITHER STARTED BY THIS SEAT:**

| version | instant | how it was started |
|---|---|---|
| `hz832zL8rkcnC2fNailBAR` | `2026-09-10T18:16:56Z` | scheduler picked up the missed occurrence |
| (next) | `2026-09-10T18:30:11Z` | the quarter-hour repetition |

The second one is what makes this a **cadence** rather than a single event. Both carry
`trigger_measured: scheduled` and an ancestry of
`python.exe <- cmd.exe <- svchost.exe <- services.exe <- wininit.exe`, which a shell-launched run
cannot have.

**Acceptance:** `O28-AC1` battery, 6 arms, **6 HOLD / 0 FAIL**, token
`OS28-DRIFT-PUBLISHES-WITHOUT-A-HUMAN`, rc=0 captured unpiped.

**No hand publish was made at any point.** The artifact was allowed to sit 18.3 h stale, and that
staleness is the evidence arm (a) rests on.

**Rollback not exercised** — nothing required it. It remains one line against
`os28_task.BEFORE.xml`, sha256 `457E61C387D792E2…`, which is committed alongside this entry.

**Surprise row filed:** `NFRA_OUTSET-S46` (the `.tools/aws` shim is not executable by a Windows
Python parent; fixed in the battery by resolving the shim rather than assuming it).

⛔ **STILL OPEN AND OWNED BY ANDREW:** the S4U principal line above. Until it runs, this device
publishes nothing while nobody is logged on, and **the report should say this device is silent
rather than be made green by hand.**
