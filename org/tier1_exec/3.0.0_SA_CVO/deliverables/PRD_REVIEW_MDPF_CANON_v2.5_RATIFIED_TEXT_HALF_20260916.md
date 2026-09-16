# PRD review -- MDPF_CANON v2.5, ratified-text half (ENDPOINT + CONTRACTS)

Reviewer: `3.0.0_SA_CVO`. Delivered by `1.0.0_SA_CTO` msg 97534 (record 97536).
PRD: `org/missions/D8/MDPF/MDPF_CANON/prd/MDPF_CANON_PRD.md` @ `062c062749`, ratified-text half_hash `427180b19796`.
Prior review: v2.4 REFUSED, `PRD_REVIEW_MDPF_CANON_v2.4_RATIFIED_TEXT_HALF_20260916.md` @ `9bc1cac31a` + addendum @ `ea5f7bcbb5`.

## VERDICT: SIGN

## Method

The ratified-text section diff `ef899e790f..062c062749` is 3 hunks: FWD-1's headline, FWD-1's ACCEPT, and
CONTRACTS `:177`. FWD-2..FWD-8 and every other CONTRACTS row are byte-unchanged.

## The three defects

**DEFECT 1 (state typed) -- CURED.**
- `:177` now reads state "at the address `address()` returns for the `state` tier under R21 and Rule 30".
- Bronze and the firm platinum slice are also stated as builder output. Their current values are marked
  "today" beside that, so the builder is the authority.
- No data home in the row is a typed destination any more. The one typed address left is the historical
  combined slice `opal-data-portal-v2/platinum/mdpf/global/`, which the row already exempts (X2).
- In the review of v2.4, `address()` returned the firm bucket for each firm scope's state and
  `opal-data-mdpf` for global. The parenthetical now says exactly that.

**DEFECT 2 (history + seat reference) -- CURED.** The "this replaces ... the CVO's finding" clause and "measured
at HEAD" are gone from CONTRACTS. Andrew's call 3 is cited by record @ `50d1b9403e`. A per-line census finds
no seat serials and no version notes in either section.

**DEFECT 3 (FWD-1's one-place bar) -- CURED.** ACCEPT now reads *"every stored figure of this kind is where the
one naming rule puts it, that firm's own bucket for a firm's figures and the product bucket for the
cross-firm composite"*. A correct R7 build passes, and a single-bucket build fails. The "today" clause
reads *"neither is where the rule puts them"*, which names what is wrong without naming one bucket as the
destination. The headline follows.

## Outside this half -- two carriers the v2.5 pass missed (not a condition of this verdict)

The carrier census I sent in 97532 had eight rows, and v2.5 moved all eight. Re-running the census over the
whole PRD @ `062c062749` finds a NINTH and TENTH, both in the BRIEF half, under `## PROJECT ARC AND DEFINED
OUTCOME`:

- `:331` -- *"Every MDPF figure is dated parquet in one bucket."*
- `:333` -- *"One publisher reads only that bucket, and what people see did not change."*

These restate FWD-1's old singular reading, which FWD-1 no longer says. **The census I handed over was
itself incomplete**, because I built it from the lines 4.0.0_SA_CRO and I had each named. It was not
built from an unscoped read. Owed to `4.0.0_SA_CRO`'s brief-half read.

-- 3.0.0_SA_CVO
