---
name: taxsma-step1
description: PFMG_TAXSMA step 1, the daily runner: pull the morning's FIS Short Sale Avail File attachments from the monitored mailbox into SharePoint TAX/Short Sale with Yang's exact naming, via the m365 gateway's server-side transfer. Every trading morning after ~7:00 ET, or on "run the tax sma step 1". Needs a write_files-entitled identity. Idempotent.
---

# /taxsma-step1 — Short Sale file intake (PFMG_TAXSMA step 1)

**Design of record:** `docs/briefs/PFMG_TAXSMA_S0.1_S0.3_close_20260714.md` (the ratified S0.3 rule)
+ `docs/briefs/ANDREW_BRIEF_20260714_taxsma_and_ticket_system.md` Part 1.
**Never:** overwrite an existing file (the tool physically cannot — `conflictBehavior=fail`);
silently drop or silently rename an unexpected extra send; write anywhere but `TAX/Short Sale`.

## Constants

- **Site:** "Shared" — `find_sharepoint_site("Shared")` →
  `opalinvest.sharepoint.com,9332c03f-2ad0-4b84-97fe-7bcd2c9cb90a,18b7f31c-c878-41ea-9b7e-0c103bcb5679`
  (re-resolve if the id ever misses; do not hardcode-trust across tenants).
- **Target folder:** `TAX/Short Sale` (default document library).
- **Source emails:** subject `Short Sale Avail File`, FIS sender `SmartLoan9990@fisglobal.com`,
  arriving as Yang's auto-forwards (from `yang@opalinvest.com`) in the connected user's mailbox.
- **DATE:** today's `YYYYMMDD` in **ET** (the FIS sends are ET-morning; do not use UTC date after 8 PM ET).

## Steps

1. **Find today's emails:** `search_email("Short Sale Avail File", top=10)` and keep messages whose
   `receivedDateTime` falls on DATE (ET). Expect 2 on a normal morning. 0 → report NO-FILES (a
   holiday/weekend is normal — check the trading calendar before calling it a failure). 1 → proceed
   but flag PARTIAL (the second may not have arrived yet; re-run later).
2. **Attachments:** for each message, `list_email_attachments(message_id)`. Expect exactly one
   non-inline attachment each, `.ASC`, ~10-15 MB. **Log the attachment names verbatim** — the first
   run byte-confirms the S0.3 name hypothesis (SSAVAIL1/SSAVAIL2-style self-identifying bases).
3. **Map PRELIM vs FINAL (the S0.3 rule, in order):**
   a. **Attachment-name primary:** if the base names differ in a self-identifying way (e.g.
      `SSAVAIL1` vs `SSAVAIL2`, or an explicit prelim marker), map by name.
   b. **Time fallback (names identical):** FIS send time (from the forwarded header block in the
      body, or receivedDateTime − ~4 min) **before 6:00 ET = PRELIM**; first send ≥ 6:00 ET = FINAL.
   c. Beyond the mapped pair: EXTRA (see step 5).
4. **Save both files** with `save_email_attachment_to_site`:
   - PRELIM → `{base} {DATE} PRELIM{ext}` (e.g. `SSAVAIL1 20260715 PRELIM.ASC`)
   - FINAL → `{base} {DATE}{ext}` (e.g. `SSAVAIL2 20260715.ASC` — must match Yang's kept pattern)
   - `folder_path="TAX/Short Sale"`, site id above. Record each returned `sha256` + `bytes` + item id.
5. **Extra sends (the 07-10 case):** any 3rd+ email/attachment saves as
   `{base} {DATE} EXTRA-{n}{ext}` AND is reported loudly in the run summary (never silently mapped
   to FINAL). If a name collision errors (`conflictBehavior=fail`), that IS the re-run/duplicate
   signal — report it, do not work around it.
6. **Verify:** `list_site_files(site_id, "TAX/Short Sale")` — confirm the new items by name + size
   (listing-based acceptance, matching the landing-verification house rule).
7. **Report** (chat + broker summary; on failure also MCP `0.5.0_AE_OpalETL`): DATE, emails found,
   attachment names verbatim, mapping used (name-based vs time-fallback), files written
   (name/bytes/sha256), extras/collisions, verification listing result.

## First-run addendum (still open as of 2026-07-14)

- The first live run **closes the S0.3 name hypothesis**: record the actual attachment base names
  into `docs/briefs/PFMG_TAXSMA_S0.1_S0.3_close_20260714.md` (append a dated confirmation line).
- Backfill question for Yang (surface once, via Andrew): whether to backfill missed dates between
  his last manual save and go-live (mail history has the attachments).
