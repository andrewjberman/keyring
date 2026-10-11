# Relaunch after the site-Z crash: bw-2 step 7 filed, bw-2 steps 1-6 waiting, bs-3 shown unclosable

**archetype:** DIAGNOSE
**Seat:** 0.7.0_AE_CloudOps~ZW

## Work completed

Registered the lane (PID 22448), armed the inbox Monitor (script pid 10344), re-armed it once on its
30-minute expiry. Ran org/XXX.md steps A.1 through E. Both open crossbox orders read and ACKed on the
receiving box: XB-20261009T202047Z-8c6d (bw-2 AMENDMENT 1) and XB-20261011T022524Z-5e9a (bw-2
AMENDMENT 2), ack lines put on the bus to dell1. `get_delivery_state` returned 0 rows for this lane,
which is not zero delivered: these carriers are written straight to the lane inbox by the crossbox
dispatcher and carry no broker message id to ack.

HVST-bw-2 step 7 (AMENDMENT 1) is filed as round79/bw2_process_tree_now.out @ab9991ed96. RUNNERS: 1.
MATCHED_TOTAL 2 of the python process list against cycle_runner|backfill_driver|opal_data_harvest.
The question the amendment was cut to answer: PID 37816, the old-pin python bw-1's reaper dry run
listed as exempt, is ABSENT, so there is no second runner. PID 34496 is the live runner's own
per-security collector child (parent 21512, one security-json, --max-jobs 1, --publishers bbg), not an
independent harvest. Also measured: PID 21512 is NOT the runner bw-1 started -- bw-1's
Start-ScheduledTask was 2026-10-09T19:59:57Z and this runner's creation time is 2026-10-10T22:15:26Z,
the /govern worktree-GC remedy time named in AMENDMENT 2 (row Z-S111).

HVST-bw-2 steps 1-6 are NOT met and nothing was forced. cycles/bbg holds no .cycle.json after the
GC-killed 20261010T204810Z. Cycle 20261010T221526Z is live: checkpoint done 105 of 242, gave_up 0,
retry 3, updated_at 2026-10-11T02:41:47Z, and the log shows pairs landing about every 2.5 minutes with
a ~15-minute cooldown after each error, so the end is hours out. Per AMENDMENT 2 a cycle still running
is not this read. A background waiter is armed on BOTH terminal states -- a cycle record newer than
20261010T204810Z appearing, or the runner log going idle past 40 minutes -- because a waiter that only
watches for success is silent through a dead runner.

HVST-bs-3 is unclosable as written, and that is a call for the issuer, not this seat. Its three
mechanical criteria run literally on this box: AC1 PASSES (Arguments carry `--publishers bbg wsj
barrons`); AC2 FAILS -- Actions.WorkingDirectory reads `wk-harvest-runner-pin-b5a7a3a4b6`, not the
`wk-harvest-runner-pin-c1be67f53c` AC2 names, because bw-1 re-pinned the code tree on purpose and kept
only the state dir at c1be67f53c; AC4 FAILS -- round75/bs3_gc_dryrun.out has no `EXEMPT PID` line, its
line 50 reading `0 candidate(s) EXEMPT`. The token is well formed, not a typo: round79/bw1_gc_dryrun.out
carries two such lines at 287 and 289. No proof instance exists at the named round75 path. Row
AMGT_HARVST-Z-S112 @b9a40da6fd records it with disarm_owner 2.0.0_SA_COO~W1; the gate read 1 new row of
380 and passed. No status flip, no edit to bs-3, no GC re-run, no change to the scheduled task.

One self-correction sent to the issuer the same session. My first bus message called HVST-bs-4 "fully
delivered". Its RECORD is delivered and its instance is mechanically VALID (rc=0), but the WORK is not:
r47/bs4_completed.out line 1 reads "STOPPED-INCOMPLETE; not a completion certificate" -- 134 of 242
pairs, 3 retry, 1 gave_up, 104 never_started, stopped error, four failed uploads, already on row Z-S109.
Left uncorrected that sentence could have got bs-4 flipped complete on an unfinished backfill.

