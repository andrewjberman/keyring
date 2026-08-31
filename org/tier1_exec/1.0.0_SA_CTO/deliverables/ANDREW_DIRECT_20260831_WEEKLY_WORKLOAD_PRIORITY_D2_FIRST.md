# Weekly Workload Priority - D2 First

**Seat:** 1.0.0_SA_CTO
**Date:** 2026-08-31
**Source:** Andrew-direct in this session

## Priority Ruling

Andrew clarified the week-level ordering:

1. D2 Advisor Intelligence performance reporting is the peak priority.
2. The immediate business question is how far 49Financial is from being properly set up end to end.
3. D8 `MDPF_HEALGAP` and the self-healing auth-failure/retry standardization are important
   enhancements and should be standardized across similar auth-dependent pipelines.
4. D8 must not outrank D2. D8 work should proceed when it protects the D2 path or when D2 has no
   executable gate, but the primary delivery focus is finishing D2 end to end.

## D2 Workload Shape

The current near-term D2 critical path is:

- `ADVI_BDPARITY` W2: `0.4.0_DS_ClientPlatform~Y` owns the Andrew-approved re-fire. It is waiting for
  the 00:00Z fresh Black Diamond session mint, then must re-run the one-call auth pre-flight, fire W2
  if fresh, and report the four acceptance criteria with denominators.
- `ADVI_49F`: C02-g-10 / A07STAMP is closed on exercised evidence. C02-g-13 / VINTAGEDIGEST waits on
  the Tuesday 2026-09-01 12:45Z scheduled fire; no hand invoke. The eight lost DS gold uncommitted
  edits must be disclosed to the next DS gold seat but do not block the currently served C02 cells.
- `ADVI_INSURE`: S1e repair is landed, but S1e remains open until the first post-repair scheduled
  2026-09-01 04:35Z fire proves clauses 1 and 4. No hand invoke or substitute evidence.
- D2 performance-reporting readiness assessment: after the W2 result and the Tuesday scheduled-fire
  reads, CTO/COO need a compact readiness map for 49Financial covering what is complete, what remains
  gated, who owns each remaining action, and whether the portal-facing setup is blocked by data,
  parity, insurance, serve, or frontend work.

## D8 Boundary

`MDPF_HEALGAP` remains important but secondary to D2. Its atom-decomp is usable design input but not a
certified final rectangle, and TOs remain blocked pending the Site Z comb and Andrew's
whole-register/device placement decision. The Cottonwood one-shot remains separately open at Andrew;
the `ADVI_BDPARITY` W2 egress approval does not cover it.

For this week, D8 standardization should be framed as a reusable auth/retry pattern to apply across
similar pipelines only after the placement/execution gate is settled, and without creating alarms or
detect/report monitors while the D10 `GLOBALALARM` hold is active.

## Responsibility Rule

COO owns work-population routing and stale/open face triage. CTO owns architecture gates, priority
posture, and the readiness assessment. MSTR owns register placement/device-decision process and Site Z
comb orchestration. CVO owns certification/verdicts. Executing DS/AE lanes own their scoped evidence
and must report denominators, not ratios.

No seat should convert this priority clarification into a new implementation task without the
applicable Rule 27 stage, existing TO, or issuer-routed lane.
