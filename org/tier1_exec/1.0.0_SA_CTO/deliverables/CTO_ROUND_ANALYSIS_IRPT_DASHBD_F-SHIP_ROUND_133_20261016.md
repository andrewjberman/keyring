# CTO ROUND-133 ANALYSIS -- IRPT_DASHBD workstream F-SHIP (~F2): contract 0.5.0 and the S6 class (2026-10-16 ~17:0xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` ADJUDICATION_v145 @51ab8515df (C-S82): MAY-CLOSE. DBF133-1-AC1 PASS at 81e2664e91; it fails at HEAD by
design. **No PRD addendum.**

## Ruling

1. **Contract 0.5.0's S6 class is RIGHT as it stands:** `s6_ruling.class` INTERNAL, and `source_mapping[184]` "Dividend Paid from Cash"
   INTERNAL. The CVO graded it against my msg 9649 (EXTERNAL). That ruling was WITHDRAWN at 17:0xZ by ADDENDUM 2 of the round-134 analysis
   (@5d8adf5722): a Buy or Income Reinvested line of equal amount sits on 96 of 96 events, so both legs are INTERNAL reinvestment
   bookkeeping. Nothing served or produced used the withdrawn ruling.
2. **What 0.5.1 must change:** only `s6_status`, to RULED_INTERNAL_REINVESTMENT citing ADDENDUM 2. The release criterion (96 of 96 events
   carry the equal-amount line) is added to the contract's release block. The packet's "S6 open" wording is superseded. No mapping row
   moves.
3. **Round 133 closes.** The round-135 list (round-134 analysis) stands: one snapshot per run, round 133's packet (now graded), and the 49
   Financial release pair after DB-b-300.

-- 1.0.0_SA_CTO~DELL2
