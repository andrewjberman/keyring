# work cycle — 0.4.2_RD_AdvisorIntelligence~C — 2026-06-02 ~1908Z

## NO new dispatch — productive W2-FE pre-assessment (read-only) while gated

W1 awaiting Andrew/CTO visual smoke (human); DistributionTab annotation apply-decision pending COO; W2 not yet dispatched to AE. Used the gap to pre-assess the W2-FE side so it's instant when AE's W2 lands.

### Symptom 2 (Firm Overview absent for external Inflection) — FE data path traced
`ClientsTab.tsx` (BooksTab): Firm Overview gates on `clientsTabData` (L306 useMemo) <- `dashboardQuery.data?.clients_tab.headline`. The 3 firm-level queries (L195-208):
- `dashboardQuery`  = getPlatinumFirmDashboard(firmOverride), key ['platinum-firm-dashboard', firmOverride]
- `mixQuery`        = getPlatinumFirmMixSummary(firmOverride), key ['platinum-firm-mix-summary', firmOverride]
- `headerQuery`     = getHeaderMetrics(firmOverride),          key ['header-metrics', firmOverride]

All keyed/parameterized on `firmOverride` ONLY. For external Inflection firmOverride=undefined -> fetchers hit the firm-dashboard Lambda with no ?firm= -> P0's "?firmId=-no-fallback" -> empty -> Firm Overview absent. This is Symptom 2's FE leg.

### W2-FE decision (depends on AE's W2 backend design)
- **If AE's W2 = Lambda resolves firmId from JWT/X-Firm-Id when ?firm= absent** (backend-only fallback): **ZERO FE change** — the existing `getPlatinum*(firmOverride=undefined)` calls work once the Lambda JWT-falls-back. Cleanest; recommend this.
- **If AE's W2 expects the FE to pass an explicit firm key**: small FE thread — pass `firmOverride ?? firmId` to the 3 fetchers + update the 3 query keys to `firmOverride ?? firmId`. firmId is already a prop in BooksTab; the `effectiveFirmKey = firmOverride ?? firmId` pattern already exists at inflection/index.tsx:155, and it mirrors my W1 two-param contract + the F1 PartnerAnalytics:173 `firmId ?? firmOverride`.
  - Cache note: changing the key from `firmOverride` to `firmOverride ?? firmId` merges external-Inflection + internal-admin-viewing-Inflection onto the same 'inflection' key — CORRECT (same firm data), not a collision.

### Coordination
Sent AE the contract pre-assessment (CC COO) so AE can pick JWT-fallback deliberately = no FE change. Ready to execute either path the moment W2 lands. No code touched (read-only). W1 CVO-PASS'd (b71a0d6d3); DistributionTab finding CLOSED-INTENTIONAL pending annotation (COO apply-decision).
