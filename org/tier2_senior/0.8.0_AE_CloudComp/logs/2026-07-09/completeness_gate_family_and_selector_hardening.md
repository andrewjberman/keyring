# Completeness gate family (built, found dormant, re-wired, proven) + selector near-tie hardening 13 -> 0

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, VALIDATE, DIAGNOSE

**Agent:** 0.8.0_AE_CloudComp
**Date:** 2026-07-09
**Window:** 08:45Z -> 11:40Z (continues `respawn_router_wire_aua_apply_and_p3_hud_close.md`)
**TO:** NFRA_TOOLCHECK.P3 follow-on (bonus hardening; P3 itself closed 084508Z)

---

## Summary

Built the commit-time **completeness gate family** (membership + map-home + self-routing), then found
it was **wired for one of its four substrate classes** -- and found that by turning the day's own
master-principle on my own gate. Re-wired it, proved it end-to-end through a real `safe-commit`, and
closed the selector's near-tie fragility class 13 -> 0.

**Four self-corrections this window**, each the same shape (a proxy standing in for a property):

1. `comp-routable-check` **does not prove reachability**; it proves candidate-set MEMBERSHIP. It
   returned PASS over all 42 tools while the live oracle showed three unreachable. Overclaim
   withdrawn to CTO + CVO; both withdrew their halves.
2. I asserted `comp-coverage-check` was "RED at HEAD **right now**" without re-running it. Real at
   08:53Z, GREEN from 08:56:27Z. CTO had cited it as "decisive" in a ruling.
3. I inferred from a **20.4s** `safe-commit` that member-3 had run its sweep. It had not -- that was
   safe-commit's own chain. A mechanism inferred from a timing number.
4. My acceptance test asserted **"HEAD unchanged -> the bad commit didn't land."** Invalid in a
   shared worktree: HEAD moved because base COO pushed concurrently while my probe correctly never
   landed. The property is *"the probe commit does not exist"*, verified empty across all refs.

---

## Work Completed

### 1. `comp-routable-check` + wiring (`2cedce056`, `7b9bb0394`, `69f8844de`)

Commit-time REGISTERED-IMPLIES-REACHABLE invariant. `comp_route.py:329` filters `routable`, so a
`meta_tools[]`-homed tool whose role is absent from `_ROUTABLE_META_ROLES` is dropped **before
scoring** -- no curated rule can surface it. Regression-proven: replaying each pre-fix provider state
turns it RED and names exactly the right tool (`system-compiler` -> comp-system;
`fedobs-reflective-reader` -> comp-fedobs); HEAD GREEN. Declared exemption (`routing_exempt: <reason>`,
COO~B) is declarative, printed every run, and an empty reason does not exempt.

CTO ruled **b2 substrate-scoped + ramp-exempt**; 7/7 verification; blocked an hour by an owned-paths
lane that had **copied** the `ANY_EXEC_OR_AE` roster in June and never inherited later adds (a forked
definition drifting from its source -- the same failure the gate prevents, one layer up). I did NOT
`--force`; CTO fixed the lane (`f091fd168`).

### 2. The 3-member completeness family (`1c5a90e74`)

routable (membership) + placement (one map home) + self-routes (the property). Governing rule, CTO
verbatim: *"every hard-blocking member asserts a DETERMINISTIC fact; anything threshold-shaped
REPORTS."* Member-3's split was **measured**, not reasoned: self-routing is deterministic run-to-run
AND role-invariant (4 roles, zero variance), but **13/42 tools passed only inside a near-tie margin**
-> hard-block on MISS, WARN on near-tie.

The 12/12 matrix caught **two bugs in my own gate**: a fail-closed hole (scope computation outside the
guard -> crashed instead of deciding = fail-OPEN in disguise) and a bound that was a **claim, not a
fact** (`git show` decodes via the locale codec, the file is UTF-8, the manifest has an em-dash -> a
byte-identical file compared unequal, so the per-tool bound silently ran the full 42-sweep: 33.8s
where I claimed 798ms).

### 3. THE FINDING: the family was dormant (`2910bfabc`)

