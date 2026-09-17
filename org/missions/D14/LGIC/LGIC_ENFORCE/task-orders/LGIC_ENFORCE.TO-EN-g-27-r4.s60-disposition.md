# TO LGIC_ENFORCE.TO-EN-g-27-r4 -- S60, the ship classifier's undercount, dispositioned

<to_id>LGIC_ENFORCE.TO-EN-g-27-r4</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~4</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-17</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` v1.3 (ADMITTED; both halves current) | **Decomp cell:** `EN-g-27` = round-4 cell 27 (decomposition v3.3, section 0d) | **outcome_ref:** FWD-3 | **depends_on:** nothing (level 0)

---

## WORKER FACE

### THE CELL

`EN-g-27` -- row `LGIC_ENFORCE-S60`, RULINGS R-16 and R-26, R-32's cell 27. **You write ONE file, your own deliverable:** `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/S60_DISPOSITION.r4.md`.

**WHY.** R-16 ruled that the SHIP / REPO-ONLY split of the generator's targets is derived by CALLING the deploy gate's own classifier, `.tools/safe_deploy_core.py`, over the target list. S60 measured the hole in that: `safe_deploy_core` decides the **S3/DS plane only** -- called over the generator's 10 targets it returns a determination for 3 and `None` for 7, so a single-classifier split would print at least 5 SHIPPING targets as REPO-ONLY. The CVO graduated S60 as a standing finding in round 3, and R-32 gives it this cell: **it gets a disposition, either FIXED with its measurement or CARDED with an owner and a reason.**

**WHAT TO DO, in order.**

1. **MEASURE the live behaviour.** Run `python lib/opal_naming.py targets` and read every row. Round 3's EN-g-9 built that subcommand under R-26, which ruled the split PER PLANE: each row prints `SHIP` / `REPO-ONLY` / `UNCLASSIFIED`, its plane, its path, and `measured:` naming **the instrument of that row's own plane** -- `safe_deploy_core` for S3/DS, `lambda-source-map.json` for the Lambda plane (a shared import resolved to every importing function), the consuming Terraform root for the Terraform plane.
2. **DECIDE the disposition from what you measured, not from the row's text.** If every target carries a plane-specific `measured:` instrument and nothing reads `UNCLASSIFIED`, then S60's undercount is **FIXED** by R-26's per-plane split, and your record says so **with the numbers**: the target count, the per-plane counts, the distinct instruments called, and the hash-pinned-consumer census line. If any target is UNCLASSIFIED, or any plane is still decided by another plane's instrument, then S60 is **CARDED**: name the owner (the classifier is R-16's mechanism, so its owner is `1.0.0_SA_CTO`) and the reason, and say exactly which targets are wrong.
3. **STATE THE ONE THING A PASSING READ DOES NOT PROVE.** `targets` is a read-only print; it does not deploy. So a correct split is evidence about the CLASSIFIER, not about any deployment that already happened under the old single-classifier reading. Say that plainly in the record, and name the earlier act S60's own text cites (a comment-only re-render that re-minted a production bundle) as out of this cell's scope.
4. **Do not change the classifier or the generator.** `lib/opal_naming.py`, `.tools/safe_deploy_core.py` and every registry file are outside your grant. If your measurement shows a fix is needed, that is a BLOCKING row naming the defect and its coordinate -- the fix is a cell someone cuts, not an edit here.

**Read:** row `LGIC_ENFORCE-S60` in the project's `surprise-channel/investigations/INVESTIGATION_v1.md` (whole, including its `notes`); R-16 and R-26 in `org/tier1_exec/1.0.0_SA_CTO/deliverables/SELF_DRIVE_LGIC_RULINGS_20260916.md`; `lib/opal_naming.py`'s `targets` / `targets_report` and its plane helpers; `.tools/safe_deploy_core.py` (`file_to_s3_target`, `bundle_for_member`); `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~5/target-split.r3.result.md` (round 3's own account of building it).

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="G27R4-AC1" cell_refs="EN-g-27"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_en_r4.py g27-plane-instruments</invocation><expect>PASS-G27-PLANE-INSTRUMENTS</expect></criterion>

<criterion id="G27R4-AC2" cell_refs="EN-g-27"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_en_r4.py g27-disposition</invocation><expect>PASS-G27-DISPOSITION</expect></criterion>

<criterion id="G27R4-AC3" cell_refs="EN-g-27" judgment="true"/>

<expected_criteria>G27R4-AC1, G27R4-AC2, G27R4-AC3</expected_criteria>

**Measured at the cut, by the issuer, against this tree:** AC1 reads **PASS** already -- `TARGETS: 10`, 10 classified rows, **5 distinct measuring instruments**, 0 UNCLASSIFIED -- and it must STILL pass at your close; it is the regression read on R-26's per-plane split, and it FAILS if one instrument ever decides every plane again (that is S60's shape), if any row loses its `measured:` line, or if the printed TARGETS count stops matching the rows. AC2 reads `FAIL-G27-DISPOSITION` -- the record does not exist yet. **G27R4-AC3, for `3.0.0_SA_CVO` at L9 (no verdict from you):** the disposition follows from the numbers in the record rather than from the row's prose, and the record states what a passing read does not prove.

`<WS>` is your worktree's absolute path, given in your identity line. Every invocation above runs from your worktree root; the checker reads the tree it is run in.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/` and this order's own file. Nothing else. A path you need that is not named is a BLOCKING row on that criterion -- never an override.
- **NO CODE CHANGE.** `lib/opal_naming.py`, `.tools/safe_deploy_core.py` and every file under `infra/logic/registry/` are outside your grant this round.
- **Branch.** Work in the worktree named in your identity line, on its branch. Never push, merge, rebase, `checkout --` or `clean`.
- **Fixed inputs are read-only**, everything under `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/`. If you believe a criterion's checker is wrong, file a BLOCKING row naming the arm and the evidence; never work around it and never edit it.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_ENFORCE-W<n>-S<k>` (`<n>` your slot). **Append at the END of the existing JSON array, keeping every existing row's bytes and indentation.** Keep working after filing. A row's `disarm_owner` is never a worker serial.
- **Judge from the files this order names and cite them** (`path:line @commit`), never the CLAUDE.md or memory text every worker starts with.
- **Numbers in this order are CONTEXT, measured by the issuer at the cut, never acceptance values** -- except where a criterion prints one. Re-measure at your own tree.
- **Commit before you grade.** The checker reads the tree it runs in; commit your artifact, then run every criterion, then write the proof instance.
- **Nothing live moves.** `targets` is a read-only print; do NOT run `generate`, which would re-stamp shipping views (R-16).

