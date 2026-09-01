# CVO FORK-1 ADMISSIBILITY MEASUREMENT: the eight step-5 lenses, measured before admission

**Discharges the AT-SELF gate carried in `handoffs/2026-09-01_1905Z.md`:** *"per-tool compilation
measurement for fork 1's admissibility gate -- MUST PRECEDE admission."* Until this file, the
battery in `CVO_ADJUDICATION_CANONICAL_WORKFLOW_FORKS_20260901.md` was **proposed on two measured
tools and six assumed ones.**

**THE GATE BEING APPLIED (fork 1, Andrew-agreed):** a lens is admissible to the canonical step-5
battery only if it **EITHER compiles its corpus at runtime OR prints its corpus vintage** -- and the
`<preflight>` record captures which.

**INSTRUMENTS, and they are deliberately two:** (1) SOURCE read of the resolved implementation file;
(2) LIVE EXERCISE of the tool, reading what it actually prints. **The exercise plane is the
authority here**, because the gate's predicate is about PRINTED OUTPUT, and a docstring is the
artifact describing itself. That split earned its cost twice below.

⛔ **RESOLUTION NOTE:** every tool was resolved by READING ITS SHIM, not by name. The previous
attempt at this measurement (2026-09-01, earlier session) mis-resolved `comp-similar` to
`comp_trigger.py` and its numbers were discarded unreported.

---

## 1 · THE RESULT

| lens | corpus | RUNTIME? | VINTAGE PRINTED? | VERDICT |
|---|---|---|---|---|
| `comp-blast` | kuzu, 27,107 nodes + worktree overlay | overlay HEAD-pinned | **YES** -- `built:` + age + Nessie snapshot ids + per-table cadence | **ADMIT** |
| `comp-dataflow` | parsed producer `.py` at working-tree HEAD | **YES** | **YES** -- explicit `VINTAGE:` line | **ADMIT** |
| `comp-schedule` | 5 gate carriers, compiled at read time | **YES** -- "VIEW-TIME COMPILED; no artifact" | n/a (nothing to age) | **ADMIT** |
| `comp-iam` | 395 `.tf` files across 3 trees | **YES** | plane + denominator + holes | **ADMIT** (bounded, s.3) |
| `comp-trigger` | live EventBridge/Scheduler API | **YES** | denominator + region | **ADMIT** |
| `comp-pipescript` | `ast.parse` x4 + `glob`/`os.walk` x10 | **YES** (measured 09-01) | refuses without `--pipeline` | **ADMIT** |
| `comp-denytest` | live `simulate-principal-policy` | **YES** (no corpus) | n/a | **ADMIT** |
| `comp-similar` | kuzu corpus + heat | **NO** | **NO -- neither text NOR `--json`** | ⛔ **REFUSE** |

>> **SEVEN ADMITTED, ONE REFUSED.** The battery is admissible with `comp-similar` withheld. <<

---

## 2 · THE ONE REFUSAL -- `comp-similar`

**MEASURED ON BOTH CARRIERS.** Text path: a bare `summary-similar peers of bd-49f-runner:` header
and 40 rows. `--json` path: top-level keys are exactly `['arn', 'neighbors']`.

```
  vintage / built / snapshot / provenance / as_of / corpus / denominator keys : NONE
  neighbors returned : 40   out of an UNSTATED corpus
```

⛔ **It reads the SAME kuzu corpus `comp-blast` reads, and `comp-blast` prints a full provenance
header over it.** So this is not a missing capability in the family -- it is one tool not emitting a
header its sibling already emits over the identical DB. **The remedy is small and it is not mine to
apply** (`0.8.0_AE_CloudComp` owns the comp-tool surface).

⭐ **Its `--self-test` is 7/7 with genuinely discriminating controls** (C1 false-twin, C3 blind-row,
C5 hold-aware). **The tool is not weak. It is undisclosed** -- and under a gate about disclosure that
is the whole question. Its BUILD-LADDER rung-2 role (rung 2 = "the estate already has it") is real
and I want it back the moment it carries a header.

---

## 3 · TWO CORRECTIONS TO MY OWN FORK-1 DOC -- both were inherited, neither was measured

**(a) "the dependency graph EXPLICITLY CACHED ... any lens reading it enters as CACHED and must print
the provenance vintage."** ⛔ **FALSE FOR THE TOOL I BUILT IT AROUND.** `comp-blast` does not read the
dependency graph at all. `cli.py:812`: *"the main path's universe is kuzu"*. Its own NOT-FOUND banner:
*"The old private trace universe (2,255 nodes, 4 S3 buckets) is retired."* And it **already prints a
richer vintage than my gate demands** -- `built: 2026-09-01T16:18:23Z (age: 1.2h)`, both Nessie
snapshot ids, per-table cadence, plus the caveat *"'last-write' is the TABLE's write time, NOT the age
of the data in it."* **I derived "cached" from Rule 20's prose about a DIFFERENT artifact and never
opened the tool.**

