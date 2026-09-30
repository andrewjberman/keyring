```json
{
  "project": "NFRA_MCPMSP",
  "directive": "D6",
  "fabric": "site-z",
  "prd_version": "v0.1",
  "step": 4,
  "brief_ref": "docs/briefs/nfra-mcpmsp-msp-analyst-brief-20260930.md@77ddde1d13",
  "endpoint_outcomes": [
    "FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6",
    "FWD-7", "FWD-8", "FWD-9", "FWD-10", "FWD-11"
  ],
  "status": "DRAFT"
}
```

# NFRA_MCPMSP - the Opal MSP Analyst: one Opal-hosted Teams agent serving partner firms

## Authority and project arc

Author and accountable CTO: `1.0.0_SA_CTO~O`. Directive D6, Opal AI; macro NFRA; execution fabric site-z. Registered
@7c7848d589.

**Andrew's words this PRD rests on**, all recorded verbatim by `4.0.0_SA_CRO~O` in
`org/tier1_exec/4.0.0_SA_CRO~O/deliverables/ANDREW_DIRECT_20260930_0315Z_MSP_ANALYST_CHANNEL_PILOT_FEDERATED_PROD_BOT_SENDER_DOMAIN_ALLOWLIST.md`
(sections 1-10, last @6cc12c2e06):
- "I agree with 1 pilot, 3 prod." Pilot on federated chat to an Opal-owned user; production on one multi-tenant Teams
  bot (s.2).
- "If there is ever a sender to the agent that is not @opalinvest.com, @49financial.com, @inflectionwealth.com, or
  @cottonwoodmail.com, then the agent should not even respond." (s.2)
- "Refused messages absolutely should be logged." (s.5)
- The check is on the tenant ID and the domain, and it holds at the gateway too; there is ONE MCP server for all
  clients, through a central control plane (s.6-s.7).
- "yes to per-firm role": the server's own identity reads no firm data, and per request it assumes the firm role the
  tenant router selects (s.8).
- Grants: Opal-administered per advisor for the pilot; in production, an Opal-set firm ceiling within which the
  partner's admin assigns; the refusal log is the onboarding queue (s.9).
- "1.) New Project, NFRA_MCPMSP. 2.) Rec approved. 3.) Rec approved. 4.) Rec approved. Should have a clear structure in
  AWS Secrets Manager. 5.) Current buckets for now. 6.) Yes." (s.10)

