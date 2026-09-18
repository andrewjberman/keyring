# BRIEF -- the Model panel, from current to desired

**From** `4.0.0_SA_CRO~Z`, 2026-09-18 ~18:5xZ, at Andrew's word: *"write it up and get it over to CTO~Z. I told them
after they receive this brief and integrate it into their flow, they may proceed with COO~Z. You and I will proceed to
Posture regardless, but the greater fabric does not need to be held up on that."* **To** `1.0.0_SA_CTO~Z`, for the
panel-briefs intake. **Status:** a BRIEF. It creates no gate and cuts no order. **Per Andrew, this is the last brief the
CTO waits for before proceeding to `2.0.0_SA_COO~Z`;** the Posture brief follows separately and holds nothing up.

**His decision on this panel** (verbatim, addendum to `ANDREW_DIRECT_20260918_17xxZ_PEERS_SEEKING_ALPHA.md`): *"I'd use
Bloomberg as primary, seeking alpha as a fall back"* -- for the forecast years. His standing direction also applies: no
fleet run until the process is validated end to end, and every stage framed by what makes it run for a NEW security.

**Code vintage:** HEAD at write time; cited files unchanged since `@e2d89be7da` unless stated.

---

## 0. The denominator

33 keyed names, from `crosswalk/v1/2026-09-15.json` records with resolution MEASURED. Figures were read with the
adapter's own `read_thesis_bundle` (the `/thesis` payload the Model tab reads) and `read_model_block_versions`.

---

## 1. Where the panel stands, measured 2026-09-18

**Model is the healthiest panel in the series.** The producer is
`integrations/bloomberg/research/model_block_pull.py`: stage `pull` lands raw Bloomberg bytes at
`raw/bloomberg/<key>/<stamp>/`, and stage `derive` joins on fiscal year and lands
`derived/model_block/<key>/<stamp>/model_block.json`, every figure carrying unit, sign, basis, vintage and source. The
adapter `read_model_block` (`scoped_amgt.py:924`) reads the newest block and applies the shared corrected fiscal-price
overlay. The check face grades every figure, and `ModelTab.tsx` renders it in the shape of Adam's Model sheet
(`modelSheet.ts`).

| what | measured over 33 |
|---|---|
| model block SERVED | **33** |
| fiscal years | 2016-2025 on 32; 2018-2025 on 1 |
| fields per name | 19 on 28; fewer on 5 (banks and insurers carry no EBITDA -- honest) |
| check-face verdicts | **PASS 5,926 -- REFUSE 348 -- PROVISIONAL 103** |
| names with at least one REFUSED figure | 31 |
| stamps per name | 1 on 30; 5 on 3 (the pilot names BA, SAP, BABA) |
| newest stamp | 2026-09-16 on all 33 -- one hand run |
| Upside / Base / Downside cases | ABSENT on 33 (hard-coded) |
| Robustness / Peers V / Divergence | ABSENT on 33, each with its own reason |

### 1.1 The 348 refusals are one missing registry entry, not bad data

| field | refused | reason on every one |
|---|---|---|
| `IS_DIV_PER_SHR` (dividend per share) | 297 | unit/sign convention "NOT-YET-BUILT" |
| `EQY_FREE_FLOAT_PCT` | 29 | the same |
| `SHORT_INT_RATIO` | 12 | the same |
| `SI_PERCENT_EQUITY_FLOAT` | 10 | the same |

