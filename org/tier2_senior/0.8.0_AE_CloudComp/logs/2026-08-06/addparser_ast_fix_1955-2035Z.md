# A blocking gate was reading prose as code — and the docstring explaining that defect got harvested as two phantom subcommands — 0.8.0_AE_CloudComp

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DIAGNOSE

**Date:** 2026-08-06
**Task Order:** ad-hoc — TASKED Andrew-direct via `1.0.0_SA_CTO~B` MCP `20260806T200157Z`. VERBATIM (Andrew, at the CTO~B terminal): *"Task 0.8.0_AE with the fix as they are live and ready with the context."*
**Status:** COMPLETE

---

## Objective

Fix the comment-blind `_ADD_PARSER` extractor I reported as Finding 2 in the prior window, exercise
it as a blocking gate deserves, measure how many of the 11 standing-drift tools were this
false-positive class, and land the Finding 1 record fix the defective gate had been refusing.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-manifest-check | `completeness` | PASS | End-to-end control. Exit 0; comp-drift no longer UNDECLARED and left the STANDING DRIFT line |
| comp-manifest-check | (auto, via safe-commit) | PASS | The gate that blocked the identical edit last window now passes it — the sequencing IS the proof |
| commit-gate.sh | `commit-gate.sh org/modules/graph/manifest_check_cli.py` | PASS | Rule 14, `.py` edit. py_compile + ds-precommit + ruff all clean |
| comp-system | `comp-system` | PASS | Two-phase discharge, `as_of HEAD=2175f3cab8` |
| comp-pulse | (auto `[risk-reflex]`) | PASS | [HOLD] on the manifest; citation read, not committed through. Denominator 1659 danger nodes |
| comp-state | `--self-test` then bare | PASS | 3/3 discriminating. Run for /exec-sum grounding, not for this fix |

**What worked:** the gate's own failure text was the diagnostic — it named the tool, the token, and
the remediation, which is what made the false premise visible rather than merely annoying. And
`comp-manifest-check completeness` passing on the same edit it refused an hour earlier is a cleaner
proof of the fix than any assertion I could write.

**What failed:** nothing new. The already-reported defect behaved exactly as characterised.

**Gap found:** none new. The one from the prior window is now closed at source.

---

## Work Completed

### 1. The fix — AST, and why not the cheaper option

`org/modules/graph/manifest_check_cli.py`: replaced

```python
_ADD_PARSER = re.compile(r"add_parser\(\s*['\"]([a-z][a-z0-9-]*)['\"]")
```

with `_add_parser_names(src)`, which walks the AST for `add_parser` Call nodes carrying a
string-literal first positional arg, keeping the identical `^[a-z][a-z0-9-]*$` token grammar.

CTO~B explicitly left the choice to me (AST vs stripping comments before matching). **I chose AST
because a docstring is not a comment.** `"""... add_parser('x') ..."""` survives a comment-strip and
reopens the identical class one layer down. Under AST both close **by construction** — a comment is
not a node at all, and a string literal is a `Constant`, not a `Call`. That is a structural
guarantee rather than a better pattern, which is the same reason the estate moved `comp-iam` to an
AST tracer (`extract_iam.py`, Rule 22a).

**No regex fallback on a parse error.** Falling back would restore the defect precisely when the
file is least trustworthy, and silently. Unparseable returns `None` -> UNKNOWN -> never blocks.
"Parsed fine, registers nothing" (`set()`) stays a **different fact** from "could not tell"
(`None`), and the caller keeps them distinct.

Recorded in the docstring as a deliberate limit rather than implied: a dynamically-built subparser
(`for n in NAMES: sub.add_parser(n)`) has no string literal to read, so neither the old regex nor
this sees it. False negative, on the branch that never blocks — the safe direction, but a limit.

### 2. The control I did not design, which became the best evidence in the commit

My first positive control asserted `AST >= regex` on the working copy. **It FAILED.** The failure
was correct and my assertion was wrong: the docstring I had just written **to explain the defect**
quotes `add_parser('reconcile')` and `add_parser('x')` as narrative examples, and the old regex
harvested both. `comp-manifest-check` is itself in `tools_index` — so under the extractor being
replaced, **this fix's own documentation would have made the gate report two phantom subcommands
for itself and block commits.** The defect propagated through prose about the defect.

Re-graded against HEAD as the clean baseline, **with the retrieval positive-controlled at 81,148
bytes** so a `fatal:` string could never be silently graded as source: regex 8, AST 8, identical.
No real detection lost.

### 3. Exercised, not just fixed

This is a BLOCKING gate on every agent's commit path; a regression wedges the fabric the way
`comp-claimlink` did this morning. Harness: `scratchpad/exercise_addparser.py`, exit 0.

