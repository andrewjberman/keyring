# L4-R review, NFRA_OPLGTW PRD v2.1, ratified-text half (ENDPOINT FWD-14 to FWD-19; CONTRACTS C2-C4) -- SIGN (3.0.0_SA_CVO~Z for 3.0.0_SA_CVO~O, 2026-10-08 ~23:5xZ)

**Asked by** `1.0.0_SA_CTO~O` msgs 32123 and 32125 (acked). **Bytes reviewed:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md`
@8dccd20fa2, unchanged at HEAD; `git diff e43ee663be 8dccd20fa2` on that file, whole (the header, FWD-14 to FWD-19, the v2.1
addendum). Half hash at review: ratified-text `0121932260a9`, ENDPOINT `be52a62a19f1`.
**Sources read whole:** `ANDREW_DIRECT_20261008_220xZ_ALYSSA_TAX_WORKFLOW_...md` @618699ceeb;
`ANDREW_DIRECT_20261008_212xZ_ALYSSA_13M_AND_TAX_SMA_MASTER_ASAP.md` @6233bae5de. From the brief
`docs/briefs/oplgtw-tax-workflow-midstream-brief-20261008.md` @dae0456eb4: the gap table (G-2 to G-12) and measurements 3 to 6.
**Prior review:** `L4R_REVIEW_NFRA_OPLGTW_v2.0_RATIFIED_TEXT_20261008_Z.md` @c894f5631b.

## Verdict: SIGN

Every outcome is a read, at the width of his ~22:0xZ words, and the scope bound is his own sentence: "We don't have to do
the whole workflow for her. We just have to be able to give her the right information."

- **FWD-14** is his rows 11-15: beginning value, flows, gain/loss and ending value. A figure that does not tie says why.
  The brief could not find the source of the workbook's quarter-start value, so that clause will be used.
- **FWD-15** keys on last four plus a name. That is the pair his row 6 holds ("client name ... the account number with
  the last 4 digits"). The refusal of last four alone rests on a printed measurement: 1,831 of 5,320 last-fours are
  shared in 08335338.
- **FWD-16** is "that since inception value for every given tax account". Taking inception from the roster, not from
  account open, rests on the brief's G-3: 11 of 11 accounts were opened before their Tax inception. "Computes no return"
  is his scope bound.
- **FWD-17** is "realized gains losses, unrealized gains losses, and any kind of tax slots or cost basis", plus his
  "potentially" top-10 holdings. A missing basis reads missing, never zero.
- **FWD-18** is "Alyssa is going to need to go to both of those places". Item 3 states its own narrowing to the roster's
  Black Diamond accounts as a reading, so the narrowing is visible, not silent.
- **FWD-19** is "a backfill uh, on whatever the contents are of this new Schwab master".
- **Item 1:** no download operation, citing his ~19:2xZ word.
- **Item 2:** strikes the v2.0 gate (my note 1 of the v2.0 review).
- The hidden classes stay hidden, and nothing touches his ~20:0xZ hold on her close run.

## Carried to the CTO (not grounds)

1. **"Every given tax account" vs what the text serves.** He asked for the since-inception value of every Tax account.
   The text proves FWD-16 on two accounts whose inception is inside the window. It does not say what Alyssa reads for an
   account outside it. The brief also measures 2 of its 15 workbook accounts (RIA 49 Financial) in none of the three
   sources. The 13-month cap is sound for the 15 measured accounts (inceptions 2026-04-08 to 2026-08-05), but that
   covers 15 accounts, not the roster. The fix needs only a sentence: an account with no source, or with an inception
   past the cap, reads as unavailable with that reason. A roster-wide count would then show whether his "13 months will
   cover that unilaterally" holds.
2. **Sector allocation (row 33).** He linked `Sector Allocation.xlsx`, and the brief finds its source is a FactSet file
   export. "NOT served: no source exists" is true of both custodians' silver. Saying "the source is a FactSet export
   outside the gateway; a vendor read needs his per-use word" would let him see the choice instead of an absence.
3. **Last four alone.** Refusing a last-four that matches exactly one account is narrower than "a good key to match
   on". The text's own ambiguity rule (return the candidates, pick none) would serve last four alone without guessing.
   Minor; the CTO's call.
4. **Black Diamond is Cottonwood RIA's firm prefix.** Reading `blackdiamond/cottonwood/silver/` for Opal's Tax accounts
   is a cross-firm read. The NEVER rule's guard enumerates firms. The never-widen halves on the BD cell should name the
   account-scoped IAM condition that confines it.

-- 3.0.0_SA_CVO~Z
