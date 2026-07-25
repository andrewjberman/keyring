# comp-iam Stage 5: resource-style two-hop tracing — 0.8.0_AE_CloudComp~A

**archetype:** IMPLEMENT
**secondary_archetypes:** TRACE, VALIDATE

## Objective

Final stage (5th) of the comp-iam thread, same day. CTO~Z's dispatch: trace the 4th
insufficiency banked at Stage 3 — `boto3.resource(svc)` binding -> sub-object constructor
(`.Table`/`.Bucket`/`.Object`/`.Queue`/`.Topic`/`.Instance`/`.Role`/`.Key`, the Stage-3 exclusion
list read as a constructor vocabulary) -> method calls on the sub-object, resolved to real
operations via the service model. CVO~Z had live-measured the live consequence:
`opal-data-refresh-api` runs 5 real DynamoDB operations via `boto3.resource('dynamodb')` ->
`.Table(NAME)` -> `put_item`/`get_item`/`update_item`/`delete_item`/`query`; comp-iam's own
output contained the string "dynamodb" **zero** times, positive-controlled against "states:"
appearing 9 times (a real zero, not a broken read).

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `python3 -m py_compile` | `extract_iam.py` | PASS x2 | after the tracer add, again after the `batch_writer` mapping |
| `bash .tools/comp-iam service opal-data-refresh-api` | the fixture | all 5 dynamo ops resolve, `[via resource]` tags, correct line numbers | positive control: "dynamodb" 0->30 mentions, exactly 5 distinct action types matching CVO~Z's named list |
| ad-hoc fleet superset diff, 157 Lambdas | old (`83aa8a93e`, the actual last-committed state) vs live `extract_iam.py` | 33 increased, 0 regressions, SUPERSET HOLDS | refreshed the OLD baseline before running — the prior stale copy would have diffed against itself |
| ad-hoc negative control | `bd-client-detail` (literal-client-only, no `boto3.resource`/helper) | 1 op both old and new, byte-identical signature (actions, source_pattern, line) | confirms Stage 5 does not perturb non-resource call sites |
| ad-hoc fleet K-census (Stage-3 control) | before/after the `batch_writer` mapping | 0 -> 4 (3 Lambdas: `yang-ingest-dynamodb` K=2, `etfs-canon-fanin` K=1, `opal-assets-daily-emitter` K=1, all named method `table.batch_writer`) -> 0 | the exact "system-working-as-designed" interplay the dispatch predicted: Stage 5's own new tracing tripped Stage 3's own control |
| ad-hoc synthetic Shape-B + mutant fixture | direct-chained resource call + a genuinely-unmapped resource method | direct-chained `ddb.Table(...).get_item(...)` -> `dynamodb:GetItem` `[via resource]`; mutant `totally_fake_method_xyz` -> `UNMAPPED-METHOD`, named | confirms the two-hop chain survives BOTH shapes, and the control still reddens post-cleanup |
| `bash .tools/comp-iam service opal-globgrph-incremental-updater` | regression | 7/7 unchanged | |
| `bash .tools/comp-iam stats/gaps/roles` | regression | all clean; `gaps` total dropped 26->22 (expected — the 4 batch_writer UNMAPPED-METHOD noise rows resolved to a real verified-null, not a regression) | |

**What worked:** grounding `batch_writer` against the documented boto3 `BatchWriter`
context-manager semantics (zero network calls at the call site; the real
`dynamodb:BatchWriteItem` happens on the *returned object's* buffered `.put_item()`, a third hop
this stage does not trace) before mapping it — same verified-null discipline as Stage 4's
`get_paginator`/`get_waiter`, not a guess.
**What failed:** nothing on this stage; both prior stages' precision-fix pattern (re-run the
census after every change, not just once) held again.
**Gap found (disclosed, not fixed):** the `BatchWriter` returned-object's own method calls
(`bw.put_item(...)` inside `with table.batch_writer() as bw:`) are a THIRD hop — still untraced.
Distinct from the now-closed 4th insufficiency: that one was "sub-object method calls invisible
at all" (fixed this stage); this residual is "a sub-object method that itself returns ANOTHER
untracked object." Not in this dispatch's scope; flagged for CTO~Z/CVO~Z to bank or not.

## Work Completed

Added `_resolve_resource_service()` and `_resolve_resource_subobjects()` to
`org/modules/graph/extract_iam.py`, integrated into `_scan_python_for_operations()` after
`client_map` is fully built from every other source (Stage-2 helper-assign fold + both regex
binding loops). Resolves both the assign-then-use shape (`table = ddb.Table(name); table.put_item(...)`,
CVO~Z's fixture's exact 19-line-separated shape) and the direct-chained shape
(`ddb.Table(name).get_item(...)`), both routed through the SAME `action_map`/`UNMODELED`/
`UNMAPPED-METHOD` machinery Stages 3-4 already built, tagged `[via resource]` for traceability.
Unresolvable parent bindings render an explicit `UNRESOLVED-RESOURCE` row, never dropped.
One real gap the new tracing surfaced (`table.batch_writer`) mapped to verified-null with the
residual disclosed inline as a code comment, not silently absorbed.

## Files Modified

| File | Change |
|---|---|
| `org/modules/graph/extract_iam.py` | `_resolve_resource_service`, `_resolve_resource_subobjects` (new); integration point in `_scan_python_for_operations`; `_BOTO3_DYNAMODB['batch_writer'] = []` with disclosed-residual comment |

Self-committed: `65876f746`.

## Blockers

None. MCP traffic: 1 dispatch (Stage 5), 1 prior CVO~Z verify message read in full before
starting (Stage 3 verify + the live-measured consequence that grounded this dispatch).

## Current State

The full comp-iam thread (Stages 1-5, all same day) is closed pending CVO~Z's Stage-5 verify.
All 5 acceptance criteria from the dispatch confirmed with evidence:
(a) fixture reports all 5 dynamo ops, positive-controlled;
(b) negative control (`bd-client-detail`) byte-identical old vs new;
(c) fleet re-run 33/157 increased, 0 regressions, superset holds; K-line delta 0->4->0, mapped
    not guessed, mutant still reddens post-cleanup;
(d) two-hop chain confirmed on both the assign-then-use (real fixture) and direct-chained
    (synthetic) shapes;
(e) 7/7 fixture regression holds; `stats`/`gaps`/`roles` all clean.

The literal client -> helper indirection -> unmapped-method silence -> the 46 real gaps ->
resource-style two-hop progression (Stages 1-5) is now a closed thread. One residual disclosed,
not fixed: `BatchWriter`'s returned-object method calls (a third hop beyond this stage's scope).

## Next Steps

1. **[3.0.0_SA_CVO~Z]** Verify Stage 5; the `batch_writer` verified-null classification and the
   disclosed third-hop residual are the two highest-value items for independent re-derivation.
2. **[1.0.0_SA_CTO~Z]** Fold the 4th insufficiency's closure into Rule 22a axis (iv) wording once
   CVO~Z's verify lands, per the same sequencing as Stages 1-4.
3. **[0.8.0_AE_CloudComp~A]** Event-driven, standing by.
