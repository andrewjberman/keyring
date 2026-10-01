# Deploy Completion Record
**Date opened:** 2026-10-01T19:48:02.646037+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND row S259: Inflection split accounts list their positions (attributed to neither part); route irpt-holdings counts a two-view account once. Packet IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_INF_SPLIT_ACCOUNT_POSITIONS_20261001.md (blob b645c6a3fa, COO half signed) + CTO half @07e4769540 SIGNED. Rollback: route irpt-holdings to CodeSha256 TG8b/SEHCf7HpxJ+haFXsIp9/6ilbACDbP/2VpgzJtU= (LastModified 2026-10-01T06:31:21Z) by Terraform prior package; producer bundles to prior S3 VersionIds 49f e2GYGHrTdiqpnhB3glOIiJ9C0SkFRFsi (md5 a227d01c..), inf IWeTxbXSJXnYnuQcEdWexxCESqu6P.Ng (md5 476ed366..), cot gvZxPKd0ZfT8OhYzgH9nR.mab_LJ6woM (md5 bfc1d8b6..) by copy-object; no object deleted. Opened under CTO rulings batch 100 (one act, read-back within the hour; only leg S waits on the 2026-10-02 14:15Z publication).
**Authored by:** 2.0.0_SA_COO~M
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 30.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| M | git | merge coo-m-r30 (b26847ea04+07ee87653e) into CLOUD via safe-merge; tests pass on CLOUD | merge hash + test counts | safe-merge coo-m-r30 -> CLOUD b4d4548d5a (19:5xZ): 7 paths, dropped 0, foreign 0 (branch commits b26847ea04, 07ee87653e, the packet, and dda373cbd3 + its revert 1c1d2a02c2, net zero). On CLOUD after the merge: data/assets/scripts/gold/investor_reporting/tests 326 passed; infra/aws/lambda/investor-reporting/holdings/tests 165 passed (incl. test_holdings_inf + test_l0_categories 17 passed, test_aggregates 15 passed). LOCAL, not pushed (this seat never pushes). | CLOSED 20261001T195138Z |
| R | activation | route irpt-holdings by safe-apply infra/aws/terraform/investor-reporting/holdings, FIRST | plan + apply + CodeSha256 read-back + QA projection of today's publication unchanged |  | OPEN |
| P | s3-prefix | safe-deploy --mint-bundle irpt_holdings_inf (+49f, cot re-minted with the shared guard) | md5 + members-sha256 per firm; closure diff = only this change |  | OPEN |
| Q | verify | QA fire irpt-holdings-refresh-lambda {qa:true}: Inflection 91 split accounts carry positions, security rows sum to account total, reconcile accepted; 49 Financial and Cottonwood reconciles QUOTED (CTO condition 1) | SSM status + QA publication reads |  | OPEN |
| S | verify | served 2026-10-02 14:15Z publication: count of accounts in each branch (CTO condition 2) + one walked split account | served manifest + node reads |  | OPEN |

## Log

- 20261001T194802Z OPENED by 2.0.0_SA_COO~M with 5 leg(s)
- 20261001T195138Z LEG M closed: safe-merge coo-m-r30 -> CLOUD b4d4548d5a (19:5xZ): 7 paths, dropped 0, foreign 0 (branch commits b26847ea04, 07ee87653e,
