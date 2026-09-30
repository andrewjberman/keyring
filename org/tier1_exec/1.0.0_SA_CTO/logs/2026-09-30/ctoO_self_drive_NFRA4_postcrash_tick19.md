# /self-drive NFRA four -- ticks 18-19 + MSP events (1.0.0_SA_CTO~O, site Z, 2026-09-30 03:24Z-04:2xZ)

- **state:** ARMED
- **Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260929_182xZ_SELF_DRIVE_O_NFRA_FOUR_PROJECTS_POSTCRASH.md` @680afc11fd
- **Cron:** 625c63e4

## Measured (the four projects)

- **Inbox:** 0 unread at both ticks (six CRO~O messages in between, all acked).
- **Open TOs:** 12 of 180 (last-tag read). OG 4, OA 4, MP 2, MX 2.
- **Scope commits by other seats since 03:45Z:** none.
- **Completion:** 0 of 4. 1 REACHABLE (MCPINDEX), 3 UNREACHABLE (acts per the tick-11 log).

## Andrew's MSP decisions, as recorded by 4.0.0_SA_CRO~O

All six are in the same record, `org/tier1_exec/4.0.0_SA_CRO~O/deliverables/ANDREW_DIRECT_20260930_0315Z_MSP_ANALYST_CHANNEL_PILOT_FEDERATED_PROD_BOT_SENDER_DOMAIN_ALLOWLIST.md`.
Each binds the MSP design only, and none is applied to the four projects' open orders.

| msg | section @commit | decision |
|---|---|---|
| 26876 | s.2 @e62c14116d | pilot on federated chat, production on a multi-tenant bot; four-domain sender allowlist |
| 26879 | s.5 @ac103f1cda | "Refused messages absolutely should be logged." |
| 26881 | s.6-7 @0594f19025, @23c2020ddd | tenant-id + domain check, enforced at the gateway too; ONE MCP server for all clients via a central control plane |
| 26883 | s.8 @a289703ffc | "yes to per-firm role": the server identity reads no firm data; per request it assumes the firm role the router selects |
| 26886 | s.9 @6c61d0ce73 | pilot grants are Opal-administered per advisor; production uses an Opal firm ceiling with partner-admin assignment; the refusal log is the onboarding queue |
| 26899 | s.10 @6cc12c2e06 | new project NFRA_MCPMSP; 6 cards approved (go-live bar, tenant ids learned without a lookup, per-firm key + cap in Secrets Manager, current buckets, governance) |

s.7 supersedes the per-firm gateway boxes in this seat's MSP diagram and primer section 4. The one server holds each firm
apart by per-request role, not by separate gateways.

## This seat's act: NFRA_MCPMSP L2

- The L1 brief `docs/briefs/nfra-mcpmsp-msp-analyst-brief-20260930.md` (@77ddde1d13, msg 26905) was read in full.
- `/endpoint --forward` gives 11 outcomes, FWD-1 through FWD-11. FWD-1 is the thread: an Inflection advisor gets an answer
  in Teams from Inflection's data.
  - Reachable by working: 6 of 11.
  - 5 need external acts: partner IT allowing external chat and the app, named advisors, and Andrew's go-live word.
- Record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_NFRA_MCPMSP_20260930.md` @64617f8afa. NOT YET LANDED in
  a PRD. It waits on Andrew's DONE WHEN confirmation, then L3 registration (proposed directive D6) and the L4 PRD.
- NFRA_MCPMSP is outside this loop's four-project scope; it runs on Andrew's own word.

## Calls

No open calls in scope (ticks 18-19).

## Acts only Andrew can do (each cited)

- Confirm NFRA_MCPMSP's DONE WHEN lines (his 2026-09-03 word reserves that confirmation to him).
- G-ACCT step 5 (his login or spend decision). MCPORTAL G-2ND and G-CLOSE. OPLGTW G-D and Part D. MX-t-11: his
  widening word. G-C is external at Opal IT.

## Compiler Tools

- None beyond git reads, the task-order last-tag census and reading the brief.
