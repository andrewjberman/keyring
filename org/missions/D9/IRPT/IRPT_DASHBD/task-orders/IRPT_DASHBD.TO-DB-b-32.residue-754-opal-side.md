# TO IRPT_DASHBD.TO-DB-b-32 -- E2: re-read the 754 non-closure UNEXPLAINED segments with Opal's served daily series, now readable on dell2, against the closed reason set (FWD-8; zero vendor calls)

<to_id>IRPT_DASHBD.TO-DB-b-32</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~17</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 round-19 analysis @b402b7b2e3 item E2 ("The ~754
non-closure residue ... (1) counted against the closed reason set with named evidence; (2) a reason outside the set is a surprise row, not
added") | **Decomp cell:** `DB-b-32` (decomposition section 20) | **outcome_ref:** FWD-8 | **depends_on:** DB-b-30 (merged @5831f348b8).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-17`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~17/`.

**The cell (`DB-b-32`).** Round 19 read these 754 segments from BD's side only, because Opal's served series was fenced from this box. It
is readable now. Re-read each segment with Opal's side as well, and assign a closed-set reason only on evidence named in the row:
FLOW_TIMING (a re-link of Opal's daily returns under the START or MID flow convention lands within 0.35 pp of BD's gross figure),
INCOME_DATE (the link with Opal's income_return removed on its pay days lands within 0.35 pp), MISSING_PRICE (Opal's served days in the
segment carry `holdings_price_return_reason` other than OK), COVERAGE_DAYS (a day-count difference of 2 or more), else UNEXPLAINED with
what was checked. These are the round-17 rules (`deliverables/0.9.0_WK_IRPT_DASHBD~12/tieout_e2.py`); apply them against BD's GROSS figure.
The closed set is FLOW_TIMING, MISSING_PRICE, INCOME_DATE, COVERAGE_DAYS, UNEXPLAINED; a basis difference is never a reason.

**The set (the check re-derives it):** rows of `deliverables/0.9.0_WK_IRPT_DASHBD~15/RESIDUE_NONCLOSURE_E2.json` with reason UNEXPLAINED.
There are 754. BD's GROSS figure for each is in `deliverables/0.9.0_WK_IRPT_DASHBD~13/TIEOUT_49F_BD_POPULATION_E2_GROSS.json`.

**Inputs (both readable from this box since the fence join):** Opal's served series
`s3://opal-data-49financial/irpt/49financial/gold/account_return_daily/date=<YYYY-MM-DD>/data.parquet`; BD's landed responses
`s3://opal-data-assets/blackdiamond/49financial/bronze/reporting_performance/pull=20261004/acct=<bd_account>.json`.

**What you build:**
1. `residue_754_e2.py` in your folder, read-only (S3 `list_objects_v2`/`get_object` only), writing `RESIDUE_754_E2.json`: `counts`
   {`denominator` (754), `per_reason` (summing to it), `final_unexplained`} and `rows`, one per segment, `{account, segment, reason,
   evidence}`. A pattern that needs a reason the set lacks: ONE surprise row, the segments stay UNEXPLAINED, the row id named in the summary.
2. `tests/test_residue_754_e2.py`: at least 4 offline tests on synthetic inputs, naming `residue`.
3. A summary `RESIDUE_754_E2.md`, COUNTS ONLY (no client figure).
4. Run once; commit script, tests, record and summary. If an S3 read is denied, file ONE BLOCKING row with the error text and STOP;
   never try to change a policy.

<criterion id="DB20-2-AC1" cell_refs="DB-b-32"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r20/p20_measured.py" . DB20-2-AC1</invocation><expect>DB20-2-AC1 PASS</expect></criterion>
`DB20-2-AC1` -- denominator 754 re-derived; per-reason sums to it; final UNEXPLAINED matches the rows. Base: FAIL.

<criterion id="DB20-2-AC2" cell_refs="DB-b-32"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r20/p20_measured.py" . DB20-2-AC2</invocation><expect>DB20-2-AC2 PASS</expect></criterion>
`DB20-2-AC2` -- one row per residue segment, each with a closed-set reason and non-empty evidence. Base: FAIL.

<criterion id="DB20-2-AC3" cell_refs="DB-b-32"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r20/p20_measured.py" . DB20-2-AC3</invocation><expect>DB20-2-AC3 PASS</expect></criterion>
`DB20-2-AC3` -- the tests pass (at least 4, naming residue). Base: FAIL.

<expected_criteria>DB20-2-AC1,DB20-2-AC2,DB20-2-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** S3 reads only, of the two prefixes above. No vendor call, no write, no policy change.
- **Refusal clause.** A reason added to the closed set, a vendor call, a write, a policy change, or a client figure in a committed `.md`
  is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~17/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-32.residue-754-opal-side.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 20 (round 20, workstream B), cell `DB-b-32`.
<owned_cells>DB-b-32</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB20-2-AC1, DB20-2-AC2, DB20-2-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~17/IRPT_DASHBD.TO-DB-b-32.residue-754-opal-side.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB20-2-AC1,DB20-2-AC2,DB20-2-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the counts and per-reason residue, the evidence kinds used, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- an offline read of served and landed data; 0 served bytes move; no vendor call.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads only; both buckets read from dell2 since the fence join (TO-APPLY-4 @aefcf32c11).
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB20-2-AC1, AC2 and AC3 base FAIL (no record, no tests), dry-run at base e5267d5a2b 2026-10-07 ~11:1xZ.
lane: the <paths> block IS the grant.
</preflight>
