{
  "project_code": "TRSB_PATHFIX",
  "macro_code": "TRSB",
  "name": "Trade Submission Path Mismatch + SES Group Reconciliation",
  "description": "Hot-fix on top of TRSB_TFIMPT (2026-04-21) to resolve Andrew's `Unexpected token '<'` error on trade submission. Two backend gaps: (1) portal/src/pages/TradeSubmission/ POSTs to /api/general/trades/* but no API GW route exists at that path — CF returns custom_error_response 403/404→/index.html which the browser tries to JSON.parse as HTML; (2) trade-users DDB schema drift — current authorizers field should be approvers per spec, AJ in authorizers but spec says executor only. PRD scope: 3 TOs — W1 AE adds 12 API GW routes (CUSTOM+naqxlm auth), W2 DT renames DDB authorizers→approvers + adds 2 missing rows (7→9) with 1-week dual-write window, W3 AE+Andrew SES alyssa@opalinvest.com verify + prod-access submission.",
  "prds": [
    {"path": "docs/architecture/TRSB_PATHFIX_PRD.md", "label": "TRSB Path Mismatch + SES Reconciliation PRD v1", "date": "2026-04-27"}
  ],
  "status": "active",
  "phase": "Phase 1 — **TO-1 COMPLETE 2026-04-27** (AE 0.7.0: 12 routes live with CUSTOM+naqxlm auth, Lambda perms on 4 Lambdas, comp-routes 23 behaviors stable, tag `trade-pipeline-v1.6.0`; status flip 2026-04-29 during AE TO sweep). **TO-3 COMPLETE-AS-SANDBOX-FINAL 2026-04-30** (Andrew ruling: 'sandbox mode is fine, we don't really need to involve external parties at this stage') — all 9 spec emails verified in SES, BROKERAGE_EMAILS override routes externals to andrew@; W3 closed without prod-access submission. **TO-2 AMENDED + GO 2026-04-30** (CTO per Andrew directive 'full send, no disruption since trade ops not started'): dual-write window dropped, categorical clean cutover — single commit removes 'authorizers' from DDB + Lambda code, ships at `trade-pipeline-v1.8.0` (v1.7.0 consumed by TFIMPT.W3 on 2026-04-29). 2 COMPLETE / 1 PENDING (DT 0.3 dispatch in flight). TO-4 firm-scoping-backend remains DRAFT (separate scope, not in current sweep).",
  "blocking": "TO-2 DT 0.3.0 ship + RAVC4 — last open AC for project closure. On RAVC4: project closeable via 3-step atomic close (JSON status → complete + REGISTRY row move + PRD note). TO-4 carries forward as separate Phase 2 (firm-scoping) if/when Andrew prioritizes.",
  "created": "2026-04-27",
  "pods": ["0.3", "0.7"],
  "pipeline": "trade-pipeline",
  "lanes": ["0.7.0_AE_CloudOps", "0.3.0_DT_Trading"],
  "lane_note": "AE 0.7 owns API GW routes (W1) + SES verify (W3). DT 0.3 owns DDB rename + row additions (W2). Andrew owns SES prod-access submission (W3 outbound).",
  "waves": [
    {"id": "W1", "label": "API GW routes /api/general/trades/* (CUSTOM+naqxlm auth)", "owners": ["0.7.0_AE_CloudOps"], "target_tag": "trade-pipeline-v1.6.0"},
    {"id": "W2", "label": "trade-users DDB schema reconciliation (authorizers REMOVED + 7→9 rows; categorical clean cutover per Andrew 2026-04-30)", "owners": ["0.3.0_DT_TradingOperations"], "target_tag": "trade-pipeline-v1.8.0"},
    {"id": "W3", "label": "SES verify alyssa@opalinvest.com + sandbox-final ruling (Andrew 2026-04-30: no external party / prod-access submission)", "owners": ["0.7.0_AE_CloudOps"], "target_tag": "—"}
  ],
  "follow_up_backlog": [
    "TRSB_CLEANUP — orphan API w8jnzvs21g: 30-day CW zero-traffic gate then delete TO",
    "TRSB_CLEANUP — /api/public/trades/* NONE auth: upgrade to CUSTOM or delete after W1 parallel set proven"
  ],
  "depends_on": ["TRSB_TFIMPT"],
  "depends_on_note": "Built on top of TRSB_TFIMPT W1+W2 (Terraform import + reclamation). Same trade-pipeline Terraform module, same DDB. Hot-fix scope only — TRSB_TFIMPT remains the canonical baseline.",
  "thread_counter": 0,
  "threads": []
}
