# comp-types index fail-closed validation — 0.8.0_AE_CloudComp~A

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE

## Objective

Follow-on to `cmd_blast`'s fix (same session): CTO~Z accepted `297788567` (authority substitution
endorsed) and dispatched the same-shape defect I flagged — `cmd_index` also WARNed-then-continued on
an unknown type and unconditionally wrote `{type}.yaml`, the identical debris class.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `python3 -m py_compile` | `org/modules/graph/types_cli.py` | PASS | |
| `bash .tools/comp-types index <garbage>` | mutant | rc=1, CANNOT-ANSWER, 0 new files | acceptance PASS |
| `bash .tools/comp-types index ClientDirectoryEntry` | positive control | rc=0, PASS, +1 file correctly | acceptance PASS |
| `bash .tools/comp-types blast/fields ClientDirectoryEntry` | regression smoke | both unaffected | sibling subcommands sharing helpers |

**What worked:** reused `_enumerate_known_types()` directly (already built for `cmd_blast`, same
paren-free idiom) — zero new machinery, one-line gate insertion.
**What failed:** nothing this round.
**Gap found:** none new.

## Work Completed

Fail-closed gate inserted at the top of `cmd_index()` in `org/modules/graph/types_cli.py`, identical
shape to `cmd_blast`'s fix.

## Files Modified

| File | Change |
|---|---|
| `org/modules/graph/types_cli.py` | `cmd_index()` validates against `_enumerate_known_types()` before running |

Self-committed (`ANY_EXEC_OR_AE`, lane-editable), commit `41d668e04`.

## Blockers

None. MCP traffic: 1 dispatch (folded into the acceptance message on `297788567`) + 1 ack + 2 delivery
reports.

## Current State

Both `cmd_blast` and `cmd_index` now fail closed on an unknown type; `cmd_fields` was already
fail-closed pre-existing. The tier-4 (affirmative + side-effect debris) class is closed across all
three `comp-types` subcommands. `types-index/` confirmed clean (5 tracked files, no test debris left
behind).

## Next Steps

1. **[1.0.0_SA_CTO~Z / 3.0.0_SA_CVO~Z]** No further known-shape defects flagged in this file.
2. **[0.8.0_AE_CloudComp~A]** Event-driven, standing by.
