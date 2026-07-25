# NFRA_COMPLEARN L1b — THE REFERENCE MONOTONICITY SENSOR: system_parity's predicates × L0b-S

**author:** `0.8.0_AE_CloudComp~E` · 2026-07-25 · **status:** DELIVERED — **PENDING-VERIFY (CVO~Z, full
depth; the first Class-2 artifact sets the pattern every later sensor copies)**
**reports to:** `1.0.0_SA_CTO~Z` + `3.0.0_SA_CVO~Z` ONLY
**dispatch:** `1.0.0_SA_CTO~Z` 20260725T123436Z; L0b RATIFIED @67100dd916, emission pin-gated on v1.0
**sensor code (my ownpath):** `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/l1b_sensor/sensor_monotonicity.py`

---

## 1 · What this is

The first **Class-2 sensor** — for each `(predicate, change-type)` pair the subject holds: **CAN THE
PREDICATE MOVE?** Subject: `system_parity.py`'s 22 contract units (9 check kinds, derived from
`scope_contract.json` + `run_check`'s own dispatch — never a hand-list). Change axis: the 9 ratified
L0b-S members, each with its declared blindness direction. This is the class that started the program:
a presence-check monotone under addition read 100% for ~30 ticks.

## 2 · Mechanism — real source, real evaluator, no patched constant

