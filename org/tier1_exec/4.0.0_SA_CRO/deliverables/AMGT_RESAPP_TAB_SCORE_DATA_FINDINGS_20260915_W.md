# AMGT_RESAPP: CRO~W review of the five tab-score research calls

**Reviewer:** `4.0.0_SA_CRO~W`. **Date:** 2026-09-15, approximately 19:10–19:30Z.
**Status:** research findings from document/code review, four offline counterexamples and bounded live Bloomberg/S3 reads. Source and model limitations remain explicit below.
**Delivery:** canonical send was refused because this seat's launcher-owned heartbeat is absent. This local file is ready for CTO~W; delivery is not claimed.
**Push state:** LOCAL. Origin SITEZ observed at `6f09a06dc919bf21ef96b52aff5cd7e9608ccf85`.

## Authority and evidence boundary

Andrew's direct request in this Codex session, verbatim (exact arrival time unavailable; next clock read 19:09:44Z):

> CTO~W says youre not registered and they cant find you, but you need to review this and send it to them: org\tier1_exec\1.0.0_SA_CTO\deliverables\ANDREW_DIRECT_20260915_190xZ_FIVE_TAB_SCORE_CALLS_ANSWERED_BRIEF_TO_CRO_W_SEEKING_ALPHA_TO_CRO_Z.md

Read the entire named record and the linked `AMGT_RESAPP_TAB_SCORE_DATA_RESEARCH_BRIEF_20260915_W.md`, the CTO's
`AMGT_RESAPP_SUBSTRATE_MEASUREMENTS_20260915_W/TAB_SCORE_SOURCING_BLOOMBERG_LUSHA_MEASURED.md`, and the relevant checked-in instruments.
Repository HEAD observed during review: `fc8cdf1a1ed334eefa7434600e8b128121766573`.
Numbers attributed below to the CTO are their approximately 18:2x–19:0xZ measurements. New CRO measurements are explicitly identified.
The evidence folder `AMGT_RESAPP_TAB_SCORE_REVIEW_20260915_W/` contains exact query parameters, timestamps, raw responses and analysis.
Read-only Bloomberg requests and 33 S3 object reads were performed. No Lusha vendor calls, credentials, publisher reauthentication,
S3 writes or served-code changes in this review.
Seeking Alpha discovery remains with CRO~Z. No matching 20260915 Seeking Alpha/consensus/score findings filename was located in
the shared CRO deliverables folder during this review; that is a scoped local observation, not a claim about that seat's progress.
Exact inbox messages 23220, 23222 and 23225 subsequently arrived and were read; they confirm this research assignment and the separate
CRO~Z crawl. The content-specific ACK also failed the missing-liveness gate. Research proceeded under Andrew's direct request.

**My assessment:** keep the proposed factor architecture, but distinguish the intended economic quantity from its proxy and from
mere field availability. The current measurement scripts do not establish production-score coverage. Resolve the issues below
before using their counts as the basis for an addendum or presenting a high percentile as a favorable investment judgment.

## 1. Lusha and management tenure

**Andrew:** “Yes” to the bounded enrich; no emails or phones requested. His named metric is executives' time with the company.

### New code finding: an empty reveal list is omitted

