# BRIEF v3 (consolidated): NFRA_TRNSPT -- Investment Commentary pipeline, tied to the IRPT Analysis tab and the Ticket Center

- Author: `4.0.0_SA_CRO` (base), 2026-09-30. Consumer: `1.0.0_SA_CTO` (L4 PRD, L3 registration). Extends `docs/briefs/nfra-trnspt-opal-transcript-database-brief-20260929.md`.
- READ THIS ONE. It consolidates v1 (`...expansion-brief-20260930.md`) and v2 (`...expansion-brief-v2-20260930.md`) and the three Andrew-direct records below. Where they differ, this brief wins; section 11 lists what it supersedes.
- Andrew's words, verbatim, in: `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260930_023xZ_TRNSPT_EXTERNAL_SEND_IS_APPROVED_DREDGE_BACK_AS_FAR_AS_POSSIBLE.md`; `..._03xxZ_TRNSPT_OPEN_CALLS_ANSWERED_TICKET_CENTER_OWN_INGESTION.md` @b6bceab3ce; `..._03xxZ_TRNSPT_REQUESTER_MAY_CLAIM_OWN_TICKET_D7_MOVES_TO_LAPTOP_ATTACHMENTS.md` @1dcc313303; and `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260930_020xZ_TRNSPT_COMMENTARY_TIERS_KIMI_TEST_MAILBOX_HANDOFF_TO_CRO.md`.
- Claim classes: READ (file:line seen by this seat or its subagent, not re-opened line by line), MEASURED, PROPOSED, OPEN, ABSENT (scope stated). Every path is a SHAPE; real paths are `address()` output after the registry rows exist (CLAUDE.md rule 30).

## ADDENDUM 2026-09-30 (Andrew's answers to section 10; record `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260930_03xxZ_TRNSPT_YANG_IN_CROSS_FIRM_TICKET_TEXT_AND_ATTACHMENT_SOD_RULE_ALL_TICKETS.md`) -- the addendum wins over the sections below

