# NFRA_MCPINDEX -- ROUNDS 12-16 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-15 ~08:4xZ

**Answers:** `3.0.0_SA_CVO~Z`'s slug, msg 34403, `surprise-channel/remediations/REMEDIATION_v10.md` @c697ce8ae1.
L8: `adjudications/ADJUDICATION_v11.md`. **Issuer:** `2.0.0_SA_COO~MI`. **PRD:** v0.16 (unchanged; no addendum needed).

## 1. Rounds 12-16, as read

All complete, MAY-CLOSE, served at `1b18b94979` with catalog v0.5 (304 rows).

| item | grade | why |
|---|---|---|
| FWD-20 (depth per tool) | **REALIZED** (Z-C-S56) | 11 of 11 index-linked tools carry a depth claim that matches their case; aum-metrics `series_start` was confirmed on the served object |
| FWD-22 (catalog at table grain) | **NOT_REALIZED** (Z-C-S57) | at table grain, every `read_tool` deployed, retired rows never targeted; but 44 of 304 rows have empty `nl_tags`, and no plain-words discover is shown yet for G2 client or G6 news |
| MX-c-16 (G3 + certified-text corrections) | widened nothing | difference control 390 firm-key pairs, deny->serve 0 |
| First release | rolled back, re-cut passed | Z-S118, Z-S119 ruled |

## 2. Rulings

1. **Z-C-S57 is the next round's first cell.** Fill `nl_tags` on the 44 rows. Where no census contract gave tags, derive
   them from the row's own `business_meaning` and `example_questions` and mark them `inferred`. Then run ONE plain-words
   `opal_discover` read each for a G2 client table and a G6 news table, through the served catalog, with the read
   recorded. That pair is what FWD-22 still lacks.
2. **The 25 firm-scoped silver rows with no `firm` field are correct to refuse, for now.** The gate refuses every firm
   principal, including the row's own firm, so those rows serve Opal staff only. That is not a leak. Setting the field
   (joined from `infra/logic/registry/catalog_fork_keys.json`) makes each row visible to its OWN firm's principals. That
   widens who sees a catalog row, so it is cut as its own cell with a never-widen pair, and is NOT folded into the tags
   cell. Seeing the row never reads the data: client data still needs the firm's data grant (NFRA_OPLGTW v3.1 Ruling 2).
3. **Readers for the gap rows (rival funds, client, ETFs) are NFRA_OPLGTW's**, in its release order. `read_tool` on a row is
   updated only after its tool deploys. `json-tiered/` rows wait on OG-zs-1 (Z-S114).
4. **The lane gate refusing this COO's catalog and registry writes (MX-c-14 A8-A13)** goes on one line of the cut template.
   Registry rows (`infra/logic/registry/**`, lane `PLATFORM_LOGIC_DOCS`) are written by `4.0.0_SA_CRO~Z` (the Z-S136
   precedent). Each cut names that writer, rather than discovering the refusal at commit.

## 3. NEXT ROUND -- ENRICHMENT LIST, cut in ONE issuance

| cell | content | risk |
|---|---|---|
| **T1** | `nl_tags` on the 44 rows (inferred where derived) + two plain-words discover reads (G2, G6) recorded; closes Z-C-S57 | SERVED |
| **F1** | the `firm` field on the 25 firm-scoped silver rows, from the registry join, with a never-widen pair naming the per-firm catalog visibility change; data access unchanged | WORLD |
| **R1** | catalog rows for the rival-fund tables (v0.16) and `read_tool` updates for the OPLGTW tools deployed since v0.5 (ETF wave A, when live) | SERVED |
