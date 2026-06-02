# ws-charter cycle 0032 — 2026-06-02 1649Z

**Class:** NOVEL (Andrew-direct — 2 PRDs authored + distributed)
**Serial:** 1.0.0_SA_CTO (ws CTO, Tier-1)

## Direction
Andrew direct: (1) write ADVI_INFOTD for the out-the-door items (AUA->AUM + Count), (2) write ADVI_INFPRM for the firm-scoped permissions/auth cluster, distribute both to COO; then NNA.

## Action — 2 PRDs (committed e5f750f7f, pushed)
- **ADVI_INFOTD** (docs/architecture/ADVI_INFOTD.md): out-the-door FE polish, bundles with S5 promotion.
  - W1 AUA->AUM relabel: AdvisorIntelligence ALWAYS firm-scoped -> unconditional (~90 sites); ModelPortfolios conditional on effectiveFirmId!=='global' (~15); ~105 total/~24 files; labels-only NOT keys; assetsLabel() helper rec.
  - W2 per-firm Count: FE+DATA; rollup build_aggregate_aua_timeseries.py:191-218 drops the model-only account_count the partition already computes; DS rollup add + RD type+FE consume.
- **ADVI_INFPRM** (docs/architecture/ADVI_INFPRM.md): firm-scoped resolution sweep.
  - CONFIRMED single root cause via code read: _partners/inflection/index.tsx:154 firmOverride=undefined for external users -> _shared consumers (AdvisorPublicProfile:1155, AdvisorBookView:143, ClientsTab) resolve layout+data from firmOverride alone -> DEFAULT_LAYOUT(49F)+failed fetches. Role Composition wrongly shows, Firm Overview missing, Book view fails. = the ADVI_INFMVP F1 audit-sweep (F1 fixed PartnerAnalytics identically).
  - NOT a stale entitlement record (firmId provisioned — verified in S5). Ruled out Andrew's literal "permissions" framing, kept the spirit (firm-scoped identity not flowing into gates).
  - P0 sweep -> W1 layout-from-firmId (SHARED.006 two-param useTenantLayout) -> W2 data-routing (RD FE; AE conditional if edge). Regression matrix across 49F/demo/internal MANDATORY (asymmetric bug).

## Distribution
- HANDOFF x2 -> 2.0.0_SA_COO (broker 20260602T164932Z): register both projects + decompose. Owners RD~B primary both, DS INFOTD-W2, AE conditional INFPRM-W2, CVO verify. CTO sequencing rec: INFOTD ships w/ S5 (1st promotion), INFPRM 2nd; Andrew final call. Promotion HELD.

## Method note
Andrew interrupted the spawned permissions-investigation agent; honored that — did light self-directed code reads (no spawned agent, no PII/DynamoDB entitlement reads) to confirm the root cause. Grounded both PRDs in exact file:line.

## Next
- COO registers + decomposes -> RD~B/DS execute. INFPRM P0 can start in parallel now (lanes live).
- Per Andrew's sequence: PRDs done+distributed -> clear to move to the NNA discussion.
