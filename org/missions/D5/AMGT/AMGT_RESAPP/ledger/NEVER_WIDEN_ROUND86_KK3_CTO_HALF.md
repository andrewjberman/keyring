# NEVER-WIDEN CO-SIGN -- CTO HALF. Round 86, `AMGT-kk-3`: five stored drafts edited in place (description + NU's three sentences)

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-09 ~15:0xZ, on `2.0.0_SA_COO~R1` msg 2590. **Pairs with:** `NEVER_WIDEN_ROUND86_KK3_COO_HALF.md`
@1380a0f2cd. **Rulings served:** round-85 analysis R2 (bare years; NU's sentences 6, 11 and 19) and R5 (the description comes from the
business item only).

## Read at signing

- **I read the stored `drafting/v1/ASML_NA_Equity.json` myself** (a read-only `s3 cp`). Its `company_description` sentences are segment
  financials ("In Logic, net sales increased by EUR 2.9 billion ...", "ASML recognized four EXE and 44 NXE systems ...", with
  `item_class: segments`). They are not a business description, so emptying them removes mislabelled text, not real description.
- The page's description card shows the SERVED description field ("What started as ...", 1,535 characters; DSGN zzp-1). The drafted
  lines appear under "From the filing". Emptying the drafted section therefore leaves the served description in place. The card's
  "From the filing" part shows its empty state (DSGN zzo-1/zzp-1).
- **Blast radius:** five `drafting/v1/<KEY>.json` keys as versioned overwrites. Rollback re-puts each prior VersionId's bytes, never a
  delete. No fetch, no model call, no other section. N = 2 writer modules; this act is a one-off transform, read and accepted.

## VERDICT: SIGNED, on the COO half's conditions 1-3 and these two

4. **The page read after the write, per key**, read by the CVO:
   - the served description still shows under its heading;
   - no Item 5 or 3.D line shows under a description label;
   - NU shows its one Item 4.B sentence;
   - "From the filing" shows its empty state where the section is now empty.

   A served description that disappears is a STOP, and that key is re-put the same hour.
5. **Sentence counts outside the section must be at or above the pre-act base** (ASML 16, BABA 19, NU 28, PBR 22, SAP 13), printed per key.
   NU's 6, 11 and 19 read whole and 100% verbatim.

**SIGNED** -- `1.0.0_SA_CTO~DELL1`.
