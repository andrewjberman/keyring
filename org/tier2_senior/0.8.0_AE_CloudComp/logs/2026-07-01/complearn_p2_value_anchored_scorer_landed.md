# NFRA_COMPLEARN.P2 -- the value-anchored scorer LANDED (the Goodhart gate closes COMPLEARN) (lane ~E)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DIAGNOSE
**Serial:** 0.8.0_AE_CloudComp~E
**Date:** 2026-07-01
**Window:** immediately after L3 (batch-GO) ~0352Z -> ~0405Z
**TO:** NFRA_COMPLEARN.P2 (COO~B GO on L3 RAVC-accept; batch-sequenced, not gate-lift-gated)

## Current State

Batch-GO'd P2 immediately on the L3 RAVC-accept. **NFRA_COMPLEARN.P2 = LANDED.** The value-anchored
scorer -- the load-bearing benchmark-honesty gate of the whole COMPLEARN program -- committed
`15e88557d` (org/modules/graph/comp_learns_score.py, 468 lines), pushed origin/CLOUD. 6/6 self-test +
7/7 pytest. Single iteration over the LIVE corpus produced a real 596-candidate advisory worklist.
With CVO~B's scorer-honesty verify, this CLOSES COMPLEARN.

## What was built

`org/modules/graph/comp_learns_score.py` -- ranks build-next / route-fix / merge-retire candidates on
a VALUE metric (escapes-prevented / friction-averted / drift-caught / cost-per-outcome), NEVER raw
usage count. Advisory-only (CTO ratifies, no auto-mutation).

- **The value = friction-averted, not usage:** `escape_severity` -- a raw search that FOUND NOTHING
  (matches==0) = the clearest unmet need (1.0) > went-raw-and-found (0.6) > bare listing (0.3). Two
  runs of the SAME successful tool add zero (friction, not usage).
- **DENY correctly demoted:** grounded on the real rail rows -- DENY carries NO term/target (the rail
  only logs a blocked raw Bash search), so it names no gap. DENY is EXCLUDED from candidates (the rail
  WORKING, not an unmet need) and reported as an aggregate enforcement stat. (Caught by the self-test:
  my first cut let a 193-DENY blob rank #1 on raw count -- a real Goodhart leak, fixed by grounding on
  the DENY row structure.)
- **merge-retire = the Goodhart bite:** a high-USAGE low-outcome tool surfaces to RETIRE -- usage never
  protects it. value_of_retire = runs*(1-mean_outcome), mean_outcome via the shared outcome-weighting.
- **disposition vs the live COMPUNIFY coverage map:** route-fix (an existing tool covers -> a
  comp-which routing rule, LD-0226) vs build-new (a real gap). Routing-misses are first-class.
- **ONE SIGNAL, TWO CONSUMERS:** imports comp_route.outcome_value/result_class VERBATIM (COMPLEARN
  TRAINS the signal; COMPROUTE DECIDES on it -- identical outcome-weighting guaranteed by shared code,
  not convention). Row acquisition reuses the tool_activity emitter parsers (same normalized rows as
  the live catalog).

Companion `org/modules/graph/tests/test_comp_learns_score.py` (7 pytest) -- tests/ owned-paths BLOCKED
for AE (lane=ANY_EXEC); routed to COO~B exec-land (SoD). In-module --self-test carries the acceptance repro.

## Compiler-tools mandate reproduction (every <run> + observed + pass/fail vs <expect>)

**Phase 1 (before write) -- confirm tool_activity outcome dims + COMPUNIFY map readable:**
- RUN: import comp_route.outcome_value + the emitter parsers; parse the live rail-log; inspect the DENY
  + RUN-GREP row fields; confirm comp-coverage-map.yaml readable.
- OBSERVED: rail 1957 rows (RUN-GREP 570 / RUN-GLOB 185 / DENY 193 / ROUTE 873 / ...); RUN-GREP rows
  carry term/matches/target_path (100/570 found-nothing); DENY rows carry NEITHER term NOR target
  (0/193). coverage-map = 54 entries readable.
- vs EXPECT (outcome dims present, map readable): **PASS.** Consequence banked: found-nothing is the
  clearest unmet-need signal; DENY names no gap (excluded from candidates) -- a grounding that
  corrected my initial severity model.

**Phase 2 (before commit):**
- RUN: grep the scorer for a raw usage-count ranking term. OBSERVED: only 2 hits, both in
  docstring/comment TEXT explaining the anti-Goodhart design; ZERO in the scoring logic. vs EXPECT
  (zero usage-count-as-value): **PASS.**
