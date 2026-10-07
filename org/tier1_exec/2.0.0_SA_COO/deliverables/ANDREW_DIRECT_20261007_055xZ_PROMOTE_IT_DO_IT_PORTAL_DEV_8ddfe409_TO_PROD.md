# ANDREW-DIRECT 2026-10-07 ~05:5xZ-06:0xZ -- "promote it", then "Do it": portal DEV 8ddfe409 to PROD

- **Channel:** the site-Z terminal of `2.0.0_SA_COO~D` (session 83c2c1d1-733c-4463-b47c-1dc1b819822e), typed by Andrew.
- **Recorded by:** `2.0.0_SA_COO~D`, same turn.

## Verbatim, in order

1. "promote it" -- in reply to this seat's line that DSGN round 45 was on DEV, 4 commits ahead of PROD, and that the PROD promote
   waited on his word.
2. "Do it" -- in reply to this seat's one-card call after it re-read the heads and found DEV had moved.

## The card the second word answers

**Call:** "Promote all of DEV `8ddfe409` to PROD, including the two `/freshness` commits: yes/no?"
**Recommendation approved:** Yes.

## Scope, as written and no wider

- One promote of portal DEV `8ddfe409` to PROD (base `ab3191d0`, rollback `ab3191d0`). `origin/PROD..origin/DEV` at the read (05:53Z):
  7 commits, 6 non-merge -- the four DSGN_AMGTV1 round 45 commits (to `659104f4`), AMGT_RESAPP round 77's `/freshness` change
  `504ddb3d` (merged as `3a29250a`), and `8ddfe409`, which limits `/freshness` to Dev users (its message cites Andrew-direct
  2026-10-07).
- Stated to Andrew on the card: this seat did not read `/freshness` on DEV with those two changes; that page is
  `2.0.0_SA_COO~Z`'s. CI on `8ddfe409` read success.
- A DEV head other than `8ddfe409` at push time is not covered.
