# RESEARCH -- the security swap, and running the Analysis Request with no YCharts at all

**archetype:** EXPLORE
**Author:** 4.0.0_SA_CRO~DELL2, 2026-10-09 ~04:4xZ to 05:1xZ
**Ask:** Andrew-direct, in-session (two messages, verbatim at the end).
**Read:**
- `infra/aws/lambda/investor-reporting/intake/{resolution_kimi,upload_suggestions,security_resolution}.py`
- `infra/aws/lambda/v2_portal/_shared/etf_classification_model.py`
- `org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md` (FWD-16, S31, S32)
- `org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md`
- the live DynamoDB `etf-classifications` table (full scan, 11,361 of 11,361 rows, read-only)

## Answer

**How the swap works today:** it does not run.
- `KimiAdvisory.call("swap", ...)` (`resolution_kimi.py`) returns `KIMI_WEB_SEARCH_UNVERIFIED` until a web-search tool
  configuration is QA-pinned.
- Even when it runs, it asks Kimi to *propose* up to three ETFs itself (prompt at `resolution_kimi.py:~50-58`). That is the
  wrong way round from Andrew's gist: the proxy must come from Opal's own registry, not from the model.
- The only part that runs today is the **typo check** (`upload_suggestions.py`). Kimi suggests a ticker, and **YCharts'
  `securities_info`** verifies it. So the check depends on YCharts too.

**Andrew's method fits pieces that already exist.** Of its four steps, the existence check, the classification and the
registry are built. Only the yfinance checker and the proxy pick need writing (section 2).

## 1. What already exists for each step

| Andrew's step | What exists | Where | Gap |
|---|---|---|---|
| Does Opal already know the security? | the registry, hash key `ticker`, 11,361 rows (equity 7,151; fixed income 2,901; structured 527; cash 381; alternatives 239; commodities 162); MDPF_SECHIST's per-security price series | `etf-classifications` (GSIs `asset-class-index`, `sub-asset-class-index`); MDPF_SECHIST C-SERIES | the check reads YCharts today, not these (IRPT_YCDGEN S31 plans the move, unbuilt) |
| If not, does yfinance have it? (the checker) | yfinance 1.7.0 is installed on dell1; Yahoo egress is open on every box (law edit 4d77a9c3ea) | the backfill pattern in `RESEARCH_20261008_COTTONWOOD_YAHOO_PRICE_BACKFILL_STRUCTURE.md` | no live per-security check in the upload path |
| If not, classify it with the SECCLASS taxonomy | `etf_classification_model.py`: Kimi K3 gets the name and ticker only, returns `asset_class` from the six classes (cash, fixed_income, equity, structured, alternatives, commodities) and a `sub_asset_class` from the live table's own vocabulary. Confidence below 0.80 is FLAGGED, never held. An out-of-vocabulary reply is refused to null | MDPF_SECCLASS (C-TABLE, C-BOUND) | no web search: it classifies from the name alone. Andrew's "quick google search" is the missing input |
| Pick a registry ETF as the proxy | 193 rows with `instrument_kind = fund`, 197 `classified_by = seed`: the core ETFs, each with a class and sub-class (SPY, IVV, VOO -> equity / US Large Cap; IWM -> US Small Cap; EFA, IEFA -> Developed; VWO, EEM -> EM; AGG, BND -> fixed_income / Intermediate; HYG -> High Yield; MUB -> Municipal; SHY -> Short Duration; BIL, SGOV -> Ultra Short Duration; TIP -> TIPS; GLD, IAU -> commodities / Metals; DBC -> Commodities; USO -> Oil; VNQ -> alternatives / Real Estate; JEPI -> structured / Options Income) | `etf-classifications` | no proxy rule; coverage gaps below |

**Coverage, measured.**
- The registry has 40 distinct (class, sub-class) pairs; 25 of them have at least one fund row.
- With no fund row: cash, all 3 sub-classes (Cash, Money Market, T-Bill); equity, 10 of 18 (sector-named sub-classes
  such as Financials, which carry single stocks only); alternatives, the null sub-class; fixed income, 1 of 11.
- `instrument_kind` is set on only 1,003 rows (10,358 null). So "is this row an ETF?" cannot be read from the table
  except for the seeded core.

## 2. The recommended method (one pass per unknown holding)

1. **KNOWN?** Look the ticker (or CUSIP) up in `etf-classifications` and in MDPF_SECHIST.
   - Found with prices: use it; no swap.
   - A typo (the existing Kimi `check`): verify the suggestion against **the registry and yfinance**, not YCharts.
2. **YFINANCE CHECKER.** One yfinance call for the symbol, giving `info` (quote type, long name, category) and the price
   history.
   - **Has history:** the security is real and Opal can price it itself. Add a registry row (classified by step 3,
     `identifier_namespace = TICKER`) and land its prices in MDPF_SECHIST (C-SERIES). No swap; the client keeps the
     real holding.
   - **Paced** per the backfill structure's gentle schedule. One symbol per call; an Analysis Request carries few
     unknowns, so this is seconds.
