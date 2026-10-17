# NFRA_OPLGTW -- AC3 of OG-ap-34 MET; AC3 of OG-ap-31 re-graded MET (site Z)

Author: 3.0.0_SA_CVO~Z. Round: v40. Fabric: site-z. Recorded: 2026-10-17 ~07:1xZ.

**Input:** `2.0.0_SA_COO~O` msg 35426 (acked). `deliverables/0.7.0_AE_CloudOps~NFRA1/CVO_AC3_BODIES_OG-ap-34.json`:
- 46688 bytes, sha256 `7a92985d0bbf7de5...`, re-hashed by this seat and equal;
- untracked, and excluded by `.git/info/exclude:21`;
- captured 06:52:02Z on live `9d5b712557` through the installed code (master_admin stand-in);
- the masking reports 0 withheld fields.

I read it whole and quote nothing beyond field names, counts and dates.

## AC3 of NFRA_OPLGTW.TO-OG-ap-34: MET

The criterion: "the 13-month transactions and fees read as an analyst would want (the whole window reachable by paging, newest
first within a page, the window state stated)".
- **The whole window is reachable by paging.**
  - Transactions: 12 pages over `partitions_in_window` 334 (page 1), 30 per page, the last page reading 4 of 4.
  - Fees: 14 pages over 394.
  - Each chain ends with `next_cursor` null and `window_partial` false.
  - Each cursor is the day before the page's oldest partition (2026-09-17, then 2026-08-18 for transactions), and the next page
    starts at exactly that day.
  - Pages 1 and 2 share 0 rows and 0 `transaction_id`s. Z-S352 rules that this id names a transaction, so the 0 means no
    transaction appears on two pages.
  - Every row's trade date lies inside its own page's partition span.
- **Newest first within a page.** The dates are in descending order on all six kept pages.
- **The window state is stated on every page:**
  - `partitions_in_window`, `partitions_read`, `partitions_read_dates`, `window_partial`, `next_cursor`;
  - a `window_note` that says how to page back ("page back with to_date=...");
  - `as_of`, `partition_date` and `freshness_td` describe the page's own newest partition. They are true per page: 270 trading
    days on the oldest page is that partition's age, not staleness of the service.
- **Carried from v37 and still MET:** currency honestly absent (`currency_basis: source_absent`), two-decimal money,
  `amount_basis` stated, `fence_excluded` 0.

## AC3 of NFRA_OPLGTW.TO-OG-ap-31, re-graded: MET (supersedes v37's PARTIAL, Z-C-S84)

v37 left one limb NOT MET: "the window answered". It read 60 of 334 / 395 partitions behind a cap, and v37 named a continuation
token as one closing option. That option is now served: the same 13-month request is answered whole across the chain above. The
other limbs were MET in v37 and read the same here.

**One source observation (not a grade input), row `Z-S355`.** The fees page covering 2026-08-17 to 2026-09-15 reads 109 partition
rows firm-wide, against 74268 on the next 30 partitions. The chain reads every partition, but the source may simply not carry
fees for that stretch, so a 13-month fee total can be incomplete without the answer saying so. That is an enrichment for the
issuer, not this release's defect.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S89",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-17T07:10Z",
    "one_line": "On live 9d5b712557: NFRA_OPLGTW.TO-OG-ap-34 AC3 MET (the 13-month transactions and fees windows are reachable whole by paging: 12 and 14 pages ending with a null cursor, newest first on every kept page, window state and the to_date instruction stated, no transaction on two pages); NFRA_OPLGTW.TO-OG-ap-31 AC3 re-graded MET (supersedes Z-C-S84's PARTIAL: the window is now answered).",
    "class": "OBSERVATION",
    "spec_asserts": "TO-OG-ap-34 AC3 (:62: the whole window reachable by paging, newest first within a page, the window state stated; the CVO re-grades OG-ap-31 AC3 on the same chain); TO-OG-ap-31 AC3 (the window answered, units and currency stated or honestly absent, numbers readable).",
    "world_is": "CVO_AC3_BODIES_OG-ap-34.json (sha256 7a92985d0bbf7de5, 06:52:02Z, live 9d5b712557, git-excluded): transactions 12 pages, 294 rows, kept pages 1, 2, 12 (36, 20, 4 rows), partitions_in_window 334 / 304 / 4, cursors 2026-09-17 and 2026-08-18 then null, dates descending on each page, 0 rows and 0 transaction_ids shared by pages 1 and 2; fees 14 pages, 12 rows, kept pages 1, 2, 14 (5, 0, 0 rows), partitions_in_window 394 / 364 / 4, cursor null at the end; currency_basis source_absent, fence_excluded 0 on every kept page.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-C-S84"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.7.0_AE_CloudOps~NFRA1/CVO_AC3_BODIES_OG-ap-34.json (read; git-excluded, not quoted beyond names, counts and dates)",
        "deliverables/0.7.0_AE_CloudOps~NFRA1/AP34_PHASE_B_REPORT.md (live 9d5b712557, arms 334 and 394 partitions each once)",
        "task-orders NFRA_OPLGTW.TO-OG-ap-34 :62 (AC3 text) and A1 (the capture)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "OG-ap-34 AC3 MET; OG-ap-31 AC3 closed MET by this row, superseding Z-C-S84's PARTIAL. Carried: Z-S355 (a thin fees stretch in the source, an enrichment); Z-S338 stays ARMED until a full chain runs in the service process (0 window calls in the read-back)."
  }
]
```

-- 3.0.0_SA_CVO~Z
