# INFINC.006 Pattern E TXN — CTO End-to-End Validation

**Author:** 1.0.0_SA_CTO
**Date:** 2026-05-15
**Trigger:** Andrew direct — "look into this, validate it end to end, then coordinate with COO to run a thread on whether/how to implement."
**Subject:** DS~D brief — Pattern E TXN incremental pull, client-level endpoint design.
**Verdict:** Brief's narrow technical claims all VALIDATE. Its foundational scope premise does NOT — there is a parallel live transaction path the brief, the INFINC.006 TO, and the INFINC.005 probe never acknowledge. **Do not green-light implementation as-is. Thread it.**

---

## 1. What was validated

Primary sources read end-to-end: `pull_inflection_transactions_rest.py` (current code body), `inf_006_phase0_probe.py` + `inf_006_phase0_result.json` (Phase 0 empirical), `convert_transactions_to_silver.py` (DWSPLT Rule-17 silver), `_orion_api_silver_lib.py` (`coerce_silver_ids`), `inf-api-txn` Lambda (`lambda_function.py`), `pull_inflection_transactions_v2.py`, `orion-gold-dispatch.sh` (chain catalog), the INFINC.006 TO, the INFINC.005 capability-probe brief, the Q2 backdate-distribution brief, `ADVI_DWSPLT.json` / `ADVI_INFINC.json`, `lambda-source-map.json`.

---

## 2. Claims that VALIDATE (brief is honest and correct)

| # | Brief claim | Verdict | Evidence |
|---|---|---|---|
| 1 | Current state: only the docstring was edited; no code logic changed | **CONFIRMED** | `_rest.py` body is 100% the old account-level full-history pull — iterates ~1,160 accounts via `/Portfolio/Accounts/{id}/Transactions`, no date params, no merge logic. `--full-pull`/`--since` appear in the new docstring's usage block but **do not exist in argparse**. Git: working-tree-modified, uncommitted. |
| 2 | Firm-level endpoint missing 11 cols incl. `householdId`, `avgPrice` | **CONFIRMED EXACTLY** | `inf_006_phase0_result.json` → `schema_parity.in_account_not_firm` = 11 cols: avgPrice, blockId, custodianName, executionTime, fundFamilyName, householdId, orderCreatedBy, orderId, registrationCode, registrationSleeveStrategyName, tradeOrderId. |
| 3 | Client-level schema identical to account-level (30 cols) | **CONFIRMED** (thin sample) | Probe `client_7d.cols` == `account_baseline.cols`, exact 30-col match. Caveat: client side verified on 1 client / 9-row window / `row[0]` keys. Adequate for a schema-stable REST endpoint; not bulletproof. |
| 4 | Silver requires `householdId`; firm-level would silently corrupt gold | **CONFIRMED + SHARPENED** | `convert_transactions_to_silver.py` is the DWSPLT Rule-17 strict passthrough: `df = bronze.copy()`, then `coerce_silver_ids(df, cols=(...,"householdId",...))`. **`coerce_silver_ids` silently skips missing columns** — firm-level bronze would NOT fail loud; silver would emit a wrong-shaped frame and corruption surfaces downstream at gold. "Silently corrupt 6 days/week" is mechanically accurate. |
| 5 | Firm-level is not a safe drop-in | **CONFIRMED beyond schema** | INFINC.005 probe: 30-day firm window **read-timeout at 120s**; ≤30-day cap without entity id. Firm-level is fragile on payload as well as schema. |
| 6 | PERF short windows work (no timeout) | **CONFIRMED** | Probe PERF 7d=2.0s, 14d=1.5s, baseline=7.0s, all HTTP 200. The "5y+ timeout" docstring was long-window-only. |

The Phase 0 work is good. DS~D caught the firm-level schema gap that the INFINC.005 probe missed — INFINC.005 claimed "identical key set in every probe preview" (it had hedged "preview was truncated"), and the INFINC.006 Phase 0 re-probe correctly disproved it. Verify-don't-trust discipline worked.

