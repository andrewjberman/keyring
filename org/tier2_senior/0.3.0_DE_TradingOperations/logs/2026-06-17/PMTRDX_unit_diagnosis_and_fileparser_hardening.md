# PMTRDX.001 — weight-unit regression diagnosis + fileParser defensive hardening

**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT, COORDINATE

**Portal DEV commit:** `d725f7f3`
**Workspace CLOUD commits:** `0ccd7f247` -> `49b7969ea` (diagnosis brief)
**Date:** 2026-06-17 | **Session:** Andrew-direct dispatch (PM->TradeSubmission % unit bug)

---

## Launch-protocol RD catch-up (2 uncovered pod commits)

On re-spawn (last log 2026-05-23), two pod RD commits were not covered by my logs (I was killed
2026-05-23 -> re-spawned today). Both are on PROD (v2.1.114), no action needed, recorded here:
- `13618900` (2026-06-03, 0.3.1_RD_PortfolioManagement~B) — comment-only PMTRDX.001 canonical-unit
  contract note on `TradeSecurity` in trade-submission.ts (decimal-fraction contract). No build impact.
- `3e0ce8d0` (2026-06-03, 0.3.2_RD_TradeSubmission) — security: repoint xlsx npm -> SheetJS CDN 0.20.3
  (kills 2 HIGH CVEs on the user-uploaded-xlsx attack surface). Pure dep-source swap, zero source change.
- Also noted: `5ad23559` (0.4.0_DE, cross-pod) removed a 19-file dead PortfolioManagement refactor subtree.

## Current State

Andrew + Yang reported a PFDE trade submission rendering weights x100 too large (AMZN CURRENT 555.00%,
should be 5.55%). Andrew asked: find the prior fix work + determine if it was overwritten / never
deployed, and whether there's a frontend inconsistency. Full diagnosis + turnkey fix spec in
`docs/briefs/pmtrdx-001-weight-unit-regression-diagnosis-20260617.md`.

**Root cause (ground-truthed):** the 2026-06-03 PMTRDX.001 fix (CTO ruling `fa9dc3cb3`, canonical =
DECIMAL FRACTION) shipped only 2 of 3 legs — the doc-note (v2.1.114) + the remediation script — but the
actual **going-forward producer fix** (`÷100` in `portfolio_excel_generator.build_trade_securities` +
`weight_unit='fraction'`) was **never committed** (`git log -S` empty; all 6 file commits Jan–Feb) **and
never deployed** (`opal-portfolio-excel-generator` LastModified was 2026-05-19). Live record
`TRADE-20260617-144856-MKYYDP` = percent-numbers, `weight_unit` absent. Both Andrew hypotheses confirmed.
NOT a bad trade — broker Vident CSV is intentionally percent-numbers; this was display/record-integrity.

**Frontend inconsistency (real):** the portal display (TradeDetailsModal/SecuritiesTable, `×100`) was the
only contract-correct consumer; both Excel generators (`÷100`) assumed percent-numbers — inverted.
Verified the workflow-handler excel_generator output IS the broker execution-email attachment
(`workflow_handler.py:392 -> send_brokerage_email`), so a naive flip would have sent Vident a 100x-wrong
proposed weight. CTO ruled per-output conversion (record/portal = fraction; broker Excel + Vident CSV
byte-identical to today). I supplied the per-column broker-output delta + the provably-byte-identical
`×100`-on-read recipe AE adopted.

**Resolution — core fix (AE lane, LIVE):** routed through COO -> AE 0.7.0 deployed PATCH 1 (producer)
+ PATCH 2 (per-output Excel) + PATCH 3 (remediation). Verified LIVE post-deploy:
`opal-portfolio-excel-generator` LastModified now 2026-06-17T15:55:13Z; records (incl. the original buggy
one) now carry `weight_unit=fraction`. PMTRDX.001 ledger closed `596b4afd4`.

