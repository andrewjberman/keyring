# TO IRPT_DASHBD.TO-DB-b-26 -- E2: the 0.35 pp tie-out of the 49 Financial served total return against Black Diamond's own return, over all 9,082 landed segments (FWD-8; zero vendor calls)

<to_id>IRPT_DASHBD.TO-DB-b-26</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~12</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-05</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>17</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 1.0.0_SA_CTO round-15 analysis item E2
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_IRPT_DASHBD_ROUNDS_12_14_B_20261005.md` @b09cafb7a4): "per account and per Opal
gap-free segment, the served 49F total return against Black Diamond's performancePeriod return, graded against 0.35 pp; every disagreement
carries a stated reason from C-TIEOUT's classes ... or UNEXPLAINED; counts only". E1 (the pull) is complete: ledger
irpt-dashbd-e3-bd-population-pull-20261004, P1 closed @54cbe5a477, S3 5,252 of 5,252 | **Decomp cell:** `DB-b-26` (decomposition section
17) | **outcome_ref:** FWD-8 | **depends_on:** E1 (complete).

THIS CELL MAKES NO VENDOR CALL. Every input is already landed.

---

## WORKER FACE

Your worktree is `C:/Users/AndrewBerman/Desktop/wk-irpt-dashbd-12`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~12/`.

**The inputs:**
- **Black Diamond's side:** one `performancePeriod` response per account at
  `s3://opal-data-assets/blackdiamond/49financial/bronze/reporting_performance/pull=20261004/acct=<bd_internal_id>.json` (5,252 objects).
  Each request asked for that account's Opal gap-free segments as its dateRanges. The plan
  `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~6/BD_POPULATION_PLAN_E3.json` lists each account's `segments`
  (9,082 in all) and its `bd_account`.
- **Opal's side:** the SERVED 49 Financial total return for the same account and segment. That is the daily-TWR gold the portal's
  Performance tab reads (PATH B; DB-b-1's gold and its successors). Find its location from the code, not by guessing: start at
  `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.4.0_DS_ClientPlatform~S/tieout/TIEOUT_49F_BLACKDIAMOND_R1.md`, the round-1 tie-out
  on five periods, and from the reporting producer it names. Link the daily returns geometrically over exactly the segment's days.
- **The method precedent:** that round-1 record. Its central finding: Opal's link EXCLUDES account-days it withheld, while BD covers
  its full `daysHeld`, so day-coverage dominated the difference. Apply the same reading per segment.

**What you build:**
1. **A tie-out script** in your folder that reads the plan, every landed BD response and the served Opal series, and writes
   `TIEOUT_49F_BD_POPULATION_E2.json` with:
   - `tolerance_pp: 0.35` and `vendor_calls: 0`;
   - `inputs`: `bronze_prefix`, `bronze_object_count` (read: 5252), `served_series` (its location) and `served_accounts` (how many
     accounts it covers), plus the plan path;
   - `counts`: `segments_planned` (= the plan's 9,082), `graded`, `not_gradable`, `within_tolerance`, `outside_tolerance`, and the
     outside counts per reason;
   - `segments`: one row per segment, `{account, segment, bd_return, opal_return, abs_diff_pp, verdict: WITHIN | OUTSIDE |
     NOT_GRADABLE}`. An OUTSIDE row carries `reason` from the closed set: FLOW_TIMING, MISSING_PRICE, INCOME_DATE, COVERAGE_DAYS (Opal
     withheld days BD counted) or UNEXPLAINED. Assign a reason only on evidence you can name in the row's `evidence` field; else
     UNEXPLAINED. A NOT_GRADABLE row carries `why`, e.g. BD returned no value for the range, or the served series lacks the account.
   - The JSON may carry figures (it stays local and is gitignored if the folder already ignores data). The summary `.md` you write
     beside it carries COUNTS ONLY, per the analysis: no client figure.
2. **`tests/test_tieout_e2.py`**, at least 4 offline tests with synthetic inputs:
   - within the tolerance;
   - outside with a reason;
   - not_gradable with a why;
   - the counts reconcile.

   The words `tolerance`, `reason` and `not_gradable` appear in the file.
3. **Run the script once**, then commit the script, tests, record and summary.

<criterion id="DB17-1-AC1" cell_refs="DB-b-26"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r17/p17_tieout.py" . DB17-1-AC1</invocation><expect>DB17-1-AC1 PASS</expect></criterion>
`DB17-1-AC1` -- the record reconciles: planned = graded + not gradable, graded = within + outside, every outside row has a reason from
the closed set, every not-gradable row has a why, and 0 vendor calls. Base: FAIL.

<criterion id="DB17-1-AC2" cell_refs="DB-b-26"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r17/p17_tieout.py" . DB17-1-AC2</invocation><expect>DB17-1-AC2 PASS</expect></criterion>
`DB17-1-AC2` -- the inputs are named with their denominators (5,252 bronze objects, the served series and its account count), and the
tests pass (at least 4). Base: FAIL.

<criterion id="DB17-1-AC3" cell_refs="DB-b-26"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r17/p17_tieout.py" . DB17-1-AC3</invocation><expect>DB17-1-AC3 PASS</expect></criterion>
`DB17-1-AC3` -- a GUARD: your commits touch only your grant. Base: PASS.

<expected_criteria>DB17-1-AC1,DB17-1-AC2,DB17-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** S3 reads only (the bronze prefix and the served series). NO Black Diamond or other vendor call, and no write.
- **Refusal clause.** A vendor call, a write to S3, or a client figure in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~12/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-26.tieout-49f-bd-population.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 17 (round 17, workstream B), cell `DB-b-26`.
<owned_cells>DB-b-26</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB17-1-AC1, DB17-1-AC2, DB17-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~12/IRPT_DASHBD.TO-DB-b-26.tieout-49f-bd-population.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB17-1-AC1,DB17-1-AC2,DB17-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes, each criterion's last line, the counts (planned, graded, within, outside per
reason, not gradable per why), the served series used, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- an offline grade over landed data; 0 served bytes move; no vendor call.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads only.
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB17-1-AC1 base FAIL (no record), DB17-1-AC2 base FAIL (no inputs or tests), DB17-1-AC3 base PASS (guard), dry-run at base 1b30e3b6d6 2026-10-05 ~16:1xZ.
lane: the <paths> block IS the grant.
</preflight>
