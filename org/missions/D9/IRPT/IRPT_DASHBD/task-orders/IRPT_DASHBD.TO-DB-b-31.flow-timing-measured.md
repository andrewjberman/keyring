# TO IRPT_DASHBD.TO-DB-b-31 -- E1: measure the 226 inferred FLOW_TIMING segments -- a Modified Dietz of Opal's dated flows over Black Diamond's own totals, with a midpoint negative control and a flow-totals guard (FWD-8; zero vendor calls)

<to_id>IRPT_DASHBD.TO-DB-b-31</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~16</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 round-19 analysis @b402b7b2e3 item E1, method
ruled in msg 400 ("Modified Dietz of Opal's dated flows over BD's own totals ... Add two guards: (1) a negative control: shift each
segment's flows to the range midpoint and print how many still fall inside 0.35 pp ... (2) print per segment whether Opal's summed flows
equal BD's netAdditions. Where they do not, the segment is UNEXPLAINED whatever Dietz gives.") | **Decomp cell:** `DB-b-31` (decomposition
section 20) | **outcome_ref:** FWD-8 | **depends_on:** DB-b-30 (merged @5831f348b8).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-16`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~16/`.

**The cell (`DB-b-31`).** Round 19 tagged 226 segments FLOW_TIMING on an INFERENCE (`claim: inferred`): a large net flow, with both returns
inside the Dietz envelope of that flow placed at segment start or end. Measure each one instead:
1. **Opal's dated flows:** for the segment's account and days, read Opal's daily external flows from the served 49F series
   `s3://opal-data-49financial/irpt/49financial/gold/account_return_daily/date=<YYYY-MM-DD>/data.parquet` (readable from this box since
   the fence join; the round-17 script `deliverables/0.9.0_WK_IRPT_DASHBD~12/tieout_e2.py` shows how it reads the series). Name the flow
   column you use in the record.
2. **BD's own totals:** for the same segment, read BD's Account-level `beginningMarketValue`, `endingMarketValue` and `netAdditions` from
   the landed response `s3://opal-data-assets/blackdiamond/49financial/bronze/reporting_performance/pull=20261004/acct=<bd_account>.json`
   (the plan `deliverables/0.9.0_WK_IRPT_DASHBD~6/BD_POPULATION_PLAN_E3.json` maps account to bd_account).
3. **`dietz_return`:** the Modified Dietz return over BD's bmv, emv and netAdditions with each Opal flow weighted by the fraction of the
   segment remaining after its date. `abs_diff_pp_dietz` = |dietz_return - bd_gross_return| x 100, where `bd_gross_return` is in
   `deliverables/0.9.0_WK_IRPT_DASHBD~13/TIEOUT_49F_BD_POPULATION_E2_GROSS.json`.
4. **Guard (2):** `flows_match` is true when |sum of Opal's flows - netAdditions| <= max(1.00, 0.005 x |netAdditions|). Print both sums.
5. **Guard (1), the negative control:** `abs_diff_pp_midpoint` is the same Dietz with every flow moved to the segment's midpoint day.
6. **Verdict:** `MEASURED_FLOW_TIMING` only when `flows_match` is true AND `abs_diff_pp_dietz` <= 0.35; otherwise `UNEXPLAINED`.

**The set (the check re-derives it):** rows of `deliverables/0.9.0_WK_IRPT_DASHBD~15/RESIDUE_NONCLOSURE_E2.json` with reason FLOW_TIMING.
There are 226.

**What you build:**
1. `flow_measured_e1.py` in your folder, read-only (S3 `list_objects_v2`/`get_object` only), writing `FLOW_MEASURED_E1.json`: `counts`
   {`measured`, `returned_unexplained`, `unexplained_measured_basis` (= 3,053 + returned_unexplained: round 19 left 754 non-closure + 2,299
   closure UNEXPLAINED), `negative_control_within`}, `inputs` (the flow column, gold partitions read, the bronze prefix) and `rows`, one
   per segment: `{account, segment, bd_gross_return, dietz_return, abs_diff_pp_dietz, abs_diff_pp_midpoint, opal_flow_sum,
   bd_net_additions, flows_match, verdict}`.
2. `tests/test_flow_measured_e1.py`: at least 4 offline tests on synthetic inputs, naming `midpoint`: a dated flow that reproduces BD's
   figure; the same flow at the midpoint failing; a flows mismatch forcing UNEXPLAINED; the counts reconciling.
3. A summary `FLOW_MEASURED_E1.md`, COUNTS ONLY (no client figure), with the negative-control count beside the measured count.
4. Run once; commit script, tests, record and summary. If an S3 read is denied, file ONE BLOCKING row with the error text and STOP;
   never try to change a policy.

<criterion id="DB20-1-AC1" cell_refs="DB-b-31"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r20/p20_measured.py" . DB20-1-AC1</invocation><expect>DB20-1-AC1 PASS</expect></criterion>
`DB20-1-AC1` -- one row per FLOW_TIMING segment with the E1 fields and a two-value verdict; measured, returned and the measured-basis
UNEXPLAINED count reconcile. Base: FAIL.

<criterion id="DB20-1-AC2" cell_refs="DB-b-31"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r20/p20_measured.py" . DB20-1-AC2</invocation><expect>DB20-1-AC2 PASS</expect></criterion>
`DB20-1-AC2` -- the guards: the midpoint control is printed and re-derives; no segment is measured with a flows mismatch or a Dietz gap
above 0.35 pp. Base: FAIL.

<criterion id="DB20-1-AC3" cell_refs="DB-b-31"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r20/p20_measured.py" . DB20-1-AC3</invocation><expect>DB20-1-AC3 PASS</expect></criterion>
`DB20-1-AC3` -- the tests pass (at least 4, naming midpoint). Base: FAIL.

<expected_criteria>DB20-1-AC1,DB20-1-AC2,DB20-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** S3 reads only, of the two prefixes above. No vendor call, no write, no policy change.
- **Refusal clause.** A vendor call, a write, a policy change, a changed served figure, or a client figure in a committed `.md` is a
  defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~16/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-31.flow-timing-measured.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 20 (round 20, workstream B), cell `DB-b-31`.
<owned_cells>DB-b-31</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB20-1-AC1, DB20-1-AC2, DB20-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~16/IRPT_DASHBD.TO-DB-b-31.flow-timing-measured.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB20-1-AC1,DB20-1-AC2,DB20-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the counts (measured, returned, negative control), the flow column, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- an offline measurement; 0 served bytes move; no vendor call.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads only; both buckets read from dell2 since the fence join (TO-APPLY-4 @aefcf32c11).
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB20-1-AC1, AC2 and AC3 base FAIL (no record, no tests), dry-run at base e5267d5a2b 2026-10-07 ~11:1xZ.
lane: the <paths> block IS the grant.
</preflight>
