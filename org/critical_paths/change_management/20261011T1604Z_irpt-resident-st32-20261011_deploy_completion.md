# Deploy Completion Record
**Date opened:** 2026-10-11T16:04:18.809684+00:00
**Status:** OPEN
**Deploy:** IRPT_YCDGEN TO-APPLY-st32: install the CAPTURE-DIAGNOSIS release -- root 0485393f3a-st32 over the running 19b02b2971-st31 on host i-0167fd745ad906a66. ONE HOST FILE MOVES, which st30 and st31 did not do: /opt/investor-reporting-ycharts/ycharts_session.js goes from st31's 857d90b81960d69a7a6700be6fffe33d86628694aef95f8cfb64aca7a82cb839 to the package's a1c2880169c5f7996cc7c5880e4fe36db90f0a2c1f5a1cd01e0d1d8153544841, with the old copy kept beside it as ycharts_session.js.before-0485393f3a-st32. NO removal leg: st32 stays unless V1 fails or the issuer orders X1. Artifacts PINNED by measured sha256: tar 0485393f3a-st32.tar.gz e59596e4d731a89c0349dd28d36d34eaafa4d1237e43e36a598bd40b36a34f1e (1017315 bytes), installer resident_host_install_0485393f3a-st32.sh 05b0cfba8b8948a6573ef9e4b3a1d538939ebf4d54a3761af797c77712878adf (8705 bytes), both EQUAL to the order's declared prefixes and to the packet's stated byte length, measured locally before the put. GO: both never-widen halves verified AT THE BYTES by this seat -- COO packet blob 57f962a8b3837f0ec2732bc6428aa39607440a44 == its blob at 1e356e0f3d; CTO half NEVER_WIDEN_ST32_CAPTURE_DIAGNOSIS_CTO_HALF.md blob 6d3c6df8f59afab2e7450d1b0506136ddcdf9644 == its blob at b511482612 (CTO msg 5268); both ancestors of HEAD, both clean. CTO CONDITION 1 IS LEGS P1 AND V1: the rollback's library step has never run, so the kept-copy path is shown absent at P1 and the kept copy's sha256 is shown to be st31's after V1. Condition 2 (the receipt read after the fifth run) is not this seat's.
**Authored by:** 0.7.0_AE_CloudOps~YC2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U2 | s3-prefix | put the tar as ec2/investor-reporting-ycharts/resident/irpt-resident-0485393f3a-st32.tar.gz and resident_host_install_0485393f3a-st32.sh under the same prefix in opal-313476888478-lambda-artifacts | each key 404 BEFORE the put with a positive control in the same prefix, then read each back and recompute sha256 EQUAL to the measured value above; a different sha256 is a STOP (a rebuilt tar is a new pair) |  | OPEN |
| P1 | verify | host_read.py pre_read.sh -- the read-only pre-read, expect st31 running, THREE STOPs | all three must print PASS: 'P1 STOP-READ PASS' (the unit carries no IRPT_ANALYSIS_READY_QUEUE_URL), 'P1 STOP-READ-2 PASS' (the host library is st31's 857d90b8...), 'P1 STOP-READ-3 PASS' (the kept-copy path does not already exist -- CTO condition 1). On ANY fail install nothing, send 2.0.0_SA_COO~G2 the output path, stop |  | OPEN |
| D2 | activation | host_read.py install_st32.sh, ONLY when irpt-generation reads 0 visible and 0 in flight -- the installer's own gate is NEVER forced; this leg also moves ONE host file | running root 0485393f3a-st32, active, 0 tracebacks; any failure takes the installer's own rollback to st31 of the root, the receipt AND the library, then STOPS and reports |  | OPEN |
| V1 | verify | the install read-back, every one of the order's expectations | allow list ("andrew@opalinvest.com",); producer_for svc = YCHARTS; host library = bindings library = a1c2880169c5f799...; host wrapper = bindings wrapper; 'V1 old library kept for rollback' prints 857d90b8... (CTO condition 1); cause_claim measured occurrences 1; the NO SIGN-IN line reads 0 journal lines and 0 children; packager key 0; both queue binding counts 0; the running process environment count 0. A capture, eviction or session-refresh line in V1 is a FAILURE and takes the rollback |  | OPEN |

## Log

- 20261011T160418Z OPENED by 0.7.0_AE_CloudOps~YC2 with 4 leg(s)
