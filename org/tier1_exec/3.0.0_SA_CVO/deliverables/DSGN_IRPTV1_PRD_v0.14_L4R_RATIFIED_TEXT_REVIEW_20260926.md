# L4-R review -- DSGN_IRPTV1 PRD v0.14, ratified-text half (`3.0.0_SA_CVO`)

**PRD:** `org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md` @`c236788365` (v0.14). **Half:** ratified-text,
`half_hash` `8e820005ecbd`, ENDPOINT hash `816f28fccf7c`, re-measured with `prd_signoff_lib` at the pin and matching
delivery 101514. **Prior:** SIGNED at v0.13 @`01998542eb`. **Delta:** one FWD-23 ACCEPT clause and its SOURCE. CONTRACTS
is byte-equal, and the section holds 0 seat serials.

**Verdict: REFUSE, on one phrase.** The precedence half of the new clause is exactly Andrew's word. The "every security"
half is not, and it contradicts two lines of the same section.

## R1 -- "every security shows its correct class" (BLOCKING)

FWD-23 ACCEPT, PRD :248-250: "every security shows its correct class, and a security the ETF Classifier already tags
keeps that class (VXX is Structured; GLD and PHYS are Commodities), never a lumped 'Alternatives'".

- **The ratified pin is narrower.** Andrew, record @`714ba46408`, verbatim: "securities which were already
  listed/tagged in the ETF CLassifier table should retain the same classification ... VXX is tagged to 'Structured'
  and GLD or PHYS are tagged to 'Commodities'." Its "What it binds" item 1 is a precedence rule: "for any security
  the ETF Classifier table lists, its tag there IS the security's classification." Nothing in it promises a correct
  class for every security.
- **It contradicts FWD-13**, PRD :164: "a security not yet classified says 'unclassified' rather than borrowing another
  class's colour". An untagged security reading "unclassified" passes FWD-13 and fails "every security shows its
  correct class".
- **It contradicts the section's own "Not promised" list**, PRD :259: "widening the security classifier's coverage,
  which is a data-plane act and not a cell here". A correct class for every security requires exactly that widening.

**Fix:** drop "every security shows its correct class, and". The clause becomes "a security the ETF Classifier already
tags keeps that class (VXX is Structured; GLD and PHYS are Commodities), never a lumped 'Alternatives'". That is
Andrew's rule verbatim in substance, and it agrees with FWD-13 and the "Not promised" list.

## Checked and clean

- The precedence half and its named defects match the record.
- The SOURCE cites UIR-50 and the record by pin.
- FWD-1 to FWD-22 are unchanged.
- The v0.13 observations O1-O3 (review @`9883284cf6`) stand.

-- `3.0.0_SA_CVO`, 2026-09-26 ~21:3xZ
