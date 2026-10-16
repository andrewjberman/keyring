# NFRA_OPLGTW -- AC3 of OG-ap-28 graded on six unscrubbed live answer bodies (site Z)

Author: 3.0.0_SA_CVO~Z. Round: v35. Fabric: site-z. Recorded: 2026-10-16 ~19:0xZ.
**Input:** `2.0.0_SA_COO~O` msg 35194 (acked). `deliverables/0.7.0_AE_CloudOps~Z/CVO_AC3_BODIES_OG-ap-28.json`, read whole.
- Its sha256 is `0db2c9b8be28aeac...`, re-hashed by this seat and equal to the issuer's.
- It was captured at 18:52:53Z from live `bf9d23b518`.
- It is **untracked and excluded** (`.git/info/exclude:18`), because it holds client data. This record quotes no client value
  beyond field names, row counts, dates and a masked `****<last4>`.

Masking per the file: accounts as `****<last4>`; e-mail, phone, person-name fields and the vendor account id are withheld;
numbers and security ids are as served.

**NFRA_OPLGTW.TO-OG-ap-28 AC3: PARTIAL.**

The criterion: the first 49F Black Diamond live answers, and the unit, currency and floor fields, read as an analyst would
want, with the data date stated, figures with units, and nothing merged across firms.

| marker | reading | grade |
|---|---|---|
| **data date stated** | every 49F answer states `partition_date` and `freshness_td`: holdings 10-09/4, transactions 10-16/0, allocation 10-09/4 with its profile 08-18/41, fees 10-14/1. Transactions and fees add `window_partial: true` with a plain note: "one partition read; the window is answered from that partition only". Chatter states `trading_days_behind_t1: 5` and `newest_chatter_day`. The news floor states "no articles in window ..., newest article at 2026-10-16". | MET |
| **nothing merged across firms** | one 49F account (`****2308`); `fence_excluded: 0` on every 49F denominator, against partition sizes of 108,439, 14,359, 7,345 and 3,081 | MET |
| **figures with units** | **holdings** carry `weight_unit: fraction` and `currency: null` with `currency_basis: source_absent` (honest: the source has no currency column), plus `grain: "tax lots, not positions"`. **Allocation** weights (`account_allocation`, `cash_allocation`) carry no unit field. **Transaction** `amount` and **fee** `amount` carry no currency or currency-basis field; transactions do state `amount_basis` (gross market value). | HALF MET |

**Readability defects an analyst meets (observations; the next enrichment cell):**
1. The allocation `market_value_profile` serves figures as long strings: allocations to 24 decimal places, market values to
   6. The profile also repeats identical rows.
2. A holdings weight serves in scientific notation (a 17-significant-digit value of order 1e-05), and market values carry 14 significant
   digits.
3. Holdings and allocation answer `as_of: null` beside a real `partition_date`. The date is there, but the field a reader
   looks at first is empty.
4. The allocation profile reads the opal-data-assets copy at 41 trading days behind. It is stated honestly; it is also the
   stale copy beside a current live table.
5. **A functional limit, flagged honestly:** transactions and fees asked for a 13-month window are answered from ONE daily
   partition (`window_partial: true`). An analyst asking a year of transactions gets one day's. The flag is present, but
   the answer is materially short of the question.

**Why PARTIAL, not MET:** the date and firm markers are met, and the new en-4/5/6 fields read well where they apply. But
"figures with units" holds only on the holdings rows; allocation weights and transaction/fee amounts carry none. Item 5
means the transaction and fee answers do not yet answer their window. The honest flag earns the readability, not the
answer.

## Rows

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S82",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-16T19:05Z",
    "one_line": "NFRA_OPLGTW.TO-OG-ap-28 AC3 PARTIAL on six unscrubbed live bodies: data dates (partition_date, freshness_td, window_partial notes) and firm separation (fence_excluded 0) are MET, and the news floor and chatter lag read well; figures with units are HALF MET (holdings carry weight_unit and an honest currency_basis; allocation weights and transaction/fee amounts carry none); transactions and fees answer a 13-month window from one daily partition.",
    "class": "OBSERVATION",
    "spec_asserts": "TO-OG-ap-28 AC3 (judgment): the first 49F Black Diamond live answers and the unit/currency/floor fields read as an analyst would want -- data date stated, figures with units, nothing merged across firms -- graded on a real master_admin call.",
    "world_is": "CVO_AC3_BODIES_OG-ap-28.json (sha256 0db2c9b8be28aeac, captured 18:52:53Z from bf9d23b518, untracked and excluded): holdings 34 lots, partition 2026-10-09, freshness_td 4, weight_unit fraction, currency null, currency_basis source_absent, as_of null; transactions 2, partition 2026-10-16, amount_basis gross, no currency field, window_partial true; allocation 7, weights without a unit, a profile of 24-decimal strings with duplicate rows from the assets copy at 41 trading days; fees 2, no currency field, window_partial true; fence_excluded 0 on all four; news coverage_floor message present; chatter trading_days_behind_t1 5.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.7.0_AE_CloudOps~Z/CVO_AC3_BODIES_OG-ap-28.json (read whole; untracked, excluded, not quoted beyond field names, counts and dates)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Enrichments for the issuer: (1) a weight_unit on allocation weights and a currency/currency_basis on transaction and fee amounts; (2) numeric figures served as numbers at sensible precision, no 24-decimal strings or scientific notation, and the profile's duplicate rows removed; (3) as_of set from partition_date where the source has no as-of; (4) transactions and fees answering a window from more than one partition, or the window narrowed to what was read; (5) the allocation profile read from the live table when one exists. AC3 re-grades on a capture after those land."
  }
]
```

-- 3.0.0_SA_CVO~Z
