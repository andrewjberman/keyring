# TO LGIC_LGCTFM.TO-LT-x-5-r4 -- THE REAL RUN, RE-CUT: FWD-1's acceptance arm, on an engine whose conformance was measured first

<to_id>LGIC_LGCTFM.TO-LT-x-5-r4</to_id>
<project>LGIC_LGCTFM</project>
<issued_to>0.9.0_WK_LGIC_LGCTFM~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-19</issued_date>
<status>complete -- 0.9.0_WK_LGIC_LGCTFM~1. AC1/AC2 PASS at the cell's pin; AC3 read FAIL there because THE ISSUER'S ARM WAS THE DEFECT (x4-no-registry-move graded the whole TREE, so 4.0.0_SA_CRO's IRPT_BCKEND commit failed this cell and the cheapest green was to revert another project -- LGIC_LGCTFM-W1-S39). Arm repaired @d08be0b693; all mechanical criteria re-run by 2.0.0_SA_COO~G at the merged tree 5755205bed and PASS. The pinned proof is NOT rewritten and still records AC3 FAIL at its own vintage. AC4 judgment PASS at L9 (3.0.0_SA_CVO).</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_LGCTFM_PRD.md` v1.4 (ADMITTED; both halves SIGNED and current) | **Decomp cell:** `LT-x-5` (decomposition v1.5 s.15) | **outcome_ref:** FWD-1 | **depends_on:** LGIC_LGCTFM.TO-LT-e-6-r4 -- DRAINED, with its two conformance arms PASS, before this worktree is cut

---

## WORKER FACE

### THE CELL

`LT-x-5`. This is `LT-x-4` re-cut. Round 3 issued it, `S30` measured the engine NON-CONFORMANT against
R-81, and `R-82` ratified the consequence: **a real run on an unmeasured engine produces a green that means
the engine RAN, not that it was RIGHT.** It was superseded and never spawned. `LT-e-6` has now repaired both
halves, and this cell runs the subject for real.

FWD-1's ACCEPT, which this run is graded against: the person opening the 49 Financial migration *"never has
to go and list the SCHEDULES, MACHINES, ROLES and BUCKETS by hand to fill a gap the contract left blank
WITHOUT SAYING SO"*. `1.0.0_SA_CTO` adopted the arm: **every live node the involved instrument reaches
carries a row, and the denominator is printed per node_type against the live plane.**

### WHAT YOU DO

1. **One real run into the run home:**
   `python lib/opal_lgctfm.py run --subject 49financial --run-home-subject blackdiamond-49financial --seed opal-data-bd --seed opal-data-49financial <the token/leg flags LT-e-6 built> --root workflows/legacy_transform`
   -- read `LT-e-6`'s result record and `infra/logic/10_LEGACY_TRANSFORM.md` for the exact flags; they are
   that cell's design, now R-81-conformant. The run lands at
   `workflows/legacy_transform/blackdiamond-49financial/<run-id>/` with its own `HASHES.json` (R-40); the
   arms find it by that manifest and its run-id, never by position.
2. **No MARK.** This is not a first run. `x4-no-registry-move` REFUSES any change under
   `infra/logic/registry/` or to `LEGACY_SERVED_PATHS.json` since the cut.
3. **Read the run like the person the ACCEPT names.** In your result record, list what the 49F pipeline is
   made of from the contract alone -- its schedules and rules, its Lambdas and EC2 runner, its roles, its
   table, its buckets -- and name anything you still had to look up by hand. That list is what `AC4` is
   graded on.

**AMENDED PRE-SPAWN ON THE SUPERSEDED FACE (rows `S28`, `S27`), carried here:** R-81 binds how you READ the
run -- **A RELATION READING ZERO IS A QUESTION, NEVER AN ANSWER.** TRIGGERS read 0 across the entire live
graph until an IAM grant landed on 2026-09-04 while Terraform declared real targets. Any empty relation or
empty column in your run is recorded as UNVERIFIED until a positive control fires, never as "the subject has
none". And `comp-trigger --list --json` carries **NO target field** (167 entries, keys `arn kind name pattern
schedule state`) -- targets come from whatever source `LT-e-6` designed, and you state which produced each.

**AMENDED PRE-SPAWN A SECOND TIME, ON WHAT `LT-e-6` MEASURED AT ITS DRAIN (rows `W1-S36`, `W1-S38`).**

1. ⛔ **DO NOT REACH FOR `coverage.hand_surfaces` IN THE CONTRACT -- IT CANNOT EXIST THERE.**
   `org/standards/LGCTFM_CONTRACT.schema.json` `$defs.coverage` is CLOSED (`additionalProperties: false`),
   so R-81's guard output is REFUSED by the schema: `LT-e-6`'s first build read
   `HAND BACK ... Additional properties are not allowed`. The guard rides in
   `deliverables/0.9.0_WK_LGIC_LGCTFM~1/e6_walk/HAND_SURFACES.json`, beside the contract, and the contract
   itself reads `ACCEPT lgctfm-contract` (rc=0). **The schema is OUTSIDE your grant and is not yours to
   widen** -- read the sidecar, cite it, and if your run needs the guard inside the contract, that is a ROW,
   not an edit. `LT-e-6` flagged this FOR YOU specifically; the round should not pay for it twice.

2. **The stale-proof bar's COUNT is informational and its SET is the bar** (repaired at `21a163f492` on
   `W1-S38`): `fixed_input_commits_since_cut` is checkout-dependent -- measure it AT YOUR OWN WRITE TIME and
   never copy a number from this order -- while `proofs_re_run` must EQUAL the set of ROUND-4 proofs that
   existed before the earliest counted commit. Two round-4 proofs are now pinned (`LT-m-1`, `LT-e-6`), so
   that set is NO LONGER EMPTY: enumerate what the arm names and re-run exactly those, or the arm refuses
   both the under- and the over-enumeration.

**RECORD SHAPE (the one carrier is `deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/R4_BASE.json`; this is a quotation of it)**

```json
{
  "entry": {"id": "<cloud.inventory.*>", "tool": "<the R-81-assigned instrument>", "near_duplicates_considered": [{"id": "<an existing entry>", "why_different": "<...>"}]},
  "repoint": {"legs": ["<leg>"], "authorization_instrument": "<comp-iam live|reconcile|simulate>", "hand_surfaces": [{"file": "<path>", "treatment": "GUARDED|DECLARED", "guard_or_declaration": "<the comp-lambdamap run, or date+owner+un_defers_when>"}]},
  "coverage_delta": {"by_node_type": {"<TYPE>": {"round3_involved": 0, "round4_involved": 0, "dropped": [{"name": "<node>", "old_leg": "<leg>", "why_not_reached": "<...>"}]}}},
  "run": {"run_id": "<the new run>", "registries_unchanged": true},
  "stale_proofs": {"fixed_input_commits_since_cut": 0, "proofs_re_run": []}
}
```

**You fill `run` and `stale_proofs`.** Write it to
`<WS>/org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/COVERAGE_RUN_R4.json`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="X5R4-AC1" cell_refs="LT-x-5"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_lt_r4.py x4-run</invocation><expect>PASS-X4-RUN</expect></criterion>

<criterion id="X5R4-AC2" cell_refs="LT-x-5"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_lt_r4.py x4-floor</invocation><expect>PASS-X4-FLOOR</expect></criterion>

<criterion id="X5R4-AC3" cell_refs="LT-x-5"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_lt_r4.py x4-no-registry-move</invocation><expect>PASS-X4-NO-REGISTRY-MOVE</expect></criterion>

<criterion id="X5R4-AC4" cell_refs="LT-x-5" judgment="true"/>

<expected_criteria>X5R4-AC1, X5R4-AC2, X5R4-AC3, X5R4-AC4</expected_criteria>

**AC1 AND AC2 READ FAIL AT THE CUT** (no post-cut run exists). ⚠ **AC3 IS GUARD-SHAPED AND READS PASS AT THE
CUT** -- it protects the registries and must still read PASS after your run. `x4-floor` runs ROUND 3's OWN
CORES by import and RE-MEASURES the token floor with comp-find at grade time, an instrument the engine's walk
does not use for grading, so the run cannot grade itself on its own discovery.

**`X5R4-AC4`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** FWD-1's ACCEPT, read as its sentence --
would the person opening the 49 Financial migration learn what the pipeline is made of from this contract,
without listing schedules, machines, roles or buckets by hand? Your result record's list is the evidence.

**THE CHECKER'S CONTROLS:** run `... check_lt_r4.py selftest-arms` FIRST; expect `PASS-ARMS-DISCRIMINATE`.

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/` and this order's own file. Nothing else.
- **Branch.** Your worktree is cut from HEAD AFTER `LT-e-6` has drained. Never push, merge, rebase, `checkout --` or `clean`.
- ⛔ **NOTHING LIVE MOVES (FWD-10).** The run's own `FWD10.json` before/after must show no delta outside the run.
- ⛔ **YOU DO NOT EDIT THE ENGINE, THE RENDERER, THE SCHEMA, THE MANIFEST OR ANY REGISTRY.** You RUN them. A defect you find is a surprise ROW with its measurement.
- ⛔ **ONE run.** If it fails part way, the partial run dir is evidence: keep it, file a row, re-run once; never delete a run dir.
- **Surprises** by **TEXTUAL SPLICE**; never re-dump; assert the non-ASCII CHARACTER count and backslash-u count unchanged.
- **Id** `LGIC_LGCTFM-W<n>-S<k>`, re-measured at your own write time.
- **Commit before you grade.**

<paths>
workflows/legacy_transform/blackdiamond-49financial/
org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md</decomp_doc> v1.5, round-4 cell `LT-x-5` (section 15).
<owned_cells>LT-x-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids `X5R4-AC1` through `X5R4-AC4`. Instance at
`org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-x-5-r4.coverage-run-on-the-repaired-engine.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> X5R4-AC1,X5R4-AC2,X5R4-AC3,X5R4-AC4 --governing-order org/missions/D14/LGIC/LGIC_LGCTFM/task-orders/LGIC_LGCTFM.TO-LT-x-5-r4.coverage-run-on-the-repaired-engine.md` BEFORE the `complete` flip.
Result file `coverage-run-on-the-repaired-engine.r4.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.** `controls` admits only `mutant`/`determinism`. `introduces` entries are LITERAL tokens present at the pin and absent at its parent.
`X5R4-AC4` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. PRINT the run id, the per-node_type coverage table against the re-measured floor with its denominator, the COMPUTE column as rendered, every relation that read zero and is therefore UNVERIFIED, and the list from step 3 including anything you had to look up by hand.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-4 cut: no schedule is created; comp-trigger is read-only inside the engine.
comp-iam: RUN at the round-4 cut: no grant moves; comp-iam live/reconcile/simulate are read by the engine as the authorization leg.
comp-adversary: RUN at the round-4 cut: the adversarial control is x4-floor, which re-measures the token floor on comp-find at grade time -- an instrument the engine's walk does not use for grading -- so the run cannot grade itself on its own discovery, and its named-class half admits no exclusion. x4-no-registry-move is guard-shaped and disclosed. The deeper control is the ORDERING: this cell is spawned only after LT-e-6's two conformance arms read PASS (R-82).
lane: <paths> is the grant; the run home subdirectory is this cell's alone this round; deliverables/0.9.0_WK_LGIC_LGCTFM~1/ by the tree convention.
contention: the channel is the only shared file -- append-only, 14b's inversion applies. No other round-4 order writes under workflows/legacy_transform/.
</preflight>

Seating: slot `~1`, level 1, second of two on the slot; spawned only after `LT-e-6` drains with its conformance arms PASS. Round 4 of LGIC_LGCTFM, issued by `2.0.0_SA_COO~G` on decomposition v1.5 s.15, carrying FWD-1's acceptance arm and the pre-spawn amendment recorded as `S28`. Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/`. Rulings carried: R-81, R-82, R-40, S27, S28, S30, FWD-10.
