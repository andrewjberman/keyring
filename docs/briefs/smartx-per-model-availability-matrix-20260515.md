# SmartX Per-Model Endpoint Availability Matrix

| | |
|---|---|
| **TO** | SXPL_RESTIN.001.dsb-per-model-availability-assessment |
| **Author** | 0.4.0_DS_ClientPlatform~B |
| **Date** | 2026-05-15 |
| **Project** | SXPL_RESTIN (SmartX REST Integration) |
| **Status** | COMPLETE — deliverable for COO to scope TO-3+ |
| **Design brief** | `docs/briefs/smartx-rest-integration-design-20260515.md` (commit 352ab4585) |
| **Probe harness** | `data/smartx/scripts/sxpl_restin_probe.py` (read-only; creds from Secrets Manager) |

This brief closes the empirical gaps the SmartX HAR left: real per-model response schemas + a per-model x per-endpoint availability matrix. It is the ground truth TO-2 (pull flow) and TO-3+ (silver/gold modeling) build against.

## Method

Probed all 7 modelIds x 13 endpoints (brief §6.2–6.4) live 2026-05-15 18:11–18:21Z. One ROPC token (Secrets Manager creds). Throttled 3.6 s/call (~17 req/min). ~95 calls, **zero 429/rate-limit responses**. reportedModelId chained off `/models/{modelId}` per design-brief §7.

---

## AC1 — The 7 models resolved

All 7 are `status=active`, `type=web`, enterprise **Opal Capital LLC**.

| # | modelId | Model name | shortName | reportedModelId | Exporter scope |
|---|---|---|---|---|---|
| 1 | `0f76a5a0-…51d8` | Opal Short-Term | `49FiLiSh000` | `955c9631-…6d0d` | **ST** |
| 2 | `48af6559-…3ad8` | Opal Dividend Income | `TitlDivGro000` | `ea6cbb22-…733b` | — (not in exporter) |
| 3 | `69cc5e3b-…1bc9` | Opal Long-Term Aggressive | `49FiLiLoAg000` | `54e83021-…f38e` | **LTA** |
| 4 | `729210dd-…7afd` | Opal Intermediate-Term | `49FiLiIn000` | `14540628-…ac6c` | **INT** |
| 5 | `74c119db-…8121` | Opal Conservative Growth | `49FiLiCoGr000` | `3f111210-…f478` | **LTC** |
| 6 | `843d875b-…37d5` | Pathfinder Focused Opportunities | `OpGEGTR000` | `ab0a2a03-…7422` | — (not in exporter) |
| 7 | `c000fe6a-…d175` | Opal Ultra Short-Term Income | `OpaGlUlShIn000` | `3f8e94c4-…7b39` | **UST** |

**5 known Opal portfolios identified** — ST / INT / LTC / LTA / UST map cleanly to the exporter's `PORTFOLIOS=UST,ST,INT,LTC,LTA` (`production.env`). The `49Fi…` shortName prefix marks exactly these 5 — they are the 49F family.

**The 2 previously-unidentified modelIds (design-brief §10 open question) are characterized:**
- **Opal Dividend Income** (`48af6559`, `TitlDivGro000`)
- **Pathfinder Focused Opportunities** (`843d875b`, `OpGEGTR000`)

Both are real, active Opal Capital models — they are simply outside the legacy browser-exporter's 5-portfolio scope (different shortName prefixes, not `49Fi…`). The REST integration can cover all 7; whether Dividend Income + Pathfinder are in-scope for the portal is a product call for Andrew.

---

## AC2/AC3 — Availability matrix + schemas

`api/3.1` responses use the envelope `{data, version, hostDetails, statusCode, requestId, timestamp}` — payload under `data` (`reportedmodels/*` + `enterprises/allocations` also carry a top-level `count`). All data hosts require `Authorization: Bearer <JWT>`.

| Endpoint | Grain | 7-model result | Bytes (range) |
|---|---|---|---|
| `models/{modelId}` | static metadata | 7/7 OK | ~0.9 KB |
| `models/{modelId}/statistics` | **live snapshot** | 7/7 OK | ~0.8 KB |
| `enterprises/aum?modelid=` | **daily time series** | 7/7 OK | 33–116 KB |
| `enterprises/allocations?modelid=` | per-allocation roster (snapshot) | 7/7 OK | 25 KB–1.2 MB |
| `enterprises/advisors?modelid=` | advisor roster (snapshot) | 7/7 OK | ~0.7–1.2 KB |
| `allocations/performance?modelids=&grouping=m&start=&end=` | heavy nested perf stats (snapshot) | 6/7 OK; **1 timeout** | 265 KB–11.7 MB |
| `reportedmodels/{reportedModelId}` | static metadata | 7/7 OK | ~0.6 KB |
| `reportedmodels/{reportedModelId}/holdings` | **current holdings + weights (snapshot)** | 7/7 OK | 5–10 KB |
| `reportedmodels/{reportedModelId}/historicalperformance` | short perf time series | 7/7 OK | 0.6–4.8 KB |
| `reportedmodels/{reportedModelId}/changerequesthistory` | trade change-request event log | 7/7 OK | 17–145 KB |
| `performance.smartxadvisory.com/models/performance` | deep risk/return stats (snapshot) | 7/7 OK | 37–97 KB |
| `smartx.managedaccounts.io/api/3.0/models/{id}` (legacy) | — | 7/7 return `{status,msg,type}` 105 B | **not usable as probed** |
| `…/api/3.0/models/{id}/commentary` (legacy) | model notes | 7/7 return 47 B (empty) | **not usable as probed** |

