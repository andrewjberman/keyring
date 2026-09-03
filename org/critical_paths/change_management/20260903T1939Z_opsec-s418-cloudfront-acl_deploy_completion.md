# Deploy Completion Record
**Date opened:** 2026-09-03T19:39:15.440647+00:00
**Status:** OPEN
**Deploy:** NFRA_OPSEC202609.TO-OP-S-4-18, ACL 1 of 2 -- opal-cloudfront-protection: the two opal-blocked-ips CLOUDFRONT sets created EMPTY, their IPSetReference Block rule at the FREE priority 0, and three AWS managed rule groups ALL IN COUNT. Bot Control deliberately absent. NO existing rule's priority or action changes
**Authored by:** 0.7.0_AE_CloudOps~S
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | waf-cloudfront.tf committed under 0.7.0_AE_CloudOps~S with both roots' UNSCOPED baselines quoted BEFORE the edit | commit hash + baselines |  | OPEN |
| L2 | activation | safe-apply of portal-auth -- 2 to add (the v4 and v6 IP sets), 1 to change (the ACL, IN-PLACE), 0 to destroy, 0 forces-replacement PLAN-WIDE -- ROLLBACK: remove the four added rule blocks and the two ip_set resources and re-apply, which returns the ACL to its 2-rule shape; a web ACL REPLACEMENT would drop edge protection between destroy and create and is an immediate STOP, not a rollback | apply output + enumerated changed-resource list |  | OPEN |
| L3 | verify | S18-AC1 + S18-AC2 on this ACL -- list-ip-sets CLOUDFRONT returns the new sets where the face quotes [] as the before; get-ip-set reads Addresses [] on each; both addresses in terraform state list; and the FULL rule array pasted before and after showing RateLimitRule still 1/Block and AuthLoginRateLimit still 2/Block | pasted reads, both rule arrays |  | OPEN |
| L4 | verify | S4-AC1 -- three managed groups present each with OverrideAction Count (3 of 3 pasted) and a census showing AWSManagedRulesBotControlRuleSet count = 0 with its denominator. A group in Block is a FAIL | pasted read + census |  | OPEN |
| L5 | verify | S4-AC2 -- the soak is RUNNING and COUNTING, measured not asserted: sampled requests or a CloudWatch datapoint for at least one of the three groups, with read time and window. No traffic yet files UNCOMPUTABLE with the window, never PASS on the configuration | sampled-requests or metric read |  | OPEN |
| L6 | verify | S418-AC3 for THIS root -- UNSCOPED re-plan 0-diff after; nothing else rode; push state MEASURED | plan + ls-remote |  | OPEN |

## Log

- 20260903T193915Z OPENED by 0.7.0_AE_CloudOps~S with 6 leg(s)
