# DATA_SSOTMG — Canonical Headline-AUA Design + the Non-Schwab Threading

**Status:** DESIGN (grounded 2026-06-29) | **Owner:** 0.4.0_DS_ClientPlatform | **Gates:** the BD->canonical serving-flip (COO S7) | **Sovereign:** Andrew
**For:** the Schwab-SSOT cutover — keeping the firm TOTAL AUA consistent + threading the non-Schwab/held-away book cleanly, reaching the SAME Group-D Publisher endpoints with no client-side change.

---

## 1. The problem (why this is "more than a source swap")

The firm headline AUA is **not** a positioned-holdings number — it is a **reported-AUA number**: the BD **allocations book** (every account BD reports on, all custodians). Schwab gives us a clean *positioned* book; it does NOT give us the held-away/Fidelity accounts (no Schwab positions exist for them). So a pure Schwab-native pipeline can never reproduce the headline alone — the non-Schwab accounts must be **threaded in as AUA-only rows**, and the Schwab accounts must come from canonical WITHOUT double-counting BD.

## 2. The partition rule (Andrew-direct 2026-06-29)

> Any totals we have from Schwab are canonical-source on those accounts, and they should commensurately **not draw from BD**. Whatever accounts are left in the balance (non-Schwab) are the **surplus** amount.

```
Firm headline = SUM canonical(Schwab accounts)  +  SUM BD-allocations(accounts NOT in Schwab)
```
No double-count: an account is EITHER Schwab-canonical OR BD-surplus, never both.

## 3. Grounded reconciliation (2026-06-24, live artifacts)

```
BD allocations total (today's served book) ... $1,812,018,889   (6,811 accts)
   Schwab accts, BD's value ................... $1,542,494,758   (5,482) -> DROP, replace w/ canonical
   NON-Schwab "surplus" ...................... $  269,524,130   (1,329) -> KEEP (BD account_market_value)

canonical Schwab positioned (authoritative) .. $1,591,227,965   (5,894 accts)

CLEAN HEADLINE (the rule) = canonical(Schwab) + surplus
   $1,591,227,965 + $269,524,130 = $1,860,752,096
   vs BD-served $1,812,018,889  ->  +$48,733,207 move
```

### 3a. The +$48.7M move decomposes (the accept-vs-reconcile decision)
```
(1) ACCOUNT-SET  +$78,188,617   412 Schwab accts canonical HAS, BD allocations does NOT
                                (canonical more complete; xref @2026-04-21 is STALE -> won't bridge newer accts)
(2) VALUATION    -$29,455,410   on the 5,482 SHARED accts canonical is ~$29.5M LOWER than BD
                                (5,394/5,482 lower, median -$1,008/acct; NOT cash -- canonical $1.513B < BD ex-cash $1.542B;
                                 canonical = Schwab-direct RPS, BD = its own feed -> a price-date or price-source diff)
                 ────────────
            net  +$48,733,207   (reconciles exactly)
```
**Both effects say canonical is the better number** (more complete + more conservative/accurate). But it is a real upward move the firm sees -> a CONSCIOUS dispositioned decision at S7, not a silent delta. Open: (i) confirm the 412 are legit newer Schwab accts; (ii) confirm the -$29.5M is price-date vs price-source -- both need a FRESH xref (current is 2026-04-21).

## 4. The mechanism: `G0.held_away_aua` (one producer owns the non-Schwab union)

A new canonical-native producer (the "I never think about Fidelity again" surface):
1. READS: BD `silver/allocations/<date>` + a **REFRESHED** `account_xref` (bd_account_id <-> schwab_padded_id).
2. PARTITIONS every allocations account: bridges to a canonical Schwab positioned account? -> **SCHWAB (drop -- canonical owns it)**; else -> **NON-SCHWAB SURPLUS (keep BD account_market_value)**.
3. EMITS the surplus rows: `account_id, relationship_id, custodian {fidelity|held_away|other}, market_value, as_of, included_in_headline`.
4. Vintage-flagged (roles_source/as_of pattern) + carries the active/total inclusion flag so BOTH the header rule (~$1.75B) and the total ($1.82B) derive from ONE tagged book, not two computations.

WRITE: `canonical/schwab/gold/held_away_aua/date=YYYY-MM-DD/` (parallel/NOT-served). DS-owned. Same-firm bridge (49f), not a cross-firm mirror.

## 5. Threading into the A/B/C/D DAG (reach the same publisher, client untouched)

- The surplus rows join the canonical account set at the **A-tier / account_performance (G4/C_03) level** as **AUA-only** (no positions), exactly where BD's `positions_cube` silently unions all custodians today.
- They roll up at **D_00/G10 -> header_metrics** -> publisher. The D-layer + `bd-portal-publisher` see the full headline and never know the custodian split -> **no client-side change**.
- Publisher contract (must emit byte-schema-identical): `gold/artifacts/{timeseries_chart, architect_leaderboard, clients_tab, summary/header_metrics, filters/dimensions, snapshots/aua_by_*}.json`.

## 6. S7 cutover gate — TOTAL-AUA PASS criterion (folds into CVO S7)

The serving-flip CANNOT fire until, over the N-clean-days parallel window:
```
canonical(Schwab) + G0(non-Schwab surplus)  ==  the agreed firm headline
```
PASS requires: (a) the surplus reconciles per-account through a FRESH xref; (b) the +$48.7M Schwab-valuation delta is DISPOSITIONED (accept canonical-as-truth, or reconciled to BD with the price-date/price-source cause named); (c) the active/total flag reproduces both the header (~$1.75B) and total ($1.82B). Proven, not asserted. cc CVO (S7 owner), CTO.

## 7. Still owed to hit the publisher (the rest of the iceberg, from the seam pass)
Canonical A-tier gold dims (accounts/client/advisor/fee_rate + a Schwab positions_cube analog) · the C-bridges (`account_team` C_07, `mix_daily_summary` C_06, `role_aua` C_01b, `holdings_lots` B_01) · the D artifact-JSON layer (the 6 published files) · `G0.held_away_aua` (this) · the active/total flag. Analytics core G1-G14 is done + order-correct; this doc covers the headline-AUA + non-Schwab thread.

---
*Grounded vs live S3 (allocations 2026-06-24 $1.812B; canonical_holdings $1.591B; xref @2026-04-21; gold_dispatch.sh A/B/C/D order; bd-portal-publisher inputs). DATA_SSOTMG, 0.4.0_DS_ClientPlatform.*
