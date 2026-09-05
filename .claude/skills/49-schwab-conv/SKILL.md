---
name: 49-schwab-conv
description: AE-only recurring 49F Schwab ingest: sync the new Schwab CRS files from OneDrive to s3://opal-data-schwab and roll all six silver tables (ACC, RPS, TRN, TRN_NNA, ULN, RLD) forward -- all seven steps, every time. Use when new Schwab files have landed or DS reports stale silver partitions. Other serials route to the pod AE.
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
| **SOURCE OF RECORD (2026-07-17 onward)** | **`s3://opal-data-assets/schwab/08242234/bronze/{feed}/{YYYYMMDD}/08242234.CRS{YYYYMMDD}.{FEED}.zip`** — the monolith puller, double-zipped, unzip-at-read. **ALL SEVEN converters read this** via `_monolith_bronze.py`; none reads local or `01_raw`. |
| ~~Source (local)~~ **DEAD** | ~~`C:\Users\AndrewBerman\OneDrive - Opal Capital\Documents\Schwab Data Delivery\08242234\`~~ — **STOPPED RECEIVING DELIVERIES AFTER `CRS20260715`** (verified 2026-07-24: newest local file `CRS20260715.TRN`, mtime 2026-07-16T14:00:31Z). **This folder is NOT a discrimination instrument any more** — checking it alone returns "ABSENT" for data that is present in the monolith. |
| File pattern | `CRS{YYYYMMDD}.{ACC,RPS,TRN,ULN,RLD,SEC,UPN,UPT,...}` (Schwab SI2 Desktop delivers per-account) |
| ~~Raw S3 dest~~ **DEAD** | ~~`s3://opal-data-schwab/01_raw/`~~ — frozen at `20260715`, fed only by the dead local folder. **No converter in this cycle reads it.** ⚠ **BUT `data/canonical/schwab/build_canonical_daily.py:154-156` STILL ENUMERATES IT** — see Step 7.5. |
| Silver S3 dest | `s3://opal-data-bd/schwab/silver/{acc,rps,trn,trn_nna,uln,ult,rld}/date=YYYYMMDD/data.parquet` (ULT WIRED 2026-07-02 — it IS from the lots converter mode-3, NOT B_03; the old "B_03-sourced" note was WRONG and the ult mode was never invoked → silver/ult froze 85d. Now run every time.) |
| Last-known state | **as of 2026-07-24T16:1xZ (0.6.2_AE_PartnerETL~C, GC-BF1): all 7 silver tables through `20260723`**, 42/42 partitions landed for the six trading days 07-16/17/20/21/22/23. mdpf 49financial gate exercised on the DEPLOYED trigger bytes: `latest_partition=2026-07-23, behind=1, max_lag=2, fresh=True`. Also cleared a large historical backlog: **225 uln + 225 ult + 221 rld** dates built (those tables are now COMPLETE, not merely current — `ult` feeds `B_02.canonical_lots`). **Canonical (step 7.5) ALSO caught up 20260715 -> 20260723 — 54/54 partitions across 9 tables**, via the per-date workaround in Step 7.5 (each run 25/25). (update this line each run) |
| ⚠ **NO BRIDGE. THE "TRN READS LOCAL" WARNING IS RETIRED** | The prior version of this row said, in capitals, *"TRN's converter reads the LOCAL OneDrive folder, not S3"*. **That was true only until 2026-07-17**, when the A4 L5b re-point moved **every** converter to monolith bronze (`convert_schwab_trn_to_parquet.py:70-76`). The row was dated **2026-07-16 — one day before the change** and was never updated, so on 2026-07-24 it was relayed by CTO (who authored the re-point) and restated by COO three times. **Corrected at CTO's direction, 154535Z.** Doctrine banked from it: **a stale record is most convincing when it is relayed by the author of the change that retired it.** Had the bridge been built, the converters would have succeeded anyway and the bridge would have been *credited* — re-certifying a dead channel with a fresh success. |
| 🔒 **0824-ONLY IS STRUCTURAL — BUT ONLY AGAINST THE UNKNOWN-PURPOSE FAILURE** | `_monolith_bronze.py:29-45` — `master_for()` maps `model_portfolios -> 08242234` and **raises `KeyError` on anything unmapped ("NO default, NO literal")**, so these bd-tree converters cannot reach `0833` by accident. `_unzip_at_read` (:68-82) likewise **REFUSES** a multi-member zip rather than silently picking one. ⚠ **DO NOT OVER-READ THIS, as I did on 2026-07-24:** the gate refuses an **UNKNOWN** purpose; it **cannot refuse a WRONG-but-known one**. `master_for('advisor_intelligence')` is an equally legal call returning `08335338`. **The neighbouring `data/canonical/schwab/` tree IS 0833** (`build_fact_position.py:35-40`) — so the two masters live one directory apart and the gate will not stop a caller who names the wrong one confidently. Derive the purpose from the module's own declaration; never a literal at the call site. |

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

## Step 1 — ~~Sync OneDrive -> S3~~ **INERT AS OF 2026-07-17 — SKIP IT**

