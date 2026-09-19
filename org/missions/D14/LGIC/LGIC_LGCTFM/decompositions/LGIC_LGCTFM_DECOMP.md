# LGIC_LGCTFM -- DECOMPOSITION (L5)

**Cut by** `2.0.0_SA_COO~G`, 2026-09-16, on PRD **v1.1 @`92154e0b63`**, ADMITTED -- both halves SIGNED and
current, read from `python .tools/prd-signoff.py status LGIC_LGCTFM` (ratified-text `3.0.0_SA_CVO`, brief
`4.0.0_SA_CRO`), which is the one read that decides it.

> The project row's `blocking` prose still says the brief half is "owed by 4.0.0_SA_CRO on the re-offer".
> That text is STALE against the tool, which reads SIGNED and current. The tool is the authority and the row
> is prose; noted here rather than acted on, because the field is `1.0.0_SA_CTO`'s as the L3 register carrier.

---

## 0. WHAT L5 READ, AND WHAT IT MEASURED BEFORE CUTTING ANYTHING

**Input.** PRD v1.1's ENDPOINT (ten cards, FWD-1..FWD-10), CONTRACTS, THE DECISIONS CLOSED AT L4, CELL
CANDIDATES (thirteen rows, T1..T13), PATHS and SURFACE MANIFEST. The PRD says in terms that the
decomposition is this lane's and that it "may split, merge or re-sequence these"; this cut re-sequences and
constrains, and merges nothing.

**THE SUBSTRATE CENSUS, run before the cut rather than discovered by a worker.** A cell whose read-path does
not exist is defective at the cut, and a cell whose new home already exists is not creating what it claims.

```
  read-paths the candidates consume ................... 20 named   0 ABSENT
  new homes the candidates create ...................... 8 named   0 ALREADY PRESENT
```

Every one of `NAMING_SCHEMA.json`, `02_DOCTRINE.md`, `06_CONFORMANCE_LEDGER.md`,
`07_ROUTING_REDERIVATION.md`, `08_TENSION_MAP.md`, `lib/opal_naming.py`, `lib/trading_calendar.py`,
`lambda-source-map.json`, `EC2_MANIFEST.json`, `infra/aws/terraform/`, the ATOM_DECOMP skill and its
`ssot_establishment.schema.json`, `workflows/atom_decomposition/README.md`, the `draw` and `canonical-flow`
skills, `.tools/receiving-check.py`, `.tools/naming-gate.py`, `remediations.json`, `scopes.json` and
`LEGACY_SERVED_PATHS.json` resolves. Every one of `LGCTFM_CONTRACT.schema.json`,
`10_LEGACY_TRANSFORM.md`, `lib/opal_lgctfm.py`, `lib/lgctfm_render.py`, `lib/tests/test_opal_lgctfm.py`,
`.claude/skills/lgctfm/SKILL.md`, `workflows/legacy_transform/` and this project's `deliverables/` is absent.
**So the PRD is not built on anything missing, and nothing it calls new already exists.**

---

## 1. THE DOMAIN, BY SUBTRACTION (Rule 24(i))

The declared domain is *the work that carries LGIC_LGCTFM's ten endpoint outcomes from ADMITTED PRD to a
CLOSED row*. Written as a subtraction from a printed denominator, never as a forward list:

```
  candidate cells in PRD v1.1 s.CELL CANDIDATES ................... 13   (T1 .. T13)
  minus candidates this cut DROPS ................................. -0
  minus candidates this cut DEFERS to a later round ............... -0
  = CELLS IN THIS DECOMPOSITION ................................... 13
```

**NOTHING IS DEFERRED, and that is the spine's requirement, not a preference:** L6's one issuance covers
EVERY cell, and a later round exists only when the CTO's round-N analysis sends work back. A cell this cut
could not cover would mean this cut is not ready to issue.

**THE WAIT AUDIT (Rule 27: NO FWD IS A WAIT).** Two outcomes look like waits and neither is:

- **FWD-4** is graded by a NAMED PERSON -- "Andrew has read the list for one subject". The MECHANISM is
  driven deliberately by T13, which puts one subject's list in front of him; the organic case (he happens to
  read one) is the negative arm, never the plan. The PRD qualifies the state as APPLIED with the named actor
  until he has, and refuses a report standing in for him. That qualification is the PRD's, at L4, and this
  cut carries it verbatim rather than re-deciding it.
- **FWD-8** reads "after a migration wave", which sounds like waiting for another project. It is not: the
  PRD's own T12 row admits "a real **or practice** wave", so the second run is driven on a practice wave in
  a scratch worktree at this lane's own hand. A round that waited for ADVI_FIRMBKTS to migrate would wait
  forever and would be exactly the defect Rule 27 names.

---

## 2. THE RECTANGLE -- every outcome has a serving cell

Read DOWN for an outcome's cells, ACROSS for a cell's outcomes. The coverage claim is the column check:
**10 of 10 outcomes carry at least one cell**, so no outcome is UNCOVERED at the cut.

| outcome | plane (R-17) | cells that serve it |
|---|---|---|
| FWD-1  the one contract, each row naming its instrument and blind spot | REPO | T1, T3, T10 |
| FWD-2  forks named by the engine, canonical member marked | REPO | T4 |
| FWD-3  desired name/address computed by the builders, never typed | REPO | T1, T4, T13 |
| FWD-4  typed, ranked tensions with the ranking rule printed | NAMED-PERSON | T5, T13 |
| FWD-5  current and desired flow pictures, drawn by a program | REPO | T7 |
| FWD-6  the migration work plan, decomposable directly | REPO | T2, T6 |
| FWD-7  the subject MARKED so a later added use is refused | REPO (+`--enforce` practice checkout) | T10, T11 |
| FWD-8  re-run shows closed / opened / unchanged | REPO | T8, T12 |
| FWD-9  same subject, same pin, same files | REPO | T9 |
| FWD-10 the instrument moves nothing | LIVE | T10 |

**THE LIVE ROW IS THE ONE TO WATCH (R-17).** FWD-10's cell must NAME its estate instrument in the
invocation: `comp-find --corpus aws` with the nodes-scanned denominator and the DB's own `built:` line as
vintage, plus the served portal routes read from the served plane. A LIVE-plane criterion cut against a repo
record is returned, not worked.

---

## 3. THE CELLS -- 13

Cell ids are `LT-<axis>-<n>`; the PRD's `T<n>` label is kept beside each so the PRD row is findable. Acceptance
clauses below are the PRD's drafts, tightened to ONE CLAUSE PER CRITERION at the cut (a compound criterion is
refused by the L6 gate).

| cell | PRD | what it does | serves | writes |
|---|---|---|---|---|
| `LT-s-1` | T1 | the contract schema + its Rule 24 record | FWD-1, FWD-3 | `org/standards/LGCTFM_CONTRACT.schema.json`, `deliverables/CONTRACT_SCHEMA_RULE24.md` |
| `LT-s-2` | T2 | the receiving checker's `lgctfm-contract` artifact type | FWD-1, FWD-6 | `.tools/receiving-check.py` |
| `LT-e-1` | T3 | THE WALK -- the CURRENT half, every row with its instrument and blind spot | FWD-1 | `lib/opal_lgctfm.py`, `infra/logic/10_LEGACY_TRANSFORM.md`, `.claude/skills/lgctfm/SKILL.md` |
| `LT-e-2` | T4 | the DESIRED oracle and the fork test | FWD-2, FWD-3 | `lib/opal_lgctfm.py` |
| `LT-e-3` | T5 | the tensions, four measured factors each, ranking rule printed | FWD-4 | `lib/opal_lgctfm.py` |
| `LT-p-1` | T6 | the plan, R19's six steps, no package executed | FWD-6 | the run directory |
| `LT-r-1` | T7 | the renderer, two diagrams from the contract | FWD-5 | `lib/lgctfm_render.py` |
| `LT-h-1` | T8 | the run home and the diff | FWD-8 | `workflows/legacy_transform/` |
| `LT-d-1` | T9 | determinism, negative arm fired FIRST | FWD-9 | `lib/tests/test_opal_lgctfm.py` |
| `LT-x-1` | T10 | the first real run and the MARK | FWD-1, FWD-7, FWD-10 | the run dir; appends to 3 registry files |
| `LT-x-2` | T11 | the planted refusal, in a practice checkout | FWD-7 | nothing tracked |
| `LT-x-3` | T12 | the second run and the diff on a real subject | FWD-8 | the run directory |
| `LT-v-1` | T13 | the reviewer's reproduction and Andrew's read | FWD-3, FWD-4 | `deliverables/` |

### 3a. THE FIXED INPUTS L6 CUTS INTO THE FACES

Written by this seat BEFORE the issuance, under
`org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/`, and read-only to every
worker:

- `check_lt_r1.py` -- the checker every round-1 criterion invokes, one subcommand per criterion, each with a
  RED-FIRST self-test arm exercised ALONE.
- `SUBJECT_CONTROL.json` -- the hand-built composition of the first subject, taken from the ADVI_FIRMBKTS
  brief's IV.1-IV.9, so `LT-e-1`'s walk is graded against a control it cannot edit.
- `FORK_CONTROLS.json` -- **FOUR** POSITIVE forks and the ONE NEGATIVE control (the SmartX
  platform/account pair). The negative control is the whole discriminator: a fork detector that fires on
  everything that looks alike passes every positive arm and is worthless, so the SmartX pair NOT appearing is
  a criterion in its own right, never a clause inside the fork criterion.

  > **FIVE, NOT THE FOUR THIS SECTION FIRST SAID AND THE PRD STILL SAYS (`LGIC_LGCTFM-S1`).** PRD v1.1's T4
  > row reads "IV.5's four positive forks"; the brief's IV.5 -- the carrier that ENUMERATES them -- lists five
  > semicolon-separated members and closes "Each is a positive control for O2". Part III O2 names three inside
  > em-dashes, which is illustration, not a count. This cut first welded the PRD's four to O2's three examples
  > and checked neither: the exact forward-list shape Rule 24(i) refuses. The enumerating carrier wins, and the
  > fifth member (the `bd` / `49f` / `49financial` spellings) is carried with its own dispute noted, being the
  > only one of the five that is not a pair of paths.

  > **THEN FOUR, ON THE MEASUREMENT (R-24 clause 3).** R-24 ruled five but required the fifth to be ONE
  > MEASURED PAIR, not the spelling class, because the class splits into one fork and many A3 tensions. The
  > pair was measured on both planes and does not exist at this vintage: on the live plane 0 of 113 names
  > begin with `49f-` (every occurrence is compound, e.g. `bd-49f-auto-login`, one resource carrying both
  > spellings), and on the repo plane every `49f-` string is an identifier with no `bd-` twin. A positive
  > control fired the pair-finder on a planted `49f-fees` beside the real `bd-fees` (1 pair) and on the
  > real names alone it returns 0, so the zero is an absence. **FORK-5 is withdrawn to the tension set; the
  > count is FOUR.** PRD v1.3's DEC-5 states the controls by reference and re-reads the count from this
  > fixture, so it stays true without an edit; T4 still names five and is the one carrier left to match.

---

## 4. PLACEMENT AXIS

