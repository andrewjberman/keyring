# TO IRPT_DASHBD.TO-DB-b-27 -- E1: re-grade the E2 tie-out on ONE gross basis, Black Diamond's own reported fee added back per segment (FWD-8, W12-S1 ruled; zero vendor calls)

<to_id>IRPT_DASHBD.TO-DB-b-27</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~13</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 round-15..17 analysis item E1
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUNDS_15_17_20261007.md` @e363a194ed, section 2 ruling on
W12-S1 and section 5 row E1) | **Decomp cell:** `DB-b-27` (decomposition section 18) | **outcome_ref:** FWD-8 | **depends_on:** none.

THIS CELL MAKES NO VENDOR CALL. Every input is already landed.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-13`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~13/`.

**The cell (`DB-b-27`), verbatim from the ruling:** "The E2 tie-out compares on ONE basis, gross of fees: Opal's served 49F return is
gross (fee_basis GROSS, IB-pr-221), so Black Diamond's net figure is compared after adding back BD's own reported fee for that segment,
and the add-back is printed per segment beside both figures. No FEES reason joins the closed set: a basis difference is not an
explanation. A segment with no BD-reported fee stays UNEXPLAINED." Tolerance stays 0.35 pp. The closed reason set stays FLOW_TIMING,
MISSING_PRICE, INCOME_DATE, COVERAGE_DAYS, UNEXPLAINED.

**What exists (read it, do not edit it):** the round-17 tie-out in
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~12/`: `tieout_e2.py` (335 lines), its tests, and its record
`TIEOUT_49F_BD_POPULATION_E2.json` (9,082 planned, 9,078 graded). It reads the plan
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~6/BD_POPULATION_PLAN_E3.json`, the landed BD responses at
`s3://opal-data-assets/blackdiamond/49financial/bronze/reporting_performance/pull=20261004/acct=<id>.json` (5,252 objects) and the
served 49F series. Its function `fee_observation` already computes BD's fee drag as `fees / ((bmv + emv) / 2)` from the BD range's
`fees`, `bmv` and `emv`; round 17 subtracted that drag from Opal's figure. That direction is now forbidden: no net-of-fee Opal figure
is produced anywhere (FWD-9).

