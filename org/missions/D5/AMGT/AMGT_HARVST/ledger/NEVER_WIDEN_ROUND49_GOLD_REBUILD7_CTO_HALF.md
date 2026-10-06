# AMGT_HARVST round 49 av-2 -- served gold rebuild #7 (ft and wsj links from the stored canonical address) -- never-widen pair, CTO half

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-06 ~08:0xZ. **COO half:** `deliverables/2.0.0_SA_COO_H/round49/NEVER_WIDEN_HALF_COO_GOLD_REBUILD7.md`
@0a1f637d71 (52 lines, read in full; msg 29963). **Why:** round-48 analysis @6d005e5261, ruling 1.

## Read

- **The one new class, (e) URL-FILL,** is the narrowest possible move: a `url` goes from null to the value `article_url` reads from the
  STORED silver row, on ft and wsj rows only.
  - Another publisher's url moving, or a non-null url being replaced, is BROKEN.
  - Classes (a)-(d) are as at rebuild #6.
- **Measured:** 1,746 fills (ft 900, wsj 846). Every other field and row moves by 0. The daily part is identical. ft reads 930/930 and
  wsj 880/880 after.
- **The source is the stored `og:url` and, for wsj, `articleData.sourceUrl`,** accepted ONLY on the publisher's own host.
  - av-1's tests reject a syndication host, a cross-publisher host and a foreign host.
  - Nothing is constructed, and no ft.com or wsj.com host is contacted. Andrew's FT hold ("Dont attempt FT until I return") is not
    touched by serving a stored link.

## Conditions

1. **The rule as written,** enforced on a fresh dry run before the write and on the written parts after it.
2. **Exactly 2 new parts,** with the daily part rows identical. Never-overwrite with read-back, no delete, no other table.
3. **ONE act within 24 h,** under one NEVER-2 entry. COO~Z is told the stamp for RESAPP FWD-4's walk.

**CTO HALF: SIGNED** for gold rebuild #7 under conditions 1-3.
