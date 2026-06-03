# ws-charter — 2026-06-03 1729Z — PM→TradeSubmission ×100 bug routed + comp-validate flip scribed-live + ZERO_CHECKS ruling

**CLASS:** FIX (Andrew-direct bug routing) + doctrine scribe (comp-validate flip (d) + §10.1b ruling).

## (1) Andrew-direct bug — PM export ×100 (Yang-reported)

Portfolio Management portal "export to Trade Submission" scales weights ×100 — 20bps buy renders/submits as "20% buy". Andrew: "new RD~B to explore + fix."
- Authored **TO PMTRDX.001** (FIX-class, explore-then-fix): `org/tier3_rd/0.3.1_RD_PortfolioManagement/task_orders/PMTRDX.001.export-weight-x100-bps-as-percent.md`. Pre-traced: `ExportModal.tsx` (finalWeight payload) → `trade-submission.ts` (proposed_weight) → `TradeDetailsModal.tsx` (renders 20%). Hypothesis: fraction/bps-vs-percent unit mismatch; fix at the boundary. CRITICAL: determine if SUBMITTED order is wrong (real bad-trade exposure) vs display-only — trace end-to-end + verify the actual submitted record before patching.
- Spawn routed to MSTR (HARD-BLOCK #8 — can't spawn): recommended 0.3.1_RD~B (PM-export origin). CC COO (dispatch + drive-track). Rides v2.1.114+ promote.

## (2) comp-validate flip — scribed LIVE (d) + ZERO_CHECKS ruling (§10.1b)

DS flipped NO_CONFIG → exit-2 LIVE (`316e97967`); waivers E_02/E_04/E_22 blessed; gate-path inventory was EMPTY (zero automated-breakage); --strict → no-op alias.
- Scribed (d): COMP_VALIDATE_PROTOCOL §10 table (NO_CONFIG row marked LIVE; added ZERO_CHECKS row) + §10.1 (rollout marked EXECUTED/flipped-live) + CLAUDE.md line (LIVE + ZERO_CHECKS). LD-0148 ratified.
- **RULED §10.1b (DS sibling finding):** `PASS: all 0 checks passed` exit-0 (all-SKIP configs, e.g. C_01/B_01) is the SAME absence!=PASS false-green — MORE reachable than NO_CONFIG (recognized ids). Fix: `pass_count==0` → `ZERO_CHECKS: UNVALIDATED` exit-2, message names the deferred validator (comp-pipescript); --lenient/waiver escape. Distinct from NO_CONFIG (config exists, validation deferred-not-absent). PHASED (mirror §10.1): inventory all-SKIP count (uncounted in §10.1 inventory) → classify (legit-deferred vs needs-real-checks) → flip the guard. Did NOT bundle unilaterally (DS correct) — scope decision I own; GO with phasing.

## Follow-on

- RD~B (PMTRDX.001): MSTR spawn → COO dispatch → end-to-end trace → boundary fix → RAVC2.
- DS: comp-validate ZERO_CHECKS — inventory all-SKIP count → classify → flip guard (phased, my GO after count).
- comp-validate NO_CONFIG flip = DONE-live; COO broadcasts announce line on confirm.
