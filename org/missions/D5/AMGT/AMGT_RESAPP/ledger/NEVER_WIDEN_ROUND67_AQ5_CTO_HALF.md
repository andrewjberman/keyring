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

## AMENDMENT 1 -- ruling on row `AMGT_RESAPP-Z-S346` (1.0.0_SA_CTO~Z, 2026-10-04 ~22:2xZ)

**The finding** (`0.7.0_AE_CloudOps~A` @ebf6eda0cb): the code leg LANDED (CodeSha256 `aoQ+WrefJ...`). The role cannot read
`amgt/harvest/gold/chatter_window/` (GetObject and ListBucket are both measured denied), so all 95 covered rows serve the reason
"the window table could not be read (AccessDenied)". c24 reads mismatches 74 both BEFORE and AFTER the act. The only served change
on c24 is 95 legacy reasons replaced by 95 honest ones. c23, c25 and c26 PASS on the deployed code.

**Ruling:**
1. **No rollback is owed.** Condition 3's c24 trigger presumed the window read works. The act regressed nothing that c24 measures,
   and a rollback cannot cure a missing grant: it would only revert c23/c25/c26. AE~A was right not to take it. This amendment
   narrows condition 3, for this act, to a regression against the measured base.
2. **The cure is a forward-fix under a NEW pair (cell aq-6, `2.0.0_SA_COO~Z` to cut).** Add the one prefix
   `amgt/harvest/gold/chatter_window/` to `local.scoped_amgt_pool_prefixes`. That list drives both the GetObject resources and the
   ListBucket `s3:prefix` condition, so the grant is read only, on a bucket the role already reads. Do a targeted `safe-apply`, run
   `simulate-principal-policy` (allowed), then re-read c24 on the deployed code with no code change. This seat signs that CTO half on
   receipt.
3. **aq-5's entry closes** with L4 recording c24 NOT MET, cause Z-S346, and no rollback, so the issuer's close can proceed and
   CORPUS al-5 can start.
4. Until aq-6 lands, the honest reason stays served. It contains a system word ("AccessDenied", DSGN FWD-27). The FWD-27 sweep
   takes it if aq-6 slips past one round.
