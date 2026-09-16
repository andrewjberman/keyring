# TO LGIC_ENFORCE.TO-EN-p-4-r3 -- the 18 ownerless records into their first minting author's folders, the live readers re-pointed, the readers census pinned

<to_id>LGIC_ENFORCE.TO-EN-p-4-r3</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~6</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-16</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` v1.3 (ADMITTED; both halves current) | **Decomp cell:** `EN-p-4` = round-3 cell 4 (decomposition v3.2, section 0c) | **outcome_ref:** FWD-1 | **depends_on:** EN-s-6-r3, EN-w-7-r3 and EN-t-8-r3 (spawns after all three drain: it moves records they read)

---

## WORKER FACE

### THE CELL

`EN-p-4` -- RULINGS R-2 and R-12 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/SELF_DRIVE_LGIC_RULINGS_20260916.md`), ruled a WORKER cell by R-23. 18 files sit DIRECTLY under `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/` with no serial folder, so lane TREE_DELIVERABLES admits nobody to them; this order's `<paths>` admits you on both sides of each move.

1. **Move all 18** with `git mv` to the destination `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/PLACEMENT_MAP.json` names for each -- its FIRST minting author's folder, measured by `git log --diff-filter=A` before the move. The map is fixed; do not recompute it.
2. **Re-point the LIVE READERS** -- code that opens or assigns an old path. Measured at the cut: 4 string literals in 3 files, all in your `<paths>`: `0.9.0_WK_LGIC_ENFORCE~3/instrument/census.py` and `controls/t2_coverage.py` (`TF_LABEL_CENSUS.md`), and `2.0.0_SA_COO~G/tools/issuance_rulings.py` (`FIRM_FORMS_READERS.md`, `LIMB_ROOTS_CENSUS.md`). **Do NOT rewrite records that cite an old path** -- task orders, proof instances, surprise rows, ledger entries and logs are history pinned at their vintage, and most may not be edited by anyone.
3. **Re-derive the FIRM_FORMS_READERS census, PINNED.** The "held 62-entry edit" no longer exists (it was reverted and its script is gone), and `git grep -l firm_forms` moves as records are written (82 files at the cut's HEAD, 81 one commit earlier). In the relocated `FIRM_FORMS_READERS.md` (destination `0.9.0_WK_LGIC_ENFORCE~1/`), add ONE fenced json: `{"vintage": "<a commit>", "exclusions": [...], "files": [{"path": ..., "class": ...}]}` -- every tracked file naming `firm_forms` AT THAT VINTAGE, minus stated exclusions (an exact path, a `dir/` prefix, or a trailing `**`), each with a class (`reader` for code that reads the key, `record` for prose, `another-project` for a record of another project). **S21's disarm:** LGIC_NAMING's two records that quote the token are listed as `another-project`.
4. **S35's count** is 18, not the 17 it records (all 18 predate its own timestamp); state that in your result record.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="P4R3-AC1" cell_refs="EN-p-4"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py p4-population</invocation><expect>PASS-P4-POPULATION-EMPTY</expect></criterion>

<criterion id="P4R3-AC2" cell_refs="EN-p-4"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py p4-destinations</invocation><expect>PASS-P4-DESTINATIONS-ALL-PLACED</expect></criterion>

<criterion id="P4R3-AC3" cell_refs="EN-p-4"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py p4-citations</invocation><expect>PASS-P4-LIVE-READERS-REPOINTED</expect></criterion>

<criterion id="P4R3-AC4" cell_refs="EN-p-4"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py p4-readers-census org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/FIRM_FORMS_READERS.md</invocation><expect>PASS-P4-READERS-CENSUS-EQUALS-VINTAGE</expect></criterion>

<criterion id="P4R3-AC5" cell_refs="EN-p-4" judgment="true"/>

<expected_criteria>P4R3-AC1, P4R3-AC2, P4R3-AC3, P4R3-AC4, P4R3-AC5</expected_criteria>

**All four arms read RED at the cut** (18 flat; 0 placed; 4 live-reader literals; the doc is flat and unpinned). AC1 reads git's object TYPES, so the 9 serial folders never count as files. AC3 reads every tracked `.py` through the AST, docstrings excluded, so a file that only DESCRIBES where a record used to live is not a reader. AC4 recomputes `git grep -l firm_forms <your vintage>` itself; a record written after your vintage does not move it. **P4R3-AC5, for `3.0.0_SA_CVO` at L9:** each row's class is right, and S21's two LGIC_NAMING records read `another-project`.

`<WS>` is your worktree's absolute path, given in your identity line. Every invocation above runs from your worktree root; the checker reads the tree it is run in.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/` and this order's own file. Nothing else. A path you need that is not named is a BLOCKING row on that criterion -- never an override.
- **Branch.** Work in the worktree named in your identity line, on its branch. Never push, merge, rebase, `checkout --` or `clean`.
- **Fixed inputs are read-only**, including `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py`. If you believe a criterion's checker is wrong, file a BLOCKING row naming the arm and the evidence; never work around it and never edit it.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_ENFORCE-W<n>-S<k>` (`<n>` your slot). Keep working after filing. A row's `disarm_owner` is never a worker serial.
- **Judge from the files this order names and cite them** (`path:line @commit`), never the CLAUDE.md or memory text every worker starts with.
- **Numbers in this order are CONTEXT, measured by the issuer at the cut, never acceptance values** -- except where a criterion prints one. Re-measure at your own tree.
- **A value that must be read from the estate is read with the instrument this order names**, and its denominator is printed beside it.
- **Nothing live moves.** Moves and edits in the repository only.
- **Move with `git mv`, one commit per logical step is fine; never copy-then-delete by hand.**
- **Do not touch any file that is not in `<paths>`** -- including records citing an old path.

<paths>
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/CARRIER_CENSUS.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/CARRIER_CENSUS.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/EXERCISE_FWD1_SEARCH.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~8/EXERCISE_FWD1_SEARCH.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/EXERCISE_FWD2.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/EXERCISE_FWD2.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/EXERCISE_FWD2_R2.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~4/EXERCISE_FWD2_R2.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/EXERCISE_FWD6.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/EXERCISE_FWD6.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/EXERCISE_FWD7.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~8/EXERCISE_FWD7.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/EXERCISE_FWD7_R2.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~5/EXERCISE_FWD7_R2.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/FENCE_PLAN.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/FENCE_PLAN.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/FENCE_PRIOR_POLICY.json
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/FENCE_PRIOR_POLICY.json
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/FENCE_PROBES.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/FENCE_PROBES.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/FENCE_WRITER_CENSUS.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/FENCE_WRITER_CENSUS.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/FIRM_FORMS_READERS.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/FIRM_FORMS_READERS.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/LIMB_ROOTS_CENSUS.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~3/LIMB_ROOTS_CENSUS.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/NAMING_CENSUS_COMPARISON.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~7/NAMING_CENSUS_COMPARISON.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/NAMING_CENSUS_REPORT.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~7/NAMING_CENSUS_REPORT.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/REGISTRY_TOKEN_CLASSES.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/REGISTRY_TOKEN_CLASSES.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/RESOURCE_ROWS.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/RESOURCE_ROWS.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/TF_LABEL_CENSUS.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~3/TF_LABEL_CENSUS.md
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~3/instrument/census.py
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~3/controls/t2_coverage.py
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/tools/issuance_rulings.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.2, round-3 cell 4 (section 0c; the v3.1 and v3.2 amendments).
<owned_cells>EN-p-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `P4R3-AC1`, `P4R3-AC2`, `P4R3-AC3`, `P4R3-AC4`, `P4R3-AC5`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~6/LGIC_ENFORCE.TO-EN-p-4-r3.placement.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> P4R3-AC1,P4R3-AC2,P4R3-AC3,P4R3-AC4,P4R3-AC5 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-p-4-r3.placement.md` BEFORE the `complete` flip.
Result file `placement.r3.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`P4R3-AC5` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; a PASS or FAIL there is invalid.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-3 cut. This cell is gated by G-C and by the drains of EN-s-6-r3, EN-w-7-r3 and EN-t-8-r3.
comp-iam: DECLARED-NOT-APPLICABLE -- repository moves and three code edits; no principal, policy or resource changes.
comp-adversary: RUN -- the re-derived census is the adversarial surface: AC4 recomputes the population at the worker's own vintage rather than reading the doc's claim.
lane: the 18 sources have no owner under TREE_DELIVERABLES; each source and destination is named exactly in <paths>, which admits the worker on both sides (R-23 clause 5).
contention: this cell runs LAST on its component because it moves records EN-s-6-r3, EN-w-7-r3 and EN-t-8-r3 read at their flat paths.
</preflight>

Seating: slot ~6, queue position 1. Round 3 of LGIC_ENFORCE, the recut of `1.0.0_SA_CTO`'s round-2 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_ENFORCE_ROUND2_20260916.md`); issued by `2.0.0_SA_COO~G`. Decomposition v3.2, section 0c. Rulings carried: R-2, R-12, R-23 clause 5, R-27, S21, S22, S35.
