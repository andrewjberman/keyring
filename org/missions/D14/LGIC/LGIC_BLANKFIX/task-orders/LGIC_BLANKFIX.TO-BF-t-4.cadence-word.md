# TO LGIC_BLANKFIX.TO-BF-t-4 -- round 1 BF-t-4: the cadence word -- a schedule's own expression gives its word, or the row is listed with the reason

<to_id>LGIC_BLANKFIX.TO-BF-t-4</to_id>
<project>LGIC_BLANKFIX</project>
<issued_to>0.9.0_WK_LGIC_BLANKFIX~4</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~G</workstream>

**Directive:** D14 | **Fabric:** laptop | **Decomp cell:** `BF-t-4` (`decompositions/LGIC_BLANKFIX_DECOMP.md`) | **outcome_ref:** FWD-1 (hop 5), FWD-4 (thin) |
**depends_on:** none

---

## WORKER FACE

### CONTEXT

**What the check is.** `python lib/opal_naming.py census --repo` reads names from the repository and grades each with
`grade(name, type) -> (verdict, canonical)`. `census_repo()` (`lib/opal_naming.py`) returns `(items, stats)`; each item is a dict
`{"plane": "repo", "type": <node type>, "current": <the name>, "where": "<repo-relative file>:<line>"}`. A canonical form may carry a
blank written in braces: `{system}`, `{cadence}`, `{source}`, `{scope}`. `grade()` raises `opal_naming.RaiseDefect` for a name it
cannot place. Import the library with `sys.path.insert(0, "lib")` then `import opal_naming`. Python 3.9 syntax only; ASCII only
in code and output; no new dependency.

**The root of this round** is `infra/aws/terraform/bd-pipeline/` read together with the Lambda source folders it deploys (at the cut:
`infra/aws/lambda/bd-pipeline/`). Measured at the cut on the repository plane: the root's `.tf` files give 96 graded names, 12 with a
`{system}` blank and 9 with a `{cadence}` blank; the source folder gives 37 graded names, 16 with a `{source}/{scope}` blank, and 6
names skipped by the cards in `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/NOT_JUDGED_R13.json`.

### THE CELL

`BF-t-4`, the thread's hop 5. The grammar ends a schedule's or an event rule's name with a cadence word. Where the current name
carries none, `grade()` prints `{cadence}`. The schema says that blank is filled "from the schedule". Nobody has measured whether a
schedule's own expression is enough to choose the word. You build the reader and you make that measurement.

**Facts you need.** The cadence vocabulary is `opal_naming._vocab().cadences`; at the cut it is `1min`, `5min`, `daily`, `hourly`,
`monthly`, `weekly` (read it from the library, do not type it). `opal_naming.census_tf_names(path, text)` returns the names a `.tf`
file declares with their type and `where`; the types here are `EVENT_RULE` and `SCHEDULE`. A resource's expression is its
`schedule_expression` attribute (`rate(...)` or `cron(...)`); an event rule may instead carry only an `event_pattern`. In the root
at the cut: `rate(15 minutes)` at `bd-49f-interim.tf:151`, several weekday-only crons (`MON-FRI`, `MON-SAT`), and one rule with an
`event_pattern` and no schedule at `bd-49f-session-chain.tf:246`.

**Build** `lib/opal_naming_cadence.py` (a new module; do not edit `lib/opal_naming.py`):

1. `word_for(expression) -> (word or None, basis)`. A word is returned ONLY when the expression fires on exactly that word's
   period with no other restriction: `rate(1 minute)` -> `1min`; `rate(5 minutes)` -> `5min`; once an hour, every hour, every day
   -> `hourly`; once a day, every day of the week -> `daily`; once a week -> `weekly`; once a month -> `monthly`. Anything else
   returns `None` with a `basis` that says why in plain words (for example "every 15 minutes: no cadence word for this period",
   "weekdays only: not every day"). `None` input (no schedule) returns `None` with the basis "no schedule expression".
2. `cadences(root) -> list[dict]`: one dict per `EVENT_RULE` or `SCHEDULE` name `census_tf_names()` finds in the root's `.tf`
   files, with `type`, `current`, `where`, `expression` (the literal, or `None`), `word`, `basis`, and `has_event_pattern`. Find
   the expression in the SAME resource block as the name. An expression that is not one literal string (a variable, a local) is
   `expression: None` with the basis "expression is not a literal".
