# IRPT_ANLREQ round 9, workstream ~G (ENGINE) -- decomposition: the first wave on the round-7 and round-8 reads (the portfolio series, the price-adapter facts, the repair of the round-7 modules)

Issuer `2.0.0_SA_COO~G2`, 2026-10-15.

**Input:** the five drained cells of rounds 7 and 8 and their records: `AR-g-51` (price chain core, merged `e8f1f82f2b`), `AR-g-52` (replacement rule, `35cdaff302`), `AR-g-53` (C-SWITCH design read,
`286f7c048d`), `AR-g-54` (engine compose and variants read, `684ad06f1b`) and `AR-g-55` (the door's UNRESOLVED path read, `e9c9bdf1f0`). CTO msg 8377 (four lanes), PRD v0.15.

## What the reads decided (ruled by the issuer, inside this workstream's decomposition)

- **C-SWITCH (AR-g-53):** placement A. The accept step stamps a server-owned `ticket_confirmed` after one `GetItem` on the ticket table, under the rule: the item exists, `ticket_type`
  is `analysis_request`, `source` starts `dashboard_form:`, and `requester.email` equals the accepted `owner.principal_id`. `producer_for` then also admits `ticket_confirmed is True`. The grant
  (generate role, `generate.tf`) is a NEW widening: a CloudOps act under a never-widen pair with the CTO's half. Source first; it fails closed to the YCharts path while the stamp is absent.
- **Compose and variants (AR-g-54):** the priced Overview reads ONE `[epoch_ms, level]` series per figure; no estate store holds a portfolio series, so it is built from the holdings' price
  rows by buy-and-hold (cell `AR-g-63`). `opal_producer._opal_map` empties the map's calls, which would make every call-sourced element OUTSIDE_BUDGET under pricing. The Comparison and
  Multi-Comp requests render an Overview today. The MDPF_DEMQUE store is NOT readable by the resident (no grant); the Bloomberg history is.
- **The door (AR-g-55):** the filer's Keep is the equal pair `{TICKER_NOT_FOUND, from == to}`; the server accepts it only for that code and files the row as `UNRESOLVED` (no provider receipt).
  The vendor path (`normalized_input.py`) must refuse it (its bare subscript raises a TypeError: armed row `W174-S3`, disarm owner this seat; disarmed by the door build cell). The Opal path
  must carry the marker (it is dropped at `opal_producer.py:220` today). Y2's portal Keep must not ship before the door cell lands.
- **Observations ruled:** `W170-S1` (a bare string iterated as symbols) and `S2` (calendar-impossible dates), `W171-S1` (a `classify` error; a ticker with two classes). One repair cell, `AR-g-70`.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-63` | the PORTFOLIO SERIES: `ycharts/research/portfolio_series.py` (NEW): `to_epoch_ms`, `to_pairs`, `buy_and_hold` (the layout's own arithmetic, level 100 at the common start, typed exclusions, coverage), `named_series`; stdlib only; 12 checked cases and a test file | `portfolio_series.py`, `tests/test_portfolio_series.py`, the worker's folder | WORLD (the floor of an infrastructure path; source and tests only, nothing deployed) |
| `AR-g-69` | the PRICE-ADAPTER FACTS READ: the YCharts per-symbol call pattern (secret NAME, call shape, pacing), the one total-return formula across the DEMQUE store, the Bloomberg history and Yahoo, what the resident host can run, and the four adapters' signatures with the adapter build cells; a cited-line record checked by script; no source edited | the worker's record folder | LOCAL (a read of source and notes and a record) |
| `AR-g-70` | the REPAIR of the round-7 modules: `price_source.py` refuses a bare-string `symbols` and calendar-impossible or reversed windows and drops impossible row dates; `swap_replacement.py` drops a `classify` error as NOT_CLASSIFIED and treats a ticker with two classes as CLASS_AMBIGUOUS; tests added | `price_source.py`, `swap_replacement.py`, their two test files, the worker's folder | WORLD (the floor of an infrastructure path; source and tests only, nothing deployed) |

## Edges and chains

- THREE independent chains, disjoint write sets: `portfolio_series.py` (new), the worker's record folder, and the two merged round-7 modules with their tests. No cell consumes another's output.
- Next wave, cut on `AR-g-69`'s record and a read of the code each touches (each only with its own text and checks): the adapters (`AR-g-8k`, files per `AR-g-69`), the door build
  (`AR-g-68`: `intake/portfolio.py`, `ycharts/generate/normalized_input.py`, `ycharts/research/runner.py`), the C-SWITCH stamp (`AR-g-67`: `submission_service.py`, `acceptance.py`, the
  `generate.tf` statement as SOURCE), the resident variant binding and `producer_for` (`AR-g-64`: `resident_installed.py`, `resident_worker.py`), the map statistic fix (`AR-g-65`: three
  elements of `overview_map.json`, whose statistic values are read first), the compose into `opal_producer` (`AR-g-66`, after `AR-g-63`, the adapters, `AR-g-70` and the door build) and the ONE
  resident release build r32 (`AR-g-71`, the only writer of `build_resident_package.py`).
- Optional, not cut: the resident IAM leg for the DEMQUE store (`resident.tf`, estate-wide read). Without it the estate tier of the chain reads only the Bloomberg history and the rest falls to Yahoo; the
  report differs only in its source labels. Offered to the CTO as an enrichment.

## Four-postulate record

(i) Domain: the price chain's remaining pure parts and the repairs of the round-7 modules (FWD-7). (ii) Same grain: a new module, a read, and a repair of two modules. (iii) One intent per
cell. (iv) What this cut does NOT move: any deployed byte, any grant, the portal, the resident, the door, the producer.

fanout: 3 of 3 chains for workers per cut (AR-g-63 slot 175, AR-g-69 slot 176, AR-g-70 slot 177), cap 8, reason: a new pure module, a read-only trace and a repair of two merged modules share no write surface and no data edge.
