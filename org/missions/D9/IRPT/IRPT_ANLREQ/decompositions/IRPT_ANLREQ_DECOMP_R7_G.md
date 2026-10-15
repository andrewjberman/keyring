# IRPT_ANLREQ round 7, workstream ~G (ENGINE) -- decomposition: the report engine's price chain core, the replacement rule core, and the two reads that decide the switch and the compose

Issuer `2.0.0_SA_COO~G2`, 2026-10-15.

**Input:** `1.0.0_SA_CTO~DELL2` msg 8377 and the ruling
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_ANLREQ_FOUR_LANES_END_TO_END_20261015.md` @cea3f6d497, on Andrew's parallelize word:
`~G2` is the ENGINE lane (C-PRICES, C-SWITCH, C-SWAP step 2, the Comparison and Multi-Comp variants) and the single issuer of the resident
release; PRD v0.14 @81d9691b71 ADMITTED (msg 8400): the price chain is estate stores, then Yahoo (T-1), then YCharts one symbol per call, then
C-SWAP, else the report runs without the security and names it; C-SWAP is the class-matched pool and the longest Yahoo history, ties by ticker,
deterministic, the model never decides the pick (CTO price ruling ADDENDUMs 2 and 3, `CTO_RULING_DELL2_IRPT_ANLREQ_PRICE_SOURCES_AFTER_COVERAGE_READ_20261014.md`).

## State read before the cut

- Resident release 31 is INSTALLED (deploy ledger `20261015T0622Z_irpt-resident-r31-20261014`, CLOSED 06:37Z): `analysis_ready` send, `commentary_ready`
  consume and the packager wirings are in, dormant until the IB-pr-456 apply (IB-pr-579, `2.0.0_SA_COO~P2` to `0.7.0_AE_CloudOps~IB2`).
  The next resident release (r32) is this workstream's, and it also removes the synthetic producer address `fwd1-staff-r41a@opal.invalid`
  after the FWD-1 run (the list's own comment, `resident_worker.py` lines 159-167).
- The C-SWITCH read of source exists (`deliverables/0.9.0_WK_IRPT_ANLREQ~135/r41/C_SWITCH_READ.json`, cell `AR-y-326`): the principal is a staff
  member's sign-in email; `ticket_id` is client-set and only pattern-checked; no Investor Reporting code reads the ticket table; it recommended
  keying on a ticket the ticket table confirms, which needs a read that does not exist. `AR-g-53` settles where that read lives.
- The Opal engine renders the Overview only, with `pricing=False`: the one report on record has 257 sections, 6 VALUE, 251 NOT_AVAILABLE
  (CRO trace `TICKET_CENTER_ANALYSIS_REQUEST_END_TO_END_GAP_BRIEF_20261014.md`, hops 9 and 10).
- The estate has no stored price series for the holdings beyond MDPF_DEMQUE's Yahoo store (483 securities) and the Opal ETFs' Bloomberg
  history (CTO price ruling, "What the read changed"); the CRO's probe measured Yahoo for the missing symbols (16 symbols in 2.21 s).

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-51` | C-PRICES, the CHAIN CORE: `ycharts/research/price_source.py` (NEW), `resolve_prices(symbols, start, end, readers, as_of)`: estate, then yfinance, then ycharts, first usable answer wins, later tiers uncalled, YCharts one symbol per call, rows cut at `as_of`, bad rows dropped, a raising tier typed and its message withheld, a MISSING symbol named, never raises on data; stdlib only; 12 checked cases and a test file | `price_source.py`, `tests/test_price_source.py`, the worker's record folder | WORLD (the floor of an infrastructure path; source and tests only, nothing deployed) |
| `AR-g-52` | C-SWAP step 2, the REPLACEMENT RULE: `ycharts/research/swap_replacement.py` (NEW), `choose_replacement(...)`: the class-matched pool of `etf-classifications` plus class-checked model proposals, Yahoo-priced only, longest history wins, ties by ticker, order-independent, with `proxy_for`/`method`/`confidence` and the sentence the report prints; stdlib only; 14 checked cases and a test file | `swap_replacement.py`, `tests/test_swap_replacement.py`, the worker's record folder | WORLD (the floor of an infrastructure path; source and tests only, nothing deployed) |
| `AR-g-53` | the C-SWITCH DESIGN READ: where a client `ticket_id` is confirmed against the ticket table (at acceptance in `irpt-ycharts-generate`, or at the resident), what each placement can read today, the exact change set and IAM diff for each, the forgeability rule, and a recommendation; a cited-line record checked by script; no source edited | the worker's record folder | LOCAL (a read of source and a record) |
| `AR-g-54` | the ENGINE COMPOSE READ: what the priced layout consumes (the one series shape), the two estate price stores (address, key, format, symbol key, basis, readability by the resident, cross-firm note), what the Comparison and Multi-Comp maps need and what the Opal engine does with them today, and the seams where prices and the swap enter `opal_producer`; ends with the round-8 build cell list; a cited-line record checked by script; no source edited | the worker's record folder | LOCAL (a read of source and a record) |

