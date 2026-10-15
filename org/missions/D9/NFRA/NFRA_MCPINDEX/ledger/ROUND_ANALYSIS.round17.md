# NFRA_MCPINDEX -- ROUND 17 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-15 ~20:4xZ

**Answers:** `3.0.0_SA_CVO~Z`'s slug, msg 34578, `surprise-channel/remediations/REMEDIATION_v11.md` @4c130326ff.
- L8: `adjudications/ADJUDICATION_v12.md`.
- **Issuers:** `2.0.0_SA_COO~MI` (workstream ASSETS) and `2.0.0_SA_COO~MI2` (workstream RESEARCH), per PRD v0.17.
- **PRD:** v0.17 (@532d1e68bb, item 4 corrected @b2cc19d18e). No further addendum is needed.

## 1. Round 17, as read

4 of 4 orders complete, MAY-CLOSE, live at `c4c106aea1` (MX-r-14).

| item | grade | why |
|---|---|---|
| FWD-22, catalog side | **REALIZED on this project's side** (Z-C-S59) | 304 of 304 rows tagged; every `read_tool` is deployed, or null with its gap owner; a plain-words read is recorded for each landed group, G2 and G6 included |
| Z-C-S57 | REMEDIATED | the 44 rows have tags, and both discover reads are recorded |
| F1 firm widening | own-firm only | all 24 labels match the measured firm; leaks 0 |
| Z-C-S61 | OPEN, a quality item | the 44 `inferred` tags are mechanical fragments, not words a person would type |

**The finish line moved under this grade.** Andrew's word at ~18:4xZ (PRD v0.17) makes FWD-22's done for this project:
- C-GROUP on every in-scope row;
- a live `read_tool` on every in-scope row;
- by 2026-10-16 ~22:00Z.

"REALIZED on this project's side" holds for the census catalog as it stands. The v0.17 finish is graded at round 18's
close, not here.

**One line in the slug is stale.** It says "G2 readers (OPLGTW client_* cells) remain uncut". They were cut at 17:2xZ
(`OG-cl-1..6` @6fc29c2dbf), and 5 of 8 build cells are verified as of 20:30Z (COO~O msg 34573).

## 2. Rulings

1. **Z-C-S61 is round 18's.** Each workstream curates the tags on its OWN files: ASSETS for the assets and bd rows, RESEARCH
   for the rest. Tags come from the census contracts' business meaning and example questions, marked `curated`. It closes
   at 0 of the in-scope rows carrying `inferred`.
2. **SmartX stays `firm: multi` in C-GROUP**, even though the CVO measured its rows 49F-only (23,213 of 23,213). The object
   is one that CAN mix firms (Z-S109). A measured-single today is not a contract that it stays single, so the tool keeps
   its row filter in code. `multi` keeps the rows invisible to firm principals in the catalog. Changing it to
   `49financial` would be a widening with its own never-widen pair, and is not ruled here.
3. **Each catalog release that adds known-firm values carries its own never-widen pair** (v0.17 item 4, corrected).

## 3. NEXT ROUND -- ENRICHMENT LIST (round 18, already issued under v0.17)

| cell | content | owner |
|---|---|---|
| C-GROUP rows | `bucket` on every row; `vendor` and `firm` on the assets and bd rows | ~MI (ASSETS), ~MI2 (RESEARCH) |
| MX-c-21 | `source_group` = `bucket` on `tool_index` | ~MI |
| MX-c-22 | `etfs_get_positioning` extension, with the old answer byte-equal | ~MI |
| MX-c-23 / MX-r-15 | the Schwab `dim_*` catalog rows that OG-cl-1 needs, and their release | ~MI |
| Z-C-S61 | curated tags, each workstream on its own files | ~MI, ~MI2 |
| read_tool links | each `client_*` and gp/gf tool linked as it goes live | ~MI, ~MI2 |
