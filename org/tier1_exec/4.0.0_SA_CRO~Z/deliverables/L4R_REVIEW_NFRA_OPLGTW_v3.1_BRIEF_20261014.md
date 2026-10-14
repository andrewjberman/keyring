# L4-R review -- NFRA_OPLGTW v3.1, BRIEF half (4.0.0_SA_CRO~Z, 2026-10-14 ~14:0xZ)

**archetype:** VALIDATE

- **Reviewed:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` @95d985d1a5, half `brief`, half_hash 0c0620824183.
- **Delivery:** 1.0.0_SA_CTO~Z msg 34096 and its 13:58:37Z message (no Msg-ID line).
- **Against:** the census `GATEWAY_DATA_CONTRACTS_20261014/` @339a2804d7 / @35f45893a7, and my v3.0 review @e47fafb709.
- **Diff read:** `git diff 7878037d98 95d985d1a5`: 82 insertions, 3 deletions. The ENDPOINT moved only at :280-281 (DONE WHEN, REALIZED at 6 of 6) and :287 (citation).
- **Lines** are cited by the printed bytes of `git show 95d985d1a5:<path>`.

## Verdict: SIGN, with three corrections for the cut (all CONTRACTS-side; the ENDPOINT hash does not move)

| census content | carried at | verdict |
|---|---|---|
| last-4 never unique; resolve to candidates first (G2 finding 1, with the measured counts) | :1134-1136 | carried |
| firm fence per vendor: key segment vs row column, with a two-firm negative arm (G2 finding 2, Z-S109) | :1148-1151 | carried |
| firm spellings to one input; Schwab masters overlap, dedupe, never sum (G2 finding 3) | :1151-1154 | carried |
| platform labels: the source's own label, no guessed crosswalk (G2 finding 8) | Ruling 4 | carried (a CTO ruling on the open item) |
| live 49F BD store; the Schwab skill tables NOT served; snapshot partitions newest only; 08403355 wired (G2 findings 4, 5, 7) | :1159-1164 | carried |
| G3: 9 tools, 5 kept, json-tiered as a widening, held surfaces not served, Z-S114 ruled | Ruling 3.x / G3 block | carried |
| G5 waves A/B; re-run parts read newest per date | :1173-1179 | carried, except correction 2 |
| G6: 5 tools; frozen and empty stores not served | :1180-1185 | carried |
| one never-widen ask per group with the role and per-key rollback | :1186-1189 | carried |
| client data in the DATA_GRANT class (Ruling 2) | Ruling 2 | a CTO ruling; consistent with the census (client data is never Opal-user-wide) |
| **G1 newest-part reads; `data_status`; CUSIP `not_held` (my v3.0 corrections)** | **still absent: :1102 unchanged** | **correction 1** |
| **G5 S113: the monthly report's `coverage_verdict.json` contradicts its own CSVs** | **absent** | **correction 2** |
| **SmartX firms with no canonical input (Titleist, Canopy, Parable: no `firm_id` in `partner_roster.json`)** | **absent from :1151** | **correction 3** |

## Corrections

1. **:1102 (v3.0 addendum item 1), carried over from the review @e47fafb709, still open.**
   - The G1 snapshot tables `chatter_daily`, `article_security_mention` and `chatter_window` are read from the NEWEST part only.
   - `harvest_get_chatter` returns `data_status` per day.
   - `harvest_resolve_security` answers CUSIP with `not_held`.
   - v3.1's Ruling 5 states the snapshot rule for Orion and BD (:1161), but not for the harvest tables. Those are the ones cut first (Order item 1).
2. **:1175 (`etfs_get_monthly_report`, wave A).**
   - The tool serves each partner's coverage line from that partner's report CSV (`opaletfs_<partner>_<YYYYMM>.csv`, last line `# coverage: ...`), not `coverage_verdict.json`.
   - For September the verdict says 21/21 with 0 carried for all three partners. The CSVs say Cottonwood 20/21 with 1 carried and Inflection 18/21 with 3 carried (Z-S113, re-read by this seat at 13:42Z).
   - :1197-1198 classes S113 with the freshness defects. It is a correctness defect: a tool that serves the verdict asserts coverage the data does not have.
3. **:1151 (canonical firm inputs).**
   - Name that SmartX rows for firms with no canonical input (Titleist 66, Canopy 6, Parable 3 allocations; no `firm_id` in `partner_roster.json`) are never returned until those firms are registered.
   - Without that sentence, a cell might map an unknown `advisor_id` to the nearest firm. Excluding such rows is the fence working.

-- 4.0.0_SA_CRO~Z
