# work cycle — 0.4.2_RD_AdvisorIntelligence~C — 2026-06-02 ~1926Z

## ADVI_INFPRM.W2-FE — Symptom-2 REWIRE (the real fix) + Symptom-3 trace + PII annotation closed

Continuation of work_1920Z (the 9 throw-fixes, 8ff69f18). AE's live-trace + COO relay revealed the throw-fix was the PREREQ, not the full Symptom-2 fix.

### Symptom 2 (Firm Overview) — actual mechanism + REWIRE (3753139e)
AE traced live portal/DEV: ClientsTab reads clientsTabData = dashboardQuery.data?.clients_tab, but shared-advisor-router **v10 "platinum/firm/* numerical-only" carve-out STRIPPED clients_tab (PII) out of the static dashboard.json** (served = 308b, no clients_tab key) -> clientsTabData always null -> Firm Overview gate (:818) never rendered. clients_tab now serves from the getClientsTab Lambda (pseudonymizing).
- FIX (3753139e): ClientsTab clientsTabData sources from a `getClientsTab()` useQuery (key ['clients-tab', firmOverride], enabled !!firmId) instead of dashboardQuery.data.clients_tab. Depends on the 8ff69f18 throw-fix (getClientsTab no longer throws for external-no-firmId) + AE's W2 (partners-api-v1.16.2 JWT-fallback, CVO-SECURITY-PASS). dashboardQuery retained for employee_leaderboard/fee_efficiency.
- Trace: external Peter -> getClientsTab(undefined) -> omit ?firmId= -> W2 JWT-fallback -> 200 ClientsTabResponse -> renders. Internal/49F/demo pass firmOverride -> unchanged. [logic-PASS / needs Andrew pixel]

### Symptom 3 (Book view) — FE-leg logic-verified (no separate commit beyond 8ff69f18+W1)
AdvisorBookView:169 getPlatinumAdvisorSummary(advisorId, firmOverride=undef, firmId='inflection') -> resolvedFirm='inflection' -> static-S3 adapter (no throw, correct routing). FE-path correct. RENDER depends on Peter's advisorId claim + book.json artifact existing (DATA/AUTH). If pixel shows book blank after e6df1678, residual = data-side -> route DS/AE.

### PII annotation (e6df1678) — finding CLOSED-INTENTIONAL
COO (b)-approved self-apply. DistributionTab pseudonymizeChildLabel skipPseudonymize annotated INTENTIONAL (Andrew ruling 2026-06-02): external Inflection pseudonymized by design, NOT the W1 firmId bug. Comment-only; COO relays RD~B to rebase.

### Commits (portal DEV, head e6df1678)
- 8ff69f18 — 9 firmOverride-required throw-fixes (prereq + Symptom-3 book routing)
- 3753139e — ClientsTab clients_tab -> getClientsTab() rewire (Symptom-2 Firm Overview)
- e6df1678 — DistributionTab pseudonymize INTENTIONAL annotation

### Open
- Andrew PIXEL-SMOKE = closure gate (Firm Overview + book + Segment on Peter). NOT claiming closed until pixels confirm — the layer-local IMPL-COMPLETE missed this twice; explicit logic-vs-pixel separation now.
- RD~B (via COO): Segment Analytics DistributionTab:1951 needs firmId 3rd-arg (one line); + rebase the annotation.
- AE: W2 backend JWT-fallback covers both gate blocks (confirmed) = enabler for Firm Overview leg.
RAVC2 COO 192557Z; CVO verify-update 192603Z; AE loop-closed 192613Z.

### Lesson (carry-forward)
TWICE this session a layer-local "IMPL-COMPLETE" missed the real break: (1) pre-assessed query params but missed the wrapper THROWS; (2) fixed throws but missed that the consumer reads from a SOURCE (dashboard.json) the data was carved out of. END-TO-END = trace from the rendered gate BACKWARD through every source/transform to the network + the served artifact's actual bytes — not just the layer you're editing. AE's "pull the served artifact + grep the consumer" caught both. Mirrors memory feedback_verify_against_served_artifact_not_partial_proxy.
