# TO LGIC_ENFORCE.TO-EN-c-33-r6 -- the campaign continued: 1370 carried rows, three classes, and the 235 that are not a timebox

<to_id>LGIC_ENFORCE.TO-EN-c-33-r6</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-18</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` (ADMITTED; both halves current) | **Decomp cell:** `EN-c-33` (decomposition v3.5 s.0f) | **outcome_ref:** FWD-5 | **depends_on:** `EN-s-32-r6` drained -- same queue, same channel

---

## WORKER FACE

### THE CELL

`EN-c-33` (rulings **R-38**, **R-33**, **R-29**). Round 5's campaign resolved 41 of 1411 placeholder rows,
carded 1370 with owners and reasons, and **stopped on its timebox as designed**. You take the 1370 forward.

**MEASURE YOUR OWN START FROM THE HANDING RECORD, not from this order.** It is
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/PLACEHOLDER_CAMPAIGN_R5.json`, its
`delta_riding_next_round.count`. The arm `c33-population` refuses a declared start that disagrees with a
fresh read of it -- an inherited count is a subset measurement until you ask what population it enumerated.

### THE THREE CLASSES ARE CARRIED BY NAME, AND THE 235 ARE A DIFFERENT QUESTION

Round 5's 1370 split into three reasons, and you carry every one **by name with its count** in an
`inherited_classes` map read fresh from that record:

```
  TIMEBOXED_R33 .......................... 1134   the campaign simply did not reach these
  NON_SYSTEM_PLACEHOLDER_TOKEN ............ 235   the token IS NOT A SYSTEM AT ALL
  TYPE_MISMATCH_NEEDS_CONFIRMATION ........... 1   a repo row typed EC2_INSTANCE whose Terraform declares a Lambda role
```

⛔ **THE 235 DO NOT RIDE THE TIMEBOX AND ONE REMEDY DOES NOT MOVE BOTH** (Rule 24(iv), state coherence).
A `TIMEBOXED_R33` row is one nobody got to -- next round reaches it. A `NON_SYSTEM_PLACEHOLDER_TOKEN` row
is one where **"resolve the substitution from a declared source" may not even apply**, because the token
is not a system. Folding them together would let 235 rows ride a timebox forever under a reason that was
never theirs. So your record carries a **`non_system_disposition`** object with its own `rule` and `count`
-- what the disposition of that class IS, stated once, and how many rows it covers.

### WHAT YOU DO

1. **Measure the start** (above), and print it.
2. **RESOLVE what can be measured** from a declared source -- `lambda-source-map.json`'s
   `source_dir`/`tf_file`, `EC2_MANIFEST.json`'s `source_path`, the Terraform tree that declares it --
   with `owner_claim: inferred` and the citation as `owner_basis`.
3. **CARD what cannot**, with owner and reason. **DEFER what the timebox stops you reaching**, also with
   owner and reason. `resolved + carded + deferred == start` and the arm checks it.
4. **PRINT BOTH DENOMINATORS** -- `population_at_start` and `population_at_close`, instrument named, with a
   `denominator_delta_note` if they differ.

### THE TWO BOUNDS THAT ARE RULINGS

- **R-29's FENCE GUARD:** a row whose mint would change a GENERATED POLICY on an APPLIED resource is NOT
  minted -- it is carded **BLOCKING** for never-widen sign-off. `infra/logic/registry/exemptions.json` must
  stay byte-identical to the pinned base (22,891 bytes at `372b1d653d`), and an unreadable baseline is a
  FAIL, because a guard that cannot read its own baseline certifies nothing.
- **R-33's TIMEBOX:** past your start + 25 MEASURED resolutions, **STOP**, file the delta, let the
  remainder ride round 7. **Stopping is not failing** -- round 5 stopped and graded PASS on that branch.
  The arm grades both branches: over the bar without stopping FAILS, and stopping without a well-formed
  `delta_riding_next_round` FAILS too.

**DO NOT:** run `generate`; add a row to `exemptions.json`; mint `security` (R-39 -- and its TOKEN_COLLISION
cards were corrected in round 5); or touch `NAMING_CENSUS_REPORT.r4.md` / `.r5.md` and
`NAMING_CENSUS_COMPARISON.r4.md`, which belong to other workers' folders and whose lane gate will refuse
you.

**Read:** the r5 campaign record whole; `infra/logic/registry/` `_about` blocks; decomposition v3.5 s.0f;
rows `LGIC_ENFORCE-W2-S13` and `-S64` for what round 5 closed and what it did not.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="C33R6-AC1" cell_refs="EN-c-33"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r6/check_en_r6.py c33-population</invocation><expect>PASS-C33-START-IS-ROUND-5S-MEASURED-DELTA</expect></criterion>

