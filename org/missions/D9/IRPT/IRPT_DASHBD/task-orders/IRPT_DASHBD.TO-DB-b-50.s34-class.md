# TO IRPT_DASHBD.TO-DB-b-50 -- E1: class S34's 440 accounts whose Black Diamond split halves do not recompose to BD's own full segment; trace the 724.16 pp outlier; print the overlap with the right-half misses

<to_id>IRPT_DASHBD.TO-DB-b-50</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~29</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>29</round>
<workstream>BD</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's round-28 analysis @e9b17e6e75
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_28_20261008.md` section 2, item E1) | **Decomp cell:**
`DB-b-50` (decomposition section 31) | **outcome_ref:** FWD-8 | **depends_on:** DB-b-49 (complete, merged @a556d87e79).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-29`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~29/`.

**The cell (`DB-b-50`).** Round 28's split tie-out (`deliverables/0.9.0_WK_IRPT_DASHBD~28/TIEOUT_SPLIT_E1.json`, script
`tieout_split_e1.py` beside it) read Black Diamond's gross return for each of 2,299 accounts as two ranges, (segment start ..
2025-01-08) and (2025-01-10 .. segment end). Each row carries `left`, `right` {bd_return, opal_return, abs_diff_pp, tied, bd_net_return,
bd_fee_addback} and `recompose` {chained, bd_full_gross, abs_diff_pp, within}. On **440** rows `recompose.within` is false: BD's two
halves chained, (1+left)(1+right)-1, do not reproduce BD's own full-segment gross from the earlier pull within 0.35 pp (largest gap
724.16 pp). Until those 440 are classed, a right-half miss on them is not an Opal-versus-BD finding.
Sources, all landed (read only):
- the split pull `s3://opal-data-assets/blackdiamond/49financial/bronze/reporting_performance/pull=split20261007/acct=<bd_internal_id>.json`
  (plan with each account's `bd_account`, `ranges`, `landing_key`: `deliverables/0.9.0_WK_IRPT_DASHBD~25/SPLIT_PULL_PLAN.json`);
- the earlier full-period pull `s3://opal-data-assets/blackdiamond/49financial/bronze/reporting_performance/pull=20261004/`, read
  through round 18's readers in `deliverables/0.9.0_WK_IRPT_DASHBD~13/tieout_e2_gross.py` (import them; do not restate them); its
  record `TIEOUT_49F_BD_POPULATION_E2_GROSS.json` carries per segment `bd_return`, `bd_fees_reported`, `bd_fee_addback`,
  `bd_gross_return`, `bd_days_held`, `opal_days`.

1. Take the 440 as exactly the rows of `TIEOUT_SPLIT_E1.json` with `recompose.within == false` (do not re-derive the set). Give each ONE
   `cause_class` from: `opened_or_closed_in_segment` (BD's inception or termination falls inside the segment, so a half covers fewer
   days than requested); `fee_or_basis_between_pulls` (the two pulls disagree on fees or the net/gross basis enough to explain the gap);
   `missing_or_zero_half` (a half is absent, zero, or covers no days); `full_period_annualized` (the full-period figure is annualized
   while the halves are cumulative, or the reverse); or `other:<the cause, named>`. State in each row the evidence that decided it. Write
   `counts` per class; they must sum to 440.
2. Trace the account with the largest `recompose.abs_diff_pp`: its `bd_left`, `bd_right`, `bd_full`, `chained` and `abs_diff_pp`, and
   what the landed files say about it (ranges returned, days, fees).
3. Print `overlap`: `right_misses` (rows with `right.tied` false), `in_s34` (of those, how many are in the 440), `outside_s34`.
4. Write `S34_CLASS_E1.json` (`rows` [{account, cause_class, evidence}], `counts`, `outlier`, `overlap`, `files_read`) and
   `S34_CLASS_E1.md`, COUNTS AND PERCENTAGES ONLY -- no account number, name or balance (the landed files carry names; never print them).

<criterion id="DB29-1-AC1" cell_refs="DB-b-50"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r29/p29_round29.py" . DB29-1-AC1</invocation><expect>DB29-1-AC1 PASS</expect></criterion>
`DB29-1-AC1` -- the 440 each carry one class from the closed set or a named `other:`; counts equal the tally and sum to 440. Base: FAIL.

<criterion id="DB29-1-AC2" cell_refs="DB-b-50"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r29/p29_round29.py" . DB29-1-AC2</invocation><expect>DB29-1-AC2 PASS</expect></criterion>
`DB29-1-AC2` -- the 724.16 pp account traced with its three BD figures and the chained value. Base: FAIL.

<criterion id="DB29-1-AC3" cell_refs="DB-b-50"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r29/p29_round29.py" . DB29-1-AC3</invocation><expect>DB29-1-AC3 PASS</expect></criterion>
`DB29-1-AC3` -- the overlap {right_misses, in_s34, outside_s34} equals the counts from DB-b-49's record. Base: FAIL.

<expected_criteria>DB29-1-AC1,DB29-1-AC2,DB29-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. The plan, the landed files, round 18's and round 28's scripts and records are read, never edited.
- **AWS:** S3 reads only. NO Black Diamond call, no secret read, no S3 write, no bun, no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a filled figure, or an account number, name or balance in a committed
  `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~29/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-50.s34-class.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 31 (round 29), cell `DB-b-50`.
<owned_cells>DB-b-50</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB29-1-AC1, DB29-1-AC2, DB29-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~29/IRPT_DASHBD.TO-DB-b-50.s34-class.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB29-1-AC1,DB29-1-AC2,DB29-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the class counts, the outlier trace, the overlap, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read-only classification over landed files; no S3 write.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only, from this box; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB29-1-AC1, AC2 and AC3 base FAIL (no record) at base 62a01a0c61; positive control on planted records PASS (440 of 440, overlap 1,834 / 306 / 1,528).
lane: the <paths> block IS the grant.
</preflight>
