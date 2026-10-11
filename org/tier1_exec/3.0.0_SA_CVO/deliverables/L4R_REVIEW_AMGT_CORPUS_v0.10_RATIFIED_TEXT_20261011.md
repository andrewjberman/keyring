# L4-R review, AMGT_CORPUS PRD v0.10, ratified-text half -- SIGN (3.0.0_SA_CVO, dell1, 2026-10-11 ~16:0xZ)

**Delivery:** `1.0.0_SA_CTO~DELL1` msg 3964. **Signing for:** `3.0.0_SA_CVO~Z` (owed lane, no live session), at the CTO's request
on this fabric. **Bytes reviewed:** `org/missions/D5/AMGT/AMGT_CORPUS/prd/AMGT_CORPUS_PRD.md` @9794728d6e (clean against HEAD).
ratified-text half_hash a9effe484daaf8dd219bd96182e96d46c3876e9f3112667e77d71b8056454a84 (ENDPOINT hash 7662246f2f39...).
**Read:** `git show 9794728d6e` on that file, whole: three hunks (header `prd_version` v0.9 -> v0.10; FWD-15 DONE WHEN; ADDENDUM E appended).
**Prior review:** `L4R_REVIEW_AMGT_CORPUS_v0.9_CURED_RATIFIED_TEXT_20261007_Z.md` (SIGN).

## Verdict: SIGN

**The ENDPOINT change (FWD-15) is a relocation, not a weakening.**
- The old DONE WHEN: "both render cited on the header posture line and the Posture tab".
- The new DONE WHEN: "both render cited on the Posture tab beside the machine verdict".
- The ACCEPT is unchanged ("The team's posture informs the reader without becoming the judgment"), and so is the byte-unchanged
  machine-verdict arm. The new wording binds a place ("beside the machine verdict") the old one did not.
- The ground is real, read by this seat. Portal commit `29eb8ed4` ("AV-zzk-3: tabs in the first screen, identity once, plumbing out
  of the face") is an ancestor of portal `origin/DEV`, and it removed the header posture line. The CTO's review
  `ledger/CTO_REVIEW_R46_AV_2_PORTAL_CANDIDATE.md` exists. An outcome that required a render on a removed element would be
  unmeetable by design, and the design project governs the face.
- Evidence it is meetable as worded: this seat's round-46 L9 (ADJUDICATION_v61 @80f1356183) read both items rendering cited on the
  Posture tab, beside an unchanged verdict.

**The DEC on FWD-20 (not an ENDPOINT change) narrows nothing the outcome promised.**
- It reads "every row the team's sheet carries" by row class: FIGURE 3,381 + HEADING 316 + CONTROL 62 = 3,759.
- A CONTROL row is counted but not shown as a figure.
- A vendor field-code label must render as the vendor's description, never the code (row D1-S5).
- Consequence, carried for grading: on this reading, this seat's row C-S45 is a FWD-20 defect until round 47's cell lands. On live
  VNcX9ntm, EQY_FUND_YEAR renders as a heading on 32 of 32 workbooks, and BEST_FPERIOD_OVERRIDE renders as a figure on 29 of 32.

**Nothing else moved:** every other outcome and every contract are byte-identical outside the three hunks.

-- 3.0.0_SA_CVO
