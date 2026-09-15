# Tab-score sourcing, measured -- Bloomberg DAPI, Lusha and the pool, for the four scores Andrew set 2026-09-15 ~17:4xZ-18:3xZ

**Measured by:** `1.0.0_SA_CTO~W`, 2026-09-15 ~18:2xZ-19:0xZ. **Instruments:** Bloomberg DAPI at 127.0.0.1:8194 (`//blp/apiflds`
FieldSearch and FieldInfo with documentation; `//blp/refdata` ReferenceData with overrides and HistoricalData), boto3 reads of
`s3://opal-data-harvest` (the AMGT pool) and `s3://opal-data-imo` (FIND_INSURE's Lusha tiers, counts and key names only), and the repo.
**Status:** QA measurement. Nothing here is a production artifact; scripts and JSON outputs sit in this seat's session scratchpad.
**Records it answers:** @`4eef3ae75a` (per-tab principle), @`260402c006` + @`3f9481ea12` (Robustness; "all from Bloomberg"; the Mgmt
tab from Bloomberg then Lusha; Lusha reliability), @`947b9793a1` (Peers V), the ~18:3xZ Divergence record.

**Populations.** POOL = the 33 names holding a `peers/v1` object in the pool (the analyzed-company set this seat can enumerate today).
ANALYZED FIVE = BA US, COST US, HD US, SAP GY, BABA US. PEER-COMPLETE = the 10 pool names whose served peer set is non-empty.

---

## 1. Mgmt tab -- executive tenure

| Bloomberg field | what its documentation says | coverage |
|---|---|---|
| `EXECUTIVE_AVERAGE_TENURE` | average tenure of all current company executives, **in any executive position**, in years | 33 of 33 now; yearly history 2 of 5 (COST, HD, 2021-2025); BA, SAP, BABA none |
| `TOTAL_TENURE_OF_CEO_COMPANY` | the current CEO's total tenure **at the company** (since the most recent appointment if they left and rejoined) | 33 of 33; yearly history 5 of 5 |
| `CHIEF_EXECUTIVE_OFFICER_TENURE` | the current CEO's tenure **as CEO only** | 33 of 33; yearly history 5 of 5 |
| `LAST_CFO_START_DATE`, `LAST_COO_START_DATE` | the date the current CFO / COO took the role | 5 of 5 each |
| `COMPANY_EXEC_OFFICERS` (bulk) | officer name and title, **no dates** | BA 17 rows, SAP 16 rows |
| `BOARD_AVERAGE_TENURE` | directors, not executives | 33 of 33 |

- **What it answers.** Andrew's "average exec management time with company" is served today by `EXECUTIVE_AVERAGE_TENURE` on every
  pool name, so the absolute and the pool percentile are computable now. Its definition is time IN AN EXECUTIVE POSITION -- the "as a
  manager" reading. The append-over-time store starts today for 3 of the analyzed five (no yearly history).
- **What it does not answer.** Average time AT THE COMPANY in general, per executive: Bloomberg carries that only for the CEO. No
  field gives per-officer join dates; the bulk officer list is names and titles.
- **Not corroboration:** BA's filings-derived average (rj-8, M-1, 12 officers) is 4.08; Bloomberg's is 4.52 over a 17-officer list.
  Different officer sets and definitions, two instruments that do not measure the same thing.

### Lusha, for the per-officer measures Bloomberg lacks

| read | result |
|---|---|
| prospecting against the filing officers (rj-8, M-1) | 11 of 48 matched; the Lusha title equals the filing role for 4 of those 11; **no dates in the response** |
| real Lusha data the estate holds (`opal-data-imo/corp/*/silver/linkedin-scrape/`, run 2026-05-27, 24 companies) | 661 contact records; **0 of 661 carry `currentPosition` or `previousPositions`** -- every record is the prospecting shape, marked `contact_reveal_deferred` |
| FIND_INSURE gold (148 objects) | 0 rows carry a tenure value |
| the only position history with dates in the repo | a hand-built test fixture (`contacts_enrich_happy.json`, a fictional contact) -- never observed from the live API here |
| Lusha's public enrich documentation page | names emails and phones only |
| the code gate | `contacts_enrich` raises unless `LUSHA_CONTACT_REVEAL_ENABLED` is set (Andrew's credit-conservation policy, FIND_INSURE.034); its `reveal` list is optional, so an enrich requesting no emails or phones may be possible -- its credit cost and whether it returns positions are both unmeasured |

- **Verdict.** Lusha's reliability for executive tenure is NOT MEASURABLE from what the estate holds: the parsers for positions and
  start dates exist and are tested, but no live response has ever carried them. One bounded enrich over the 11 matched officers would
  settle both reliability and parseability; it needs Andrew's word on the flag.

---

## 2. Thesis/Risk tab -- Robustness, on Bloomberg

Current values on the analyzed five: `EBIT`, `IS_INT_EXPENSE`, `INTEREST_COVERAGE_RATIO`, `NET_DEBT`, `NET_DEBT_TO_EBITDA`,
`BS_CASH_NEAR_CASH_ITEM`, `BS_TOTAL_LINE_OF_CREDIT`, `BS_TOTAL_AVAIL_LINE_OF_CREDIT`, `BS_ST_BORROW`, `BS_TOTL_DEBT_DEBT_SCHEDULE`,
`TRAIL_12M_FREE_CASH_FLOW`, `FREE_CASH_FLOW_MARGIN` 5 of 5; `BS_YEAR_1_PRINCIPAL` / `BS_YEAR_2_PRINCIPAL` 4 of 5 (BA absent);
`BS_CONTRACTUAL_OBLIG_YEAR_1` 1 of 5 (SAP). `BS_TOT_DEBT_OUTSTANDING_TOTAL` and `TRAIL_12M_EBIT` are invalid mnemonics.

The model's history requirement, quarterly `HistoricalData` 2023-01-01 to 2026-09-15 over the POOL (33 names, 0 security errors):

| constraint | Bloomberg inputs | names with the model's full history | names with at least one quarter |
|---|---|---|---|
| x1 EBIT / interest | `EBIT`, `IS_INT_EXPENSE` quarterly, 11 quarters summed to 8 TTM | 14 | 15 |
| x2 net debt / EBITDA | `NET_DEBT`, `TRAIL_12M_EBITDA` | 22 | 23 |
| x3 (cash + undrawn revolver) / 24m obligations | cash, `BS_TOTAL_AVAIL_LINE_OF_CREDIT`, year-1 + year-2 principal | 3 | 13 |
| x4 debt due in 24m / total debt | year-1 + year-2 principal, `BS_TOTL_DEBT_DEBT_SCHEDULE` | 3 | 14 |
| x5 FCF / revenue, TTM | `TRAIL_12M_FREE_CASH_FLOW`, `TRAIL_12M_NET_SALES` | 22 | 22 |
| x6 largest customer / revenue | none -- no scalar field; `SUPPLY_CHAIN_CUSTOMERS` returns a ticker list | 0 | 0 |

- **Names by constraints with full history:** 0 -> 11 names, 2 -> 8, 3 -> 11, 5 -> 3. **The model ranks a name only at n >= 5, so
  3 of 33 are rankable today**, and because x6 has no source, a rankable name needs all of x1-x5.
- **Traps.** `BS_TOTAL_LINE_OF_CREDIT` reads 0 for BA at 2025-03-31 between quarters of 10000 (a false zero); `NET_DEBT_TO_EBITDA` is
  absent in BA's negative-EBITDA quarters; SAP has no quarterly interest expense; the principal ladder is an annual disclosure, so a
  quarterly sd over it is an sd over carried-forward values; covenant fields on Bloomberg describe bonds, not equity thresholds, so
  x1 and x2 fall to the model's "else" thresholds.
- **Correction.** The pre-read's earlier "0 of 6 constraints computable at 8 TTM quarters" was measured on the pool's model block. That
  block does not carry these fields. Bloomberg itself serves x2 and x5 at full history for 22 of 33.

---

## 3. Peers tab -- V, computed on Bloomberg over the served peer sets

- **Peer sets served:** 10 of 33 pool names carry 12 members; 23 carry 0. Member rows carry market cap and no valuation value.
- **Member identity:** 120 member rows were requested as their raw identifier plus " Equity". 113 name the same company; **4 are
  invalid** (Toyota and Fast Retailing, requested without an exchange code, in the BABA and HD sets); **3 resolve to a DIFFERENT
  security** -- Nestle to a Taiwan warrant, Infineon to a Chinese ETF, MediaTek to a German fund. So member identity is resolved to an
  exchange-coded Bloomberg security before any measure is read (candidate 12's rule reaches the valuation inputs).
- **Fields,** `BEST_FPERIOD_OVERRIDE=BF` and `EQY_FUND_CRNCY=USD`, over 121 securities: FCF yield 101, forward P/E 116, trailing P/E 111,
  dividends paid 113, buybacks 116, USD market cap 117, forward EV/EBITDA 105, forward EV/sales 105.
- **Field trap:** a `BEST_*` field WITHOUT the override is the next fiscal QUARTER (the default `1FQ`): BA's forward P/E reads 174.8 at
  the default and 83.2 at `BF`.

V with the 7 bad identity rows excluded (excluding them moved no V by more than 0.01, because the wrong securities carried no measures):

| name | peers used | measures | V |
|---|---|---|---|
| BA US | 12 | 5 (inverse PEG absent: forward EPS negative against trailing) | -0.94 |
| BABA US | 10 | 6 | +3.45 |
| COST US | 11 | 6 | -0.45 |
| HAL US | 12 | 6 | +0.27 |
| HD US | 10 | 6 | +0.18 |
| INTU US | 12 | 6 | +1.48 |
| KMB US | 12 | 6 | +0.29 |
| NU US | 12 | 3 (bank peers: FCF and both EV measures fall below 6 peers) | -0.85 |
| SAP GY | 10 | 6 | +0.37 |
| VLO US | 12 | 6 | +1.38 |

- **Method points for the addendum.** (i) The model winsorizes the PEERS, not the subject, so one measure can carry V: BABA's inverse
  PEG z is +19.17 because trailing EPS is depressed against forward, and V without that measure is +0.30. (ii) Buybacks come from the
  fiscal-year cash flow, not TTM. (iii) NTM E/P is left ABSENT for a negative forward EPS here, because the forward P/E is undefined
  there; a signed yield needs EPS and price in one currency, and BABA's estimates are CNY against a USD price. (iv) P ranks V within
  sector, and today the population holding a V is 10 names.

---

## 4. Model tab -- Divergence D

| input | Bloomberg | coverage over the POOL |
|---|---|---|
| F_cons, consensus NTM FCF | `BEST_ESTIMATE_FCF` (also `BEST_CALCULATED_FCF`) at `BF`, `1FY`, `2FY` | 31 of 33 (26 of 33) |
| s_cons, sd of analyst FCF estimates | **no field** -- `_STDDEV`, `_NUMEST`, `_HI`, `_LO`, `_MEDIAN` variants of both FCF mnemonics are INVALID on 33 of 33 | 0 |
| N_est, analysts contributing to FCF | **no field** (as above) | 0 |
| nearest dispersion Bloomberg carries | cash flow per share: `BEST_CPS_STDDEV` with `BEST_CPS_NUMEST` (at 1FY: BA 4, COST 5, HD 5, SAP 10, BABA 8); EPS: `BEST_EPS_STDDEV` with 26-38 estimates | 29 of 33; 33 of 33 |
| R_ntm, consensus NTM revenue | `BEST_SALES` at `BF` | 33 of 33 |
| F_model, the house model's NTM FCF | **ABSENT** -- see below | 0 |

- **F_model does not exist.** The pool holds 17 model-block objects (14 `derived/model_block`, 3 `derived/model_block_fye`). Both
  carry REPORTED fiscal years pulled from Bloomberg history (BA's block: fiscal years 2016-2023, every figure `source: bloomberg-dapi`),
  with no forecast line, no projection and no driver. The PRD's Model tab is "the plain financial model, built the same way for every
  company". So D is SUPPRESSED for every name today under Andrew's own guard (F_model missing), and the pre-deployment degeneracy check
  has nothing to run on. Divergence needs a forecast producer whose drivers are seeded at least partly independently of consensus; the
  estate has none, so it is new scope.
- **Traps.** At `BF` the estimate counts are time-weighted blends and come back fractional (COST 38.54), so the N_est < 4 guard needs
  the fiscal-year count; BABA's estimates are in CNY against a USD listing; `BEST_PERIOD_END_DT` is not a valid mnemonic, so the
  fiscal-year end behind `1FY` / `2FY` has to come from another field before an NTM figure is calendarized.

---

## 5. Decisions this card surfaces for Andrew (none is taken here)

1. **Lusha:** one bounded enrich over the 11 matched officers, requesting no emails and no phones, contact fields discarded in memory,
   to measure whether position start dates come back and how often -- needs `LUSHA_CONTACT_REVEAL_ENABLED` for that one call.
2. **FCF dispersion:** Bloomberg has no FCF estimate spread or count. Choose a proxy (cash-flow-per-share spread, thin at 4-10
   estimates; EPS spread scaled; or another source) or hold D.
3. **F_model:** Divergence needs a house forecast of NTM FCF with independently seeded drivers; none exists.
4. **"| sector" against the pool:** Robustness, Peers and Divergence all percentile by sector; the ~17:5xZ word set the pool of
   analyzed companies, 33 names today, where a sector holds one to four of them.
