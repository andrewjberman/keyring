# CTO ruling -- muse (ms) on the OpalGateway MCP, 2026-10-16 ~06:4xZ

By `1.0.0_SA_CTO~Z`, under `/self-drive 30m sitez open calls`. Input: relay msg 34756 (muse, bus 7aca8520). Scope:
`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/MUSE_OPALGATEWAY_SETUP_SCOPE_20261016.md` @6e57b47a6a (4.0.0_SA_CRO~Z, read whole).

## Ruling

1. **The standing path is route C:** a muse-only narrowed OAuth client.
   - The gateway narrows an unscoped identity by client, so muse's client sees ONLY:
     - the mail reads: `list_recent_email`, `list_email_filtered`, `search_email`, `read_email`, `list_email_attachments`,
       `inspect_email_attachment`;
     - the Teams reads: `list_chats`, `read_chat_messages`, `read_chat_message_images`, `read_teams_attachment`,
       `list_teams`, `list_channels`, `read_channel_messages`, `poll_addressed_teams_messages`;
     - `whoami`;
     - `create_draft`, which is reversible.
   - It sees NO irreversible send (`send_email`, `reply_email`, `send_chat_message`, `send_channel_message`) and no other
     data source.
   - It is an NFRA_OPLGTW cell under `2.0.0_SA_COO~O`, cut AFTER the 2026-10-16 22:00Z gateway finish, with criteria:
     - a planted call by muse's client to a send tool and to a Schwab tool both REFUSE;
     - the same calls through Andrew's own client still pass.
   - Why: least privilege. Muse's ask is reads plus replies, and a draft gives Andrew the reply while he still presses
     send. The CVO's OG-ap-25 lesson applies again: a "confirm=True" guard the caller sets itself is a speed bump, not an
     approval.
2. **Route A (muse signs in as Andrew and carries his whole gateway reach, sends and client data included) is an ACT ONLY
   ANDREW CAN DO.** It hands his MASTER_ADMIN entitlement to another agent, which is an entitlement beyond any grant this
   fabric holds. The relayed "on Andrew's word per ms" is unverified (MSTR~Z msg 34756), so this fabric does not act on it.
   A recorded ANDREW_DIRECT naming muse and the full set, if he wants it before route C lands, is the citation.
3. **Route B (the `/hx/*` REST bearers) is not used for muse.** It is REST, not MCP, its mail route is limited to a table
   with no reply, and reusing COMM_ASSIST's bearer would make two callers indistinguishable in the audit.
4. **The dev-bid job** (scope section 7) is COMM_ASSIST's scope and is held on the laptop as row `87a2`. Nothing is moved here.

## Addendum ~06:5xZ -- Andrew-direct: the work folds into NFRA_OPLGTW under `2.0.0_SA_COO~O`

Recorded by `4.0.0_SA_CRO~Z` at `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20261016_065xZ_MUSE_GATEWAY_SCOPE_FOLDS_INTO_OPLGTW_COO_O.md`
@66f25c55e2. VERBATIM: "ok i want the COO~O to have this work folded in to OPLGTW, let CTO~Z know that."

This confirms ruling 1's placement: route C is an NFRA_OPLGTW cell under `2.0.0_SA_COO~O`, after the 22:00Z finish. His words
name the work's home, not route A, so open act row `sitez-20261016T063450Z-8f44` (full reach) stays open for his own word.

## Addendum ~07:0xZ -- Andrew-direct: route A authorized for now; route C narrows to the M365 Teams/email tools

Record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_070xZ_MUSE_FULL_GATEWAY_ACCESS_FOR_NOW_M365_TEAMS_EMAIL_TARGET.md`.
VERBATIM: "im fine with muse having full access for now, ultimately it should just have m365 teams/emai, but we can get there."

- Ruling 2 is answered: muse may sign in as Andrew now. Row `sitez-20261016T063450Z-8f44` closes ruled-by andrew.
- Ruling 1's tool set is REPLACED. Route C's narrowed client gets the M365 mail and Teams tools (read and send) plus `whoami`,
  and no other data source. Its criteria: a planted call by muse's client to a Schwab tool and to a portal tool both REFUSE,
  a mail read and a Teams read pass, and Andrew's own client is unchanged.
