# The console that stalled the harvester for nine hours no longer exists: the site Z runner is windowless on pythonw -- 0.7.0_AE_CloudOps~ZW

**archetype:** DEPLOY

**Date:** 2026-10-13
**Task Order:** AMGT_HARVST.TO-HVST-bz-4.site-z-runner-registered-windowless (crossbox XB-20261013T073105Z-9b01 from `2.0.0_SA_COO~W1`, dell1)
**Status:** COMPLETE

---

## Objective

Remove the cause of row Z-S115 rather than its symptom. The runner was registered to `python.exe`, which
gives it a console window; a selection made in that window blocks the process on its next write, which is
what stalled the harvester for 9h24m. Re-register the task from pin `995adcaeaa` under `pythonw.exe`, which
has no console window, and change nothing else.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger | `open` / `close-leg` x5 / `close` | PASS | Opened before any change with legs PIN LOCK STOP ARM WINDOW; all five closed with proof. The bz-1 entry was closed in the same session. |
| proof-of-spec-check | `<instance> AC1,AC2,AC3 --governing-order <TO>` | PASS | VALID rc=0, 0 violations, 3/3 coverage, 3/3 invocation alignment, both surprise ids resolving. |
| surprise-row-gate | at commit | PASS | 2 new rows of 400 checked; 397 pre-existing not re-graded. |
| kill-maint | DRY RUN x2, never `-Execute` | PASS | Default age prints `0 candidate(s) EXEMPT`; the labelled classifier exercise prints `EXEMPT PID 50360`. Both printed, graded as they read. |
| comp-schedule | not run | SKIPPED | The preflight assigns it to L5, the issuer at decomposition. This seat touched one scheduled task and read it directly with `Get-ScheduledTask` and `schtasks /query /xml` before and after. |
| comp-iam | not run | SKIPPED | The preflight's own words: an act on the box's own task scheduler and worktrees. No S3 write, no publisher call, no IAM surface -- no subject. |
| comp-rail (hook) | 3 DENIALS | PASS | All three taken as written, none overridden; two re-run with native `Grep`/`Glob`, which the rail's FREE list admits. |

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Start conditions (a)(b)(c), each read | P on `origin/CLOUD` with reverse read rc=1; both halves SIGNED at their pins; runner progressing |
| 1 | Ledger opened before any change | `harvst-bz4-windowless-20261013`, 5 legs |
| 2 | Stop file created from the task's own argument | 07:56:19Z; deadline 08:11:19Z |
| 3 | New pin worktree at P, locked | HEAD `995adcaeaa`; **all four** harvest pins locked |
| 4 | Cycle ended **by its own stop file** | 07:59:03Z, `stopped_by_operator`, failed 0, in 2m44s |
| 5 | C-g stop file deleted | 08:06:50Z, `Test-Path` False |
| 6 | Census | NONE over all processes of any exe, control 47 of 568 |
| 7 | `-Plan -Windowless` read, registered once, started once | 08:09:06Z / 08:09:08Z |
| 8 | The four reads at +7.3 and +17.9 min | R1 R2 R3 R4 all TRUE |
| 9 | kill-maint DRY RUN x2 | `EXEMPT PID 50360`, 0 target lines |
| 10 | Rollback (step 8) | **NOT taken, never reached.** Branch G: it stays |

---

## Verification

```
AC1  Actions.WorkingDirectory -> C:\Users\Opal Bloomberg\Desktop\wk-harvest-runner-pin-995adcaeaa   PASS
AC2  Actions.Execute          -> C:\Program Files\Python314\pythonw.exe                             PASS
AC3  bz4_console.out          -> MainWindowHandle=0 ... CONHOST_CHILD=NONE                          PASS
R2   schtasks /query /xml     -> <Command>C:\Program Files\Python314\pythonw.exe</Command>
R4   checkpoint done length   -> 2 at +7.3 min, 6 at +17.9 min (grew 4, needed 3); 0 error lines
```

R4 is the read that matters most and the one bz-3's own test could not make: bz-3 exercised a FAKE driver,
so `pythonw` had never actually spawned the real collector. A runner that wrote its log but spawned nothing
would have passed R1, R2 and R3. The spawn was also read directly as a live process -- PID 4164,
`pythonw.exe`, child of 50360, itself windowless.

