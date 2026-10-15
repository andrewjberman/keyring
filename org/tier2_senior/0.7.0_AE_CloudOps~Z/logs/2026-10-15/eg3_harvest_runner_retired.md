# 0.7.0_AE_CloudOps~Z -- handoff #10: the site Z harvest runner is RETIRED (OG-eg-3), and two instruments were wrong before the world was

Reassigned to this seat mid-session in A1 `167a5e9ecb`: `0.7.0_AE_CloudOps~ZW` owns the runner but is
stopped at a weekly usage-limit dialog until Oct 18, and `0.0.0_AB_MSTR~Z` declined to seat another
instance because the same model policy would meet the same limit. Andrew moved all harvest operations to
dell1; PRD v3.11 and the CTO's msg 34500 retire the runner; dell1's CTO accepted all four publishers.

| | |
|---|---|
| **stopped** | 2026-10-15T18:33:06Z (the runner's own last log line), process gone between 18:33:06Z and 18:53:36Z |
| **disabled** | 2026-10-15T19:04:24Z, `State=Disabled`, `Settings.Enabled=false`, still registered |
| **pins** | 5 of 5 LOCKED, untouched |
| **ledgers** | `...-retire` CLOSED (4 legs); `...-silver-cache` and `...-sa` CLOSED **SUPERSEDED** |
| **proof** | `eg3.AC1` PASS, `eg3.AC2` PASS, both exit 0 |
| **commit** | `9e71fa7215`, ON ORIGIN |

## 1. The act

STOP file written 18:13:30Z. The runner honoured it exactly as designed: *"ending after the current job
(7 pairs done)"*, then `CYCLE sa 20261015T153409Z ... stopped stopped_by_operator completed false`, then
*"no further cycle"*. Never killed, task untouched until the Disable.

Two things read rather than assumed before writing the file:

- **the predicate**: `cycle_runner.stop_requested` is `bool(args.stop_file and Path(args.stop_file).exists())`
  -- existence only, content never read -- and the stop file is **passed down to the backfill driver**,
  which is why the end lands on a JOB boundary rather than only between cycles.
- **row `Z-S120`'s defect** (the installer may not create the stop file's parent): checked first, the
  directory existed. Writing into an absent directory would have failed silently-ish and looked like a
  runner that ignored the file.

Pre-state at the Disable read **Ready, not Running** -- the runner had already exited, so the task was
waiting for its next trigger. That is *why* the Disable matters: the 3.14.8 reinstall at ~15:03Z means a
relaunch would now succeed. Registration byte-unchanged against the step-1 read, compared field by field:
arguments 412 chars, working_directory 64, execute 38.

## 2. The order's premise was false, and it changes a number someone else will use (`Z-S151`)

OG-eg-3 says site Z *"has stored `new 0` for every publisher since the 14:02Z Python outage, so retiring
it opens no capture gap that is not already there."* The runner's own log:

```
18:25:18Z JOB sa security-d13cdd57ffa64286 status=new_articles stored=2
18:33:06Z CYCLE sa ... asked 242 new 3 held 922 failed 0 stopped stopped_by_operator
```

**The mechanism is in my own step-1 read**: PID 37428 started **07:47:40Z**, hours before
`C:/Program Files/Python314` lost its `Lib`. A long-lived process keeps the standard library it loaded;
the outage broke new **launches** only. So site Z was still capturing when I stopped it.

The retire stands on its own authority and never depended on that sentence. What it changes is a
**baseline**: the pins stay locked until "dell1 reports a productive cycle per publisher", and anyone
comparing dell1's first cycles against a site Z baseline of zero would read a thin dell1 cycle as a match
rather than a regression. The honest `sa` baseline here is `new 3` over a cycle that reached **7 of 242**
pairs.

> **The generalisable form**: *"the platform broke at T, therefore nothing ran after T"* is false for
> every long-lived process started before T. The tell was the process's own creation time sitting hours
> on the wrong side of the outage -- which is why step 1 recorded it at all.