**Resolution — belt-and-suspenders (my lane, DEV):** the manual-upload parser had the same latent class
(`parseWeight` comment claimed a 0–1 range-check that never existed, so a percent-number cell stored
un-normalized). Built `assertFractionBasis()` — throws a loud descriptive Error if any current/proposed
weight > 150% (percent-number form), wired into both parse paths, surfaced via the existing FileUploadZone
red banner. parseWeight no longer silently passes un-normalized percent-numbers. Committed DEV `d725f7f3`;
COO accepted RAVC2; routed 0.4.0_DT for the DEV->PROD promote.

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| portal/src/pages/TradeSubmission/services/fileParser.ts | +assertFractionBasis unit guard (both parse paths) + parseWeight comment/contract fix; export for testability | Yes — DEV `d725f7f3` |
| docs/briefs/pmtrdx-001-weight-unit-regression-diagnosis-20260617.md | New: full diagnosis + turnkey 3-patch fix spec (re-spec'd PATCH 2 to per-output per CTO ruling) | Yes — CLOUD `0ccd7f247`, `49b7969ea` |

## Postmortem: PMTRDX.001 producer fix lost before commit

### Root Cause
The 06-03 going-forward producer fix lived only as an uncommitted working-tree edit and evaporated; the
two artifacts that DID survive (doc-note, remediation script) made the fix look complete. The deployed
Lambda was never updated (LastModified 2026-05-19), so every PM-export submission regressed immediately.

### Mismatches Found
| Field (stored securities[]) | Contract (canonical) | Actual (live record, pre-fix) |
|---|---|---|
| current_weight / proposed_weight / delta | decimal fraction (0.0555) | percent-number (5.55) |
| weight_unit marker | 'fraction' | absent |

### Resolution
- Producer ÷100 + weight_unit stamp — AE deployed, LIVE-verified. DONE.
- Per-output Excel conversion (broker byte-identical) — AE deployed. DONE.
- Existing-record remediation — ran, records re-stamped fraction. DONE.
- fileParser defensive guard (manual-upload path) — DE, DEV `d725f7f3`. PENDING DT PROD promote.

## Compiler Tools

| Tool | Result | Note |
|------|--------|------|
| `comp-blast parseWeight` | "No nodes matching" | portal-internal service helpers aren't in the comp trace graph (graph = 2131 nodes, data-pipeline/component-oriented) — a coverage gap for portal `services/*.ts`; fell back to Grep |
| Grep consumer cross-check | blast radius CONTAINED | parseWeight + assertFractionBasis consumed only within fileParser.ts (the two parse paths); exporting for tests adds no external surface |
| `aws dynamodb get-item/scan` | ground truth | live record = percent-numbers/no weight_unit (pre-fix); post-fix = weight_unit=fraction |
| `aws lambda get-function-configuration` | deploy proof | LastModified 2026-05-19 (pre-fix, deploy never happened) -> 2026-06-17T15:55 (post-fix LIVE) |
| `git log -S / --follow` | archaeology | producer ÷100/weight_unit never in committed history |
| bun `tsc -b --noEmit` + exercise harness | 9/9 PASS, tsc exit 0 | real-parse-path E2E: percent-number CSV rejects loud, fraction/%-string pass |

comp-transform schema-check / comp-routes not run: no portal component prop-shape change, no new
cohort/mode, no 4xx debugging — the change is an additive defensive guard inside one service function.

## Next Steps
- `[0.4.0_DT_TradingOperations / DevOps]` Promote `d725f7f3` DEV->PROD (push DEV first — my commit is
  local; COO routed; I'm on-hand for any parse-logic question).
- `[2.0.0_SA_COO]` Reports DT's verified PROD landing to Andrew -> closes the fileParser-hardening leg.
- `[Dashboard Engineer]` On-hand; threshold (150%) trivially tunable if Andrew wants it tighter/looser.
