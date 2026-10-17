# Client Ops Early Warning -- design (fast-path)

**Author:** `4.0.0_SA_CRO~DELL1` | **Date:** 2026-10-16 | **Status:** DRAFT for Andrew

**Authority:** `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261016_1801Z_CLIENT_OPS_EARLY_WARNING_FAST_PATH.md`.
That record carries the fast-path, the explicit lift of the alert moratorium for this scope, "cast it on tv", and
"delta 5s first, i approve, teams later".

**Evidence base:** 48 client-ops failures YTD, 33 of them strict. The ledger is
`scratchpad/postmortems/ytd_ledger.md`; this design copies it into the repo as the replay set (section 7).

---

## 1. What it does

Opal sees a client-ops item falling through the cracks before an advisor, partner or client does. Today, 45 of the 48
YTD failures were found by someone outside Opal, after anywhere from 6 hours to about 270 days.

## 2. Two speeds, one store

| Speed | Sources | How they arrive |
|---|---|---|
| FAST (about 5-7 s) | Mail in `49@opalinvest.com` plus the Opal staff mailboxes, Inbox and Sent Items | Graph delta query every 5 s |
| FAST (clock) | Aging of every open item, in business hours | Ticker every 5 s; computed, never fetched |
| DAILY | Schwab balance, position and transaction files, both masters (T-1) | On file landing, with a fixed daily schedule as backstop (never success-of-upstream alone) |
| SLOW | Tax SMA tracking sheet (SharePoint) | Drive delta every 60 s, if it is in round 1 |
| LATER | Teams chats | Deferred (Andrew: "teams later") |

```
 49@ + staff mail ── delta 5s ──► mail-poller ──┐
 (Inbox + Sent)     (resume on deltaLink)       │ events
 Schwab daily files ── on landing + schedule ──►├──► rule engine ──► open-items store ──► push ──► screen
 Tax SMA sheet ── drive delta 60s ──────────────┘    (6 rules)         ▲ age ticker 5s
                                                                       │ (business hours)
```

## 3. The mail poller (reuse, not new code)

- **Reuse:** `infra/aws/lambda/investor-reporting/intake/graph_client.py` and `checkpoint.py` (IRPT_BCKEND IB-s-6).
  They already handle:
  - `nextLink` versus `deltaLink` as distinct types;
  - the 410 resync back to a declared cutoff;
  - `Retry-After`;
  - immutable message ids;
  - a durable checkpoint that advances only after the event is persisted.
- **Change:** the trigger only. The IRPT version is a 15-minute Lambda. This one is ONE always-on process that loops
  every 5 s over N mailboxes x 2 folders.
  - Lambda's one-minute schedule floor rules Lambda out.
  - Load: about 12 mailboxes x 2 folders x 12 calls a minute is about 290 calls a minute tenant-wide. Per mailbox that is
    about 240 calls per 10 minutes, against Graph's 10,000 per 10 minutes.
- **Scope of what is read:** sender, recipients, conversationId, timestamps, subject, and the body preview, used only to
  classify the message.
- **Stored:** derived fields only (section 4). Never the full body, and never attachments. This matches Andrew's
  "metadata focused" stance on SOC2_MSLOGS.

## 4. The open item (the one schema)

| Field | Meaning |
|---|---|
| `item_id` | Stable hash of (`rule`, `subject_key`) |
| `rule` | One of the six rule names in section 6 |
| `subject_key` | For mail, the Graph `conversationId`. For an account, the feed `account_ref`. For a distribution, `account_ref` plus the due date |
| `state` | `OPEN` -> `WARN` -> `OVERDUE` -> `CLOSED` (or `DISMISSED`, with a reason) |
| `opened_at` | The event time that opened it |
| `sla_due_at` | `opened_at` plus the rule's SLA, in business hours |
| `owner` | The Opal person responsible (round 1: the PM or ops seat named by rule) |
| `display` | Client initials plus the last 4 of the account, and a one-line summary. NEVER a full name or full number on the screen |
| `evidence` | Graph message id(s) or feed row reference(s) |
| `claim` | `measured` / `inferred`, matching the ledger's labels |
| `closed_by` | The event that closed it (an Opal reply id, the first trade row, a sheet entry, or a human dismissal) |

Every transition is an appended event, so the store doubles as the audit trail.

## 5. The clock

- **Business hours:** trading days from `lib/trading_calendar.py` (`is_trading_day`, `trading_days_between`), plus a
  declared 08:00-18:00 America/Chicago window. 49 is in Austin.
- **Ticker:** every 5 s it moves an item `OPEN` -> `WARN` at 75% of its SLA and -> `OVERDUE` at 100%. Each move is an
  event, and the screen receives only the change.
- **Weekends, holidays and nights do not age an item.** A Friday 5pm request is not overdue on Monday at 8am.

## 6. The six rules (round order)

