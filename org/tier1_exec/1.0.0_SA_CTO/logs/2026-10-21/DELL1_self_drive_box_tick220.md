# DELL1 self-drive box -- ticks 219-220, 2026-10-21 ~04:18-04:49Z (hour floor; the Fidelity account-list has no pager -- the per-G sweep ruled as the source)

**archetype:** COORDINATE
**state:** ARMED (cron 520f0ff2, record ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md @fa59eb8dec). The FIDUPL drive loop,
cron 19710f50, runs beside it.

## Inbox and open calls
- 0 unread at 04:49Z. Acked since tick 218: 8981, 8982, 8985.
- open_calls.json: 163 rows, 4 OPEN: 89c9 and ea86 (Andrew's); 3bc7 and 5013 done or withdrawn, held CROSS-BOX by the tool.

## Acts and rulings
- **NFRA_FIDUPL quiet spell** (29 min at 04:18Z): asked P1 for the blocking step; answer (8981, corrected by 8982): FT-s-8's paging
  probe waited only on the sign-in cap (three in the trailing hour); the 03:46Z SSM Failed is unmeasured.
- **Probe 2P** (NFRA1 @3dd0e138d8d, 04:30-04:32Z, one sign-in, 48 requests, every status 200): all eleven candidate paging forms
  returned the same 2000 rows of 5204 available; the server never sees a start.
  - **Ruled** (04:37Z): decouple the firm split from the pager; key off account.txt's own G column if it carries one; read the
    CRO's HARs for the real page-2 call before another sign-in.
  - **P1's two reads** (8985, record @6077b873db7): account.txt is 5009 x 141 with NO G column; the HARs show accountList is not paged
    at all (the UI says "too many results, narrow your search" above 2000).
  - **Ruled** (04:42Z): the top-level list is not the source. The product's own model is the switcher: a G scopes the session and
    its book is what accountList returns under that scope. Probe v2 = the per-G sweep (switch to each of the 31, one accountList,
    at most 2000 each, masked by ordinal); that membership is what the split keys off; the sum against the 5009-row file is the
    coverage cross-check (overlaps and the unattributed named, never merged); accountSearch narrowing only for a G above 2000,
    cut when a size says so. One sign-in for the sweep, under the cap. FT-s-9 REPAIR 1 (probe v2) drained @217476105df; FT-s-8 step
    2P-v2 added @6d4650d4dfd; the twenty-third delivery complete @371f02ab912.
- **AMGT_HARVST:** no change; co-7 stage 7 waits for its apply span (2026-10-22 10:30Z to 10-23 08:30Z).

## Scope state
- **NFRA_FIDUPL:** FT-s-8, FU-s-11, FU-x-1 pending. 19 objects under `fidelity/alongside/bronze/` (6 data, 13 run records). Rules
  ENABLED (first fire 09:45Z). No firm prefix, no backfill earliest-date row yet.
- **AMGT_HARVST:** round 100, co-7 stage 7 pending.
- **ADVI_COTBOOKS:** L2, waiting on ea86.
- **Completion test:** NOT DONE.

## ACTS ONLY ANDREW CAN DO
- **ea86:** confirm ADVI_COTBOOKS v2's DONE WHEN lines (L2).
- **89c9:** the SOC2_MSLOGS re-derive (his MFA).
- **Conditional:** a back-dated Fidelity export profile, only if the wizard's step-1 date field cannot be automated (CRO 8916).

## Compiler Tools
- `git show` of the probe record and the reopen; `get_agent_status` (P1 LIVE).
- `list-objects-v2` (counts only).
