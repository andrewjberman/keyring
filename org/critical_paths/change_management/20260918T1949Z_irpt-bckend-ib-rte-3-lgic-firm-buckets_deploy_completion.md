# Deploy Completion Record
**Date opened:** 2026-09-18T19:49:17.100897+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND.TO-IB-rte-3 -- opal-data-inflection and opal-data-cottonwood created, empty, fenced, ahead of D14 (Andrew-direct 2026-09-18 ~17:3xZ approved @af794c77e3; CTO Rule-30 placement, round-4 analysis s.6(b))
**Authored by:** 0.9.0_WK_IRPT_BCKEND~3
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | infra/aws/terraform/shared-infra safe-apply -- 10 new resources (2 buckets, versioning, SSE, public-access block, Deny-fence policy) | apply output + resource list |  | OPEN |
| L2 | verify | post-apply reads both buckets -- head-bucket 200, versioning Enabled, public-access block all four true, bucket policy sha256, 0 keys each | head-bucket + get-bucket-versioning + get-public-access-block + get-bucket-policy + list-objects-v2 | RECOVERED 2026-09-21 17:35:59Z-17:36:39Z by 4.0.0_SA_CRO on Andrew-direct (break-glass roles firmsep-inf/cot-bucket-recovery-role, created by Andrew in console; each role matches its firm fence role/*-inf-* / role/*-cot-*). BEFORE (read as the recovery role): each policy exempted ONLY role/*-{inf,cot}-* -- no user -- confirming the W3-S43 self-lockout. PUT: the policy the TF renders with exemptions.json's 3 users (Andrew_Berman, Andrew_Berman_Console, Opal_Terminal). AFTER, as user/Andrew_Berman with no role: get-bucket-policy rc=0 and equal to the rendered policy; head-bucket rc=0 (us-east-1); versioning Enabled; public-access-block True x4; list-objects-v2 Contents None = 0 keys each (instrument positive control: opal-data-49financial returns keys). OPEN for L1/L3/L4: a shared-infra plan should now read 0/0/0 on aws_s3_bucket_policy.lgic_firm. | CLOSED 20260921T173804Z |
| L3 | verify | re-plan on the shared-infra root reads 0/0/0 | terraform plan output |  | OPEN |
| L4 | verify | negative control from host i-02448edb624a7a7cf via read-only SSM -- host role write to inflection DENIED, 49f principal read of cottonwood DENIED, 2 of 2 | SSM command id + AccessDenied error code |  | OPEN |

## Log

- 20260918T194917Z OPENED by 0.9.0_WK_IRPT_BCKEND~3 with 4 leg(s)
- 20260921T173804Z LEG L2 closed: RECOVERED 2026-09-21 17:35:59Z-17:36:39Z by 4.0.0_SA_CRO on Andrew-direct (break-glass roles firmsep-inf/cot-bucket-reco
