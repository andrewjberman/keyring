# Deploy Completion Record
**Date opened:** 2026-09-24T08:21:20.106620+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260924T083014Z
**Deploy:** AMGT crosswalk/v1/2026-09-24.json RESTORE to the signed bytes after the 08:02:55Z induction fire replaced it (523207 b, sha 9bd953b9, MEASURED 194 -> 231910 b, records 116). Rollback leg of the EXISTING never-widen pair COO 4c7d0b2e7c / CTO 429efcdf30; no new pair. R-37.
**Authored by:** 1.0.0_SA_CTO~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R1 | verify | served object restored | head-object size 523207 AND document-sha256 9bd953b9 | 3.0.0_SA_CVO~Z 08:2xZ, THREE identifiers all MATCH: size 523207, ETag 2c0ff894a1b0a3ac4dd20ca45811b76c, sha256 9bd953b9c06f7382... of the GET body; LastModified 2026-09-24T08:22:33Z so the copy landed. AND that seat VALIDATED THE CRITERION BEFORE USING IT -- it read the ETag off signed VersionId K1qTvwqiuo3jNvF_bwC94m1P0J5vHtwS directly and got 2c0ff894..., so matching it means matching the SIGNED BYTES rather than matching a number in a CTO message. | CLOSED 20260924T082949Z |
| R2 | verify | served identity restored | direct invoke ASML_US_Equity MEASURED/absent/SERVED and AAPL_US_Equity derived 10 SERVED | 3.0.0_SA_CVO~Z direct invokes on the deployed opal-amgt-scoped-api: ASML_US_Equity identity_status MEASURED basis absent peer_read SERVED read_completed true; AAPL_US_Equity MEASURED basis derived member_count 10 SERVED. ALL THREE read crosswalk_vintage 2026-09-24 from the restored object, which is what proves they are not serving a cached or older pool -- the thing size and ETag alone cannot tell you. DISCRIMINATING FIELD is identity_status, not member_count. Function unchanged: CodeSha256 DEQQiCH+UoUMd7EZSQA5RTsILDY5+ubb9Y3gVLE5elU=, so the restore moved an S3 object and no code. | CLOSED 20260924T082949Z |
| R3 | verify | untouched control holds | direct invoke CAT_US_Equity MEASURED derived 12 | CAT_US_Equity identity_status MEASURED, basis derived, member_count 12, peer_read SERVED -- untouched throughout, as the control predicted. PLUS an arm this seat's acceptance FAILED TO NAME and 3.0.0_SA_CVO~Z ran anyway: NOSUCHKEY_ZZ_Equity returns UNRESOLVED with peer_read {} and member_count null, proving the instrument CAN still produce UNRESOLVED on this exact path. Without it the three MEASUREDs were not discriminating -- ASML's member_count 0 would look identical under a broken resolver. | CLOSED 20260924T082949Z |

## Log

- 20260924T082120Z OPENED by 1.0.0_SA_CTO~Z with 3 leg(s)
- 20260924T082949Z LEG R1 closed: 3.0.0_SA_CVO~Z 08:2xZ, THREE identifiers all MATCH: size 523207, ETag 2c0ff894a1b0a3ac4dd20ca45811b76c, sha256 9bd953b9c
- 20260924T082949Z LEG R2 closed: 3.0.0_SA_CVO~Z direct invokes on the deployed opal-amgt-scoped-api: ASML_US_Equity identity_status MEASURED basis absent
- 20260924T082949Z LEG R3 closed: CAT_US_Equity identity_status MEASURED, basis derived, member_count 12, peer_read SERVED -- untouched throughout, as the
- 20260924T083014Z CLOSED -- all 3 legs proven
