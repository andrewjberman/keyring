# Never-widen sign-off packet -- UIR-07: the directory search ranks an exact full-name match first (v2)

**Author:** `2.0.0_SA_COO~P`, 2026-09-26 ~22:1xZ. **Order:** `1.0.0_SA_CTO` 101506 (DSGN_IRPTV1 PRD v0.13 UIR-07:
"Bring it under a half; it is a served ranking change"). **Halves asked:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`.
**Ledger (opened before any write):** `irpt-uir07-search-rank-20260926`.

**v2 supersedes v1 (blob b833af43, CTO-signed 101534). It adds `entry.py` (browse) to the act.** The served
before-run found that `/directory/search` already ranked the reported Cottonwood case first in both orders. The page's
header search (portal `ClientSearch.tsx:95`) calls `/directory/browse` with `q`, which orders every any-token match
alphabetically: the reported case ranked **2** there in both orders, and 49F targets ranked as low as 81.

## 1. The act

Rebuild and apply ONE function, `irpt-directory-search`: its live artifact `o9Qu0Jm7..` plus two members at backend
49b935c213.

| member | live blob | new |
|---|---|---|
| `handler.py` | c80dab8c | `full_name_match` + search's first sort key |
| `entry.py` | d9848e7f | browse's first sort key |

The build census against the live zip must show exactly these two differing, or the act stops.

Not moved: `irpt-directory-refresh` (it packages both files, but serves neither search nor browse), `irpt-holdings`
and `irpt-status` (their own older handler.py pins, no search or browse).

## 2. The change, both branches

ONE predicate, `handler.full_name_match(entry, qtokens)`: the display name's tokens, sorted, equal the query's tokens,
sorted. It becomes the FIRST sort key in:
- `handler.search`, followed by the unchanged weighted score (exact*4 + prefix*2 + discriminator*3), the name and the
  entry id;
- `entry.browse` (the page's header search), followed by the unchanged directory browse order.

What the change leaves alone:
- **What a viewer sees.** `project()` (scope, cross-firm gate, permitted accounts), browse's WHOLE-only filter and its
  any-token match filter run first and are not touched. The same query returns the SAME result SET before and after;
  only the order moves, and only for an exact full-name match.
- **Browse with an empty query, or with no full match:** the order is exactly as before.
- **The continuation** already binds the query (browse's `binding`), so a cursor's order is fixed for its life.
- **The response shapes, `match_score` and the `ambiguous` rule.**

**Writers of the ranking: 2 call sites of 1 predicate.** The page never re-ranks.

## 3. Blast radius

- **Touches:** `irpt-directory-search` code only (`source_code_hash`, `s3_object_version`). No IAM, route, table,
  directory artifact or portal file.
- **Writes by the proof:** none. Search is a pure read (`handler.py` :164 "no I/O of any kind on this path").
- **Rollback, per key:** re-point `irpt-directory-search` to `o9Qu0Jm7..` (its S3 version, recorded in the ledger
  before the upload) through safe-apply.

## 4. Proof

**Offline** (backend 49b935c213; directory/tests 169 passed):
- search: 4 query spellings put "Thiessen, Anna" ahead of "Anna Thiessen Trust", and 1 arm keeps the ranking
  without a full match. On the old handler.py the 4 exact-match arms fail.
- browse: 3 spellings put the exact match first across the cursor, and 1 arm keeps the directory order for q="" and
  for a partial query. On the old entry.py the 3 exact-match arms fail.

**On the served function, before and after** (`search_rank_arm.py`: a direct IAM invoke with a synthetic internal
Opal subject; digests and ranks only, no names):
- Targets:
  - per firm, deterministic unique-name entries from browse's first page: 49F 20, COT 5, INF 5 (CTO 101534);
  - up to 5 "collision" entries per firm;
  - the reported Cottonwood case in both name orders, by id, its query taken from the environment and never
    written.
- Each target is queried with its tokens reversed, through search AND through browse(q) across every cursor page.
- **Before (live o9Qu0Jm7, `reopen_arm/UIR07_ARM_BEFORE_20260926.json`):**
  - search: rank 1 for all 32 targets;
  - browse(q), 49F: [5, 11, 16, 4, 7, 1, 1, 1, 1, 2, 4, 1, 3, 1, 81, 2, 2, 15, 3, 12], collision [1];
  - browse(q), COT: [4, 4, 1, 4, 2]; the reported case 2 and 2;
  - browse(q), INF: [25, 1, 3, 2, 35].
- **Pass after:**
  - every search SET and every browse(q) SET (all pages) is identical to before;
  - every after-rank is 1 in search AND in browse(q). "Rank 1" allows only exact full-name twins ahead; there were 0
    twins among the 33 targets before;
  - no before-rank of 1 is lost.

Any set difference means STOP and a same-turn rollback.

## 5. Not in this act

Any other UIR item; the portal (it never re-ranks); `irpt-directory-refresh`.
