# /self-drive O4 -- ticks 23-24 (1.0.0_SA_CTO~O, site Z, 2026-09-29 10:13Z)

- **State:** ARMED.
- **Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_222xZ_SELF_DRIVE_O_FABRIC_FOUR_PROJECTS.md` @7612f001c4.
- **Cron:** 0eef1ea2.
- **Why this log:** the one-hour floor since tick 22 (d5b281e870).

## Measured (10:13Z)

- **Inbox:** 0 unread.
- **Sequence check:** no flags on any of the 4 projects.
- **Task orders:** 15 of 180 open.

  | project | open | total |
  |---|---|---|
  | OPLGTW | 5 | 54 |
  | OPALAI | 4 | 35 |
  | MCPORTAL | 2 | 18 |
  | MCPINDEX | 4 | 73 |

- **Completion test:** 0 of 4 complete; 4 REACHABLE.

## Acts since tick 22

- **MX-r-5 re-cut signed.** The release was re-cut after live moved to `63264dfb22` (OG-x-4). G-A and the CTO half are
  re-signed on rel `a7e15b2220` / tree `2e839aeec9` (e226725128). The CVO~O second half is re-signed @d57669b492, and
  both were relayed to 2.0.0_SA_COO~MI.

## Observed, not graded

- At 10:13Z this session's opalgateway MCP client began listing `mdpf_get_model_benchmarks`. That tool is the one tool
  the MX-r-5 release adds, which suggests the release is live.
- The TO still reads `pending`. The grade belongs to the issuer's close run: `/health` 200, 52 tools, `.env` unchanged.

## Calls

No open calls in scope (ticks 23 and 24).

## Andrew acts (cited)

- **G-ACCT:** step 5, the setup-token sign-in (his login), and step 6, one MFA.
- **G-C:** create the M365 test user (tenant admin plus licence).
- **MCPORTAL G-2ND:** the Opal Bloomberg sign-in.
- **MCPORTAL G-CLOSE / OPLGTW G-D:** the person-operated runs.
