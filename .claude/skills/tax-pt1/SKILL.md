---
name: tax-pt1
description: OPAL_TAXSMA part-1 daily runner (Andrew naming ruling 2026-07-14, "/tax-pt1; tax-pt2 etc as needed") -- pull the morning's FIS "Short Sale Avail File" attachments from the monitored mailbox and file them into the SharePoint TAX/Short Sale folder with Yang's exact naming (S0.3 rule). THE SSAVAIL EMAIL INTAKE/PARSING IS THE PRINCIPAL AUTOMATION ASPECT OF THIS PROJECT (Andrew ruling #2, 2026-07-14). Uses the m365 gateway's list_email_attachments + save_email_attachment_to_site (server-side transfer; the 10-15MB .ASC never rides the MCP channel). Run every trading morning after ~7:00 ET, or on demand ("run tax pt1" / "pull the short sale files"). Alyssa-operable: master AND standard tiers are write_files-entitled (standard granted on-box 2026-07-14 per Andrew ruling #4). Idempotent: conflictBehavior=fail means a re-run can never overwrite -- collisions are loud.
---

# /tax-pt1 — Short Sale file intake (OPAL_TAXSMA part 1)

**Scope rulings (Andrew-direct 2026-07-14, ADDENDUM 2 of the ~A ANDREW_DIRECT TO):** this intake
is the project's principal automation; step-5 trade-file conversion is DESCOPED for now; step-2
cost-basis stays MANUAL (no Schwab ask; the 3 accounts are not derivable in-estate — ULN/ACC
negative on the record). Future parts land as /tax-pt2, /tax-pt3, ...

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
   **Folder-agnostic by design:** Graph `$search` spans mail folders, so an Outlook rule filing the
   forwards into a dedicated subfolder (Andrew ruling #5 — welcome, recommended name "SSAVAIL")
   changes nothing here. Never key on folder location.
2. **Attachments:** for each message, `list_email_attachments(message_id)`. Expect exactly one
   non-inline attachment each, `.ASC`, ~10-15 MB. **Log the attachment names verbatim** — the first
   run byte-confirmed the S0.3 names (2026-07-15): early send = `SSAVAIL.ASC`, late = `SSAVAIL2.ASC`.
3. **Map PRELIM vs FINAL (the S0.3 rule, in order):**
   0. **STUB floor (added 2026-07-15, backfill-evidenced):** an attachment **< 1 MB is a STUB**,
      never canonical — FIS has a recurring bad-send mode delivering ~404-byte error placeholders
      (observed 06-30 x2, 07-01, 07-10; real files run 2.8-15.6 MB). Save as
      `{base} {DATE} STUB{ext}` and report loudly. Canonical mapping below considers only
      qualifying (>= 1 MB) sends.
   a. **Attachment-name primary:** if the base names differ in a self-identifying way (e.g.
      `SSAVAIL` vs `SSAVAIL2` — the CONFIRMED live pair — or an explicit prelim marker), map by
      name: first QUALIFYING send of each base takes the canonical name.
   b. **Time fallback (names identical):** FIS send time (from the forwarded header block in the
      body, or receivedDateTime − ~4 min) **before 6:00 ET = PRELIM**; first send ≥ 6:00 ET = FINAL.
   c. Beyond the mapped pair: EXTRA (see step 5). A qualifying re-send of an already-mapped base
      is EXTRA-n — flag it loudly (it is usually FIS correcting a bad earlier send; a suspiciously
      small canonical + a larger EXTRA needs Yang's adjudication, never a silent swap).
4. **Save both files** with `save_email_attachment_to_site`:
   - PRELIM → `{base} {DATE} PRELIM{ext}` (e.g. `SSAVAIL 20260715 PRELIM.ASC`)
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

## First-run addendum — CLOSED 2026-07-15 (first live run GREEN, Andrew observing)

- S0.3 names byte-confirmed with correction (`SSAVAIL`/`SSAVAIL2`, not SSAVAIL1/2); dated
  confirmation appended to `docs/briefs/PFMG_TAXSMA_S0.1_S0.3_close_20260714.md`.
- Scope proof: upload rides consented `Files.ReadWrite.All` alone (no Sites.ReadWrite.All, no IT ask).
- STILL OPEN (surface once, via Andrew): (a) backfill Yang's missed dates (last manual save 06-25 →
  go-live; mail history has the attachments); (b) Yang's practice keeps FINALs only on sparse dates —
  spec says save both daily; automation follows the SPEC until Yang/Andrew says otherwise.
