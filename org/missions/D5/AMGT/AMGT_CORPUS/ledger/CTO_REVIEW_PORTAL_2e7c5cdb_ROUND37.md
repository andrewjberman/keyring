# AMGT_CORPUS round 37 -- CTO product-file review of portal `2e7c5cdb` (am-3) -- APPROVED for DEV

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-05 ~00:4xZ. **Ask:** `2.0.0_SA_COO~X` msg 29348 (branch `wk-AMGT_CORPUS-2-portal`, outer drain
@ff24d30809). **Authority:** round-36 analysis @4c3e3755a7, rulings 1 (page half) and 2.

## What I read

- **Against DEV:** `2e7c5cdb` CONTAINS origin/DEV `6936e92b`, so it is a fast-forward. The diff is 2 files: `modelSheet.ts` +63 and
  `tabs/ModelTab.tsx` +54/-17.
- **Gap reasons (ruling 2):** `cellReasons` per (mnemonic, year) come from the SERVED `fiscal_unresolved` reason, said in words;
  "never invented". The issuer measured 92 of 92 on 1299 HK.
- **Currency (ruling 1, the page half):** `rowCurrency` names a row's currency only when EVERY money figure in the row carries the
  same served `currency`. Mixed or unlabelled money gets a `*` and one footnote ("currency not stated by the source"). Nothing is
  converted. So until the producer cell labels every money figure, the page states the gap rather than guessing.
- **The issuer's checks on the merge:** am3_check 2/2 + 2/2, harness 12/12, typecheck clean, DSGN battery29 ALL PASS. The file is
  shared with DSGN; its checks are green.

## Verdict

**APPROVED for the DEV push.** The push takes Andrew's word (CLAUDE.md Portal), and `0.0.0_AB_MSTR~Z` pushes. The producer half of
ruling 1, a currency on every monetary figure (the re-derive under a pair), is graded separately. FWD-20's currency limb is met only
when the null-currency census reads 0 on the served blocks.
