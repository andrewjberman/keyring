# MDPF_ASSETS WS-E — 49 Financial Black Diamond Book: Custody-Cutout Audit

**Finding brief — Phase 0 (investigation)**
**TO:** MDPF_ASSETS.001 (`dsa-49f-blackdiamond-book-custody-cutout-audit`)
**Author:** 0.4.0_DS_ClientPlatform~A
**Date:** 2026-05-18
**PRD:** `docs/architecture/MDPF_ASSETS.md` v0.1 — §3.4, §4 WS-E, §6.2 Phase 0

---

## Verdict — one line

The §3.4 identity `non_model_aua(49F) = certified_aua − model_aua − Σ cutouts` **is structurally sound and daily-computable** — but the TO's "~$70M Fidelity-custodied" premise **does not hold empirically**: Fidelity-custodied assets are **$12.96M (12 accounts)**, not ~$70M. The real custody cutout is dominated by **ByAll Accounts — $135.6M of held-away aggregated assets**. Total custody cutout ≈ **$149.7M**, which brings the current naive non-model figure from **$455.3M → ~$305.6M** — reconciling closely to the historical ~$271M plug. The one true gap: **no machine-readable custodian attribute exists on the certified_aua source** (`silver/allocations`); it must be joined in from a second artifact (`silver/fees`).

---

## AC1 — The Fidelity cutout, confirmed empirically (premise corrected)

### How certified_aua is built (grounding)

`certified_aua` is produced by `data/black_diamond/scripts/gold/E_19.write_aua_certification.py`:
it is the **sum of `account_market_value` over `silver/allocations/{date}.parquet`, excluding exactly three liability `account_type`s** (CreditCard, Mortgage, Loans). Nothing else is excluded.

Verified to the cent for 2026-05-14: my recomputation = `$1,812,432,585.32` = the published `gold/aua_certification/2026-05-14.json` `certified_aua` exactly. The book is 6,706 accounts (6,676 after liability exclusion).

### The custodian attribute is NOT on the certified_aua source

`silver/allocations/{date}.parquet` (92→90 columns; the raw `ALLOC_DAILY_*.xlsx` Black Diamond export has **92 columns**) carries **no custodian field** — not dropped by the silver converter, genuinely absent from the Black Diamond "allocations" report 49F configured. There is no `Billing Account Custodian`, no custodian code, nothing.

The custodian attribute lives in a **different** Black Diamond report — the daily **Fees** report (`Fees_OpalCapital_Daily_*.xlsx` → `silver/fees/{date}.parquet`), column **`billing_account_custodian`**, keyed by `account_id` (the BD `AccountID`, which joins 1:1 to `silver/allocations.account_id`).

`silver/fees` is **transaction-grain** (fee transactions, ~1,000 rows/day) — not an account roster — so a stable `account_id → custodian` crosswalk must be built by aggregating fee history. I built it from **all 1,855 `silver/fees` partitions (2020-03-06 → 2026-05-14, 3.3M fee rows, 10,442 distinct accounts)**. Custodian is **perfectly stable per account** — 0 accounts ever show >1 custodian — so the crosswalk is reliable.

### The empirical custody decomposition of certified_aua (2026-05-14)

| Custodian | MV | % of certified_aua | Accounts |
|-----------|---:|---:|---:|
| Schwab | $1,655,447,182.20 | 91.34% | 6,146 |
| **ByAll Accounts** | **$135,602,222.34** | **7.48%** | 500 |
| **Fidelity IWS** | **$12,955,930.66** | **0.71%** | 12 |
| (unmatched — no fee record ever) | $7,273,392.78 | 0.40% | 15 |
| **DST** | **$1,153,857.35** | **0.06%** | 3 |
| **certified_aua** | **$1,812,432,585.32** | 100% | 6,676 |

The unmatched bucket is just **15 accounts / $7.3M**, all opened 2025-03 → 2025-12 (new accounts not yet in any fee cycle).

### AC1 result — the premise is corrected

- **Fidelity-custodied assets = $12,955,930.66 across 12 accounts** — identifying attribute: `silver/fees.billing_account_custodian == 'Fidelity IWS'` (Fidelity Institutional Wealth Services). This is the empirically-confirmed Fidelity figure. **It is ~$13M, not ~$70M.**
- The PRD §3.4 "~$70M Fidelity-custodied" figure is **not supported by the data**. No single custodian totals ~$70M. The closest interpretations: ByAll Accounts *excluding* its insurance-typed accounts ≈ $78.7M; or the figure is a stale/mistaken estimate. **The audit cannot confirm a ~$70M Fidelity slice — it does not exist in the current book.**
- The genuinely material non-Schwab custodian is **ByAll Accounts ($135.6M)** — see AC2.

---

## AC2 — Complete cutout enumeration

### Custody-based cutout candidates

