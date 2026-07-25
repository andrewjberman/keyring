# comp-iam FINAL ROUND: Key/Attr false positive + arc close — 0.8.0_AE_CloudComp~A

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, SCRIBE

## Objective

CTO~Z tagged this the FINAL round of the comp-iam tracer arc (Stages 1-6, same day),
accepting CVO~Z's unprompted request to choose an end rather than let the arc run until finds
dry up. Two items: (1) fix the `Key`/`Attr` condition-builder chained-call false positive
CVO~Z's Stage 6 verify found; (2) re-derive the 22/157·50-row exposure figure post-fix. The
separate Stage-7 over-perm honesty item was explicitly re-tagged out of this arc by CTO~Z
(125806Z) — different surface, different defect class, its own timeline.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `python3 -m py_compile` | `extract_iam.py` | PASS | |
| `bash .tools/comp-iam service opal-portfolio-export-download` | real fixture | false-positive rows gone; `dynamodb:Query` still correctly reported | |
| ad-hoc before/after diff | same fixture, old (`b6745914d`) vs new | ONLY the 2 false-positive rows removed (`Key(...).eq`, `Key(...).begins_with`); `dynamodb:Query` + the real `generate_presigned_url` DEFERRED row byte-identical | precise, no collateral |
| ad-hoc synthetic positive control | real `kms.Key(key_id)` resource-constructor chain (KMS, a resolved client_map service) | still correctly resolves as a resource sub-object, unaffected | proves the fix discriminates by AST-grounded import binding, not a name collision |
| ad-hoc synthetic regression | earlier UNRESOLVED-CLIENT/RESOURCE fixture (genuine unresolvable `Table()`/helper chains) | unchanged | `Table` isn't in the condition-builder set |
| ad-hoc fleet exposure re-derivation, 157 Lambdas | post-fix | 22/157 Lambdas, 48 rows (was 22/157, 50) | Lambda-count unchanged (opal-portfolio-export-download keeps its one genuine presigned-url row); row-count drops by exactly 2 |
| ad-hoc fleet superset diff | this fix vs Stage-6-committed (`b6745914d`) | 156 unchanged, 1 "regression" (`opal-portfolio-export-download: 4 -> 2`) — EXPECTED, not a defect: this round's job was removing 2 false-positive rows, so the superset-only invariant (valid for Stages 1-5's purely additive changes) does not apply to a bug-fix round | disclosed, not hidden behind a passing label |
| `bash .tools/comp-iam service opal-globgrph-incremental-updater` | regression | 7/7 unchanged | |
| `bash .tools/comp-iam stats/gaps/roles` | regression | clean; `gaps` total 22->20 (2 fewer false MISSING-classified rows removed, not a new gap) | |

**What worked:** grounding the fix in an AST import-binding detector rather than a hardcoded
`'conditions'` string match — the positive control (real KMS `.Key()`) proves the distinction
holds on the actual ambiguity (module-alias-qualified `Key`/`Attr` vs every other use of the
same constructor names), not on a name that happened to appear in one fixture.
**What failed:** nothing this round.
**Gap found:** none new.

## Work Completed

Added an AST-grounded condition-builder-alias detector to `_resolve_resource_subobjects()`:
scans each file's `import boto3.dynamodb.conditions [as X]` statements, collects the bound
name(s), and treats a `<name>.Key(...)`/`<name>.Attr(...)` chain as a condition builder (zero
IAM impact, no Operation emitted) rather than an unresolved resource sub-object, at both Shape
A (assign-then-use) and Shape B (direct-chained) match points. Re-derived the fleet exposure
count post-fix: **22/157 Lambdas, 48 DEFERRED/UNTRACED rows** — the corrected number to quote
going forward, replacing the pre-fix 50.

## Files Modified

| File | Change |
|---|---|
| `org/modules/graph/extract_iam.py` | condition-builder alias detector + exclusion check at Shape A and Shape B |

Self-committed: `4ed47a8f2`.

## Blockers

None. MCP traffic this window: CVO~Z's Stage 6 verify (actionable, one false-positive class
named), CTO~Z's Part-1 ruling (over-perm honesty fix, design-held item b, part 3 withdrawn),
CTO~Z's FINAL-round dispatch (this work).

## Current State

**The comp-iam tracer arc (Stages 1-6 + this FINAL round) is CLOSED.** Named residuals,
carried forward rather than chased (per CTO~Z's explicit bar: fix only if it makes an output
WRONG, moves a QUOTED number, or creates a NEW silent absence):
- **BatchWriter's returned-object `.put_item()`/`.delete_item()` — a third hop beyond
  Stage 5/6's two-hop tracer.** `batch_writer()` itself is correctly verified-null and named
  (`dynamodb:BatchWriteItem` implied); the actual buffered calls on the returned object are
  still untraced. Disclosed since Stage 5, unchanged.
- **Cross-file helper construction** — a client-factory helper defined in a different file
  than the one being scanned is invisible (each file is parsed independently). Disclosed since
  Stage 2, unchanged.

Corrected fleet exposure figure for the deletion-hazard framing: **22/157 Lambdas, 48 rows**
(supersedes the pre-fix 22/157·50 quoted in the Stage 6 log/report). The over-perm applied-
plane honesty fix (CTO~Z ruling 125708Z) is explicitly NOT part of this arc — separate item,
own timeline, to be picked up next.

## Next Steps

1. **[3.0.0_SA_CVO~Z]** Verify the false-positive fix + the corrected 22/157·48 exposure
   number.
2. **[1.0.0_SA_CTO~Z]** Arc closure acknowledgment; the over-perm honesty item (ruling
   125708Z) is next, on its own timeline, not gated on this.
3. **[0.8.0_AE_CloudComp~A]** Move to the over-perm honesty fix (separate item) next.
