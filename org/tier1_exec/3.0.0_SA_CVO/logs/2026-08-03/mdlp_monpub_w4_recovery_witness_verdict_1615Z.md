# MDLP_MONPUB W4 recovery publish -- independent post-publish witness: PASS

**archetype:** VERIFY

**Serial:** `3.0.0_SA_CVO`. Window: 2026-08-03T1610-1615Z.
**Scope (per CTO 155100Z ruling + MSTR relay):** the W4 recovery publish AND W2's
exercised-PASSING leg. W2's failing-direction battery remains PENDING (separate witness).

## Verdict: PASS on every check, values read

1. **Vintage coherence:** all THREE benchmark keys (`model_portfolio_benchmarks.json`,
   `benchmark_returns.json`, `model_portfolio_timeseries.json`) read `data_as_of=2026-07-31`
   with IDENTICAL `generated_at=2026-08-03T16:10:23Z`. No mixed-vintage serve.
2. **Estate probe:** `json/macro/macro_data.json` also `data_as_of=2026-07-31` (16:10:25Z) --
   the rebuild healed the wider estate, not just the named surface.
3. **ETag flip:** served comprehensive key `0a122e2c95...` -> `ada142139b024788914eaf2638b0b7c8`
   (16:10:24Z). Detected by my own pre-armed watch, not a report.
4. **CONTENT -- the check skipped this morning, now run:** served ST MODEL row vs sitez's
   AUTHORITATIVE pinned table (relayed verbatim by MSTR 161055Z; control-validated replica,
   staged pkl md5 2a4703465c00f76ce71094db5ae522c0): **ALL 10 PERIODS MATCH TO 2dp, model
   ret/vol AND index-benchmark column** (1D..SinceInception; tolerance 0.005; script inline,
   denominator 10/10 printed). No deviation to investigate.
5. **Execution:** `20260803_v2-c2ea0112` SUCCEEDED (16:08:20->16:12:22Z) -- the first successful
   T-1-correct run since the incident opened; the four 07-31 duplicate-labels failures are
   superseded by the corrected pkl.
6. **Edge cache:** post-publish CloudFront invalidations on EVTSA9VEHNZVH: 16:11:44 + 16:11:51
   Completed, 16:12:19 InProgress -- pipeline-side invalidators fired; edge will serve 07-31.
   (Client-side RQ caches: open sessions still hold old data until W6 lands -- known, ordered.)
7. **Interval integrity (no serve mutation in the blocked window):** version walk shows NO write
   on the served key between 13:29:12Z (Andrew's rollback state) and 16:10:24Z (recovery). The
   15:05Z `20260803_w1republish-150535` attempt (original corrupt 07-30 manifest, pre-block)
   FAILED in 2.3s BEFORE any publish step -- zero serve impact, confirmed by the version walk.
   Its failure cause is surface-level only ("one or more steps failed", fast-fail); root cause
   belongs to the W1 postmortem, not this witness.

**W2 status per this witness:** exercised-PASSING leg CLOSED (a newer-date publish succeeded
through the deployed guard, yang-v2.4.17 live 15:46:38Z). Failing-direction legs (older-date
mutant / mid-build-crash mutant / force_publish bypass) still PENDING my separate witness -- W2
is NOT complete until then; a guard never exercised in the failing direction is not a control.