## Edges and chains

- `AR-g-51`, `AR-g-52`, `AR-g-53` and `AR-g-54` are FOUR independent chains: two new files with their tests, and two reads with no write surface
  in the product tree. No cell consumes another's output; the write sets are disjoint (`price_source.py`, `swap_replacement.py`, two worker folders).
- `AR-g-51` and `AR-g-52` share one later consumer (the compose cell of round 8, `AR-g-6x`), which calls `swap_replacement` only for a symbol
  `price_source` returns MISSING, and prices every candidate through `price_source`'s Yahoo tier. That edge is a later cell's, not a dependency here: each
  module takes the other's function as an argument.
- Round 8, to be cut on the two reads (names provisional until `AR-g-54` lists them): the store adapters (estate stores and the yfinance and YCharts
  readers, with the T-1 cut from `lib/trading_calendar.py`), the compose into `opal_producer` (`pricing` on, `price_source` then `swap_replacement`,
  the named omission), the Comparison and Multi-Comp variants in the Opal engine, the C-SWITCH build and the IAM leg it needs, and ONE resident
  release build (r32) that carries `price_source.py` and `swap_replacement.py` in its member list and removes the synthetic producer address.
- The single resident release is ONE artifact under ONE never-widen pair, issued by this lane (CTO ruling shared rule 1); `~Y2` hands the portal-side
  contract it needs, and neither applies a resident change alone. Neither cell here changes a deployed byte.

## Battery findings (where they touch the owned cells)

- `AR-g-51`: the traps the checker is built to catch are a later tier called after an earlier answer (a vendor call spent for nothing), YCharts
  batched (it cannot batch: ONE symbol per call, CTO ADDENDUM 1), today's intraday row let through (the cut is `as_of`, T-1), an exception message with a
  credential in the result, and the chain raising and so blocking the report. Feed test: a reference build passes all twelve cases; a mutant
  (`<= 0` relaxed to `< 0`) fails case 9; the absent module fails every arm.
- `AR-g-52`: the traps are the model deciding the pick, a proposal admitted on the model's own stated class, a tie broken by input order, and a hole
  in the report with no sentence naming it. Feed test: a reference build passes all fourteen cases; a mutant (history sort reversed) fails four.
- `AR-g-53`, `AR-g-54`: a "no" said without a search, a store assumed readable, a price basis assumed, and a round-8 list with overlapping write sets.
  The cite checker re-opens every cited line; a missed cite fails the criterion; the absent record fails every arm.
- NOT seen by this battery: the live roles, stores and vendors. The reads and the adapter cells are where they are read.

## Four-postulate record

(i) Domain: the ENGINE lane's first round, FWD-7 (C-PRICES, C-SWAP) and FWD-1 hop 8 (C-SWITCH) only; nothing of the filing lane (`~Y2`) or the
commentary lane (`~T2`). (ii) Same grain: each cell is one file pair or one record. (iii) One intent per cell: a price chain, a replacement
rule, a placement decision, a seam map. (iv) What this round does NOT move: any deployed byte, any grant, any queue, the resident, the portal, the
ticket service, the YCharts or Yahoo accounts, the producer allow list. It ADDS two modules nothing imports yet and two records.

fanout: 4 of 4 chains, cap 8, reason: two new pure modules with their tests and two read-only traces share no write surface and no data edge; slots 170 (AR-g-51), 171 (AR-g-52), 172 (AR-g-53), 173 (AR-g-54).
