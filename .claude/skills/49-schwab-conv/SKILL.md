---
name: 49-schwab-conv
description: AE-owned recurring 49F (account 08242234) Schwab ingest — sync the newly-delivered Schwab CRS files from the OneDrive delivery folder to S3 and roll all six silver tables forward. The canonical 7-step process, in order — (1) sync OneDrive -> s3://opal-data-schwab/01_raw/ (all extensions) + mirror *.RPS to bronze/rps/, then the idempotent silver converters (2) ACC (3) RPS (4) TRN-Layer-A (5) TRN-NNA-Layer-B (6) ULN-canonical-via-lots_to_silver (7) RLD — followed by an S3 verification of the latest partition per table and a notify to Andrew + DS. Folds every banked gotcha: the opal-data-schwab PutObject AES256-SSE deny (DS is blocked here, which is why this is AE-owned), RLD is NON-OPTIONAL (B_02 canonical_lots primary realized-lot tax source — omitting it silently degrades gold), all converters idempotent (skip converted dates, --force rewrites, --since scopes), and the ACC triple-`state`-column header dup. Use when new Schwab files have landed locally (Andrew says "we downloaded the new Schwab data" / "convert the Schwab files" / "update the Schwab data") or DS reports stale silver/{ACC,RPS,TRN,TRN_NNA,ULN,RLD} partitions. "Convert the Schwab files" = ALL SEVEN STEPS, every time. AE-only (0.x.0_AE_*); other serials route to the pod AE.
---

# /49-schwab-conv — 49F Schwab ingest (AE-owned recurring task)

Sync the newly-delivered Schwab `CRS{YYYYMMDD}.{ext}` files from the OneDrive delivery folder to
S3, then roll all six silver tables forward. **The authority for this process is your
`prompt.md` § "Schwab Ingest"** (the persona spec); this skill is the executable entry point and
folds the dry-run-first + verify-after discipline. The standard wins on any divergence.

**Why AE-owned (not DS):** the `opal-data-schwab` bucket policy is a resource-based DENY on
`PutObject` for the `Andrew_Berman` IAM user without SSE — DS cannot upload directly. AE runs the
full ingest. (AE = `0.x.0_AE_*`; any other serial halts at Step 0 and routes to the pod AE.)

**"Convert the Schwab files" = ALL SEVEN STEPS, every time.** The converters produce independent
silver tables; skipping any (especially RLD, or the trn_nna Layer-B) silently degrades a downstream
gold consumer. **trn_nna (TRN Layer B) is the NNA-classified flows the gold C_01.canonical_nna reads**
— it MUST run after trn (Layer A) every time, else canonical_nna silently gets zero Schwab flow.

## Fixed facts (49F, account 08242234)