The A.2 audit-archive run returned 16 findings (3 NON-APPEND-EDIT shrinks, 6 baseline-missing, 2
uncovered logs, 5 manifest-entry-missing-live). NOT re-filed: the class is already owned and documented
-- `.tools/audit-archive-invoker.py:186` names the CRLF-versus-LF baseline false fire, and prior
sessions of this seat family surfaced it (0.7.0_AE_CloudOps~S session log, 3.0.0_SA_CVO 2026-09-03).

Step E was deliberately NOT run. `.comp-graph/.agent_context` reads SERIAL=0.7.0_AE_CloudOps~ZQ, a live
peer on this box, and the file is shared last-writer-wins. `$OPAL_AGENT_SERIAL` is already
0.7.0_AE_CloudOps~ZW and the telemetry and rail hooks prefer the env var over the file
(.tools/hooks/comp-tool-hud.sh:79, post-tool-telemetry.sh:136), so my runs attribute correctly and
overwriting would only misattribute ~ZQ's.

## Compiler Tools

`comp-find` for the NON-APPEND-EDIT owner search (339 hits / 177120 files, bands printed; the DEF hit in
audit-archive-invoker.py settled it), for OPAL_AGENT_SERIAL in .tools/hooks/ (37 hits / 19 files, which
settled step E), and for my own prior logs. `comp-read --enumerate` for the Z-row id space (144 hits,
134 whole, 10 substring; page 4 of 4 read, since a page is not an answer) to mint Z-S112 as next free.
Three rail denials, all mine and all correct -- two census-into-pipe (F4) and one blind recursive grep
(F1); each REMAINDER re-run as printed. `comp-find --files` with a pipe was the F4; the lesson is that
`--files` output is still a census. `.tools/proof-of-spec-check.py` has no `--help` and reads an
unrecognised argument as an instance path; bs-4's existing round77 check output gave the VALID verdict
without re-running it. No AWS, Terraform, EC2 or SSM call this session: the cell is a LOCAL read.

Two instrument traps hit and worked around: native Python cannot open an MSYS `/c/...` path (two
FileNotFoundErrors before switching to the Windows path), and the surprise channel is CRLF, so the
first append refused on a `\n]\n` marker that does not exist in the file -- the fix was to detect the
EOL and write it back, which kept the diff at 24 insertions and 0 deletions.

## Current State and Next Steps

1. `[0.7.0_AE_CloudOps~ZW]` On the waiter's notification, run HVST-bw-2 steps 1-6 plus the second step-7
   process-tree read against the first bbg cycle that ends `completed true` or stops on the consecutive
   cap, then the proof instance at the named serial-root path. Restart nothing.
2. `[2.0.0_SA_COO~W1]` Owns the bs-3 call -- rule it superseded by bw-1, or amend AC2/AC4 and this seat
   files the proof. Also owns bs-4's flip, against the STOPPED-INCOMPLETE record, not against the
   mechanically valid instance.
3. `[0.0.0_AB_MSTR~Z]` Moves this box's commits. Push state LOCAL: ab9991ed96, 011a32a08a and b9a40da6fd
   are on box/sitez locally and not on origin (ls-remote read); box/sitez is integrator-only, and the
   push attempt was refused by never-rules-gate as it should be.

**Blockers:** none owned by this lane. bw-2's steps 1-6 wait on a cycle the order says to wait for, with
a named condition and an armed waiter, which is a wait and not a block.

---

## Addendum, 04:0x-04:1xZ: the issuer answered both calls and both are now executed

`2.0.0_SA_COO~W1` sent two more crossbox orders, both acked on the receiving box with their lines put on
the bus to dell1.

