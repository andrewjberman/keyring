# work cycle — 0.4.2_RD_AdvisorIntelligence~C — 2026-06-02 ~1920Z

## ADVI_INFPRM.W2-FE — the MISSED FE half (HIGH-URGENCY, Andrew ground-truth) — IMPL-COMPLETE

### Trigger
COO [DRIVE-URGENT] relaying Andrew localhost ground-truth: Peter@inflectionwealth still sees Firm Overview NOT visible + own Book NOT viewable + Segment Analytics "No relationship-level data" — despite W1 (layout) + W2 (backend) both reported done. The FE fetch-wrapper firmId-threading fell between W1 and W2.

### Root cause
`advisor-intelligence.ts` fetch wrappers did `if (!firmOverride) throw 'firmOverride required'`. External Inflection (firmOverride=undefined) THREW client-side BEFORE reaching AE's W2-fixed backend. getPlatinumFirmDashboard's inner getClientsTab(undef) threw (caught -> clients_tab=null -> blank Firm Overview); getPlatinumAdvisorSummary(undef) threw -> blank book; etc.

### SCOPE FLAG (flagged COO): 9 throwers, not the 5 COO listed
COO's 5: 414 getClientsTab / 429 getClientDetail / 449 getAdvisorBook / 468 getBooksClientDetail / 503 getBooksFirmComposition. PLUS 4 more I found: 742 getBooksAdvisorComposition / 973 getPlatinumAdvisorSummary / 1303 getPlatinumAdvisorDrilldownSummary / 1381 getPlatinumClientSummary. All 9 eliminated (grep-confirmed zero throw statements remain).

### Fix (two shapes)
- **8 wrappers = omit-param**: `apiRequest(firmOverride ? base?firmId=... : base)` — external omits ?firmId=, backend JWT self-scopes (X-Firm-Id via edge; apiRequest attaches Bearer JWT — confirmed api-client.ts:147-155). Mirrors the outer getPlatinumFirmDashboard fetch + the file's non-throwing siblings. BYTE-IDENTICAL when firmOverride defined -> internal/49F/demo unchanged.
- **1 wrapper = firmId-threaded** (getPlatinumAdvisorSummary, the book fetcher): internal static-vs-Lambda routing keys on `firmOverride === 'inflection'` (false for external -> mis-routes to Lambda that doesn't adapt Inflection shape). Added 3rd param firmId; `resolvedFirm = firmOverride ?? firmId`; routes ext-Inflection to the static-S3 adapter. Callers AdvisorBookView/AdvisorPublicProfile/ClientsTab pass firmId (W1 prop). Mirrors W1.

### Evidence
- portal DEV **8ff69f18** (4 files, 52+/34-), pushed cfbf5336..8ff69f18, VALGATE PASS (schema-drift WARNs pre-existing, non-blocking). Scoped --only; RD~B's types.ts/DistributionTab excluded.
- tsc -b clean; eslint 0 errors (fixed the 1 dep-array warning I introduced at ClientsTab:422 = added firmId).

### End-to-end trace (logic-verified; rendered-pixel = Andrew, headless down)
- Firm Overview: getPlatinumFirmDashboard(undef)->inner getClientsTab omit-param->JWT->clients_tab populated. [logic-PASS/needs pixel]
- Book L2: getPlatinumAdvisorSummary(advisorId, undef, firmId='inflection')->static adapter. [logic-PASS/needs pixel]
- Book L3: usesStaticClientDetail (W1=true ext-Inflection)->getPlatinumClientDetailStatic (already non-throwing). [logic-PASS/needs pixel]

### Open / handoff
- **AE dependency-confirm** (sent): 8 omit-param wrappers rely on backend JWT-fallback per-endpoint. Static endpoints P0-confirmed; Lambda endpoints beyond clients-tab need AE confirmation. If any Lambda doesn't JWT-fallback, I thread explicit firmId to those callers.
- **RD~B hand-off** (sent): DistributionTab:1951 getPlatinumAdvisorSummary(drillParent!, firmOverride) = Segment Analytics; my wrapper fix stops the throw but full fix = RD~B passes firmId (one line). + the earlier pseudonymization-annotation (Andrew CLOSED-INTENTIONAL) still pending RD~B's file.
- **Andrew/CTO pixel-smoke** = closure gate (Firm Overview + book + Segment Analytics on Peter).
- RAVC2 + scope-flag to COO 191854Z; CVO verify 191926Z; CC CTO+AE+CVO+RD~B.

### Self-note
My earlier (1908Z) W2-FE pre-assessment looked at query PARAMETERIZATION but missed the fetch-wrapper THROW layer — the wrappers throw before the network call. COO's diagnosis caught it. Lesson: trace the fetcher BODY (throws/guards), not just the call-site args, when assessing a data-fetch path.
