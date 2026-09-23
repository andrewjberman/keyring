# /self-drive IRPT_FNTEND IRPT_BCKEND -- tick 15 (~23:1xZ 2026-09-21)

- **Arming record:** carrier `c9ccd9f4e3`; cron `46e545b7`.
- **State:** ARMED.
- **Projects:** 2, both `active` / EXECUTING.
- **Sequence:** no flags.
- **COO lanes:** 2 of 3 live.

## Inbox (0.8)

- 2 messages since tick 14: 99311 and 99315.
- Both are read and acked; 0 unread.

## Driver acts: rulings in msg 99312/99313 to 2.0.0_SA_COO~B, cc 3.0.0_SA_CVO~B

### CALL 1 -- L4 needs a grant (rti-3 non-verdict @`726888a84f`)

The BOUNDED TEST PRINCIPAL is APPROVED as a ROUND-10 cell, not mid-round. The cell must:
- create one non-exempt role via safe-apply, whose name matches neither `*-inf-*` nor `*-cot-*`;
- grant it ListBucket ONLY, on the 2 empty buckets plus 1 unfenced control;
- run a positive arm and a negative arm, with the negative arm's denial attributed to the resource policy;
- destroy the role in the same session and verify NoSuchEntity;
- open and close a change-management ledger entry;
- carry CTO + CRO halves.

This supersedes 99299's "no grant widened" line for this one self-deleting role only. The L4 ledger row stays OPEN, owner `2.0.0_SA_COO~B`.

### CALL 2 -- rti-2 residual (@`cd21deffcf`)

- **Ruling:** (i) PARK "redeploy irpt-ycharts-generate from HEAD". Owner: `2.0.0_SA_COO~B`.
- **Un-park condition:** any served change to the function, OR IRPT_FNTEND FWD-4 needs the rth-1 loaders.py fix.
- **Measured this tick, CloudWatch plane:**
  - Last modified 2026-09-19T14:29:32Z.
  - Invocations 1 / 5 / 3 over 09-16..09-19, none since.
  - Errors 0.
  - Latest stream: START/END/REPORT only (1907 ms, 129 MB), with no application line.
  - So it RUNS CLEAN. That is not evidence its output is correct.

### rti-1, row W9-S1

- **Ruling:** NO DEV origin. The allowlist is exactly the renderer's own configured origin(s), read and cited.
- This seat's half is to be signed against packet blob `56ad3283...` after an independent read. The COO half is pending the COO fork.

## Project state

- **IRPT_BCKEND:**
  - Round 9: rti-2 and rti-3 drained.
  - rti-1 first pass drained @`b18045c550`; it awaits both never-widen halves.
  - rti-6 is STAGED.
- **IRPT_FNTEND:**
  - Round 10 L7 is 4 of 4 terminal (@`0a28a5d1b4`).
  - The L8 packet went to `3.0.0_SA_CVO~F` as msg 99314.
  - New row S69: the receipt card hard-codes LOADING.

## CVO~F reachability (the 99315 concern)

- `get_agent_status` reads LIVE, last seen 20s ago, "READY: codex seat bound".
- COO~F's L8 packet sits in its inbox at top level, i.e. not yet taken.
- `3.0.0_SA_CVO~F`'s last commit is `4368801e4b` at 16:06 today.
- The seat is alive and idle-ready; the packet is ~12 min old.
- COO~F owns the nudge under the packet protocol. This seat does not duplicate it.
- Owed from this seat: the round-10 analysis on CVO~F's slug.

## Completion test

NOT DONE: 0 of 2 projects complete.

## Compiler Tools

`get_agent_status`, `.tools/aws` (lambda list-functions, cloudwatch get-metric-statistics, logs), `git log`.
