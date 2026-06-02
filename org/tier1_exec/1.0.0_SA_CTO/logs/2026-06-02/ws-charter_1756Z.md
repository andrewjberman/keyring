# ws-charter cycle 0036 — 2026-06-02 1756Z

**Class:** FIX (CTO adjudication/direction within active projects)
**Serial:** 1.0.0_SA_CTO

## Inbox (3, peer-CC)
- RD~B INFPRM.P0 finding (c35e3cd40): W1=3 FE useTenantLayout(firmOverride)->firmId sites (AdvisorBookView:143, AdvisorPublicProfile:1155, ClientsTab:150) fixes Symptom 1+3; W2=getClientsTab (advisor-intelligence.ts:414 throw) = ONLY true backend bug (Symptom 2), AE edge-fallback recommended.
- DS INFNNA W1+W6 DEPLOYED + served-verified: geo YTD==firm YTD==$4,225,486.45 (65% undercount ELIMINATED); W6 reconciliation all_pass=True/max_abs_delta=0.0 + granularity_coverage stamped; unified-additive+tiered as approved; clients sum==advisor to-the-cent, all 9 windows.
- RD~B drill-render-type ANSWER: city(L2)+client(L2) Continuous leaves DO chart a per-period time-series (computeLegacyBarData, DistributionTab:1325-1332) -> windows-only incomplete -> DS add light monthly series.

## Actions
1. DS DIRECT: add the light monthly per-city/per-client series at the L2 leaves (RD~B confirmed they chart) -> puts those leaves on canonical + lets W2 retire computeLegacyBarData. Re-stamp W6 recon at new grain, re-serve+verify. Ack'd W1+W6 deploy (undercount eliminated; W6 standing guard live).
2. INFPRM W1/W2 CTO SIGN-OFF to COO (author TOs): W1=RD 3 FE sites via SHARED.006 two-param useTenantLayout (regression matrix 49F/demo/internal MANDATORY); W2=AE EDGE FALLBACK (getClientsTab Lambda falls back to authorizer user_firm_id at lambda_function.py:1626 when ?firmId= absent) — concur RD~B; AE confirms the edge premise before build, else FE-thread fallback. INFPRM = 2nd promotion.

## State
- INFOTD bundle: COMPLETE on DEV (S5+NNA+W1+W2F) — awaiting Andrew visual smoke -> single promote GO. THE gate.
- INFNNA P2: W1+W6 DEPLOYED+verified (undercount gone at canonical, standing guard live); +light-monthly-series at L2 leaves directed; W2-FE (repoint+fallback-removal) + W4 (CVO rerunning vs served) next.
- INFPRM: P0 sized; W1/W2 signed off -> COO authors TOs (RD W1 + AE W2-conditional).

## Next
- Andrew smoke of INFOTD bundle = first PROD ship.
- DS light-series re-emit -> W2-FE repoint -> CVO W4 gate.
- COO authors INFPRM W1/W2; AE confirms edge premise.
