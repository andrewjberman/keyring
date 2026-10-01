# Deploy Completion Record
**Date opened:** 2026-10-01T15:04:20.836733+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261001T151522Z
**Deploy:** IRPT_DASHBD round 1 DB-b-3: write the tie-out proposal into dim_return_method/method_version=1 -- flow_convention STAYS END, tieout_tolerance_proposed 0.037
**Authored by:** 0.4.0_DS_ClientPlatform~S
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| M2 | activation | dim_return_method v1 flow_convention + tieout_tolerance_proposed | the two values read back from the LANDED parquet, plus the schema_hash the type change forces | Read back from the LANDED parquet, not the producer's stdout: dim_return_method/method_version=1 holds 1 row and 18 fields; flow_convention 'END' (unchanged, as amendment 3 requires -- a convention changes only by a new method_version); tieout_tolerance_proposed 0.037; tolerance 0.001244, large_flow_share 0.002535, comparability_max_excluded_weight 0.002488 all unchanged. THE TYPE CHANGE THE ISSUER PREDICTED OCCURRED: tieout_tolerance_proposed is now double where it was null, so schema_hash moved fe0d01b511ef... -> 198109613065ed7b72afd5ff178ac31c7ace2facddf0c65e96a65acfdd42e47d and the contract is bumped to 0.2.0 (written uncommitted for the issuer, lane ANY_EXEC). NO DAY PARTITION WAS TOUCHED: --method-row-only, verified by the producer's own line and by the 559 day partitions being absent from this write set. DB-3-AC2 PASS with END recomputed on 62 of 62 gradable days. | CLOSED 20261001T151521Z |

## Log

- 20261001T150420Z OPENED by 0.4.0_DS_ClientPlatform~S with 1 leg(s)
- 20261001T151521Z LEG M2 closed: Read back from the LANDED parquet, not the producer's stdout: dim_return_method/method_version=1 holds 1 row and 18 fiel
- 20261001T151522Z CLOSED -- all 1 legs proven
