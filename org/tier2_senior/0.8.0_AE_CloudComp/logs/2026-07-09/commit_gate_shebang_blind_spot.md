# The universal commit-gate keyed on the .py EXTENSION, not on "is this Python"

**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT, VALIDATE

**Agent:** 0.8.0_AE_CloudComp
**Date:** 2026-07-09
**Window:** 11:40Z -> 12:15Z (continues `completeness_gate_family_and_selector_hardening.md`)

---

## Summary

Refused to design a CTO-approved follow-on because its premise was unexercised. Falsifying it -- and
then falsifying my own replacement hypothesis -- surfaced a real defect in the gate every commit in
the fabric passes through. Landed `4c99c9dd9` after clearing the debt it would otherwise have blocked
on (`70c3903f0`).

---

## How it was found (the method is the point)

CTO GO'd a consolidated "sanctioned path for add / delete / force-add-ignored" staging pass, on the
reading that COO~B and I had found the **same root twice**: *the wrapper's staging assumes files
present-and-not-ignored.*

1. **Grounded COO~B's half before designing around it. It did not reproduce.**
   `safe-commit.sh:271` already does `git add -f -- "${PATHSPEC[@]}"`, comment and all. Probe: a
   `check-ignore`-confirmed ignored file **stages** under `git add -f`. No staging gap.
2. **My own leading hypothesis also did not reproduce.** I guessed one of the 16 force-added tools is
   Python (`comp-honesty`) and had failed `commit-gate` fail-closed. Ran `commit-gate.sh` over all
   sixteen: **rc=0, "clean for 16 file(s)"**.
3. **Chasing WHY it didn't reproduce gave the answer.** The gate returned clean because **every one of
   the 16 is extensionless**, so the suffix dispatch never routes them to `py_compile`/`ruff` at all.
   `comp-honesty` has a `#!/usr/bin/env python3` shebang and no `.py`. The gate never looks at it.

COO~B then reconstructed the true cause of their failure from task logs -- a **concurrent
`index.lock`**, not a wrapper limitation -- and withdrew the finding. CTO withdrew the GO, noting his
premise had been `INFERRED`, not established, and that under his own Rule 22 an inferred causal claim
cannot authorise a critical-surface change.

**A wrong hypothesis, properly executed, found the bug.**

---

## The defect

`commit_gate_runner.py` dispatched on `f.endswith(".py")` -- the **filename** (a proxy) -- for
**"this file is Python"** (the property). Python-by-shebang scripts without a `.py` suffix were never
compiled, never linted, never AST/silver-id scanned.

**Blast radius, grounded (prove-the-universe):** 28 tracked extensionless python-by-shebang files
bypassed the gate. **15 are first-party**, including:

- **`.tools/comp-which`** -- the router CLAUDE.md Rule 21 makes the default for every search
- **three GATES**: `comp-routable-check`, `comp-coverage-check`, `comp-kit-striplist-gate`
- comp-glob, comp-grep, comp-fedobs, comp-freshness, comp-heat, comp-honesty, comp-dups,
  comp-secrets, check-lambda-layer-deps, loop-quiescence

The rest are vendored venv / lambda console-scripts, correctly excluded.

**Not theoretical.** The gate's own ruff over the first-party set found:
```
  .tools/comp-honesty:5:1     E401  multiple imports on one line
  .tools/comp-honesty:9:71    E702  multiple statements on one line
  .tools/loop-quiescence:270  F541  f-string without any placeholders
```
`loop-quiescence:270` is **F541 -- the exact rule of `18c92b9ac`**, the audited gate-bypass whose
remediation CVO had certified as *"the bypass path is closed + bites."* That cert was `.py`-scoped and
false for precisely the class where the rule recurred and sat live at HEAD. CTO and CVO both owned the
re-scope; CVO re-scoped its cert.

Every edit I made to `comp-which` and `comp-routable-check` tonight passed through **no** py_compile,
**no** ruff, **no** ds-precommit. I ran `py_compile` by hand each time out of habit.
**Habit is not a gate.**

---

## The fix (`70c3903f0` then `4c99c9dd9`)

**Sequence (CTO condition 1):** clear the debt first, or the widened gate lands RED and blocks every
agent on debt none of them created. `70c3903f0` fixed all three.

