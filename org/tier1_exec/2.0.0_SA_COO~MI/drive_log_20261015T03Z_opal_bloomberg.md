# Drive log 2026-10-15 ~00:40Z to ~03:15Z -- 2.0.0_SA_COO~MI, NFRA_MCPINDEX (box/sitez, opal_bloomberg)

Stage: round 16 closed MAY-CLOSE; the round 12 release MX-r-13 waits on NFRA_OPLGTW. Lease FULL. Push state: on origin @439b74862381 (ls-remote read, equal to local HEAD at 03:13Z).

## Acts

- Round 16 drained. MX-c-17 merged `d0e04b517d` (worker ~41), MX-c-16 merged `7406f93e89` (worker ~40); tool-index link to the denied aum row removed `9838864288`; both orders complete `575e55fd43`. On the merged tree: c16.AC1-3 PASS (difference control 390 pairs, deny->serve=0, serve->deny=1 = the aum row for opal-internal), c17.AC2 PASS (14 of 226 table rows differ, exactly the 14 enriched), c14.AC1-2 and c15.AC1 PASS, atom_decomposition tests 189 passed, gateway failing-ID set equals the baseline of 48.
- The round 16 catalog landed through worker ~38 under MX-c-14 A10: `bacc8d7238` (the gate graded 0 literals on a prose-only diff, so no CATALOG-EXEMPT line; ruled benign, row Z-W38-S16). MX-c-14 complete `332923310a`. COO~O told.
- Round close first read REFUSED on worker ~41's AC2 FAIL row: the order's expect text (216) was the issuer's error, the check counts 226. Order corrected (`063ba69a3e`), the instance regraded by the worker (A1, `7be487a7cd`); `round-close-check --round 16` reads MAY-CLOSE. MX-c-17 complete `acccb377a8`. The project row stays EXECUTING: MX-r-13 is open.
- `portal_lookup.py`: the legacy `mdpf` channel retired and the `mdpf-platinum` note corrected (`b4c387cd2f`), this seat measured PERMIT on that lane (0.0.0_AB_MSTR~Z msg 34306).
- `r13.AC4` (the round 13, 14, 16 catalog live on the host: version 0.5, 78 harvest, 216 table rows, md5 equal to the tree, every read_tool served) written and dry-run: base FAIL as expected, planted arms 5 of 5 (`734b29bbb8`).
- `mdpf_get_category_views`: COO~O took the table-row route as OG-pt-5 (msg 34294); no certified-entity round.
- /keep-driving ON (Andrew-direct ~02:0xZ, relayed 34308): CONFIRMED to 0.0.0_AB_MSTR~Z, cron 31dd41d8 hourly :07.

## Open

- MX-r-13 PHASE A GO: behind OG-ap-17 (pending), OG-ap-19 and OG-ap-20 (staged); OG-ap-18 is complete and live at 047f11aa99. At the GO: regenerate the harvest and table rows against the live ref's tool census, re-emit, land the catalog through a worker, amend MX-r-13 (A3: ships the catalog and integration blobs, adds r13.AC4).
- G5 wave A rows are in the catalog; COO~O's et-1 and et-2 workers build on them.
