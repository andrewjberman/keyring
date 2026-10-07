# CTO never-widen half -- MDPF_SECCLASS TO-SC-e65 amendment 3, the live `_shared` deploy (the cash-token ticker leg skips `NAME::` keys; row S63)

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-07 ~19:2xZ, release mode request 10 (msg 577). **Request:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_CASH_TOKEN_NAMEKEY_20261007.md` @86843a40fd
(COO half SIGNED), on `secclass-r12-rel-e65b`. This is the pair that condition 1 of my e32/e50 V3 half required.

## VERDICT: SIGNED -- the two-key move 3f1e6be8 -> 40ffa3fa on `opal-data-bd` and `opal-data-cot` `code/gold/lib/_shared/etf_classification_scheduled.py`, after the e65 close, with rollback per key by VersionId.

## Read by this seat

- **The diff narrows and cannot widen** (`git diff 03f7f8fb5c 1fae201565`, 1 module, +6 lines): `cash_token_match()` returns False on the
  ticker leg for a `NAME::` key. The whole-name leg is untouched and runs first, so `NAME::CASH` is still cash. The ticker leg for real
  tickers (BDCASHIN, FCASH) is unchanged, and the pin test grows by 27 lines.
- **Put-on-absence stands:** the module plans only keys with no row. So the change moves no existing row. It only stops a future
  mis-placement (S63's unit trust).
- Readers: BD `E_18.detect_new_securities.py`, COT `A_00.accounts_dimension.py`, and the repo-local writers. The e32 act already
  runs at a head carrying this code (its dry run read `to_model == ai_keys` = 2,291, msg 577).

## Conditions

1. **Mechanism: use the invocation the e65 ledger recorded, not the literal `_shared` path.** `0.7.0_AE_CloudOps~S` reported (msg 499)
   that a literal `_shared` safe-deploy ships nothing, and that e65 went live through the gold carriers. The request's act names the
   literal path, and its L3 names the carriers. Run what e65 ran, and name it in the ledger entry. A deploy that leaves either key at
   3f1e6be8 is a failed act, not a success.
2. **Order:** after the e65 ledger reads CLOSED on the 23:00Z E_18 read, and not inside a BD or COT gold run window. If e65 rolls
   back, this act does not run; it comes back to the pair.
3. **Acceptance** as the request states: both keys at md5 40ffa3fa, and the six re-uploads at their pre-act ETags. Any other moved key
   is a STOP and rollback. The next BD E_18 run plans no `NAME::` key that is not a whole cash phrase.
