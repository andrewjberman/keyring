# IRPT_ANLREQ round 45, workstream ~G (ENGINE) -- decomposition: BUILD the r34g resident (the door asks yfinance first, opal_pricing ON) over the running r34f root

Issuer `2.0.0_SA_COO~G2`, 2026-10-16.

**Input:** round 44 merged AR-g-133 (`c99d9e5269`, worker 265; the issuer re-ran build, guard and regress and read the diff) and AR-g-134 (`1180b2f0b1`, worker 266, the YCharts-id trace). CTO msgs 9600 and 9620: r34g carries PRD v0.22 items 1 and 2 (the door asks yfinance first; `opal_pricing` ON); item 3 is met by naming the remaining YCharts calls (8 to 9 per report; 0 at the door when every holding is kept); item 4 (the lease count per window) ships later, after the CRO's paced read. The release is NOT installed while run 3 is pinned to r34f and its window is open or about to open.

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **The release is built over the RUNNING r34f root.** The delta against the r34f tarball (sha256 `0d223e50...a3f`) is exactly three members: `SHA256SUMS`, `reports/resident_bindings.json` (only `provenance.package_pin` and `opal_pricing` false -> true differ) and `intake/security_resolution.py`. The build driver refuses on anything else; the verifier recomputes it. The AR-g-134 trace needs no removal cell in this release (CTO msg 9620), so `AR-g-135` is not cut.
- **The pin is a SCRATCH commit** for the same reason as r34f: the DASHBD hunk `f25618c0b4` (`lib/trading_calendar.py`) rides only its own pair (CTO msg 9571). The pin `cd48501d0d4022fa4aa1eb5611cdf4133876fa60` (branch `scratch/r34g-pin`, never merged) is trunk at `252cc5b1bd` with that one file put back to the r34e bytes. The tools are committed at `60e07baf51`.
- **Names:** root `0485393f3a-r34g`, tarball and sums `irpt-resident-0485393f3a-r34g.*`, ledger `irpt-resident-r34g-20261016`, stage folder `C:/dev/irpt-release-r34m`.
- The issuer's own trial build of the pin (stage `C:/dev/irpt-release-r34l-issuer`): 314 members, changed 3, added 0, removed 0, builds identical 314 of 314, tarball `1e5b3ef4120b8799ebd5f1cf620044b01b5e1bfeac2e1d4169d3f576a802580b`; the verifier printed AR-G137-OK. The worker's official build must equal it.
- **Rollback** is the r34f root, which stays on the host.
- **The apply (`AR-g-139`) is held** behind run 3 (CTO msg 9600). The CTO half of the packet is asked for now; the GO to the applier (IB2, rule 34) waits on ~Y2's word that run 3's window has closed.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-138` | the r34g tarball, sums and four host scripts at the pin, record `RESIDENT_R34G_BUILD.json` in the worker's folder, stage folder `C:/dev/irpt-release-r34m` | the worker's folder, the order, the channel file | WORLD (nothing installed, no host touched, no AWS call) |
| `AR-g-139` | the r34g resident applied to the host under the signed pair (applier order `TO-APPLY-R34G`, own pair), V2 inside the service's own environment with the four controls, the back-off, the door and the pricing checks | the applier's `deliverables/`, the ledger `irpt-resident-r34g-20261016` | WORLD (S3 write, a host root, a restart; rollback the r34f root) |

## Edges and chains

- ONE chain: `AR-g-138` (the build) feeds the signed packet and `AR-g-139` (the apply, held behind run 3).

## Four-postulate record

(i) Domain: one resident tarball of 314 members. (ii) One pin and one verifier. (iii) One intent: ship the yfinance-first door and the pricing binding. (iv) What this cut does NOT move: any host, S3 object, the r34c to r34f artifacts, the Lambdas, the DASHBD calendar hunk, the lease.

fanout: 1 of 1 chains, cap 8, reason: one worker cell (slot 267); the apply cell AR-g-139 is the issuer's applier order, not a worker cell.
