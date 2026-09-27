# Never-widen sign-off packet -- irpt-performance-adapter: a RENDER_DELEGATE reads only the selection its grant pins

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Author and operator:** `2.0.0_SA_COO~P`, 2026-09-27 ~23:4xZ.
**Ruling:** 1.0.0_SA_CTO 102216 (adapter only, `_scope` untouched, conditions 1-5); 4.0.0_SA_CRO 102219 (the five
arms). **Ledger (opened before any write):** `irpt-adapter-render-selection-20260927` (U1 closed).

## 1. What window 19 found

The export's render reached the adapter under a valid, decryptable grant: no AccessDenied after f7aa7b3c. It was then
refused at 23:21Z (corr-6a0911404047): SelectionRefused "current entitled viewer required", public OBJECT_NOT_COVERED.

`performance/entry.py:92-102` resolved every selection through `_scope/selection.resolve_selection`, whose `_check`
refuses principal_class RENDER_DELEGATE (`selection.py:49-50`). So no render could read its report.

## 2. The change (backend c8ef8b7751; `performance/entry.py` only, plus a new test file)

`_resolve_selected` routes a RENDER_DELEGATE to `_resolve_render_selection`. Every other class goes through
`resolve_selection` unchanged, and `_scope/selection.py` is untouched (condition 1). The rules:
1. The selection id comes ONLY from the render grant's pinned `accountSetId` (the grant named by the verified
   X-Render-Revision, and naming this delegator). A request naming a different set refuses.
2. The selection's firm must equal the tenant, which must equal the grant's firm.
3. Every account must sit inside the Enforcer's delegator-by-grant intersection: the scope's permitted set, built at
   `enforce.py` `_resolve_render_delegate` (the delegator's scope re-resolved NOW, intersected with the bundle's pins).
4. Every other binding check of `resolve_selection` stays: the schema, the directory revision, the reference hash and
   the canonical member list.

The grant read is one helper, `_render_grant`, now shared with `_request_principal`; its behaviour is unchanged.

**Tests** (`performance/tests/test_render_selection.py`; performance suite 210 passed):
- arm 1: a delegate with a valid grant reads its pinned selection;
- arm 2: a request naming another set is refused;
- arm 3: an account outside the delegator's grant is refused;
- arm 4: a cross-firm selection, and another tenant, are refused;
- arm 5: a non-delegate read still goes through `resolve_selection`, and `selection._check` still refuses a
  RENDER_DELEGATE;
- plus a changed binding refused, and a grant naming another delegator refused.

## 3. The artifact and the move

| | live | new |
|---|---|---|
| irpt-performance-adapter CodeSha256 | `bOefL9nx..` (S3 version 8uohgNwE.) | `F0bYtOfB..` (S3 version G4UtfeeR.) |

- **Census:** 69 -> 69; ONLY `entry.py` differs. Its live blob equals the backend parent's (7f92ad76), so exactly the
  reviewed change moves.
- **Built-zip flat smoke** (condition 4): the handler module `runtime` imports with `lambda_handler` callable, and
  `entry` imports with the new functions callable. After apply, a cold-start invoke must answer.
- **Dry plan** (performance root, null plan tfvars): **0/1/0**, code only. No plan is armed, and IAM is unchanged.
- **Rollback:** re-apply at S3 version 8uohgNwE. (bOefL9nx), restored as latest, as done for irpt-status at 23:15Z.

## 4. Blast radius

- **Moves:** a RENDER_DELEGATE Performance read. Before: refused at selection (always). After: admitted for the ONE
  grant-pinned selection within the delegator's current grant, and refused otherwise, by name.
- **Unchanged:** every human read (FIRM_ADVISOR, FIRM_OPERATIONS, OPAL_GLOBAL, the internal V1) and every vendor path.
  No plan is armed.
- **Reachable:** only a render token minted by an export submit, which today means the walk windows only.

## 5. Proof

The next K8 window: the render's Performance read answers with no SelectionRefused, and the export reaches READY
with a %PDF (ledger A1). S27's receipt-state fix is a separate change (contract first, CTO ask 102224).

## What the halves sign against

This file's committed blob; backend c8ef8b7751; artifact F0bYtOfB with its census, smoke, 0/1/0 plan and rollback;
and the arms in section 2.