Everything this project builds is PLATFORM code and PLATFORM records, not firm data: the engine and renderer
in `lib/`, the schema in `org/standards/`, the method beside the canon in `infra/logic/`, the runs in
`workflows/legacy_transform/`. **No firm-attributable output exists**, so the tier homes of Rule 30 / R1-R21
are consumed by the engine as RULES and are not themselves written to. The only writes that touch the LGIC
registry are `LT-x-1`'s three appends, which are the MARK and are covered by R-16 (a registry edit is a
deploy on every shipping generated view, disclosed and printed by the gate).

---

## 5. DEPENDENCY EDGES, LEVELS, AND THE TWO DISJOINTNESS CONSTRAINTS

**Edges** (`X -> Y`: Y cannot start until X has drained):

```
  LT-s-1 -> LT-s-2      the checker validates the schema, so the schema exists first
  LT-s-1 -> LT-e-1      the walk emits rows shaped by the schema
  LT-s-1 -> LT-r-1      the renderer reads a contract, and a planted one suffices
  LT-e-1 -> LT-e-2      the desired half is computed FOR the current rows
  LT-e-2 -> LT-e-3      a tension is a disagreement between current and desired
  LT-e-2 -> LT-d-1      determinism is measured on an engine that produces something
  LT-e-3 -> LT-p-1      the plan is ordered by the tension set
  LT-e-3, LT-p-1, LT-r-1, LT-h-1 -> LT-x-1     the first real run needs the whole instrument
  LT-x-1 -> LT-x-2      the planted refusal needs a MARK to violate
  LT-x-1 -> LT-x-3      the second run needs a first
  LT-e-3, LT-x-1 -> LT-v-1                     the reviewer reproduces from a real run's rows
  LT-h-1                independent of the schema: a run home and a diff keyed on row identity
```

**Levels** (cells on one level are mutually independent and may run in parallel):

```
  L0   LT-s-1   LT-h-1
  L1   LT-s-2   LT-e-1   LT-r-1
  L2   LT-e-2
  L3   LT-e-3   LT-d-1
  L4   LT-p-1
  L5   LT-x-1
  L6   LT-x-2   LT-x-3   LT-v-1
```

**SEVEN LEVELS DEEP AND THREE WIDE. THIS PROJECT IS A SERIAL BUILD, AND THE FAN-OUT IS BOUNDED BY DEPTH, NOT
BY THE CAP.** The whole edge set is ONE connected component -- by the strict chain reading M = 1 -- so the
honest statement is that the widest level, 3, is the real parallelism and eight workers would buy nothing.

### CONSTRAINT 1 -- `lib/opal_lgctfm.py` has THREE writers, and they go in ONE queue

`LT-e-1`, `LT-e-2` and `LT-e-3` all write `lib/opal_lgctfm.py`. Measured across the thirteen candidates: 18
distinct write surfaces, and this is the ONE file more than one cell writes. Two cells writing one file
cannot run in parallel, and under ADHC_OWNPTH.005 both orders would hold a live grant to it at once.

> **They are therefore ONE WORKER'S QUEUE, in the order `LT-e-1` -> `LT-e-2` -> `LT-e-3`** -- which the edge
> set already forces, so the constraint costs nothing. This is the same defect this lane caught in its own
> LGIC_NAMING v7 cut, where two cells wrote `GRADING_RULE.md`; it is cheap to see at L5 and expensive to see
> at a drain.

### CONSTRAINT 2 -- the run home overlaps at the GRANT level, not the file level

`LT-p-1`, `LT-h-1`, `LT-x-1` and `LT-x-3` write different LEAF files, but all four live under
`workflows/legacy_transform/`. **A `<paths>` entry ending in `/` is a DIRECTORY PREFIX and grants the whole
subtree** (`_paths_block_entries`), so four orders naming that prefix would each hold the whole run home.

> **So these four are also ONE WORKER'S QUEUE** (`LT-h-1` -> `LT-p-1` -> `LT-x-1` -> `LT-x-3`), and where a
> cell needs only its own run directory the order names **that directory**, not the prefix. A grant is
> narrowed at the cut or it is not narrowed at all.

### The distinct-worker constraint

`LT-v-1` is the reviewer's reproduction and **must be a DIFFERENT worker slot from the one that built the
engine** -- the PRD says "a worker who is not the engine's author", and a reproduction by the author is
Rule 22's REPETITION, not corroboration. Likewise `LT-d-1`'s negative arm runs on a de-sorted COPY of the
engine on a scratch branch, never on the engine's own checkout.

**Slot assignment, 3 slots:**

```
  slot ~1  LT-s-1 -> LT-e-1 -> LT-e-2 -> LT-e-3        the schema and the engine spine (one file, one queue)
  slot ~2  LT-h-1 -> LT-p-1 -> LT-x-1 -> LT-x-3        the run home and the runs (one prefix, one queue)
  slot ~3  LT-s-2 -> LT-r-1 -> LT-d-1 -> LT-x-2 -> LT-v-1   the consumers, the controls, the reproduction
```

`fanout: 3 of 1 chain, cap 8, reason: one connected edge set 7 levels deep and 3 wide; two write surfaces
(lib/opal_lgctfm.py and workflows/legacy_transform/) each force a single queue, and LT-v-1 must not be the
engine's author.`

---

## 6. BATTERY DISPOSITION

- **`comp-adversary`: RUN.** The fork test is the adversarial surface -- a detector that fires on everything
  that looks alike passes every positive arm. Its findings ride `LT-e-2`'s negative control.
- **`comp-schedule`: RUN, and APPLICABLE.** `LT-e-1` reads both trigger APIs and must print BOTH
  denominators; a schedule the walk cannot see is an UNMEASURED row, not an absent one.
- **`comp-iam`: RUN, and APPLICABLE.** Roles compose the subject and `comp-iam` is one of the walk's named
  instruments.
- **Beyond the core:** `comp-kuzu` and `comp-find --corpus aws` are the LIVE-plane readers for `LT-e-1`'s
  current half and `LT-x-1`'s FWD-10 before/after; both are READ-ONLY here and neither is a write surface.

---

## 7. RULE 24 FOUR-POSTULATE RECORD

- **(i) MECE over a declared domain.** Domain in s.1, written as 13 minus 0 minus 0 from the PRD's printed
  denominator of 13. The uncovered member was hunted on the OUTCOME axis, not the cell axis: s.2's rectangle
  checks all ten FWD ids, and an outcome with no cell would read UNCOVERED there.
- **(ii) SAME GRAIN.** One row per candidate cell; one criterion per acceptance clause at the cut. No cell
  here is a programme and none is a single assertion.
- **(iii) INTENT COHERENCE.** One axis: *what must be BUILT and EXERCISED for the ten outcomes*. Grading is
  not in this document -- verdicts are the CVO's at L9 and the CTO's at the close.
- **(iv) STATE COHERENCE.** What this decomposition does NOT move: it moves no cloud state (FWD-10 is the
  outcome that says so), it executes no package of the plan (`LT-p-1`'s own clause forbids it), and it does
  not migrate ADVI_FIRMBKTS -- the MARK is a record, and the migration is a separate project under its own
  sign-off.

---

## 8. CHOICES THIS DECOMPOSITION MAKES THAT THE PRD DID NOT

1. **Three writers of `lib/opal_lgctfm.py` become one worker's queue** rather than three cells with a shared
   grant. The PRD names the file three times and does not say who writes it when.
2. **The run home is granted by RUN DIRECTORY, not by the `workflows/legacy_transform/` prefix**, wherever a
   cell needs only its own run. The PRD's paths table names the prefix.
3. **`LT-h-1` is placed at L0**, independent of the schema. The PRD's ordering implies it follows the
   contract; nothing in the diff's row-identity keying requires that, and putting it early takes one level
   off the critical path.
4. **`LT-v-1` is bound to a different worker slot from the engine's author.** The PRD says "a worker who is
   not the engine's author"; this cut makes that a slot constraint the issuance can be checked against,
   rather than an instruction a worker has to honour about itself.
5. **The fork NEGATIVE control is a criterion of its own**, not a line inside the fork criterion -- so a
   detector that finds the four forks AND the SmartX pair fails, where a compound clause would have let it
   pass on "found the forks".

---

## 9. WHAT THIS DECOMPOSITION DOES NOT CLAIM

- It does not claim the instruments can see everything. The opposite is designed in: a resource no instrument
  reaches is an UNMEASURED row, and `LT-e-1` is graded by PLANTING one outside every instrument's scope.
- It does not claim the first subject is representative. It is the subject the brief names, and FWD-8's
  second run is what tests the instrument over time.
- It does not claim FWD-4 can be closed without Andrew. It carries the PRD's NAMED-PERSON qualification and
  drives the card to him; it does not let a report stand in for his read.
- It does not grade anything. Every verdict here is a bar to be measured, and the cells' own criteria, not
  this document, are what a worker satisfies.

---

## 10. v1.1 -- THE ADDENDUM AT THE L6 CUT (2026-09-17, `2.0.0_SA_COO~G`), before any round-1 order existed

**The cell set is unchanged: 13 cells, the table in section 3, nothing added, dropped or deferred.** PRD v1.4 is
ADMITTED (`prd-signoff.py status LGIC_LGCTFM`: both halves SIGNED, current); v1.2-v1.4 moved only T4's fork count and
DEC-5's wording, which FORK_CONTROLS.json v1.1 already carries (four positives, one negative). Three things the cut
measured that section 5 did not say:

1. **CONSTRAINT 1 COUNTED THREE WRITERS OF `lib/opal_lgctfm.py`; THE CUT HAS FOUR.** T6's plan is engine code (the
   PRD's PATHS row names `lib/opal_lgctfm.py` for T3-T9, and the plan is T6), so `LT-p-1` writes the engine too, on
   slot ~2. It is not a concurrency hazard: the edge `LT-e-3 -> LT-p-1` already forces it after slot ~1's queue drains,
   and the face says so. `LT-p-1` also carries the `run` verb that assembles a run directory, so `LT-x-1` and
   `LT-x-3` run the instrument and edit no code. Row `LGIC_LGCTFM-S2`.
2. **`LT-h-1`'s code has a home that is not the engine:** `workflows/legacy_transform/run_home.py` (`new`, `manifest`,
   `diff`). `LT-h-1` sits at level 0 beside `LT-e-1`, which holds the engine, so the run home cannot live in it.
3. **The interfaces every criterion reads are fixed in the faces** -- the contract's field names (from
   `infra/logic/11_LGCTFM_CONTRACT_SCHEMA_RECORD.md`), the CLI verbs, the artifact paths -- and the checker
   `fixed_inputs/r1/check_lt_r1.py` reads exactly those. `PLANTED_CONTRACT.json` is the one planted contract the
   schema, the receiving check, the renderer and the diff are exercised on.

**Slot plan (unchanged from section 5):** ~1 `LT-s-1 -> LT-e-1 -> LT-e-2 -> LT-e-3`; ~2 `LT-h-1 -> LT-p-1 -> LT-x-1 ->
LT-x-3`; ~3 `LT-s-2 -> LT-r-1 -> LT-d-1 -> LT-x-2 -> LT-v-1`.

---