**What you build:**
1. `tieout_e2_gross.py` in your folder. Import or copy what you need from the round-17 script; do not edit that script. For every
   segment it writes, in `TIEOUT_49F_BD_POPULATION_E2_GROSS.json`:
   - top level: `basis: "GROSS"`, `tolerance_pp: 0.35`, `vendor_calls: 0`, `inputs` (as round 17) and `counts` (as round 17:
     `segments_planned`, `graded`, `not_gradable`, `within_tolerance`, `outside_tolerance`, outside per reason);
   - per segment: the round-17 keys (`account`, `segment`, `bd_return`, `opal_return`, `opal_days`, `bd_days_held`, `verdict`,
     `reason`, `evidence`, `why`), plus `bd_fees_reported` (BD's raw `fees` for the range, or null), `bd_fee_addback`
     (`fees / ((bmv + emv) / 2)`, or null when BD reported no fee or zero fee, or the average value is not positive) and
     `bd_gross_return` (`bd_return + bd_fee_addback`, or `bd_return` when the add-back is null). `abs_diff_pp` is
     `|bd_gross_return - opal_return| * 100`, and the verdict is graded on it.
   - `opal_return` is the served figure exactly as round 17 read it. Never write a key naming Opal together with net or fee.
   - A reason is assigned on named evidence only, by the round-17 rules; the BD_FEES observation clause is dropped, because the
     basis now carries it.
2. `tests/test_tieout_e2_gross.py`: at least 4 offline tests on synthetic inputs, naming `bd_fee_addback`: an add-back that brings a
   segment within tolerance; a null add-back (no BD fee) that stays UNEXPLAINED when outside; a non-positive average value giving a
   null add-back; the counts reconciling.
3. A summary `TIEOUT_49F_BD_POPULATION_E2_GROSS.md` beside the record, COUNTS ONLY (no client figure): the counts table, how many rows
   carry a null add-back, and the change in each count against round 17.
4. Run the script once; commit the script, tests, record and summary.

<criterion id="DB18-1-AC1" cell_refs="DB-b-27"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r18/p18_gross.py" . DB18-1-AC1</invocation><expect>DB18-1-AC1 PASS</expect></criterion>
`DB18-1-AC1` -- the GROSS record reconciles: basis GROSS, 0.35 pp, 0 vendor calls; planned = graded + not gradable = the plan's count;
every graded row carries `bd_fee_addback` and `bd_gross_return`; every outside row's reason is in the unchanged closed set. Base: FAIL.

<criterion id="DB18-1-AC2" cell_refs="DB-b-27"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r18/p18_gross.py" . DB18-1-AC2</invocation><expect>DB18-1-AC2 PASS</expect></criterion>
`DB18-1-AC2` -- `bd_fee_addback` is null exactly where `bd_fees_reported` is null or zero, and the tests pass (at least 4). Base: FAIL.

<criterion id="DB18-1-AC3" cell_refs="DB-b-27"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r18/p18_gross.py" . DB18-1-AC3</invocation><expect>DB18-1-AC3 PASS</expect></criterion>
`DB18-1-AC3` -- no net-of-fee Opal figure: no key names Opal with net or fee, and every graded row's `opal_return` equals the round-17
record's for the same account and segment. Base: FAIL.

<expected_criteria>DB18-1-AC1,DB18-1-AC2,DB18-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Read the round-17 folder, the plan and the bronze prefix; write only your folder.
- **AWS:** S3 reads only. NO Black Diamond or other vendor call, and no write.
- **Refusal clause.** A vendor call, a write to S3, a net-of-fee Opal figure, a FEES reason, or a client figure in a committed `.md`
  is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~13/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-27.tieout-e2-gross-basis.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 18 (round 18, workstream B), cell `DB-b-27`.
<owned_cells>DB-b-27</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB18-1-AC1, DB18-1-AC2, DB18-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~13/IRPT_DASHBD.TO-DB-b-27.tieout-e2-gross-basis.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB18-1-AC1,DB18-1-AC2,DB18-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes, each criterion's last line, the counts (planned, graded, within, outside per
reason, not gradable per why), the number of null add-backs, the change in each count against round 17, and any row ids.


## AMENDMENT 1 (2026-10-07 ~09:5xZ, issuer 2.0.0_SA_COO~D2, rows W13-S1 and W13-S3)

- **W13-S1 ruled:** the served 49F gold is fenced from the dell2 identity, so under 1.0.0_SA_CTO~DELL2's standing rule the laptop's
  3.0.0_SA_CVO ran this order's script at fb966b0a72, unchanged and read-only. Its record is in commit e6ed5380e6
  (sha256 febe370fbed76497...). The worker copies that record byte-exact and makes no AWS call.
- **W13-S3 ruled, the checker's defect:** DB18-1-AC2 nulled the add-back only where the fees are null or zero. This face also nulls it
  where BD's average value is not positive, and the record carries no market values. The issuer measured the one disagreeing range
  in the landed bronze object (2026-06-17..2026-07-21: fees -52.99, beginningMarketValue 0.01, endingMarketValue -0.70). The checker
  now admits exactly that literal range. A negative control without the exemption still FAILs.
- No gate limb graded this modification: LIMB 6 does not fire on a modification, and GATE (viii) grades the unchanged
  `<placeholders>NONE</placeholders>`.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- an offline re-grade over landed data; 0 served bytes move; no vendor call.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads only.
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB18-1-AC1, AC2 and AC3 base FAIL (no record), dry-run at base 3dd25927f2 2026-10-07 ~08:5xZ.
lane: the <paths> block IS the grant.
</preflight>
