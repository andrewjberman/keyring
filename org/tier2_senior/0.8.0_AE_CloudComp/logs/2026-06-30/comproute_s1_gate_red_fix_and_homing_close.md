# NFRA_COMPROUTE Stage-1 -- gate-RED fix + comp-symbols homing close (lane ~E)

**archetype:** COORDINATE
**secondary_archetypes:** IMPLEMENT
**Serial:** 0.8.0_AE_CloudComp~E
**Date:** 2026-07-01 UTC
**Window:** since the route-fixes log (301d9f9ed) -> ~0209Z

## Summary

Thin coordination delta closing out the COMPROUTE Stage-1 build-out. ~C caught that comp-symbols was
RED-ing the shared coverage gate (untracked shim + unplaced-in-map); I fixed both halves and ~C homed
it. Both Stage-1 tools (comp-dispatch + comp-symbols) are now HOMED + routed, gate GREEN, both shims
tracked. Also: /watcher re-arm under active box fork-exhaustion.

## The gate-RED fix (the substantive work this window)

~C's finding: `.tools/comp-symbols` was UNTRACKED (`.gitignore:183` blanket `.tools/` ignore) -> it
would NOT propagate to fresh checkouts, AND comp-symbols on disk made `comp-coverage-check
inventory_completeness` FAIL ("UNPLACED") for anyone holding the file -> masked real gate-verifies
for the fleet.

- **Part 1 (propagation) -- FIXED:** `git add -f .tools/comp-symbols .tools/comp-dispatch` +
  safe-commit `4fd568a0b` (pushed). Both shims now git-tracked. NOTE: comp-dispatch had the SAME
  latent gap -- its engine was tracked (d804ff744) but its shim wasn't; fixed both.
- **Part 2 (map landing) -- HANDED ~C:** the precise concern-based distinct_from (comp-symbols =
  single-file FORWARD definition-inventory; input=FILE; distinct from comp-blast's reverse
  blast-radius input=NAME, and from the cross-file usage/drift/consumer neighbors by concern).
  ~C homed it `df606c15a`: gate GREEN, selfcheck 17/17, routing verified (T6 file-symbol intent ->
  comp-symbols; T7 control graph-wide-occurrence still -> comp-xref, NOT hijacked). ~C declared the
  FORMAL distinct_from to comp-blast ONLY (the only shared-resource `symbol-defn` neighbor -- the
  declared_non_redundancy gate keys on shared-resource overlap; the others touch different resources).
  RAVC-closed: I validated + agreed (no 4-way formal declaration needed).

## Reachability (watcher)

The inbox Monitor died 3x this session with FORK EXHAUSTION (`CreateProcessW failed ... errno 27`,
`fork: Resource temporarily unavailable`) -- a box-wide resource signal (COO~B saw it independently,
2 agents ground-truthing = real fork-saturation, flagged MSTR; not a per-agent bug, not a charter).
Mitigation held lossless via turn-top `check_inbox` pulls (per the watcher caveat -- messages persist).
Re-armed at /watcher (task bbxuq09vl) -- this arm is live (streamed the read/ backlog without dying;
pressure appears eased).

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| comp-grep | symbol-family tools in comp-coverage-map.yaml | PARTIAL | 0 literal matches (map uses different keys) -> grounded that I couldn't confirm the neighbor keys -> gave ~C the concern-PRINCIPLE distinct_from, ~C matched to real keys |
| safe-commit.sh | 4fd568a0b (force-added shims) | PASS | git add -f past the .gitignore, then safe-commit the pathspec |

**What worked:** the force-add fixed BOTH shims (comp-symbols + the latent comp-dispatch gap) in one
commit; the concern-based distinct_from let ~C land the map entry against the real neighbors.
**What failed:** the Monitor fork-exhaustion (environmental, box load; worked around via check_inbox).
**Gap found:** the comp-tool SHIM-tracking gap -- a new comp-tool's engine (org/modules/graph/*.py)
commits fine, but the `.tools/` shim is gitignored + needs an explicit `git add -f` (else it doesn't
propagate + RED-s the coverage gate). Worth folding into the comp-tool creation checklist.

## Current State

Both NFRA_COMPROUTE Stage-1 tools (comp-dispatch + comp-symbols) HOMED in the COMPUNIFY map + routed;
gate GREEN (selfcheck 17/17); all 3 routing rules landed (dispatch-intent + output-key + file-symbol);
both shims git-tracked. Full session delivered + live: COMPLEARN P0+P1+P3 (substrate) + Behavior
re-emit + gap_heat worklist v0 + comp-dispatch + comp-symbols + 3 route-fixes. All deploy ledgers
CLOSED; all commits pushed. Reachable (Monitor bbxuq09vl + check_inbox fallback).

## Next Steps

1. **[2.0.0_SA_COO~B / 1.0.0_SA_CTO]** the COMPROUTE L3 CORE POSTERIOR ENGINE (COO~B named me owner --
   I own tool_activity + the views + both Stage-1 tools) + the P2 scorer -- both un-gate on CVO~B's
   COMPUNIFY no-regression PASS (in progress). Available immediately on dispatch.
2. **[0.0.0_AB_MSTR / 2.0.0_SA_COO~B]** the box fork-exhaustion (cap-awareness) -- COO~B flagged;
   eases as substrate parallelism winds down post-gate-lift.
3. **[0.7.0_AE_CloudOps / CTF]** the logs->S3 sync for in-VPC Behavior/Change re-emit autonomy (shared
   w/ code_heat) -- COO~B-routed.

## Blockers

None. L3 core + P2 scorer await CVO~B's COMPUNIFY gate-lift PASS (a real external gate). All
depth-independent solo work delivered + verified this session.
