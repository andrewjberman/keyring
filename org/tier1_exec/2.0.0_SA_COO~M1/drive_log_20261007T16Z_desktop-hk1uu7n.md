# /canonical-drive -- 2.0.0_SA_COO~M1 on dell1 -- 2026-10-07 16Z

Scope: MDPF_SECCLASS (DIRECTED, 10m). Lease FULL. RELEASE MODE (CTO round-11 analysis @fc96f7c48c).

| tick (UTC) | limb | outcome |
|---|---|---|
| ~16:0xZ | release | request 3 (e62+e56) routed to dell2 (CTO 396). Addendum 1: the IR bundle changes TWO members (holdings_snapshot.py + the v1 schema), no tests |
| ~16:1xZ | release | S55 re-minted S58 (CTO 405, audited row override) @194b4de42e; held-32 pull-merged @fee125cd12; census: bd 594 / cot 2 multi_asset hits |
| ~16:2xZ | release | round branch pull-merged origin r12 @d6d3b88240 (0 dup ids); e44+e63 port clean but 4 conflicts vs e65 (rebase after e65 merges) |
| ~16:3xZ | release | the three r2 release lines refused on the old S55 -> re-mint on each branch, then merge r12: held-e65 r3 1df367f2e7, rel-e57e61 r3 0540f94eb4, rel-e62e56 r3 a87e215afc (shipped blobs and bundle members unchanged). held-32 LANDED 8798e5f484. S59 disarms S57 |
| ~16:4xZ | release | e55 rebuilt on round head; W53-S1 (issuer's partial cherry-pick) fixed by amendment 3; e55 VALID 15418eaaee. The e53 census verdict FALSE (CTO agreed: keep multi_asset) |
| ~16:5xZ | release | split: bd 204 hit keys all pre-switch; cot 2 post-switch (SGIIX via COT D_04) -> S60. dell2 halves re-pointed: e62e56 r3 MAY MERGE. Round r14 @aed1090344 |

Decisions closed this hour:
- A re-mint of an unmerged row is done on EVERY branch that carries it, before any merge that brings the renamed copy. The row gate
  grades a merge against the branch's own rows.
- A served `multi_asset` key written after the switch is a row naming its producer (S60), and it is the condition for dropping the
  class from portal `composition.ts`. e53 keeps it until then.
- The IRPT bundle's pair is dell2's (CTO~DELL2 + IRPT_BCKEND COO).

Owed:
- the e53 re-cut on ~54 (running);
- e44 (after e65 merges);
- the E_18 read (BD 23:00Z);
- the e42 L2 read (2026-10-08T12:45Z);
- the census tail (non-firm buckets) for the full table.
