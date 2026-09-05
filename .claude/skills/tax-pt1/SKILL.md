---
name: tax-pt1
description: OPAL_TAXSMA part 1, the daily runner: pull the morning's FIS Short Sale Avail File attachments from the monitored mailbox and file them into SharePoint TAX/Short Sale with Yang's exact naming, via the m365 gateway's server-side transfer. The trigger is the `/tax-pt1` invocation itself, every trading morning after ~7:00 ET. Idempotent: a re-run never overwrites.
---

# /tax-pt1 — Short Sale file intake (OPAL_TAXSMA part 1)

**Scope rulings (Andrew-direct 2026-07-14, ADDENDUM 2 of the ~A ANDREW_DIRECT TO):** this intake
is the project's principal automation; step-5 trade-file conversion is DESCOPED for now.
**[RETRACTED 2026-07-16] the original clause "step-2 cost-basis stays MANUAL / not derivable in-estate
(ULN/ACC negative on the record)" is FALSIFIED** -- S0.1 tested `opal-data-schwab`/0824 ONLY; all 3
Tax SMA accounts ARE in the 0833 master (`schwab/08335338/`, fact_acc 1/1/1, DT 07-16), so step-2 IS
derivable and is BUILT as `/tax-pt2` (agent-run @77a523510). The "ULN negative" read the WRONG table:
Tax SMA lots ride `fact_ult`, not `fact_uln` (0 ULN rows). Future parts land as /tax-pt2 (built),
/tax-pt3 (converter runner), ...

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
3. **VALIDATE every attachment BEFORE any save (Content Contract v1.0 — Andrew-direct #8;
   requires the 2026-07-15 validator gateway deploy):**
   a. Compute the expected as-of = PRIOR TRADING DAY of DATE via the estate's ONE calendar.
      **EXACT RECIPE (pinned 2026-07-15 — `expected_last_trading_day(D)` INCLUDES D itself,
      so pass D minus one day):**
      `python -c "from lib.trading_calendar import expected_last_trading_day; from datetime import date, timedelta; print(expected_last_trading_day(date(YYYY,M,D) - timedelta(days=1)).strftime('%Y%m%d'))"`
      (corpus-verified incl. Monday-over-weekend and holiday cases; never hand-compute).
   b. For each attachment: `validate_ssavail_attachment(message_id, attachment_id,
      expected_asof=YYYYMMDD)` → verdict PASS | FLAG with per-check results (C1 fixed-width /
      C2 ascii / C3 header / C4 as-of / C5 trailer-tie / C6 records / C7 volume envelope /
      C9 warn). Contract: `docs/briefs/OPAL_TAXSMA_SSAVAIL_CONTENT_CONTRACT.md`. Known classes:
      STUB (404B, trailer==2) and TRUNCATED-VALID (trailer TIES but volume ~22% of envelope —
      the checksum lies; only C7 catches it).
4. **Map + route by verdict (the S0.3 rule on PASS files only):**
   a. **Attachment-name primary:** `SSAVAIL` vs `SSAVAIL2` (the confirmed live pair) — first
      PASS send of each base takes the canonical name:
      PRELIM → `{base} {DATE} PRELIM{ext}` · FINAL → `{base} {DATE}{ext}`
   b. **Time fallback (names identical):** FIS send < 6:00 ET = PRELIM; first ≥ 6:00 ET = FINAL.
   c. **FLAG files** → `folder_path="TAX/Short Sale/Flagged Files"`, name
      `{base} {DATE} FLAGGED-{flag_class}{ext}` (e.g. `SSAVAIL 20260710 FLAGGED-STUB.ASC`).
      NEVER canonical, NEVER silently dropped; every flag goes in the run report.
   d. **Extras:** a PASS re-send of an already-mapped base → `{base} {DATE} EXTRA-{n}{ext}`,
      loud. Re-sends are UPDATED SNAPSHOTS (07-10: +809 rows), never discard unseen; a small
      canonical + larger EXTRA needs Yang's adjudication, never a silent swap.
   All saves via `save_email_attachment_to_site`; record sha256 + bytes + item id (the sha256
   must MATCH the validator's — a mismatch means the attachment changed between validate and
   save: STOP and re-run).
5. **Collisions:** `conflictBehavior=fail` — a name collision IS the re-run/duplicate signal;
   report it, never work around it.
6. **Verify:** `list_site_files` on BOTH folders (`TAX/Short Sale`, `TAX/Short Sale/Flagged Files`)
   — listing-based acceptance by name + size.
7. **Report + shared-cloud log (Andrew-direct #8):**
   a. Chat + broker summary: DATE, emails, verdicts per attachment (verbatim flag_reasons),
      mapping, files written (name/bytes/sha256), flags/extras/collisions, listing result.
   b. Write the run log via `upload_text_to_site` →
      `TAX/Short Sale/Intake Logs/{DATE}-{HHMMSS}Z intake-log.md` (timestamped = never collides;
      newest file IS latest). If ANY flag: also write
      `{DATE}-{HHMMSS}Z flag-report.md` there — the compiled flagged-features report (file,
      flag_class, failing checks, sizes, sha256s, disposition).
   On failure at any step: MCP note to `0.5.0_AE_OpalETL` as well.

## Cadence (Andrew ruling 2026-07-15: "Yes B now, we will do A later.")

- **Option B (LIVE): operator-cadence.** This skill IS the daily runner — Alyssa or Andrew invokes
  **/tax-pt1** every trading morning (the slash command is the interface). Primary run: **after ~7:00 ET** (both normal sends in by
  6:47). **If ANY attachment FLAGs or the pair is incomplete: re-run after ~9:00 ET** — the
  corpus shows FIS corrections arrive 8:10–8:20 ET on bad-send days; re-sends are updated
  snapshots. Collisions on the re-run are the already-filed signal, not errors.
- **Option A (DEFERRED): scheduled-autonomous** (EventBridge → server-side runner). Revisit
  after the validator has run live for a week or two; the orchestration port inherits this
  skill's flow verbatim.

## First-run addendum — CLOSED 2026-07-15 (first live run GREEN, Andrew observing)

- S0.3 names byte-confirmed with correction (`SSAVAIL`/`SSAVAIL2`, not SSAVAIL1/2); dated
  confirmation appended to `docs/briefs/PFMG_TAXSMA_S0.1_S0.3_close_20260714.md`.
- Scope proof: upload rides consented `Files.ReadWrite.All` alone (no Sites.ReadWrite.All, no IT ask).
- STILL OPEN (surface once, via Andrew): (a) backfill Yang's missed dates (last manual save 06-25 →
  go-live; mail history has the attachments); (b) Yang's practice keeps FINALs only on sparse dates —
  spec says save both daily; automation follows the SPEC until Yang/Andrew says otherwise.
