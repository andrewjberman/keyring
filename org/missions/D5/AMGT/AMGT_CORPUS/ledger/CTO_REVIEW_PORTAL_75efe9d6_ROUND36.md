# AMGT_CORPUS round 36 -- CTO product-file RE-review of portal `75efe9d6` (al-2 reworked) -- APPROVED for DEV

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-04 ~22:5xZ. **Ask:** `2.0.0_SA_COO~X` msg 29292. **Prior:** REWORK @934205909b (`fb1f3cbb`).

## What I read

- **Against DEV:** `75efe9d6` CONTAINS origin/DEV `1b9f553d`, so it is a fast-forward. The diff against DEV is the 3 al-2 files only
  (`modelSheet.ts` +154, `ModelTab.tsx` +64, `types.ts` +3).
- **The conflict resolution:** the import lines only. DSGN's AV-zg-5 and AV-zi-1 bodies are unchanged; "What changed" still leads.
- **ModelTab:** the V3 group's notes are one labelled line of the four header facts, then each absent line's reason ONCE, never per
  row. The text is navy (`INK_NAVY`), 13px, with no light text. Values are shown as served: a number is grouped digits, a MILLIONS
  unit says "million", and text is shown as served.
- **The four header facts** (`V3_HEADER_LABELS`) are short name, country, average daily value traded (3M) and market capitalisation.
  The 0-decimal rounding suits these two amounts. No ratio or percent passes through `v3FactValue`.
- **The issuer's checks on the merge:** al2_check 3/3 + 1/1, harness 12/12, typecheck clean, DSGN battery29 ALL PASS, DSGN r34 x3 and
  r35 changed/cloud/payload PASS, and instrument35 0/4 (equal to DSGN's own recorded base).

## Verdict

**APPROVED for the DEV push.** The push takes Andrew's word (CLAUDE.md Portal), and `0.0.0_AB_MSTR~Z` pushes.

**Carried to the round-36 analysis, not blocking DEV:** "Market capitalisation: 96,078 million" and the average daily value do not
name their currency. `CRNCY_ADJ_MKT_CAP` is in millions of that name's currency (Z-W1-S30), so a non-USD name reads ambiguously. Each
amount should carry its currency from the block.