<criterion id="C33R6-AC2" cell_refs="EN-c-33"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r6/check_en_r6.py c33-covered</invocation><expect>PASS-C33-EVERY-CARRIED-ROW-ACCOUNTED</expect></criterion>

<criterion id="C33R6-AC3" cell_refs="EN-c-33"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r6/check_en_r6.py c33-classes</invocation><expect>PASS-C33-INHERITED-CLASSES-CARRIED-BY-NAME</expect></criterion>

<criterion id="C33R6-AC4" cell_refs="EN-c-33"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r6/check_en_r6.py c33-fence</invocation><expect>PASS-C33-APPLIED-FENCE-UNCHANGED</expect></criterion>

<criterion id="C33R6-AC5" cell_refs="EN-c-33"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r6/check_en_r6.py c33-timebox</invocation><expect>PASS-C33-R33-TIMEBOX-RESPECTED</expect></criterion>

<criterion id="C33R6-AC6" cell_refs="EN-c-33" judgment="true"/>

<expected_criteria>C33R6-AC1, C33R6-AC2, C33R6-AC3, C33R6-AC4, C33R6-AC5, C33R6-AC6</expected_criteria>

**AT THE CUT:** AC1, AC2, AC3 and AC5 read **FAIL** (their inputs do not exist yet). **AC4 reads PASS and
is a GUARD, not a target** -- the applied fence must STAY unchanged, so that arm refuses your work only if
you touch it. Measured by the issuer, not assumed.

**`C33R6-AC6`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether a RESOLVED row's substitution was
genuinely MEASURED from a declared source rather than inferred from the token's shape; and whether the
`non_system_disposition` rule is one a later census can ACT on rather than a label that parks 235 rows.

`<WS>` is your worktree's absolute path.

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/` and this order's own file. Nothing else. A path you need that is not named is a BLOCKING row, never an override.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- **Fixed inputs are read-only.** Round 5's own campaign arm WAS defective and a worker filing a row is how it was found -- if an arm here cannot be satisfied by work you believe is right, that is a BLOCKING row quoting the arm.
- **Surprises** go to the project's `INVESTIGATION_v1.md`, appended to the fence that PARSES AS A LIST -- that file carries THREE json fences and only fence 0 is the row array; a splice at the file's last `]` would corrupt the document. Id `LGIC_ENFORCE-W<n>-S<k>`, `<k>` one above the highest in ANY document under that channel.
- **Numbers in this order are CONTEXT, measured by the issuer at the cut, never acceptance values.** Re-measure at your own tree -- that is AC1.
- **Commit before you grade.**
- **Nothing live moves.** Every AWS read is read-only through the `.tools/aws` shim. No apply, no write, no deploy, no rename.
- **Disk is tight.** Keep scratch small; delete any temporary worktree you create before you report.

<paths>
infra/logic/registry/systems.json
infra/logic/registry/resources.json
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.5, round-6 cell `EN-c-33` (section 0f).
<owned_cells>EN-c-33</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `C33R6-AC1` through `C33R6-AC6`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-c-33-r6.campaign-continued.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> C33R6-AC1,C33R6-AC2,C33R6-AC3,C33R6-AC4,C33R6-AC5,C33R6-AC6 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-c-33-r6.campaign-continued.md` BEFORE the `complete` flip.
Result file `campaign-continued.r6.result.md` beside it; your campaign record is `PLACEHOLDER_CAMPAIGN_R6.json` in the same folder. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`C33R6-AC6` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape, and PRINT BOTH DENOMINATORS and the three class counts.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-6 cut: the campaign reads declared sources and creates no schedule.
comp-iam: RUN at the round-6 cut: no grant moves. The fence guard exists precisely because a mint COULD change a generated policy on an applied resource, and that case is carded BLOCKING rather than minted.
comp-adversary: RUN at the round-6 cut: the denominator is the adversarial read -- the cell measures its own start from the handing record rather than inheriting it, re-measures at write time, and prints both. Round 5 did the same and it is the half of R-38 most likely to be skipped.
lane: the <paths> block is the grant (RULING 1 shape c); deliverables/<serial>/ is granted by the tree convention.
contention: systems.json and resources.json are written by no other open order in any LGIC project at the cut. The channel is also written by EN-s-32-r6 EARLIER in this same queue, which is why this cell is second. No round-6 cell runs `generate`, so the two opal_name test fixtures stay at their round-3 stamp -- an ISSUER act still owed, recorded in the v3.4 section and unchanged here.
</preflight>

Seating: slot `~1`, level 1, SECOND of the queue (`EN-s-32-r6` -> `EN-c-33-r6`). Round 6 of LGIC_ENFORCE, issued by `2.0.0_SA_COO~G` on decomposition v3.5 s.0f. Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r6/` (`check_en_r6.py`, `R6_BASE.json` pinning `372b1d653d`). Rulings carried: R-38, R-33, R-29, R-39.
