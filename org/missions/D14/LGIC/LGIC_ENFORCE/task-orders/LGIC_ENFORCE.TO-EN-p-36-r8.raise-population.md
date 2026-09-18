# TO LGIC_ENFORCE.TO-EN-p-36-r8 -- THE RAISE POPULATION WHOLESALE: no conformance claim over this estate has a denominator above 3

<to_id>LGIC_ENFORCE.TO-EN-p-36-r8</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-18</issued_date>
<status>complete -- 0.9.0_WK_LGIC_ENFORCE~1 2026-09-18: both planes RUN TO THE END (stopped=null), 462 raises dispositioned (0 resolved, 462 carded citing OWNER_CARDS_R4.md), resolved+carded==raise_population per plane (131 live, 331 repo); RAISE_POPULATION_R8.json @54659987c0; proof-of-spec-check rc=0 VALID; P36R8-AC1..AC4 PASS-by-output, P36R8-AC5 UNVERIFIABLE-BY-INSTRUMENT reserved for 3.0.0_SA_CVO at L9</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` (ADMITTED; both halves current) | **Decomp cell:** `EN-p-36` (decomposition v3.7 s.0h) | **outcome_ref:** FWD-5 | **depends_on:** none -- FIRST and only order on slot `~1`

---

## WORKER FACE

### THE CELL

`EN-p-36`. **The naming census stops on its FIRST RAISE, on both planes, and has for eight rounds.**
Measured by the issuer at the cut:

```
  live   2205 nodes, 1838 to judge   -> STOPPED after  3 judged  on API_GW     sentiment-query-api
  repo   1878 names,  475 .tf files  -> STOPPED after  2 judged  on IAM_POLICY F49ServedAndSourceRead
```

So every sentence anyone has written about this estate conforming rests on **3 live names and 2 repo
names**. Your job is to make the census RUN TO THE END on both planes, so that a conformance claim
finally has a denominator.

### THE TWO THINGS THAT MAKE THIS CELL DIFFERENT FROM A TOKEN FIX

⛔ **DO NOT FIX THE STOP TOKEN.** `W7-S1` measured **504 of 1805 live** and **623 of 1869 repo** names
RAISING in `grade()`. Registering `sentiment-query-api` moves the stop to the next raiser, of which
there are ~503 more: **a per-token fix is a treadmill with 504 steps whose first step looks exactly
like a fix.** Those two figures are carried in `R8_BASE.json` with `claim: reported` -- they are
`W7-S1`'s, not the issuer's, and **you re-measure both at your own write time.**

⛔ **AND THE TWO PLANES STOP ON DIFFERENT TOKENS.** The register names only the live one. A cell that
treated "the stop token" as one thing would clear the live plane and leave repo stopped at its third
name. Both planes, separately, with separate denominators.

### THE MECHANISM ALREADY EXISTS -- POPULATE IT, DO NOT BUILD ONE

`lib/opal_naming.py census --not-judged <FILE>`, ratified by **R-29 AMENDMENT 1**, its own help text
verbatim: *"JSON file: a list of {name, plane, card} names CARDED rather than graded -- a RAISE on one
of these does not stop the run."* That is the BUILD LADDER's rung 2: the estate already has it. You
**populate** it; you do not write a second one.

For every RAISE, exactly one of:
- **RESOLVED** -- a registry row under `infra/logic/registry/` makes the token resolve. Rule 30: *a
  builder REFUSAL is a missing registry row to add, never a hand-typed workaround.*
- **CARDED** -- an entry in the not-judged file with a `card` REASON saying what you looked at and why
  the name cannot be resolved today.

**`resolved + carded == the RAISE population, per plane, with both denominators printed.`**

⛔ **A CARD WITH NO REASON IS THE DEFECT THIS PROJECT ALREADY NAMED.** `TIMEBOXED_R33` described the
MEASURING PROCESS rather than the measured domain and passed every count check because 1093 rows really
did carry it (R-60). A bare card is that shape again. Every card names its own subject.

**Read:** `R8_BASE.json` whole, especially `raise_population` and its `NOT_re-derived_here` note;
`lib/opal_naming.py census_judge`; round 3's `NOT_JUDGED_S6.r3.json` as the FORMAT precedent.

### WHERE YOUR RECORD GOES

`<WS>/org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/RAISE_POPULATION_R8.json`

Shape, and the arms read exactly these keys:

```
  {"planes": {"live": {"resolved": [...], "carded": [{"name","plane","card"}...],
                       "raise_population": <int>, "stopped": null, "judged": <int>,
                       "denominator_measured_at_write_time": {"instrument": "...", "value": <int>}},
              "repo": { ... the same ... }}}
