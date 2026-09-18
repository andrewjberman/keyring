# TO LGIC_ENFORCE.TO-EN-s-41-r9 -- W3-S17's SCOPE DECISION: brace-only or wider, TAKEN, with a negative arm either way

<to_id>LGIC_ENFORCE.TO-EN-s-41-r9</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~2</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-18</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` (ADMITTED; both halves current) | **Decomp cell:** `EN-s-41` (decomposition v3.8 s.0i) | **outcome_ref:** FWD-2 | **depends_on:** none -- the only order on slot `~2`

---

## WORKER FACE

### THE CELL

`EN-s-41`. Row `LGIC_ENFORCE-W3-S17` is **ARMED** and its subject is a SCOPE QUESTION, not a bug:

> `PLACEHOLDER_CAMPAIGN_R6.json`'s S3Key row `silver/%s/` (plane `repo`, **two occurrences**) carries a
> python **%-STYLE** runtime substitution field **WITH NO BRACE AT ALL**.

Round 7's `unsanctioned_brace` instrument and round 8's `key.template_detection` are **BOTH brace-only by
their own stated scope**, so both correctly class that row ORDINARY. **NEITHER IS DEFECTIVE.** The question
is whether the estate's template rule is *braces* or *runtime substitution of any syntax*, and it has never
been decided -- it has only been assumed by every instrument that implemented it.

⛔ **`EN-m-39` FILED THIS AS A COUNTEREXAMPLE RATHER THAN WIDENING THE RULE TO SWALLOW IT, AND THAT IS THE
ONLY REASON THE DECISION IS STILL AVAILABLE TO BE TAKEN PROPERLY.** Widening silently was the cheap move and
it would have made the scope UNFALSIFIABLE -- an instrument that matches whatever it meets can never be shown
wrong. Do not undo that by patching a regex.

### YOU TAKE ONE OF EXACTLY TWO DECISIONS, AND YOU DEFEND IT

```
  HOLD-BRACE-ONLY   the template rule is BRACES. The %-style row stays ORDINARY, and the SCOPE is
                    written down explicitly so the next instrument inherits a stated bound and not
                    an accident of implementation.
  WIDEN             the rule is RUNTIME SUBSTITUTION. The %-style class is named, its syntax bounded,
                    and org/standards/NAMING_SCHEMA.json carries the wider scope.
```

⛔ **BOTH BRANCHES REQUIRE A WRITE TO `org/standards/NAMING_SCHEMA.json`.** A HOLD that changes no file
leaves the scope exactly as unfalsifiable as it is today and is NOT a decision -- it is the status quo with
a sentence about it. HOLD writes the BOUND; WIDEN writes the WIDER RULE. There is no no-op branch.

### THE NEGATIVE ARM -- REQUIRED ON EITHER BRANCH

`s41-negative-arm` requires you to state, and MEASURE, **what your decision EXCLUDES**:

```
  HOLD  -> name a construct that IS runtime substitution and REMAINS out of scope, and show the
           instrument leaves it ORDINARY. The exclusion is the content of the decision.
  WIDEN -> name a construct that LOOKS like substitution and STAYS out of scope (a literal percent,
           a printf in prose, a URL-encoded byte), and show it is NOT swept in.
```

⛔ **A SCOPE WITH NO STATED EXCLUSION IS THE UNFALSIFIABLE RULE UNDER A DIFFERENT NAME.** Rule 24(iv):
name which values your remedy does NOT move.

### THE POPULATION, AND YOU MEASURE IT BEFORE YOU DECIDE

`s41-population` requires a census of %-style substitution across the SAME corpus the brace instrument
reads, with its **DENOMINATOR PRINTED**, measured at YOUR write time. **DECIDE AFTER THE COUNT, NOT BEFORE.**
Two occurrences in one file argues one way; two hundred across the estate argues the other, and nobody has
looked. ⛔ **An unscoped read only falsifies a domain if you then INSPECT WHAT IT FOUND OUTSIDE IT** -- if
the sweep finds %-style outside the campaign file, name where.

⛔ **`s41-no-silent-move` IS THE ADVERSARIAL ARM: NO GRADE MOVES THIS ROUND.** If you WIDEN, the schema
says so and the re-grading is a LATER round's cut, seated deliberately. A scope decision that silently
re-verdicts 2474 rows inside a scope cell is exactly the shape this cell exists to prevent.

### WHERE YOUR RECORD GOES

`<WS>/org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/PERCENT_STYLE_SCOPE_R9.json`

```
  {"decision": "HOLD-BRACE-ONLY" | "WIDEN",
   "why": "...",
   "population": {"instrument": "...", "denominator_measured_at_write_time": <int>,
                  "percent_style_occurrences": <int>, "files": [...],
                  "outside_the_campaign_file": [...]},
   "excludes": [{"construct": "...", "shown_by": "...", "verdict_observed": "..."}],
   "schema_change": {"file": "org/standards/NAMING_SCHEMA.json", "what": "...", "applied": true},
   "grades_moved": 0,
   "disarms": "LGIC_ENFORCE-W3-S17"}