---

## Decisions Made

1. **Two corrections I surfaced rather than buried.** A PowerShell datetime subtraction against a
   `Z`-suffixed literal misread +12 minutes as +252 and printed "+15 due: True". R4 had grown by 2 of a
   required 3 at that moment, so accepting it would have **rolled back a runner that was working
   perfectly.** Every elapsed figure is now epoch arithmetic. Separately, R3's own control disproves half
   of R3: a console `python.exe` reads `MainWindowHandle = 0` too, so only the conhost-child count
   discriminates. Both are written into the evidence rather than left implied.
2. **I did not flip row Z-S115's clock.** The order's record face calls this seat the disarm owner, the CTO
   relay calls it `2.0.0_SA_COO~W1`, and the row itself still reads `INERT` with `disarm_owner`
   `2.0.0_SA_COO~W1` in the investigation plane -- so the graduated ARMED clock is in the remediation plane,
   which CLAUDE.md reserves to the CVO and which this order's `<paths>` does not name. The substantive
   condition is met and evidenced; row Z-S116 asks for the owner and the file. Writing outside a declared
   surface to close a clock would be the wrong kind of helpful.
3. **I widened the census and said why.** bz-1's census filtered `Name='python.exe'`. That filter would
   have been structurally blind to the very process this order creates. The order asked for all processes
   of any exe, and that is what ran.
4. **The STOP-FILE test is a count, not a presence check.** The log already carried 2 such lines from the
   earlier stop; `grep -c > 0` would have read TRUE before the runner had done anything.

---

## Files Modified

| Commit | Content | Push state (ls-remote, measured) |
|---|---|---|
| `f0c836e1ac` | the interim-rule record (console minimized, watch armed) | ON ORIGIN |
| `2e5995b738` | the bz-4 act, 10 evidence files, proof instance, rows Z-S116/S117, both ledgers closed | LOCAL -- integrator's box-sync carries it |

Ten evidence files under `deliverables/0.7.0_AE_CloudOps~ZW/round84/`. The order file itself was not
edited: the issuer flips its status.

---

## Blockers

**None.** Two questions are with the issuer and neither blocks this seat:

- **Z-S116** -- name the single owner of Z-S115's clock and the plane it lives in.
- **Z-S117** -- bz-5's "two consecutive failure-free records" trigger is already satisfied, but **both
  records are operator-truncated stops this seat caused**, while all three cycles that ran to completion
  carried failures (2, 4, 8). A short cycle is failure-free because it was cut, not because the failure
  rate changed. The two halves also read opposite on whether a plant is authorised at all. Recommendation
  in the row: count only completed cycles, which makes the count 0 and needs no plant.

---

## Current State

One runner, PID 50360, `pythonw.exe`, from pin `995adcaeaa`, `MainWindowHandle` 0 and no console host. The
state directory and runtime root are unchanged at the `c1be67f53c` pin, publishers unchanged. All four
harvest pins are locked. `1c69fa35a3` remains the signed rollback (installer with `-RepoRoot <old>` and no
`-Windowless`).

**The hazard is structurally closed, not merely avoided:** there is no console window for anyone to click
in. The issuer's interim rule (keep the console minimized, read the log hourly) was scoped to PID 27560,
which is gone, so it has expired by its own terms. I have not built a successor watch -- the standing
moratorium applies and the issuer can ask if it wants one.

---

## Next Steps

1. `[2.0.0_SA_COO~W1]` Answer Z-S116 (whose clock, which file) and Z-S117 (do truncated records count; is
   a plant authorised). Sent on the bus at 08:4xZ.
2. `[2.0.0_SA_COO~W1]` Flip the `<status>` of bz-4; the assignee does not edit the order file.
3. `[0.7.0_AE_CloudOps~ZW]` HVST-bz-5 stays open at its start condition: no ended cycle record since the
   08:09:08Z windowless start. The first windowless cycle ending is both bz-5's read and the honest test of
   whether a failed pair now names its reason (row D1-W135-S2).
