<task_order>
<metadata>
  <to_id>ADVI_INFPRM.W4f</to_id>
  <project>ADVI_INFPRM</project>
  <title>RD~C: CORRECT the non-admin model — Inflection non-admins get [Distribution, Profile], NOT Profile-only. Distribution at full admin fidelity; Profile = AdvisorPublicProfile self-scoped w/ Profile|Book toggle.</title>
  <assigned_to>0.4.2_RD_AdvisorIntelligence~C</assigned_to>
  <issued_by>2.0.0_SA_COO</issued_by>
  <issued_date>2026-06-02</issued_date>
  <status>IMPL-COMPLETE (status flipped by COO per RD~C owned-paths request). Landed portal DEV c009f98c (RD~C, 1 file inflection/index.tsx, ci-green). Andrew confirmed Joe DISTRIBUTION now works. nonAdminTabs corrected [Distribution, Profile]; P2-a distribution isFirmAdmin guard REVERTED (was enforcing the wrong Profile-only model); Books branch STAYS admin-only (no-BI-leak invariant); Profile branch renders the LITERAL self-scoped AdvisorPublicProfile (advisorId=claims.advisorId, Profile default, Profile|Book toggle gated by canSeeBookToggle(scope)=scope!==1 ADVI_ROLGAT, NOT accessPolicy). W4g (COO Profile-tab dispatch) SUBSUMED — Profile branch was always wired to the literal AdvisorPublicProfile; comp-transform schema-check confirmed the component fields all match (issue was invocation/precondition, not component). REMAINING: (1) Andrew RE-SMOKE Joe on c009f98c (Distribution full + Profile w/ toggle); (2) AE precondition — Joe's advisorRole must be Group 2/3 for the Book toggle + JWT must carry advisorId (partnerIdentity build); (3) ANDREW DECISION — non-admin cross-advisor drill is edge-403 by-design (.004a self-scope): (a) FE-disable other-advisor drill targets [recommended] vs (b) edge .004a policy change + ownership_map for true cross-advisor 'Peter fidelity'. Promote HELD til Joe re-smoke green.</status>
  <dispatch_held>false</dispatch_held>
  <priority>URGENT — Andrew actively smoking; this is the non-admin half of the access model.</priority>
  <references>
    <ref type="andrew-verbatim">"Joe should see /Distribution tab in same fidelity and depth as Peter. However instead of a Books/ tab, Joe should see a 'Profile' tab. On that profile tab is the AdvisorPublicProfile, just like Peter has, which defaults to the 'Profile' toggle view, however can toggle to see his own book as well, just like Peter has. The only difference with Joe and peter is that Joe has the Books/ tab replaced with a profile tab, whereas Peter can navigate to his profile or any other advisors via the advisor list on Books/ tab."</ref>
    <ref type="bug">inflection/index.tsx:142-145 nonAdminTabs = [profile] only (Distribution dropped); :229 distribution render branch has `&& isFirmAdmin` (blocks non-admins); P2-a 328a8459 reinforced the wrong guard.</ref>
    <ref type="pattern">AdvisorPublicProfile.tsx (the Profile|Book toggle component Peter sees on advisor-drill) + 49financial NonAdminProfileTab usage (advisorId={nonAdminAdvisorId}).</ref>
  </references>
</metadata>

<scope>
W4b implemented the WRONG model (Profile-ONLY for non-admins). Andrew's correct model:

CORRECT INFLECTION TABS:
- ADMIN (Peter): [Distribution, Books]  — Books has the advisor list -> navigate to ANY advisor's profile/book + Firm Overview + BI. (unchanged — Peter is GREEN)
- NON-ADMIN (Joe): [Distribution, Profile]  — Distribution IDENTICAL to admin (same fidelity + depth); Profile REPLACES Books.

THE ONLY admin-vs-non-admin difference = the 2nd tab: Books (multi-advisor nav) for admin vs Profile (self only) for non-admin. Distribution is the SAME for both.

## The fix (inflection/index.tsx + layout.ts):
1. **nonAdminTabs MUST include Distribution.** Change `nonAdminTabs` (currently [advisors?(disabled), profile]) to **[Distribution, Profile]**:
   - `layout.tabs.distribution.enabled ? {id:'distribution', label:'Distribution'} : null,`
   - `layout.panels.advisorPublicProfile.enabled ? {id:'profile', label:'Profile'} : null,`
   So non-admins get Distribution + Profile (NOT Profile-only).
2. **Distribution renders for non-admins at full fidelity** — REMOVE the `&& isFirmAdmin` guard on the distribution render branch (:229), mirror 49F :263 (no guard). REVERT the P2-a hardening (328a8459) for the distribution branch — that guard enforced the wrong model. (advisors branch is moot — inflection advisors.enabled=false — but reconcile so distribution is ungated.)
3. **Profile tab = AdvisorPublicProfile self-scoped, Profile|Book toggle.** The Profile branch must render the SAME AdvisorPublicProfile component Peter sees when he drills an advisor from the Books advisor-list — scoped to the non-admin's OWN advisorId (from claims.advisorId; Joe=joe_brandenburg), DEFAULTING to the "Profile" toggle view, with a working toggle to view his OWN book (mirror 49F's NonAdminProfileTab advisorId={nonAdminAdvisorId}). CONFIRM the component provides the Profile|Book toggle (Andrew: "just like Peter has... we already have this pattern" in 49); if the inflection profile branch currently renders a stripped/no-toggle version, wire the full AdvisorPublicProfile-with-toggle.
4. defaultTab for non-admin = Distribution (tabs[0]) — same landing as admin; the "defaults to Profile toggle" is WITHIN the Profile tab, not the active-tab default.
</scope>

<acceptance>
- [ ] AC-W4f(non-admin tabs) — Joe (firmRole=null) sees exactly TWO tabs: Distribution + Profile. NO Books/ tab.
- [ ] AC-W4f(distribution parity) — Joe's Distribution tab = Peter's Distribution (same panels, same drill depth, renders fully — no blank/guard).
- [ ] AC-W4f(profile) — Joe's Profile tab renders AdvisorPublicProfile scoped to joe_brandenburg, defaults to the Profile toggle, toggles to his OWN book (his book.json). Same component/behavior Peter sees when he drills himself from Books.
- [ ] AC-W4f(admin unchanged) — Peter still [Distribution, Books] with full advisor-list nav + FO + BI. 49F/demo/internal UNCHANGED.
- FE-only. tsc+eslint green. RAVC2 to CTO+COO+CVO.
- **Closure = Andrew dual-login re-smoke** (Peter admin + Joe non-admin both correct). Promote HELD.
- **DATA-SCOPE FLAG (to CVO/AE, not blocking this FE TO):** with Joe on full Distribution, does the per-advisor relationship-drill into OTHER advisors (not joe_brandenburg) edge-403 a non-admin, or render? Andrew wants "same fidelity"; confirm whether non-admin Distribution advisor-drills need self-scope or are firm-aggregate-open. Verify item, not a blocker for the tab fix.
</acceptance>

<notes>
Decomposed by COO from Andrew's verbatim correction 2026-06-02 (after Peter-admin GREEN, Joe-non-admin wrong). W4b's "Profile-only" was a misread of the original ruling; the correct model is admin-tabs-with-Books->Profile (Distribution shared). NOTE the P2-a "hardening" (328a8459, CVO-praised as defense-in-depth) actually reinforced the wrong model for distribution — revert that guard. CC CTO + AE + CVO + RD~B. This supersedes the W4b Profile-only behavior.
</notes>
</task_order>
