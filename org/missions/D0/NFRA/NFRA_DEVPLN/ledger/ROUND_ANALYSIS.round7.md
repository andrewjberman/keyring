# NFRA_DEVPLN -- ROUND-7 ANALYSIS (1.0.0_SA_CTO, 2026-10-14 ~02:2xZ)

**On:** the issuer's drain end `org/tier1_exec/2.0.0_SA_COO~DV/deliverables/NFRA_DEVPLN_ROUND7_DRAIN_END_20261014.md` (1 of 1 order,
MAY-CLOSE; no CVO packet). **PRD:** v0.3, unchanged. **Next:** round 8 on section 3.

## 1. What round 7 moved

**DP-i-1:**
- The release check now reads `origin/<trunk>` and prints the resolved ref and sha. The real seam reads PROD `7d5cb34d`,
  `features=2 unapproved=0`; before the fix it read a stale local `PROD` as `features=1`.
- Test case 9 no longer makes a real ref lookup.
- The one consumer, `/prod-deploy` Step 4's `sed`, still extracts the branch from both line forms.

Project state: two chosen-set promotes are on PROD with `unapproved=0`, and the DEV payload limb is on all four boxes. The plan's
only remaining work is A14, FWD-1's client-facing close, and it waits on Andrew's five dell2 approvals.

## 2. Ruling (row `NFRA_DEVPLN-S5`): the owed-call wait cannot see another box's row

**RULED: widen the tool. No laptop pointer call.**
- `unblock.py tick --owed-call <id>` reads only this box's list. The call id names its box (`dell2-...`), and this project already
  built the reader that finds another box's row from its freshest source (DP-e-2, `approval_read`).
- So `--owed-call` resolves the id's box and reads that box's row through the same reader.
- A pointer call on the laptop list would be a second copy of the same decision: two rows for Andrew, one of which can go stale. That
  is the duplicate-state class this cluster removes.
- Done when `tick --owed-call dell2-20261013T221411Z-3635` reads `WAITING CALL ... OPEN` from the laptop, and a CLOSED or absent
  remote row counts as before.
- **Owner:** `.tools/unblock.py` is a shared keep-driving tool. If it is inside this project's `<paths>`, it is round 8's one cell. If
  it is not, the issuer routes the cell to `2.0.0_SA_COO~C` (NFRA_CTLPLN owns the keep-driving mechanism) through a row, and records
  this project's wait meanwhile with `--wait-until <a dated read of Andrew's rows> --owner andrew`.

## 3. ENRICHMENT LIST for round 8

1. **The S5 widening** (section 2): one worker-light cell, or the routed row.
2. **After Andrew rules the dell2 rows:** A14, FWD-1's client-facing close (SERVED, with the L8 packet).

Until then the project's honest state is a recorded wait on Andrew, not a round. The DT's uncommitted ledger close stays the DT's act.
