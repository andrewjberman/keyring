# TO IRPT_DASHBD.TO-DB-b-38 -- E2 (runs first): measure the lag between each trade and its lot row and set LEG_LAG_DAYS from the distribution (row W21-S5) (FWD-4)

<to_id>IRPT_DASHBD.TO-DB-b-38</to_id>
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

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 round-24 analysis @99580aac8c item E2 ("the lag between each trade and its lot row over the read window, printed as a distribution; LEG_LAG_DAYS is set from it, with the percentile it covers stated") | **Decomp cell:** `DB-b-38`
(decomposition section 25) | **outcome_ref:** FWD-4 | **depends_on:** DB-b-37 (merged @f71fd042c1).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-22`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~22/`.

**The cell (`DB-b-38`).** Round 24 set `LEG_LAG_DAYS = 3` in the producer as a bound the worker chose, not one measured (row IRPT_DASHBD-W21-S5). Measure it. Read `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~21/IDENTITY_REGRADE_E2.json` and `GAP_DIAGNOSIS_E1.json` first (round 24: the same 91 accounts over 2026-09-01..2026-10-05; 55 tie within one cent, 36 miss: ROUNDING 32 at the 0.05 tolerance, MISSING-TERM 3, OTHER 1). The producer is `data/assets/scripts/gold/irpt_reporting/account_activity_lots.py`; its sources are `s3://opal-data-assets/schwab/08335338/silver/` (`fact_trn`, `fact_rld`, `fact_uln`/`fact_ult`, `dim_position`, `dim_balance`). Round 24's re-grade helper is `deliverables/0.9.0_WK_IRPT_DASHBD~21/identity_regrade_e2.py`; copy what you need into your folder.

1. For every trade in the 91 accounts' window that should produce or relieve a lot (buys, sells, in-kind arrivals and departures),
   find its lot row (`fact_rld` for a closed lot; the open-lot tables for an opened one) and the lag in TRADING days between them
   (`lib/trading_calendar.py`). A trade with no lot row in the read window is counted separately as `unmatched`, never as a lag.
2. Write `LOT_LAG_E2.json`: `lags` `{n, percentiles: {p50, p90, p95, p99, max}, counts_by_days: {"<days>": count}}` (n = matched trades),
   `unmatched` (count, with up to 20 example keys), `leg_lag_days` (an int you choose FROM the distribution), `covered_percentile` (the
   share of lags at or under it, in percent) and `choice_rule` (the rule you used to choose it).
3. Set `LEG_LAG_DAYS` in the producer to `leg_lag_days`. Keep the producer's tests passing. Write `LOT_LAG_E2.md`, COUNTS ONLY.

<criterion id="DB25-1-AC1" cell_refs="DB-b-38"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r25/p25_windows.py" . DB25-1-AC1</invocation><expect>DB25-1-AC1 PASS</expect></criterion>
`DB25-1-AC1` -- the lag distribution printed; LEG_LAG_DAYS in the producer equals the chosen value and covers the stated percentile. Base: FAIL.

<expected_criteria>DB25-1-AC1</expected_criteria>

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
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-38.lot-lag-bound.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 25 (round 25, workstream B), cell `DB-b-38`.
<owned_cells>DB-b-38</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB25-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~22/IRPT_DASHBD.TO-DB-b-38.lot-lag-bound.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB25-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, what you changed, the numbers each criterion prints, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a constant in the round-23 producer, which serves nothing yet; no S3 write.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only, from this box; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB25-1-AC1 base FAIL (no record), dry-run at base 99580aac8c 2026-10-07 ~17:2xZ.
lane: the <paths> block IS the grant.
</preflight>
