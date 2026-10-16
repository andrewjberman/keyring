# IRPT_ANLREQ round 27, workstream ~G (ENGINE) -- decomposition: the release-33 apply and the release-34 resident build

Issuer `2.0.0_SA_COO~G2`, 2026-10-16.

**Input:** CTO msg 8863 (the r33 CTO half SIGNED at packet blob `6a8a30a5a5`, applier `0.7.0_AE_CloudOps~AQ2`, `irpt-status` first, then `irpt-ycharts-generate`) and the standing sequence r33, then r34 (resident: the swap pass and the dated pool snapshot, own pair), then FWD-1 run 3. Round 26 delivered the r33 build (`AR-g-103`, merged `9d99b510a5`, verifier `AR-G103-OK`) and the pool snapshot (`AR-g-106`, `dcdc6cb3d1`).

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **The r33 apply is ONE applier order with the two ledgers in the pair's sequence** (`irpt-status` apply and V-read, then `irpt-ycharts-generate`), because the CTO half orders the sequence and the CVO single-executor rule makes each artifact group one executor; the order is the issuer's cell `AR-g-104` (not a worker cell).
- **The r34 build is a worker cell** (`AR-g-107`, BUILD ONLY, like `AR-g-92`): the tooling is committed (`78f2c2a9c3`: builder with `--opal-swap-pool`, packer, clock wrapper, script generator, files-from list, driver `r34_build.py`) and the issuer's trial build at that commit gave 313 members, 7 changed, 3 added, 0 removed, builds identical, tar `b6986b68...f263`. The verifier `ar_g107_checks.py` recomputes all of it and requires the tarball to equal the issuer's own trial build of the same pin.
- **The r34 pin is the tooling commit** `78f2c2a9c3a9be8f88d82ddfd6a6e997ee0bed58`: the tools on disk must equal the tools at the pin (the driver refuses otherwise), and no resident-relevant product file has changed since the swap-pool binding merge (`8e55b664bb`).

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-104` | the AQ2 apply order for r33 (two code releases, one env var, one inline policy) and its after-reads | the applier's `deliverables/irpt_anlreq_r33/`, the ledgers, the map record | WORLD (a deploy under a signed pair) |
| `AR-g-107` | the r34 resident tarball, four host scripts and the build record `RESIDENT_R34_BUILD.json` in a stage folder outside the repo | the worker's `deliverables` folder, the order, the channel file | WORLD (floor of an infrastructure path; nothing installed, no host touched, no AWS call) |
| `AR-g-108` | the AQ2 apply order for the r34 resident (install, census, one-ticker Yahoo read), cut after both halves of the r34 pair were signed (CTO msg 8904); it starts only after both r33 ledgers close | the applier's `deliverables/irpt_anlreq_r34/`, the ledger | WORLD (a deploy under a signed pair) |

## Edges and chains

- THREE cells, TWO independent chains and one gated edge: `AR-g-108` depends on `AR-g-104` closing (CTO condition 1) and on `AR-g-107` (merged). `AR-g-104` depends on the signed pair (done). `AR-g-107` depends on `AR-g-98`, `AR-g-101` and `AR-g-106` (all merged) and feeds the r34 packet; the r34 apply order depends on the r34 pair.

## Four-postulate record

(i) Domain: two Lambda releases; one resident tarball of 313 members. (ii) One pin and one verifier per build. (iii) One intent per cell. (iv) What this cut does NOT move: the host, the routes, the queues, the classifier, any vendor call.

fanout: 1 of 2 chains, cap 8, reason: one worker cell (the r34 build, slot 225); the other chain (AR-g-104) is an applier order to `0.7.0_AE_CloudOps~AQ2`, not a worker.
