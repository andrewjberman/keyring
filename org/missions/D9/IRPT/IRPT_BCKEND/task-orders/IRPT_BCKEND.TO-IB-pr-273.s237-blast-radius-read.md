# TO IRPT_BCKEND.TO-IB-pr-273 -- Does the retiring engine's skipped-day error reach a served period return? Measured on the deployed adapter and every served reader

<to_id>IRPT_BCKEND.TO-IB-pr-273</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~100</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-09-30</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>27</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 1.0.0_SA_CTO ROUND-26 ~P ANALYSIS ruling 4
(`org/missions/D9/IRPT/IRPT_BCKEND/ledger/ROUND_ANALYSIS.round26P.md` @7c9ed807bb); rows S237 and S239 (BLOCKING, ARMED) |
**Decomp cell:** `IB-pr-273` (decomposition section 25) | **outcome_ref:** FWD-3 (49F) | **depends_on:** none

---

## WORKER FACE

**The cell.** Read-only. Row S237 (read it in `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`):
2025-01-09 was an NYSE closure the 49F engine (`data/assets/scripts/gold/runners_49f/c02_twr_engine.py`) skips, but the custodian book
moved that day, and `c02:460` reads the flow ledger at `date=D` only, so 01-09's flows sit in 01-10's end value and in neither the begin
value nor the flow: account `0093614544` served `r_net` +56.10% on 2025-01-10 for a $1,125,000 deposit; 46 accounts, 44 with OK rows,
max error +91.13 pp. Row S239 adds that `parity_period_returns.py:373-388` links a non-OK day as NEUTRAL BY VALUE, so a period spanning
2025-01-10 carries the error. The question the CTO asks: **does it reach a SERVED period return?** Answer it by measurement.

**Read 1 -- the deployed Performance adapter.** Take the EXACT deployed code: `aws lambda get-function-configuration --function-name
irpt-performance-adapter` (CodeSha256 at the cut `+h/AH/RY7PK+MLuXyflt+YYzWg+jXHSXTOUBwr0EHbo=`, applied 2026-09-29T16:40:25Z, the 49F
r3 re-switch to the holdings gold) and its artifact (`get-function` -> the code location, or `s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-performance-adapter.zip`
at the S3 version whose metadata `content-sha256` equals it). Run it as a cold container with the existing harness
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r20/adapter_cold_periods.py` (read its header for the extract and
the event shape; it reads real S3, writes nothing). Ask since-inception (SI) and 3Y for `0093614544` and at least two other S237
accounts (their ids are in the row). Record per account `SI`, `3Y` (a figure or a named refusal code, verbatim), and `reads` (the table
the answer came from: the holdings gold `irpt/49financial/gold/holdings_performance_daily/` or the engine's `gold/advi/canonical/twr_daily/`).
Name `reader_shape` for the served adapter path: `PARTITION_LISTING` (lists partitions and refuses a non-OK window),
`CALENDAR_ENUMERATION` (enumerates days and can hide the gap), or `NOT_A_TWR_DAILY_READER` (it reads the holdings gold only).
Also say whether RETAINED reports (the reopen path, `infra/aws/lambda/investor-reporting/performance/retained.py`) still carry
engine-era figures spanning 2025-01-10.

**Read 2 -- every other served reader of `twr_daily`.** The census at the cut (decomposition section 24): 19 first-party files name
`twr_daily`, among them `data/assets/scripts/gold/runners_49f/{parity_period_returns,perfrp_emit_core,perfrp_rollup,perfrp_contract,c04_validation_battery,chain_49f_entrypoint}.py`,
`infra/aws/lambda/investor-reporting/performance/{f49_engine,holdings_gold,retained}.py`, and the portal's
`portal/src/pages/AdvisorIntelligence/_shared/perfrp/{cards,contract}.ts`. For each file that feeds a SERVED surface, one row:
`file`, `served_surface` (the page or API a person reads, or "none"), `reads_2025_01_09` (does its served window include that
partition), `propagates` (true/false, with the measured figure where true).

**The record:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~100/S237_BLAST_RADIUS.json` with `adapter`
(`function`, `code_sha256` you ran, `accounts`, `propagates`), `reader_shape`, `readers`, and `verdict` (`PROPAGATES` if any served
reader carries it, else `DOES_NOT_PROPAGATE`). You remedy nothing: if it propagates, the CTO's ruling moves the 49F re-switch into this
round as the issuer's cell, and the engine is never patched.

<criterion id="P27-3-AC1" cell_refs="IB-pr-273"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r27/p27_3_blast_radius.py" .</invocation><expect>P27-3-AC1 PASS</expect></criterion>
`P27-3-AC1` -- the record's adapter read ran the code whose CodeSha256 equals the live function's (read at check time); three accounts
with SI and 3Y; a named reader shape; every served reader censused with a propagates flag; a verdict consistent with the rows.
Base: FAIL (record absent).

<expected_criteria>P27-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (the channel), plus your deliverables folder and this order's file. Everything else READ only.
- **No write to AWS, no invoke of the live function, no vendor call.** The cold container runs locally on the deployed bytes.
- **Refusal clause.** If the deployed artifact cannot be matched to the live CodeSha256, stop and say so in a row; never run the repo copy
  in its place.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r27/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r20/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 25 (round 27, workstream ~P), cell `IB-pr-273`.
<owned_cells>IB-pr-273</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: P27-3-AC1. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~100/IRPT_BCKEND.TO-IB-pr-273.s237-blast-radius-read.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> P27-3-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message: the commit hash, the criterion's last line, the verdict, the adapter's reader shape, each propagating
reader with its figure, and any surprise row id (`IRPT_BCKEND-W100-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: read-only; no schedule, trigger or cron is created, read for change, or moved.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: read-only; 0 roles or policies touched; the cold container uses the reader's own credentials for S3 reads.
comp-blast: RUN -- denominator: 19 first-party files naming twr_daily at the cut (section 24 census); 0 writes outside the worker's deliverables and the channel.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route; the served surfaces are named, not changed.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache.
comp-adversary: RUN -- P27-3-AC1 base FAIL (record absent); the check reads the live CodeSha256 at run time, so a read on the repo copy cannot pass.
lane: the <paths> block IS the grant.
</preflight>
