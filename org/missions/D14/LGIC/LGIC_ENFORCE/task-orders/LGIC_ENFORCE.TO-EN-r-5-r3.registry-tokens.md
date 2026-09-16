# TO LGIC_ENFORCE.TO-EN-r-5-r3 -- R-6's six unresolved registry tokens: imo retired, find refused, four owners MEASURED

<to_id>LGIC_ENFORCE.TO-EN-r-5-r3</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~2</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-16</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` v1.3 (ADMITTED; both halves current) | **Decomp cell:** `EN-r-5` = round-3 cell 5 (decomposition v3.2, section 0c) | **outcome_ref:** FWD-5 | **depends_on:** none -- level 0; EN-s-6-r3 and EN-w-7-r3 wait on this drain

---

## WORKER FACE

### THE CELL

`EN-r-5` -- RULING R-6 on the six tokens EN-r-2 left in `infra/logic/registry/systems.json` `unresolved` (`org/tier1_exec/1.0.0_SA_CTO/deliverables/SELF_DRIVE_LGIC_RULINGS_20260916.md` R-6). **You edit `infra/logic/registry/systems.json`, and regenerate the two generated files that read it.**

**WHERE THE REFUSED KEYS LIVE.** Refused keys are the `refused_keys` DICT inside `systems.json` (classes `workstream_code`, `generic_noun`, `purpose_word`). **There is no `refused_keys.json` file** -- two records name one; neither is right (row LGIC_ENFORCE-S58).

Per R-6, token by token:
1. **`imo` -- RETIRED** on Andrew's card 9. Add a `refused_keys.retired` class with `imo` as its first member and its basis (the tick-list row and card 9). Write its Rule 24 record in `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/RETIRED_CLASS_RULE24.r3.md`: the axis is "a token Andrew retired by card", disjoint from `workstream_code`, `generic_noun` and `purpose_word`; name the uncovered member you hunted for.
2. **`find` -- REFUSED as a project code** (`refused_keys.workstream_code`; a project code is never a system). Basis: the FIND_* orders and `data/find/`.
3. **`harvest`, `astn`, `news`, `trade` -- the OWNER is MEASURED, never inferred from recall.** For each, read its live resources' DECLARED sources (`infra/aws/lambda/ci/lambda-source-map.json` `source_dir`/`tf_file`; `infra/aws/ec2/EC2_MANIFEST.json` `source_path`; the repo tree the resources deploy from; for `trade`, the tradeops root). Where the tree links to a directive or a mission-tree project, mint a PRODUCT row with `owner_claim: inferred` and the citation as `owner_basis`. Where it links to NONE, the token STAYS `unresolved` with the MEASURED fact written into a NEW `why`, and you write ONE owner card per such token to `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/OWNER_CARDS.r3.md`. A `trade` whose resources deploy from the tradeops root is recorded as that fabric's, not minted here.
4. **Regenerate.** `systems.json` feeds `infra/aws/terraform/modules/opal_name/tests/vectors.json` and `tests/opal_name.tftest.hcl` (`lib/opal_naming.py` `TARGET_REGISTRY_KEYS`). Run `python lib/opal_naming.py generate` and commit those two regenerated files with your registry edit. `lib/opal_naming.py validate` must still read OK.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="R5R3-AC1" cell_refs="EN-r-5"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py r5-imo-retired</invocation><expect>PASS-R5-IMO-RETIRED</expect></criterion>

<criterion id="R5R3-AC2" cell_refs="EN-r-5"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py r5-find-refused</invocation><expect>PASS-R5-FIND-REFUSED</expect></criterion>

<criterion id="R5R3-AC3" cell_refs="EN-r-5"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py r5-product-owners</invocation><expect>PASS-R5-OWNERS-MEASURED</expect></criterion>

<criterion id="R5R3-AC4" cell_refs="EN-r-5"><invocation>cd <WS> && timeout 120 python lib/opal_naming.py validate</invocation><expect>VALIDATE: OK</expect></criterion>

<criterion id="R5R3-AC5" cell_refs="EN-r-5" judgment="true"/>

<expected_criteria>R5R3-AC1, R5R3-AC2, R5R3-AC3, R5R3-AC4, R5R3-AC5</expected_criteria>

**AC1-AC3 read RED at the cut** (all six tokens unresolved; no `retired` class). **AC4 reads OK at the cut and must stay OK.** **R5R3-AC5, for `3.0.0_SA_CVO` at L9:** each `owner_basis` citation resolves to the declared source it names, the retired class's Rule 24 record names the member it hunted for, and every token left unresolved carries a measured `why` and its owner card.

`<WS>` is your worktree's absolute path, given in your identity line. Every invocation above runs from your worktree root; the checker reads the tree it is run in.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/` and this order's own file. Nothing else. A path you need that is not named is a BLOCKING row on that criterion -- never an override.
- **Branch.** Work in the worktree named in your identity line, on its branch. Never push, merge, rebase, `checkout --` or `clean`.
- **Fixed inputs are read-only**, including `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py`. If you believe a criterion's checker is wrong, file a BLOCKING row naming the arm and the evidence; never work around it and never edit it.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_ENFORCE-W<n>-S<k>` (`<n>` your slot). Keep working after filing. A row's `disarm_owner` is never a worker serial.
- **Judge from the files this order names and cite them** (`path:line @commit`), never the CLAUDE.md or memory text every worker starts with.
- **Numbers in this order are CONTEXT, measured by the issuer at the cut, never acceptance values** -- except where a criterion prints one. Re-measure at your own tree.
- **A value that must be read from the estate is read with the instrument this order names**, and its denominator is printed beside it.
- **Nothing live moves.** No AWS write, no Terraform apply, no rename of a live name. Neither regenerated file enters an applied plan (both are test fixtures, R-26).
- **Do not edit `scopes`, `tiers`, `resources` or `exemptions`** -- the first two would re-stamp every shipping generated view (R-16), and `exemptions` is the next cell's.

