# TO LGIC_ENFORCE.TO-EN-t-34-r7 -- THE LABELS THAT LIE: a label that hides a two-carrier row, and a reason that names the wrong thing entirely

<to_id>LGIC_ENFORCE.TO-EN-t-34-r7</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-18</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` (ADMITTED; both halves current) | **Decomp cell:** `EN-t-34` (decomposition v3.6 s.0g) | **outcome_ref:** FWD-5 | **depends_on:** none -- FIRST of this slot's two-order queue

---

## WORKER FACE

### THE CELL

`EN-t-34`. **Two groups of rows carry a label that says something FALSE about them. You make both labels
true.** You resolve nothing, you re-grade nothing, and you change no grading behaviour.

⛔ **THIS ROUND DOES NOT ATTEMPT THE 1093 DEFERRED ROWS AND NEITHER DO YOU.** `R-60` read `FWD-5`'s own
ACCEPT at the bytes: *"a ranked list of every name and address that breaks the pattern, each paired with
its correct form, totals shown ... THIS IS THE LIST CLEAN-UP PROJECTS START FROM."* **THE OUTCOME IS THE
LIST; the resolution is the clean-up projects' work.** Rounds 5 and 6 each resolved 41 rows against a bar
`FWD-5` never set. If you find yourself resolving a placeholder, you have left this cell.

### GROUP ONE: THE 51 TWO-CARRIER ROWS

Round 6's best finding. A single label -- `NON_SYSTEM_PLACEHOLDER_TOKEN` -- hid a group where
**NEITHER REMEDY ALONE CLEARS A ROW**: the `{system}` half is a `resources.json` row and IS inside a
cell's grant; the `{cadence}` half is a schedule read and is NOT. **A row needing two remedies filed
under a one-remedy label is INVISIBLE TO BOTH.** That is Rule 24 INTENT COHERENCE failing inside the
campaign built to enumerate, and no amount of grinding through the count would ever have surfaced it.

`R7_BASE.json` pins them at **51**, re-identified INDEPENDENTLY of round 6's own label by requiring both
`{system}` and `{cadence}` in the row's own text -- the agreement with the declared count is the
corroboration, and the label is not the test. Types: `EVENT_RULE` 49, `LOG_GROUP` 2.

**WHAT MAKES THE NEW LABEL ACCEPTABLE, and it is the arm most likely to catch good-faith work:** every
row's entry names **BOTH REMEDIES AND EACH REMEDY'S CARRIER** -- WHERE the value comes from, not merely
that there are two. *"Two remedies"* is a DESCRIPTION. *"The `{system}` half is a `resources.json` row;
the `{cadence}` half is the schedule that drives it"* is an INSTRUCTION. The defect you are fixing is a
label that described where it should have instructed, so a label that describes again fixes nothing.
Your record also carries a `label_definition` a later census can read.

### GROUP TWO: THE 15 KEY FORMAT TEMPLATES

These carry `reason: NON_SYSTEM_PLACEHOLDER_TOKEN`, which says **THE TOKEN IS NOT A SYSTEM**. The truth,
ruled at `R-62`, is that **THE ROW IS NOT A NAME**. A key format template is a producer's RUNTIME
SUBSTITUTION FIELD -- `{snap}`, `{dim_name}` -- and `grade.placeholder` says a placeholder fills *"a slot
THE NAME DOES NOT CARRY"*, which presupposes a name. So *"resolve the substitution from a declared
source"* had no source **because the question was never a substitution.**

You give all 15 a reason that says that. One field each. Nothing else about them changes.

⛔ **AND YOU DO NOT REMOVE THEM FROM ANY GRADE. THIS IS THE REFUSAL, AND IT IS A GRADED ARM.** It is
tempting -- and it was ruled and REFUSED. Read `R7_BASE.json`'s `the_exclusion_switch_HAZARD` before you
touch anything near it:

```
  all 15 rows are type S3Key, and S3Key is ALREADY in types_not_graded_by_kind
  lib/opal_naming.py:493   graded_types = by_type | set(types_not_graded_by_kind)   <- UNIONS IT IN
  lib/opal_naming.py:1012  not_graded = {t for t,why in tng.items()
                                         if str(why).startswith("NOT GRADED")}      <- THE REAL SWITCH
  15 entries: 8 genuinely out, 7 STILL GRADED -- S3Key among them, reason "the key grammar (key)"
