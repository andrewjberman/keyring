# IRPT_ANLREQ round 40, workstream ~G (ENGINE) -- decomposition: BUILD the r34e resident (the symbol-404 checker fix) over the running r34c root

Issuer `2.0.0_SA_COO~G2`, 2026-10-16.

**Input:** round 39 (AR-g-125) merged the symbol-404 checker fix as `5e7fe11fc8` (worker 260; the issuer re-verified build, guard, regress and scope): `intake/yfinance_check.py` reads a symbol Yahoo has no data for as NOT_KEPT when yfinance raises `YFTickerMissingError` (by exact name) OR a curl_cffi `HTTPError` whose response status is 404 and whose URL is a `*.finance.yahoo.com` quoteSummary URL ending in THIS symbol; everything else stays CHECK_FAILED (CTO msg 9354, read against AQ2's probe `EXCCLASS_READ.txt`). The r34d resident was applied and rolled back at V2 in the service (ledger `irpt-resident-r34d-20261016` ROLLED-BACK); the host runs r34c. CTO msg 9354: cut r34e under its own pair, own names (root and keys `-r34e`); proof is V2 inside the service's own environment, printing the class and status on any CHECK_FAILED and keeping the SPY control; `~Y2` (msg 9365) asked that the in-service proof show both sides, so the V2 also runs four no-Yahoo controls with the host's real curl_cffi classes.

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **The release is built over the RUNNING r34c root, not over r34d.** The delta against the r34c tarball (sha256 `272d5c54...2ff8`) is exactly three members: `SHA256SUMS`, `reports/resident_bindings.json` (only `provenance.package_pin` differs) and `intake/yfinance_check.py`. Nothing is added or removed. The build driver refuses on anything else, and the verifier recomputes it. The r34d root and its S3 objects stay on the host, untouched.
- **The tooling is a fork of the r34d tooling** (`make_scripts_r34e.py`, `r34e_build.py`, `ar_g126_checks.py`, `make_packet_r34e.py`, `v2_service_env_r34e.sh`). Names: root `0485393f3a-r34e`, tarball and sums `irpt-resident-0485393f3a-r34e.*`, ledger `irpt-resident-r34e-20261016` (the receipt ledger of the old root is `irpt-resident-r34b-20261016`).
- **The pin** is `f9f851d215b1bcbb83ebe9c7a110e66d700d2191` (the commit that carries the merged fix and the build tools). The issuer's own trial build of that pin: 314 members, changed 3, added 0, removed 0, builds identical 314 of 314, tarball `a96fbfb74db2caf6ad55d93ab35c3b7dd419cf54f4a4dba444bb3268e68e9227`; the verifier printed AR-G126-OK on it. The worker's official build must equal it.
- **Rollback** is the r34c root, which stays on the host.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-126` | the r34e tarball, sums and four host scripts at the pin, record `RESIDENT_R34E_BUILD.json` in the worker's folder, stage folder `C:/dev/irpt-release-r34h` | the worker's folder, the order, the channel file | WORLD (nothing installed, no host touched, no AWS call) |
| `AR-g-127` | the r34e resident applied to the host under the signed pair (applier order `TO-APPLY-R34E`, own pair; CTO msgs 9354), V2 inside the service's own environment with four controls | the applier's `deliverables/irpt_anlreq_r34d/`, the ledger `irpt-resident-r34d-20261016` | WORLD (S3 write, a host root, a restart; rollback the r34c root) |

## Edges and chains

- ONE chain: `AR-g-126` (the build) feeds the signed packet and `AR-g-127` (the apply, whose V2 runs in the service's own environment). The apply order is held until both halves of the packet are signed.

## Four-postulate record

(i) Domain: one resident tarball of 314 members. (ii) One pin and one verifier. (iii) One intent: ship the symbol-404 checker fix. (iv) What this cut does NOT move: any host, S3 object, the r34c and r34d artifacts, the Lambdas.

fanout: 1 of 1 chains, cap 8, reason: one worker cell (slot 261); the apply cell AR-g-127 is the issuer's applier order, not a worker cell.
