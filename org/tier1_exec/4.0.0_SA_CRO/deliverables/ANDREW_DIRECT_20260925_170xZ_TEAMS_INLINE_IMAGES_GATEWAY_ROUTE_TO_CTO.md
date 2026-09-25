# ANDREW-DIRECT 2026-09-25 ~17:0xZ -- the gateway cannot read pasted Teams images, and its chat reader 500s; routed to the CTO

**Channel:** the 4.0.0_SA_CRO terminal. **Recorded by:** 4.0.0_SA_CRO, same turn. Vintage: CLOUD @`1b923deaf1`.

## Verbatim

> i own the gateway im a cloud application administrator, see if there are entitlements we need to be able to provide
> to this end

> yes

The "yes" answers this seat's question: "Want me to send both code gaps to the CTO? Either fix changes the live
gateway server, so it's their call."

## Why it matters now

Lauren Harmon's Trade Submission report (record
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260925_152xZ_PM_AUTOSAVE_PFOE_500_ROUTE_TO_CTO.md`) could
not be read through the gateway:
- her pasted screenshots are unreadable by any gateway tool;
- `read_chat_messages` on her chat returns `Graph 500 InternalServerError: Error while processing response` at
  `top >= 3` and reads at `top = 1` and `top = 2` (measured 2026-09-25 ~15:0xZ).

Andrew had to paste the images into the terminal by hand.

## Finding 1 -- no new Graph permission is needed

- The gateway requests delegated `Chat.ReadWrite` (`infra/aws/ec2/opal-gateway/app/config.py:53`). The comment at
  `:39-47` says every string was verified on the App-2 admin-consent screen.
- The scope is applied and exercised: chat reads on Lauren's thread succeed at `top = 1` and `top = 2`. A missing
  scope would return 403 on every read, not 500 on the wider window only.
- Microsoft Graph documents `Chat.Read` or `Chat.ReadWrite` (delegated) as sufficient for
  `GET /chats/{chat-id}/messages/{message-id}/hostedContents/{id}/$value`. INFERRED from Microsoft's documentation;
  not exercised, because no gateway tool calls that endpoint.

## Finding 2 -- code gap A: no tool fetches inline (pasted) images

- An image pasted into a Teams message is a `hostedContents` item, a navigation property that `$select` cannot
  reach. The gateway says so itself: `app/tools.py:662-663` and the `read_teams_attachment` docstring at `:690-692`.
- Need: a read tool (or a `read_chat_messages` option) that lists a message's hosted contents and returns each one's
  bytes, so an agent can parse the image.

## Finding 3 -- code gap B: the chat reader's `$select` makes Graph return 500

- `read_chat_messages` sends `_TEAMS_MSG_FIELDS` (`app/tools.py:664-667`, used at `:724`), added at `684e7eb90a`
  (2026-09-11) and deployed 2026-09-18 at gateway commit `1764e54a16`.
- Diagnosed twice, independently:
  - `4.0.0_SA_CRO~Z`, commit `2af2c4530c`
    (`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/TEAMS_WATCH_THREE_DEFECTS_AND_AN_IDENTITY_SWAP_20260924.md`). The
    failure depends on chat content; channel reads with the IDENTICAL projection succeed. Falsifier named: the old
    six-field `$select` on the same chat.
  - `0.9.0_WK_NFRA_OPALAI~4`, commit `e459c5d6df` (READ_FAILURE_DIAGNOSIS.md).
- No commit to `app/tools.py` since `f49ea6ce48` (2026-09-17) touches the projection. The defect is live.

## Finding 4 -- one real permission gap, not needed today

- The READ_ONLY user tier cannot read chats at all: App-2 consented only the ReadWrite forms, with no `Chat.Read`
  (`app/config.py:73-84`; runbook `docs/runbooks/opal-gateway-readonly-scope-gap.md`).
- Andrew can grant that delegated consent himself: per Microsoft's documentation, a Cloud Application Administrator
  can grant tenant-wide admin consent for delegated permissions. Trigger: a read-only identity that needs chat reads.

## Done when

1. A gateway read returns the bytes of a pasted image in Lauren Harmon's chat (the 2026-09-25 ~10:35 AM ET
   messages), on Andrew's identity.
2. `read_chat_messages(<Lauren's chat id>, top=25)` returns 25 messages with no Graph 500.

The owner is `1.0.0_SA_CTO`: either fix changes the live gateway on EC2.
