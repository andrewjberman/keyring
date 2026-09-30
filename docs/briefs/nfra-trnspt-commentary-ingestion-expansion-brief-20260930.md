# BRIEF (expansion): NFRA_TRNSPT -- commentary ingestion, tiers and schemas, ten depth items

- Author: `4.0.0_SA_CRO` (base), 2026-09-30. Answers the CTO hand-off `org/tier1_exec/1.0.0_SA_CTO/deliverables/HANDOFF_TO_CRO_NFRA_TRNSPT_COMMENTARY_INGESTION_AND_TIERS_20260930.md` @050b4da760, section 9.
- Consumer: `1.0.0_SA_CTO`, for the L4 PRD and the L3 registration. Extends `docs/briefs/nfra-trnspt-opal-transcript-database-brief-20260929.md`; does not replace it.
- Andrew's words: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260930_020xZ_TRNSPT_COMMENTARY_TIERS_KIMI_TEST_MAILBOX_HANDOFF_TO_CRO.md`.
- Claim classes: READ (seen in a file, cited), MEASURED (a call run), PROPOSED (this seat's design), OPEN (needs a ruling), ABSENT (searched, scope stated). Estate facts marked READ were read by a research subagent of this seat from the cited lines; this seat did not re-open each line. Alyssa's PRD-001/002 were read through the Opal gateway (read-only) by a subagent; no client names or PII were copied out.

## 0. What changes since the hand-off

1. **Kimi is already in the estate (READ).** `infra/aws/ec2/estate-report-runner/estate_report_runner.py:58-60` (env `ESTATE_KIMI_SECRET_ID/URL/MODEL`, daily exec summary); `infra/aws/lambda/investor-reporting/intake/resolution_kimi.py:20` (`MODEL = "kimi-k3"`); secret name `astn/kimi/api-key`, endpoint `https://api.moonshot.ai/v1/chat/completions` (`infra/aws/ec2/bd-cot-auto-login/bd_49f_auto_login.js:64`). Andrew's "already in use" holds. UNREAD: where the `ESTATE_KIMI_*` values are set. Egress still needs Andrew's per-use word (CLAUDE.md, Agent Autonomy).
2. **A Graph mail delta client already exists (READ).** `infra/aws/lambda/investor-reporting/intake/graph_client.py` (secret `irpt/graph/app-registration`, delta paging, 410 resync, scheduler 08:00-23:45 ET). It lives in the IRPT firm tree: it is a pattern to copy, not a module to import across pipeline trees. OPEN: its granted scopes and mailbox, which decide whether it contradicts Andrew's 2026-09-25 "skip a new registration".
3. **`outlook` and `sharepoint` are not registry rows (READ, ABSENT in `infra/logic/registry/*` and `lib/opal_naming.py`).** `teams` (`systems.json:400`) and scope `transcripts` (`scopes.json:333-341`, `bucket_provisioned: true`) exist.
4. **The Bloomberg 9a model-weights table has no definition anywhere this seat searched (ABSENT: `integrations/bloomberg/`, `docs/architecture/`, `docs/briefs/`).** It is PRD-001 Q3, owner Andrew.
5. **PRD-001's `record_id` is a per-mailbox key (READ, PRD-001 section 8).** See item 3.

## 1. Silver PII wipe: spec and test

**What is PII here (PROPOSED).** Four surfaces: (a) body text and HTML, (b) headers (from, to, cc, reply-to, internetMessageId contains a host), (c) subject, (d) attachment names and PDF contents.

**Spec (PROPOSED).**
- Headers: silver keeps `sender_domain` only. No address, no display name. `internet_message_id` stays as a dedup key and is a Bronze/Silver-internal column (opaque, not shown to the serving layer).
- Subject and body: replace (i) every string on a CLIENT ROSTER, (ii) every email address, (iii) account-number patterns, (iv) salutation targets ("Hi <first name>", "Dear ..."), (v) phone numbers. Replacement token `[CLIENT]`, `[EMAIL]`, `[ACCT]`, `[NAME]`.
- Alyssa's scrub takes client names from the SUBJECT line only and strips account patterns (READ, hand-off 5.2). That leaves body-only names, salutations and addresses. The roster removes the dependence on the subject.
- Attachment names: hashed or class-labelled in silver (`attachment_sha256[]`, `attachment_kind`); the original name stays in bronze only.
- Sanitised HTML form: keep block structure (`p`, `br`, `b`, `li`, headings, table rows) because `classify.py` splits on those tags (READ: PRD-001 `src/classify.py`), and strip attributes, images, links and scripts. Wipe inside the tags, never before the classifier runs.

**OPEN (blocks the spec).** Where the client roster comes from and who maintains it. Nothing in the estate is a ready scrubber: the only candidate found is `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/pseudonymizer.py` (READ path only, contents UNREAD; a repo search of `lib`, `.tools`, `infra/aws/lambda`, `infra/aws/ec2` found no other). Recommendation: a roster derived from the firm's own client list, owned by Andrew, versioned as `pii_wipe_version`.

**Test (PROPOSED).** A leak test with PLANTED tokens: a synthetic message set carrying every class above (a roster name in body-only, in a salutation, in a quoted reply, in an attachment name, as an email address, an account number, split across an HTML tag boundary, in different case). PASS = zero planted tokens survive in silver; each miss is a named class. The test runs at every change of `pii_wipe_version`. It proves the classes the plant covers, not absence of PII; say so in the record.

**Gate.** Silver is not "real" and no gold body text leaves Opal until the leak test passes. Regardless of test result, the Kimi call needs Andrew's per-use word. The wipe is heuristic, so this brief recommends the first vendor call use only messages Andrew has read as sanitised.

## 2. Fetch rule and scope

**Test mailbox (Andrew's word).** `andrew@opalinvest.com`. Never Alyssa's mailbox in the test.

**Rule (PROPOSED, keyword-free, from the hand-off).** For a fixed date window, list every message in the folders that hold commentary threads, then add every other message of each `conversationId` touched (needed for `approved` and PDFs). Land all of it in bronze; `classify.py` decides relevance downstream, never the fetcher.

**Scope decisions this brief recommends.**
- Folders: Inbox and Sent Items of the test mailbox, by folder-and-date LIST, not search (MEASURED in the hand-off: gateway search rejects quoted phrases and is fuzzy). OPEN: whether the gateway's list tools accept a folder and a date range; if not, the puller is a Lambda on Graph directly, which is the auth question below.
- Senders: not filtered at fetch. Both domains `@opalinvest.com` and `@49financial.com` appear as Manav's sender domains (MEASURED, hand-off 5), so a domain filter at fetch would lose half.
- Window: from 2026-03-01 (PRD-001 backfill start, READ) to the run date; then a daily delta.

**Path from test to production (OPEN, Andrew's security call).**
- Test: delegated read as Andrew through the gateway.
- Production: a scheduled pull needs an identity with no person present. The gateway holds delegated tokens only; its token broker refreshes silently but raises `NeedsLogin` when the refresh fails (READ: `infra/aws/ec2/opal-gateway/app/token_broker.py:171-183`), so an unattended run depends on a prior interactive sign-in and its lifetime is NOT measured. The alternative is an application permission (PRD-001's Mail.Read app-only, which Andrew told Alyssa on 2026-09-25 to skip because it is tenant-wide) or a scoped mailbox policy.
- Recommendation: put the decision to Andrew as ONE card with the two routes and their blast radius, and do not build the production pull before it. The test pull and bronze landing do not depend on it.

**Owner of the daily job.** OPEN (hand-off section 10: the commentary pull owner). PRD-001 puts the Graph rail with Andrew (READ, PRD-001 section 9/owners).

## 3. Dedup and identity

- **Defect in PRD-001's key (READ + reasoning).** `record_id` is "a hash of the Graph message id". The Graph `id` is per-mailbox, so a message that sits in Andrew's, Manav's and Alyssa's mailboxes has three ids and would land as three records. Silver dedups on `internetMessageId` (hand-off 5.3). Recommendation: `record_id = sha256(internetMessageId)`; the Graph `id` and mailbox go in the bronze sidecar only. A change to `record_id` is a shape change: a major bump under PRD-001 section 9 (see item 8).
- `internetMessageId` is absent on some drafts. PROPOSED fallback: hash of (sent_at, from-domain, subject_clean, body hash), flagged `id_source=fallback`.
- Replies and forwards carry their own `internetMessageId` and are distinct records; the reply chain inside the body is cut for `body_text` (field 2) but stays in bronze.
- `conversationId` groups threads and can differ across mailboxes for the same message; do not use it as a dedup key, only for thread reconstruction (item 5).
- Test: land the same message from two mailboxes in the fixture and assert one silver row and two bronze sidecars.

## 4. Attachments

- **Bronze (PROPOSED).** PDFs stored raw, byte for byte, with `sha256`, size, `attachment id`, parent message id in the sidecar. Same rule as the .pptx in FWD-6.
- **Holdings parser (field 6).** NEW work (READ: PRD-001 says extraction is not built; only `classify.py` exists). Recommendation: NOT a round-1 gate. Gold ships `holdings` nullable with `finder_status`; the parser is an enrichment with its own acceptance (holdings recovered from N sample PDFs versus a hand-keyed set Alyssa supplies).
- **Spreadsheet fallback.** `Y Charts\49 Requests` (hand-off). OPEN: whose drive and whether a fetcher can read it; do not depend on it until located.
- PDFs may carry client names: bronze only, two named readers (hand-off section 3). Silver stores names of nothing from the PDF except the holdings table after the parser exists.

## 5. The `approved` rule

**Rule (READ from PRD-001; PROPOSED tightening).** A LATER message in the same `conversationId` from Manav starting "Looks good" / "Good to go" / "Approved".

**False positives and their handling (PROPOSED).**
- "Looks good, but change X": approval with a change request. Rule: the approving clause must be the whole first unquoted sentence, and no later sentence in the same message contains an imperative or "but"/"however"/"change". Otherwise `approved = unknown`.
- Someone other than Manav says "Looks good": sender is checked against a named approver list (the list is Andrew's).
- Quoted text: the approval string sits inside a quoted earlier reply. Rule: read only the unquoted top of the message (same cut as field 2).
- Approval of a different draft in a long thread: `approved` binds to the LATEST draft before the approval message; store `approved_by_message_id` and `approved_at` so a human can check.
- Make it tri-state (`true / false / unknown`) rather than boolean; the few-shot slicer takes only `true`.
- Test: a labelled set of threads with known approvals from Alyssa (her `labels.csv` is on her machine only, READ hand-off 2); until it is shared, the test is the synthetic set of the classes above. OPEN: Alyssa must supply or run the comparison.

## 6. `model_snapshots` source (PRD Q3)

- **State.** The Bloomberg 9a table has no definition (ABSENT, scope in section 0). READ: the daily models leg writes pickles `data/model YYYYMMDD v1.pkl` (`integrations/bloomberg/pipeline/README.md:89`) with no parquet table defined for them; the nearest weight artifact is model AUM weights in `yang-generate-positioning/lambda_function.py:2216-2225`.
- **Two definitions of `model_as_of` conflict (READ).** SCHEMA_v2: the model-data date printed on the YCharts PDF, joined to a new `model_snapshots` (tech %, duration, yield, top holdings). PRD-001: the date of `sent_at`, joined to `model_weights` (the Bloomberg pull stored raw). PRD-001's 9/23 decision "not from backfilling YCharts PDFs" supersedes SCHEMA_v2.
- **Recommendation.** Adopt the PRD-001 definition, name the table `model_weights` (SCHEMA_v2's `model_snapshots` is the older name), key `(model_code, as_of_date)`, join `as_of_date <= date(sent_at)` (latest on or before, not equal, because a send can fall on a non-trading day; trading-day frontier is `lib/trading_calendar.py`).
- **Not a round-1 gate.** Ship `model_as_of` nullable; the source and history depth (does it reach 2026-03) are Andrew's answer to Q3. This brief does not invent the shape.

## 7. Field naming and freeze

- Field 3: `yc_variant` (PRD-001, its mock JSON, its code) over `model_variant` (SCHEMA_v2, which is older). Recommendation: `yc_variant`, and SCHEMA_v2 gets a note that it is superseded.
- Count: SCHEMA_v2 is titled "9 + an id" but section 8 adds field 10; PRD-001 section 8 lists `record_id` plus ten numbered fields. Use the PRD-001 list: `record_id`, `sent_at`, `body_text`, `yc_variant`, `models_referenced`, `account_type`, `holdings`, `mention_rate`, `themes`, `approved`, `model_as_of`, plus `finder_status` (gold-only, from `classify.py`).
- `themes` is `{theme, client, model}` in both documents (READ).
- Freeze (READ): PRD-001 section 9, Andrew signs off the section 8 fields; a shape change after that is a major bump with a changelog note, told to the other side first. Recommendation: the L4 PRD cites the section 8 hash, not its prose, and the freeze is a file signed by Andrew, not a chat statement.
- Nullable-until-source: `holdings`, `model_as_of`, `approved` may be null/unknown at first run without breaking the freeze; say that in the contract so a null is not a schema violation.

## 8. Ownership boundary with PRD-001

- **Split (READ, PRD-001).** Alyssa: the front end and the finder rules. Andrew: the back end, the Graph rail and storage.
- **What TRNSPT changes in PRD-001 and how each PRD-001 open question resolves:**

| PRD-001 Q | TRNSPT answer | State |
|---|---|---|
| Q1 mailboxes | test = Andrew's; production OPEN | OPEN (item 2) |
| Q2 Graph app registration | Andrew told Alyssa 2026-09-25 to skip; gateway route | OPEN (item 2 auth) |
| Q3 Bloomberg 9a table | no definition found | OPEN, Andrew (item 6) |
| Q4 S3 JSONL or DynamoDB | parquet at silver and gold, raw JSON/PDF in bronze | Andrew ruled 2026-09-30 |
| Q5 rules on unseen emails | acceptance in item 5.4 of the hand-off | Alyssa, before backfill |
| Q6 alert destinations | none: standing alert moratorium (CLAUDE.md section 5) | closed by the moratorium |
| Q7 design guidance | not this project's | Andrew/Austin |

- Q4 and Q6 answers change PRD-001's storage and run-alert plan, and Q2 changes its fetch plan. Under PRD-001 section 9 each is a major bump. Recommendation: a one-page RECONCILIATION note, signed by Andrew, acknowledged by Alyssa, listing the PRD-001 sections that TRNSPT overrides. Alyssa's product stays hers; the storage and fetch are TRNSPT's.
- `commentary.jsonl` (PRD-001) is replaced by bronze JSON + silver/gold parquet. `review.jsonl` and `errors.jsonl` become partitions or a `finder_status` column; the errors file is a data record, not an alert.
- PRD-002 (earnings notecards, v2.1) has no commentary ingestion, no mail read, no market-update pipeline (READ). Shared plumbing only: the gateway, S3, an internal audience; one shared dependency: PRD-002 reads `positioning_data.json` in the platinum tier of `opal-data-portal-v2`. UNVERIFIED whether that is the same source as the Q3 weights.

## 9. FWD-6 market updates

- **Canonical source (READ from the hand-off, MEASURED 2026-09-29/30 by the CTO).** SharePoint site Opal Capital, `Shared Documents/Market Update` (1 deck today). Archive: about 48 decks 2024-08-19 to 2025-12-08 in Andrew's OneDrive (one bulk copy 2025-12-01). This seat did not re-measure either.
- **Recommendation.** SharePoint folder = the live source; the OneDrive archive is a one-time backfill source landed under a distinct source marker in the sidecar, so the two are never conflated as one stream.
- **Identity.** File hash: the Graph `quickXorHash` (recorded by the CTO for the July deck) plus a `sha256` computed at landing on the received bytes, both in the sidecar. A re-saved copy differs in bytes but shares title and near-date: treat identical `sha256` as "same deck" and record a same-title-different-hash as "re-saved of X" in the sidecar, not as a new deck by default. FWD-6's accept line ("a re-saved copy is recognisable as the same deck") needs that pointer; the rule for how similar counts as a re-save is OPEN and small.
- **Generator under `Documents/Desktop/ajb_workspace/tools/market_update/`.** Prior art for later tiers (style guide, corpora); NOT in scope for bronze. Do not import it. UNREAD by this seat.
- **Not searched (carried from the addendum).** Opal Trade Submissions, Opal Consulting, Opal CIO Office for 49 Financial, 49 Financial Internal for market updates; the CTO's search of Opal OCIO found none.
- **Trigger.** A schedule on the folder listing (delta by `lastModifiedDateTime` and hash), since it is a weekly-ish manual drop; no notification subscription is claimed.

## 10. Registry rows, names and the moratorium

- **Rows to add before any path is real (READ procedure).** Add `outlook` and `sharepoint` to `infra/logic/registry/systems.json` with `key`, `class`, `long`, `owner_directive` (D9), `owner_claim`, `owner_basis`; run `python lib/opal_naming.py validate`. `address()` refuses an unregistered source (`lib/opal_naming.py:1701-1704`). Registry rows belong to the LGIC canon lane; the CTO L3 registers them and the L4 PRD cites `address()` output for every path and `name()` for every resource (CLAUDE.md rule 30). This brief types no path as a real one.
- **Shape of the addresses (PROPOSED, to be replaced by builder output).** `s3://opal-data-transcripts/outlook/transcripts/bronze/analysis_commentary/date=YYYY-MM-DD/` and `.../sharepoint/transcripts/bronze/market_update/date=.../`. Table names snake_case `analysis_commentary`, `market_update` (Andrew wrote hyphens; the grammar is snake_case, READ in the L1 brief finding 3).
- **Silver and gold homes.** The parquet tiers use `{table}/date={D}/` (READ `docs/doctrine/CLAUDE_ANNEX.md:436`). There is NO shared tier-writer in `lib/` (READ, ABSENT): each pipeline writes its own with pyarrow, so the PRD names the schema module and does not assume a shared writer.
- **Moratorium (READ `docs/architecture/MDPF_DEBTCLEAN_PRD.md` section 11; CLAUDE.md section 5).** A daily pull is a route, allowed. It must NOT add a failure alarm, SNS/SES send, freshness checker, health report or monitor, and must be scheduled on its own clock, not "success of upstream" as the only trigger. The O4 gap record is a data table of what is present and missing, not a notification. Any alert PRD-001 Q6 wanted needs Andrew's explicit word.
- **Bucket access.** The bucket has two named readers (L1 brief O8): PII in bronze (client names in threads and PDFs) means the commentary bronze table inherits that rule. A pipeline role that writes is a third principal to be named in the PRD; the writer cannot be a reader by accident.

## Recommended shape of round 1 (for the CTO's decomposition)

1. Registry rows for `outlook` and `sharepoint` (item 10).
2. Bronze landing from Andrew's mailbox for one fixed window, plus conversation expansion, plus the sidecar (items 2, 3, 4).
3. Silver with the wipe and its planted-token test (item 1) as the gate.
4. Gold first run on the PRD-001 fields with `holdings`, `model_as_of`, `approved` allowed null/unknown (items 4-7).
5. Reconciliation note with PRD-001 (item 8).

Not round 1: production auth, the PDF holdings parser, the Kimi serving Lambda (needs Andrew's per-use word and a passed wipe test), the market-update backfill.

## Calls waiting on Andrew (minimum set)

1. Production mailbox and identity route (stored delegated sign-in versus application permission), and the mailbox scope.
2. Client roster owner for the PII wipe.
3. PRD-001 Q3: the weights source and history depth.
4. Sign the section 8 field freeze and the PRD-001 reconciliation note.
5. Per-use word for the first hosted-model call.
6. Approver list for `approved` (Manav only, or more).

## What this brief does not claim

- It did not read `resolution_kimi.py` or `graph_client.py` beyond the cited lines, nor the pseudonymizer.
- It did not measure any mail count, token lifetime, or gateway list-tool capability.
- It did not verify the 70-of-70 fixture claims (fixtures are on Alyssa's machine).
- It did not read the market-update generator or search the sites listed above.
- No `search` was run for "kimi" across secrets stores beyond names in Terraform and `.scratch`; secret values were never read.