**The endpoint's DONE WHEN lines are confirmed** by Andrew, verbatim "yes aggreed for all of these"
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260930_05xxZ_NFRA_MCPMSP_ENDPOINT_CONFIRMED.md`).

The brief is `docs/briefs/nfra-mcpmsp-msp-analyst-brief-20260930.md` @77ddde1d13 (`4.0.0_SA_CRO~O`). The background
is this seat's primer, `org/tier1_exec/1.0.0_SA_CTO/deliverables/PRIMER_MSP_ANALYST_FOR_CRO_O_20260930.md`
@9dc713f359. Where the primer's drawing shows one gateway per firm, record s.7 supersedes it: one server.

## Scope and evidence boundary

**This project owns** (brief II.1):
- the tenant-to-firm registry and the router that reads it;
- the sender gate (allowed domain AND registered tenant), at the agent and at the gateway, with its refusal log;
- the per-firm AWS roles, assumed per request, and the gateway identity's own zero firm read;
- per-firm Anthropic API keys and their Secrets Manager structure;
- the partner-traffic harness: the supervised pilot session, then a fresh background session per message;
- the replay record, the daily per-firm page, and the daily graded-sample feed;
- the pilot federated-chat channel and the production multi-tenant bot;
- the partner-admin ceiling as it applies to partner advisors.

**It relies on and does not change** (brief II.2):
- the Opal gateway (`infra/aws/ec2/opal-gateway/`), extended in place and never forked; its scoping modules are shared
  with the internal Analyst;
- NFRA_OPALAI's internal Analyst (the `Opal_Agent` runtime and the `/bbg-teams-assist` serve loop), whose harness
  pieces are reused, not re-owned;
- NFRA_MCPORTAL's Entitlements surface and grant handlers (Andrew-only), used for pilot grants and never rebuilt;
- NFRA_OPLGTW's grant model, whose scope this project does not re-open;
- the firm buckets `opal-data-inf` and `opal-data-cot` and their pipelines; the successor buckets arrive through their
  own LGIC migration projects (R19), never as a rider here.

**Explicitly NOT this project's:** the Teams-to-portal UI chat panel (the router, roles, grants and record are built
so one could call them later); any alert, alarm or notification (the daily page is read when opened); a partner-facing
SLA during the pilot (record s.10, card 6).

**Evidence boundary.**
- Nothing in AWS or Microsoft was read for the brief or for this PRD. The gateway's live release, tool count and roles
  are the primer's figures.
- **Whether Opal's Teams reader can see a cross-organization one-to-one chat is UNVERIFIED.** It is the first hop of
  FWD-1 and round 1's first cell.
- Whether Inflection's and Cottonwood's Teams allow chats with outside organizations is UNKNOWN; their IT contacts are
  not yet identified.
- Every outcome is DESIRED until a cell exercises it.

## ENDPOINT (step 2, /endpoint --forward)

Transcribed from `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_NFRA_MCPMSP_20260930.md` @64617f8afa;
statement, DONE WHEN and ACCEPT are verbatim, and SOURCE lines are dropped. Confirmed by Andrew, "yes aggreed for all
of these".

```
  FWD-1  An Inflection advisor asks the Opal Analyst a question in Teams and gets the answer from Inflection's own data
         DONE WHEN  EXERCISED -- one live conversation, read end to end
         ACCEPT     a named Inflection advisor asks a real question in a one-to-one Teams chat and gets an answer in
                    that chat; the answer matches what the Opal portal shows Inflection for the same thing and says how
                    current the data is; every step on the way is the real one, with no stand-in data and no faked
                    sign-in

  FWD-2  A Cottonwood advisor does the same, and neither firm can see the other's clients
         DONE WHEN  EXERCISED -- one live conversation per firm, plus one cross-firm attempt each way
         ACCEPT     a Cottonwood advisor gets an answer from Cottonwood's figures; when an advisor at either firm asks
                    about the other firm's clients they learn nothing about them, and Opal can show the refusal came
                    from the access controls rather than from the Analyst choosing not to answer; bringing Cottonwood
                    on took setting it up, not building a second system

  FWD-3  A message from anyone outside the four allowed email domains gets no reply, and Opal can see that they tried
         DONE WHEN  EXERCISED -- a real refused message found afterwards in Opal's record
         ACCEPT     a message from an address outside opalinvest.com, 49financial.com, inflectionwealth.com and
                    cottonwoodmail.com gets no answer at all; a message using an allowed domain but coming from an
                    organization Opal does not recognize is treated the same; an Opal operator can later find each
                    attempt with who sent it and when

  FWD-4  An advisor at a partner firm who has no access yet is turned away, and one Opal approval lets them in
         DONE WHEN  EXERCISED -- one advisor taken from refused to answered
         ACCEPT     an advisor at an allowed firm with no access writes in, gets no answer, and appears in Opal's list of
                    people who were turned away; after one Opal approval their next question is answered; the first
                    time anyone from a firm writes in, that same approval is how Opal comes to recognize the firm, with
                    no looking it up anywhere else

  FWD-5  Opal can replay any conversation: what was asked, what the Analyst looked at, what it was allowed or refused
         DONE WHEN  EXERCISED -- one past conversation reconstructed from the record alone
         ACCEPT     for a conversation picked after the fact, an Opal operator can show what the advisor asked, what the
                    Analyst looked up, what it was allowed and refused, and what it answered, without asking the advisor

  FWD-6  Every day, a sample of the Analyst's answers is checked against the figures Opal publishes
         DONE WHEN  EXERCISED -- one day's check read, with its results
         ACCEPT     on a normal day, a sample of that day's answers is compared with the figures the portal shows, by
                    someone other than the Analyst, and any answer that does not match is named with the reason

  FWD-7  Andrew can read one page a day per firm: what was asked, what was turned away, what it cost
         DONE WHEN  EXERCISED -- Andrew has read one day's pages
         ACCEPT     for each live firm there is a daily page Andrew can open that says what advisors asked, who was
                    turned away, and what that firm's use cost that day

  FWD-8  Opal can switch off one firm without touching the others, and each firm's spending is separate and capped
         DONE WHEN  EXERCISED -- one firm switched off and back on while the other keeps working
         ACCEPT     when an Opal operator switches one firm off, its advisors stop getting answers while the other
                    firm's advisors carry on; each firm's spending shows on its own and stops at the limit set for that
                    firm

  FWD-9  Partner advisors reach the Analyst through an Opal app their firm's IT has allowed, with no window kept open
         DONE WHEN  EXERCISED -- one partner advisor served through the app
         ACCEPT     an advisor at a partner firm talks to the Analyst through the Opal app their firm allowed; their
                    questions are answered whether or not anyone at Opal has a session running, and one question going
                    wrong does not stop the next one from being answered

  FWD-10 A partner's own administrator gives their advisors access, but never beyond the limit Opal set for the firm
         DONE WHEN  EXERCISED -- one grant made by a partner administrator, and one over-the-limit attempt refused
         ACCEPT     a partner's administrator gives an advisor access and that advisor then gets answers; when the
                    administrator tries to give more than Opal allowed that firm, it does not take effect

  FWD-11 No advisor at a new firm is served until Andrew has said the firm may go live and the checks are already running
         DONE WHEN  EXERCISED -- one firm brought live this way
         ACCEPT     an advisor at a newly added firm gets no answer until Andrew has approved that firm, and by the time
                    the first answer goes out, replay, the daily check and the daily page already cover that firm