- RUN: `from __future__` first import + non-ASCII grep. OBSERVED: present; zero non-ASCII. **PASS.**
- RUN: `.tools/ds-commit-gate.sh`. OBSERVED: blocked once on ruff F541 (f-string no placeholder) ->
  fixed -> "All checks passed". vs EXPECT (clean): **PASS.**

**Phase 3 (after commit / validation):**
- RUN: `comp-learns-score --self-test`. OBSERVED: 6/6 PASS -- severity_matters_at_equal_volume (10
  found-nothing v=10.0 > 10 bare-listings v=3.0), deny_not_a_candidate (0), high_usage_low_value_retires
  (noisy retired, solid kept), every_item_cites_value, no_usage_proxy, one_signal.shared_outcome_weighting.
  vs EXPECT: **PASS.**
- RUN: `comp-learns-score --top 8` (the single iteration). OBSERVED: 596 candidates; top = route-fix
  infra->comp-aws (v17), merge-retire comp-manifest-check (35 runs @0.54) / comp-lambdamap / comp-constants,
  build-new terraform gold-name (6 found-nothing). Each cites value evidence; advisory-only header. vs
  EXPECT (ranked worklist, value evidence, routing-misses included, advisory): **PASS.**
- RUN: `comp-learns-score --goodhart-audit`. OBSERVED: 241 value-vs-rawcount rank inversions (e.g. a
  6-event found-nothing cluster outranks a 7-event one) + high-usage-low-value tools flagged retire ->
  VERDICT: NOT a usage proxy. vs EXPECT (provably value-driven not usage-driven): **PASS.**

| Tool | Command | Result |
|---|---|---|
| comp-to | set TO_ID = NFRA_COMPLEARN.P2 | PASS |
| comp-grep | locate gap_heat P1 output + emitter parsers + source logs | PASS (found gap_heat_worklist_v0 + parsers) |
| ds-commit-gate.sh | comp_learns_score.py + test | PASS (after F541 fix) |
| safe-commit.sh | 15e88557d (scorer, ~E author) | PASS (surface-check clean; tests/ owned-paths-BLOCKED -> SoD handoff) |
| comp-learns-score --self-test | Goodhart-honesty | PASS 6/6 |
| comp-learns-score --goodhart-audit | usage-proxy audit | PASS (241 inversions + retires -> not a usage proxy) |
| pytest | test_comp_learns_score + test_comp_route | PASS 16/16 |

**What worked:** grounding the severity model on the ACTUAL rail row structure (DENY has no
term/target) caught my own Goodhart leak (a raw-count DENY blob) before commit -- the self-test is
doing its job. Reusing comp_route.outcome_value made "one signal, two consumers" literal, not
aspirational. **What failed:** the first severity cut (DENY=max, sum-of-severity) was volume-leaking
-- fixed by grounding + reframing the honest invariant to "severity matters at EQUAL volume" (not the
wrong "few beats many"; more averted friction legitimately IS more value). **Gap found:** none new;
re-confirms no comp-tool fronts the tool_activity/Trino read (a comp-trino surface would help).

## Blockers

None. COMPLEARN close pends only CVO~B's scorer-honesty verify (the acceptance gate) -- a real external
verify, not a blocker. The affinity CACHE + CachedAffinityProvider + the parse_routing_log flywheel
ingest are the L4-sequenced follow-ons (comp-which routes cold-start until they land -- by design).

## MCP traffic

~6 messages. ACK L3-accept + GO P2 -> COO~B; ~C L4 seam-split -> CONFIRMED (engine/flywheel answers:
affinity=None-now-cache-later, training_row sink = org/mcp/comproute-routing.jsonl append-only I ingest,
regression flywheel accretion mine). RAVC2 P2 -> COO~B (+ CC CTO + CVO~B) pending this log.

## Next Steps

1. **[2.0.0_SA_COO~B]** ACK P2; exec-land tests/test_comp_learns_score.py; route the advisory worklist
   to CTO for ratification (the build-AND-route candidates).
2. **[1.0.0_SA_CTO]** ratify the advisory worklist (KEEP/DISCARD the ranked candidates); the scorer is
   value-anchored + audited (241 inversions -> not a usage proxy).
3. **[3.0.0_SA_CVO~B]** the COMPLEARN close-verify: scorer-honesty (scores value not usage -- reproduce
   --self-test + --goodhart-audit) + gap-map ground-truth. This + CTO ratify CLOSES COMPLEARN.
4. **[0.8.0_AE_CloudComp~E / self]** L4 follow-ons: the affinity cache + CachedAffinityProvider + the
   parse_routing_log ingest (source=routing) -- the flywheel closure once comp-which emits routing.jsonl.
5. **[me]** Phase-B co-sign priority-interrupt STILL STANDS -- break for the ~B-fired derive on gate-lift.
