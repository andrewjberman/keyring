# /self-drive tick 1 -- ~O fabric, four projects (1.0.0_SA_CTO~O)

**archetype:** COORDINATE

- Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_222xZ_SELF_DRIVE_O_FABRIC_FOUR_PROJECTS.md`
  @7612f001c4. Cron `0eef1ea2` (`12,42 * * * *`, session-only, 7-day expiry).
- Ticks covered: 1 (~22:2xZ). **state: ARMED**

## Scope

| project | directive | status | dep_stage | TOs (open / total) | COO |
|---|---|---|---|---|---|
| NFRA_OPLGTW | D9 | active | EXECUTING | 14 / 50 | `2.0.0_SA_COO~O` |
| NFRA_OPALAI | D6 | active | EXECUTING | 15 / 30 | `2.0.0_SA_COO~AI` |
| NFRA_MCPORTAL | D6 | active | EXECUTING | 3 / 18 | `2.0.0_SA_COO~MP` |
| NFRA_MCPINDEX | D9 | active | EXECUTING | 4 / 64 | `2.0.0_SA_COO~MI` |

The open count is the last `<status>` tag per order file: 36 open of 162. Device: site Z (every project row reads
`fabric: site-z`).

## Measurements

- Inbox: 0 unread at the tick start; 4 COO arm replies acked since (26248, 26249, 26251, plus ~MI pending).
- Active commitments: 1 line in 1 of 25 ledgers (this seat's G-A ruling to COO~MI).
- Sequence: NFRA_OPLGTW and NFRA_MCPINDEX are PLACED at stage 0, with no WAITING or HELD flag. NFRA_OPALAI and
  NFRA_MCPORTAL are not placed, so they are driven as before.
  - DRIFT on both placed rows: the file says `laptop`, the register says `site-z`. Raised to `1.0.0_SA_CTO~Z`
    (msg 20260928T221833Z).
  - The D9 directive row's `device: LAPTOP` is recorded in the arming record as register drift.

## Open calls in scope

0 at Andrew. All ~O calls were answered 2026-09-28 (records @7bfa5811c6, @cd53207, @805bcdfe14). 0 pitched to
CVO~O, and no GOVERNANCE or DESIGN fork is open.

## Paired halves

| COO | project | cron |
|---|---|---|
| ~O | NFRA_OPLGTW | 3c719297 (27,57) |
| ~MP | NFRA_MCPORTAL | 8445c0ae |
| ~AI | NFRA_OPALAI | e6d80809 |
| ~MI | NFRA_MCPINDEX | reply pending |

## This seat's owed acts

- **G-A:** the s.8.1 arch-gate for `opal_discover` and `portal_index`, when COO~MI sends MX-r-4's PHASE A pin.
- **G-C:** the OPLGTW record, when COO~O seats a CloudOps identity admin (before E1).

## Completion test

NOT DONE: 0 of 4 projects complete. REACHABLE 4, UNREACHABLE 0.

## Compiler Tools

- `directives-check.py --json`: 15 live; D6 SITEZ holds 2 in scope, D9 LAPTOP holds 2.
- `sequence-check.py --project` x4: DRIFT=1 on OPLGTW and on MCPINDEX, none on the other two.
- `active-commitments.py`: 1 line.
- A Python census of the order files' last `<status>` tag: 36 open of 162. It worked. The gap: `to-check.py --all`
  prints rows without a per-project open count.
