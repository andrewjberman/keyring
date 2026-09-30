# TO IRPT_DASHBD.TO-DB-b-3 -- The 49 Financial tie-out against Black Diamond's own returns already landed in bronze: the measured tolerance and the flow-timing winner

<to_id>IRPT_DASHBD.TO-DB-b-3</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.4.0_DS_ClientPlatform~S</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-09-30</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>seat</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** PRD @84cff9014b CONTRACTS C-TIEOUT, C-FLOWTIME; ADDENDUM v0.2 ruling 11 ("round 1 of
workstream B MEASURES the 49 Financial sample's agreement distribution against Black Diamond's own return ... and PROPOSES the tolerance from
it; 1.0.0_SA_CTO rules it on read"); CTO 103264 | **Decomp cell:** `DB-b-3` (decomposition section 1) | **outcome_ref:** FWD-8 |
**depends_on:** DB-b-1 (its gold and its method row)

---

## WORKER FACE

**The cell.** Measure how far Opal's daily-TWR total return (DB-b-1's gold) sits from Black Diamond's own time-weighted return for the
same accounts and periods, using ONLY the vendor responses ALREADY LANDED in bronze; propose the tie-out tolerance and pick the
flow-timing convention. LANDED RESPONSES FIRST (ISSUER AMENDMENT 1, 2026-09-30 ~19:4xZ, on Andrew's egress grant to this seat,
record `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/ANDREW_DIRECT_20260930_1855Z_EGRESS_FOR_WHATEVER_CALLS_YOU_NEED.md`
@4c4989c800, verbatim "Ok Proceed, you have egress for whatever calls you need"): measure the overlap first -- the count of
(account, period) pairs where a landed response's period lies inside the gold's history. Only if that count is below 5 may you make a
fresh Black Diamond `performancePeriod` pull, for the sample accounts only, through the existing request builder
(`infra/aws/lambda/opal-assets/opal-assets-bd49f-reporting-pull/lambda_function.py`), landing each raw response byte-for-byte under the
same bronze prefix; record `overlap_before_pull` and the number of calls in `vendor_calls`. No other vendor act is read into the grant.

**The oracle, landed.** `s3://opal-data-assets/blackdiamond/49f/bronze/reporting_performance/<pull date>/reporting_performance_<bd_internal_id>_<period end>.json`
-- pull dates 2026-07-17 (relationship 22596361, period end 2026-06-30), 2026-08-30 (13477111, 18927251, 21089351, 22596361, 23221671; end
2026-08-28), 2026-08-31 (20265531, 20277481, 20350771) and 2026-09-01 (12152081, 12152601, 12153251), each a raw `performancePeriod`
response (`infra/aws/lambda/opal-assets/opal-assets-bd49f-reporting-pull/lambda_function.py:216-266` built the request:
`accountFilters.accounts=[account_id]`, the calendar-year, trailing-12-month and YTD ranges; BD returns its own period list and ignores a
start it does not hold). Map `bd_internal_id` -> `schwab_account` through `s3://opal-data-assets/blackdiamond/49f/_ops/taxsma_roster.json`
(`accounts[]` rows: `bd_internal_id`, `schwab_account`, `status`). Read every JSON you use and list its key in the record. Where a
relationship is not in the roster, say so and skip it (denominator printed).

**What you compute, per (account, period the oracle carries).** From DB-b-1's gold rows for the account over [start, end]: the geometric
link of `total_return_daily` under the END convention as emitted, AND recomputed under START and MIDPOINT conventions from the same daily
columns (`market_value_eod`, `external_flow`, `income_received`: START = `(V_t - V_(t-1) - F_t) / (V_(t-1) + F_t)`, MIDPOINT =
`(V_t - V_(t-1) - F_t) / (V_(t-1) + F_t / 2)`), skipping NOT_MEASURABLE days with the gap stated. Record `bd_twr`, `opal_twr_start`,
`opal_twr_end`, `opal_twr_mid`, `abs_diff` (winner convention), and for every period whose `abs_diff` exceeds the proposed tolerance the
`reasons`: the days that drive it (flow timing, a missing price, an income date, a `day_quality` other than MEASURED). Summary: median,
p90, max of `abs_diff`; `per_convention_summary` for the three; `flow_convention_winner` = the convention with the lowest median (ties to
END); `proposed_tieout_tolerance` = the winner's p90 rounded up to the next 5 bp, with the sentence that defends it.