| # | Rule | Opens when | Closes when | SLA (proposal) | YTD it targets |
|---|---|---|---|---|---|
| 1 | INBOX RADAR | An external client-ops sender (49financial.com, Cottonwood/Alongside, Inflection, 818 FO) sent the last message in a conversation that Opal received, and a classifier says it is a request, not a thank-you or FYI | Any Opal-staff message lands in the same conversation, or an owner dismisses it | 4 business hours (WARN at 3) | 21 |
| 2 | SLEEPING MONEY ALARM | A new `account_ref` appears in the feed, OR positions or cash arrive with no trade for 3 business days | First trade, or the account appears on the Tax SMA sheet | 3 business days | 4 |
| 3 | FEE TRIPWIRE | A `TPFEE` (or other fee) posts on an account with no trade since funding, OR settled cash goes negative after a fee | Reviewed and dismissed, or a credit posts | Same day | 6 |
| 4 | PAYDAY GUARD | A recurring withdrawal (inferred from its own history) is due within 2 business days and settled cash, net of pending trades, does not cover it | Cash raised | T-2 | 4 |
| 5 | RULE CHANGE RELAY | A custodian-domain email names a minimum, cutoff, eligibility or effective date | Every account in onboarding in the last 60 days has been checked off | 1 business day | 7 |
| 6 | REPORT PROOFER | An outgoing report or update has missing or changed figures | Corrected | Before send | 6 |

**Escalation tone** is a flag on rule 1, not a seventh rule. It bumps an item straight to `OVERDUE` when the text reads
like "how did this happen" or "surprise".

## 7. Proof: replay the year before go-live

- **Replay set:** copy the 48-row ledger into the repo with labels only; the private name key never enters the repo.
- **Method:** run rules 1-4 against the YTD mail and the Schwab history.
- **Pass:** each rule fires on the strict rows it targets, on or before the date in the ledger, AND the daily count of
  open items stays small enough for a TV.
- **Printed per rule:**
  - fired;
  - fired early (days ahead of the discovery date);
  - missed;
  - false-open rate per day.

## 8. The screen (after streaming works)

- **What it is:** an Opal-internal page behind the existing staff login. It receives pushed changes from the store
  (server-sent events), so the screen does no polling.
- **Layout:** one row per open item, showing:
  - the rule name;
  - initials and the last 4 of the account;
  - age, in business hours or days;
  - owner;
  - colour by state.
- **Cast path:** to be chosen once the TV hardware is known (smart-TV browser, Chromecast, or a small dedicated PC).

## 9. Runtime and access

- **Process:** ONE always-on container beside the gateway on AWS (about $10-15 a month). It holds the poller, the rule
  engine, the ticker and the push endpoint.
- **Names and keys:** every name and S3 address comes from `lib/opal_naming.py` (`name()`, `address()`). A builder
  refusal means a missing registry row to add; it is never hand-typed.
- **No duplicate pipeline:** the daily rules READ the existing Schwab silver (`data/assets/scripts/silver/schwab_schemas.py`)
  and never copy it.
- **Graph access -- the first blocker.** `ib_s_6_graph_inspection.md` records that the estate has NO application-permission
  mail grant; the gateway reads mail through stored delegated user tokens. This needs, approved by Andrew:
  1. An app registration (new, or the existing "App-2 / m365-graph") with Graph **`Mail.Read` as an APPLICATION
     permission**, plus admin consent.
  2. A mail-enabled security group holding exactly the monitored mailboxes (49@ plus the named staff).
  3. Exchange Online: `New-ApplicationAccessPolicy -AppId <id> -PolicyScopeGroupId <group> -AccessRight RestrictAccess`,
     then `Test-ApplicationAccessPolicy` against one member and one non-member. Both results are printed and recorded,
     never assumed.
  4. A certificate credential, not a client secret, stored under a new secret name. The gateway's secrets are never
     reused, because that would widen its blast radius.
- **Account identity on screen:** the Schwab feed hashes account numbers (`acr_v1_...`). Ops needs the last 4. This is an
  open decision: either an authorized lookup from the producer, or the existing `client_resolve_account` surface once a
  firm is canonical.

## 10. Phasing

| Day | Ships | Proof |
|---|---|---|
| 0 | Graph app permission plus access policy (Andrew) | `Test-ApplicationAccessPolicy`: the member passes, the non-member is denied |
| 1 | Mail poller (delta 5 s) plus INBOX RADAR plus the open-items store | Replay of the 21 request rows; then a live test email opens an item within 10 s and an Opal reply closes it |
| 2 | SLEEPING MONEY ALARM plus FEE TRIPWIRE on the daily file | Replay fires on the Victor account by 9/25 (funded 9/22) and on its 10/13 fee |
| 3 | PAYDAY GUARD | Replay fires before the 4 recurring-cash rows |
| 4-5 | RULE CHANGE RELAY; the screen | A custodian-notice fixture opens a relay item; the page updates within 5 s of a state change |
| later | REPORT PROOFER; Teams; webhooks if 5 s is too slow | -- |

## 11. Open decisions (Andrew)

1. The monitored staff mailboxes, by name.
2. Each rule's SLA. Section 6 holds proposals.
3. The owner per rule: who is on the hook when an item turns red.
4. The account-identity path for the last 4 on screen.
5. Whether the Tax SMA sheet is in round 1.
6. The TV hardware.
