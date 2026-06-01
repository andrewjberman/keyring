# /work — 0.4.0_DE_ClientPlatform — 2026-06-01 1824Z (TO-1a Schwab re-derive serving-verify — RUN-AND-RETURN)

**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE

## Dispatch
DS~B [TO-1a LANDED]: 49F Schwab re-derive (82 partitions 1/16-5/17 + rollup) live on served feed; run pre-staged harness on json/mdpf/{49financial,global}/aggregate-aua-timeseries.json + RAVC2 COO+CTO. (gen 18:21:19Z, commit 120652cb6 rollup-provenance.)

## VERDICT: TO-1a 49F CORE SEAM-CLOSURE = PASS
Ran verify_schwab_rederive.py (AC2/AC3/AC4/AC6) on the served feed (consumer-resolved path):

**49financial (re-derive target) — PASS:**
- AC4 continuity: custody step@5/18 = $0 (was -$156M); non_model +$8.7M (was -$172M); rank 0.050/0.725 = within-normal. The BD->Schwab seam is CLOSED. 1/16 boundary SMOOTH (custody +$3.6M, non_model +$1.3M — no new seam from legacy<->Schwab transition).
- AC2 identity: total = 1a+1b+1c to the dollar, 1/16-fwd (92 dates, worst diff $0.00).
- AC3 estimate-flags: PRESENT + fully populated. meta.basis_provenance {schwab_exact_range 1/16-5/17, interpolated_1c, pre_1_16:pending_andrew_disposition} + per-date cohort_provenance (82 dates 1/16-5/15) all flagging sma_1c:interpolated_estimate (gap_linear_interp) + custody roll-forward (2/16->2/13, 4/3->4/2 holidays). Estimated regions FLAGGED, not silent.

**Two harness FAILs — BOTH out-of-TO-1a-scope (not regressions):**
- AC6: 12/27 gone (prior fix); ADD-DAYS (12/30,12/31,1/2,2/2,3/2,4/1,5/1) = DS~B-declared FOLLOW-ON, explicitly NOT in this core landing. Expected.
- GLOBAL: still shows the 5/18 seam (non_model -$269M, opal_aggregate -$62M rank 0.993). Consistent with PRD §2 "Global needs no work; Inflection separate" — re-derive was 49F-only; global aggregates the not-yet-re-derived Inflection/other firms. FLAG-for-confirm: global is a consumed view too; confirm its residual seam is intentionally deferred (Inflection-gated).

## Commits
- CLOUD `<pending>` — this log (harness ephemeral .runtmp)

## Comms
- RAVC2 (TO-1a 49F core = PASS; AC6 follow-on + global flag) -> COO + CTO; CC DS~B. CVO independent-verify in parallel.

## Next
- [COO/CTO] confirm global residual-seam disposition (Inflection-gated?) + Andrew §4 pre-1/16 disposition (still pending_andrew_disposition).
- [DS~B] AC6 ADD-DAYS follow-on; Inflection re-derive (separate).
- [Andrew] rendered-visual on 49F Model Portfolios trend (seam-gone). Held: FE-slim (WIP-owner trace); RD~B fold verify. /work cron live.
