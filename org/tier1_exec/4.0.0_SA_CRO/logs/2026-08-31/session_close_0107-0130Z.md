# Recovery, W4-COX Card 7 Certification, and D11 Wind-Down - 4.0.0_SA_CRO~X
**archetype:** MIXED
**Date:** 2026-08-31
**Task Order:** Ad-hoc D11 wind-down
**Status:** COMPLETE

---

## Objective

Recover the exact `4.0.0_SA_CRO~X` Codex seat, consume and act on its canonical inbox, independently validate W4-COX card 7, preserve the resulting joint and issuer state, and execute Andrew's direct instruction to record the seat log before the D11 fabric is wound down.

## Compiler Tools

| Tool | Command / Use | Result | Note |
|---|---|---|---|
| `comp-which` | Asked for the canonical validation route | PARTIAL | It did not identify the current substrate-card checker route. |
| Current substrate-card checker | Applied to the exact committed card-7 blob | PASS | All 7 of 7 checks passed against the candidate tree. |
| `git cat-file blob` | Extracted the exact Git object as raw bytes | PASS | Produced the authoritative 16,498-byte object and matching SHA-256. |
| `codex-seat-status.ps1` | Measured exact-seat readiness | PASS | The full 9-check conjunction was green. |

What worked: exact-object inspection with `git cat-file blob`, the repository's current checker, live AWS observations, and the canonical Codex seat-status oracle produced reproducible evidence.

What failed: piping `git archive` through PowerShell transformed the binary stream and produced a false 16,634-byte artifact; Git Bash also interpreted the Windows drive prefix as a remote-style path. Neither result was used for certification.

Gap found: `comp-which` did not route this substrate-card validation, and the attempted PowerShell archive pipeline was not byte-safe for exact-object custody. The successful fallback was repository-local raw Git object extraction.

## Work Completed

1. Recovered and loaded the exact seat `4.0.0_SA_CRO~X` through the repository-local Codex startup contract.
   - Re-derived identity with `codex-seat-load.py` and measured readiness with `codex-seat-status.ps1`.
   - Corrected the ignored runtime session-serial file from a stale MSTR value to the exact CRO serial.
   - Left the launcher-owned heartbeat, turn bridge, detector, and TUI lifecycle intact; no duplicate helper was started.
   - Read and acted on the accumulated exact-seat root inbox in message order.

2. Independently validated W4-COX card 7 at candidate `47954ef3de`.
   - Card blob: `59cf3e436f67aca8c4e2c430188ea335ea0dd3ff`.
   - Card size: 16,498 bytes.
   - Card SHA-256: `bdd4e3afa7a77edc325080cec0dc2b5638eaff01d183b0ab261517881fb3b445`.
   - Builder blob: `07f8ff6a8f2a646b1429a86cc25abd51501e16ba`.
   - Current Rule-3 checker: 7 of 7 valid.
   - Live S3 observation: 9 objects, 550,227 bytes, 2 data plus 7 metadata objects, 2 write-days, first write `2026-07-16T13:22:36Z`, last write `2026-07-17T18:11:09Z`, and heartbeat at the same final timestamp with 132 bytes.
   - KeyCount behavior was observed both with and without the projection: `0` with the field present under projection, and no field without projection. A nonexistent bucket and the simulated exact-code full response both refused with return code 255.
   - Trigger-name census found 140 EventBridge rules with 0 `ms_heat` names and 4 `globgrph` controls; Scheduler had 18 schedules with 0 `ms_heat` names and 1 `globgrph` control. Targets and payloads were not measured, so no cadence claim was made.
   - Sent an evidence-backed CRO CARD PASS to CloudOps, CVO, and COO.

3. Recorded the joint and issuer disposition.
   - CVO acknowledged the independent CRO CARD PASS.
   - COO advanced W4-COX from 6 to 7 of 7 cells and closed card 7 at `47954ef3de`.
   - The previous three STOPPED history pins remain stopped.
   - The face proof is unblocked but unstarted; face status remains pending and class close is not due.
   - The denominator remains explicit: 7 of 7 cells within 12 wave-4 REMOTE total, with 5 double-carded elsewhere. No bare 7 of 7 class-close claim was made.

4. Re-derived the card artifact under Addendum 1w Amendment 5 at `e41ede0180`, which requires a correction to be treated as a new census.
   - SET: exact committed card blob `59cf3e436f67aca8c4e2c430188ea335ea0dd3ff`.
   - LEAF UNIVERSE: all 16,498 committed bytes.
   - EXCLUSION: none.
   - MATCH TARGET: Git blob identity, byte length, and SHA-256 listed above.
   - The raw `git cat-file blob` result matched all targets, superseding the transformed archive-pipeline artifact.

5. Executed Andrew's direct D11 wind-down order as relayed by CTO.
   - Recorded this `/log` under the exact seat author.
   - Prepared the required one-line report naming the commit and measured push state.
   - Did not deregister the seat, kill watchers, close the face, advance the count, close the class, change gates, touch `~Y`, or wind down MSTR.

## Decisions

| Decision | Rationale |
|---|---|
| Certify only candidate `47954ef3de` | The CRO decision rests on independently reproduced exact-object and live evidence, not an inherited CVO result. |
| Preserve pending face and class state | The issuer closed the cell card only; the face remains unstarted and class close is not due. |
| Treat the transformed extraction as a failed census | Amendment 5 requires a corrected figure to be fully re-derived under the same declared census parameters. |
| Leave launcher-owned runtime helpers intact | The wind-down order requested `/log` and a landing report, not runtime teardown or deregistration. |
| Report local commit state precisely | Repository history states that origin/CLOUD is integrator-owned; no unauthorized push was attempted. |

## Files Modified

- `org/tier1_exec/4.0.0_SA_CRO/logs/2026-08-31/session_close_0107-0130Z.md` - Yes, committed by this close operation.
- Ignored runtime session-serial state - No repository commit; corrected locally to the exact seat during recovery.

## Blockers

None.

## Current State

- Exact seat: `4.0.0_SA_CRO~X`.
- Runtime readiness: measured green on the full 9-check conjunction before wind-down logging.
- W4-COX card 7: jointly certified and closed at `47954ef3de`.
- W4-COX cells: 7 of 7, within a denominator of 12 wave-4 REMOTE instances.
- Face proof: unblocked, unstarted, and pending.
- Class close: not due.
- v3.1 emitter: dormant.
- HALTGT shape (a): queued behind face close and not started.
- D11 wind-down act authorized here: log and report only.

## Next Steps

1. `[1.0.0_SA_CTO~X]` Receive the exact log commit and measured push state, then proceed with the fabric-level log/handoff only after all required seat logs are in.
2. `[0.7.0_AE_CloudOps~X]` Preserve the unstarted pending face state absent a new explicit GO.
3. `[4.0.0_SA_CRO~X]` Take no additional wind-down action; leave launcher-owned runtime helpers and all preserved gates unchanged.
