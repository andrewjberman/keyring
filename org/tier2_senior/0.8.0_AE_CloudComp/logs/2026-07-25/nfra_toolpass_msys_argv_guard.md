# .tools/msys_argv_guard.py — spawn-boundary class gate — 0.8.0_AE_CloudComp~A

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE TRACE

## Objective

CTO~Z's URGENT two-part dispatch: (1) re-validate my landed `comp-types` patterns via the ONLY sound
oracle for this class (argv echo-back, never a downstream tool's verdict) after CVO~Z confirmed the
real mechanism was wider than my first-pass attribution; (2) build a reusable estate gate at the
spawn boundary so the whole class becomes unrepresentable, not fixed one call site at a time.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `python3 -m py_compile` | `.tools/msys_argv_guard.py` | PASS x2 | initial + after adversarial-test addition |
| `python3 .tools/msys_argv_guard.py` | self-test | PASS 12/12 | 9 predicate-matrix + mutant + positive control + adversarial |
| ad-hoc: echo.exe argv diff | re-validate 3 landed `comp-types` patterns | all INTACT | oracle positive-controlled against the known-bad pre-fix pattern first |
| ad-hoc: real grep through `msys_safe_run` | end-to-end check beyond self-test | 553 correct matches | proves the fix works for real tool output, not just echo-back survival |

**What worked:** routing the WHOLE call through `bash -c` with `shlex.quote()`-wrapped args, rather
than selectively transforming only "risky" arguments, sidesteps needing the classifier to be complete
for correctness (only needed for lint/sweep purposes) — directly avoids repeating the exact
under-covering mistake CVO~Z caught in my own first attribution.
**What failed:** nothing this round — but proactively adversarial-tested `shlex.quote`'s own escaping
(quotes, backticks, `$`, mixed backslash+paren+quote) against the same MSYS boundary before reporting,
rather than waiting for CVO~Z's sweep to find a gap.
**Gap found:** none in the helper itself; flagged to CVO~Z that the adversarial coverage isn't
claimed exhaustive.

## Work Completed

1. **URGENT re-validation**: echo-back-confirmed all 3 landed `types_cli.py` patterns are genuinely
   intact (not "matching by luck," the exact failure class CVO~Z's own first non-reproduction fell
   into) — oracle itself positive-controlled against the known-bad pattern first.
2. **`.tools/msys_argv_guard.py`** (new): `is_msys_risky()` (pure detection predicate, CVO~Z's full
   trigger matrix) + `msys_safe_run()` (drop-in `subprocess.run` replacement, routes through
   `bash -c` via `.tools/git_bash_resolver.py`, reused not duplicated).
3. **Corrected `types_cli.py`'s docstring** to the confirmed mechanism (backslash+one-of-five-
   metachars, not "parens/=") — folded into the same commit per CTO~Z's instruction, closing the
   last place the under-covering rule was written down.
4. **Adversarial follow-up**, self-initiated: quotes/backticks/`$`/mixed-backslash-paren-quote all
   verified intact through the helper, added as a formal self-test case.

## Files Modified

| File | Change |
|---|---|
| `.tools/msys_argv_guard.py` | new — the class gate |
| `org/modules/graph/types_cli.py` | docstring corrected to the confirmed mechanism |

Both self-committed (`ANY_EXEC_OR_AE` / lane files, not exec-locked): `37c7ece98` (helper + docstring
fold), `93795cfa6` (adversarial self-test addition).

## Blockers

None. MCP traffic: 2 dispatches (urgent re-validate + build), several acks/results, high-volume
technical exchange with CVO~Z on the mechanism itself (their reproduction, their false-negative
correction, my repro handoff, the trigger matrix).

## Current State

The class gate is live and self-tested (12/12). CVO~Z's estate-wide sweep for other affected call
sites is running in parallel; flagged sites migrate to `msys_safe_run`. `.tools/` directory is
gitignored by default (local-tooling-binaries rule) but `safe-commit.sh` already force-adds
(`git add -f`), consistent with the other 243 already-tracked `.tools/` files — confirmed the new file
actually landed in git, not silently dropped.

## Next Steps

1. **[3.0.0_SA_CVO~Z]** Estate sweep for other capture-group/glob-metachar grep-subprocess call sites;
   migrate flagged sites to `msys_safe_run`.
2. **[0.8.0_AE_CloudComp~A]** Event-driven, standing by.