`data/find/imo/scripts/_util/lusha_client.py:574-599` builds `{"ids": contact_ids}` and only inserts `reveal` when the list is truthy.
Therefore `contacts_enrich(ids, reveal=[])` sends no `reveal` field. The offline reproduction confirms this without a vendor call.
The official [combined-enrichment tutorial](https://docs.lusha.com/tutorials/sheets-contact) says omitting the filter returns all
available data. The separate [contact-enrichment tutorial](https://docs.lusha.com/tutorials/sheets-prospecting-contacts) excludes
rows with neither contact channel selected; it does not establish a position-only request. These are distinct endpoints: the first
tutorial's default is a warning, not proof of the second endpoint's precise defaults. The documented safe request for our exact
no-contact-data call remains unestablished. **The authorized stop condition applies; no enrich was attempted and the flag stayed off.**

Classification: **NOT_REACHED**, specifically an unestablished permitted request and a client that drops an explicit empty list.
This is not evidence that Lusha lacks employment dates. The [official overview](https://docs.lusha.com/guides) describes employment
enrichment, but does not guarantee the date fields or their coverage for these officers. Do not extrapolate a fictional fixture.

CTO prior population: 11/48 matched filing officers; 4/11 titles agree. Date agreement, same-company role history and per-officer
credit cost remain UNMEASURED. Zero calls here is not a zero-credit price quote for the intended batch.

**New Bloomberg measurement:** all 33 pool names return `COMPANY_EXEC_OFFICERS`, with a single bulk column `Executive Officers`.
There are no structured join/start-date columns in those responses. CFO role-start date is present for 32/33, COO for 22/33.
Dictionary searches under executive tenure, officer start, company join date and employment date found aggregate tenure and particular
officer-role fields, not an all-officer company-join field. Company-join dates are **NOT_CARRIED in the measured officer bulk shape**;
this does not assert they are absent from every Bloomberg product. Executive-position average, CEO company tenure and CEO role tenure
are available for 33/33 in the pool probes. Eighteen names have executive-average observations for all eight sampled years 2018–2025;
CEO-company tenure has 33/33. Neither history changes the executive-company-tenure definition gap.

### Definition mismatch to fix in the briefing

The CTO's own field description says `EXECUTIVE_AVERAGE_TENURE` is time in executive positions. That is not total time at the company.
Its reported 33/33 availability therefore does **not** establish 33/33 coverage of Andrew's chosen headline metric. CEO company tenure
is a one-officer measure, not an all-executive substitute. Average current-role tenure is a third distinct quantity.

Recommendation: retain separate metric IDs for company tenure, executive-position tenure and current-role tenure; show roster/date
coverage and date precision for each. Compare sources on the same officer roster. Preserve rejoin dates and employment gaps; do not
sum overlapping positions or count simultaneous roles twice. Annual join dates produce a tenure range, not fictitious day precision.
Bloomberg's executive-position aggregate can be shown as a clearly named available companion measure. No headline substitution is ruled.

## 2. CFPS/EPS dispersion for Divergence

**Andrew:** “CFPS or EPS is fine.”

**New measurement:** corrected peer identifiers were verified against returned names and company FIGIs. There are 111 distinct
member requests representing 110 companies; Alibaba's ADR and Hong Kong listing share a company FIGI. Counts below deliberately use
request/listing grain, not an inflated claim of 111 companies. `analysis.json` retains every security's values and exceptions.

| Population / period | CFPS spread | CFPS spread and N >= 4 | EPS spread and N >= 4 |
|---|---:|---:|---:|
| Pool, 1FY | 29/33 | 23/33 | 33/33 |
| Pool, 2FY | 29/33 | 23/33 | 33/33 |
| Peer members, 1FY | 103/111 | 92/111 | 111/111 |
| Peer members, 2FY | 104/111 | 92/111 | 111/111 |

The two 92-member qualifying lists are not identical. The named five all qualify under CFPS at both annual periods.
`BEST_PERIOD_END_DATE` is the valid mnemonic, found by dictionary search and served in the probes: the earlier `_DT` spelling was
**NOT_REACHED**, not unavailable period metadata. COST's 1FY currently ends 2026-08-31, before this retrieval; do not label every 1FY
response a future year or mechanically convert the 1FY/2FY pair into NTM.

**Recommendation:** evaluate CFPS first as the economically closer proxy, then evaluate EPS as a separately identified fallback.
Neither is the standard deviation of FCF. More EPS contributors do not make EPS dispersion an FCF statistic.

Two candidate conversions, with their meaning explicit:

```text
s_proxy_FCF = abs(F_cons) * sd(CFPS) / abs(mean(CFPS))
```

This transfers relative CFPS uncertainty to FCF by assumption. Matching mean and dispersion currencies cancel within their ratio;
the result inherits F_cons's units. A zero/near-zero CFPS mean needs its own guard. Illustrative, not measured company data:
FCF consensus 1,000 million and CFPS 10 +/- 2 gives a 200-million proxy denominator.

```text
sd(CFPS) * appropriately matched share count
```

This gives aggregate cash-flow dispersion in the units represented by CFPS; it does not automatically give free-cash-flow dispersion.
If FCF = operating cash flow minus capex, Var(FCF) also depends on capex variance and covariance. EPS-times-shares similarly gives
earnings dispersion. Establish diluted/ordinary/ADR share basis and estimate currency before multiplication, particularly BABA.

For NTM calendarization, do not add annual standard deviations. With weights a and b:

```text
Var(NTM) = a*a*s1*s1 + b*b*s2*s2 + 2*a*b*Cov(FY1, FY2)
```

Prefer contributor-level matched forecasts; otherwise disclose a covariance assumption and sensitivity or propose a fiscal-year
variant. BF fractional counts cannot stand for distinct analysts. A count guard on the proxy does not establish FCF contributor count.
Require actual period-end dates and a common as-of cut. Version scores by proxy so changing CFPS to EPS does not look like changed opinion.

### Five-name conversion arithmetic, newly measured

Scaled values below are in the native displayed units of FCF consensus. No USD conversion was applied. Full inputs, counts,
share multiplication alternative and 2FY results are in `analysis.json:five_name_scaling`; both annual periods were pulled.

| Name / 1FY end | Currency | FCF mean | CFPS mean / sd | FCF-scaled CFPS spread | FCF-scaled EPS spread |
|---|---|---:|---:|---:|---:|
| BA / 2026-12-31 | USD | 2,438.912 | 7.025 / 3.182 | 1,104.714 | 2,012.837 |
| COST / 2026-08-31 | USD | 7,770.752 | 32.798 / 4.338 | 1,027.792 | 67.726 |
| HD / 2027-01-31 | USD | 15,849.063 | 19.976 / 0.361 | 286.419 | 253.711 |
| SAP / 2026-12-31 | EUR | 9,782.657 | 8.828 / 0.778 | 862.133 | 298.277 |
| BABA / 2027-03-31 | CNY | -59,569.165 | 64.6975 / 18.488 | 17,022.524 | 5,269.962 |

Example: BA's relative CFPS scaling is `abs(2438.9119) * 3.182 / abs(7.025) = 1104.714`.
The alternative CFPS-sd times reported average shares gives BA 2417.684, COST 1926.007, HD 358.473, SAP 907.148 and BABA 42909.339
in cash-flow aggregate units; it is not FCF dispersion. COST's approximately 15-fold difference between the two relative proxies
shows why silently mixing EPS and CFPS scores would change their interpretation.

### Discovery and entitlement result

Dictionary queries for free cash flow estimates, free cash flow broker and free cash flow dispersion found the two FCF consensus fields,
but no direct FCF spread or broker-grid mnemonic in those searches. **No direct scalar spread was found in the searched dictionary;
global absence from Bloomberg is not established.** Crucially, actual broker-level alternatives exist and were reached:
`BEST_CPS_BRK_GRID` and `BEST_CAPEX_BROKER_GRID`, with current/next-period values and dates.

| Name | Numeric CPS broker rows / all rows | Numeric capex broker rows / all rows | Matched numeric CPS+capex brokers |
|---|---:|---:|---:|
| BA | 0/4 | 5/22 | 0 |
| COST | 0/6 | 5/29 | 0 |
| HD | 1/8 | 5/29 | 1 |
| SAP | 1/15 | 2/29 | 1 |
| BABA | 17/26 | 33/48 | 17 |

Every remaining current-value cell in these grids explicitly says **PERM DENIED**: **NOT_ENTITLED**, not missing source coverage.
This is a positive-control route with both served and denied observations. Header rows are excluded from these denominators.
Bloomberg documents calculated FCF as CPS times reported average shares plus negative capex. Matching the entitled BABA brokers
therefore opens a reconstruction path; the saved diagnostic computes it, but forecast share basis, date freshness, provider criteria
and contributor eligibility are not yet validated, so its dispersion is not promoted to s_cons. Four of five names cannot reach
the four-estimate guard through this matched route under current access.

## 3. Seeking Alpha consensus and the independent house forecast

**Andrew:** “Ask CRO~Z to explore Seeking Alpha with an authenticated crawl, they should have consensus figures.”

Seeking Alpha's consensus can improve F_cons or estimate coverage. It cannot alone supply the independent F_model against which that
same consensus is compared. A second website is not proof of a second contributor population. CRO~Z should return field definitions,
periods, contributor counts, vendor provenance and retrieval evidence; no duplicate crawl was run here.

The prior card reports 17 historical model blocks and no house forecast. The scoped local code search found
`integrations/bloomberg/research/model_block_pull.py`, and no separately named model/forecast producer in `lib/research` or
`integrations/bloomberg/research`; this is not an exhaustive estate-wide absence claim. The D guard remains unsatisfied on the evidence available.

Proposed producer: independently seed revenue drivers, operating margins, cash taxes, capex and working-capital assumptions from
dated filings, operating history and documented business evidence; compute a consistently defined forecast FCF; only then compare
against consensus. Store each assumption, source and timestamp. Quant scores, author forecasts and analyst revisions have distinct
provenance and are not automatically independent house inputs. Do not fabricate divergence by perturbing consensus.

Keep `sd(D) < 0.25` as the recorded predeployment diagnostic; my recommendation to Andrew is to review its interpretation, since low
dispersion can reflect genuine agreement or an overlarge denominator as well as consensus copying. It is not proof of predictive
failure. Evaluate forecast-error improvement and directional disagreement out of sample using archived vintages. A high D means
greater house optimism relative to its chosen denominator; it does not establish accuracy or undervaluation.

## 4. Discovery, Robustness eligibility and percentile populations

**Andrew:** “Make sure that in any of these cases that you have robust discovery mechanisms, want to make sure we aren't missing things because of how the data is pulled versus lack of coverage itself. In any case, we will have to reorient around data availability.”

### New instrument finding: history count is not score eligibility

In `robustness_coverage.py`, `last_n_complete(sec, needed, n)` never uses n to select a window. It counts all matching dates anywhere
in the response. The offline counterexample passes its eight-observation gate with alternating missing quarters and the latest quarter
missing. The instrument does not construct the eight TTM observations, validate fiscal-period semantics, apply the model's domain
guards, validate thresholds or produce transformed headroom/sigma/S. Quarterly HistoricalData sampling alone does not prove the field
contains that fiscal quarter's flow; summing four samples is only valid after confirming the field's fundamental-period semantics.

Thus **3/33 is the CTO's raw field-count eligibility result, not a verified rankable-score count**. The instrument's historical
result can also be stale because the latest observation need not exist. Its x3 substitutes 24-month principal for 24-month obligations;
those are different definitions unless Andrew explicitly scopes obligations to debt principal. Annual ladder values sampled repeatedly
do not become eight independent disclosures. All these are **NOT_REACHED** validation or input-definition gaps, not demonstrated source absence.

Reorientation must follow a corrected availability matrix. Under the CTO's reported raw count distribution (11 names at zero,
8 at two, 11 at three, 3 at five), reducing the constraint minimum from five to four would still leave 3/33 eligible by that count.
It does not solve coverage. Reducing to three would give 14/33 by the same unvalidated count, while materially weakening the model.
An annual variant needs its own measured history, calibration and resulting count; those cannot be derived from this card.

### New discovery and corrected-period measurements

Bloomberg **does carry customer-revenue percentages**: `SUPPLY_CHAIN_REVENUE_PERCENTAGE`, the matching column in
`SUPPLY_CHAIN_CUSTOMERS_ALL_DATA`, and `SUPPLY_CHAIN_SUM_TOP_REVENUES` with count override 1. The scalar serves 21/33 names now.
BA is 34.78%, BABA 2.4%, SAP 1.0%. This overturns the prior current-input absence claim: **NOT_REACHED** by the earlier ticker-only route.
The field covers disclosed customers and warns that it may differ from company disclosure. It is not automatically the largest
customer from a complete TTM population. The count override also limited the bulk response to one customer; these samples cannot
prove exhaustive customer discovery. Eight-observation history was not returned through HistoricalData at either sampled frequency.
Do not carry today's relationship back into historical quarters. Some scalar failures report not applicable to the request, not an
economic determination about customer concentration.

The dictionary also establishes `FUND_PER` defaults to last fiscal year; `Q` selects quarterly fundamentals. A corrected read with
`FUND_PER=Q` and the latest completed calendar-quarter window through 2026Q2 gives the following **input-window counts**, before
fiscal/publication-date alignment, TTM construction, domain guards, sigma and thresholds:

| Input combination | Default FUND_PER | Explicit Q |
|---|---:|---:|
| EBIT and interest, 11 consecutive samples | 9/33 | 12/33 |
| Net debt and TTM EBITDA, 8 | 17/33 | 21/33 |
| Cash, facility and two principal years, 8 | 1/33 | 2/33 |
| Two principal years and total debt, 8 | 1/33 | 2/33 |
| TTM FCF and sales, 8 | 16/33 | 20/33 |
| Top-disclosed-customer scalar, 8 | 0/33 | 0/33 |

Only INTU has five of these input windows after the Q correction; lowering n to four still gives one, lowering to three gives 12.
These are **not S score counts**. Explicit annual fundamentals across 2018–2025 improve the principal-based x3 window to 6/33 and
x4 to 7/33, but using the same TTM-field requests leaves zero names with five windows. An annual strategy needs native annual
flow inputs and recalibration; simply changing the frequency is insufficient. No unmeasured improvement is promised.

The exact 24-month obligations input remains unresolved: dictionary results group years 2 and 3, not a separate year 2. Half of that
group is not a measured year-2 obligation. `BS_CONTRACTUAL_OBLIG_YEAR_2` was an invalid candidate, not a coverage failure. Moreover,
the documentation for the principal fields refers to municipal disclosures even though equity values are returned. Resolve that
definition inconsistency before using the values as corporate maturity inputs.

**EMPTY peers audited:** all 23/33 have explicit missing subject classification/header or unresolved scanner-join reasons.
They are **NOT_REACHED**, not evidence that the company has no comparable peers. The peer universe code documents stale scanner
vintage and unconverted non-USD model-header caps, both relevant to a size-band audit. Do not weaken peer rules to work around these
input defects. A bounded subject-header/identity repair is the first reorientation; its future member counts have not been fabricated.

### Population recommendation

Separate the analyzed-company ranking pool, the per-subject peer set and the statistical calibration universe. A peers/v1 object,
especially an EMPTY one, is a discovery denominator; it does not establish that a company has completed analysis or the metric.
Deduplicate companies across listings and filter by metric version and usable date before ranking.

**New sector census of the 33:** Consumer Staples 6, Financials 5, Information Technology 5, Energy 4, Utilities 4,
Consumer Discretionary 3, Communication Services 3, Health Care 2, Industrials 1. This corrects the earlier one-to-four summary.
Under the illustrative endpoint rank formula (rank-1)/(N-1), N=1 is undefined, N=2 has only 0/100, and N=4 has 0/33/67/100.
A minimum sector size of 5 would include 16/33 names before metric eligibility; a minimum of 8 includes 0/33.
A broad scanner population may eventually support sector calibration, but
2,851 identities are not 2,851 available Robustness histories or forecast estimates. Do not count them as calibration coverage.

Recommendation for discussion: show absolute scores with coverage now; compute whole-analyzed-pool percentiles only under an explicit
approved population rule, and defer sector percentiles until a declared minimum is met. A global fallback must be labeled; silently
mixing sector and global ranks is not acceptable. Sector adjustment and whole-pool ranking can coexist if separately defined and validated.

## 5. Subject capping in Peers V

**Andrew:** “Yeah sure” to capping the subject at its peers' bounds. Implement in the future score producer exactly at the measure stage:

```text
lo, hi = percentile(raw_valid_peers, 5), percentile(raw_valid_peers, 95)
peer_w = clamp(raw_valid_peers, lo, hi)
subject_w = clamp(raw_subject, lo, hi)
z = (subject_w - median(peer_w)) / sample_sd(peer_w)
V = mean(eligible_z)
```

Exclude the subject and deduplicate company identities before constructing the bounds. Preserve raw and capped values plus bounds.
The existing feasibility script has no subject clamp. This review fetched new raw values, retained the original instrument's proxy
measure calculations to isolate the cap effect, and saved precise bounds, z values and contributions. Five corrected identifiers
(Toyota, Fast Retailing, Nestle, Infineon, MediaTek) resolve all seven previously wrong/invalid member rows; returned names were
reviewed for all 111 requests and company FIGIs enforce self-exclusion/deduplication. Each of these ten sets has 12 distinct peer companies.

| Subject | Uncapped V on corrected identities | Capped V on same values | Largest absolute contribution share |
|---|---:|---:|---:|
| BA | -0.922 | -0.404 | 33.2% |
| BABA | 3.541 | 0.605 | 33.0% |
| COST | -0.532 | -0.510 | 28.4% |
| HAL | 0.263 | 0.012 | 23.3% |
| HD | 0.183 | 0.183 | 30.4% |
| INTU | 1.482 | 1.482 | 26.8% |
| KMB | 0.248 | 0.248 | 32.7% |
| NU | -0.823 | -0.817 | 49.4% |
| SAP | 0.424 | 0.433 | 41.3% |
| VLO | 1.376 | 1.364 | 28.1% |

All ten pass the instrument's K/M gates; BA uses five measures, NU three, the others six. No name has a single measure above half
of total absolute contribution after capping. This is a **cap feasibility comparison**, not production qualification of the proxy
measure definitions. Do not compare the new uncapped column against the prior card as a cap-only delta: identities and data vintage changed.

Two additional offline counterexamples show why capping alone is insufficient:

- Missing buybacks plus known dividends still yields measure 3: the script substitutes zero for the absent component.
- Negative trailing EBITDA plus a positive forward EV/EBITDA still yields measure 4. Forward and trailing bases are interchanged;
  eligibility must use the same period as the chosen measure and the agreed EBITDA guard.

The script also derives inverse-PEG growth from trailing/forward P/E, rather than requesting a separately defined NTM EPS-growth
input, and uses fiscal-year buybacks alongside trailing dividends. These are **NOT_REACHED** contract-fidelity gaps. Missing negative
E/P can require direct EPS/price reconstruction with currency/share-basis checks, not a positive-P/E-only inversion.

The saved capped rerun reports each measure's signed z and `abs(z_m)/sum(abs(z))`, plus leave-one-measure-out V.
“More than half of V” alone is unstable when positive and negative measures cancel. Capping bounds an outlier but does not guarantee
balanced contributions or remove overlap between correlated valuation measures.

## Summary for CTO~W

| Score | Available evidence | Computable count this review establishes | Recommendation / remaining measurement |
|---|---|---|---|
| Management: executive company tenure | 33/33 executive-position aggregate and officer lists, no structured join dates in the bulk | Headline company-tenure coverage unverified | Available companion aggregate 33/33; permitted Lusha request and roster-level coverage remain open |
| Robustness | Corrected Q input windows 12/21/2/2/20/0; customer scalar 21/33 now | One name with five input windows; no verified S count | Minimum four still one; minimum three gives 12 input-window candidates, requiring a changed model; annual-frequency-only change does not solve it |
| Peers V | Corrected identities, ten capped feasibility scores; 23 EMPTY causes identified | 10/33 cap-feasibility outputs, not contract-correct V qualification | Fix subject metadata for other 23; harmonize proxy periods and missing-value treatment |
| Divergence D | CFPS >=4: 23/33; EPS >=4: 33/33 at each year; BABA 17 accessible matched broker pairs | No supported D today without house forecast | CFPS-first proxy with coverage, explicit units/vintage; independently seeded forecast; CRO~Z evidence pending |

**What remains open:** a documented no-contact-data Lusha request (the brief's stop condition prevented the call); CRO~Z's separate
Seeking Alpha findings; all-executive company-join dates; exact 24-month obligations and historical customer concentration; final
fiscal/publication-date alignment and score calibration; forecast-share and currency basis for broker reconstruction; the independent
house forecast producer. The requested bounded discovery, annual dispersion matrices, five-name arithmetic, EMPTY-peer/sector census
and capped feasibility comparison are supplied. Source-wide absence is not asserted where the evidence cannot distinguish coverage
from access, request semantics or undiscovered routes. No round-11 specification or production setting was changed.

## Reproduction and runtime defect

Run `python org/tier1_exec/4.0.0_SA_CRO/deliverables/AMGT_RESAPP_TAB_SCORE_REVIEW_20260915_W/reproduce.py`.
Four offline counterexamples passed; the script extracts only named AST functions and prints source SHA-256 values. It runs no
top-level vendor code. These are synthetic behavior checks, not live coverage results.

`codex-seat-status.ps1 -Serial '4.0.0_SA_CRO~W'` measured RED: heartbeat `pids=[]`, liveness absent. App-server
`ws://127.0.0.1:55183`, bridge PID 42920, detector PID 40996, bound thread `01a0a28e-b65b-7e62-abe3-39ddf550523d` were alive.
`.runtime/codex-seats/4.0.0_SA_CRO~W/heartbeat.stderr.log` records an uncaught `PermissionError [WinError 5]` in
`server.py:_locked_liveness`, replacing `org/mcp/liveness.json.tmp` with `liveness.json`. The formerly registered heartbeat PID was 19296.
The observed exception establishes the immediate failure; it does not establish which competing process or filesystem condition caused it.

Canonical ACK send failed: `codex-send REFUSED: 4.0.0_SA_CRO~W has no fresh liveness entry (age=ABSENTs)`.
The repository's `org/mcp/CODEX_INBOX_MONITOR.md` assigns heartbeat lifecycle to the launcher and forbids alternate helpers. No liveness
record was fabricated, no send gate bypassed, and no duplicate helper started. Delivery and Andrew-direct broadcast remain blocked
until the canonical launcher registration is restored. This is a runtime defect, not a missing serial or a reason for Andrew to repeat it.
