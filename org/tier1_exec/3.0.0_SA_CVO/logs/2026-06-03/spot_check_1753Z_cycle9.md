# /spot-check cycle 9 — 2026-06-03T~1753Z

**Delta:** d47702c72..b9d04e3fa — 11 commits (1 own dropped).

## WATCH — HIGH substance item in-flight (NOT my fix; already TO'd+dispatched)
**PMTRDX.001 "export-weight-x100-bps-as-percent"** (CTO bde576a22 / ws-charter_1729Z) — portfolio weight exported 100x off (bps-vs-percent unit mismatch): ExportModal.tsx finalWeight -> trade-submission.ts proposed_weight -> TradeDetailsModal renders 20%. HIGH trade-integrity. CTO's critical Q (correct): SUBMITTED order wrong (real bad-trade exposure) vs display-only — must trace end-to-end + verify the ACTUAL submitted record before patching. Owner RD~B (0.3.1_RD_PortfolioManagement) via MSTR spawn -> COO dispatch. CVO disposition: WATCH for the fix RAVC2 -> closeout-class verify when it lands (verify-channel discipline: read the submitted-record artifact, not the rendered %). Ready to verify on land. No action now (RD mid-trace).

## OBSERVATION — untracked-TO governance blind-spot (2nd instance today)
PMTRDX.001 TO is UNCOMMITTED (CTO->MSTR note 173329Z), same as the 0.7.0 BDTSCLB.001 draft (cycle 8). Two untracked TOs in one day = git-based TO-status governance scans can't see them. Pattern surfaced to Andrew (session summary) + MSTR aware (holds the CTO uncommitted-note). Holding MCP (avoid noise; both governance owners aware). Flag if a 3rd instance.

## Other — no drift
- comp-validate NO_CONFIG fail-closed FLIP LANDED (316e97967 step-c + bde576a22 scribe LIVE) — the fabric-wide default-flip I flagged to watch; DS shipped 26-test regression suite (8a9677306) locking the hardening = reassuring. DS tool code, OUT-scope.
- ADHC_CMPAWS S3+IAM per-bucket fixture (c8531c23c) built FOR CVO hand-audit — queued future CVO work on the CMPAWS project (separate active, not current closeout queue). Noted/available.
- 0.7.0 CMPAWS compute/IAM census + Track-1 inf-otp-relay cleanup = AE active-lane, OUT-scope.
- COO tick13: my 2 bd-backlog P3s (orphan-served + windowing) dispatched to 0.6.0. Good.
No numeric META trigger requiring a NEW finding (PMTRDX already caught+TO'd). Checkpoint -> b9d04e3fa.
