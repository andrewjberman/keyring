# TO LGIC_ENFORCE.TO-EN-r-7-r14 -- ONE RENDER PATH FOR EVERY COLUMN, NOT A FIX TO ONE COLUMN

<to_id>LGIC_ENFORCE.TO-EN-r-7-r14</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-19</issued_date>
<status>complete -- re-graded 2026-09-19 in worktree wk-lgic-enforce-14-1b (base 3948ba37d9) after LGIC_ENFORCE-S106 repaired check_en_r14.py's r14-vintage-field arm to grade records present in its checkout, and the drain (dda2125b35) landed EN-p-38's record on this branch: R7R14-AC1/AC2/AC3/AC4 all PASS by fresh output (this cell's own artifact unchanged, confirmed byte-identical to 37865221aa); R7R14-AC5 stays UNVERIFIABLE-BY-INSTRUMENT, routed to 3.0.0_SA_CVO at L9. proof_of_spec.json VALID rc=0 via proof-of-spec-check.py.</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` (ADMITTED; both halves SIGNED and current) | **Decomp cell:** `EN-r-7` (decomposition v3.13 s.0n) | **outcome_ref:** FWD-3 | **depends_on:** none -- **NOT paired with `EN-p-38`, which runs beside it**

---

## WORKER FACE

### THE CELL

`EN-r-7`. A REPAIR on how the round-13 population report RENDERS. `3.0.0_SA_CVO`'s `S101`, measured at L9:
the report renders a brace as a PARENTHESIS in the `current` and `where` columns only. Across 3264 table
rows the `canonical` column carries 1303 braces and 0 paren-wrapped tokens; the escaped columns carry 0
braces and 8 paren-wrapped tokens. **The same token renders one way in one column and another way in the
column beside it, so the table MANUFACTURES AN APPARENT DIFFERENCE between two cells that are EQUAL AT THE
VALUES.** What it cost is measured: the grader's first pass on the cause verdict's load-bearing evidence
returned **0 of 5** and would have been a FALSE FINDING against the cell. **The cost is borne by the
GRADER, not the author** -- every check of that evidence, run against the artifact the record points at,
returns a false negative.

⛔ **THE SHAPE OF THE REPAIR IS THE WHOLE POINT.** `1.0.0_SA_CTO`, round-13 analysis @`cf0cf68868`,
verbatim: *"cut it to make both columns render through ONE path, NOT to 'fix' the current column, **or the
asymmetry returns the next time a third column is added**."*

⭐ **READ THIS BEFORE YOU TOUCH ANYTHING -- THIS SEAT MEASURED IT AT THE CUT AND NEITHER `S101` NOR THE
ANALYSIS CARRIES IT.** The substitution is **DELIBERATE AND DECLARED**. `PLACEHOLDER_POPULATION_TABLE_R13.md`
lines 7-16 @`f658dc53cb` say so in their own words: the escaped columns are escaped **so that a pre-existing
literal template brace in the OBSERVED name is never double-counted**, leaving *"the `canonical` cell ... the
ONLY column left with real `{` `}` bytes"*; the column header literally reads `current(escaped)`.
**SO THE ESCAPING IS LOAD-BEARING: it is what let the round-13 arm identify the population by which column
carries brace bytes.** A repair that simply deletes it breaks that discriminator while LOOKING like a tidy
fix. That is why `AC1` requires a `population_discriminator`.

⚠ **AND IT DOES NOT MAKE `S101` WRONG.** The asymmetry is real, it produced a false negative for a real
grader, and **declaring a hazard in prose is not removing it** -- a reader checking the record's evidence
against the artifact still gets 0 of 5. Filed as `LGIC_ENFORCE-W2-S104`.

### WHAT YOU BUILD

1. **ONE RENDERER, AT ONE SITE, THAT EVERY COLUMN CALLS.** Name it `file:line`. **The arm does NOT dictate
   WHICH rule** -- escape every column, or escape none and solve the double-count another way; both PASS,
   and the self-test proves it with a positive arm for each. What the arm requires is **ONE RULE OVER EVERY
   COLUMN**.
2. **THE COLUMN DENOMINATOR, AND THE ROUTED SET AS A SUBTRACTION FROM IT.** `columns_total` is the table's
   OWN column list; `columns_routed` is what goes through the one path; the arm PRINTS `total MINUS routed`
   and refuses a non-empty remainder. **Do not write `columns_total` as a forward list of the columns you
   had in mind -- read it off the table** (Rule 24: a set written as a subtraction from a printed
   denominator cannot lose a member silently).
3. **`rule_per_column`** -- one entry per column in the denominator, naming the rendering rule applied. The
   arm counts the DISTINCT values and refuses anything but exactly one.
4. **A WITNESS.** A token that actually occurs in **at least TWO** columns, with its rendering in each. The
   arm refuses a record where those renderings differ. ⭐ **This is the arm that can tell a real repair from
   a renamed one**: `rule_per_column` is your own description, the witness is the artifact.
5. **`population_discriminator`** -- what identifies R-38's population now that no column is singled out by
   carrying brace bytes. If your rule keeps the escaping, say so and say which column is authoritative.
6. **`before` / `after` counts** for both columns. ⛔ **THESE ARE DISCLOSURE, NOT A BAR.** The arm does
   **not** grade them against each other, deliberately: the two columns hold DIFFERENT CONTENT, so
   `canonical_braces == current_braces` is a bar no correct artifact can meet. **This seat drafted exactly
   that bar and repaired it before issuing.**
7. **`third_column_argument`** -- why a column added tomorrow renders the same way without anyone
   remembering to make it.
8. **THE VINTAGE FIELD:** `fixed_inputs_at_pin`, mapping each fixed input you invoked to the COMMIT you
   invoked it at -- both `check_en_r14.py` and `R14_BASE.json`, each resolvable against its path.

**RECORD SHAPE (the one carrier is `deliverables/2.0.0_SA_COO~G/fixed_inputs/r14/R14_BASE.json`; this is a quotation of its `render` half)**

```json
{
  "render": {
    "one_path": "<file:line of the single renderer EVERY column now calls>",
    "columns_total": ["<every column in the table, its own denominator>"],
    "columns_routed": ["<the ones routed; the arm prints the SUBTRACTION>"],
    "rule_per_column": {"<column>": "<the rendering rule applied -- exactly ONE distinct value>"},
    "witness": {"token": "<a token occurring in at least TWO columns>", "rendered_in": {"<column>": "<its rendering there -- the arm requires them identical>"}},
    "population_discriminator": "<what identifies the population now that no column is singled out by carrying brace bytes>",
    "before": {"canonical_braces": 0, "canonical_parens": 0, "current_braces": 0, "current_parens": 0},
    "after": {"canonical_braces": 0, "canonical_parens": 0, "current_braces": 0, "current_parens": 0},
    "denominator_rows": 0,
    "third_column_argument": "<why a third column would now render the same way>"
  },
  "fixed_inputs_at_pin": {"<path>": "<commit>"},
  "stale_proofs": {"fixed_input_commits_since_cut": 0, "proofs_re_run": []}
}
```

Write it to `<WS>/org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/ONE_RENDER_PATH_R14.json`.

**AND REGENERATE THE REPORT THROUGH THE ONE PATH.** The record describes a renderer; the table is what a
grader reads. A renderer nothing produced output with is a description.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="R7R14-AC1" cell_refs="EN-r-7"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r14/check_en_r14.py r7-one-path</invocation><expect>PASS-R7-ONE-PATH</expect></criterion>

<criterion id="R7R14-AC2" cell_refs="EN-r-7"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r14/check_en_r14.py r7-no-producer-change</invocation><expect>PASS-R7-NO-PRODUCER-CHANGE</expect></criterion>

<criterion id="R7R14-AC3" cell_refs="EN-r-7"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r14/check_en_r14.py r14-vintage-field</invocation><expect>PASS-R14-VINTAGE-FIELD</expect></criterion>

<criterion id="R7R14-AC4" cell_refs="EN-r-7"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r14/check_en_r14.py r14-stale-proofs</invocation><expect>PASS-R14-STALE-PROOFS</expect></criterion>

<criterion id="R7R14-AC5" cell_refs="EN-r-7" judgment="true"/>

<expected_criteria>R7R14-AC1, R7R14-AC2, R7R14-AC3, R7R14-AC4, R7R14-AC5</expected_criteria>

**WIRING AT THE CUT:** `AC1` and `AC3` **FAIL** (no record exists yet). ⚠ `AC2` and `AC4` are
**GUARD-SHAPED and read PASS at the cut** -- `AC2` guards against a producer change you must not make, and
`AC4`'s window is empty until a fixed input moves.

⚠ **WHAT THE MECHANICAL ARMS CANNOT SEE, stated so you do not over-read a green:** the arm reads your
RECORD. It cannot open the regenerated table and confirm the renderer actually produced it, and it cannot
tell whether `rule_per_column` describes the code you wrote. **A PASS means your record is internally sound
and carries a witness, never that the artifact matches it.** That half is `AC5`'s.

**`R7R14-AC5`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether the regenerated table was actually
produced by the named renderer; whether the witness token is real in that table at both columns; whether the
population discriminator survives the change; and whether `S101`'s original false-negative now returns the
right answer against the regenerated artifact.

⭐ **THE BAR THESE CRITERIA WERE BUILT AGAINST, and you may hold me to it:** each was checked against a
HAND-BUILT CORRECT RECORD before this order shipped, driven in the checker's self-test as a
POSITIVE-SATISFIABILITY arm (`python .../check_en_r14.py selftest-arms`, 28 arms, 9 positive). The CTO's
words: *"can a CORRECT artifact satisfy this? Where the honest answer is no, THE CRITERION IS THE DEFECT,
NOT THE CELL."* **One such criterion was found and repaired IN THIS ORDER'S OWN DRAFT** -- see item 6. **If
you find another, file it BLOCKING and keep working.**

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/` and this order's own file. Nothing else.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- ⛔ **`lib/opal_naming.py` IS NOT YOURS THIS ROUND.** `S101` resolved AT THE SOURCE that the producer is
  CORRECT at the values (`{dim_name}` on 10 of 10 matching lines, `(dim_name)` on 0, over a printed
  denominator of 71 tracked files). **This cell changes RENDERING ONLY.** `r7-no-producer-change` grades the
  commits **YOU** authored against it; another seat's commit there is excused and printed, never charged to
  you. Read it freely.
- ⛔ **DO NOT TOUCH `EN-p-38`'s QUESTION.** The cell beside you measures the 1449-vs-1303 grain. The analysis
  refused to pair them: *"they share a file and nothing else, and a joint cell will report the easier one."*
  Your record has no grain field and your arms read none.
- ⚠ **YOU REGENERATE A REPORT THE OTHER CELL READS.** That is why `EN-p-38` pins its input at
  `c05f9f9fc9` and reads it with `git show`. **Do not "helpfully" leave the old table in place, and do not
  coordinate with that cell** -- the pin already removes the ordering between you.
- **Surprises** by **TEXTUAL SPLICE** into the fence that PARSES AS A LIST; never re-dump; preserve line
  endings exactly. Copy an existing row's field set exactly.
- **Id** `LGIC_ENFORCE-W<n>-S<k>`, `<k>` one above the highest in ANY document under that channel, re-measured
  at your own write time. **`S104` is taken -- this seat filed it at the cut, and one other order is open
  this round.**
- Every `.py` edit passes `.tools/commit-gate.sh`. **Commit before you grade.**

<paths>
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.13, round-14 cell `EN-r-7` (section 0n).
<owned_cells>EN-r-7</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids `R7R14-AC1` through `R7R14-AC5`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-r-7-r14.one-render-path.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> R7R14-AC1,R7R14-AC2,R7R14-AC3,R7R14-AC4,R7R14-AC5 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-r-7-r14.one-render-path.md` BEFORE the `complete` flip.
Result file `one-render-path.r14.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.** `controls` admits only `mutant`/`determinism`. `introduces` entries are LITERAL tokens present at the pin and absent at its parent.
`R7R14-AC5` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. PRINT the one renderer's `file:line`,
the column denominator and the subtraction, the single rule, the witness token with its rendering in each
column it occurs in, the population discriminator, the before/after counts, and the regenerated table's
path. If you kept the escaping, say what is authoritative for the population now.

---

## RECORD FACE

⛔ **THE ONE-LINE RECUT THIS ROUND CARRIES, FOR `3.0.0_SA_CVO` AT L9:** the two cells this round are
DELIBERATELY UNPAIRED on the analysis's instruction, and they share exactly one file -- the r13 population
table. `EN-r-7` REGENERATES it; `EN-p-38` READS it AT A PIN. **An L9 that grades them as one round must not
grade them as one cell:** a finding about the rendering says nothing about the grain, and the easier cell
finishing first is not evidence about the other.

<preflight>
comp-schedule: RUN at the round-14 cut: no schedule is created or read.
comp-iam: RUN at the round-14 cut: no grant moves.
comp-adversary: RUN at the round-14 cut: the cheapest satisfying move for AC1 is to rename the current column's rule in the record without changing the renderer, so the arm requires a WITNESS -- a real token rendered in two columns -- which the record cannot produce from a description. The second-cheapest is to route two columns and leave the rest, so the routed set is graded as a SUBTRACTION from the table's own column denominator. What no mechanical arm here can see is whether the regenerated table was produced by the named renderer at all -- stated on the order and routed to AC5.
lane: <paths> is the grant; deliverables/0.9.0_WK_LGIC_ENFORCE~1/ by the tree convention. lib/opal_naming.py has NO writer this round.
contention: the channel is shared -- append-only, 14b's inversion applies. The r13 table is regenerated by THIS cell and read by EN-p-38 AT A PIN, so there is no ordering between the two cells.
</preflight>

Seating: slot `~1`, level 0, one of TWO unpaired orders this round. Round 14 of LGIC_ENFORCE, issued by
`2.0.0_SA_COO~G` on decomposition v3.13 s.0n, from `1.0.0_SA_CTO`'s round-13 analysis @`cf0cf68868` and
`3.0.0_SA_CVO`'s `S101`. Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r14/` (`check_en_r14.py`,
`R14_BASE.json` pinning `c05f9f9fc9`). Rulings carried: S85's ONE CARRIER, the CUT-TIME criterion bar,
ADDENDUM 3's vintage field, LD-0521, W1-S39's author-scoped no-repair shape, Rule 24's subtraction.
