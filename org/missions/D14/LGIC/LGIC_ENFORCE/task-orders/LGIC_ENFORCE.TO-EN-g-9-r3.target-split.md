# TO LGIC_ENFORCE.TO-EN-g-9-r3 -- the generator prints its target list and the SHIP / REPO-ONLY split, per plane (R-26)

<to_id>LGIC_ENFORCE.TO-EN-g-9-r3</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~5</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-16</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` v1.3 (ADMITTED; both halves current) | **Decomp cell:** `EN-g-9` = round-3 cell 9 (decomposition v3.2, section 0c) | **outcome_ref:** FWD-3 | **depends_on:** none -- level 0

---

## WORKER FACE

### THE CELL

`EN-g-9` -- RULINGS R-16 and R-26 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/SELF_DRIVE_LGIC_RULINGS_20260916.md`). **You edit `lib/opal_naming.py` (and its test file).**

**WHY.** A registry edit re-stamps every generated view that reads the changed file, and some of those views SHIP -- a comment-only re-render once re-minted a production bundle (S50). DEC-5 states the coupling; this cell makes the generator PRINT it.

**THE INTERFACE, fixed so the criteria can grade it:**
```
python lib/opal_naming.py targets [--extra-target <path>]
  TARGETS: <n>
  <SHIP|REPO-ONLY|UNCLASSIFIED> <plane> <path> measured: <instrument>     one row per target
  PLANE <plane>: <k>                                                       one line per plane
  HASH-PINNED CONSUMERS: <n> of <m> scanned
exit non-zero when any row is UNCLASSIFIED
```
- **The target list** is `generate()`'s own `known` list: the `VIEWS` tuples plus the named extras -- 10 at the cut.
- **The split calls EACH PLANE'S OWN RECORD, never a re-derived rule (R-26):** `.tools/safe_deploy_core.py` for the S3/DS plane (at the cut it claims exactly 3: `investor_reporting/directory_runner.py`, `investor_reporting/holdings_snapshot.py`, `runners_49f/perfrp_firm_pin.py`); `infra/aws/lambda/ci/lambda-source-map.json` for the Lambda plane, a SHARED import resolved to every function that imports it; the consuming Terraform root, measured, for the Terraform plane (the `opal_name` module has one consuming root at the cut, `shared-infra`). Each row's `measured:` names the instrument.
- **A target no plane claims prints UNCLASSIFIED and the command exits non-zero.** `--extra-target` adds one path so this can be exercised.
- **`tests/vectors.json` and `tests/opal_name.tftest.hcl` are REPO-ONLY**, their plane named: a fixture beside a shipping module is not a deploy.
- **The hash-pinned-consumer census** counts the instruments keyed on a shipping bundle's md5 or a member's sha256, with its denominator. It is never UNKNOWN and never a bare zero.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="G9R3-AC1" cell_refs="EN-g-9"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py g9-target-count</invocation><expect>PASS-G9-TARGET-COUNT-EQUALS-AST</expect></criterion>

<criterion id="G9R3-AC2" cell_refs="EN-g-9"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py g9-s3-plane-agrees</invocation><expect>PASS-G9-S3-PLANE-EQUALS-GATE</expect></criterion>

<criterion id="G9R3-AC3" cell_refs="EN-g-9"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py g9-unclassified-refuses</invocation><expect>PASS-G9-UNCLASSIFIED-REFUSES</expect></criterion>

<criterion id="G9R3-AC4" cell_refs="EN-g-9"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py g9-fixtures-repo-only</invocation><expect>PASS-G9-FIXTURES-REPO-ONLY</expect></criterion>

<criterion id="G9R3-AC5" cell_refs="EN-g-9"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py g9-consumer-census</invocation><expect>PASS-G9-CONSUMER-CENSUS-PRINTED</expect></criterion>

<criterion id="G9R3-AC6" cell_refs="EN-g-9"><invocation>cd <WS> && timeout 300 python -m pytest -q --color=no lib/tests/test_opal_naming.py</invocation><expect>(?m)^[0-9]+ passed in </expect></criterion>

