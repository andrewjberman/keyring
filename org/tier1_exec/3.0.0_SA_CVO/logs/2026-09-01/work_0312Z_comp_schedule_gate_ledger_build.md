# Session log -- 3.0.0_SA_CVO~C -- 2026-09-01 01:45Z to 03:12Z

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE

Lane `~C` of `3.0.0_SA_CVO`; no `~C` agent folder exists, so this log is homed in the base-serial
folder with the lane in the title. Window = since `02401f20ff` (the 00:35-01:45Z log).

---

## Window summary

Built `comp-schedule` -- the gate ledger -- end to end on Andrew's word, from a measurement pass
that materially changed the design before any code was written. Registered it through three
registry homes the commit gate correctly demanded, wrapped it in a skill on the `/comp-adversary`
structure, and discharged the resulting two-phase override in-session. `1.0.0_SA_CTO` ruled all
five gate questions from the previous window while this was in flight; none of it blocked the build.

---

## What was done

### 1. The measurement pass that reshaped the design (before any code)

Andrew asked for the `/draw` + `/exec-sum` of comp-schedule. Re-grounding the carriers for that
drawing is what produced the finding, so the drawing was not a restatement -- it was the design
work.

**The inherited design (CTO handoff 90454) called all five carriers "machine-discoverable". They
are not the same kind of thing.**

```
  org/projects/*.json `blocking`   348 files, 333 carry the key
      9   empty
    189   the word "None" written in ENGLISH        <- a null as prose
    135   non-null prose                            <- looks like 135 blocked projects
             of which  16 SELF-NEGATE   ("SEQUENCING (not a hard blocker)")
                        65 use closed / complete / resolved / superseded language
    648   median characters.   30,625 at the longest.
```

>> **A 30,625-character `blocking` field is an essay, not a field.** Report "135 blocked" and the
   tool is wrong before its second line -- and NO REGEX SETTLES IT, because the negation is in the
   prose. **Refusing that total became the single most load-bearing decision in the build.**

### 2. `comp-schedule` BUILT -- `97c0064e09` (5 files, +828/-1)

**Nothing is stored.** View-time compiled from five carriers; no artifact, no cache, no registry,
so there is nothing to go stale -- which is the exact failure a hand-curated gate list reproduces.

**The DECIDABILITY schema** (Rule 24 four-postulate record in the source header). ONE axis: can a
machine settle, from this carrier's own bytes, whether a gate is armed?

| carrier | decidability | live numbers |
|---|---|---|
| C1 SENTINEL (`# DEPLOY-SERVE-HELD:`) | DECIDABLE | 20 lines -> **4 gates** |
| C2 DEPLOY-LEDGER (`.open_deploys/`) | DECIDABLE | 2 open entries |
| C3 MORATORIA (CLAUDE.md NEVER block) | DECIDABLE | 12 clauses |
| C4 SCOPE-GUARD (task orders) | SEMI-DECIDABLE | 19 files, listed never counted |
| C5 PROJECT-BLOCKING | **NOT-DECIDABLE** | 333 -> **ZERO gates**, a reading list |
| (fourth value) UNREADABLE | -- | never rendered as zero rows |

**Build ladder rung 2, and it matters more than usual here:** the sentinel grammar is IMPORTED from
`safe_deploy_core.SERVE_HELD_RE` -- the same regex that gates real deploys. A second copy would be
a shadow grammar that drifts from the thing that actually enforces, and then this ledger would
report a gate the deployer does not honour, or miss one it does. The battery asserts no second copy.

### 3. WHAT IT FOUND ON ITS FIRST LIVE RUN -- the class Andrew described, instantiated

```
  data/inf/scripts/silver/convert_transactions_to_silver.py:94
  # DEPLOY-SERVE-HELD -- and READ WHY, because the reason CHANGED and the sentinel did not:
  #   NEVER#2 (never-widen co-sign): *** SATISFIED. *** CTO 113603Z + COO -- co-sign GIVEN 2026-07-13
```
**A gate whose own comment says its condition was satisfied on 2026-07-13, still armed seven weeks
later.** It is `--drift` row one.

Also: **20 sentinel lines collapse to 4 GATES** -- one gate stamped across 12 files is ONE gate. A
further 19 raw matches were agents QUOTING a sentinel in inbox mail; `org/mcp/inbox` is excluded and
the exclusion is DECLARED in the output.

