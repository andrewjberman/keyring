# comp-iam Stage 3: UNMAPPED-METHOD control — 0.8.0_AE_CloudComp~A

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE VALIDATE

## Objective

CVO~Z's finding #3 (surfaced during Stage 2 verify): there was no control at all for a call to a
MODELED service whose specific METHOD is absent from `_BOTO3_BY_SERVICE` -- it fell through with
zero signal, and Stage 2's own tracer win increased that exposure (every newly-found call site
that happens to hit an unmapped method became a new silent gap). CTO~Z dispatched the fix: an
UNMAPPED-METHOD sentinel + per-Lambda denominator line + a fleet-wide K-distribution census.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `python3 -m py_compile` | `extract_iam.py`, `iam_cli.py` | PASS x2 | after the sentinel additions and after the resource-accessor exclusion |
| ad-hoc synthetic mutant | `client.select_object_content(...)` (real, unmapped S3 method) | renders `UNMAPPED-METHOD`, named | acceptance (a) |
| `bash .tools/comp-iam service opal-globgrph-incremental-updater` | positive control | K=0, no METHOD-MAP line | acceptance (b) |
| ad-hoc fleet census, 157 Lambdas | K-distribution | first run: 97 across 38; after exclusion fix: 46 across 8 | acceptance (c) |
| `bash .tools/comp-iam stats/gaps` | regression | both rc=0, unaffected | acceptance (d) |

**What worked:** running the real fleet census immediately (not just the synthetic mutant) surfaced
a precision defect in my own new code before it shipped -- `boto3.resource().Table()`-style
sub-object accessors were being flagged as unmapped API methods when they make no API call at all.
**What failed:** first census (97 gaps, 38 Lambdas) would have shipped as a plausible-looking but
diluted number if I hadn't looked at what the named methods actually were.
**Gap found:** the resource-accessor exclusion itself surfaces a fourth, deeper insufficiency --
once a sub-resource object is constructed (`table = dynamodb.Table(name)`), calls made ON it
(`table.get_item(...)`) are entirely untraced. Flagged, not fixed -- explicitly out of this
stage's scope.

## Work Completed

`UNMAPPED-METHOD` sentinel Operation added at all 3 method-lookup sites in
`extract_iam.py` (2 pre-existing regex blocks + the Stage-2 AST block); `_BOTO3_RESOURCE_
SUBOBJECT_ACCESSORS` exclusion set (Table/Bucket/Object/Queue/Topic/Instance/Role/Key); per-Lambda
`METHOD-MAP COVERAGE` denominator line in `iam_cli.py`'s `cmd_service`, emitted only when K>0.

## Files Modified

| File | Change |
|---|---|
| `org/modules/graph/extract_iam.py` | UNMAPPED-METHOD sentinel x3 sites + resource-accessor exclusion |
| `org/modules/graph/iam_cli.py` | K-line display |

Self-committed (lane-editable, not exec-locked): `1eb8cec1f`.

## Blockers

None. MCP traffic: 1 dispatch, 1 ack, 2 delivery reports.

## Current State

Fleet census: 46 genuine UNMAPPED-METHOD call sites across 8 Lambdas (down from a noisy 97/38
before the self-caught precision fix), every named method a real AWS API call. Fixture stays K=0
clean. `stats`/`gaps` regression-clean. Flagged to CVO~Z: the resource-accessor exclusion list is
my own judgment call, worth independent scrutiny; the fourth insufficiency (untraced sub-resource
method calls) is named but not solved.

## Next Steps

1. **[3.0.0_SA_CVO~Z]** Verify the exclusion list is complete/correct; independently re-derive at
   least the two largest fleet K entries.
2. **[1.0.0_SA_CTO~Z]** Decide whether the fourth insufficiency (sub-resource method tracing)
   becomes its own follow-on.
3. **[0.8.0_AE_CloudComp~A]** Event-driven, standing by.