---

## 3. Claims that are WEAK — flag, don't block

**PERF "no wall-time win" is asserted, not proven.** The probe measured raw single-call latency on one client (7.0s → 2.0s windowed — a 3.5x per-call drop), NOT throttled end-to-end wall-time across all ~314 clients. Whether the 3.5x per-call latency drop yields a wall-time win depends on whether PERF is throttle-bound or latency-bound — unmeasured. There is also an unexplained gap: probe baseline 7.0s/call vs INFINC.005's implied ~1.7s/call production average (~9min / 314 calls). PERF defer-v1 is a defensible call (PERF is gravy-on-gravy, P2) — but the evidence is softer than the brief states. Either label it "soft evidence" or take one clean end-to-end windowed-PERF wall-time measurement before final defer.

---

## 4. The foundational gap — UNVERIFIED SCOPE PREMISE

The brief calls `pull_inflection_transactions_rest.py` "**the** Orion transaction bronze pull." It is not the only one. End-to-end tracing found **three transaction-pull lineages and two live writers of the same silver artifact**:

| Lineage | Source mechanism | Windowed? | Invoked by | Bronze key |
|---|---|---|---|---|
| `pull_inflection_transactions_rest.py` | REST per-account `/Portfolio/Accounts/{id}/Transactions` | **No** — full history | gold chain `INF_API_PULL_TXN` (`orion-gold-dispatch.sh:185`) | `bronze/transactions/{date}.parquet` |
| `pull_inflection_transactions_v2.py` | Orion Custom Report 28198 (CSV) | **Yes — already rolling-7-day default** + `--start/--end-date` | `inf-api-txn` Lambda, EventBridge `cron(0 13 * * ? *)` daily | `bronze/orion-api/{date}/transactions.csv` |
| `pull_inflection_transactions.py` (v1) | Custom Report 28198 | yes | superseded by v2 (per v2 docstring) | — |

**Both live paths write `s3://opal-data-inf/silver/transactions/{date}.parquet`:**
- Gold chain `INF_API_SILVER_TXN` → `convert_transactions_to_silver.py` (reads REST parquet bronze; DWSPLT Rule-17).
- `inf-api-txn` Lambda → `convert_orion_api_to_silver.build_transactions` (reads Custom-Report CSV bronze) → writes `silver/transactions/{date}.parquet` directly ("CTO Option B ruling" per Lambda docstring).

They use different data sources, different converters, different bronze keys, and appear to have **different semantics** — the Lambda passes a single-day window (≈1-day delta); the gold chain's `_rest.py` produces a full snapshot. Last writer wins the partition. This is a live dual-writer / mixed-semantics race — the same class of problem ADVI_DWSPLT exists to fix, and DWSPLT's named scope (`convert_orion_to_silver.py` LEGACY vs `convert_transactions_to_silver.py` REST) may not even cover the `inf-api-txn` Lambda's `convert_orion_api_to_silver.py` writer.

Consequences:
- **INFINC.006 does not *create* this race** (the merge-into-prior reads `bronze/transactions/`, self-contained to the REST lineage) — but it is scoped as if the race does not exist.
- **Implementing Pattern E on `_rest.py` is only correct if the gold-chain REST path is the canonical/intended daily producer.** That is unverified. If `inf-api-txn` is canonical (it matches the LAMBDA-DIMS 12:30–13:00 UTC daily cron from ADVI_INFETL), the chain's TXN steps may be redundant — in which case the right move is a Pattern-A skip-gate or deletion, not a Pattern-E windowing of `_rest.py`.
- **The windowed-incremental capability the brief proposes to BUILD already EXISTS** in `_v2.py` (rolling-7-day default). Compiler-Mandate Auto-Rule #5 (pre-authoring repo check — "does this capability already exist") was not satisfied by the INFINC.005 probe or the INFINC.006 TO.

