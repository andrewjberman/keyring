# /canonical-drive NFRA_OPALAI -- 2.0.0_SA_COO~AI -- 2026-10-09 01Z-02Z (site Z)

**archetype:** COORDINATE

Arm: `org/ref/LIVE_ARMS.md` ~O row (`/canonical-drive <own project> 30m`, paired with `1.0.0_SA_CTO~O` `/self-drive`),
re-seat by `1.0.0_SA_CTO~O` msg 32039. Ticks 1-6 (2026-10-08 ~22:2xZ to 10-09 ~00:3xZ) were NO-OP: every open round-2
order waits on the item-0 close run, Andrew's act with Alyssa (his 10-06 word: "nothing we can do on the call 1 at this
time"). The per-tick rows are in `org/mcp/drive_ticks/2.0.0_SA_COO~AI.md`.

## Tick 7 -- EMPTY TICK -> `/next-calls NFRA_OPALAI --drive` (empty_tick=on)

| project | limb | round | TOs t/T | cells | thread | act fired |
|---|---|---|---|---|---|---|
| NFRA_OPALAI | L7 EXECUTING, lease FULL | 2 | 38/42 after re-open, 39/42 after drain | no uncovered cell | y | DRIVE FORWARD around the block |

- **Calls:** none genuinely open. The Alyssa sitting was answered on 10-06 and is not queued again.
- **Option 1, FREE: R5's persistence arm for the DAPI 8194 wall.** Site Z booted at 2026-10-08T20:56:05Z, which is after
  OA-f-11's acceptance, and bbcomm was up on 8194, so the arm could be read.
  - First cut as a new order, OA-f-15. `.tools/to-pipeline-gate.py` REFUSED it: round 2 already has its one issuance,
    and "a re-cut into the first issuance MODIFIES its orders and adds no file".
  - Re-cut as OA-f-11 amendment A2 with AC4 (@997238e4fc). LIMB 6 does not fire on a modification; GATE (viii) graded
    it. Checks: base FAIL; synthetic GREEN PASS; RED FAIL on agent OPEN; RED FAIL on a boot before the apply.
  - Worker `0.9.0_WK_NFRA_OPALAI~26` (worker-light) committed 3722b9a96f: Opal_Agent and Opal_MSP were REFUSED on 8194
    and OPEN on 8790; the operator was OPEN on 8194; R1 rules 0.
  - Issuer re-grade on the worker branch: PASS. AC1 and AC3 entries are content-equal to before; no probe leftovers;
    8790 has 0 listeners.
  - Drained @438c776cd8 (safe-merge fast lane). AC4 on the shared tree: PASS. Slot worktree and branch removed.
  - **Result: the wall holds across a reboot.** R5's last open arm is closed.
- **Option 2, FREE: the close-run card's state, re-read.**
  - opal_ai PROD = DEV = de5ce25fa3.
  - The runtime checkout is at 9c0a80b8d0, clean, and fast-forwards to PROD; `launcher.ps1` and `launch-gate.ps1` are
    unchanged.
  - Wall persistence PASS.
  - Appended to `CLOSE_RUN_CARD_20261002.md` in this commit.
- **Row NFRA_OPALAI-Z-W26-S1 (worker):** the issuer's sparse cone for slot ~26 left out `org/projects`, `org/devices`
  and `org/missions`, so safe-commit refused three times until the worker widened it. This is the issuer's own defect.
  Ruling: every future slot cone for this project includes those three directories.
- **After both options:** no FREE option remains. NOTHING-LEFT: OA-t-1 r2, OA-t-3 r2 and OA-e-8 wait on the item-0
  close run (Andrew's act, no sitting set). No call has been queued on it, because it is already answered.

## Inbox

Acked, each with no effect on this lane:
- 32163: law edit 538f0f51a7, per-box branches.
- 32228: law edit c55a7b39cd, the rule-30 naming gate REFUSES.
- 32247: KEEP-DRIVING ON, which this lane was already following.

## Compiler Tools

| Tool | Target | Result | Note |
|---|---|---|---|
| `comp-surprise --project NFRA_OPALAI --json` | channel | PASS | 124 items, 17 open, 2 armed. Z-S57 reads ARMED only because the CVO has not adjudicated it; it was disarmed in Z-S60 |
| `comp-find` | `persist`, credential refs | PASS | 33 hits / 240 files; found R5's persistence arm and row Z-S41 (no direct credential use by this seat) |
| `.tools/to-pipeline-gate.py` (via safe-commit) | OA-f-15, then OA-f-11 A2 | REFUSED, then OK | the one-issuance limb; the gate's remedy was followed |
| `comp-blast` / `comp-routes` / `comp-cache` | -- | NOT RUN | a measurement-only amendment, no route, cache or infra edge |

**What failed:** a raw `find` or `grep -r` over a scratch directory is refused by the rail. A `cat ... | grep` pipe
receiver is the allowed form.
