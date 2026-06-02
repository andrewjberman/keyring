# work cycle — 0.4.2_RD_AdvisorIntelligence~C — 2026-06-02 ~1934Z

## ADVI_INFPRM.W2-FE — reverted the redundant rewire per COO+CVO ruling; W2-FE final + clean

COO ruled REVERT 3753139e (agreeing with my flag + CVO's split-mode finding). Executed.

### What + why
CVO traced getPlatinumFirmDashboard as a SPLIT-MODE composite (split=true stub -> parallel getClientsTab fetch -> merge into clients_tab at L910, pre-existing). So once 8ff69f18 stopped getClientsTab throwing for external users, dashboardQuery.data.clients_tab is populated (300 clients) -> ClientsTab:307 reads it -> Firm Overview renders. My rewire (3753139e standalone clientsTabQuery) was functionally correct but a redundant 61KB double-fetch. The 308b dashboard.json = the split STUB by design (AE's "no clients_tab -> rewire needed" premise was an incomplete read; CVO's split-trace was the right depth).

### Done (revert 794dc54e)
- Reversed all 4 rewire edits exactly (2+/15-): clientsTabData <- dashboardQuery.data.clients_tab; removed clientsTabQuery + getClientsTab import.
- Kept 8ff69f18 (CVO-certified complete) + e6df1678 (annotation). Verified 8ff69f18's getPlatinumAdvisorSummary(...,firmId) caller (ClientsTab:399) intact; zero getClientsTab refs remain.
- tsc -b + eslint green. Surface returned to the exact CVO-certified 8ff69f18 path -> CVO PASS stands, no new verify needed.

### FINAL W2-FE surface (portal DEV head 794dc54e)
- 8ff69f18 — 9 firmOverride-required throw-fixes (Symptom 2 Firm Overview via split-merge [CVO-PASS verify_channel_ADVI_INFPRM_W2FE_1926Z.md] + Symptom 3 book static-adapter routing).
- e6df1678 — DistributionTab pseudonymize INTENTIONAL annotation (finding CLOSED-INTENTIONAL).
- 794dc54e — revert the redundant rewire.
Net: minimal, CVO-certified, no double-fetch, established split-merge pattern preserved.

### Open (others' gates; coherent Andrew re-smoke, COO-sequenced)
- AE book-data verify (Peter's advisorId claim + book.json artifact) — COO dispatching.
- RD~B DistributionTab:1951 Segment firmId one-liner — RD~B's lane, COO relaying.
- Andrew/CTO pixel-smoke = closure gate (held for coherent surface).
Nothing blocked on me. RAVC2 COO 193432Z (CC CVO+AE+CTO).

### Self-note (carry-forward)
Correct-but-unneeded work: I built the rewire off AE's incomplete-read premise without first tracing the split-mode composite myself. CVO's depth caught it; I flagged honestly + COO ruled revert. Lesson reinforced: before ADDING a data path, trace the EXISTING one to its source (incl. composite/split-mode behavior), not just the surface symptom. Net still positive (throw-fix is the certified fix) but the rewire was avoidable churn.
