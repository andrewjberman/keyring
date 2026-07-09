# CVO CERT -- commit-gate suffix-dispatch: re-scope + shebang-aware fix + forward-hardening (VERIFIED)

**Supersedes:** my 095507Z inline cert (on the `18c92b9ac` gate-bypass remediation), which was too strong.
**Trigger:** 0.8.0_AE_CloudComp finding 114605Z. **All claims grounded independently (source + live + exercised), not on report.**
**Date:** 2026-07-09.

## 1. The over-strong cert, corrected

My 095507Z cert concluded enforcement was "complete for the safe-commit path... bare-commit is the last
remaining path." **Wrong.** The gate dispatched on the filename **extension**
(`commit_gate_runner.py`, old `if f.endswith(".py")`), so a python-by-shebang file with no recognized
extension bypassed py_compile / ruff / the AST scan entirely -- **even on the safe-commit path**. The gate
bound the filename PROXY, not the is-Python PROPERTY ([[feedback_check_must_bind_to_property_exercised_not_proxy]]).
Re-scoped and now closed by two landed commits, both verified at committed HEAD.

## 2. Core shebang-aware dispatch (`4c99c9dd9`) -- CERTIFIED

`_is_python_source(f)`: True if `.py` (**unconditional**, before the vendored check -- so the 87 vendored
`.py` files the old predicate already gated keep their treatment; a "vendored-first" predicate would have
silently dropped them, narrowing a gate inside a commit that claims to widen it); else, for a non-`.py`
file, True iff a first-line `#!...python` shebang AND not vendored.

- **Exercised (my own):** a first-party extensionless `#!python` file with a deliberate F541 ->
  `commit_gate_runner.py` FLAGS F541, `BLOCKED`, rc=1. A clean first-party extensionless file -> passes
  (the gate refuses defects, not everything). Independently reproduced.
- **End-to-end (0.8.0, accepted):** a REAL `safe-commit` of the same -> rc=1, BLOCKED, **probe commit
  ABSENT across all refs** (property, not "HEAD unchanged" -- a shared worktree cannot distinguish a
  blocked commit from a teammate's concurrent push; the assertion was hardened accordingly).

## 3. Forward-hardening: the vendored DENYLIST -> structural predicate (`18a84f5bf`) -- CERTIFIED

CTO/0.8.0's first cut excluded vendored trees by a path-marker **denylist** (`/bin/`, `/package/`, ...) --
itself a PROXY for "we don't own this." A first-party tool at `.tools/bin/comp-future` or
`.../package/comp_future` was **silently excluded** (marker matched, ownership did not). `18a84f5bf`
replaces it: a tree is vendored iff **package-managed** -- an ancestor with `pyvenv.cfg`, an ancestor with
a `*.dist-info`, or an ancestor named `site-packages`/`node_modules`. Names gone from the logic.
**Fails-safe-toward-inclusion:** any uncertainty (unreadable dir, OSError, unknown layout) -> not-vendored
-> the file IS gated. A misconfig over-includes (loud) and can never silently exclude (invisible).

- **Grounded APPLIED (Rule 22a):** `git merge-base --is-ancestor 18a84f5bf HEAD` = YES; `HEAD:commit_gate_runner.py`
  carries `_VENDOR_DIRNAMES`/`pyvenv.cfg`/`dist-info`; working tree CLEAN (committed == running). (An
  earlier transient -- HEAD still on the denylist while the shared working tree carried 0.8.0's not-yet-merged
  edit -- was resolved by grounding, NOT relayed as a "you forgot to commit" false finding.)
- **Exercised (my own):** first-party extensionless `#!python` F541 under `.tools/bin/` -> BLOCKS (rc=1)
  = the forward-risk acceptance test PASSES (silently-excluded before). A vendored console-script under a
  real `.dist-info` tree (`.../package/bin/normalizer`) -> NOT gated ("0 file(s)") = no pip-lint regression.

## 4. Residual carried (CTO-flagged, 0.8.0-grounded, CVO-verified) -- real mechanism, live host, ZERO current effect

`_is_vendored` fails safe in every direction EXCEPT one: a **positive `*.dist-info` match inside a
first-party tree** would make that tree read as package-managed and **silently exclude** extensionless
Python beneath it. This shape exists today: `infra/aws/lambda/infrastructure_monitor/` holds first-party
handlers (`lambda_function.py`, `openai_cost_tracker.py`) alongside **16 `*.dist-info`** at the same level
-- a **CLAUDE.md Rule-3 violation** (`pip install -t .` into a source dir; the same tree the CVO SES
finding touched). **Current effect: zero** (independently confirmed): the only extensionless files there
are vendored `bin/` console-scripts (`distro`/`httpx`/`openai`/`tqdm` -- correctly excluded); no
first-party extensionless Python lives there; the first-party `.py` handlers are gated (`.py`
unconditional). **Route (not a path-proxy belt): fix the Rule-3 violation** -- vendored deps -> a Lambda
Layer -- owner 0.7.0_AE_CloudOps (per the SES sweep). Fixing it removes the residual as a side effect.

## 5. Corrections carried so the record is clean

- **No "live F541 at HEAD":** the `loop-quiescence:270` exemplar was live at finding-time (1146Z), fixed
  by 0.8.0's `70c3903f0` (1150Z). It was real (proof the bypass was exploitable), now closed. The
  **dispatch hole** was the finding; the three violations were its evidence.
- **Count is 31, not 28** (15 first-party, 16 vendored) -- 0.8.0's earlier 28 was an `os.path.isfile`
  false-negative on 217-char Windows paths (a measurement artifact, twice).
- **Meta-lesson banked:** CTO's proposed fix (a first-party root **allowlist**) was itself a path-proxy
  one level up -- every vendored tree lives UNDER a first-party root, so "roots always-included" would
  have re-included all 97 vendored files and started linting pip. **A proxy can hide inside a correction
  to a proxy; only enumerating the universe separates them.** ([[feedback_proxy_can_hide_inside_a_proxy_correction_enumerate_the_universe]])

## VERDICT

**CERTIFIED at committed HEAD.** Honest scope (verified, not relayed): *every Python edit -- by suffix OR
by shebang, first-party -- passes the gate; package-managed trees are exempt by OWNERSHIP
(`pyvenv.cfg`/`*.dist-info`/`site-packages`), not by name.* One non-fails-safe path (a `.dist-info` inside
a first-party tree) exists at `infrastructure_monitor` as a Rule-3 violation, excludes nothing today, and
is routed to its owner for fix. My prior "bypass path closed" claim is corrected; the class is now closed
in code, not carried as author-discipline.

Signed: 3.0.0_SA_CVO -- 2026-07-09
