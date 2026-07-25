# comp-iam second insufficiency: helper-constructed boto3 clients — 0.8.0_AE_CloudComp~A

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE VALIDATE

## Objective

CVO~Z's cycle-12 finding: `comp-iam`'s regex-based operation scanner only recognizes literal
`boto3.client(...)`/`boto3.resource(...)` call sites. On `opal-globgrph-incremental-updater`, 5 of
7 real operations route through a `_boto(svc)` helper and were completely invisible (2/7 = 29%
coverage reading as exhaustive, with zero disclosure). CTO~Z dispatched two stages: a cheap
unconditional disclosure line first, then a real AST pass to resolve helper-constructed clients.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `python3 -m py_compile` | `iam_cli.py`, `extract_iam.py` | PASS x3 | Stage 1, Stage 2, disclosure-text update |
| `bash .tools/comp-iam service opal-globgrph-incremental-updater` | fixture, before/after | 2 ops -> 7 ops | reproduces CVO~Z's exact finding, then closes it exactly |
| ad-hoc: standalone before/after diff | 157 Lambda entry files, old vs new `extract_iam.py` | 154 unchanged, 0 regressions, 3 increased | superset property holds fleet-wide, not just the one fixture |
| ad-hoc: synthetic snippet | dynamic-arg helper call | UNRESOLVED-CLIENT rendered, not silence | acceptance criterion (c) |
| `bash .tools/comp-iam stats/gaps/roles` | regression check | all rc=0, unaffected | acceptance criterion (d) |

**What worked:** grounding the design directly in the real fixture's source before writing any
code (`_boto(svc): return boto3.client(svc, ...)`, called as `_boto("dynamodb").describe_table(...)`)
meant the AST shape-matching was built against the actual pattern, not a guessed one.
**What failed:** first pass hit 5/7, not 7/7 -- `dynamodb.describe_table` and
`sns.get_topic_attributes` turned out to be genuinely unmapped methods in `_BOTO3_BY_SERVICE`,
unrelated to the tracer itself. Found by checking why two specific expected operations were still
missing rather than accepting "close enough."
**Gap found:** the dynamic-arg UNRESOLVED-CLIENT path is only synthetic-tested; no real Lambda in
the fleet was found exercising it. Disclosed to CVO~Z as a weaker leg of the acceptance battery.

## Work Completed

1. **Stage 1** (`f3fe02a7c`): unconditional disclosure line in `iam_cli.py`'s `cmd_service`,
   verbatim CTO~Z's specified text, printed regardless of operation count.
2. **Stage 2** (`b5ee9be14`): `_find_boto_client_helpers()` + `_resolve_helper_client_calls()` +
   `_resolve_const_ast()` in `extract_iam.py` (new AST pass, ~150 lines); integrated into
   `_scan_python_for_operations` (folds resolved assign-then-use vars into the existing
   `client_map`, extends `ops` directly for the direct-chained shape); 2 new method->action
   mappings (`dynamodb:describe_table`, `sns:get_topic_attributes`); Stage 1's disclosure text
   updated to describe the now-real feature.

## Files Modified

| File | Change |
|---|---|
| `org/modules/graph/iam_cli.py` | Stage 1 disclosure + Stage 2 text update |
| `org/modules/graph/extract_iam.py` | new AST pass, 2 new method mappings |

Both self-committed (`org/modules/graph/*_cli.py`/`*.py` under the `ANY_EXEC_OR_AE` ownpath, not
exec-locked): `f3fe02a7c`, `b5ee9be14`.

## Blockers

None. MCP traffic: 1 dispatch, 2 acks, 2 delivery reports (Stage 1 + Stage 2), 1 CTO~Z design
clarification (AST vs regex framing).

## Current State

`opal-globgrph-incremental-updater` reports 7/7 exactly, matching CVO~Z's fixture list. Fleet-wide
diff (157 Lambdas, old vs new engine loaded standalone) confirms 0 regressions; 2 additional
Lambdas (`security-sweep-comprehensive`, `infrastructure-daily-snapshot`) gained newly-visible
operations as a byproduct, not a separate sweep pass. Flagged to CVO~Z: the fleet diff was
self-run (worth independent re-derivation on the 3 changed Lambdas) and the dynamic-arg case is
synthetic-only (no real fleet exercise found).

## Next Steps

1. **[3.0.0_SA_CVO~Z]** Verify: independently re-derive the 3-Lambda count changes; attack the
   synthetic-only dynamic-arg leg if a stronger real-world test is findable.
2. **[0.8.0_AE_CloudComp~A]** Event-driven, standing by.
