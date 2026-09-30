# HAND-OFF to 4.0.0_SA_CRO (base) -- NFRA_TRNSPT: commentary ingestion, tiers and schemas, for expansion before the PRD

**From:** 1.0.0_SA_CTO. **Date:** 2026-09-30 ~02:1xZ. **Project:** NFRA_TRNSPT (D9), owned by this laptop fabric
(record `ANDREW_DIRECT_20260930_001xZ_TRNSPT_THIS_FABRIC_EDICT_STAYS_IN_COO_STARTUP.md`). **Status: NOT REGISTERED, NO PRD.**
**Ask (one):** expand the ten items in section 9 to brief depth, so the CTO can write the L4 PRD and the L3 registration on solid ground.
**Andrew's words** for this hand-off and the tiering: `ANDREW_DIRECT_20260930_020xZ_TRNSPT_COMMENTARY_TIERS_KIMI_TEST_MAILBOX_HANDOFF_TO_CRO.md` (verbatim, same directory).
**Read first:** `docs/briefs/nfra-trnspt-opal-transcript-database-brief-20260929.md` (the ~T lane's L1 brief) and the endpoint
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_NFRA_TRNSPT_20260930.md` (FWD-1..9; DONE WHEN lines still unconfirmed by Andrew).
Claim classes: READ (seen in a file), MEASURED (a call I ran), PROPOSED (my design), OPEN (needs a ruling).

## 1. What Andrew ruled this session (verbatim in the record above)
- Bronze: agreed. Silver = typed, de-duplicated bronze in parquet with PII wiped. Gold = the first run of Alyssa's schema.
- Serving = a Lambda calling a hosted model API; Andrew proposes Kimi K3 ("already in use elsewhere in the estate": NOT VERIFIED by me).
- Test fetch mailbox = andrew@opalinvest.com (he is on the threads; avoids touching Alyssa's private mail).
- Analysis commentary (FWD-7) and market update (FWD-6) stay in this project's bronze; the PRD and registration wait for the CRO's expansion.

## 2. Where Alyssa's material is (READ)
SharePoint site "Shared" (`https://opalinvest.sharepoint.com/sites/Shared`), library Documents, folder `Product-Alyssa/`
(her sync path: `Opal Capital\Shared - Documents\Product-Alyssa\`). Site id
`opalinvest.sharepoint.com,9332c03f-2ad0-4b84-97fe-7bcd2c9cb90a,18b7f31c-c878-41ea-9b7e-0c103bcb5679`.
Contents: `README.md` (index), `FORMAT.md`, `MAP.md`, `AUTOMATION-INVENTORY.md`, `_conventions/`, `YCharts/` (24 MB),
`PRD-001_commentary/` (v1.1 draft, 2026-09-23), `PRD-002_earnings-notecards/` (v2.1, 2026-09-28; NOT READ by me).
PRD-001 holds `PRD.md`, `CHANGELOG.md`, `assets/SCHEMA_v2.md`, `assets/FINDER_REPORT_2026-09-23.md`, `assets/mock/commentary_record.json`,
`src/classify.py|features.py|evaluate.py`, `intake/` (Andrew's 9/23 Teams thread; a note that commentary is held back from advisors), `steps/01..06` (READMEs only).
**Not in the folder:** any mail-fetch script (`scripts/` is a stub README) and the `/yc-commentary` skill (it lives on her machine; NOT READ).
Her labeled fixtures (183 Graph messages, `labels.csv`, client PII) are on her machine only:
`C:\Users\AlyssaKeith\Claude Files\YCharts Commentary DB\fixtures\`.

## 3. Tiers (PROPOSED, per Andrew's definitions)
```
BRONZE  as received      s3://opal-data-transcripts/<source>/.../bronze/analysis_commentary/date=YYYY-MM-DD/
                         (path must come from lib/opal_naming.py address(); the source registry row is OPEN)
                         msg_<id>.json (Graph message, byte for byte) + attachments/*.pdf + sidecar (pulled_at, mailbox, sha256, run id)
                         JSON and PDF stay native: "as received" cannot be a re-typed table. PII lives here; two named readers only.
SILVER  typed, dedup'd   PARQUET, PII wiped. One row per unique message. Keys: internetMessageId (dedup across mailboxes) + conversationId.
                         Columns: message_id, internet_message_id, conversation_id, sent_at (UTC timestamp), sender_domain,
                         body_html_clean (see 5.1), subject_clean, attachment_names[], attachment_sha256[], has_pdf, bronze_ref, pii_wipe_version.
GOLD    Alyssa's schema  PARQUET. commentary_example = the 10 fields + finder_status; commentary_slice_key; model_snapshots (join).
SERVING Lambda           slice gold by (yc_variant, models_referenced, account_type, themes, approved=true, recency) -> few-shot examples
                         + system prompt (Alyssa's /yc-commentary text, a prompt asset) -> hosted model API -> draft to Alyssa.
```
Why parquet for silver and gold: enforced types, native nested types (themes as list of struct, holdings as list of string), estate consistency
(the estate tier-writer standard was NOT checked). At about 70 rows and 3 new per week speed is irrelevant. Alyssa's PRD says `commentary.jsonl`: the one plan to change.

## 4. Gold schema and derivations (READ from SCHEMA_v2.md; tier placement PROPOSED)
| # | field | derived from | note |
|---|---|---|---|
| - | record_id | hash of Graph message id | idempotency key |
| 1 | sent_at | sentDateTime header | UTC |
| 2 | body_text | HTML to text; cut reply chain and signature; client tokens to [CLIENT]; account numbers removed | PII rule too narrow, see 5.2 |
| 3 | yc_variant | 0 models=1, 1=2, 2+=3, computed from field 4 | SCHEMA_v2 calls it model_variant; PRD and mock say yc_variant |
| 4 | models_referenced | dictionary match on body and PDF file names | fixed dictionary of Opal model names |
| 5 | account_type | keywords in subject and body (IRA, Roth, 401(k), brokerage, trust, else household) | |
| 6 | holdings | holdings table in the YCharts PDF attachment; fallback the request spreadsheet in `Y Charts\49 Requests` | PDF parsing is NEW work |
| 7 | mention_rate | holdings named in body / count of holdings | |
| 8 | themes | bold headings in order plus first "X% versus Y%" per paragraph, as a list of {theme, client, model} | |
| 9 | approved | a LATER message in the same thread from Manav starting "Looks good" / "Good to go" / "Approved" | cross-message |
| 10 | model_as_of | sent_at date joined to `model_snapshots` (model, as_of) | needs the Bloomberg 9a model-weights table (shape OPEN, PRD Q3) |
| + | finder_status | keep / review / skip from classify.py | see section 5 |

## 5. Ingestion: what exists and what does not
**READ.** No fetcher exists. `classify.py` scores an already-fetched Graph-shaped message. keep = at least 2 theme sections (a heading from the theme
vocabulary followed by a paragraph of 150+ characters) AND the thread is YCharts-linked (mentions YCharts, stress test or multi-comp, or carries a PDF; a
Morningstar/X-Ray-only thread is excluded). review = the theme test passes without the link. skip = the rest. Her scored result (build set, an upper bound):
64 of 70 real write-ups kept, 6 in review, 0 lost to skip, precision 90.1%, recall of keep 91.4%. She got the 183 candidates by having Claude search her
mailbox with keyword terms; the terms and the mailbox are not recorded.

**MEASURED (2026-09-30, read-only, andrew@opalinvest.com via the gateway):**
(a) the gateway's mail search REJECTS quoted phrases (Graph 400 "An identifier was expected") and is fuzzy: a query for the heading words returned about 50 mixed
threads, so keyword search cannot be the deterministic identifier;
(b) Andrew's mailbox does see the commentary threads, dated 2025-11 to 2026-09, sent by Manav Shah from BOTH `@opalinvest.com` and `@49financial.com`, and by Alyssa and Yang Liu;
(c) the exact count of true commentary emails in his mailbox was NOT established. The probe surfaced client names into the CTO session; nothing was copied out.

**PROPOSED fetch rule (deterministic, keyword-free):** for the test mailbox, every message in a fixed date window from the folders that hold commentary threads
(scope OPEN, item 2 below), plus every other message in each `conversationId` touched (needed for `approved` and the PDFs). Land ALL of it in bronze. Relevance is
decided downstream by `classify.py`, never at fetch, so recall is not capped by a search query.

5.1 **Constraint.** The classifier reads HTML structure (`</p>`, `<br>`, `<b>` tags). Silver must keep sanitized HTML (or a block list) with PII removed inside it.
Converting to plain text before the classifier runs breaks it.
5.2 **Constraint.** Her scrub replaces client names taken from the SUBJECT line and strips account-number patterns. It does not cover names that appear only in the body,
salutations, or advisor and client email addresses. "PII wiped" needs its own spec and a test before silver is real.
5.3 **Dedup.** The same message sits in several mailboxes (Andrew is on the threads). Silver de-duplicates on `internetMessageId`, not the per-mailbox Graph `id`.
5.4 **Acceptance for the puller (PROPOSED):** over March to September 2026 the pull plus classify reproduces Alyssa's 70 labeled write-ups against `labels.csv`
(she must share or run the comparison; the labels are on her machine).

## 6. Auth route (OPEN; the security decision is Andrew's)
PRD-001 assumes a Graph app registration (app-only Mail.Read). Andrew told Alyssa on 2026-09-25 to skip a new registration (tenant-wide scopes) and use the Opal gateway.
The gateway holds delegated tokens only; its headless paths run under one fixed identity's server-held token. How long a stored token stays usable is NOT measured.
For the test, a delegated read as andrew@opalinvest.com is simplest. A scheduled production pull needs the fixed-identity route and Andrew's word on the mailbox scope.

## 7. Serving layer (PROPOSED)
A Lambda calling a hosted model API (Kimi K3 proposed by Andrew), with Alyssa's `/yc-commentary` text as a prompt asset (not a table). An external vendor call needs
Andrew's per-use word (CLAUDE.md, Agent Autonomy). The gold body text leaves Opal infrastructure to the vendor and the PII wipe is heuristic, so the wipe test in 5.2 gates
that call. Estate use of Kimi: NOT VERIFIED.

## 8. Market updates (FWD-6) -- READ, from the gateway on 2026-09-29/30
Canonical home since 2026-07: SharePoint site Opal Capital, `Shared Documents/Market Update` (1 deck: `Opal Market Update 7-27-2026 (from Manav).pptx`, 202,534 bytes,
quickXorHash `aBmLs6Y8SDB3LKH8eN+jRAwyAd0=`). Archive: about 48 decks 2024-08-19 to 2025-12-08 in Andrew's OneDrive (bulk-copied 2025-12-01), plus a generator under
`Documents/Desktop/ajb_workspace/tools/market_update/` (style guide; writing, analysis and bullets corpora). The 49F CIO Office site holds 6 April-June 2024 files
(5 PDF/PNG, 1 pptx). Sites searched with no hit: Opal OCIO, Opal Consulting, Trade Submissions, 49 Financial Internal.

## 9. Depth items for the CRO to expand (the ask)
1. **Silver PII wipe spec and test:** what counts as PII in body, headers and attachment names; the sanitized-HTML form (5.1); a leak test with planted names. Gates silver and the Kimi call.
2. **Fetch rule and scope:** which folders and date window; all Sent Items or defined senders; both domains (`opalinvest.com` and `49financial.com`); the path from the test mailbox to a production mailbox.
3. **Dedup and identity:** `internetMessageId` across mailboxes; forwards and replies; the PRD's `record_id` hash against this key.
4. **Attachments:** PDFs stored raw in bronze; the YCharts PDF holdings parser (new work); the spreadsheet fallback.
5. **`approved` rule** and thread reconstruction from `conversationId`; false-positive risk on "Looks good".
6. **`model_snapshots` source:** the Bloomberg 9a model-weights table shape and its history since March 2026 (PRD Q3); the join key.
7. **Field naming and freeze:** `yc_variant` against `model_variant`; the 10 fields against SCHEMA_v2's 9; when the contract freezes.
8. **Ownership boundary with PRD-001:** it remains Alyssa's product (front end) but its storage and fetch plans change; who signs the reconciliation (Andrew, Alyssa).
9. **FWD-6 market updates:** canonical source (SharePoint folder or OneDrive), identity by file hash, whether the OneDrive generator is prior art or in scope; and read PRD-002 for overlap.
10. **Registry rows and names:** sources `outlook` and `sharepoint` need rows before any path is real; every address from `address()`, every name from `name()` (CLAUDE.md rule 30). Check the daily-job design against the no-alerts moratorium.

## 10. State of the CTO's own work
Endpoint FWD-1..9 written, not confirmed by Andrew (`ENDPOINT_FORWARD_NFRA_TRNSPT_20260930.md` @19b4670). Register carriers (L3) and PRD (L4) are NOT started; they wait on
the CRO's expansion and Andrew's DONE WHEN confirmation. Open Andrew calls: the unattended Microsoft sign-in (gates FWD-1), the Research Meeting refusal cause (FWD-2),
the commentary pull owner.
