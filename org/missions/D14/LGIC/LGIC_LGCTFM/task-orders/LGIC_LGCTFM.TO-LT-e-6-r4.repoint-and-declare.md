# TO LGIC_LGCTFM.TO-LT-e-6-r4 -- THE TWO R-81 REPAIRS: the authorization leg moves to the LIVE plane, and the hand surface is guarded or declared

<to_id>LGIC_LGCTFM.TO-LT-e-6-r4</to_id>
<project>LGIC_LGCTFM</project>
<issued_to>0.9.0_WK_LGIC_LGCTFM~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-19</issued_date>
<status>complete -- 0.9.0_WK_LGIC_LGCTFM~1. AC2-AC4 PASS at the cell's pin; AC1 read FAIL there because THE ISSUER'S ARM WAS THE DEFECT (e6-sources searched the whole method note, so the only passing move was to delete Andrew's COMP-TOOL LEDGER -- LGIC_LGCTFM-W1-S35). Arm repaired @21a163f492; all mechanical criteria re-run by 2.0.0_SA_COO~G at the merged tree 9ac7b0b2c3 and PASS. The pinned proof is NOT rewritten and still records AC1 FAIL at its own vintage. AC5 judgment PASS at L9 (3.0.0_SA_CVO).</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_LGCTFM_PRD.md` v1.4 (ADMITTED; both halves SIGNED and current) | **Decomp cell:** `LT-e-6` (decomposition v1.5 s.15) | **outcome_ref:** FWD-1 | **depends_on:** none -- first on slot `~1`, ahead of `LT-x-4b`

---

## WORKER FACE

### THE CELL

`LT-e-6`. Round 3's discovery works and its coverage is complete -- and row `LGIC_LGCTFM-S30` measured it
NON-CONFORMANT against ruling R-81 on **both** halves. The cell that built it could not have been built
against R-81: the ruling landed 25 minutes after that round was issued. **Your job is the repair, not a
rebuild.**

```
  HALF ONE   the iam_grant leg reads `comp-iam role ""` -- a TERRAFORM-plane sibling of the refused
             `roles`. R-81 assigns authorization to `comp-iam live / reconcile / simulate` ONLY.
  HALF TWO   lambda-source-map.json is read by the source_text leg with NEITHER the comp-lambdamap guard
             NOR a dated declaration. R-81: "No third option."
```

**WHY HALF TWO IS NOT A FORMALITY, measured by `1.0.0_SA_CTO`:** the map holds **216 entries against 217
live**, and **THE TOTALS NEARLY AGREE WHILE 19 NAMES DISAGREE** -- 10 live functions absent from the map, 9
map entries with no live function, the sharpest being a RENAME the map never followed. **A reader comparing
COUNTS concludes the map is current.**

### WHAT YOU BUILD

1. **RE-POINT THE `iam_grant` LEG** onto `comp-iam live` (or `reconcile` / `simulate`). That also moves the
   leg from the DECLARED plane to the LIVE one, which is the axis R-81's assignment exists to hold. Update
   the leg's description in `infra/logic/10_LEGACY_TRANSFORM.md` and in the contract's `coverage.instrument`
   so the record and the code say the same thing.
2. **TREAT THE HAND SURFACE**, one of exactly two ways, and say which in your record:
   - **GUARDED** -- run comp-lambdamap's two-plane check as part of the walk and carry its output; or
   - **DECLARED** -- a block in the contract's coverage carrying the map's **date**, its **owner**, and the
     **condition that un-defers it**.
3. **RE-RUN THE WALK** into `<WS>/org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/e6_walk/e6.lgctfm-contract.json`.
   ⛔ **THE FILENAME IS NOT A STYLE CHOICE.** `.tools/receiving-check.py` routes BY PATH; a contract in a
   deliverables folder is routed only if it is named `*.lgctfm-contract.json`. That exact defect broke round
   3's `e5-schema` arm (rows `W1-S23` / `S29`), and it was the ISSUER's, not a worker's.
4. ⛔ **A RE-POINT MAY ADD INVOLVED NODES AND MUST NOT SILENTLY REMOVE ANY.** `e6-no-loss` compares your
   per-node_type `involved` against round 3's measured figures (LAMBDA 67, IAM_ROLE 46, S3Key 154,
   EVENT_RULE 37, EC2_INSTANCE 19, IAM_POLICY 22, INSTANCE_PROFILE 6, SCHEDULE 9, ...). **A drop is
   admissible ONLY when your record NAMES the node and the leg that used to reach it and why the
   R-81-assigned instrument does not.** Moving from the declared plane to the live one can legitimately drop
   a declared-only role -- say so, per node, and the arm passes.

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

**You fill `repoint`, `coverage_delta` and `stale_proofs`** -- `entry` is `LT-m-1`'s and `run` is
`LT-x-4b`'s. Write it to `<WS>/org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/REPOINT_R4.json`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="E6R4-AC1" cell_refs="LT-e-6"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_lt_r4.py e6-sources</invocation><expect>PASS-E6-SOURCES</expect></criterion>