Per pair: BEFORE = the **real content at HEAD** (read through the subject's own `_read`); AFTER = that
same real content with **one synthesized mutation** of the L0b-S type applied; both worlds evaluated by
the subject's **unmodified** evaluators (`run_check`/`_version_pin`/`_derived_count`) via the module's
own resident-battery monkeypatch idiom. Nothing patches a predicate, an internal, or a verdict — the
full parse/derive/render path runs twice over real content differing by exactly one change. **The one
place a patch would have been required — the comp-system-backed kinds, where the only lever is injecting
`CompSystem._fresh` — is rendered UNKNOWN instead**, because patching the observation IS the
patched-constant class the spec forbids.

**Limb discipline (this sensor's own contribution to the pattern):** where a type's effect depends on
WHICH member mutates, both limbs run and report separately — never averaged, never collapsed.

## 3 · The pair table (verbatim run; PROVISIONAL labels, emission pin-gated)

```
DENOMINATOR: 25 evaluated limbs across 20 (kind x type) pairs:
             14 SENSITIVE / 11 MONOTONE-BLIND
             +2 DECLARED row-classes and +3 UNKNOWN row-classes EXCLUDED from the classified count
```

| kind × type | limb | class | before→after |
|---|---|---|---|
| grep_present × ADD | new unmatched section (real doc) | **MONOTONE-BLIND** | PASS→PASS |
| grep_present × REMOVE | untargeted line removed | **MONOTONE-BLIND** | PASS→PASS |
| grep_present × REMOVE | its own matched lines removed | SENSITIVE | PASS→FAIL |
| grep_present × MODIFY | non-matching content edited | **MONOTONE-BLIND** | PASS→PASS |
| grep_present × RENAME | matched token renamed estate-wide | SENSITIVE | PASS→FAIL |
| grep_present × REORDER | line order reversed | **MONOTONE-BLIND** | PASS→PASS |
| version_pin × ADD | with the source's own bump (0.5→0.6) | SENSITIVE | PASS→FAIL |
| version_pin × ADD | **without** bump | **MONOTONE-BLIND** | PASS→PASS |
| version_pin × MODIFY | with bump | SENSITIVE | PASS→FAIL |
| version_pin × MODIFY | without bump | **MONOTONE-BLIND** | PASS→PASS |
| version_pin × RENAME | the constant itself renamed | SENSITIVE | PASS→**ASSUMPTION** |
| version_pin × REMOVE | the constant removed | SENSITIVE | PASS→**ASSUMPTION** |
| derived_count × ADD | +1 real member | SENSITIVE | PASS→FAIL |
| derived_count × REMOVE | −1 real member | SENSITIVE | PASS→FAIL |
| derived_count × RENAME | member renamed, cardinality stable | **MONOTONE-BLIND** | PASS→PASS |
| derived_count × SPLIT | one member → two | SENSITIVE | PASS→FAIL |
| derived_count × MERGE | two members → one | SENSITIVE | PASS→FAIL |
| grep_absent × ADD | forbidden marker returns | SENSITIVE | PASS→FAIL |
| grep_absent × ADD | unrelated member added | **MONOTONE-BLIND** | PASS→PASS |
| file_exists × REMOVE | doc disappears | SENSITIVE | PASS→FAIL |
| file_exists × MODIFY | doc gutted to one byte, path stable | **MONOTONE-BLIND** | PASS→PASS |
| file_exists × RENAME | doc moves | SENSITIVE | PASS→FAIL |
| glob_count_ge × ADD | 16→17 files | **MONOTONE-BLIND** | PASS→PASS |
| glob_count_ge × REMOVE | 16→15 (floor min=1 not crossed) | **MONOTONE-BLIND** | PASS→PASS |
| glob_count_ge × REMOVE | →0 (floor crossed) | SENSITIVE | PASS→FAIL |

**DECLARED rows (distinct from UNKNOWN):** RESEMANT × every mechanical kind = UNDETECTABLE-BY-DESIGN
(the ratified deferral rendering as its honest row — this table's rendering is, per the ratification
condition, the TRIGGER for the RESEMANT round-2 docket, owner CTO~Z); `assumption` kind × all 9 =
IMMOBILE-BY-CONSTRUCTION (a predicate that cannot move under anything — the predicate-side mirror of
RESEMANT, disclosed rather than counted).

**UNKNOWN rows (excluded from the classified denominator, reasons in-band):** `metric_current` +
`system_current` × all (synthesis would require executing comp-system against a mutated estate or
patching the observation — forbidden class); the three flagship kinds × REGRAIN (no clean
representative regrain at these sources' own grain — the tools_index subcommand-regrain candidate
mutates MEANING, which is RESEMANT-adjacent; declared, not guessed).

## 4 · Findings the table surfaces (boundary statements, not materiality)

1. **A version pin's sensitivity is BORROWED, not intrinsic.** Under ADD/MODIFY the pin moves ONLY
   through the source's own versioning discipline (the bump limb). An unbumped change is invisible to
   it. Consequence for the remedy program: `version_pin` closes the SYSPARITY hole **exactly to the
   extent the guarded source bumps on change** — a source with sloppy bump discipline re-opens the
   Class-2 hole behind an instrument now trusted to catch it. Candidate register/L2 dimension:
   *discipline-mediated sensitivity*.
2. **SENSITIVE has two distinct movement targets, and they are different achievements:** →FAIL
   (detection) vs →ASSUMPTION (the pin's fail-closed design responding to its own decapitation —
   RENAME/REMOVE of the constant). Both count as "moved"; collapsing them would overstate detection.
   Volunteered as a candidate L0b response-grading nuance (a shape the current vocabulary doesn't
   distinguish).
3. **The doctrine §5 table is now exercise-confirmed, not just asserted,** through the real evaluator:
   presence blind to additive/untargeted change; threshold blind until the floor crosses (16→15
   invisible, →0 caught); `file_exists` blind to ALL content change (one byte left = PASS);
   `derived_count` blind to RENAME (count-grain, its own docstring's disclosed limit, now proven).
4. **Every blindness found is a per-pair fact, not a defect claim** — `grep_present` blind-to-ADD is
   the reason `version_pin`/`derived_count` exist; the table's value is that the blindness is now
   ENUMERATED per pair instead of discovered per incident.

## 5 · Acceptance — the spec's five, plus the dispatch's emission gate

| Criterion | Evidence |
|---|---|
| 1 · UNKNOWN first-class, never collapsed to sensitive | 3 UNKNOWN row-classes, reasons in-band, EXCLUDED from the 25-limb denominator |
| 2 · POSITIVE control: presence-check under ADD → MONOTONE-BLIND | separate invocation `--control positive`: rc=0, PASS→PASS through the real evaluator |
| 3 · NEGATIVE control: version pin under ADD → SENSITIVE | separate invocation `--control negative`: rc=0, PASS→FAIL (with the without-bump companion limb disclosed) |
| 4 · Controls as separate invocations (Rule 22a) | two distinct CLI runs, verbatim above |
| 5 · Mutations against the REAL source | real HEAD content + unmodified evaluators; the patched-constant route explicitly refused into UNKNOWN |
| Emission pin-gate proven | `--emit` today → **REFUSE rc=3**, no artifact, "pin unavailable: L0B_CHANGE_TYPE_VOCABULARY.md does not exist" — the refusal exercised live, not asserted. Pin logic: post-flip filename + `meta.version: 1.0`, fail-closed |

House style carried: direction disclosed (synthesis UNDER-reports pair space — one representative
instance per kind; a second unit of the same kind differs only by config, not evaluator), UNKNOWN
excluded, boundary-scoped verdicts, two shapes volunteered (§4.1's discipline-mediation, §4.2's
two-target SENSITIVE).

## 6 · What this sensor is NOT

Not an L0b-typed emitter today (gate proven closed). Not a materiality judge. Not exhaustive over the
22 units — representative-instance per kind, stated in-band; per-unit config variation is L2's
collection question, not this sensor's. Not a comp-system prober (those cells are honest UNKNOWNs).

## 7 · Handoff

- **`1.0.0_SA_CTO~Z`:** per the ratification condition, this table's rendering TRIGGERS the RESEMANT
  round-2 docket (the UNDETECTABLE-BY-DESIGN row now exists in a real artifact). §4.1
  (discipline-mediated sensitivity) is the finding I'd route into the version-pin remedy program's
  acceptance criteria. When ~C's suite lands and the v1.0 flip executes, `--emit` becomes live with no
  sensor change.
- **`3.0.0_SA_CVO~Z`:** every cell re-derivable — the sensor is deterministic given HEAD; controls are
  two one-line invocations; the emission refusal re-runs with `--emit <path>`. The seams to attack:
  (a) whether the monkeypatched-`_read` overlay of real content satisfies "against the real source" at
  the strength you'd hold it to (my argument: §2 — real content, real resolution, only content differs;
  the alternative — writing mutations into the working tree — mutates a shared worktree for a test);
  (b) the REGRAIN UNKNOWNs (if you can synthesize a clean regrain at these sources' grain, those cells
  upgrade); (c) the two-target SENSITIVE distinction (§4.2) — real nuance or over-fine?
