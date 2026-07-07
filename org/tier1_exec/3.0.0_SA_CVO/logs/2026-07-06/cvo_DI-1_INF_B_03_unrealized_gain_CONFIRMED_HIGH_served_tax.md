# CVO verify: DI-1 (INF_B_03 unrealized_gain) -- CONFIRMED HIGH, served client tax overstated. Design->CTO.

**archetype:** VALIDATE (DIAGNOSE)
**serial:** 3.0.0_SA_CVO | **date:** 2026-07-06 ~2137Z | **source:** 0.4.0_DS_ClientPlatform~A DI-1 flag (ADHC_GLDINC INF-gold bug-hunt, Andrew-directed) | **method:** independent source + comp-pipescript + SERVED-artifact grounding (Rule 22 -- "materially overstated served tax" is a causal claim; verified, not accepted on self-report).

## VERDICT: DI-1 CONFIRMED HIGH (source-grounded + served-quantified). Design decision routed to CTO; CVO = verifier, not deciding the fix.

### All 3 claims source-confirmed
1. **MIXED UNIT UNIVERSE (confirmed):** `unrealized_gain = market_value - cost_basis` (INF_B_03:124-126). market_value = positions_cube units x price (INF_B_01:131; units <- gold/positions_cube, I_A03). cost_basis = canonical-CLAMPED current_units x cost_per_unit (INF_B_02:92-94 clamp lot units to gold/canonical/ Orion holdings). Two different unit anchors; the clamp exists because raw-txn units over-retain vs the positions API -> where they diverge, market_value(positions_cube) inflated vs cost_basis(canonical) -> gain overstated.
2. **FILLNA PHANTOM, silent (confirmed):** `market_value.fillna(0) - cost_basis.fillna(0)` on a how='left' merge (INF_B_03:115,124-126). Holding in B_01 absent from lots -> cost_basis NaN->0 -> unrealized_gain = FULL market_value (100% phantom gain); unpriced -> phantom loss. Left-join drops/raises nothing = silent.
3. **BLAST to served tax (confirmed):** comp-pipescript io -> gold/account_gains -> INF_C_03 (account_performance) + INF_C_05 (client_tax_liability, household qual/non-qual, short/long-term). Script's own comments (:215-228) name I_C05 served tax liability as the consumer.

### Served magnitude (quantified, gold/account_gains/2026-06-30 -- the latest served partition)
- Total served unrealized_gain: **$180,806,569**.
- PHANTOM limb: **2,546 rows** where unrealized_gain == market_value EXACTLY (cost_basis 0) = **$24,481,623** = **13.5% of served unrealized gain**, **588 distinct accounts**.
- The MIXED-UNIVERSE limb is ADDITIONAL (not in this measure; needs a canonical-unit recompute to size).
- => served client unrealized-gain / tax-liability overstated by >=13.5% on the affected accounts, ACTIVE on served data (not merely a latent code path).

### Design decision (CTO's call; DS~A framed 2, CVO severity-color)
- (a) UNIT ANCHOR [architecture call]: anchor market_value to canonical holdings (single base) OR derive market_value from canonical-anchored lots' current_units x price.
- (b) STOP fillna(0) -> NaN so downstream SUMS EXCLUDE missing rather than phantom-book. [Low-controversy; recommend regardless of (a) -- excluding-missing beats full-MV-as-gain for a tax number.]

### FIX-020 interaction
DS~A FIX-020 today (cc8956eb8) emits residual lots for canonical-held positions previously 100%-missing from gold/lots -> may REDUCE the phantom count on tonight's run. Folded into my cc8956eb8 lots-validation belt: I report the phantom-$ delta post-FIX-020 so CTO sees how much (b) still must catch.

## Compiler Tools
| tool | invocation | result | note |
|---|---|---|---|
| Read (INF_B_03/B_02/B_01) | market_value-cost_basis + fillna + unit-anchor provenance | PASS | all 3 claims source-confirmed w/ file:line |
| comp-pipescript io INF_B_03 | blast (consumers) | PASS | account_gains -> INF_C_03 + INF_C_05 (served tax) |
| aws s3 + pandas | quantify phantom on served 2026-06-30 | PASS | $24.5M / 13.5% / 588 accts phantom, ACTIVE on served |

## Disposition
CONFIRMED HIGH -> routed CTO (design ruling) CC COO + DS~A. CVO verifies the served delta post-fix (phantom-$ -> 0 + gain on a single unit base) before tax re-certifies. Also holding the cc8956eb8 (FIX-019/020) lots-validation belt on tonight's gold/lots. Surfaced to Andrew (his bug-hunt; client-tax-facing).

-- 3.0.0_SA_CVO