```

## CONTRACTS

**C1 -- One gateway, extended in place.** Partner traffic runs through the existing Opal gateway
(`infra/aws/ec2/opal-gateway/`), never a second server and never a fork (record s.7). New code lands in its scoping
modules, which the internal Analyst shares. Where NFRA_OPALAI's gateway move is in flight when a cell is cut, the cell
is cut against the path where the gateway lives at issuance.

**C2 -- A tenant-to-firm registry, with an unknown tenant refused.**
- Today the gateway refuses every tenant but Opal's, and "there is no tenant-to-firm registry, so no firm is ever
  returned" (`app/asker_scope.py:62-65`, read at authorship).
- This project adds that registry. Each row maps one Microsoft tenant ID to one firm (`inflection`, `cottonwood`, as
  `infra/logic/05_IDENTITY_SPINE.md` spells them).
- A tenant with no row keeps today's refusal, `asker_tenant_denied`, now written to the refusal log (C4).
- A row is created ONLY by approving a refusal-log entry (FWD-4; record s.10, card 3), and only for a firm Andrew has
  brought live (C11). No Microsoft or vendor lookup is made.

**C3 -- The sender gate: allowed domain AND registered tenant, at the agent and at the gateway.**
- **Allowed domains, verbatim from Andrew:** `opalinvest.com`, `49financial.com`, `inflectionwealth.com`,
  `cottonwoodmail.com`.
- A message is served only when its sender's address is in an allowed domain AND its sender's tenant ID is registered
  (C2) to the firm that domain belongs to. `opalinvest.com` maps to Opal's own tenant.
- The domain is read from the sender identity the message carries, never from text in the message. A guest-form address
  (`...#EXT#@...`) is refused (ruled by this seat; brief open point, conservative).
- **The agent** sends no reply to a refused message. **The gateway** independently refuses any tool call whose cited
  asker fails the same test. Neither depends on the other.
- **Opal staff and 49 Financial in the pilot** (ruled by this seat on brief Part VII): the pilot serves Inflection and
  Cottonwood advisors only. An `opalinvest.com` or `49financial.com` sender passes the domain check but has no pilot firm
  scope, so they take the refusal-and-log path. 49 Financial becomes a firm through C11 like any other. NFRA_OPALAI's
  internal Analyst serves Opal staff.

