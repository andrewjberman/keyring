# IRPT_ANLREQ round 49, workstream ~G (ENGINE) -- decomposition: the lease's window count in its OWN row (a rework of AR-g-142 so a rollback to r34g leaves the lease readable)

Issuer `2.0.0_SA_COO~G2`, 2026-10-16.

**Input:** while writing the r34h never-widen packet's rollback section the issuer found a defect in the merged AR-g-142 design (round 47). It stores the per-window call count inside the provider lease row as two extra keys. The r34g resident that runs on the host reads that row with an exact key-set check (`OperationLease._read`), so after r34h writes the keys a rollback to r34g would leave every lease read refusing the row (`OPERATION_STORE_INVALID`), while the rollback script's own checks (running root, queue, member sha) still read green. NEVER-2 requires a same-session rollback that leaves the host working, so the mechanism is reworked before the r34h pair is signed.

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **The count moves to its own store row** (`PROVIDER_OPERATION#<hash of provider, account and "window">`, keys exactly `version`, `window_start`, `window_count`), written after the lease-row swap by the same holder (the lease serialises holders, so the row has no concurrent writer). The lease row keeps exactly its eight keys with or without a budget, and `acquire` needs no carry-over. Still ONE count per host account, shared by every caller (CTO msg 9727).
- **A refusal over the budget writes nothing** (decided inside the lease-row transform, before its swap). **A commit that cannot be written is swallowed**: the call already holds its reservation, so it proceeds; the count is then one short. This fails open on counting, not on spacing or in-flight, and is named in the r34h packet.
- **Cell `AR-g-142` is not reverted**: its public behaviour (the constructor argument, the refusal code and retry_after, the rollover, `ResidentSession(window_budget=)`) stays; only the storage changes. `AR-g-146` rewrites the part of `operation_lease.py` and its tests that AR-g-142 added.
- **r34h waits for this cell**; AR-g-144 (worker 271) does not touch the lease and proceeds.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-146` | the window count in its own row; the lease row back to eight keys; tests rewritten | `ycharts/session/operation_lease.py`, `tests/test_operation_lease.py`, `tests/test_window_budget.py`, the worker's folder | WORLD (infra path; nothing deployed) |

## Edges and chains

- ONE chain, no dependency on AR-g-144. The r34h build needs 142, 143, 144 and 146 merged.

## Four-postulate record

(i) Domain: the lease module's storage of the window count. (ii) One check file (`ar_g146_checks.py`), dry-run against a reference fix and four mutants. (iii) One intent: the same budget with a lease row an older reader still accepts. (iv) What this cut does NOT move: the budget's constructor argument and refusal code, `resident_session.py`, the resolve hop, the bindings, any deployed byte.

fanout: 1 of 1 chains, cap 8, reason: one worker cell (slot 273).
