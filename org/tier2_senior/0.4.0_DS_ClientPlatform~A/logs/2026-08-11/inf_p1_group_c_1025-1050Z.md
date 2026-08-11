# INF_RUNNER_REFACTOR.P1 — Group C built, QA-run, proof-instanced (1025–1050Z)

**archetype:** IMPLEMENT
**Serial:** 0.4.0_DS_ClientPlatform~A · **TO:** INF_RUNNER_REFACTOR.P1
**Commits:** C mint @2a785d9289 (pre-registered) · C build (c00–c05, this window)
**Critical-path note:** this group's completion report FIRES the pre-staged Group D ruling
(CTO 103254Z); Andrew's kill condition chains through it (COO 103033Z).

## What was built (six scripts, seven tables)

c00 flow_ledger — 1,407,740 rows, each in exactly ONE final class (in==out); sign-semantic
census 100% clean in every class (the debit_credit amendment transposed as sign-vs-class
verification); exchanges 99.90% pair-VERIFIED (852 unpaired flagged, stay INTERNAL per the
ratified bucket); journals 1,978 pair-matched INTERNAL (the ratified claim VERIFIED) / 738
unmatched → EXTERNAL-BY-DEFAULT (F-4's input); UNRESOLVED 732 rows (0.052% / 0.050% dual
frame); Remark + Reversal SPECIMEN-CHARACTERIZED ONLY (COO fold — reads show Remark as
all-nonnegative ticker'd position-shaped entries, 75/174 with units, $1M FID:CASH top
specimen; Reversal all FID:CASH unit-matched positives; ruling = CTO's on these reads).
Controls: determinism census identical; dropped-pair-leg mutant fired at the exact
counterpart (matched 1978→1976, unmatched 738→739).

c01 nna_canonical — re-based ON the ledger; headline = code-rule EXTERNAL only (15,472 rows,
$136,711,346.75), segregated nna_unresolved_direction 738 rows $2,837,172.35 carried never
folded; no-residual identity to the penny; MIGRATION DIFF vs legacy canonical_nna_2026-08-07:
ZERO accounts differ >$0.01, day-net EXACT tie ($-47,234.61 both) — the re-base reproduces
the ratified NNA while adding the F-4 discrimination.

c02 twr_engine — 5/5 synthetic GIPS fixtures (EOD identity, geometric-vs-summed divergence,
zero-BMV UNCOMPUTABLE, gross/net add-back identity); live window 08-07..08-10: 970 computed /
768 REFUSED (the 312-class propagating loudly — a plausible return off a coerced-zero base is
strictly worse than a refusal); |r|>5% census 4 (0.41%); periods geometric-linked only;
MTD/QTD/YTD declared UNCOMPUTABLE-AT-P1-QA-WINDOW (P2 backfill computes them).

c03 twr_lineage — sec10 fields all non-null or declared; acceptance status pure function:
TRUE_TWR 483 / UNSUPPORTED 384 / INDICATIVE_ONLY 2; inject-unresolved mutant derived
UNSUPPORTED at the exact bar ($1,000,000.00 > $316.24).

c04 validation_battery — 9/9 GRADED (SKIPPED absent by construction): position-tie
PASS-WITH-CENSUS; cash-balance-roll UNCOMPUTABLE-BY-SOURCE-SHAPE (named); classified
PASS-WITH-CENSUS; BMV-rolls verified; price-flags census; matched journals net $-0.00;
anomaly census; vendor-tie UNCOMPUTABLE-WINDOW-MISMATCH (vendor Rolling-3-Year starts
2023-08-11 vs our V(t) floor 2026-04-28 — MEASURED, with the named P2 computation);
P&L identity UNCOMPUTABLE-AT-BUILD (tax_unrealized carries ending_mv + lt_cost_basis, no
direct unrealized column — schema fact recorded; P2 month-grain computes it).

c05 verification_twr — vendor TWR RAW, method disclosure in-band (907/907 CalcMethod=TWR),
Rolling-3-Year window measured, 554/907 twr_value populated (the same window class), 0
outliers >100pct on this partition; provenance separation stated in-artifact: NEVER served
as OUR return. boundary_version deliberately NOT stamped (vendor-raw, boundary-independent
by design — declared).

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| comp-to | (standing) | TO context INF_RUNNER_REFACTOR.P1 |
| comp-validate / comp-pipescript | family probes (Group A window) | unregistered — declared exclusion carried (P2/P3) |

Stage-by-stage py_compile + ruff per script (3 stage catches fixed pre-commit).

## Next

C-completion report to COO (fires the D ruling). Wave-close: 06_current_state recompile at
COO exec lane; session logs committed per group.