| # | Custodian | MV (2026-05-14) | Accounts | Identifying attribute | Cutout rationale |
|---|-----------|---:|---:|---|---|
| 1 | ByAll Accounts | $135,602,222.34 | 500 | `silver/fees.billing_account_custodian == 'ByAll Accounts'` | **Morningstar ByAllAccounts** is a held-away **account-aggregation** service — outside/held-away accounts pulled into Black Diamond for financial-planning visibility. Account-type mix is classic held-away: Insurance $56.9M, IRA $17.2M, 401K $16.2M, Brokerage $15.8M, Annuity $4.0M, TermLife $1.8M, 403B $1.4M. Largest portfolio_group is "No Advisor" ($90.3M). **Strong cutout candidate** — these are not Opal-discretionary advised assets. |
| 2 | Fidelity IWS | $12,955,930.66 | 12 | `billing_account_custodian == 'Fidelity IWS'` | 12 accounts, mostly Corporate retirement plans (i401k, SIMPLE, BrokerageLink) — e.g. "Jeane Thomas - i401k" $6.5M. **Ambiguous** — could be genuinely Opal-advised accounts that custody at Fidelity rather than Schwab. Needs a business call (see AC3). |
| 3 | DST | $1,153,857.35 | 3 | `billing_account_custodian == 'DST'` | DST/SS&C mutual-fund-platform accounts. Immaterial ($1.2M). |
| 4 | (unmatched) | $7,273,392.78 | 15 | no `silver/fees` record | 15 new accounts (opened 2025) not yet fee-cycled — custodian unknown until their first fee event. Default-assign Schwab pending confirmation (49F is 91% Schwab). |

### Account-type-based cutout candidates

- **Insurance / annuity / life products.** `account_type` ∈ {Insurance $57.7M, Annuity, TermLife} — held-away insurance products. **Note:** `data/black_diamond/scripts/gold/insurance_accounts.json` lists 109 such accounts ($61.8M in the 2026-05-14 book, 105 of them ByAll-custodied). **This list is NOT an AUA-exclusion list** — `lib/exclusions.py` uses it only to apply a longer (180-day vs 45-day) active-account staleness gate. So insurance is currently *in* certified_aua and *in* the non-model figure. It overlaps heavily with the ByAll cutout (the $56.9M ByAll-insurance is the bulk of it) — **do not double-subtract**. If a cutout is defined custody-first (ByAll), insurance is already inside it.

### Was the audit exhaustive?

Yes for custody: every one of the 6,676 certified-eligible accounts was classified — 4 custodians + a 15-account/$7.3M unmatched residual, all reconciling to certified_aua to the cent. There are exactly **four custodians** in 49F's Black Diamond book: Schwab, ByAll Accounts, Fidelity IWS, DST. No others exist.

---

## AC3 — §3.4 derivation feasibility

```
non_model_aua(49F) = certified_aua − model_aua − Σ cutouts
```

### It computes — and it reconciles

Current live values (2026-05-15):

| Term | Value | Source |
|------|------:|--------|
| `certified_aua` | $1,812,432,585.32 | `gold/aua_certification/{date}.json` (BD pipeline, daily) |
| `model_aua` | $1,357,098,578.30 | `aum-timeseries.json` `aggregate[].aum` (SmartX, daily) |
| naive `non_model` (certified − model) | **$455,334,007.02** | what `non_model_assets.json` publishes **today** |
| Σ custody cutouts (ByAll + Fidelity + DST) | $149,712,010.35 | this audit |
| **`non_model_aua` (WS-E refined)** | **≈ $305,621,996.67** | certified − model − cutouts |

The frozen historical plug was **$271.2M** (Jan 2026). The WS-E-refined figure **$305.6M** is +$34M / +13% above it — consistent with ~4.5 months of market appreciation + book growth. **The cutout layer is what closes the gap**: the naive subtraction ($455M) is ~$184M too high precisely because certified_aua includes ~$150M of held-away custody plus the remainder is genuine growth. The §3.4 design is validated.

> **Note on the superseded brief.** `docs/briefs/smartx-non-model-live-derivation-20260513.md` (the WS-E starting point) has already been *partially* shipped — `non_model_assets.json` is no longer the frozen $272M plug; it now publishes the naive `certified_aua − model_aua = $455.3M` daily. WS-E Phase 1's job is to add the **cutout subtraction** ($455M → $306M).

### The gaps — named specifically (AC3 requirement)

