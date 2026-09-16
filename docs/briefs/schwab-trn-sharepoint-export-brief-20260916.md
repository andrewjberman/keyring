# BRIEF -- Schwab transactions to SharePoint: the first AWS -> SharePoint file movement

**Author:** `4.0.0_SA_CRO~G` | **Written:** 2026-09-16 (UTC) | **Mode:** NEW (no project exists; prior art only)
**Asked by:** Andrew, directly at this seat's terminal, after `1.0.0_SA_CTO` relayed his call-4 ruling (msg 97507,
record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260916_182xZ_RESERVED_GROUP_FOUR_CALLS_RULED.md`
@50d1b9403e).
**Consumer:** `2.0.0_SA_COO~G` (fold-in), or `1.0.0_SA_CTO` `/endpoint --forward` if a project is made (see s.8).

---

## ANDREW'S WORDS, VERBATIM (this terminal, 2026-09-16, ~3:0x-3:4x PM ET)

The ruling that created this seat's task (via 97507): *"We need to relegate this to a new agent for this session,
4.0.0_SA_CRO~G. I will discuss implementation with them and they can write the brief qualifying it for COO~G. I don't
think we really need to make a new project for this, will just fold it into the COO~G workflow, maybe even them just
handling it direct from me. Depends on how complicated the implementation is once I see the brief from CRO~G. If it
requires much consideration, we may create a new project for this, which will center around AWS -> Sharepoint file
movements as a patterned structure, with this case being the actual initial implementation."*

The five inputs: *"1.) Let's make an "AWS" folder, I'd prefer it on the main Opal sharepoint the one that has the bulk
of the content. We can also discuss naming nomenclature/path structure based on LGIC_NAMING 2.) For now, just Schwab
0824 and 0833. 3.) I think we can probably manage these ones quarterly (depends if there is more than 16k transactions
in a quarterly period, might have to be monthly depending. 4.) Initially just Menachem, menachem@opalinvest.com, but we
will wait for that as I need to make sure it works successfully for a few days and info is clean and clear first. 5.)
Standing output, daily, follows the existing daily pulls by appending new rows to the relevant monthly output maybe 15m
after the Schwab autopull."*

On the path: *"Yes you understand what im asking for exactly, that is what I wanted you to comprehend that we should
follow AWS path structure via LGIC_NAMING, makes it very easy to manage. Also yes, it probably is going to end up making
more sense to do them monthly anyway if it's anywhere near 16k a quarter. If however its like 5k a quarter or something
then quarterly is better."*

On the 16k figure: *"I thought excel docs could only take 16k rows, apparently they actually take a little over 1m
rows. I think this means we can probably manage these on a quarterly intterval and not have bulky slow excel (in
theory)."*

His answers to this seat's three cards, after the measured file sizes were put to him: period **"Monthly
(Recommended)"**; masters **"Separate per master (Recommended)"**; columns **"140-column full"**.

---

## PART I -- THE OUTCOME TERRITORY

### O1. Andrew opens one Excel file per Schwab master per month on the main Opal SharePoint and reads every transaction in it
Masters 08242234 and 08335338, separately. All 140 vendor columns. The file for the current month exists from the first
trading day's data onward.

### O2. Each morning Andrew finds yesterday's transactions already in the current month's file, without anyone running anything
The file updates itself after the daily Schwab pull completes, about 15 minutes after it. No clock-only schedule: if
the pull is late, so is the update, and a day never shows up half-written.

### O3. Andrew (and later any Opal user) finds any AWS-delivered file by knowing its AWS address -- the SharePoint path IS the S3 path
The SharePoint location under the `AWS` folder repeats the naming-builder address segment for segment (s.4.3). Someone who
knows where a dataset lives in S3 knows where it lives in SharePoint, and the reverse.

### O4. Andrew checks what each run delivered -- which days, how many rows -- and can tell a short file from a quiet day
Every run prints and records its denominator: data days read, rows written, per master per month. A day with no data is
distinguishable from a day the run failed to read.

### O5. Andrew turns on delivery to Menachem when he judges the files clean, and not before
Recipient delivery (menachem@opalinvest.com) is built so that it is OFF until Andrew's word, after several days of clean
runs. Nothing is sent to Menachem as a side effect of building or testing.

### O6. The next AWS -> SharePoint movement is a new configuration, not a new build
Dataset, masters or firm, period and columns are inputs; the trigger, the address mirror, the rebuild-and-replace
delivery and the run record are shared. Schwab transactions is the first instance of the pattern (his "patterned
structure ... this case being the actual initial implementation").

---

## PART II -- WHERE THE BOUNDARY SITS

**Owns:** the monthly workbook producer for Schwab transactions; the S3 home of the workbooks; the SharePoint mirror of
them under `AWS/`; the run record; the OFF-by-default recipient switch; the SharePoint path grammar as a naming rule.

**Relies on, does not own:**
- **The Schwab daily pull and silver conversion** (`canonical-schwab-si2-*-daily-pull` rules, Lambda
  `opal-assets-silver-schwab`) -- it consumes their completion marker and never changes them.
- **LGIC_NAMING / LGIC_ENFORCE** (held by `2.0.0_SA_COO~G`) -- the builder `lib/opal_naming.py` and
  `org/standards/NAMING_SCHEMA.json`. A SharePoint path rule is an ADDITION to that canon and is theirs to admit (s.5).
- **The Opal Gateway** (`infra/aws/ec2/opal-gateway`) -- the one existing SharePoint write path. A replace-in-place,
  large-file write is a new capability on it (s.4.4).
- **NFRA_OPLGTW** (`2.0.0_SA_COO~O`) -- NOT a home for this. Andrew's ruling retired FWD-9 there (97507). Its six-prefix
  contract role is never widened for this reader; any reader here is its own role.

**Explicitly out:** any change to silver data; any de-duplication across masters; recipients other than Menachem; other
custodians or datasets (they are future instances under O6, not this build).

---

## PART III -- THE QUALITATIVE BAR

- Andrew opens the month's file for a master and uses it instead of asking an agent to pull the transactions.
- A transaction in the file matches the same row in S3 silver field for field; a row count he reads there matches the
  count the run printed for that month.
- He opens the file from SharePoint without it being so slow he gives up on it (the measured sizes are in s.6; whether
  they pass is his judgment on real use, not a number set here).
- When a morning's update did not happen, he can tell that from the run record, not by noticing a missing day.

---

## PART IV -- THE SUBSTRATE (findings, measured 2026-09-16)

### 4.1 The data
- Source rows: `s3://opal-data-assets/schwab/{08242234|08335338}/silver/fact_trn/date=YYYY-MM-DD/data.parquet`, one
  file per day per master; 140 columns. `dim_transaction` is a 44-column projection of the same rows with identical
  counts (0 of 304 partitions differ per master; the writer refuses a mismatch,
  `data/assets/scripts/silver/schwab_projections.py:55-68,118-122`). Andrew chose the 140-column table.
