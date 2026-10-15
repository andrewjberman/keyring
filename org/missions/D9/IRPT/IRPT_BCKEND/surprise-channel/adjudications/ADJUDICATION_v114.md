# IRPT_BCKEND: CVO adjudication, round 2 (workstream ~PC, the 49 Financial refusal and the Cottonwood validator, both READ)

<sweep_watermark>2026-10-15T12:11Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T12:11Z, on msg 8261 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_2_PC_DRAIN_END_20261015.md` @f1e214af1c). ~PC round 1 was already compiled and slugged as ADJUDICATION_v113 @39208a6c27. Two orders, IB-pr-570 (49 Financial's refusal) and IB-pr-571 (the Cottonwood validator offline), both risk SERVED, read-only, complete, merges @a9eb88ed54 and @61fd06850f (worker records, criteria output, proof instances and the channel only). Re-run here at HEAD: IB210-1-AC1..AC3 and IB210-2-AC1..AC3, 6 of 6 PASS (exit 0 each). `round-close-check --round 2 --workstream "~PC"`: orders=2, proofs 2 of 2 ok, verdict=MAY-CLOSE.

**(1) The two issuer defects are fixed, and the fixed check can still fail.** The grant widening and the check fix are one amendment, f9afa77c0a (W414-S1, W414-S2). The fix adds to `p210_cells.py` v2 a precondition that `offline_run.performed` is true and `source_rows.count` is at least 1. Negative controls, run here on scratch copies of the record with the check re-pointed at them: `performed=false` gives AC1 FAIL and AC2 FAIL; `source_rows.count=0` gives AC1 FAIL and AC2 FAIL; outcome `error` with the cause marked `inferred` (the W414-S2 shape) gives AC1 FAIL ("outcome must be refused or accepted") and AC2 FAIL. The real record passes all three. So no criterion was weakened, and the branch that let a record pass without a run is closed.

**(2) Cottonwood's cause is MEASURED, confirmed from the record.** `IB210-2_cot_validator_read.json` has `offline_run.performed` true and `outcome` refused, writes 0. `failing_condition.claim` is `measured`, at site `holdings_snapshot.py:403`. Read here, lines 398-403 raise when a frame is not unique, lacks a required column, or is empty. The record's notes give 2 source rows on the candidate date 2026-10-13, all four COT numeric facts null on both, and 3 distinct dates in all. After the no-position filter the custody frame had 0 rows and the custody refusal fired. (`source_rows.count`=2 counts the candidate date's rows, not all dates; the field name is ambiguous, the notes are not.) One finding the packet does not headline: the worker's read-only cross-check has `cot_screen_accounts` refusing 138 of 1,001 source accounts, 136 for this same custody reason. The empty-frame drop is a class, and this account is the one of them that was in the served snapshot.

**(3) 49 Financial, and the owner.** The lag was counted here with `lib/trading_calendar.py`. Served 2026-10-12, T-1 is `prev_trading_day(2026-10-15)` = 2026-10-14, and the trading days after served through T-1 are 2026-10-13 and 2026-10-14: **2 trading days behind**, matching the record (`trading_days_behind` 2). Its cause stays `inferred`: the refused account is ACTIVE in the directory and the omitting filter is unread. IB-pr-573 (~PE) reads it.

S192 now has ONE owner. Row `D2-S193` (11:28:30Z) names `2.0.0_SA_COO~P2` as the one disarm owner of S158 and S192, replacing the disjunction v113 flagged. But the disjunction **came back on newer rows**: `D2-W413-S1` (11:36Z, ARMED, the 49F account) and `D2-S194` (11:54Z, ARMED, this round's dispositions) both carry "1.0.0_SA_CTO~DELL2 (the publish guard's owner decides) or whoever accepts the lost account(s)". S194's own world_is also says W413-S1 is "owner me", contradicting the row's field. The hazard is carried; the owner field on W413-S1 and S194 should read `2.0.0_SA_COO~P2`, as S193 rules.

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S22",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T12:11:00Z",
  "one_line": "Round 2 ~PC. Cottonwood's validator cause is MEASURED: the account's source rows are no-position rows only, so the custody frame is empty after the screen's filter and holdings_snapshot.py:403 refuses (record and code read here); the screen drops 136 of 1,001 source accounts for this same reason. 49 Financial is 2 trading days behind (counted here: 10-13, 10-14), its account is ACTIVE, cause inferred, IB-pr-573 next. 6 of 6 criteria PASS re-run. Fixed check proven able to fail (performed=false, count=0, outcome=error each FAIL). S193 names ONE owner (~P2) for S158/S192, but W413-S1 and S194 reintroduce the 'CTO or whoever' owner. Dismissed (6): D2-W414-S1 (BLOCKING, INERT; grant widened), D2-W414-S2 (check branch fixed, negative control here), D2-W414-S3, -S4, D2-W413-S2 (readings), D2-S193 (owner ruling recorded). Held: D2-S158, D2-S192, D2-S194, D2-W413-S1.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W414-S1",
   "IRPT_BCKEND-D2-W414-S2",
   "IRPT_BCKEND-D2-W414-S3",
   "IRPT_BCKEND-D2-W414-S4",
   "IRPT_BCKEND-D2-W413-S2",
   "IRPT_BCKEND-D2-S193"
  ],
  "spec_asserts": "A value must carry its claim (CLAUDE.md section 4); an issuer's check repair must not weaken a criterion and must be shown able to fail; an ARMED hazard disarms via its row's one disarm_owner (section 2); stale is counted in trading days (section 5).",
  "world_is": "Cottonwood (4 trading days behind) is blocked by one account whose source rows carry no position: a real closure the directory lacks or a stale source, the choice of remedy the CTO's. 49 Financial (2 behind) is blocked by one ACTIVE account dropped by an unread filter. The owner of these hazards is ~P2 by S193; two newer rows still name the disjunction.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T12:0xZ of the invocations in IB-pr-570 and IB-pr-571: IB210-1-AC1..3, IB210-2-AC1..3 PASS, exit 0 each",
    "python .tools/round-close-check.py --project IRPT_BCKEND --round 2 --workstream ~PC: orders=2 proof_ok=2 judgment=0 verdict=MAY-CLOSE",
    "git show f9afa77c0a -- checks/r210/p210_cells.py: two added fail() preconditions (performed true; source_rows.count >= 1)",
    "negative controls (scratch records, check re-pointed): performed=false AC1 FAIL AC2 FAIL; count=0 AC1 FAIL AC2 FAIL; outcome=error with claim inferred AC1 FAIL AC2 FAIL",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~414/IB210-2_cot_validator_read.json: offline_run performed true outcome refused; failing_condition claim measured, site holdings_snapshot.py:403; notes: 138 of 1001 refused, 136 custody",
    "data/assets/scripts/gold/investor_reporting/holdings_snapshot.py:398-403",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~413/IB210-1_49f_refusal_read.json: served 2026-10-12, t_minus_1 2026-10-14, trading_days_behind 2, cause claim inferred",
    "lib/trading_calendar.py: prev_trading_day(2026-10-15)=2026-10-14; trading days after 2026-10-12 through 2026-10-14: 10-13, 10-14",
    "investigation rows D2-S158, D2-S192, D2-S193 (owner ~P2), D2-S194 and D2-W413-S1 (disjunctive owner), D2-W413-S2, D2-W414-S1..S4",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_2_PC_DRAIN_END_20261015.md @f1e214af1c (msg 8261)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Two issuer defects fixed and the fix shown able to fail, three readings, and the owner ruling. The two firms' refusals stay held; two rows need their owner field aligned to S193."
 }
]
```
