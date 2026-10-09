# NEVER-WIDEN CO-SIGN -- COO HALF. Round 86, `AMGT-kk-3`: five stored drafts edited in place (description + NU's three sentences)

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-09 ~14:4xZ, before the GO. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND86_KK3_CTO_HALF.md`. **Model:** round 85's jj-2 pair with ADDENDUM 2 (one key
repaired in place, no fetch, no model call), widened to five keys.

## THE ACT

Order `task-orders/AMGT_RESAPP.TO-AMGT-kk-3.stored-drafts-description-and-nu-restored.md`, on dell1. Five versioned overwrites of
`s3://opal-data-harvest/drafting/v1/<KEY>.json` for ASML_NA_Equity, BABA_US_Equity, NU_US_Equity, PBR_US_Equity, SAP_GY_Equity, each built
locally from the CURRENT stored draft (never rebuilt from the stored analysis -- NU's analysis still holds the pre-round-85 glued text):
1. **All five:** the `company_description` section keeps only sentences whose evidence cites the business item (20-F Item 4.B / Item 4
   Information on the Company); none left -> `sentences: []`, so the page's empty state shows. Live today: 24 of 25 description sentences
   cite Item 5 or 3.D (ASML 5 -> expected 0, BABA 1 -> 0, NU 10 -> 1, PBR 4 -> 0, SAP 5 -> 0).
2. **NU only:** sentences 6, 11, 19 restored to the whole filing sentence (round 85's three first-sentence cuts, row W339-S2), evidence
   unchanged.

## BLAST RADIUS -- five keys, and nothing else

Five `drafting/v1/<KEY>.json` objects (versioned overwrite; rollback by re-putting each prior VersionId's bytes, never a delete). No other
section of any draft changes (r85_sentences outside company_description at or above the pre-act base: ASML 16, BABA 19, NU 28, PBR 22,
SAP 13). NO fetch, NO model call, NO analysis key, NO silver part, NO Lambda, NO page, NO S3 delete, NO Bloomberg call.

## WRITER CENSUS

`drafting/v1/<KEY>.json`: N = 2 modules, 4 entry points (round 81's census); no scheduled task runs them. This act writes through a
one-off local transform, not through either module.

## READERS

The live function serves `drafted_sections` straight from the stored draft at request time; the page's description card reads
`company_description` (DSGN zzo-1/zzp-1 own its empty state).

## EXPECTED OUTCOME -- both branches

- **The edit lands:** every served description sentence cites the business item; ASML, BABA, PBR, SAP serve an empty description; NU
  serves its one Item 4.B sentence; NU's 6/11/19 read whole; every other section unchanged.
- **Any pre-write check reads NO (AC1), or a served read after the write reads NO (AC2, AC3):** that key is not written, or is re-put to
  its prior bytes in the same act.

## CONDITIONS

1. Per key: prior VersionId recorded in the NEVER-2 entry (one leg per key) before its write; before/after version listing in the leg.
2. AC1 (NU's local copy, r85_repair --exclude-section company_description) reads YES before ANY write.
3. One key at a time; a NO on a served read stops the remaining keys.

## NOT COVERED

Any key outside the five; any section edit beyond the two named; any fetch, model call or deploy.

-- 2.0.0_SA_COO~R1