Equivalence bound to the **semantic** property, because **AST-identity is the wrong invariant here** --
removing an f-prefix turns `JoinedStr` into `Constant`; splitting an import changes node count. Both
differ *by construction*, which is the point of the fix. So: the f-string had no placeholders ->
evaluated **value identical**; comp-honesty's **import bindings + call sequence identical**; both tools
**exercised** (`comp-honesty --self-test` 9/9).

**`_is_python_source(f)`**: `.py` -> True **unconditionally**; else a non-`.py` file with a first-line
`#!...python` shebang, with vendored trees excluded.

### I nearly shipped the opposite of what the commit claimed

My first cut tested `_is_vendored()` **before** the `.py` check. Measured coverage: the gate saw
**4769** `.py` files before and **4697** after -- my "widening" silently removed **87 vendored `.py`
files** from enforcement that `endswith(".py")` had always gated. A commit whose message said *widen*
while the diff *narrowed*.

Caught only by measuring the before/after **set**, not by trusting the direction of my own change.
Fixed: `.py` returns True unconditionally, before `_is_vendored` is consulted; the exclusion guards
only the new shebang path, where the danger lives (vendored console-scripts are extensionless).
**0 `.py` lost, 15 gained -- a strict superset.**

*(Second measurement artifact, corrected rather than reported: a follow-up count showed "6 lost."
Those are `.py` files under `org/threads/.../refs/` with 217-character paths that `os.path.isfile`
cannot see on Windows. The predicate returns True for all 4769; my measurement's `isfile` pre-filter
was the liar.)*

---

## Verification (8/8 at the LANDED HEAD, gate from committed code)

| case | result |
|---|---|
| INCLUDE: first-party extensionless python + deliberate F541 | **BLOCKS**, ruff names it |
| EXCLUDE: **vendored** python-shebang + the SAME F541 | does **not** block (pip stays safe) |
| control: clean first-party extensionless python | passes |
| `comp-which` / `comp-routable-check` (now gated) | pass |
| unrelated `.py` / deleted `.py` | unchanged |
| **REAL `safe-commit`** of an extensionless F541 file | rc=1, BLOCKED, unstaged, **probe commit ABSENT across all refs** |

CTO's condition 2 required the vendored boundary exercised from **both** sides -- a one-sided test
leaves the catastrophic side ("the gate starts linting pip") unproven. Acceptance asserted on
**probe-commit-absence**, never "HEAD unchanged": that assertion is invalid in a shared worktree, as
base COO's concurrent push proved earlier today.

---

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| commit-gate / safe-commit | 8/8 | the subject; now shebang-aware, strictly additive |
| ruff (py39, the gate's own pin) | 3 violations found, cleared | the blind spot's live proof |
| comp-honesty | self-test 9/9 | exercised to prove the lint fix was behaviour-preserving |
| comp-which-routing-test / comp-routable-check | PASS 42/42 / PASS | no regression from the widening |

**What worked:** grounding a handed premise instead of designing on it. Both instances of the
"same root twice" pattern evaporated, and the chase produced a real defect neither of us had seen.

**What failed:** my own diff, silently narrowing a gate it advertised as widening -- caught by
measuring, not by reading.

**Gap found:** CLAUDE.md Rule 14 says *"every `.py` edit passes commit-gate."* The intent is *every
Python edit*; the words describe the proxy the gate used to bind. Amendment is CTO's/Andrew's lane.

---

## Blockers

**None.**

## Current State

- Universal commit-gate is shebang-aware at HEAD. `comp-which` + three gates are inside the
  enforcement they embody. Strict superset: 0 `.py` lost, 15 first-party files newly covered.
- Triangle: CTO arch-gate DONE (source-grounded), CVO cert + `18c92b9ac` re-scope DONE, COO~B accept
  routed.
- The "consolidated staging pass" is **dead**: force-add premise falsified (index.lock), deletion case
  real and landed (`2910bfabc`).

## Next Steps

1. **[1.0.0_SA_CTO / Andrew]** Rule 14 wording: *"every `.py` edit"* -> *"every Python edit."* The gate
   now matches the intent; the rule still describes the proxy.
2. **[1.0.0_SA_CTO]** heldout tier (p@1 50% / recall@surf 70%) -- the selector's real gap. Curated
   vocabulary is saturated; it is a COMPROUTE-posterior investment. COO~B holds it as the next lever.
3. **[me, on GO]** nothing outstanding.
