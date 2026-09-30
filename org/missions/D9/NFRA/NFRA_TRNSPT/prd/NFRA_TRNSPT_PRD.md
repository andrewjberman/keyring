# NFRA_TRNSPT -- the Opal communications database and the commentary drafter

```json
{
 "project": "NFRA_TRNSPT",
 "directive": "D9",
 "fabric": "laptop",
 "prd_version": "v0.1",
 "step": 4,
 "brief_ref": "docs/briefs/nfra-trnspt-commentary-ingestion-expansion-brief-v3-20260930.md@bd14c47f70",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7", "FWD-8", "FWD-9", "FWD-10", "FWD-11"],
 "status": "RATIFIED"
}
```

Author: `1.0.0_SA_CTO`. D9 / NFRA / laptop. Register row `org/missions/D9/NFRA/NFRA_TRNSPT/project.json` @1d8905b007 (COO lane `2.0.0_SA_COO~T`, @194a27ce43).

Briefs: the header's `brief_ref` is the CRO's consolidated commentary brief (it extends the L1 brief `docs/briefs/nfra-trnspt-opal-transcript-database-brief-20260929.md` @4206994dd3 from `4.0.0_SA_CRO~T`, which is read as a second brief and covered in section 8); the consolidated brief is
`docs/briefs/nfra-trnspt-commentary-ingestion-expansion-brief-v3-20260930.md` @bd14c47f70, which wins over its own v1 and v2 where they differ. Endpoint:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_NFRA_TRNSPT_20260930.md` revision 2 @3d825e1a26. Andrew confirmed its DONE WHEN lines, 2026-09-30 ~06:xxZ:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260930_06xxZ_TRNSPT_DONE_WHEN_CONFIRMED_PAGEFILE_APPROVED_KIMI_STANDING_WORD.md` @6a861c4e18
("Confirm, we have a lot more stuff that is going to be going through that bucket/channel but that one is a start"). The section below carries the endpoint's outcomes verbatim.

## ENDPOINT (step 2, /endpoint --forward)

```
  FWD-1  Andrew opens the database on a Monday afternoon and finds that morning's meeting, with who said what, and nobody touched anything
         DONE WHEN  EXERCISED -- one real Monday meeting followed from its end to the readable transcript, no person running a step
         ACCEPT     Andrew reads the Monday meeting in the database the same day; it fails if anyone had to sit at a keyboard or run a command
         SOURCE     L1 brief O1, Part III

  FWD-2  Every regular investment meeting arrives on its own, the Research Meeting included
         DONE WHEN  EXERCISED -- one occurrence of each of the four meeting types has arrived unaided
         ACCEPT     for each of the four meeting types, the latest meeting is in the database without anyone fetching it
         SOURCE     L1 brief O2, findings 6-7

  FWD-3  Someone who needs last quarter's meetings gets them, and new meetings no longer expire unread
         DONE WHEN  EXERCISED -- a named past meeting still held by Microsoft has been checked in the database, and a new one landed before expiry
         ACCEPT     Andrew names a past meeting that Microsoft still holds and finds it; no meeting that could be fetched on 29 September is later found missing
         SOURCE     L1 brief O3, finding 5

  FWD-4  A person can tell what the database holds and what it is missing, and why
         DONE WHEN  EXERCISED -- asked about one missing meeting, a person gets its reason
         ACCEPT     for any meeting and date, the answer is "here" or a cause (never recorded, expired, refused); never a shrug
         SOURCE     L1 brief O4

  FWD-5  An analyst reads a transcript as structured speech, not a raw file
         DONE WHEN  EXERCISED -- one analyst has read one meeting this way, including one of the 29 existing Research Meeting transcripts
         ACCEPT     an analyst who now opens a file to find what was said about one company gets it without opening the file
         SOURCE     L1 brief O5, finding 11

  FWD-6  A market update (a PowerPoint) is put in the database and kept exactly as received
         DONE WHEN  EXERCISED -- one real market update placed and later compared with the original
         ACCEPT     someone places a market update and later gets back the identical deck; a re-saved copy is recognisable as the same deck
         SOURCE     L1 brief O6, addendum A1, A3

  FWD-7  (AMENDED IN PLACE) Investment feedback that Manav sends a client with a YCharts report attached is filed in the database on its own, every day, and never altered
         DONE WHEN  EXERCISED -- one real such email followed from its sending to its filed copy by the ordinary daily run, no person starting it
         ACCEPT     Andrew finds a real feedback email the next day in the database; the original is kept exactly as received and only two people can read it;
                    the searchable copy has client names and identifying numbers removed; an email that does not meet all three tests (Manav or another named
                    author, a client recipient, a YCharts report attached) is not treated as feedback
         SOURCE     v3 brief sections 2-5; Andrew-direct 2026-09-30 (own ingestion, criterion, daily pull from his mailbox)

  FWD-8  Andrew can show who may read the database, and it is only the people he named
         DONE WHEN  EXERCISED -- a third person is tried and refused, in front of Andrew
         ACCEPT     Andrew and the terminal seat's account can read the original; a third person cannot by any route, and Andrew sees that shown, not asserted.
                    A separate, narrower reader may see only the copy with names and numbers removed
         SOURCE     L1 brief O8; v3 brief section 4 (a scoped role reads the wiped copies only)

  FWD-9  A builder asks one question across meetings, updates and commentary
         DONE WHEN  APPLIED -- the shared layer that makes it possible is in place; a live question is a later round
         ACCEPT     an analyst asks which securities were discussed this quarter and gets one answer covering all three, not three searches
         SOURCE     L1 brief O9 -- later round, not a round-1 promise

  FWD-10 When someone generates an analysis report in Investor Reporting, a draft commentary in Opal's voice appears for an Opal person to review, without slowing the report
         DONE WHEN  EXERCISED -- one real report generated, and its draft commentary opened by the person who asked for it
         ACCEPT     the person who generates a report (first Alyssa, later advisors) finds a ticket with a draft written from past commentary for a similar report;
                    the draft never reaches an advisor unless a person sends it; the person who asked can claim and finish their own ticket; the report itself is never
                    late or failed because of the draft; nothing in the draft identifies another client or firm
         SOURCE     v3 brief sections 1, 7, 8; Andrew-direct 2026-09-30 (Analysis tab tie-in, Ticket Center, draft only, Kimi K3, requester may claim own ticket, all tickets)

  FWD-11 The report itself is attached to the commentary ticket, not linked
         DONE WHEN  EXERCISED -- a person opens the report from the ticket, and a person at a different firm is tried and refused
         ACCEPT     the Opal person who opens the ticket opens the actual report from it; a person at another firm cannot open it
         SOURCE     v3 brief addendum 3; Andrew-direct 2026-09-30 ("the text is just included + attachment included on the ticket"). Depends on the ticket system's
                    attachment work (D7, now on the laptop); until it lands the ticket carries the text and a link, so FWD-10 does not wait on it.
```

