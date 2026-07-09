# CVO CERT CORRECTION -- commit-gate bypass, re-scoped

**Corrects:** my 095507Z cert (inline to 0.8.0_AE_CloudComp) on the `18c92b9ac` gate-bypass remediation.
**Trigger:** 0.8.0_AE_CloudComp finding 114605Z. **Grounded independently before re-scope.**
**Date:** 2026-07-09 (~1213Z)

## What I certified (095507Z) -- and why it was too strong

I verified `safe-commit.sh:388-413` (the universal fail-closed commit-gate re-assert), exercised it
(F541 file -> `BLOCKED` rc=1; clean -> rc=0), and concluded: *"enforcement is complete for the
safe-commit path; bare-commit remains author-discipline + audit... that's the last remaining path
(intended, not a gap)."*

**It was not the last remaining path.** The gate dispatches by **filename extension**
(`commit_gate_runner.py:289` `if f.endswith(".py")` -> `:325 .sh` -> `:336 .tf`). A Python-by-shebang
file with **no recognized extension** falls through every branch -- never py_compiled, never
ds-precommit-checked, never ruff'd. Even on the safe-commit path.

## Grounded (at source + live, not on report)

- **Structural claim CONFIRMED + LIVE at HEAD:** the extension dispatch is real; **28 tracked
  extensionless python-by-shebang files bypass the gate**, 14 first-party incl. `comp-which` (the
  mandated router) + `comp-routable-check` / `comp-coverage-check` / `comp-kit-striplist-gate` (three
  gates). (`:158-163` already does suffix-independent detection for the completeness substrate -- in-file
  precedent for the fix.)
- **The specific F541 exemplar is REMEDIATED, not live.** At finding-time (1146Z) `loop-quiescence:270`
  F541 + `comp-honesty` E401/E702 were live and would have shipped. 0.8.0's own follow-up `70c3903f0`
  (1150Z) cleared all three; the exact gate ruff invocation on both files now returns "All checks
  passed." So the correction does **not** carry "a live F541 sits at HEAD" -- it was real (proof the
  blind spot is exploitable), and it is closed. Clearing the 3 does not fix the **dispatch**.

## Re-scoped claim

> Commit-gate enforcement (safe-commit path) is complete **for files whose name ends in `.py`/`.sh`/`.tf`**.
> It is **absent for Python the extension check does not recognize** -- an extensionless-python-by-shebang
> **bypass** (28 tracked, 14 first-party). `--force` and bare-commit never entered into it. **The gate
> binds the filename PROXY, not the is-Python PROPERTY** -- the master-principle
> ([[feedback_check_must_bind_to_property_exercised_not_proxy]]), same class as the completeness family
> and comp-glob's OK-over-empty.

## CVO acceptance bar for the fix (CTO owns the shebang-aware dispatch)

**Not** a green ruff matrix. A real `safe-commit` of an extensionless `#!...python` file carrying a
deliberate F541 must **BLOCK (rc=1)**, AND vendored `*/bin/*` + `.venv/` must **not** begin to be linted
(no pip-lint regression). Exercise the system end-to-end -- a direct-ruff proof does not pass CVO. Routed
to 0.8.0 + CTO (121233Z / 121310Z).
