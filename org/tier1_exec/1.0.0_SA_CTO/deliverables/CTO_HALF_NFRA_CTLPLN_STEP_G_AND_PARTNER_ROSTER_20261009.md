# CTO never-widen halves -- NFRA_CTLPLN step G, and the partner_roster.json redeploy (1.0.0_SA_CTO, 2026-10-09 ~00:2xZ)

## 1. NFRA_CTLPLN step G (the three step-F follow-ups) -- SIGNED

**Counterpart:** `org/tier1_exec/2.0.0_SA_COO/deliverables/NEVER_WIDEN_HALF_NFRA_CTLPLN_DELL_IDENTITY_STEP_G_STEP_F_FOLLOWUPS_20261008.md`
@737a66ea46 (msg 107495), read by section. Plan 0/2/0: one secret ARN added to the Dells' read (the IRPT render-token PUBLIC key;
classed PLATFORM-KEY with a ruling row S37 because the census has no public class) and one exact-ARN Deny on writes to
`/mdpf/custody_source`; the stale PassRole test retired (test only). These are exactly this seat's step-F rulings S31, S32, S33.
Condition: the counterpart's read-back (public key readable, `opal/auth/jwt-public-key` still refused, a re-plan reads no changes).
A future census class for public keys replaces the S37 ruling row; not this step.

## 2. `s3://opal-data-mdpf/code/scripts/gold/partner_roster.json` -- RULED and SIGNED as owner

**Ask:** dell1 1.0.0_SA_CTO~DELL1 msg 1265 (relay `org/tier0_exec/0.0.0_AB_MSTR/deliverables/RELAY_20261009T0006Z_DELL1_PARTNER_ROSTER_SERVED_DRIFT.md`):
served copy (LastModified 2026-07-28) still reads Cottonwood cadence "D+2" against HEAD's "T-1" (b3ed0e8d69, Andrew-direct
2026-08-27, "Yes that config is what needs to change"), so a missed Cottonwood day can read lag 0 and HEALTHY.

**Ruled:** dell1's `0.7.0_AE_CloudOps~DELL1` deploys it (MDPF runs on dell1; Andrew ~22:0xZ, each box deploys its own), through
`safe-deploy` under one change-management ledger, uploading the bytes of `git show HEAD:<path>` (LF), never the CRLF working file;
after, the served object's content hash equals the HEAD blob's. **Blast radius:** one config object the gold runner reads; the
only behaviour change is Cottonwood's freshness cadence (T-1), so a missed Cottonwood day reads late, as Andrew ruled on 08-27.
Rollback: re-copy the prior object version. A dell1 COO half pairs this one.

**SIGNED (both)** -- `1.0.0_SA_CTO`
