# /email-check — what actually landed in the inbox that matters

**Purpose (Andrew-direct, 2026-08-31 ~19:5xZ, MSTR terminal, VERBATIM):** *"THe purpose of this is to
basically analyze what is in my inbox. 99% of emails in my inbox are useless."* and, narrowing it:
*"if its not from somebody i explicitly wrote, or an opal employee/partner, maybe thats how we do it we
include whitelisted domains, then it doesnt matter."*

When Andrew runs `/email-check`, he wants ONE thing: **the short list of mail that is actually his to
read, and a count of what was dropped.** Not a summary of his inbox. Not triage advice.

---

## The rule

```
  KEEP  if  sender domain  in allow_domains
        or  sender address in allow_addresses / allow_addresses_automated
  DROP  if  local-part     in deny_local_parts      <- applies INSIDE allowed domains too
  KEEP  anyway if the subject starts with Re:/RE:/FW:/Fwd: AND the sender is otherwise allowed
```

Allowlist lives at **`.claude/skills/email-check/contacts.yaml`**. **This skill NEVER edits it** — it proposes
additions in the residual and Andrew adds them.

⭐ **THE FINDING THE RULE IS BUILT ON: A PERSON-SHAPED SENDER IS NOT SIGNAL.** Measured 2026-08-31 over
~55 messages / 3 days: `cgavigan@bairdstrategas.com`, `drissmiller@bairdstrategas.com`,
`sean.farrell@fundstrat.com` are named humans writing *"Andrew, ..."* — and all are bulk research
distribution, 12 of them in 3 days. **Sender IDENTITY is the test; sender SHAPE is not.** Do not add
heuristics that reward a real-looking human name.

## Step 1 — Pull

`mcp__opal-gateway__list_recent_email(top=<N>, since_iso=<optional>)`. Default **`top=60`**, which covered
~3 days on the measured mailbox. `--since <ISO>` sets `since_iso`; `--unread` sets `unread_only=true`.

⛔ **ONE CALL PER PAGE. DO NOT call `read_email` per message to enrich** — see HAZARDS.

## Step 2 — Classify

Apply the rule to each message using only `from.emailAddress.address` and `subject`. Two special types
carry `@odata.type`:
- `#microsoft.graph.eventMessageRequest` = a **meeting invite** — keep if the sender is allowed.
- `#microsoft.graph.eventMessageResponse` = an **Accepted:/Declined:** notice — **always DROP**, including
  the ones that appear to come from Andrew himself via an Exchange `/O=EXCHANGELABS/...` legacy DN.

## Step 3 — Report, in this shape

```
EMAIL CHECK — {n} of {m} worth reading ({date time}, window {oldest}..{newest})

  {age}  {Sender Name} <{address}>
         {subject}
         {one line of why it was kept: allowed-domain | allowed-address | conversation Re:/FW:}

DROPPED {m-n}. Distinct senders not on the list ({k}):
  {address}  x{count}   {most recent subject, truncated}
  ...
```

- **Signal first, newest first.** No prose summary, no advice, no "you may want to".
- ⛔ **THE RESIDUAL IS MANDATORY AND IS HALF THE SKILL.** Print the dropped COUNT and the DISTINCT
  UNKNOWN SENDERS every run. **A false negative is the only expensive error here** — a real mail dropped
  silently is invisible forever, while a false positive costs one line of reading. The residual is what
  makes the expensive error visible and grows the allowlist.
- **Never quote body content beyond the subject line** unless Andrew asks for a specific message.

## Discipline

- ⛔ **READ-ONLY. NEVER** mark read, move, delete, flag, draft, or send. `reply_email` / `send_email` /
  `create_draft` are OUT OF SCOPE for this skill; sending is egress and needs Andrew's explicit per-use
  word every time.
- ⛔ **AD-HOC ONLY. DO NOT schedule it, cron it, or wire it to a Monitor.** A scheduled inbox checker that
  notifies is a MONITOR, and that is inside the standing alert/monitor moratorium (`MDPF_DEBTCLEAN_PRD`
  §11-12). Andrew ratified ad-hoc on 2026-08-31; a cadence needs a fresh word.
- ⛔ **NEVER persist message bodies, previews or subjects into the repo.** The allowlist holds ADDRESSES,
  which is contact data, not correspondence. Nothing else about his mail gets committed.
- **Zero signal is a real answer:** print `Nothing in the inbox needs you. Dropped {m}.` and stop.

## ⛔ HAZARDS — measured 2026-08-31, do not re-derive

**The gateway hard-codes its `$select`.** `list_recent_email` returns exactly
`id, subject, from, receivedDateTime, isRead, bodyPreview` and nothing else. Therefore:
- **NO `toRecipients` / `ccRecipients`** — *"was I the only recipient"* is **NOT COMPUTABLE** from the
  list. It would cost one `read_email` per message (~60 calls/run). The allowlist exists precisely so
  that question never has to be asked.
- **NO `conversationId` and NO `internetMessageHeaders`** — reply-threading cannot be done by header.
  The `Re:`/`FW:` subject prefix is a HEURISTIC standing in for it, and it is the best available.
- **NO `parentFolderId`** — Inbox vs Sent cannot be distinguished from the list.

**Sent Items enumeration is UNCONFIRMED.** `search_email` is full-text and returned sparse,
non-recency-ordered results (4 hits, all ~9 months stale) when probed. **So "a reply to something I sent
in the last 2 weeks" is NOT directly implementable** — and it does not need to be: if Andrew wrote to
someone, that someone belongs on the allowlist, so the reply is kept by the sender rule. **The allowlist
SUBSUMES the reply rule.** The one case it misses — a first-ever reply from someone newly written to —
is exactly what the residual surfaces.

**The mailbox is `Andrew@opalinvest.com`** (`whoami`), not the `andrew@fideles.capital` identity used for
attribution elsewhere in this workspace. Correspondence with `@opalinvest.com` colleagues IS in scope.

## Invocation forms

| Form | Behavior |
|---|---|
| `/email-check` | last 60 messages, full rule, residual printed |
| `/email-check --since YYYY-MM-DD` | `since_iso` window instead of a count |
| `/email-check --unread` | unread only |
| `/email-check --all` | print the dropped messages in full, not just the sender tally |

## Cross-references

Allowlist `.claude/skills/email-check/contacts.yaml` · ledger LD-0489 · gateway tools
`mcp__opal-gateway__{list_recent_email,search_email,read_email}` · sibling read-and-rank skills
`/open-calls`, `/next-steps` (same card discipline: signal first, residual named, no padding).
