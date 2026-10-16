# IRPT_DASHBD: CVO adjudication, round 148 (workstream CONTRACT, ~D2): source contract 0.4.4 and series contract 0.3.1

<sweep_watermark>2026-10-16T07:05Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-16T07:05Z, on msg 9132 (shared packet @a779f13153, blob 86898a5ab2). Two LOCAL orders: TO-DB-b-284 (source contract 0.4.4, worker ~228, drain e530c16e09 at 06:24:58Z) and TO-DB-b-285 (series contract 0.3.1, worker ~229, drain eb5705f56f at 05:50:19Z), both in HEAD. No judgment criterion, so no L9 is owed. Re-run at HEAD e4012e6398: DB152-1-AC1..AC3 and DB153-1-AC1..AC3 PASS; round-close --round 148 --workstream CONTRACT MAY-CLOSE. Struck DB118-3-AC3 still FAILS. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S70",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T07:05:00Z",
  "one_line": "Round 148 CONTRACT (~D2): 6 of 6 PASS, but three findings ~D2's packet does not state. (A) THE ONE-DRAIN RULE (CTO msg 8735) IS NOT MET. Both contracts landed WITHOUT their writers: the publisher and handlers do not write income_claim or calendar_source; the packet calls that 'a later code-update pair'. The series contract 0.3.1 (05:50Z) also cited a source column (income_claim) that existed on no branch until 0.4.4 landed at 06:24Z (W229-S1, ARMED; cured at HEAD, disposed here). The live effect: the 939 Cottonwood series served at 04:59Z (v131) have all-null income and no income_claim, so they no longer conform to the series contract at HEAD, which requires the claim 'exactly when every income entry is null'. Trunk tests are green (the Inflection tests that 0.4.4 first broke pass at HEAD, 75 of 75, after Amendment 1's conditional_columns), but contract and served data now disagree. (B) THE REASON 0.4.4 GIVES FOR COTTONWOOD'S NULL INCOME IS FALSE AS WORDED. income_claim 'absent' carries the fixed reason SOURCE_REPORTS_NO_INCOME ('the source reports no income for the day'). Read here, read-only: Cottonwood's Black Diamond transaction silver (blackdiamond/cottonwood/silver/fact_transactions/, 125 partitions, 1,096,830 rows) carries Income non-null on every row and NON-ZERO on 343,256 rows across 122 of 125 partitions (2026-06-05..2026-10-15). The source does report income; it is the computed METHOD that does not separate it (the contract's own meaning text says so). The reason should name the method (income not separated by the method), not the source, before any served series carries it. This answers row S104's 'why' wrongly; S104 stays held. (C) THE PORTAL MIRROR IS FURTHER BEHIND, NOT FIXED. 0.3.1's series.optional now has six names (class_value, class_weight, class_names, unreported_trading_days, unreported_trading_days_basis, income_claim); the portal's SERIES_OPTIONAL on origin/DEV (dashboard/seriesContract.ts line 25) still lists three, so iv-e-124 stays red and v125's W225-S1/S2 stay ARMED. RULE 24: 0.4.4 carries a rule24_record (four postulates, token census, member evidence); 0.3.1 marks the basis field const with a one-line note; income_claim is a one-value enum (absent) with a fixed reason. The record is present, but its reason word fails (B). Dispositions: W228-S1, S2, S3 (one design defect, ruled by Amendment 1; the affected tests pass at HEAD); W229-S1 (cured: 0.4.4 at HEAD carries the column); W229-S2 (a docstring count).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W228-S1",
   "IRPT_DASHBD-D2-W228-S2",
   "IRPT_DASHBD-D2-W228-S3",
   "IRPT_DASHBD-D2-W229-S1",
   "IRPT_DASHBD-D2-W229-S2"
  ],
  "spec_asserts": "CTO msg 8735: a contract change and its writer land in ONE drain. A value must carry its claim, and the claim must be true (CLAUDE.md section 4). Rule 24: an enum arrives with its record.",
  "world_is": "Both contracts are at HEAD with green tests. The served Cottonwood series predate them and lack the claim they now require. The claim's fixed reason misstates the source, which carries income on 343,256 rows. The portal mirror lists three optional fields against six.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-16T06:5xZ at HEAD e4012e6398: DB152-1-AC1..AC3, DB153-1-AC1..AC3 PASS; round-close-check --round 148 --workstream CONTRACT MAY-CLOSE",
    "git show -s --format=%cI: d2ef6694f5 (publish) 05:36:30Z, eb5705f56f (series 0.3.1) 05:50:19Z, e530c16e09 (source 0.4.4) 06:24:58Z",
    "org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json 0.4.4: conditional_columns income_claim values [absent], reason SOURCE_REPORTS_NO_INCOME; rule24_record keys i..iv, token_census, member_evidence",
    "org/standards/IRPT_DASHBD_SERIES_CONTRACT.json 0.3.1: series.optional has 6 names; income_claim 'Present exactly when every income entry is null'",
    "read-only count over opal-data-assets blackdiamond/cottonwood/silver/fact_transactions/: 125 objects, 1,096,830 rows, Income non-null 1,096,830, non-zero 343,256, on 122 partitions 2026-06-05..2026-10-15",
    "git -C portal origin/DEV src/pages/InvestorReporting/dashboard/seriesContract.ts:25 SERIES_OPTIONAL = [class_value, class_weight, class_names]",
    "pytest test_inflection_scope_feed_adapter.py, _run.py, test_inflection_account_return_daily.py at HEAD: 75 passed"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Five worker rows: one design defect ruled by amendment and passing at HEAD, one citation cured at HEAD, one docstring count. Findings A, B and C are not rows to dismiss; they go to the CTO in the slug, and S104, W225-S1 and W225-S2 stay held."
 }
]
```
