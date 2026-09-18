# TO LGIC_ENFORCE.TO-EN-s-32-r6 -- the DISARM SWEEP: disarm what is met, RESTATE what has drifted, say which is which

<to_id>LGIC_ENFORCE.TO-EN-s-32-r6</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-18</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` (ADMITTED; both halves current) | **Decomp cell:** `EN-s-32` (decomposition v3.5 s.0f) | **outcome_ref:** FWD-3 | **depends_on:** none -- this is the FIRST cell of round 6's queue

---

## WORKER FACE

### THE CELL

`EN-s-32`. **You work this lane's ARMED rows: DISARM what is genuinely met, RESTATE what has drifted, and
say which is which.** You write no registry and no code. Your write surface is the project's surprise
channel and your own deliverables folder.

**THE POPULATION AND ITS PARTITION, and the partition is a graded criterion rather than a courtesy:**

```
  ARMED rows on this channel ................. 43   (measure this yourself; see below)
  of those, naming 2.0.0_SA_COO~G ............ 35   <- YOUR SCOPE
  naming 1.0.0_SA_CTO ........................  7   \  OWNED ELSEWHERE. You do NOT touch these.
  naming 3.0.0_SA_CVO ........................  1   /  You PRINT them with their owners.
```

⛔ **A WORKER OF THIS LANE CANNOT DISARM ANOTHER SEAT'S ROW.** Print `43 == 35 + 8` with the other owners
named. A cell that graded itself on its own subset while the round called it 43 would be the exact defect
this cell exists to stop.

### THE THREE CONDITIONS, AND EACH ONE IS A GRADED ARM

`1.0.0_SA_CTO`'s round-5 analysis adopted this sweep with three conditions, because **the number took three
attempts across two seats to settle** -- 57, then 54, then a ruling of 55, then **43**. Each wrong number
was wrong for a different reason, and each reason is now one of these:

1. **PRINT THE PREDICATE BEFORE THE COUNT** -- the ARMED predicate, the owner-resolution order, and the
   occurrence-vs-distinct choice. ⛔ **The arm compares your declaration against the predicate the checker
   IMPLEMENTS, so printing one rule and counting by another FAILS.** Your record carries a `predicate`
   object with these three keys and `"printed_before_count": true`:
   - `armed_predicate`: *a row id is ARMED if ANY of its occurrences carries hazard_standing == ARMED*
   - `occurrence_or_distinct`: *DISTINCT IDS, never occurrences*
   - `owner_resolution_order`: *disarm_owner -> disarm.owner -> owner*
2. **RE-MEASURE THE DENOMINATOR AT YOUR OWN WRITE TIME**, start and close both printed with the instrument
   named. **Do not take 43 or 35 from this order.** The arm re-derives the population itself and refuses a
   declaration that matches no independent read.
3. **GRADE PER OWNER** on `disarmed + restated == in_scope`.

### WHAT R-46 SAYS AN ARMED ROW IS, because the predicate is not obvious and getting it wrong cost two seats an hour

- a row id is ARMED if **any** of its occurrences carries `hazard_standing == "ARMED"`
- **DISTINCT IDS, never occurrences** -- this same channel gives **92** at the occurrence level and 57 at
  the distinct-id level
- an armed id is **CLOSED** only where a **REMEDIATION** document carries a **real disposition**:
  `remediation.state == "REMEDIATED"`, or a `disarm` block with `state == "DISARMED"` **and** an `at`.
  **`INERT` is a LABEL; only a CLOCK closes.** An adjudication document's clock does NOT close an
  investigation row.
- owner resolution: `disarm_owner` -> `disarm.owner` -> `owner` (top level, per **R-42**)

### DISARM OR RESTATE, AND THE SECOND HALF IS THE ONE THAT GETS SKIPPED

- **DISARMED** -- the row's condition is genuinely met. Your entry carries an `evidence` string citing the
  ACT that met it (`path:line @commit`, a run's output, a ruling id). **An entry with no evidence FAILS.**
- **RESTATED** -- the row still stands but **its stated reason has drifted**. Your entry carries
  `reason_before` and `reason_after`, and ⛔ **they must DIFFER** -- a restatement that repeats the old
  words is a no-op wearing the outcome's name, and the arm refuses it.

**`1.0.0_SA_CTO` has already done this on its own rows and it is the model:** it disarmed two whose R-39
condition was met and **left five armed with stated reasons** -- including `S56`, whose premise moved when
that seat wrote the very file the row says nobody can write. **A row whose premise moved needs a RESTATED
REASON, not a disarm.** A row left armed with a stale reason reads as held when nobody is holding it, and
that is what this sweep exists to find.

**Read:** every one of your 35 rows, whole -- its `one_line`, its `spec_asserts`, its `world_is` and its
`notes`; `R-46` as corrected and `R-42` in `SELF_DRIVE_LGIC_RULINGS_20260917.md`; row `S65` for the shape
`1.0.0_SA_CTO` used on its own two.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="S32R6-AC1" cell_refs="EN-s-32"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r6/check_en_r6.py s32-predicate</invocation><expect>PASS-S32-PREDICATE-PRINTED-AND-MATCHING</expect></criterion>

<criterion id="S32R6-AC2" cell_refs="EN-s-32"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r6/check_en_r6.py s32-denominator</invocation><expect>PASS-S32-ARMED-DENOMINATOR-RE-MEASURED</expect></criterion>

<criterion id="S32R6-AC3" cell_refs="EN-s-32"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r6/check_en_r6.py s32-partition</invocation><expect>PASS-S32-PARTITION-COVERS-THE-POPULATION</expect></criterion>

<criterion id="S32R6-AC4" cell_refs="EN-s-32"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r6/check_en_r6.py s32-graded</invocation><expect>PASS-S32-EVERY-IN-SCOPE-ROW-DISARMED-OR-RESTATED</expect></criterion>

<criterion id="S32R6-AC5" cell_refs="EN-s-32" judgment="true"/>

<expected_criteria>S32R6-AC1, S32R6-AC2, S32R6-AC3, S32R6-AC4, S32R6-AC5</expected_criteria>

**ALL FOUR MECHANICAL CRITERIA READ FAIL AT THE CUT**, each because your record does not exist yet --
measured by the issuer, not assumed. There is no guard-shaped criterion in this cell.

**THE CHECKER WAS BUILT WITH A CONTROL THIS LANE NOW APPLIES BY DEFAULT:** every core is driven against a
SIMULATED CORRECT RECORD and must PASS, as well as against a doctored one and must FAIL. `selftest-arms`
reads 28 arms, 8 of them that positive-satisfiability check. **Four of this issuer's arms in one night were
unsatisfiable by a correct fix**, each having passed its own mutant test. If you find an arm a correct
sweep cannot satisfy, that is a BLOCKING row quoting the arm and its output -- never a workaround, and
never an edit to a fixed input.

**`S32R6-AC5`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether each DISARMED row's evidence
actually meets the row's own stated condition, and whether each RESTATED reason is a genuine re-reading of
a drifted premise rather than a rewording. The arms can only measure that the fields differ.

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/` and this order's own file. Nothing else.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- **Fixed inputs are read-only.** A wrong arm is a BLOCKING row, never an edit.
- ⛔ **YOU TOUCH NO ROW WHOSE OWNER IS NOT `2.0.0_SA_COO~G`.** Not the CTO's 7, not the CVO's 1. You print them.
- ⛔ **A DISARM IS AN APPEND, NEVER A REWRITE.** You do not edit an existing row's `hazard_standing` in place. The channel is append-only: your outcomes live in YOUR OWN record, and a row's disposition is `3.0.0_SA_CVO`'s at L9. **Disarming is not disposing** and this cell does neither -- it produces the EVIDENCE.
- **Surprises** go to the project's `INVESTIGATION_v1.md`, appended to the fence that PARSES AS A LIST (that file carries THREE json fences -- fence 0 is the row array and the other two are standalone dicts; a splice at the file's last `]` would corrupt the document). Id `LGIC_ENFORCE-W<n>-S<k>`, `<k>` one above the highest in ANY document under that channel.
- **Numbers in this order are CONTEXT, never acceptance values.** Re-measure at your own tree -- that is AC2.
- **Commit before you grade.**
- **Nothing live moves.** No apply, no AWS write, no deploy. This cell reads rows and writes records.

