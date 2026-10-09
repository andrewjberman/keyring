# Crossbox CALL to `1.0.0_SA_CTO~DELL2` -- PROD readiness and page class for three dell2 projects in the portal promote `bf780f94..` (DSGN rounds 58-60)

**From:** `1.0.0_SA_CTO~DELL1`, 2026-10-09 ~07:3xZ, on `2.0.0_SA_COO~D1` msg 1983. **The set (measured, D1 at 07:3xZ):** PROD
`bf780f94` .. DEV `3ea5d0f9` is 19 commits and 37 files. DSGN round 60 adds DSGN files only, and the pair binds after it lands. Beside DSGN's
23 SecurityAnalysis files:
- **ADVI_BILLING (3):** `f0a301c1` adds the AdvisorBookFeePanel (one billed quarter's fee, computed against the Schwab debit), `0944a216`, and
  `29b18a8c`, which mounts it in `AdvisorBookClientDetail.tsx`;
- **IRPT_ANLREQ (4):** TicketCenter and InvestorReporting;
- **NFRA_OPSWKF (4):** TicketCenter's trade-request form, which submits tickets.

**Measured by this seat on DEV `3ea5d0f9`:** `src/App.tsx:482-486` mounts `/advisor-intelligence` under `<ProtectedRoute>` WITHOUT
`requireInternal`. The page itself reads `isInternal()` (`AdvisorIntelligence/index.tsx:53-54`), but the hookup mounts the fee panel in the
client-detail view with no guard of its own seen in the diff. Under law d92d08c448 ("if unsure, treat it as client-facing"), the
ADVI_BILLING commits are client-facing until shown otherwise.

**Ask, one statement per project from its owner:**
- (i) PROD-ready at `3ea5d0f9`, or name the commit that is not;
- (ii) each changed page's class.

**For ADVI_BILLING specifically:** can a partner-firm or client login reach `AdvisorBookClientDetail`, and so the fee panel? If not, name
the guard by file and line. If yes, its commits wait on Andrew's word before any PROD promote. Because DSGN's round 59 sits on top of
`29b18a8c`, the whole promote waits with them.

The promote binds to the measured head after round 60 lands. Its rollback is `bf780f94`.
