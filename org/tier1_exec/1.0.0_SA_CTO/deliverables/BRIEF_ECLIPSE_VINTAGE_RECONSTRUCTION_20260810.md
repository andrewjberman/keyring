# BRIEF — CAN A LOST ECLIPSE VALUATION VINTAGE BE RECONSTRUCTED?

**Commissioned:** Andrew-direct 2026-08-10, CTO terminal. **Author:** `1.0.0_SA_CTO`.
**Assigned to:** `0.2.0_DS_PortfolioAnalytics` (instantiation by `0.0.0_AB_MSTR`).
**Spec of record:** `data/assets/vendor_api/orioneclipse/` — full OpenAPI 3.0.3, 493 paths, 582 ops.

---

## 1 · THE PROBLEM, STATED PRECISELY

Eclipse's `date=` partition key is the **RUN date** (the day we pulled), not the data date — established
on five our-side instruments and corroborated vendor-side: **no `/portfolio/**` endpoint accepts a date
parameter.** The feed is **current-state only**.

The partition `date=2026-08-06` is **absent from BRONZE as well as silver** (measured: 992 bronze
objects → 72 date folders; 72 silver partitions; set difference empty both ways). Under run-date + T−1:

```
date=2026-08-05  ->  vintage 2026-08-04
date=2026-08-06  ->  ABSENT   ->  VINTAGE 2026-08-05 NEVER CAPTURED
date=2026-08-07  ->  vintage 2026-08-06
```

**⇒ THE LOST VINTAGE IS 2026-08-05.** A Thursday-run gap on a feed that writes weekends, so the
trading calendar does **not** explain it.

**AND IT CANNOT BE RE-PULLED.** `pull_eclipse_portfolios.py:3-29`: *"`--date` IS AN OUTPUT FILENAME,
NOT A QUERY … a PAST date here writes TODAY'S data"* and the sidecar *"STAMPS THE FALSE VINTAGE — the
artifact self-certifies the lie."* **A naive backfill does not fail; it FABRICATES.** That is the
single most important sentence in this brief.

---

## 2 · ⛔ TIER 0 — PROVE RECONSTRUCTION IS NECESSARY BEFORE BUILDING ONE

**DO NOT START AT TIER 1. Three cheap probes may make the whole effort unnecessary, and two of them
are read-only single calls.**

**T0-a · THE REPORT ENDPOINTS MAY ALREADY SERVE HISTORY.** From the registry:
```
GET /report/allocations                 startDate, endDate
GET /report/trades/reportByAccounts     startDate, endDate
GET /report/blocks/blockBybroker        startDate, endDate
```
**`/report/allocations` is dated and is allocation-shaped — exactly the quantity MDPF consumes.** If it
returns per-date allocations or values for a past window, **there is nothing to reconstruct; there is
a feed to add.** ⚠ The spec's `components.schemas` is EMPTY, so **the registry cannot tell you what
comes back** — this must be settled by an actual call, not by reading the spec.

**T0-b · ORION ALREADY HOLDS THE SAME ACCOUNTS.** `orion/inflection/silver/fact_assets` is a separate
vendor feed over the same book, current through 2026-08-10 with deep history. If orion carries
2026-08-05, the **custody** total for that date already exists. It does not directly give
**model-level** attribution — but it bounds the answer and may satisfy the actual serving need.

**T0-c · IS THE VINTAGE EVEN SERVED?** The axis spans 2024-11-01 → frontier, so 08-05 is a *rendered
point on a client-facing chart*. Confirm the business impact before engineering: **one interior point
on a 440-date series may warrant an honest named gap rather than a reconstruction.**

> **T0 EXIT:** if `/report/allocations` returns dated data, **STOP and write a feed brief instead.**

---

## 3 · TIER 1 — THE ROLL-BACK RECONSTRUCTION, IF T0 FAILS

**The identity.** For portfolio *p*, reconstruct backwards from a **known-good later snapshot**:

```
V_p(2026-08-05)  =  V_p(2026-08-06)  −  ΔTRADES  −  ΔFLOWS  −  ΔMARKET
```

`V_p(2026-08-06)` is **present and trustworthy** — it is what `date=2026-08-07` contains.

