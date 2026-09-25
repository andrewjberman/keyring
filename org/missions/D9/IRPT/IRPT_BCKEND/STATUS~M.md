# IRPT_BCKEND~M -- Holdings with the snapshot model overlay -- status

Seat `2.0.0_SA_COO~M` (CLAUDE). Lease FAST `IRPT_BCKEND~M`, extending while Andrew is active (drive-mode.log). Goal record
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_224xZ_COO_M_GOAL_HOLDINGS_SNAPSHOT_MODEL_OVERLAY_LOOP_20M.md`
(Done = /verify SOUND). The 20-minute goal loop reads this lease first on every tick (C11). Reviewer: `3.0.0_SA_CVO`
(not live; the FAST line is parked below). As of 2026-09-24T23:2xZ.

## Pins

| What | Value |
|---|---|
| Working branch / worktree | `codex/irpt-m-completion` at `../ajb_irpt_m` @f8e54f2931 (LOCAL) |
| Served holdings (since 23:14-23:21Z) | COT fc199c8e (index ykQofbha); INF ba9001d5 (ipomYxTG); 49F 9ab377ce (OqjgF6qs) -- the prior served revisions plus the v0.6 classification members |
| Prior revisions (rollback) | COT dec293d6, INF d32e50c6, 49F 5a25ae76, retained |
| Receipts | `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/HOLDINGS_{COT,INF,49F}_CLASSIFIED_PUBLICATION_RECEIPT_20260924.json` @7e57abcabd |
| Push state | LOCAL; shared pushes are 0.0.0_AB_MSTR's |

## Live thread

LIVE END TO END through the deployed API at all three firms, signed in:
- **INF:** Greene SIMPLE (HAR 18:36Z).
- **49F:** Alison Horton IRA, with a model leaf (HAR 18:36Z).
- **COT:** Anna (HAR 14:17Z).

The screen fixes landed on portal DEV a65a8db5 (~D): exact amounts, firm-tab filter. Andrew walked it ~19:0xZ
("it looks great"). The classification members are served since 23:2xZ, and ~D's colour cells read them. The PROD
a0690a03 parser reads READY at every firm.

## Goal criteria

| Criterion | State | Evidence |
|---|---|---|
| (1) signed-in journey, 49F / INF / COT | API EXERCISED at all three; screen walked by Andrew on the fixed build; the firm-tab HAR is the one artifact asked | VERIFY_HOLDINGS_GOAL_20260924.md addenda |
| (2) every active 49F/INF account resolvable, or refused explicitly | 49F 7,417 resolve + 37 refused (no custody at 09-22), 0 empty of 7,454; INF 875 resolve, 0 empty | HOLDINGS_ACCOUNT_CENSUS_49F_INF_20260924.json @acaa51635d |
| (3) COT soundness + window disclosed | disclosed in the receipts | COT_LABELLED_PUBLICATION_RECEIPT_20260924.json |

## Write claims

`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/*` and `data/assets/scripts/gold/investor_reporting/*` on the M
branch. No code edit is open.

## Next list (in order)

1. Andrew's firm-tab HAR, then /verify on the goal.
2. On the CTO's routing of the widening request (`CLASSIFIER_WIDENING_REQUEST_20260924.md` @d8a88cef4b; 287 rows, 69
   readers): if the CTO rules it this seat's, fill 49F's 62 CUSIP-only rows (symbol and name from the Schwab security
   master) in the Holdings producer.
Done this lease: the investor_reporting suite is green, 267 passed and 0 failed @1848e5caef. Each stale test's premise
is pinned (unattested currency, the required Eclipse capture, the lib.opal_naming binding); no assertion was loosened.

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| Served directory still 09-17. The S125 fix RAN at the 09-25 13:00Z fire: fired_on was recorded and the dispatch was reached at all 3 firms, then REFRESH_FAILED HAND_OVER_RUNNER_OFFLINE. The runner host starts 12:52Z (mdpf-feeder-trigger) and stops 16:41Z (ec2-auto-shutdown-enforcer), so the 13:00Z fire races it (row S126 @0efe2d88cc; ~P DISARMED it @61bce7ee33 -- the refresh now fires 09:30 America/New_York = 13:30Z EDT, inside the host window; next scheduled fire 2026-09-26T13:30Z). Ledger irpt-directory-refresh-s125-m-20260924 is HELD on that gate @d03b6e4 | 2.0.0_SA_COO~M (read S1); 2.0.0_SA_COO~P (schedule) | the 09-26 13:30Z fire, or one ad-hoc fire today while the host is Online (Andrew's word; up until 16:41Z) |
| Merging CLOUD into a seat branch is REFUSED by the law-lock budget: `.claude/skills/canonical-flow/SKILL.md` is 52,132 bytes and `dispatch/SKILL.md` 33,599, against 25,600 (org/law-edit-audit.log line `2026-09-24T23:04:17Z REFUSED-BUDGET author=2.0.0_SA_COO~M`) | 1.0.0_SA_CTO (the skills' owners) | the two files shrink under budget, or the gate exempts a merge carrying files the author did not change |
| Public reason for a selected account with no custody row: NOT_READY (transient) vs NOT_FOUND (`_authz/errors.py:58`) | 1.0.0_SA_CTO (contract) | the CTO rules the code |
| The FULL -> FAST line to the CVO ("FAST from 18:1xZ; pins graded after the fact") | 2.0.0_SA_COO~M | 3.0.0_SA_CVO registers live |
| IRPT_BCKEND-S124: the bundle mint reads working-tree bytes | owner of .tools/safe_deploy_core.py | next bundle re-mint |

## Limits

- No CVO verdict on any criterion.
- Two acts this session wrote served state:
  - the directory refresh deploy (ledger A1 closed, S1 open);
  - the three classified Holdings republishes (receipts).
