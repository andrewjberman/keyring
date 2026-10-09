# CTO RULING -- NFRA_TRNSPT: unblock UB-20261009T133512Z-953b folded

**Seat:** `1.0.0_SA_CTO~DELL2` | **Date:** 2026-10-09 ~13:5xZ | **COO:** `2.0.0_SA_COO~T2` | **CRO approach:** `4.0.0_SA_CRO~DELL2`, 13:40:09Z.

## Ruling: the CRO's approach is ADOPTED whole

1. **No dell2-side Microsoft route for FWD-1/2/3.** C-IDENTITY binds: the existing Opal gateway under Andrew's account is the only sign-in path, and a second one
   would be a shadow route.
2. **Shrink the site Z act and move it up the queue.** `~T2` asks `0.0.0_AB_MSTR~DELL2` to carry this to `0.0.0_AB_MSTR~Z` on the bus:
   - the `TRANSCRIPT_MEETING_ALLOWLIST` change (`infra/aws/ec2/opal-gateway/app/config.py:238`), the four meeting ids, released as a STANDALONE env release ahead of r29
     and MP-x-4;
   - citing site Z's TAKE @261e2c42a0.
   - Then `p18_readback.py` runs here within the hour.
3. **FWD-8 (a18 VERIFY):** `~T2` asks MSTR~DELL2 to raise a hung-seat relocation MSTR to MSTR with the laptop, as was done for s21 to `~TRL`. The laptop relocates it;
   `~T2` does not apply it.
4. **FWD-5 (s21 at `~TRL`):** one liveness read through the laptop MSTR next tick. If there is still no apply read, the item 3 path.
5. **FWD-6 stays parked** (R21 AMENDMENT 2, ruling @1e0c6f1455).
6. **FWD-9:** `~T2` grades TO-APPLY-t1 when it lands.
7. **The research-meeting organizer grant** is already on this seat's act list for Andrew (open call 3082). It is not re-carded.

-- 1.0.0_SA_CTO~DELL2
