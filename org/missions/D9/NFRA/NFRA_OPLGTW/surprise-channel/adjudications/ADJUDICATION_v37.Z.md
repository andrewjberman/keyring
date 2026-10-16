# NFRA_OPLGTW -- OG-ap-31 live: the guard condition met; AC3 of OG-ap-31 PARTIAL; AC3 of OG-ap-28 re-graded MET (site Z)

Author: 3.0.0_SA_CVO~Z. Round: v37. Fabric: site-z. Recorded: 2026-10-16 ~22:5xZ.
**Input:** `2.0.0_SA_COO~O` msg 35282 (acked). Live `4be300110e` since 22:00Z.
- `deliverables/0.7.0_AE_CloudOps~NFRA1/CVO_AC3_BODIES_OG-ap-31.json`: sha256 `5aeca420901d2b22...`, re-hashed by this seat and equal.
  It is git-excluded, so it is not committed or quoted here beyond field names, counts and dates. Captured at 22:36:08Z.
- `CODE3_SERVED.json`: `live_commit` `4be300110e`; arms e1, e2, e3, e4 and e6 all true.

## My OG-ap-31 condition 1: the guard's three branches, MET

`CODE3_SERVED.json` arm `e4_owner_browser_guard`:
- **Owner, internal page:** no denial, with **0** store reads on the exempt call.
- **Owner, no route class:** 403.
- **Owner, consent class:** 403. `/callback` is unchanged.
- **Non-admin against the live table:** 403 on an internal page and 403 with no class.
- **Roster:** `MASTER_ADMIN_EMAILS` holds 1 entry.

The exemption reaches the owner on the four internal pages only, and every other branch keeps the record verdict.
- **Bound (the issuer's own limit):** the owner arm is an in-process stand-in built from the host's roster key, not Andrew's
  signed-in browser. Andrew's own look is his.

## AC3 of NFRA_OPLGTW.TO-OG-ap-28, re-graded: MET (supersedes v35's PARTIAL, Z-C-S82)

On the new release's bodies (holdings, transactions, allocation and fees for one 49F account):
- **Data date stated:** MET. `as_of` is now set on every answer (holdings and allocation from the partition date, which was
  `null` before), beside `partition_date` and `freshness_td`.
- **Figures with units:** MET.
  - Holdings weights carry `weight_unit: fraction`.
  - Transactions and fees carry `currency` with `currency_basis: source_absent`, per row and on the envelope. This is an honest
    absence: the source has no currency column.
  - Allocation carries `weight_unit: null` with `weight_unit_basis: not_established`, an honest absence because the live scale
    was not measured (Z-S313).
  - Figures serve as JSON numbers: weights at 6 decimals, money at 2. The allocation profile's duplicate rows are removed (6),
    and no 24-decimal strings or scientific notation remain.
- **Nothing merged across firms:** MET. `fence_excluded: 0` on all four denominators.
- **Residual, not grounds:** holdings `unit_cost` still serves at full float precision. It is a cost figure the rounding rule
  did not reach.

## AC3 of NFRA_OPLGTW.TO-OG-ap-31: PARTIAL

The criterion: "the 49F transactions and fees windows and figures read as an analyst would want (the window answered, units
and currency stated or honestly absent, numbers readable)".
- **Units and currency stated or honestly absent:** MET, as above.
- **Numbers readable:** MET. Two-decimal money, `total_in_window` for fees, and transaction amounts with `amount_basis` (gross).
- **The window answered: NOT MET, honestly flagged.** A 13-month request returns:
  - transactions: `partitions_in_window` 334, `partitions_read` 60, the newest 60 (dates from 2026-08-18), `window_partial: true`;
  - fees: 395 in the window, 60 read, partial.

  The note names the cap (`MAX_WINDOW_PARTITIONS = 60`) and `partitions_read_dates` lists exactly what was read. So the
  analyst is told the truth: about two months of a thirteen-month question. That is far better than v35's single day. It is
  still not the window answered.
- **Exact-duplicate removal reads as intended:** 355 exact duplicates were removed from the transactions read, and a row is
  dropped only when every field equals an earlier row.

**What closes it (the issuer's design call):** the window has to be answered in full or narrowed up front. Options:
- raise the cap where a 13-month window fits a call's budget;
- a continuation token over the remaining partitions;
- read a pre-aggregated or monthly source;
- or narrow the requested window to what one call can read, and say so before the rows.

The flag already in place stays.

## Rows

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S84",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-16T22:55Z",
    "one_line": "On live 4be300110e: NFRA_OPLGTW.TO-OG-ap-28 AC3 re-graded MET (as_of set, units and currency stated or honestly absent, numbers at fixed precision, fence_excluded 0); NFRA_OPLGTW.TO-OG-ap-31 AC3 PARTIAL (units and numbers MET; the 13-month window is answered from the newest 60 of 334 transaction and 60 of 395 fee partitions, about two months, honestly flagged); my OG-ap-31 guard condition is MET (e4: owner internal page passes with 0 store reads, every other branch 403).",
    "class": "OBSERVATION",
    "spec_asserts": "TO-OG-ap-28 AC3 (data date, figures with units, nothing merged across firms); TO-OG-ap-31 AC3 (:64: the window answered, units and currency stated or honestly absent, numbers readable); my OG-ap-31 half condition 1 (the guard's three branches on the served read).",
    "world_is": "CVO_AC3_BODIES_OG-ap-31.json (sha256 5aeca420901d2b22, 22:36:08Z, live 4be300110e, git-excluded): holdings as_of 2026-10-09, weight_unit fraction, currency_basis source_absent; transactions currency/basis present, partitions_in_window 334, read 60, window_partial true, exact_duplicates_removed 355; fees 395 in window, 60 read, partial, total_in_window present; allocation weight_unit null with not_established, profile duplicates removed 6; fence_excluded 0 on all four. CODE3_SERVED.json e4: owner internal_page no denial and 0 store reads; owner no-class 403; owner consent 403; non-admin internal and no-class 403; roster 1.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-C-S82"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.7.0_AE_CloudOps~NFRA1/CVO_AC3_BODIES_OG-ap-31.json (read; git-excluded, not quoted beyond names, counts and dates)",
        "deliverables/0.7.0_AE_CloudOps~NFRA1/CODE3_SERVED.json (arms, e4 arm_counts, limits)",
        "task-orders NFRA_OPLGTW.TO-OG-ap-31 :64 (AC3 text)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "OG-ap-28 AC3 is closed MET by this row (supersedes Z-C-S82's PARTIAL). OG-ap-31 AC3 stays PARTIAL until the 13-month window is answered in full or narrowed up front (a larger cap, a continuation, a monthly source, or a narrowed window stated before the rows). Residual: holdings unit_cost at full precision."
  }
]
```

-- 3.0.0_SA_CVO~Z
