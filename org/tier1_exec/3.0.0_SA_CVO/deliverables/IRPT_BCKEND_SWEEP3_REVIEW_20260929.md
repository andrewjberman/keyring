# IRPT_BCKEND -- project sweep 3: L8 compile and L9 review (`3.0.0_SA_CVO`)

**Rule:** CTO RULING 102674 (one project sweep; at most one slug per 2 hours; sweep 2's slug went at about 12:2xZ).
**Triggers:** `2.0.0_SA_COO~M` drain-ends 102886 (~M r20) and 102947 (~M r23), and `2.0.0_SA_COO~P` drain-end 102978
(~P r20 amendment 2, r22, r23; ~E r4, r5). **Watermark:** `<sweep_watermark>2026-09-29T18:45Z</sweep_watermark>` in
both carriers: the order-set cut. The row census was taken at 19:05Z and the newest row compiled is S218 (18:05Z). The
row gate refused a 19:05Z watermark on TO-IB-pr-241 (pending, first added 18:48Z), which is outside this sweep. **Carriers:** `ADJUDICATION_v17.md` (C-S247..C-S255) and `REMEDIATION_v13.md` (7 rows), co-committed.

## Drained since sweep 2 (order status words read at HEAD)

~M r20: m20-201, m20-202, m20-203, m20-204. ~M r22: m22-221. ~M r23: m23-231. ~P: pr-201 amendment 2, pr-221, pr-231.
~E: er-401 (graded at sweep 2), er-501. All read `complete`. In flight and outside this sweep: m22-222 (Part 2 reads
the 2026-09-30 14:15Z fire) and pr-241 (the S216 diagnosis), both `pending`. No swept order carries a JUDGMENT
criterion (0 occurrences in 11 order files), so L9 has no judgment grade to give.

## Denominator

489 investigation rows; 464 named by a carrier; 25 not named; 0 unparsed JSON blocks. All 25 are compiled: 18
dismissed, 7 graduated.

## Rows

| row | disposition | basis |
|---|---|---|
| S216 (BLOCKING, ARMED) | graduated to 2.0.0_SA_COO~P, stays ARMED | this seat's live read at 19:0xZ: the bronze positions prefix ends at 2026-09-27; 09-28 and 09-29 are absent |
| S218 (BLOCKING, ARMED) | graduated to 2.0.0_SA_COO~P, stays ARMED | row evidence only; not re-read live |
| S217 (ARMED) | graduated to 2.0.0_SA_COO~M, stays ARMED | read at HEAD: the directory bundle's member list has no schwab_account_codes; directory_runner.py:121 imports it |
| S213 (ARMED) | graduated to 2.0.0_SA_COO~Y, stays ARMED | row evidence only |
| W80-S1 (ARMED) | graduated to 2.0.0_SA_COO~P, stays ARMED | the INF producer is plan-only, so nothing served carries it yet |
| S215 (carries S206) | graduated to 1.0.0_SA_CTO, INERT | the contract question is the CTO's |
| S214 (carries S212) | graduated to 2.0.0_SA_COO~P, INERT | enrichment candidate |
| S205, S209 | dismissed, disarmed | this seat's live read: the Lambda's code hash is gLRGHIyi, not a1ZUOSw5; ledger closed 969b4deffd |
| S208, W81-S1, S210 | dismissed | act 4 closed by its owner; census complete |
| S211, W81-S2, W75-S1 | dismissed, each fixed at HEAD | 4d676b93a9; TO line 53; schema line 259 |
| W43-S1, W78-S1, W74-S1 | dismissed | instrument limit or same-turn mechanical fix |
| S146, S188, S192, W65-S1 | dismissed | disposition records whose subjects are already carried |

## The real runs named in the drain-ends

R4 (the first scheduled Holdings fire): this seat read the served Inflection index and the 2026-09-28 manifest at
19:0xZ. `latest_date` is 2026-09-28 and the manifest's custody clock is 2026-09-28. The 49F and COT served indexes were
not re-read by this seat; they stand on the worker's read-back and the CRO's after-read (102840).

## What you should have asked but did not

Why Inflection's Holdings fire succeeded for 2026-09-28 while Inflection's Performance producer cannot. They read two
different position sources. The Holdings manifest names `silver/api_dims/positions_mv/snapshot_date=2026-09-29`, which
is current. The Performance producer reads `orion/inflection/silver/fact_positions/`, which stopped at 09-27 (S216).
One firm's positions reach the product through two pipes with different freshness. S216's diagnosis (pr-241) should
say whether the second pipe is needed at all, before anyone repairs it.

Two smaller notes. W78-S1 shows the naming gate grades a generated file only when it is in a diff, so a registry pin
can drift unseen between touches. S218 and S207 together mean two consecutive walk windows returned one report; a third
window before the session path is repaired spends its cap for the same result.

## Not done by this seat

0.0.0_AB_MSTR's message 102976 asks what the uncommitted edit in the removed worktree `cvo-r19-wt` was. This session
began after the removal and holds no record of it. Sweeps 1 and 2 are committed (13b9063b2e, 786f5bbcad).

-- 3.0.0_SA_CVO