## ENDPOINT PROVENANCE (outside the ratified section)

- FWD-1..FWD-6, FWD-8, FWD-9 come from the L1 brief @4206994dd3 (O1-O6, O8, O9). FWD-7's wording is the CRO's v3 criterion; the L1 brief's O7 ("analysis commentary, supplied by Alyssa") is
  RETIRED into it: the source is Andrew's mailbox, not Alyssa's supply. This is a scope change to the same outcome, not a shrink: it now asks for EXERCISED.
- FWD-10 and FWD-11 are new at revision 2; ids are permanent and no id is renumbered.
- **A volume finding that bears on FWD-10, reported to Andrew and not decided here.** The CRO's first real-mailbox measurement (v3 addendum 8) finds the test mailbox starts in October 2025 and holds roughly 6 to 18
  real commentary emails in eleven months, not hundreds; Alyssa's labelled cache is 70. A variant-matched slice may therefore find zero or one precedent. The PRD's answer is in C-SLICE: a draft with no precedent is
  produced and says so. Whether to add Alyssa's cache as a second source is a later Andrew call.
- **The transcripts thread and the communications workstream run in parallel** (Andrew: "that one is a start"; a workstream is a SCOPE, not a round). FWD-1 is the thread; the communications workstream's own
  thread is FWD-7 in test.

## CONTRACTS

