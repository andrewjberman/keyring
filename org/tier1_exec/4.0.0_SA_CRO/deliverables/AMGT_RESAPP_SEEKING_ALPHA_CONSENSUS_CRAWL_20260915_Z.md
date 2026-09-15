# Seeking Alpha consensus figures for the AMGT_RESAPP pool -- what the canonical rider returns, every field classed

**Author:** `4.0.0_SA_CRO~Z` | **Date:** 2026-09-15 | **For:** `1.0.0_SA_CTO~W` (AMGT_RESAPP), who asked; `4.0.0_SA_CRO~W`
cites this; `0.0.0_AB_MSTR~Z` carries.
**Authority:** Andrew-direct ~19:0xZ (record @`a026de4004`), *"Ask CRO~Z to explore Seeking Alpha with an authenticated
crawl, they should have consensus figures."* And ~19:30Z at this terminal, *"do not reinvent the wheel with seeking
alpha scraping, we have the harvest scrapers for this reason to get cookies and they are canonical"* (record
`ANDREW_DIRECT_20260915_193xZ_SA_CRAWL_USE_CANONICAL_HARVEST_SCRAPERS_NO_REINVENTION.md`).
**Method:** the canonical rider only. `sa_rest_fetch.build_session` (the parked `seeking-alpha/session` cookies, the
residential-proxy egress, Chrome TLS impersonation, the proxy-CA `verify=False`) plus GETs to SA's JSON estimates API
with the documented per-page `Referer`. No browser, no new scraper. Secrets read through `comp-secrets get --reveal`;
no value printed or written.

---

## THE ANSWER FIRST

- **Seeking Alpha serves consensus for EPS and revenue, in full, per fiscal year, for all five names.** One JSON route
  returns the mean, high, low, analyst count and the reported actual, dated, for FY-1 through FY+3.
- **It does NOT serve free cash flow or cash-flow-per-share consensus.** Measured, not assumed: 10 documented
  cash-flow item-name variants returned empty on a route where a positive control (`ebitda_consensus_mean`) returned
  data in the same call. This is NOT_CARRIED, not a pull that missed it.
- **It carries EBITDA consensus, but only the mean and actual -- no high, low or analyst count**, so EBITDA has no
  dispersion here.
- **For the Model tab's Divergence denominator, this settles Andrew's item 2 ("CFPS or EPS is fine") toward EPS:**
  SA carries EPS analyst dispersion (high, low, count) per fiscal year for all five, which is the FCF dispersion
  Bloomberg lacked. SA offers no FCF dispersion of its own.

## 1. THE ROUTE, AND WHY IT IS THE CANONICAL WHEEL

`GET /api/v3/symbol_data/estimates?period_type=annual&relative_periods=-1,0,1,2,3&ticker_ids={id}&estimates_data_items={items}`

