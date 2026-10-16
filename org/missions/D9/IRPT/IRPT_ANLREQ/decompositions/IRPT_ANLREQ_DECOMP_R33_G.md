# IRPT_ANLREQ round 33, workstream ~G (ENGINE) -- decomposition: the r34 resident rebuilt a third time, with the hop_failure writers folded in

Issuer `2.0.0_SA_COO~G2`, 2026-10-16.

**Input:** AQ2 installed the rebuilt r34 (`AR-g-112`) and stopped at V2 (msg 9066: no `yfinance` on the host); the CTO ruled it rolled back (msg 9070) and the host reads r32 again (AQ2 msg 9085, ledger `irpt-resident-r34-20261016` ROLLED-BACK). The library (yfinance 1.2.0 and its Linux closure) is delivered through the intake route under its own pair (CTO msg 9075; call `XB-20261016T052534Z-983c` to `2.0.0_SA_COO~C`, acked); r34 is re-applied afterwards on a signed packet.

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **The re-apply carries the C-HOP-FAILURE resident writers (`AR-g-109`, merged `bc0e7e96c4`) instead of a second install cycle later.** The delivery of the library takes time, the packet must be re-signed anyway (a new pin), and the writers are dormant until the `irpt-status` reader (`AR-g-115`, built and merged) is applied. Their blast radius is two single-attribute writes to the job row (packet section 2d) and one added read (V3: the simulator on `UpdateItem` for the host role).
- **Files-from gains `durable_job.py`; the delta is 10 changed, 4 added of 314** (the 8/4 of `AR-g-112` plus `durable_job.py` and `resident_worker.py`). A NEW ledger name (`irpt-resident-r34b-20261016`) because the first attempt's ledger is closed.
- **Pin `c43f8fc13a950dd031f2c5c79a7ab0e11d730fd0`** (the tooling commit). The issuer's trial build: 314 members, builds identical, tar `56410a26...f725`, verifier `ar_g107_checks.py` OK.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-116` | the resident tarball and four host scripts rebuilt at the pin, record `RESIDENT_R34_BUILD.json` in the worker's folder, stage folder `C:/dev/irpt-release-r34d` | the worker's folder, the order, the channel file | WORLD (nothing installed, no host touched, no AWS call) |

## Edges and chains

- ONE chain. Depends on `AR-g-109` and `AR-g-110` (merged). Feeds the re-cut r34 packet, the CTO's re-signature, the library packet and the AQ2 apply order (`AR-g-108`, re-issued after the library is installed).

## Four-postulate record

(i) Domain: one resident tarball of 314 members. (ii) One pin and one verifier. (iii) One intent. (iv) What this cut does NOT move: any host, the Lambdas, IAM, the commentary writer, the classifier.

fanout: 1 of 1 chains, cap 8, reason: one worker cell (slot 256).
