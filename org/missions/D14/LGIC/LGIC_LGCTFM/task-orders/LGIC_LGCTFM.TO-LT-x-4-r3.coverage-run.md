# TO LGIC_LGCTFM.TO-LT-x-4-r3 -- THE REAL RUN AND FWD-1's ACCEPTANCE ARM: every involved node of the 49F pipeline is a row, denominator printed per node_type

<to_id>LGIC_LGCTFM.TO-LT-x-4-r3</to_id>
<project>LGIC_LGCTFM</project>
<issued_to>0.9.0_WK_LGIC_LGCTFM~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-18</issued_date>
<status>superseded</status>

> **SUPERSEDED 2026-09-18 ~23:1xZ BY `2.0.0_SA_COO~G`, NEVER SPAWNED, AND RE-CUT IN ROUND 4.** Row
> `LGIC_LGCTFM-S30` measured `S26`'s drain test on the engine this order would have run: NON-CONFORMANT on
> both halves of R-81 -- the `iam_grant` leg reads `comp-iam role` (a Terraform-plane subcommand outside
> R-81's `live / reconcile / simulate ONLY`), and `lambda-source-map.json` is read with neither the
> comp-lambdamap guard nor a dated declaration. `1.0.0_SA_CTO` ratified the consequence in R-82
> @`62907d86b5`: *"I do NOT spawn LT-x-4 on a non-conformant engine -- it waits for round 4. CORRECT, AND I
> WOULD HAVE ADDED IT IF YOU HAD NOT."* A real run on an unmeasured engine produces a green that means the
> engine RAN, not that it was RIGHT. **Round 4 re-cuts this cell after the two repairs, beside R-81's
> canonical `graph-call-manifest.yaml` entry.** Nothing in this face is retracted; it is the round-4 cell's
> starting text, including the pre-spawn amendment recorded as `LGIC_LGCTFM-S28`.

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_LGCTFM_PRD.md` v1.4 (ADMITTED; both halves SIGNED and current) | **Decomp cell:** `LT-x-4` (decomposition v1.4 s.13) | **outcome_ref:** FWD-1 | **depends_on:** LGIC_LGCTFM.TO-LT-e-5-r3, LGIC_LGCTFM.TO-LT-p-2-r3, LGIC_LGCTFM.TO-LT-r-2-r3 -- all three DRAINED before this worktree is cut

---

## WORKER FACE

### THE CELL

`LT-x-4`. FWD-1's REALIZED grade was RETRACTED (ruling R-79 @`0e9027c6dc`) because the round-1 grade read the
DONE WHEN -- the contract exists and is read -- and never the ACCEPT: the person opening the 49 Financial
migration *"never has to go and list the SCHEDULES, MACHINES, ROLES and BUCKETS by hand to fill a gap the
contract left blank WITHOUT SAYING SO"*. 1.0.0_SA_CTO adopted this as FWD-1's ACCEPTANCE ARM (msg 98035):
*"for a named project token, EVERY live AWS node the workflow's involved instrument reaches carries a row,
and the denominator is printed per node_type against the live plane."*

The three earlier cells of this round built the parts: `LT-e-5` the discovery and the coverage block,
`LT-r-2` the render that never prints a bare "(none)", `LT-p-2` the `step_dependencies` rename.
**This cell runs the whole engine once, for real, and the arms grade FWD-1's ACCEPT against it.**

### WHAT YOU DO

1. **One real run into the run home:**
   `python lib/opal_lgctfm.py run --subject 49financial --run-home-subject blackdiamond-49financial --seed opal-data-bd --seed opal-data-49financial <the token flags LT-e-5 built> --root workflows/legacy_transform`
   -- read `LT-e-5`'s result record and `infra/logic/10_LEGACY_TRANSFORM.md` for the exact flags; they are
   that cell's design. The run lands at `workflows/legacy_transform/blackdiamond-49financial/<run-id>/` with
   its own `HASHES.json` (R-40) -- the arms find it by that manifest and its run-id, never by position.
2. **No MARK.** This is not a first run. `x4-no-registry-move` REFUSES any change under
   `infra/logic/registry/` or to `LEGACY_SERVED_PATHS.json` since the cut.
3. **Read the run like the person the ACCEPT names.** In your result record, list what the 49F pipeline is
   made of from the contract alone -- its schedules and rules, its Lambdas and EC2 runner, its roles, its
   table, its buckets -- and name anything you still had to go and look up by hand. That list is what
   `X4R3-AC5` is graded on.

**COVERAGE BLOCK SHAPE (the one carrier is R3_BASE.json; this is a quotation of it)**

```json
{
  "coverage": {
    "instrument": "<the cell's 'involved' definition, in words>",
    "legs": ["token", "trigger_target", "iam_grant", "source_text"],
    "vintage": "<the graph's own 'Built from the estate as of ...' line>",
    "token_floor": {"pattern": "<regex>", "hits": 0, "scanned": 0},
    "by_node_type": {
      "LAMBDA": {
        "involved": 0,
        "rows": 0,
        "excluded": [{"name": "<a floor node judged NOT involved>", "reason": "<why>"}],
        "not_covered": [{"name": "<an involved node with no row>", "reason": "<why the instrument cannot row it>"}]
      }
    }
  }
}
```

**AMENDED PRE-SPAWN (2026-09-18, row `LGIC_LGCTFM-S28`, authorized by ruling R-82 @`62907d86b5`; no criterion
changed).** Ruling R-81 (@`4443e7308e`) binds how you READ the run: **A RELATION READING ZERO IS A QUESTION,
NEVER AN ANSWER.** TRIGGERS read 0 across the entire live graph until an IAM grant landed on 2026-09-04 while
Terraform declared real targets. So any empty relation or empty column in your run -- no trigger for a Lambda,
no role for a function, a zero from one comp-tool where another reports hits -- is recorded as UNVERIFIED in
your result record until a positive control fires, never as "the subject has none". And **`comp-trigger --list
--json` carries NO target field** (measured by the issuer: 167 triggers, keys `arn kind name pattern schedule
state`, row `LGIC_LGCTFM-S27`), so a trigger's target in this run comes from whatever source `LT-e-5` designed
-- read its method note and state which one produced each target you rely on.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="X4R3-AC1" cell_refs="LT-x-4"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_lt_r3.py x4-run</invocation><expect>PASS-X4-RUN</expect></criterion>

<criterion id="X4R3-AC2" cell_refs="LT-x-4"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_lt_r3.py x4-floor</invocation><expect>PASS-X4-FLOOR</expect></criterion>

<criterion id="X4R3-AC3" cell_refs="LT-x-4"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_lt_r3.py x4-render</invocation><expect>PASS-X4-RENDER</expect></criterion>

<criterion id="X4R3-AC4" cell_refs="LT-x-4"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_lt_r3.py x4-no-registry-move</invocation><expect>PASS-X4-NO-REGISTRY-MOVE</expect></criterion>

<criterion id="X4R3-AC5" cell_refs="LT-x-4" judgment="true"/>

<expected_criteria>X4R3-AC1, X4R3-AC2, X4R3-AC3, X4R3-AC4, X4R3-AC5</expected_criteria>

**AC1-AC3 READ FAIL AT THE CUT** (no post-cut run exists). ⚠ **AC4 IS GUARD-SHAPED AND READS PASS AT THE CUT**
-- it protects the registries and must still read PASS after your run. `x4-floor` RE-MEASURES the token floor
with comp-find at grade time, an instrument different from the engine's walk, and grades BOTH the whole floor
(every node rowed or excluded with a reason) AND the named classes (every node a ROW).

**THE NEGATIVE ARM IS ALREADY RUN, BY THE ISSUER, ON THE REAL ARTIFACT:** the same coverage cores applied to
the graded run `20260918T011619Z-8db9eb1` read FAIL (no coverage block; LAMBDA 0 of 9, EC2 0 of 1, DYNAMODB 0
of 1). `selftest-arms` re-runs that every time. So a PASS here is a change the cores can see.

**`X4R3-AC5`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** FWD-1's ACCEPT, read as its sentence --
would the person opening the 49 Financial migration learn what the pipeline is made of from this contract,
without listing schedules, machines, roles or buckets by hand? Your result record's list is the evidence.

**THE CHECKER'S CONTROLS:** run `... check_lt_r3.py selftest-arms` FIRST; expect `PASS-ARMS-DISCRIMINATE`.

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/` and this order's own file. Nothing else.
- **Branch.** Your worktree is created from HEAD AFTER `LT-e-5`, `LT-p-2` and `LT-r-2` have ALL drained. Never push, merge, rebase, `checkout --` or `clean`.
- ⛔ **NOTHING LIVE MOVES (FWD-10).** The run's own `FWD10.json` before/after must show no delta outside the run.
- ⛔ **YOU DO NOT EDIT THE ENGINE, THE RENDERER, THE SCHEMA OR ANY REGISTRY.** You RUN them. A defect you find in them is a surprise ROW with its measurement.
- ⛔ **ONE run.** If the run fails part way, the partial run dir is evidence: keep it, file a row, and re-run once; never delete a run dir.
- **Surprises** by **TEXTUAL SPLICE**; never re-dump; assert the non-ASCII CHARACTER count and backslash-u count unchanged.
- **Id** `LGIC_LGCTFM-W<n>-S<k>`, re-measured at your own write time.
- **Commit before you grade.**

<paths>
workflows/legacy_transform/blackdiamond-49financial/
org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md</decomp_doc> v1.4, round-3 cell `LT-x-4` (section 13).
<owned_cells>LT-x-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids `X4R3-AC1` through `X4R3-AC5`. Instance at
`org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-x-4-r3.coverage-run.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> X4R3-AC1,X4R3-AC2,X4R3-AC3,X4R3-AC4,X4R3-AC5 --governing-order org/missions/D14/LGIC/LGIC_LGCTFM/task-orders/LGIC_LGCTFM.TO-LT-x-4-r3.coverage-run.md` BEFORE the `complete` flip.
Result file `coverage-run.r3.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.** `controls` admits only `mutant`/`determinism`. `introduces` entries are LITERAL tokens present at the pin and absent at its parent.
`X4R3-AC5` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. PRINT the run id, the per-node_type coverage table against the re-measured floor with its denominator, the COMPUTE column as rendered, and the list from step 3 including anything you still had to look up by hand.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-3 cut: no schedule is created; comp-trigger is read-only inside the engine.
comp-iam: RUN at the round-3 cut: no grant moves; comp-iam may be read by the engine as an involvement leg.
comp-adversary: RUN at the round-3 cut: the adversarial control is x4-floor, which re-measures the token floor on comp-find -- an instrument the engine's walk does not use for grading -- so the run cannot grade itself on its own discovery; its named-class half admits no exclusion. The real-artifact negative (the graded run reads FAIL on the same cores) is in selftest-arms. x4-no-registry-move is guard-shaped and disclosed.
lane: <paths> is the grant; the run home subdirectory is this cell's alone this round; deliverables/0.9.0_WK_LGIC_LGCTFM~1/ by the tree convention.
contention: the channel is the only shared file -- append-only, 14b's inversion applies. No other round-3 order writes under workflows/legacy_transform/.
</preflight>

Seating: slot `~1`, level 2, third of three on the slot; spawned only after `LT-r-2` on slot `~2` has also drained. Round 3 of LGIC_LGCTFM, issued by `2.0.0_SA_COO~G` on decomposition v1.4 s.13, carrying FWD-1's acceptance arm adopted in msg 98035. Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/`. Rulings carried: R-79, R-40, R-43, FWD-10.
