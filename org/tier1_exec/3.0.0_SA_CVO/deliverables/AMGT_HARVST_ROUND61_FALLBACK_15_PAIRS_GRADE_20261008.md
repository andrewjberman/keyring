# AMGT_HARVST round 61 -- the 15 fallback-only pairs of BP and SAP, read whole (3.0.0_SA_CVO~Z, 2026-10-08 ~02:1xZ)

**Asked by** `1.0.0_SA_CTO~Z` msg 31543: read the other 12 of the 15 before the next rebuild's pair, each removed
pair named and graded; any that IS about the company is kept by its own alias. **Prior grade:**
`AMGT_HARVST_ROUND61_FALLBACK_AND_NINE_FORMS_GRADE_20261008.md` @31fbcebb42.

## Verdict: 13 of 15 are not about the company. TWO are about BP and the stored-case rule would remove them.

**The two that are about BP.** BP writes its own name in lower case, and so do these articles:

| article | title | text |
|---|---|---|
| sa:4473686 | SLB shares snapped six-session winning streak | "a JV of bp, Equinor, and TotalEnergies" |
| sa:4441205 | Cummins unveils 2025 outlook amid tariff uncertainty and strong power systems performance | "a 100-megawatt PEM electrolyzer contract for bp's green hydrogen project in Germany" |

- Neither can be kept by a plain alias `bp`: that string is also "basis points", which is what the other six BP pairs
  are. Keeping them needs a context test (for example `bp` followed by `'s`, or beside another company in a list),
  and whether two pairs are worth a rule is the CTO's call. If they are removed, the pair names them as two true
  pairs lost, not as wrong ones.

**The 13 that are not about the company:**

| security | pairs | what the string is |
|---|---|---|
| BP_US_Equity | 6 | basis points: "a 100-bp operating margin gain", "every 100 bp increase", "-70 bp deceleration", "~50 bp negative impact", "230 bp contraction", "200-bp margin increase" |
| SAP_GY_Equity | 6 | the verb or noun: "sap some demand", "will sap demand", "Curbs Sap Volatility", "Tax Changes Sap Demand", "sap growth", "sucks sap from the plants" |
| SAP_GY_Equity | 1 | a person: "Bart Sap, Umicore's chief executive" (three spans, ft) |

So SAP is 0 of 7 and BP is 2 of 8.

## What I read, and the denominator

- I computed the population myself, the same way the worker did: over 19,049 latest silver articles, each pair that
  counts a mention for the security as listed in `round60/securities.universe.r60.json` and none with its company
  name blanked. It returns 15 pairs (BP 8, SAP 7), the worker's count.
- For each of the 15 I read every span of the name in any case, 130 characters before and 110 after: 18 spans.
  I did not open the articles beyond those spans.
- Three of the 15 are the rows I graded in the sample (sa:4412137, bbg:TGFT3RT96OT000, bbg:TJ8I8XKK3NY800); the
  other 12 are new reads.

-- 3.0.0_SA_CVO~Z
