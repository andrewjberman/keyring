# PFMG_TAXSMA — S0.1 + S0.3 discovery CLOSE (grounded, 2026-07-14)

**Author:** 0.5.0_AE_OpalETL~A (Andrew-direct execution delegation ~19:30Z, recorded in the ~A ANDREW_DIRECT
TO addendum). **Method:** live primitives only — Graph reads via the OPLMCP gateway ~19:2x-19:3xZ, S3 pulls
of the actual silver parquets. S0.2 was already COMPLETE (2026-06-29, converters canonical).

---

## S0.1 — the step-2 cost-basis lever: VERDICT = NOT A LOOKUP (the data is not there)

**The 3 live Tax SMA accounts** (from `Tax SMA Accounts.xlsx`, SharePoint site "Shared" /TAX, item modified
2026-07-14T13:28Z — read live via Graph Workbook API; Traded=Yes rows):

| Index | Account | Client | Strategy | Advisor |
|---|---|---|---|---|
| 1 | 2726-5115 | Chiles, Colby & Nicole | SMA 200 | Mitchell Roper |
| 3 | 3594-0058 | Bump, Dan & Kim | SMA 145 | Dean Dillenberg |
| 5 | 9193-9812 | Macy, Vincent | SMA 145 | Tim Rodgers, Luke Heiligenthal |

(2 more accounts on the master, Traded=No. Advisors are 49 Financial people — which made CRS-membership
a live hypothesis worth testing, not assuming either way.)

**Membership test — NEGATIVE on two tables, two axes:**
- `s3://opal-data-schwab/silver/ULN/date=20260508/data.parquet` (the latest partition; 226,608 lot rows,
  3,690 accounts, `account_id` zero-padded 10-digit): digit-normalized exact AND endswith matches for
  27265115 / 35940058 / 91939812 = **0 / 0 / 0**.
- `s3://opal-data-schwab/silver/ACC/date=20260508/data.parquet` (6,897-account master): same numbers **0**,
  AND taxpayer-name axis CHILES / BUMP / MACY = **0 hits**.
- Timing control: Chiles + Bump incepted 2026-04-08 — they EXISTED for a month before the 05-08 partition
  and are absent, so absence is membership, not vintage. (Macy incepted 06-05, after the partition —
  its absence alone would have been inconclusive; that is why the verdict rests on the other two.)

**VERDICT:** the CRS delivery covers the 49F RPS custody universe; the Tax SMA accounts are a different
Schwab relationship and are NOT in `opal-data-schwab`. **Step-2 cannot be an S3 lookup today.** Also noted:
the existing silver is itself stale (latest partition 2026-05-08; the ingest is hand-run) — even a positive
membership would have needed a cadence fix.

