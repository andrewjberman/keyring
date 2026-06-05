# 0.6.0_AE_PartnerETL session log — 2026-06-05 work_1514Z (ADHC_GLDINC two-axis addendum)

**archetype:** ANALYZE

## ADHC_GLDINC two-axis addendum (Andrew framework)
Digested Andrew's two-axis optimization framework (docs/briefs/gold-rightsizing-optimization-framework-20260605.md); RAVC2'd a roadmap addendum (appended to the audit, commit c6ac4ec8e). CC COO+CTO+0.4.0.

- AXIS 1 (freeze-baseline): re-examined my 6 FULL-RECOMPUTE-INHERENT scripts → ALL 6 reclassify to IWR. Freeze closed historical periods + incremental open-period + periodic rebaseline. D_00b (firm timeseries, reads all canonical_nna nightly) = the canonical/biggest freeze win. D_00c (freeze per-advisor window stats + cheap re-rank/OLS-refit), D_01 (freeze closed period-ends), D_00 (freeze trailing-NNA), C_05 (snapshot-delta), C_07 (freeze learned table weekly — the one genuinely-global core, but cheap). 0 of 6 remain truly inherent.
- UPGRADED HEADLINE: win is LARGER than original ~50-70% — firm-level all-history readers incrementalize too; irreducible residue shrinks to C_07's cheap core.
- AXIS 2 (cost model): box = OUTPUT of minimize sum(runtime x rate) fit on perf_history (shipped, accruing tonight). R3 r6i.4xlarge = first-order point; tonight's nightly = first r6i data point (+c6i history = 2 pts to seed regression). GLDINC shrinks working set → memory+runtime both drop → re-fit per phase. R3+GLDINC = one joint optimization.
- Restatement-trigger reconcile (re-freeze restated closed periods) = the subtle correctness core, flagged for 0.4.0_DS.
- HOLD build-PRD draft per COO (CTO's lane, await Andrew build-GO); addendum is the analysis feed.

## Threads (holding)
- bd-gold R3: right-size live, validates tonight. demo-reclone3: ~10/min R8-safe, let-it-run. inf-gold: COMPLETED+self-stopped (resolved). ADHC_GLDINC: Phase0+addendum done, await Andrew build-GO.
