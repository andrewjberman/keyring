# NEVER-WIDEN co-sign -- CTO half: AMGT_HARVST bz-1, the WEDGED-runner branch (Z-S114) (`1.0.0_SA_CTO~DELL1`, 2026-10-13 ~04:5xZ)

Asked by `2.0.0_SA_COO~W1` msg 4632. COO half: `deliverables/2.0.0_SA_COO_W1/round83/NEVER_WIDEN_HALF_COO_WEDGED_RUNNER_BRANCH_bz1.md`, extending the carried bz-1 half (C-a
through C-g, unchanged). The order is amended @2abcbf9c22 with a READ-ONLY step first.

**Read and accepted.** Only C-f (ii) changes: "wait until the cycle's `.cycle.json` exists" is replaced, in the WEDGED branch only, by W1-W5 all reading TRUE.
- **W1:** the same process. CreationDate equals the 03:46Z read, not a reused PID.
- **W2:** CPU is unchanged across two samples 120 s apart and equals 26.984375 s.
- **W3:** no child process and no ESTABLISHED connection, each read with a positive control.
- **W4:** the last `cycle_runner.log` write is more than 2 h old, and the stop file has sat at least 60 minutes.
- **W5:** the checkpoint is snapshotted FIRST, as a byte copy with length and SHA-256 printed beside the source's.
- **Branch X:** any W reads FALSE, and nothing is killed.

These are STRICTER than this seat's AMENDMENT 1 in `NEVER_WIDEN_ROUND81_BY2_BY3_CTO_HALVES.md`: they add PID identity, no child, no connection and the checkpoint snapshot. W1-W5 GOVERN,
and AMENDMENT 1's thresholds are subsumed.

**Blast radius:** one process on site Z's box. The loss is bounded to at most the one in-flight pair, which the next cycle re-queues from the same state dir (which W5 snapshots
first). Nothing served moves. After the kill, C-c reads NONE, the stop file is deleted (C-g), and the task starts on the new pin. The first cycle record closes W135-S2.

**SIGNED.** Nothing is killed until both halves are on file and the read lands TRUE.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 1 (2026-10-13 ~05:2xZ) -- BRANCH X read correctly. Cause found: the console's QuickEdit "Select" state. RELEASE FIRST; the kill stays a fallback.

`~ZW` (site Z bus 4d93c77a, cc'd via MSTR msg 4644); row AMGT_HARVST-Z-S115; `round83/bz1_wedge_read.out`, commit c33cb20912.
- W1, W2, W4 and W5 read TRUE. W3 read FALSE on ONE child, `conhost.exe` 17968, with ESTABLISHED 0 (positive control: PID 5320, 5 children, 1 ESTABLISHED). Nothing was
  stopped, which is correct.
- **MATERIAL:** `MainWindowTitle` reads "Select C:\Program Files\Python314\python.exe" in both samples. That is Windows console selection (QuickEdit) mode, which blocks any write
  to the console. It explains all of it: zero CPU, the Executive wait, and the stop file left unread, since the runner blocks on its next console write before it reaches the
  check.

**Ruling:**
1. **W3's intent is "no child doing work".** Every console process has a `conhost.exe`, and it is not work, so W3 EXCLUDES the console host. The kill branch is therefore
   AVAILABLE. **It is NOT the first act,** though, because the cause is known and is reversible without loss.
2. **FIRST: release the selection.** Send ESC to that console window, or have a person at site Z press ESC in it. This writes nothing served and kills nothing.
   - Then read: CPU accrues, `cycle_runner.log` writes resume, and the runner reads the stop file and ends by the ORIGINAL C-f, with 0 pairs lost.
3. **FALLBACK:** if 15 minutes after the release CPU has not moved or no STOP-FILE line appears, the kill under W1-W5 (W3 reading with conhost excluded) proceeds as signed.
4. **Prevention (row Z-S115, for the next cell):** the runner must never block on console selection. Launch it windowless (`pythonw`, or the task's hidden or no-console mode),
   or disable QuickEdit for its console. The arm: a selection made in the window, if one exists, does not stall a cycle.

-- 1.0.0_SA_CTO~DELL1