Ridden through `org/tier1_exec/4.0.0_SA_CRO/scripts/sa_rest_fetch.py` `build_session` (the same session builder the
estate's `integrations/seekingalpha/rest_fetch.py` ETL uses). The parked session was confirmed authorized before any
estimate call: `sa_rest_fetch.py check` -> `authorized=True`, Annual subscription, active, through the proxy. Two
conditions from the canonical contract held: the full PerimeterX jar (identity alone is 403) and a per-page `Referer`
(without it the API answers 200 with a 2-byte body). Every call was a GET; SA's estimates API is JSON.

The `ticker_ids` value is SA's internal numeric ticker id, returned by the canonical `symbol` verb: BA 769, COST 58,
HD 799, SAP 1320, BABA 137271.

## 2. COVERAGE MATRIX -- 15 (ticker x metric) probes, all reads 2026-09-15 ~21:5xZ

| metric | mean | high | low | # analysts | actual | fiscal years | class |
|---|---|---|---|---|---|---|---|
| EPS (`eps_normalized`) | Y | Y | Y | Y | Y | FY-1..FY+3 | **CARRIED** 5 of 5 |
| Revenue (`revenue`) | Y | Y | Y | Y | Y | FY-1..FY+3 | **CARRIED** 5 of 5 |
| EBITDA (`ebitda`) | Y | -- | -- | -- | Y | FY-1..FY+3 | **CARRIED, mean+actual only** 5 of 5 |
| Free cash flow | -- | -- | -- | -- | -- | -- | **NOT_CARRIED** (see s.3) |
| Cash flow per share | -- | -- | -- | -- | -- | -- | **NOT_CARRIED** (see s.3) |

Each name resolves to five items: `{metric}_consensus_mean`, `_consensus_high`, `_consensus_low`,
`_num_of_estimates`, `{metric}_actual`. Every estimate entry carries its fiscal year, period-end date and an
`effectivedate` (the as-of), so revision timing is on every figure.

Concrete, so the shape is not abstract -- BA (id 769), FY2026 (FY+1), read from the served bytes:
consensus EPS mean **-1.078**, high **-0.30**, low **-1.85**, from **22** analysts.

The fiscal-year windows differ by company calendar: BA/COST/SAP return FY2024-2028, HD/BABA return FY2025-2029
(their fiscal years end off the calendar year). Latest effective dates span 2026-09-04 to 2026-09-15, so the
consensus is current.

## 3. EVERY MISSING FIELD CLASSED (Andrew's item 4: coverage vs pull method)

- **FCF -- NOT_CARRIED.** DISCRIMINATED, not inferred from one empty read. On BA, 10 documented cash-flow item-name
  variants (`free_cash_flow_*`, `fcf_*`, `levered_free_cash_flow_*`, `unlevered_free_cash_flow_*`,
  `cash_flow_*`, `operating_cash_flow_*`, `cfps_*`, `cfps_normalized_*`, `cash_flow_per_share_*`, `ffo_*`) each
  returned empty **while, in the same call, the control `eps_normalized_consensus_mean` returned data on all 11
  calls and `ebitda_consensus_mean` returned data.** A route that returns EBITDA and EPS but no cash-flow variant is
  a route whose estimates feed does not carry cash flow, not a route we failed to reach.
- **CFPS -- NOT_CARRIED**, by the same discrimination (the `cfps_*` and `cash_flow_per_share_*` variants are in the
  10 above).
- **EBITDA high/low/count -- NOT_CARRIED.** The mean and actual return; the dispersion items return empty on a call
  where the EPS dispersion items return, so the feed carries an EBITDA point estimate without a spread.
- **Up/down revision counts -- NOT_REACHED (bounded, not absent).** The estimates response carries a `revisions`
  sibling block that is empty unless revision-specific data items are requested; those item names were not probed,
  to keep the crawl bounded. The revision *timing* is already covered by the `effectivedate` on every estimate. If
  the CTO wants explicit up/down counts, that is one more bounded probe of the same route with revision items.
- **Quarterly estimates -- NOT_REACHED (bounded).** Only `period_type=annual` was requested, because the tab scores
  are annual. `period_type=quarterly` on the same route is one parameter away.

## 4. IS IT SEEKING ALPHA'S OWN SET, OR A RELAY (Andrew's item 3)

**Inferred from the payload shape, not from an attribution string SA served.** The estimates payload is a licensed
institutional consensus feed: each entry is keyed by `periodtypeid`, `fiscalquarter`, `fiscalyear`, `calendarquarter`,
`periodenddate`, `advancedate`, with mean/high/low/count -- the standard sell-side estimate-aggregator schema, not
Seeking Alpha's own contributor or author content. Seeking Alpha's *own* opinion surfaces are separate and already
mapped in this estate: the `virtual_analysts` report and the quant/author ratings routes (the reference
`AMGT_RESAPP_SEEKING_ALPHA_AUTH_INVESTIGATION_20260910.md`). So the consensus figures here are a relay of a
third-party estimates aggregator, and SA's own analysis is a different object. **NOT verified:** which aggregator, and
SA's terms on programmatic reuse of the estimates feed. The page does not name the vendor in the JSON.

## 5. WHAT THIS MEANS FOR THE MODEL TAB'S DIVERGENCE (for the CTO, not adjudicated here)

- Bloomberg served consensus FCF but no FCF spread/count (the card `TAB_SCORE_SOURCING_BLOOMBERG_LUSHA_MEASURED.md`
  s.4). **Seeking Alpha adds no FCF dispersion** -- neither source carries it.
- Andrew's item 2 ruled CFPS or EPS acceptable as the dispersion proxy. **SA carries EPS dispersion (high, low,
  count) per fiscal year for all five, and no CFPS at all.** So EPS is the proxy SA supports; CFPS via SA is not
  available. Bloomberg's `BEST_CPS_STDDEV` remains the only CFPS-dispersion source, thin at 4-10 estimates (the
  card). EPS dispersion is the wider-covered choice on both sources.
- **The house forecast `F_model` question Andrew's answer left open is not answered by a consensus feed** -- consensus
  is the denominator's peer, not the house numerator. SA offers nothing that seeds an independent house FCF forecast;
  its estimates ARE consensus. That remains research for `4.0.0_SA_CRO~W`'s brief.

## 6. WHAT WAS NOT DONE

- No scheduled job, no bucket write, no backfill. A bounded read-only research crawl, one pass, five tickers, on
  Andrew's per-use word for Seeking Alpha only.
- The bespoke browser route-discovery script this seat started was ABANDONED on Andrew's ~19:30Z word; its one run
  had failed on a Git Bash path-mangling defect and recorded nothing. Nothing from it is in the repo.
- Quarterly estimates, explicit revision counts, and the aggregator's identity were left as named bounded follow-ups
  (s.3, s.4), not chased.
- The raw estimate JSON per ticker was captured to this session's scratch only; it is not committed (raw vendor bytes
  belong in the harvest pool's `raw/seekingalpha/{key}/{stamp}/` shape under the harvest owner's cadence, not in a
  CRO deliverable).

## 7. PROVENANCE

```
RUNS (2026-09-15, this device, this seat, canonical rider, residential proxy):
  sa_rest_fetch.py check                 -> authorized, Annual, active           21:26Z
  sa_estimates_probe.py BA 769           -> estimates route 200; eps/rev data; fcf/cfps empty   21:52Z
  sa_fcf_discriminate.py BA 769          -> 11/11 control present; ebitda present; 10 cash-flow variants empty   21:55Z
  sa_rest_fetch.py symbol COST HD SAP BABA -> ids 58/799/1320/137271            21:55Z
  sa_estimates_matrix.py x5              -> 15 probes, matrix in s.2            21:57Z
SECRETS: read seeking-alpha/session and astn/brightdata/residential-proxy via comp-secrets get --reveal into a
  locked session-scratch dir; no value printed, logged or committed.
CANONICAL CODE RIDDEN (not modified): org/tier1_exec/4.0.0_SA_CRO/scripts/sa_rest_fetch.py (build_session, get path).
REFERENCE: org/tier1_exec/4.0.0_SA_CRO/deliverables/AMGT_RESAPP_SEEKING_ALPHA_AUTH_INVESTIGATION_20260910.md;
  the canonical package lib/opal_data_harvest/ (contracts.json names sa's session/consumer).
Push state: LOCAL (site-Z push hold; 0.0.0_AB_MSTR~Z carries).
```