<criterion id="E6R4-AC2" cell_refs="LT-e-6"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_lt_r4.py e6-handsurface</invocation><expect>PASS-E6-HANDSURFACE</expect></criterion>

<criterion id="E6R4-AC3" cell_refs="LT-e-6"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_lt_r4.py e6-coverage</invocation><expect>PASS-E6-COVERAGE</expect></criterion>

<criterion id="E6R4-AC4" cell_refs="LT-e-6"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_lt_r4.py e6-no-loss</invocation><expect>PASS-E6-NO-LOSS</expect></criterion>

<criterion id="E6R4-AC5" cell_refs="LT-e-6" judgment="true"/>

<expected_criteria>E6R4-AC1, E6R4-AC2, E6R4-AC3, E6R4-AC4, E6R4-AC5</expected_criteria>

**ALL FOUR MECHANICAL CRITERIA READ FAIL AT THE CUT**, measured by the issuer. `e6-coverage` runs ROUND 3's
OWN CORES by import -- the grading rule is not re-implemented here, and its floor is re-measured on comp-find
at your grade time.

**`E6R4-AC5`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether the re-point is a real move to the
LIVE plane rather than a rename of the same read, and whether every drop you name is genuinely explained by
the plane change rather than by the instrument being asked a narrower question.

**THE CHECKER'S CONTROLS:** run `... check_lt_r4.py selftest-arms` FIRST; expect `PASS-ARMS-DISCRIMINATE`
(21 arms, 8 positive-satisfiability). An arm a CORRECT repair cannot satisfy is a BLOCKING surprise row
quoting the arm and its output -- never a workaround, never an edit to a fixed input.

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/` and this order's own file. Nothing else.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- ⛔ **NOTHING LIVE MOVES (FWD-10).** Every AWS read is read-only through the assigned comp-tools.
- ⛔ **YOU DO NOT RUN `run` INTO THE RUN HOME** -- the real run is `LT-x-4b`'s, next on your slot, and it must not start on an engine whose conformance is unmeasured.
- ⛔ **YOU DO NOT EDIT `org/modules/graph/graph-call-manifest.yaml`** -- that is `LT-m-1`'s, on the other slot.
- ⛔ **YOU DO NOT WIDEN THE `involved` DEFINITION** to recover a drop. Name the drop instead; an honest loss with its reason is what the arm admits.
- **Surprises** by **TEXTUAL SPLICE**; never re-dump; assert the non-ASCII CHARACTER count and backslash-u count unchanged. Copy an existing row's field set exactly.
- **Id** `LGIC_LGCTFM-W<n>-S<k>`, re-measured at your own write time. **One other order is open this round.**
- Every `.py` edit passes `.tools/commit-gate.sh`. **Commit before you grade.**

<paths>
lib/opal_lgctfm.py
infra/logic/10_LEGACY_TRANSFORM.md
org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md</decomp_doc> v1.5, round-4 cell `LT-e-6` (section 15).
<owned_cells>LT-e-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids `E6R4-AC1` through `E6R4-AC5`. Instance at
`org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-e-6-r4.repoint-and-declare.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> E6R4-AC1,E6R4-AC2,E6R4-AC3,E6R4-AC4,E6R4-AC5 --governing-order org/missions/D14/LGIC/LGIC_LGCTFM/task-orders/LGIC_LGCTFM.TO-LT-e-6-r4.repoint-and-declare.md` BEFORE the `complete` flip.
Result file `repoint-and-declare.r4.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.** `controls` admits only `mutant`/`determinism`. `introduces` entries are LITERAL tokens present at the pin and absent at its parent.
`E6R4-AC5` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. PRINT the authorization instrument you moved to, the hand-surface treatment and its evidence, the per-node_type involved counts round 3 vs round 4, and every dropped node with the leg that used to reach it.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-4 cut: no schedule is created or read beyond comp-trigger's read-only census.
comp-iam: RUN at the round-4 cut: no grant moves. comp-iam live/reconcile/simulate are READ as the authorization leg; nothing is written to IAM, and the Terraform-plane subcommands are refused as discovery sources by R-81.
comp-adversary: RUN at the round-4 cut: the adversarial control is e6-no-loss paired with e6-sources. The cheapest satisfying move for e6-sources is to rename the leg's description while still reading the Terraform plane; the coverage arm re-measures the floor on comp-find at grade time and no-loss compares against round 3's measured involved counts, so a leg that stopped reaching nodes shows up as an unnamed drop. e6-handsurface admits exactly two treatments and no third.
lane: <paths> is the grant; deliverables/0.9.0_WK_LGIC_LGCTFM~1/ by the tree convention. lib/opal_lgctfm.py has one writer at a time and LT-x-4b only RUNS it.
contention: the channel is shared with slot ~2 -- append-only, 14b's inversion applies.
</preflight>

Seating: slot `~1`, level 0, first of two on the slot. Round 4 of LGIC_LGCTFM, issued by `2.0.0_SA_COO~G` on decomposition v1.5 s.15, from `S30`'s two halves as R-82 ratified them. Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/`. Rulings carried: R-81, R-82, S30, S23/S29, S32.
