# Never-widen sign-off packet -- UIR-07: the directory search ranks an exact full-name match first

**Author:** `2.0.0_SA_COO~P`, 2026-09-26 ~21:5xZ. **Order:** `1.0.0_SA_CTO` 101506 (DSGN_IRPTV1 PRD v0.13 UIR-07:
"Bring it under a half; it is a served ranking change"). **Halves asked:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`.
**Ledger (opened before any write):** `irpt-uir07-search-rank-20260926`.

## 1. The act

Rebuild and apply ONE function, `irpt-directory-search`: its live artifact `o9Qu0Jm7..` plus `directory/handler.py` at
backend 1068a4b5a5 (the parent blob c80dab8c is the live one). The build census against the live zip must show
exactly `handler.py` differing, or the act stops.

Not moved: `irpt-directory-refresh` (it packages handler.py, but never calls `search`), `irpt-holdings` and
`irpt-status` (they stage their own older handler.py pins and never call `search`).

## 2. The change, both branches

`handler.search` sorts the viewer's projection with a new FIRST key: 0 when the entry's display-name tokens, sorted,
equal the query's tokens, sorted; else 1. Then comes the unchanged weighted score (exact*4 + prefix*2 +
discriminator*3), then name, then entry id.

- **What a viewer sees is unchanged.** `project()` (scope, cross-firm gate, permitted accounts) runs first and is not
  touched. The same query returns the SAME result SET before and after; only the order moves, and only when an entry
  is an exact full-name match.
- **Branches:**
  - A query with an exact full-name match puts it first, in either name order.
  - A query without one ranks exactly as before.
  - The `ambiguous` rule and the `match_score` shape are unchanged.
- **Writers of the ranking: 1** (`handler.search`). The page never re-ranks (UIR-07).

## 3. Blast radius

- **Touches:** `irpt-directory-search` code only (`source_code_hash`, `s3_object_version`). No IAM, route, table,
  directory artifact or portal file.
- **Writes by the proof:** none. Search is a pure read (`handler.py` :164 "no I/O of any kind on this path").
- **Rollback, per key:** re-point `irpt-directory-search` to `o9Qu0Jm7..` (its S3 version, recorded in the ledger
  before the upload) through safe-apply.

## 4. Proof

**Offline** (backend 1068a4b5a5): 4 query spellings (both orders, a comma, case and spaces) put "Thiessen, Anna"
ahead of "Anna Thiessen Trust"; 1 arm shows the ranking unchanged with no full match. On HEAD's handler.py the 4
exact-match arms fail. directory/tests: 165 passed.

**On the served function, before and after** (a direct IAM invoke with a synthetic internal Opal subject, the
`deploy_b_human_arm.py` pattern; no names printed):
1. Take 20 real 49F directory entries, chosen deterministically (the first 20 entry_ids in sorted order whose
   display name has at least 2 tokens and is unique in the firm).
2. For each, query its name tokens REVERSED, and record the result-set digest (entry_ids, sorted) and the matched
   entry's 1-based rank.
3. Pass:
   - every result SET is identical before and after (DELTA=0 on what is visible);
   - every after-rank is 1;
   - every query whose before-rank was already 1 keeps it.

Any set difference means STOP and a same-turn rollback.

## 5. Not in this act

Any other UIR item; the portal (it never re-ranks).