3. **CLASSIFY (only if yfinance has nothing).** Run Kimi K3 with web search: the existing `etf_classification_model`
   prompt plus the search tool, so the "quick google search" feeds it.
   - Output: `asset_class` and `sub_asset_class`, bound to the live vocabulary (C-BOUND), plus the sources used.
   - Below 0.80 confidence, the result is FLAGGED on the row (Andrew's standing word: a flag, not human review).
   - Two existing pieces make one: SECCLASS's classifier gains the search tool, and `resolution_kimi`'s swap prompt
     is retired.
4. **PROXY (deterministic, no model).** From the registry, choose the proxy for that (class, sub-class):
   - a **designated proxy** per pair, a small fixed table of one seeded core ETF per pair (for example US Large Cap ->
     VOO; Intermediate -> AGG; Metals -> GLD);
   - else the parent class's default (equity -> VT or VOO; fixed income -> AGG; cash -> SGOV or BIL; alternatives ->
     VNQ; commodities -> DBC; structured -> JEPI);
   - the proxy must have prices in MDPF_SECHIST;
   - the 15 pairs with no fund row fall to the class default until a proxy is designated.
5. **RECORD.** The holding stays named as the client named it. Its row carries `proxy_for: <original>`,
   `proxy: <ETF>`, `method` (`KNOWN` / `YFINANCE` / `KIMI_CLASSIFIED+PROXY`), `confidence`, `low_confidence` and
   `sources`. In the form, the advisor sees "X is not priced; analysed as VOO (US Large Cap)" and can accept or change
   it before filing. That is IRPT_ANLREQ FWD-2's security swap.

**Why this order:** yfinance first keeps the client's real holding wherever it can be priced, and each step is cheaper
than the next. Kimi runs only for genuinely unknown securities. The proxy pick has no model in it, so it is repeatable
and auditable.

## 3. No YCharts anywhere (Andrew's second message)

**Agreed; the pieces are mostly there.**
- IRPT_YCDGEN mapped all three report types' elements from the captured YCharts exchange (task orders YCD-m-1 Overview,
  YCD-m-3 Comparison and Multi, YCD-m-2/4/5 charts, labels, residuals).
- The Opal engine produces the Overview with zero YCharts calls.
- Its price-based elements print `NOT_IN_THIS_VERSION` only because v1 has no prices (C-V1).

What still touches YCharts, and how each goes:

| Today | Replace with | Owner (IRPT_ANLREQ C-ABSORB) |
|---|---|---|
| symbol resolution via `securities_info` (`intake/resolution_broker.py`), with the session EVICTED since 10-05 | step 1 of section 2: the registry, then yfinance (IRPT_YCDGEN S31) | ~Y2, `intake/*` |
| typo-check verification via `securities_info` (`upload_suggestions.py`) | the same: registry, then yfinance | ~Y2 |
| the swap (Kimi proposes ETFs, refused) | section 2 steps 3-4 | ~Y2 with MDPF_SECCLASS |
| price-based report elements (returns, risk, comparisons) | MDPF_SECHIST series (Bloomberg plus Yahoo), plus yfinance for a missing one | ~G2 engine reads SECHIST |
| the vendor generation path (resident to YCharts, 21 PDFs) | retired (IRPT_YCDGEN FWD-11) once the Opal engine renders the three types with prices | ~G2 |

**The one real dependency:** comparisons and benchmarks need the comparables' and the holdings' daily prices in
MDPF_SECHIST. The Opal models' and the seeded ETFs' series are the first to backfill, since every comparison uses them.
The price backfill is now owned by MDPF_SECHIST, but MDPF_DEMQUE also claims it (consolidation research @53e1588f09,
section 5.2). One owner is needed first.

## 4. Changes this implies (for the CTO; nothing built here)

1. IRPT_ANLREQ FWD-2's security swap reads as section 2: known, then yfinance, then classify with search, then the
   designated proxy. A PRD wording bump.
2. MDPF_SECCLASS: one designated proxy per (class, sub-class), on the seeded rows, plus the class defaults. The
   classifier gains the web-search tool (the `resolution_kimi` swap's QA pin becomes this one tool's pin).
3. IRPT_YCDGEN S31 (verification off YCharts) and S32 (candidates from the registry) are the cells this fills.
   IRPT_ANLREQ already absorbs both.
4. A YCharts retirement line: the date YCharts is no longer called by any Analysis Request hop, graded by a request
   whose trace shows zero YCharts calls end to end.

## Andrew-direct -- verbatim record

Channel: this seat's dell2 terminal, in-session, 2026-10-09 ~04:4xZ.

> Also on the security swap item, i want you to look into how this actually works. what the gist of it should be is
> something like "check security exists, if not, run a quick google search on it to assess asset class/sub-asset class
> (using SECCLASS taxonomy), then select an ETF that can act as a proxy that is in the registry.

> Yeah I do not think we actually need YCHARTS for anything. we should have been able to figure out by this point based
> on the YCharts 4 API calls that get made prior to YCharts generating their export, we should have already parsed
> YCharts export packet and figured out exactly what they use what figures to generate, thereby we do it all in house. I
> know this was the entire point of the YCDGEN project, but now that we're expanding our securities backlog via SECCLASS
> and SECHIST and all that, it seems like we should be able to manage even the price stuff internally. I think theres
> probably room here to pull off a yfinance call for the given missing security if absolutely necessary, thats
> effectively the checker, if yfinance doesnt have it then we do the Kimi process to match to something we have the
> data for already,.
