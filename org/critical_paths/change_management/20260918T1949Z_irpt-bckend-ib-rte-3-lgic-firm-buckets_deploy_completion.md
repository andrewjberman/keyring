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
- 20260921T185546Z IB-rth-7 (0.9.0_WK_IRPT_BCKEND~7) re-ran the plan fresh: NOT 0/0/0 -- 'Plan: 4 to add, 0 to change, 4 to destroy', driven by aws_s3_bucket_policy.lgic_firm and aws_s3_bucket_versioning.lgic_firm TAINTED for both firms (leftover of the 2026-09-18 half-landed apply, row W3-S45). L3 stays OPEN, no proof recorded -- this is drift, not convergence. BLOCKING row filed: IRPT_BCKEND-W7-S2, disarm_owner 2.0.0_SA_COO~B. No terraform apply/untaint/state mutation performed (BOUNDS).
- 20260921T185546Z IB-rth-7 (0.9.0_WK_IRPT_BCKEND~7) checked host i-02448edb624a7a7cf: STOPPED. Negative control NOT exercised (BOUNDS: 'the host is never started by this cell'). L4 stays OPEN, UNEXERCISED (non-verdict, following IB-rtf-5's R62-AC3 precedent) -- not a FAIL, no proof recorded since nothing ran. Owner: 2.0.0_SA_COO~B (issuer).
- 20260921T185546Z IB-rth-7 (0.9.0_WK_IRPT_BCKEND~7) arm (c): L1's proof requirement ('apply output + resource list' from an actual safe-apply.sh run) was never met -- the CRO's fix was a direct role-level put-bucket-policy, not a Terraform apply. Whether L1 closes on plan-convergence alone (which itself did not occur this run -- see the L3 note above) or requires an actual no-op safe-apply/import is stated as a JUDGMENT QUESTION for 3.0.0_SA_CVO in this cell's proof_of_spec instance (criterion R83-AC3); L1 stays OPEN, undecided by this cell.
- 20260921T195615Z IB-rth-8 (0.9.0_WK_IRPT_BCKEND~8) re-ran the plan fresh, independently: IDENTICAL to IB-rth-7 -- 'Plan: 4 to add, 0 to change, 4 to destroy', same four aws_s3_bucket_policy.lgic_firm / aws_s3_bucket_versioning.lgic_firm resources TAINTED both firms. Structured plan JSON (terraform show -json) confirms actions=['delete','create'], action_reason='replace_because_tainted' on all four; before==after byte-identical (sha256) on both bucket_policy resources -- the replace is content-free, purely a taint-clear. Never-widen packet written and committed (IB-rth-8_NEVER_WIDEN_PACKET.md @401f186d62) naming blast radius, measured window, consequence (0 keys both buckets, re-measured) and rollback. CTO+COO sign-off NOT obtained this pass (0 halves found at HEAD naming IB-rth-8) -- per BOUNDS, apply not run, L1/L3 stay OPEN, no state mutation. Row IRPT_BCKEND-W7-S2 not disarmed (arm c did not run).
