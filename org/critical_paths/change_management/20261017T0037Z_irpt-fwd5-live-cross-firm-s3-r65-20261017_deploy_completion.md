# Deploy Completion Record
**Date opened:** 2026-10-17T00:37:16.369705+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-RUN-FWD5.live-cross-firm-s3-ib2 (third sitting, round 65, cell AR-tz-75): two scoped principals (digests 28cb5947d068 and 7b925797fd61) minted once each in opal-users-v2, a control then a firm-B run for each of two targets (packaged and synthetic ticket), then BOTH removed. Worktree union read 2026-10-17T00:4xZ: 99 worktrees, 2050 marker files, 16 naming the users table, ticket service or FWD5, all 16 ledgers CLOSED.
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| M | activation | TWO users rows (digests 28cb5947d068 and 7b925797fd61) minted once each by fwd5_mint.py with the stated scopes, entitlement_rows 0 | MINT-OK READBACK-OK and MINT-SCOPE lines for both |  | OPEN |
| C1 | verify | PACKAGED target control run (--control) as the entitled identity | driver exit 0 |  | OPEN |
| F1 | verify | PACKAGED target firm-B run (only after a control exit 0) | driver exit and report counts recorded |  | OPEN |
| C2 | verify | SYNTHETIC target control run (--control) | driver exit 0 |  | OPEN |
| F2 | verify | SYNTHETIC target firm-B run (only after a control exit 0) | driver exit and report counts recorded |  | OPEN |
| R | activation | removal of BOTH principals and ABSENT by the email GSI and a ConsistentRead for each, then r56_checks absent | R56-ABSENT-OK |  | OPEN |

## Log

- 20261017T003716Z OPENED by 0.7.0_AE_CloudOps~IB2 with 6 leg(s)
