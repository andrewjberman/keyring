# 0.4.0_DS_ClientPlatform — /work tick work_1813Z (NFRA.W2(b) pickup + coordinate-before-build)

**archetype:** DIAGNOSE
**secondary:** COORDINATE

## Inbox
- SENIOR_DISPATCH (COO): `[DRIVE] NFRA.W2(b)` — gold_prof.py PSS-parity-or-deprecate, **decide with 0.6.0, coordinate before building**, NORMAL pri. Constraint: NO ad-hoc gold run; validate on next scheduled nightly.
- Same msg confirmed D_04 orphan-cleanup RAVC2 (a74ff46eb) **received + accepted — clean**.

## Diagnosis (read the live wiring before building)
- **gold_prof.py:101** uses tree-summed **RSS** (`p.memory_info().rss`) = the CoW-inflation bug (phantom TB peaks). 0.6.0's runner-telemetry.py (fe907a974) fixed the same class with tree-summed **PSS** primary + RSS-retained + `sys_mem_*` (`_aggregate_sample`, lines 93-154).
- **gold_prof.py is the CANONICAL CROSS-PIPELINE profiler**, not bd-local: `orion-gold-dispatch.sh:398` pulls it from `s3://opal-runner-shared/code/gold/gold_prof.py`. It is the per-script wrapper for BOTH chains — bd `gold_dispatch.sh:245` + orion `orion-gold-dispatch.sh:452` (+ eclipse :512).
- **Output contract load-bearing on both chains:** `merge_perf_report()` (bd:412/1134, orion:585/1329) consumes gold_prof's `/tmp/perf_scripts/{id}.json` per-script aggregate -> `perf_report.json` -> `s3://{bucket}/gold/perf_report.json`. runner-telemetry emits a DIFFERENT shape (per-tick JSONL -> `.runtmp/telemetry`). A bare wrapper-swap breaks the merge unless it's also rewritten.
- 0.6.0 W2(a) state: their latest log (1718Z) = ADHC_BDTSCLB close + publisher decommission; **W2(a) not yet built**. Genuine pre-build coordination moment for both.

## Decision framing -> sent to 0.6.0 (SYNC-ASK) + CC COO
- The port-vs-deprecate call HINGES on W2(a) scope: end-to-end both-chains swap (wrapper + merge rewrite + opal-runner-shared retire) before tonight = DEPRECATE (I don't port); narrower = gold_prof STAYS the orion/inf emitter -> PORT the PSS fix.
- **My recommendation: PORT now** — ~10-line contained change (rss->pss + RSS fallback + sys_mem), makes BOTH chains' perf_report.json true-physical on TONIGHT's scheduled runs at zero extra compute (per Andrew's constraint), reversible. Reserve the full runner-telemetry-as-canonical-emitter swap as the deliberate CTO-gated W2(a)/W2(c) fleet move rather than racing it tonight.

## Posture
Holding the build pending 0.6.0's W2(a)-scope reply (NORMAL pri, not on 0.6.0's critical path). Build the agreed path this tick or next; RAVC2 on the scheduled-run validation. **No ad-hoc gold run** either way.

work-cycle:0007
