# MDPF_DEMQUE -- round 7 L8/L9 adjudication

<sweep_watermark>2026-10-11T04:15Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T04:15:00Z. L8 packet: 2.0.0_SA_COO~Q1 msg 3463, org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/2.0.0_SA_COO~Q1/ROUND7_REAL_RUN.md @a7bfc074a7. 3 of 3 complete, MAY-CLOSE. 7 investigation rows plus this seat's D1-C-S17: Z-W1-S4 and D1-W19-S2 dismissed; D1-W19-S1, D1-S5, D1-S6, D1-S7, D1-S8 and this seat's D1-C-S17 graduated INERT to `remediations/REMEDIATION_v6.md`. REMEDIATION_v5 D1-W17-S1 and D1-S4 REMEDIATED.

**L9:** every mechanical criterion re-runs green on this seat's run. FWD-3 drew on a non-trading day at the measured ceiling; its next-morning production arm reads on 2026-10-12. Served TR is 109 of 141: C-PRICES (Andrew-direct v0.5, every price table) is short 32 symbols until they are re-written (D1-S8). No FWD graded this round reads those 32.

```json
[
  {
    "id": "MDPF_DEMQUE-D1-C-S14",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T04:15:00Z",
    "one_line": "Round 7 L9: no judgment owed; 3 of 3 complete, proof_ok 3, MAY-CLOSE (this seat's round-close-check at origin/CLOUD 2260a375e1). This seat re-ran all six criteria and the carried served read: NTD-OK, NTDQ-OK (finish 2026-10-17; 2026-10-09 allowance 0; 2026-10-10 allowance 5858; ceiling measured), QALLT-OK, QALL-OK 6 of 6, BKF-OK (8 passed), DRAW-OK 5858 of 5858, SERVED-TR-OK. Calendar per lib/trading_calendar.py (NYSE/pandas_market_calendars): 2026-10-09 Fri trading, 2026-10-10 Sat NON-trading, 2026-10-12 Mon trading, 2026-10-17 Sat NON-trading. Own read of the t24 artifacts: history-2026-10-10.parquet 2929 rows (KO 1260, JNJ 1260, T 409; 2021-10-01..2026-10-08), 5858 non-null cells over the two fields; receipt outcome DRAWN, stop_reason null, 38 chunk attempts with 0 diagnostics; run.started.json day 2026-10-10. BBG_ACTUALS.jsonl line 4 reads the same 5858 DRAWN. Own S3 read of s3://opal-data-assets/yahoo/global/silver/price_history: 141 prices.parquet listed = 141 index rows; 109 carry 7 columns (all last-modified 2026-10-10, 0 of 109 with no total_return), 32 carry the original 3 (all last-modified 2026-10-09). FWD-3: the backfill drew only on a non-trading day at the measured ceiling and a trading day quotes 0, but the ACCEPT's next-morning production read is Monday 2026-10-12, not yet readable; FWD-3 is not graded REALIZED this round. REMEDIATION_v5 D1-W17-S1 and D1-S4 are REMEDIATED.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence.",
    "world_is": "Round 7 L9: no judgment owed; 3 of 3 complete, proof_ok 3, MAY-CLOSE (this seat's round-close-check at origin/CLOUD 2260a375e1). This seat re-ran all six criteria and the carried served read: NTD-OK, NTDQ-OK (finish 2026-10-17; 2026-10-09 allowance 0; 2026-10-10 allowance 5858; ceiling measured), QALLT-OK, QALL-OK 6 of 6, BKF-OK (8 passed), DRAW-OK 5858 of 5858, SERVED-TR-OK. Calendar per lib/trading_calendar.py (NYSE/pandas_market_calendars): 2026-10-09 Fri trading, 2026-10-10 Sat NON-trading, 2026-10-12 Mon trading, 2026-10-17 Sat NON-trading. Own read of the t24 artifacts: history-2026-10-10.parquet 2929 rows (KO 1260, JNJ 1260, T 409; 2021-10-01..2026-10-08), 5858 non-null cells over the two fields; receipt outcome DRAWN, stop_reason null, 38 chunk attempts with 0 diagnostics; run.started.json day 2026-10-10. BBG_ACTUALS.jsonl line 4 reads the same 5858 DRAWN. Own S3 read of s3://opal-data-assets/yahoo/global/silver/price_history: 141 prices.parquet listed = 141 index rows; 109 carry 7 columns (all last-modified 2026-10-10, 0 of 109 with no total_return), 32 carry the original 3 (all last-modified 2026-10-09). FWD-3: the backfill drew only on a non-trading day at the measured ceiling and a trading day quotes 0, but the ACCEPT's next-morning production read is Monday 2026-10-12, not yet readable; FWD-3 is not graded REALIZED this round. REMEDIATION_v5 D1-W17-S1 and D1-S4 are REMEDIATED.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python .tools/round-close-check.py --project MDPF_DEMQUE --round 7 at origin/CLOUD 2260a375e1: verdict=MAY-CLOSE",
        "the seven R7_CHECKS scripts re-run by 3.0.0_SA_CVO at origin/CLOUD 2260a375e1",
        "org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MDPF_DEMQUE_ZQ_T24/{history-2026-10-10.parquet,receipt.json,run.started.json} @794152a492",
        "boto3 list/read of s3://opal-data-assets/yahoo/global/silver/price_history (3.0.0_SA_CVO, 2026-10-11T04:0xZ)",
        "org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/2.0.0_SA_COO~Q1/ROUND7_REAL_RUN.md @a7bfc074a7"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 record, not a hazard."
  },
  {
    "id": "MDPF_DEMQUE-D1-C-S15",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T04:15:00Z",
    "one_line": "Z-W1-S4 dismissed: resolved in-round by the issuer AMENDMENT @9c613dea5b, and the grant is in force at origin/CLOUD 2260a375e1. integrations/bloomberg/mcp/blp_client.py historical_data takes an opt-in diagnostics list (lines 248-255) that receives field exceptions and security errors (309-313). bbg_quote.py --record takes --outcome {DRAWN,STOPPED} and --stop-reason. test_demque_bbg_backfill.py carries test_backfill_stops_at_the_days_allowance, test_backfill_stops_on_a_vendor_limit_warning and test_trading_day_backfill_draws_nothing: 8 passed on this seat's run. The live draw read 0 diagnostics over 38 chunk attempts, and the receipt carries outcome and stop_reason.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_DEMQUE-Z-W1-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence.",
    "world_is": "Z-W1-S4 dismissed: resolved in-round by the issuer AMENDMENT @9c613dea5b, and the grant is in force at origin/CLOUD 2260a375e1. integrations/bloomberg/mcp/blp_client.py historical_data takes an opt-in diagnostics list (lines 248-255) that receives field exceptions and security errors (309-313). bbg_quote.py --record takes --outcome {DRAWN,STOPPED} and --stop-reason. test_demque_bbg_backfill.py carries test_backfill_stops_at_the_days_allowance, test_backfill_stops_on_a_vendor_limit_warning and test_trading_day_backfill_draws_nothing: 8 passed on this seat's run. The live draw read 0 diagnostics over 38 chunk attempts, and the receipt carries outcome and stop_reason.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show 9c613dea5b",
        "integrations/bloomberg/mcp/blp_client.py:248-255,309-313 at 2260a375e1",
        "python data/mdpf/scripts/demque/bbg_quote.py --help (outcome, stop-reason)",
        "pytest data/mdpf/scripts/demque/test_demque_bbg_backfill.py: 8 passed (3.0.0_SA_CVO)",
        "MDPF_DEMQUE_ZQ_T24/receipt.json attempts[*].diagnostics: 0 over 38"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Z-W1-S4 dismissed: resolved in-round by the issuer AMENDMENT @9c613dea5b, and the grant is in force at origin/CLOUD 2260a375e1. integrations/bloomberg/mcp/blp_client.py historical_data takes an opt-in diagnostics list (lines 248-255) that receives field exceptions and security errors (309-313). bbg_quote.py --record takes --outcome {DRAWN,STOPPED} and --stop-reason. test_demque_bbg_backfill.py carries test_backfill_stops_at_the_days_allowance, test_backfill_stops_on_a_vendor_limit_warning and test_trading_day_backfill_draws_nothing: 8 passed on this seat's run. The live draw read 0 diagnostics over 38 chunk attempts, and the receipt carries outcome and stop_reason."
  },
  {
    "id": "MDPF_DEMQUE-D1-C-S16",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T04:15:00Z",
    "one_line": "D1-W19-S2 dismissed: the stale schema was a worktree artifact. org/standards/PROOF_OF_SPEC.schema.json at origin/CLOUD 2260a375e1 is byte-equal to the 6b65ca5a52 content (cmp), the worker restored the original bytes and committed no schema, and round-close-check reads proof_ok 3 of 3 at that base.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_DEMQUE-D1-W19-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence.",
    "world_is": "D1-W19-S2 dismissed: the stale schema was a worktree artifact. org/standards/PROOF_OF_SPEC.schema.json at origin/CLOUD 2260a375e1 is byte-equal to the 6b65ca5a52 content (cmp), the worker restored the original bytes and committed no schema, and round-close-check reads proof_ok 3 of 3 at that base.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "cmp of git show 6b65ca5a52:org/standards/PROOF_OF_SPEC.schema.json against the file at 2260a375e1: equal",
        "round-close-check round 7: PROOFS complete=3 proof_ok=3 proof_bad=0"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W19-S2 dismissed: the stale schema was a worktree artifact. org/standards/PROOF_OF_SPEC.schema.json at origin/CLOUD 2260a375e1 is byte-equal to the 6b65ca5a52 content (cmp), the worker restored the original bytes and committed no schema, and round-close-check reads proof_ok 3 of 3 at that base."
  },
  {
    "id": "MDPF_DEMQUE-D1-C-S17",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T04:15:00Z",
    "one_line": "The 15,720-cell TR request carries two finish dates and no drawer. Its frozen quote reads 2026-10-13 (weekday rule, frozen @70379bb41d before DQ-t-22), and the rule in force quotes 2026-10-17. The only draw was the removed one-shot task, so 9,862 cells stay OPEN with nothing scheduled to draw them. This seat's quote_vs_actual.py --all at origin/CLOUD 2260a375e1 reads DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS cells_drawn 5858 of 15720, finish_date 2026-10-13 (the frozen .quote.json, finish_date_claim held), verdict OPEN. bbg_quote.py --quote reads finish 2026-10-17 for --today 2026-10-09 and 2026-10-10, and 2026-10-18 for --today 2026-10-11; that is the whole 15,720, not net of the 5,858 drawn. The t24 deploy entry's leg L4 reads 'exact task absent; daily tasks unchanged', and BBG_ACTUALS.jsonl holds one row for this request. So the 2026-10-11 non-trading allowance went unused and the frozen quote will read LATE after 2026-10-13. FWD-4 ACCEPT ('what the run then uses is close to what was quoted') is read against two quotes. Inert: research use, nothing served reads it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "FWD-4 ACCEPT: told before anything runs what it costs and the day it will finish, and what the run then uses is close to what was quoted. DQ-t-24 build 4: run bbg_backfill.py ONCE on 2026-10-10 by a one-shot task, removed after.",
    "world_is": "The 15,720-cell TR request carries two finish dates and no drawer. Its frozen quote reads 2026-10-13 (weekday rule, frozen @70379bb41d before DQ-t-22), and the rule in force quotes 2026-10-17. The only draw was the removed one-shot task, so 9,862 cells stay OPEN with nothing scheduled to draw them. This seat's quote_vs_actual.py --all at origin/CLOUD 2260a375e1 reads DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS cells_drawn 5858 of 15720, finish_date 2026-10-13 (the frozen .quote.json, finish_date_claim held), verdict OPEN. bbg_quote.py --quote reads finish 2026-10-17 for --today 2026-10-09 and 2026-10-10, and 2026-10-18 for --today 2026-10-11; that is the whole 15,720, not net of the 5,858 drawn. The t24 deploy entry's leg L4 reads 'exact task absent; daily tasks unchanged', and BBG_ACTUALS.jsonl holds one row for this request. So the 2026-10-11 non-trading allowance went unused and the frozen quote will read LATE after 2026-10-13. FWD-4 ACCEPT ('what the run then uses is close to what was quoted') is read against two quotes. Inert: research use, nothing served reads it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python data/mdpf/scripts/demque/quote_vs_actual.py --all at origin/CLOUD 2260a375e1 (3.0.0_SA_CVO)",
        "python data/mdpf/scripts/demque/bbg_quote.py --quote requests/DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS.json --today 2026-10-09|10|11 (3.0.0_SA_CVO)",
        "org/missions/D8/MDPF/MDPF_DEMQUE/requests/DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS.quote.json @70379bb41d",
        "org/critical_paths/change_management/20261009T1613Z_mdpf-demque-zq-t24_deploy_completion.md leg L4",
        "org/missions/D8/MDPF/MDPF_DEMQUE/ledger/BBG_ACTUALS.jsonl line 4"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Graduated to REMEDIATION_v6: the CTO rules which quote binds a request quoted before DQ-t-22, and whether a non-trading-day drawer is cut for standing backfills or the request closes at 5,858 cells."
  }
]
```
