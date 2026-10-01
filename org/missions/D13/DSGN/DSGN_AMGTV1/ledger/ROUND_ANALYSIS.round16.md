# DSGN_AMGTV1 -- ROUND 16 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-01 ~09:4xZ

**Input:** CVO slug msg 27713, `ADJUDICATION_v18.md` @b8a3aee418 (5 of 5 terminal; AC4 3 of 3 MET). Drain-end read
@565abdca56 (render FAIL 6 of 77, down from 16; the live signed-in walk was VALID). PRD v0.6 ADMITTED. **The freeze is
22:00Z.**

## 1. WHAT THE ROUND DELIVERED

- **g-1 walker lease:** ARM and DISARM posted, disarm proven (401). Z-S10's class did not recur on site Z.
- **g-2 header cards:** equal widths, each with its eyebrow band.
- **g-3 render instrument:** sees both demo faces.
- **g-4 the chatter face:** live, with 9 September bubbles sized by `collected`, a working month cursor, and "9 of 95
  covered names have collected articles this period".
- **g-5:** no "Lead Panel" string; the identity card is in the card family.

**Round 16 is CLOSED.**

## 2. RULINGS

| # | ruling | why |
|---|---|---|
| 1 | **The live price face is the one unproven demo face.** Round 17 cell 1 is one live signed-in walk that WAITS on `[data-price-bar]` (up to 30 s after the route answers). Bars render: the face is proven, done. No bar after the wait: the cell captures the route body and the component state, and root-causes it the same round. | CVO v18 section 5.1. The field contract holds: the deployed handler serves `return_30d_pct` = `score` when `window_days` = 30 (`scoped_amgt.py:763-788`), which `PriceBars.tsx:47` reads. So the skeleton is either a capture race or a stuck query, and the wait discriminates. |
| 2 | **The identity card's "BA US" contrast** (`lowContrastChars`) is cell 2, a one-line fix. | issuer input 1 |
| 3 | **Raw-key bubble labels close with RESAPP round 58** (ah-2 signed @656b226d50). Nothing page-side. Cell 1's walk re-reads the chatter face after ah-2 deploys: 0 of the sized labels equal a `security_key`. | Z-S331; CONTRACT section 0, one writer |
| 4 | **The walker rule stays one device at a time** until the laptop's checkout carries e41e28e641 (CTO msg to MSTR~Z 08:50Z). | the lease guards only the site Z copy |

## 3. THE ENRICHMENT LIST -- round 17, `2.0.0_SA_COO~D`, ONE issuance

| # | cell | criteria shape |
|---|---|---|
| 1 | live walk: the price face plus the chatter labels (rulings 1, 3) | the PNG shows bars with `[data-price-bar]` present; after RESAPP ah-2, 0 sized bubble labels equal a `security_key` |
| 2 | identity card contrast | the render's `lowContrastChars` reads 0 on the identity card |

**L9 (CVO, as a person):** the price PNG reads as ranked bars, longest first, with signs. **The close walk is the
Friday acceptance read of DSGN.** After it: the freeze, then the promote (PROD payload per CVO verdict 27503).

## 4. ACTS ONLY ANDREW CAN DO (cited)

1. **The PROD promote payload beyond Security Analysis** (CVO verdict 27503).
2. **Recursive removal of the DSGN worktrees and scratch roots** (CLAUDE.md human confirmation for recursive deletion).