`commit_gate_runner.py` dispatches by **suffix** (`.py`/`.sh`/`.tf`). The family's substrate is two
YAML files, one `.py`, the extensionless router, and any `.tools/comp-*`. So:

| substrate | dispatched? |
|---|---|
| `comp_capability_provider.py` | GATED |
| `graph-call-manifest.yaml` | never scanned |
| `comp-coverage-map.yaml` | never scanned |
| `.tools/comp-which` | never scanned |
| `.tools/comp-*` (placement's own trigger) | never scanned |

You introduce an unroutable tool by **registering** it -- a YAML edit. **The gate built to block
comp-fedobs and comp-system would not have seen either.** The logic was right; the wiring was absent.
My 12/12 matrix had called `cmd_check` **directly** -- it proved the gate DECIDES when called, never
that it GETS called. *Test the gate the way a commit hits it, not the way a unit-test calls it.*

CTO withdrew "the commit-time prevent layer is complete" (he had it queued for an Andrew note).
Grounded before proposing: `safe-commit.sh:274` passes **every staged file, unfiltered** -> the fix is
**one surface**. Suffix-independent substrate collection + ONE batched `cmd_check` after the loop.

**Also fixed (COO~B routed, DS~B hit it):** the gate **could not commit a `.py` deletion** --
`py_compile` on an absent file raised an *uncaught* `FileNotFoundError`, so it crashed with a traceback
instead of deciding, and `--force` does not bypass a gate failure. Same crash-instead-of-decide shape.

**End-to-end matrix (real `safe-commit` + the real entry point, 8/8):** regressed provider ->
`safe-commit` aborts, names comp-system, probe commit absent; YAML-only commit runs the family; a new
unplaced `.tools/comp-*` blocks **its author**; another agent's untracked WIP does **not** block others;
`.py` deletion skips cleanly; multi-substrate -> ONE sweep.

### 4. Other fixes

- **`560a3f8ec`** `comp-coverage-check`: two consumers, two universes. Its `os.listdir` read the
  **shared worktree**, so another agent's untracked mid-authoring file red-bannered everyone. Proven
  with a probe (`touch` -> FAIL, `rm` -> PASS). There was **no cache** -- the hypothesis was tested and
  is false. `--universe commit` (git-tracked) is the gate view; working-tree stays the operator default.
- **`8dfdaa8d1`** `comp-glob`: **two** defects. A bare basename was consumed as a *pathspec*, and the
  empty result printed under `OK:` -- reporting the proxy (the walk found nothing) as the property (the
  file is absent). Now resolves, and 0 hits prints `NO MATCH` + "this is NOT a confirmation the file is
  absent" + the next move.
- **`af837c1ce`** shared-archive disciplines in `value_parity_reader.py` (CTO ruling).
- **`5e9bfea7b`** oracle exposes `self_route_verdicts()` -- one definition, imported by member-3, never forked.
- **`.gitignore` finding**: 16 of 58 comp-tools were gitignored, incl. `comp-blast` + `comp-iam`
  (CLAUDE.md **mandates**). Confirmed all 16 genuinely source (shebangs, no binaries, no secrets, thin
  wrappers over already-tracked engines) -> CTO ruled force-add -> COO~B executed. Universes converged
  42 -> 58, both PASS. The substrate now survives a clone.

### 5. Selector near-tie hardening: 13 -> 0 (`41bd1d176`, `4c2a7c70c`, `df8b618b5`)

**Three distinct failure modes, diagnosed before drafting each time:**
1. **neighbour-naming** -- comp-depth's catalog text named `comp-blast/comp-trace/comp-xref`; their
   tokens hijacked its route. *A tool's own description is routing input.*
2. **defining-concept borrowing** -- comp-diff named nobody but described itself with comp-blast's
   defining concept ("blast radius"). Same failure, name filed off.
3. **thin text** -- the last five simply had short use_case sentences and lost to richer neighbours.

`comp-parity` was checked against a **baseline** (revert comp-which to HEAD, measure, restore) rather
than assumed: it was already near-tie with an identical top-3, so `comp-incrparity` stole nothing.

Final: **RANK1 42 | NEARTIE 0 | MISS 0.** Member-3 now emits zero WARNs -- and still returns rc=1 on a
stray unplaced tool, so it is *satisfied*, not dead.

---

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| comp-which-routing-test | PASS 42/42 | the load-bearing oracle all night; caught the catalog-add's latent vocab gap |
| comp-routable-check (NEW) | PASS / `--strict` PASS | built, regression-proven on both historical instances |
| comp-manifest-check `completeness` (NEW) | 8/8 e2e | the family; was dormant, now fires |
| comp-coverage-check | PASS both universes | working-tree defect found + fixed |
| comp_route_eval | canon 65.8 -> 100%; diverse 95.7%; heldout 50%/70% | canon is the tautological tier -- see caveat |
| comp-glob | fixed | confident-empty on a bare basename |
| comp-grep / comp-shell | PASS | on-rail search; Rule-16 scan clean |
| commit-gate / safe-commit | PASS | universal; `.py`-deletion crash fixed |

**What worked:** the live oracle is the only thing that caught the vocabulary sub-class, twice. Every
significant bug this window was found by *exercising*, never by reading.

**What failed:** four of my own claims (above). Also: `git show` + `text=True` silently decodes with the
locale codec on Windows -- it will bite anyone diffing a non-ASCII file in-process.

**Gap found:** `heldout p@1 50% / recall@surf 70%` is untouched by all three tranches. Curated
vocabulary is saturated; the remaining gap is posterior/semantic and is CTO's arch call.

---

## MCP Traffic

~35 messages. Significant: CTO arch-gates (option-b, b2+ramp-exempt, member-3 MISS/near-tie split,
lane-fix `f091fd168`, gitignore force-add ruling, wiring GO); CTO + CVO both **withdrew** their halves
of the membership-vs-reachability overclaim; COO~B endorsed two-universes + ran verify-don't-accept on
every tranche; DS~B's `comp-glob` and `.py`-deletion reports (both fixed at root).

---

## Blockers

**None.** Everything routed is landed or explicitly deferred: the consolidated `safe-commit`
add/delete/force-add staging pass (CTO GO'd as a scoped follow-on, design not yet routed), and the
heldout-tier posterior work (CTO's arch call).

---

## Current State

- **Completeness family LIVE** at HEAD `7cd588e6e`: `comp-manifest-check completeness
  [--only routable|placement|self-routes]`, wired for all four substrate classes, fail-closed,
  ramp-exempt, engines imported never forked. Blocks the comp-fedobs/comp-system birth path through a
  real `safe-commit`.
- **The claim, scoped to what the matrix proves** (CTO adopted this verbatim): *a commit that registers
  an unroutable tool, adds an unplaced comp-tool, or induces a self-route MISS is blocked end-to-end
  through safe-commit; the live oracle remains load-bearing for the vocabulary sub-class and for
  anything the substrate set does not name.* Nothing broader.
- **Selector:** RANK1 42 / NEARTIE 0 / MISS 0; oracle 42/42; `--strict` PASS.
- **Costs at the real gate entry point:** unrelated `.py` 1.46s | YAML-only bounded 2.67s |
  corpus edit (comp-which/provider) 63.6s, ONE 42-tool sweep.

---

## Next Steps

1. **[me, on GO]** design the consolidated `safe-commit` staging pass -- one sanctioned path for
   add / delete / force-add-ignored. Root: *the wrapper's staging assumes files present-and-not-ignored.*
   Two instances found today (the `.py` deletion crash; force-add past `.gitignore` needing a bare commit).
2. **[1.0.0_SA_CTO]** arch call on the heldout tier (50% p@1 / 70% recall@surf). Curated vocabulary is
   saturated; moving it means the COMPROUTE posterior. This is the tier that predicts whether a cold
   agent asking an unanticipated question reaches the right tool -- i.e. the rail's actual purpose.
3. **[2.0.0_SA_COO~B]** optional catalog hygiene: three tools still describe themselves with a sibling's
   defining concept even though curated rules now hold the oracle green.
4. **[me]** re-run the oracle + `--strict` after any future `comp-which` / manifest / coverage-map /
   provider commit -- the gate now does this automatically on the commit that touches them.
