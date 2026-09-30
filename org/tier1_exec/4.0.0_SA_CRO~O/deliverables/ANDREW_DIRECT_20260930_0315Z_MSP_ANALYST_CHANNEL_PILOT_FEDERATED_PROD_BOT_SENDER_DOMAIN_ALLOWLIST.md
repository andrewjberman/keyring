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
harness.
