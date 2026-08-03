# MDLP_MONPUB spec validation (RAVC) -- CONDITIONAL GO with one required amendment

**archetype:** VERIFY

**Serial:** `3.0.0_SA_CVO`. Window: 2026-08-03T1436-1515Z.
**Tasking:** MSTR-TO 20260803T143438Z (Andrew-direct relay) + CTO RAVC-REQUEST 20260803T144551Z.
**Target:** `docs/architecture/MDLP_MONPUB_MANIFEST_REGRESSION_FIX.md` @d59fc15920 (CTO ordering spec
for ~F's finding @99c3e50a36).

---

## Verdict

**CONDITIONAL GO.** ~F's mechanism is CONFIRMED end-to-end by independent live grounding -- every
load-bearing claim re-derived, none refuted. The CTO spec's W1/W3/W4, the W2 guard semantics
(older=reject / equal=allow / missing-served=allow-loud / force_publish bypass), the W1-before-W2
ordering, and the moratorium reading are all VALIDATED. **One required amendment to W2 (Finding 1:
publish-after-build reorder -- the failure mode has a second half the spec does not close), plus two
residuals to record (Findings 2, 3) and two cheap acceptance additions (Findings 4, 5).** None of
this re-opens the design; the amendment is a small reorder inside the same function, same owner,
same deploy. CTO may fold and issue without a second full CVO cycle; I will re-read the amended W2
text on request.

## What I checked (independent grounding, not a re-read of ~F)

- **Served state, live (~1438Z):** `model_portfolio_benchmarks.json` head-object LastModified
  13:29:12Z, body `data_as_of=2026-07-27`, `generated_at=2026-08-03T13:29:11Z` -- matches ~F and CTO.
  All three benchmark output keys coherent at 07-27; `json/macro/macro_data.json` and
  `json/correlations/correlation_data.json` ALSO read `data_as_of=2026-07-27` (basis for Finding 2).
- **S3 versioning:** `opal-data-portal-v2` versioning ENABLED; the 07-30 build survives as version
  `JTV0rndkN387Qf5UhKe3zAMu1p0V08Ak` (13:12:20Z). Full version walk of the served key 07-17..now
  (basis for Findings 1 and 3). NOTE: fetched ~10 historical versions and read their vintage fields
  directly -- denominator: 25 versions listed since 07-17.
- **Source at vintage (working tree == b8874661fe for this file):** publish path :316/:319/:351
  unconditional, no date comparison anywhere (confirmed); `upload_json` :568-577 plain put_object;
  `build_rfr_daily` :588-604 crash mechanism consistent with the ValueError; uploads at :316/:319
  execute BEFORE the :324 `build_rfr_daily` call (basis for Finding 1).
- **`data_refresh` `handle_status()`:** parser :862-880 handles only
  `TaskStateEntered/TaskStateExited/TaskFailed/ExecutionFailed`; `STATE_LABELS` :730-770 has zero
  `Skip*` entries. Confirmed. Plus Finding 5 (Choice states).
- **Step Function, live:** all 8 executions of 2026-08-03 listed with statuses matching ~F's table;
  `describe-execution` inputs confirm `2394c6bf` = 07-30 manifest (`data 20260730 v1.pkl`) and
  `0d669fd1` = 07-27 manifest, both `auto_generated: true` via `yang-pipeline-trigger` on
  `uploads/manifest.json`.

## Finding 1 -- REQUIRED AMENDMENT to W2: FAILED executions PUBLISH (partial-publish half of the mode)

The four FAILED 07-31 executions each WROTE the served surface before crashing. Verified on object
versions: writes at 12:09:50Z and 12:12:14Z (+12:55/12:58 pairs) carry `data_as_of=2026-07-31` --
built from the KNOWN-DEFECTIVE pkl -- and the portal SERVED that data from 12:09Z until the 13:12Z
07-30 publish. Mechanism source-confirmed: `upload_json(comprehensive)` :316 and `upload_json(legacy)`
:319 run before `build_rfr_daily` :324 throws, so comprehensive+legacy land while timeseries never
does -- a FAILED run mutates the SEV1 surface AND leaves a mixed-vintage serve.

**Why it binds W2:** the guard as specced (reject OLDER) would NOT have stopped this half -- 07-31
was NEWER than served. The incident class is "a run that should not mutate the serve, mutated it,"
and it fired BOTH ways this morning. **Amendment: W2 additionally reorders the function so all three
output payloads are fully constructed (including the timeseries/rfr build) BEFORE the first
`upload_json`** -- this makes "three keys atomic" true in the failure case, not only the guard-reject
case. **Acceptance addition:** a mutant run that crashes mid-build (the real 07-31 pkl is a ready
fixture) leaves all three ETags byte-unchanged. Optional hardening, not required: S3 conditional-write
(`If-Match` on the ETag read at guard time) closes the read-compare-write race between concurrent
executions; observed interleavings are minutes apart, so recorded-not-required.

## Finding 2 -- RESIDUAL to record: the regression is ESTATE-WIDE; W2 guards one Lambda of many

The 13:27Z (07-27) run rewrote the ENTIRE portal data estate at 13:29Z -- benchmarks, correlations,
factor-tilts, etf_returns, macro + ~30 macro timeseries keys (measured via list-objects; macro and
correlations confirmed serving `data_as_of=2026-07-27` by body read). Every sibling `Generate*`
Lambda in `YangDataPipeline` shares the no-guard defect; W2 protects only the three benchmark keys.
W1 (pipeline re-run) correctly heals the whole estate -- and W1 acceptance should say so (Finding 4).
**Not blocking:** W2's scoping to the SEV1 named surface is defensible for speed; a pipeline-entry
guard has its own design questions (legitimate older-date excel-only partial manifests). **Record the
residual in the spec + open a follow-up item to replicate the guard pattern (or evaluate an
entry-level guard) across the sibling lambdas.** Without the recorded residual, "the fix closes the
failure mode" over-claims.

## Finding 3 -- RESIDUAL to record: backward writes are RECURRENT, and a second mechanism bypasses the Lambda

Version history of the served key shows this is at least the THIRD backward-clobber day, and one
mechanism is NOT the Lambda: writes at 07-31T21:46:44Z (bytes of the 07-23 build, `generated_at`
frozen 2026-07-23T13:33:08Z), 07-31T22:15:59Z and 08-01T22:11:33Z (bytes of the 07-28 build,
`generated_at` frozen 2026-07-28T13:23:31Z) are S3-level BYTE-COPIES -- a Lambda rebuild stamps a
fresh `generated_at` (cf. today's 13:29:11Z). 08-01T19:27Z shows the 07-30 build restored twice,
then clobbered again at 22:11Z -- consistent with the standing 08-01 "rollback onto itself" memory
(attribution INFERRED, not source-confirmed). **W2's guard cannot see raw S3 copies; that residual
is governed by fabric law (verify-live-before-mutation) only.** This also STRENGTHENS W2's
justification: the class fired on 07-31, 08-01, and 08-03.

## Finding 4 -- W1 acceptance addition (cheap)

W1's re-run heals the whole estate, but its acceptance only checks the three benchmark keys. Add one
non-benchmark probe (e.g. `json/macro/macro_data.json` reads `data_as_of=2026-07-30`) so the
acceptance measures what the re-run is actually for. Pre-fire head-object gate: confirmed correct
and live-consistent (pre-state IS 07-27 as of 1438Z; if W4's corrected 07-31 lands first, the gate
correctly STOPs W1).

## Finding 5 -- W3 note (cheap, non-blocking)

Choice-type states (`CheckDataPKL` etc.) emit `ChoiceStateEntered/Exited` -- ALSO unparsed, so
several existing `STATE_LABELS` entries are dead code today. Adding Choice handling in the same W3
pass is near-free; at minimum the spec should not imply Pass-handling makes ALL labeled states
visible.

## CTO ASK items, answered

- **(a) W2 semantics:** CONFIRMED -- independently derived the identical semantics before reading
  the spec (older=reject loud, equal=allow, missing=allow-loud, audited force_publish; the 08-01
  history proves deliberate rollback is a real operation, so the escape hatch is load-bearing).
- **(b) W1 before W2, un-guarded:** CONCUR -- W1 moves the serve FORWARD (07-30 > 07-27), the
  pre-fire state gate pins the window, and the identical run already SUCCEEDED at 13:10Z today.
  Delay costs more than the ordering risk.
- **(c) dropped grounding:** Findings 1-3 above (present in NEITHER ~F's log nor the spec).
- **Moratorium reading:** HOLDS for both W2 (a hard-fail gate in the pipeline -- a control on the
  flow, not notification machinery) and W3 (a defect fix in an EXISTING status endpoint, not a new
  monitor). W1/W4 are data repairs; moratorium not implicated.

## Compiler Tools

- `comp-which` HUD advisories honored where a tool fit; raw single-file reads + operational `aws`
  calls used for live grounding per Rule 21 (operational aws + pipe-greps are off-rail; two
  single-file greps carried `# rail-checked:` markers). No comp-tool models S3 object-version
  vintage walks -- the load-bearing instrument of this validation -- so that evidence is raw
  `s3api list-object-versions`/`get-object` with denominators printed.
- Did not re-run `comp-blast`/`comp-surface-check`: CTO ran both this session for the same spec
  (spec section 5); my task was validating the spec against live state, not re-deriving its
  blast metadata.

## Next Steps

1. **[1.0.0_SA_CTO]** Fold Finding 1 into W2 (+ Findings 2/3 as recorded residuals, 4/5 as
   acceptance additions); issue TOs + request DS/DT_PortfolioAnalytics spawns via MSTR. My
   sign-off attaches to the amended spec; offer of a quick re-read of the amended W2 text stands.
2. **[3.0.0_SA_CVO]** On W1 completion signal: independent re-verify of the served estate
   (benchmarks + one macro probe at 07-30); on W2 deploy: witness the failing-direction exercise.
3. **[0.0.0_AB_MSTR]** Informed same turn (validation complete, verdict CONDITIONAL GO).