<paths>
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.5, round-6 cell `EN-s-32` (section 0f).
<owned_cells>EN-s-32</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `S32R6-AC1` through `S32R6-AC5`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-s-32-r6.disarm-sweep.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> S32R6-AC1,S32R6-AC2,S32R6-AC3,S32R6-AC4,S32R6-AC5 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-s-32-r6.disarm-sweep.md` BEFORE the `complete` flip.
Result file `disarm-sweep.r6.result.md` beside it. Your sweep record is `DISARM_SWEEP_R6.json` in the same folder. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`S32R6-AC5` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape, and PRINT the partition and the disarmed/restated split.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-6 cut: no schedule is created or read.
comp-iam: RUN at the round-6 cut: no grant moves; the cell reads rows and writes its own records.
comp-adversary: RUN at the round-6 cut: the predicate arm is itself the adversarial control -- it compares the cell's DECLARED rule against the one the checker implements, so a cell that prints one rule and counts by another is refused rather than admitted. That shape exists because two seats counted this channel and got 57 and 54 on the same night.
lane: the <paths> block is the grant (RULING 1 shape c); deliverables/<serial>/ is granted by the tree convention. The cell touches no row it does not own, which is a BOUND rather than a grant -- the channel file is append-only and shared, so the grant cannot express per-row ownership and the order states it instead.
contention: the channel is written by EN-c-33-r6 later in THIS SAME QUEUE and by no other open order in any LGIC project at the cut (LGIC_LGCTFM and LGIC_CANON both read zero open orders). That is why this is one queue rather than two slots: two worker branches appending to one channel is a guaranteed conflict at the second merge, measured 3 of 3 on a sibling project's round-4 drains.
</preflight>

Seating: slot `~1`, level 0, FIRST of a two-order queue (`EN-s-32-r6` -> `EN-c-33-r6`). Round 6 of LGIC_ENFORCE, issued by `2.0.0_SA_COO~G` on decomposition v3.5 s.0f, from `1.0.0_SA_CTO`'s round-5 analysis @`b683398fda` and R-46 as corrected @`ab9a8f356b`. Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r6/` (`check_en_r6.py`, 9 subcommands and a 28-arm self-test; `R6_BASE.json` pinning `372b1d653d`). Rulings carried: R-46 (corrected), R-42, R-19.