>> **THIS STEP NO LONGER FEEDS ANYTHING IN THIS CYCLE. DO NOT RUN IT AND DO NOT COUNT IT.**
> After the A4 L5b re-point, all seven converters read **monolith bronze**; the `01_raw/` prefix this step
> writes to is read by **no converter here**. The local folder it reads *from* stopped receiving deliveries
> after `CRS20260715`, so it would upload nothing anyway.
> **Verified by running the full cycle WITHOUT it on 2026-07-24: all seven legs succeeded, 42/42 partitions
> landed.** That is the proof it is inert, not an argument that it is.
> **It is not merely undated — it is dead for this cycle.** Kept below only because `01_raw/` still has one
> live consumer (`build_canonical_daily.py`'s date enumeration — see Step 7.5), and retiring the step
> outright is a decision for whoever fixes that. **"Seven steps" now means Steps 2-7 + 7.5.**

<details><summary>Retired Step 1 (do not run; kept for the 01_raw decommission decision)</summary>

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

</details>

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

>> ⚠ **EXPECTED-AND-EXPLAINED: `TRN` reports `ERR=61` (`NoSuchKey`), all on 2024-era dates.** Do not chase
> it as a new fault and do not fold it into a GREEN. **Measured 2026-07-24 (0.6.2~C), full census:**
> **719 monolith-bronze partitions are PRESENT BUT UNREADABLE** because they were landed under the *raw*
> name `CRS{d8}.{FEED}` instead of the puller grammar `{master}.CRS{d8}.{FEED}.zip` that
> `monolith_bronze_key()` builds — so `GetObject` raises `NoSuchKey` on data that is sitting right there.
> ```
> feed  partitions  conforming  NONCONFORMING  range
> acc      633         514          119        20240116..20240705
> rps      634         514          120        20240112..20240705
> trn      633         514          119        20240116..20240705
> uln      634         514          120        20240112..20240705
> ult      634         514          120        20240112..20240705
> rld      883         762          121        20230117..20230711
> ```
> **ONLY TRN SURFACES IT, AND THAT IS THE DANGEROUS PART.** The other five feeds already hold those dates in
> silver (converted years ago from the old `01_raw` source), so they *skip* instead of erroring — the fault
> is **masked by silver already being populated**. Confirmed by control: `silver/trn/date=20240116` is
> absent while `silver/{acc,rps,uln,ult}/date=20240116` each exist.
> **Consequence: a `--force` rewrite, or any silver rebuild, would fail on ~120 dates PER FEED.** The
> historical backfill is one bad-rename away from being unreadable across the whole tree. Routed, not fixed
> here (bronze is immutable under Rule 17a — this is a re-land/alias decision, not an edit).

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

>> ⚠ **KNOWN DEFECT (found 2026-07-24, 0.6.2~C, source-confirmed — READ BEFORE RUNNING).**
> **`build_canonical_daily.py:154-156` still enumerates raw dates from the DEAD channel**
> `s3://opal-data-schwab/01_raw/*.RPS`, which is frozen at `20260715`. The A4 L5b re-point moved the
> *fact builders* to monolith bronze (`build_fact_position.py:32,59` uses `MONOLITH_BUCKET` +
> `monolith_bronze_key`) but **did not move the orchestrator's date picker.**
> **SYMPTOM:** a run with `--date 2026-07-23` builds **silver facts for 2026-07-15** and then runs GOLD at
> `t1=2026-07-23`, so every gold step that reads `fact_position/date=2026-07-23` dies `NoSuchKey`.
> Measured: **20/25 steps OK, 5 ERR** (`build_gold_holdings`, `account_gains`, `build_gold_canonical_lots`,
> `build_gold_firm_composition`, `build_gold_client_tax_liability`).
> **`=== done: N/M steps OK ===` IS NOT A PASS LINE — READ IT.** It exits reporting partial success.
>
> **WORKAROUND UNTIL FIXED (no code change, used successfully 2026-07-24):** `dates_to_build()` falls back
> to `[t1_iso]` when its (stale) enumeration yields nothing, and the fact builders themselves read monolith
> bronze correctly — so **invoke the orchestrator ONCE PER DATE, in ascending order**, and each run advances
> the canonical frontier by one day:
> ```bash
> for d in 2026-07-16 2026-07-17 2026-07-20 2026-07-21 2026-07-22 2026-07-23; do
>   python data/canonical/schwab/build_canonical_daily.py --date "$d" --upload
> done
> ```
> **Do NOT "fix" this by re-syncing `01_raw`** — the local folder is dead, so the sync cannot repopulate it;
> that is treating the symptom with an instrument that is itself retired.
> **FIXED by `0.4.0_DS_ClientPlatform` @ `3b0113227`** (date axis re-pointed to monolith bronze `rps`
> partition directories; 14 tests, 5/5 mutants). Kept here because the *symptom* is what a future runner
> will see if it ever regresses.
>
> ⛔ **AND A CORRECTION TO MY OWN ROUTING NOTE, because it was dangerous:** an earlier version of this block
> suggested re-pointing at `opal-data-bd/schwab/silver/rps/` or via `master_for('model_portfolios')`.
> **BOTH ARE 0824. THE CANONICAL STORE IS 0833** (`build_fact_position.py:35-40`,
> `PURPOSE = "advisor_intelligence"`, and its docstring is explicit: *"No MP consumer exists on this
> store"*). Either would have been a **0833 -> 0824 SUBSTITUTION** — the standing never-substitute
> prohibition, not merely a wrong path. DS did not take the suggestion; they anchored on the module's own
> `PURPOSE` and pinned it with a test that fails if anyone swaps in `08242234`.
> >> **THE GENERAL LESSON, and it qualifies the 0824-only row above: `master_for()` refuses an UNKNOWN
>    purpose. It CANNOT refuse a WRONG-but-known one.** `master_for('model_portfolios')` is a legal call
>    that returns the wrong book for the canonical tree. **The gate stops typos and omissions, not a
>    confident caller naming the wrong business purpose.** Always derive the purpose from the module's own
>    declaration — never write a purpose literal at a call site, and never in a recommendation.

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
