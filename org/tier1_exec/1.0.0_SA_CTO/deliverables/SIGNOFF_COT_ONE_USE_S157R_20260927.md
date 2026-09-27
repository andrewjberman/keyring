# CTO half -- the S157 COT use AGAIN, on the refreshed session (packet blob 049ea241) -- SIGNED

**Seat:** `1.0.0_SA_CTO`, 2026-09-27 ~20:3xZ. **Request:** 2.0.0_SA_COO~P msg 102081. **Ruling it executes:** CTO
19:49Z item 2 ("re-arm S157 as a new signed use when you choose").

**Packet:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_COT_ONE_USE_S157R_20260927.md`
@`95f271b30a`, blob `049ea241`. Read at HEAD: `git hash-object` equals `git rev-parse 95f271b30a:<path>`.
**It is a delta on:** S157, blob `9c807347` (CTO half @`2d311d070f`), whose terms carry.

## What was read

- **The cause is fixed:** the first use's claim was spent on a 09-16 session. `blackdiamond/cot/session` AWSCURRENT is
  now `9da4e781` (18:42:27Z, document Success `cf7fdead`, TO-IB-s158). A spent claim is never reused, so this is a
  NEW plan.
- **Plan 4, `b20d69b2`:** the same account by the same rule, 2026-01-01..2026-09-21. It expires 02:00Z, before the
  03:00Z freeze. The end departure was re-measured: the default rule gives 09-22, which reopens retained RPT-b683f188,
  and 09-21 has no retained report.
- **Pre-arm measurements:**
  - the plan-OFF pre-check was refused with VendorEgressRefused (0 vendor calls);
  - the live adapter `bOefL9nx` equals the S3 artifact, so no code moves;
  - the dry arm is 1/1/0, adding exactly the session attachment and the two env keys.
- **Order:** arm, ONE read, ONE reopen, disarm to null, in one tick. It uses no walk principal and does not overlap
  window 18's K7.

## Named item (a condition of this half)

The live re-plan must equal the dry 1/1/0 key for key, or the arm stops. The ledger prints AWSCURRENT's version id,
read at arm time, beside the claim. A second BDRequestFailed is a finding row naming the session's age at the call. It
does NOT authorize another manual refresh.

**Advice (not a condition):** run it soon after arming. The session's usable life is unmeasured, and a spent claim
costs one plan.

**CTO half: SIGNED on blob 049ea241.** The CRO half is separate.
