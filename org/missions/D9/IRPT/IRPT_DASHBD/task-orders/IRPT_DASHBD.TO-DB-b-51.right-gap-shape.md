# TO IRPT_DASHBD.TO-DB-b-51 -- E2: the shape of the right-half gap (after 2025-01-10) for the 1,528 misses outside S34, from Opal's side only; the top Opal-side driver, with a left-half control

<to_id>IRPT_DASHBD.TO-DB-b-51</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~30</issued_to>
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
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_28_20261008.md` section 2, item E2) | **Decomp cell:**
`DB-b-51` (decomposition section 31) | **outcome_ref:** FWD-8 | **depends_on:** DB-b-49 (complete, merged @a556d87e79). Not on DB-b-50:
the population is fixed by DB-b-49's per-row `recompose.within` flag.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-30`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~30/`.

**The cell (`DB-b-51`).** Round 28's split tie-out (`deliverables/0.9.0_WK_IRPT_DASHBD~28/TIEOUT_SPLIT_E1.json`) compared Black
Diamond's gross return with Opal's served linked return for 2,299 accounts over two ranges each. Each row carries `left` and `right`
{range {start, end}, bd_return, opal_return, abs_diff_pp, tied} and `recompose` {within}. The left half (to 2025-01-08) ties on 2,220;
the right half (from 2025-01-10) ties on only 465. Opal and BD diverge after the closure. This cell describes that divergence from
Opal's side. Returns are fractions; pp = fraction x 100.

**Populations (take them from the record exactly; do not re-derive):**
- E2 set: rows with `right.tied == false` AND `recompose.within == true` (1,528).
- control set: rows with `left.tied == true` (2,220).
- signed gap (pp) = `(right.opal_return - right.bd_return) * 100`.

**Opal's components:** the served gold `s3://opal-data-49financial/irpt/49financial/gold/account_return_daily/date=<YYYY-MM-DD>/data.parquet`,
one partition per business date. Columns: account_id, business_date, market_value_eod, external_flow, income_received, income_return,
total_return_daily, fee_amount, day_quality, carried_days. Round 18's reader of this series is in
`deliverables/0.9.0_WK_IRPT_DASHBD~13/tieout_e2_gross.py` (import it; do not restate it).

1. Over the E2 set: the signed gap's `median`, `p10`, `p90` (linear-interpolated percentiles), and `length_scaling`
   {corr_with_right_days}, the Pearson correlation of the signed gap with the right half's length in days.
2. For each account in the E2 set, sum over its right-half range: `external_flow`, `income_received` and `fee_amount`, each divided by
   the range's first-day `market_value_eod`; `market_value_eod` (mean); the count of days whose `day_quality` is not clean; and
   `carried_days` (sum). Record `drivers`: one {component, corr} per component, where corr is the Pearson correlation of that
   per-account statistic with the signed gap. `top_driver` is the component with the largest |corr|. State the statistic's definition
   in the record.
3. Control: compute the same statistic for `top_driver` over the control set's LEFT-half ranges, correlated with the left half's signed
   gap. Write `control` {population_count, corr, signature_absent}, where `signature_absent` = |control corr| < |top corr| / 2 (the rule
   is stated in the check before the run; the verdict is printed, not graded).
4. Write `RIGHT_GAP_E2.json` (`population` [accounts], `gap_pp`, `length_scaling`, `drivers`, `top_driver`, `statistic`, `control`,
   `files_read`) and `RIGHT_GAP_E2.md`, COUNTS AND STATISTICS ONLY (no account number, name or balance).

<criterion id="DB29-2-AC1" cell_refs="DB-b-51"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r29/p29_round29.py" . DB29-2-AC1</invocation><expect>DB29-2-AC1 PASS</expect></criterion>
`DB29-2-AC1` -- the population is exactly the E2 set; the gap's median, p10 and p90 equal the check's recomputation; the length correlation is printed. Base: FAIL.

<criterion id="DB29-2-AC2" cell_refs="DB-b-51"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r29/p29_round29.py" . DB29-2-AC2</invocation><expect>DB29-2-AC2 PASS</expect></criterion>
`DB29-2-AC2` -- at least three Opal components carry a numeric correlation; `top_driver` is the one with the largest absolute correlation. Base: FAIL.

<criterion id="DB29-2-AC3" cell_refs="DB-b-51"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r29/p29_round29.py" . DB29-2-AC3</invocation><expect>DB29-2-AC3 PASS</expect></criterion>
`DB29-2-AC3` -- the control runs over exactly the 2,220 left-half ties with the top driver's statistic; `signature_absent` follows the stated rule. Base: FAIL.

<expected_criteria>DB29-2-AC1,DB29-2-AC2,DB29-2-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Round 18's and round 28's scripts and records are read, never edited.
- **AWS:** S3 reads only. NO Black Diamond call, no secret read, no S3 write, no bun, no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a filled figure, or an account number, name or balance in a committed
  `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~30/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-51.right-gap-shape.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 31 (round 29), cell `DB-b-51`.
<owned_cells>DB-b-51</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB29-2-AC1, DB29-2-AC2, DB29-2-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~30/IRPT_DASHBD.TO-DB-b-51.right-gap-shape.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB29-2-AC1,DB29-2-AC2,DB29-2-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the gap distribution, the drivers and top driver, the control, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read-only analysis over the landed record and the served gold; no S3 write.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only, from this box; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB29-2-AC1..AC3 base FAIL (no record) at base 62a01a0c61; positive control on a planted record PASS (1,528 population; gap pp median 0.567, p10 0.374, p90 0.764; control 2,220).
lane: the <paths> block IS the grant.
</preflight>
