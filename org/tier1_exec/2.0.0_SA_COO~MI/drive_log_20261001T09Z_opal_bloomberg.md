# /canonical-drive NFRA_MCPINDEX -- 2.0.0_SA_COO~MI -- 2026-10-01 09Z-10Z (host opal_bloomberg)

Lease FULL, round 6, limb L7, thread y.

## Decisions closed this span

- **MX-d-6 built** (worker ~22 @c6adb5f700, LOCAL): AC1 2/2, AC2 ROUTING 24/27, AC3 REACHABILITY 10/10, proof VALID.
  - Row Z-W22-S1 (cross-firm visibility of firm-scoped silver rows) is ruled by **A1 @5a3f56291d: FAIL CLOSED**.
    Firm-scoped silver rows serve OPAL_INTERNAL only until a catalog firm field exists (carried to round 7).
  - A fresh ~22 is on A1 then MX-g-3. Resume was refused ("No transcript found"), the second time this session.
- **MX-x-4 COMPLETE and drained** @42a8147e45 (chain 2 end).
  - Issuer re-grade on CLOUD: x4.AC1 8 passed, AC2 three arms, AC3 10 passed. Proof VALID.
  - Drain hygiene: `bash -n` on the wrapper and halt gate; `py_compile` on the emitter; halt-gate-ld0131-test 7/7 with
    the new serial order.
  - Rows Z-W23-S1..S3 (INERT) are carried to the slug. S2: `.tools/test-haltgt-recipient-scoping.sh` is red at HEAD
    0/9 on the retired `.agent_context`; S3: worker worktrees lack `portal/src/api`.
  - Worktree wk-mcpindex-r6-23 NOT removed. It holds gitignored audit logs, and `--force` would destroy them. It joins
    the operator-confirmed cleanup list.
- **MX-s-16 PHASE A reported** (worker ~24 @a8db7f31bf, LOCAL).
  - Z-S72's cause: 6 empty unrealized templates whose skip is counted as a failure, and a stale script copy that the
    documents run. The fix is on the branch, not deployed.
  - Allocation coverage 131/131. Saved targeted plan 0/5/0.
  - BLOCKING Z-W24-S2 (sentinel-less days leave the documents as the only same-day writer) is ruled by **A1
    @0de93e672c**: diagnose the producer cause before any halves. A fresh ~24 is on that read-only continuation.

## Compiler Tools

- `safe-merge.sh` (the drain, row gate over the merged index); `proof-of-spec-check.py`; `halt-gate-ld0131-test.sh`.
