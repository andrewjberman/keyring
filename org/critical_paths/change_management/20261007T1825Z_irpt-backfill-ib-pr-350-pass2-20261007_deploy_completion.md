# Deploy Completion Record
**Date opened:** 2026-10-07T18:25:48.324420+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261007T184235Z
**Deploy:** IB-pr-350 pass 2: back-fill covered_account_ids into ONE pre-343 receipt (49financial, EXP-e29b5415), both halves signed against packet blob 2e073c2d3e
**Authored by:** 0.7.0_AE_CloudOps~I
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | preconditions: both halves at the published HEAD naming packet blob 2e073c2d3e (COO @295835f61f, CTO @c48b2d2442, ref 84bc3c379c); CTO ADDED CONDITION bundle-set == pending-set; identity arn:aws:iam::313476888478:user/Andrew_Berman. ROLLBACK SOURCE = s3://opal-data-ycharts/firms/49financial/generations/EXP-e29b5415a06f90f943481c41a1a4821b/receipt.json?versionId=3BN57Lb6hJ7._Nn0hGZ4Yj7NEFYOV_Qa | the two halves' paths+commits, the set-equality read, and the version id | Both halves read in full at origin q/dell2/seat-work-1745/r4 @84bc3c379c and both cite packet blob 2e073c2d3e16246136183efb30a3c62e3152b5b2: COO @295835f61f, CTO @c48b2d2442. CTO ADDED CONDITION MET: bundle-derived set == pending.json account_ids set, both size 1, 0 only-in-either, derived with the freeze's own bundle.covered_account_ids_of from bundle.py sha256 09ff638dc839 (the member IB-pr-349 released); report_kind performance, not retained. Bundle integrity agrees three ways (3fdb1a1870bf...d6b0). Identity arn:aws:iam::313476888478:user/Andrew_Berman. Rollback source 3BN57Lb6hJ7._Nn0hGZ4Yj7NEFYOV_Qa read pre-write. | CLOSED 20261007T184233Z |
| L2 | activation | backfill_covered_account_ids.py --apply --bucket opal-data-ycharts on the ONE signed key; tool blob 23cea9f84a | apply output with wrote=1 denied=0, and the new object version id | Apply-time dry run re-read the signed tuple 1/1/1/0/0/1/0 denied 0, identical to the packet, BEFORE the write. Then: 'apply: listed 1; read 1 = filled 1 + unfillable 0; would_write 1; wrote 1; denied buckets 0, objects 0'. New object version Jg0xDC0pFmB8UBfEv0sl1eOQ_OrcSAqs (925 B, was 870), still SSE-KMS. ONE key written, the one both halves signed. | CLOSED 20261007T184234Z |
| L3 | verify | after-reads: the written receipt re-reads with a non-empty facts.covered_account_ids; a back-filled export is ADMITTED for an in-scope Opal principal through the DEPLOYED bytes and REFUSED for an out-of-scope one; counts unmoved | IB69-1_backfill_after_reads.json + IB69-1-AC1 last line | Receipt re-read FRESH from S3: facts.covered_account_ids is an array of 1; all other fields byte-identical (bundle_sha256, artifact.sha256, page_count 11, validation_status PASSED, job_state READY). Through the DEPLOYED bytes (entry.py sha fc241d806ecc), no token minted: IN-SCOPE principal ADMITTED (ok=True named=1 outside=0); OUT-OF-SCOPE and EMPTY-SCOPE both REFUSED on the COUNTS branch ('1 of 1 account(s) outside the viewer's current scope'), not the names-no-account branch -- the positive proof the fill took. Exactly 1 irpt_export_read_admitted line emitted with covered_account_ids_count 1. IB69-1-AC1 PASS ('OK: 1 listed, 1 written and re-read, 0 unfillable, 0 denied'), with two planted mutants fired (denied=1 and rewritten_reread_ok=0 each FAIL on their own field). Pre-write version re-read after the act and still retrievable. | CLOSED 20261007T184234Z |

## Log

- 20261007T182548Z OPENED by 0.7.0_AE_CloudOps~I with 3 leg(s)
- 20261007T184233Z LEG L1 closed: Both halves read in full at origin q/dell2/seat-work-1745/r4 @84bc3c379c and both cite packet blob 2e073c2d3e16246136183
- 20261007T184234Z LEG L2 closed: Apply-time dry run re-read the signed tuple 1/1/1/0/0/1/0 denied 0, identical to the packet, BEFORE the write. Then: 'ap
- 20261007T184234Z LEG L3 closed: Receipt re-read FRESH from S3: facts.covered_account_ids is an array of 1; all other fields byte-identical (bundle_sha25
- 20261007T184235Z CLOSED -- all 3 legs proven
