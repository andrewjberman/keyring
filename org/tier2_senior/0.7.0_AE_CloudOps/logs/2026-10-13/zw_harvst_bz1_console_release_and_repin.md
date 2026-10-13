# A console left in QuickEdit selection mode had stalled the harvest runner for 9 hours; one Escape ended it cleanly and the re-pin landed as signed -- 0.7.0_AE_CloudOps~ZW

**archetype:** DIAGNOSE

**Date:** 2026-10-13
**Task Order:** AMGT_HARVST.TO-HVST-bz-1.the-runner-repinned-to-the-bx3-merge (crossbox XB-20261012T204423Z-6082 from `2.0.0_SA_COO~W1`, dell1)
**Status:** COMPLETE (the CYCLE ledger leg is a ~11h wait, HELD, not a blocker)

---

## Objective

Re-pin site Z's AMGT_HARVST cycle runner from `b5a7a3a4b6` to `P = 1c69fa35a3` (the merge of HVST-bx-3, which
makes a failed pair carry its reason), carry the state directory unchanged, and lock both pins. Seated for this
by CTO ruling `sitez-20261013T021451Z-39fc`, which restarted this lane specifically because it held live dell1
work.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | `comp-find '39fc' --files --limit 30` | PASS | DENOMINATOR 650 hits / 197318 files scanned, corpus=all. Found the CTO ruling that explains this seating. |
| comp-rail (hook) | two DENIALS taken as written | PASS | F4 (a census piped into a cutting receiver) and F1 (a recursive grep of the memory dir). Neither was overridden; the second was re-run with the native `Grep` tool, which the rail's FREE list admits. The rail was right both times. |
| comp-schedule | not run | SKIPPED | The order's `<preflight>` assigns comp-schedule to **L5**, the issuer at decomposition, not to the executing seat. This seat touched exactly one scheduled task and read it directly with `Get-ScheduledTask` before and after; no other schedule was touched. |
| comp-iam | not run | SKIPPED | The preflight's own words: this cell is LOCAL reads and writes on the site Z box only (a worktree, a scheduled task, the runner's state dir). No AWS call, no publisher host, no IAM surface -- comp-iam has no subject here. |
| proof-of-spec-check | `proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <TO>` | PASS | VALID rc=0, 0 violations, 3/3 coverage, 3/3 invocation alignment, both surprise ids resolving. First run was INVALID on 5 CCX rows; fixed by pinning already-committed artifacts to their real commits. |
| deploy_ledger | `open` / `close-leg` x4 / `hold` | PASS | Two `hold` forms were REFUSED mid-act for sound reasons and left standing rather than worked around; the hold was accepted only once every apply leg carried proof. |

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Start condition read, not assumed | `cat-file -e` rc=0, `is-ancestor P origin/CLOUD` rc=0, reverse read rc=1 (discriminates) |
| 1 | Both never-widen halves read at their pins | round-81 pair, then the wedge pair, then the console-release pair; negative control proves the `git show` read discriminates |
| 2 | Ledger opened before any change | `harvst-bz1-runner-repin-20261012`, legs PIN LOCK STOP ARM CYCLE |
| 3 | Stop file created from the task's own `--stop-file` | 03:57:25Z; its parent directory did not exist and needed `mkdir -p` |
| 4 | New pin worktree at P | `rev-parse HEAD` = `1c69fa35a34370...`, control on `<old>` reads `b5a7a3a4b6275...` |
| 5 | Both pins locked (C-e) | all three harvest pins read a `locked` line; closes row Z-S111's GC hazard |
| 6 | **Runner found WEDGED; no act** | AMENDMENT 2 gate read BRANCH X -- W3 FALSE on a `conhost.exe` child. Row Z-S114, then Z-S115. |
| 7 | Issuer ruled W3 excludes the console host; AMENDMENT 3 | Gate Y all six TRUE at 05:43:01Z, snapshot FIRST |
| 8 | ONE Escape to handle 1310950 | 05:46:00Z; the runner ended **itself** on its own stop file 3s later |
| 9 | C-g stop file deleted | 05:51:08Z, `Test-Path` False, before any start |
| 10 | C-c census | NONE, controlled at 44 matching rows of 47 total python processes |
| 11 | Installer `-Plan` read, then registered once, started once | 05:52:40Z / 05:52:43Z |
| 12 | kill-maint DRY RUN only, never `-Execute` | `EXEMPT PID 27560` via the labelled classifier exercise |

---

## Verification

The runner's own log, at the second of the keypress:

```
05:46:00Z STOP-FILE ...\wk-harvest-runner-pin-b5a7a3a4b6\.runtime\harvest-cycle\STOP present: ending after the current job (24 pairs done)
05:46:00Z CYCLE bbg 20261012T191641Z floor 2026-10-12 asked 242 new 1 held 0 failed 0 stopped stopped_by_operator completed false
05:46:00Z STOP-FILE ...\STOP present: no further cycle
```

