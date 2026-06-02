# work cycle — 0.4.2_RD_AdvisorIntelligence~C — 2026-06-02 ~1952Z

## ADVI_INFPRM.W4b — mirror 49F admin/non-admin tab-gating onto Inflection — IMPL-COMPLETE

### Dispatch
COO SENIOR_DISPATCH (org/projects/task_orders/ADVI_INFPRM.W4b...md). Andrew access-model (CTO PRD §3.W4, d2c96bb1b): admins (Peter, firmRole=admin) = full Books tab (advisor list + Firm Overview + BI); non-admins (Patrick/Joe, firmRole=null) = Profile tab ONLY (own profile/book), NO Books/FO/BI. FE-only (AE owns W4a provisioning).

### Root + fix (portal DEV 4b8375ab)
ROOT: inflection/index.tsx tabs = isFirmAdmin ? adminTabs : (nonAdminTabs.length>0 ? nonAdminTabs : adminTabs) fell EVERYONE back to adminTabs because nonAdminTabs was EMPTY (layout advisorPublicProfile.enabled=false + advisors.enabled=false). So non-admins WRONGLY saw admin tabs.
FIX (mirror 49financial:145/279/284):
1. inflection/layout.ts: advisorPublicProfile.enabled false->true -> nonAdminTabs=[profile] (advisors stays disabled = Profile-ONLY, exactly Andrew's intent). Matches 49F (true) + demo (true).
2. inflection/index.tsx:145: dropped the fallback -> tabs = isFirmAdmin ? adminTabs : nonAdminTabs.
3. books branch +isFirmAdmin guard (49F:279); profile branch !isFirmAdmin (49F:284, already present). NonAdminProfileTab renders own profile/book via the W1+W2-FE static-adapter path (firmId threaded).

### Regression (logic-verified)
- 49F/demo: separate files, untouched. UNCHANGED.
- internal (Opal admin viewing Inflection): isFirmAdmin=internal=true -> adminTabs. UNCHANGED.
- inflection external admin (Peter post-W4a): isFirmAdmin=true -> adminTabs (same as today; the fallback also gave admin tabs). UNCHANGED.
- inflection external non-admin (Patrick/Joe): WAS adminTabs (fallback bug) -> NOW [profile] Profile-ONLY. THE INTENDED FIX.
- No BI-leak: useTabNavigation inits activeTab=defaultTab with NO URL/localStorage restore + NO deep-link (read the hook). Non-admin defaultTab='profile', only Profile tab shown -> can never reach distribution/advisors/books branches. So the unguarded distribution/advisors branches are unreachable for non-admins (matches 49F, which doesn't guard them either). books+profile guards meet AC-W4b.
tsc -b + eslint green.

### BUILD-FINDING (TO asked to confirm): RD~B Segment :1951 NOT subsumed by W4a
TO hypothesized RD~B's DistributionTab:1951 firmId-add might be subsumed by W4a's admin-provisioning. CONFIRMED NOT: Peter is an EXTERNAL admin, so firmOverride = (internal ? FIRM_ID : undefined) = undefined regardless of firmRole=admin. So his Segment advisor-drill (getPlatinumAdvisorSummary(drillParent, firmOverride=undefined), no firmId 3rd-arg) still routes resolvedFirm=undefined -> Lambda (degraded Inflection shape) not the static adapter. The :1951 firmId-add is STILL NEEDED for Peter's Segment drill to render correctly. Flagged COO+RD~B.

### Open
- Andrew pixel-smoke BOTH admin (Peter) + non-admin (Patrick/Joe) inflection login = closure gate. Promote HELD for coherent joint re-smoke (W4a + W4b + FO/book).
- RD~B :1951 firmId-add (not subsumed) — RD~B's lane, via COO.
RAVC2 COO+CTO+CVO. portal DEV head 4b8375ab.
