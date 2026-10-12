# Deploy Completion Record
**Date opened:** 2026-10-12T11:09:26.152726+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-ap-10 Phase B2: the gateway release of the .pptx -> bronze market_update pair (OG-ab-2 + OG-mu-1), re-cut on the live ref 28ba9532b6 as d9f2ebded9. Both never-widen halves signed AT that sha (COO @a9472f2a8d, CTO @3bcecf1c76). ONE new .env key, no new tool, no grant act (the grant went live in OG-ap-8 @a62894577a), no object written. NFRA_MCPORTAL MP-n-1 is queued behind this ledger's close and re-cuts on the new live ref.
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | the re-cut exists at release_sha with BOTH never-widen halves signed at it, and no other gateway ledger is open in any worktree | release_sha, both half commits, and the per-worktree gateway-sentinel census with denominators |  | OPEN |
| L2 | activation | safe-ec2-deploy.sh run FROM the release worktree C:/tmp/og-rel-pptx with DEPLOY_BASE_REF=28ba9532b648061cecafe426836d3e96af4529cd and NO HALT_OVERRIDE | rc=0 and the service restarts |  | OPEN |
| L3 | verify | ap10_verify.py, written for THIS release's trigger set and run IMMEDIATELY after the deploy against the before-state read at the act | tool names UNCHANGED; .env key names +1 and the added one is exactly ADVI_MARKET_UPDATE_S3_ROOT; every pre-existing .env digest unchanged; shipped md5 equals the RELEASE blobs; fee-statement root unchanged |  | OPEN |
| L4 | verify | the SERVED read through the INSTALLED code (step 6), writing W/AP10_SERVED.json | tool_takes_extension, market_update_root_equals_address as a BOOLEAN only, bad_extension_refused on .docx before any read, objects_written 0, fee_root_unchanged |  | OPEN |
| L5 | git | the record clauses: runbook 7.2 names the new live release, and EC2_MANIFEST deployed_commit plus file_checksums from the RELEASE blobs | the commit carrying both edits, written on box/sitez not imported from the release tree |  | OPEN |
| L6 | verify | ap10.AC2 re-run at HEAD after this ledger closes | entries at HEAD, CLOSED=yes, sentinel gone, equal=yes, rb.AC2 PASS, served .pptx pair fields yes -- RESULT PASS at rc=0 |  | OPEN |

## Log

- 20261012T110926Z OPENED by 0.7.0_AE_CloudOps~Z with 6 leg(s)
