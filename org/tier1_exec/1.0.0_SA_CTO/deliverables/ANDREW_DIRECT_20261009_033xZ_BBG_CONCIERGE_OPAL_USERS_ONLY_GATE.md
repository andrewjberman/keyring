# ANDREW-DIRECT 2026-10-09 ~03:3xZ (1.0.0_SA_CTO~O terminal, site Z) -- the Bloomberg concierge answers Opal Capital users only

He gave this in-session at the `1.0.0_SA_CTO~O` terminal, right after
`ANDREW_DIRECT_20261009_032xZ_OPAL_GATEWAY_BBG_MIRRORS_OPALGATEWAY.md` (the mirror).

## His words, VERBATIM AND ENTIRE

> "it should only accept inquiries from opal capital users however, no external users, should not even respond at all, or otherwise be gated from responding to any user without an @opalinvest.com entra ID"

## What it rules, at the width written

| Item | Reading |
|---|---|
| Subject | The `opal-gateway-bbg` / `opalbloomberg` concierge (0.0.3_BG_BBGTerminal), which now mirrors Andrew's access. |
| Who it serves | Only a user whose Entra identity is `@opalinvest.com`. |
| Everyone else | No response at all, never even a refusal, or else a gate that keeps it from responding to anyone without that Entra ID. |
| It is a gate | Andrew asked for it in these words, so it is not an inferred gate (CLAUDE.md section 2). |

## Ruled by this seat (NFRA_OPLGTW's CTO), at the width written

1. **The mechanical gate sits in the gateway, for the `opalbloomberg` principal.**
   - `poll_addressed_teams_messages` and the chat and channel reads return no message whose sender's Entra UPN is not
     `@opalinvest.com`. The seat never sees an external inquiry.
   - `send_chat_message` and `send_channel_message` refuse to send into a chat or channel holding any member outside
     `@opalinvest.com`.
   - The identity comes from Graph's sender and member records, never from a display name. An unreadable sender or roster
     counts as external.
2. **The mirror ships only with the gate.** The mirror is the v2.3 grant of Andrew's width to `opalbloomberg`. If the gate
   cannot ride the same release, the mirror waits.
3. **The seat's own layer belongs to the `0.0.3_BG_BBGTerminal` seat's CTO.** That is the `bg-teams-assist` skill's own
   check, owned by `1.0.0_SA_CTO~Z`. It is defence in depth, not the gate.

## Not said

- Nothing about the per-identity tool and data rules, which stay deferred ("eventually we will make rules but not yet").
