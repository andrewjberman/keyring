# IRPT_ANLREQ round 50, workstream ~G (ENGINE) -- decomposition: BUILD the r34h resident (the host call budget, the resolve-hop requeue and the YCharts price tier) over the running r34g root

Issuer `2.0.0_SA_COO~G2`, 2026-10-16.

**Input:** rounds 47 to 49 merged: AR-g-142 (the provider lease counts reserved calls per window; `ResidentSession(window_budget=)`), AR-g-143 (the resolve hop re-sends a `:OPERATION_WINDOW_BUDGET` retry like a busy provider), AR-g-144 (the `ycharts` price tier, the `ycharts_window_budget` binding and the stored-session transport) and AR-g-146 (the count in its own store row, so the lease row keeps the eight keys the r34g lease reads and a rollback leaves the host working). CTO msgs 9727, 9757 and 9761: one release under its own pair; the budget is (6 calls, 390 s), a floor counting every securities_info call, set in the bindings; the YCharts use is ordered paced read, 390 s rest, window 4, rest, then the unknown-symbol paced read and the three-unknowns measurement. The paced read is done (12 of 12 clean).

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **The release is built over the RUNNING r34g root.** The delta against the r34g tarball (sha256 `1e5b3ef4...80b`) is exactly six changed members (`SHA256SUMS`, `reports/resident_bindings.json`, `reports/resident_installed.py`, `ycharts/generate/resident_worker.py`, `ycharts/session/operation_lease.py`, `ycharts/session/resident_session.py`) and one added (`ycharts/research/price_transport_ycharts.py`). The bindings differ only in provenance (`package_pin` and the files-from list's count and sha256, which grew by the two members r34h takes from the pin), `opal_pricing` (the `ycharts` tier added, still enabled) and the new key `ycharts_window_budget` = `{"calls": 6, "window_s": 390}`. The build driver refuses on anything else; the verifier recomputes it.
- **The pin is a SCRATCH commit** for the same reason as r34f and r34g: the DASHBD hunk `f25618c0b4` (`lib/trading_calendar.py`) rides only its own pair. The pin `12c5c4f8dac9bb3fac2cfcc1cc68303ad1c75a03` (branch `scratch/r34h-pin`, never merged) is trunk at `9362ed79ac` with that one file at the r34e bytes. The tools are committed (`64a348dc50` and the provenance fix).
- **Names:** root `0485393f3a-r34h`, tarball and sums `irpt-resident-0485393f3a-r34h.*`, ledger `irpt-resident-r34h-20261016`, stage folder `C:/dev/irpt-release-r34r`.
- The issuer's own trial build of the pin (stage `C:/dev/irpt-release-r34q-issuer`): 315 members, changed 6, added 1, removed 0, builds identical 315 of 315, tarball `60cc8d1d68627c993121df7eca946a40046f1d7f63ddfd2968f83e27077b93c0`; the verifier printed AR-G145-OK. The worker's official build must equal it.
- **Rollback** is the r34g root, which stays on the host; the lease row is unchanged by r34h, so the r34g lease keeps reading it.
- **The apply (`AR-g-148`) waits for ~Y2's window 4** (CTO msg 9727 condition 2) and is ordered to IB2 (rule 34) under the signed pair.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-147` | the r34h tarball, sums and four host scripts at the pin, record `RESIDENT_R34H_BUILD.json` in the worker's folder, stage folder `C:/dev/irpt-release-r34r` | the worker's folder, the order, the channel file | WORLD (nothing installed, no host touched, no AWS call) |
| `AR-g-148` | the r34h resident applied to the host under the signed pair (applier order `TO-APPLY-R34H`, own pair), V2 inside the service's own environment with the controls, back-off, door, pricing, budget and tier checks | the applier's `deliverables/`, the ledger `irpt-resident-r34h-20261016` | WORLD (S3 write, a host root, a restart; rollback the r34g root) |

## Edges and chains

- ONE chain: `AR-g-147` (the build) feeds the signed packet and `AR-g-148` (the apply, after window 4).

## Four-postulate record

(i) Domain: one resident tarball of 315 members. (ii) One pin and one verifier. (iii) One intent: ship the host call budget and the YCharts price tier. (iv) What this cut does NOT move: any host, S3 object, the r34c to r34g artifacts, the Lambdas, the DASHBD calendar hunk, the unknown-symbol read and the three-unknowns measurement.

fanout: 1 of 1 chains, cap 8, reason: one worker cell (slot 274); the apply cell AR-g-148 is the issuer's applier order, not a worker cell.
