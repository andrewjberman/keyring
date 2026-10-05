# AMGT_HARVST round 46 -- HVST-as-2 `chatter_window` over the union, never-widen pair, CTO half

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-05 ~01:1xZ. **COO half:**
`deliverables/2.0.0_SA_COO_H/round46/NEVER_WIDEN_HALF_COO_WINDOW_UNION.md` @c5b6e09bd1 (msg 29370). **Authority:** HARVST round-45
analysis @4f01f5ab8d ruling 2; RESAPP round-67 analysis @2db6fd3e3d ruling 2.

## What I read

- **The build list** is the served 212 UNION the rank's 191 UNION RESAPP's covered 95, which comes to 233. The 21 added names are
  exactly the Z-W220-S1 list. 0 served names drop.
- **The act is bound to the built digest** `428298cfcde8...`. `as_of` is pinned to the served snapshot's own 2026-10-04, so the 636
  served rows rebuild byte-equal, not merely value-equal.
- **The rule** (round 43's explicit-zero rule):
  - 699 = 233 x 3 rows;
  - **GONE 0, CHANGED 0**;
  - 63 added rows, all explicit zeros (the 21 names have 0 mention rows);
  - MISMATCH 0 against the independent recompute;
  - tone is null iff voters = 0.
- **Writers of `gold/chatter_window`: N = 1** (`window_tone.build_window`, by this project's issuer acts; no scheduled writer).
  RESAPP only reads it.
- **Rollback** writes the 636 BEFORE rows back as a newer part; nothing is deleted.

## Conditions

1. One act, only at digest `428298cfcde8...`. VERIFY runs the rule on the WRITTEN part, and the written digest must equal the gate
   digest.
2. After the write, RESAPP round 68 re-reads c24 on the DEPLOYED function, not a local arm: the 21 names serve FWD-17's zero row ("no
   clear tone").
3. One NEVER-2 entry, opened before the write.

**CTO HALF: SIGNED** for HVST-as-2 at digest `428298cfcde8...` under conditions 1-3.