### 4. Registration -- the gate refused an unregistered comp-tool, correctly

Three homes were required, not one: `comp-coverage-map.yaml` `meta_tools[]` (routable:true), and
`graph-call-manifest.yaml` `excluded_not_graph_use_cases` with a stated reason -- it queries
RECORDS, never the dependency graph, the `comp-surprise`/`comp-missions` precedent exactly. That
exclusion is recorded as a **DEBT, not a resting place**: the owed follow-up is a curated
`comp-which` vocabulary pass, and the need is real because the entire point of the tool is that an
agent can ASK what is blocking it.

### 5. Skill wrapper + override discharge

`.claude/skills/comp-schedule/SKILL.md` on the `/comp-adversary` structure (Andrew-direct this
window). Registering the tool edits `org/modules/graph/` -- the rule bank -- and `comp-system`
refuses to compile an UNCOMMITTED source, so land-then-recompile is two-phase BY NECESSITY. Took
the reserved `STRUCTURAL-TWOPHASE/rule-bank` override and **DISCHARGED IT IN-SESSION** at
`693f5a07bf` (comp-* ledger union 100 -> 101). An undischarged structural override is a discipline
event; a discharged one is not.

---

## Compiler Tools

| tool | result | note |
|---|---|---|
| `comp-schedule` (NEW) | PASS | the build target; `--self-test` 5/5, render rc=0, 18 gate rows |
| `test_comp_schedule.py` (NEW) | PASS | 9/9 after, **0/9 before the tool existed** |
| `comp-read --enumerate` | PASS | dogfooded the tool I shipped last window to read the coverage map + the hook |
| `comp-find` | PASS | sentinel/scope_guard censuses, full-corpus, no `head` |
| `comp-system` | PASS | recompiled twice; the second discharges the override |
| `.tools/commit-gate.sh` | PASS | rc=0 "clean for 4 of 4" after registration; correctly BLOCKED before it |
| `python -m py_compile` + `ruff py39` | PASS | run EXPLICITLY on the extensionless executable |
| `.tools/safe-commit.sh` | PASS | both commits; one refusal was the `-m` execution-vector gate firing on `$(...)` in my own command line -- correct, switched to `-F` |
| `.tools/provision-path-shims.sh` | PASS | `comp-schedule` resolves bare |

**What worked:** measuring the carriers BEFORE designing. The prose finding is not a detail -- it
inverted the central assumption of the inherited design, and it was only visible because the
carriers were counted rather than described. Red-first held for the third build this session (0/9).

**What failed -- four defects in my own build, every one found by RUNNING IT ON LIVE DATA:**
1. **It crashed mid-render.** cp1252 `UnicodeEncodeError` on a `U+26D4` in a CLAUDE.md moratorium
   line, after emitting 16 of 18 gates -- **the header said 18 and the body showed 16.** A ledger
   that dies PART WAY through is worse than one that fails at the start: the output looks complete
   to anything reading the top. Fixed with `_ascii()` -- **the identical fix I wrote into
   comp-adversary earlier the same session and did not carry here. A lesson applied in one file is
   not a lesson applied in the estate.**
2. A dot-prefixed TOOL STATE file (`.unindexed_red_state.json`) counted as a gate -- inventing an
   armed gate with no owner and no discharge condition.
3. `SERVE_HELD_RE` is single-line BY DESIGN; the 07-13 gate's reason spans lines, so it rendered
   with a nonsense discharge and an UNNAMED owner until the continuation was read HERE rather than
   by widening a grammar that gates real deploys.
4. **`PROSE_IS_NEVER_A_GATE` was declared and never CONSULTED.** The mutant flipped it and nothing
   changed -- a switch that cannot alter behaviour cannot certify the behaviour is enforced. Wired;
   the mutant now reports 153 (18 + 135) against the real 18.

**Gap found:** three of the nine failing legs were bugs in **my own test**, not the tool, and I
fixed the test rather than the subject -- (a) leg 4 required the inbox path to be ABSENT from the
output while ALSO requiring the exclusion to be DECLARED, and the declaration contains the string
(self-contradictory); (b) leg 5's regex expected `sentinel lines=N` where the tool prints
`N sentinel line(s)`; (c) **the mutant ran from a `TemporaryDirectory`, which broke the subject's
sibling import so it reported 14 gates for a reason having nothing to do with the mutation.** A
harness that breaks the subject's imports measures the harness.

---

## MCP traffic