| Control | Result |
|---|---|
| POSITIVE | AST == regex on clean HEAD — exactly the 8 real subparsers |
| SELF-DEMO (1b) | old regex harvests my prose as `{reconcile, x}`; AST sees only the 8 |
| NEGATIVE | `drift_cli.py`: regex `['reconcile']` -> AST `[]` (defect reproduced first, then closed) |
| MUTANT | 4 planted shapes — line comment, trailing comment, **docstring**, plain string literal. Regex harvests all 4, AST none |
| MUTANT (discriminating) | real code still yields `{'realcmd'}` — so the mutant test cannot pass by finding nothing ever |
| HONESTY | unparseable -> `None`; parseable-but-empty -> `set()`. Distinct |
| REGRESSION AUDIT | every `tools_index` engine, both directions: **51 identical, 0 ADDED, 0 engines lost to parse failure** |
| END-TO-END | `comp-manifest-check completeness` exit 0; comp-drift clean |

The regression audit was not requested. A fix that trades a false POSITIVE for a false NEGATIVE on a
blocking gate is worse than the defect, and "an engine that stops parsing" is the only route to that
— so I measured that list empty rather than reasoning that it probably was.

### 4. The measurement CTO~B asked for

Re-ran the drift computation with both extractors, everything else identical:

```
BEFORE (regex/text): 12 drifted, 29 checked, 47 unknown
AFTER  (AST/code)  : 10 drifted, 28 checked, 48 unknown
```

**Of the original 11 standing-drift tools, exactly 1 was phantom (`comp-drift`). The other 10 are
genuine.**

I am being deliberate about the 12th row: `comp-manifest-check` appears as a second phantom **only**
because of this commit's own docstring — a defect I introduced and removed in the same change. It
was never part of the standing 11, and counting it would credit my fix for my own mess.

The genuine 10, as a worklist rather than a suspect number:

| Tool | Undeclared derivations |
|---|---|
| comp-transform | all, chains, fields, stats, trace, unused |
| comp-pii | fields, routes, sweep |
| comp-routes | components, endpoints, stats |
| comp-chainrun | selfcheck, spec |
| comp-iam | investigate-candidates, investigate-candidates-self-test |
| comp-tagauthz | check, pairs |
| comp-types | blast, fields |
| comp-constants | complete |
| comp-coverage | report |
| comp-shell | list-forbidden |

**CTO~B's hypothesis does not hold, and that is the useful result.** He wrote that if most of the 11
were phantom, the STANDING DRIFT line had been training every agent to read a real signal as noise.
It had not — 10 of 11 are real, so the line has been honest and the backfill behind it is worth
doing. A measurement that discharges a worry is worth as much as one that confirms it, and it only
counts because the number landed where it did rather than where it was pointed.

One classification shift, flagged because it reads like a loss and is not: ESTABLISHABLE 29 -> 28,
UNKNOWN 47 -> 48. That is `comp-drift` moving to UNKNOWN, which is **correct** — it genuinely has no
subparsers (positional `target` + `--deep` + `--json`). It was only ever "establishable" because a
comment lied.

### 5. Finding 1 landed

`graph-call-manifest.yaml:1749` now reads `comp-pipescript`. Same one-line edit, same gate, passes
now. Ground truth unchanged from last window: `drift-topology.yaml` carries no `pipescript` engine;
seam-2's real engine is `comp-pipescript deployed` (`:85`).

---

## Decisions Made

| Decision | Rationale |
|---|---|
| AST over comment-stripping | A docstring is not a comment; stripping closes the reported case and leaves the class open one layer down. AST closes both by construction. |
| No regex fallback on parse failure | It would restore the defect exactly when the file is least trustworthy, and silently. UNKNOWN never blocks, so failing to UNKNOWN is honest and safe. |
| Keep `set()` and `None` distinct | "Registers nothing" and "could not tell" are different facts; collapsing them is how a gate reports a clean pass it never earned. |
| Re-grade the positive control against HEAD, not the working copy | The working copy contains my own new docstring. Grading against it measures my prose, not the extractor. |
| Report 1-of-11, not 2-of-12 | The second phantom is one I introduced this commit. Counting it inflates the fix with my own mess. |
| Land the fix and F1 as SEPARATE commits, in that order | The second commit landing through the same gate that refused it is the end-to-end proof; bundling them would have destroyed the demonstration. |
| Did not widen the gate | CTO~B constraint and my own prior argument: it keys on a closed set of structured fields by design. Make the scan honest, not broader. |

---

## Files Modified

See commit messages: `6cd587f54`, `2175f3cab`, `065805a03`. Rows needing extra context:

| File | Change | Committed |
|---|---|---|
| `org/modules/graph/manifest_check_cli.py` | `import ast`; `_ADD_PARSER` regex -> `_add_parser_names()` AST walker; caller distinguishes parse-failure from empty | Yes — `6cd587f54` |
| `org/modules/graph/graph-call-manifest.yaml` | `:1749` comp-drift `does:` -> `comp-pipescript` (F1, previously gate-blocked) | Yes — `2175f3cab` |
| `infra/system/06_current_state.{md,json}` | comp-system regen, `as_of HEAD=2175f3cab8` | Yes — `065805a03` |
| `scratchpad/exercise_addparser.py` | 4 controls + self-demo + regression audit; exit 0 | No — scratch, deliberately not committed |

**Lane note:** `manifest_check_cli.py` resolved to `COMPILER_MANIFEST_CHECK`, which I hold — so no
override was needed and the `.tools/**` BASE_EXEC enforcer-hold I flagged in my ACK did not apply.
I checked before writing rather than after being refused.

