# IRPT_BCKEND round 22 -- workstream ~Y (Analysis) decomposition

Issuer `2.0.0_SA_COO~Y`, 2026-09-29 ~08:5xZ. Trigger: CTO condition 102655 on the st4 install (the RETRY re-offer's
terminal bound) and ~P's measurement 102659. The live irpt-generation RedrivePolicy is maxReceiveCount 5 to
irpt-generation-dlq. With IB-yr-211's 60 s re-offer, a resolve that keeps failing is dead-lettered after about 5 min,
and its NORMALIZATION row stays RESOLVING while the message sits in the DLQ. IB-yr-211 made that path faster, so this
cell is ~Y's own remediation. st4 is not installed until it drains.

| cell | item | outcome served | risk | worker | depends on | checks (base dry-run at CLOUD HEAD) |
|---|---|---|---|---|---|---|
| `IB-yr-221` | a resolve RETRY is bounded below the DLQ: `poll_once` asks SQS for `ApproximateReceiveCount`; at `RESOLVE_MAX_RECEIVES` (4, below maxReceiveCount 5) a RETRY gives up on that message by name (delete, `IRPT_RESIDENT_RESOLVE state=GAVE_UP code=RESOLVE_RETRY_EXHAUSTED`); the row stays RESOLVING for the client poll's existing redrive (`intake/uploads.py` `_answer`, `REDRIVE_SECONDS` 960) | FWD-4 (an upload never ends stuck in the DLQ) | WORLD (the infra/ floor; nothing served moves) | `~73` | IB-yr-211 (same file, drained @14c961af32) | `R22_CHECKS/test_r22_y1_resolve_bounded.py`: gives_up FAIL (RESOLVE_MAX_RECEIVES absent), asks_count FAIL (no AttributeNames), early PASS (control) |

Why no new row state: the NORMALIZATION states are RESOLVING / NORMALIZED / NEEDS_CORRECTION, and the portal (~D) reads
them. Giving up on the MESSAGE while keeping the ROW recoverable uses the recovery path that already exists, and adds no
state to the contract.

Carried, not cut here (row filed separately): generation messages share the same RedrivePolicy. A generation job that
keeps READ_BACK_PENDING (900 s retains) is dead-lettered after 5 receives, about 75 min, and stays non-terminal:
REQ-3a1b73a8 has been in the DLQ since 09-27.

Edges: IB-yr-211 -> IB-yr-221 (one file). fanout: 1 of 1 chains, cap 8. Slot maxima (S197 ruling): authors 72, orders
72, branches 61, so ~73.

**Amendment 1 (2026-09-29 ~09:4xZ, issuer ruling on CTO 102688 / CRO 102684).** Cell `IB-yr-221` now ENDS the job at
the bound: the row moves from RESOLVING to the existing terminal NEEDS_CORRECTION with reason RESOLVE_RETRY_EXHAUSTED,
the resident prints `state=ATTENTION code=RESOLVE_RETRY_EXHAUSTED`, and the message is deleted, so the client's 960 s
redrive stops. Still no new row state. Check `test_fourth_retry_ends_attention_by_name` replaces
`test_gives_up_by_name_before_the_dlq`; dry-run at the worker's @c125c68396: AC1 FAIL as expected, AC2 and AC3 PASS.
Worker ~73 continues on its branch.
