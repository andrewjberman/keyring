# Deploy Completion Record
**Date opened:** 2026-09-25T19:27:14.559322+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260928T140421Z -- gate: external / leg N1 needs the daily-runner host (the only principal the firm roles trust); host i-02448edb624a7a7cf stopped Fri evening; interim: simulate-principal-policy COT->opal-data-bd implicitDeny, 49F->opal-data-cot implicitDeny, positive controls allowed (held since 2026-09-25T19:44:40.034307+00:00)
**Deploy:** R4 rows 2+4b: apply the directory root -- 3 firm holdings principals, the dispatch function, the holdings slot retargeted (DISABLED); CTO half @6c5c27a666, COO half @885ae2f3d6
**Authored by:** 2.0.0_SA_COO~M
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | re-plan at apply time | Plan 11 add / 2 change / 0 destroy, same addresses, irpt_directory_refresh absent | terraform plan -out=r4.tfplan at CLOUD 19:2xZ: Plan: 11 to add, 2 to change, 0 to destroy; the same 13 addresses as the packet @885ae2f3d6; irpt_directory_refresh 0 change lines (15 mentions, all state refreshes) | CLOSED 20260925T192928Z |
| AP1 | activation | safe-apply of the saved plan | Apply complete: 11 added, 2 changed, 0 destroyed | safe-apply (terraform 1.14.5 = the state's version) of r4.tfplan: 10 of 11 created + 2 modified, then IAM refused the 3 firm policies (MalformedPolicyDocument: ClassifierScan had no Resource; the grants record's dynamodb_scan was empty, fixed @674a9c02f6); finished IN-SESSION by r4b.tfplan: Apply complete 3 added, 0 changed, 0 destroyed; a fresh plan reads No changes. Name disclosed vs packet: the dispatch inline policy is irpt-holdings-refresh-policy (naming gate, @89e0565411) | CLOSED 20260925T194220Z |
| V1 | verify | read-back | schedule DISABLED with the new target; each inline policy == plan JSON; function CodeSha256 == artifact sha | boto3 read-back: irpt-holdings-snapshot State DISABLED, cron(15 10 ? * MON-FRI *) America/New_York, target irpt-holdings-refresh-lambda; irpt-holdings-refresh-lambda CodeSha256 53bj8Qb6ZAl3XxbP5iQHf0sZPEp88NCKb/A1NRHTn6g= == artifact; get-role-policy == planned JSON for irpt-{49f,inf,cot}-holdings-policy and irpt-holdings-refresh-policy (4 of 4 True) | CLOSED 20260925T194310Z |
| N1 | verify | negative arm exercised as the principals | COT principal GetObject on opal-data-bd refused AND 49F principal GetObject on opal-data-cot refused | 2026-09-28T13:5xZ SSM da369659-c8ab-4fa3-8ddb-fa2224d8ff35 on the mdpf-daily-runner host (i-02448edb624a7a7cf), run as each firm principal via r4_monday_negative_arm.py: irpt-cot-holdings-role on opal-data-bd REFUSED; irpt-49f-holdings-role on opal-data-cot REFUSED; positive controls irpt-cot-holdings-role on opal-data-cot ALLOWED and irpt-49f-holdings-role on opal-data-bd ALLOWED; 4 of 4 match (status Success). Read-only GetObject to /dev/null. CTO 102342 cleared N1 before the purge CLOSE. | CLOSED 20260928T135856Z |

## Log

- 20260925T192714Z OPENED by 2.0.0_SA_COO~M with 4 leg(s)
- 20260925T192928Z LEG P1 closed: terraform plan -out=r4.tfplan at CLOUD 19:2xZ: Plan: 11 to add, 2 to change, 0 to destroy; the same 13 addresses as the 
- 20260925T194220Z LEG AP1 closed: safe-apply (terraform 1.14.5 = the state's version) of r4.tfplan: 10 of 11 created + 2 modified, then IAM refused the 3 
- 20260925T194310Z LEG V1 closed: boto3 read-back: irpt-holdings-snapshot State DISABLED, cron(15 10 ? * MON-FRI *) America/New_York, target irpt-holdings
- 20260925T194440Z HELD-SOVEREIGN-GATED gate=external/leg N1 needs the daily-runner host (the only principal the firm roles trust); ho
- 20260928T135856Z LEG N1 closed: 2026-09-28T13:5xZ SSM da369659-c8ab-4fa3-8ddb-fa2224d8ff35 on the mdpf-daily-runner host (i-02448edb624a7a7cf), run as e
- 20260928T140421Z CLOSED -- all 4 legs proven
