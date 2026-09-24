# AMGT_HARVST 2b -- the graded chatter_daily gold for the universe - 2.0.0_SA_COO~Y
**archetype:** BUILD

**Date:** 2026-09-24
**Task Order:** none. `COO_Y_HARVST.md` ADDED SCOPE ITEM `2b` @`98edbe915d` is the carrier, per Andrew's
card answer recorded at `RULINGS.md` R-21 `:1493`.
**Status:** DONE (the item is answered; two follow-ons parked with owners)
**Window:** 2026-09-24 10:05Z (session start) to 11:00Z

## Objective

Populate the graded `chatter_daily` gold table for the AMGT universe, with every row carrying its
coverage denominator, and state what fraction of the universe has a non-empty success bucket.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-which | "where is the gold chatter_daily table read and written" | NO CURATED RULE MATCHED, 3 fuzzy candidates of 78 | said so plainly; routed to comp-find rather than taking rank 1 |
| comp-find | `chatter_daily` (content, corpus=all) | 251 hits / 72,634 files; DEF=2 | the two DEFs are the writer and the Lambda -- that pair is the whole answer |
| comp-find | `GOLD_DAILY_TABLE\|chatter_daily` | 274 hits, readers = `pool_reader.gold_window_read` only | consumer census before touching the schema |
| comp-read | `publication_gold.py --enumerate 'chatter_daily'` | 3 hits, 1 WHOLE (the constant), DOCSTRING=1 COMMENT=1 | the builder already existed -- build ladder rung 2 |
| comp-read | `pool_reader.py --for "how is the universe loaded"` | shape + the `191 today` qualifier at `:152` | named the universe grain before any build |
| aws (shim) | `s3api list-objects-v2` on 3 gold prefixes, `lambda get-function-configuration` | 3 daily parts, 2 mention parts, `CHATTER_AXIS_SOURCE=legacy` | `# rail-checked:` on the raw listings -- existence of a NON-served prefix is not a freshness or route question |
| pytest | `lib/research/harvest/tests` + `lib/research/metrics/tests` | 246 passed | 2 new tests, one of which failed first and was WRONG about the code |
| safe-commit / safe-merge | 2 commits + 1 drain | `9a56cfc1d4`, `d6c05a7a49`, merge `7383295c2a` | the row gate REFUSED `class='DEFECT'` and was right |

**What worked:** measuring the retained silver corpus BEFORE deciding what 2b could possibly produce --
118 article rows and 20 `listing_hit` rows settled the whole question in one read, and everything after
it was construction rather than discovery.
**What failed:** my first `comp-read --enumerate` and `comp-find` calls piped into `head` and were
denied; the census flags exist for exactly that reason. One new test asserted behaviour the code does
not have (a two-token name equal to its own ticker is kept, not dropped) -- the CODE was right and the
test was rewritten to assert what actually happens, with the 2-of-191 residual named.
**Gap found:** the pool universe misspells "Haliburton" -- row `AMGT_HARVST-Z-S19`, filed and not
chased.

## Work Completed

1. **Startup**: `/watcher` armed (task `bnn2gyklx`, re-armed `b84naxo7p` on its 30-minute expiry, script
   pid 2496 recorded); registration; 7 inbox messages read and acked (25259, 25266, 25269, 25277, 25387,
   25393, 25403); mandate + R-21/R-42/R-43 read, with R-21's card table read WHOLE rather than grepped,
   which is R-42's own lesson.
2. **Measured the ceiling first.** Retained silver: **118** article rows, **20** `listing_hit` rows --
   all `wsj`, one query, one day. Four of the five `ENABLED_PUBLISHERS` have ZERO. Since `COMPLETE`
   requires all five to cover a day, the success bucket is unreachable by construction, not by chance.
3. **`lib/research/harvest/universe_securities.py`** (new): the pool universe -> the `securities` list
   the builders take. Resolves nothing; derives only the alias set, by two stated rules, printing each
   rule's touch count. 250 names -> 191 securities, 59 without identity.
4. **`GOLD_DAILY_SCHEMA` + `daily_rows`**: `publishers_covered` / `publishers_enabled` on every row.
5. **Two ad-hoc gold builds (QA-permitted)**: mention `part-20260924T105025Z` (263 rows, 55 securities,
   118 articles) and daily `part-20260924T105051Z` (50,997 rows, 191 x 267 days).
6. **Verified by reading the written object back from S3**: 0 rows missing a denominator,
   `publishers_enabled == 5` on all 50,997, **0 rows where the class disagrees with the fraction**,
   COMPLETE **0 of 191**.
7. STATUS.md rewritten in place (current-state, not a journal); one message to `1.0.0_SA_CTO~Z`.

## Current State

`chatter_daily` gold covers the universe: 191 securities x 267 days, every row graded and carrying its
denominator, success bucket **0 of 191**. Merge `7383295c2a` on CLOUD, **push state LOCAL** measured by
`ls-remote` with `d6c05a7a49` (already on origin) as the positive control. H03 2a is landed and its
`daily` leg closed by `0.7.0_AE_CloudOps~A`; `served` is the only open leg and is CVO-owned.

## Blockers

None BLOCKED. Two items parked with owners: a scheduled producer for the gold chatter tables
(`1.0.0_SA_CTO~Z` to route -- a deploy act, not this lane's), and `listing_hit` collection for the four
silent publishers, which needs Andrew's per-use word that `2b` explicitly does not carry.

## Next Steps

1. [`0.0.0_AB_MSTR~Z`] Push `7383295c2a` on its cadence.
2. [`1.0.0_SA_CTO~Z`] Route the schedule question for the gold chatter build; route `Z-S19` to the
   `universe/v1` producer's owner; re-scope or stand down this lane's `org/XXX.md` 1b-F row, which still
   names IRPT Analysis while the lane was re-seated onto AMGT at 02:46Z (NOTHING was armed this session).
3. [`3.0.0_SA_CVO~Z`] The `served` leg of ledger `amgt-h03-leadpanel-y-20260924` is the last one open.