**(b) "`comp-iam` population is LAMBDA ENTRY POINTS ONLY -- the EC2/SSM chain is invisible."**
⛔ **NOT WHAT THE TOOL REPORTS:** `Lambda services: 166, EC2 services: 21`. The real, self-declared
holes are different and worse-shaped:
```
  policy blocks NOT ATTACHED : 24   "statements comp-iam has NEVER SEEN"
  deny statements unparsed   :  2   for_each -- `role = each.value` unresolved
```
>> **"comp-iam CANNOT answer 'is this denied?'. Among these are NEVER#1's cross-firm Deny belts.
Asking this tool about a Deny it never parsed returns SILENCE, and silence must not be read as
allowed."** -- the tool's own banner. <<
**That is the bound a decomp must carry, and it is not the one I wrote down.**

⚠ **Both corrections have the same shape as the class I bank against: a claim inherited from prose
and re-emitted as measured.** I wrote the battery table from tool DESCRIPTIONS during the 106-tool
scan and carried it into an Andrew-agreed adjudication without opening two of the eight.

---

## 4 · THE GATE ITSELF NEEDS A THIRD LIMB

**The two-limb gate (runtime OR vintage) passes all eight tools except one -- and it is NOT what
separated the good lenses from the weak ones in practice.** What actually distinguished them:

```
  comp-dataflow  COVERAGE: ... | BLIND: ... | VINTAGE: ... | DENOMINATOR: 2 reads scanned,
                 2 unresolved-dynamic (blind), 0 served-origin flagged
  comp-iam       plane + 395-file denominator + 24 never-seen blocks + the deny-silence warning
  comp-schedule  per-carrier denominator AND decidability, and "last-verified [DERIVED from the
                 carrier's last EDIT -- a WEAK proxy: it dates the edit, NOT a human confirming]"
  comp-blast     refuses AMBIGUOUS-SUBJECT rather than guessing; on NOT-FOUND prints the
                 denominator "so typo and out-of-scope stop looking identical"
```

>> **RECOMMENDED THIRD LIMB (at Andrew): a lens is admissible only if it prints a DENOMINATOR or an
explicit BLIND/COVERAGE statement with its answer.** A vintage tells you how old the corpus is. It
does not tell you the lens was blind on your specific subject -- and that is the failure a decomp
actually eats. <<

⭐ **Live specimen from this measurement.** `comp-dataflow origin perfrp_emit_core.py` -- the file at
the centre of today's incident -- returned `2 reads scanned, 2 unresolved-dynamic (blind)`. **A lens
that printed only a vintage would have returned two rows and looked like an answer. The denominator
is what says "this lens saw nothing here."**

**COST of the third limb:** it disqualifies nothing in the current battery (all seven admitted
already satisfy it); it is one more `<preflight>` field. **NON-APPLICATION:** a lens whose output is
a single boolean over a named subject (`comp-denytest`) has no population and owes no denominator.

---

## 5 · CARRIED, NOT CHASED

- ⚠ **`comp-similar` provenance header** -> `0.8.0_AE_CloudComp`. Blocks its admission, nothing else.
- ⚠ **`_emit_trace_provenance` docstring says "printed on EVERY walk"; it has ONE caller** (`cli.py:357`,
  `cmd_trace`). Harmless today -- `comp-trace` is the only consumer and it DOES print. **Recorded because
  it is the declarative-drift class**, same as the `/watcher` doc that was false for six weeks.
- ⚠ **The trace graph's drift check cannot see a NEW file.** `check_node_freshness` iterates
  `graph.nodes.values()` -- an unindexed file has no node, so no drift, so the cache is served.
  **MEASURED INCIDENCE TODAY: 1 file**, and currently **MASKED** (drift=34 forces a rebuild anyway).
  Structural, low-frequency, silent. Scoped to `comp-trace`; `comp-blast` left this universe.
- ⚠ **A memory entry may be wrong.** `comptool_gap_comp_iam_reconcile_census_stale_06_03.md` records
  `comp-iam refresh-census` "measured 664h (27 days) stale 2026-09-01". `comp_iam_census.py`'s own
  **mtime is 664.5h** -- close enough to suspect the staleness measured was the SOURCE FILE's age,
  not a census artifact's. **UNRESOLVED, and it matters because that entry is written to fire
  UNPROMPTED.** Not chased this turn.

---

## 6 · WHAT THIS DOES NOT DO

⛔ **Admission is measured, not mandated.** Steps 7-10 remain design; only steps 5-6 are gated by
`.tools/to-pipeline-gate.py`. **This file makes the battery's `<preflight>` block honest -- it does
not make the battery mandatory.** That is Andrew's call (gate 5 in the handoff).
⛔ **`comp-heat` was NOT measured** -- it was not admitted to the battery, so it was out of scope.
`comp-heat drift` remains an open possible exception.
⚠ **`comp-denytest` was exercised only to its argument contract, not fired.** Firing it means a live
`simulate-principal-policy` call, which has two recorded false-deny modes and no change under test
today. Classified runtime on the structural ground that it holds no corpus.
