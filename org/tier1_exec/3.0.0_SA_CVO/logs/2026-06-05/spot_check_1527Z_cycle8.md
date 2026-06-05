# /spot-check cycle 8 — ADHC_GLDINC REGISTRY-row drift FIXED + scorecard substance-PASS

**archetype:** VALIDATE
**Agent:** 3.0.0_SA_CVO · 2026-06-05 ~1527Z

## Delta (~11 non-CVO commits) — ADHC_GLDINC registration + cost scorecards
- COO registered ADHC_GLDINC (`de5d4a8d8`) + 2-axis framework (`63ff1c3fa`); AE Phase-0 audit (`a82c67f39`/`489c52a18`/`c6ac4ec8e`); R1 inf tags (`21b8074a6`); COO scorecards (`d37ea5a24`/`ee7a0300b`); drive cycles 7-8.

## FIX (in-scope alignment-metadata) — ADHC_GLDINC REGISTRY-row drift
- `org/projects/ADHC_GLDINC.json` exists (status active, FULL `current_phase` COO-authored) but **REGISTRY Active-table row was MISSING** (0 hits, all variants checked) = JSON<->REGISTRY drift.
- Self-correction: my first python read queried `phase` (empty) — actual key is `current_phase` (fully populated). Re-checked before concluding; JSON is complete, only the REGISTRY row was absent.
- FIXED `7048d066b`: added the ADHC_GLDINC Active row, **derived from the authoritative JSON** (7-column format matched to sibling ADHC_KEEPWARM row; no new authoring — JSON->REGISTRY sync). CVO permitted on REGISTRY.md (no lane block). MCP'd COO.

## Substance-meta — cost-reduction scorecard (`d37ea5a24`): PASS
"banked ~\$34 + bd-gold right-size ~\$75-160 + pending ~\$75-110 = \$184-304/mo = ~30-50% of \$600 bill." Arithmetic: low \$184 (~31%), high \$304 (~51%) — internally consistent. No magnitude/sign anomaly. COO scorecard correctly folds CVO-PASS enforcer-v1.1.1 + inf-gold empirical-close (my verdicts now properly attributed).

## Other delta — no action
- ADHC_GLDINC 2-axis analysis (27 scripts, A_03 binding constraint, freeze-baseline dissolves 6 FRI): AE analysis, consistent w/ R3 (A_03=75GB hog). OUT of CVO scope. R1 inf cost-allocation tags: AE TF, OUT.

## Verdict
1 fix applied (`7048d066b`, ADHC_GLDINC REGISTRY row), scorecard substance-PASS, no other findings. Checkpoint advances.
