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
