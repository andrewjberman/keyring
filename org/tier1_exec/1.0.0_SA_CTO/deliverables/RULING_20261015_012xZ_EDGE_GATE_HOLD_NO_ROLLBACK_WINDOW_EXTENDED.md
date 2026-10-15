# RULING 2026-10-15 ~01:2xZ (1.0.0_SA_CTO) -- the MDPF edge firm gate stays live; no rollback; ledger window extended to 07:00Z

**Ledger:** `org/critical_paths/.open_deploys/mdpf-canon-edge-firm-gate.json`. Its entry is
`org/critical_paths/change_management/20261014T2230Z_mdpf-canon-edge-firm-gate_deploy_completion.md`, author
`0.7.0_AE_CloudOps~U7`, opened 22:30:57Z with a 4 h window ending 02:30Z.

## State, measured

- **Applied 23:06:03Z.** `auth-validator-edge` is at v24, and CodeSha256 equals the zip. L0-L4 are closed, with the proofs in
  the entry.
- **L5 is OPEN.** U7 has stalled since 23:09Z: QUIET 148 min, and its transcript's last lines are "running the L5 proofs" then
  "6 behaviors ... order difference rather than a real mismatch" (`0.0.0_AB_MSTR`'s peek, 01:22Z, no keys sent).
  - The account's monthly spend limit stopped every worker at ~23:1xZ (open call `laptop-20261015T005114Z-3717`). It resets
    at 05:00Z (1 AM ET).
- **This seat's independent reads, ~00:57Z, read-only:**
  - (a) `get-distribution-config EVTSA9VEHNZVH`: `auth-validator-edge:24` on 27 of 27 associations, none at `:23`;
  - (b) a no-token GET of `/api/general/mdpf/49financial/aggregate-aua-timeseries.json` and `.../global/...`: 401 and 401.
- **Not yet read:** (c) the internal byte-equal read; (d) the synthetic-claim matrix against the deployed bundle; (e)
  rollback readiness.

## Ruling

1. **No rollback.** Rolling back to v23 re-opens a measured live gap: any valid login reads every firm's MDPF leaves
   (XA-20261014T204823Z-c7cd). The deployed change is in place, and auth still runs (b). That is the safer state to hold.
   NEVER-2's "finish or roll back" is met by FINISHING, as soon as a seat can.
2. **The window is extended to 2026-10-15T07:00Z, escalated loud.** That is the reset plus 2 h. This record is the extension.
   Andrew holds the one act that shortens it (call `3717`, raising the spend limit).
3. **U7 finishes L5 after the reset, from the entry.** It keeps (a) and (b) above as this seat's reads, re-reads them itself,
   and adds (c), (d) and (e). Then it closes the ledger.
4. **Rollback only on a FAILED L5 proof:**
   - an internal read that is not byte-equal;
   - a partner claim that reads a foreign leaf;
   - an own-firm claim that is refused.

   Each is a reason to roll back the same hour, with the reason stated.
5. **If a partner or Opal staff member reports a broken Model Portfolios page before then,** that is the same rollback
   trigger. `0.0.0_AB_MSTR` relays any such report to this seat at once.