## 11. v1.2 -- THE ROUND-1 AMENDMENT (2026-09-17, `2.0.0_SA_COO~G`), on `1.0.0_SA_CTO`'s RULING R-36

**ONE cell is ADDED: `LT-e-4`. The other 13 are unchanged -- nothing is dropped, deferred or re-scoped.** The
count is 14.

**Why the cell exists.** `LT-x-1`'s `X1R1-AC1` FAILED on one row, and the cause was a contradiction between two
DRAINED cells rather than a defect in either: `LT-s-1`'s schema built `$defs.node_type.enum` as EXACTLY
`NAMING_SCHEMA.json`'s 33 graded types BY SUBTRACTION, which its own order required, and `LT-e-3`'s untypeable
plant emits a row whose `node_type` is `COGNITO_USER_POOL`, outside those 33 -- unconditionally, in `cmd_walk()`,
on every subject. So every contract the engine writes failed validation on that row. Row `LGIC_LGCTFM-W2-S2`.
R-36 ruled REC (A) and REFUSED the sentinel alternative: the enum's equality by subtraction is the invariant that
lets the contract say a type is ungraded at all (Rule 24(i)), and a schema that can absorb an ungraded type stops
being able to say so.

**Why `LT-e-4`, and why the `e` series.** The substantive change is ENGINE behaviour -- the plant becomes opt-in
and an untypeable node is carried instead of written -- so it belongs with `LT-e-1..LT-e-3`, and 4 is the next free
number in that series. The one non-engine byte it needs (the contract's count field) is the ISSUER's, landed with
this amendment rather than left to the cell: a criterion that cannot be satisfied by any write inside the cell's
own grant is the exact defect class R-36 exists to close, and the schema is `LT-s-1`'s drained deliverable.

| cell | PRD row | what it is | outcomes | write surface |
|---|---|---|---|---|
| `LT-e-4` | T5 (amends), T10 (unblocks) | the untypeable plant becomes OPT-IN; an ungraded node is CARRIED in the run's own `PLANT_UNTYPEABLE.json` with `NOT_COVERED` and COUNTED in the contract; two real runs prove both halves | FWD-1, FWD-4 | `lib/opal_lgctfm.py`, the run home |

**Seating: slot ~2, level 5.** `depends_on`: `LT-p-1` (the `run` verb that assembles a run directory, drained on
this slot) and `LT-e-3` (the plant this cell makes opt-in, drained on slot ~1). It is the FIFTH writer of
`lib/opal_lgctfm.py` and the LAST, and CONSTRAINT 1's queue still holds: slot ~1's engine queue drained before
`LT-p-1`, and this cell is after `LT-p-1` on the same slot, so no two writers are ever concurrent. Section 10's
count of four writers becomes FIVE with this cell.

**What the ISSUER landed with this amendment, so the cell's criteria are satisfiable inside its grant:**

1. `org/standards/LGCTFM_CONTRACT.schema.json` gains ONE property, `untypeable`, a `$defs/cell` whose value is the
   count, and it is added to `required`. **Required is the mechanism, not decoration:** R-36's words are that an
   empty carrier must not be readable as "the walk met none" -- a printed zero is a measurement and an absent one
   is silence -- and `required` is what makes absence impossible rather than merely discouraged. `$defs.node_type`
   is NOT touched, so `LT-s-1`'s subtraction invariant is untouched and `s1-node-types` still grades it.
2. `fixed_inputs/r1/PLANTED_CONTRACT.json` gains that cell with `value: 0`, because the schema's top level is
   `additionalProperties: false` and a new required property would otherwise make the planted fixture -- the one
   input `LT-s-1`'s and `LT-s-2`'s criteria validate -- INVALID at the cut. Measured after: `s1-valid`,
   `s1-bare-value`, `s1-one-api`, `s1-no-instrument`, `s1-node-types`, `s1-enums`, `s2-accept-valid`,
   `s2-refuse-bare`, `s2-unchecked`, `s2-selftest`, `r1-identical`, `r1-edit`, `r1-hand-edit`, `r1-fresh`,
   `e2-reproduce` and `e3-untypeable` all still PASS.
3. `fixed_inputs/r1/check_lt_r1.py` gains five arms (`a4-plant-off`, `a4-flag-on`, `a4-count-typed`,
   `a4-schema-valid`, `a4-e3-exercised`) and `core_untypeable` now grades EITHER carrier shape, so the historical
   walk artifact keeps its verdict while the amendment's runs are graded on what they actually write. Self-test 70
   of 70, each new arm's GREEN fixture and DOCTORED twin driven alone.

**`LT-x-1` is NOT reopened by the cell.** Its order stays `pending` until this amendment drains; the worker
re-runs `x1-run-dir` as its own criterion, and the ISSUER re-opens and flips `LT-x-1` at the drain. A worker never
flips another cell's order.

---

## 12. v1.3 -- THE ROUND-2 RECUT (2026-09-18, `2.0.0_SA_COO~G`), on `1.0.0_SA_CTO`'s round-1 analysis

**Input, and the two carriers DISAGREE on one point so the fresher one governs.**
`LGIC_LGCTFM_ROUND1_ANALYSIS.md` @`fe2d71cb2a`-era, section "WHAT ROUND 2 CARRIES", items 1-5; and
`project.json`'s `blocking` as `1.0.0_SA_CTO` corrected it at `last_updated 2026-09-18T06:55:00Z`. The
analysis item 1 says *"S10's TWO branch-relative arms"*; the register says **FOUR**, citing row `S18` and
`3.0.0_SA_CVO`'s independent confirmation @`98f7074714`. **THE REGISTER IS FRESHER AND IS RIGHT, AND THE
ANALYSIS IS THE CARRIER THAT WENT STALE** -- which is this evening's own R-51 class, read in the direction
that matters: a cut that took the analysis at face value would have scoped this round to HALF its
population.

Round 1 graded **REALIZED 8 of 10**. `FWD-4` is APPLIED-not-realized and `FWD-6` NOT REALIZED, and
[HARD] **NEITHER CAN BE CLOSED BY AN ENGINE CELL** -- `FWD-4` closes on Andrew's own read of `ANDREW_CARD.md`,
`FWD-6` when a REAL migration's decomposition is cut from the plan, which is `LGIC_CANON`'s C6 practice
wave. **So round 2 is a HARDENING round and says so rather than implying progress toward an outcome it
cannot move.** Its job is to leave the instrument TRUSTWORTHY for the R19 migrations that will consume it.

### 12.1 THE CELLS -- 3, and no earlier cell is re-opened

```
  cells at v1.2 ......................................................... 14
  plus round 2's three .................................................. +3
  = cells in this decomposition ......................................... 17
  round 2 runs exactly the three: LT-a-2, LT-n-2, LT-c-2
```

| cell | id | what it does | serves | rows it answers |
|---|---|---|---|---|
| 15 | `LT-a-2` | **THE RE-DERIVATION RECORD.** Takes round 1's FOURTEEN judgment claims and re-derives each from a THIRD POSITION -- neither the branch that produced it nor the checkout that graded it -- recording per claim RE-DERIVED or NOT-RE-DERIVABLE **with its mechanism**. The four checkout-dependent arms are EXPECTED in the second class; a partition that finds fewer than four has not looked | FWD-3, FWD-9 | `S10`, `S18` |
| 16 | `LT-n-2` | **RUN IDS AND CONTENT HASHES ON EVERY NUMBER** a round-1 judgment record cites, enumerated BY SUBTRACTION from the records and never as a forward list, with `E3` EXCLUDED BY NAME and its reason stated | FWD-3 | `S11` |
| 17 | `LT-c-2` | **THE CARD NAMES ITS SUBJECT ON ITS FACE** -- run id plus contract content hash plus the INSTRUMENT that produced the hash, and a pointer to the adjudication. [HARD] **IT DOES NOT TOUCH THE RANKING OR THE RECOMMENDATION** | FWD-4's readability, not its closure | `S12`, `S16` |

### 12.2 WHY `LT-a-2` IS A RECORD AND NOT A REPAIR, WHICH IS THE OPPOSITE OF WHAT THE ITEM SOUNDS LIKE

The obvious reading of *"re-cut to run where the claim is consumed"* is **repair round 1's checker**. That
is REFUSED here, on this lane's own filed position and on `R-43`: `check_lt_r1.py` is a FIXED INPUT of a
CLOSED, GRADED round. On their own branches those arms' windows were NON-EMPTY, so the grades they fed are
SOUND and an edit now moves no grade. R-43 scopes a frozen-history defect's remedy to ONE LIVE-DIRECTION
document, never a sweep over rounds already closed.

[KEY] **WHAT IS ACTUALLY MISSING IS THE THING NOBODY HAS: A STATEMENT OF WHICH OF ROUND 1's CLAIMS A LATER
SEAT CAN CHECK.** A claim that can only be verified in the place that makes verification repetition is not
a claim a migration can rely on. So the cell produces the partition, and the four known members are its
FLOOR rather than its answer -- `S18` found two of them only by an UNSCOPED read of the shared mechanism,
and the cell is told to do the same rather than to work from the list.

### 12.3 `LT-c-2` IS HOW `S16` IS RESOLVED, AND THE RESOLUTION IS A GRANT

`S12`'s named remedy is one line in `ANDREW_CARD.md`. `S16` recorded that **this remedy could never be
performed by its own disarm owner**: `.tools/owned-paths-validate.py` clause 4 refuses an ISSUER's edit
inside a worker's deliverables folder, measured twice on that exact file. The remedy is not impossible --
**it needs a CELL whose `<paths>` names the card**, which is a worker's grant and not an issuer's.

[HARD] **AND THE CELL IS DELIBERATELY NARROWER THAN THE ROW.** `S6`'s condition was that the card's correction
reach the decision-maker BESIDE it *"rather than as a silent rewrite"*, and it did, by
`1.0.0_SA_CTO`'s adjudication @`662d53b793`. So this cell ADDS the subject pin and a pointer, and a graded
arm REFUSES any change to the ranking table or the recommendation line -- byte-identity on the 179-row
order is an acceptance criterion, not a courtesy. A round that quietly rewrote a card sitting with a
decision-maker would be the exact act `S6` exists to prevent.

### 12.4 WRITE SURFACES, AND THE ONE CROSS-WORKER GRANT

```
  LT-a-2   deliverables/<its own serial>/ + the project's surprise channel
  LT-n-2   deliverables/<its own serial>/ + the project's surprise channel
  LT-c-2   deliverables/0.9.0_WK_LGIC_LGCTFM~3/ANDREW_CARD.md   <- CROSS-WORKER, granted explicitly
           + deliverables/<its own serial>/ + the project's surprise channel
```

### 12.5 THE FAN-OUT, AND THIS ROUND CARRIES A STATED EXPERIMENT

```
  slot ~1   LT-a-2  ->  LT-c-2
  slot ~2   LT-n-2
```

`fanout: 2 slots over 2 connected components, cap 8, reason: the three cells share ONLY the surprise
channel and no cell reads another's output; levels L0 = {LT-a-2, LT-n-2}, L1 = {LT-c-2}. LT-c-2 queues
behind LT-a-2 because the card's pin should cite the re-derivation record if that record contradicts it.`

[CAUTION] **ROUND 6 OF `LGIC_ENFORCE` PUT BOTH ITS CELLS ON ONE QUEUE on the rule that two worker branches
appending to one channel is a GUARANTEED conflict** -- measured 3 of 3 on a sibling project's round-4
drains. **THIS ROUND TAKES TWO SLOTS, AND THE REASON IS A MEASUREMENT THAT CUTS THE OTHER WAY.** At round
6's second drain, `1.0.0_SA_CTO` had appended `LGIC_ENFORCE-S70` to the channel in the shared tree while
this lane's worker appended `W1-S70` on its branch -- a genuine concurrent append at the same array end --
and `safe-merge` merged it **with NO conflict**: the union test over every document read 190 ids expected
and 190 merged, nothing missing, nothing extra, both rows present.

[KEY] **THE HYPOTHESIS THIS ROUND TESTS, STATED SO IT CAN BE REFUTED: a TEXTUAL SPLICE merges where a
WHOLE-ARRAY RE-DUMP conflicts.** A splice touches only the bytes between the last row and the closing
bracket, which is a 3-way merge git resolves; a re-dump rewrites every line of the array, which conflicts
with any other change to it. The 3-of-3 conflicts and this 1-of-1 clean merge are then not contradictory
-- they are two different write methods. **BOTH ORDERS THEREFORE MANDATE A TEXTUAL SPLICE AND FORBID A
RE-DUMP**, and if the second drain conflicts anyway the hypothesis is refuted and recorded as such rather
than quietly forgotten. n=1 is not a result; it is a reason to run the test with the cost bounded to one
union merge.

### 12.6 THE FIXED INPUT, AND WHAT IT CARRIES FROM THE ROUND-1 HEADLINE

`deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_lt_r2.py`. Round 1's own headline is adopted as a
construction rule rather than a lesson: **three of this lane's arms were UNSATISFIABLE BY A CORRECT FIX
and all three passed their INJECTED self-tests**, because a fixture written by the arm's author shares the
arm's assumption. So every core in this checker is driven against a **SIMULATED CORRECT RECORD and must
PASS**, as well as against a doctored one and must FAIL. [HARD] **A MUTANT TEST CANNOT CATCH A VACUOUS PASS**
(`R-47`): the mutant proves an arm CAN fail, and a vacuous arm fails it happily while passing everything
real. Both controls exist here or the arm is not cut.

**AND EVERY ARM IS POSITION-INDEPENDENT BY CONSTRUCTION, WHICH IS THE WHOLE POINT OF THE ROUND:** no arm
resolves its subject by position in a directory, and none reads `git merge-base HEAD CLOUD`. A cell's
commits are found by AUTHOR plus its order id in the message; a run is found by its own `HASHES.json`
manifest (`R-40`); and any arm whose verdict could depend on the checkout PRINTS that dependence.

### 12.7 WHAT THIS ROUND DOES NOT CLAIM

- It does **not** move `FWD-4` or `FWD-6`. Both bar on acts outside this engine and the round says so.
- It does **not** re-grade `E3`. `S11`'s remedy is the CONVENTION, and `E3`'s judgment was SOUND AT ITS
  OWN VINTAGE -- it ran before `LT-e-4` made the untypeable plant opt-in, which is what moved the
  population. Re-grading it would falsify a correct grade.
- It does **not** repair round 1's checker, and 12.2 says why.
- It does **not** touch the card's ranking or recommendation, and 12.3 makes that a graded refusal.


---

## 13. v1.4 -- THE ROUND-3 RECUT (2026-09-18, `2.0.0_SA_COO~G`), on `1.0.0_SA_CTO`'s RULING R-79

**Input.** R-79 @`0e9027c6dc` (msg 98034) and its answer to this lane's crossing recommendation (msg 98035).
**FWD-1's REALIZED grade is RETRACTED: 7 of 10, not 8.** It is a DEFECT against FWD-1, not a new outcome:
the ratified ACCEPT already reads *"never has to go and list the SCHEDULES, MACHINES, ROLES and BUCKETS by
hand to fill a gap the contract left blank WITHOUT SAYING SO"*, and Andrew's word at ~18:2xZ (record
@`28a8ae74e3`) names the same list in other words -- *"If we are missing lambdas/ec2/eventbridge rules or
schedules/ddb/etc, any involved aws resources, then the workflow process is not done"*, *"the workflow must
be designed to create rows for these items"*. PRD unchanged at v1.4, both halves SIGNED and current (read
from `prd-signoff.py status` at this cut).

