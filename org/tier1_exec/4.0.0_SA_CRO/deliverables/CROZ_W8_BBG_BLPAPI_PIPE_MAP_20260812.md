# W8 — BBG blpapi pipe map: what is served where, and how

**Author:** `4.0.0_SA_CRO~Z` · **Started:** 2026-08-12 ~1710Z · site Z (the Terminal box)
**Authorization:** Andrew-direct ~1702Z @`f09cbd13ef`, relayed `0.0.0_AB_MSTR~Z` 170523Z.
**Egress scope:** TRAVERSE + READ ONLY. Downloads expressly forbidden. Verification pulls are a
separate, sized ask.

> **METHOD DECLARATION — READ THIS BEFORE ANY NUMBER BELOW.**
> Every increment states its own DENOMINATOR: how many of how many, **by what instrument**, and
> what that instrument is blind to. A map that resumes cleanly but cannot say what fraction of the
> surface it covers reads complete and is not — and its author is the one person who cannot tell.
> **Nothing in this file was produced by a data pull.** Sources are: on-disk source read, `comp-find`,
> and prior committed measurement (cited with its vintage). Where a fact is inherited rather than
> re-measured, it is marked `INHERITED` with its date — an inherited measurement is a claim about
> the past, not the present.

---

## 0. STATUS / RESUME POINTER

| Increment | Covers | State |
|---|---|---|
| 1 | Ingress: services, request types, session-openers, transport | **LANDED** @`52f215db0f` |
| 2 | The request universe + the BBG-origin join over served surfaces | **LANDED** (§8-§10) |
| 3 | Consumer/entitlement reconciliation + the sized-pull proposal (if any) | NOT STARTED |

**If this session died, resume at increment 3.** Nothing below needs re-deriving.

---

## 1. THE PHYSICAL PIPE — there is exactly one, and it is loopback

```
   Bloomberg  ──────>  bbcomm.exe  ──────>  127.0.0.1:8194   (DAPI, loopback ONLY)
                       (service)             │
                                             │  every consumer below crosses THIS ONE socket
                     ┌───────────────────────┴────────────────────────┐
                     │                                                │
              blp_client.py                                   cma env  (tia / blpapi)
           (.tools/bloomberg-mcp)                        Yang's notebooks + repo forks
                     │                                                │
              server.py (FastMCP "bloomberg")                   run_daily_pull.py
                     │                                                │
        stdio ───────┴─────── streamable-http 127.0.0.1:8790     data/model PKL
     (local Claude Code)        (SSM port-forward; NOT built)          │
                                                                (increment 2)
```

**The load-bearing property: DAPI binds `127.0.0.1`, never `0.0.0.0`** (`INHERITED`, measured
2026-07-30, NFRA_BBGMCP_PRD §1). No VPN, peering, or security-group change reaches it — **something
running ON this box must make the blpapi call.** Every remote-access design that forgets this fails
at the same place. This is why the tunnel terminates locally rather than exposing a port.

---

## 2. SERVICE AXIS — denominator 6, and we open 1

`INHERITED` — all six measured by live `openService()` on this seat, 2026-07-30
(NFRA_BBGMCP_PRD §4.2). **I did not re-probe; re-probing is a live call and the map does not need
it.** Vintage caveat: 13 days old, and §1 of that PRD explicitly warns a seat's entitlements can
change with nothing reporting it.

| Service | Open on this seat | Opened by our code | Note |
|---|---|---|---|
| `//blp/refdata` | True | **YES — the only one** | BDP / BDH / BDS / IntradayBar / IntradayTick / BEQS / Portfolio |
| `//blp/apiflds` | True | no | field discovery; PRD calls it highest-value unbuilt |
| `//blp/instruments` | True | no | security resolution |
| `//blp/tasvc` | True | no | technical studies; no demand |
| `//blp/mktdata` | True | no | streaming; **excluded BY DESIGN**, not overlooked (push-shaped vs request/response MCP) |
| `//blp/emsx` | **False** | never | order/trade. **Not reachable from this seat at all.** |