<paths>
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.3, round-4 cell `EN-g-27` (section 0d).
<owned_cells>EN-g-27</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `G27R4-AC1`, `G27R4-AC2`, `G27R4-AC3`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~4/LGIC_ENFORCE.TO-EN-g-27-r4.s60-disposition.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> G27R4-AC1,G27R4-AC2,G27R4-AC3 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-g-27-r4.s60-disposition.md` BEFORE the `complete` flip.
Result file `s60-disposition.r4.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`G27R4-AC3` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; a PASS or FAIL there is invalid.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-4 cut. Level 0, gated by nothing.
comp-iam: DECLARED-NOT-APPLICABLE -- a read-only print and one record; no principal, policy or resource changes.
comp-adversary: RUN -- DENOMINATOR 10 targets over 4 planes, 5 distinct measuring instruments at the cut; adversarial shapes covered 4 of 4 (one classifier deciding every plane -- S60's own shape -- refused; an UNCLASSIFIED row refused; a printed TARGETS count that does not match the rows refused; a record asserting FIXED with neither measurement nor card shape refused). BLIND to whether an earlier deploy already ran under the old single-classifier reading: this arm reads the classifier, never deployment history, and the record must say so.
lane: the worker's own deliverables folder; the <paths> block adds only the channel. No code surface is granted.
contention: no other cell in either live project writes this worker's folder. This worker's serial also carries round 3's EN-s-6 deliverables, which are read-only history here.
</preflight>

Seating: slot ~4, queue position 1. Round 4 of LGIC_ENFORCE, the recut of `1.0.0_SA_CTO`'s round-3 analysis @`969f89b0e7`; issued by `2.0.0_SA_COO~G`. Decomposition v3.3, section 0d. Rulings carried: R-16, R-26, R-32; row S60 (graduated in round 3, dispositioned here).
