# NEVER-WIDEN SIGN-OFF -- CTO HALF -- IRPT_BCKEND IB-rtj-2 (L4 bounded test principal)

- **Signer:** `1.0.0_SA_CTO`
- **Date:** 2026-09-22 ~01:1xZ
- **Packet:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~V/NEVER_WIDEN_SIGNOFF_PACKET_IB-rtj-2.md`
- **Packet blob:** `e2f521e5b55e236da0ae83f80254a10a1cbe84a8`. I re-derived it with `git rev-parse HEAD:<path>`.
- **Role:** `irpt-fence-probe-l4-role`
- **Inline policy:** `irpt-fence-probe-l4-policy`
- **Root:** `infra/aws/terraform/investor-reporting/l4-fence-probe/`
- **Other half owed:** `4.0.0_SA_CRO`, per my ruling in msg 99312, CALL 1.

## VERDICT: SIGNED

The act matches my 99312 ruling in shape. I checked each part below myself.

### Blast radius: exactly two creates, then exactly two deletes

I read the grant in `role.tf` at HEAD:

- **Actions:** `s3:ListBucket` only. There are no object ARNs and no wildcard.
- **Resources:** 3 bucket ARNs: the 2 registry-selected fenced firm buckets, plus `opal-313476888478-lambda-artifacts`.
- **Registry guard:** a `precondition` refuses the plan unless the registry yields exactly 2 fenced firm buckets. A registry edit therefore cannot widen the signed grant.
- **Trust:** `sts:AssumeRole` is granted to `user/Andrew_Berman` only. That principal already holds admin, so no new actor gains anything.
- **Session:** `max_session_duration` is 3600.

### The role is NOT exempt from the fence

I read both bucket policies live, which is a different instrument from the one the packet used. I then ran an fnmatch of the role ARN against every `ArnNotLike` pattern.

- **opal-data-inflection** (`DenyForeignFirmPrincipals`, Deny `s3:*`, 4 exemptions): `role/*-inf-*`, `user/Andrew_Berman`, `user/Andrew_Berman_Console`, `user/Opal_Terminal`. The role ARN matches **0 of 4**.
- **opal-data-cottonwood** (the same statement shape): `role/*-cot-*` plus the same three users. The role ARN matches **0 of 4**.
- **The session ARN:** after AssumeRole, `aws:PrincipalArn` is the ROLE's ARN, not Andrew_Berman's. The operator's own exemption therefore does not carry into the probe session. This is the property the test depends on.

### The control is sound

The only statement on `opal-313476888478-lambda-artifacts` is `PortalCISurfaceCheckGet`, which Allows `s3:GetObject` with 0 conditions. There is no Deny and no fence. A ListBucket there succeeds on the identity grant alone, so it serves as the positive arm.

### The attribution-control arm is ACCEPTED

This is the extra ListBucket on `opal-data-assets`, a bucket that is neither granted nor denied.

- It is an attempt only. It adds no grant and touches no data.
- It shows that S3's two denial wordings really do separate the two causes: "no identity-based policy allows" versus "explicit deny in a resource-based policy".
- That separation is what makes the wording in the negative arms evidence. It strengthens criterion (c) of my ruling.

### Rollback

Rollback is the act's own destroy step:

- `plan -destroy` must show exactly 2 deletions, run through safe-apply.
- `get-role` must then return `NoSuchEntity`, printed.
- The root's `.tf` files are deleted and committed, so no later apply can recreate the role.
- The ledger entry `20260922T0050Z_irpt-bckend-ib-rtj-2-l4-fence-probe` is opened before the apply and closed after the destroy.

### If the fence leaks

If a fenced bucket LISTS for the role, file a BLOCKING row and destroy anyway. Both buckets hold 0 keys, so no data is exposed.

## Not covered by this signature

- This signature does not cover any grant, principal or bucket-policy change beyond the two resources above.
- It does not cover any write action.
- A leak finding is NOT closed by the destroy. It becomes its own remediation.

**Push state:** LOCAL on CLOUD. `0.0.0_AB_MSTR` pushes.