> **THE READ-ONLY PROPERTY IS AN ENTITLEMENT FACT, NOT ONLY A CODE CONVENTION.** `//blp/emsx` is
> structurally absent, so the blast radius of a client bug is bounded by Bloomberg and not merely by
> our restraint. **This must not be used to weaken the code convention** — entitlements can change
> silently — but it is the strongest single safety fact on this box.

**Blind spot of this axis:** `openService` answers *reachable*, never *entitled for a given
security*. Those are different questions and the second has already burned this estate (see §5).

---

## 3. REQUEST-TYPE AXIS — denominator 7 named on refdata, 3 implemented

Source-confirmed by direct read of `.tools/bloomberg-mcp/blp_client.py` @`f09cbd13ef` (this box, today).

| Request type | Implemented | Where | Pull class under W8 |
|---|---|---|---|
| `ReferenceDataRequest` (BDP) | YES | `blp_client.py:153` | traversal-permitted **BY CALL SHAPE, not by name** — see below |
| `ReferenceDataRequest` w/ bulk fields (BDS) | YES (same call) | `_el_to_py` array branch `:105` | same |
| `HistoricalDataRequest` (BDH) | YES | `blp_client.py:211` | **PULL — sized ask required** |
| `IntradayBarRequest` | YES | `blp_client.py:265` | **PULL — sized ask required** |
| `IntradayTickRequest` | NO | — | docstring once claimed it; never existed |
| `BeqsRequest` (screens) | NO | — | proposed |
| `PortfolioDataRequest` (PORT) | NO | — | proposed |

