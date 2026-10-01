# SELF-DRIVE OPALAI_MCP_SITEZ -- tick 1 -- 1.0.0_SA_CTO~O

**archetype:** COORDINATE
**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_04xxZ_SELF_DRIVE_OPALAI_MCP_SITEZ.md` @80102ed73d
**Ticks covered:** 1 (2026-10-01 ~04:0xZ-04:1xZ). Cron job 84d0ab03, every hour at :07 local, session-only.
**state:** ARMED

## Scope

| project | directive | fabric | status | dep_stage | open TOs | issuer lane | lane live? |
|---|---|---|---|---|---|---|---|
| NFRA_OPLGTW | D9 | site-z | active | EXECUTING | 9 (3 pending, 6 staged) | 2.0.0_SA_COO~O | dark |
| NFRA_MCPINDEX | D9 | site-z | active | EXECUTING | 4 pending | 2.0.0_SA_COO~MI | dark |
| NFRA_OPALAI | D6 | site-z | active | EXECUTING | 4 pending | 2.0.0_SA_COO~AI | dark |
| NFRA_MCPMSP | D6 | site-z | active | EXECUTING | 6 (1 pending, 5 staged) | 2.0.0_SA_COO~MS | dark |
| NFRA_MCPORTAL | D6 | site-z | active | EXECUTING | 2 staged | 2.0.0_SA_COO~MP | dark |

Denominator: 5 projects, 25 open orders. Excluded: NFRA_TRNSPT (laptop fabric), all TAXSMA work (Andrew).
Sequence (`sequence-check`, file @2bed2ad08b): no WAITING or HELD flag on any of the 5. LANE-DARK on OPLGTW and
MCPINDEX. Next COO slot in the sequence's order: MDPF_CANON (laptop), then NFRA_MCPINDEX, then NFRA_OPLGTW.
Inbox: 0 unread at tick start. Active commitments: 1 line in 26 ledgers, none in scope.

## Calls ruled by the driver (5)

| # | call | REC = ruling | reason |
|---|---|---|---|
| 1 | OPLGTW Z-S24: where the principal rosters live | ONE Secrets Manager entry, SECRET-grammar name, read host-side at deploy, role read grant on exactly it | matches the other gateway bearers; removes the single-device copy that blocks every non-~O releaser |
| 2 | OPLGTW Z-W17-S1: rotate the 64-hex value printed into SSM output | ROTATE at the next gateway release | SSM keeps command output; the release rewrites `.env` anyway, so rotation costs nothing extra |
| 3 | OG-rl-1 waits on G-SENDERS | NOT a gate | PRD C7 already makes the sender table a data asset that grows when Yang's addresses arrive |
| 4 | OPALAI blocking reads "BLOCKED on Andrew (G-ACCT step 5)" | STALE; step 6 measured DONE | the Analyst passed the identity gate at ~01:45Z; the remaining gate is the ~AI cut of Z-S50 + the refs ruling |
| 5 | Release order across OPLGTW / MCPINDEX / MCPMSP on one host | DESIGN FORK, research asked | `4.0.0_SA_CRO~O` `/closer trace`; ruled on the report |

Earlier this session (before arming, @2b8f3151c6): C7 headless prefixes (PRD v1.3) and the Analyst refs read ruling.

## Acts taken

- Arming record @80102ed73d; cron 84d0ab03.
- `project.json` blocking prefixes on NFRA_OPLGTW and NFRA_OPALAI (this commit).
- Messages: `4.0.0_SA_CRO~O` trace ask (delivered); `0.0.0_AB_MSTR~Z` seat ask for COO ~O, ~MI, ~AI (delivered);
  `2.0.0_SA_COO~O` rulings 1-3 (queued, lane dark; the carrier is the project blocking field).

## Acts only Andrew can perform (each with its citation)

- OG-g-1: the unprivileged M365 test user from Opal IT (entitlement beyond his grants; record
  `org/tier1_exec/2.0.0_SA_COO~O/ANDREW_DIRECT_20260930_205xZ_NEXT_CALLS_GO_WITH_RECS_PART_D_GIVEN.md`).
- G-TEAMS-TX: the Teams transcript tenant settings via IT (PRD v1.3 C7 preconditions).
- MX-t-12: G-W (his "NOT YET" stands; MCPINDEX blocking).
- MCPORTAL MP-c-1 G-CLOSE and MP-v-1 G-2ND: his own Entitlements-tab acts and a person signing in (MCPORTAL blocking).
- MCPMSP A1 gates G-USER, G-IT-INF, G-ADVISOR, G-FIRM, and G-MSPID (identity/entitlement; PRD v0.4); FWD-8 G-KEY (spend).
- G-PUSH: shared-branch push by `0.0.0_AB_MSTR~Z` on his word (org/XXX.md shared-branch law).

## Completion test

NOT DONE: 0 of 5 projects complete. REACHABLE 4 (OPLGTW, MCPINDEX, OPALAI, MCPMSP have seat-actionable orders once
their lanes are seated). UNREACHABLE 1: NFRA_MCPORTAL (both open orders wait only on Andrew's acts G-CLOSE and G-2ND).

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| directives-check | `--json` | 15 live directives | D9 device label vs member fabric mismatch surfaced to MSTR~Z |
| sequence-check | header + `--project` x5 | rc=0 all | LANE-DARK x2; capacity reads 1 live COO, no cap ruled |
| active-commitments | bare | 1 line / 26 ledgers | none in scope |
| prd-signoff | `status NFRA_OPLGTW` | ADMITTED at v1.3 | bound to the ENDPOINT hash |

**What worked:** the project blocking fields carried every parked item with its owner, so the call census was one read.
**Gap:** `to-check.py --assignee` returned other seats' orders; the per-project census was done by reading `<status>` tags.
