# IRPT_ANLREQ round 34, workstream ~G (ENGINE) -- decomposition: the r34 resident under its own names (r34c)

Issuer `2.0.0_SA_COO~G2`, 2026-10-16.

**Input:** CTO msg 9114: the third-form r34 packet (blob `db596c0725`) was not signed because its pre-read (the r34 root absent) and D1 (every S3 key 404) cannot pass: the first attempt's root `/opt/irpt-resident/0485393f3a-r34` and its three S3 objects were KEPT by the rollback (AQ2 msg 9086), and deleting them is an S3 delete that needs Andrew's word. Fix ruled: this release gets its own names, root `0485393f3a-r34c` and keys `...-r34c.*`, with the scripts and the generator emitting them, and the pre-read checking that the r34c names are absent. Rebuild, re-hash, re-packet; the CTO signs the new blob.

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **Only the release's names change.** The tooling commit `bc9f2d0c44` renames the release identity `0485393f3a-r34` to `0485393f3a-r34c` in the scripts generator, the build driver, the packet generator and the verifier; the members, the delta (10 changed, 4 added of 314), the pool and the ledger name `irpt-resident-r34b-20261016` are unchanged. The issuer's trial build: 314 members, builds identical, tar `272d5c54...2ff8`, verifier `ar_g107_checks.py` OK; the four generated scripts carry no `0485393f3a-r34` without the `c`.
- **The first attempt is left exactly as it is** (root, receipt copy, three S3 objects, ledger ROLLED-BACK).

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-118` | the r34c tarball and four host scripts at the pin, record `RESIDENT_R34_BUILD.json` in the worker's folder, stage folder `C:/dev/irpt-release-r34f` | the worker's folder, the order, the channel file | WORLD (nothing installed, no host touched, no AWS call) |
| `AR-g-119` | the yfinance 1.2.0 closure (17 approved wheels) delivered into the resident host's pydeps (applier order `TO-APPLY-YFDEPS`, own pair; CTO msgs 9070, 9075, 9143) | the applier's `deliverables/irpt_anlreq_yfdeps/`, the ledger | WORLD (S3 write, a host folder; no restart) |

## Edges and chains

- TWO chains. `AR-g-118` feeds the signed packet R34D and the AQ2 apply order; `AR-g-119` (the library) is the hard gate of that order (CTO msg 9138): it must close before the r34c apply starts.

## Four-postulate record

(i) Domain: one resident tarball of 314 members. (ii) One pin and one verifier. (iii) One intent. (iv) What this cut does NOT move: any host, S3 object, the first attempt's artifacts, the Lambdas.

fanout: 1 of 1 chains, cap 8, reason: one worker cell (slot 257).