<paths>
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
infra/logic/registry/systems.json
infra/aws/terraform/modules/opal_name/tests/vectors.json
infra/aws/terraform/modules/opal_name/tests/opal_name.tftest.hcl
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.2, round-3 cell 5 (section 0c; the v3.1 and v3.2 amendments).
<owned_cells>EN-r-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `R5R3-AC1`, `R5R3-AC2`, `R5R3-AC3`, `R5R3-AC4`, `R5R3-AC5`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/LGIC_ENFORCE.TO-EN-r-5-r3.registry-tokens.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> R5R3-AC1,R5R3-AC2,R5R3-AC3,R5R3-AC4,R5R3-AC5 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-r-5-r3.registry-tokens.md` BEFORE the `complete` flip.
Result file `registry-tokens.r3.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`R5R3-AC5` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; a PASS or FAIL there is invalid.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-3 cut. This cell is gated by G-C only.
comp-iam: DECLARED-NOT-APPLICABLE -- a registry data edit and two regenerated test fixtures; no principal, policy or resource changes.
comp-adversary: RUN -- the owner rows are the adversarial surface (an inferred owner without a citation is the guess the registry's owner_claim field exists to refuse); R5R3-AC3 refuses an unchanged cut-time why and AC5 grades each citation.
lane: systems.json is PLATFORM_LOGIC_DOCS and lib generated fixtures are ANY/BASE_EXEC; the <paths> block is the grant (ADHC_OWNPTH.005, R-23).
contention: the two opal_name test fixtures are ALSO regenerated by EN-w-7-r3; both cells are slot ~2's queue, this one first.
</preflight>

Seating: slot ~2, queue position 1. Round 3 of LGIC_ENFORCE, the recut of `1.0.0_SA_CTO`'s round-2 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_ENFORCE_ROUND2_20260916.md`); issued by `2.0.0_SA_COO~G`. Decomposition v3.2, section 0c. Rulings carried: R-6, R-7, R-23, S58.