```

Any instrument you cite goes in that same folder and is **COMMITTED** (row `LGIC_ENFORCE-S69`).

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="P36R8-AC1" cell_refs="EN-p-36"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r8/check_en_r8.py p36-population</invocation><expect>PASS-P36-POPULATION</expect></criterion>

<criterion id="P36R8-AC2" cell_refs="EN-p-36"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r8/check_en_r8.py p36-runs-to-end</invocation><expect>PASS-P36-RUNS-TO-END</expect></criterion>

<criterion id="P36R8-AC3" cell_refs="EN-p-36"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r8/check_en_r8.py p36-own-denominator</invocation><expect>PASS-P36-OWN-DENOMINATOR</expect></criterion>

<criterion id="P36R8-AC4" cell_refs="EN-p-36"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r8/check_en_r8.py p36-cards-carry-reasons</invocation><expect>PASS-P36-CARDS-CARRY-REASONS</expect></criterion>

<criterion id="P36R8-AC5" cell_refs="EN-p-36" judgment="true"/>

<expected_criteria>P36R8-AC1, P36R8-AC2, P36R8-AC3, P36R8-AC4, P36R8-AC5</expected_criteria>

**ALL FOUR MECHANICAL CRITERIA READ FAIL AT THE CUT**, MEASURED by the issuer and not assumed, because
your record does not exist. There is no guard-shaped criterion in this cell.

**`P36R8-AC5`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether each CARD reflects a real
search rather than a shrug, and whether the RESOLVED rows resolve because a registry row genuinely
covers them rather than because a token was added to make a check pass. The arms can only check that
the arithmetic closes and the fields are present.

**THE CHECKER'S CONTROLS:** `selftest-arms` drives **31 arms, 13 POSITIVE-SATISFIABILITY** against
simulated correct records. Run it first. An arm a correct record cannot satisfy is a BLOCKING surprise
row quoting the arm and its output -- never a workaround, never an edit to a fixed input.

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/` and this order's own file. Nothing else.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- ⛔ **YOU DO NOT EDIT `org/standards/NAMING_SCHEMA.json`.** That file is `EN-m-39`'s this round and yours never. If the schema is wrong, that is a surprise ROW with its measurement.
- ⛔ **NOTHING LIVE MOVES.** Every AWS read is read-only through the `.tools/aws` shim. No apply, no write, no deploy. The live census is a READ.
- **Registry rows** under `infra/logic/registry/` ARE yours to add where a resolution is genuine (Rule 30). A row you add is evidence in the record, named with its token.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md`, appended by **TEXTUAL SPLICE** to the fence that PARSES AS A LIST. ⛔ **NEVER RE-DUMP THE ARRAY** -- assert the non-ASCII CHARACTER count and the backslash-u count are both unchanged afterwards. Note `len(b)-len(b.decode())` is a BYTE DELTA, not a character count; for a count use `sum(1 for ch in text if ord(ch) > 127)`.
- **Id** `LGIC_ENFORCE-W<n>-S<k>`, `<k>` one above the highest in ANY document under that channel, re-measured at your own write time. **Three other orders are open this round and two of them may append before you.**
- **Commit before you grade.**

<paths>
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
infra/logic/registry/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.7, round-8 cell `EN-p-36` (section 0h).
<owned_cells>EN-p-36</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `P36R8-AC1` through `P36R8-AC5`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-p-36-r8.raise-population.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> P36R8-AC1,P36R8-AC2,P36R8-AC3,P36R8-AC4,P36R8-AC5 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-p-36-r8.raise-population.md` BEFORE the `complete` flip.
Result file `raise-population.r8.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`P36R8-AC5` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. PRINT `resolved + carded == <population>` FOR EACH PLANE with its own denominator, both stop states, and how many registry rows you added.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-8 cut: no schedule is created or read by this cell.
comp-iam: RUN at the round-8 cut: no grant moves. The cell READS the live AWS plane through the shim and WRITES nothing there; registry rows are repo files, not IAM.
comp-adversary: RUN at the round-8 cut: the adversarial control is p36-runs-to-end's judged FLOOR. Without it, `stopped: null` alone would pass on a census that judged nothing -- a card file that cards EVERYTHING reaches the end of both planes and measures no estate at all. The floor (judged must EXCEED the cut's 3 live / 2 repo) is what makes carding a disposition rather than an escape, and it is the arm that stops this cell from buying its own green.
lane: the <paths> block is the grant; deliverables/0.9.0_WK_LGIC_ENFORCE~1/ is granted by the tree convention. NAMING_SCHEMA.json is EN-m-39's this round and is refused to this cell by a BOUND rather than by a path, because the <paths> block cannot express "another cell owns this".
contention: the channel is written by three other open orders this round. THREE SLOTS, and the channel is the ONLY shared file -- 14b's append-only inversion applies and no slot isolates there. The registry directory is this cell's alone; no other round-8 cell writes infra/logic/registry/.
</preflight>

Seating: slot `~1`, level 0, the only order on its slot. Round 8 of LGIC_ENFORCE, issued by `2.0.0_SA_COO~G` on decomposition v3.7 s.0h, from the REGISTER's ROUND 8 MATERIAL block `(e)`. Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r8/` (`check_en_r8.py`, 14 real arms and a 31-arm self-test with 13 positive-satisfiability arms; `R8_BASE.json` pinning `43243d281397eba6204aaa0c1a0027cc7d295ebe`). Rulings carried: R-67, R-29, R-30, R-38.
