# comp-system BLOCKED-ON-PEER-LANDING guard v3 — wrong-entry-fails-open hole closed — 0.8.0_AE_CloudComp~A

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE

## Objective

Final follow-on in the same-session guard chain. CVO~Z's v2 verification (sound overall, deeper-gap
probe refuted) found one real latent hole: `_METRIC_SOURCE_FILES` hand-duplicated a fact
`compute_metrics()` already declares; a WRONG entry (not a missing one) fails OPEN, reintroducing the
laundering hazard the whole control exists to prevent. CTO~Z dispatched the close-out.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `python3 -m py_compile` | `org/modules/graph/comp_system.py` | PASS | after the hoist + consistency-fn edit |
| `comp-system --self-test` | `bash .tools/comp-system --self-test` | PASS 23/23 | 21 unchanged + 2 new (11e real-map-agrees, 11f mutant-caught) |
| `comp-system --check`/`--gate` | live, separate invocations | rc=0, SYSTEM CURRENT both | tree resolved to clean mid-session (peer commit landed) -- confirms the gate opens cleanly, not just blocks |

**What worked:** did both offered fixes (structural elimination via shared constants + an explicit
consistency check with a mutant) rather than picking one, since a construction-only fix has no runtime
proof and a check-only fix still allows the underlying duplicate to exist.
**What failed:** nothing this round — straightforward hoist + one new pure function.
**Gap found:** none new; this pass closes the one CVO~Z found in v2.

## Work Completed

`_MANIFEST_PATH`/`_LEDGER_PATH` module-level constants (hoisted from `compute_metrics()`'s locals);
`compute_metrics()` and `_METRIC_SOURCE_FILES` both now reference them (no re-typed duplicate).
`_metric_source_files_mismatches(candidate)` (new, pure) + self-test chk 11e/11f. Memo §6-7 updated.

## Files Modified

| File | Change |
|---|---|
| `org/modules/graph/comp_system.py` | v3 on top of v1+v2 (same file, still uncommitted) |
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/SYSPARITY_BLOCKED_ON_PEER_LANDING_20260725.md` | §6-7 new |

Neither committed by this lane (exec-lock / BASE_EXEC-lane convention, unchanged from v1/v2).

## Blockers

None. MCP traffic: 2 messages in (CVO~Z verification + CTO~Z dispatch) + 1 ack + 2 delivery reports.

## Current State

v1+v2+v3 all live in the uncommitted `comp_system.py`, 23/23 self-test, live tree confirmed CURRENT
(clean) on both entry points. Delivered to CTO~Z (land, stated as the last item on this control) and
CVO~Z (re-derive 11f independently, same discipline as 11b).

## Next Steps

1. **[1.0.0_SA_CTO~Z]** Land `comp_system.py` (v1+v2+v3 together) -- final pass on this control.
2. **[3.0.0_SA_CVO~Z]** Independently re-derive chk 11f's exact expected-mismatch tuple.
3. **[0.8.0_AE_CloudComp~A]** Event-driven, standing by.