```

**THAT TABLE IS A ROUTING TABLE AND ITS NAME IS THE OPPOSITE OF ITS BEHAVIOUR.** A CTO ruling reached for
it as an exclusion mechanism and was wrong. **REWORDING A REASON IN IT SILENTLY RE-GRADES A TYPE** --
turning *"NOT GRADED: AWS-issued identifier"* into *"AWS-issued identifier, not graded"* puts that type
back into the grade and nothing announces it. Eight types sit on that edge. `t34-no-grade-change` READS
PASS AT THE CUT and exists only to refuse you if you move it.

**Read:** `R7_BASE.json` whole; round 6's `PLACEHOLDER_CAMPAIGN_R6.json` `non_system_disposition`,
especially `partition_by_remedy`; `org/standards/NAMING_SCHEMA.json` `grade.placeholder`.

### WHERE YOUR RECORD GOES

`<WS>/org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LABEL_TRUTH_R7.json`

Any script you cite as an instrument goes in that same folder and is **COMMITTED** -- row
`LGIC_ENFORCE-S69`: a record citing an untracked instrument has an unverifiable claim at its centre, and
the drain deletes the evidence as routine hygiene.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="T34R7-AC1" cell_refs="EN-t-34"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r7/check_en_r7.py t34-51-both</invocation><expect>PASS-T34-51-NAME-BOTH-REMEDIES</expect></criterion>

<criterion id="T34R7-AC2" cell_refs="EN-t-34"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r7/check_en_r7.py t34-actionable</invocation><expect>PASS-T34-LABEL-IS-ACTIONABLE</expect></criterion>

<criterion id="T34R7-AC3" cell_refs="EN-t-34"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r7/check_en_r7.py t34-15-true</invocation><expect>PASS-T34-15-CARRY-A-TRUE-REASON</expect></criterion>

<criterion id="T34R7-AC4" cell_refs="EN-t-34"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r7/check_en_r7.py t34-no-grade-change</invocation><expect>PASS-T34-NO-GRADE-CHANGE</expect></criterion>

<criterion id="T34R7-AC5" cell_refs="EN-t-34" judgment="true"/>

<expected_criteria>T34R7-AC1, T34R7-AC2, T34R7-AC3, T34R7-AC4, T34R7-AC5</expected_criteria>

**MEASURED BY THE ISSUER AT THE CUT, not assumed:** `T34R7-AC1`, `AC2` and `AC3` read **FAIL** -- your
record does not exist yet. **`T34R7-AC4` reads PASS and is a GUARD, not a target** -- the exclusion table
is untouched now and must stay so, which is why only your own edit can break it.

**`T34R7-AC5`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether the new label is one a LATER
CENSUS COULD ACT ON rather than a better-worded description, and whether the 15's new reason is a true
account of what those rows are rather than a rephrasing of the old one. The arms can only check that
fields are present, that carriers are named and that the old reason is gone.

**THE CHECKER'S CONTROLS:** `selftest-arms` drives **21 arms, 8 POSITIVE-SATISFIABILITY** against
simulated correct records -- including one that drives `t34-no-grade-change` against a schema with
`S3Key` pushed across the `NOT GRADED` switch, which is the exact one-prefix edit R-62 refused. Run it
first. An arm a correct record cannot satisfy is a BLOCKING surprise row quoting the arm and its output
-- never a workaround, never an edit to a fixed input.

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/` and this order's own file. Nothing else. A path you need that is not named is a BLOCKING row, never an override.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- ⛔ **`org/standards/NAMING_SCHEMA.json` IS NOT IN YOUR GRANT AND MUST NOT CHANGE.** Neither must `infra/logic/registry/`. This cell changes LABELS ON RECORDS, never grading behaviour.
- ⛔ **NO PLACEHOLDER IS RESOLVED.** If a row looks resolvable, that is round 8's or a clean-up project's, and noting it is a surprise ROW rather than an act.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md`, appended by **TEXTUAL SPLICE** to the fence that PARSES AS A LIST -- that file carries several fences and only one is the row array. ⛔ **NEVER RE-DUMP THE ARRAY:** `ensure_ascii=False` unescapes existing `\uXXXX` into raw non-ASCII and `ensure_ascii=True` re-escapes literal UTF-8, each rewriting the other convention, and **comparing PARSED objects is blind to it.** Assert the non-ASCII CHARACTER count and the backslash-u count are both unchanged. **A JSON array append costs exactly ONE deletion** -- the previous last element gains its comma; expect `N insertions, 1 deletion` and verify the deleted line is only ` }` becoming ` },`.
- **Id** `LGIC_ENFORCE-W<n>-S<k>`, `<k>` one above the highest in ANY document under that channel, re-measured at your own write time.
- **Numbers in this order are CONTEXT, never acceptance values.**
- **Commit before you grade.**
- **Nothing live moves.** No apply, no AWS write, no deploy.

<paths>
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.6, round-7 cell `EN-t-34` (section 0g).
<owned_cells>EN-t-34</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `T34R7-AC1` through `T34R7-AC5`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-t-34-r7.labels-that-lie.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> T34R7-AC1,T34R7-AC2,T34R7-AC3,T34R7-AC4,T34R7-AC5 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-t-34-r7.labels-that-lie.md` BEFORE the `complete` flip.
Result file `labels-that-lie.r7.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`T34R7-AC5` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. PRINT the 51 re-identified at your own write time with the instrument named, the 15 with their old reason gone, and the exclusion table's 8/7 split BEFORE and AFTER to show the guard held.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-7 cut: no schedule is created or read by this cell.
comp-iam: RUN at the round-7 cut: no grant moves; the cell reads round-6 records and writes one of its own.
comp-adversary: RUN at the round-7 cut: the adversarial control is t34-no-grade-change, a GUARD that reads PASS at the cut and can only be broken by this cell's own edit. It exists because the tempting act here -- adding a types_not_graded_by_kind entry -- was RULED AND REFUSED, and because the acceptance condition originally attached to that act would have PASSED VACUOUSLY: nothing would have left any grade, so the count it required could not move. The guard measures the 8/7 split directly instead.
lane: the <paths> block is the grant (RULING 1 shape c); deliverables/0.9.0_WK_LGIC_ENFORCE~1/ is granted by the tree convention. NAMING_SCHEMA.json and infra/logic/registry/ are excluded by a BOUND as well as by the grant's silence, because the grant cannot express "do not change grading behaviour" and the order states it.
contention: the channel is written by EN-o-35-r7 LATER IN THIS SAME QUEUE and by no other open order in any LGIC project at the cut. ONE QUEUE, and this round has the MEASUREMENT rather than the rule: LGIC_LGCTFM round 2 ran two slots on a stated hypothesis that a textual splice merges where a whole-array re-dump conflicts, and IT WAS REFUTED -- the second drain conflicted although both sides spliced, and safe-merge's own banner says an append-only channel conflicts on EVERY concurrent drain. The cost was one union merge, exactly as bounded, and the hypothesis is recorded dead rather than quietly dropped.
</preflight>

Seating: slot `~1`, level 0, FIRST of a two-order queue (`EN-t-34-r7` -> `EN-o-35-r7`). Round 7 of LGIC_ENFORCE, issued by `2.0.0_SA_COO~G` on decomposition v3.6 s.0g, from the REGISTER's round-7 material at `last_updated 2026-09-18T08:40:00Z` rather than from the round-6 analysis's forward carry (R-57 -- and this lane took its first framing of this round from the analysis and had to withdraw it, so the rule is applied here deliberately rather than remembered). Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r7/` (`check_en_r7.py`, 8 subcommands and a 21-arm self-test with 8 positive-satisfiability arms; `R7_BASE.json` pinning `2c3d7b0cb2`). Rulings carried: R-60, R-62, R-47, R-40.
