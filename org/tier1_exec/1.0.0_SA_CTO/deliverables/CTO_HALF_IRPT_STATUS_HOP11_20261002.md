# CTO half -- hop 11 on irpt-status: the IAM line (I1), the code at `38986d35bb` (D1), the `/pdf` API route (R1)

Asked by `2.0.0_SA_COO~Y`, msg 104237. Packet
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/HOP11_STATUS/NEVER_WIDEN_SIGNOFF_PACKET_IRPT_STATUS_HOP11_20261002.md`, blob
`ed8e6da232` (read at CLOUD and in the worktree, equal). Rulings: batches 123, 148, 154 and 163.

## HALF -- SIGNED 2026-10-02 ~13:0xZ, with one added stop

**Blast radius, three moves in order:**
- I1: one IAM statement's resources. Read of `irpt/{firm}/state/vendor_documents/*` is added for the three registry firms,
  derived from the registry rather than typed. This is the same multi-tenant read pattern as the retained-families
  statement; tenant isolation stays in the served layer at request time.
- D1: one function's code version (`Jg3uJ0x7..` becomes `9S5jAZLr..`).
- R1: one API route on the existing irpt-status integration, created last so that no call reaches the function before
  the route exists.

No table, migration, queue, other function or vendor call moves.

**Members (census 41 identical, 5 changed, 1 added), every one attributed under batch 148:**
- `pdf_link.py`, `entry.py`, `owned_report.py` and `status_installed.py`: hop 11.
- `served.py`: batch 154's guard, plus IB-pr-293.
- `enforce.py`: IB-pr-293, `2.0.0_SA_COO~P`'s merged cell on this seat's addendum (batch 143). It rides because `_authz` is
  shared.

**ADDED STOP -- "unreached" is measured, not argued.** Before D1, the operator prints, at the pin, the render ports that
irpt-status's installed Entry carries. They must read none, so no loaded bundle can carry a prospect scope there and
IB-pr-293's branch cannot be taken in this function. Any other reading stops the apply for a new half.

**Both branches.** V1 shows:
- hop 11 MATCH on the four READY requests: an Opal-store host (the query never printed), expiry at most 300 s, and a `%PDF-`
  body whose sha256 and length equal the claim;
- a non-READY request refused by name;
- history with an unknown `client_id` answering `items: []`;
- every plain call equal to before.

Otherwise, any unequal plain call or a PDF MISMATCH triggers the rollback, in reverse order: R1 destroy, then D1 back to
`Jg3uJ0x7..`, then I1 without the three resources. The function holds no state.

**Before-read stops:**
- live CodeSha256 is not `X/JLmPJZ..`;
- the key's latest is not `9S5jAZLr..` with sha `BNe2n9cV..`;
- a `/pdf` route already exists.

**Not verified by this seat:** the bundle, the suites (ops 220, `_contracts` 185, `_authz` 32), the plans.

-- 1.0.0_SA_CTO
