# CTO rulings -- cluster-lead tick 12 (2026-10-11 11:57Z)

Read: `python .tools/open-calls.py list --all --cloud` at 11:57:53Z: 4 of 4 boxes, 12 OPEN (fork 2, act 10), 79 closed.
keep-driving scan=off empty_tick=off on all four. New: dell1 c290.

## dell1-20261011T113148Z-c290 -- SEV1 alert texts have not reached Andrew's phone since 2026-09-27; send ONE test text?

**Ruling: YES, one test text, on these terms.** (Rows ADVI_FIRMBKTS-D1-S15/S16/S20; AWS: "No origination identity available";
the delivery-status logging landed this morning shows 2 failures at 11:18Z and 11:20Z; every setting on the number reads
clean: ACTIVE, TOLL_FREE, TRANSACTIONAL, registration COMPLETE, not opted out, spend 50/50.)

Why this seat rules it: the SEV1 paging channel to Andrew has been dead for two weeks; the act is one diagnostic text to
Andrew's own phone over the channel he already asked for (not a new alert mechanism); its cost of being wrong is one text.

Terms:
1. Exactly ONE message, body `Opal test, no action`, from the registered toll-free number straight to Andrew's phone
   (the Pinpoint/SMS send API, not SNS), by the laptop CloudOps seat with the laptop identity, under a task order
   `2.0.0_SA_COO~B1` cuts citing this ruling (the row is dell1's project's). No other text, no retry, no loop.
2. The send's message id, status and any delivery-status log line are the record; the seat reports them through
   `0.0.0_AB_MSTR` to dell1 within the hour.
3. Outcome branches, both named now: (a) it arrives: the fault is SNS routing to the number; dell1 cuts the routing fix
   as a cell under never-widen, no cost. (b) it does not arrive, or the API refuses: the number itself is at fault; the
   next step is an AWS Support case, which is Andrew's act; the row then goes to him with the measured refusal.
4. Andrew is told in the tick report to expect one text reading `Opal test, no action`.

## Held for Andrew (unchanged): dell1 e7f2 (PROD promote), dell1 fe9b (X2 fold A/B, rec A). Reserved to Andrew: sitez 058e, 21c5,
f0d2, 8ed7, a519 (moot); dell2 01c5, 3cb1, fbb1, plus dell2 e260 (the Opal_Terminal key read).
