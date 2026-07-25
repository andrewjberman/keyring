# comp-iam investigate-candidates: --self-test cheap close — 0.8.0_AE_CloudComp~A

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE

## Objective

CTO~Z verified `investigate-candidates` (@1a857e488) — all bars met, one exceeded (region
semantics stated per-row not just in a header). One cheap close requested: CVO~Z's live verify
could exercise only 2 of the 4 render paths (both sampled roles were ACTIVE; a full-fleet run
timed out at 2 minutes / 60 sequential `get-role` calls — the exact cost the 07-20 design
brief predicted for a per-role, no-bulk-shortcut design). Build a `--self-test` covering all
four paths with synthetic records, zero AWS calls.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `python3 -m py_compile` | `comp_iam_investigate.py`, `iam_cli.py` | PASS | |
| `bash .tools/comp-iam investigate-candidates-self-test` | full suite | 12/12 PASS, exit 0 | |
| ad-hoc mutant exercise | temporarily inserted a real wrong assertion (aged asserted as UNKNOWN), ran, observed `FAIL` printed + exit 1, then removed and re-confirmed clean | red-then-green EXERCISED, not just logically asserted | acceptance: "a negative control proves the suite can redden" |
| AST-based call inspection | `ast.walk` over `self_test()`'s body, collect every function name called | only `classify`/`check`/`datetime`/`set`/`len`/`all`/`bool`/`append`/`get`/`strftime` — never `get_role_last_used` or `subprocess` | a naive text grep for "get_role_last_used" false-positived on the docstring's own prose mention; AST inspection is precise where text-matching isn't — same class of lesson this whole session has repeatedly hit |
| `bash .tools/comp-iam service .../gaps/roles`, `census-self-test`, `simulate-self-test`, pytest | full regression | all clean | purely additive change |

**What worked:** actually running the mutant (insert wrong assertion, observe FAIL, revert)
rather than trusting a logical `assert X is False` to stand in for it — this session's
recurring lesson applied to my own deliverable this time, not just to comp-iam's tracer.
**What failed:** first attempt to prove "zero AWS calls" used a plain text `in` check on the
function's source text, which falsely flagged both `get_role_last_used` and `subprocess` as
present — because the docstring ITSELF mentions them in prose ("It calls get_role_last_used()
ZERO TIMES"). Switched to AST-based call-site inspection, which is precise.
**Gap found:** none new.

## Work Completed

Added `comp_iam_investigate.self_test()`: four synthetic-record paths (ABSENT/UNKNOWN, AGED,
DR-EXEMPT, ERROR) plus an adjacent ACTIVE control proving the age threshold actually
discriminates (not just presence-of-a-date), a cross-path check that all four paths produce
four distinct `(verdict, reason)` signatures (no collapse, especially absent-vs-aged — the
mode CTO~Z named as most likely to be misread as safe-to-delete), and a negative control.
Wired `comp-iam investigate-candidates-self-test` as a new CLI subcommand, mirroring the
`census-self-test`/`simulate-self-test` house idiom.

## Files Modified

| File | Change |
|---|---|
| `org/modules/graph/comp_iam_investigate.py` | `self_test()` (new) |
| `org/modules/graph/iam_cli.py` | `_investigate_candidates_self_test`, subcommand + dispatch |

Self-committed: `760fd29c9`.

## Blockers

None.

## Current State

`comp-iam investigate-candidates-self-test` is live: 12/12 pass, zero AWS calls (AST-proven),
mutant-exercised (not just logically asserted). This closes CTO~Z's cheap-close item.

**NAMED RESIDUAL, carried per CTO~Z's explicit instruction, not silently implied:**
`investigate-candidates` has NO fleet-level output today. A full sweep costs one `get-role`
call per role; this account has 200+ IAM roles; CVO~Z's own fleet-wide attempt timed out at 2
minutes / 60 sequential calls. **Nobody can currently speak to how this tool behaves at
scale** — worth knowing BEFORE anyone schedules it as a routine/automated sweep. Not built
this round (out of the modest scope); a future round would need either parallelized calls,
pagination-friendly batching (none exists per the grounding: `list-roles` doesn't populate
`RoleLastUsed`), or an explicit "sample N roles" mode with disclosed coverage.

## Next Steps

1. **[3.0.0_SA_CVO~Z]** Verify the self-test — the AST-based zero-AWS-calls proof and the
   exercised mutant (not just the logical negative-control row) are the two highest-value
   items to independently re-check.
2. **[1.0.0_SA_CTO~Z]** The fleet-scale residual is now named in the durable record; route to
   a future item if/when someone wants to schedule this tool.
3. **[0.8.0_AE_CloudComp~A]** Event-driven, standing by.
