# IRPT_ANLREQ round 43, workstream ~G (ENGINE) -- decomposition: BUILD the r34f resident (the resolve hop's WAF back-off) over the running r34e root

Issuer `2.0.0_SA_COO~G2`, 2026-10-16.

**Input:** round 42 (AR-g-129) merged the back-off as `53c40793dd` (worker 263; the issuer re-verified build, guard, regress and scope): `ycharts/generate/resident_worker.py` releases a resolve-hop RETRY whose code ends `:WAF_CHALLENGE` for 150, 300, 450 s at receives 1, 2, 3 (900 s = the CTO's cap, under `REDRIVE_SECONDS` 960 and the queue's maxReceiveCount 5); every other cause keeps 60 s; the journal names the delay (CTO msgs 9429, 9447; design `WAF_BACKOFF_DESIGN_20261016.md`). The host runs r34e (ledger `irpt-resident-r34e-20261016` CLOSED). Run 3 stays HELD until this release is live or a clean SET 3 window is measured.

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **The release is built over the RUNNING r34e root.** The delta against the r34e tarball (sha256 `a96fbfb7...9227`) is exactly three members: `SHA256SUMS`, `reports/resident_bindings.json` (only `provenance.package_pin` differs) and `ycharts/generate/resident_worker.py`. The build driver refuses on anything else; the verifier recomputes it. The r34e root stays on the host (the rollback).
- **The pin is a SCRATCH commit.** `a23b898c9c` (tools plus the merged change) made the first trial build refuse: `lib/trading_calendar.py` also differed from r34e, because the IRPT_DASHBD hunk `f25618c0b4` (one business_date for all three firms, +14 lines) landed on the branch after r34e was built. That hunk is not part of this cut and has no CTO half here. The pin is therefore `a81abf691f3af84fdde5ee1cf2c0dafc2b2966ed` (branch `scratch/r34f-pin`, never merged): `a23b898c9c` with `lib/trading_calendar.py` put back to the r34e bytes (`5e7fe11fc8`). Its other files are those of `a23b898c9c`. The hunk ships in a later release under its own pair. The packet names this.
- **Names:** root `0485393f3a-r34f`, tarball and sums `irpt-resident-0485393f3a-r34f.*`, ledger `irpt-resident-r34f-20261016`, stage folder `C:/dev/irpt-release-r34i`.
- The issuer's own trial build of the pin (stage `C:/dev/irpt-release-r34j-issuer`): 314 members, changed 3, added 0, removed 0, builds identical 314 of 314, tarball `0d223e500a92aa274bbb52437d33657dd870b9f29af41ec942463c936d904a3f`; the verifier printed AR-G130-OK. The worker's official build must equal it.
- **Rollback** is the r34e root, which stays on the host.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-131` | the r34f tarball, sums and four host scripts at the pin, record `RESIDENT_R34F_BUILD.json` in the worker's folder, stage folder `C:/dev/irpt-release-r34i` | the worker's folder, the order, the channel file | WORLD (nothing installed, no host touched, no AWS call) |
| `AR-g-132` | the r34f resident applied under the signed pair (applier order `TO-APPLY-R34F`, own pair), V2 inside the service's own environment with the four controls plus the back-off check | the applier's `deliverables/`, the ledger `irpt-resident-r34f-20261016` | WORLD (S3 write, a host root, a restart; rollback the r34e root) |

## Edges and chains

- ONE chain: `AR-g-131` (the build) feeds the signed packet and `AR-g-132` (the apply). The apply order is held until both halves of the packet are signed.

## Four-postulate record

(i) Domain: one resident tarball of 314 members. (ii) One pin and one verifier. (iii) One intent: ship the WAF back-off. (iv) What this cut does NOT move: any host, S3 object, the r34c to r34e artifacts, the Lambdas, the DASHBD calendar hunk.

fanout: 1 of 1 chains, cap 8, reason: one worker cell (slot 264); the apply cell AR-g-132 is the issuer's applier order, not a worker cell.