0 sends this window; 4 messages received and ACKed (90545, 90553, 90555, plus the CVO grade).
Significant:
- **RECEIVED 90545** -- `1.0.0_SA_CTO` ruled ALL FIVE gate questions from my brief. Q2 (the rule is
  scoped to the REPO CORPUS) landed as LAW `@c6bf69427f`; Q3 ruled the predicate is `-f`, not an
  extension match, and the correct predicate already exists at `comp-tool-hud.sh:141`, 41 lines
  above the broken one. **None of it blocked this build, and this seat must not touch the hook.**
- **RECEIVED 90553 / 90555** -- attribution: the Q3 finding has ONE origin, this seat's brief B.3,
  and two senior seats read it and agreed (repetition, not corroboration). The `:141` citation was
  genuinely convergent. Recorded, nothing owed.

---

## Blockers

**None owned by this seat.** Sequence state only:
1. **Andrew's test trigger** is reserved for all three builds this session (stage 4, `--enumerate`,
   `comp-schedule`). This seat reports READY and does not self-certify.
2. **PUSH refused by mechanism** -- LD-0367/LD-0368 integrator-only on CLOUD. No override attempted.

Surfaced, not chased: the `comp-pipescript` suite RED (CTO ruled Q5 -- assert the PROPERTY not the
CONSTANT; owner `0.8.0_AE_CloudComp`); the `comp-system` AGE-WARN (carried graph rows >24h TTL, not
mine, not discharged).

---

## Current State

- **`97c0064e09`** -- `comp-schedule` (NEW, `.tools/comp-schedule`, ~500 lines). Carriers
  `c1_sentinels()` `c2_ledger()` `c3_moratoria()` `c4_scope_guards()` `c5_prose()`; helpers
  `_ascii()` `_full_reason()` `_owner_from_condition()` `_last_touched()` `_drift_flags()`;
  `compile_view()` / `render()` / `self_test()`. Modes: bare, `--drift`, `--owner`, `--gate`,
  `--self-test`. Switch `PROSE_IS_NEVER_A_GATE`. Test `.tools/tests/test_comp_schedule.py` (9 legs).
  Skill `.claude/skills/comp-schedule/SKILL.md`. Registered in
  `org/modules/graph/comp-coverage-map.yaml` + `graph-call-manifest.yaml`.
- **`693f5a07bf`** -- recompile discharging the STRUCTURAL-TWOPHASE override.
- **LIVE READING, first run:** 18 gates armed (C1 4 / C2 2 / C3 12), 135 NEEDS-READ prose fields,
  2 drift candidates -- `G-3` (own comment says SATISFIED 2026-07-13, still armed) and `G-4` (the
  calendar guard naming `code/gold/lib/`, where the repo has `lib/trading_calendar.py` -- DESIRED vs
  APPLIED, deliberately NOT called discharged).
- **PUSH STATE: LOCAL.** MEASURED: local `CLOUD` = `693f5a07bf`; `git ls-remote origin CLOUD` =
  `173a873139` read at 2026-09-01T02:24:48Z. Perishable -- it ages the moment the integrator runs.
- `comp-schedule` resolves bare via the provisioned `~/bin` shim.
- `.tools/hooks/comp-tool-hud.sh` UNTOUCHED throughout, per CTO's Q1/Q3 rulings.

---

## Next Steps

1. `[Andrew]` trigger the test on any of the three builds; and rule whether `LAST VERIFIED` stays a
   derived weak proxy or gets a written stamp -- the one design question this seat reserved.
2. `[3.0.0_SA_CVO]` grade `comp-schedule` as base, and adjudicate the two DRIFT CANDIDATES -- the
   tool raises them and by design will never close them.
3. `[0.7.0_AE_CloudOps]` / `[1.0.0_SA_CTO]` `G-3` is a live armed gate whose own comment records
   NEVER#2 as satisfied 2026-07-13. It needs a human discharge or a corrected sentinel.
4. `[0.8.0_AE_CloudComp]` the owed curated `comp-which` vocabulary pass that deletes
   `comp-schedule`'s graph-manifest exclusion; plus the Q5 `test_pipescript_digest` repair.
5. `[0.0.0_AB_MSTR]` five commits from this seat are LOCAL and move on the next integration window:
   `1f4bc0e513`, `3648481523`, `7d857989eb`, `02401f20ff`, `97c0064e09`, `693f5a07bf`.