<criterion id="G9R3-AC7" cell_refs="EN-g-9" judgment="true"/>

<expected_criteria>G9R3-AC1, G9R3-AC2, G9R3-AC3, G9R3-AC4, G9R3-AC5, G9R3-AC6, G9R3-AC7</expected_criteria>

**AC1-AC5 read RED at the cut** (the `targets` subcommand does not exist). The checker never trusts your print: AC1 compares `TARGETS` to its OWN AST read of `generate()`, and AC2 compares your S3/DS rows to its OWN call to `safe_deploy_core`. **AC6 is the existing suite, which must still pass.** **G9R3-AC7, for `3.0.0_SA_CVO` at L9:** each Lambda-plane row resolves its shared import to every importing function, and each Terraform-plane row names the consuming root.

`<WS>` is your worktree's absolute path, given in your identity line. Every invocation above runs from your worktree root; the checker reads the tree it is run in.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/` and this order's own file. Nothing else. A path you need that is not named is a BLOCKING row on that criterion -- never an override.
- **Branch.** Work in the worktree named in your identity line, on its branch. Never push, merge, rebase, `checkout --` or `clean`.
- **Fixed inputs are read-only**, including `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py`. If you believe a criterion's checker is wrong, file a BLOCKING row naming the arm and the evidence; never work around it and never edit it.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_ENFORCE-W<n>-S<k>` (`<n>` your slot). Keep working after filing. A row's `disarm_owner` is never a worker serial.
- **Judge from the files this order names and cite them** (`path:line @commit`), never the CLAUDE.md or memory text every worker starts with.
- **Numbers in this order are CONTEXT, measured by the issuer at the cut, never acceptance values** -- except where a criterion prints one. Re-measure at your own tree.
- **A value that must be read from the estate is read with the instrument this order names**, and its denominator is printed beside it.
- **Do NOT run `generate`** and do not change any generated file: this cell adds a read-only print. Re-rendering would re-stamp shipping views (R-16).
- **Do not change `VIEWS`, `TARGET_REGISTRY_KEYS` or the mark.** The mark is DEC-5's provenance control (R-16 refused taking it out).

<paths>
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
lib/opal_naming.py
lib/tests/test_opal_naming.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.2, round-3 cell 9 (section 0c; the v3.1 and v3.2 amendments).
<owned_cells>EN-g-9</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `G9R3-AC1`, `G9R3-AC2`, `G9R3-AC3`, `G9R3-AC4`, `G9R3-AC5`, `G9R3-AC6`, `G9R3-AC7`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~5/LGIC_ENFORCE.TO-EN-g-9-r3.target-split.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> G9R3-AC1,G9R3-AC2,G9R3-AC3,G9R3-AC4,G9R3-AC5,G9R3-AC6,G9R3-AC7 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-g-9-r3.target-split.md` BEFORE the `complete` flip.
Result file `target-split.r3.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`G9R3-AC7` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; a PASS or FAIL there is invalid.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-3 cut. This cell is gated by G-C only.
comp-iam: DECLARED-NOT-APPLICABLE -- a read-only print in a library; no principal, policy or resource changes.
comp-adversary: RUN -- the split is the adversarial surface: AC2 re-calls the deploy gate and fails a row that borrows its name, and AC3 plants an unclaimed target.
lane: lib/opal_naming.py and its test are BASE_EXEC; the <paths> block is the grant (R-23).
contention: lib/opal_naming.py is written by this cell alone in round 3; EN-r-5-r3 and EN-w-7-r3 RUN its generate command but do not edit it.
</preflight>

Seating: slot ~5, queue position 1. Round 3 of LGIC_ENFORCE, the recut of `1.0.0_SA_CTO`'s round-2 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_ENFORCE_ROUND2_20260916.md`); issued by `2.0.0_SA_COO~G`. Decomposition v3.2, section 0c. Rulings carried: R-16, R-26, S50, S60.