[CORRECTION, recorded against this lane] **I recommended a PRD ADDENDUM at 18:19Z on the premise that the
bars "never named" compute. The premise was false and I had not read FWD-1's ACCEPT before asserting it.**
`1.0.0_SA_CTO` printed the ACCEPT and the premise fell. What survived is the gradeable form, adopted as
FWD-1's ACCEPTANCE ARM: *for a named project token, EVERY live AWS node the involved instrument reaches
carries a row, and the denominator is printed per node_type against the live plane.*

**The round-1 grade measured the DONE WHEN, never the ACCEPT** -- existence and readership, not coverage.
Measured at this cut by the issuer, on an instrument DIFFERENT from the engine's walk (comp-find over the
live aws corpus for the subject's two token spellings: 88 hits across 2590 nodes, graph 2026-09-18
12:17:28 UTC), against the graded run `20260918T011619Z-8db9eb1`:

```
  node_type        live floor   rows in the graded run
  LAMBDA                9              0
  EC2_INSTANCE          1              0
  DYNAMODB_TABLE        1              0
  SCHEDULE              4              1
  IAM_ROLE             13              1   (a PLANT)
  flow.current.md  -- COMPUTE --  (none)   <- a blank that does not say it is a gap
```

### 13.1 THE CELLS -- 4, R-79's (a)-(d) plus FWD-1's adopted acceptance arm

```
  cells at v1.3 ......................................................... 17
  plus round 3's four ................................................... +4
  = cells in this decomposition ......................................... 21
  round 3 runs exactly the four: LT-e-5, LT-r-2, LT-p-2, LT-x-4
```

| cell | id | what it does | serves | R-79 item |
|---|---|---|---|---|
| 18 | `LT-e-5` | **DISCOVERY BY DESIGN.** The walk reaches the subject's compute, schedules, machines, roles and tables -- seeded by the subject's TOKEN beside its buckets, and following the readers the estate already runs (comp-trigger targets, `lambda-source-map.json`, comp-iam statements). **The cell DEFINES "involved"** (token / trigger target / IAM grant / source text, or several) and writes a top-level `coverage` block into the contract whose shape is R3_BASE.json's, the ONE carrier. Schema admits it; the frozen graded contract still validates | FWD-1 | (a), (b), (c) |
| 19 | `LT-r-2` | **NO BARE "(none)".** An empty column is a statement about the INSTRUMENT: with a coverage block, every column prints `<R> row(s) of <I> involved`; without one (every run before this round), every column prints `NOT MEASURED`. FWD-5's regenerate-and-compare arm stays PASS | FWD-1 (the blank that does not say so), FWD-5 kept | (c) |
| 20 | `LT-p-2` | **`dependencies` -> `step_dependencies`** on every plan package, values preserved value-for-value, frozen runs untouched. RCN-0009 P4, adopted by R-79 as owed | FWD-6's reading hazard | (d) |
| 21 | `LT-x-4` | **THE REAL RUN AND THE ACCEPTANCE ARM.** One new 49F run into the run home, with the new discovery, render and plan. Every floor node of every type is a row or an excluded entry with a reason; every NAMED-class floor node is a ROW. The COMPUTE column names the Lambdas and the EC2 runner. **No registry mark** | FWD-1's ACCEPT, graded | the arm 98035 adopted |

### 13.2 WRITE SURFACES, AND WHY THREE CELLS SHARE ONE QUEUE

```
  LT-e-5   lib/opal_lgctfm.py, org/standards/LGCTFM_CONTRACT.schema.json,
           infra/logic/10_LEGACY_TRANSFORM.md, deliverables/0.9.0_WK_LGIC_LGCTFM~1/, channel
  LT-r-2   lib/lgctfm_render.py, deliverables/0.9.0_WK_LGIC_LGCTFM~2/, channel
  LT-p-2   lib/opal_lgctfm.py, infra/logic/10_LEGACY_TRANSFORM.md, deliverables/0.9.0_WK_LGIC_LGCTFM~1/, channel
  LT-x-4   workflows/legacy_transform/blackdiamond-49financial/<new run-id>/,
           deliverables/0.9.0_WK_LGIC_LGCTFM~1/, channel
```

CONSTRAINT 1 (s.5) still binds: `lib/opal_lgctfm.py` has one writer at a time, so `LT-e-5` and `LT-p-2`
QUEUE on slot `~1`; `LT-x-4` queues behind both because it runs the engine they produce. `LT-r-2` touches
only the renderer and runs beside them on slot `~2`; `LT-x-4` is spawned only once `LT-r-2` has DRAINED,
because its render arm reads the new renderer's output.

```
  slot ~1   LT-e-5  ->  LT-p-2  ->  LT-x-4
  slot ~2   LT-r-2
```

`fanout: 2 slots over 4 cells, cap 8, reason: three cells write or run lib/opal_lgctfm.py and queue on one
slot (CONSTRAINT 1); the renderer is disjoint and runs beside them; levels L0 = {LT-e-5, LT-r-2},
L1 = {LT-p-2}, L2 = {LT-x-4}, with LT-x-4 also depending on LT-r-2's drain.`

### 13.3 THE FIXED INPUT, AND THE RULE IT ADOPTS FROM A SIBLING'S DEFECT

`deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/` -- `R3_BASE.json` and `check_lt_r3.py`, 14 real arms
and a 24-arm self-test. Three construction rules, each from a measured defect:

1. **THE FLOOR IS RE-MEASURED AT GRADE TIME, WITH AN INSTRUMENT THAT IS NOT THE ENGINE.** A floor read from
   the fixed input at grade time would be a stale figure acting as a bar.
2. **ONE REAL NEGATIVE.** The self-test runs the coverage cores against the ACTUAL graded run and requires
   FAIL (LAMBDA 0 of 9), beside the author's own mutants -- a mutant shares its author's assumption.
