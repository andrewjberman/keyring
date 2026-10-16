# IRPT_ANLREQ round 52, workstream ~G (ENGINE) -- decomposition: the YCharts price tier's query form (r34i)

Issuer `2.0.0_SA_COO~G2`, 2026-10-16.

**Input:** r34h applied and verified (ledger `irpt-resident-r34h-20261016` CLOSED; three S3 objects equal by hash). IB2's two reads on r34h (records `UNKNOWN_READ.txt` @03768568b7, `PRICE_PROBE.txt` @994446e4c5): the budget (6 calls, 390 s) holds, a challenge came at call 7; the price tier's query `securities=id:<TICKER>,include:true,&zoom=max` is refused HTTP 400 text/plain, signed in AND signed out, for SPY and AAPL (INFERRED: the form is wrong, not the session). CTO msg 9991 RULED: the tier stays unused (condition 1 reads failed); find the form the working recipe path uses (read-only, repo first); cut r34i with that form, or with the tiers back to [estate, yfinance] if none exists.

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **The form exists in the repo.** The CRO's captured map `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json`, call `benchmark_level_series`, is a working one-security series call: `GET /charts/fund_data.json` with `securities=id:^SPXTR,include:true,,` (note the DOUBLE trailing comma), `calcs=id:level,include:true,,`, `zoom=max`, `maxPoints=100000`, `partner=basic_2000` (and a start/end window). The tier's adapter sends neither `calcs`, the second comma, `maxPoints` nor `partner`. The adapter's own docstring says the answer is a cumulative level, which is what `calcs=id:level` asks for.
- **Measure before building around it (AR-g-151).** One read-only script, `ycharts_price_probe2.sh` (@5b3d245789, 19 offline cases): A1 signed-in `id:SPY` in the recipe form; if it answers rows the existing reader parses, A2 `id:AAPL` and A3 the SIGNED-OUT `id:SPY`; only if A1 is refused or empty, B1 a sessionless lookup of SPY's typed id, then B2 and B3 with it. At most four requests under the root's budget. It answers the CTO's three unknowns with the right form.
- **The build is the form change (AR-g-152).** The adapter sends the recipe form with the plain ticker (the likeliest outcome of A1); the tier's other behaviour (one call per symbol, errors propagate, the tiers list and the budget) does not move. If the read says the plain ticker is refused and the typed id works (branch B), the cell is recut: the tier then costs two calls per symbol (lookup plus series), which the budget (3 symbols per window) must be told. If neither works, r34i sets the tiers back to [estate, yfinance] (CTO ruling 3).
- **Not in this cut:** the budget number, FWD-7's Opal-built report path (price pages are Andrew's hold, C-V1; CTO msg 9923), the classifier.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-151` | the recipe-form read run once on r34h; output verbatim in `RECIPE_FORM_READ.txt` | the applier's `deliverables/` | WORLD (up to four outbound calls to the provider from the production host) |
| `AR-g-152` | `price_adapter_ycharts.py` sends the recipe form; its three tests move with it | `ycharts/research/price_adapter_ycharts.py` and its tests | LOCAL (code and tests; the release is a later cell) |

## Edges and chains

- Two chains: `AR-g-151` (the read) and `AR-g-152` (the code) do not depend on each other for their first version. The release (r34i build, packet, signatures, apply) follows both and is cut after them.

## Four-postulate record

(i) Domain: one adapter, one query form, the three unknowns. (ii) One grain: a request. (iii) One intent: make the price tier's first call a call YCharts answers. (iv) What this cut does NOT move: the budget, the lease, the tiers list, the transport, the door.

fanout: 1 of 2 chains, cap 8, reason: AR-g-152 is the one worker cell; AR-g-151 is the issuer's applier order to IB2 (rule 34), not a worker cell.
