# L4-R review, NFRA_MCPINDEX v0.20 (FWD-26) and NFRA_MCPORTAL v0.11 (FWD-30), ratified-text halves -- SIGN both (3.0.0_SA_CVO~Z, 2026-10-21 ~15:2xZ)

**Asked by** `1.0.0_SA_CTO~Z` msgs 36295 and 36303, read. They are not acked: this seat's broker tools are disconnected. The
same ask's third half, NFRA_OPLGTW v3.18, is REFUSED in `L4R_REVIEW_NFRA_OPLGTW_v3.18_RATIFIED_TEXT_20261021_Z.md`
@78774c1f94.

**Bytes reviewed:**
- **NFRA_MCPINDEX:** `git diff 7c42c0c743 1b5bf86827` on its PRD, the v0.20 addendum, read whole. It sits outside the hashed
  ENDPOINT section, so it is graded on its text, as for v0.18. HEAD equals the pin.
- **NFRA_MCPORTAL:** `git diff 9b4bbcfbb9 52d9b2a986` on its PRD, the v0.11 addendum, read whole. HEAD equals the pin.

## NFRA_MCPINDEX v0.20 FWD-26 (the light index): SIGN

- It carries Andrew's word, "index it a little just so Claude didn't have to ... pull a bunch of shit into its context".
- Each indexed table carries its folder, its meaning and a size class taken from measured rows and bytes. The size class
  decides aggregate-or-page.
- No typed tools are built.
- It is sequenced after FWD-23's tool names exist.
- **Note, not grounds:** "Claude picks the right folder and table" is graded through a model, so it needs a fixed,
  committed set of plain-words questions. A good set is one per first-cut vendor and one per size class, each with its
  expected folder and table, so a re-run grades the same thing. That is for the decomposition.

## NFRA_MCPORTAL v0.11 FWD-30 (the folder switch per person): SIGN

- It carries his entitlement word: a bucket, or a folder within one, per person.
- The proof is on, off, refused by folder name, and restored.
- The shape needs no writer change: `channels_allow` and `channels_deny` strings, with deny winning.
- W1' is unchanged: only the owner_gate principal's confirm counts.
- **The dependency, stated:**
  - FWD-30 turns on `opal-data-assets` whole for Menachem, and what that reaches is NFRA_OPLGTW FWD-24's reading.
  - This seat refused v3.18 because a whole-bucket grant there reaches `schwab/<master>/bronze`.
  - FWD-30 is safe exactly when FWD-24 states that a bucket grant never reaches bronze. Its issuer, `2.0.0_SA_COO~MP`, is
    already sequenced "after NFRA_OPLGTW's FWD-24 reading is live", so that cure lands first.

## Verdict: SIGN both ratified-text halves

-- 3.0.0_SA_CVO~Z
