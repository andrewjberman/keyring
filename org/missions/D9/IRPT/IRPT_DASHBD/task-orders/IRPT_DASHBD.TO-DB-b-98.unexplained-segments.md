# TO IRPT_DASHBD.TO-DB-b-98 -- E1: classify each of the 510 UNEXPLAINED outside segments of the 49F vs Black Diamond tie-out (TIEOUT_COMPOUND_V2, 990 outside) by a named reason from a declared set with its rule-24 record, or file it as a defect row; the per-reason counts sum to 990

<to_id>IRPT_DASHBD.TO-DB-b-98</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~73</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>48</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's ADDENDUM 14 (msg 3416), enrichment item E1 | **Decomp cell:** `DB-b-98` (decomposition section 50) | **outcome_ref:** FWD-8 | **depends_on:** none.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-73`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~73/`.

**The cell (`DB-b-98`).** FWD-8's ACCEPT requires every segment where our return and Black Diamond's disagree to carry a stated reason. The latest
tie-out, `C:/dev/wk-irpt-dashbd-73/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~35/TIEOUT_COMPOUND_V2.json` (TO-DB-b-57, produced by `tieout_compound_v2.py` in the same folder),
graded 9,078 segments: 8,088 WITHIN and 990 OUTSIDE. Its summary `outside_by_reason` gives FLOW_TIMING 449, INCOME_DATE 26, MISSING_PRICE 1,
COVERAGE_DAYS 4, and UNEXPLAINED 510. The per-segment rows carry no reason. The CTO placed this cell (ADDENDUM 14 item 2). The tolerance itself
is Andrew's word (open call 2f53) and does not change this cell.

1. **Re-derive the UNEXPLAINED set.** Re-run `tieout_compound_v2.py`'s reason logic over its existing inputs. Identify the 510 OUTSIDE segments
   (account + segment) that fell to UNEXPLAINED, and confirm the count is 510. If it is not, file a row and stop.
2. **Declare the reason set.** Keep the existing reasons. Add only new reasons that the inputs can prove; candidates include an inception or
   termination partial window, a fee-period misalignment, a corporate action, or a vendor-side restatement.
   - Write its rule-24 record as `REASON_SET_RULE24.md`: (i) MECE over the 990 OUTSIDE segments, the domain printed; (ii) one grain, a segment;
     (iii) one axis, why the two returns differ; (iv) which values each remedy does not move.
   - UNEXPLAINED is not a member.
3. **Classify each of the 510** by a reason whose test you can show on that segment's inputs. A segment that no reason explains is a DEFECT:
   file it as a row in the channel with the id form `IRPT_DASHBD-D2-W73-S<k>`. Several segments may share one row if they share one cause.
4. Record `UNEXPLAINED_CLASSIFIED.json`:
   - `denominator_outside`: 990;
   - `reason_set`;
   - `by_reason`, over all 990 and summing to 990;
   - `classified`: [{account, segment, reason, row (for DEFECT)}], the 510;
   - `rule24_record` (path).

   Use the account keys exactly as V2 writes them; copy no client identifier beyond them.

**Inputs only, no vendor call, no AWS write.** Tests are not required; the record and its check are the proof.

<criterion id="DB48-1-AC1" cell_refs="DB-b-98"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r48/p48_round48.py" . DB48-1-AC1</invocation><expect>DB48-1-AC1 PASS</expect></criterion>
`DB48-1-AC1` -- the 990 outside segments sum over a declared reason set with no UNEXPLAINED, and each of the 510 is reasoned or a filed defect. Base: FAIL.

<expected_criteria>DB48-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's exception:** you read the tie-out inputs in place and write only in your folder and the channel. No vendor call.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~73/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~73/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-98.unexplained-segments.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 50 (round 48), cell `DB-b-98`.
<owned_cells>DB-b-98</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB48-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~73/IRPT_DASHBD.TO-DB-b-98.unexplained-segments.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB48-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the reason set, the per-reason counts, the defects, and any row, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: an offline classification over existing inputs; nothing served moves.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS write; reads only what V2 already read.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB48-1-AC1 FAIL at base (no record). CTO ADDENDUM 14 item 2.
lane: the <paths> block IS the grant.
</preflight>
