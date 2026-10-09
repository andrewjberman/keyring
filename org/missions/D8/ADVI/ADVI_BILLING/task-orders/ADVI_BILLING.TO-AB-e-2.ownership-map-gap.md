# TO ADVI_BILLING.TO-AB-e-2 -- E1 gap: the 5 49 Financial advisorKeys missing from the ownership map, fixed at its producer, the regenerated diff printed and not written

<to_id>ADVI_BILLING.TO-AB-e-2</to_id>
<project>ADVI_BILLING</project>
<issued_to>0.9.0_WK_ADVI_BILLING~4</issued_to>
<issued_by>2.0.0_SA_COO~B2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>

**Directive:** D8 | **Fabric:** dell2 | **PRD:** v0.2 @d45dc8a52f | **Decomp cell:** `AB-e-2` (decomposition section 3, round 2) | **outcome_ref:** FWD-1 (E1 gap) | **depends_on:** none.

---

## WORKER FACE

Your worktree is `C:/dev/wk-advi-billing-4`; run everything from its root. Your folder is
`org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.9.0_WK_ADVI_BILLING~4/`.

**The cell.** The portal's CloudFront edge (`infra/aws/lambda-edge/auth-validator-edge/index.mjs:466-539`) admits an advisor to a
household's `/books/relationship/{id}/*` data only if the id is in `s3://opal-data-bd/platinum/49financial/ownership_map.json` under the
JWT's `advisorId`. 5 of the 11 `advisorKey`s in DynamoDB table `opal-partner-49financial` (rows keyed by email; fields `advisorKey`,
`advisorRole`, `firmRole`) are absent from the map's `advisors` keys, so those advisors are refused their own books. The map is produced by
`data/assets/scripts/gold/runners_49f/d08_firm_ownership_map.py` (pin file `data/assets/scripts/gold/runners_49f/pins/pin_d08_ownership_map.json`).

1. Read the live map and the table (DynamoDB `scan` of `opal-partner-49financial`, read-only; print only advisorKeys, never emails or
   names) and name the 5 missing advisorKeys.
2. Find in the producer why they are absent (the source of its advisor universe, a key-format mismatch, a filter) and fix it there. Never
   hand-edit the map.
3. Test it: `data/assets/scripts/gold/runners_49f/tests/test_d08_ownership_gap.py`, with a test whose name contains `missing`, proving the
   5 keys now appear and no other advisor's relationship list changes (fixture-driven; no S3 write).
4. Run the fixed producer in a DRY mode that writes nothing to S3 (add the flag if it lacks one) and record `OWNERSHIP_GAP_R2.json` in
   your folder: `missing_before` (the 5 advisorKeys), `present_after_fix` (keys now present), `relationships_per_added_advisor` (counts),
   `other_advisors_changed` (count of pre-existing advisors whose list changed -- must be 0), `written` false, and the cause in one line.
   The served regeneration is the issuer's act under a never-widen pair naming these 5 advisorIds.

<criterion id="AB2-2-AC1" cell_refs="AB-e-2"><invocation>python org/missions/D8/ADVI/ADVI_BILLING/deliverables/2.0.0_SA_COO~B2/checks/r2/r2_checks.py . AB2-2-AC1</invocation><expect>AB2-2-AC1 PASS</expect></criterion>
`AB2-2-AC1` -- the producer test passes, one test named *missing*. Base: FAIL.

<criterion id="AB2-2-AC2" cell_refs="AB-e-2"><invocation>python org/missions/D8/ADVI/ADVI_BILLING/deliverables/2.0.0_SA_COO~B2/checks/r2/r2_checks.py . AB2-2-AC2</invocation><expect>AB2-2-AC2 PASS</expect></criterion>
`AB2-2-AC2` -- the record names the 5 advisorKeys, all present after the fix, 0 other advisors changed, nothing written. Base: FAIL.

<expected_criteria>AB2-2-AC1,AB2-2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- DynamoDB and S3 READS only. NO write to the ownership map or any S3 key, no deploy, no edit of the edge or any Lambda.
- **Refusal clause.** An edit outside the grant, a write the face does not name, a vendor call, a secret read, or an account
  number, name or dollar figure in a committed file is a defect: stop and file a row.

<paths>
data/assets/scripts/gold/runners_49f/d08_firm_ownership_map.py
data/assets/scripts/gold/runners_49f/tests/test_d08_ownership_gap.py
org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.9.0_WK_ADVI_BILLING~4/
org/missions/D8/ADVI/ADVI_BILLING/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D8/ADVI/ADVI_BILLING/task-orders/ADVI_BILLING.TO-AB-e-2.ownership-map-gap.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_BILLING/decompositions/ADVI_BILLING_DECOMP.md</decomp_doc> section 3 (round 2), cell `AB-e-2`.
<owned_cells>AB-e-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AB2-2-AC1, AB2-2-AC2. The instance goes at
`org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.9.0_WK_ADVI_BILLING~4/ADVI_BILLING.TO-AB-e-2.ownership-map-gap.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> AB2-2-AC1,AB2-2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, what the cell measured (counts, classes, masked ids only), and every row id.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the cell writes no served key; the regeneration is the issuer's act under a pair.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no role is created or changed in this cell.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: enrichment cell; no served claim is graded here.
checks dry-run at base: AB2-2-AC1, AB2-2-AC2 FAIL as expected.
lane: the <paths> block IS the grant.
</preflight>
