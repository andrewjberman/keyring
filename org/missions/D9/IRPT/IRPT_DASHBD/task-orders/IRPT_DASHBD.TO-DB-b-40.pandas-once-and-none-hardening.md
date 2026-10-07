# TO IRPT_DASHBD.TO-DB-b-40 -- E3 (last in the queue): the pandas option set once per process in the activity producer; the served producer's classify_and_sum hardened against None in the repository (row W21-S6) (FWD-4)

<to_id>IRPT_DASHBD.TO-DB-b-40</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~22</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>25</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 round-24 analysis @99580aac8c item E3 ("future.infer_string is set once per process, or classification runs outside the pool; a threaded test that would flip under the old per-call context passes; the served producer's classify_and_sum is hardened against None in the repository, with a test on pandas 3 semantics. Shipping it is the next release's half") | **Decomp cell:** `DB-b-40`
(decomposition section 25) | **outcome_ref:** FWD-4 | **depends_on:** DB-b-39 (same worker, same queue: run it last, because it edits the same producer file).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-22`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~22/`.

**The cell (`DB-b-40`).** Round 24 ran the served flow call under a per-call `pd.option_context("future.infer_string", False)` (`served_runtime()`), which is process-global and is entered around a thread pool (row IRPT_DASHBD-W21-S6). Separately, `classify_and_sum` in `data/assets/scripts/gold/irpt_reporting/account_return_daily.py` resolves the CONDITIONAL-BY-COUNTERPARTY class with `_final is None`; on pandas 3 the None becomes NaN and those rows drop. The served function runs pandas 2.2.3 today and is unaffected; this cell hardens the SOURCE only. Nothing is built, staged or deployed.

1. In `account_activity_lots.py`, set `future.infer_string` to False ONCE per process at the producer's entry (where the option exists),
   or run classification outside the pool; remove the per-call context. Add a test whose name contains `thread` that classifies
   conditional rows from several threads at once and asserts every one resolves; it must be a test that would fail under a per-call
   context entered by one thread while others run.
2. In `account_return_daily.py`, make `classify_and_sum` resolve the conditional class without depending on None surviving a pandas
   column (test with `pd.isna`, or keep the column `object` dtype explicitly). Change nothing else in that file: its outputs on pandas
   2.2.3 must not move. Add `tests/test_account_return_daily_none.py`: synthetic conditional rows through `classify_and_sum` resolve under
   pandas-3 string inference (enable `future.infer_string` inside the test where the option exists) and give the same sums as with it off.
3. Keep every test in the folder passing.

<criterion id="DB25-3-AC1" cell_refs="DB-b-40"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r25/p25_windows.py" . DB25-3-AC1</invocation><expect>DB25-3-AC1 PASS</expect></criterion>
`DB25-3-AC1` -- a threaded test passes and the producer's test file passes. Base: FAIL.

<criterion id="DB25-3-AC2" cell_refs="DB-b-40"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r25/p25_windows.py" . DB25-3-AC2</invocation><expect>DB25-3-AC2 PASS</expect></criterion>
`DB25-3-AC2` -- the None-hardening test of classify_and_sum passes. Base: FAIL.

<expected_criteria>DB25-3-AC1,DB25-3-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** S3 reads only. No write, no deploy, no vendor call, no bun, no download of any package, script or program.
- **Refusal clause.** A plugged gap, a per-account patch, an S3 write, a deploy, or a client figure in a committed `.md` is a defect:
  stop and file a row.

<paths>
data/assets/scripts/gold/irpt_reporting/account_activity_lots.py
data/assets/scripts/gold/irpt_reporting/tests/test_account_activity_lots.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~22/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
data/assets/scripts/gold/irpt_reporting/account_return_daily.py
data/assets/scripts/gold/irpt_reporting/tests/test_account_return_daily_none.py
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-40.pandas-once-and-none-hardening.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 25 (round 25, workstream B), cell `DB-b-40`.
<owned_cells>DB-b-40</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB25-3-AC1, DB25-3-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~22/IRPT_DASHBD.TO-DB-b-40.pandas-once-and-none-hardening.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB25-3-AC1,DB25-3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, what you changed, the numbers each criterion prints, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a source-only hardening of the served producer, not built, staged or deployed (the served layer runs pandas 2.2.3; shipping is the next release's half under its own sign-off); no S3 write.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only, from this box; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB25-3-AC1 and AC2 base FAIL (no threaded test; no None test file), dry-run at base 99580aac8c 2026-10-07 ~17:2xZ.
lane: the <paths> block IS the grant.
</preflight>
