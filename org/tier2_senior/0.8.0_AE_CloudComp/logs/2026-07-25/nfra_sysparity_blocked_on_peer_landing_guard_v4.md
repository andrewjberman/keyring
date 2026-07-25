# comp-system BLOCKED-ON-PEER-LANDING guard v4 — association third limb — 0.8.0_AE_CloudComp~A

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE

## Objective

Final follow-on in the guard chain (v1-v4, all this session). CVO~Z's v3 verification named one
narrow residual: `_metric_source_files_mismatches()`'s own `truth` dict is a third hand-written
statement of the metric->path association. CTO~Z dispatched the close-out with CVO~Z's
verified-implementable fix (basename-in-source).

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `python3 -m py_compile` | `org/modules/graph/comp_system.py` | PASS | |
| `comp-system --self-test` | `bash .tools/comp-system --self-test` | PASS 26/26 | 23 unchanged + 3 new (11f2 typo mutant, 11g association holds, 11h association mutant) |
| `comp-system --check`/`--gate` | live, separate invocations | rc=2, BLOCKED-ON-PEER-LANDING both | tree still organically dirty (different peer file this round), 0 regenerate mentions |

**What worked:** folding CVO~Z's own verification-message test shape (the .yml/.yaml typo) into the
committed suite rather than leaving it only as a report artifact.
**What failed:** nothing new this round.
**Gap found:** flagged proactively (not waiting for CVO~Z to find it) — the new association check is a
weak substring test (`basename in source`), which could false-pass on a source string containing the
expected basename as a substring of an unrelated longer filename. Disclosed in the delivery message,
not fixed this pass (avoided over-engineering past the verified-implementable spec).

## Work Completed

`_metric_source_association_mismatches(candidate, metrics)` (new, pure) in
`org/modules/graph/comp_system.py`; self-test chk 11f2/11g/11h. Memo §7-8 updated with the v4 closeout
and the v3 CVO~Z verification result.

## Files Modified

| File | Change |
|---|---|
| `org/modules/graph/comp_system.py` | v4 on top of v1-v3 (same file, still uncommitted) |
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/SYSPARITY_BLOCKED_ON_PEER_LANDING_20260725.md` | §7-8 new |

Neither committed by this lane (exec-lock / BASE_EXEC-lane convention, unchanged across all four rounds).

## Blockers

None. MCP traffic: 2 messages in (CVO~Z v3 verification + CTO~Z v4 dispatch) + 1 ack + 2 delivery
reports.

## Current State

v1-v4 all live in the uncommitted `comp_system.py`, 26/26 self-test, live tree still organically dirty
and correctly blocking. Delivered to CTO~Z (land, stated closing item) and CVO~Z (self-flagged the
substring-match weak-coupling edge for their attention, not withheld).

## Next Steps

1. **[1.0.0_SA_CTO~Z]** Land `comp_system.py` (v1-v4 together) — final pass on this control.
2. **[3.0.0_SA_CVO~Z]** Decide whether the flagged substring-match edge needs closing or is acceptable
   residual risk for this control's scope.
3. **[0.8.0_AE_CloudComp~A]** Event-driven, standing by.