---

## Verification

```
CONTROL 1  -- POSITIVE (graded on HEAD, retrieval positive-controlled at 81,148 bytes)
  regex found 8: ['check','completeness','existence','list','retired-alias','routable','selfcheck','tally']
  AST   found 8: ['check','completeness','existence','list','retired-alias','routable','selfcheck','tally']
  [PASS] AST == regex on the clean HEAD file (NO real detection lost)

CONTROL 1b -- SELF-DEMONSTRATION
  regex on the post-fix file: 10 -> [... 'reconcile' ... 'x']
  AST   on the post-fix file:  8 -> (the 8 real ones)
  [PASS] the OLD regex would have harvested my prose as 2 phantom subcommands

CONTROL 2  -- NEGATIVE
  regex (the defect): ['reconcile']      AST (the fix): []

CONTROL 3  -- MUTANT   line comment / trailing comment / docstring / string literal
  regex harvests all four; AST harvests none
  [PASS] AST DOES harvest a genuine add_parser call   <- discriminating

FALSE-NEGATIVE AUDIT -- every tools_index engine, both directions
  identical under both extractors: 51 engine(s)
  REMOVED by AST (the phantoms):   2   (comp-drift, comp-manifest-check[mine])
  ADDED by AST:                    0
  ENGINE DOES NOT PARSE -> UNKNOWN: 0

VERDICT: ALL CONTROLS PASS   (exit 0)

END-TO-END
  [manifest-check] subcommand-declaration: 28 of 76 ESTABLISHABLE (48 UNKNOWN); 10 drifted, 0 in THIS commit
  [manifest-check] STANDING DRIFT: comp-chainrun(+2), comp-constants(+1), comp-coverage(+1),
                   comp-iam(+2), comp-pii(+3), comp-routes(+3), comp-shell(+1), comp-tagauthz(+2) ...
  PASS: routable + placement + self-routes + existence, over 76 registered tool(s).   [comp-drift ABSENT]
```

No Deployment Sequence table: a compiler-tool source fix with no Lambda, EC2, Terraform or S3 leg —
nothing deployed to verify. The gate run above is the behavioural evidence.

---

## Blockers

None. My deliverable is complete and nothing is waiting on me.

---

## Current State

`org/modules/graph/manifest_check_cli.py` now establishes a tool's derivation surface from the AST
(`_add_parser_names`, replacing the `_ADD_PARSER` text regex at the old `:1193`), landed
`6cd587f54`, exercised 4/4 with a regression audit showing 51 engines identical / 0 added / 0 lost
to parse failure. That unblocked `graph-call-manifest.yaml:1749`, landed `2175f3cab` — the same
one-line edit the gate refused in the prior window, now passing the same gate. Two-phase override
discharged `065805a03` (`comp-system` regen, `as_of HEAD=2175f3cab8`). Measured and reported to
`1.0.0_SA_CTO~B` (RAVC2 `20260806T202749Z`): **of the 11 standing-drift tools, 1 was phantom and 10
are genuine**, with the genuine set enumerated as a backfill worklist. Session total is 8 commits,
none pushed (lanes commit, integrators push; 5 ahead of `origin/CLOUD` including peers'). I am IDLE
and event-driven.

---

## Next Steps

1. **[1.0.0_SA_CTO~B] Route the genuine-10 subcommand backfill** — now a grounded worklist rather
   than a suspect number. `comp-transform` (6 undeclared), `comp-pii` and `comp-routes` (3 each) are
   the concentrations, and several are derivations the tool tables actively point agents at.
2. **[1.0.0_SA_CTO~B] The code residue stays open** — sharpest remains
   `.tools/portal-hooks/commit-msg`, still auto-appending `SURFACE_ACK` and self-testing against the
   portal CI workflow the retirement deleted, still installed by `install.sh:31`. Acknowledged as
   carried, no action wanted this task.
3. **[1.0.0_SA_CTO] `NFRA_GRAPHS` record drift** — surfaced from the `/exec-sum` grounding, not
   edited: status `active`, record untouched since 2026-06-16, and I struck a standing ruling inside
   its PRD this session (`26dea574e`). A close or a phase update is the owner's grounded act, not a
   status lens's.
4. **[0.8.0_AE_CloudComp]** IDLE, event-driven. 74 active TOs carry my serial; none dispatched.
   `ADHOC.comp-tool-universe-audit` remains `staged` at the unstaffed `~B` lane, holding a delivered
   named input from `0.7.0_AE_CloudOps~B`.

---

## Note on a doctrine candidate — proposed, NOT written

The shape from this window, offered to CTO~B and deliberately not landed anywhere on my own
initiative: **a defective instrument was not merely reporting noise — it was structurally preventing
the correction of a defect in the thing it guards, and the only route it offered through was to make
the guarded surface less true.** A gate you can satisfy only by lying to it converts every honest
agent into a blocked one and every fast agent into a liar. Whether that earns a doctrine line is
CTO's call; per CLAUDE.md's own editing test it would need to be actionable without retelling this
incident, and I have not attempted that extraction.
