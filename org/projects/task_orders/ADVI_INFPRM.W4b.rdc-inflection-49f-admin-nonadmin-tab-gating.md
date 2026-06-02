<task_order>
<metadata>
  <to_id>ADVI_INFPRM.W4b</to_id>
  <project>ADVI_INFPRM</project>
  <title>RD~C: mirror 49 Financial's admin/non-admin tab-gating onto Inflection — non-admins (Patrick/Joe) get Profile-tab-ONLY; admins (Peter) keep the full Books/ tab. Remove the adminTabs fallback.</title>
  <assigned_to>0.4.2_RD_AdvisorIntelligence~C</assigned_to>
  <issued_by>2.0.0_SA_COO</issued_by>
  <issued_date>2026-06-02</issued_date>
  <status>DISPATCHED — W4(b) of the access-model. The MODEL (broader than the immediate Segment-unblock, which is W4a/AE provisioning). FE-only, no backend.</status>
  <dispatch_held>false</dispatch_held>
  <priority>HIGH — Andrew-direct access-model. Pairs with W4a (AE provision Peter admin). Together = Andrew's full admin/non-admin intent.</priority>
  <references>
    <ref type="prd">docs/architecture/ADVI_INFPRM.md sec.3.W4 (b) + AC4(b) (d2c96bb1b)</ref>
    <ref type="pattern">portal/src/pages/AdvisorIntelligence/_partners/49financial/index.tsx:145/241/279/284 (the canonical admin/non-admin split to mirror)</ref>
    <ref type="bug">portal/src/pages/AdvisorIntelligence/_partners/inflection/index.tsx:145 (adminTabs fallback shows ADMIN tabs to EVERYONE — opposite Andrew intent)</ref>
    <ref type="layout">portal/src/pages/AdvisorIntelligence/_partners/inflection/layout.ts:103 (advisors.enabled=false + advisorPublicProfile.enabled=false -> nonAdminTabs EMPTY -> the fallback)</ref>
  </references>
</metadata>

<scope>
Andrew (verbatim): "Admins (like Peter) should see all users' books in the advisor list including firm overview [+ BI, the Books/ tab]. Non-admins (like Patrick or Joe) should have a Profile tab like we do in 49 that has their profile/book, but they can't see the BI and firm overview and all that in the Books/ tab (they don't get a Books/ tab). Look at how 49 does it — we already have this pattern."

ROOT (CTO-traced): inflection's `tabs = isFirmAdmin ? adminTabs : (nonAdminTabs.length > 0 ? nonAdminTabs : adminTabs)` (index.tsx:145) falls EVERYONE back to adminTabs because inflection's nonAdminTabs is EMPTY (layout.ts:103 advisors + advisorPublicProfile both disabled). 49F does it right: `tabs = isFirmAdmin ? adminTabs : nonAdminTabs` + `activeTab==='books' && isFirmAdmin` + `activeTab==='profile' && !isFirmAdmin` (49financial:241/279/284).

The mechanism ALREADY EXISTS + is identical across firms: `isFirmAdmin = internal || claims?.firmRole === 'admin'` (inflection:128 = 49financial:160 = demo:135); firmRole flows from the user record into claims (AuthContext.tsx:121-125). So this is a CONFIG+WIRING mirror, not new infra.

## The work — mirror 49F onto inflection:
1. **Enable the non-admin Profile path in inflection's layout** — set `advisorPublicProfile.enabled=true` (+ whatever 49F enables for its NonAdminProfileTab) so inflection's `nonAdminTabs` is NON-EMPTY (a Profile tab carrying the user's own profile/book). Compare exactly to 49financial/layout.ts.
2. **Remove the adminTabs fallback** at inflection/index.tsx:145 — change to `tabs = isFirmAdmin ? adminTabs : nonAdminTabs` (the 49F form). Non-admins now get Profile-ONLY (no Books/ tab, no Firm Overview, no BI).
3. **Wire the NonAdminProfileTab** for inflection exactly as 49F (the activeTab guards :279/:284 — `books` admin-only, `profile` non-admin-only; default-tab selection per role).
4. **Regression matrix:** 49F + demo + internal UNCHANGED. internal (isFirmAdmin via `internal`) still sees admin. Verify no other inflection consumer relied on the fallback.
</scope>

<acceptance>
- [ ] AC-W4b(admin) — Peter (firmRole=admin, once W4a lands) sees the full adminTabs: advisor list + Firm Overview + BI + Books/ tab. Unchanged from today for admins.
- [ ] AC-W4b(non-admin) — a non-admin inflection user (Patrick/Joe, firmRole=null) sees Profile-tab-ONLY: own profile/book, NO Books/ tab, NO Firm Overview, NO BI. (This is the behavior change — today they wrongly see admin tabs.)
- [ ] AC-W4b(regression) — 49F / demo / internal tab-sets UNCHANGED (side-by-side compare).
- FE-only; no backend/edge (that's W4a/AE). RAVC2 to CTO+COO+CVO. RD~B's Segment :1951 firmId-add likely SUBSUMED by W4a's admin-provisioning — confirm in build before adding it.
- **Closure gate = Andrew pixel-smoke** on BOTH an admin (Peter) AND a non-admin (Patrick/Joe) inflection login — the end-to-end render gate, NOT layer-local IMPL-COMPLETE. Hold the promote until coherent with W4a + the FO/book re-smoke (no piecemeal portal promotes).
</acceptance>

<notes>
Decomposed by COO from CTO PRD §3.W4 (Andrew-direct d2c96bb1b). Pairs with W4a (AE: provision Peter admin + edge + ownership_map). W4a is the immediate Segment-drill unblock; W4b is the MODEL (non-admin restriction). Sequencing: with current code Peter already sees admin TABS (the fallback), so this TO doesn't block his FO/book re-smoke — but it's required for the non-admin half of Andrew's intent + removes the wrong everyone-sees-admin behavior. CC CTO + AE + CVO + RD~B. Coordinate the coherent promote with COO (all INFPRM promotes held til the joint re-smoke).
</notes>
</task_order>