1. **Section 2 (a) becomes an AUTHOR table.** Sender is Manav or Yang (any address of theirs); (b) client-domain recipient and (c) YCharts PDF are unchanged. Yang's addresses are a data asset to supply. The near-miss review in section 2 now lists Yang-to-client-with-PDF as an INCLUDED case and, as near-misses, any other Opal-internal sender with a PDF to a client.
2. **Section 7: slice ACROSS firms.** `recipient_firm` stays a column and is not a filter. Consequence to build in, not a call: because examples now cross firms, add the client firms' names (49 Financial, Inflection, Cottonwood and any later firm) and advisor names to the wipe's dictionary and allowlist-exclusion, so a firm's identity cannot ride inside a cross-firm example. The section 5 stated limit stands.
3. **Section 8: the ticket carries the draft text AND the report as an ATTACHMENT** (not a link). That pulls D7's attachment chain (WS-1 storage read and ticket bucket, then WS-2 attachments; `docs/architecture/D7_TICKET_VNEXT_PRD.md:76-96, 168`) onto round 1's critical path; section 8 step 3 and section 9's "later: the PDF on the ticket" are replaced by this. Attachment is the long pole. INTERIM (PROPOSED, the CTO's to rule): the ticket ships with text and a report link until WS-2 lands, then gains the attachment; the first real Generate waits for neither. The draft text also rides the ticket-create notification email (Andrew: "the text is just included"); section 10 call 3 is closed by that.
4. **Section 8 step 4 and section 10 call 4: the requester-claim ruling applies to ALL tickets.** The ticket API's segregation-of-duties block (`_sod_block`, `lambda_function.py:904`) is removed or neutered across the Ticket Center: a D7 build. One check for D7, not a question to Andrew: the same table carries `trade_request` tickets; Andrew called requester-cannot-approve a Trade Submission concept, and the trade controls live in `trade-workflow-handler` (READ in the 2026-08-12 finding: it enforces per-action segregation), so D7 confirms nothing in the Ticket Center was the only control on a trade.
6. **ROUTE (Andrew, record `..._04xxZ_TRNSPT_GRAPH_PERMISSIONS_...`, messages 4-6): the daily pull runs through the EXISTING Opal gateway under Andrew's account; no new app registration, no IT.** This replaces the "dedicated app registration" idea and rewrites section 3's OPEN dependency. What the gateway already holds (READ, `infra/aws/ec2/opal-gateway/app/config.py:51`): delegated `Mail.Read`, `Mail.ReadWrite` (and Files/Sites scopes); IT's consent record is `IT_REQUEST.md:21-51`. So the missing pieces are gateway TOOLS, under the existing Mail.Read: (i) an attachment-download tool (Graph `.../attachments/{id}/$value`), (ii) a filtered, paged list (by sender, received date, has-attachment, following `@odata.nextLink`; the current list is capped at 1000 with no paging and search at 275 hits, fuzzy), (iii) `ccRecipients` returned with each message (today only To is). Bcc stays invisible: Microsoft shows it only on the sender's own copy. These are a code change in the gateway project (NFRA_OPLGTW), a task order via the CTO, not a permission request. Unattended running uses the gateway's existing headless pattern (a stored token for one fixed identity, READ in the L1 brief finding 9); that token's lifetime is UNMEASURED, and if it lapses Andrew signs in again (accepted for now: "wing it through my account"). A dedicated mailbox-scoped registration is a LATER hardening, not a blocker.
7. **Criterion (b) is a recorded attribute, not a gate (Andrew, `..._04xxZ_...` addendum).** Ingest = sender Manav or Yang + a YCharts report attached + investment feedback; the recipient domain is stored on the row. The PDF name-and-size discriminator and the automated-mail exclusion from the first-pass findings carry the precision. Section 2 and section 5 read accordingly.
8. **FIRST REAL-MAILBOX MEASUREMENTS (2026-09-30, Andrew's mailbox, read-only through the existing gateway tools; subagent report; local files under the desktop folder NFRA_TRNSPT_SAMPLE_LOCAL, not in the repo). They correct sections 2, 3, 6 and 9.**
   - **The mailbox starts in October 2025.** The earliest message from Manav or Yang anywhere in it is 2025-10-21; a 2020 to 2025-10-26 slice returned 9 Manav and 1 Yang messages, none with attachments. "Back as far as it goes" is about eleven months.
   - **Date-sliced search works** through today's gateway tools: `from:manav hasattachments:true received>=2026-03-01 AND received<2026-04-01` (`from:manav` matches both addresses; `from:yang` likewise; `top=300`; a double quote returns a 400; `NOT` returned nothing and is not trusted). No monthly slice reached the 275 cap (largest: Yang, June 2026, 225 hits, nearly all vendor short-sale-availability forwards). This is the dredge method under the current tools.
   - **Enumerated: 124 candidates** (89 Manav, 35 Yang after dropping the automated Yang vendor forwards, about 220 in June alone). Manav per month: Nov-Dec 2025 15; Jan 6; Feb 4; Mar 11; Apr 12; May 3; Jun 3; Jul 14; Aug 12; Sep 9.
   - **Sender x client-domain To x non-inline PDF of 300 KB or more:**

     | Sender | To at client domain | PDF >= 300 KB | Count |
     |---|---|---|---|
     | Manav | yes | yes | 16 |
     | Manav | yes | no | 57 |
     | Manav | no | yes | 3 |
     | Manav | no | no | 13 |
     | Yang | yes | yes | 2 |
     | Yang | yes | no | 9 |
     | Yang | no | yes | 2 |
     | Yang | no | no | 22 |

   - **Under the old rule (client domain as a gate) 18 messages qualify; with the domain as an attribute (Andrew) the large-PDF set is 23** (Manav 19, Yang 4). None of the 18 went to `cottonwoodmail.com`.
   - **THE PRECISION CLAIM DOES NOT HOLD ON THE NAME-AND-SIZE RULE ALONE.** Of the 18: 6 have body or subject evidence of a YCharts report ("YC report", "YChart"); about 7 more look like YCharts reports by name and size (500 to 830 KB, named by surname or "surname vs LTC" or a strategy title) but are unproven; about 5 do not look like YCharts (two private-equity fund documents, two generic "Opal Portfolios" PDFs, one 1 MB production summary). So a size rule alone lets non-YCharts PDFs in. Under the current tools no attachment bytes are returned, so "this PDF is a YCharts report" cannot be tested by content (no producer field, no page-1 text). The test stays a heuristic (name pattern + size band + body words) until an attachment-download tool exists, which is a HELD item (record `..._04xxZ_...` addendum 3). The number to carry is 6 confirmed and about 13 probable, of 18.
   - **THE DATASET IS SMALL.** Roughly 6 to 18 real commentary emails, not hundreds, in eleven months of this mailbox; Yang contributes 2 of 18. Alyssa's labelled cache is 70 write-ups (March to September 2026, per the hand-off); this mailbox sees only threads Andrew received. With a variant-matched slice (section 7), a request for a multi-model report may find zero or one precedent. This bears on the earlier "own ingestion, not her cache" ruling: the concern then was precision, the finding now is volume. It is reported to Andrew as a fact to weigh, not decided here.
   - **Automated "49 Trade Update" mail is deterministic to exclude.** 15 messages: subject of the form "49 Trade Update (date)", a single To that is a firm-wide distribution address at `49financial.com`, a body opening "49, The Investment team has made adjustments within our model portfolios", one signature PNG plus an update PDF of 228 to 242 KB (73 KB and 54 KB on two later dates). All 15 meet the raw sender and recipient tests and none reaches 300 KB, so the size floor happens to exclude them, but the rule should exclude them explicitly: subject prefix plus a single distribution-address recipient plus no reply prefix. Of the 15, 13 are pure automated sends and 2 are hand-written "Re:" replies, so the "no reply prefix" clause matters.
   - **The distro channel is not complete** (Andrew's point holds): `49@opalinvest.com` is on 11 of the 18 matches and missing on all 4 sent to `inflectionwealth.com` and on 3 others.
   - **Cc and Bcc are not returned** by `read_email`; only To.
   - **What the sample cannot support.** The saved `idx_*.json` files are hand-converted plain text, except `idx_25` and `idx_36`, which are raw tool output; nearly all `body_html_length` values are estimates. So the HTML parsing and cut rules seen so far (signature at `<div id="Signature">`; quoted chain at `<div id="appendonsend">`, then `<hr>`, then `<div id="divRplyFwdMsg">`; compliance boilerplate opening "Certain appropriately licensed individuals are registered to offer advisory services"; inline `cid:` images) are READ from three replies and one market update, not from a byte-exact sample. Writing the final cut rules needs raw HTML, which needs a read that persists it: a NEW gateway call, HELD until Andrew has seen site Z's work.
   - **Not searched:** other people in the Manav and Yang orbit (assistants); `hasattachments:true` is a superset (it counts inline images), and a match with no attachment flag would be missed.
5. **Section 10 is now empty of calls to Andrew,** apart from what the earlier sections name as owned dependencies (gateway sign-in lifetime and attachment tool, the IRPT trigger, the ticket-tenant security state).

## 1. The premise, as a flow

```
IRPT Analysis tab: a user (initially Alyssa, beta, on behalf of advisors; later the advisors) hits Generate
  -> irpt-ycharts-generate accepts, enqueues -> resident worker -> YCharts -> report READY   (exists)
  -> [NEW HOOK] -> commentary Lambda
       1. read the request's frozen composition (variant, comparison_keys, holdings, settings) + requester identity
       2. PYTHON slices gold commentary -> ~10 candidate emails                 (no AI)
       3. ONE Kimi call: candidate cards + bodies + prompt -> picks the best few, drafts
       4. create a Ticket Center ticket: type Analysis Request, draft text in the ticket,
          requester name and firm, report reference, (later) the report PDF attached
  -> an Opal-internal person claims the ticket, edits the draft, sends it
Daily, separately: the ingestion job pulls new commentary emails from Andrew's mailbox into bronze.
```
Kimi is used once, at step 3. Everything before it is deterministic Python.

## 2. The ingestion criterion (Andrew, verbatim in the records)

An email is INGESTED when ALL hold: (a) the sender is Manav, from either his `@49financial.com` or his `@opalinvest.com` address; (b) at least one recipient is at a client domain (today `@49financial.com`, `@inflectionwealth.com`, `@cottonwoodmail.com`; Andrew said "including", so the list is open-ended); (c) it carries investment feedback with a YCharts report attached. Andrew's claim: under this criterion, precision is 100%. This replaces `classify.py`, `finder_status` and the earlier "external recipient" rule.

**PROPOSED implementation.**
- (a) a sender table of Manav's addresses; (b) a versioned client-domain table (an editable data asset, not code); (c) "a YCharts report" = an attachment that is a PDF and identifies as a YCharts report. The detection mechanism (PDF producer or metadata field, filename convention, first-page text, or the `custom_pdf_reports` template signature) is OPEN and needs one look at a real attachment; it must be an explicit rule, not a keyword guess.
- The criterion is applied at bronze-to-silver from the RAW headers and attachments. Bronze lands the CANDIDATE set the daily pull sees (everything Manav sent to any client-domain recipient), and silver keeps only rows that pass (c). Nothing is dropped at fetch.
- Store the three booleans (`sender_ok`, `client_recipient`, `ycharts_pdf`) and `recipient_firm` in silver so the inclusion decision is auditable and re-runnable when the client-domain list grows.

**Consequences of the criterion, stated once (Andrew's call to accept):**
- **Yang is out.** In the 12-thread sample, one multi-model commentary was written by Yang. Under (a) it is excluded.
- **Commentary with no YCharts PDF is out.** In the sample, 2 of 4 commentary replies had no PDF.
- **Coverage is Andrew's mailbox.** A Manav-to-client email where Andrew is not a recipient, on copy, or on a thread he holds is not seen. "100% precision" is a claim about the rule; recall is bounded by what the mailbox holds.
- **How precision is checked (PROPOSED):** the first run produces a reviewed sample: a list of ingested items and the near-misses (Manav to a client with no PDF; Yang to a client with a PDF; Manav to Opal staff with a PDF), for Andrew to read himself. No labels file is needed.

## 3. Daily pull through the Opal gateway (Andrew: hits his mailbox daily)

- **Test/dredge:** everything the mailbox holds, back as far as it goes (Andrew), then a daily delta.
- **Gateway tools (MEASURED by a subagent):** `list_recent_email(since_iso, top, unread_only)` is the only date filter (a lower bound; no folder parameter); `search_email(query, top)` is fuzzy with no folder or date filter. So the daily job is: `since_iso` = last watermark, filter client-side by the criterion, pull the full message and attachments by id, plus every other message in each touched `conversationId` (kept in bronze for context).
- **OPEN dependency (not this project's build):** the gateway (NFRA_OPLGTW) holds delegated tokens; a scheduled headless run uses a stored token that raises `NeedsLogin` when the refresh fails (READ `infra/aws/ec2/opal-gateway/app/token_broker.py:171-183`), and the lifetime is not measured. Andrew ruled the route (gateway, his mailbox); what remains is a MEASUREMENT of how long the stored sign-in lasts, and the gateway tool for attachment bytes (whether an attachment-download tool exists is not established; `list_email_attachments` and `read_email` take a message id). Both are named in the PRD as owned dependencies.
- **Schedule:** its own clock (EventBridge cron), not "on success of upstream" (CLAUDE.md). No failure alarm, SNS or SES send; the run writes a run record.

## 4. Bronze (PROPOSED)

`s3://opal-data-transcripts/outlook/transcripts/bronze/analysis_commentary/date=<sent date UTC>/`: `msg_<sha256(internetMessageId)[:16]>.json` (Graph message byte for byte), `attachments/<sha256>.<ext>` (raw), and a sidecar (`pulled_at`, run id, Graph id, `internetMessageId`, mailbox tag). Partition by SENT date so a re-pull overwrites the same key. Whether the grammar allows subfolders under `date=` is UNPROVEN until `address()` runs; if not, the hash goes in the filename. Needs registry rows `outlook` (and `sharepoint` for FWD-6) in `infra/logic/registry/systems.json` (READ procedure, `lib/opal_naming.py:1701-1704`; ABSENT today). PII lives here: two named readers (Andrew, `opalbloomberg@opalinvest.com`); bronze never gains a third.

## 5. Silver and the wipe (Andrew: name-token dictionary + hash number strings > 4 characters)

Silver: `.../silver/analysis_commentary/date=.../` parquet, one row per unique `internetMessageId`, produced by an event-triggered Python Lambda from bronze. The wipe runs inside this step, so unwiped text never reaches silver. No AI.

**Mechanism (PROPOSED, Andrew's design with four guards):**
1. Parse HTML into a block list with the stdlib parser; keep headings, paragraphs and list items (the slicer uses them); drop the signature, the compliance disclaimer, the quoted reply chain, images and links.
2. **Names:** replace any token found in a names dictionary with `[NAME]`. The dictionary is a vendored, hash-pinned DATA FILE in the repo built from public name lists (for example the US SSA given-name and Census surname lists), not a runtime `pip install` or a runtime download. Guard 1: match case-sensitively on capitalised tokens, so the word "will" or "grant" is not a name. Guard 2: an ALLOWLIST is applied first (Opal model names and their aliases, product names, tickers, finance terms, theme labels), so "Long Term", "Dividend", "Mark-to-market", "Hunt" in a ticker, or a model called "Grant" are not wiped. The allowlist is a versioned asset; its size is a real maintenance cost and I state it.
3. **Numbers:** replace an identifier-like string, meaning a token longer than 4 characters that contains a digit and is not a percentage, a decimal, a comma-grouped or dollar-prefixed amount, a 4-digit year, or a date (Andrew's examples `08242253`, `z09302843`), with a token. Guard 3: use a KEYED HMAC (a secret the wipe holds), not a plain hash: an 8-digit account number has 10^8 possibilities and an unkeyed hash of it can be reversed by enumeration in seconds. Or replace with `[ID]`; the keyed form is only worth having if the same id must map to the same token (nothing in the design needs it). RECOMMENDATION: `[ID]`, no hash.
4. Emails, phone numbers: regex, replaced by `[EMAIL]`, `[PHONE]`.
5. **Theme labels are wiped too.** The sample shows client-specific position names used as headings.
6. Anything left that looks like a capitalised name not in the dictionary or allowlist goes to `pii_residual_flags`; flagged rows are held out of the serving slice until reviewed.
7. Headers: silver keeps `sender_role`, `recipient_firm` (from the client-domain table), `sent_at`; no addresses, no display names. Attachment names are stored as `attachment_sha256[]` and a class; original names stay in bronze.

**Stated limit:** the wipe removes dictionary names, identifier-like numbers and patterns. It does not remove a client name that is not in the dictionary and not flagged. A leak test with planted tokens is the gate (names in a heading, in a salutation, split across an HTML tag, in a different case, in a common-word name, plus 8-digit and alphanumeric ids); its result is "the planted classes were removed", not "no PII remains".

## 6. Gold: our format (Alyssa's PRD-001 is inspiration only, Andrew)

Parquet, `.../gold/analysis_commentary/date=.../`, one row per silver row, derived by one Python Lambda (`pyarrow`; layer `pandas-pyarrow-layer:1` exists, READ `lambda-layer-map.json:85`). No AI. Fields are chosen for the slicer and the Kimi call, not to match PRD-001:

| Field | Derivation | Why |
|---|---|---|
| `record_id` | `sha256(internetMessageId)` | idempotent, mailbox-independent |
| `sent_at` | header, UTC | recency |
| `recipient_firm` | client-domain table (`49f`, `inflection`, `cottonwood`, ...) | same-firm precedent; see section 7 |
| `yc_variant` | 1 / 2 / 3 from the count of models referenced (0 / 1 / 2+) | the same axis as IRPT's Overview / Comparison / Multi |
| `models_referenced` | ALIAS TABLE match on body | prose uses LTC / 49 Long Term, ULT / Ultra Long Term / LTA, UST, PFOE, DIVZ, Dividend Income Strategy, Short / Intermediate / Long Term; table must map to IRPT `comparison_keys` (OPEN: their names) |
| `account_type` | keyword rules (IRA, Roth, 401(k), brokerage, trust, else household) | slicer tie-break |
| `themes` | `list<struct{theme, client_figure, model_figure}>` from block headings and the first "X% versus Y%" in a paragraph | what the commentary argues |
| `body_text` | cleaned blocks | the example the model reads |
| `paragraph_hashes[]`, `body_hash` | SHA-256 | de-duplicate reused boilerplate |
| `pdf_sha256`, `has_pdf` | silver | always true under the criterion |
| `holdings` | PDF table parse, nullable | new work; `pypdf` is packaged in two layers, `pdfplumber` is NOT in the python3.12 Lambda runtime (READ `ycharts/extract/extract.py:129-135`); untested |
| `request_text` | the advisor's request in the same conversation, wiped, nullable | pairs request and response for the model (PROPOSED; OPEN whether wanted) |

Dropped from v2: `approved`, `finder_status`, `sent_external` (replaced by the section 2 booleans in silver), `model_as_of` and the model-weights join (no source found; PRD-001 Q3 is unanswered; add only if the slicer needs it).

**A concrete example row (synthetic):**
```
record_id         9f2c...e1        sent_at        2026-09-02T14:31:07Z     recipient_firm   "49f"
yc_variant        3                models_referenced ["Short Term","Intermediate","Long Term"]
account_type      "brokerage"      holdings       null
themes            [{theme:"Risk Positioning", client_figure:"6.1 duration", model_figure:"4.4"}, ...]
body_text         "[NAME], ... fixed income duration of 6.1 versus 4.4 ..."     paragraph_hashes [...]
```

## 7. The slicer, and a firm-separation question that is new

- **Inputs from the Generate request (READ, subagent):** `variant` (0 = Overview, 1 = Comparison, 2-5 = Multi), `comparison_keys`, `client_id`, holdings and `holdings_fingerprint`, `settings`.
- **Slice (PROPOSED, all Python):** `yc_variant` equal to the request's variant, ranked by overlap of `models_referenced` with the request's models, then `account_type`, then recency; near-duplicates removed by `paragraph_hashes`; about 10 candidates. With no candidate at the variant, fall back to the nearest variant and say so in the draft's provenance. At hundreds of rows the Lambda reads the gold partitions with pyarrow directly; no Athena needed.
- **NEW CALL (Andrew): same-firm or cross-firm precedent.** The three client domains are three different firms. A draft for one firm's advisor built on another firm's earlier client commentary carries that firm's content across the firm line, even wiped. PROPOSED: slice WITHIN `recipient_firm` first; cross to another firm only if none exists and only with Andrew's word, recorded in the draft's provenance. CLAUDE.md's cross-firm rule binds pipeline trees, not this serving path, so the rule does not decide it: it is a business call.

## 8. The trigger, the Kimi call, and the Ticket Center

**Trigger (READ, subagent).** No hook exists after a report is READY: the request and job DynamoDB tables (`irpt-requests`, `irpt-jobs`, `irpt-outbox`) declare no streams; there is no S3 notification, Step Functions or EventBridge on the generate path; READY is a transactional put of `REPORT#<report_id>#<revision>` into `irpt-requests` (`report_index.py:46-50`); queue messages carry ids only, 4096 bytes max (`core/sqs.tf:27`). PROPOSED: a DynamoDB stream on `irpt-requests` filtered to `REPORT#` items feeding the commentary Lambda. That is a change in the IRPT tree: a task order to IRPT_BCKEND, not a TRNSPT build. A trigger is a route; the moratorium does not apply. The commentary must never block or fail the report; a failure goes to a dead-letter queue and a retry.

**Kimi (READ).** Already in the estate: `infra/aws/lambda/investor-reporting/intake/resolution_kimi.py:20` (`kimi-k3`); secret `astn/kimi/api-key`; endpoint `https://api.moonshot.ai/v1/chat/completions` (`infra/aws/ec2/bd-cot-auto-login/bd_49f_auto_login.js:64`). Andrew's word: yes to the first call, input limited to abstract fields (variant, model names, account type, themes, holdings as category weights; no client identity, no account ids), only after the wipe test passes. Kimi output is a DRAFT, visible in Opal-internal views only.

**Ticket Center (READ from the working tree by a subagent; deployed bytes not checked).**
- Portal `/ticket-center`, `ProtectedRoute requireInternal` (`portal/src/App.tsx:474-481`); Lambda `opal-ticket-api` (`infra/aws/lambda/ticket_center/lambda_function.py`, 1,112 lines); DynamoDB `opal-tickets`, hash `ticket_id`, GSI `status-index`; routes `POST/GET /api/scoped/tickets`, `.../{id}`, `/claim`, `/complete`, `/submit`, `/metrics`.
- Types today: `trade_request`, `service_request`, `meeting_request`, `other` (`:62`). No "Analysis Request". States: `open`, `in_progress`, `completed`. Fields: `title` (300), `description` (8000), `requester{email,name,firm}`, `linked_submission_id`, `client_updates[]` (2000 each, 50 max), `events[]`, `routing`.
- **Creation by a service:** `POST /api/scoped/tickets` accepts internal humans and two service subjects (`svc-ticket-form`, `svc-analyst-intake`); a service token must carry `userType == "service"` and `sub` equal to the name (`:211-227`). Body fields read: `ticket_type, title, description, source, requester_name, requester_email, requester_firm, linked_submission_id`. The service-token CREATE pair was "held on a firm-attribution fork" (`OPAL_TICKET.json`); its current state is unverified.
- **Visibility:** list and get are internal-only (`firmId == opal-capital`); that satisfies "internal views only". There is no "own tickets" client view.
- **Notifications (existing behaviour):** every create sends an SES email to an internal DL with the title, requester and description (`:514-546`), plus a Teams post by a separate runner. A draft containing client-derived text would travel by that email. OPEN: whether Analysis Request tickets carry the draft in the mail body or only a link.
- **Attachments: ABSENT.** No S3 client, no upload route, no bucket (`D7_TICKET_VNEXT_PRD.md` section 2, measured there with positive controls). D7 vNext WS-2 is purpose-level only, WS-1 (the storage architecture read and the ticket bucket, path shape included) comes first, and the PRD bars any attachment write before WS-1's cross-firm read fix (`D7_TICKET_VNEXT_PRD.md:76-96, 168`). WS-2's own EXERCISE: an authorized user uploads and retrieves, and a user from a DIFFERENT firm is REFUSED that object.

**How it would work (PROPOSED).**
1. New ticket type `analysis_request`, and a new service subject for the commentary Lambda (not reusing `svc-analyst-intake`). Both are changes to the ticket API; D7 moves to the laptop (Andrew, record `1dcc313303`), so they are D7's build, and this project is a consumer.
2. Ticket content: `title` names the report; `description` carries the draft (capped near 6,000 characters so the header fits 8,000); `linked_submission_id` = the IRPT `report_id`; `requester_name` / `requester_firm` = the identity that hit Generate (Alyssa first; the advisors later), set explicitly by the service; metadata (variant, models, account type, slice key, candidate record ids, `kimi_model`, `prompt_hash`) is a provenance JSON in S3 whose key is referenced from the ticket, since the ticket has no tags field written today.
3. **Attachment function (Andrew: build it).** Round 1 of the ticket carries the draft text and a link to the report in IRPT's served tier. The PDF rides on the ticket when D7's WS-1 (storage ruling, ticket bucket, cross-firm read fix) and WS-2 land. That is a D7 dependency chain: WS-1 -> WS-2 -> the commentary ticket attaches the PDF. It is the reason to sequence D7's WS-1 early.
4. **Who claims:** Andrew: the requester may claim their own ticket ("that shouldn't be a rule"). The ticket API's segregation-of-duties block (`_sod_block`, `:904`) stops that today. Andrew's word does not say whether "this case" is Analysis Request only or all tickets; put to the CTO (record `1dcc313303`).
5. **Security state to confirm before client-derived text goes into tickets:** the 2026-08-12 finding (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ctoZ_SECURITY_FINDING_20260812_TICKET_API_MISSING_TENANT_AUTHORIZATION.md`) measured deployed bytes that stamped caller identity and never checked it; list showed every firm's tickets to any authenticated user. The working-tree source I had read is newer (a deny-by-default method matrix, internal-only list/get), but the read path is described as having no firm scoping (`portal firmAccess.ts:104-113`, per the subagent), and the DEPLOYED state was not re-measured. Whether the finding is remediated is OPEN; it is the CTO's and D7's to read before a draft that quotes a firm's advisor commentary goes into a shared table.

## 9. Round-1 shape (for the CTO's decomposition)

1. Registry rows `outlook`, `sharepoint`; the model alias table, the client-domain table, the Manav address table, the name dictionary and allowlist as versioned assets.
2. The YCharts-report detection rule (one look at a real attachment), then the dredge and the daily pull into bronze.
3. Silver with the wipe; the planted-token test is the gate.
4. Gold first run on the section 6 fields.
5. The slicer as a tested Python function against gold, run over a REPLAY of past Generate compositions (no live trigger).
6. Owned dependencies, not built here: the gateway's stored-sign-in lifetime and attachment-download tool (NFRA_OPLGTW); the IRPT trigger (IRPT_BCKEND); the ticket type, service subject, SoD ruling and attachment function (D7, now on the laptop); the tickets' security state.
Later: the Kimi call and the ticket write (after a passed wipe test), the PDF on the ticket (after D7 WS-1/2), the PDF holdings parser, news and keyword context.

## 10. Calls waiting on Andrew (new since the last round)

1. Is Yang's commentary in or out of the criterion? (Section 2.)
2. Slice within a recipient firm only, or across firms? (Section 7.)
3. Analysis Request tickets: draft in the SES email body, or a link only? (Section 8.)
4. (CTO's, from `1dcc313303`.) Requester-claim ruling: Analysis Request only, or all tickets?

## 11. Superseded, and what this brief does not claim

- **Superseded from v1:** item 1 (roster-based wipe), item 5 (`approved` and the "Looks good" rule), item 6 (model-weights source as a gold dependency), item 7 (PRD-001 field freeze and the reconciliation sign-off as a gate: Andrew: format is ours). **From v2:** section 4 (Alyssa's fixtures as a seed), section 5 (roster, `sent_external`), section 6 (`finder_status`, PRD-001 fidelity), section 8 (output home in `opal-data-irpt`, now the Ticket Center), section 11 (the eight calls, answered). Still standing from v1: items 3 (`record_id`), 4 (attachments in bronze), 10 (registry rows and the moratorium).
- Not read: `AnalysisTab.tsx`, `resolution_kimi.py`, `graph_client.py`, `/yc-commentary`, the deployed ticket Lambda bytes, the D7 IA spec, the live gateway attachment tools.
- Not measured: the count of commentary emails, the stored-sign-in lifetime, the YCharts PDF signature, the pypdf holdings recovery.
- Estate facts were read by subagents from the cited lines; this seat did not re-open each. No client names appear here.