| Contract | Direction / owner | Binding agreement |
|---|---|---|
| C-BUCKET: the bucket | consumed; `0.7.0_AE_CloudOps` built it (`infra/aws/terraform/transcripts/main.tf`) | `opal-data-transcripts`: private, SSE-KMS under its own key, versioned, public access blocked, TLS-only (READ L1 brief Part IV.1). Scope `transcripts` and source `teams` are registry rows; `bucket_provisioned` is true. |
| C-TIERS: the medallion | Andrew-direct 2026-09-30 | BRONZE holds each object exactly as received (Graph JSON, WebVTT, PDF, PPTX; byte for byte, with a sidecar). SILVER is typed, de-duplicated, PARQUET, with PII wiped. GOLD is where Alyssa-style fields are derived and where the first run of the commentary schema lives (CLAUDE_ANNEX 17c: one Opal shape, one contract file). Bronze stays in its native format because "as received" cannot be a re-typed table. |
| C-SOURCES: registry rows | LGIC lane; this project's L3 | `outlook` and `sharepoint` are NOT registry rows today (READ v3 section 4; `infra/logic/registry/systems.json`). Nothing is written to a path until both rows exist and `lib/opal_naming.py validate` passes. |
| C-NAMES: rule 30 | consumed; LGIC | Every S3 address is `lib/opal_naming.py address()` output and every resource name is `name()` output. The shapes in the v3 brief are shapes, not addresses. A builder refusal is a missing registry row, never a typed workaround. |
| C-IDENTITY: the pull's sign-in | Andrew-direct 2026-09-30 | The daily pull runs through the EXISTING Opal gateway under Andrew's account; no new app registration, no IT (Andrew is a Cloud Application Administrator and can grant any Graph permission needed). Test fetches use `andrew@opalinvest.com`, never Alyssa's mailbox. How long a stored sign-in lasts is UNMEASURED: an engineering item with its own criterion, not an Andrew call. The gateway holds delegated `Mail.Read` (READ `infra/aws/ec2/opal-gateway/app/config.py:51`). |
| C-GATEWAY-TOOLS: owned dependency | `NFRA_OPLGTW` (site Z, `1.0.0_SA_CTO~O`) | Three gateway tools under the existing Mail.Read: an attachment-download tool, a filtered paged mail list (sender, received date, has-attachment, following `@odata.nextLink`), and `ccRecipients` returned. Requested through MSTR's bus at L6; this project does not build them. Until they land the criterion's YCharts test is a heuristic (C-CRITERION). |
| C-CRITERION: what is feedback | Andrew-direct 2026-09-30 | An email is ingested when the SENDER is on a named author table (Manav; Yang if her addresses are supplied) AND a YCharts report is attached AND it is investment feedback. The recipient domain is a stored ATTRIBUTE (`recipient_firm`), not a gate. The scan is of the author's mail, not the distribution channels. Automated "49 Trade Update" mail is excluded by rule (subject prefix, single distribution-address recipient, no reply prefix). The three booleans and `recipient_firm` are stored so the decision is auditable and re-runnable. Precision is a claim to MEASURE: v3 addendum 8 found 6 confirmed and about 13 probable of 18 on the name-and-size rule alone, so the PDF test is a stated heuristic until the attachment tool exists. |
| C-DEDUP: identity | this project | `record_id = sha256(internetMessageId)`. The Graph `id` is per mailbox and goes only in the bronze sidecar. An absent `internetMessageId` falls back to a hash of (sent_at, sender domain, subject, body hash), flagged `id_source=fallback`. `conversationId` groups threads and is never a dedup key. |
| C-WIPE: silver's PII wipe | Andrew's design, v3 section 5 | Names: a vendored, hash-pinned dictionary (public name lists) applied case-sensitively, behind an ALLOWLIST (Opal model names, products, tickers, finance terms, theme labels), plus the client firms' names and advisor names. Identifier-like strings (a token over 4 characters with a digit, not a percentage, decimal, amount, year or date): replaced by `[ID]`, no hash (a hash of an 8-digit id is reversible by enumeration). Emails and phone numbers by pattern. Theme labels are wiped too. Anything capitalised and unknown goes to `pii_residual_flags` and is held out of serving. Block structure is kept because the slicer needs it. STATED LIMIT: the wipe removes dictionary names, identifier-like numbers and patterns; it does not remove a client name that is on no list. |
| C-WIPE-GATE: silver is not real until | this project | A planted-token leak test passes (names in a heading, in a salutation, split across an HTML tag, in a different case, in a common-word name, plus 8-digit and alphanumeric ids). Its result is "the planted classes were removed", never "no PII remains". No gold body text leaves Opal before it passes. |
| C-GOLD-FIELDS: the commentary gold table | this project; CLAUDE_ANNEX 17c | ONE contract file `org/standards/NFRA_TRNSPT_COMMENTARY_GOLD_CONTRACT.json` (authored by a round-1 cell). Fields per v3 section 6: `record_id`, `sent_at`, `recipient_firm`, `yc_variant` (1/2/3 from models referenced 0/1/2+), `models_referenced` (an alias table mapped to IRPT `comparison_keys`), `account_type`, `themes` (list of {theme, client_figure, model_figure}), `body_text`, `paragraph_hashes[]`, `body_hash`, `pdf_sha256`, `has_pdf`, plus nullable `holdings` and `request_text`. Alyssa's PRD-001 is inspiration only. `approved` is not a field (an external send is approved); a null is not a schema violation for a field named nullable. |
| C-SLICE: the slicer | this project | All Python, no AI. `yc_variant` equal to the request's variant, ranked by overlap of models with the request's models, then account type, then recency; near-duplicates removed by `paragraph_hashes`; about ten candidates. Across firms (Andrew: "across all firms, its not their content, its manav's response"). With no candidate the slicer falls back to the nearest variant and the draft says so in its provenance; with none at all a draft is still produced and says it has no precedent. |
| C-KIMI: the one model call | Andrew-direct 2026-09-30 | Kimi K3, reusing the estate's existing implementation (READ v3 section 8: `infra/aws/lambda/investor-reporting/intake/resolution_kimi.py:20`, secret `astn/kimi/api-key`). Input limited to abstract fields (variant, model names, account type, themes, holdings as category weights; no client identity, no account ids). Output is a DRAFT, visible in Opal-internal views only. Andrew's word is given for the first call, and only after C-WIPE-GATE passes; any other use of a vendor call carries his word per use. |
| C-TICKET: where the draft lands | consumed; D7 `OPAL_TICKET_VNEXT` (now laptop) | A new ticket type `analysis_request`; the draft text in the ticket and the report as an ATTACHMENT; requester name and firm on the ticket (Alyssa first). The Ticket Center is internal-only (READ v3 section 8). The requester may claim and complete their own ticket, for ALL tickets: D7 removes the segregation-of-duties block (`_sod_block`, `infra/aws/lambda/ticket_center/lambda_function.py:904`) after confirming nothing there was the only control on a trade ticket. The ticket's deployed security state (the 2026-08-12 finding) is read BEFORE client-derived text goes into it. |
| C-TICKET-ATTACH: the attachment | D7 WS-1 then WS-2 | D7's storage read and ticket bucket (WS-1, with its cross-firm read fix) come before any attachment write; WS-2's own exercise is an authorised upload and retrieval and a different-firm user REFUSED. Until it lands the ticket carries text and a report link (INTERIM, this PRD's ruling 6.5). |
| C-TRIGGER: the READY hook | consumed; IRPT_BCKEND | No hook exists after a report is READY (READ v3 section 8). The build is a task order to IRPT_BCKEND, not a TRNSPT build; a DynamoDB stream on `irpt-requests` filtered to `REPORT#` items is the proposed route. A trigger is a route, not an alert. The commentary must never block or fail the report; a failure goes to a dead-letter queue and a retry. |
| C-READERS: who reads what | Andrew-direct L1 brief O8 | The raw (bronze) tier has exactly two named readers: Andrew and `opalbloomberg@opalinvest.com`. A pipeline role that WRITES is a third principal and is named in the round's halves; the writer cannot be a reader by accident. A separate scoped role may read the wiped silver and gold prefixes only. |
| C-MORATORIUM: no alerts | law (CLAUDE.md section 5) | No failure alarm, SNS or SES send, freshness checker, health report or monitor is built. A daily pull runs on its own clock (a schedule), never "on success of upstream" alone. Gaps (FWD-4) are a data table, not a notification. Anything else needs Andrew's explicit word. |
| C-FIRM: firms | law (CLAUDE.md section 5) | The cross-firm rule binds pipeline trees, not this serving path. Because examples cross firms, the wipe removes firm and advisor names so a firm's identity cannot ride inside a draft. |
| C-COPY: what is not copied | law (CLAUDE.md section 5) | Nothing here creates a shadow pipeline or a standing parity comparator. The OneDrive market-update generator is prior art for later tiers, not in scope for bronze, and is not imported. |

## 1. The arc

Start: a private bucket with 90 objects landed by hand (30 Teams transcripts as raw WebVTT, raw metadata and a sidecar; 15 Morning Meeting, 7 OCIO IC, 8 Asset Management IC); no puller; the Research Meeting refused with a
"User does not have access to lookup meeting" (3003) reading; 34 transcripts listed and 30 retrieved before four expired; market updates as decks in a SharePoint folder (one deck) and a OneDrive archive (about 48);
investment feedback emails held in mailboxes; and a commentary skill that exists only on Alyssa's machine. Nothing is in one place and nothing arrives on its own.

End: the four regular meetings, the market updates and the investment feedback land in one database on their own, kept as received in bronze and typed and wiped in silver; a person can say what is held and why anything
is missing; only two people can read the raw tier; and an Analysis report generated in Investor Reporting produces a draft commentary ticket for an Opal person, from past commentary in Manav's voice, without slowing the report.

## 2. THREAD -- FWD-1, the Monday meeting end to end (round 1, transcripts workstream)

1. The meeting ends -> a SCHEDULED pull notices it (a listing of the meeting's series by its meeting id; no change notification is claimed; the cadence is a schedule on its own clock)
2. The pull -> the Opal gateway's transcript tools under Andrew's account (the tools are `NFRA_OPLGTW`'s parked spec `docs/briefs/opal-gateway-meeting-transcript-tools-spec-20260929.md`; built on site Z)
3. The gateway -> bronze landing under the builder-produced address for source `teams`, scope `transcripts`, table for the meeting: the raw WebVTT, the raw metadata WebVTT and the sidecar, byte for byte
4. Bronze -> silver: the parsed speaker turns as parquet (speaker, order, time), for one meeting (FWD-5's first exercise)
5. Silver -> the reader: Andrew opens the meeting through the reader route he uses (the route is a C-READERS decision: the gateway tool or a dedicated AWS role) and reads who said what
6. Trace -> every step ran without a person; the run's record shows the pull, the landing and the parse with their timestamps

Round 1 builds only this thread for the transcripts workstream. It is blocked on ONE thing outside this project: the unattended sign-in (C-IDENTITY), whose stored-token lifetime is measured first. It is not a reason to stop
the round: hops 3 to 6 are built and exercised against a pull run under a fresh sign-in, and hop 1 to 2 waits on the measurement.

## 3. ENRICHMENT BACKLOG (ordered, one line each)

**Transcripts workstream**
1. The Research Meeting: find why the refusal happens (organizer Lauren Harmon; a different route or a tenant setting) and land its transcripts (FWD-2).
2. The other three meeting archetypes' unattended pull and their series enumeration (FWD-2).
3. Backfill: existing history Microsoft still holds, oldest first, before its roughly 120-day expiry (FWD-3).
4. The completeness record: per meeting and date, "here" or a cause (FWD-4).
5. The 29 existing Research Meeting transcripts and their parser folded in, with the store's later home decided (FWD-5).
6. The second reader route and the two-reader demonstration (FWD-8).

**Communications workstream (parallel; round 1 is the CRO's v3 section 9 shape)**
1. Registry rows `outlook` and `sharepoint`; the alias table, the client-domain table, the author-address table, the name dictionary and allowlist as versioned data assets.
2. The YCharts-report detection rule (one look at a real attachment) and the dredge of Andrew's mailbox into bronze by the date-sliced method that works under today's tools (v3 addendum 8), then the daily pull.
3. Silver with the wipe, and the planted-token test as its gate.
4. Gold first run on the C-GOLD-FIELDS schema and its contract file.
5. The slicer as a tested Python function against gold, run over a REPLAY of past Generate compositions (no live trigger).
6. FWD-6: the market update placed and later compared with the original; identity by SHA-256 plus Graph `quickXorHash`; the SharePoint folder as the live source and the OneDrive archive as a one-time backfill under a distinct marker.
7. After the wipe test passes: the Kimi call and the ticket write (FWD-10), the READY hook (IRPT_BCKEND), the ticket type and identity and requester-claim (D7), then the report attached (FWD-11).
8. FWD-9's shared query layer.

## 4. Engines (one row per engine)

| Engine | Serving shape | Role here | Deploy mechanics |
|---|---|---|---|
| Opal gateway (`infra/aws/ec2/opal-gateway`, site Z) | an EC2 service with delegated tokens | the only Microsoft sign-in path Opal runs; the transcript tools and the three mail tools are built there | `NFRA_OPLGTW`'s project; requested via MSTR's bus |
| the pull jobs | scheduled Python on an EventBridge clock, one per source | list, fetch and land into bronze | names per C-NAMES; DS/AE lane; each schedule its own clock |
| bronze to silver | an event-triggered Python Lambda | parse, wipe, de-duplicate, write parquet | Terraform only for the Lambda; the wipe data assets are versioned and hash-pinned |
| gold derivation | one Python Lambda with pyarrow (layer `pandas-pyarrow-layer:1`, READ v3 section 6) | commentary gold; no AI | same |
| the commentary Lambda | Lambda reading gold partitions with pyarrow, one Kimi call | FWD-10's draft | the first call after C-WIPE-GATE and Andrew's word |
| the Ticket Center (`opal-ticket-api`) | Lambda over DynamoDB `opal-tickets` | where the draft lands | D7's builds |
| IRPT | request/worker Lambdas, an EC2 resident host | the report and its READY signal | IRPT_BCKEND's project |

## 5. WORKSTREAMS AND OWNERS

- **`2.0.0_SA_COO~T` is the COO lane** (Andrew-direct 2026-09-30: "I want COO~T spawned to get on the NFRA_TRNSPT work now"; seating accepted: "No that should be fine, I do not care about TAXSMA right now"). Seat brief:
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/SEAT_BRIEF_COO_T_NFRA_TRNSPT_20260930.md` @194a27ce43. `~T` holds this one project.
- **Two workstreams with disjoint write surfaces** (a workstream is a scope): TRANSCRIPTS (FWD-1..5; its write surface is the `teams`-source tables, their pull job and parse) and COMMUNICATIONS (FWD-6..11; its
  write surface is the `outlook` and `sharepoint`-source tables, the commentary gold, the commentary Lambda and its ticket write). If the COO wants a second lane instance for one of them, that is the COO's L6 call under
  the one-issuer-per-round rule.
- **Owned elsewhere, named in the decomposition and NOT built here:** the gateway tools (`NFRA_OPLGTW`, site Z, via the CTO relay); the READY hook (IRPT_BCKEND); the ticket type, service identity, requester-claim
  and attachments (D7 `OPAL_TICKET_VNEXT`, laptop); the ticket API's deployed security state (D7 and the CTO read it); registry rows (LGIC lane, this project's L3).
- **The CRO** (`4.0.0_SA_CRO`) signs the BRIEF half of the sign-off; the CVO (`3.0.0_SA_CVO`) the ratified-text half.

## 6. Rulings closed at L4 (no decide-first question enters L5)

1. The tiering is Andrew's (C-TIERS); silver and gold are parquet; bronze is native.
2. The route is the existing gateway under Andrew's account (C-IDENTITY); no app registration, no IT. The stored sign-in's lifetime is a measurement, not a call.
3. The ingest criterion is C-CRITERION, with the recipient domain an attribute. Its precision is measured on the first run and reported; the heuristic status of the PDF test is stated until the attachment tool exists.
4. PII: the wipe is C-WIPE, with `[ID]` and not a hash for identifier-like strings, and C-WIPE-GATE decides when silver is real. A wipe is not proof of no PII, and no record says it is.
5. INTERIM for FWD-11: the ticket ships with the draft text and a link to the report until D7's WS-1 and WS-2 land, then gains the attachment. FWD-10 does not wait on the attachment.
6. Kimi K3 is the model; Andrew's word is given for the first call after C-WIPE-GATE; anything else is per use.
7. Contract files are data and are authored in round 1 (C-GOLD-FIELDS, C-CRITERION's tables); the freeze is a file signed by Andrew, not a chat statement.
8. Anything that needs a new outcome (Andrew: "we have a lot more stuff that is going to be going through that bucket/channel") is a PRD addendum with the next unused FWD id, never a cell's choice.

## 7. SURFACE MANIFEST (step 4 -> step 5)

`claim` names the evidence class of the address. `measured` means the file was read to exist at L4 (2026-09-30 ~07:xxZ); paths and line numbers cited in the briefs are `held` from the CRO's subagent reads
unless stated. NEW surfaces are `unmeasured`.

| id | outcome_ref | surface | claim | MEASURED-BY / evidence | lane | verb | depends_on | accept | bound |
|---|---|---|---|---|---|---|---|---|---|
| S01 | FWD-1..FWD-9 | bucket `opal-data-transcripts` (`infra/aws/terraform/transcripts/main.tf`) | measured | file exists at L4; the bucket read by CloudOps (L1 brief Part IV.1) | AE CloudOps | consume | -- | all | two named readers |
| S02 | all | registry rows `outlook`, `sharepoint` (`infra/logic/registry/systems.json`) | measured (file); rows unmeasured | file exists at L4; the rows are ABSENT (v3 section 4, `lib/opal_naming.py:1701-1704`) | LGIC / this project | wire | -- | FWD-6, FWD-7 | `lib/opal_naming.py validate` passes |
| S03 | FWD-1 | the pull job for the four meeting types (NEW) | unmeasured | names per `name()` | DS/AE | wire | S01, S05 | FWD-1 | its own schedule |
| S04 | FWD-1 | transcript tools on the gateway (`infra/aws/ec2/opal-gateway/app/`) | measured (dir); tools unmeasured | dir exists at L4; spec `docs/briefs/opal-gateway-meeting-transcript-tools-spec-20260929.md` | site Z `NFRA_OPLGTW` | consume | -- | FWD-1 | not built here |
| S05 | FWD-1 | the unattended sign-in and its measured lifetime (`infra/aws/ec2/opal-gateway/app/token_broker.py`) | measured (file); lifetime unmeasured | file exists at L4; `NeedsLogin` at :171-183 (held) | site Z `NFRA_OPLGTW` | measure | -- | FWD-1 | a measurement first |
| S06 | FWD-1, FWD-5 | silver `transcripts` parse (NEW; the WebVTT parser prior art is `research_transcripts/`) | measured (prior art dir); new surface unmeasured | dir exists at L4 | DS | wire | S03 | FWD-5 | parquet; no `bd` firm data |
| S07 | FWD-2 | the Research Meeting refusal investigation (NEW) | unmeasured | L1 brief finding 6 | this project | verify | -- | FWD-2 | cause named or a route found |
| S08 | FWD-4 | the completeness table (NEW) | unmeasured | -- | this project | wire | S03, S06 | FWD-4 | a data table; no alert |
| S09 | FWD-7 | author, client-domain, alias tables and the name dictionary and allowlist (NEW, versioned data) | unmeasured | C-CRITERION, C-WIPE, C-GOLD-FIELDS | this project | wire | -- | FWD-7 | hash-pinned |
| S10 | FWD-7 | the YCharts-report detection rule (NEW) | unmeasured | one look at a real attachment | this project | measure | S12 | FWD-7 | an explicit rule, not a keyword guess |
| S11 | FWD-7 | the dredge and the daily pull of Andrew's mailbox (NEW) | unmeasured | date-sliced search method (v3 addendum 8) | DS/AE | wire | S02, S12 | FWD-7 | delegated read; no writes to mail |
| S12 | FWD-7 | three gateway mail tools: attachment download, filtered paged list, `ccRecipients` (`infra/aws/ec2/opal-gateway/app/config.py:51` for the scope) | measured (file); tools unmeasured | file exists at L4; the tools are ABSENT (v3 addendum 6) | site Z `NFRA_OPLGTW` | consume | -- | FWD-7 | requested via MSTR's bus |
| S13 | FWD-7 | bronze `analysis_commentary` landing (NEW) | unmeasured | address by `address()` | DS/AE | wire | S01, S02, S11 | FWD-7 | byte for byte; two readers |
| S14 | FWD-7 | silver with wipe and its planted-token test (NEW) | unmeasured | C-WIPE, C-WIPE-GATE | DS | wire | S09, S13 | FWD-7 | the test is the gate |
| S15 | FWD-7, FWD-10 | gold contract file `org/standards/NFRA_TRNSPT_COMMENTARY_GOLD_CONTRACT.json` and gold derivation (NEW) | unmeasured | C-GOLD-FIELDS; CLAUDE_ANNEX 17c | DS | wire | S14 | FWD-7 | one contract; hash conformance |
| S16 | FWD-10 | the slicer (NEW; a Python function, replay-tested) | unmeasured | C-SLICE | DS | wire | S15 | FWD-10 | no AI |
| S17 | FWD-6 | market-update landing: SharePoint folder (live) and the OneDrive archive (one-time) into bronze `market_update` (NEW) | unmeasured | the deck is the one under `Shared Documents/Market Update` (MEASURED by the CTO 2026-09-29/30) | DS/AE | wire | S02 | FWD-6 | identity by SHA-256 and `quickXorHash` |
| S18 | FWD-10 | the IRPT READY hook on `irpt-requests` (`infra/aws/lambda/investor-reporting/ycharts/generate/durable_job.py` for the job state) | measured (file); hook unmeasured | file exists at L4; hook ABSENT (v3 section 8) | IRPT_BCKEND | consume | -- | FWD-10 | a task order there; the report never blocked |
| S19 | FWD-10 | the commentary Lambda and its one Kimi call (`infra/aws/lambda/investor-reporting/intake/resolution_kimi.py` is the estate's implementation) | measured (file); Lambda unmeasured | file exists at L4 | DS/AE | wire | S16, S18, S14 | FWD-10 | first call only after C-WIPE-GATE and Andrew's word |
| S20 | FWD-10, FWD-11 | ticket type `analysis_request`, a service identity, requester-claim on all tickets, attachments (`infra/aws/lambda/ticket_center/lambda_function.py`, `docs/architecture/D7_TICKET_VNEXT_PRD.md`) | measured (files); changes unmeasured | files exist at L4 | D7 `OPAL_TICKET_VNEXT` | consume | -- | FWD-10, FWD-11 | D7's builds; security state read first |
| S21 | FWD-8 | the second-reader route and the third-person refusal demonstration (NEW) | unmeasured | L1 brief O8 | AE CloudOps | verify | S01 | FWD-8 | shown to Andrew |
| S22 | FWD-1..FWD-11 | NEW journey test across S01-S21 | unmeasured | the eleven ACCEPT lines | verification | verify | S06, S13, S15 | all | reads served artifacts |

MECE check: outcomes 11 of 11 have at least one row (FWD-9 rides S15's contract and S22; its live query is a later round). Every dependency named in section 5 has a row or is named as owned elsewhere
(S04, S05, S12, S18, S20). Relied-on work has no row by design.

## 8. BRIEF COVERAGE -- content carried, not just cited

The L1 brief @4206994dd3 has 1 level-1 title, 9 level-2 headings (Parts I-VII, REFS TO CARRY, ADDENDUM) and 2 level-3 headings: 12 of 12 are mapped. The v3 brief @bd14c47f70 has 1 level-1 title and 12 level-2
headings (the ADDENDUM and sections 1-11): 13 of 13 are mapped.

| Brief heading | Carried content | Consuming sections / surfaces |
|---|---|---|
| L1 title and preamble | Andrew's words: bronze ingestion for market update and analysis commentary; the bucket as a central database of Opal communications | header; C-BUCKET; section 1 |
| L1 PART I -- outcome territory (candidate thread; the rest) | O1 the Monday thread; O2-O9 | FWD-1..FWD-9; section 2 |
| L1 PART II -- boundary | owns the bucket's contents and how they arrive; relies on NFRA_OPLGTW, OPAL_ALTRESEARCH, LGIC, the Teams tenant, the BBG seat | C-GATEWAY-TOOLS; section 5; related in the register row |
| L1 PART III -- qualitative bar | per-outcome pass tests | ACCEPT lines; ruling 6.3 |
| L1 PART IV -- substrate findings 1-12 | bucket private by key; canonical name; the snake_case table slot; delegated access proven; retention real; the Research Meeting refused; one meeting id serves a series; a start signal is readable; gateway is per-user; over-broad sign-in not to build on; the transcript store and parser exist; no design for market updates found | C-BUCKET; C-SOURCES; C-NAMES; C-IDENTITY; section 1; section 2; S06, S07 |
| L1 PART V -- what must be true | a no-person Microsoft path; a trigger or schedule; the Research Meeting answer; reader route; registry rows; a definition of market update and commentary; the silver home; a completeness record; a retention view; an owner for the gateway tools | C-IDENTITY; C-READERS; C-GATEWAY-TOOLS; S02-S08; section 3 |
| L1 PART VI -- status (not outcome-bearing) | 90 objects landed by hand; no puller; readers are Andrew only | section 1 |
| L1 PART VII -- does not claim | no push trigger; no token lifetime; not why the Research Meeting is refused | C-IDENTITY; S05, S07 |
| L1 REFS TO CARRY | the recon and spec briefs, the first-pull and reader-principal records, the bucket handoff, the placement record, `research_transcripts/` | related in the register row; S04, S06 |
| L1 ADDENDUM 2026-09-29 (A1-A4) | market update is a PowerPoint (three locations); commentary is email (Alyssa's route, superseded by v3); new dependencies; push can wait | FWD-6, FWD-7; C-DEDUP; S17 |
| v3 title, preamble | the CRO's consolidated brief; supersedes v1 and v2 where they differ | header |
| v3 ADDENDUM (items 1-8) | the author table, cross-firm slicing, the ticket carries text and attachment, requester-claim on all tickets, the gateway route and three tools, criterion (b) an attribute, and the first real-mailbox measurements (124 candidates, 6 confirmed and about 13 probable of 18, a small dataset, an October 2025 start) | C-CRITERION; C-SLICE; C-TICKET; C-GATEWAY-TOOLS; section 1; S10-S12 |
| v3 section 1 -- the premise, as a flow | the Generate, READY, hook, slice, one Kimi call, ticket flow | FWD-10; C-TRIGGER; C-SLICE; C-KIMI; S16, S18, S19 |
| v3 section 2 -- the ingestion criterion | the three tests; consequences accepted | C-CRITERION; ruling 6.3; S10 |
| v3 section 3 -- daily pull | gateway tools measured; date-sliced search; schedule on its own clock; no alarm | C-IDENTITY; C-MORATORIUM; S11 |
| v3 section 4 -- bronze | byte-for-byte objects, sidecar, partition by sent date, two readers | C-TIERS; C-READERS; S13 |
| v3 section 5 -- silver and the wipe | dictionary, allowlist, `[ID]`, guards, stated limit | C-WIPE; C-WIPE-GATE; S14 |
| v3 section 6 -- gold | the field table and derivations; a concrete example row | C-GOLD-FIELDS; S15 |
| v3 section 7 -- the slicer | the slice; the same-firm question, closed as across firms by Andrew | C-SLICE; C-FIRM; S16 |
| v3 section 8 -- trigger, Kimi, Ticket Center | the hook is absent; Kimi in the estate; the Ticket Center's types, service creation, notifications, attachments ABSENT, the security finding | C-TRIGGER; C-KIMI; C-TICKET; C-TICKET-ATTACH; S18-S20 |
| v3 section 9 -- round-1 shape | registry rows, the rule and bronze, silver with the wipe, gold first run, the slicer over a replay, owned dependencies | section 3 (communications); section 5 |
| v3 section 10 -- calls to Andrew | now empty of calls, apart from owned dependencies | section 6 |
| v3 section 11 -- superseded and not claimed | what v1 and v2 lose; not read and not measured items | ruling 6.3; section 1 |
