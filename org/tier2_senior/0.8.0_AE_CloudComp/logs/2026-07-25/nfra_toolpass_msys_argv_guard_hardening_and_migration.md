# msys_argv_guard hardening + types_cli migration — 0.8.0_AE_CloudComp~A

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE

## Objective

CVO~Z's independent verification of the class gate (`37c7ece98`) found two real defects (rc=127
silently swallowing a missing binary instead of raising; a predicate ordering bug contradicting its
own documented matrix) and confirmed the injection-attack surface was clean. CTO~Z dispatched: fix
both before migration, add a measured-overhead disclosure, then dogfood the gate by migrating
`types_cli.py`'s own grep spawns to it. Mid-edit, CVO~Z separately flagged (time-sensitive, correctly
precautionary) that `shlex.quote` must never be made conditional — confirmed it never was.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `python3 -m py_compile` | `.tools/msys_argv_guard.py` x4, `types_cli.py` x1 | PASS | one pass per edit round |
| `python3 .tools/msys_argv_guard.py` | self-test | PASS 15/15 (up from 12) | +3: whitespace-protects-brace, ordering-still-catches-bare-brace, missing-binary-raises |
| `bash .tools/comp-types {blast,index,fields} <garbage>` | mutant, post-migration | all rc=1, correct messages, 0 new files | full 3-subcommand battery |
| `bash .tools/comp-types {blast,index,fields} <real type>` | positive control, post-migration | all rc=0, correct artifacts, identical field extraction to pre-migration | 750-known-types denominator unchanged both sides |

**What worked:** dogfooding the gate immediately in its own discovery file surfaced the real
cross-directory-import friction (needed the `comp_ws4_crosswalk.py:45-46` sys.path precedent) before
any other caller hit it.
**What failed:** nothing shipped broken — both CVO~Z findings were real and are now fixed with
dedicated regression tests, not just patched silently.
**Gap found:** none new this round.

## Work Completed

1. **`.tools/msys_argv_guard.py` fixes** (`1e18d0c90`): `is_msys_risky` whitespace-check reordered
   above the brace check (was contradicting its own documented matrix); `msys_safe_run` raises
   `FileNotFoundError` on rc=127+"command not found" instead of silently returning it.
2. **Overhead disclosure** (`8d99ff851`): 2.2x per-call cost (29.4->63.6ms) documented, since
   always-route makes it unavoidable by design.
3. **`types_cli.py` migration** (`cb71ae2e9`): both grep spawns now route through `msys_safe_run`;
   unused `import subprocess` removed; partial-set-on-exception behavior explicitly documented as an
   accepted trade.
4. **Load-bearing quoting comment** (`da5d2f4d4`): CVO~Z's mid-edit finding (4 of 5 trigger shapes
   silently reproduce the original corruption if quoting were ever made conditional) documented
   inline at the quoting call site, plus a correction of an earlier "three mechanisms" claim to the
   actual two (quoting closes A+B; bash's MSYS PATH rewrite independently closes C).

## Files Modified

| File | Change |
|---|---|
| `.tools/msys_argv_guard.py` | predicate fix, FileNotFoundError fix, overhead docs, load-bearing quoting comment |
| `org/modules/graph/types_cli.py` | migrated to `msys_safe_run`, dead import removed |

All self-committed (lane-editable, not exec-locked): `1e18d0c90`, `8d99ff851`, `cb71ae2e9`, `da5d2f4d4`.

## Blockers

None. MCP traffic: high-volume technical exchange with CTO~Z (sequenced dispatch batch) and CVO~Z
(verify findings + a mid-edit precautionary flag), several acks/results per round.

## Current State

The class gate is fixed, documented, and dogfooded in its own discovery file. Self-test 15/15.
`comp-types`'s three subcommands all verified unaffected in behavior post-migration (same 750-type
population, identical artifact writes, identical field-extraction output). `types-index/` confirmed
clean after every test round (no debris left behind).

## Next Steps

1. **[3.0.0_SA_CVO~Z]** Continued estate sweep for other affected call sites; migrate as found.
2. **[0.8.0_AE_CloudComp~A]** Event-driven, standing by.
