# Deploy Completion Record
**Date opened:** 2026-10-12T01:26:59.981076+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-ap-11: OG-fd-1's per-family DLQ drain on the SCHWAB converter ONLY -- PARTIAL ROLL-OUT. After this deploy only the schwab sweep is per-family; the etf, blackdiamond, orion and eclipse sweeps STILL DRAIN THE WHOLE SHARED QUEUE until their own signed pairs land (CTO half @aafc1640e8). Row Z-S91 stays open until every sweeping family is per-family.
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | box/sitez commit moving local.silver_build_commit.schwab in infra/aws/terraform/opal-assets/silver.tf plus the lambda-source-map.json schwab entry | commit hash |  | OPEN |
| L2 | activation | terraform apply via .tools/safe-apply.sh -target the one schwab function: code fields plus the single OPAL_BUILD_COMMIT env value, 1 resource changed and no other row | saved-plan summary plus apply result |  | OPEN |
| L3 | verify | live read-back of opal-assets-silver-schwab: CodeSha256 equals the recorded build and differs from the prior, State Active, LastUpdateStatus Successful | get-function-configuration output |  | OPEN |

## Log

- 20261012T012659Z OPENED by 0.7.0_AE_CloudOps~Z with 3 leg(s)