3. **THE RECORD SHAPE HAS ONE CARRIER** (`LGIC_ENFORCE-S85`, this lane's own defect three hours earlier).
   The coverage block's shape lives ONLY in R3_BASE.json; the positive records are BUILT from it; and the
   self-test refuses if any round-3 order's quoted shape differs from it. **Also caught at this cut, and
   fixed before issuance:** the first draft's positive shape test passed because it was handed only the
   12 node_types the simulated record happened to cover, while the real arm requires all 18 floor types.
   A positive arm that passes only once the checker narrows its own input is the vacuous pass this rule
   exists to stop.

**WIRING AT THE CUT:** 11 of 14 real arms FAIL, each for the measured reason (10 bare "(none)" lines over 5
of 5 runs; 1074 packages carrying `dependencies`, 895 populated; no e-5 contract; no post-cut run). **THREE
ARE GUARD-SHAPED AND READ PASS AT THE CUT, DISCLOSED:** `r2-regen` (FWD-5's arm, must stay PASS),
`p2-old-untouched` (frozen history, R-43), `x4-no-registry-move` (no mark). Each protects a thing that
works; none measures the round's work.

### 13.4 WHAT THIS ROUND DOES NOT CLAIM

- It does **not** build the resource dependency relation (edges). FWD-6 inherits from FWD-1 and the repair
  order is FWD-1 first (R-79). A cell MAY write per-class extras its discovery already reads; no arm needs it.
- It does **not** pick the subject between MDPF_CANON and 49F -- Andrew's. 49F is used because FWD-1's
  ACCEPT names it.
- It does **not** re-grade round 1 or 2 (R-43), and it does **not** edit the graded run.
- It does **not** close FWD-1. `1.0.0_SA_CTO` re-grades the outcome at L10 against its ACCEPT.
- It does **not** build the CONSUMER WALK. Andrew-direct ~18:3xZ (msg 98038, record @`c9e54d5c0f`): *"the
  final step of the current resource/state manifest should include a walk of the pipeline ... to assess
  what exactly consumes the final artifacts (and if those artifacts are visible or invisible to a viewer on
  the portal)"*. `4.0.0_SA_CRO` is attempting it on MDPF_CANON and writing the BRIEF; its carrier into this
  project is `1.0.0_SA_CTO`'s. Cutting it here would pre-empt both. What round 3 DOES take from the same
  word is its first sentence -- *"work in all the comp-tools to this process"* -- as `LT-e-5`'s COMP-TOOL
  LEDGER: every listed comp-tool, USED or NOT USED with a reason, denominator printed.


---

## 14. ROUND 3 AS IT ACTUALLY CLOSED (2026-09-18 ~23:1xZ, `2.0.0_SA_COO~G`)

```
  LT-e-5  DRAINED @2b10693186   discovery by design; four arms PASS on the merged tree
  LT-r-2  DRAINED @20464bafee   no bare "(none)"; three arms PASS at its own tip
  LT-p-2  DRAINED @7e0c52281b   step_dependencies; three arms PASS at its own tip
  LT-x-4  SUPERSEDED, NEVER SPAWNED -> re-cut in round 4 (row S30, ratified by R-82)
```

**WHY `LT-x-4` DID NOT RUN.** `S26` recorded that R-81 landed 25 minutes after the issuance; `S30` ran its
drain test and read NON-CONFORMANT on both halves -- the `iam_grant` leg reads `comp-iam role` (Terraform
plane, outside R-81's `live / reconcile / simulate ONLY`) and `lambda-source-map.json` carries neither the
comp-lambdamap guard nor a dated declaration. `1.0.0_SA_CTO` ratified the consequence rather than merely
permitting it (R-82): a real run on an unmeasured engine produces a green that means the engine RAN, not
that it was RIGHT. The cell is not at fault -- it could not have been built against a ruling that did not
exist when it was dispatched.

### 14.1 `LGIC_LGCTFM-W1-S31`, THE DISARM OWNER'S WORD -- AND THE LIVE-DIRECTION STATEMENT ITSELF

`W1-S31` is this lane's, and the row's own analysis is adopted: round 1's `check_lt_r1.py` names
`dependencies` in `PACKAGE_FIELDS`; its `p1-fields` arm reads the FROZEN `plan_r1/plan.json` and so reads
PASS (1626 packages, 0 missing), while the same core over a FRESHLY BUILT plan reports 1074 of 1074 missing.
That is an EXPOSURE, not an INCIDENT: nothing was admitted, and round 1's graded evidence stands.

[HARD] **THE STATEMENT, WHICH IS THE REMEDY R-43 ALLOWS AND THE ONLY ONE THIS ROUND TAKES: EVERY ARM OF A
CLOSED ROUND'S CHECKER IS FROZEN AGAINST THAT ROUND'S OWN ARTIFACTS, AND A RUN OF IT AGAINST A LATER
ARTIFACT IS NOT A REGRESSION AND NOT EVIDENCE ABOUT ANYTHING.** `check_lt_r1.py` is a FIXED INPUT of a
CLOSED, GRADED round; R-43 scopes a frozen-history defect's remedy to ONE LIVE-DIRECTION DOCUMENT and never
to a sweep over rounds already closed -- this section is that document, and the r1 checker is NOT edited.
The same reading retires the hazard for every later rename: a field the engine no longer writes will always
"break" a closed round's checker against a fresh artifact, by construction. **WHAT WOULD REOPEN IT:** a
round that RE-USES `check_lt_r1.py` as a live instrument rather than as a record. That round owns the edit.
COST: none -- a reading rule. NON-APPLICATION: a checker still cited as live by an OPEN order.

`W1-S30` (the order named three write sites and `render_plan_md()` was never one) is INERT and needs no act:
the cell renamed the two that existed and refused to invent the third, which is the same restraint
`WHAT YOU BUILD 4` asks for. Whether `plan.md` should print a step relation at all belongs to FWD-6's
`resource_dependencies`, not here.

### 14.2 WHAT ROUND 4 OPENS WITH, IN ORDER

```
  1  the canonical graph-call-manifest.yaml entry for the AWS-inventory question   R-81, cell one
  2  re-point the iam_grant leg to comp-iam live (or reconcile/simulate)           S30 half one
  3  guard (comp-lambdamap) or DECLARE (date, owner, un-defer) the source map      S30 half two
  4  LT-x-4 re-cut: the real 49F run on the repaired engine                        FWD-1's ACCEPT arm
```

Item 4 is cut only after 2 and 3 drain, for the reason R-82 ratified. Items 2 and 3 are small and share one
file, so they queue on one slot; item 1 touches only the manifest and runs beside them.

[HARD] **AND ROUND 4's ISSUANCE CARRIES ONE SENTENCE THAT IS OWED, NOT OPTIONAL** -- `3.0.0_SA_CVO`'s round-3
L9 (@`71d0c885fd`) measured it and set the remedy: **`LT-e-5`'s PINNED PROOF RECORDS `E5R3-AC4` AS FAIL WHILE
THE ARM READS PASS AT HEAD.** The instance was pinned at `b736ee4fdf` and the issuer's repair landed at
`fd02b24c51`, 42 minutes later; **A PINNED PROOF IS NOT RE-GRADED WHEN A FIXED INPUT MOVES UNDER IT**, and
rewriting one would be the worse defect. So no artifact changes and no proof is rewritten -- round 4's
issuance STATES that `E5R3-AC4` reads PASS at HEAD, that the pinned instance records FAIL at its own vintage,
and that both are true of their own moments. It is written here rather than remembered, because a lesson
written in a report is not a control and this one has exactly one place it can fire: the next cut.


---

## 15. v1.5 -- THE ROUND-4 RECUT (2026-09-19, `2.0.0_SA_COO~G`), on the L10 round analysis @`ba1dcf65e9`

**Input.** `LGIC_LGCTFM_ROUND3_ANALYSIS.md` @`ba1dcf65e9` (msg 98094): coverage complete on both rounds, **NO
PRD addendum owed**, neither round enters `/open-calls`. The four items s.14.2 already named are cut here in
that order, and nothing else is.

[HARD] **THE SENTENCE THIS ROUND OWES, DISCHARGED HERE AND IN THE ISSUANCE COMMIT.** `LT-e-5`'s PINNED PROOF
records `E5R3-AC4` as **FAIL** at its own vintage (`b736ee4fdf`, 2026-09-18T16:27:12-04:00) while the arm
reads **PASS** at HEAD, because the issuer's repair (`fd02b24c51`, 17:09:25-04:00) landed **42 minutes after
the pin**. **BOTH ARE TRUE OF THEIR OWN MOMENTS.** No proof is rewritten and no artifact changes: a pinned
proof is a record of a vintage, and rewriting one would be the worse defect (`3.0.0_SA_CVO` @`71d0c885fd`,
adopted by the analysis).

### 15.1 THE CELLS -- 3

| cell | id | what it does | serves | source |
|---|---|---|---|---|
| 22 | `LT-m-1` | **THE MISSING CANONICAL ENTRY.** `comp-which` asked "what AWS resources exist" returns a SIX-WAY TIE with no winner; by NFRA_GRAPHS AC1 that is a missing canonical entry, not a ranking problem. One `cloud.inventory.*` entry naming R-81's assigned instrument, in the manifest's own 11-key shape, with every pre-existing entry byte-identical | the estate's own routing; R-81 cell one | R-81 |
| 23 | `LT-e-6` | **THE TWO R-81 REPAIRS.** Re-point the `iam_grant` leg off `comp-iam role` (Terraform plane) onto `comp-iam live / reconcile / simulate`; and either GUARD `lambda-source-map.json` with comp-lambdamap or DECLARE it with date, owner and un-defer condition. A re-point MAY ADD involved nodes and MUST NOT silently remove any | FWD-1 | `S30` |
| 24 | `LT-x-5` | **THE REAL RUN, RE-CUT.** One 49F run on the repaired engine; every floor node rowed or excluded with a reason; every NAMED class a ROW; no registry mark | FWD-1's ACCEPT arm | R-82 |

```
  slot ~1   LT-e-6  ->  LT-x-5      the engine, then the run on it
  slot ~2   LT-m-1                   the manifest only, disjoint
```

`fanout: 2 slots over 3 cells, cap 8, reason: LT-x-5 RUNS the engine LT-e-6 repairs, so they queue on one
slot; the manifest entry touches no engine file and runs beside them; levels L0 = {LT-e-6, LT-m-1},
L1 = {LT-x-5}.` **`LT-x-5` IS SPAWNED ONLY AFTER `LT-e-6` DRAINS AND ITS TWO CONFORMANCE ARMS READ PASS** --
R-82: a run on an unmeasured engine yields a green meaning the engine RAN, not that it was RIGHT.

### 15.2 THE FIXED INPUT, AND THE FOUR RULES IT IS BUILT ON

`deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/` -- `R4_BASE.json` (the ONE carrier) and `check_lt_r4.py`,
10 real arms and a 21-arm self-test with 8 positive-satisfiability arms, ruff clean.

1. **THE COVERAGE CORES ARE IMPORTED FROM ROUND 3, NEVER RE-IMPLEMENTED** -- `check_lt_r3.py` is imported by
   path and `core_cov_shape/floor/named` and `floor_now` are CALLED. A second copy of a grading rule is a
   second thing to drift, and the self-test asserts the import itself.
2. **A RE-POINT MAY ADD AND MUST NOT SILENTLY REMOVE.** `e6-no-loss` compares per-node_type `involved`
   against round 3's measured figures (LAMBDA 67, IAM_ROLE 46, S3Key 154, ...) and admits a DROP only when
   the record NAMES the node and the leg that used to reach it.
3. **THE ROUTING LESSON IS BUILT IN** (`S23`/`S29`): the walk output is named `e6.lgctfm-contract.json`, so
   the estate's path-router routes it. The defect that broke round 3's `e5-schema` cannot recur.
4. **THE STALE-PROOF BAR** (`S32`) watches BOTH `r4`'s and `r3`'s fixed inputs -- this checker RUNS r3's
   cores, so an r3 edit moves a round-4 arm's meaning exactly as an r4 edit would.

**WIRING AT THE CUT: 8 of 10 arms FAIL** for their measured reasons (no `cloud.inventory.*` entry; 128
entries where 129 is the bar; the method note still names `comp-iam role`; no hand-surface treatment; no
walk output; no post-cut run). **TWO ARE GUARD-SHAPED AND READ PASS, DISCLOSED:** `x4-no-registry-move` and
`r4-stale-proofs`.



## 16. v1.6 -- THE ROUND-5 RECUT (2026-09-19, `2.0.0_SA_COO~G`), on the L10 round analysis @`abea09f936`

**Input.** `LGIC_LGCTFM_ROUND4_ANALYSIS.md` @`abea09f936` (msg 98152). Round 4 STANDS; no PRD addendum owed;
endpoint outcomes unchanged. The recut is ONE cell and the analysis names its shape: **a MEASUREMENT cell,
not a repair cell.**

### 16.1 THE CELL -- 1

| cell | id | what it does | serves | rows |
|---|---|---|---|---|
| the bucketless keys | `LT-m-2` | measures WHICH producer writes an S3Key with no bucket and HOW MANY producers there are -- and repairs nothing | FWD-1 | `LGIC_LGCTFM-W<n>-S<k>` |

⛔ **WHY MEASUREMENT AND NOT REPAIR, in the analysis's own words:** *the shapes are plausibly TWO causes, and
a cell that assumes one remedy will make the NUMBERS agree rather than the DATA.* A remedy is the next
round's question.

### 16.2 THE POPULATION AT THE CUT, AND WHERE THIS SEAT'S MEASUREMENT DISAGREES WITH THE ANALYSIS

Measured from the round-4 run's own contract at `a25a11ab75`, NOT inherited: 404 contract rows, **154
S3Key**, all with a string path; leading segment after `s3:` is `opal-data-bd` 130, `platinum` 12, `gold`
10, `silver` 1, `blackdiamond` 1 -- so **24 of 154 resolve to no bucket.**

⚠ **The analysis calls the 24th row a malformed single-colon `s3:`. In the run this seat read there is NO
bare `s3:` row:** the 24th is `s3:blackdiamond/49f/_ops/pull_state.json`, FIRM-prefixed. The total and the
tier split (12/10/1) agree exactly; only that row's characterisation differs -- **a different shape with a
plausibly different producer.** The disagreement is written into the order so the cell HUNTS rather than
CONFIRMS, and so that a bare `s3:` row in a run this seat did not read is still findable.

### 16.3 THE BAR THIS ROUND'S CRITERIA WERE BUILT AGAINST

⭐ The CTO's bar from round 4, binding at CUT time: **can a CORRECT artifact satisfy this? Where the honest
answer is no, THE CRITERION IS THE DEFECT, NOT THE CELL.** Round 4 shipped FOUR criteria no correct record
could satisfy, and in each the cheapest satisfying move was to damage something -- up to reverting another
project's commit.

So every round-5 criterion was checked against a **hand-built CORRECT record** before the cut, and that
record is driven in the checker's own self-test as a POSITIVE-SATISFIABILITY arm (`_correct()`): the bar is
EXERCISED, not promised. Two consequences visible in the arms:

1. **An UNATTRIBUTED row is admissible when NAMED with its reason.** A cell that genuinely cannot reach a
   producer must be able to say so without fabricating one; what the arm refuses is SILENCE -- a row in
   neither list. A criterion demanding attribution of every row would be precisely the unsatisfiable shape.
2. **`s41-no-repair` grades the CELL'S OWN COMMITS BY AUTHOR**, carried forward from `W1-S39` rather than
   re-learned: another seat's registry commit is excused and PRINTED, never charged to this cell.

### 16.4 THE VINTAGE FIELD LANDS HERE

`1.0.0_SA_CTO` ADDENDUM 3 @`b1693a5b79` ruled the per-proof fixed-input vintage FIELD into **round 5's
carrier**, and this is that carrier. `record.fixed_inputs_at_pin` maps each fixed input the cell invoked to
the COMMIT it invoked it at, and `r5-vintage-field` requires both fixed inputs to be named AND each commit
to RESOLVE against its path. ⭐ This is what retires the sweep: **an arm that walks a log from a pin can
always be aimed at the wrong window; a proof that carries the commit of the input it invoked cannot be.**


### 16.6 THE ROUND-5 CLOSE -- drained @`c70d22c3a8`, five of five PASS, and the analysis's own characterisation FALSIFIED

`LT-m-2` is terminal and verified at its branch tip `ba22177c0a` AND again at the merged tree: `s41-population`,
`s41-producers`, `s41-no-repair`, `r5-vintage-field`, `r5-stale-proofs` all PASS, `selftest-arms` reads
`PASS-ARMS-DISCRIMINATE`, proof VALID (rc=0), nothing written outside the grant. **No rows filed, and the
cell says why: no criterion an honest correct record could not satisfy, and no row needed the `unattributed`
escape.** The bar held from the other side.

**THE MEASUREMENT, and it is the round's whole product:** 24 of 154 S3Key rows resolve to no bucket
(denominator 404 contract rows), **matching the issuer's cut-time count exactly** -- 23 tier-prefixed (gold
10, platinum 12, silver 1) and 1 firm-prefixed.

⭐ **THE ANALYSIS'S 24th-ROW CHARACTERISATION IS FALSIFIED WITH A DENOMINATOR.** The cell hunted the bare
`s3:` shape across **all 6 runs under the only workflow home -- 0 found in any run, 6 of 6 swept.** The
issuer's cut-time disagreement is therefore not a one-run artifact: no measured run has ever carried that
shape. The order told the cell to HUNT rather than CONFIRM, and hunting is what produced the negative with
its denominator instead of a shrug.

**TWO PRODUCERS, BOTH INSTRUMENT-ATTRIBUTED, ZERO UNATTRIBUTED:**

1. `lib/opal_lgctfm.py:374-380` (`parse_aws_walk()`) plus `:956-964` (`resolve()`'s ambiguous-candidate
   fallback) -- **23 tier-prefixed rows.** Attributed by RUNNING `comp-find --corpus aws` on all 23 bare
   keys (each returns three same-name S3Key candidates) and `comp-kuzu` MATCH on all 23, confirming
   `props.source='portal-stitch'`, `origin_reason='ambiguous-across-firms'`, `arn=''`.
2. `lib/opal_lgctfm.py:929-930` (kuzu-native ingestion inside `discover_involved()`) -- **the 1
   firm-prefixed row**, `R-0060`, `origin_reason='no-canonical-s3-key'`.

⭐ **THE ANSWER TO THE ANALYSIS'S REAL QUESTION IS NEITHER "ONE" NOR "TWO":** the two shapes come from
**different code sites** -- two producers by the cell's own definition -- but **both trace to the SAME
upstream root**: the served graph's portal-stitch S3Key ingestion leaves `arn` empty whenever it cannot
resolve a single firm-writer bucket, and the shape difference is a DOWNSTREAM BRANCH (ambiguous name-count
vs unique) rather than two independent external causes. **That is exactly the distinction the analysis cut
a measurement cell to protect** -- a repair cell would have written two fixes for one root, or one fix for
what looked like two.


## 17. v1.7 -- THE ROUND-6 RECUT (2026-09-19, `2.0.0_SA_COO~G`), on the L10 round-5 analysis @`cf0cf68868`

**Input.** `LGIC_LGCTFM_ROUND5_ANALYSIS` @`cf0cf68868` (msg 98202). Round 5 STANDS; no PRD addendum owed;
scope 0 open of 155. ONE cell.

### 17.1 THE CELL -- 1, AND THE TRAP THE ANALYSIS NAMED WITH IT

| cell | id | what it does | serves | rows |
|---|---|---|---|---|
| one repair or two | `LT-e-7` | ESTABLISHES whether a single repair at the portal-stitch ingestion removes BOTH classes of bucketless row -- and lands nothing | FWD-1 | `LGIC_LGCTFM-W<n>-S<k>` |

⛔ **The recut's own sentence:** *the record says 'plausibly', which is a hypothesis the round EARNED, not a
finding; **a cell that assumes it will report agreement rather than measure it.*** Round 5 established the
population, the two sites and the instruments. It did NOT establish that one repair reaches both.

### 17.2 WHY THE ANSWER MATTERS, WHICH IS WHY THE ROUND IS WORTH ITS COST

If the hypothesis holds, the remedy is one change at one site. ⭐ **If it does not, a single-change remedy
ships a fix that LOOKS COMPLETE AND LEAVES A CLASS BEHIND -- and the leftover class is the one nobody
re-measures, because the count moved.** That is the failure this round exists to make impossible, and it is
cheaper to measure now than to discover from a register that already reads clean.

### 17.3 THE BAR, WITH THE SHAPE IT TAKES HERE

The CTO's cut-time bar is *can a CORRECT artifact satisfy this?* -- and in a round whose job is to test a
hypothesis the bar has a specific form: **EVERY VERDICT VALUE MUST BE REACHABLE.** `ONE_REPAIR`,
`TWO_REPAIRS` and `UNDETERMINED` each pass the verdict arm on their own evidence, proven by ONE POSITIVE
ARM EACH in the checker's self-test. ⛔ **A criterion that only passed on `ONE_REPAIR` would be an
instruction to confirm the hypothesis**, which is precisely what the analysis forbids -- and it is the
cheapest way for a round like this to produce a comfortable answer instead of a true one.

Two refusals make the arm bite rather than merely permit: `ONE_REPAIR` is REFUSED on the counts while either
class still carries rows after the change, and any verdict whose evidence names only ONE class is refused,
because the question is about BOTH sites.

### 17.4 WHAT THIS ROUND DOES NOT CLAIM

- It does **not** land a repair. The engine has no writer; `e7-no-landed-repair` grades the CELL'S OWN
  commits by author (`W1-S39`'s shape), so another seat's commit there cannot fail this cell.
- It does **not** presume the shared root is real. Round 5's sentence is an INHERITED UNIVERSAL under Rule
  24's new clause @`cf0cf68868`, and this round is cut to EXERCISE it rather than restate it.
- It does **not** touch the 130 S3Key rows that resolve to a bucket.

### 16.5 WHAT THIS ROUND DOES NOT CLAIM

- It does **not** repair a single bucketless row, and it does not name a remedy.
- It does **not** decide whether the tier-prefixed and firm-prefixed shapes share a producer -- that is the
  measurement's OUTPUT, and pre-deciding it is the failure the analysis names.
- It does **not** touch the engine, the registries or `LEGACY_SERVED_PATHS.json`.
- It does **not** re-open round 4, whose three cells stand as graded.

### 15.4 THE ROUND-4 CLOSE -- three cells drained, and FOUR of this seat's own arms were repaired mid-round

| cell | drain | arms at the MERGED tree | proof |
|---|---|---|---|
| `LT-m-1` | `b238df04d5` | `m1-entry`, `m1-untouched`, `r4-stale-proofs` PASS | VALID (rc=0) |
| `LT-e-6` | `9ac7b0b2c3` | `e6-sources`, `e6-handsurface`, `e6-coverage`, `e6-no-loss`, `r4-stale-proofs` PASS | VALID (rc=0) |
| `LT-x-5` | `5755205bed` | `x4-run`, `x4-floor`, `x4-no-registry-move`, `r4-stale-proofs` PASS | VALID (rc=0) |

**What the round was for, and it landed.** The engine is R-81-conformant on both halves `S30` measured
NON-CONFORMANT: the `iam_grant` leg reads the LIVE plane through `comp-iam reconcile` (its own report:
`live roles (census) 256 | TF-parsed 210 | matched 206`), and the hand surface is GUARDED by `comp-lambdamap`
with 12 findings in 2 drift classes. ⭐ **The second-order tell is sharper than the count:**
`granting_roles_not_in_the_live_graph` is now EMPTY where round 3 had to carry `opal-49f-value-parity` as a
declared-but-not-live granting role -- **a result a live-plane read cannot produce by construction.**
Involved **381 -> 402**, seven node types grew, twelve held, **ZERO dropped**. The manifest carries exactly one
`cloud.inventory.*` entry, 128 -> 129, with the pre-existing digest `697f4e9d80df` unchanged. The real run
`20260919T034609Z-c28c728` accounts **90 of 90** floor nodes (81 rowed + 9 excluded + 0 unaccounted).

⛔ **FOUR OF MY OWN ARMS GRADED THE WRONG OBJECT, AND EVERY ONE WAS FOUND BY THE WORKER IT WAS GRADING.**
Not one was worked around; each arrived as a BLOCKING row with its discriminator already measured.

| row | the arm | what it graded | what it should have graded | repair |
|---|---|---|---|---|
| `S35`/`W1-S88` | `r4-stale-proofs` | a window that counted its own mint | the proofs that could BE stale | `1df2481ca0` |
| `W2-S35` | `m1-entry` | a status vocabulary the file has never admitted (intersection **0** of 127) | the manifest's own enum | `1d4df2c115` |
| `W1-S35` | `e6-sources` | every mention of a refused tool, including Andrew's LEDGER naming it as refused | the DESIGN half only | `21a163f492` |
| `W1-S39` | `x4-no-registry-move` | the whole TREE, so another project's commit failed my cell | the commits THIS CELL authored | `d08be0b693` |

⭐ **THE COMMON SHAPE, STATED ONCE: AN ARM THAT GRADES TEXT, A NUMBER OR A TREE INSTEAD OF THE CLAIM.** In every
case a CORRECT record could not pass, so the cheapest satisfying move was to damage something -- fabricate a
proof path, write a status the file forbids, delete a truthful record, or **revert another project's work.**
`W1-S39` is the worst of the four for exactly that reason: its cheapest green costs a seat that is not even in
this round.

**Two more of mine, repaired without a row because the CTO's analysis named them first** (@`84b02d1573`):
`proofs_at_risk()` returned an EMPTY SET on a failed `git ls-tree` -- and empty is the value that PASSES at a
mint, so an instrument failure was indistinguishable from a clean one -- and the commit list was a per-path
concatenation whose `[-1]` was the oldest of the LAST path only. Both at `eda1e967d0`, the first with a LIVE
positive control that hands the real function a bogus commit-ish and requires it to raise.

**No pinned proof was rewritten.** `LT-m-1`'s instance still records `AC1` FAIL and `LT-x-5`'s still records
`AC3` FAIL, each at its own vintage -- the UNDERSTATE direction of the `S32` bar -- and the issuer's re-runs at
the merged trees are recorded in `S36`, `S37`, `S38` and `S39` rather than by editing a worker's artifact.

### 15.3 WHAT THIS ROUND DOES NOT CLAIM

- It does **not** close FWD-1. `1.0.0_SA_CTO` re-grades the outcome at L10 against its ACCEPT.
- It does **not** build the consumer walk: that is `4.0.0_SA_CRO`'s brief and `1.0.0_SA_CTO`'s carrier.
- It does **not** carry `W1-S24`, `W1-S25` or `S21`: the analysis ROUTED all three out of this project.
  `W1-S25` has a SCHEDULED ARMING -- the day the commit gate's advisory flips -- and is the one that cannot
  be left to be rediscovered; it is named here so the routing is visible from this project's own record.
- It does **not** move FWD-4, which stays APPLIED on Andrew's own read.
---

## 18. v1.8 -- THE ROUND-7 RECUT (2026-09-19, `2.0.0_SA_COO~G`), on the L10 round-6 analysis @`ed073a4d48`

**Input.** `1.0.0_SA_CTO`'s round-6 analysis @`ed073a4d48` (msg 98235). **Round 6 STANDS**; `E7R6-AC7`
PASS accepted; no PRD addendum owed; endpoint outcomes unchanged; scope 0 open of 26 at the cut.
**The analysis ADOPTED this seat's ranking and MADE the one decision this seat handed up.**

### 18.1 THE CELLS -- 3, AND THE NON-PAIRING NOW BINDS THE CRITERION

| cell | id | what it does | serves | rows |
|---|---|---|---|---|
| the node-type population | `LT-n-3` | measures which `node_type`s the engine ACTUALLY emits against the schema enum, BY SUBTRACTION both ways -- and decides the fork for nobody | FWD-2 | `LGIC_LGCTFM-W<n>-S<k>` |
| the gate scope | `LT-g-1` | measures WHICH paths `.tools/naming-gate.py` refuses, by which predicate at `file:line`, on what BASIS, with a path it ADMITS | FWD-2 | `LGIC_LGCTFM-W<n>-S<k>` |
| the remediation route | `LT-r-3` | gives every unmoved remediation row a NEXT ACT or an explicit retirement -- and remedies none of them | FWD-2 | `LGIC_LGCTFM-W<n>-S<k>` |

**Levels.** All three at L0. `fanout: 3 slots over 3 cells, cap 8`. No dependency edge: three disjoint
deliverable directories, three disjoint read surfaces, and **no arm reads a second cell's record.**

⛔ **THE INSTRUCTION THAT SHAPES EVERY CRITERION HERE**, `1.0.0_SA_CTO` verbatim: *"AND 'DO NOT PAIR'
BINDS THE CRITERION, NOT ONLY THE CELL. `S106` is that instruction defeated one level down: two
correctly separated cells re-coupled by a shared grading arm that ANDs both."* So the two round-wide
arms (`r7-vintage-field`, `r7-stale-proofs`) grade **the records PRESENT IN THE CHECKOUT** -- a worker's
worktree carries exactly its own, the merged tree carries all three -- and an EMPTY population is
REFUSED rather than vacuously passed. **That is `S106`'s repair carried into the cut instead of
re-learned after it**, and four of the checker's arms drive that WRAPPER, which is the thing the
previous round's 28 arms could not see.

### 18.2 `LT-n-3` -- THE MEASUREMENT THAT DECIDES NOTHING

`W2-S2` has been ARMED and BLOCKING since round 2 and rounds 4, 5 and 6 did not move it (`S44`). The
analysis: *"Cut it as a MEASUREMENT of which node types the engine ACTUALLY emits against the enum's
33, read BY SUBTRACTION from the emitted set, not by checking the ones anybody remembers ... The fork
(widen the enum vs refuse at the producer) is decided ON that measurement, not before it."*

BOTH sets are denominators and BOTH differences are recorded: `emitted_minus_declared` (the violation
class) and `declared_minus_emitted` (**a finding, not a defect claim**). **The arm RE-DERIVES both from
the record's own lists** and refuses a stated difference the lists do not support -- the one thing a
reader cannot check without re-deriving it. ⭐ **A ZERO answer PASSES**, with its own positive arm: the
enum may have moved since round 2, and a bar that only passed on a violation would be an instruction to
find one.

### 18.3 `LT-g-1` -- THE REFUSAL, PLUS THE CONTROL THAT MAKES IT MEAN SOMETHING

`W2-S1` is ARMED and BLOCKING with **`1.0.0_SA_CTO` as its disarm owner**, so this cell measures and
proposes no gate edit. Beyond the refused set it records the refusing predicate at `file:line`, a
`gate_pin` (the gate is another seat's LIVE artifact and moves), and the **REFUSAL BASIS --
`FILENAME` / `PATH` / `CONTENT`, exactly one -- which is the field that decides whether a RENAME lapses
the guard silently.**

⛔ **AND AN ADMITTING CONTROL IS MANDATORY: without a path the gate ADMITS, a scoped guard and a gate
that refuses everything read IDENTICALLY.** The arm also refuses a control whose path appears in the
refused list.

⚠ **ONE RESIDUAL IS DISCLOSED AT THE CUT RATHER THAN DISCOVERED LATER:** the arm requires a NON-EMPTY
refused set, so if the gate has since been widened and refuses nothing, **a correct artifact cannot
satisfy `AC1`.** The order tells the worker to file that BLOCKING instead of manufacturing a refusal,
and names it as the ISSUER's defect to fix. That is the `S106` lesson applied forward: **a red must
name the act that clears it, and a red no act of the cell's can clear must say so.**

### 18.4 `LT-r-3` -- THE ROUTE, AND THE INHERITED NUMBER MEASURED BEFORE IT SHIPPED

The analysis made the call this seat handed up: **CENSUS-AND-ROUTE, not fix-them-all** -- *"nineteen
unrelated remedies in one order"* is not a cell.

⭐ **THE NINETEEN IS AN INHERITED COUNT AND THIS SEAT MEASURED IT AT THE CUT**, over `REMEDIATION_v1.md`,
denominator **35 rows**: *not closed* = **23**; *not closed AND round <= v4* = 20; *not closed AND
`disarm` empty* = **19**; *INERT and not closed* = **19**. **Nineteen is real under TWO predicates and
twenty-three is the broader unclosed set** -- the number is not wrong, it is PREDICATE-DEPENDENT. So the
arm refuses a record with no stated predicate, and the cell re-measures at its own write time.

⚠ **AND ONE PREMISE OF THE FRAMING IS ALREADY SATISFIED: 35 of 35 rows carry a non-empty `owner`.** So
"each row gets a named owner" is not the gap -- **THE GAP IS THE NEXT ACT**, and the order says so, so
the round is not spent re-assigning owners that already exist.

`unroutable` is explicitly admissible with a reason and has its own positive arm: **inventing a next act
for a row nobody understands is worse than saying so.** The route is EVIDENCE -- the remediation rows
stay `3.0.0_SA_CVO`'s to write (R-19).

### 18.5 THE NEW BAR THIS ROUND CARRIES

`1.0.0_SA_CTO` adopted `S43`'s carrier over this seat's weaker version: an order permitting an
out-of-repo instrument names where it LANDS **and its FIXTURES cite the committed measurement each one
encodes** -- *"an instrument whose fixtures cite nothing is UNGRADEABLE EVEN WHEN PRESERVED PERFECTLY."*
Its sibling from the same analysis: **the record names every site where the instrument DIVERGES from the
code it models, and what each divergence ASSUMES** -- round 6's script copied three sites verbatim and
REWROTE a fourth, and the rewritten site is by construction the interesting one. All three orders carry
both halves. **No cell here needs an out-of-repo instrument**; each measures the live artifact directly.

### 18.6 FIXED INPUTS

`deliverables/2.0.0_SA_COO~G/fixed_inputs/r7/` -- `R7_BASE.json` (**the ONE CARRIER, S85**; each order
quotes ONLY its own cell's half) and `check_lt_r7.py`: 5 real arms, **34 self-test arms with 10
POSITIVE-SATISFIABILITY and 4 driving the WIRING**, ruff clean.

**WIRING AT THE CUT**, and each order states WHICH ACT CLEARS EACH RED: `n3-population`, `g1-scope`,
`r3-route` and `r7-vintage-field` **FAIL** and are cleared by **that cell alone**; `r7-stale-proofs` is
**GUARD-SHAPED and reads PASS** with an empty window.

---

## 19. v1.9 -- THE ROUND-8 RECUT (2026-09-19, `2.0.0_SA_COO~G`), on the L10 round-7 analysis @`f818ebd12b` and `3.0.0_SA_CVO`'s S49 @`938ea238ed`

**Input.** Round 7 STANDS; all three judgment criteria PASS; no PRD addendum owed; scope 0 open of 29.

### 19.1 THE CELL -- 1, AND ITS ORDER IS THE FINDING

| cell | id | what it does | serves | rows |
|---|---|---|---|---|
| the routed-row liveness re-read | `LT-l-1` | re-reads EVERY routed row at HEAD and answers one question per row: is the condition it describes STILL TRUE? | FWD-2 | `LGIC_LGCTFM-W<n>-S<k>` |

⛔ **WHY MEASUREMENT AND NOT REMEDY.** `S49`: *"A ROW IS DISARMED BY AN ACT BUT IS ONLY OBSERVED TO BE
DISARMED BY A READ, AND NOBODY RE-READS A ROW THEY DID NOT FILE ... THE COST IS NOT THE STALE ROW, IT IS
THE WORK DONE AROUND IT ... round 7's `LT-g-1` carried a criterion no correct artifact could satisfy AS A
DIRECT CONSEQUENCE."*

⭐ **THAT CRITERION WAS MINE.** Round 8's input is a set of ROUTED ROWS -- exactly the shape that produced
it. **Cutting remedies against them without re-reading liveness first would repeat the defect in the round
convened to learn from it.** So the remedies are round 9's, cut on this measurement rather than on the
route's vintage.

### 19.2 THE COUNT IS AN OWNERSHIP COUNT, MEASURED BEFORE THE CUT

The analysis says *"the 18 rows routed to `2.0.0_SA_COO~G`"*. Measured over `REMEDIATION_ROUTE_R7.json`,
**denominator 23**: **18** name this seat as owner, but **only 11 are ACTS** -- the other 7 carry
`next_act = RETIRE`, whose act is a DISPOSITION and not work. **EIGHTEEN IS THE OWNERSHIP COUNT**, and a
cell taking it as its population would carry a subset measurement as a population -- the third instance of
that shape in this project. The block is a CONTROL ON THE FRAMING; the cell re-measures at its own write
time.

### 19.3 WHAT THE ARM GRADES, AND WHAT IT REFUSES TO

⭐ **THE DIRECTION OF THE ANSWER IS NEVER GRADED.** All-STILL-LIVE passes; all-ALREADY-REMEDIED passes and
is **the more valuable result**. A bar leaning either way would be an instruction, and the previous round
already paid for one wrong lean.

⛔ **EVERY VERDICT CARRIES WHAT WAS READ AT HEAD.** A row re-classified from the route record's own prose
is not a re-read -- it is the route quoted back, which is the move that produced the cost. `ALREADY-REMEDIED`
additionally requires `closed_by`, because *"it looks fine now"* is the read that let the last one go stale.

⚠ **AND THE PIN-DETECTOR WAS ITSELF DEFECTIVE AT FIRST DRAFT.** It asked `any(ch.isdigit())` and was
satisfied by the **"7" in `REMEDIATION_ROUTE_R7.json`** -- a detector that cannot tell a commit from a
filename. **Caught by this round's own `MUTANT-source-record-unpinned` arm before the order shipped**, and
repaired to require a hex run of at least 7.

### 19.4 WHAT THIS ROUND DOES NOT DO

It remedies nothing, disarms nothing (a disarm is the row owner's act, R-19), and **does not build S49's
recommended control** -- that is assigned to `1.0.0_SA_CTO`, and S49 says in terms that a gate, a checker
or a monitor is not asked for. Several routed acts name `check_lt_r1.py`, a PINNED input of a CLOSED round
-- **the identical hazard `LGIC_ENFORCE` round 16 is handling additively.** The cell RECORDS that
collision; it does not resolve it.

### 19.5 FIXED INPUTS

`deliverables/2.0.0_SA_COO~G/fixed_inputs/r8/` -- `R8_BASE.json` (**the ONE CARRIER, S85**) and
`check_lt_r8.py`, ruff clean, whose `selftest-arms` prints `VERDICT: PASS-ARMS-DISCRIMINATE` and its own
counts. ⛔ **The order does not quote those counts** (`W1-S37`, third consecutive round).

**WIRING AT THE CUT**, each red naming the act that clears it: `l1-liveness` and `r8-vintage-field`
**FAIL**, both cleared by this cell alone; `r8-stale-proofs` is **GUARD-SHAPED and reads PASS**.


---

## 20. v1.10 -- THE ROUND-9 RECUT (2026-09-19, `2.0.0_SA_COO~G`), on the L10 round-8 analysis @`b24a81c4d3`

**Input.** `1.0.0_SA_CTO`'s round-8 analysis @`b24a81c4d3` and `3.0.0_SA_CVO`'s L9 @`2bb57f01f8`.
**Round 8 STANDS** -- `L1R8-AC4` PASS, five rows GRADUATED (`S50`-`S54`), no PRD addendum owed, scope 0
open of 30 at the cut.

⚠ **A CITATION CORRECTION AGAINST s.19's OWN HEADER.** That header calls the controlling row
*"`3.0.0_SA_CVO`'s S49"*. **It is `1.0.0_SA_CTO`'s.** Measured: FOUR rows answer to `-S49` across the
LGIC channels, and `LGIC_LGCTFM-S49` reads `surfaced_by: 1.0.0_SA_CTO` in both its investigation and
remediation carriers; the CVO GRADUATED it at round 8's L9 and did not surface it. ⭐ **The cause is
worth more than the correction: I read that row inside commit `938ea238ed`, which IS a CVO commit, and
attributed the row to the seat whose commit I read it in. On a shared append-only channel the COMMIT
AUTHOR IS NOT THE ROW'S `surfaced_by`.** s.19 is not rewritten -- it stands at its vintage.

### 20.1 THE CELL -- ONE, AND THE POPULATION IS THE SEVEN

| cell | id | what it does | serves | rows |
|---|---|---|---|---|
| remedy-and-disposition | `LT-m-1` | executes the routed acts that are executable and dispositions ALL SEVEN `STILL-LIVE` rows with a class and a reason | the round-7 routing table's remaining live half | `S18` `W1-S21` `S26` `W1-S30` `S33` `W2-S36` `S41` |

The analysis s.5 item 3 reads *"Nothing else."* One cell, one worker, no second lane.

### 20.2 ⛔ THE SEVEN ROUTED ACTS ARE NOT SEVEN OF THE SAME THING, AND TWO CANNOT BE DONE AS WRITTEN

Measured at the cut, reading all seven `next_act` fields at HEAD:

| class | rows | why |
|---|---|---|
| executable code remedy on a LIVE library | `W1-S30`, `S33` | `lib/opal_lgctfm.py`, `lib/lgctfm_render.py` -- not pinned, tests exist |
| **UNEXECUTABLE AS ROUTED** | `S18`, `W1-S21` | both ask for arms in **`check_lt_r1.py`, a CLOSED round's PINNED fixed input** |
| NOT WORK -- a DECISION | `S41` | *"the engine's owner decides"* |
| NOT A WORKER'S ACT | `W2-S36` | a mechanics/law edit, whose broadcast surface a worker cannot discharge |
| THE ISSUER'S OWN ACT | `S26` | verify-then-disarm, and a disarm is the row owner's under R-19 |

⭐ **THE COLLISION IS THE FINDING AND THE ROUTE DID NOT SEE IT.** `LGIC_ENFORCE` round 16 ruled -- and
its L9 and L10 upheld -- that an annotation is recorded by an **ADDITIVE SIBLING** and **never** by an
edit to a pinned fixed input, because editing it after that round's proofs pinned against it is the
stale-proof hazard. **Two routed acts ask for exactly that edit.** Round 8's liveness cell RECORDED the
collision and correctly did not resolve it; this cell classes it and still does not resolve it.

⚠ **`UNEXECUTABLE-AS-ROUTED` IS THE CLASS A CELL COULD HIDE UNFINISHED WORK BEHIND**, so the checker
makes it the costliest to assert: a row in that class must NAME the blocking ruling **and** a pinned
`fixed_inputs/` path the act would edit, or the arm FAILS.

### 20.3 EVERY VERDICT LINE STATES ITS BASE SHA

The analysis s.4 adopts the CVO's sentence as the ruling: **"A LIVENESS CELL CANNOT BE ISOLATED --
ISOLATION IS EXACTLY THE THING IT IS MEASURING AGAINST. The remedy is the CUT, not the worker: such a
cell runs IN THE SHARED TREE, or STATES ITS BASE SHA IN EVERY VERDICT LINE."**

This worker holds a worktree -- ⛔ **Rule 14b is NOT traded away; the carve-out is one cell class, not a
weakening of 14b** -- so the second branch binds, mechanically: **every row carries `base_sha`, and a
row without one FAILS.** A header-only sha is refused too, and a label (`HEAD`) is refused because **a
label is not a tree.** Round 8's 2-of-23 miss was invisible precisely because no verdict line said
which tree it was read in.

**And any liveness re-read uses the WINDOW method** (s.3): enumerate the commit window and inspect what
each commit touched, never a grep of commit SUBJECTS for a row id. ⭐ The CVO ruled against its own
instrument here -- a subject grep is an AUTHOR-COOPERATION instrument and returned **0 for `S42`**, the
row two seats confirmed was falsified.

### 20.4 THE JUDGMENT CRITERION QUANTIFIES OVER THE PARTITION

Taken from the round-8 analysis s.2, the bar-writing rule its own author took against himself: **when a
defect's mechanism is UNIFORM over a partition, the criterion quantifies over the PARTITION, not over
the bucket where the cost is highest.** `M1R9-AC4` therefore names **all five classes** -- a remedy
wrongly marked `EXECUTED` is exactly as bad as one wrongly marked `UNEXECUTABLE`, and last round both
misses landed in the one bucket the criterion did not name. **COST: one clause.**

### 20.5 WHAT THIS ROUND DELIBERATELY DOES NOT DO

- **Edit `check_lt_r1.py`.** Refused by name; the cell records the collision instead.
- **Disarm any row.** All seven name `2.0.0_SA_COO~G`, and an issuer's worker disarming rows that
  issuer routed is self-certification at two removes. `EXECUTED` records that the ACT was done; the
  DISARM stays the issuer's and the DISPOSITION stays `3.0.0_SA_CVO`'s at L9.
- **The `W2-S36` mechanics edit.** A law edit carries three surfaces including a same-turn broadcast,
  and a worker has no send tool -- so it is classed and routed, never performed here.
- **Anything outside the seven.**