This is not a knock on DS~D — the TO scoped DS~D to `_rest.py`; the Phase 0 work on that script was excellent. The gap is PRD/TO-authoring: no `comp-blast` / consumer-enumeration on the transaction silver artifact at authoring time. (CTO included — my session-24 fast ACK of the client-level fallback did not catch this either; that is exactly why Andrew asked for a real validation.)

---

## 5. AC deviations needing formal revision

| AC | TO text | Reality | Action |
|---|---|---|---|
| AC1 | daily run uses **firm-level** endpoint | firm-level rejected (schema gap) → client-level | revise to client-level (brief flagged this) |
| AC5 | `~7min → <1min` target | client-level ≈ 314 calls ≈ ~2 min; `<1min` was a firm-level (1-call) number | revise to ~2 min (**brief did NOT flag**) |
| AC7 | daily window = **exactly 7 days** | CTO session-24 spec, premised on firm-level (window size = timeout risk). Client-level call count is window-**independent** → window size is ~free. Q2 empirical brief (DS~B, 200,811 txns) found **max backdate lag 65 days**, recommends **90-day** window. | thread decision with Q2 data visible (**brief did NOT flag**) |
| AC2 | backstop via a **different endpoint** | both modes are client-level now; backstop differs by **window** (full-history vs trailing), not endpoint | reword |

The AC7 7-vs-90 question is the substantive design call. 7 days + a working Sunday full-pull = bounded ~7-day eventual consistency on the rare far-backdated correction (Q2: 58 events / 7 months, mostly `Cancel Account` batches at 63–65d lag). With client-level the window is nearly free, so sizing to the empirical correctness requirement (Q2's 90d) rather than inheriting a firm-level-era number is the more defensible default — but it should be a deliberate thread call, not silent inheritance.

Also unspecified: the merge-into-prior-snapshot needs an explicit **missing-prior-partition fallback** (find most-recent existing partition; if none within window / absent, escalate to a full pull). The TO says only "append to prior bronze."

---

## 6. Cross-project / ground truth

- **ADVI_DWSPLT TO-2/3/5 shipped atomically** in `f69461357` (2026-05-13, on CLOUD) — silver Rule-17 strict + INF gold consumer migration. **`ADVI_DWSPLT.json` is stale** (still says TO-2 "paused", TO-3/5 pending). CTO to correct as startup ground-truth follow-up.
- INFINC.006 ↔ DWSPLT: decoupled on the **schema** axis (bronze stays 30 API cols + `pull_date`); **not** independent on the **artifact** axis — the `silver/transactions/` dual-writer is squarely DWSPLT's domain.

---

## 7. Recommendation — thread agenda

Do NOT green-light client-level implementation yet. Run a thread — **CTO + COO + DS~D + AE 0.6.1** (AE owns `inf-api-txn` / LAMBDA-DIMS / dispatch plumbing; DS~D owns the brief + `_rest.py`/`_v2.py`).

Resolve, in order:
1. **TOPOLOGY (blocking).** Is the gold-chain REST TXN path the canonical daily producer, or is `inf-api-txn` Lambda? Are they meant to coexist? What is the intended end-state of the `silver/transactions/` dual-writer? Outcome determines whether INFINC.006 (a) proceeds on `_rest.py` as planned, (b) targets `_v2.py`/the Lambda, (c) becomes a skip-gate/delete of a redundant chain step, or (d) defers pending a DWSPLT-scope expansion.
2. **If `_rest.py` proceeds:** ratify AC1→client-level, AC5→~2min, decide AC7 7d-vs-90d with the Q2 data on the table, spec the missing-prior-partition fallback.
3. **PERF:** ratify defer-v1 (evidence is soft) or take one clean end-to-end measurement.

The cost is one thread cycle. The cost of shipping mis-scoped P2 work is the work plus cleanup plus erosion of verify-before-build. Thread it.
