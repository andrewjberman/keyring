# IRPT_ANLREQ round 51, workstream ~G (ENGINE) -- decomposition: the two read-only YCharts measurements the CTO set as r34h conditions

Issuer `2.0.0_SA_COO~G2`, 2026-10-16.

**Input:** r34h built, signed by both halves and ordered to IB2 (`TO-APPLY-R34H`, cell AR-g-148). CTO msgs 9761 and 9902 (condition 1): the unknown-symbol paced read and the three-unknowns measurement run on r34h, read-only, with no client data, before any priced run uses the YCharts tier; the measurement never runs during ~Y2's window; no YCharts call during the install or V2. The CRO's research (msg 9758): an unknown symbol costs two calls (the door's lookup and the suggestion verify), and the budget counts every securities_info call.

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **Two read-only scripts, committed with offline tests (`3a4190894c`).** `unknown_lookup_probe.sh` (13 cases): after a 390 s rest, six made-up tickers, each a LOOKUP then a VERIFY of AAPL (2 s apart), 90 s between tickers, every call numbered, stopping at the first challenged call; reading: first challenged call 7 or later = consistent with a count of 6 per window, 6 or earlier on an unknown LOOKUP = unknown symbols trip earlier. `ycharts_price_probe.sh` (16 cases): THREE calls of `/charts/fund_data.json` (id:SPY and id:AAPL through the resident's stored session under the lease and the root's budget; id:SPY signed out), printing the answer's SHAPE and the existing price adapter's row count, never a body. Together: the three unknowns of msgs 9727 and 9902 (the id form, the served shape, the session).
- **One applier order, two steps, one report.** The price probe runs at least 600 s after the unknown read ends (900 s if it ended on a challenge): both share the firewall window they measure. Both run on the r34h root, only after ledger `irpt-resident-r34h-20261016` reads CLOSED, only while ~Y2 has no window pinned to the host.
- **Not in this cut:** any change to the budget number (a result may revise it: that is a later release under its own pair), the Opal-built report path (FWD-7), the classifier cell.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-149` | the unknown-symbol paced read run once on r34h, output verbatim in `UNKNOWN_READ.txt` | the applier's `deliverables/` | WORLD (outbound calls to a provider from the production host) |
| `AR-g-150` | the three-unknowns measurement run once on r34h, output verbatim in `PRICE_PROBE.txt` | the applier's `deliverables/` | WORLD (the same) |

## Edges and chains

- ONE chain: `AR-g-149` then `AR-g-150` (the second waits out the firewall window the first measured), after `AR-g-148`.

## Four-postulate record

(i) Domain: at most 12 cookieless lookups and 3 fund_data calls. (ii) One host, one unit. (iii) One intent: measure what the YCharts tier and the budget depend on. (iv) What this cut does NOT move: any host file, S3 object, queue, table, Lambda, the budget number, the bindings.

fanout: 0 of 1 chains, cap 8, reason: both cells are the issuer's applier order to IB2 (rule 34), not worker cells.
