# work cycle — 0.4.2_RD_AdvisorIntelligence~C — 2026-06-02 ~2049Z

## ADVI_INFPRM.W4f — CORRECT non-admin model + promote pre-stage re-warm

### Andrew smoke correction (the visual gate working)
Promote was pre-staged + held for GO. Andrew's dual-login smoke: Peter (admin) GREEN; Joe (non-admin) WRONG — W4b's "Profile-ONLY" misread Andrew's model. COO dispatched W4f. The data/logic was "correct" per the W4b TO, but the TO's MODEL was wrong — only the rendered pixel-smoke caught it (exactly the portal-closure visual-gate lesson).

### Correct model (Andrew verbatim)
- Peter (admin): [Distribution, Books] (unchanged — GREEN).
- Joe (non-admin): [Distribution, Profile] — Distribution at SAME full fidelity as admin; Books REPLACED by Profile. Only the 2nd tab differs.

### Fix (portal DEV c009f98c, inflection/index.tsx)
1. nonAdminTabs [advisors(disabled), profile] -> [Distribution, Profile].
2. REVERTED the P2-a isFirmAdmin guard on the distribution branch (328a8459 enforced the wrong Profile-only model) -> distribution renders for non-admins at full fidelity (mirror 49F:263). Reverted the moot advisors-branch guard too. Books branch KEEPS `&& isFirmAdmin` (W4b core — the real BI/Firm-Overview no-leak boundary, CVO-confirmed). Profile branch stays !isFirmAdmin.
3. Profile tab: already renders full self-scoped AdvisorPublicProfile (advisorId=claims.advisorId, defaults Profile view) with Profile|Book toggle gated by canSeeBookToggle(scope)=scope!==1 (ADVI_ROLGAT role model; accessPolicy prop is unused/_accessPolicy). No FE change needed — same component+toggle Peter gets on drill. Joe sees toggle iff Group 2/3.
4. EDGE-FIX: HH->Books deep-link guarded admin-only (onNavigateToBooksClient = isFirmAdmin ? ... : undefined) — non-admins have no Books tab; prevents a blank-Books dead-end. ContinuousChartView disables click-through gracefully on undefined.
5. defaultTab non-admin = Distribution (tabs[0]); "defaults to Profile toggle" is WITHIN the Profile tab.
Regression: Peter [Distribution,Books] unchanged; 49F/demo/internal untouched. tsc+eslint green. ci.yml GREEN (run 26847035947, 2m7s).

### CVO alignment (pre-RAVC2 heads-up)
CVO independently confirmed: FE revert correct (won't flag missing distribution guard as leak); cross-advisor relationship-drill 403 for non-admins = edge .004a advisor_scoping_denied (NOT FE) — routed aggregate-vs-cross-drill architecture to CTO/COO. Matches the DATA-SCOPE flag I raised in my RAVC2. Keep Books guard (done). Profile-toggle = CVO's remaining verify angle.

### Promote pre-stage re-warm
DEV head moved 328a8459 -> c009f98c (W4f). Re-confirmed: clean+pushed, ci.yml GREEN (gh run watch exit 0 + run list success), 14 ahead of PROD, rollback a33c230f. Notified CTO (204948Z) — Andrew re-smokes JOE on c009f98c, then CTO GO -> I fire the 5-phase.

### Flags (to CTO/COO/CVO, not blockers)
- TOGGLE-ROLE: if Joe-smoke shows no Profile|Book toggle, that's Joe=Group1(implementor) by ADVI_ROLGAT (not FE) — Joe's role data, or an Andrew/CTO canSeeBookToggle policy ruling.
- DATA-SCOPE: cross-advisor ADV-drill 403 (edge .004a) — CVO routed to CTO/COO.

### State
W4f IMPL-COMPLETE, ci-GREEN. Promote HELD for Joe re-smoke + CTO GO. RAVC2 COO 204710Z; CTO 204716Z+204948Z; CVO ACK 204830Z. Asked COO to flip W4f TO status (ANY_EXEC owned-paths).