**The cause, read at source:** the producer takes each figure's unit from `field_map.json`, and **that map lives in a
worker's deliverables folder**: `_FIELD_MAP_PATH` at `model_block_pull.py:286-288` =
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/field_map.json`. It carries 32 fields: 28 with
one unit for every security, and exactly these four with a PER-SECURITY unit, measured for only the three pilot names.
For every other name, `_resolved_unit` (`:300-316`) falls back to "SEE field_map.json ... not yet built", and
`checkface/run_checks.py:54-55` maps that to REFUSE. **The dividend row is refused on 30 of 33 names for a map entry,
not a data problem.**

The 103 PROVISIONAL are 10 fields on one name carrying a live `currency_caveat` (a reporting-currency reconciliation,
`run_checks.py:44-47`) -- correctly held, not passed.

### 1.2 The sheet rows the block cannot fill

Of the 17 declared summary and margin rows (`modelSheet.ts:39-58`), **five have no field behind them and always render
ABSENT:** Revenue/Sh, FCF yield, FCF margin, RoTA and Earnings margin. The page correctly refuses to compute them. There
are no year-on-year growth rows, and no forecast years, because `HIST_END = "2025-12-31"` (`model_block_pull.py`) and no
estimate field is pulled.

### 1.3 The scores explain themselves -- read from `scores/v1/BA_US_Equity/2026-09-17.json`

| score | why ABSENT |
|---|---|
| Robustness | "n=1 of 6 measured ... below the n>=5 eligibility floor"; the block is annual, not the ruled 8-quarter TTM window, and lacks fields such as interest expense; one constraint has no covenant threshold |
| Peers V | no measure computes from the subject's own row -- now covered by the Peers brief (SA shape, floors 5/5) |
| Divergence | "FWD-20's house FCF forecast has not been built yet (no model_fcf producer exists)" -- ABSENT by ruling |

---

## 2. Forecast years: Bloomberg primary, Seeking Alpha fallback -- measured

Bloomberg consensus over the 33, one `ReferenceDataRequest` per fiscal year with an EXPLICIT
`BEST_FPERIOD_OVERRIDE` (1FY / 2FY / 3FY) -- `BEST_` fields default to the next quarter without it:

| field | FY1 | FY2 | FY3 |
|---|---|---|---|
| `BEST_EPS` | 33 | 33 | 33 |
| `BEST_SALES` | 33 | 33 | 32 |
| `BEST_EBITDA` | 31 | 31 | 31 |
| `BEST_PE_RATIO` | 31 | 32 | 32 |
| `BEST_DPS` | 33 | 33 | 33 |
| `BEST_PERIOD_END_DATE` | 33 | 33 | 33 |

**Control:** Boeing reads FY2026 EPS -0.83, FY2027 3.95, FY2028 8.05, with period-end dates 2026-12-31, 2027-12-31 and
2028-12-31. **The Seeking Alpha fallback is needed for a handful of cells, not a column.** The EBITDA and P/E gaps
fall on the names that also carry no historical EBITDA (banks and insurers), where "not meaningful" is the honest cell,
not a gap to fill.

**Two cautions for the L4:**
- The crosswalk stores Bloomberg ids WITHOUT the yellow key (`BA US`). This seat's first pull used them raw and got 33
  of 33 security errors -- a failed instrument, not a coverage finding. Every Bloomberg call appends ` Equity` (or
  reads the model block's own security string).
- **Each forecast cell carries its fiscal year AND its source** (`BBG` / `SA_FALLBACK`), and the page labels it as
  consensus, not reported. The column header comes from `BEST_PERIOD_END_DATE`, never from a counted offset -- the
  same "never a fiscal-year label over an NTM figure" rule `csc.py` already enforces.

---

## 3. One decision still Andrew's

| the question | why it is his |
|---|---|
| **What are the Upside / Base / Downside cases built from, and who sets them?** | The sheet's cases are EPS x multiple -> price -> return. With consensus now available, EPS has a source. The multiple and the scenario spread are Opal's JUDGMENT -- Adam's sheet names them and no data source carries them. Until he rules, the cases stay ABSENT with that reason. |

---

## 4. What makes this run for a new security -- today and desired

| step | today | desired |
|---|---|---|
| 1. the pull | by hand: `model_block_pull.py pull --securities ...` (default list: the 3 pilots); not a leg of `scheduled_daily_pull.cmd` | a step of instantiating the security, then refreshed after each fiscal year closes, on a cadence Andrew sets (his reservation on the Bloomberg pull cadence stands) |
| 2. units | `field_map.json` in a worker's folder; per-security units for 3 names | the map in a proper home, and built for each new security during instantiation, so no figure is refused for a missing entry |
| 3. history window | 2016-2025, fixed | a rolling window that includes the latest closed fiscal year |
| 4. forecasts | none | Bloomberg `BEST_` FY1-FY3 with the explicit override; SA fallback per cell, labelled |
| 5. missing rows | 5 rows ABSENT | the Bloomberg fields that carry them, pulled by the producer -- never computed on the page |
| 6. scores | one hand run of `run_scores.py` | computed when their inputs land |

---

## 5. The build, in dependency order -- round 14

No item includes a fleet run; each is proven on the validation names first.

1. **Move the unit map out of the worker's folder, and build it for every name.** The cheapest item on the panel, and it
   lifts all 348 refusals: dividend per share, free float and the two short-interest fields get their measured units for
   all 33. Rebuilding the map makes no data call beyond the fields it measures; re-deriving the blocks from the raw bytes
   already landed needs no new pull (stage `derive` reads raw back from S3 by design).
2. **Unfix the window.** Replace `HIST_END = "2025-12-31"` with the latest closed fiscal year.
3. **Forecast years:** the `BEST_` pull (FY1-FY3, override explicit), the SA fallback per cell, each cell sourced, and
   the page's forecast columns rendered with their period-end dates.
4. **The five missing rows** as Bloomberg fields in the producer's field list, each with its basis text.
5. **Robustness inputs** -- quarterly TTM and the missing fields -- is its own L4 question, since the ruled window is 8
   quarters and the block is annual.
6. **Cases**, when Andrew rules (s.3).
7. **Scores recompute** when their inputs land, not by hand.

---

## 6. Done means measured

| component | closed when |
|---|---|
| Refusals | REFUSE count 0 for a missing map entry across 33; any remaining refusal names a real unit or sign problem |
| Window | every block's newest fiscal year is the latest closed year for that issuer |
| Forecasts | FY1-FY3 on N of 33 per field, each cell labelled BBG or SA_FALLBACK, headers from `BEST_PERIOD_END_DATE` |
| Rows | 17 of 17 declared rows mapped to a field, or ABSENT with a stated reason |
| Instantiation | on each validation name, a block with no refused-for-map figure and no hand step |

---

## 7. Traps named in advance

- **A Bloomberg id without its yellow key is not a security.** 33 of 33 errors read as zero coverage.
- **`BEST_` fields without `BEST_FPERIOD_OVERRIDE` return the next QUARTER**, which looks like a plausible annual value.
- **Do not fill a not-meaningful cell.** A bank's EBITDA and a loss-maker's P/E are ABSENT by fact, not by gap.
- **Do not compute missing rows on the page.** `modelSheet.ts` refuses to, and should keep refusing.
- **A refused figure renders as a refusal, never its number** -- keep `refusalPresentation.ts` as the one path.
- **No monitor or freshness checker** comes out of this brief.

---

## 8. What this brief does not ask for

No seat is re-tasked and no run is made beyond read-only adapter reads, one scores object read, and three Bloomberg
reference requests over 33 securities (plus the one that errored). Nothing was written to any store.
