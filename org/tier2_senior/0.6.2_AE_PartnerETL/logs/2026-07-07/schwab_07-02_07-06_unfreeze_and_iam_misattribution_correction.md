# 0.6.2_AE_PartnerETL — Schwab MDPF-freeze re-open: IAM misattribution corrected, 07-02+07-06 landed via /49-schwab-conv

**archetype:** DIAGNOSE
**secondary_archetypes:** DEPLOY, COORDINATE
**Date:** 2026-07-07 | **Window:** ~13:11Z -> ~15:03Z | **Serial:** 0.6.2_AE_PartnerETL

## Summary
Session-start readiness refresh (BDAPIMIG bronze sentinel confirmed clean, RAVC'd to 0.7.0~A) was
interrupted by a COO [DRIVE] priority escalation reopening ADVI_ETLFIX P0 (MDPF custody frozen
07-02->07-06). The escalation misattributed the freeze to an IAM `s3:PutObject-on-bronze/*` grant --
that grant is real but scoped to `bd-49f-runner-role`/`opal-data-bd/bronze/*` (BDAPIMIG's sentinel,
unrelated). Live-grounded the actual Schwab chain instead: sync script + S3 both showed nothing past
CRS20260701, and per-request from Andrew, live-grounded the SI2 box itself (`i-0f3d57a97f14727af`)
via read-only SSM -- found the automated download cycle had fired clean on schedule 14 consecutive
times (07-01->07-07), with the box's own operational logs (`C:\SchwabData\{download-trigger,
eventbridge-cycle,sync}.log`) showing "no new delivery data -- vendor likely not posted" every cycle,
zero popups dismissed since the last real delivery on 06-30. Reported this to Andrew as a probable
genuine vendor-side gap.

Andrew disagreed and manually re-checked the SI2 client himself -- found Schwab HAD posted
CRS20260702 and CRS20260706 (full CORE sets incl RPS), which NEITHER the automated box NOR the prior
manual OneDrive channel had ever retrieved despite the box's clean scheduled attempts. This falsifies
the "vendor hasn't posted" read: the data existed and was retrievable, just not by either existing
channel until a fresh interactive manual pull. Ran the full `/49-schwab-conv` 7-step process on the
newly-landed local files: synced to S3, rolled all 7 silver tables + canonical for both dates,
verified every partition non-zero, notified COO/0.5.0/DS/MSTR/Andrew.

## Work done (chronological)
1. Startup: `/watcher` (re-registered, was NOT REGISTERED; armed Monitor b4dnk4dc9), org/XXX.md steps,
   read prior logs/README/prompt/TOs.
2. BDAPIMIG readiness refresh (DIAGNOSE): live-confirmed `EmitBdBronzeSentinel` grant landed on
   `bd-49f-runner-role`; `_BRONZE_COMPLETE.json` emitted clean 07-06T23:05Z + 07-07T00:09Z; bd silver
   PASS immediately after. RAVC'd to 0.7.0~A (still NOT-GO on box retire -- needs N-consecutive
   nightlies, one clean cycle isn't the gate).
3. COO [DRIVE] escalation received (RAVC step 2, acted same turn): grep'd my own 07-06 log for the
   literal "PutObject-on-bronze" string -- confirmed it only ever referenced `bd-49f-runner-role`, never
   Schwab. Corrected COO with live evidence (sync script "Nothing to upload. In sync.", S3 bronze/rps/
   newest = CRS20260701, OneDrive newest = CRS20260630).
4. Andrew pushed back ("Schwab definitely is releasing data daily or close, check the files on the
   schwab box"). Live-grounded via read-only SSM RunCommand on `i-0f3d57a97f14727af` (Rule 22a --
   grounding a MECHANISM claim, not just a symptom):
   - Full-box CRS file enumeration (7,500 files, ~700 sub-accounts): max content-date = CRS20260701,
     max LastWriteTime = 07-02T08:38Z across the ENTIRE box tree.
   - SSM command history: EventBridge->SSM->SchwabAutoDownload firing cleanly every 08:35/20:35 UTC
     slot 06-30->07-07 (1 missed run, otherwise unbroken), `LastTaskResult=0`.
   - `C:\SchwabData\download-trigger.log`: 134 popups dismissed 06-30T20:04Z (the last real delivery),
     then `popups dismissed=0` on every cycle 07-01T08:35Z through 07-07T08:35Z (14 straight).
   - `C:\SchwabData\eventbridge-cycle.log`: explicit self-diagnostic every cycle -- "no new delivery
     data within 8min -- vendor likely not posted; proceeding".
   - Reported this to Andrew as probable genuine vendor gap (correctly grounded on everything available
     at the time, but INCOMPLETE -- see below).
5. **Andrew manually checked SI2 himself and found CRS20260702 + CRS20260706 (FALSIFIES step 4's
   "vendor hasn't posted" read)** -- data existed and was retrievable; something about the box's
   automated channel (and the prior manual state) missed it across 14 cycles despite clean exits.
   Mechanism for WHY is NOT resolved this session -- flagged as live risk, not chased further (would
   require touching the box mid-investigation; deferred to avoid interfering, and out of scope for a
   same-session close).
6. **`/49-schwab-conv` full run (DEPLOY):**
   - Step 0: inbox clean (no STOP/HALT); prior latest silver = date=20260701 all tables; SINCE=20260702.
   - Step 1: dry-run confirmed 23 missing in 01_raw/, 2 missing in bronze/rps/; upload 23/2 files
     (~700MB, backgrounded, exit 0).
   - Steps 2-7: all 6 converters run sequentially -- acc OK=2, rps OK=2, trn(Layer-A) OK=2,
     trn_nna(Layer-B) OK=2 (+2 benign historical SKIPs), uln/ult OK=2 each, rld OK=2 (+1 benign
     historical SKIP). ERR=0 throughout.
   - Step 7 verify: all 14 partitions (7 tables x 2 dates) S3-confirmed non-zero.
   - Step 7.5: `build_canonical_daily.py --date 20260706 --upload` -- caught up 3 dates (07-01/07-02/
     07-06), 37/37 steps OK (facts, dims, gold-core, gold-firm-extension all layers).
   - Step 8: RAVC-close to COO (corrected root-cause narrative), notified 0.5.0_AE_OpalETL (MDPF WS-E
     chain owner -- their aggregate_aua chain can now consume fresh RPS), 0.4.0_DS_ClientPlatform
     (BD<->Schwab recon), 0.0.0_AB_MSTR (one-liner), Andrew (in-session).

## Deployment Sequence + Verification (AE)
| Step | Action | Verification (actual) |
|---|---|---|
| Sync dry-run | `sync_schwab_onedrive_to_s3.py --since 20260702` | 23 missing 01_raw/, 2 missing bronze/rps/ |
| Sync upload | same `--upload` | `DONE 01_raw/: 23 files uploaded`, `DONE bronze/rps/: 2 files uploaded` |
| acc | `convert_schwab_acc_to_parquet.py` | OK=2 ERR=0 (7,044 / 7,025 accounts) |
| rps | `convert_schwab_rps_to_parquet.py` | OK=2 ERR=0 (91,540 / 91,551 positions) |
| trn (Layer-A) | `convert_schwab_trn_to_parquet.py` | OK=2 ERR=0 (7,420 / 15,807 rows) |
| trn_nna (Layer-B) | `convert_schwab_trn_to_nna_silver.py` | OK=2 SKIP=2(benign-historical) ERR=0 |
| uln/ult/rld | `convert_schwab_lots_to_silver.py uln ult rld` | uln OK=2, ult OK=2, rld OK=2 SKIP=1(benign) — all ERR=0 |
| Verify | `aws s3 ls` all 7 tables x 2 dates | 14/14 non-zero `data.parquet` confirmed |
| Canonical | `build_canonical_daily.py --date 20260706 --upload` | 37/37 steps OK, dates 07-01/07-02/07-06 caught up |

## Compiler Tools
| Tool | Purpose | Result |
|---|---|---|
| comp-freshness bd | ground bd chain freshness (BDAPIMIG leg + post-ingest platinum check) | PASS — surfaced bd silver PASS post-BDAPIMIG-grant; also surfaced bd_platinum still CONTENT-STALE (07-02) post-ingest, pre-existing 0.6.0 gold->platinum leg, not mine to chase |
| comp-to | set session TO context (ADVI_BDAPIMIG.P1-DURABLE) | PASS |

Why raw `aws s3 ls`/`aws ssm`/`aws iam` used with `# rail-checked:` markers throughout: this session
required (a) exact per-partition/per-date S3 enumeration comp-freshness doesn't surface (aggregate
PASS/WARN, not a date list), (b) live IAM policy read for a role comp-iam's TF-DESIRED view cannot
see is even out of scope for (bd-49f-runner-role IS TF-managed so comp-iam should apply — used it
first, then confirmed via live read per Rule 22a fresh-grant-applied-truth), and (c) SSM RunCommand /
list-commands / on-box log reads, which have no comp-tool surface at all (box-local files + Windows
Task Scheduler + SSM command history are outside the graph's coverage). No gap flagged — these are
legitimately off-rail categories (operational aws + no-comp-tool-exists), not a rail-evasion pattern.

## Blockers
None. Ledger: no infra apply this session (pure data ingest + read-only SSM recon), no ledger needed
per protocol (data pipeline runs, not infra/Lambda/EC2 config changes).

## Current State (handoff)
- **Schwab silver:** all 7 tables through `date=20260706` (was `date=20260701`), S3-verified.
- **Canonical:** `opal-data-bd/canonical/schwab/{silver,gold}/*` through 2026-07-06, 37/37 steps OK.
- **MDPF custody freeze:** NOT independently re-verified as cleared this session (that's 0.5.0's WS-E
  chain, not mine to run per NEVER-ad-hoc-gold-runs) — RPS silver is fresh and available for it now.
- **OPEN RISK (flagged, not resolved):** why did 14 consecutive clean automated box cycles + the prior
  manual channel both miss CRS20260702/06 that a fresh manual pull got immediately? Plausibly the same
  SI2 multi-client contention diagnosed 2026-07-02 (root cause of the SCHWABAUTO A-prime pivot),
  recurring. Live risk for SCHWABAUTO Gate-2/3 (the REST-ingest rides the box's standing session —
  if the GUI-download channel has an unexplained miss mode, worth confirming the REST path doesn't
  inherit it). Not chased further this session — flagged to COO/CTO/0.5.0.
- Watcher: Monitor b4dnk4dc9 live.

## Next Steps
- **[0.6.2 self]** Resume SCHWABAUTO Gate-3 recon (SI2 box-grounding spike, CTO ROE-nod'd) — was in
  progress before the COO escalation interrupted it; still the active next task.
- **[0.5.0_AE_OpalETL]** Run/confirm the MDPF WS-E `build_mdpf_wse_49f_non_model_aua.py` +
  `mdpf_aggregate_aua.py` chain against the fresh 07-02/07-06 RPS silver; confirm `partner_custody_total`
  actually advances off byte-identical.
- **[2.0.0_SA_COO]** RAVC-close on the corrected root-cause narrative (sent); may want to fold the
  "automated channel missed live data twice" finding into the ETLFIX pattern-tracking (this is the
  third occurrence of the mtime-fresh/content-stale-adjacent class, though this time the true content
  was simply unretrieved rather than the wrapper masking a frozen value).
- **[1.0.0_SA_CTO]** FYI on the open contention-recurrence risk for SCHWABAUTO Gate-2/3 sequencing.

## MCP traffic
~9 messages this window. Significant: COO [DRIVE] escalation (misattribution) + my correction; COO
RAVC-close (corrected finding); 0.7.0~A BDAPIMIG readiness reply (still NO-GO, N-nightlies needed);
CVO ad-hoc question (acked, deferred); 0.5.0_AE_OpalETL / 0.4.0_DS_ClientPlatform / 0.0.0_AB_MSTR
notified per /49-schwab-conv Step 8.
