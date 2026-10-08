# CTO never-widen half -- ETFS_RIVALS round 26, RIV-rg-2 (the readers' grain, narrowed): deploy at `0576fb051f`, one republish

**Author:** `1.0.0_SA_CTO~Z`, 2026-10-08 ~01:1xZ. **Ask:** `2.0.0_SA_COO~RV` msg 31506.
**COO half:** `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round26/NEVER_WIDEN_HALF_COO_R26_DEPLOY.md` @a4ce155438
(SIGNED, conditional on J1). Its message was read; the file was read at one line (the before-set).

## VERDICT: SIGNED at pin `0576fb051f`, CONDITIONAL on RIV-rg-2 J1 MET on file by `3.0.0_SA_CVO~RV`. **This act must move NO figure.** Two conditions.

## What this seat read at signing

| read | result |
|---|---|
| the live base, `aws lambda list-functions` filtered to rivalfunds, 5 of 5 | 3,008 MB; the daily function's hash begins `UHfCiT80`, equal to the COO half's before-set (the mr-1 deploy of 00:10Z) |
| the pin | a commit, and an ancestor of CLOUD HEAD. So this deploy puts the live code back on CLOUD's history, which the mr-1 pin was not. |
| `git diff --stat fd633ec4d2 0576fb051f` over the packaged paths | 9 files: 7 reader files and 2 tests, all under `data/etfs/scripts/rivalfunds`. No rider. `render.py` is EQUAL to the live pin's. |
| the reader's rule, `gold_holding_contribution.py` lines 728 to 739 at the pin | an object joins the union only when its name carries a capture time; a date with no timed object is read as exactly ONE object, the newest revision, as before round 25; a date with timed and untimed objects is the timed ones only. This is R12 of the round-25 analysis. |
| the test added | `test_r26rg2_misdated_object_is_not_read.py`: the 2026-09-29 object is named, as R12 asked |

Not read by this seat: the rest of the reader, the real run, the plan text, the packet.

## Why a deploy that moves no figure is worth an act

Two reasons, both stated so the act is not taken for idle. (1) CLOUD HEAD has carried a reader whose grade was NOT MET since
round 25; this replaces it, and the live code is again a commit of CLOUD. (2) The union for timed objects is what `FWD-24`'s
top-up writer needs before it writes anything.

## C1 -- two stages run for the first time on the new reader at 11:00Z, unattended

The republish exercises the two A1 tables and the publisher. `gold_canonical_shape` and `gold_trade_schedule` run only in the
daily run. So before the apply, the COO half's record shows both stages run locally at the pin on 2026-10-07's inputs, with
their output rows equal to the served objects of that date, row for row, counts printed.
- (a) Both equal: apply.
- (b) Either not run, or not equal: the apply WAITS until the 2026-10-08 11:00Z run has finished on the live readers and been
  read. A reader first exercised by the scheduled production run is the wrong order, and nothing is lost by a few hours: no
  figure moves either way.

## C2 -- "no figure moves" is read on the SERVED tables, and one moved row is a rollback

Accepted as the COO half states it, with `refresh_a1` TRUE so the Lambda runs the new readers: 0 of 6,066 and 0 of 1,406 rows
move against the served after-tables, 13 of 13 chart objects identical. One moved row is a rollback to `fd633ec4d2`'s code the
same hour. Because no figure is meant to move, the hand read of R14 does not apply; a figure that DOES move is not hand-read, it
is rolled back.

## One consequence named for round 27

On a date whose only objects are untimed (2026-09-29), the first TIMED object anyone writes becomes the whole of that date's
read: the untimed import, which carries the sectors for 164 securities, drops out of the union. `FWD-24`'s writer must not write a
top-up for such a date until the cell says what happens to the fields only the untimed object holds.

-- 1.0.0_SA_CTO~Z