**What you write.** `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.4.0_DS_ClientPlatform~S/tieout/TIEOUT_49F_BLACKDIAMOND_R1.json` (keys:
`measured_at`, `vendor_calls` (0 unless the overlap forced a pull), `overlap_before_pull`, `oracle_keys`, `roster_key`, `periods`, `summary`, `per_convention_summary`, `flow_convention_winner`,
`proposed_tieout_tolerance`, `sentence`) and `TIEOUT_49F_BLACKDIAMOND_R1.md` (one page for the CTO's ruling: the table, the sentence, what
was NOT measured). Then write the winner and the proposal into the method: `org/standards/IRPT_DASHBD_DIM_RETURN_METHOD_CONTRACT.json`
`method_versions[0].flow_convention` and `.tieout_tolerance_proposed`, and re-emit `dim_return_method/method_version=1` with the same two
values (the ONLY gold write of this cell; re-open DB-b-1's ledger `irpt-dashbd-account-return-daily-49f-r1-20260930` is CLOSED -- open a
new one-leg entry `irpt-dashbd-method-row-tieout-r1-20260930` with `--leg "M2|activation|dim_return_method v1 flow_convention + tieout_tolerance_proposed|the two values read back"`,
close it). If the winner is not END, ALSO re-emit the gold? NO: state in the md that the served daily returns stand on END until the CTO
rules, and that a re-emit is a round-2 cell; the contract records the winner as `flow_convention_measured_winner` beside `flow_convention`
(which stays END). The check reads `flow_convention` against the record's winner ONLY when they are meant to be equal, so if the winner is
not END write `flow_convention_winner` in the record as the value you wrote to the row, and name the discrepancy in the md.

<criterion id="DB-3-AC1" cell_refs="DB-b-3"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r1/p1_3_ac1_tieout_record.py" .</invocation><expect>DB-3-AC1 PASS</expect></criterion>
`DB-3-AC1` -- the record exists, `vendor_calls` is 0 or is non-zero only beside an `overlap_before_pull` below 5, every oracle key sits under the bronze prefix and reads, >= 5 periods with the named
fields, the summary recomputes, a positive proposed tolerance and a named winner with all three conventions summarised. Base: FAIL.

<criterion id="DB-3-AC2" cell_refs="DB-b-3"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r1/p1_3_ac2_method_winner_written.py" .</invocation><expect>DB-3-AC2 PASS</expect></criterion>
`DB-3-AC2` -- the method contract's `method_versions[0]` and the served `dim_return_method` row both carry the record's winner and proposal.
Base: FAIL.

<expected_criteria>DB-3-AC1,DB-3-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **AWS writes admitted:** the one `dim_return_method/method_version=1` object, and the raw responses of a conditional pull under the
  bronze prefix above. Reads of bronze and gold only otherwise. No vendor call beyond the conditional pull (amendment 1).
- **Refusal clause.** A relationship without a roster row, a period the gold does not cover, or a JSON shape you cannot parse is a row
  and a skipped row, never a guess.

<paths>
data/assets/scripts/gold/irpt_reporting/
org/standards/IRPT_DASHBD_DIM_RETURN_METHOD_CONTRACT.json
lib/opal_naming.py
lib/trading_calendar.py
org/critical_paths/change_management/
org/critical_paths/.open_deploys/irpt-dashbd-method-row-tieout-r1-20260930.json
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r1/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 1 (round 1, workstream B), cell `DB-b-3`.
<owned_cells>DB-b-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB-3-AC1, DB-3-AC2. Instance at `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.4.0_DS_ClientPlatform~S/IRPT_DASHBD.TO-DB-b-3.tieout-black-diamond-landed-pulls.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DB-3-AC1 DB-3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** to `2.0.0_SA_COO~P` (one message, under 150 words): the commit hashes, each criterion's last line, the median/p90/max, the
winner and the proposal, and any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: a read-only measurement over landed bronze plus one gold dim row rewrite; no schedule, trigger or cron is created, read or moved (0 .tf files in the cell's paths).
comp-iam: DECLARED-NOT-APPLICABLE -- reason: the DS seat reads bronze and gold and rewrites one gold object with its own standing credentials; 0 roles, policies or grants are touched (0 .tf files in the cell's paths).
comp-blast: RUN -- one gold dim row's two fields; 0 readers today (comp-estate: 0 of 135 chains name dim_return_method).
comp-routes: DECLARED-NOT-APPLICABLE.
comp-cache: DECLARED-NOT-APPLICABLE.
comp-adversary: RUN -- DB-3-AC1 base FAIL (no record); DB-3-AC2 base FAIL (no record).
sequencing: second in 0.4.0_DS_ClientPlatform~S's queue, after DB-b-1 reports.
lane: the <paths> block IS the grant.
</preflight>