**Step-2 paths forward (per the PRD's own ranking — extend-the-feed beats browser-automation):**
1. **PREFERRED, external-gated:** ask Schwab (via Yang/ops) to add the 3 Tax SMA accounts to a CRS
   delivery (the exact file family the estate already ingests + silvers). When that lands, step-2 collapses
   to lookup + format — the schema is ALREADY sufficient (ULN carries ticker / current_quantity /
   current_market_value / cost_per_share / acquired_date — every field the step-3 converter's
   CostBasis_Acct CSV needs). **This is a one-line ops request, zero new code class.** Needs Andrew/Yang.
2. Browser automation against the Schwab UI ("Export only lot level detail") — credential-bearing +
   brittle; only if (1) is refused. Its security design is CTO-gate material per the PRD.
3. **Interim (live today, unchanged):** step 2 stays the manual export it is today; steps 1/3/4-gate/5
   automation does not depend on it (the converter consumes whatever lands in `Tax Lot/YYYYMMDD/`).

## S0.3 — the PRELIM/final email rule: CLOSED (with a ground-truth correction to the spec's frame)

**Live feed characterization (Andrew's mailbox, Graph search 19:0xZ):** the FIS emails
(`SmartLoan9990@fisglobal.com`, subject "Short Sale Avail File") reach Andrew as **Yang's auto-forwards**
(~3-4 min lag at every hour incl. 5 AM — a mailbox rule, mechanical; recipients Manav/Menachem/Andrew/
Alyssa). Send-time pattern (ET): first ~5:01-5:03, second ~6:47, daily 07-08..07-14 — **and 07-10 had FOUR
sends (5:01, 6:47, 8:10, 8:14), so naive first/second arrival-order is NOT deterministic.**

**Ground truth from Yang's own Short Sale folder (SharePoint, listed live):** the kept artifact is
**`SSAVAIL2 YYYYMMDD.ASC`** (~10-15 MB), ONE per day, only on TRADE days (2026-04-06/07/08, 06-05, 06-24,
06-25 — exactly tracking the master file's inception/trade dates). **No " PRELIM"-suffixed file is kept at
all.** The `SSAVAIL2` base strongly suggests FIS's attachment names are self-identifying (SSAVAIL1 = prelim
file, SSAVAIL2 = final — Yang's saved name = attachment base + " YYYYMMDD"); to be byte-confirmed on the
first attachment-metadata read once the fetch capability lands (it is the first thing step-1 logs).

**THE RATIFIED RULE (step-1 implements exactly this):**
1. Enumerate the day's "Short Sale Avail File" emails in the monitored mailbox.
2. **Primary discriminator = ATTACHMENT NAME** (self-identifying base, e.g. SSAVAIL1/SSAVAIL2) — mapped
   PRELIM/final by name, arrival order ignored.
3. **Fallback (names identical/uninformative):** ET-send-time window — before 6:00 ET = PRELIM, first send
   ≥6:00 ET = final.
4. Renames per Yang's spec: PRELIM -> `{base} YYYYMMDD PRELIM{ext}`, final -> `{base} YYYYMMDD{ext}`.
5. **Any send beyond the mapped pair lands as `{base} YYYYMMDD EXTRA-{n}{ext}` + a human notification —
   NEVER a silent overwrite, NEVER silently dropped** (the 07-10 four-send day is the live case).
6. The FINAL file is the load-bearing artifact (matches Yang's own kept set).

## Consequences for the build (what this session now does)

- **Step-1 buildable NOW:** gateway gains `list_email_attachments` + `save_email_attachment_to_site`
  (server-side Graph transfer, mail-read + Files.ReadWrite.All — both INSIDE the already-consented
  envelope, no new Graph permissions; the 12 MB .ASC never rides the MCP channel). Then the step-1 runner
  applies the rule above. Acceptance: reproduce Yang's filing for a live day byte-for-byte (name + size).
- **Step-2:** ops request drafted to Andrew/Yang (path 1); manual export remains the interim; no code leg
  until the feed answer lands.
- **Steps 3/5:** cloud-stage pattern — pull `Tax Lot/{date}` + master from SharePoint to a staging dir,
  run the CANONICAL converters verbatim (BASE+date injected), push `Initial Holding/{date}` /
  `Trade/{date}` back. Step-4 = the waiting-on-Yang gate + Teams/mail notify.
- The trade file is GENERATED, never executed/uploaded — unchanged, non-negotiable.

---

## S0.3 CONFIRMED — first live /tax-pt1 run, 2026-07-15 (byte-grounded)

The attachment-name-primary hypothesis is CONFIRMED with one correction: the actual base pair is
**`SSAVAIL` (early send) / `SSAVAIL2` (late send)** — not SSAVAIL1/SSAVAIL2 as hypothesized.
Evidence (Graph, verbatim): 5:02:10 ET send carries `SSAVAIL.ASC` (12,694,603 attachment bytes);
6:47:41 ET send carries `SSAVAIL2.ASC` (12,934,383). Name rule and time-fallback agree. FINAL base
matches Yang's own kept files exactly (`SSAVAIL2 YYYYMMDD.ASC`, verified against his 6 manual saves
Apr 06 - Jun 25). First-run writes, listing-verified: `SSAVAIL 20260715 PRELIM.ASC` (12,694,286 B,
sha256 8cddb66c...fbe2d) + `SSAVAIL2 20260715.ASC` (12,934,060 B, sha256 6292e2e9...8988) in
TAX/Short Sale. Scope note: upload rode the consented `Files.ReadWrite.All` alone — no
Sites.ReadWrite.All needed, no IT ask (exercised, not inferred). Practice observation on record:
Yang's folder holds FINALs only, sparse dates — spec says save both; automation follows the spec
pending his word. Backfill question (last manual save 06-25 -> go-live) OPEN with Andrew/Yang.

## BACKFILL COMPLETE + STUB RULE ADDED -- 2026-07-15 (Andrew-direct, live session)

Backfilled all trading days 06-29 -> 07-14 (07-03 holiday correctly absent): 27 files saved,
listing-verified 35/35 in TAX/Short Sale. NEW EVIDENCE from the sweep: FIS has a RECURRING
BAD-SEND MODE -- ~404-byte error-placeholder attachments (06-30 BOTH sends, 07-01 early, 07-10
early; the two 06-30 stubs byte-identical sha256 98ea39e5...27ff), corrected by full-size
re-sends hours later. This is what the "extra sends" always were. RULE AMENDED (skill step 3.0):
<1 MB = STUB, never canonical, saved as "{base} {DATE} STUB.ASC"; canonical = first >=1MB send
per base; qualifying re-sends = EXTRA-n, loud. OPEN FOR YANG (one item): 07-01 FINAL ambiguity --
canonical SSAVAIL2 20260701.ASC is 2.9 MB (6:47 send, 4-5x smaller than every neighbor) while
SSAVAIL2 20260701 EXTRA-1.ASC (8:20 re-send) is 13.6 MB; rule kept the 6:47 canonical, flagged
not swapped. Also standing: the 06-26 18:03 batch (Yang bulk-forwarded ~15 Nov-Dec 2025 vintage
files while writing the spec) is historical sample material, NOT filed.
