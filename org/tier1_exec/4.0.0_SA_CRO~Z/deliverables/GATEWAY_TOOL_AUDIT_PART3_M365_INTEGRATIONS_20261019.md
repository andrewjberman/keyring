# Gateway tool-call audit, part 3: Microsoft 365 and integrations (and the outage between parts 2 and 3)

**Author:** 4.0.0_SA_CRO~Z, 2026-10-19 ~19:1xZ (3:1x PM ET). **Order:** Andrew-direct ~16:2xZ, record @634d368d98.
**Parts 1-2:** @216dfc8144, @48c5806982. **Outage row:** NFRA_OPLGTW-Z-S420 @28d8c7e3f1.

**Instrument.**
- Live calls through the served gateway (opalgateway MCP, Andrew@), 18:57Z-19:1xZ, after the gateway recovered.
- One call at a time, on 2.0.0_SA_COO~O's instruction (msg 36075), with the smallest page each tool allows.
- No message, file or person content is reproduced here; only counts, shapes and verdicts.
- Send and write tools were called only where a guaranteed no-send path exists. None qualified, so none was called.

## 1. Answer first

**The outage.** The served gateway was down for every user from about 17:30Z to 18:51Z (1:30-2:51 PM ET).
- Measured by 2.0.0_SA_COO~O (msg 36075): the service sat at MemoryCurrent 1.28 GB against MemoryHigh 1.26 GB on the
  t4g.small host, with the process at 1.41 GB RSS.
- A restart cleared it to 85 MB.
- Not separated: whether part 2's unbounded replies (743 KB, 585 KB), COO~MI's six parallel runners, or both pushed it
  there.
- Andrew's word: a resize to t4g.large follows the 19:00Z session.
- Z-S420 stays ARMED until the resize is read back.
- **The audit's own lesson: a tool with no size cap is a load risk to the host, not only to the reader.** The P4-P7 fix
  (Z-S413) is now also an availability fix.

**Part 3 denominator: 54 tools.** That is the 42 Microsoft 365 tools plus 12 integration tools. Together with parts 1-2
it covers every tool the served gateway lists; part 3b compared the full tool list against parts 1-3 and found none left.

| Group | Tools | PASS | of which a caveat | FAIL | Correct refusal | NOT RUN |
|---|---|---|---|---|---|---|
| Microsoft 365 | 42 | 30 | 2 oversize | 0 | 1 | 11: 8 with no guaranteed no-send path, 3 with no input at hand |
| Integrations | 12 | 8 | 4 | 2 | 1 | 1 (the upload, a write) |
| **total** | **54** | **38** | **6** | **2** | **2** | **12** |

## 2. Microsoft 365 (42)

**PASS (30):**
- **Mail:** whoami, list_recent_email, list_email_filtered (paged token), search_email, read_email, list_email_attachments,
  inspect_email_attachment.
- **Calendar and OneDrive:** list_calendar, list_onedrive, get_item, search_files (**75.9 KB, no result cap**), read_file,
  read_workbook.
- **SharePoint:** find_sharepoint_site, list_site_drives, list_site_files (pages at 100), search_site_files
  (**80.9 KB, no result cap**), get_site_item, profile_site_file, read_site_file, read_site_workbook.
- **Documents:** read_document (returns the PDF rendition size only; no text, by design).
- **Teams:** list_teams, list_chats, list_channels, read_chat_messages, read_channel_messages.
- **Meetings:** find_online_meeting, list_meeting_transcripts (7 rows), read_meeting_transcript (byte-paged; total
  64,432 bytes and sha256 reported).

**Checks:**
- inspect_email_attachment and validate_ssavail_attachment report the same sha256 for one attachment.
- read_site_file returns the same leading bytes that profile_site_file samples.

**Correct refusal (1):** validate_ssavail_attachment, run against a PNG, answers FLAG STRUCTURE with every check named,
which is the right negative.

**NOT RUN (11):**
- **No guaranteed no-send path (8):** send_email, reply_email, create_draft, upload_text_to_site,
  save_email_attachment_to_site, copy_site_file_to_s3, send_chat_message, send_channel_message.
  - The two Teams sends gate their `confirm_required` on message reach inside `_run`, so a one-to-one chat may send
    without the preview step (tools.py:1749-1770).
  - That is a battery design point: FWD-24 needs a send tool with an always-preview flag before any send tool can be
    exercised.
- **No input at hand (3):** read_chat_message_images and read_teams_attachment had no sampled message carrying an
  inline image or attachment; list_shared_folder had no sharing URL.

## 3. Integrations (12)

| Tool | Verdict | Note |
|---|---|---|
| ycharts_freshness | PASS | session live, HTTP 200 |
| ycharts_search | PASS | DIVZ resolves |
| ycharts_snapshot_metrics | PASS, **defect Y1** | `^SPX` ytd_total_return 12.91 comes back keyed under `"None"`, not the symbol, so a multi-symbol answer cannot be attributed |
| ycharts_fund_series | PASS, verified, oversize | DIVZ 1,255 daily points 2021-10-18..2026-10-16; the 10-16 close 37.6179 equals the price in SmartX holdings (part 1); **59 KB, no cap** |
| ycharts_time_series | **FAIL (Y2)** | upstream HTTP 403; answers `points: 0, series: []` with no reason field |
| ycharts_risk_return_scatter | **FAIL (Y2)** | upstream HTTP 403; `series: []` with no reason field |
| graph_status | PASS | vintage 17:56:56Z, last swap 18:00:34Z |
| graph_cypher | PASS | 42 S3 buckets; the age line says the stitch source was built 2026-10-11 (8 days) |
| opal_asker_query | correct refusal, **observation A1** | a Cottonwood sender answers `asker_tenant_denied`: Cottonwood's mail tenant is not a registered partner tenant, so a Cottonwood asker can never be served. Correct to the registry; whether Cottonwood should be registered is Andrew's call |
| opal_data_refresh_status | PASS, **defect R1** | an unknown execution id answers `status: UNKNOWN, terminal: false` over an HTTP 404, so a caller told to "poll until terminal" polls forever |
| poll_addressed_teams_messages | PASS, **defect T1** | `top=2` returned 4 messages: `top` is not honoured |
| opal_data_refresh_upload | NOT RUN | a write even on dry_run (uploads into pending/) |

## 4. Defects (proposed owners; the CTO routes)

| Item | What | Proposed owner |
|---|---|---|
| Oversize (search_files, search_site_files, ycharts_fund_series) | three more uncapped replies, the same class as P4-P7 and a load risk to the t4g host | NFRA_OPLGTW, with Z-S413 |
| Y2 | ycharts_time_series and risk_return_scatter get 403 and answer an empty series with no reason | NFRA_OPLGTW (the YCharts integration); first read whether the 403 is an entitlement or an endpoint change |
| Y1 | snapshot_metrics loses the symbol key | NFRA_OPLGTW |
| R1 | data_refresh_status: an unknown id never reaches a terminal state | NFRA_OPLGTW |
| T1 | poll_addressed_teams_messages ignores `top` | NFRA_OPLGTW |
| Send tools | no always-preview path, so no battery can exercise them safely | NFRA_MCPINDEX FWD-24 design, with NFRA_OPLGTW |
| A1 | Cottonwood's tenant is not registered for asker answers | Andrew |

## 5. Bounds

- **Coverage.** One call per tool, smallest page.
- **Not exercised.** Paging beyond page 1, the full-text options, every send and write path.
- **Mail choices.** Mail reads used system notices, never client mail.
- **Teams reads.** The chat and channel reads touched one message each.
- **Writes.** Nothing was sent, written, uploaded or committed anywhere but this file.
