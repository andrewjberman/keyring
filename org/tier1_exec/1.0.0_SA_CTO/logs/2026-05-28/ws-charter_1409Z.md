# ws-charter cycle 1409Z — FIX (ADVI demo-prep dispatch-management + FIND_INSURE PRD decision-record)

**Author:** 1.0.0_SA_CTO (ws CTO)
**Class:** FIX (active-project dispatch decisions; no NOVEL PRD authoring) + minor PRD decision-record
**Cron tick:** /ws-charter a22eb079

## Inbox classification

- **DS 0.4.0_DS_ClientPlatform [ARTIFACT-SOURCE CONFIRM + revised Cost Basis scope]** → DRIVE/FIX. INF_B_02 reads silver/transactions ONLY (no holdings input) — my artifact-contamination REORDER concern moot. Root cause: 90% = cash-sweep tickers never disposed by FIFO; 14.8K phantom = uncaptured disposal type_descs. Revised: Fix 1 (cash exclusion) = 90% fix, demo-targetable; Fix 2 (Merge Out/In + disposal descs) = tail.
- **CVO 3.0.0_SA_CVO [VERIFY status F5 PASS + F3 PASS, F4 ready]** → CVO_CC. F3 lookback-AUA PASS @428454ac1 (25 quarters ×3 advisors; Peter latest == canonical $166.1M). F5 Raeleen+headline PASS @722ac687a (canonical-exact; 2 non-blocking flags: shadow household hh511 $0.01 + RD newest-relationship tie). F4 standing for DS rebuild; canonical-vs-stale half already GREEN (reads correct $205.6M not $347.9M).
- **COO 2.0.0_SA_COO [ACK aligned on B]** → DRIVE. Corrected DS~C to (B) + retracted AE 4-Lambda deploy per my updated ruling; asked me to note AC6=productionization/B=v0.1 in PRD this charter.
- DS~C + COO .024-fork messages = re-surfaces of already-ruled fork (B). No new action.

## Actions taken

1. **Cost Basis sequencing call → DS (140547Z):** GO Fix 1 (cash-sweep exclusion) now — draft + dry-run for go/no-go; it's the demo-targetable 90% fix. **Acceptance-bar refinement:** by-year MV reconciles to the NON-CASH book (~$155M Peter, not $166M — cash ~$10.5M correctly excluded from lots); cost_basis just below that MV. Fix 2 = post-demo tail.
2. **F4 acceptance refinement → CVO (140554Z):** same non-cash bar; don't false-flag the ~$10.5M cash gap (correct-by-design). Ack F3/F5 PASS.
3. **FIND_INSURE PRD decision-record:** added Phase 2A execution-model decision to docs/architecture/FIND_INSURE.md §Phase 2 Part A — (B) DS local/SSM driver for v0.1 exploratory; AC6 deployed-Lambda = productionization model; 5 non-negotiable v0.1 conditions. Per COO request + my .024 ruling.

## ADVI_INFDEMO demo-prep state (today's priority)

- F1 (ETF default) + F2 (toggle hidden) + F3 (lookback AUA) = CODE COMPLETE on portal DEV (f61cb40b), F3 CVO-verified PASS (428454ac1). Awaiting Andrew browser visual-confirm.
- F3b (active-since/role chips) = RD graceful-hidden (4bdb844e); Andrew posture-confirm pending.
- F4 (Cost Basis) = DS drafting Fix 1 (cash exclusion); CVO standing to verify on non-cash bar; ship-vs-caveat call as result lands (2-4h runway).
- F5 (data verify) = PASS; Raeleen "newest relationship" answer = shadow-household + tie-break, surfaced to Andrew (fix-on-nod).

## Follow-on / next-cycle expected state

- DS Fix 1 go/no-go read → my ship-vs-caveat call with Andrew.
- Andrew: visual-confirm frontend + F3b posture + Raeleen-fix nod.
- FIND_INSURE Phase 2A (background): DS~E scoring.json + DS~C local-driver under cost-gate; live invoke gated on both.
