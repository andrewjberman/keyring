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
| L1 | git | function-map artifact_sha256 updates for the two entries plus this ledger sentinel and the receipt, committed with explicit paths | commit ids recorded | function-map artifact_sha256 for both entries (DhBc5TbO..) plus this ledger sentinel and the receipt committed with explicit paths at 69532c748c | CLOSED 20261017T044604Z |
| L2 | s3-prefix | the cot artifact key (a NEW key) and a NEW VERSION of the 49 Financial read artifact key, each built == landed == the C3 record hash | new VersionIds, landed sha256 equal | cot key investor-reporting/irpt-cot-reporting-read-lambda.zip NEW (version OiXyRy.lp9Rs..) and the read key a NEW VERSION fsxJB7NLJToYf_cO..; both built == landed == DhBc5TbO.. (the C3 hash, 32 members); rollback version J9krUD0Q.. kept | CLOSED 20261017T044209Z |
| L3 | tf-lambda | ONE safe-apply of reporting-read-iso (5 add 0 change 0 destroy) and ONE safe-apply of reporting-read (1 add 1 change 0 destroy), each with a clean re-plan | plan counts, naming gate, replan No changes | reporting-read-iso plan 5 add 0 change 0 destroy, ONE safe-apply, replan No changes; reporting-read plan 1 add 1 change 0 destroy (forward policy; code and the one new env variable), ONE safe-apply, replan No changes; naming gate PASS (5 and 7 graded) | CLOSED 20261017T044209Z |
| L4 | verify | the eight probes by label, the three iam simulations, the forged forward refused before Act 4 | probe table in the record | eight probes by label: direct manifest 200 735 bytes, series gzip 2671, forged forward refused FIRM_BINDING 408 bytes (before Act 4); via 49F: control 200, cottonwood manifest 735 and series gzip 2671 equal to direct, inflection and non-internal FIRM_BINDING; simulations allowed / implicitDeny / implicitDeny; class OPAL_GLOBAL | CLOSED 20261017T044210Z |
| L5 | verify | the after-read and the receipt written; counts equal before and after | record and criteria | after-read and receipt written (COT_READ_APPLY_RECORD.json); prefixes 939, objects 1878, versions 5640 and the bucket policy hash equal before and after; ledger left OPEN for the issuer | CLOSED 20261017T044322Z |

## Log

- 20261017T042616Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
- 20261017T044209Z LEG L2 closed: cot key investor-reporting/irpt-cot-reporting-read-lambda.zip NEW (version OiXyRy.lp9Rs..) and the read key a NEW VERSIO
- 20261017T044209Z LEG L3 closed: reporting-read-iso plan 5 add 0 change 0 destroy, ONE safe-apply, replan No changes; reporting-read plan 1 add 1 change 
- 20261017T044210Z LEG L4 closed: eight probes by label: direct manifest 200 735 bytes, series gzip 2671, forged forward refused FIRM_BINDING 408 bytes (b
- 20261017T044322Z LEG L5 closed: after-read and receipt written (COT_READ_APPLY_RECORD.json); prefixes 939, objects 1878, versions 5640 and the bucket po
- 20261017T044604Z LEG L1 closed: function-map artifact_sha256 for both entries (DhBc5TbO..) plus this ledger sentinel and the receipt committed with expl