`STOP-FILE` lines in the log: **0 before the key, 2 after.** Cycle record `20261012T191641Z.cycle.json` (388
bytes) reads `"stopped": "stopped_by_operator"`, `ended_at 2026-10-13T05:46:00Z`, `asked 242`, `failed 0`,
`requeued` 2. Task `Ready`, `LastTaskResult 0` -- a clean exit, not a termination.

Acceptance, each invocation run literally:

```
AC1  WorkingDirectory -> C:\Users\Opal Bloomberg\Desktop\wk-harvest-runner-pin-1c69fa35a3        PASS
AC2  Arguments        -> --state-dir "...wk-harvest-runner-pin-c1be67f53c/..."                   PASS
AC3  bz1_lock.out     -> wk-harvest-runner-pin-1c69fa35a3 ... locked                             PASS
```

The new runner is progressing on the discriminator the wedge taught: CPU 0.8125 and rising, **3 threads**
(the wedged one held 1), `MainWindowTitle` with no `Select ` prefix, cadence restored to ~2.5 min
(06:00:42, 06:03:18, 06:05:54, 06:08:31Z). Exactly one `cycle_runner`, PID 27560, from the new pin. One of
the two requeued pairs is already being re-asked from the carried state dir.

---

## Decisions Made

1. **Graded W3 on its words, not its evident intent, and took no act.** A `conhost.exe` is plainly not the
   "worker child doing work" the condition was hunting, and reading the intent would have authorised the kill
   immediately. But both halves had enumerated "a child" unqualified as a branch-X trigger, and reading a
   signed condition narrower than its words is the widening the pair exists to prevent. The cost was one
   message; the return was that the issuer re-read the condition, found the real cause in the evidence, and
   cut a cheaper act than the one I was about to be authorised to perform.
2. **Did not take the audited push override.** `never-rules-gate.sh` admits a `box/sitez` push only from the
   integrator, and CLAUDE.md defers "who may push where" to that gate. The override republishes every other
   seat's local commits, so push state is reported as measured instead.
3. **Did not work around either `hold` refusal.** The entry sat OPEN/RED between acts, which is the correct
   blaring signal, and took the hold only once every apply leg carried proof.
4. **Graded step 6 as failing on its wording** rather than reading the criterion down to fit the tool's
   current output, then satisfied it by round 79's own labelled method and declared what that proves.

---

## Files Modified

Commits, all authored `0.7.0_AE_CloudOps~ZW`:

| Commit | Content | Push state (ls-remote, measured) |
|---|---|---|
| `06eba89e3d` | pin + locks + row Z-S114 + ledger open | ON ORIGIN |
| `c33cb20912` | the wedge read + W5 snapshot + row Z-S115 | ON ORIGIN |
| `ee6847a39c` | console release, the act, proof instance, ledger HELD | LOCAL -- integrator's box-sync carries it |

Eleven evidence files under `deliverables/0.7.0_AE_CloudOps~ZW/round83/`, plus the proof-of-spec instance.
The order file itself was **not** edited: the issuer flips its status.

---

## Blockers

**None.** The one open item is a clock, not a seat: the ledger's `CYCLE` leg closes on the first ENDED cycle
record under the new pin, and a bbg cycle measures ~11h against a 05:52:43Z start. The entry is
`HELD-SOVEREIGN-GATED` on exactly that gate, so it reads KNOWN-HELD rather than half-landed RED.

---

## Current State

The act is complete and verified on both planes. The scheduled task runs from `1c69fa35a3`, so from the next
cycle record a failed pair carries its reason -- which is what row `AMGT_HARVST-D1-W135-S2` was waiting on.
The state directory and runtime root are unchanged at the `c1be67f53c` pin, as both halves ruled. All three
harvest pins are `git worktree lock`ed. `<old>` stays in place as the rollback (installer with
`-RepoRoot <old>`, same state flags, start once).

Nothing was killed. The cycle that had been stalled since 2026-10-12T20:22:35Z ended by its own stop file
with its 24 pairs recorded and 2 requeued.

---

## Next Steps

1. `[2.0.0_SA_COO~W1]` Disposition rows `AMGT_HARVST-Z-S114` and `Z-S115` -- both are `UNDER_INVESTIGATION`
   with this lane as surfacer and the issuer as `disarm_owner`. Reported on the bus at 06:1xZ.
2. `[2.0.0_SA_COO~W1]` Cut the prevention cell under `Z-S115`: launch the runner windowless (`pythonw`, or
   the task's no-console mode) or with QuickEdit off, so a selection in its window can never again stall a
   cycle. Per the CTO half's ADDENDUM 1 item 4 this is explicitly the NEXT cell, not this order's.
3. `[2.0.0_SA_COO~W1]` Flip this order's `<status>`; the assignee does not edit the order file.
4. `[0.7.0_AE_CloudOps~ZW]` On the first ended cycle record under the new pin, close the `CYCLE` leg and the
   ledger. That read also confirms a failed pair now names its reason, which closes W135-S2's `CARRIED_BY`.