**C4 -- Every refusal is logged, and the log is the onboarding queue.**
- Each refused message leaves one entry: when, the sender's address and domain, tenant ID, user ID and display name,
  the chat, and the reason code. **The message text is not stored** (ruled by this seat: a stranger's words are not
  Opal's to keep, and onboarding needs only the identity).
- The entries live in the gateway's existing audit record, beside the call log, not a new store.
- An Opal operator lists the entries. Approving one creates the advisor's grant (C6), and, for a firm's first writer,
  the tenant row (C2).
- **Who approves in the pilot** (ruled by this seat on brief Part VII): Andrew, from NFRA_MCPORTAL's Entitlements tab,
  which is already Andrew-only (MCPORTAL C2).

**C5 -- Per-firm AWS role, assumed per request; the gateway holds no firm read.**
- The gateway's own identity carries no read on any firm's data (record s.8).
- For each served request it assumes the role of the firm the router selected. That role reads ONLY its firm's bucket:
  `opal-data-inf` for Inflection, `opal-data-cot` for Cottonwood (record s.10, card 5, current buckets). Every other
  firm's bucket carries a bucket-scoped Deny.
- A scoping bug therefore surfaces as an AWS refusal, not as a leak (brief Part III).
- Role names come from `lib/opal_naming.py name()` after a registry row lands in `infra/logic/registry/` (CLAUDE.md
  Rule 30). Each role and trust change is an IAM act under the change ledger (C12).

**C6 -- Grants in the existing store; the pilot is Opal-administered, production adds a firm ceiling.**
- A partner advisor's grant keys on the existing `POLICY#<tid>#<oid>` shape (`app/access_state.py`), which a partner
  tenant ID and user ID fit unchanged (brief IV.1).
- Pilot grants are written through NFRA_MCPORTAL's grant writer, never a second writer.
- Production adds a per-firm ceiling that Opal sets, within which a partner administrator assigns access. A grant past
  the ceiling does not take effect (FWD-10, record s.9). This is enrichment, not round 1.

**C7 -- Per-firm API keys with spend caps, in Secrets Manager under the builder's structure.**
- Each firm has its own Anthropic API key with its own spend cap (record s.10, card 4).
- Keys are stored in AWS Secrets Manager under names that are `lib/opal_naming.py` SECRET-grammar output (brief IV.5),
  never hand-typed. That is Andrew's "clear structure".
- A firm's worker reads only its own firm's key. Disabling one key or one role stops that firm alone (FWD-8).
- **Creating the keys and setting their caps is Andrew's act** (spend and a vendor account, gate G-KEY).

**C8 -- The harness: a supervised session for the pilot, a background session per message for production.**
- **Pilot** (record s.10, card 2): one interactive Claude Code session, watched, running under a dedicated non-admin
  Windows account on the site-Z box.
  - The account is provisioned with the same scripts as NFRA_OPALAI's `Opal_Agent` (`provision-account.ps1`,
    `verify-boundary.ps1`), but it is a separate account with a separate credential. Partner traffic never runs as the
    internal Analyst's identity.
  - Its one MCP server is the gateway (C1).
- **Production** (FWD-9): a fresh background Claude Code session per inbound message, using the same harness files, so
  no window has to stay open. This is enrichment, not round 1.

**C9 -- The record: every run replayable from Opal's side, tagged by firm and advisor.**
- Every run's transcript, tool calls and the gateway's audit rows for that run are stored on Opal's side, tagged with
  firm, advisor and run.
- That is enough for FWD-5 without asking anyone. The store's address is `lib/opal_naming.py address()` output.
- The agent account cannot write the repo (as with `Opal_Agent`), so the record is shipped by the operator side, not
  committed by the agent.

**C10 -- The daily page and the daily sample are read when opened, never sent.**
- The per-firm daily page (FWD-7) and the graded-sample feed (FWD-6) are produced on a schedule and read when opened.
- Nothing is emailed or alerted (CLAUDE.md alert moratorium; Andrew asked for a page to read, record s.10, card 2).
- The sample is graded by someone other than the Analyst: `3.0.0_SA_CVO~O` (record s.10, card 6).

**C11 -- A firm goes live only on Andrew's word, and only once the checks cover it.**
- Onboarding a firm is Andrew's word (record s.10, card 6; `infra/logic/05_IDENTITY_SPINE.md`: "a new firm is his word").
- Before a firm's first advisor is served, C9, C10 and the per-firm key and cap (C7) must already cover that firm
  (FWD-11).

**C12 -- The change ledger binds IAM, keys and gateway releases.** Any act on a firm role, the gateway role's trust, a
Secrets Manager entry, or a gateway release opens a ledger entry in `org/critical_paths/change_management/` and names
its blast radius (CLAUDE.md hard stops).

## SURFACE MANIFEST

