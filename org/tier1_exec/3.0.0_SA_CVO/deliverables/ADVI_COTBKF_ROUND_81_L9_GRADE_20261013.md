# ADVI_COTBKF round 81 -- L9 grades of three judgment criteria

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-13 ~19:3xZ. **Asked by:** msg from `2.0.0_SA_COO~C2` (19:22Z), packet
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_81_DRAIN_END_20261013.md` @f57d308ab4. I read the
three criteria in the orders (`task-orders/ADVI_COTBKF.TO-CB-cc-{1,2,3}.*.md`) and the three records.
**Result: CB81cc1-AC2 PASS; CB81cc2-AC2 PASS (with one note); CB81cc3-AC2 PASS (with one note).**

## CB81cc1-AC2 -- PASS

Record: `deliverables/0.9.0_WK_ADVI_COTBKF~158/CONSUMER_READ.json`.
- **Graph first, with its age printed.** The `graph` block names the call (comp-platinum reverse, from the manifest), the cache files'
  mtime (16:51Z) and their age at writing (about 20 minutes).
- **No zero is claimed without a positive control.** The order's named control (the cot price store) returned nothing, and the worker
  said so. It then used a sibling with a known page consumer (`platinum/firm/client_directory.json`, found by CottonwoodClientsSection
  and ClientsTab). The graph's zero is scoped to the portal-platinum domain only.
- **Every search carries its denominator.** All 20 searches print files scanned; the first reads 228 hits across 77,065 files.
- **Writers are separate from consumers.** `commonwealth_fwd3_serve.py --apply` and the ARD guarded mint are listed under `writers`. The
  two `consumers` (the ARD adapter at :221-226 and the price-basis census at :292-295) are code readers, and neither is a page.
- **`consumers_found`, not `no_consumer`.** The second hop to a page (the gold ARD, then reporting-publish, then the dashboard) is
  `not_established`, because the route reads "Planned, not applied". Nothing was built, served or corrected.
- This confirms why I would not accept D2-S134 in round 80: the minted table has readers.

## CB81cc2-AC2 -- PASS, with a note

Record: `deliverables/0.9.0_WK_ADVI_COTBKF~159/STAGE_READ.json`.
- **Each stage is read from its own source.**
  - The store is read at its S3 version, 97,443,387 bytes, byte count matched.
  - The vendor Close, build and minted copy are read from their files.
  - Each security carries a `drift.days_read` list of its own reads, not round 80's figures.
- **"Served" is what is served.** The three served prefixes are listed (one object each). `served_row` is `absent` on all five chosen days,
  because none falls in the served window 2026-04-22 to 2026-06-07. That is said as absent, not filled. HON's 47 partitions were read
  as a supplement.
- **The first stage off 1.0 is named only where the ratio shows it.**
  - APH, CTVA and HON: `store_row_vs_vendor`, at a 0.5 percent tolerance.
  - KLAC and SCCO: `not_established`, with every stage `absent` and the reason stated.
- **No account id or amount.** Counts only. The per-share prices are trade prices, not account amounts. The one 8-digit run in the file
  is an object size.
- **Note:** the order sets the minted copy's source as the local `.scratch/.../fwd3_serve_r34/` copy. The S3 minted objects were only
  listed, never compared byte for byte with that local copy. So `minted_over_build = 1.0` describes the local copy; that it equals the
  served object is assumed, not read. The correction cell should read the served object.

## CB81cc3-AC2 -- PASS, with a note

Record: `deliverables/0.9.0_WK_ADVI_COTBKF~160/DATE_BOUNDS.json`.
- **The inventory has its denominators.**
  - The decompositions: 81 files read, 150 date literals.
  - The PRD: 1 file, 14 dated lines.
  - The open orders: to-check over 6,224 faces.
  - Result: 4 determinate windows and 8 `not_established`, each with the record it was looked for in.
- **The law is quoted from its record.** The floor 2012-01-01 and 365 non-client days come from
  `ANDREW_DIRECT_20261013_141xZ_BACKFILL_FLOOR_2012_AND_EARLIEST_CLIENT_RECORD.md` @82c7c92449, read by `git show origin/box/dell1`,
  with both addenda named.
- **The one moving bound moves by the law's rule.** The price store starts 2006-01-02 and moves to 2012-01-01 under `floor_2012`, 2,190
  days before the floor.
- **The not-established windows carry real reasons.** Example: the order limited the request file to its non-security fields, so the
  per-security bound could not be computed.
- **Nothing was deleted, narrowed or rebuilt.** No account id appears. The one 8-digit run is a file name's date.
- **Note:** "the minted table's range" is `not_established` here, but the parallel cell ~158 read the minted rows' span (2013-04-03 to
  2026-06-22) from the local copy. The next cut can take the range from that record.

-- 3.0.0_SA_CVO
