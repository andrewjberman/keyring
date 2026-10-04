# AMGT_CORPUS ROUND 36 -- L8 COMPILE + L9 -- al-2 AC3 PASS (the V3 lines and their reasons read as plain words); al-3 AC2 PASS (24 verdicts and the TSM currency count reproduce), with a scope correction: the missing currency label also hits 68 BASE money figures on TSM, not only the 52; L10 precondition MET

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-04 ~23:5xZ
**Input:** `2.0.0_SA_COO~X`'s `ROUND36_DRAIN_END_PACKET.md` @`3d5f1e2b7e` (read to EOF), msg 29328.
- al-1, al-2, al-3 and al-5 are terminal.
- al-4 is CARRIED, as a named read on the 2026-10-05 13:00Z fire (CTO msg 29322).

## 1. al-5 (WORLD) -- live read

`aws lambda get-function-configuration opal-amgt-scoped-api`: CodeSha256 `2rFeF57lMh8M...`, LastModified 2026-10-04T22:42:11Z, memory
1769, Active. This equals the ledger's L2 (`amgt-corpus-r36-al5`, CLOSED @`e2790c8b2b`).

## 2. al-2 AC3 (JUDGMENT): "a PM reads the V3 lines on BA's and 1299 HK's Model tab, and each reason reads as plain words"

This seat read the walk shots, BA `tmp/ui-walk/20261004T224710Z/shots/019-BA-US-Equity-Model-expanded.png` and 1299 HK
`tmp/ui-walk/20261004T225046Z/shots/012-1299-HK-Equity-Model-expanded.png`, on the candidate now on portal DEV `75efe9d6` against the
redeployed API.

On 1299 HK:
- **The group.** "VALUATION, RETURN AND BALANCE-SHEET LINES" follows "EBITDA AND MARGIN HISTORY". Every row is a plain-English name
  with its unit in brackets: "Total assets (millions)", "Average enterprise value to trailing EBIT (multiple)", "Return on equity,
  normalised (%)", "Market capitalisation at the fiscal year end (millions)".
- **The facts line.** "Company short name: AIA; Country: HONG KONG; Average daily value traded (three months): 2,079,092,000; Market
  capitalisation: 715,988 million."
- **The reason.** "Lines with no figure: Bloomberg returned no value for this line for this company." Under it, a footnote names the
  fully-absent lines in words (Goodwill, Other intangible assets, Shares outstanding as reported, Total current liabilities, ...).

On BA, the 9,761-px shot is too tall to read row text at the scale this seat viewed it. Its layout shows the same group position.
BA's fiscal reasons are 0, per AC1's control (`al1 build 1/1 control 1/1`: BA 0/0), so BA has no reason line to grade. BA's row text
is NOT read here.

**Grade: PASS.** Every reason the page prints is a sentence a PM reads without a glossary: no mnemonics, codes or status tokens.

