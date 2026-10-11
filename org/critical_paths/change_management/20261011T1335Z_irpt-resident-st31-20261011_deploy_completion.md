# Deploy Completion Record
**Date opened:** 2026-10-11T13:35:35.651940+00:00
**Status:** OPEN
**Deploy:** IRPT_YCDGEN TO-APPLY-st31: install the DEAD-LETTER release -- root 19b02b2971-st31 over the running 37210c771a-st30 on host i-0167fd745ad906a66, one restart, and read it back. ONE served change (D1): a generation job whose handler raises on its fifth receive records FAILED with code DELIVERIES_EXHAUSTED, the exception's CLASS and the receive count; no binding is added. NO removal leg: st31 stays unless V1 fails or the issuer orders X1. Artifacts PINNED by measured sha256: tar 19b02b2971-st31.tar.gz 00532ad07e3e250b4a136b32585f4244ca25c6bf7108c850dc1af600118c4b99 (1004820 bytes), installer resident_host_install_19b02b2971-st31.sh 40207530c2c2b547d4502bea56260291be2752160321ffa8dae6985e1c410c64 (8705 bytes), both EQUAL to the order's declared prefixes, measured locally before the put. GO: both never-widen halves verified AT THE BYTES by this seat -- COO packet blob 8d68f341d2dba2cb2ff13d9c9d6fc94eb0584d09 == its blob at a61d835162; CTO half NEVER_WIDEN_ST31_DEAD_LETTER_RECORD_CTO_HALF.md blob e9394cad1e == its blob at bb5f7303b7; the half's CONDITION 1 record blob b44407b758 == its blob at 5643d0e811 (CTO msg 5016); all three commits ancestors of HEAD and all files clean. CTO CONDITION 2 binds this close: the state is recorded as APPLIED, UNEXERCISED in those words.
**Authored by:** 0.7.0_AE_CloudOps~YC2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U2 | s3-prefix | put the tar as ec2/investor-reporting-ycharts/resident/irpt-resident-19b02b2971-st31.tar.gz and resident_host_install_19b02b2971-st31.sh under the same prefix in opal-313476888478-lambda-artifacts | each key 404 BEFORE the put with a positive control in the same prefix, then read each back and recompute sha256 EQUAL to the measured value above; a different sha256 is a STOP (a rebuilt tar is a new pair) |  | OPEN |
| P1 | verify | host_read.py pre_read.sh -- the read-only pre-read, expect st30 running | the output prints 'P1 STOP-READ PASS' (IRPT_ANALYSIS_READY_QUEUE_URL reads 0 three ways); on FAIL install nothing, send 2.0.0_SA_COO~G2 the output path, stop |  | OPEN |
| D2 | activation | host_read.py install_st31.sh, ONLY when irpt-generation reads 0 visible and 0 in flight -- the installer's own gate is NEVER forced | running root 19b02b2971-st31, active, 0 tracebacks; any failure takes the installer's own rollback to st30 then STOPS and reports |  | OPEN |
| V1 | verify | the install read-back, all EIGHT of the order's expectations | allow list ("andrew@opalinvest.com",); producer_for svc = YCHARTS; GENERATE_MAX_RECEIVES = 5; READ_BACK_RELEASE_VISIBILITY_S = 390; ticket_package occurrences 0; both queue binding counts 0; the running process environment count 0; root active with 0 tracebacks -- reported to 2.0.0_SA_COO~G2 as V1 closed, stating D1 as APPLIED, UNEXERCISED per CTO condition 2 |  | OPEN |

## Log

- 20261011T133535Z OPENED by 0.7.0_AE_CloudOps~YC2 with 4 leg(s)