| Thing | Value |
|---|---|
| Source (local) | `C:\Users\AndrewBerman\OneDrive - Opal Capital\Documents\Schwab Data Delivery\08242234\` |
| File pattern | `CRS{YYYYMMDD}.{ACC,RPS,TRN,ULN,RLD,SEC,UPN,UPT,...}` (Schwab SI2 Desktop delivers per-account) |
| Raw S3 dest | `s3://opal-data-schwab/01_raw/` (all ext) + `*.RPS` mirror to `s3://opal-data-schwab/bronze/rps/` |
| Silver S3 dest | `s3://opal-data-bd/schwab/silver/{acc,rps,trn,trn_nna,uln,ult,rld}/date=YYYYMMDD/data.parquet` (ULT WIRED 2026-07-02 — it IS from the lots converter mode-3, NOT B_03; the old "B_03-sourced" note was WRONG and the ult mode was never invoked → silver/ult froze 85d. Now run every time.) |
| Last-known state | as of 2026-07-02, all 6 silver tables through **20260701** (07-01 landed via the Andrew-GO'd ONE-OFF bridge from the quartz-box validation prefix -- 0.6.2, ledger 20260702T1515Z; N=5 repoint hold + OneDrive going-forward path INTACT; CVO-verified custody $1,604,173,986.44). GOTCHA banked: `convert_schwab_trn_to_parquet.py` reads **LOCAL OneDrive disk** (DEFAULT_SRC_DIR, floored 06-30) -> a bridge that advances only S3 silently NO-OPs TRN Layer-A; stage the raw locally + pass `--src-dir <dir>` (durable fix = DS~A C3: point TRN-A at S3 01_raw/). Step-7.5 canonical (`build_canonical_daily`) NOT run in that bridge -- run it if the canonical store must match silver. `build_canonical_daily.py --date` needs a **HYPHENATED** date (`2026-06-25`), NOT compact — compact crashes `position_t0` strptime + throws a gold_holdings NoSuchKey (2026-07-01 CVO finding). (update this line each run) |

**SSE gotcha:** `opal-data-schwab` DENIES `PutObject` without `x-amz-server-side-encryption:
AES256`. The sync script already passes `ExtraArgs={'ServerSideEncryption':'AES256'}` — if you ever
fork/rewrite it, keep that line or every upload silently fails `AccessDenied`.

**comp-rail (Rule 21):** every step here is OPERATIONAL aws/python (sync/cp/ls + running converters)
= FREE, not gated. No raw inspection-grep/aws needed.

## Step 0 — Identify + scope

- **AE-only check:** serial not `0.x.0_AE_*` and not explicitly Andrew-directed -> HALT, route to AE.
- Anchor at the workspace root: `cd /c/Users/AndrewBerman/Desktop/ajb_workspace`.
- Pull inbox (`check-inbox` + `get_agent_status`) — a `[STOP]`/`[HALT]` blocks the ingest.
- Find the prior latest silver date (the last `/49-schwab-conv` log, or `aws s3 ls
  s3://opal-data-bd/schwab/silver/trn/ | tail`). New ingest extends from there. Set
  `SINCE=<prior_latest+1>` (e.g. `20260605`) to scope the sync.

## Step 1 — Sync OneDrive -> S3 (DRY-RUN first, then upload)

```bash
# 1a. DRY-RUN — preview exactly what will upload (the script defaults to dry-run, no --upload)
python data/black_diamond/scripts/bronze/sync_schwab_onedrive_to_s3.py --since {SINCE}
#   -> confirm "Missing in 01_raw/: N" + the sample files are the expected new dates.
#      0 missing = nothing new (the data didn't land where expected — check the OneDrive folder).

# 1b. UPLOAD — large files (ULN ~180MB/day, ULT ~140MB/day); run in the BACKGROUND, it can be GBs
python data/black_diamond/scripts/bronze/sync_schwab_onedrive_to_s3.py --upload --since {SINCE}
#   -> "DONE 01_raw/: N files uploaded" + "DONE bronze/rps/: M files uploaded"
```

The sync is idempotent (compares filenames to existing S3 keys, uploads only missing). `--since`
just scopes the scan; omit it to scan the whole folder (slower, same result). Run **1b in the
background** (`run_in_background`) and proceed to verify once it exits 0.

## Steps 2-7 — Roll the silver tables forward (after Step 1 completes)

All idempotent (skip already-converted dates; `--force` rewrites; `--date YYYYMMDD` single date).
Can run in parallel after Step 1, but SEQUENTIAL is cleaner on this box (per-table output + error
isolation; each only processes the new dates). Run them and capture each rc:

```bash
python data/black_diamond/scripts/bronze/convert_schwab_acc_to_parquet.py        # -> schwab/silver/acc/      (account xref)
python data/black_diamond/scripts/bronze/convert_schwab_rps_to_parquet.py        # -> schwab/silver/rps/      (position snapshots)
python data/black_diamond/scripts/bronze/convert_schwab_trn_to_parquet.py        # -> schwab/silver/trn/      (TRN Layer A: raw transactions — INTERMEDIATE, not the NNA layer)
python data/black_diamond/scripts/bronze/convert_schwab_trn_to_nna_silver.py     # -> schwab/silver/trn_nna/  (TRN Layer B: NNA-classified flows — the GOLD-CONSUMED table; reads trn/; feeds C_01.canonical_nna. MUST run AFTER trn Layer A)
python data/black_diamond/scripts/bronze/convert_schwab_lots_to_silver.py uln ult rld  # ONE call, 3 modes -> schwab/silver/{uln,ult,rld}/
#   uln = unrealized lots long+short (non-taxable) — CANONICAL; replaces retired convert_schwab_uln_to_silver.py long-only Rule-17 filter
#   ult = unrealized lot detail, TAXABLE (brokerage) — identical format to uln; FEEDS B_02.canonical_lots (gated gold-freshness input schwab_ult, warn_age 36h). WIRED 2026-07-02 (0.6.2, CTO-arch-gated): was NEVER invoked -> silver/ult froze 85 days (04-07..07-01) + degraded B_02 lot-cost-basis silently. RUN ULT EVERY TIME.
#   rld = canonical realized lots — PRIMARY realized tax detail
```

Expect `OK=N SKIP=0 ERR=0` per converter (N = new dates). A `SKIP` on an old historical date with
no data rows (e.g. an RLD date with 0 DL rows) is benign; `ERR>0` is not — investigate before
reporting done.

**RLD is NON-OPTIONAL.** `B_02.canonical_lots.py` uses `schwab/silver/rld/` as its **primary
realized-lot tax source**; when an RLD partition is missing for a date, B_02 silently falls back to
BD's own realized data — lower-quality output, NO error. (Discovered gap 2026-04-30.) Run RLD every
time.

## Step 7 — Verify the served artifacts (never trust rc=0)

Confirm the latest partition exists + is non-zero for ALL SIX tables:

```bash
LATEST={new_latest_date}   # e.g. 20260618
for t in acc rps trn trn_nna uln ult rld; do
  aws s3 ls "s3://opal-data-bd/schwab/silver/$t/date=$LATEST/data.parquet"
done
```

All six must return a non-zero-byte `data.parquet` dated today. RLD especially — it's the one that
silently no-ops downstream if missing; and trn_nna — the gold C_01.canonical_nna reads it.

## Step 7.5 — Refresh the Schwab-raw-native canonical (daily-incremental orchestrator)

After the six silver tables verify, run the DATA_ANALYTICS canonical daily-incremental build as the
TAIL of this skill (COO Option-A, DS 2026-06-25: zero new infra; fires exactly when fresh Schwab
silver lands — this skill's lane). It orchestrates the 5 silver facts + 5 dims + gold holdings +
trailing-30d account_gains off the silver you just rolled:

```bash
# --date accepts compact ($LATEST is YYYYMMDD, e.g. 20260625) OR hyphenated (2026-06-25);
# build_canonical_daily.py normalizes both in-script (2026-07-01 CVO compact-crash finding fixed).
python data/canonical/schwab/build_canonical_daily.py --date $LATEST --upload
# (or just --upload -> defaults to the latest RPS silver date)
```

Idempotent (overwrites the date's partitions), self-contained, reports `N/M steps OK` + non-zero
exits on failure. Design: `data/canonical/schwab/docs/07_PRODUCTIONIZATION.md`. On a non-zero exit,
investigate before notifying (a canonical-build failure does NOT undo the silver roll, but the
canonical store stays a day behind until re-run). When it reports all steps OK, the canonical
`opal-data-bd/canonical/{silver,gold}/*` reflects `$LATEST` end-to-end.

## Step 8 — Notify + log

- **Message Andrew** (direct, in-session) with: # raw files synced, the new silver date partitions
  per table, and the latest silver date for each of the five tables.
- **Message `0.4.0_DS_ClientPlatform`**: new partitions through `{LATEST}` available for the BD <->
  Schwab reconciliation. (DS picks up from there.)
- **Message `0.0.0_AB_MSTR`** a one-line summary (per prompt.md).
- Write the session log via `/log` (archetype DEPLOY/IMPLEMENT) — table of new partitions per feed +
  the verification output. Update the "Last-known state" line at the top of this skill to `{LATEST}`.

## Known edge cases (already patched in the converters — do not re-fix)

- **ACC triple-`state` header:** ACC raw H2 header repeats `state` 3x; `convert_schwab_acc_to_parquet.py`
  suffixes dups `__2`/`__3` before DataFrame construction (commit `f41b37f5`).
- **Bucket SSE deny:** see SSE gotcha above — the sync script handles it; keep the `AES256` ExtraArg.
- **Partial-prior-ingest:** the sync `--since` may show fewer new dates than calendar days if an
  earlier run already covered some (e.g. weekend gaps + a prior partial). The converters are
  authoritative — `To convert: N` reflects the true delta. Report the actual N, not the calendar span.

## Report (end of every invocation)

```
/49-schwab-conv {serial}
  SYNC:    {N} raw -> 01_raw/, {M} -> bronze/rps/  (since {SINCE})
  SILVER:  acc/rps/trn/uln/rld each OK={K} ERR=0; new dates {list}
  LATEST:  all five tables through {LATEST} (S3-verified non-zero)
  NOTIFY:  Andrew + DS (+ MSTR) sent
```
