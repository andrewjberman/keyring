# AUA Disparity Decomposition: Silver vs Gold — 1.0.0_SA_CTO

**Date:** 2026-03-26
**Source:** MCP message from 0.4.0_DS_ClientPlatform (20260326T211520Z)

## Context

DS sent an unsolicited AUA disparity analysis during the GLDRST.002 gold run. This is the first time the silver-vs-gold AUA gap has been fully decomposed to a $0.01 residual.

---

## Key Numbers

- **Silver AUA:** $1,599,738,414
- **Gold AUA:** $1,574,802,768
- **Total gap:** $24,935,645.78
- **Residual after decomposition:** $0.01

---

## Five Root Causes

| Bucket | Description | Amount | Accounts | Root Cause |
|--------|-------------|--------|----------|------------|
| **B0** | Accounts invisible to gold | $6,264,893 | 18 | Exist in BD allocations but zero transaction history. Script 00 builds accounts_dimension from transactions, so these never enter gold. Includes insurance/annuity (VUL, Structured Brighthouse), real estate ($3.75M across 2 properties), banking. |
| **B1** | Relationships with no gold data | $2,962,046 | 204 (158 rels) | All accounts have zero rows in positions_cube. BD reports AUA in client roster but no positions data exists. 162 are dust ($0 or <$100). 38 have real AUA ($2.97M). |
| **B3-universe** | Accounts with no positions inside gold relationships | $13,553,340 | 380 | Same root cause as B1 (no positions_cube rows), but these accounts belong to relationships where OTHER accounts DO have positions. Their silver AUA inflates the relationship total vs gold. **Single largest contributor.** |
| **B3a** | Pricing methodology diff | $71,344 | 5,842 | BD internal pricing vs canonical_prices (units * price). Gross $268M bidirectional, nets to near-zero. Includes bond face-value discrepancies (e.g., BNP PARIBAS: $20.7M gold vs $1.8M silver). |
| **B3b** | Ghost account exclusions | $2,084,022 | 4 | Script 05 excludes 4 accounts via aua_overrides.json. Silver includes them. Exact match confirmed: gold + ghost MV = recomputed total. |

---

## Key Insight

B0 + B1 + B3-universe are the **same root cause** (accounts with no positions data), just partitioned by where they land in the pipeline:
- B0: never enters gold at all (no transactions)
- B1: enters gold as a relationship but with zero positions
- B3-universe: other accounts in the relationship have positions, but these specific accounts don't

**Combined:** 602 accounts with $22,780,279 in silver AUA but zero positions data. This is **91.4% of the total gap**.

---

## Architectural Implications (return to these)

1. **B0 is a pipeline design decision, not a bug.** Script 00 builds accounts_dimension from transactions. Accounts with no transaction history (insurance, real estate, banking) are structurally excluded. Fixing this would require an alternative account ingestion path — e.g., building accounts_dimension from BD's client roster instead of (or in addition to) transactions.

2. **B3-universe is the biggest single bucket ($13.5M).** These accounts inflate relationship-level AUA in silver but contribute nothing in gold. Any relationship-level AUA display in the portal that sources from gold will undercount vs BD's own reporting. This matters for partner-facing analytics.

3. **B3a pricing diffs are noise.** $268M gross but $71K net — this is expected divergence between BD's internal pricing and our canonical prices. Not actionable unless a specific bond valuation causes a visible anomaly.

4. **B3b ghost exclusions are by-design.** The 4 accounts in aua_overrides.json are excluded deliberately. This $2.08M is a known, auditable gap.

5. **The -3.6% structural gap from ADVI_GLDPRE/ADVI_PRICES is now fully explained.** This decomposition provides the evidence base for that number.

---

## Next Steps

1. **Return to this when scoping GLDRST P3+** — the pre-computed views and restructured S3 layout should document which AUA definition they use (gold-only vs silver-inclusive)
2. **Consider a B0 fix as a future project** — alternative account ingestion from BD client roster for non-transactional accounts (insurance, RE, banking)
3. **Portal AUA displays should footnote the gap** — "AUA reflects securities with positions data; excludes insurance, real estate, and banking accounts"
