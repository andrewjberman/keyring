# ANDREW-DIRECT -- MSP Analyst channel identity: pilot on federated chat, production on a multi-tenant bot, sender-domain allowlist

**Recorded by:** 4.0.0_SA_CRO~O (site Z)
**Channel:** Claude Code terminal session of 4.0.0_SA_CRO~O, 2026-09-30 ~03:15Z (2026-09-29 ~23:15 ET)
**Context:** the Andrew + CRO~O discussion requested in 1.0.0_SA_CTO~O msg 26827, primer
`org/tier1_exec/1.0.0_SA_CTO/deliverables/PRIMER_MSP_ANALYST_FOR_CRO_O_20260930.md` (@9dc713f359), open question 1
(channel identity).

## 1. The question Andrew answered (CRO~O's options, as put to him)

1. Federated chat to an Opal-owned "Opal Analyst" user. The partner's IT does nothing if their Teams allows chats with
   outside organizations; asker identity is the sender's tenant ID and user ID on the message (UNVERIFIED); we poll.
2. Guest accounts. Dropped in the recommendation.
3. One multi-tenant Teams bot. The partner's IT allows the app in the Teams admin center; tenant ID and user ID are
   signed by Microsoft on every message; push.

CRO~O recommendation: pilot on 1, production on 3.

## 2. Andrew, verbatim

> "I dont know who runs IT at either but this is easy enough to figure out. I agree with 1 pilot, 3 prod. I also think
> we should make messages to this agent key on the sender's domain. If there is ever a sender to the agent that is not
> @opalinvest.com, @49financial.com, @inflectionwealth.com, or @cottonwoodmail.com, then the agent should not even
> respond. This should never happen, but it's a good guardrail to have preemptiveluy. ;"

## 3. What this records (the ruling is the quote above; this is a reading aid, not a widening)

- Channel: option 1 (federated chat) for the pilot; option 3 (multi-tenant bot) for production.
- Sender-domain allowlist on the agent's inbound messages: `opalinvest.com`, `49financial.com`,
  `inflectionwealth.com`, `cottonwoodmail.com`. Any other sender domain: the agent does not respond.
- Partner IT contacts at Inflection and Cottonwood: unknown; Andrew judges them easy to find. Not assigned to anyone here.

## 4. Not decided here (CRO~O proposals, for the continuing discussion -- NOT part of the ruling)

- Whether the domain check stands alone or must also agree with the tenant ID (tid -> firm) on the same message.
- Where the check sits: the agent harness, the router, the gateway, or more than one.
- ~~Whether a refused message leaves an audit record (not responding and not recording are different acts).~~
  ANSWERED in section 5.
- How a guest-form address (`...#EXT#@...`) is read against the allowlist.

## 5. Andrew, verbatim, same channel, 2026-09-30 ~03:23Z

Asked by CRO~O: "Do you want refused messages logged silently, or dropped with no trace?"

> "Refused messages absolutely should be logged."

Reading aid: a message refused by the sender-domain allowlist gets no response AND leaves a log record. Where the
record lives and what it carries is not decided here. Still open from CRO~O's proposal (no answer yet): mapping each
allowed domain to its Microsoft tenant ID and enforcing on the tenant ID, and enforcing at the gateway as well as the
harness. (Both answered in section 6.)

## 6. Andrew, verbatim, same channel, 2026-09-30 ~03:26Z

Asked by CRO~O: yes or no on (1) mapping each allowed domain to its Microsoft tenant ID and checking the tenant ID on
every message (the one-time lookup being a Microsoft endpoint that needs his word), and (2) enforcing at the gateway
as well.

> "Yes Check tenant ID if its surfaced, i like tenant id and domain check. yes to enforce at gateway as well."

Reading aid:
- Both checks: the sender's domain AND the tenant ID, the tenant ID checked where the message surfaces one.
- The check is enforced at the gateway as well as at the agent.
- NOT read as given: authorization for the one-time domain-to-tenant lookup against a Microsoft endpoint. The quote
  does not name it; vendor egress needs his explicit per-use word, so it stays unauthorized until he says so.

## 7. Andrew, verbatim, same channel, 2026-09-30 ~03:28Z (unprompted)

> "The truth of the matter is, it is probably easier to just run MCP on our server for all clients, rather than
> building a separate server per client, that would be annoying, better to just handle their channels and etc at some
> central control plane and use the one server."

Reading aid:
- Direction: ONE MCP server for all client firms, with channels and the rest handled at a central control plane; NOT a
  separate server per client. This departs from the primer's section 4 drawing, which showed a gateway per firm.
- Andrew's wording is "probably"; recorded as his stated direction, not a final design.
- Not decided here: how firm isolation holds inside one server (answered in section 8).

## 8. Andrew, verbatim, same channel, 2026-09-30 ~03:31Z

Asked by CRO~O: the one server's own AWS identity holds no read on any firm's data; per request, the router maps the
tenant ID to a firm and the server assumes that firm's role for that request only, so a scoping bug is refused by AWS
rather than leaking data. "Yes on the per-firm role?"

> "yes to per-firm role"

Reading aid: firm isolation inside the one server is a per-firm AWS role assumed per request, selected by the
tenant-to-firm router; the server's own identity reads no firm data. Role names and policies are not decided here
(they come from the LGIC builders, CLAUDE.md rule 30). Still unauthorized: the Microsoft domain-to-tenant lookup.

## 9. Andrew, verbatim, same channel, 2026-09-30 ~03:43Z -- primer open question 2 (asker identity across tenants)

Put by CRO~O: grants already key on tenant ID + user ID (`POLICY#<tid>#<oid>`, `app/access_state.py`), the pair a
partner advisor's message carries. Options: (A) Opal administers each advisor's grant; (B) the partner's admin
self-serves in the MCPORTAL Entitlements tab; (C) Opal sets a per-firm ceiling and the partner's admin assigns within
it. Learning the user ID: an allowed-tenant advisor with no grant is refused and logged (section 5); that log is the
onboarding queue, and one approval turns an entry into a grant. Recommendation: A for the pilot, C for production.
"Agree?"

> "agreee"

Reading aid: pilot grants are Opal-administered per advisor; production is an Opal-set firm ceiling with the partner's
admin assigning within it; the refusal log doubles as the onboarding queue. Who at Opal approves an entry is not
decided here.
