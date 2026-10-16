# IRPT_ANLREQ round 37, workstream ~G (ENGINE) -- decomposition: BUILD the r34d resident (the checker fix) over the running r34c root

Issuer `2.0.0_SA_COO~G2`, 2026-10-16.

**Input:** round 36 (AR-g-121) merged the checker fix as `b535f41cb8`: `intake/yfinance_check.py` reads a `YFTickerMissingError` (exact class name in the MRO) as no rows, so an unknown symbol is NOT_KEPT and never CHECK_FAILED; every other exception stays CHECK_FAILED (CTO msg 9291). The resident that serves the door runs r34c, which carries the pre-fix bytes. CTO msg 9291: cut r34d under its own pair, with its own names (root and keys `-r34d`); proof is a V2 run in the service's own environment with SPY KEPT and ZQXWVK NOT_KEPT.

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **The release is built over the RUNNING r34c root, not over r32.** The delta against the r34c tarball (sha256 `272d5c54...2ff8`) is exactly three members: `SHA256SUMS`, `reports/resident_bindings.json` (only `provenance.package_pin` differs) and `intake/yfinance_check.py`. Nothing is added or removed. The build driver refuses on anything else, and the verifier recomputes it.
- **The tooling is a fork** (`make_scripts_r34d.py`, `r34d_build.py`, `ar_g122_checks.py`), so the signed r34c generation stays reproducible. Names: root `0485393f3a-r34d`, tarball and sums `irpt-resident-0485393f3a-r34d.*`, ledger `irpt-resident-r34d-20261016` (the receipt ledger of the old root is `irpt-resident-r34b-20261016`).
- **The pin** is `11e0751415c1e811bffd0381d24a7c890ad1f33d` (the commit that carries the merged fix, the forked tooling and the verifier). The issuer's own trial build of that pin: 314 members, changed 3, added 0, removed 0, builds identical 314 of 314, tarball `9a088a5cfdeecd84173ee85b82d93ecf2b6fdfa311d3aec982e7db7134cf78ab`; the verifier printed AR-G122-OK on it. The worker's official build must equal it.
- **Rollback** is the r34c root, which stays on the host.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-122` | the r34d tarball, sums and four host scripts at the pin, record `RESIDENT_R34D_BUILD.json` in the worker's folder, stage folder `C:/dev/irpt-release-r34g` | the worker's folder, the order, the channel file | WORLD (nothing installed, no host touched, no AWS call) |
| `AR-g-123` | the r34d resident applied to the host under the signed pair (applier order `TO-APPLY-R34D`, own pair; CTO msg 9291), V2 inside the service's own environment | the applier's `deliverables/irpt_anlreq_r34d/`, the ledger `irpt-resident-r34d-20261016` | WORLD (S3 write, a host root, a restart; rollback the r34c root) |

## Edges and chains

- ONE chain: `AR-g-122` (the build) feeds the signed packet and `AR-g-123` (the apply, whose V2 runs in the service's own environment). The apply order is held until both halves of the packet are signed.

## Four-postulate record

(i) Domain: one resident tarball of 314 members. (ii) One pin and one verifier. (iii) One intent: ship the checker fix. (iv) What this cut does NOT move: any host, S3 object, the r34c artifacts, the Lambdas.

fanout: 1 of 1 chains, cap 8, reason: one worker cell (slot 259); the apply cell AR-g-123 is the issuer's applier order, not a worker cell.
