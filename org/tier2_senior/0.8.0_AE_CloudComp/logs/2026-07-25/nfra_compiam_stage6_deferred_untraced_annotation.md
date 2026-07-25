# comp-iam Stage 6: DEFERRED/UNTRACED annotation convention — 0.8.0_AE_CloudComp~A

**archetype:** IMPLEMENT
**secondary_archetypes:** TRACE, VALIDATE

## Objective

Final stage (6th, last) of the comp-iam thread, same day. CTO~Z's dispatch, reframed by
CVO~Z's Stage-5 live measurement: an under-reporting IAM instrument does not cause
AccessDenied — it causes a future engineer doing least-privilege cleanup to delete a grant a
live construct still needs (measured: opal-data-refresh-api, comp-iam reports 0 dynamodb ops
while a correctly-scoped policy grants 6). SILENCE is the defect; a trace is a bonus. Build
one annotation convention — `DEFERRED/UNTRACED -- grant required, not observable at this
call site` — covering all four blind-spot axes rather than four more patches.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `python3 -m py_compile` | `extract_iam.py`, `iam_cli.py` | PASS x2 | |
| `bash .tools/comp-iam service opal-data-refresh-api` | site 1 fixture | `s3:PutObject` named, `[UNKNOWN]` header confirms it flows through the normal action pipeline, not just a sentinel string | positive-controlled |
| `bash .tools/comp-iam service etfs-canon-fanin` | site 2 fixture | `dynamodb:BatchWriteItem` named on `table.batch_writer` | |
| `bash .tools/comp-iam service infrastructure_monitor` | site 4 fixture | 4 distinct services (lambda/s3/sns/ec2) all correctly named via the paginator/waiter-name lookup | |
| `bash .tools/comp-iam service opal-data-refresh-api` | site 4 clean case | paginator `get_paginator('list_objects_v2')` annotation correctly SUPPRESSED — the same file also calls `s3_client.list_objects_v2()` directly at 2 other line numbers | REAL fixture, not synthetic — proves acceptance (c) |
| ad-hoc synthetic fixture | site 3 (UNRESOLVED-CLIENT/RESOURCE, all 4 shapes) + mutant | all 4 unified with the shared wording; mutant (`totally_fake_ec2_method_xyz`) still renders UNMAPPED-METHOD, unaffected — confirms site 3 and the pre-existing Stage-3 control are correctly kept as separate classes | |
| ad-hoc fleet census, 157 Lambdas | count of Lambdas carrying >=1 DEFERRED/UNTRACED row | 22 of 157, 50 total rows | the estate's first exposure number for the deletion hazard |
| ad-hoc fleet superset diff | Stage 6 vs Stage-5-committed (`65876f746`) baseline | 22/157 increased (exactly matches the census), 0 regressions, SUPERSET HOLDS | |
| ad-hoc negative control | `bd-client-detail` | byte-identical, unaffected | |
| `bash .tools/comp-iam service opal-globgrph-incremental-updater` | regression | 7/7 unchanged | |
| `bash .tools/comp-iam stats/gaps/roles` | regression | clean; `gaps` missing-count unchanged at 22, deny-present count rose 233->292 (expected — more real, named actions now exist to compare against deny statements) | |

**What worked:** grounding every resolvable action through the SAME `_BOTO3_BY_SERVICE`
lookup already built by Stages 1-5 (paginator names ARE client method names for every
service in this estate's usage), rather than inventing a parallel action table.
**What failed/found:** wiring the resolver into the Stage-2 AST helper-direct-chained block
surfaced a REAL pre-existing defect: that block's `if X and Y: ... elif not-Z:` condition
collapsed "known-mapped-but-null" and "genuinely-unmapped" into one path, so a
`get_paginator`/`batch_writer`/etc. reached via a direct-chained helper call was mislabeled
UNMAPPED-METHOD instead of staying silent (pre-Stage-6) or getting DEFERRED (now). Fixed to
the same 3-way split the regex sites already used correctly. Disclosed, not hidden — a defect
found while building the feature that needed the correct 3-way split to route through it.
**Gap found:** none new; this stage's job was disclosure, not further tracing.

## Work Completed

Added `_deferred_implication()` to `extract_iam.py`: a closed resolver (NOT a general
mapper) for exactly the 4 verified-null methods CTO~Z's dispatch named. Wired into all 4
method-lookup call sites (2 regex per-line blocks, the Stage-2 AST helper direct-chained
block, the Stage-5 AST resource direct-chained block) via a consistent 3-way
`if method in action_map: (real op) / (deferred) elif unmapped` structure — fixing the one
site that had it wrong. Site 4's conditional emission resolves in a post-pass at the end of
`_scan_python_for_operations`, after the full per-file operation list exists, checking
whether the candidate's implied action is already independently visible elsewhere in the
same file. Added 3 grounded mappings (`cloudtrail.lookup_events`, `iam.list_roles`,
`sns.list_topics`) so the paginator-name lookup resolves for every real used call site.
Unified UNRESOLVED-CLIENT/UNRESOLVED-RESOURCE wording at all 4 existing emission sites.
Added the doc line to `iam_cli.py`'s own `comp-iam service` output.

## Files Modified

| File | Change |
|---|---|
| `org/modules/graph/extract_iam.py` | `_deferred_implication`, `_ast_call_args_text` (new); `_EC2_WAITER_UNDERLYING_METHOD`, `_DEFERRED_UNTRACED` (new constants); 4 method-lookup call sites restructured/wired; 3 new grounded action-map entries; UNRESOLVED-CLIENT/RESOURCE wording unified at 4 sites; post-pass added to `_scan_python_for_operations` |
| `org/modules/graph/iam_cli.py` | doc line: operation list is a FLOOR, never a deletion warrant |

Self-committed: `b6745914d`.

## Blockers

None. MCP traffic: 1 dispatch (Stage 6), plus the prior Stage-5 ACK read in full before
starting.

## Current State

The full comp-iam thread (Stages 1-6, all same day) is closed pending CVO~Z's Stage-6 verify.
All 5 acceptance criteria confirmed with evidence, all on REAL estate fixtures where possible
(synthetic only for site 3, since no real fixture in the estate currently has an unresolvable
helper/resource binding):
(a) all 4 sites render on real fixtures, verified at output;
(b) presigned-url/batch_writer name the implied grant explicitly;
(c) the clean-suppression case (already-visible paginator target) proven on a real fixture
    (`opal-data-refresh-api`), not constructed;
(d) fleet census: 22/157 Lambdas, 50 rows — the estate's first deletion-hazard exposure
    count; fleet superset diff confirms 0 regressions;
(e) 7/7 + stats/gaps/roles regression holds.

One real pre-existing defect found and fixed while building this stage (the Stage-2
collapsed-condition mislabeling), disclosed above, not folded silently into the Stage-6 diff.

## Next Steps

1. **[3.0.0_SA_CVO~Z]** Verify Stage 6 (FULL, per its own instance/bar) — specifically
   whether the annotation reads as actionable to a human doing cleanup, per its own stated
   check, and independently re-derive the 3 new grounded action-map entries.
2. **[1.0.0_SA_CTO~Z]** Fold Stage 6's closure into the durable record once CVO~Z's verify
   lands — this closes the full 6-stage comp-iam thread.
3. **[0.8.0_AE_CloudComp~A]** Event-driven, standing by.
