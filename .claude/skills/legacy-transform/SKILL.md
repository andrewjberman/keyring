---
name: legacy-transform
description: Run the LGIC legacy-transform method on ONE legacy subject: walk its current state from the live AWS and trigger planes, compute the desired half from the builders, find forks from the desired twin, type and rank the tensions, emit the ordered plan, render both diagrams, and mark the subject in the three registries. The instrument moves nothing on the applied plane. Use on `/legacy-transform <subject>`, "transform X to canonical LGIC form", "what would X look like under the canon", "current state vs desired state for X", or before a migration, consolidation, bucket move or decommission of a pre-LGIC pipeline.
---

# /legacy-transform -- ad-hoc invocation of the LGIC legacy-transform method

**THE METHOD LIVES IN ITS OWN DOCUMENTS; THIS SKILL IS THE INVOCATION FRAME.** Never restate the
method from memory -- read these, in this order, and follow them:

> 1. `infra/logic/10_LEGACY_TRANSFORM.md` -- the method note: walk order, fork test, twin, tension,
>    plan, mark, coverage hole. It LEGISLATES NOTHING of its own -- every rule in it is cited to the
>    PRD's DECs, `02_DOCTRINE.md` or `08_TENSION_MAP.md`, and it names neither the run home nor the
>    run layout. Go to the PRD for law and to the run home's README for the layout.
> 2. `infra/logic/11_LGCTFM_CONTRACT_SCHEMA_RECORD.md` -- what every field MEANS (the Rule 24
>    four-postulate record the schema is authored FROM).
> 3. `org/standards/LGCTFM_CONTRACT.schema.json` -- the contract's shape; `additionalProperties:
>    false`, every fact a `$defs.cell`.
> 4. `org/missions/D14/LGIC/LGIC_LGCTFM/prd/LGIC_LGCTFM_PRD.md` -- DEC-1..DEC-14, the constitutional
>    record, and the two open outcomes.
> 5. `workflows/legacy_transform/README.md` -- the run home's own law (immutability, manifest, diff).

**Read the engine's verbs from `python lib/opal_lgctfm.py --help`, never from a page about it.** The
round-1 skill `/lgctfm` documented `walk` alone and was RETIRED on 2026-09-18 once three more verbs had
shipped past it; the PRD, the decomposition and the `LT-e-1` task order still name that path as a
round-1 deliverable, and those are frozen records (R-43), not a live pointer. This shim adds the
estate frame:

## Step 0 -- Scope the run

- **Subject:** ONE per run, named by its **registry key** (a `infra/logic/registry/scopes.json` or
  `systems.json` key), never a spelling. No subject given -> ask; the run cannot pin a vintage without it.
- **Seeds are the caller's boundary, not a derivation:** `--seed <bucket-or-prefix>` (repeatable) is
  where the walk starts. `forks` needs its own grammar, `--seed-loc bucket:prefix[:format]` -- a
  storage location, never a pair. The ledger is read for context; it does not supply the seeds.
- **Posture (DEC-13, the headline refusal): the instrument moves nothing.** Read-only against AWS and
  the repo; the only writes are the run directory and, at the mark, three registry files. No apply,
  no rename, no bucket mint, no sign-off.
- **This is for LEGACY subjects.** A NEW pipeline is built to the canon directly (Rule 30 + the LGIC
  builders); it does not come through here.
- **Pin the vintage triple first:** repo HEAD, the live graph's own `built:` stamp, and
  `registry_hash()`. Every number the run later publishes is read at that triple.

## Step 1 -- Execute: one command assembles a run

```
python lib/opal_lgctfm.py run --subject <registry key> --run-home-subject <dir name> \
    --seed <bucket> [--seed ...] [--seed-loc bucket:prefix[:format]] \
    --root workflows/legacy_transform [--plant-untypeable]
```

It allocates the run directory through `run_home.py new`, self-invokes `walk`, optionally folds in a
`forks` pass, calls `plan`, renders through `lib/lgctfm_render.py`, and refreshes `MANIFEST.md`.
Standalone verbs when a stage is re-run: `walk`, `forks`, `plan <run_dir>`.

- **Diagrams are not a second truth:** `python lib/lgctfm_render.py check <contract.json> --out <dir>`
  must report a fresh render equal to the files byte for byte. A hand-edited diagram is a defect.
- **Determinism:** `lib/tests/test_opal_lgctfm.py`. The NEGATIVE arm (a de-sorted copy of the engine on
  a scratch branch producing different files) fires BEFORE the sorted engine is trusted -- a
  determinism test whose negative arm has never fired is a constant.
- **`--plant-untypeable` stays OFF by default (R-36).** An ungraded node is CARRIED in
  `PLANT_UNTYPEABLE.json` with `NOT_COVERED` and COUNTED in the contract's `untypeable` cell -- never
  written into rows, and never fixed by widening the 33-value `node_type` enum.

## Step 2 -- Land at the ONE HOME

```
workflows/legacy_transform/<subject>/<run-id>/   VINTAGE.json contract.json flow.current.md
                                                 flow.desired.md plan.json plan.md PLANT.json
                                                 [PLANT_UNTYPEABLE.json HASHES.json MARK.json DIFF.md]
