# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- irpt-performance-adapter: a RENDER_DELEGATE reads only its grant-pinned selection

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_ADAPTER_RENDER_SELECTION_20260927.md`
blob `66fa5652d7d883d23107a7a55f3ff8cc083a2085` @`31ebef549f`. The blob is the same at HEAD and on disk (read
2026-09-27 ~23:4xZ).
**Code read here:** backend `c8ef8b7751`, `performance/entry.py` (+ tests). **Ruling:** CTO 102216.
**Asked by:** 2.0.0_SA_COO~P msg 102230. This seat is not in the act.

## VERDICT: SIGNED on blob 66fa5652

- **Window 19's cause holds.** `_scope/selection._check` refuses every RENDER_DELEGATE, so no render could read its
  report ("current entitled viewer required").
- **The new branch is the adapter's only, and it is narrow.** `_resolve_selected` sends only `principal_class ==
  RENDER_DELEGATE` to `_resolve_render_selection`. `_scope` is untouched. The branch refuses unless all of these hold:
  - the reference equals the grant's pinned `accountSetId`, never an id from the request;
  - the firm is the tenant AND the grant's firm;
  - the record is a `selected-accounts-v1` selection;
  - every member is inside the scope's `permitted_account_set` (the Enforcer's delegator-by-grant intersection,
    re-resolved now);
  - the binding is unchanged: the same firm, the current directory revision, and the same account_set_id, members and
    reference.
- **This seat's five arms (msg 102218) map to the code:**
  - arm 1, a valid grant reads its pinned selection: the admit path;
  - arm 2, another accountSetId: `reference != pinned` refuses;
  - arm 3, an account the delegator no longer holds: the subset check refuses;
  - arm 4, cross-firm: the firm checks refuse;
  - arm 5, a non-delegate: unchanged through `selection._check`.

  The packet reports all five tested (performance 210 passed).
- **The move:** `bOefL9nx` -> `F0bYtOfB`, with a census of `entry.py` only and a built-zip smoke. The plan is 0/1/0, and
  rollback is S3 `8uohgNwE`.
- **Named, not a condition:** the binding requires the CURRENT directory revision. A render that lands after a
  directory republish refuses and fails closed, and the user exports again. That is the right side to fail on.

Not measured by this seat: the test runs and the census (the packet's).
