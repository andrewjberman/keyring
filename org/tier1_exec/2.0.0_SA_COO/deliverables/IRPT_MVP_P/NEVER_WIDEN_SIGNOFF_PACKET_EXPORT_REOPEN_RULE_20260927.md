# Never-widen sign-off packet -- irpt-export-render: a caller who may view a retained report may export it

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Author and operator:** `2.0.0_SA_COO~P`, 2026-09-27 ~17:3xZ.
**Ruling:** 1.0.0_SA_CTO 101991, (a). **Ledger (opened before any write):** `irpt-export-reopen-rule-20260927`.

## 1. The change (backend f92445392d; publish 787a785ee6)

`export/retained_export.py` `authorizer()` drops ONE conjunct, `owner.principal_id == caller.principal_id`. It keeps:
- `candidate == caller`;
- `owner.firm_id == caller.firm_id`, so there is no cross-firm path (CTO condition 2);
- the owner's accounts non-empty and a subset of the caller's `permitted_account_set`.

That set is the served Entry's Enforcer-resolved live-grant set, the same live-grant resolution the Performance reopen
(P-REOPEN-01) runs, not a copy of a rule (CTO condition 1). The render grant's `delegator_subject` is already the
CALLER's principal id (`render_grant`, retained_export.py:76-86), so the grant and receipt name who exported (CTO
condition 3; CRO arm 4). The original owner stays on the record, unchanged, and admits nobody.

**Tests** (export suite, 108 passed):
- a second in-scope principal exports, and the grant names it;
- a second principal missing one account is refused;
- a caller in another firm is refused.
The positive test fails on the old line (negative control).

## 2. The artifact and the move

| | live | new |
|---|---|---|
| irpt-export-render CodeSha256 | `ryEMGlRu..` (S3 version 9atDu8b.) | `3EST/hewG..` (S3 version te7rGPXk.) |

- Census: 58 of 58 members; ONLY `retained_export.py` differs.
- The dry plan (export root, 17:3xZ) reads **0/1/0**, code only (s3_object_version and source_code_hash).
- Rollback: re-apply at S3 version 9atDu8b. (ryEMGlRu), the pattern of every prior export deploy.

## 3. Blast radius

- **Moves:** which callers the export's submit admits for a retained report, from "the owner principal" to "any
  same-firm caller whose current grants cover every account". Nothing else changes: no env, no IAM, no route, and no
  change to the render, the token, the grant shape or the receipt.
- **Reachable now:** only a signed-in export POST. Today that is the walk windows only (the route is not open to firm
  users). No existing export record changes; exports are created by submits.

## 4. Proof arms (CTO condition 4; CRO arms 1-4), in the NEXT K8 window

1. A second in-scope principal exports READY: the walk principal exports a report it did not compute, reaching a PDF.
2. A principal missing one account gets ReportDenied (the negative arm). It runs by direct invoke with a
   synthetic scope, or as a unit-level proof on the served code if the window cannot stage it; the K8 packet names
   which.
3. The owner is unchanged on the record.
4. The render grant and the receipt name the CALLER.

## What the halves sign against

This file's committed blob; the one-conjunct change at backend f92445392d; artifact 3EST/hewG with its 0/1/0 plan
and rollback; the four arms in the next K8 window.