1. **No custodian column on the certified_aua source.** `silver/allocations` has no custodian; `certified_aua` therefore cannot be custody-decomposed without joining `silver/fees`. The WS-E Phase-1 pipeline must build and maintain an `account_id → billing_account_custodian` crosswalk from the full `silver/fees` history (cheap — 0 conflicts, custodian is stable; rebuild as a gold-layer step). **This is the one real engineering gap.**
2. **`model_aua` is a SmartX-side figure, not BD-side.** The identity assumes `model_aua ⊂ certified_aua` — i.e. the SmartX-modeled assets are the same Schwab-custodied accounts BD aggregates. This holds in principle (49F's Opal-model accounts custody at Schwab; $1.357B model ⊂ $1.655B Schwab slice) but the two sides are **not account-keyed to each other** today — `model_aua` is a daily scalar, not a per-account series. A drift in either feed silently corrupts the residual. WS-A's convergent schema should make `model_aua` account-grain so the identity is reconcilable per §3.5, not just as a scalar subtraction.
3. **The cutout SET is a business decision, not a data fact.** The audit proves *what* the custodians are and *how much* each holds. Whether each is "not Opal advised AUA" is a judgment: ByAll Accounts (held-away aggregation) is a strong cutout; **Fidelity IWS is genuinely ambiguous** — 12 retirement-plan accounts that may be Opal-advised-at-Fidelity rather than held-away. DST is immaterial. **This needs an Andrew/CTO ruling before WS-E Phase 1 hard-codes the cutout set.**
4. **The 15-account/$7.3M unmatched bucket** has no custodian until each account's first fee cycle. Immaterial, but the Phase-1 pipeline needs a default rule (recommend: assume Schwab, the 91% prior; reclassify on first fee event).

### Verdict

§3.4 is **feasible and daily-computable** once (a) the custodian crosswalk is built into the gold layer and (b) the cutout set is ratified. It is **not** "not feasible" — but it is also not a pure `certified_aua` arithmetic identity: it needs a second artifact (`silver/fees`) joined in. Recommend WS-E Phase 1 proceed, gated on the AC3-gap-3 cutout ruling.

---

## Concrete data sources / paths for the WS-E Phase-1 build TO

| §3.4 input | Path / mechanism | Cadence |
|------------|------------------|---------|
| `certified_aua` | `s3://opal-data-bd/gold/aua_certification/{date}.json` `.certified_aua` | Daily (BD gold chain; T-1) |
| certified_aua source detail | `s3://opal-data-bd/silver/allocations/{date}.parquet` — `account_id`, `account_market_value`, `account_type` | Daily |
| **custodian crosswalk** | `s3://opal-data-bd/silver/fees/{date}.parquet` — `account_id`, `billing_account_custodian`; aggregate all partitions → stable `account_id→custodian` map | Daily (fees report; build crosswalk as a gold step) |
| `model_aua` | `s3://opal-data-portal-v2/json/portfolios/aum-timeseries.json` `aggregate[].aum` (SmartX) | Daily |
| Output (existing contract) | `s3://opal-data-portal-v2/json/portfolios/non_model_assets.json` — already live, already certified_aua-based; WS-E Phase 1 adds the cutout subtraction | Daily |
| Producer of certified_aua | `data/black_diamond/scripts/gold/E_19.write_aua_certification.py` | — |

---

## Compiler Tools

| Tool | Result |
|------|--------|
| `aws s3 ls s3://opal-data-bd/gold/aua_certification/` (TO Phase-0 mandate) | PASS — daily partitions present, latest `2026-05-14.json` written 2026-05-18 00:37Z. The certified_aua input is fresh; no WS-E Phase-1 freshness dependency. |
| `comp-pipescript io E_19` (TO Phase-0 mandate) | `comp-pipescript io E_19.write_aua_certification` returned "Script not found" (the graph indexes the script node as `E_19`, not the dotted filename). The I/O surface was established by reading the script directly: **READS** `gold/client_performance.parquet`, `silver/allocations/{date}.parquet`; **WRITES** `gold/aua_certification/{date}.json`. The 49F custody breakdown is **not** carried by any BD gold script — it required a direct `silver/allocations × silver/fees` join (this audit). Logged as a `comp-pipescript` gap: dotted-filename script args don't resolve. |

The audit's empirical core is the `silver/allocations` × `silver/fees`-crosswalk join — pandas over S3 parquet, not a graph trace.

---

## Recommendation to COO

**WS-E Phase 1 is feasible — author the build TO, gated on one ruling.** The §3.4 identity reconciles ($455M naive → $306M refined ≈ the historical $271M plug + growth). The build TO scope: (1) a gold-layer step that builds the `account_id→custodian` crosswalk from `silver/fees` history; (2) the cutout subtraction in the `non_model_assets.json` producer.

**Escalation to Andrew/CTO before the build TO is finalized:** the cutout SET is a business decision. Empirically — Fidelity is $13M not $70M; the material held-away custody is **ByAll Accounts $135.6M**. Andrew should confirm which custodians are "not Opal advised AUA": recommend **ByAll Accounts = cutout** (held-away aggregation, clear), **DST = cutout** (immaterial $1.2M), **Fidelity IWS = needs Andrew's call** (12 retirement-plan accounts, possibly genuinely advised-at-Fidelity). The PRD §3.4 text ("~$70M Fidelity-custodied — excluded") should be corrected to reflect the empirical decomposition.
