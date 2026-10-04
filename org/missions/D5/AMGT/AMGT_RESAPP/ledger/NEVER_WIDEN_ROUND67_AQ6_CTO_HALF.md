# AMGT_RESAPP round 67 -- AMGT-aq-6 never-widen pair, CTO half (one read-only chatter_window prefix on the scoped-API role)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-04 ~22:4xZ. **COO half:** `deliverables/2.0.0_SA_COO~Z/round67/NEVER_WIDEN_HALF_COO_AQ6.md`
@4d3db86faa (msg 29283). **Order:** aq-5 AMENDMENT 2, leg 3. **Ruling:** aq-5 CTO half AMENDMENT 1 @14aa3c9200, endorsed by
Andrew ("recs approved", record @c700426bc9).

## What I read, live, at signing

- `simulate-principal-policy` on `opal-amgt-scoped-api-role`, `s3:GetObject`:
  - `opal-data-harvest/amgt/harvest/gold/chatter_window/date=2026-10-01/part-0.json` = **implicitDeny**;
  - control `.../chatter_daily/...` = **allowed**.
- The function's CodeSha256 is `aoQ+WrefJ+JjQcymqyrt2c7MEIlTPmvjJEv8sqZ6M98=`, which equals the COO half's base. The act moves no code.
- **The grant:** one prefix added to `local.scoped_amgt_pool_prefixes`. That list drives both the GetObject resource and the ListBucket
  `s3:prefix` condition. It is read only, on a bucket the role already reads under 11 sibling prefixes. There is one writer
  (Terraform). The table's producer writes; this role only reads.
- **Both branches** are the COO half's: the grant takes (c24 C2 unreadable 0, C1 mismatches 0 with no-table-row 21), or it does not
  (STOP with the simulate output). A regression against the base is a policy ROLLBACK.

## Conditions

1. The plan is `opal-amgt-scoped-api-grants` ONLY: 1 to change, 0 to add, 0 to destroy. Any other resource, any code or memory
   change, or any other prefix, bucket or action is a STOP.
2. Simulate reads `allowed` on BOTH GetObject and ListBucket(prefix) after the apply, before c24 is read.
3. The leg rides the aq-5 NEVER-2 entry as leg 3, which closes only with c24 read. CORPUS al-5 still starts only after that entry
   CLOSES.

**CTO HALF: SIGNED** for AMGT-aq-6 under conditions 1-3.

## AMENDMENT 1 -- condition 3 reversed (1.0.0_SA_CTO~Z, 2026-10-04 ~22:4xZ, on `2.0.0_SA_COO~Z` msg 29289)

aq-5's NEVER-2 entry CLOSED at 22:27Z (AE~A msg 29287), before this half. CORPUS al-5 then opened `amgt-corpus-r36-al5` at 22:35Z
(@5907db84a4) on the same function at `288de3d95d`. `d8bafe6896` is an ancestor of that pin, so nothing of round 67 reverts.
Condition 3 is replaced:

3. **aq-6 runs AFTER al-5's entry CLOSES, under its OWN NEVER-2 entry** (COO amendment @a8c4eb15c8).
   - The code base is the CodeSha256 al-5's entry records at close, re-read live before the apply. If al-5 rolled back, the base is
     `aoQ+WrefJ...`.
   - The act still moves NO code; a CodeSha256 that changes during aq-6 is a STOP.
   - Serial, not concurrent, because al-5's regression set includes r67 c24. A grant landing mid-al-5 would move c24 under al-5's
     verify and confound it.

Conditions 1 and 2 stand. **CTO HALF: SIGNED**, as amended.
