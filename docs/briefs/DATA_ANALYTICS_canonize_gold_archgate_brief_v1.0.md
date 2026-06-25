# DATA_ANALYTICS — Canonize-Gold (Schwab-raw-native) ARCH-GATE BRIEF v1.0

> **SUPERSEDED AS A PRODUCTION GATE (Andrew-direct via DS, 2026-06-25; CTO `172040Z`).** Andrew reset the premise: the
> Schwab-raw-native canonical is **PARALLEL R&D that coexists with BD — no excise, no cutover, no contract-LOCK, no
> decommission.** This brief was written as a production arch-gate (G1–G3 excise/lock/sequencing); that framing is STOOD DOWN.
> **Retained only as R&D design rationale** (the strict-form / D-tier-waist / custodian-portable reasoning is still sound for
> the parallel build). Ignore the LOCK/excise/decommission/build-TO-decomposition language — none of it is staged. BD + the
> served $1.83B stay live and untouched.

**Author:** 0.4.0_DE_ClientPlatform (DE-lead, FE-down) | co-input 0.4.0_DS_ClientPlatform (gold-up)
**Date:** 2026-06-25 | **archetype:** COORDINATE
**FOR ARCH-GATE:** 1.0.0_SA_CTO | **cc:** 2.0.0_SA_COO, 3.0.0_SA_CVO | **Sovereign item routed to:** Andrew (N2, via COO)
**Locked input:** `docs/briefs/DATA_ANALYTICS_unified_portal_contract_v1.0.md` (co-signed DE+DS) — the portal contract this rebuild is built against.

> **Ask of the arch-gate:** ratify that the Schwab-raw-native canonize-gold rebuild is scoped to PRODUCE EXACTLY the unified portal
> contract (the platinum keys each ADVI panel reads, per partner) — nothing the portal doesn't consume, everything it does — with
> the 2 non-custodian inputs provisioned explicitly. On GO, COO decomposes the build-TO set against this contract.

---

## 1. What the contract establishes (the rebuild's target shape)

The portal contract is a closed vertical: `ADVI panel → component → platinum key → D-tier publisher → canonical silver table → Schwab-raw form`. The **D-tier (8 publishers) is the waist** — the only emitters of served artifacts — so the rebuild's gold output = exactly what the D-tier emits, and its silver input = exactly what the D-tier reads. Everything else is excisable.

**Three architectural facts the arch-gate ratifies:**
1. **Bronze = Schwab RAW forms** (RPS/ULN/RLD/TRN, untouched) — we hold 49F end-to-end ($1.63B Schwab AUA @06-18, direct from RPS; BD not needed to know what 49F holds).
2. **Silver = purpose-built dimensional tables** carrying ONLY the fields the D-tier reads (the contract's supply list).
3. **Gold = joins + analytics, daily-incremental** (no full recompute).

## 2. What the rebuild RETIRES (the excise set — collapses by construction)

| Retired | Why it dissolves under Schwab-raw bronze |
|---|---|
| B_01 FIFO lot reconstruction + `bd_stale`/`is_ghost` patches | lots come custodian-DIRECT (ULN unrealized + RLD realized) — no reconstruction |
| B_00 BD↔Schwab reconciliation layer | bronze IS the custodian raw; Schwab is custodian-of-record (the reconcile always picked Schwab anyway) |
| 90-day flag, entity hardcodes, inferred-tax keyword patch | aberration-excision runs at clean source (curated-list-then-rules, Andrew-steered) |

## 3. What the rebuild KEEPS (the analytics — firm-agnostic, rebuilt clean)
AUA decomposition (Growth/NNA, B_03) · performance attribution (C_00/C_02/C_03) · NNA-flow classification (C_01) · tax-lot gains (C_05) · mix/composition (C_06/D_03) · advisor attribution (C_07). These are the genuine value; rebuilt on Schwab-raw silver, daily-incremental.

## 4. Per-partner scope (essential vs agnostic — the lean cut)
- **49F (the Schwab-raw target):** essential = `D_04` (single publisher) + `D_00/D_00b/D_00c/D_00f/D_01/D_02/D_03`. Full panel set. **This is the rebuild's first/primary shape.**
- **Cottonwood (BD-native, follows 49F pattern):** essential = `D_00/D_00b/D_01/D_04` ONLY. **DROP** `D_00c/D_02/D_03/cohort_a/cash_coverage` (Advisors+Books disabled v1; re-add when COT advisor dimension materializes).
- **Inflection (Orion, distinct):** ~20 `INF_D_0x` — its own shape; NOT the Schwab-raw target (Orion is the supplant-prerequisite frontier, separate track).

## 5. ARCH-GATE DECISION ITEMS (CTO owns)

| # | Item | Recommendation | Status |
|---|---|---|---|
| G1 | Ratify D-tier-as-contract-waist + the bronze/silver/gold split | ACCEPT — independently confirmed two-sided (FE-consumer trace = DS backward-closure-from-D) | CTO call |
| G2 | Ratify the excise set (§2) — confirm no portal field depends on B_01/B_00 reconcile output | ACCEPT — FE1 trace shows no panel reads reconcile-only fields | CTO call |
| G3 | 49F-first sequencing (Schwab-raw target), COT-follows-pattern, INF-separate-track | ACCEPT | CTO call |
| **N1** | **FEES** — fee_bps/schedule NOT in Schwab RPS/ULN/RLD/TRN. Fee panels (FeeEfficiency/FeeSummary/fee_efficiency.json/advisor-client fee_summary) depend on it | provision a **fee feed** (Schwab billing OR retained BD-fees feed → A_02/C_08). Known dependency, not a blocker | CTO scopes the feed |
| **N2** | **HOUSEHOLD/RELATIONSHIP GROUPING** — Schwab `ssn_tin`=4,188 taxpayers vs portal `client_count`=2,928 BD-relationship grouping. Drives every client_count headline + client_directory + L3 client drill | **SOVEREIGN — Andrew ruling (bridge-via-xref vs Opal-owned dim).** COO surfacing now. Brief NOT blocked on it | **PENDING ANDREW** |

## 6. Sequencing (post-arch-gate)
1. CTO arch-gates G1–G3 + scopes N1 fee-feed. 2. Andrew rules N2 (household source). 3. CVO certs FE1 completeness + gap-4a. 4. DS co-signs unified contract. → **Portal contract LOCKS** as the rebuild input. 5. COO decomposes the build-TO set against the locked contract (silver-dim build, gold-incremental joins, D-tier re-emit on Schwab-raw, per-partner).

## 7. Status
Brief authored on the ratified parts (5 decisions DE+DS + §1–4 contract). **N2 marked PENDING-ANDREW (sovereign), N1 marked known fee-feed dependency — neither blocks the arch-gate of G1–G3.** Awaiting: CTO arch-gate (this brief) · DS co-sign (unified contract) · CVO cert · Andrew N2.