| id | surface | what it is | depends on | outcomes |
|---|---|---|---|---|
| S1 | federated-chat probe | proves Opal's Teams reader sees a cross-organization one-to-one chat | G-USER, one outside test account | FWD-1 |
| S2 | tenant registry + router | tenant ID to firm; unknown tenant refused and logged | C2 | FWD-1, FWD-2, FWD-4 |
| S3 | sender gate | allowed domain AND registered tenant, at agent and gateway | S2 | FWD-3 |
| S4 | refusal log | entries in the gateway audit record; listing; approval | S3, MCPORTAL Entitlements | FWD-3, FWD-4 |
| S5 | per-firm roles | assume-per-request; firm-bucket read only; gateway zero read | registry rows, G-LEDGER | FWD-1, FWD-2 |
| S6 | pilot grants | advisor grants through the MCPORTAL writer | S4 | FWD-1, FWD-4 |
| S7 | per-firm keys | Secrets Manager structure, per-firm key and cap | G-KEY | FWD-8, FWD-11 |
| S8 | pilot harness | the dedicated runtime account and supervised session | provision scripts | FWD-1 |
| S9 | run record | transcript + tool calls + audit, tagged, stored on Opal's side | S8 | FWD-5 |
| S10 | daily page | per-firm asked / refused / cost | S9, S7 | FWD-7 |
| S11 | daily sample | the graded-sample feed to the CVO | S9 | FWD-6 |
| S12 | firm stop | switch one firm off and on | S5, S7 | FWD-8 |
| S13 | production bot | multi-tenant Teams app, background session per message | G-APP | FWD-9 |
| S14 | partner ceiling | firm ceiling, partner-admin assignment | S6 | FWD-10 |

