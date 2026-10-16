# IRPT_ANLREQ round 29, workstream ~G (ENGINE) -- decomposition: the r34 resident rebuilt with the door's yfinance checker

Issuer `2.0.0_SA_COO~G2`, 2026-10-16.

**Input:** CTO msg 8968 (the checker folds into r34 if its D1 has not started; the CTO re-signs). Round 28 merged `AR-g-110` (`3c2c4eb87b`: the door's resolver builds `YfinanceChecker()`); r33 is CLOSED; r34's D1 has not started (the first r34 staged order is superseded). The r34 tooling commit `4aad96b3c0` is the pin: it carries `AR-g-110` and not `AR-g-109` (the hop_failure writers, which ship in r35). The issuer's trial build of that pin: 314 members, 8 changed (`intake/portfolio.py`, `intake/uploads.py`, `ops/status.py`, `reports/resident_bindings.json`, `reports/resident_installed.py`, `ycharts/research/opal_producer.py`, `ycharts/session/resident_session.py`, `SHA256SUMS`), 4 added (`intake/yfinance_check.py`, `ycharts/research/swap_pass.py`, `yahoo_history_days.py`, `swap_pool.json`), builds identical, tar `861e6900...abe8`, verifier `ar_g107_checks.py` OK.

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **The rebuild is one worker cell, BUILD ONLY** (`AR-g-112`), exactly as `AR-g-107` was: the worker runs the committed driver at the pin into a NEW stage folder (`C:/dev/irpt-release-r34b`), and the issuer's verifier recomputes everything and requires the tarball to equal the issuer's own trial build of the same pin.
- **Why a new round and a new folder:** the gate allows one issuance per round and round 28 already holds `AR-g-109` and `AR-g-110`; the first r34 stage folder stays as built (nothing installed from it).

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-112` | the r34 resident tarball and four host scripts rebuilt at `4aad96b3c0`, record `RESIDENT_R34_BUILD.json` in the worker's folder | the worker's folder, the order, the channel file | WORLD (nothing installed, no host touched, no AWS call) |

## Edges and chains

- ONE chain. `AR-g-112` depends on `AR-g-110` (merged) and feeds the re-cut r34 packet, the CTO's re-signature and the AQ2 apply order (`AR-g-108`, re-issued).

## Four-postulate record

(i) Domain: one resident tarball of 314 members. (ii) One pin and one verifier. (iii) One intent. (iv) What this cut does NOT move: any host, the Lambdas, the hop_failure writers, IAM.

fanout: 1 of 1 chains, cap 8, reason: one worker cell (the r34 rebuild, slot 252).
