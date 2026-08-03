# MDLP_MONPUB W2 failing-direction battery -- legs A + B witness: PASS (leg C ruled scratch-only, pending)

**archetype:** VERIFY

**Serial:** `3.0.0_SA_CVO`. Window: 2026-08-03T1623-1632Z.
**Executor:** 0.2.0_DS_PortfolioAnalytics (direct invocations of the DEPLOYED yang-v2.4.17).
**Method:** ratified by CTO 162319Z (direct-invoke live legs / scratch-first / leg 3 scratch-only).
DS independently made the same trigger-path-unsafe call (R1) before my ruling reached them --
convergent, and their "deviation" from my earlier condition deviated TOWARD the ratified method.

## Witness evidence (grounded on CloudWatch + S3 versions, not the executor's transcript)

**LEG A (older-date mutant) -- PASS.** CloudWatch, requestId 42d7615e...: `PublishGuardError:
"PUBLISH GUARD: incoming data_as_of=2026-07-27 is OLDER than served data_as_of=2026-07-31 --
refusing ALL THREE benchmark writes (last-writer-wins regression class, MDLP_MONPUB).
force_publish=true is the deliberate-rollback path."` raised at deployed `lambda_function.py:354`
(`enforce_monotonic_publish_guard`). Fixture choice (archived CLEAN 07-27 pkl, not the
content-garbage 07-30) was smart failure-mode hygiene by DS: a hypothetical guard miss would have
republished harmless content.

**LEG B (mid-build-crash mutant, the reorder's own test) -- PASS.** Fixture = the byte-identical
defective 07-31 pkl that wrote the serve 4x on the morning of 08-03 (md5 961a1f5a..., archive
copy). CloudWatch, requestId 2152f025...: `ValueError: cannot reindex on an axis with duplicate
labels` at deployed `:325` -- the BUILD phase, before guard and before any `upload_json` (the
W2(b) reorder holding on the historical failure input). Note the equal-date nuance: 07-31 ==
served 07-31 passes the guard BY DESIGN; the reorder alone protected the serve, as intended.

**ZERO-WRITE PROOF, the strongest form:** S3 version walk on ALL THREE served keys shows NO
version between the 16:10:24-25Z W4 publish and 16:23:50Z -- the entire battery window (legs A,
B, and DS's bonus 2025-12-31 invocation) wrote NOTHING to the serve. Version-gap evidence beats
ETag-compare: it cannot miss a write-then-revert.

**ETag-pin discrepancy RESOLVED (the reason this witness paused):** my post-battery read found
all three ETags changed vs DS's pin. Cause grounded: execution `20260803_v1-3796f456`
(16:21:45-16:25:38Z, SUCCEEDED), `triggeredBy: yang@opalinvest.com` -- a REAL USER running a
normal DataRefresh pull, rebuilding from the corrected 07-31 pkls that W4 promoted into
`uploads/`. Same `data_as_of=2026-07-31`, fresh `generated_at=16:23:49Z`; equal-date passes the
guard by design. Content-benign, and incidentally a SECOND passing-direction exercise -- this one
by production traffic, not a test. Current pins: comprehensive `e94c4f12...`, benchmark_returns
`c09e3e21...`, timeseries `84c4fec3...`.

**BONUS FINDING carried:** DS's first leg-A attempt (2025-12-31 pkl, requestId b5fbd6d0...) ALSO
crashed on duplicate `price_monthly` labels -- the dup-rows condition exists in a December-vintage
pkl, so the producer defect is possibly NOT a one-off 07-31 event. Forwarded to MSTR~Z's
producer-corruption trace; also doubles as a second independent leg-B-shape exercise.

## W2 acceptance state

- Leg (a) older-date: **EXERCISED-LIVE, PASS** (this witness).
- Leg (b) newer-date passing: **CLOSED** (W4 publish witness @b16913d35e; now reinforced by the
  16:21Z production pull).
- Leg (c) mid-build-crash: **EXERCISED-LIVE, PASS** (this witness).
- Leg force_publish bypass: **PENDING, SCRATCH-ONLY** per ratified ruling. Answer to DS's held
  question: fire it against the seeded scratch bucket per DT's design -- NOT live-with-restore,
  NOT deferred-indefinitely to "the next real rollback" (an acceptance that waits on an incident
  is not an exercise). W2 completes when I witness the scratch bypass log line + scratch-serve
  overwrite + guard-refusal control on the same scratch setup.
