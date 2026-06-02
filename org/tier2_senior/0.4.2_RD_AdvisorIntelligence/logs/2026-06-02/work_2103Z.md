# work cycle — 0.4.2_RD_AdvisorIntelligence~C — 2026-06-02 ~2103Z

## ADVI_INFPRM.W4g — Joe Profile tab "not mapped right" — DIAGNOSED (FE correct; gap = AE advisorId)

### Dispatch
COO W4g (Andrew mid-smoke): Joe Distribution WORKS (W4f); Profile tab "still isn't mapped right. Profile should literally be the AdvisorPublicProfile view." COO's comp-tools narrowed to invocation/wrapper, not the component. Asked me to diagnose + fix the NonAdminProfileTab wrapper + run comp-tools myself.

### Diagnosis (comp-tools + full fetch-resolution trace) — FE is CORRECT for external Joe
- comp-transform schema-check AdvisorPublicProfile: only UNUSED fields, ZERO MISSING/runtime-undefined -> component correctly wired.
- comp-trace: 5 self-fetches. EVERY fetch in Joe's Profile path resolves firm for external (firmOverride=undefined):
  - getPlatinumAdvisorSummary(advisorId, firmOverride, firmId): firmId-threaded (W2-FE) -> static adapter (explicit ?firm=inflection).
  - getPlatinumAdvisorDrilldownSummary: omit-param (W2-FE) -> JWT-resolve.
  - getAdvisorExecSummary(:1359), getPlatinumAdvisorTimeseries(:1282), getAdvisorNnaCanonical(:636): `firmOverride ? base?firm= : base` -> omit on undefined -> JWT-resolve.
  - employeeData = getFirmLeaderboard(firmOverride)(:1745): omit-param -> JWT-resolve. CORRECTED COO point-2: NO firmId-fallback gap; SAME query AdvisorsTab uses for Peter's admin drill.
- Invocation vs admin drill (AdvisorsTab:512-518): functionally EQUIVALENT (same employeeData/advisorId/firmId/firmOverride; diffs = cosmetic showBackButton/onBack + IGNORED accessPolicy/roleMeta).

### Conclusion
FE renders the literal AdvisorPublicProfile GIVEN a valid advisorId. The gap is the PRECONDITION nonAdminAdvisorId=claims?.advisorId (index.tsx:173). If Joe's JWT lacks advisorId -> null -> "Advisor Identity Unavailable" placeholder = what Andrew sees ("not mapped right"). AE-owned (Joe JWT advisorId=joe_brandenburg, partnerIdentity build; COO dispatched AE).

Did NOT make a speculative FE change — threading firmId / wrapper tweaks won't fix a null advisorId, and a cosmetic edit would falsely imply a fix + mislead the re-smoke (verify-not-assume + don't-manufacture-a-non-fix).

### Ready-if-needed (hedge)
If AE confirms advisorId PRESENT and it STILL renders wrong: next FE suspect = static-S3 JWT-injection for exec_summary/timeseries/nna (those rely on edge X-Firm-Id, unlike getPlatinumAdvisorSummary's explicit ?firm= via firmId). I can thread firmId explicitly into those 3 fetches (W1/W2-FE pattern) to remove the JWT-injection dependency — staged, ready on AE's confirm. (Headless-down: static + comp-tools analysis, no runtime confirm.)

### State
W4g DIAGNOSED. Routed to AE (advisorId confirm) via COO 210343Z (CC CTO+AE+CVO). Promote still HELD (Joe profile gates the joint re-smoke). Nothing I can commit until AE's advisorId finding.

### VALIDATED (~2105Z) — diagnosis confirmed correct on both fronts
- AE confirmed the exact gap: Joe existed only in opal-users-v2 (auth), no opal-partner-inflection partnerIdentity -> JWT advisorId=null -> claims.advisorId=null -> "Advisor Identity Unavailable" placeholder. AE FIXED: created opal-partner-inflection joe@inflectionwealth.com (advisorKey=joe_brandenburg, advisorRole=architect, firmRole=user). Fresh login -> Joe's Profile renders his own book.
- COO: W4g SUBSUMED into W4f (FE was correct; no separate build); flipping W4f TO -> IMPL-COMPLETE.
- TOGGLE-ROLE flag resolved by AE's fix: advisorRole=architect -> Group 3 -> canSeeBookToggle(scope!==1)=TRUE -> Joe sees the Profile|Book toggle. No FE/policy change.
- The verify-not-assume call held: routing the advisorId gap to AE (vs manufacturing a speculative firmId-thread that wouldn't touch a null-advisorId placeholder) was correct. The staged firmId-thread for exec/timeseries/nna was NOT needed.
- GO gate now: Andrew Joe re-smoke (fresh login) on c009f98c + CVO W4f re-verify -> CTO GO -> fire 5-phase. Promote warm.
