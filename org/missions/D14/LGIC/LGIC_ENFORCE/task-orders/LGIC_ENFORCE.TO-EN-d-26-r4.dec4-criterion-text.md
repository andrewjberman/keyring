# TO LGIC_ENFORCE.TO-EN-d-26-r4 -- DEC-4(ii)'s amended criterion text, and the guard that refuses a claim no trail can evidence

<to_id>LGIC_ENFORCE.TO-EN-d-26-r4</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~3</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-17</issued_date>
<status>complete -- 0.9.0_WK_LGIC_ENFORCE~3, e687c2ac08: D26R4-AC1/AC2/AC3 PASS-by-output against the issuer's fixed checker (proof-of-spec-check rc=0); D26R4-AC4 judgment, recorded UNVERIFIABLE-BY-INSTRUMENT for 3.0.0_SA_CVO at L9, no self-graded verdict. Proof: org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~3/LGIC_ENFORCE.TO-EN-d-26-r4.dec4-criterion-text.proof_of_spec.json</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` v1.3 (ADMITTED; both halves current) | **Decomp cell:** `EN-d-26` = round-4 cell 26 (decomposition v3.3, section 0d) | **outcome_ref:** FWD-2 (its evidence rule) | **depends_on:** nothing (level 0)

---

## WORKER FACE

### THE CELL

`EN-d-26` -- RULING R-30 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/SELF_DRIVE_LGIC_RULINGS_20260916.md` R-30), R-32's cell 26, on row `LGIC_ENFORCE-W2-S12`. **You write two files, both your own deliverables:** `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/DEC4_II_AMENDED.r4.md` and `.../fence_disposition_check.py`.

**WHY.** DEC-4(ii) of the PRD names ONE evidence path for deciding that a role is not a principal of a firm bucket: the CloudTrail data events made live on those buckets. Round 3 measured that `opal-data-demo` sits in **neither** data-event selector -- not the organisation trail's read set (`infra/aws/terraform/shared-infra/cloudtrail-organization-trail.tf`) nor the served-key write trail's (`infra/aws/terraform/globgrph/item2e_served_write_trail.tf`) -- while the bucket is live. So on that bucket the prescribed evidence can never answer, and **silence in a trail that never covered the bucket would read exactly like a clean result.** R-30 disarmed the row by RULE rather than by instrumenting the bucket, and bound the rule's text to this round's cut.

**WHAT YOU WRITE.**

1. **THE AMENDED CRITERION TEXT** in `DEC4_II_AMENDED.r4.md`: the replacement wording for DEC-4(ii)'s evidence clause, stating all four of R-30's parts --
   - a `NOT_A_PRINCIPAL` disposition on a bucket that is **not** a member of a live CloudTrail **data-event** selector is **REFUSED**;
   - the disposition then comes from a **direct IAM-grant read** (EXEMPTED, or NOT_A_PRINCIPAL by cited grant absence);
   - or the name is carded **NOT-JUDGED** with the missing-instrument reason;
   - **silence in a trail that never covered the bucket is never evidence.**
   Write it as text the CTO can lift verbatim into the PRD, with a one-line note that the lift is `1.0.0_SA_CTO`'s act. **You do NOT edit `prd/LGIC_ENFORCE_PRD.md`** -- L4 is the CTO's surface and it is not in your grant.
2. **THE GUARD** in `fence_disposition_check.py`: a stdlib-only, ASCII-only script invoked as `python <this file> <claim.json>`, where the claim file is `{"rows": [{"role", "bucket", "disposition", "evidence"}, ...]}` -- the same shape round 3's `FENCE_WRITER_DISPOSITION.r3.json` used. It must:
   - read which buckets a live data-event selector covers **from the two trail declarations named above**, never from a hand-typed list (an enumerated list lapses silently when a trail changes);
   - **exit non-zero** when any row claims `NOT_A_PRINCIPAL` on a bucket those declarations do not cover, printing the bucket and the reason;
   - **exit zero** for a claim on a covered bucket that carries its evidence;
   - print the covered-bucket count as its denominator.
   Give it its own `--self-test` that exercises both directions.
3. **EXERCISE IT BOTH WAYS YOURSELF** before you grade, and record both runs in your result file: a planted `NOT_A_PRINCIPAL` on `opal-data-demo` (must refuse) and one on a covered bucket such as `opal-data-bd` or `opal-data-49financial` (must pass). **A guard that refuses everything would satisfy the refusal half alone -- that is the shape this cell exists to prevent.**

**Read:** R-30 whole; row `LGIC_ENFORCE-W2-S12` in the project's `surprise-channel/investigations/INVESTIGATION_v1.md`; `prd/LGIC_ENFORCE_PRD.md` DEC-4 (its (i), (ii), (iii) -- read it, do not write it); the two trail declarations at the paths above; `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/FENCE_WRITER_DISPOSITION.r3.json` (round 3's claim shape).

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="D26R4-AC1" cell_refs="EN-d-26"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_en_r4.py d26-text</invocation><expect>PASS-D26-TEXT-AMENDED</expect></criterion>

<criterion id="D26R4-AC2" cell_refs="EN-d-26"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_en_r4.py d26-planted-refusal</invocation><expect>PASS-D26-PLANTED-REFUSAL</expect></criterion>

<criterion id="D26R4-AC3" cell_refs="EN-d-26"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~3/fence_disposition_check.py --self-test</invocation><expect>(?m)^SELF-TEST: ([0-9]+) of \1 </expect></criterion>

<criterion id="D26R4-AC4" cell_refs="EN-d-26" judgment="true"/>

<expected_criteria>D26R4-AC1, D26R4-AC2, D26R4-AC3, D26R4-AC4</expected_criteria>

**Measured at the cut, by the issuer, against this tree:** AC1 and AC2 both read FAIL -- neither deliverable exists yet. AC2 is a TWO-WAY arm by construction: it plants a claim on `opal-data-demo` (must be refused) AND one on a bucket it reads out of the trail declarations (must be accepted), and it FAILS a guard that refuses both. AC3 is your own self-test, and its expectation is the `N of N` form so it cannot pass with 0 arms. **D26R4-AC4, for `3.0.0_SA_CVO` at L9 (no verdict from you):** the amended text is lift-ready and says what R-30 ruled without widening it, and the guard reads trail membership from the declarations rather than from a list it carries.

`<WS>` is your worktree's absolute path, given in your identity line. Every invocation above runs from your worktree root; the checker reads the tree it is run in.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/` and this order's own file. Nothing else. A path you need that is not named is a BLOCKING row on that criterion -- never an override.
- **THE PRD IS NOT YOURS.** `prd/LGIC_ENFORCE_PRD.md` is `1.0.0_SA_CTO`'s surface (L4). You write the amended text as a deliverable; the CTO lifts it.
- **Branch.** Work in the worktree named in your identity line, on its branch. Never push, merge, rebase, `checkout --` or `clean`.
- **Fixed inputs are read-only**, everything under `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/`. If you believe a criterion's checker is wrong, file a BLOCKING row naming the arm and the evidence; never work around it and never edit it.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_ENFORCE-W<n>-S<k>` (`<n>` your slot). **Append at the END of the existing JSON array, keeping every existing row's bytes and indentation.** Keep working after filing. A row's `disarm_owner` is never a worker serial.
- **Judge from the files this order names and cite them** (`path:line @commit`), never the CLAUDE.md or memory text every worker starts with.
- **Numbers in this order are CONTEXT, measured by the issuer at the cut, never acceptance values** -- except where a criterion prints one. Re-measure at your own tree.
- **Commit before you grade.** The checker reads the tree it runs in; commit your artifact, then run every criterion, then write the proof instance.
- **Nothing live moves.** Instrumenting `opal-data-demo` is explicitly NOT ordered (R-30(4)): no trail edit, no Terraform apply, no AWS write. Reading IAM or a trail declaration is read-only.

