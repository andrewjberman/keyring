# Deploy: cot-pair-tolerance-recal

**Opened:** 2026-07-28T22:52Z by 0.7.0_AE_CloudOps · **Ruling:** CTO 224741Z option (a), conditions 1–4.
Identity-(i) gate on the S3-staged `build_cottonwood_mdpf_pair.py`: tolerance 0.01 → 0.02 with
per-run delta logging. S3-staged copy ONLY; repo copy untouched (held G7 swap). Full record:
`org/tier2_senior/0.7.0_AE_CloudOps/deliverables/COT_PAIR_TOLERANCE_20260728/NOTE.md`.

Legs: L1 S3 upload+verify → L2 divergence-record commit → L3 Stage-6 re-run under tonight's
carve-out (pair passes with delta logged → slice → cottonwood advances → cycle-complete.json
first emit). If the pair fails AGAIN with tolerance in place: STOP, report delta, never widen.

## Completion

(open)
