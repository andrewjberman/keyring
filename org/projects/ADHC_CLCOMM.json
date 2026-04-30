{
  "project_code": "ADHC_CLCOMM",
  "macro_code": "ADHC",
  "name": "COMP_LEARNS Agent Comms Channel Isolation",
  "description": "Stand up a dedicated `complearns-agent-comms` MCP channel for the `feature_clb` worktree, physically separate from `opal-agent-comms`, to eliminate cross-project inbox pollution. Origin: 2.1.0_SA_COO setup brief at `feature_clb/org/ref/COMPLEARNS_AGENT_COMMS_SETUP.md` (`5eac1f09f` on COMP branch). Andrew directive 2026-04-30: delegate ADHC TOs to AE 0.5.0 to resolve the MCP issue.",
  "prds": [
    {"path": "docs/architecture/ADHC_CLCOMM.md", "label": "CL Comms Channel Isolation Setup Brief (canonicalized 2026-04-30)", "date": "2026-04-30"}
  ],
  "status": "active",
  "phase": "Phase 1 (CL channel build + verify) + Phase 2 (cross-channel architecture codification) — TO-1+TO-2 COMPLETE / 2 STAGED 2026-04-30 PM. Phase 1: TO-1 ae-build-cl-mcp-scripts COMPLETE (AE 0.5 commit `abd95426e` — pragmatic prefix-routing-in-poller approach with documented env-var-threading-on-Claude-Code-hooks concern); TO-2 ae-feature-clb-integration COMPLETE 2026-04-30 PM via joint cross-CTO routing (Option 1): COMP-branch commits `6f2eb07e1` (1.1.0_SA_CTO — feature_clb config wire-up) + `be8713015` (1.1.0_SA_CTO — TO-1 deliverables landed on COMP); CLOUD-side commits `baf84d70c` (AE 0.5 — prep log + 4 cross-channel observations) + `6fce67ea6` (AE 0.5 — TO status flip). 12 cross-channel observations (7 from TO-1 + 5 from TO-2) seeded into TO-4 corpus. **Empirical finding flagged:** org/mcp/inbox-watch.sh divergence between COMP (has eval-exclusion + PPID-filter hardening per `c471b2fd9` + `d26a36492` from 2.1.0_SC_CompLearns) and CLOUD (doesn't); cherry-pick-back opportunity benefits opal-agent-comms watcher (Andrew directive: 'lessons learned should benefit opal-agent-comms'). TO-3 ae-verification-and-close STAGED (AE 0.5; gates on Andrew smoke-test coordination — fresh feature_clb session needed since MCP config loads at session-start). Phase 2: TO-4 cto-coo-cross-channel-architecture-doc STAGED (gates on TO-3 PASS).",
  "blocking": "TO-3 smoke-test coordination — Andrew picks: (a) spin up fresh feature_clb session for AE 0.5 to drive 9-test verification, OR (b) hand off verification protocol to whoever opens next feature_clb session. PRD §7 9-test list authoritative. **Side action surfaced 2026-04-30 PM:** inbox-watch.sh COMP→CLOUD cherry-pick (org/mcp/** is BASE_EXEC lane → CTO direct ship OR small follow-on TO; Andrew direction welcomed). TO-4 gates on TO-3 PASS.",
  "created": "2026-04-30",
  "pods": ["0.5"],
  "pipeline": "agent-infrastructure",
  "lanes": ["0.5.0_AE_OpalETL"],
  "lane_note": "AE 0.5.0 primary on TO-1/TO-2/TO-3 (CL channel build + verify). CTO+COO joint on TO-4 (cross-channel architecture doc). CTO architectural sponsor throughout; COO-CompLearns originator (2.1.0_SA_COO authored brief). XXX.md update post-TO-3 closure is CTO scope (folded into TO-4 deliverable since the cl-* command references are part of the cross-channel architecture documentation).",
  "depends_on": [],
  "depends_on_note": "No upstream dependencies. Independent of all live INFLEC/ORIAPI/DIAGFIX work.",
  "thread_counter": 0,
  "threads": []
}
