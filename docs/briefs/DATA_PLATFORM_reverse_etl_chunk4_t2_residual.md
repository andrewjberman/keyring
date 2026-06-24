# DATA_PLATFORM reverse-ETL — CHUNK-4: T2-RESIDUAL (the genuine-IP frontier)

**Lane:** 0.4.0_DS_ClientPlatform~B (2nd DS lane) · **Lead/integrator:** 0.4.0_DS_ClientPlatform (base, unified tier table)
**Date:** 2026-06-24 · **Status:** chunk-4 COMPLETE — closes my chunk set (2,3,4). RAVC2 base-DS+COO+CTO (cc CVO/0.6.0)
**Gradient:** T1 / T2-HOST (firm-owned ref data the vendor hosts) / T2-COMPUTE (genuine vendor algorithm). **2-axis confidence (CTO):** (DIFFABLE vs INFERRED) × (SNAPSHOT-cleanly-reproducible vs FLOW-mechanism-confirmed). **Perf dichotomy (CTO):** (a) standard documented method (TWR/Modified-Dietz -> replicable) vs (b) proprietary attribution (genuine-IP -> partner-or-build).
**Question:** what in BD's served output is genuinely NOT reproducible from Schwab-raw — the irreducible T2-COMPUTE layer?

---

## HEADLINE — the genuine T2-COMPUTE residual is NEARLY EMPTY for the Schwab-custodied 49F book

The two hypothesized "genuine-IP" candidates both resolve OUT of the irreducible-IP bucket on grounding:
- **Performance** = a STANDARD documented attribution method, and it is **already SELF-OWNED + Schwab-sourced** (we compute it; we do NOT ingest BD's). -> NOT a BD-IP supplant blocker.
- **Household/relationship grouping** = T2-HOST (explicit firm-assigned IDs) + T1 (deterministic rollup) — **no computed grouping IP**.

This CLOSES the supplant headline hypothesis (v0.1 Part-3): for a Schwab-custodied book, BD's served value is **mostly T0/T1 + T2-HOST, with a near-empty genuine-T2-COMPUTE residual**. Strongly feasibility-positive.

---

## TIER ROWS (data-calibrated)

### Row 4A — PERFORMANCE (C_00 -> C_02 -> C_03): **standard-method COMPUTE, SELF-OWNED + Schwab-sourced** — NOT a BD-IP blocker
- **Source-confirmed mechanism:** `C_00.canonical_performance` reads ONLY `account_gains` (B_03) + accounts_dimension — **NO BD-published-performance ingest** (comp-pipescript io C_00 + source). The method (C_00 docstring) is a STANDARD component attribution: `AUA(t)-AUA(t-1) = Growth(t) + NNA(t)`, `Growth = price_return + realized_gl + income` (a Dietz-family growth-vs-flow decomposition) — CTO case **(a) standard documented method**, replicable; NOT (b) proprietary.
- **Computed from Schwab-direct inputs:** `B_03.account_gains` derives from canonical_holdings (B_00/B_02 <- positions <- Schwab RPS) + canonical_lots (B_02) + silver/transactions. The whole perf chain is OUR medallion computing from Schwab-derived data.
- **The portal already serves OUR perf** (`C_03.account_performance` -> D_00..D_04 publishers), not BD's. So performance is, for the Schwab book, **already self-computed/served** — reproducible-from-Schwab-raw by construction.
- **Verdict:** genuine-COMPUTE class, but standard-method + self-owned + Schwab-sourced -> supplant requires NO BD-IP replication (we own the compute). Confidence: SOURCE-CONFIRMED-MECHANISM (the method is our readable code); **INFERRED on parity-vs-BD's-published-perf** (I did NOT diff our computed return against BD's own statement numbers — a separate parity verification, honest residual).

### Row 4B — HOUSEHOLD / RELATIONSHIP GROUPING (C_02 rollup): **T2-HOST + T1 — NOT T2-COMPUTE**
- **Mechanism (source-confirmed, C_02):** grouping is a deterministic `groupby(['date','relationship_id'])` on the **EXPLICIT firm-assigned `relationship_id`** (`acct_to_rel = accts[...]['relationship_id']; df['relationship_id'] = df['account_id'].map(acct_to_rel)`). **No clustering / fuzzy / household-matching heuristic** anywhere in C_02 (grep-confirmed) — accounts roll up by their explicit assignment, not a computed cluster.
- **Tier:** the relationship/portfolio ASSIGNMENTS (the Team->Relationship->Portfolio->Account star) = firm-owned ref data BD hosts = **T2-HOST** (cataloged in chunk-2 Row C — the allocations dimension is the substrate). The ROLLUP = deterministic group-by = **T1**. The hypothesized "household-grouping heuristic IP" does NOT exist for this book — grouping is assignment + arithmetic.

---

## SUPPLANT-BLUEPRINT CLOSE (what the irreducible T2-COMPUTE actually is)
After chunks 1-4, the genuine-irreproducible-vendor-IP for the 49F/Schwab book reduces to a SMALL, bounded set:
1. **Parity-matching** our self-computed performance to BD's published statement numbers (Row 4A residual) — a verification, not a build.
2. **Lots-reconstruction** (base-DS chunk-1): IF BD reconstructs FIFO lots Schwab already delivers (RLD/ULN/ULT), that's *redundant* T2-COMPUTE we may not need (the leaner-methodology target).
3. **Any BD-served analytic the portal consumes DIRECTLY from BD** (not via our medallion) — the C-chain (C_00-C_08) is self-computed, but a full consumer census would harden this (bounded residual).
The Eclipse-class genuine T2-COMPUTE (rebalance/trade-generation engine) is an inf/Orion frontier, OUT of the 49F/BD scope (D3 §14).

---

## GROUNDING + RESIDUALS (2-axis confidence)
- **comp-rail:** comp-pipescript io C_00/C_02/C_03/B_03 (the perf+grouping chain); native source Read C_00 (methodology) + targeted grep C_02 (groupby key, rail-checked); live IO graph. SNAPSHOT-vs-FLOW: perf/grouping are mechanism-confirmed via SOURCE (our own code) — the strongest grounding (we read the algorithm, not infer it).
- **49F = DIFFABLE / source-confirmed-mechanism** (we hold + author the compute). **inf performance = case (b) proprietary frontier, INFERRED** — Orion computes performance below our reach (no Fidelity-raw; can't diff below Orion); do NOT project the 49F "standard-method/self-owned" finding to inf as proven. **cot = INFERRED** (BD-bounded).
- **Residuals:** (1) parity our-perf vs BD's-published-perf — not diffed (verification follow). (2) full consumer census for any BD-direct-served analytic — bounded. (3) lots-reconstruction = base-DS chunk-1. All INFERRED-flagged per Rule-22; no false-exhaustive.