```

Every instrument you cite goes in that same folder and is **COMMITTED** (row `LGIC_ENFORCE-S69`).

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="S41R9-AC1" cell_refs="EN-s-41"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r9/check_en_r9.py s41-decision</invocation><expect>PASS-S41-DECISION</expect></criterion>

<criterion id="S41R9-AC2" cell_refs="EN-s-41"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r9/check_en_r9.py s41-population</invocation><expect>PASS-S41-POPULATION</expect></criterion>

<criterion id="S41R9-AC3" cell_refs="EN-s-41"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r9/check_en_r9.py s41-negative-arm</invocation><expect>PASS-S41-NEGATIVE-ARM</expect></criterion>

<criterion id="S41R9-AC4" cell_refs="EN-s-41"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r9/check_en_r9.py s41-no-silent-move</invocation><expect>PASS-S41-NO-SILENT-MOVE</expect></criterion>

<criterion id="S41R9-AC5" cell_refs="EN-s-41" judgment="true"/>

**ALL FOUR MECHANICAL CRITERIA READ FAIL AT THE CUT**, MEASURED by the issuer.

⚠ **`S41R9-AC4` IS GUARD-SHAPED AND ITS FAIL-AT-CUT IS A RECORD-ABSENCE, NOT A VIOLATION** -- it reads
`grades_moved` from a file that does not exist yet. It cannot distinguish "grades did not move" from "no
record"; the PASS it gives you is the record's own assertion, and `S41R9-AC5` is where a human reads whether
the assertion is true. Stated here so nobody mistakes the green for a measurement of the estate.

<expected_criteria>S41R9-AC1, S41R9-AC2, S41R9-AC3, S41R9-AC4, S41R9-AC5</expected_criteria>

**`S41R9-AC5`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether the decision is DEFENDED by the
population you measured rather than by convenience, whether the exclusion is a real construct rather than a
strawman nothing would have matched anyway, and whether the schema text actually BINDS the next instrument.

**THE CHECKER'S CONTROLS:** `selftest-arms` drives **27 arms, 13 POSITIVE-SATISFIABILITY**. Run it first. An
arm a CORRECT record cannot satisfy is a BLOCKING surprise row quoting the arm and its output.

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/` and this order's own file. Nothing else.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- ⛔ **`org/standards/NAMING_SCHEMA.json` IS YOURS THIS ROUND AND NO OTHER CELL'S.** Read it, then write the MINIMUM that states your scope. It is a live standard: do not restructure it, do not reformat it, do not re-dump it. Splice.
- ⛔ **YOU DO NOT EDIT `.tools/surprise-row-gate.py`** and you do not touch `PLACEHOLDER_CAMPAIGN_R6.json` -- the row is the SUBJECT, not the patient.
- ⛔ **NO GRADE MOVES, NO CENSUS RE-RUN, NO RE-VERDICTING.** See `s41-no-silent-move`.
- ⛔ **NOTHING LIVE MOVES.** Every AWS read is read-only through the `.tools/aws` shim.
- **W3-S17's `disarm_owner` is `2.0.0_SA_COO~G`, NOT YOU.** You produce the EVIDENCE that disarms it; the disarm row is the issuer's. ⛔ Do not write a disarm row and do not put `adjudicates` on your own row.
- **Surprises** by **TEXTUAL SPLICE** into the fence that PARSES AS A LIST; never re-dump the array; assert the non-ASCII CHARACTER count and the backslash-u count unchanged. `len(b)-len(b.decode())` is a BYTE DELTA, not a character count; for a count use `sum(1 for ch in text if ord(ch) > 127)`.
- **Id** `LGIC_ENFORCE-W<n>-S<k>`, `<k>` one above the highest in ANY document under that channel, re-measured at your own write time. **Two other orders are open this round.**
- **Commit before you grade.**

<paths>
org/standards/NAMING_SCHEMA.json
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.8, round-9 cell `EN-s-41` (section 0i).
<owned_cells>EN-s-41</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `S41R9-AC1` through `S41R9-AC5`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/LGIC_ENFORCE.TO-EN-s-41-r9.percent-style-scope.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> S41R9-AC1,S41R9-AC2,S41R9-AC3,S41R9-AC4,S41R9-AC5 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-s-41-r9.percent-style-scope.md` BEFORE the `complete` flip.
Result file `percent-style-scope.r9.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.** The instance's `controls` block admits only `mutant`/`determinism`; fold positive-control evidence into `mutant`. `introduces` entries must be LITERAL tokens present at the pin and absent at its parent, not prose.
`S41R9-AC5` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. PRINT the decision, the population with its denominator, the construct you EXCLUDE and how you showed it excluded, and the exact schema text you added.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-9 cut: no schedule is created or read by this cell.
comp-iam: RUN at the round-9 cut: no grant moves. org/standards/NAMING_SCHEMA.json is a repo standard and not an IAM or infrastructure surface; no live policy, role or key is read or written.
comp-adversary: RUN at the round-9 cut: the adversarial control is s41-no-silent-move paired with s41-negative-arm. The cheapest satisfying move is to WIDEN the regex and let the census re-verdict, which converts a scope decision into an untracked mass re-grade; the first arm forbids it and the second forbids the other cheap move, a HOLD that writes nothing and leaves the scope exactly as unfalsifiable as it is. ⚠ s41-no-silent-move reads grades_moved FROM THE CELL'S OWN RECORD -- it is a self-assertion with an instrument around it, not an independent measurement of the estate, and S41R9-AC5 is where that is judged.
lane: <paths> is the grant; deliverables/0.9.0_WK_LGIC_ENFORCE~2/ is granted by the tree convention. org/standards/NAMING_SCHEMA.json is granted to THIS cell alone this round -- verified against the other two orders' <paths> at the cut, no overlap.
contention: the channel is written by two other open orders this round -- 14b's append-only inversion applies and no slot isolates there. NAMING_SCHEMA.json has exactly one writer this round.
</preflight>

Seating: slot `~2`, level 0, the only order on its slot. Round 9 of LGIC_ENFORCE, issued by `2.0.0_SA_COO~G` on decomposition v3.8 s.0i, from the REGISTER's WHAT ROUND 9 OWES `(c)`, read at HEAD. Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r9/` (`check_en_r9.py`, 12 real arms and a 27-arm self-test with 13 positive-satisfiability arms; `R9_BASE.json` pinning `d9cdb39063`). Rulings carried: R-70, R-72, S82.
