# Deploy Completion Record
**Date opened:** 2026-09-10T11:35:43.683162+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260910T113732Z
**Deploy:** NFRA_OPSEC202609.TO-OP3-S-3: blocked-IP-set second-writer -- AC1-AC3 found the lifecycle ignore_changes=[addresses] remedy ALREADY COMMITTED (3758b14afc, TO-OP-S-15-19, predates this TO's cut). No Terraform edit/apply made -- nothing in this cell's scope needs changing. This entry documents the runtime survival DEMONSTRATION (S3-AC4/AC5): a test address added live, confirmed to survive an unscoped plan, then removed and confirmed reverted.
**Authored by:** 0.9.0_WK_NFRA_OPSEC202609~3
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | opal-gateway/waf.tf + portal-auth/waf-cloudfront.tf declared state, 4 IP-set resources | file:line citations, addresses=[] + lifecycle ignore_changes=[addresses] on all 4 | 4 of 4 sets confirmed: opal_blocked_ips_regional_v4 (opal-gateway/waf.tf:259-298, addresses=[] :264, lifecycle ignore_changes=[addresses] :294-296), opal_blocked_ips_regional_v6 (waf.tf:300-339, addresses=[] :305, lifecycle :335-337), opal_blocked_ips_cloudfront_v4 (portal-auth/waf-cloudfront.tf:337-385, addresses=[] :348, lifecycle :378-380), opal_blocked_ips_cloudfront_v6 (waf-cloudfront.tf:387-427ish, addresses=[] :392, lifecycle :422-424). git log confirms commit 3758b14afc (0.7.0_AE_CloudOps~T, TO-OP-S-15-19, S15-AC5) authored all four lifecycle blocks, predating this TO's 2026-09-10 cut. | CLOSED 20260910T113619Z |
| L2 | verify | aws wafv2 get-ip-set on all 4 sets, BEFORE | pasted Addresses arrays | BEFORE, all 4 live: opal-blocked-ips-regional (f073f448) Addresses:[]; opal-blocked-ips-regional-ipv6 (85f90377) Addresses:[]; opal-blocked-ips-cloudfront (b2e008a6) Addresses:[]; opal-blocked-ips-cloudfront-ipv6 (eb1a0caa) Addresses:[]. All 4 declared addresses=[] (L1) MATCH all 4 live Addresses:[] -- AGREEMENT on all four (S3-AC3). | CLOSED 20260910T113709Z |
| L3 | activation | runtime test address 192.0.2.55/32 added to opal-blocked-ips-regional via aws wafv2 update-ip-set (non-Terraform) | NextLockToken returned | aws wafv2 update-ip-set --name opal-blocked-ips-regional --scope REGIONAL --id f073f448-eb85-4d23-9306-0cadf4573331 --addresses 192.0.2.55/32 --lock-token ec5dab4c-5689-41db-83d4-3a3e7ec98be4 -> NextLockToken ef5b9f46-c03a-41f5-a08c-f08f021ce9b0. Confirmed live by get-ip-set: Addresses:["192.0.2.55/32"]. TEST-NET-1 (RFC 5737) address, not a live threat address. | CLOSED 20260910T113709Z |
| L4 | verify | terraform plan on opal-gateway after the test address | addresses attribute absent from diff, test address not proposed for removal | terraform -chdir=infra/aws/terraform/opal-gateway plan -input=false -lock=false: Plan: 0 to add, 2 to change, 0 to destroy. Both changes are description-only (+ description = ...); addresses is among the 7 unchanged-attributes-hidden on opal_blocked_ips_regional_v4 -- 192.0.2.55/32 is NOT proposed for removal. IDENTICAL diff shape to the BEFORE-test-address baseline plan. S3-AC4 CONFIRMED: the runtime-added address survives the plan. | CLOSED 20260910T113709Z |
| L5 | activation | test address removed via aws wafv2 update-ip-set (cleanup) | NextLockToken returned | aws wafv2 update-ip-set --name opal-blocked-ips-regional --scope REGIONAL --id f073f448-eb85-4d23-9306-0cadf4573331 --addresses (empty) --lock-token ef5b9f46-c03a-41f5-a08c-f08f021ce9b0 -> NextLockToken 6b49f6fb-3e87-4621-aa8b-d822b9f16891 | CLOSED 20260910T113732Z |
| L6 | verify | post-cleanup aws wafv2 get-ip-set matches S3-AC2 baseline | Addresses: [] | get-ip-set opal-blocked-ips-regional (post-cleanup): Addresses:[] -- matches S3-AC2's L2 BEFORE-state exactly (empty). S3-AC5 CONFIRMED: test address removed, set restored to baseline. | CLOSED 20260910T113732Z |

## Log

- 20260910T113543Z OPENED by 0.9.0_WK_NFRA_OPSEC202609~3 with 6 leg(s)
- 20260910T113619Z LEG L1 closed: 4 of 4 sets confirmed: opal_blocked_ips_regional_v4 (opal-gateway/waf.tf:259-298, addresses=[] :264, lifecycle ignore_ch
- 20260910T113709Z LEG L2 closed: BEFORE, all 4 live: opal-blocked-ips-regional (f073f448) Addresses:[]; opal-blocked-ips-regional-ipv6 (85f90377) Address
- 20260910T113709Z LEG L3 closed: aws wafv2 update-ip-set --name opal-blocked-ips-regional --scope REGIONAL --id f073f448-eb85-4d23-9306-0cadf4573331 --ad
- 20260910T113709Z LEG L4 closed: terraform -chdir=infra/aws/terraform/opal-gateway plan -input=false -lock=false: Plan: 0 to add, 2 to change, 0 to destr
- 20260910T113732Z LEG L5 closed: aws wafv2 update-ip-set --name opal-blocked-ips-regional --scope REGIONAL --id f073f448-eb85-4d23-9306-0cadf4573331 --ad
- 20260910T113732Z LEG L6 closed: get-ip-set opal-blocked-ips-regional (post-cleanup): Addresses:[] -- matches S3-AC2's L2 BEFORE-state exactly (empty). S
- 20260910T113732Z CLOSED -- all 6 legs proven
