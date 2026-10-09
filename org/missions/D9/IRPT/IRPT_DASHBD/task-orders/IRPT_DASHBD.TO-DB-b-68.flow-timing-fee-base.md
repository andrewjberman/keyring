# TO IRPT_DASHBD.TO-DB-b-68 -- E3: FLOW_TIMING_AFTER_FEE_BASE (116), the next largest UNEXPLAINED class after NEAR_ZERO -- traced per sub-class with counts, each status read under the reader of record

<to_id>IRPT_DASHBD.TO-DB-b-68</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~45</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>34</round>
<workstream>BD</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's round-33 ADDENDUM 2 @47c849d75b (msg 2116, on ADJUDICATION_v18), enrichment item E3 | **Decomp cell:** `DB-b-68` (decomposition section 36) | **outcome_ref:** FWD-8 | **depends_on:** DB-b-63 (merged @96a0c9991a).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-45`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~45/`.

**The cell (`DB-b-68`).** Round 31 classed 116 of the 1,203 UNEXPLAINED misses FLOW_TIMING_AFTER_FEE_BASE: under the corrected fee base, a
START or MID flow convention reached BD where the served END did not. Since then the reader of record adopted flow-START (round 32) and two
reader fixes (round 33, 8,385 of 9,078), so many of the 116 may now tie.

**Population:** the rows of `deliverables/0.9.0_WK_IRPT_DASHBD~36/UNEXPLAINED_CLASSES_E2.json` with
`cause_class == "FLOW_TIMING_AFTER_FEE_BASE"` (116). Take it from the record.

**Sources (read only):**
- the reader of record `org/missions/D9/IRPT/IRPT_DASHBD/tieout/tieout_reader.py`;
- round 33's record `deliverables/0.9.0_WK_IRPT_DASHBD~40/REGRADE_FIXES_E1.json` (each segment's abs_diff_pp under the reader);
- round 32's `deliverables/0.9.0_WK_IRPT_DASHBD~38/REGRADE_FLOWSTART_E2.json`;
- the BD full-period pull `pull=20261004` and the served gold.

1. For each of the 116, read its `abs_diff_pp_now` under the reader of record (from round 33's record), and trace the sub-cause.
   Examples: resolved by flow-start, a MID-day flow, a flow BD books a day apart, several flows in the segment. Give each a `sub_class`
   with `evidence`. Write `counts` and `within_now`.
2. For each sub_class, write `dispositions[sub_class]` {disposition: "fixed" | "named_cause" | "resolved_by_reader", cause, note}. A fix
   lives in a NEW module in your folder and states its effect. It never edits the reader of record.
3. Write `FLOW_TIMING_FEE_E3.json` (`rows` [{account, segment, sub_class, abs_diff_pp_now, evidence}], `counts`, `within_now`,
   `dispositions`, `files_read`) and `FLOW_TIMING_FEE_E3.md` (COUNTS ONLY).

<criterion id="DB34-3-AC1" cell_refs="DB-b-68"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r34/p34_round34.py" . DB34-3-AC1</invocation><expect>DB34-3-AC1 PASS</expect></criterion>
`DB34-3-AC1` -- the 116 each carry a sub_class and the abs_diff under the reader; counts and within_now equal the tallies. Base: FAIL.

<criterion id="DB34-3-AC2" cell_refs="DB-b-68"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r34/p34_round34.py" . DB34-3-AC2</invocation><expect>DB34-3-AC2 PASS</expect></criterion>
`DB34-3-AC2` -- every sub_class is dispositioned fixed, named_cause or resolved_by_reader, with its cause. Base: FAIL.

<expected_criteria>DB34-3-AC1,DB34-3-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~45/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-68.flow-timing-fee-base.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 36 (round 34), cell `DB-b-68`.
<owned_cells>DB-b-68</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB34-3-AC1, DB34-3-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~45/IRPT_DASHBD.TO-DB-b-68.flow-timing-fee-base.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB34-3-AC1,DB34-3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the sub-classes with counts and dispositions, within now under the reader, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: project-owned reconciliation code and records; nothing served, deployed or written to S3.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only, from this box; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB34-3-AC1/AC2 base FAIL at base 5baf94294f (no record); positive control on a planted record PASS (116).
lane: the <paths> block IS the grant.
</preflight>