- History: 0824 from 2024-01-16, 0833 from 2024-07-08, both through 2026-09-15.
- Volume per master per month, 2025-07 to 2026-08: **77,722 (2025-11) to 213,084 (2025-12)**; Aug 2026 0824 = 134,387,
  0833 = 136,753. Normal day ~1,900 rows; rebalance days ~25,000, almost all Trades (2026-08-18, 0824: 24,916 rows,
  24,661 Trades -- decoded in full by this seat, a second instrument to the helper's parquet-footer count).
- The masters overlap: Aug 2026, 99.98% of 0824's rows are in 0833 and 98.25% of 0833's in 0824; 6,150 shared accounts.
  Andrew chose separate files, so nothing is de-duplicated and the overlap is expected, not a defect. No unique row id
  exists; 97 exact same-day duplicate rows per master in August are in the source.

### 4.2 The trigger
- Pull schedule (EventBridge, live, ENABLED, every day): 0833 at 09:45 and 21:45 UTC; 0824 at 10:15 and 22:15 UTC
  (`infra/aws/terraform/canonical-schwab-ec2/monolith-daily-schedule.tf:34-37`). Under EDT that is 5:45 / 6:15 AM ET.
- Completion marker written by silver after the tables:
  `s3://opal-data-assets/schwab/{master}/meta/complete/date=YYYY-MM-DD.json`
  (`data/assets/scripts/silver/conversion_manifest.py:162-164`). On 2026-09-16 it landed 1-3 s after the tables,
  ~1 minute after the fire. Markers exist only from 2026-08-31 (11 per master).
- Irregularities the design must tolerate: the 09-11 marker arrived on the SECOND (evening) fire; the 09-15 marker was
  REWRITTEN at 19:10 UTC today by an unidentified run (886 -> ~16,000 bytes, reporting 0 tables written).

### 4.3 The address -- builder output, not hand-typed
Exercised this session against `lib/opal_naming.py`:
- `address("schwab","08242234","platinum","trn-export","month=2026-09")` ->
  `s3://opal-data-49financial/schwab/08242234/platinum/trn-export/month=2026-09` (the registry places both masters in
  the 49 Financial tenancy; both are registered MASTER scopes).
- Same call with `gold` -> `s3://opal-data-49financial/schwab/08242234/gold/trn-export/month=2026-09`. Which tier a
  delivery workbook belongs in is a canon question (Doctrine R1-R21), not settled here.
- `name("schwab", None, "trn-export", kind="lambda")` -> `schwab-trn-export-lambda`;
  `kind="daily"` -> `schwab-trn-export-daily`; `kind="role"` -> `schwab-trn-export-role`.
- `table` and the function word `trn-export` are this seat's placeholders; the builder accepted them, which proves the
  grammar, not the choice.
- **The mirror rule Andrew confirmed:** SharePoint path = `AWS/` + the builder's key, then the object. Example:
  `AWS/schwab/08242234/platinum/trn-export/month=2026-09/<object>.xlsx`. `=` is legal in SharePoint folder names.
- `org/standards/NAMING_SCHEMA.json` carries NO SharePoint grammar today (searched: no occurrence of "sharepoint").

### 4.4 The destination and the write path
- Site: **Opal Capital**, `https://opalinvest.sharepoint.com/sites/OpalCapital`, one library "Documents"; root holds
  Holdings, End of Day Updates, Opal Client Tickets, General and others; no `AWS` folder yet. It is this seat's reading of
  "the main Opal sharepoint"; the only site with more stored bytes is the 49 Financial Internal Channel (49F-specific).
  **Confirm at L2/L5.**
- SharePoint is Opal's own Microsoft 365 tenant reached through the existing Opal Gateway; this is not vendor egress.
- The Gateway's one write tool, `upload_text_to_site` (`infra/aws/ec2/opal-gateway/app/tools.py:487`), writes SMALL TEXT
  files and NEVER overwrites (`conflictBehavior=fail`). This export needs a binary workbook of tens of MB REPLACED daily.
  That is a new, bounded capability (large-file upload session, replace allowed only under `AWS/`), not a use of the
  existing tool.

### 4.5 Measured file size (this seat built the real files)
| August 2026, 0824, 134,387 rows | size | write time |
|---|---|---|
| 44 columns, CSV | 47.3 MB | 1.4 s |
| 44 columns, xlsx | 19.6 MB | 63 s |
| **140 columns, xlsx (his choice)** | **45.4 MB** | **158 s** |
Scaled linearly (INFERRED, not built): the largest month so far (2025-12, ~213k rows) would be ~72 MB.

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

1. A SharePoint path rule admitted into the naming canon (the `AWS/` + key mirror), by the LGIC_NAMING owners.
2. A decision on the delivery tier (gold vs platinum) under Doctrine R1-R21, and the `table` / function words, by
   builder output.
3. The Gateway can replace a large binary file inside `AWS/` and only there.
4. The producer rebuilds the whole month from silver on each trigger (so "append" is a rebuild: late or corrected days
   heal themselves, and a rewritten marker is harmless). **"Append new rows" is his word for the effect; a rebuild is
   this seat's rec for the mechanism** -- the COO or CTO may rule otherwise.
5. The trigger fires off each master's completion marker plus ~15 minutes and tolerates a marker on the evening fire or
   a rewritten one.
6. A read role scoped to exactly `schwab/{08242234,08335338}/silver/fact_trn/` and the output prefix -- never a widening
   of an existing role.
7. A run record per run (days read, rows written, file replaced, time) where Andrew can read it.
8. The Menachem recipient switch exists and is OFF; Andrew turns it on.
9. A backfill decision: which past months get built on first run (history exists from 2024).
10. Rollback: SharePoint version history restores the prior workbook; the S3 object is the source of the SharePoint copy;
    silver is never touched.

---

## PART VI -- STATUS (NOT OUTCOME-BEARING; measured 2026-09-16 ~18:4x-19:5x UTC)

- No producer, no `AWS` folder, no S3 output prefix, no SharePoint grammar exists.
- Silver `fact_trn` is current through 2026-09-15 for both masters.
- 0824 and 0833 markers present for 11 dates from 2026-08-31.

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- It did not check whether the 12:15 UTC `opal-assets-silver-schwab-sweep-daily` run ever writes TRN after the fire.
- It does not know who rewrote the 09-15 markers today.
- The ~72 MB largest-month figure is extrapolated; only August was built. Excel open-time on a real laptop was not measured.
- It did not check the Gateway's Microsoft Graph permissions for a replace or an upload session, nor Graph's size limits.
- It did not read NFRA_OPLGTW's OG-z-1 entitlement guard to see whether it applies to an Andrew-only file.
- "Main Opal sharepoint" is this seat's reading (s.4.4); Andrew has not named the site.
- `.claude/skills/49-schwab-conv/SKILL.md:30` points at `s3://opal-data-bd/schwab/silver/trn/`, which is not where
  current silver lives; whether the old prefix is still written was not checked.

---

## s.8 -- PROJECT OR FOLD-IN: THIS SEAT'S RECOMMENDATION

**Recommend a SMALL PROJECT**, the one Andrew named: *AWS -> SharePoint file movements as a patterned structure, this
case the first implementation.* The test he set was whether it "requires much consideration". Measured, it needs three
things that do not exist and are each owned elsewhere: a naming-canon addition (s.V.1), a new Gateway write capability
(s.V.3), and a new marker-triggered producer (s.V.4-5) -- plus a new read role. Rule 30 makes it a new pipeline built to
LGIC, which the L4 PRD is where builder output gets cited. Folded into `2.0.0_SA_COO~G`'s LGIC workflow, those would ride
on unrelated rounds. Against that: `2.0.0_SA_COO~G` already holds the naming canon, so seating the project there is
natural. **Andrew's call.**

---

## REFS

```
  BRIEF PATH        docs/briefs/schwab-trn-sharepoint-export-brief-20260916.md
  PROJECT           NONE-YET (s.8)
  EXISTING PRD      NONE
  SIBLING PROJECTS  LGIC_NAMING, LGIC_ENFORCE (2.0.0_SA_COO~G); NFRA_OPLGTW (2.0.0_SA_COO~O, FWD-9 retired)
  PRIOR ART         org/tier1_exec/2.0.0_SA_COO~O/logs/2026-09-15/session_1215-2015Z~O_nfra_oplgtw_l7.md :37-39;
                    lib/opal_naming.py address()/name(); infra/aws/ec2/opal-gateway/app/tools.py:487;
                    data/assets/scripts/silver/conversion_manifest.py:162-164;
                    data/assets/scripts/silver/schwab_projections.py;
                    infra/aws/terraform/canonical-schwab-ec2/monolith-daily-schedule.tf:34-37;
                    data/assets/docs/SCHWAB_BOX_ARCHETYPE.md
  MEASURED AT       2026-09-16 ~18:40-19:55 UTC (S3 listings, parquet reads, builder calls, SharePoint listings)
```
