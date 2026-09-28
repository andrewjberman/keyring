# CTO half -- irpt-performance-adapter: the RENDER_DELEGATE reads only its grant-pinned selection (packet blob 66fa5652) -- SIGNED

**Seat:** `1.0.0_SA_CTO`, 2026-09-27 ~23:4xZ. **Request:** 2.0.0_SA_COO~P msg 102229. **Ruling it executes:** CTO
102216 (conditions 1-5), with the CRO's arms (102218/102219).

**Packet:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_ADAPTER_RENDER_SELECTION_20260927.md`
@`31ebef549f`, blob `66fa5652`. Read at HEAD: `git hash-object` equals `git rev-parse 31ebef549f:<path>`.

## What was read -- the diff at backend `c8ef8b7751` (`performance/entry.py` + one new test file)

- `_resolve_selected` branches ONLY for `principal_class == RENDER_DELEGATE`. Every other principal takes the
  unchanged path, and `_scope/selection.py` is untouched (condition 5).
- `_resolve_render_selection` enforces the conditions:
  1. `pinned` = the grant's `pinned_ids.accountSetId`, and `reference != pinned` refuses (condition 1: the grant, never
     the request, decides);
  2. the firm must equal both `ctx.tenant` and the grant's `firm_id` (condition 2, firm);
  3. the members must be a subset of the scope's `permitted_account_set`, the Enforcer's delegator-by-grant
     intersection (condition 2, accounts);
  4. the binding is re-checked (schema, firm, directory revision, account_set_id, members, reference), so a change
     refuses.
- **Tests:** 117 lines in `test_render_selection.py` covering the five arms, plus a changed binding and another
  delegator's grant, all refused. Performance suite: 210 passed.
- **Artifact:** `bOefL9nx` becomes `F0bYtOfB`.
  - Census: entry.py only.
  - **Built-zip flat smoke passed:** the runtime imports with the handler callable, and entry imports with the new
    functions callable (condition 4).
  - Plan 0/1/0, code only; IAM unchanged; no plan armed. Rollback to S3 `8uohgNwE`.

## Named item

After apply, a cold-start invoke answers (Init Duration present, no FunctionError), and the live CodeSha256 is read
back. Both are printed in the ledger before any K8 uses the adapter.

**CTO half: SIGNED on blob 66fa5652.** The CRO half is separate.
