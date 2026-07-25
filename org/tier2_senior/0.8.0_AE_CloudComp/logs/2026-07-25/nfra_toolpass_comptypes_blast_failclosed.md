# comp-types blast fail-closed validation — 0.8.0_AE_CloudComp~A

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE VALIDATE

## Objective

CTO~Z dispatched a banked follow-on from the tool-behavior sweep: `comp-types blast <garbage>` was the
worst single behavior found (tier-4: affirmative rc=0/PASS + a side-effect manifest write into
`types-index/`, the debris class CVO~Z quarantined 19 files of today). Fix: validate the type before
running, fail closed on unknown, keep known-type behavior unchanged, print the validation denominator.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `python3 -m py_compile` | `org/modules/graph/types_cli.py` | PASS x2 | initial + after the mangling fix |
| `bash .tools/comp-types blast <garbage>` | mutant, before fix | rc=0, PASS, debris written | reproduced the reported bug |
| `bash .tools/comp-types blast ClientDirectoryEntry` | first fix attempt, real type | FALSELY REJECTED ("0 known types") | caught before reporting -- capture-group grep mangling |
| ad-hoc python subprocess bisection | isolating the MSYS mangling trigger | root cause found: capture groups / bare `=` | character-by-character isolation |
| `bash .tools/comp-types blast <garbage>` | mutant, after fix | rc=1, CANNOT-ANSWER, 0 new files | acceptance PASS |
| `bash .tools/comp-types blast ClientDirectoryEntry` | positive control, after fix | rc=0, PASS, +1 file correctly | acceptance PASS |
| `bash .tools/comp-types index ClientDirectoryEntry` | regression smoke test | unaffected | untouched code path |

**What worked:** reusing `_find_type_definition()`'s established pattern (already gating `cmd_fields`)
instead of inventing new validation machinery; generalizing it to an enumeration gave the acceptance-
mandated denominator for free.
**What failed:** the first implementation (capture-group regexes matching `_find_type_definition`'s own
style) silently rejected a REAL type as unknown when exercised live -- would have been a worse
regression than the original bug. Not shipped.
**Gap found:** a third instance of this box's MSYS-linked-binary argv-mangling class (grep.exe spawned
from native Windows Python silently mangles capture-group/`=` pattern args, rc=1/empty/no-stderr,
indistinguishable from a real empty result) -- flagged to CVO~Z as possibly affecting other
grep-via-subprocess call sites in `org/modules/graph/*.py`, not swept further this pass (out of scope).

## Work Completed

`_enumerate_known_types()` (new) + `cmd_blast()` fail-closed guard in
`org/modules/graph/types_cli.py`. Memo at
`org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/NFRA_TOOLPASS_COMPTYPES_BLAST_FAILCLOSED_20260725.md`.

## Files Modified

| File | Change |
|---|---|
| `org/modules/graph/types_cli.py` | new `_enumerate_known_types()`; `cmd_blast()` validates before running |
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/NFRA_TOOLPASS_COMPTYPES_BLAST_FAILCLOSED_20260725.md` | new memo |

`types_cli.py` is `ANY_EXEC_OR_AE` (lane-editable per `.owned-paths.yaml:1023`) -- **self-committed**,
commit `297788567`. The memo lives in CTO~Z's census directory, left on disk per the session's
established convention (not self-committed).

## Blockers

None. MCP traffic: 1 dispatch in, 1 ack, 2 delivery reports.

## Current State

Fix committed (`297788567`), both acceptance legs verified live (mutant + positive control, separate
invocations, in-stdout TRUE_RC), `types-index/` confirmed back to its pre-test 5-tracked-file clean
state (test artifacts deleted after verification). `cmd_index`'s same-shape unconditional-write defect
flagged, not fixed (scope discipline).

## Next Steps

1. **[1.0.0_SA_CTO~Z]** Decide whether `cmd_index`'s same-shape defect becomes its own follow-on.
2. **[3.0.0_SA_CVO~Z]** Decide whether to sweep other `org/modules/graph/*.py` grep-subprocess call
   sites for the same capture-group/`=` mangling class.
3. **[0.8.0_AE_CloudComp~A]** Event-driven, standing by.
