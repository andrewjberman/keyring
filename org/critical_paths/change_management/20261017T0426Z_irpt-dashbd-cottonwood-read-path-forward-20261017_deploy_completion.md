# Deploy Completion Record
**Date opened:** 2026-10-17T04:26:16.992010+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD TO-DB-b-323 (C4 of the Cottonwood Performance read path, round 150): ONE build of the cot and read function-map entries, ONE safe-apply of the new root reporting-read-iso (5 add), direct probes of the new function incl. a forged-forward event, ONE safe-apply of reporting-read (1 add, 1 change), probes through the live 49 Financial function, receipt. Gate 0(c) per the issuer's ruling (msg 10272): the open ledger irpt-bckend-serve-path-hops-3-4a-report-route-export-bundle-20261017 names the read function but its read-function legs L2 and L3 are closed and its one open leg L7 is the export-role statement: another surface for this order.
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | function-map artifact_sha256 updates for the two entries plus this ledger sentinel and the receipt, committed with explicit paths | commit ids recorded |  | OPEN |
| L2 | s3-prefix | the cot artifact key (a NEW key) and a NEW VERSION of the 49 Financial read artifact key, each built == landed == the C3 record hash | new VersionIds, landed sha256 equal |  | OPEN |
| L3 | tf-lambda | ONE safe-apply of reporting-read-iso (5 add 0 change 0 destroy) and ONE safe-apply of reporting-read (1 add 1 change 0 destroy), each with a clean re-plan | plan counts, naming gate, replan No changes |  | OPEN |
| L4 | verify | the eight probes by label, the three iam simulations, the forged forward refused before Act 4 | probe table in the record |  | OPEN |
| L5 | verify | the after-read and the receipt written; counts equal before and after | record and criteria |  | OPEN |

## Log

- 20261017T042616Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