## 3. My own waiter counted itself, and would have filed a false ARMED row (`Z-S152`)

The order says act on the runner's **exit**, not a clock poll, so I armed a background loop counting
processes whose command line matched the token `cycle_runner`. **The loop's own bash wrapper carries that
token** -- the probe path and the `-match` literal are both in its command line -- so the census included
the censor. Floor 1, exit condition 0: it could never fire. Left armed it would have run the full two
hours and reported `RUNNER-STILL-UP-AFTER-2H`, which under the order's own clause obliges an **ARMED row**
-- a false hazard about a runner that had exited cleanly 100 minutes earlier.

Measured, not reasoned: the two rows the loose filter returned at 18:53:36Z were **both created at
18:22:29Z**, the second my waiter was armed, and one was literally `bash.exe ... eval PS=powershell.exe;
SCRIPT=.../eg3_count.ps1 ... -match "cycle_runner"`. After stopping the waiter the same loose filter read
**0 of 732**. The correct filter -- `pythonw?.exe` AND `-m lib.opal_data_harvest.cycle_runner`, which a
bash wrapper can never satisfy -- reads 0, `Get-Process -Id 37428` reads absent, and the any-python
positive control reads 47-50 so the zero is absence rather than a dead filter.

> **A census must exclude the censor.** Same shape as a check whose condition includes the artifact the
> check itself writes: carve out what YOUR act creates, not only what you expect to find.
>
> **And what actually caught it was the silence being WRONG-SHAPED.** The log said an exit was due within
> minutes; 27 minutes of nothing was evidence about the waiter, not the runner. A waiter that has not
> fired is indistinguishable from a target that has not finished -- unless you know roughly when the
> target should finish. Arm a waiter with an expectation of its own latency.

## 4. The two superseded ledgers

`...-silver-cache` (OG-eg-2) wanted its FIRSTREC leg to show the first post-restart cycle record carrying
`s3_get_count`/`s3_get_bytes`; `...-sa` (OG-sa-1) wanted its WINDOW leg to show an SA bronze object newer
than the re-registration for BA, BABA and COST. Neither can ever be produced here now. Both closed
**SUPERSEDED**, each outstanding leg recorded **NOT-EXERCISED rather than passed** -- I ran neither
`eg2.AC2.sh` nor `sa1.AC2.sh` and claim neither passes. The E1/E2 GET-bytes proof is owed on dell1 at pin
`39ae28559b`.

`deploy_ledger.py` writes its own fixed close line, so the SUPERSEDED declaration the order asks for lives
in each entry's **last leg proof**, where it is greppable -- and `eg3.AC2` reads `superseded closes 2 of 2`
from exactly there.

## 5. One coordination note

My two rows sat uncommitted for ~50 minutes and that **blocked box-sync** (MSTR read 141 commits behind
CLOUD) and the issuer's worker-branch merges, because CLOUD had also changed the channel file and the row
gate refuses another seat's new rows under the issuer's author line. The retire commit cleared it and
box-sync took CLOUD two minutes later. **An append-only shared file is a chokepoint: commit a row when you
write it, not when the act around it finishes.**

## 6. State

| order | state |
|---|---|
| **OG-eg-3** | **COMPLETE** -- stopped, Disabled, AC1+AC2 PASS |
| OG-ap-20 | COMPLETE, live at `06cfb6db64` |
| OG-ap-21 | steps 1-2 done, prep committed; step 3 waits on MX-r-14, whose own gate is `2.0.0_SA_COO~MI`'s unwritten A1 |
| OG-ap-17 | PAUSED by the issuer; CTO half owed |
| OG-mg-1 | Phase B waits on two halves and a GO |

The STOP file stays in place and the pins stay locked: they are the rollback source until dell1 reports a
productive cycle per publisher, and unlocking is `0.0.0_AB_MSTR~Z`'s act. Rollback, one act in order:
delete the STOP file, `Enable-ScheduledTask`, `Start-ScheduledTask`.