<paths>
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.3, round-4 cell `EN-d-26` (section 0d).
<owned_cells>EN-d-26</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `D26R4-AC1`, `D26R4-AC2`, `D26R4-AC3`, `D26R4-AC4`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~3/LGIC_ENFORCE.TO-EN-d-26-r4.dec4-criterion-text.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> D26R4-AC1,D26R4-AC2,D26R4-AC3,D26R4-AC4 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-d-26-r4.dec4-criterion-text.md` BEFORE the `complete` flip.
Result file `dec4-criterion-text.r4.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`D26R4-AC4` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; a PASS or FAIL there is invalid.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-4 cut. Level 0, gated by nothing.
comp-iam: RUN and APPLICABLE as a READ -- the guard reads trail declarations, and the cell may read IAM grants; it changes no principal, policy or trail. R-30(4) forbids instrumenting the bucket.
comp-adversary: RUN -- DENOMINATOR 2 planted claims per grading run (1 on an uncovered bucket, 1 on a covered bucket read from 2 trail declarations); 1 adversarial shape covered (a guard that REFUSES everything, caught because the covered-bucket claim must be ACCEPTED); BLIND to whether a bucket absent from both declarations is nonetheless covered by a selector declared outside this repo -- that case would read as uncovered here.
lane: the worker's own deliverables folder; the <paths> block adds only the channel. The PRD is deliberately out of grant (L4 is 1.0.0_SA_CTO's).
contention: no other cell in either live project writes this worker's folder.
</preflight>

Seating: slot ~3, queue position 1. Round 4 of LGIC_ENFORCE, the recut of `1.0.0_SA_CTO`'s round-3 analysis @`969f89b0e7`; issued by `2.0.0_SA_COO~G`. Decomposition v3.3, section 0d. Rulings carried: R-30 (all four parts), R-32, R-19 (the row's owner moved to 1.0.0_SA_CTO, so this cell files no clock).
