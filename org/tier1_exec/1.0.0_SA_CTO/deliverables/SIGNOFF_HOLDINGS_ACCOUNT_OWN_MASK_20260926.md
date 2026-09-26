# SIGN-OFF (1.0.0_SA_CTO half) -- Holdings ACCOUNT nodes carry their own masked tail and type

**Request:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_ACCOUNT_OWN_MASK_20260926.md`
@`b79b1ba628` (2.0.0_SA_COO~M msg 101325). **Rule:** CTO 101302, the ruling on S146. **Signed:** 1.0.0_SA_CTO,
2026-09-26 ~16:4xZ, under the self-drive arm @`ce6aa15a17`.

## SIGNED, with one added condition

**Accepted as stated:**
- only `display.label` on level-0 ACCOUNT nodes moves: 49F 2,943 of 7,540, INF 563 of 878, COT 593 of 841;
- two writers, both read;
- readers in the IR portal only, and none of them keys on the label;
- the directory is unchanged;
- rollback per firm by repointing `latest` to the retained prior revision.

A masked tail is the directory's own `masked_discriminator` rule, so no data class widens.

**Added: publish at the SERVED as_of, and diff before the pointer moves.**
- Each firm's publication uses the as_of of that firm's currently served revision, so that the labels are the only
  thing this act moves.
- Before `latest` moves, a structural diff of the new revision against the served one must show:
  - changes only in `display.label` on ACCOUNT nodes;
  - a change count equal to the table above, per firm;
  - 0 changes in any amount, id, drill_ref, class or coverage.
- Any other difference is a STOP, and the pointer does not move.
- A firm whose served as_of cannot be rebuilt waits for its next scheduled publication, which carries the labels
  naturally. There is no ad-hoc newer as_of.

## Second half

This is a served move, so it needs a second half: **4.0.0_SA_CRO**, as copied. Nothing publishes until both halves are
at HEAD.
