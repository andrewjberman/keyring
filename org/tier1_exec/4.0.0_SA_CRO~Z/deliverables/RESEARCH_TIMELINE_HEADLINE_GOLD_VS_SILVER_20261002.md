# Timeline headline: gold denormalization (A) vs targeted silver read (B) -- estate precedents

**Author:** 4.0.0_SA_CRO~Z. **Asked by:** 1.0.0_SA_CTO~Z, msg 28499 (RESAPP round 63 design fork). **Date:** 2026-10-02 ~14:2xZ.
**Input:** `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round63-prep/TRACKC_FINDINGS.md` @36414ad802.
**Method:** code at HEAD, git history, the AMGT ledgers and surprise channels, the estate docs, and one census. Nothing was run
against AWS. Every claim cites its file.

## Answer

**A, as recommended.** Every display-adjacent field the estate carries on a gold row has held up. The only request-time
silver read I found in serving code is this route, and it aged in hours.

## 1. Precedents: fields carried on gold rows

| # | where | what is carried | how it aged |
|---|---|---|---|
| P1 | HARVST `chatter_event.lead_headline` (`publication_gold.py:1085`, `:1479`; built @f9fd49904e, 09-22) | **the same field, a headline**, for each event's lead article, written at gold build | The lead-selection rule changed in at least 4 rebuilds (HVST-a-3, a-4, z-1, b-1). Each rebuild re-derived the headline with no schema change. The HARVST surprise channel (`INVESTIGATION_v1.md`, the one file) names `lead_headline` in 1 row, and that row is a positive read. The round-61/62 timeout record names only the day route. |
| P2 | RESAPP B1-B5 (round 61, `ROUND_ANALYSIS.round61.md:8-16`) | served strings fixed at the function that builds each one | CLOSED on CVO~Z's deployed read. One residue, B2's system vocabulary, went to the page (ruling 2). This is the CTO's own precedent and is cited here unchanged. |
| P3 | BD/COT gold `account_performance` (`ADVI_data_lineage.md:88`; `BD_PORTAL_PUBLISHER_PLAN.md:222`, 10M rows) | all advisor fields on every row | Account-master fields pass through cleanly. **Advisor-attribution fields needed carry-forward code** (`verify_05_A_00.accounts_dimension.md:14`, L255-284 and L419-425), because later fee, sweep and dividend rows null them. |
| P4 | MDPF assets WSA `cohort_class` (`MDPF_ASSETS_WSA_CONTRACT.md:68`, Amendment 1) | a registry attribute "for query convenience; the registry is the source of truth" | The pattern is to carry the field and name its authority. I did not measure how it aged. |
| P5 | ETFS_RIVALS `canonical_shape` (`ETFS_RIVALS_PRD.md:444`) | Andrew's L1 word: *"a denormalized base table with all info that we'd want ... put it all in there"*, each field with its source and as-of date | This is Andrew's standing preference for wide gold. |

**The lesson P3 teaches, applied to A:** carry a field when it has one value per key under a newest-wins rule. Title and
`published_precision` meet that test. `record_hash` covers both (`store.py:330-334`). `store.supersedes` is the one
newest-wins rule. The gold `fetched_at` equals the newest silver `fetched_at` for 5,715 of 5,715 keys (TRACKC section 3).
Neither field has P3's failure mode, where a later row nulls the field.

## 2. Counter-precedent: a keyed read from silver at request time

- **Census:** `comp-find '"silver"'` over `infra/aws/lambda`, `lib/research/api` and `timeline_api.py` gave 33 hits in 20 of
  5,496 files. All 20 are ingest or conversion Lambdas, or tests; that includes `inf-api-positions` and `inf-api-reps`, which
  are Orion pulls to silver, not serving.
- **Limit:** a reader that reaches silver through a helper does not name the tier literally, so the census can miss it.
  `scoped_amgt.py` is such a reader: it reaches silver through `publication_gold`.
- **So the one known instance is this route, and it aged in hours** (`ROUND_ANALYSIS.round61.md` addendum; `.round62.md`
  section 1):
  - 0 timeouts in 694 invocations from 05Z to 09Z, then the first at 10:14Z as the collectors grew silver;
  - memory went from 1769 MB to 10240 MB, the Lambda maximum, and the time is CPU-bound;
  - an 18 s deadline now serves `headline: null`, and 7 of 11 cold calls hit it;
  - a manual warm-up was needed before the demo.
- **Why B inherits the curve:** the cost is linear in silver parts, and silver is append-only and partitioned by fetch date.
  B bounds it, but TRACKC's own tail remains:
  - the after-build set grows until the next gold build;
  - window misses fall back onto a partition of more than 1,000 parts;
  - one LIST stalled for 21.4 s with no established cause.

## 3. Doctrine fit

- **Rule 17b** (`CLAUDE_ANNEX.md:454-457`): *"per-consumer projection, display naming and route-shaping belong in platinum,
  NEVER in gold."* Title is the article's own source field: silver carries it, and `record_hash` covers it. It is not a
  projection or a display name, so A is in bounds **if the value is carried verbatim, with no formatting at the producer.**
- **Format rule** (`infra/logic/02_DOCTRINE.md:92`, A5): JSON only at platinum. A route reading gold is already a departure,
  and the rule's direction line says that is not a violation. B pushes the route's reach down into silver; A keeps it at gold.
- **Rule 17c:** title is common to all five publishers, so it fits the one-Opal-shape gold.

## 4. Staleness, schema churn and replay under A

- **Staleness:** the headline becomes "as of the gold build", which is the vintage the mention rows and `lead_headline`
  already carry. The day view stops mixing gold-vintage mentions with request-time silver titles.
  - The real bound is build cadence: TRACKC measured 1, 1 and 1 builds a day, then none from 09-25 to 09-28, then 3, 2, 4
    and 1.
  - A stalled build freezes titles and mentions together. A adds no new staleness class.
- **Schema churn:** `GOLD_MENTION_SCHEMA` has not changed since its creation (@f7bf47887e, 09-22, the only commit whose diff
  touches its fields). A is its first change.
- **Replay:** each gold snapshot is write-once per build, so older snapshots lack the columns. The route reads only the
  newest snapshot, so the silver fallback matters only in the gap between deploys.
  - Land the producer change and the gold rebuild before the route change, and the route never needs silver.
  - Keep the 18 s null path only as the guard for a snapshot without the column.

## 5. One build-side gain, optional, the CTO's call

The gold build already scans all silver articles twice:
- `build_mention` (`publication_gold.py:1026-1035`);
- `build_event` through `_headline_by_article_key` (`:1486-1507`), a scan that exists only to fetch titles. Its own docstring
  calls the missing title column the reason ("HVST-h-4 never carried the title forward").

Under A, `build_event` can take the title off the mention snapshot. That turns three reads of the same titles (two at build,
one per request) into one.
