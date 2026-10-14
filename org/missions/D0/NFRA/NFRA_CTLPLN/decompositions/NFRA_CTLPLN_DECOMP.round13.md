# NFRA_CTLPLN decomposition -- round 13: the batch repair, S9117's descendant stop, the fence checker re-baseline, the protected-functions census (issuer 2.0.0_SA_COO~C; cut 2026-10-13)

**Status: ISSUED in one issuance. FROZEN at the cut.**

**Input.** `ledger/ROUND_ANALYSIS.round12.md` (1.0.0_SA_CTO, @1fcb1b945a) section 3 (the ENRICHMENT LIST) and section 2 (rulings: `W79-S1`, `S9122`, `simulate_policy.py`, `W77-S3`, `S9117`); the issuer's `deliverables/2.0.0_SA_COO~C/ROUND12_INPUTS_FOR_ROUND_ANALYSIS.md`. **PRD:** v0.30, unchanged.

## Cells

| cell | what | serves | risk | workstream / round | issued to |
|---|---|---|---|---|---|
| `CT-ac-1` | ONE batch repair: `S9121` (crossbox merge carries a null `bus_message_id`; a refusal writes nothing); `W84-S1` (`spawn-agent.ps1` serial pattern); the `W81-S1` leftovers (the fabric list in three schemas guarded against the register, the stale HELD entry, the "read by AST" wording); `W79-S1` per the ruling (the OPEN-CALL arm matches the call's structured `project` field or a root path/`roots`, never free text; case 943 moves its project code into that field); `W79-S2` (the crossbox suite 50/50 independent of origin state); `W85-S2` (`derive_protected_functions.py --check` offline by default, `--live` explicit); `simulate_policy.py` retired as a gate. | FWD-2, FWD-5, FWD-10 | LOCAL | BATCH / 1 | `0.9.0_WK_NFRA_CTLPLN~87` |
| `CT-ac-2` | S9117's descendant stop: `kill-agent.ps1` ends the target's own process and its non-seat descendants and STOPS AT a descendant seat carrying another serial (prints it, logs it); an unclassifiable descendant keeps the whole-tree refusal as the floor. | FWD-21, FWD-25 | LOCAL | SEATKILL / 3 | `0.9.0_WK_NFRA_CTLPLN~88` |
| `CT-ac-3` | the fence-scoped check `shared-infra/tests/check_fence_scoped_rows.py` re-baselined (reasons 1, 3, 4 of row `ADVI_FIRMBKTS-D1-S43`; reason 2, the denied simulator, cleared with `CT-ab-2`), under the four rulings in its order; reads `ok=True` with no override. | FWD-5, FWD-10 | WORLD (path floor; read-only simulate calls only) | FENCE / 1 | `0.9.0_WK_NFRA_CTLPLN~89` |
| `CT-ac-4` | the protected-functions census re-saved at the live count (`W85-S3`: 233 saved, 238 live); read-only AWS; starts when `CT-ac-1` is merged (one chain). | FWD-10 | WORLD (path floor; read-only) | CENSUS / 1 | `0.7.0_AE_CloudOps~U7` |

## Carried with an OWNER and the CONDITION that un-parks each (not cut here; the analysis names them as seat reads first)

- **FWD-11, then FWD-9: one deliberate dell1 outage each** (v0.30: Andrew "Yes sure", at most 15 minutes, dell1, its manager parks the seats first, a time announced in advance). Owner: `0.0.0_AB_MSTR~DELL1`. Condition: it names the Tier-2 seat that holds each outage order and a window; the order is then cut as a recut (a task order cannot be issued to a Tier-0 manager).
- **FWD-27 read-back on every box** (key SSH answers; password refused with `CT-ab-7`'s grading; muse's key on dell2): Owner: `0.0.0_AB_MSTR` for `~DELL1`, `~DELL2` and site Z (Andrew's own word: MSTR issues the order to the managers). Condition: each manager's read, run with `.tools/ssh-tailnet-verify.py` at `1249b0d2d6` or later, reaches the laptop. The laptop local account arm stays GATED on Andrew's "another time".
- **S9120** (the detached headless spawn on dell2) and **S9119** (the broker heartbeat writer): Owner: `0.0.0_AB_MSTR~DELL2` and `0.0.0_AB_MSTR`. Condition: the parent-process read names a transient parent; the broker read names the writer. Cells only on what the reads name.
- Carried from round 12, unchanged: the package route on a lane that needs a package (FWD-15/18/19), the FWD-4/7/8 reads, the FWD-23/25 seat acts; `W77-S3` rides the next needed apply of the identity root (CTO ruling).

## Rule 24

**Domain:** the round-13 list (items 1-7 of the analysis's section 3), the five section-2 rulings. Every item is a cell, a carried line with owner and condition, or a ruling already applied. **Same grain; one intent per cell; disjoint write surfaces** (`CT-ac-1` writes `.tools/crossbox-*`, `spawn-agent.ps1`, the three schemas and the identity root's `tests/derive_*`; `CT-ac-2` writes `kill-agent.ps1`, `seat-boundary.ps1` and `test_seat_boundary.ps1`; `CT-ac-3` writes only the one checker; `CT-ac-4` writes only the census files). **State coherence:** no cell applies anything; `CT-ac-4` and `CT-ac-3` make read-only AWS calls (`iam simulate-*`, `lambda list/get`).

## Dependency chains and fan-out

Three chains (`CT-ac-1` then `CT-ac-4`; `CT-ac-2`; `CT-ac-3`). `fanout: 3 of 3 chains, cap 8, reason: three laptop worker cells with disjoint write sets; the census cell queues behind the batch on one chain and goes to the seated CloudOps lane`

## Recut 1 (2026-10-13 ~22:1xZ, issuer 2.0.0_SA_COO~C): the FWD-11 outage cell, un-parked by MSTR msg 108944; S9120 and FWD-27 reads recorded

Authority: a recut covers its affected cells; the carried line "FWD-11, then FWD-9" named its own un-park condition (a Tier-2 seat and a window), met by 1.0.0_SA_CTO~DELL1 msg 5262 via MSTR msg 108944. No existing cell changes.

| cell | what | serves | risk | workstream / round | issued to |
|---|---|---|---|---|---|
| `CT-ac-5` | FWD-11: dell1's state recorded before (S0) and after (S1) the manager's deliberate restart window Wed 2026-10-14 05:15-05:30Z (slot 06:15-06:45Z if it slips): which round was where, nothing lost, nothing redone; the restart is the manager's act, not the seat's. | FWD-11 | WORLD (a deliberate dell1 outage; this seat reads and publishes only) | RESTART / 1 | `0.7.0_AE_CloudOps~CT1` (dell1; re-seated by `0.0.0_AB_MSTR~DELL1` for the FWD-11 and FWD-9 orders only) |

**Carried lines, updated by the reads that arrived (MSTR msgs 108943, 108948):**
- **FWD-9's outage (05:45-06:00Z):** owner `1.0.0_SA_CTO`. Condition: it names what dell1 HOLDS that another box then takes. C-LEASE (the lease register) stays parked and "the Dells take no vendor lease", so a cell cannot be cut until that is named; the window is booked.
- **FWD-27 read-back:** key login WORKS from the laptop on dell1, dell2 and site Z (printed hostnames `DESKTOP-HK1UU7N`, `DESKTOP-N8RJV0A`, `Opal_Bloomberg`); the verify tool grades `key=MISMATCH` only because `org/devices/DEVICES.json` aliases lack those hostnames (asked of the CTO, msg 108945). `password_arm` reads `KBDINT-NO-PROMPT` on all three. Self-probes from site Z and dell2 read `key=DENIED` because those boxes hold no client key: a vantage gap, not a defect. Muse's key on dell2 is not yet read. Owner `1.0.0_SA_CTO` (the register) then `0.0.0_AB_MSTR~DELL2` (the muse key).
- **S9120: CLOSED as a condition not met.** The dell2 read (MSTR msg 108948): 14 seats, every `claude.exe` has parent `powershell.exe` whose parent is `WindowsTerminal.exe`; 0 of 14 under a transient wrapper. No cell.
- **S9119 (the broker heartbeat writer):** the read did not name a writer (dell2 `liveness.json` has 14 entries, each pid a seat's `server.py`; 14 orphaned `agent-poller.py` run with no liveness line; the original writer's entries for `~CB2`, `~TR2`, `~DELL2` are gone). Owner `0.0.0_AB_MSTR~DELL2`. Condition: a read taken while one of those three seats is live names the writer; until then no cell.

**Amendment (2026-10-13 ~23:0xZ, issuer):** `CT-ac-5`'s window moved to Wed 2026-10-14 14:30-14:45Z (dell1 CTO tick 4 on call 5263, MSTR msg 108977): dell1 has no auto-logon, Andrew's console sign-in after a restart is his act and no auto-logon will be set, so the manager restarts only when he is at the box and otherwise slips to the next hour he is. The 05:15Z and 05:45Z windows are cancelled. FWD-9 is back to PARKED (CTO ruling @79e9c3535b): no order exists for its window.

## Recut 2 (2026-10-14 ~02:5xZ, issuer 2.0.0_SA_COO~C): the foreign-box open-call read for `unblock.py tick --owed-call` (row S9123, CTO-routed from NFRA_DEVPLN round 7)

Authority: a recut covers its affected cells; `unblock.py` is the keep-driving mechanism this project owns, and the CTO routed the one worker-light cell here. No existing cell changes.

| cell | what | serves | risk | workstream / round | issued to |
|---|---|---|---|---|---|
| `CT-ac-6` | `.tools/unblock.py tick --owed-call` reads a call on another box's list through `open-calls.py approval_read` (freshest of the cluster copy, `origin/box/<box>`, the working tree; UNREADABLE never absent), prints the source, keeps this box's own read unchanged; a test with the seams. | FWD-2 | LOCAL | KEEPDRIVE / 1 | `0.9.0_WK_NFRA_CTLPLN~90` |