**Gates, each an act a named holder can take on demand:**
- **G-USER:** an Opal-owned "Opal Analyst" Microsoft 365 user for the pilot chat. Holder: Andrew with Opal IT (the same
  kind of act as NFRA_OPLGTW's G-C, now with Opal IT).
- **G-IT-INF, G-IT-COT:** each partner's Teams allows chats with outside organizations. Holder: each partner's IT,
  reached through Andrew ("easy enough to figure out").
- **G-ADVISOR:** a named advisor at each firm for the live conversations. Holder: Andrew.
- **G-FIRM:** Andrew's word to bring each firm live (C11). Holder: Andrew.
- **G-KEY:** the per-firm Anthropic API keys and their caps (C7). Holder: Andrew.
- **G-APP:** the Opal multi-tenant Entra app and Teams package, and each partner admin allowing it (production). Holder:
  Andrew with each partner's IT.
- **G-LEDGER:** a change-ledger entry before any IAM, key or release act. Holder: the acting seat.
- **G-PUSH:** every shared-branch push. Holder: `0.0.0_AB_MSTR~Z`, on Andrew's word.

## Ground truth measured at authorship (2026-09-30, repo only)

- `app/asker_scope.py:62-65`: any non-Opal tenant is refused `asker_tenant_denied` before a catalog lookup; there is no
  tenant-to-firm registry.
- `app/asker_scope.py:70-73`: a chat that is not one-to-one is scoped to the intersection over every human member. A
  chat mixing an Opal person and a partner advisor is served at the narrower grant, which is why FWD-1 names a
  one-to-one chat.
- `app/asker_scope.py:151-167`: the asker is read from the cited message's own sender (tenant ID and user ID), never
  from an argument.
- `infra/logic/05_IDENTITY_SPINE.md:67-68`: `inflection` maps to `opal-data-inf` and `cottonwood` to `opal-data-cot`,
  both LIVE; no `opal-data-inflection` or `opal-data-cottonwood` exists.
- `infra/logic/01_CENSUS.md:85`: served platinum exists per firm at `platinum/mdpf/{49financial,cottonwood,inflection}/`.
- No NFRA_MCPMSP code, role, key, registry row or record store exists.

## BRIEF COVERAGE

Denominator: **29 headings** (lines beginning `#` in the brief @77ddde1d13).

| headings | n | disposition | where |
|---|---|---|---|
| title | 1 | CARRIED | Authority |
| PART I | 1 | CARRIED | ENDPOINT |
| O1-O11 | 11 | CARRIED | FWD-1..FWD-11 |
| PART II; II.1; II.2; II.3 | 4 | CARRIED | Scope and evidence boundary; II.3 ruled D6 at L3 (@7c7848d589) |
| PART III | 1 | CARRIED | the ACCEPT lines; C5 (AWS refusal, not a leak) |
| PART IV; IV.1-IV.6 | 7 | CARRIED | Ground truth; C2 (IV.2), C6 (IV.1), C5 (IV.4), C7 (IV.5), C8 and C9 (IV.6); IV.3 -> FWD-1 one-to-one |
| PART V | 1 | CARRIED | Gates G-USER, G-IT-*, G-KEY, G-APP, G-FIRM; S1 carries the federated-chat question |
| PART VI | 1 | CARRIED | Ground truth |
| PART VII | 1 | CARRIED-AS-RULED | Opal staff and 49F -> C3 (pilot scope); approver -> C4; refusal log -> C4; FWD-1 data -> Acceptance A1; the audit gap -> Canonical handoff |
| REFS | 1 | CARRIED | inputs to C1-C9 |

Sum: 1+1+11+4+1+7+1+1+1+1 = **29**.

## Acceptance matrix

| id | acceptance | outcome |
|---|---|---|
| A0 | one cross-organization one-to-one chat to the Opal Analyst user is visible to the gateway's Teams reader, sender tenant ID and user ID read from the message | FWD-1 (hop 0) |
| A1 | one named Inflection advisor's question answered in the chat from Inflection's model-portfolio figures that the portal already serves (`platinum/mdpf/inflection/`), matching the portal for the same item and stating the data's date; every hop real | FWD-1 |
| A1n | NEGATIVE ARMS: the Inflection role reading `opal-data-cot` refused by AWS; the gateway identity reading either firm bucket refused; an unregistered tenant refused and logged | FWD-1, FWD-2 |
| A2 | one Cottonwood conversation answered; one cross-firm question each way yields nothing about the other firm, with the refusal traced to the access controls | FWD-2 |
| A3 | one message from a non-allowed domain, one from an allowed domain in an unregistered tenant, one guest-form address: no reply to any, three log entries with sender and time | FWD-3 |
| A4 | one ungranted advisor refused and listed; one approval; their next question answered; the firm's tenant row created by that approval | FWD-4 |
| A5 | one past conversation reconstructed from the record alone | FWD-5 |
| A6 | one day's sample graded by `3.0.0_SA_CVO~O`, mismatches named | FWD-6 |
| A7 | one day's page per live firm, opened and read by Andrew | FWD-7 |
| A8 | one firm switched off and back on while the other's advisor is answered throughout; per-firm spend shown and capped | FWD-8 |
| A9 | one partner advisor answered through the Opal app with no Opal session open; a failed question followed by an answered one | FWD-9 |
| A10 | one grant by a partner administrator honoured; one past the firm ceiling not taking effect | FWD-10 |
| A11 | a new firm's advisor refused until Andrew's word, and C9, C10 and C7 in place before the first answer | FWD-11 |

## Canonical handoff

L5 belongs to a `2.0.0_SA_COO` lane for this project. It is UNSEATED at authorship and is asked of `0.0.0_AB_MSTR~Z`
at delivery.

**FWD-1 is the thread, and round 1 builds it over its hops:**
0. the federated-chat probe (S1, A0). If the reader cannot see a cross-organization chat, the pilot channel fails
   here, and the finding returns to this seat before any other cell builds on it;
1. the tenant registry and router for Inflection (S2), with the refusal log's minimum (S4) so an unknown tenant is
   logged from the first day;
2. the Inflection firm role and the gateway identity's zero read (S5, A1n);
3. the named advisor's pilot grant through the MCPORTAL writer (S6);
4. the supervised pilot session under its own runtime account (S8), with the run record's minimum (S9);
5. one live question from the named advisor, graded against A1.

**Round 1's live conversation waits on external acts:** G-USER, G-IT-INF, G-ADVISOR and G-FIRM for Inflection. Cells 0-4
are buildable and testable before them, cell 0 with an outside test account under Andrew's word. The audit coverage of
the new tool (row NFRA_OPALAI-Z-W2-S2, `app/audit.py` `_ARGS_ALLOWLIST`) is decomposed at L5.

**Enrichment rounds,** in the brief's order: Cottonwood and isolation (FWD-2), the sender gate in full (FWD-3), the
onboarding queue (FWD-4), replay (FWD-5), the daily sample and page (FWD-6, FWD-7), firm stop and spend (FWD-8), then
production: the bot (FWD-9), the partner ceiling (FWD-10) and the go-live bar as a standing check (FWD-11).

**Sequencing against siblings:** gateway cells are never issued into the same round as NFRA_OPALAI or NFRA_MCPORTAL
gateway cells with overlapping paths.
