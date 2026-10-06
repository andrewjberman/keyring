# Deploy Completion Record
**Date opened:** 2026-10-06T19:58:43.869104+00:00
**Status:** OPEN
**Deploy:** ETFS_RIVALS pk-1 + al-1: five rivalfunds Lambdas at pin CLOUD 92cf1f322b (plan 0/5/0), no republish; ADDENDUM 1 census after the 2026-10-07 07:00 ET vehicle run closes the entry
**Authored by:** 2.0.0_SA_COO~RV
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 20.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| N1 | activation | safe-apply C:/tmp/rv_apply13.tfplan from C:/tmp/rv-r8 @92cf1f322b (5 code hashes) | apply output: 0 added, 5 changed, 0 destroyed | 19:59:55-20:02:57Z: HALT_ACK=1 bash .tools/safe-apply.sh -chdir=infra/aws/terraform/etfs-rivalfunds apply C:/tmp/rv_apply13.tfplan from C:/tmp/rv-r8 @92cf1f322b: Apply complete! Resources: 0 added, 5 changed, 0 destroyed | CLOSED 20261006T200417Z |
| N1v | verify | 5 live CodeSha256 equal the plan after-hashes (CTO condition 1) | get-function-configuration x5 | 20:0xZ: 5/5 live CodeSha256 equal the plan after-hashes (daily NLWa+glx, fetch pzoscnfB, canonical pX4xe2wJ, silver hJ/zqsdO, publish B5srwuWE), all LastUpdateStatus Successful | CLOSED 20261006T200417Z |
| S1v | verify | served 10-06 index.html byte-unchanged tonight, no republish (CTO condition 2) | head-object LastModified + ContentLength + ETag before = after | head-object platinum/page/date=2026-10-06/index.html before (19:58Z) = after (20:03Z): LastModified 2026-10-06T17:33:01Z, 1,294,421 B, ETag 8393ca308e6fd3c713309c493ccd9d26; no republish ran | CLOSED 20261006T200418Z |
| C1 | verify | ADDENDUM 1 census after the 2026-10-07 07:00 ET vehicle run, before the page is reported (CTO conditions 3-4) | every merged (CUSIP/ISIN, Bloomberg) pair with a count; Nebius the positive control; a wrong merge = rollback + one refresh |  | OPEN |

## Log

- 20261006T195843Z OPENED by 2.0.0_SA_COO~RV with 4 leg(s)
- 20261006T200417Z LEG N1 closed: 19:59:55-20:02:57Z: HALT_ACK=1 bash .tools/safe-apply.sh -chdir=infra/aws/terraform/etfs-rivalfunds apply C:/tmp/rv_appl
- 20261006T200417Z LEG N1v closed: 20:0xZ: 5/5 live CodeSha256 equal the plan after-hashes (daily NLWa+glx, fetch pzoscnfB, canonical pX4xe2wJ, silver hJ/z
- 20261006T200418Z LEG S1v closed: head-object platinum/page/date=2026-10-06/index.html before (19:58Z) = after (20:03Z): LastModified 2026-10-06T17:33:01Z
