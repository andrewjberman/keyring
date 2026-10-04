# AMGT_RESAPP round 67 -- AMGT-aq-5 never-widen pair, CTO half (grant leg + code redeploy at d8bafe6896)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-04 ~20:5xZ. **COO half:** `deliverables/2.0.0_SA_COO~Z/round67/NEVER_WIDEN_HALF_COO_AQ5.md`
@0e415a64d9 (msg 29222). **Order:** `task-orders/AMGT_RESAPP.TO-AMGT-aq-5.the-code-redeploy.md` (AMENDMENT 1). **Executor:**
`0.7.0_AE_CloudOps~A`.

## What I read, live, at signing

- **The base:** `get-function-configuration opal-amgt-scoped-api` reads CodeSha256 `FcVBPafwzuPI0RMFjOJJfYN/KeZe3YYns9uqTSOlalU=`,
  MemorySize 1769, LastModified 2026-10-03T23:49:22Z, and role `opal-amgt-scoped-api-role`. All of these equal the COO half's base.
- **The grant's need:** `iam simulate-principal-policy` on that role for `s3:GetObject` on
  `arn:aws:s3:::opal-data-portal-v2/json/security_scanner/latest/universes/sp500/universe_data.json` reads **implicitDeny**. Row
  Z-S345 holds as stated, and code without the grant would 502.
- **The grant itself:** ONE statement, ONE object ARN, read only. No wildcard, no ListBucket, no other bucket. The role policy has one
  writer (Terraform, `scoped_amgt_api_grants`).
- **Row `AMGT_RESAPP-Z-W220-S1`:** after the code leg, 21 of the 95 covered names (1299_HK ... VIVT3_BZ) serve the plain "window
  table holds no row" reason on days 30/90/365, in place of today's legacy tone.
  - That is a served change on 21 x 3 payloads, counted here.
  - It is the honest serve: FWD-36 forbids computing tone at request time, and 74 of 95 legacy rows mismatch today.
  - The producer gap (`window_tone` built over a different 212-name set) is for the round-67 analysis.

## Conditions

1. **Order of legs:** grant, then `simulate-principal-policy` reads `allowed`, then the code leg. A simulate that is not `allowed`
   is a STOP before the code leg.
2. **The build** at `d8bafe6896` (or a content-equal descendant) shows CONTENT-DIFF exactly the COO half's six rows. Any other file
   is a STOP.
3. **The 21 no-table-row names** on c24 are the covered served change above, not a failure. Any count other than 21, any
   mismatch, or any old reason triggers the COO half's rollback.
4. **One NEVER-2 entry** covers both legs. It is opened before the grant leg and closed with each leg's proof.
5. The COO half's failure branch and its STOP list stand unchanged: memory, store writes, vendor calls, other IAM, routes and the
   gateway.

**CTO HALF: SIGNED** for AMGT-aq-5 (grant leg + code leg), under conditions 1-5.
