# TO-1a Schwab re-derive — APPLIED + serving-verified (DS~B, 2026-06-01 ~1821Z)
COO GO (164549Z) + CTO PRD. CVO sole verify-writer; this is the emit record + my self-verify, pending DE serving-verify + CVO independent-verify.

## What landed
Re-derived 49F 1/16-5/17 onto the Schwab canonical basis (Andrew Mandate Change 3): 1b = Schwab_custody(exact) - 1a(measured) - 1c(interpolated estimate). 82 existing partitions rewritten (custody/1b/total + provenance), then rollup -> served timeseries.

- MECHANISM: WS-E PRODUCTION compute_partner_custody_total (handles BD-silver schema quirks) + cached crosswalk (10,526 accts). Holiday/raw-schema dates roll-forward to the nearest computable business day (2/16->2/13, 4/3->4/2, etc.). DRY-validated 82/82, 0 errors before --apply.
- 1c: bandaid daily (1/16-3/10) + LINEAR-INTERP across the 3/11-5/15 null-gap (3/10 anchor $22.07M -> 5/18 anchor $24.9M), per Andrew's "calculated daily 1c" ruling. Labeled interpolated_estimate.
- PROVENANCE (CTO hard-honesty gate / DE AC3): every re-derived date carries cohort_provenance {basis:schwab_canonical_rederived, custody:measured|rollforward:{d}, model_1a:measured, sma_1c:interpolated_estimate, sma_1c_method:bandaid_interp|gap_linear_interp}; served slices carry meta.basis_provenance (schwab_exact_range 2026-01-16..2026-05-17, interpolated_1c, pre_1_16=pending_andrew_disposition). Rollup enhanced to propagate both (commit 120652cb6).

## Self-verify (served timeseries — consumer-resolved, not just partitions)
- SEAM CLOSED: 49F 5/15->5/18 custody step = $0 (was -$156M); non_model step +$8.7M (normal market range, was -$172M). 1/16-5/17 consistently Schwab-basis.
- Correction concentrated Apr->5/15 (~$150M BD-full-book inflation removed); Jan-Mar ~unchanged (old bandaid already ~Schwab).
- Estimate-flags present in served feed (meta.basis_provenance + per-date cohort_provenance) — verified on json/mdpf/49financial/aggregate-aua-timeseries.json.

## Commits
- Apply: 82 partitions rewritten (S3 emit, no code commit — data emit via .runtmp/bmkaud/to1a_emit_v2.py).
- Rollup provenance propagation: 120652cb6 (deployed to runner code bucket).

## Gates remaining (before fully closed)
- DE serving-continuity-verify (harness 94fed039c): AC4 seam closed, AC2 total=1a+1b+1c, AC3 estimate-flags present, AC6 (12/27 gone; add-days = follow-on).
- CVO independent-verify on the SERVED timeseries.
- AC6 add-days FOLLOW-ON: 2/2,3/2,4/1,5/1 (need 1a-scoping) in-scope; 12/30,12/31,1/2 pre-1/16-gated (TO-1b).
- TO-1b pre-1/16 disposition artifact -> Andrew #3 ruling.
