# DATA_SSOTMG -- Custodian-Native SSOT Architecture Directive

**Author:** 3.0.0_SA_CVO | **Date:** 2026-06-29 | **Authority:** Andrew-direct (sovereign architectural decision)
**Priority:** HIGHEST -- to begin BRIGHT AND EARLY 2026-06-30 (Andrew-set). **Routed to:** 1.0.0_SA_CTO (arch owner) | cc 2.0.0_SA_COO (orchestration), 0.4.0_DS + base-DS (build), 0.6.0 (cutover machine).

## The decision (Andrew, 2026-06-29)
**Black Diamond is DEMOTED from SSOT to a fenced low-priority surplus.** The 49F (and forward, the firm) Advisor-Intelligence
SSOT becomes the **CUSTODIAN** (Schwab) directly -- clean, monolithic, regular feeds (rps, uln/ult, rld, trn, ...). Recreate
the canonical silver fact/dim + gold CLEANLY from the custodian, **no patches, no weird per-account logic, canonical form**.
Staple the BD balance (the non-custodial held-away accounts) on top as an explicitly-fenced **surplus group**, quality-tolerated.

### Why -- the original SSOT choice was wrong, and the data now proves it
Andrew chose BD as the original SSOT (it had all the assets, easy programmatic ETL). Over the engagement BD revealed: **variable
per-account lag, missing data, dirty data, aberrations** -- "nonstop bullshit." The custodian, by contrast, ships clean
monolithic tables that retrieve trivially. The CVO correctness-track measurement (comp-parity day-1, 2026-06-29) **proves it
empirically, not anecdotally**:
- **Custodian = exact.** canonical_holdings vs `schwab/silver/rps` = **0/5,892 value-breaks, $0 max delta**; canonical_lots vs
  `schwab/silver/uln` = **0/3,793, $0**. The custodian feeds reconstruct the book to the cent.
- **BD = the noise, quantified.** canonical vs BD-served = **49% non-uniform break**; a uniform date-shift does NOT align it
  (canonical-06-18 vs BD-06-24 = 99.5% break, WORSE) -> the lag is per-account, not correctable; plus a clean **2x doubling**
  aberration on account 0066026837. **grounding: SOURCE-CONFIRMED** (the live parquet ties; commits 14749a998, 30de74914).

So "demote BD to surplus" is an evidence-backed decision, on the record with the data behind it.

## The custodian-native canonical model (the build target)
**Note: the custodian-native gold ALREADY EXISTS and is PROVEN (`canonical/schwab/gold`, G1-G14).** This directive is a
COMMITMENT (make it the SSOT, not a BD-validator) + a CLEANUP (purge BD-patch residue) + a FORMALIZATION (the surplus fence) --
NOT a from-scratch build. The clean schema, from the monolithic Schwab silver tables that already land:

### Silver -- custodian fact/dim (no BD middleman)
- **Dims:** `dim_account` <- `acc` + `account_xref` (advisor, relationship, tax_status, custody, the Schwab<->BD crosswalk) ·
  `dim_security` <- security_master (cusip, ticker, asset_class) · `dim_advisor`.
- **Facts:** `fact_position` <- `rps` (daily positions) · `fact_lot` <- `uln`/`ult` (unrealized) + `rld` (realized) ·
  `fact_flow` <- `trn`/`trn_nna` (transactions, NNA).

### Gold -- recreate cleanly from facts/dims, canonical form, NO patches
- **Passthrough (custodial primitives -- exact-tie PROVEN):** holdings (`fact_position`), lots (`fact_lot`).
- **Derived-on-proven-primitives:** nna, account_gains, performance, realized_gains, firm_composition, tax, advisor analytics
  -- each a clean derivation from the facts. Because every surface derives from the PROVEN `fact_position`/`fact_lot`/`fact_flow`,
  there is NOTHING to patch: a wrong number is a derivation bug, never a BD data-wart to special-case.

### BD surplus -- stapled on top, fenced, quality-not-guaranteed
- The held-away / non-Schwab accounts (~1,329 accts, ~$269.5M) carried from BD into a DEDICATED `surplus_non_custodial` layer:
  explicitly labeled low-confidence, NEVER mixed into the clean custodian core, NEVER patched. Firm-total = custodian-core
  (proven-exact) + surplus (known-tolerated), the two always separable in the served artifact.

## Build scope (for DS, arch-gated by CTO)
1. **Ratify the silver fact/dim contract** (the dims + facts above) as the canonical custodian schema -- one clean pattern, all firms forward.
2. **Audit + purge BD-patch logic from the gold scripts** -- enumerate every gold surface still carrying BD-reconciliation /
   special-case / 90-day-patch logic; replace with the clean custodian derivation. (CVO can pre-sweep which surfaces carry patch logic.)
3. **Formalize the surplus fence** -- the `surplus_non_custodial` layer + the served-artifact separation (core vs surplus always distinguishable).
4. **Wire the correctness gate** -- comp-parity two-track (already built, 34dba060c/30de74914) is the enforcement: the custodian
   core MUST tie the custodian exact (the hard cutover gate); BD is the informational cutover-jump only.

## Enforcement / verification (CVO)
The cutover gates on **CORRECTNESS (canonical vs custodian), never on vs-BD**. comp-parity two-track is the instrument
(`.tools/comp-parity`, `data/canonical/schwab/parity/49f_parity_config.yaml`): passthrough primitives exact-tie the custodian
(proven), derived surfaces reconcile on the proven primitives, BD is measured as the display-jump only. The multi-day CLEAN
correctness streak is the cutover gate.

## Priority + ownership
- **HIGHEST PRIORITY, 2026-06-30 bright-and-early (Andrew-set).** CTO owns the arch-gate + decomposition into DS build TOs.
- DS builds (silver contract + gold cleanup + surplus fence); COO orchestrates; CVO holds the correctness gate + pre-sweeps the BD-patch inventory.
- This supersedes the "BD-as-SSOT, canonical-as-validator" framing of the prior DATA_SSOTMG TO-4: canonical IS the SSOT now; TO-4's parity harness becomes the cutover-correctness gate for THIS model.

-- 3.0.0_SA_CVO
