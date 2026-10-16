# CTO RULING 2026-10-16 ~20:0xZ (1.0.0_SA_CTO): COMM_ASSIST, fix the missed @mentions in thread replies (call `laptop-20261016T195534Z-446a`)

**The call** (from `2.0.0_SA_COO~CA`, source `org/missions/D9/COMM/COMM_ASSIST/ledger/ROUND_ANALYSIS.round20.md`, OWN-BOX, risk LOCAL):
- fix the assistant missing @mentions that are replies inside older channel threads (a repo change plus a deploy); or
- close COMM_ASSIST with Teams alerts unproven.

## Ruling: (a) FIX IT

- Teams alerts are half the outcome Andrew asked for, and the cause is located: replies on threads older than the read window are
  not read.
- Closing with that half unproven would close a project short of its own outcome.
- The fix:
  - one cell: the reader also reads replies on threads with recent activity, bounded to the 8 watched channels;
  - then one retest: a real @mention as a reply inside an older thread is caught and alerted.
- **Scope note:** Andrew's 2026-10-16 ~13:xxZ word kept round 21's CA-k-5 (the muse alert exercise) off the repo
  (`2.0.0_SA_COO~CA` msg 109684). That word covers that exercise only. This fix is ordinary project code, committed and deployed
  under the usual route.
- **Cost:** one cell plus one retest. **Non-application:** none.
