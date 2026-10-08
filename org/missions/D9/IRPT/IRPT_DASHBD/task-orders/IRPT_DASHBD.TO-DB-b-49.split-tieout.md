# TO IRPT_DASHBD.TO-DB-b-49 -- FWD-8: tie out Black Diamond's split figures (either side of the 2025-01-09 closure) against Opal's served returns for the 2,299 closure segments; grade branch A or B

<to_id>IRPT_DASHBD.TO-DB-b-49</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~28</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>28</round>
<workstream>BD</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** decomposition section 27 (the tie-out cell, cut when the pull
lands) and 1.0.0_SA_CTO~DELL2's round-19 analysis @b402b7b2e3 section 2 ("(A) the split figures tie within 0.35 pp on most of the 2,299,
which names BD's closure-day booking as the cause; (B) they do not tie, which says the gap is not the closure day at all and the residue
read widens") | **Decomp cell:** `DB-b-49` (decomposition section 30) | **outcome_ref:** FWD-8 | **depends_on:** DB-b-45 (complete
@3efc66cf42; 2,299 of 2,299 landed).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-28`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~28/`.

**The cell (`DB-b-49`).** 2,299 closure segments (one per account, `deliverables/0.9.0_WK_IRPT_DASHBD~14/CLOSURE_ALIGN_E1P.json`) do not
tie between Black Diamond and Opal on the gross basis. Black Diamond has now been asked for each segment as TWO ranges, (start ..
2025-01-08) and (2025-01-10 .. end): the plan is `deliverables/0.9.0_WK_IRPT_DASHBD~25/SPLIT_PULL_PLAN.json` (each request's `account`,
`bd_account`, `ranges`, `landing_key`), and all 2,299 responses are landed under
`s3://opal-data-assets/blackdiamond/49financial/bronze/reporting_performance/pull=split20261007/acct=<bd_internal_id>.json`
(run record `deliverables/2.0.0_SA_COO~D2/relay/SPLIT_PULL_RUN.json`). Round 18 already reads BD responses into a gross return and Opal's
served series into a linked return: `deliverables/0.9.0_WK_IRPT_DASHBD~13/tieout_e2_gross.py` and its record
`TIEOUT_49F_BD_POPULATION_E2_GROSS.json` (`bd_gross_return` per segment). Reuse its readers by import; do not restate them.

1. For each of the 2,299 accounts, read BD's gross return for each of the two ranges from the landed file (one `dateRangePoints` entry
   per requested range; the same gross basis as round 18), and compute Opal's linked return over the SAME two ranges from the served
   gold series (`s3://opal-data-49financial/irpt/49financial/gold/account_return_daily/`, the column round 18 used). Per half: `bd_return`,
   `opal_return`, `abs_diff_pp`, `tied` (abs_diff_pp <= 0.35). A figure that cannot be read is null with a `reason`, never filled.
2. Counts: `tied_both`, `tied_left_only`, `tied_right_only`, `tied_neither`, `absent`, summing to 2,299. Branch: **A** if `tied_both` is
   more than half of 2,299 (the rule is stated in the check before the run), else **B**. Write `branch`.
3. Control `recompose`: chain BD's two halves ((1+left)(1+right)-1) and compare it with BD's own full-segment gross in the round-18
   record; `{compared, within_tolerance}` at 0.35 pp. (It shows the two pulls agree with each other.)
4. Write `TIEOUT_SPLIT_E1.json` (`files_read`, `rows`, `counts`, `branch`, `recompose`, the column used) and `TIEOUT_SPLIT_E1.md`, COUNTS
   ONLY (no account number, name or balance -- the landed files carry names; never print them).

<criterion id="DB28-3-AC1" cell_refs="DB-b-49"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r28/p28_split_tieout.py" . DB28-3-AC1</invocation><expect>DB28-3-AC1 PASS</expect></criterion>
`DB28-3-AC1` -- all 2,299 files read; each half graded at 0.35 pp or named absent; counts close over 2,299. Base: FAIL.

<criterion id="DB28-3-AC2" cell_refs="DB-b-49"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r28/p28_split_tieout.py" . DB28-3-AC2</invocation><expect>DB28-3-AC2 PASS</expect></criterion>
`DB28-3-AC2` -- the branch follows the stated rule; the recompose control is printed. Base: FAIL.

<expected_criteria>DB28-3-AC1,DB28-3-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. The plan, the landed files and round 18's scripts are read, never edited.
- **AWS:** S3 reads only. NO Black Diamond call, no secret read, no S3 write, no bun, no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a filled figure, or an account number, name or balance in a committed
  `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~28/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-49.split-tieout.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 30 (round 28, workstream BD), cell `DB-b-49`.
<owned_cells>DB-b-49</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB28-3-AC1, DB28-3-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~28/IRPT_DASHBD.TO-DB-b-49.split-tieout.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB28-3-AC1,DB28-3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the counts, the branch, the recompose control, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read-only comparison over landed files and the served gold; no S3 write.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only, from this box; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB28-3-AC1 and AC2 base FAIL (no record), dry-run at base 38442c36cc 2026-10-08 ~13:5xZ; the "most" threshold (> 1,149.5 of 2,299 tied on both halves) stated in the check before the run.
lane: the <paths> block IS the grant.
</preflight>