The packet's two limits are real, but they are FWD-20 scope, not AC3 failures. AC3 grades how the reasons the page gives read, not
which gaps it gives reasons for:
1. A gap inside a showing row (1299 HK's `--` in 2016, 2017 and 2022) has no reason.
2. Money lines name no currency.

Both go to the round-37 list. Limit 1 binds FWD-20's "a row that still cannot show says why" in its narrow form.

## 3. al-3 AC2 (JUDGMENT): "each verdict is right"

Read: `deliverables/0.9.0_WK_AMGT_CORPUS~2/R36_UNITS_JUDGMENT_READ.md` (84 lines).
- **The family table (24 rows): RIGHT 19, WRONG 0, CANNOT-TELL 5. Each verdict holds.**
  - The cross-reads are sound: SAP ROE 7161/45073 = 15.9 against 15.97 served; SAP EPS 7161/1175 = 6.09 against 6.14; TSM total equity
    5.46 trillion TWD.
  - The five CANNOT-TELLs are true absences. On TSM this seat read IS_EPS 0 figures and IS_SH_FOR_DILUTED_EPS 0 figures.
  - BA EPS 2.49 against 2.93 is the preferred-dividend gap, and the read names it.
- **The TSM currency count reproduces exactly.** Through `read_model_block("TSM_US_Equity")` (raw 20261004T130954Z; currencies quote
  USD, reporting TWD, mixed True), the 52's 167 figures all carry `currency` null with basis `invariant`:
  - 91 MILLIONS + 1 ABSOLUTE = **92** monetary, all wrong;
  - 40 RATIO + 30 PERCENT + 3 TEXT + 2 DATE = **75** non-monetary, all right.

**Grade: PASS on every verdict, with one scope correction to the read's closing note.**

**The correction (it widens round-37 candidate 1).** The read says the fix is to label the 52 "the way the older MILLIONS fields already
get it". On TSM, only **60 of the 128** older MILLIONS figures carry `currency` TWD. **68 carry null / invariant too:**
- NET_INCOME, BS_TOTAL_LIABILITIES, BS_CASH_NEAR_CASH_ITEM, IS_ADJUSTED_GROSS_PROFIT and IS_ADJUSTED_OPERATING_INCOME, 10 years each;
- BEST_SALES, BEST_EBITDA, BEST_EBIT, BEST_NET_INCOME, BEST_CAPEX and BEST_ESTIMATE_FCF, 3 each;
- NET_DEBT, 1.

So on a mixed-currency block, the unlabelled-money defect covers base fields as well as the 52. A remedy scoped to the 52 alone would
leave 68 TSM figures unlabelled. Row Z-W2-S20's scope should read "every monetary figure", and the remedy's own control should count
the base fields.

## 4. Rows and L10

- `Z-W2-S20` (OBSERVATION, INERT) is open for the analysis, widened as above.
- `python .tools/comp-surprise.py --armed --project AMGT_CORPUS`: ARMED 0, 165 items, 98 remediation rows, 0 defects.
- al-4 is CARRIED by the CTO's ruling, as a named read with its expectation stated in the packet.

**L10 precondition: MET.**

```json
[
  {
    "id": "AMGT_CORPUS-Z-C-S46",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-04T23:50:00Z",
    "one_line": "Round 36 L9: al-2 AC3 PASS (1299 HK's V3 group, facts line and 'Lines with no figure: Bloomberg returned no value for this line for this company' read as plain words); al-3 AC2 PASS (24 verdicts hold; TSM 92 monetary / 75 non-monetary reproduced); scope correction: 68 of 128 older TSM MILLIONS figures (NET_INCOME, BS_TOTAL_LIABILITIES, BEST_* ...) also carry currency null on the mixed block, so Z-W2-S20's remedy must cover every monetary figure, not only the 52.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "tmp/ui-walk/20261004T225046Z/shots/012-1299-HK-Equity-Model-expanded.png and tmp/ui-walk/20261004T224710Z/shots/019-BA-US-Equity-Model-expanded.png, read by 3.0.0_SA_CVO~Z",
        "lib.research.api.scoped_amgt.read_model_block('TSM_US_Equity') raw 20261004T130954Z: the 52 -> 91 MILLIONS + 1 ABSOLUTE currency null; older MILLIONS -> 60 TWD 'reporting (EQY_FUND_CRNCY)', 68 null 'invariant'",
        "aws lambda get-function-configuration opal-amgt-scoped-api: CodeSha256 2rFeF57l..., LastModified 2026-10-04T22:42:11Z"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A compile record: both judgment criteria are graded here; the widened currency scope is carried on row Z-W2-S20 for the round-36 analysis.",
    "spec_asserts": "FWD-20: every row the sheet carries shows a figure, or says why in plain words.",
    "world_is": "The V3 lines render with plain-word reasons for fully absent rows; in-row gaps and money currencies are not yet worded.",
    "notes": "Round-37 candidate 1 (currency labels) must count base monetary fields too."
  }
]
```

-- 3.0.0_SA_CVO~Z
