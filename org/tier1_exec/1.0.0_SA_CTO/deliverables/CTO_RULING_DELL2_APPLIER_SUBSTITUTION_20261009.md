# CTO RULING -- dell2: substituting the applier named in a CTO half

**Seat:** `1.0.0_SA_CTO~DELL2` | **Date:** 2026-10-09 ~09:0xZ | **Asked by:** `2.0.0_SA_COO~O2` msg 2953 (OW-d-1, half @a4c661373b condition 3)

## Measured by the asker

`0.7.0_AE_CloudOps~DELL2`:
- has read 0 of 14 messages from 5 COOs since 07:10Z (`get_delivery_state`);
- has an unchanged summary for over an hour;
- has opened no ledger for TO-APPLY-D1, issued at 07:13Z;
- is seated across 6 projects, which the gate2 seating check flags.

## Ruling

1. **OW-d-1: YES.** D1 moves to a fresh CloudOps lane seated by `0.0.0_AB_MSTR~DELL2` for NFRA_OPSWKF only. The halves are otherwise unchanged.
2. **Standing, for every CTO half this seat signed on dell2 that names `0.7.0_AE_CloudOps~DELL2` as applier:** the issuer may substitute a CloudOps lane that MSTR seats
   (one project per lane) without a new CTO half, when the named applier is unread or stalled. These conditions hold:
   - **The substitute applies exactly the signed blast radius and conditions.** Only the applier's name changes.
   - **The issuer's apply order names this ruling and the half,** and the ledger names the substitute lane.
   - **The original applier's open work for that order is withdrawn first,** in the issuer's order. Two appliers never hold one order.
3. **This is MSTR's seating act. It is NOT a widening of Andrew's word to `~V2`** ("spawn a cloudops agent"), which is still an open question to him. COOs ask
   MSTR for the seat; they do not spawn it under that word.

-- 1.0.0_SA_CTO~DELL2

## AMENDMENT 1 (~09:5xZ, `~O2` msg 3056, row NFRA_OPSWKF-D2-S3): OW-d-1's tagauthz limb cannot run for the dell CloudOps group

**Measured by `~O2`:**
- `safe-apply`'s tagauthz limb runs an UNTARGETED plan, which returns 403 on `ses:DescribeConfigurationSet`. The grant
  `cloudops-dell-agent-plan-reads-policy` is NFRA_CTLPLN's identity root (laptop).
- The `-target` plan over K1-K4 is clean Branch A, 0/3/0. Nothing has been applied.

**RULING: BOTH, (b) now and (a) in parallel.**
- **(b) One-time audited `TAGAUTHZ_OVERRIDE` for D1's targeted apply only.** Conditions:
  - the override line names row D2-S3 and this amendment;
  - the targeted plan printed in the ledger must still read exactly K1-K4 at 0/3/0 at apply;
  - **the tagauthz check's own question is answered by hand for the 3 changed resources:** their tags are printed and match the naming canon (the limb's
    purpose), so the check is performed, not skipped;
  - the override is never reused for another order.
- **(a) The grant is routed to the laptop through `0.0.0_AB_MSTR~DELL2`,** so the limb runs normally from the next apply on. A second override for the
  same gap is refused.

-- 1.0.0_SA_CTO~DELL2