| term | source | dated? | confidence |
|---|---|---|---|
| **ΔTRADES** — buys/sells settled between the two dates | `GET /tradeorder/instances/portfolio/{portfolioId}/search` · `GET /tradeorder/closedTrades` · `GET /tradeorder/deletedTrades` | ✅ `startDate,endDate` | **HIGH** — this is exactly what these endpoints exist for |
| **ΔFLOWS** — contributions, withdrawals, set-aside cash | `GET /auditlog/portfolio/{portfolioId}` · `GET /auditlog/accountSetAsideCash/{accountId}` | ✅ `fromDate,toDate` | **MEDIUM** — audit logs record *events*, and an event log is not a cash-flow ledger |
| **ΔMARKET** — price movement on unchanged holdings | ⛔ **NOT IN ECLIPSE** | — | ⛔ **THE HARD TERM** |

### ⛔ ΔMARKET IS THE WHOLE PROBLEM, AND IT DECIDES FEASIBILITY
Eclipse serves **current** holdings and values. It does **not** serve historical prices. So reconstructing
a market-value change requires **security-level holdings at 08-05 × prices at 08-05**, and the price
vector must come from outside Eclipse.

**⇒ Two sub-questions decide whether Tier 1 is worth attempting AT ALL, and DS must answer them
before writing any reconstruction code:**
1. **Can we get per-security holdings at 08-05?** Holdings at 08-06 are known (`/portfolio/portfolios/{id}/holdings` as captured in `date=2026-08-07`); rolling them back needs the trade deltas above at **security** grain, not portfolio grain.
2. **Do we already hold an EOD price source for 08-05?** ⚠ **`ycharts_*` egress is NOT lifted — do not call it.** Check what the estate already has (Schwab CRS carries a per-security `Closing Price` and `LstUpDte` — `49financial.custody` bronze — but that is a *different firm's* book and **CLAUDE.md's firm-separation rules apply: it is a price-source question, never a holdings-source one**).

---

## 4 · WHAT IS **NOT** RECOVERABLE — say so plainly rather than discover it late

- **The vendor's own 08-05 snapshot.** Gone. No call returns it. Any reconstruction is a **DERIVED
  ESTIMATE and must be labelled one**, never emitted as `point_class: "measured"`.
  *(R-21 already records `point_class:"measured"` asserted over carried Cottonwood values — do not add
  a second instance of the same defect.)*
- **Anything that depended on intra-day state** on 08-05.
- **Certainty about WHY 08-06 never ran.** Bronze has no vendor as-of, so a vendor non-publication and
  our own missed run are **indistinguishable from the artifact alone**.

---

## 5 · DELIVERABLE + ACCEPTANCE

**D1 — T0 verdict (REQUIRED FIRST, and it may end the project).** For each of `/report/allocations`,
`/report/trades/reportByAccounts`: the exact call, the response shape, and whether it returns dated
historical allocation/value data. **PASS = a documented yes/no per endpoint with the response body.**

**D2 — feasibility ruling on Tier 1.** Answer the two ΔMARKET sub-questions. **A well-evidenced
"NOT FEASIBLE, here is why" is a SUCCESSFUL outcome** and is preferred over a speculative build.

**D3 — if and only if feasible:** a reconstruction spec — per-security roll-back, the price source,
the error bound, and the **provenance label** the output carries.

**D4 — a tie-out design.** Reconstruct a date we ALREADY HAVE (e.g. 2026-08-04, present on both sides)
and compare against the captured truth. ⛔ **NO RECONSTRUCTED VALUE IS SERVED UNTIL THE METHOD IS
EXERCISED AGAINST A KNOWN DATE AND THE ERROR IS MEASURED.** A method that cannot reproduce a known day
must not be trusted on an unknown one.

## 6 · BOUNDS — binding

- ⛔ **NEVER run `pull_eclipse_portfolios.py --date <past>`.** It fabricates and self-certifies.
- ✅ **ECLIPSE/ORION vendor egress is on the standing LIFTED list**, and Andrew has directed this work.
  **READ-ONLY probes only** — no writes, no order/trade endpoints, no `POST`/`PUT`/`PATCH`/`DELETE`.
- ⛔ **`ycharts_*` and every other vendor remain HELD** — explicit per-use word required.
- **Nothing is served from this work without a separate CTO ruling.** This brief authorizes
  **investigation and design**, not a serving change.
- **Print denominators. Label every derived value as derived.**
- **This is NOT on the MDPF repair critical path** — the repair remains the main fabric priority
  (Andrew, 2026-08-10 ~1620Z). This runs beside it, not ahead of it.
