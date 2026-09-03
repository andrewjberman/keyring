# Deploy Completion Record
**Date opened:** 2026-09-03T20:19:54.636620+00:00
**Status:** OPEN
**Deploy:** NFRA_OPSEC202609.TO-OP-S-4-18, ACL 2 of 2 -- opal-gateway-waf: the two opal-blocked-ips REGIONAL sets created EMPTY and their IPSetReference Block rule at the lowest FREE priority 4 (0 is taken by a live rate rule and the issuer ruled NO renumbering). NO managed rule group is added or changed on this ACL
**Authored by:** 0.7.0_AE_CloudOps~S
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | waf.tf committed under 0.7.0_AE_CloudOps~S with this root's UNSCOPED baseline quoted BEFORE the edit | commit hash + baseline |  | OPEN |
| L2 | activation | safe-apply of opal-gateway -- 2 to add (the regional v4 and v6 sets), 1 to change (the ACL, IN-PLACE), 0 to destroy, 0 forces-replacement PLAN-WIDE -- ROLLBACK: remove the BlockedIPs rule block and the two ip_set resources and re-apply, returning the ACL to its 4-rule shape; a web ACL REPLACEMENT would drop ALB protection between destroy and create and is an immediate STOP, never a rollback | apply output + enumerated changed-resource list |  | OPEN |
| L3 | verify | S18-AC1 + S18-AC2 on this ACL -- list-ip-sets REGIONAL returns the new sets where the face quotes [] as the before; get-ip-set reads Addresses [] on each; both in terraform state list; and the FULL rule array pasted before and after showing rate-based-ip still 0/Block, ip-reputation still 1/None, known-bad-inputs still 2/Count, common-rule-set still 3/Count. THE PLAN CHURNS TWO EXISTING MANAGED-GROUP RULES AS REMOVE-AND-RE-ADD, so the POST-APPLY READ is what actually settles whether anything moved | pasted reads, both rule arrays |  | OPEN |
| L4 | verify | S4-AC1 does NOT apply to this ACL -- no managed group is added or changed here. Recorded so the leg set is not read as an omission: this root's two Count groups do not graduate and ip-reputation stays enforced, all on soak evidence that does not exist yet | statement + the unchanged read |  | OPEN |
| L5 | verify | S418-AC3 for THIS root -- baseline quoted, changed-resource list enumerated, UNSCOPED re-plan after, push state MEASURED. THE RE-PLAN IS ALSO THE EXPERIMENT the issuer asked for: whether the managed-group churn appears on a root where this face adds NO managed group | plan + ls-remote |  | OPEN |

## Log

- 20260903T201954Z OPENED by 0.7.0_AE_CloudOps~S with 5 leg(s)
