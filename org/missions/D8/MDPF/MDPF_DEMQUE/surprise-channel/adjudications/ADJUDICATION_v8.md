# MDPF_DEMQUE -- round 8 L8/L9 adjudication (dell1)

<sweep_watermark>2026-10-11T15:35Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T15:35:00Z. L8 packet: 2.0.0_SA_COO~Q1 msg 3935,
org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/2.0.0_SA_COO~Q1/ROUND8_REAL_RUN.md @1e8306f031 (blob 38d71f8844, verified).
5 of 5 orders complete, MAY-CLOSE; every criterion re-run green on this seat's session (C-S18). NOT met: D1-S8's 141 of 141 (127 served).
This seat's store read (C-S19): no served price file reaches the T-1 frontier; all end 2026-06-22/23. 11 rows swept since v7 (watermark
2026-10-11T04:15Z; 11 of 35 investigation rows after it): 4 graduated INERT, 7 dismissed; ARMED 0, the one BLOCKING row (W23-S1) resolved.
REMEDIATION_v6: 3 rows REMEDIATED (C-S26).

```json
[
  {
    "id": "MDPF_DEMQUE-D1-C-S18",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T15:35:00Z",
    "one_line": "L9 record, round 8: every criterion re-run on this seat's session at box/dell1 HEAD 14f56caa80, all green -- dq_t25_tests TQ-OK, dq_t25_quote TQQ-OK (a: tier 4 finish 2026-10-17 today 0; b: tier 1 finish 2026-10-12 today 7322; c1 null finish with a named gap), dq_t26_tests RF-OK, dq_t26_real REFRZ-OK (finish 2026-10-17, superseded 2026-10-13 kept with its reason, graded OPEN), dq_t27_tests DRW-OK, dq_t27_fire FIRE-OK (first fire 2026-10-11 drew 5858 of its 5858 day share, drawer 0.7.0_AE_CloudOps~ZQ), dq_t28_tests RDS-OK, dq_t28_stale STALE-OK (independent parquet-footer read and tool both stale 14 of 141, so 127 of 141 seven-column), dq_t29_tests FIX-OK + LAND-OK, dq_t29_land COLLECT-OK n=111. dq_t27_sched (AC2) runs at site Z only and was not re-run here. round-close-check --round 8: 5 of 5, judgment 0, MAY-CLOSE. Trading calendar: 2026-10-11 is not a trading day; T-1 is Friday 2026-10-09; Monday 2026-10-12 is a trading day. NOT met: D1-S8's 141 of 141 (127 served; D1-S9).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "L9 record, round 8: every criterion re-run on this seat's session at box/dell1 HEAD 14f56caa80, all green -- dq_t25_tests TQ-OK, dq_t25_quote TQQ-OK (a: tier 4 finish 2026-10-17 today 0; b: tier 1 finish 2026-10-12 today 7322; c1 null finish with a named gap), dq_t26_tests RF-OK, dq_t26_real REFRZ-OK (finish 2026-10-17, superseded 2026-10-13 kept with its reason, graded OPEN), dq_t27_tests DRW-OK, dq_t27_fire FIRE-OK (first fire 2026-10-11 drew 5858 of its 5858 day share, drawer 0.7.0_AE_CloudOps~ZQ), dq_t28_tests RDS-OK, dq_t28_stale STALE-OK (independent parquet-footer read and tool both stale 14 of 141, so 127 of 141 seven-column), dq_t29_tests FIX-OK + LAND-OK, dq_t29_land COLLECT-OK n=111. dq_t27_sched (AC2) runs at site Z only and was not re-run here. round-close-check --round 8: 5 of 5, judgment 0, MAY-CLOSE. Trading calendar: 2026-10-11 is not a trading day; T-1 is Friday 2026-10-09; Monday 2026-10-12 is a trading day. NOT met: D1-S8's 141 of 141 (127 served; D1-S9).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO ran the 10 scripts under org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R8_CHECKS/ at 14f56caa80: rc 0 on each, verdict lines as stated",
        "3.0.0_SA_CVO python .tools/round-close-check.py --project MDPF_DEMQUE --round 8: verdict=MAY-CLOSE",
        "3.0.0_SA_CVO lib/trading_calendar: is_trading_day(2026-10-11) False, prev_trading_day 2026-10-09"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "L9 record, round 8: every criterion re-run on this seat's session at box/dell1 HEAD 14f56caa80, all green -- dq_t25_tests TQ-OK, dq_t25_quote TQQ-OK (a: tier 4 finish 2026-10-17 today 0; b: tier 1 finish 2026-10-12 today 7322; c1 null finish with a named gap), dq_t26_tests RF-OK, dq_t26_real REFRZ-OK (finish 2026-10-17, superseded 2026-10-13 kept with its reason, graded OPEN), dq_t27_tests DRW-OK, dq_t27_fire FIRE-OK (first fire 2026-10-11 drew 5858 of its 5858 day share, drawer 0.7.0_AE_CloudOps~ZQ), dq_t28_tests RDS-OK, dq_t28_stale STALE-OK (independent parquet-footer read and tool both stale 14 of 141, so 127 of 141 seven-column), dq_t29_tests FIX-OK + LAND-OK, dq_t29_land COLLECT-OK n=111. dq_t27_sched (AC2) runs at site Z only and was not re-run here. round-close-check --round 8: 5 of 5, judgment 0, MAY-CLOSE. Trading calendar: 2026-10-11 is not a trading day; T-1 is Friday 2026-10-09; Monday 2026-10-12 is a trading day. NOT met: D1-S8's 141 of 141 (127 served; D1-S9)."
  },
  {
    "id": "MDPF_DEMQUE-D1-C-S19",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T15:35:00Z",
    "one_line": "The served price store's frontier, read by this seat: s3://opal-data-assets/yahoo/global/silver/price_history/ holds 141 prices.parquet files; 14 have 3 columns and end 2026-06-23, 96 have 7 columns and end 2026-06-22, 31 have 7 columns and end 2026-06-23. The 18 written on 2026-10-11 by the D1-S8 re-draw all end 2026-06-23, as D1-W22-S1 predicted (the redraw request is built from each file's own window). No file reaches the T-1 frontier 2026-10-09: 2026-06-23 is 76 trading days before it (lib/trading_calendar). D1-S8's close condition asks for seven columns, not the frontier, so this does not change round 8's grade; whether the store must reach the frontier is the CTO's to rule (D1-W22-S1 graduated with this read).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "The served price store's frontier, read by this seat: s3://opal-data-assets/yahoo/global/silver/price_history/ holds 141 prices.parquet files; 14 have 3 columns and end 2026-06-23, 96 have 7 columns and end 2026-06-22, 31 have 7 columns and end 2026-06-23. The 18 written on 2026-10-11 by the D1-S8 re-draw all end 2026-06-23, as D1-W22-S1 predicted (the redraw request is built from each file's own window). No file reaches the T-1 frontier 2026-10-09: 2026-06-23 is 76 trading days before it (lib/trading_calendar). D1-S8's close condition asks for seven columns, not the frontier, so this does not change round 8's grade; whether the store must reach the frontier is the CTO's to rule (D1-W22-S1 graduated with this read).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO read every prices.parquet under the address('yahoo','global','silver','price_history') prefix 2026-10-11T15:2xZ: denominator 141, max(date) and column count per file",
        "3.0.0_SA_CVO lib/trading_calendar.trading_days_between(2026-06-23, 2026-10-09): 77 dates inclusive"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The served price store's frontier, read by this seat: s3://opal-data-assets/yahoo/global/silver/price_history/ holds 141 prices.parquet files; 14 have 3 columns and end 2026-06-23, 96 have 7 columns and end 2026-06-22, 31 have 7 columns and end 2026-06-23. The 18 written on 2026-10-11 by the D1-S8 re-draw all end 2026-06-23, as D1-W22-S1 predicted (the redraw request is built from each file's own window). No file reaches the T-1 frontier 2026-10-09: 2026-06-23 is 76 trading days before it (lib/trading_calendar). D1-S8's close condition asks for seven columns, not the frontier, so this does not change round 8's grade; whether the store must reach the frontier is the CTO's to rule (D1-W22-S1 graduated with this read)."
  },
  {
    "id": "MDPF_DEMQUE-D1-C-S20",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T15:35:00Z",
    "one_line": "D1-W22-S1 graduated INERT to REMEDIATION_v7 (owner 1.0.0_SA_CTO~DELL1): its question is now answered by C-S19 -- the re-draw kept each file's own window, so the 18 rewritten files end 2026-06-23 like the rest of the store; whether the price store must reach the frontier is a scope ruling.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_DEMQUE-D1-W22-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W22-S1 graduated INERT to REMEDIATION_v7 (owner 1.0.0_SA_CTO~DELL1): its question is now answered by C-S19 -- the re-draw kept each file's own window, so the 18 rewritten files end 2026-06-23 like the rest of the store; whether the price store must reach the frontier is a scope ruling.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_DEMQUE-D1-W22-S1",
        "adjudication row MDPF_DEMQUE-D1-C-S19"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Graduated to remediations/REMEDIATION_v7.md."
  },
  {
    "id": "MDPF_DEMQUE-D1-C-S21",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T15:35:00Z",
    "one_line": "D1-S9 graduated INERT to REMEDIATION_v7 (owner 1.0.0_SA_CTO~DELL1): 14 names re-drew and were REJECTED:LOW_TRADE_AGREEMENT by lock.py's 90 pct floor (AGREEMENT_FLOOR_PCT_X10 = 9, lock.py:19 and :85, both from 52b8a3cca2, 2026-10-09T03:35Z), so their three-column files stand and D1-S8 stays OPEN. The floor is not the decomposition's to change (the issuer's own words); the CTO rules whether a name that locked under an earlier rule keeps its file, re-draws on a wider band, or is served with a reason.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_DEMQUE-D1-S9"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-S9 graduated INERT to REMEDIATION_v7 (owner 1.0.0_SA_CTO~DELL1): 14 names re-drew and were REJECTED:LOW_TRADE_AGREEMENT by lock.py's 90 pct floor (AGREEMENT_FLOOR_PCT_X10 = 9, lock.py:19 and :85, both from 52b8a3cca2, 2026-10-09T03:35Z), so their three-column files stand and D1-S8 stays OPEN. The floor is not the decomposition's to change (the issuer's own words); the CTO rules whether a name that locked under an earlier rule keeps its file, re-draws on a wider band, or is served with a reason.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_DEMQUE-D1-S9",
        "3.0.0_SA_CVO dq_t28_stale.py: stale 14 of 141",
        "git blame data/mdpf/scripts/demque/lock.py:19,85 -> 52b8a3cca2"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Graduated to remediations/REMEDIATION_v7.md."
  },
  {
    "id": "MDPF_DEMQUE-D1-C-S22",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T15:35:00Z",
    "one_line": "D1-W23-S1 (BLOCKING, INERT) dismissed: resolved by the issuer's AMENDMENT @84806f465f (the legacy row keys derive from lookup('cottonwood')['key'] + suffix, not a typed firm token), and the lander landed at 2e88e042c3; this seat's dq_t29_tests prints LAND-OK and dq_t29_land COLLECT-OK n=111 land=7.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_DEMQUE-D1-W23-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W23-S1 (BLOCKING, INERT) dismissed: resolved by the issuer's AMENDMENT @84806f465f (the legacy row keys derive from lookup('cottonwood')['key'] + suffix, not a typed firm token), and the lander landed at 2e88e042c3; this seat's dq_t29_tests prints LAND-OK and dq_t29_land COLLECT-OK n=111 land=7.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_DEMQUE-D1-W23-S1",
        "commit 84806f465f",
        "commit 2e88e042c3 (land_cot.py)",
        "3.0.0_SA_CVO dq_t29_tests.py / dq_t29_land.py"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W23-S1 (BLOCKING, INERT) dismissed: resolved by the issuer's AMENDMENT @84806f465f (the legacy row keys derive from lookup('cottonwood')['key'] + suffix, not a typed firm token), and the lander landed at 2e88e042c3; this seat's dq_t29_tests prints LAND-OK and dq_t29_land COLLECT-OK n=111 land=7."
  },
  {
    "id": "MDPF_DEMQUE-D1-C-S23",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T15:35:00Z",
    "one_line": "D1-W21-S1, D1-W21-S2, D1-W21-S3 and D1-W22-S2 (INERT) dismissed. W21-S1's failing ledger-upload test is the D1-S6 defect, fixed by t-29 (this seat: FIX-OK, the folder collects 111). W21-S2 and W21-S3 record the builder's reading of arms the faces did not place (an inferred tier-1 reserve claim; a tier int outside 1-5; refreeze's allowance_gap key and collision counter); no served value depends on them. W22-S2 (upload_ledger's four-level root holds only under run_daily_draw.sh's PYTHONPATH) is a fragility with no unconditioned caller read.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_DEMQUE-D1-W21-S1",
      "MDPF_DEMQUE-D1-W21-S2",
      "MDPF_DEMQUE-D1-W21-S3",
      "MDPF_DEMQUE-D1-W22-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W21-S1, D1-W21-S2, D1-W21-S3 and D1-W22-S2 (INERT) dismissed. W21-S1's failing ledger-upload test is the D1-S6 defect, fixed by t-29 (this seat: FIX-OK, the folder collects 111). W21-S2 and W21-S3 record the builder's reading of arms the faces did not place (an inferred tier-1 reserve claim; a tier int outside 1-5; refreeze's allowance_gap key and collision counter); no served value depends on them. W22-S2 (upload_ledger's four-level root holds only under run_daily_draw.sh's PYTHONPATH) is a fragility with no unconditioned caller read.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows MDPF_DEMQUE-D1-W21-S1, S2, S3, D1-W22-S2",
        "3.0.0_SA_CVO dq_t29_tests.py FIX-OK, dq_t29_land.py COLLECT-OK n=111"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W21-S1, D1-W21-S2, D1-W21-S3 and D1-W22-S2 (INERT) dismissed. W21-S1's failing ledger-upload test is the D1-S6 defect, fixed by t-29 (this seat: FIX-OK, the folder collects 111). W21-S2 and W21-S3 record the builder's reading of arms the faces did not place (an inferred tier-1 reserve claim; a tier int outside 1-5; refreeze's allowance_gap key and collision counter); no served value depends on them. W22-S2 (upload_ledger's four-level root holds only under run_daily_draw.sh's PYTHONPATH) is a fragility with no unconditioned caller read."
  },
  {
    "id": "MDPF_DEMQUE-D1-C-S24",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T15:35:00Z",
    "one_line": "D1-S10 and Z-S1 dismissed. D1-S10 (138 of the 1,038 AMGT currency request rows are already held names) is not a defect: it is a scope question for the queue's owner, carried in the row's own notes, with no request quoted or drawn yet. Z-S1 (dq_t26_real could pass only once) is resolved: the check was hardened to restore its input from the superseded copy, and this seat's run reads REFRZ-OK.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_DEMQUE-D1-S10",
      "MDPF_DEMQUE-Z-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-S10 and Z-S1 dismissed. D1-S10 (138 of the 1,038 AMGT currency request rows are already held names) is not a defect: it is a scope question for the queue's owner, carried in the row's own notes, with no request quoted or drawn yet. Z-S1 (dq_t26_real could pass only once) is resolved: the check was hardened to restore its input from the superseded copy, and this seat's run reads REFRZ-OK.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows MDPF_DEMQUE-D1-S10, MDPF_DEMQUE-Z-S1",
        "3.0.0_SA_CVO dq_t26_real.py: REFRZ-OK"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-S10 and Z-S1 dismissed. D1-S10 (138 of the 1,038 AMGT currency request rows are already held names) is not a defect: it is a scope question for the queue's owner, carried in the row's own notes, with no request quoted or drawn yet. Z-S1 (dq_t26_real could pass only once) is resolved: the check was hardened to restore its input from the superseded copy, and this seat's run reads REFRZ-OK."
  },
  {
    "id": "MDPF_DEMQUE-D1-C-S25",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T15:35:00Z",
    "one_line": "Z-S2 and Z-S3 graduated INERT to REMEDIATION_v7 (owner 2.0.0_SA_COO~Q1). Z-S2: a mid-draw re-quote prices the FULL request from today and reads one fire day later (10-18 vs 10-17), a slip that is not a slip. Z-S3: the TR quote prices 1,310 weekdays per security while the vendor returns 1,260 trading days, so 15,720 quoted cells can never be drawn (full coverage 15,120), the request stays OPEN, and from 2026-10-18 each non-trading-day fire would append a DRAWN line with 0 cells. Both bear on REMEDIATION_v6 D1-C-S17's close condition (ON_TIME or LATE against one ruled quote).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_DEMQUE-Z-S2",
      "MDPF_DEMQUE-Z-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "Z-S2 and Z-S3 graduated INERT to REMEDIATION_v7 (owner 2.0.0_SA_COO~Q1). Z-S2: a mid-draw re-quote prices the FULL request from today and reads one fire day later (10-18 vs 10-17), a slip that is not a slip. Z-S3: the TR quote prices 1,310 weekdays per security while the vendor returns 1,260 trading days, so 15,720 quoted cells can never be drawn (full coverage 15,120), the request stays OPEN, and from 2026-10-18 each non-trading-day fire would append a DRAWN line with 0 cells. Both bear on REMEDIATION_v6 D1-C-S17's close condition (ON_TIME or LATE against one ruled quote).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows MDPF_DEMQUE-Z-S2, MDPF_DEMQUE-Z-S3",
        "3.0.0_SA_CVO dq_t26_real.py: cells_drawn 5858 of quoted 15720 at its ledger cut, verdict OPEN"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Graduated to remediations/REMEDIATION_v7.md."
  },
  {
    "id": "MDPF_DEMQUE-D1-C-S26",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T15:35:00Z",
    "one_line": "REMEDIATION_v6 clocks: D1-W19-S1, D1-S5 and D1-S7 closed REMEDIATED (remediation.state and closed only). W19-S1: dq_t25_quote arm a, a backfill with ceiling and reserve claims measured, walks non-trading days (finish 2026-10-17, today 0). S5: arm b, a tier-1 history request, reads allowance_today 7322 and finishes Monday 2026-10-12, a trading day. S7: the demque folder collects 111 with no INTERNALERROR. Kept OPEN: D1-S6 (its test passes; the next ETF-history ledger row carrying cells is not read), D1-S8 (127 of 141), D1-C-S17 (the request reads OPEN, not ON_TIME or LATE).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_DEMQUE-D1-W19-S1",
      "MDPF_DEMQUE-D1-S5",
      "MDPF_DEMQUE-D1-S7"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "REMEDIATION_v6 clocks: D1-W19-S1, D1-S5 and D1-S7 closed REMEDIATED (remediation.state and closed only). W19-S1: dq_t25_quote arm a, a backfill with ceiling and reserve claims measured, walks non-trading days (finish 2026-10-17, today 0). S5: arm b, a tier-1 history request, reads allowance_today 7322 and finishes Monday 2026-10-12, a trading day. S7: the demque folder collects 111 with no INTERNALERROR. Kept OPEN: D1-S6 (its test passes; the next ETF-history ledger row carrying cells is not read), D1-S8 (127 of 141), D1-C-S17 (the request reads OPEN, not ON_TIME or LATE).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO dq_t25_quote.py arms a and b",
        "3.0.0_SA_CVO dq_t29_land.py COLLECT-OK n=111",
        "3.0.0_SA_CVO dq_t28_stale.py stale 14 of 141"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "REMEDIATION_v6 clocks: D1-W19-S1, D1-S5 and D1-S7 closed REMEDIATED (remediation.state and closed only). W19-S1: dq_t25_quote arm a, a backfill with ceiling and reserve claims measured, walks non-trading days (finish 2026-10-17, today 0). S5: arm b, a tier-1 history request, reads allowance_today 7322 and finishes Monday 2026-10-12, a trading day. S7: the demque folder collects 111 with no INTERNALERROR. Kept OPEN: D1-S6 (its test passes; the next ETF-history ledger row carrying cells is not read), D1-S8 (127 of 141), D1-C-S17 (the request reads OPEN, not ON_TIME or LATE)."
  }
]
```
