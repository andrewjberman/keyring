# ANDREW-DIRECT 2026-10-04 ~20:0xZ at the laptop 0.0.0_AB_MSTR terminal -- promote portal DEV c7bc52c8 to PROD

## The question put to him, and his answer

- **Question:** "Promote portal DEV c7bc52c8 to production now?"
- **Answer, verbatim:** "Yes, promote (Recommended)"

## What the word covers

- **The commit:** portal DEV c7bc52c8, 17 commits past PROD dbd29c6320 (v2.1.198). 16 are `2.0.0_SA_COO~D`'s and 1 is
  that seat's DEV-forward merge 822ce891. The ask was `2.0.0_SA_COO~D` msg 104942, corrected by 104943.
- **Contents:** the DSGN_REBRND W3-S5 state fixes, the StatusPanel change (CTO batch 238), and the DSGN_IRPTV1 fixes.
- **CI at the word:** `CI - Build & Validate` success on c7bc52c8.

## NOT read into the word

- Portal DEV moved to 7b053135 after the question was put (`2.0.0_SA_COO~D` msg 104946). That commit was not in the
  question and its CI was still running. The promote merges c7bc52c8 by its hash, never live `origin/DEV`; 7b053135
  waits for the next promote and its own word.