> ### ⚠ THE EGRESS LINE SITS ON THE CALL SHAPE, NOT THE TOOL NAME.
> The constraint as issued draws the boundary at the tool name: historical/intraday are pulls,
> health/reference are not. **That line is not sufficient, and I am recording why before making a
> single call.** `reference_data` sits on the permitted side and can still harvest content if asked
> enough times with a wide enough field list — N securities x M fields, iterated, is a data
> acquisition conducted entirely through "allowed" calls, and a tool-name rule **reads GREEN on it.**
> **OPERATIVE RULE FOR THIS SEAT:** `reference_data` is used for SCHEMA/METADATA resolution only
> (does this identifier resolve, what is this field's shape). The moment a call's purpose is to
> obtain the values themselves, it is a pull — it stops and gets sized.
> *(Elevated by `0.0.0_AB_MSTR~Z` 170828Z as an amendment to CTO~Z's constraint 3, credited here.)*

**Session model:** every public function opens a session, runs ONE request, and stops
(`blp_client.py:150,208,262`). Correct for today; the PRD flags it as the first bottleneck under
concurrent gateway callers.

---

## 4. SESSION-OPENER AXIS — who can actually touch the socket

**Denominator by instrument:** `comp-find "blpapi"` -> **53 hits across 25,663 files scanned, 1
UNREADABLE and not searched**; bands DEF=6, SURFACED=21, DOC=26. `comp-find "//blp/"` -> 35 hits,
bands HEAD=3, SURFACED=6, DOC=26.
**What this instrument is blind to:** it counts LINES in the tracked repo. It cannot see Yang's
live OneDrive notebooks (out of repo, and they are the production source), and per CLAUDE.md Rule 21
a comp-find count is never an AST-node denominator.

| # | Session opener | Env | Path | Role |
|---|---|---|---|---|
| 1 | `blp_client.py` | MCP server env | `.tools/bloomberg-mcp/` | the agent-facing surface (4 MCP tools) |
| 2 | `bloomberg_entitlement_probe.py` | `cma` | `org/tier0_utility/0.0.3_BG_BBGTerminal/deliverables/` | the 3-layer entitlement discriminator |
| 3 | Yang notebooks via `tia` | `cma` | `workflows/bloomberg/{tplus1,tzero}/src/` | the production daily pull (repo forks) |
| 4 | Yang notebooks via `tia` | `cma` | OneDrive `202511 Model Portfolio Exposure/src/` | **the live production source — OUT OF REPO** |

**TWO INTERPRETERS, DELIBERATELY** (`scheduled_daily_pull.cmd:77`): the pull needs `cma`
(`C:\Anaconda\envs\cma\python.exe`, has tia/blpapi); the publisher needs boto3, which `cma` does not
have, so it runs under Python311. **A green `bloomberg_health` from the MCP server therefore does
NOT prove a runnable pull** — different interpreter, different process, different session. This is a
live instance of "the instrument's domain is not the question asked."

---

## 5. WHAT NO INSTRUMENT ON THIS BOX CAN TELL YOU — the entitlement blind spot

This is the single most important thing in increment 1, and it is a NEGATIVE result.

`INHERITED`, measured, from `BLOOMBERG_TERMINAL_SIGNIN_RECOVERY.md` (P0 block, 2026-08-12):

| Date | `bbcomm` | `wintrv` | `bloomberg_health` | Entitlement | Lesson |
|---|---|---|---|---|---|
| 2026-08-11 | up | dead | `ok:false` | **DEAD** 12.5h | a running `bbcomm` is **not sufficient** |
| 2026-08-12 | up | **absent** | `ok:true` | **LIVE** | a running `wintrv` is **not necessary** |

**`bloomberg_health` read cleanly through both states, so it cannot discriminate either.** It is an
instrument that could not have said otherwise. Neither the process list nor the health check answers
*"is the entitlement live."*

> ### ⛔ THE ONLY DISCRIMINATING TEST IS ITSELF A PULL — AND SO I DID NOT RUN IT.
> The runbook's sole proven discriminator is resolving the `.ST` custom index: a
> **HistoricalDataRequest** expecting ~683 rows from inception `2023-12-29` @ `100.0000`.
> **Under W8's constraint that is a DATA PULL requiring a sized ask.** So the map records the
> honest state: **the entitlement is UNVERIFIED BY THIS SEAT, and verifying it is out of scope
> without a separate authorization.**
> I did **not** substitute `bloomberg_health` for it — a clean `ok:true` is exactly the
> could-not-have-said-otherwise reading that produced the 12.5h outage's false comfort.
> **And I did not attempt a Terminal sign-in:** `wintrv` is absent today, the P0 gate states plainly
> that absence is NOT evidence a sign-in is needed, a failed login is not free, and Bloomberg locks
> the account on repeats. Acting on the natural inference here converts a non-problem into a lockout.

**Standing gap, quoted from the runbook and NOT to be closed with a monitor:** *"Nothing detects a
dead Terminal."* The 07:00 ET scheduled pull has no DAPI-liveness precondition. Per the standing
alarm moratorium this is a **route/schedule design question**, and an alarm is the wrong deliverable.
Already routed to MSTR~Z for CTO/Andrew disposition — I am not re-opening it, only recording that
the pipe map's health axis terminates here.

---

## 6. INCREMENT 1 COVERAGE STATEMENT (the denominator of the map itself)

| Axis | Enumerated | Of | By instrument | Confidence |
|---|---|---|---|---|
| blpapi services | 6 | 6 | live `openService` probe, `INHERITED` 2026-07-30 | high, **13d stale** |
| refdata request types | 7 named / 3 built | 7 | source read @`f09cbd13ef`, today | high |
| in-repo session openers | 3 | 3 | `comp-find`, 53 hits / 25,663 files | high |
| out-of-repo session openers | 1 known | **UNKNOWN** | none — structurally invisible to repo tooling | **LOW — see below** |
| transport paths | 3 (stdio, http:8790, SSM) | 3 | source read + PRD gates | high; 2 of 3 NOT BUILT |
| served surfaces | **0** | unknown | not started | increment 2 |

> **THE HONEST HOLE:** the *live production* notebooks are on OneDrive, outside the repo, and no
> repo instrument can enumerate them. The repo forks are documented as differing from production in
> exactly two ways — but that is a claim in a README, not a measurement I have made. **Any statement
> of the form "the estate's BBG surface is fully enumerated" would be false at this line.**

---

## 7. TRANSPORT / REACHABILITY STATE (not built — stated so it is not assumed)

| Gate | State | Owner |
|---|---|---|
| AWS creds on this device | **SATISFIED** (`INHERITED` 2026-07-30) | — |
| IAM role + `aws_ssm_activation` | open — **must precede the MSI** | CloudOps |
| SSM Agent MSI (one-time admin) | **NOT INSTALLED** | Andrew |
| `server.py` streamable-http on :8790 as a service | **NOT LISTENING** | CloudOps |
| Bloomberg registered as a gateway backend | open, follows the rename | CloudOps |

**Consequence for W8:** the only live path to these pipes today is **local, on this box**. There is
no remote consumer of the Bloomberg MCP surface right now, which materially bounds what "served
where" can mean in increment 2.

---

*Increment 1 ends here. Nothing in it required a Bloomberg call.*

---

# INCREMENT 2 — the request universe, and what it actually feeds

## 8. WHAT THIS PIPE ASKS BLOOMBERG FOR — the whole request universe, from source

Source-confirmed by direct read of `workflows/bloomberg/tplus1/src/market_indices_data_pull.ipynb`
@`f09cbd13ef` (14 code cells; counts extracted from the notebook's own dicts).
**No Bloomberg call was made to produce this section** — it is the *specification* of the pull,
read off disk.

**The whole daily pull is THREE `HistoricalDataRequest`s** (`tia.bbg.datamgr` ->
`sids.get_historical(...)` -> `//blp/refdata`), plus a conditional fourth:

| # | Frame | Ticker set | Fields | Window | Periodicity |
|---|---|---|---|---|---|
| 1 | `return_daily` | `dc_asset_return` (all 22 categories) | 2 | `date_end + YearEnd(-6)` -> `date_end` | DAILY |
| 2 | `return_monthly` | `dc_asset_return` | 13 | **1989-12-31** -> `date_end` | MONTHLY |
| 3 | `price_monthly` | `dc_asset_price` (macro set) | 1 (`PX_LAST`) | **1989-12-31** -> `date_end` | MONTHLY |
| 3b | *conditional* | same as its parent | same | `date_end` -> `date_end` | DAILY |

**Denominator of the ticker universe: 165 unique Bloomberg identifiers across 22 categories**
(extracted from `dc_index` + `dc_macro` in cell 4; `dc_macro` carries ~93 macro entries feeding
`dc_asset_price`). Instrument: regex over the notebook's own literal dicts — **blind to any ticker
built dynamically at runtime**, and blind to the live OneDrive copy, which is the production source
and may differ.

**Field vocabulary, verbatim from the notebook:**
`PX_LAST` · `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS` · `BEST_PE_RATIO` · `PE_RATIO` ·
`PX_TO_FREE_CASH_FLOW` · `EV_TO_T12M_SALES` · `PX_TO_BOOK_RATIO` · `PX_TO_SALES` (+ dividend yield)
— 13 in the `all` set, 2 in `return`, 1 in `price`.

> **REQUEST #3b IS THE MONTH-END HAZARD, AND IT IS IN THE PRODUCTION PATH.** When the monthly
> frame's max date is not `date_end`, the notebook appends a **one-day DAILY snapshot onto a MONTHLY
> frame**. Unguarded this duplicates the month-end row: `price_monthly` duplicates value-identical,
> **`return_monthly` does NOT** — the appended row is NaN in valuation fields, so a naive `.last()`
> dedup destroys data. Recorded here because it is a property of the *request shape*, not of the
> downstream consumer, and every artifact in §10 inherits it.

**Scale note for any future sizing conversation:** frames 2 and 3 request from **1989-12-31** —
~36 years x monthly x 165 tickers x up to 13 fields. **This is what "large pulls will be flagged"
is about.** The daily frame is deliberately bounded to ~6 years. Any verification pull proposed in
increment 3 must be sized against this baseline, not against intuition.

---

## 9. THE IDEMPOTENCE PROPERTY THAT MAKES THE PULL CHEAP — and its one sharp edge

`if os.path.exists(pkl_data): load it` (cell 7). **A re-run for a vintage already on disk makes
ZERO Bloomberg calls.** This is the single most important operational fact for quota discipline.

⛔ **The sharp edge, and it is a client-facing correctness issue, not a quota one:** `tzero` writes
`data <today> v1.pkl`; tomorrow `tplus1` targets that same date and would **reuse today's tzero file
rather than pull fresh**. Harmless if the tzero run captured a complete session; **silent corruption
of a client-facing dashboard if it ran intraday and captured a partial one — and nothing downstream
can distinguish them, because the filename is identical either way.** Guard in place: `tzero` appends
each vintage to `output/.tzero_vintages.txt` and `tplus1` refuses to start on a collision unless
given `--accept-tzero-vintage`. **Proceeding is possible; proceeding silently is not.**

---

## 10. THE JOIN — which served surfaces are Bloomberg-origin

This is W8's actual contribution. The estate already carries a complete producer -> S3 ->
CloudFront -> React lineage map (`docs/reference/yang-pipeline-lineage-map.md`, 17 portal artifacts
at field grain, `INHERITED`). **It starts at `data.pkl` / `model.pkl`.** It does not answer the
question Andrew asked, which is what the *Bloomberg pipe* serves. §8 supplies the missing upstream
segment; this section joins the two.

**Denominator: 17 yang portal artifacts** (the lineage map's own enumeration) + 27 TF-managed yang
Lambdas, of which 14 are portal-data generators.

| S3 key (`opal-data-portal-v2`) | BBG origin | Portal surface |
|---|---|---|
| `json/valuation/valuation_data.json` | **PURE** — `data.pkl -> price_monthly` | Valuation |
| `json/correlations/correlation_data.json` | **PURE** — `data.pkl -> return_monthly` | Correlation |
| `json/macro/macro_data.json` | **PURE** — `data.pkl -> price_monthly`, 84 macro series | Macroeconomics |
| `json/macro/timeseries/{slug}.json` (79 files) | **PURE** — `data.pkl -> price_monthly` | Macroeconomics (modal) |
| `json/macro/vix_data.json` | **PURE** | **NONE — orphaned export** |
| `json/factor-tilts/tier{1,2,3}-*.json` | **DERIVED** — `model.pkl` FACTOR_SPREADS | FactorTilts (3 tabs) |
| `json/benchmarks/etf_returns.json` | **DERIVED** — `model.pkl -> etf_returns` | ModelPortfolios |
| `json/benchmarks/model_portfolio_benchmarks.json` | **MIXED** — `data.pkl -> return_daily` + SmartX sidecars | ModelPortfolios |
| `json/benchmarks/benchmark_returns.json` (LEGACY) | **MIXED** — same producer | BenchmarkHeatmap |
| `json/benchmarks/model_portfolio_timeseries.json` | **MIXED** — `return_daily` + `price_monthly` + SmartX | ReturnVolatilityScatter |
| `json/positioning/positioning_data.json` | **MIXED** — `model.pkl` + `data.pkl` + BD `aum-metrics.json` | Positioning, Attribution |
| `json/valuation/risk_premium_data.json` | **MIXED** — `data.pkl` ERP + **FRED** OAS CSVs | Valuation / RiskPremium |
| `json/capital-markets/assumptions.json` | **NONE** — CMA Excel | CMA |
| `json/capital-markets/views.json` | **NONE** — SAA Excel | CMA |
| `json/peers/peer_performance.json` | **NONE** — peer Excel | ModelPortfolios |
| `json/positioning/holdings_attribution_data.json` | **NONE** — attribution Excel + DynamoDB | Positioning, Attribution |
| `json/positioning/allocation_summary.json` | **NONE** — reads the attribution artifact | Attribution |

### 10a. The operational answer: what goes dark if this pipe dies

**12 of 17 served artifacts carry Bloomberg origin; 5 do not.** Stated as blast radius:

| Portal page | Exposure if the blpapi pipe stops |
|---|---|
| **Valuation** | **FULL** — both artifacts BBG (one partially FRED-backed) |
| **Correlation** | **FULL** — single BBG artifact |
| **Macroeconomics** | **HIGH** — macro + 79 timeseries are BBG; the Volatility tab is **NOT** (market-overview pipeline) |
| **FactorTilts** | **FULL** — all three tiers off `model.pkl` |
| **ModelPortfolios** | **PARTIAL** — benchmarks + ETF returns BBG; peer performance is Excel and survives |
| **Positioning / Attribution** | **LOW** — dominated by Excel + DynamoDB; only `positioning_data` is mixed |
| **CMA** | **NONE** — Excel end to end |

> **THE FAILURE IS SILENT, AND THAT IS THE FINDING.** The pull is idempotent by filename, the
> pipeline consumes `uploads/` on success, and the served artifact carries `data_as_of`. A dead
> Terminal produces **no new PKL**, so the pipeline never fires and **the portal keeps serving
> yesterday's artifact with yesterday's `data_as_of`** — correct-looking, internally consistent, and
> stale. This is exactly the 2026-08-11 shape: 12.5h dead, found only because a human asked.
> **Per CLAUDE.md NEVER#1 this is also where a reader must not over-correct**: an unmoved
> `data_as_of` across a weekend is a HEALTHY T-1 pipeline, not an outage. The discriminator is the
> trading-day frontier, never wall-clock age.

### 10b. Two structural observations for CTO~Z

1. **One producer, two homes.** The repo carries `workflows/bloomberg/{tplus1,tzero}/src/` while the
   *production* notebooks live in OneDrive. The README asserts they differ in exactly two ways —
   **that is a claim in prose, not a measurement.** This is CLAUDE.md Rule 22a's two-homes shape:
   a filename-resolved comparison reads CLEAN where two copies have silently diverged. I am **not**
   proposing a reconciliation act; I am recording that the map's upstream segment rests on an
   unverified equivalence.
2. **`json/macro/vix_data.json` is produced every run and consumed by nothing** (proxy fn exported,
   no component imports it). Pure BBG-origin work with no served destination. Recorded as a
   surprise-channel line item, not chased.

---

## 11. INCREMENT 2 COVERAGE STATEMENT

| Axis | Enumerated | Of | Instrument | Confidence |
|---|---|---|---|---|
| daily-pull requests | 3 (+1 conditional) | 3 | notebook source read, today | high |
| ticker universe | 165 unique | 165 literal | regex over notebook dicts | high for literals; **blind to runtime-built tickers** |
| request categories | 22 | 22 | same | high |
| served yang artifacts | 17 | 17 | lineage map, `INHERITED` | high, **vintage not re-verified** |
| BBG-origin classification | 17 of 17 classified | 17 | join of §8 onto the lineage map | **medium-high — a DERIVED read** |

> **THE HONEST LIMIT ON §10:** the BBG-origin column is a **join of two documents**, not a live
> trace. It inherits the lineage map's vintage and my reading of the notebook's frames. It is strong
> enough to prioritise and to reason about blast radius; **it is not a certification**, and no
> deletion, retirement, or "unused" call should rest on it without a live check.

*Increment 2 ends here. Still zero Bloomberg calls made.*

---

# INCREMENT 3 — the one live traversal, and the sized-pull menu

## 12. THE ONLY BLOOMBERG CALLS MADE BY THIS MAP: two `bloomberg_health`

`bloomberg_health` is explicitly on the permitted side of the directive (transport traversal, no
data). I made **two**, deliberately, ~3 minutes apart — the second one specifically to discriminate
a cold-start artifact from a sustained state. **No other Bloomberg call was made.**

| Reading | Result |
|---|---|
| `bloomberg_health` @ ~17:16Z | `ok:false` — "could not start blpapi session to 127.0.0.1:8194" |
| `bloomberg_health` @ ~17:19Z | `ok:false` — identical |
| `Get-NetTCPConnection -LocalPort 8194` @ 17:19:09Z, **3 probes 4s apart** | **NO LISTENER**, all three |
| `bbcomm` | pid 24492, **ALIVE**, `Responding=True`, started **13:16:55 ET** |
| `blpcrashmon` | pid 11296, same start second |
| `wintrv` | **absent** (consistent with all day) |
| Denominator | **429 processes on the box, exactly 2 Bloomberg ones** |

**This is the half-healthy shape the runbook names**: *"bbcomm restarts on its own after a crash —
so the box looks half-healthy and is not."*

### 12a. What this is NOT — stated first, because the wrong reading is the natural one

- **NOT a data outage.** This morning's 07:00 ET run was **full end-to-end success**
  (`bbg_tplus1_20260812_070000.log`, exit 0): published `2026-08-11`, and the publisher verified the
  **served content against the PKL for all five models**. The portal correctly serves T-1. **Nothing
  is stale, and per NEVER#1 the unmoved date is the CORRECT answer, not a finding.**
- **NOT a mechanism.** `bbcomm` restarted at 13:16:55 ET — roughly when my first health probe landed
  — so **I cannot exclude that my own probe triggered a cold `bbcomm` start.** The second failure
  three minutes later argues against a *short* cold-start, but **the cause is UNDETERMINED** and
  Rule 22 forbids me authorizing anything on a hypothesis.
- **NOT a prediction** that tomorrow's 07:00 fires against a dead DAPI. That is a **risk, not a
  fact**. Task state: `Ready`, `LastTaskResult 0`, next run 2026-08-13 07:00 ET.

### 12b. What I deliberately did not do

**No sign-in attempt.** The P0 gate is explicit: an absent `wintrv` is NOT evidence a sign-in is
needed, a failed login is not free, and **Bloomberg locks the account on repeated failures.** Acting
on the natural inference converts a non-problem into a lockout and a support call.
**No `.ST` discriminator** — it is a `HistoricalDataRequest`, i.e. a pull, and forbidden to me
without a sized ask. **No alarm, checker, or monitor proposed** — the standing moratorium holds, and
the detection gap here is already routed as a route/schedule question.
**Routed to `0.0.3_BG_BBGTerminal`** (owner of terminal health) at 172118Z, FYI to CTO~Z. Not mine
to remediate.

---

## 13. SIZED-PULL MENU — offered, not requested

**The map is COMPLETE WITHOUT ANY PULL.** I am not manufacturing a need for one. This section exists
so that *if* Andrew or CTO~Z wants live verification, the ask already carries numbers rather than
adjectives — per the directive, **sizing means a number: rows, fields, date span.**

| Option | Purpose | Exact size | Class |
|---|---|---|---|
| **A** | Confirm the 165 literal identifiers still resolve | **165 securities x 1 field (`NAME`) x 0 date span** — 1 `ReferenceDataRequest`, no history | identifier resolution; borderline by my own call-shape rule -> **request it** |
| **B** | Entitlement discriminator (the runbook's) | **1 security (`.ST Index`) x 1 field x ~683 rows** from 2023-12-29, + `SPX Index` positive control as a **separate** request | `HistoricalDataRequest` — a **PULL** |
| **C** | Verify a served number end-to-end against source | **5 securities x 1 field x 1 date** | `HistoricalDataRequest` — a **PULL** |

**Baseline for comparison, so nobody sizes against intuition:** the production daily pull requests
**165 tickers x up to 13 fields x ~36 years monthly** plus ~6 years daily. Every option above is
negligible beside the pull that already runs at 07:00 each day — **which is an argument for
proportionality, NOT a licence.** The constraint is Andrew's to relax, not mine to reason around.

**Recommendation: run NONE of them today.** Option B belongs to `0.0.3_BG_BBGTerminal`'s seat, not
mine, and the entitlement question is theirs. Options A and C verify a map that is not currently
disputed.

---

## 14. FINAL COVERAGE STATEMENT

| Axis | Enumerated | Of | Confidence |
|---|---|---|---|
| blpapi services | 6 | 6 | high, `INHERITED` 13d |
| refdata request types | 7 named / 3 built | 7 | high, source-read today |
| in-repo session openers | 3 | 3 | high |
| **out-of-repo session openers** | 1 known | **UNKNOWN** | **LOW — structurally invisible** |
| daily-pull requests | 3 (+1 conditional) | 3 | high |
| ticker universe | 165 | 165 literal | high for literals |
| served yang artifacts | 17 | 17 | high, `INHERITED` |
| BBG-origin classification | 17 | 17 | medium-high, **a document join** |
| live transport state | measured twice | — | high for the reading, **UNDETERMINED for the cause** |

**THE MAP'S OWN LIMIT, stated plainly:** this is a traversal-and-read map. It is strong on
*structure* and deliberately weak on *live state*, because live state is what the constraint
forbids me to buy. **Two things in it are inherited rather than measured** (the service probe, the
lineage map), **one is structurally unmeasurable from here** (the OneDrive production notebooks),
and **the BBG-origin join is derived, not traced.** None of that is a defect in the work; all of it
is a defect a reader would otherwise have to discover for themselves.

*W8 map complete for the traverse+read mandate. Total Bloomberg calls made: 2, both `health`.*
