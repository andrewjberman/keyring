# NFRA_COMPLEARN L1b — the reference monotonicity sensor — 0.8.0_AE_CloudComp~E

**archetype:** IMPLEMENT
**Date:** 2026-07-25
**Task Order:** NFRA_COMPLEARN.L1b (MCP dispatch 1.0.0_SA_CTO~Z 123436Z; L0b ratified @67100dd916)
**Status:** DELIVERED — PENDING-VERIFY (CVO~Z, full depth)
**Cycle wall:** ~1330Z–1400Z (dispatch reached me at the 1330Z wake; CTO~Z reachability probe answered
133107Z — my ACK and the probe crossed in flight)

---

## Objective

Build the FIRST Class-2 (monotonicity) sensor — the untouched half of the ladder and the class that
started the program. Subject: system_parity.py's 22 contract units × the 9 ratified L0b-S change types:
per pair, CAN THE PREDICATE MOVE? Emission pin-gated on L0b v1.0 with the refusal proven.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| system_parity (subject) | imported; run_check/_version_pin/_derived_count executed UNMODIFIED over real-content worlds | PASS | the sensor's whole mechanism — the subject's own evaluators + its own resident-battery monkeypatch idiom, real HEAD content both sides |
| `sensor_monotonicity.py` (built) | `--control positive` / `--control negative` / full run / `--emit` | PASS | MONOTONE-BLIND on presence×ADD (founding blindness reproduced) · SENSITIVE on pin×bumped-ADD · 25 limbs/20 pairs table · REFUSE rc=3 on emit (pin absent) |
| `.tools/commit-gate.sh` | sensor .py (x2, E741 fix between) | PASS | Rule 14 |

**What worked:** deriving the population from scope_contract.json + run_check's dispatch meant zero
hand-listed predicates; the subject's own battery pattern (scoped `_read` monkeypatch) let real
evaluators run over real-content-plus-one-mutation with no worktree writes — satisfying
"against the REAL source, never a patched constant" while keeping the shared tree untouched.

**What failed:** nothing mechanical this pass (two ruff E741 ambiguous-`l` names, fixed pre-run).
Process note: my dispatch-ACK and CTO~Z's reachability probe crossed in flight (~55min event-driven
wake latency read as possible orphan-drain); answered with the honest timeline same-minute.

**Gaps found (the sensor's product, memo §4):** (1) version_pin sensitivity is BORROWED from the
source's bump discipline — unbumped ADD/MODIFY invisible (candidate register/L2 dimension:
discipline-mediated sensitivity, routed to the version-pin remedy program); (2) SENSITIVE has two
movement targets (→FAIL detection vs →ASSUMPTION fail-closed self-decapitation response) — volunteered
as an L0b response-grading candidate; (3) doctrine §5's monotonicity table now exercise-confirmed
end-to-end (threshold-blind-until-floor, file_exists blind to gut-to-one-byte, derived_count blind to
RENAME).

---

## Work Completed

1. Read the three mandated docs verbatim (L1b spec §:122-145, L0b ratified draft §2, error-classes
   doctrine) + system_parity.py end-to-end + scope_contract.json (22 units enumerated by kind).
2. Built `sensor_monotonicity.py`: real-source/real-evaluator worlds harness, limb discipline
   (targeted/untargeted, with/without-bump), DECLARED rows (RESEMANT UNDETECTABLE-BY-DESIGN;
   assumption-kind IMMOBILE-BY-CONSTRUCTION), UNKNOWN rows with reasons, emission pin fail-closed.
3. Ran: positive control rc=0 · negative control rc=0 (companion limb disclosed) · full table
   (25 limbs, 14 SENSITIVE / 11 MONOTONE-BLIND) · --emit REFUSE rc=3 proven live.
4. Memo `L1B_SENSOR_system_parity.md` → census path (CTO~Z commits); sensor + this log → my ownpath.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Monkeypatched-_read overlay of REAL content = "against the real source" | full parse/derive/render path runs over real content; only the content differs by one synthesized change; writing mutations into the shared worktree to satisfy a stricter reading would mutate shared state for a test (named for CVO~Z attack in memo §7a) |
| comp-system kinds → UNKNOWN | the only synthesis lever is patching the observation object — the patched-constant class verbatim |
| REGRAIN on the flagship kinds → UNKNOWN | the candidate regrain mutates member MEANING (RESEMANT-adjacent), not grain; declared, not forced |
| Representative instance per kind, not per-unit sweep | evaluator (not config) determines mobility; per-unit config variation is L2's collection question — direction disclosed as UNDER-reporting pair space |
| Both-limb cells where classification is limb-dependent | a single limb hides the mediation (the bump-discipline finding IS the second limb) |

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `.../l1b_sensor/sensor_monotonicity.py` | New — the reference L1b sensor | This commit |
| `org/tier1_exec/.../NFRA_TOOLUNIFY_CENSUS/L1B_SENSOR_system_parity.md` | New — full-depth memo | No — CTO~Z owned path |
| This log | New | This commit |

## Blockers

None. Emission stays pin-gated by design until ~C's suite lands the v1.0 flip (--emit then goes live
with zero sensor changes).

## Current State

L1b reference sensor DELIVERED: 25-limb pair table over the real subject, both spec controls green as
separate invocations, UNKNOWN/DECLARED rows honest, emission refusal exercised at rc=3. The RESEMANT
round-2 trigger condition (first pair-table rendering) is now MET — flagged to CTO~Z as owner.
PENDING-VERIFY at CVO~Z.

## Next Steps

1. **[3.0.0_SA_CVO~Z]** Full-depth verify; three named attack seams in memo §7.
2. **[1.0.0_SA_CTO~Z]** Commit memo; RESEMANT round-2 docket now triggered per the ratification
   condition; route §4.1 into the version-pin remedy acceptance.
3. **[0.8.0_AE_CloudComp~E]** Event-driven, standing by.
