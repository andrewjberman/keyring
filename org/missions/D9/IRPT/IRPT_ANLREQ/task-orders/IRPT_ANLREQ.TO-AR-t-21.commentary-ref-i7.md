# TO-AR-t-21 -- the commentary store's `commentary_ref` is I7; the built commentary zip stays importable (AR-t-21 + AR-t-22, round 2)

<to_id>IRPT_ANLREQ.TO-AR-t-21</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~41</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~T</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~T (commentary) | **Decomp cells:** `AR-t-21`, `AR-t-22` (`decompositions/IRPT_ANLREQ_DECOMP_R2.md`
@cff0872f0f) | **outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`AR-t-21` (row W62-S4, interface I7): "The commentary store writes `commentary_ref` as I7 on the acceptance record." I7: `commentary_ref` and
`pdf_ref` are structured `{"artifact_id", "sha256", "version_id"}`; on I5's string fields each travels as its canonical JSON (sorted keys, no
spaces; at most 512 chars, `PACKAGE_REF_MAX_CHARS`). Today `infra/aws/lambda/investor-reporting/reports/commentary_draft_store.py` returns and
stores a three-field ref (:12-13, :124, :178-201) as a DynamoDB map on the request item. Work in your worktree.

**Build:**
1. In `commentary_draft_store.py`, one helper `commentary_ref_i7(ref) -> str` that refuses any ref not EXACTLY those three non-empty string
   fields and returns `json.dumps(ref, sort_keys=True, separators=(",", ":"))`, refusing a result over 512 chars. If `PACKAGE_REF_MAX_CHARS`
   already exists in the estate, import it (cite the line); else define it once here. The put path validates the ref through it before the
   conditional update; the stored map and the returned ref stay the same three fields.
2. `infra/aws/lambda/investor-reporting/reports/tests/test_commentary_ref_i7.py` (new, fakes only): `test_ref_has_exactly_three_fields` (an
   extra or a missing field is refused); `test_canonical_json_under_512` (sorted, no spaces, length <= 512; an oversized value is refused);
   `test_stored_and_returned_ref_are_equal` (the map the conditional update writes equals the ref returned to the caller). Keep
   `reports/tests` and every `test_commentary_*.py` green.

`AR-t-22` (row W41-S1) needs no build: it is proven @00d37e622f and is re-run here as a regression guard on your merged bytes.

### ACCEPTANCE

<criterion id="AR21-t-AC1" cell_refs="AR-t-21"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R2_CHECKS/ar2_t21_checks.py</invocation><expect>AR2-T21-OK</expect></criterion>
`AR21-t-AC1` -- the three named tests pass. Dry-run at box/dell2 5759f1fd77: `AR2-T21-FAIL absent` -- FAIL as expected.

<criterion id="AR22-t-AC1" cell_refs="AR-t-22"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R2_CHECKS/ar2_t22_zip_import.py</invocation><expect>AR2-T22-OK</expect></criterion>
`AR22-t-AC1` -- the built transcripts-pull zip admits a valid analysis_ready and the negative control (keys.py removed) refuses. Reads OK at
the base (the cell was proven @00d37e622f); it must still read OK on your merged bytes.

<expected_criteria>AR21-t-AC1 AR22-t-AC1</expected_criteria>

## BOUNDS

- **Grant.** The paths below, this order's file, your deliverables folder.
- **WORLD by path floor, LOCAL in act.** No AWS call; fakes only. The AR-t-22 check runs `build.sh` locally (writes only `dist/`, gitignored).
- **Refusal clause.** If the ref shape the packager reads (`AR-g-22`, ~G2) differs from I7 at your base, keep I7, file a surprise row
  (`IRPT_ANLREQ-D2-W41-S<k>`, next unused under `surprise-channel/`).

<paths>
infra/aws/lambda/investor-reporting/reports/commentary_draft_store.py
infra/aws/lambda/investor-reporting/reports/tests/test_commentary_ref_i7.py
infra/aws/lambda/investor-reporting/reports/tests/test_commentary_draft_store.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R2.md</decomp_doc> (round 2), cells `AR-t-21`, `AR-t-22`.
<owned_cells>AR-t-21 AR-t-22</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR21-t-AC1, AR22-t-AC1. Instance at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~41/IRPT_ANLREQ.TO-AR-t-21.commentary-ref-i7.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AR21-t-AC1,AR22-t-AC1` BEFORE the flip. Commit code first, then pin.
</proof_of_spec>

**REPORT:** the helper and where the put path calls it, the cap's source, the test names, both check lines, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a validation helper and a regression guard.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no grant change.
comp-adversary: RUN -- 3 sources read (DECOMP_R2 I7 row :24, commentary_draft_store.py :12-13/:124/:178-201, W41_S1_ZIP_IMPORT_PROOF.json @00d37e622f); BLIND to ~G2's packager parse (AR-g-22, in flight). Traps: a fourth field slipping through, non-canonical JSON, a stored map differing from the returned ref; the face fixes each.
lane: commentary workstream ~T: the store module and its tests.
</preflight>

Source: ~Y2 msg 2781; IRPT_ANLREQ_DECOMP_R2.md @cff0872f0f cells AR-t-21, AR-t-22 and interface I7.