Notes:
- `allocations/performance` timed out for `74c119db` even at a 90 s read timeout — its payload exceeds the others (the 6 that succeeded ranged to 11.7 MB). The endpoint works; that one model is just very large. A production pull must window it (`start`/`end`) or avoid it — it is **not needed** for the first data goal.
- The legacy `api/3.0` host returns a `{status, msg, type}` status envelope (105 B) for `models/{id}?type=undefined` on all 7 — it does **not** serve model data the way the HAR's larger v3.0 payloads suggested. `commentary` needs a numeric model id that v3.1 does not surface. **v3.1 supersedes v3.0 for everything we need — drop the legacy host from scope.**

### Key schemas (probe-confirmed)

**`enterprises/aum?modelid=`** — daily model value series:
```
data: { enterprise:{id,name}, totalAum:float,
        performance:[ { performanceDate:{timestamp:int,friendly:str}, closingEquity:float } ] }   # 422 daily points
```

**`reportedmodels/{reportedModelId}/holdings`** — current holdings + weights:
```
data:[ { symbol:{id,ticker,assetType,companyName,industry,multiplier},
         quantity:float, price:float, multiplier:float,
         marketValue:float, percentOfPortfolio:float } ]   count:int
```

**`models/{modelId}/statistics`** — live snapshot:
```
data:{ model:{id,name},
       statistics:{ value:float, cash:float,
                    exposure:{long,short,net,gross:{dollar,percent}},
                    returns:{today,mtd,qtd,ytd:{dollar,percent}} } }
```

**`reportedmodels/{reportedModelId}/historicalperformance`**:
```
data:[ { reportedModelId:str, performanceDate:{timestamp,friendly}, performanceValue:float } ]
```

**`enterprises/allocations?modelid=`** — per-advisor allocation roster (LTA: 1,971 rows):
```
data:[ { allocationId:str, status:str, advisor:{id,name,crd},
         model:{id,name}, value:float, openedDate:{timestamp,friendly} } ]   count:int
```

**`reportedmodels/{reportedModelId}/changerequesthistory`** — trade event log (LTA: 80 events):
```
data:[ { tradeTimestamp:{timestamp,friendly}, ticker:str, company:str,
         price:float, quantity:float, activity:str, percentage:float,
         from:{quantity,percent}, to:{quantity,percent}, requestedBy:str } ]
```

---

## AC4 — Open questions answered

- **Historical-holdings endpoint — does it exist? NO.** Probed `reportedmodels/{rmid}/holdings?date=` and `?asOf=` — both return a byte-identical payload to the no-param call (params ignored). `holdings/historical` and `historicalholdings` → HTTP 404. **`/holdings` is current-snapshot only.** Daily holdings-weight history must be accrued by snapshotting `/holdings` once per day — the 09:00 ET pull. (`reportedmodels/{rmid}/historicalperformance` gives a model-level performance series but not per-symbol weights.)
- **The 2 unidentified modelIds** — Opal Dividend Income + Pathfinder Focused Opportunities (see AC1).
- **Rate limit** — probed at ~17 req/min across ~95 calls with **zero 429s**. The exact ceiling is unconfirmed (confirming it would require a deliberate burst test — not done; read-only/conservative). The exporter config's "20 req/min per SmartX agreement" is a safe planning ceiling; the pull should stay ≤17/min.

---

## Recommendations for TO-2 / TO-3

**First data goal — daily model value + holdings weights (all 7 models):**

| Want | Endpoint | Field |
|---|---|---|
| Daily model value (history) | `enterprises/aum?modelid={modelId}` | `data.performance[].closingEquity` by `performanceDate` |
| Model value (intraday live) | `models/{modelId}/statistics` | `data.statistics.value` (+ cash, exposure, returns) |
| Holdings weights (current) | `reportedmodels/{reportedModelId}/holdings` | per-symbol `percentOfPortfolio` (+ quantity, price, marketValue) |

- TO-2's daily pull is **13 calls/day** (7x `enterprises/aum` + chained `models/{id}` -> `holdings`; `models/{id}` also needed to resolve `reportedModelId`) — trivially under any rate limit.
- Holdings has no history -> the 09:00 ET run snapshots it daily; history accrues as dated partitions (same accrual model as the Orion silver snapshots).
- **Drop from first-wave scope:** the legacy `api/3.0` host (not usable), and `allocations/performance` (10 MB+, heavy, not needed for value/weights — revisit only if allocation-level performance is wanted later).
- TO-3 (silver/gold) candidates beyond the first goal: `enterprises/allocations` (per-advisor allocation roster — distribution analytics), `changerequesthistory` (trade/rebalance event log), `performance/models/performance` (risk/return stats). All 7/7 populated.

**modelId vs reportedModelId** — confirmed hard requirement: `/holdings` 400s on a modelId; chain `models/{modelId}.data.reportedModelId`. The 7-pair mapping is in the AC1 table — TO-2 can hardcode it or resolve at runtime (resolving is cheaper to maintain).

---

## Deliverables / evidence

- This brief (the matrix + schemas + answers).
- `data/smartx/scripts/sxpl_restin_probe.py` — read-only probe harness, committed; re-runnable (`--models`, `--out`). Creds from Secrets Manager only.
- No scheduled job, no production pull, no Lambda shipped (read-only TO).

## Caveats

- Schemas are structural (key names + types) from one live probe per model; field *semantics* (units, sign conventions, `performanceValue` cadence) are inferred from names — TO-3 modeling should confirm against real values.
- `allocations/performance` for `74c119db` is unprobed (timeout) — endpoint confirmed working on the other 6.
- `historicalperformance` returned 7 points for most models — cadence (daily/weekly/monthly) not determined from shape alone.
