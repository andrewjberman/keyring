# TO IRPT_BCKEND.TO-IB-pr-192 -- Since inception answers from the account's first data point (UIC-06 backend half, UIC-07)

<to_id>IRPT_BCKEND.TO-IB-pr-192</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~61</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-09-28</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>19</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `IB-pr-192` (decomposition section 13) | **outcome_ref:** FWD-3
| **depends_on:** `IRPT_BCKEND.TO-IB-pr-191` (same files; it is ahead of this order in your queue)

---

## WORKER FACE

### THE CELL

`IB-pr-192` -- for a 49 Financial account, "Since inception" answers Unavailable (UNSUPPORTED_OPERATION). The page's
preset sends start `1970-01-01` (a fixed epoch, measured by the CRO walk as UIC-07), and `f49_engine.ruled_period_for`
accepts only YTD, QTD and 1Y, so it raises `WindowNotRuled`. The engine lane's own linker already rules a fourth
period: `parity_period_returns.RULED_PERIODS = ("QTD", "YTD", "1Y", "SI")`, with `period_window(period, asof,
anchor)` and an SI anchor (read `data/assets/scripts/gold/runners_49f/parity_period_returns.py` lines 159-360 before
building). Its docstring warns that an SI with no anchor silently collapses to the window: never let that happen.

**Build**, in `infra/aws/lambda/investor-reporting/performance/f49_engine.py` of your worktree:
1. A request whose start is exactly `1970-01-01` is the Since-inception request. Anchor it at the account's FIRST
   `business_date` whose `status` is `OK` in `twr_daily` (read from the partitions, never typed or assumed), link it as
   the ruled period `SI` with that anchor, and report `dates.actual_start` = that day and `returns.period_returns`
   naming `SI`. The linker is reused, never restated.
2. Every other window that is not YTD, QTD or 1Y (3Y included) still raises `WindowNotRuled`. The IB-pr-191 guard
   (`EngineReturnImplausible`) applies to SI as to every window.
3. Add the SI fixture and the 3Y control to `tests/test_f49_engine.py`.

A Since-inception read touches every partition from the account's first day (the engine starts 2024-07-08); the
reader is already threaded (`MAX_READ_WORKERS`). Do not add a second reader.

### ACCEPTANCE (run each from your worktree root)

<criterion id="P19-2-AC1" cell_refs="IB-pr-192"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r19/p19_2_ac1_since_inception_fixture.py" .</invocation><expect>P19-2-AC1 PASS</expect></criterion>
`P19-2-AC1` -- the built behaviour with its control: arm A, start 1970-01-01 answers SI from the first OK day
2025-12-31; arm B, a 3-year request still refuses as WindowNotRuled. Base: arm A FAIL (WindowNotRuled), arm B PASS.

<criterion id="P19-2-AC2" cell_refs="IB-pr-192"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r19/p19_2_ac2_live_seam.py" .</invocation><expect>P19-2-AC2 PASS</expect></criterion>
`P19-2-AC2` -- the seam probe against the REAL engine table, read-only S3 (about 30 s): live SI for the control
account starts on its first OK day, read independently by the check, with a finite value above -1. Base: FAIL
(WindowNotRuled, first OK day 2024-11-07).

<expected_criteria>P19-2-AC1,P19-2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **No deploy, no AWS write.** AC2 reads S3 only. WORLD is the L6 path floor for a Lambda's source.
- **Refusal clause.** If a criterion cannot be met as written (for example, the linker cannot take an anchor for
  SI), stop, write the reason in your report and a surprise row, and do not weaken a check to pass.

<paths>
infra/aws/lambda/investor-reporting/performance/f49_engine.py
infra/aws/lambda/investor-reporting/performance/tests/test_f49_engine.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 13 (round 19, workstream ~P), cell `IB-pr-192`.
<owned_cells>IB-pr-192</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: P19-2-AC1, P19-2-AC2. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~61/IRPT_BCKEND.TO-IB-pr-192.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> P19-2-AC1,P19-2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message: the commit hash, each criterion's last line, and any surprise row id
(`IRPT_BCKEND-W19P-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule, trigger or cron is created or changed; the cell is code and tests on a branch.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM policy or role changes; the S3 reads in the live check run under the worker session's existing read access.
comp-blast: DECLARED-NOT-APPLICABLE -- one source file and one test change on a branch, nothing served.
comp-routes: DECLARED-NOT-APPLICABLE -- the route table is unchanged; one more window answers on the existing route.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache or CDN surface is touched.
comp-adversary: RUN -- checks dry-run at the base: AC1 FAIL (WindowNotRuled)/PASS; AC2 FAIL (WindowNotRuled, first OK 2024-11-07) as expected. The epoch sentinel is the portal's measured request (UIC-07); a date-based SI rule was rejected because the engine's history (from 2024-07-08) is shorter than 3Y, so "start before the earliest partition" would misread a 3Y request as SI.
lane: the <paths> block IS the grant.
</preflight>