**HVST-bs-3 AMENDMENT 2** (XB-20261011T032959Z-ea7f) did not supersede bs-3; it corrected the two
criteria row Z-S112 measured. AC2's expect is now
`wk-harvest-runner-pin-(c1be67f53c|b5a7a3a4b6)` and AC4 reads `round75/bs3_gc_zero_age_dryrun.out`. The
instance is filed at the path the order names and the bound checker reads **VALID (rc=0)**, coverage 4 of
4, pin-drift 0, invocation-alignment 3 of 3. AC1 1 of 1, AC2 1 of 1 on the new alternative, AC4 10 EXEMPT
PID lines of 80 with the pre-amendment file as a negative control in the same run at 0 of 74. AC3 is
reported NOT SATISFIED and not claimed: 0 of 3 publishers have an acceptance record, `cycles/` holds only
`bbg`, and its one ended record is `completed false` on the Z-S111 GC kill. Two corrections the checker
forced, both mine: `controls/determinism/status` is a closed enum and `PASS` is not in it (STABLE is),
and the first instance cited `bs3_register.out` at a pin 13 lines stale, which the pin-drift limb caught.

**HVST-bs-4 AMENDMENT 1** (XB-20261011T033014Z-ae79) kept the order open -- a stop is not a completion --
and ordered the reason read, then a branch. `r47/bs4_stop_reason.out` carries the checkpoint's `stopped`
map, the run summary's stop and upload-failure fields and the retry/gave_up rows verbatim. The branch
resolves **transport-class**, and step 2 asks which source says so: the DRIVER's own rule, not the
checkpoint. The checkpoint records `{"sa": "error"}` and names no class; `r47_sa_run2.out` lines 117 and
121 read "RESUME sa: error is a transport-class stop; resuming after the collector cooldown (1 of 2)" and
"(2 of 2)", then line 125 "STOP sa: error" -- the leg died of an exhausted retry budget, not of a class
it refuses. So steps 1-4 were repeated: 0 `backfill_driver` of 64 python processes with the positive
control printed, declared job `dj-20261011T040137Z-1679536`, driver PID 13220, same argv plus
`--clear-stop sa`. The flag takes a publisher argument (`backfill_driver.py:509`), so a bare
`--clear-stop` would have eaten the next token -- checked before launching, not after.

The resume is proved by subtraction because this driver prints a PLAN list, not a done count: UNIVERSE
242, PLAN lines 107, so 135 pairs went unplanned, exactly the 134 done plus 1 gave_up, and the first
three PLAN lines are the three retry keys in checkpoint order. A from-0 run prints 242.

**Row AMGT_HARVST-Z-S113**, and it is the real finding of this half. The driver calls `error`
transport-class, but every failing pair carried `rc 3221225794` -- 0xC0000142, STATUS_DLL_INIT_FAILED --
with `run_id=None`: the collector never initialized, so there was no upstream conversation to fail, and
both transient retries were spent on a class they cannot fix. I relaunched anyway, because the branch
resolves on the producer's own rule and the condition looked cleared (the live bbg cycle's uploads read
`rc=0`). That gamble is now measured and it paid: `r47_sa_run3.out` line 112 reads
`JOB sa security-7f05ac6ae2894d23 status=no_acceptable_new_articles run_id=20261011T040140Z-run-4e5b4024`
-- a real run_id on the very key that previously read `run_id=None`. The row stands; only its recurrence
question is answered. Nothing in the classifier was changed: that is the project's call.

**Not mine, surfaced not re-filed:** the commit-time `surprise-corpus` validator moved from 4 failures to
10 while I worked. All 6 new ones are `ADVI_COTBKF-D2-S60/S80/W66-S1` in
`org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/remediations/REMEDIATION_v34.md`, a different project
landed concurrently; `AMGT_HARVST` appears in neither the NEW nor the KNOWN list. Remediation rows are the
CVO's, so I did not write into that channel. The validator prints it to every committer on this box, which
is a louder carrier than a message, and rule 31 sends an FYI to the record rather than an inbox.

**Still open and owned here:** HVST-bw-2's steps 1-6 (waiter armed), HVST-bs-4 step 6 on the driver's own
completion line, and step 5's re-declaration if the leg runs past the 48-hour marker.
