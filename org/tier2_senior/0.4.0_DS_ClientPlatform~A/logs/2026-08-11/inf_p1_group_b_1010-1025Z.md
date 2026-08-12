# INF_RUNNER_REFACTOR.P1 — Group B built, QA-run, proof-instanced (1010–1025Z)

**archetype:** IMPLEMENT
**Serial:** 0.4.0_DS_ClientPlatform~A · **TO:** INF_RUNNER_REFACTOR.P1
**Commits:** B mint @eae331b019 (pre-registered) · B build @9e6c1f62bf

## What was built

b00 canonical_valuation — V(t) = activity.ending_mv AUTHORITATIVE (never reconstructed), with
the measured 3y-window artifact class DISCRIMINATED per account (value_status: OK 485 /
ZERO-CONTRADICTED-BY-POSITIONS 312, $68.39M of live positions behind coerced zeros /
ZERO-CORROBORATED 37 / SOURCE-ABSENT 35 — fix choice stays at CTO+COO, banked). Spot-tie
positive control TIE; FV identity 869/869. b01 canonical_positions — 35,262 rows in==out,
vendor-field-only flags (zero_price 7, zero_qty_nonzero_mv 0, recon_age_days from the vendor's
own stamp); the legacy interpolated price tier is DISCARD-class and structurally absent.
b02 accrual_decision — the honest N/A-BY-CONSTRUCTION cell, uniform shape. b03
valuation_integrity — flag plane at 1bp ex-ante PROVISIONAL (ruled-recalibration clause
verbatim): same-vintage census TIE 520 / VARIANCE-EXPLAINED 347 / VARIANCE-UNEXPLAINED 2
($389.78 total) / VINTAGE-SKEW-DECLARED 0. Determinism census identical across two runs;
mutant (poison ×1.5 on account 488) landed VARIANCE-UNEXPLAINED, never TIE.

Key measured insight: the same tie read cross-vintage gives 39/485 — vintage skew manufactures
false variance, which is why the enum carries VINTAGE-SKEW-DECLARED.

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| comp-to | (standing from session start) | TO context INF_RUNNER_REFACTOR.P1 |
| comp-validate / comp-pipescript | probes recorded in the Group A window | family unregistered — declared exclusion carried forward (P2/P3 registration) |

py_compile + ruff stage-by-stage (b03's unused import caught at stage, fixed before commit;
b01 tz-aware/naive subtraction caught by the QA run, fixed + restaged).

## Next

Group C id mint + build (c00–c05), incl. the COO-folded Remark/Reversal specimen
characterization (CHARACTERIZE only — classification ruling is CTO's on my specimens).
