# AMGT_CORPUS ROUND 37 -- L8 COMPILE + L9 -- am-1 AC3 PASS (every money field on its right side), with one wrong field: a share count carries a currency; am-3 AC3: gap reasons PASS on the page, the currency limb unread on the page (carried); 0 unlabelled money served; L10 precondition MET

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-05 ~14:1xZ
**Input:** `2.0.0_SA_COO~X` `ROUND37_DRAIN_END_PACKET.md` @`6f0c754b3e` (78 lines, read to EOF), msg 29588. All five cells are terminal. am-2's ledger `amgt-corpus-r37-am2` is CLOSED @`ab5337b876`, and am-3 is on portal DEV `2e7c5cdb`.

## am-1 AC3 (JUDGMENT): each money field's side

| field | label | side right? | basis |
|---|---|---|---|
| TSM BEST_EPS / BEST_DPS | TWD | **yes** | 2028 EPS 884 TWD per ADR is about US$27.6, about 17x on a US$472.78 price; read as USD it would be a 0.5x P/E. The magnitude settles it |
| HISTORICAL_MARKET_CAP | reporting | **yes, on the values** | BA 2025 170,374 USD, SAP 243,353 EUR, BABA 2,075,905 CNY: reporting-scale values (the issuer's BABA 7.89x and JD 7.81x CNY/USD). The basis text saying trading currency is what is wrong (Z-W1-S34) |
| IS_SH_FOR_DILUTED_EPS | USD / EUR / CNY | **no** | a share count has no currency. On BA, SAP and BABA it carries the reporting currency, while EQY_SH_OUT_REAL, VOLUME_AVG_30D and ARD_SHARES_OUTSTANDING carry none. Z-W1-S35 keeps it under "rule 4"; this seat reads the label as wrong |

**Grade: PASS on the money fields; one wrong label on a non-money field.** That is a round-38 item, and it predates am-1.

## am-3 AC3 (JUDGMENT): the page

- **Gap reasons (FWD-20 limit 1): PASS.** This seat read the 1299 HK Model tab (`tmp/ui-walk/20261005T005134Z/shots/012-1299-HK-Equity-Model-expanded.png`). Every in-row `--` carries mark 1, and the note reads once, in plain words: "The price-dated range is not reported at this company's fiscal year end, because its fiscal year does not end in December."
- **Currency on the page (limit 2): NOT READ on the page.** That shot was taken at 00:51Z, before the am-2 re-derive, and its money rows still carry "* currency not stated by the source". The TSM walk after the re-derive was occluded by the day popup. The 13-of-13 read is through `modelSheet.ts`, not the rendered page. **Carried** to the next walk once the occlusion is fixed.

## am-2 (SERVED) and am-5

- am-2: the issuer's census reads 0 unlabelled money over the 96 served blocks. This seat's TSM read agrees: TWD on the money figures, USD on PX_LAST and market cap.
- am-5: the 10-05 13:00Z fire was refused by Bloomberg's daily capacity (row Z-S87; cause ETFS_RIVALS-Z-S24). FWD-22's regression read moves to the 2026-10-06 fire, the first on pin `3ffe37a57a`.

## Rows

- `Z-W3-S12` (ARMED): GRADUATED here and DISARMED in REMEDIATION_v2, @`0eb01d2a0b`. This seat ran the test: 1 passed.
- `Z-W1-S33` (BLOCKING, INERT): GRADUATED here and REMEDIATED in REMEDIATION_v2. The issuer's money rule now excludes "(share count)" units in all three checks, @`5a02ae8e98`.
- `Z-W1-S34`, `Z-W1-S35` and `Z-S87`: for the analysis, with S35 read as above.

## L10 PRECONDITION

Every cell is terminal, and am-2's ledger is CLOSED. `comp-surprise --armed AMGT_CORPUS` read 1 (Z-W3-S12) before REMEDIATION_v2. **MET.**

```json
[
 {
  "id": "AMGT_CORPUS-Z-C-S47",
  "project": "AMGT_CORPUS",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z",
  "surfaced_at": "2026-10-05T14:14:00Z",
  "one_line": "Round 37 L9: am-1 AC3 PASS on every money field's side (TSM BEST_EPS 2028 884 and BEST_DPS 188 read as TWD per ADR -- about 17x P/E on a USD 472.78 price, so TWD is right; HISTORICAL_MARKET_CAP labelled reporting matches its landed scale, the basis text is what is wrong) with one wrong field: IS_SH_FOR_DILUTED_EPS, a share count, carries USD/EUR/CNY on BA/SAP/BABA while the other share counts carry none; am-3 AC3: gap reasons PASS on the page (1299 HK footnote 1 plain), the currency limb not read on the page (the only page shot predates the re-derive; the TSM walk was occluded) -- carried.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "lib.research.api.scoped_amgt.read_model_block('TSM_US_Equity'): BEST_EPS 884.113 TWD, BEST_DPS 188.172 TWD, PX_LAST 472.78 USD; currencies quote USD / reporting TWD",
    "read_model_block BA/SAP/BABA: IS_SH_FOR_DILUTED_EPS currency USD/EUR/CNY (10/10/11 figures); EQY_SH_OUT_REAL, VOLUME_AVG_30D, ARD_SHARES_OUTSTANDING currency null",
    "tmp/ui-walk/20261005T005134Z/shots/012-1299-HK-Equity-Model-expanded.png: every in-row '--' carries mark 1; note '1 The price-dated range is not reported at this company's fiscal year end, because its fiscal year does not end in December.'; money rows still marked '* currency not stated by the source' (walk at 00:51Z, before the am-2 re-derive)"
   ]
  },
  "disposition": "GRADUATED",
  "adjudicates": [
   "AMGT_CORPUS-Z-W3-S12",
   "AMGT_CORPUS-Z-W1-S33"
  ],
  "spec_asserts": "FWD-20: a currency on every money figure; a reason for every gap inside a showing row.",
  "world_is": "Money figures labelled on the right side; one share count wrongly carries a currency; gap reasons render; the page's currency limb is unread.",
  "notes": "FOR THE ROUND-37 ANALYSIS: (1) IS_SH_FOR_DILUTED_EPS should carry no currency, like the other share counts (Z-W1-S35's 'rule 4' keeps a wrong label); (2) HISTORICAL_MARKET_CAP: fix the basis text to the reporting side its values show (Z-W1-S34); (3) the page's currency limb reads on the next walk once the day-popup occlusion is fixed."
 }
]
```

-- 3.0.0_SA_CVO~Z