workflows/legacy_transform/<subject>/MANIFEST.md GENERATED -- never hand-edit
```

`run-id` = `<UTC YYYYMMDDTHHMMSSZ>-<repo-head[:7]>`. **A run directory that already exists is REFUSED
and left byte-identical; runs are never overwritten** -- a re-run at a new vintage is a NEW run.
Refresh the view and diff two runs:

```
python workflows/legacy_transform/run_home.py manifest --root workflows/legacy_transform --subject <dir>
python workflows/legacy_transform/run_home.py diff <runA dir> <runB dir>
```

The diff is keyed on tension identity, `<row_id>|<axis>|<kind>|<deciding_rules>`, never on prose: a
changed note alone stays UNCHANGED. **`run_home.py` has no `--check` and no self-test** (the
`atom_decomposition` sibling does) -- nothing will tell you `MANIFEST.md` has gone stale, so re-run
`manifest` yourself after every run, and re-run `diff` against the predecessor before citing "closed /
opened / unchanged".

## Step 3 -- The bars a runner actually gets wrong

The method note carries the mechanics. These are the ones this project paid for twice:

- **Every fact is a cell** `{value, status, evidence{instrument, blind_spot}}`. A resource no
  instrument saw is an UNMEASURED row, never a missing one; a `0` from an instrument that cannot see
  the path is UNMEASURED, never CONFORMANT. The blind spot travels on every row the instrument produced.
- **The desired half is computed, never typed** -- `address()`, `name()`, `grade()` verbatim. A builder
  refusal is a RAISE row naming the `missing_registry_row`, routed to LGIC_ENFORCE, never hand-patched.
- **A fork is two current rows whose desired form is ONE string**, found from the twin, never from name
  patterns. Both members non-conformant and the ledger silent -> the run returns the QUESTION and does
  not answer it. The negative control (a lookalike pair that must NOT fire) is a criterion of its own.
- **Tensions are typed on the closed set and ranked by the rule the run PRINTS at the top of the set.**
  The rule's own home is `infra/logic/08_TENSION_MAP.md` s.0 and it is emitted verbatim -- read it
  there, never retype the factor order from memory. Its four factors (`irreversible`,
  `client_facing`, `live`, `rules_colliding`) are each a MEASURED cell with its instrument, and
  `object_count` is the tiebreak. No weighting is added -- that would be a Rule 24 act. `live` is
  measured against `lib/trading_calendar.py`'s frontier, never a calendar day.
- **Both trigger APIs or the contract is refused** -- a denominator naming only `list-rules` or only
  `list-schedules` fails the schema.
- **Select by identity, never by position.** The graded run is the one carrying an R-40 `HASHES.json`;
  when that count is not exactly 1, REFUSE and print both numbers. `subject_runs()[0]` graded the wrong
  hand's file once already, and the repair that closed it missed one arm -- when a fix repoints HOW an
  object is identified, the unit of work is EVERY arm that identifies it, enumerated from the file.
- **Never base an arm on `git merge-base HEAD CLOUD`**, and run every arm in the SHARED checkout at HEAD
  before grading: an arm that passes only in the author's worktree certifies the checkout, not the work.
- **Beside every mutant arm, a simulated-correct arm that must PASS**, and make an empty input set an
  explicit printed FAIL. A mutant proves an arm CAN fail; it cannot catch a vacuous pass, and a false
  fail announces itself where a vacuous pass does not.
- **Print the denominator and what the count EXCLUDES**, and take the domain from the claim's
  population -- a census scoped to the run home, then written with the word "anywhere", reads as
  MEASURED and is not.
- **Pin every published number** to its artifact's content hash, name the instrument, and say that it
  hashes the COMMITTED bytes: `git hash-object` runs the EOL filter first, and on this autocrlf box a
  byte count from `wc -c` disagrees with the record -- size evidence is `git cat-file -s`.
- **A report to a decision-maker states a count with its denominator** ("1 of 179"), never a word
  ("the two rows"): a number invites the check a word does not.
- **The retired bare-name gold-script tracer is never called.** DEC-3 bans it by name and the method
  note repeats the ban; the live route for that question is `comp-estate`.

## Step 4 -- Mark, then route, never repair

- **The mark appends to exactly three registries** -- `infra/logic/registry/remediations.json`,
  `org/missions/D14/LGIC/LGIC_NAMING/deliverables/LEGACY_SERVED_PATHS.json`, and
  `infra/logic/registry/scopes.json` `bucket_aliases` -- under
  the subject's migration project, in the run's own commit, through `safe-commit` and the naming gate.
  A fourth mark is a Rule 24 act nobody has asked for. R-16: a registry edit is a deploy on every
  shipping generated view, so the mark commit prints the deploy gate's classification. R-35's
  naming-gate exemption covers the MINTED RUN DIRECTORY only, never the engine tree above it.
- **Everything the plan names is somebody else's act.** The packages are ATOM_DECOMP packages in R19's
  order; every served key that would move carries `never_widen_signoff_owed: true` -- NAMED here,
  SIGNED elsewhere. No package is executed; the run signs nothing.
- **Findings route, they do not get fixed here:** a builder gap -> LGIC_ENFORCE; a new tension found
  later -> a surprise row in the migration project's channel; a defect on an owner's surface -> that
  owner, via the COO.
- **Reproduction is by a DIFFERENT worker slot than the engine's author** -- a reproduction by the
  author is Rule 22 REPETITION, not corroboration.
- **A correction to a document already in a reader's hands lands BESIDE it**, with its own author line,
  never as a silent rewrite (`owned-paths` clause 4 refuses the in-place edit, and it is right).
- **Re-running a closed cell's arm can FAIL on live-builder drift, not on a defect** -- `grade()` moves
  under a frozen contract. Read any analysis at its date; take SCOPE from the register (`project.json`),
  not from a prior analysis's forward-carry.

## State of the method (read before citing it)

`LGIC_LGCTFM` (D14) is **active, not closed**: rounds 1 and 2 are CLOSED, REALIZED **8 of 10**, and a
round 3 must not be cut as another hardening round. Both open outcomes bar on acts OUTSIDE the engine:
**FWD-4** closes only on Andrew's own read of `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~3/ANDREW_CARD.md` (an
adjudication on his behalf, and any report standing in, do not close it); **FWD-6** closes when a real
migration's decomposition is cut from a run's plan (`ADVI_FIRMBKTS` at L5). Two rows stay ARMED: `S18`
(two vacuous-pass arms left unrepaired under R-43) and `W1-S21` (a non-re-derivable population).
Cutting more engine cells moves neither outcome.

## Cross-references

- Run home + its law: `workflows/legacy_transform/README.md`; project: `org/missions/D14/LGIC/LGIC_LGCTFM/`
  (register `project.json`, PRD, decomposition, surprise channel).
- Engine verbs: `lib/opal_lgctfm.py --help`; renderer `lib/lgctfm_render.py`; run home
  `workflows/legacy_transform/run_home.py`.
- **Hand the contract on through its own gate:** `python .tools/lgctfm-contract-check.py <contract.json>`
  -- rc=0 `ACCEPT`, rc=1 `HAND BACK` listing EVERY defect (bare value, missing trigger API, missing
  `evidence.instrument`, missing vintage), rc=2 usage. It fails CLOSED when `jsonschema` or the schema
  file is unavailable. `.tools/receiving-check.py <path>` is the dispatcher a consuming lane runs
  (route 1, label `lgctfm-contract`, the L5 hand-off). **Its `UNCHECKED` verdict does NOT raise the
  exit code** -- a contract whose path misses the route regex (a deeper run dir, a `contract.v2.json`)
  returns rc=0 with an UNCHECKED line, and UNCHECKED IS NOT ACCEPT. Read the verdict, not the rc.
- **Nothing in this method fires automatically.** No git hook, no commit gate and no HUD rail invokes
  any of it; every gate above refuses only when a person or the engine calls it.
- Name collisions that are NOT this method: `.tools/comp-transform` (a React dataflow tracer),
  `.tools/comp-legacywriter` (an S3 writer-contest lens), `.tools/safe-commit.legacy-golden.sh` (a
  frozen commit-queue regression fixture). Do not reach for them here.
- Siblings: `/atom-decomp` -- the plan's packages are its packages, and a run that needs deployed-truth
  rectangles belongs there; `/canonical-flow` -- Andrew's commission was "`/atom-decomp` and
  `/canonical-flow` combined", so use THAT skill to pick a project up at its limb and THIS one to
  transform a legacy subject; `/draw` -- the diagram house style the renderer emits.