3. A command line: `python lib/opal_naming_cadence.py root ROOT` prints one line per row and a last line
   `CADENCE-ROOT ok=True root=... rows=N decided=N undecided=N`, `ok=True` when `rows` equals the count of `EVENT_RULE` and
   `SCHEDULE` names `census_tf_names()` gives for the root's files (computed independently in the command) and
   `decided + undecided == rows`. `python lib/opal_naming_cadence.py estate` does the same over every root under
   `infra/aws/terraform/` and prints, last, `CADENCE-ESTATE ok=True rows=N decided=N undecided=N`, then nothing.

**Build** `lib/tests/test_opal_naming_cadence.py`, runnable as a plain script: a table of expressions and expected words covering
each of the six words, plus at least four that must return `None` (`rate(15 minutes)`, a `MON-FRI` cron, a twice-a-day cron, no
expression). Last line `CADENCE-TEST ok=True cases=N`.

**The measurement** (PRD contract C-CADENCE): in your report, the `CADENCE-ESTATE` line, and for the root every undecided row with
its expression and basis. You add no word to the vocabulary and you edit no schema: a row the expression cannot decide is LISTED.

### ACCEPTANCE

<criterion id="BF4-AC1" cell_refs="BF-t-4"><invocation>python lib/tests/test_opal_naming_cadence.py</invocation><expect>CADENCE-TEST ok=True</expect></criterion>
`BF4-AC1` -- the word is given only for an exact period, and four near-misses give none.

<criterion id="BF4-AC2" cell_refs="BF-t-4"><invocation>python lib/opal_naming_cadence.py root infra/aws/terraform/bd-pipeline</invocation><expect>CADENCE-ROOT ok=True</expect></criterion>
`BF4-AC2` -- every schedule and event rule of the root is read, the count checked against the real `census_tf_names()`.

<expected_criteria>BF4-AC1,BF4-AC2</expected_criteria>

Each invocation's LAST printed line is the line the expectation is matched against; print it exactly once, with `ok=True` only when
every assertion behind it held and `ok=False` otherwise.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit outside the grant.** No AWS call, no network call, no `terraform` command, no registry edit, no rename of any resource.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `LGIC_BLANKFIX-W4-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or
  the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does not block.

<paths>
lib/opal_naming_cadence.py
lib/tests/test_opal_naming_cadence.py
org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit: `lib/opal_naming.py`, `lib/tests/test_opal_naming.py`, `org/standards/NAMING_SCHEMA.json`, every file under `infra/logic/registry/`, every file under `infra/aws/terraform/bd-pipeline/` and `infra/aws/lambda/bd-pipeline/`, `infra/aws/lambda/ci/lambda-source-map.json`, `org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.md`. You also read every `.tf` file under `infra/aws/terraform/` for the estate measurement.

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_BLANKFIX/decompositions/LGIC_BLANKFIX_DECOMP.md</decomp_doc> (round 1), cell `BF-t-4`.
<owned_cells>BF-t-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF4-AC1, BF4-AC2. Instance at
`org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~4/LGIC_BLANKFIX.TO-BF-t-4.cadence-word.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BF4-AC1,BF4-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines and the `CADENCE-ESTATE` line whole; every undecided row of the root with its expression and basis; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches its surface.
comp-iam: DECLARED-NOT-APPLICABLE the cell reads policy names from .tf text and grants, attaches and simulates nothing.
comp-adversary: RUN -- a word chosen by rounding (a weekday cron called daily, a 15-minute rate called 5min) so that a person reading the schedule would disagree (the face fixes exact-period-only and AC1 carries four near-misses); a row dropped because its expression is a variable (listed with its basis; AC2's count is checked against census_tf_names); an expression read from a neighbouring resource block; BLIND: a schedule whose live expression differs from its .tf text.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD v0.2 @47ef4c98cc section 2 (THREAD); decomposition round 1 @f15f222030. Base dry-run at the cut: BF4-AC1, BF4-AC2 base FAIL as expected (files absent).
