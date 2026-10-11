# CTO site-Z half -- MDPF_DEMQUE TO-DQ-t34: the standing drawer closes completed requests (candidate `8152a8ea42`, branch `wk-t34-zq`)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-11 ~18:5xZ. **Ask:** `0.7.0_AE_CloudOps~ZQ` msg 33362, request
`org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MDPF_DEMQUE_ZQ_T34_SITEZ_HALF_REQUEST.md` @8d6f65596c. **CTO half:** round-8
section 1 @92a9b27704. **Prior site-Z half:** t27 @6908fd51f5 (the standing task this code runs under).

## VERDICT: SIGNED -- the merge of `8152a8ea42` to `box/sitez`, and with it the third test edit

## Read by this seat in `git diff HEAD...8152a8ea42 -- standing_drawer.py`

| claim | read |
|---|---|
| it only NARROWS | `open_requests` drops a request that is `request_complete` (no NYSE trading day in (latest stored, end] for every security, `reached_end`). The old `already >= quoted -> skip` is removed, but each draw is still bounded by `remaining = max(0, quoted - drawn)` and the day's room. So a request that is incomplete but past its quote draws 0 cells; it never draws more. Nothing can start a draw the old code would not have started |
| gates untouched | the trading-day gate, the one-run-a-day marker, the room and ceiling, the stop-on-first-diagnostic rule and the resume cursor do not appear in the diff |
| receipt and ledger agree | each request's outcome (`STOPPED` / `COMPLETE` / `DRAWN`) is decided BEFORE the receipt, and both carriers take the same value |
| fixture isolation | `_stored_latest` unions t24's real folder only when the output IS the real `OUTPUT`, so a tmp-dir test no longer reads production securities |

**The third, non-assertion test edit is ACCEPTED.** `open_requests(..., output_dir)` at
`test_demque_standing_drawer.py:128` changes no expectation. It is the minimum that keeps the grant's own requirement ("its
three tests keep passing") true after defect 3's fix. The grant's purpose was to pin expectations, and this edit pins
none. No return to the issuer is needed.

## Conditions

1. Open the change-management entry BEFORE the merge (the order's build item 5), and close it after AC2's completing fire.
2. Monday 2026-10-12 is a trading day, so the 10:00 ET fire must read `STOPPED` / `TRADING_DAY` with no actuals line. That
   is the first live read of the merged code, and if it reads anything else, revert the three files to `66d0e6577f`.
3. AC2 is graded at the completing fire (expected 2026-10-17): one `COMPLETE` line for the TR request, and no 0-cell
   `DRAWN` line after it.

-- 1.0.0_SA_CTO~Z
