# Deploy Completion Record
**Date opened:** 2026-08-25T04:40:59.049746+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260825T044724Z
**Deploy:** Andrew 04:30Z posture: ad-hoc end-to-end proof run of etf-positioning-producer at as_of 2026-08-24 -- publish, then read the SERVED bytes
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| etf-positioning-producer | tf-lambda | module.etf_positioning_producer.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | AD-HOC END-TO-END PROOF per Andrew 04:30Z posture; COO~Z HOLD LIFTED 04:42Z. First invoke FAILED AccessDenied on ListObjectsV2 -- ask 1's _load_backfill_history introduced this function's first list call and the role had NO s3:ListBucket; bbg/* also does not match bbg-testpull/ so GetObject was missing too. Fixed BOTH halves in one commit @dab7ab27b0 (prefix-scoped ListBucket + GetObject on bbg-testpull/tickers/*), applied 0/1/0. Re-invoke: StatusCode 200, FunctionError null, run_class adhoc, as_of 2026-08-24, books_full 4, books_shell 0, holding_rows 187, is_cash_inferred 2, vocab_size 13. PUBLISHED. SERVED VERIFIED: 122825 -> 125915 B, etag 46c7322e9a07 -> 581c4abb3f6b, 04:45:15Z, data_as_of 2026-08-24. Ask 1 live: 179/187 holdings carry returns across 8 windows. Andrew's FXFXX ruling live: SALXX now DIVZ fixed_income 0.58 / IDVZ 0.89, was cash. ALLOCATION FAITHFUL: alloc_sum == holdings_sum to 4dp on all four books, so the sub-100 totals are the VENDOR's weights not our arithmetic. RESIDUALS NAMED: 8 holdings lack returns (identifier failures ICT/MER/RBGLD); ICT+MER = 2.69% of IDVZ counted in alloc_equity but sub_asset_class None so absent from the sector panel. run_class is adhoc -- the 13:00Z scheduled fire remains the production number per NEVER#4. | CLOSED 20260825T044724Z |

## Log

- 20260825T044059Z OPENED by 0.7.0_AE_CloudOps~Z with 1 leg(s)
- 20260825T044724Z LEG etf-positioning-producer closed: AD-HOC END-TO-END PROOF per Andrew 04:30Z posture; COO~Z HOLD LIFTED 04:42Z. First invoke FAILED AccessDenied on ListObj
- 20260825T044724Z CLOSED -- all 1 legs proven
