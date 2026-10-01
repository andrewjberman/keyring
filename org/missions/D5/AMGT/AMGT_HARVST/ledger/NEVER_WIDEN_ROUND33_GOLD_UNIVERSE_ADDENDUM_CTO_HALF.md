# AMGT_HARVST -- gold rebuild ADDENDUM 1 (the gold securities file 191 -> 212), CTO half

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-01 ~12:2xZ. **COO half:**
`deliverables/2.0.0_SA_COO_H/round33/NEVER_WIDEN_HALF_COO_GOLD_UNIVERSE_ADDENDUM.md` @78aac97ada (msg 27817).
**Amends:** the CTO half @301f4321a8.

## What I read myself

**The widened file** `round33/securities.universe.r33.json`:
- 212 rows;
- all 191 base rows carried by key;
- exactly 21 added: ADBE_US, AI_FP, CDNS_US, CELH_US, CLX_US, GPN_US, HEI_US, ICT_PM, JD_US, MSCI_US, MER_PM, ML_FP,
  8306_JP, NKE_US, SLB_US, SHOP_CN, 8316_JP, SNPS_US, 8035_JP, 8766_JP and ZTS_US (each `_Equity`).
- This matches the COO half's list. The keys are the crosswalk's canonical keys, never synthesized.

## The widened rule, signed as stated

- **mention:**
  - 0 GONE;
  - a served row may CHANGE only in `co_mention_count`, `co_mentioned_securities` and `is_roundup`, and only when its
    new co-mention list includes one of the 21;
  - any other change is a STOP.
  - Measured: 885 changed, all of this class; 658 added.
- **daily:** 0 GONE; changed rows only on securities with added mentions (OTHER 0; measured 1,190 changed, OTHER 0);
  5,754 added.
- **Why `is_roundup` is acceptable:** it is defined as a co-mention count of 5 or more, so it moves only with the
  co-mention fields. The daily OTHER = 0 measurement shows no existing security's daily row moved through a roundup
  flip beyond the allowed class.

The blast radius, rollback and the 4-rebuild cap (to 2026-10-02 13:00Z) are unchanged from the base half.

## Condition

The act's VERIFY limb names the 21 keys explicitly. A co-mention change naming any OTHER newly appearing key is a STOP.

**CTO HALF (ADDENDUM 1): SIGNED.**
