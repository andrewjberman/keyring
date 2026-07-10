# 0.6.0_AE_PartnerETL -- 2026-07-09T23:03Z .. 2026-07-10T00:05Z: respawn, watch, and the per-partner gate review

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, COORDINATE

## Window

Respawn after a ~34-minute deaf window (Monitor absent from 22:29Z). Read all undelivered inbox
messages IN ORDER before touching any workstream -- my last known state was CANCELLED work on a
sovereign-closed subject. Nothing from it was resumed. No commits authored in this window prior to
this log; no deploys; no vendor calls; no writes to any out-of-scope prefix.

## Scope discipline (sovereign, standing)

**49 Financial / Schwab / RPS / `data/black_diamond/` / `opal-data-bd` / `opal-data-schwab` are OUT OF
SCOPE** (Andrew ~22:23Z, relayed CTO `223510Z` + COO `225425Z`/`231741Z`). Cancelled, not parked:
intersection selector, WS-E residual abstain guard, `partner_custody_as_of`, the census, the RPS
`business_date` spec, the Schwab Business-Date question. **YCharts and ANY external vendor API:
prohibited without Andrew's explicit per-use word.**

Held: no file under those trees opened; no bd/schwab write; neither `bd-49f` ledger touched; the
bd-49f L6/S5 served-verify NOT run (cancelled). bd limb of the watch = pure observation only.

## 1. THE CURVE WATCH IS A LIVE VENDOR CALL -- surfaced, and CTO killed it permanently

Curve pt3 was due 23:00Z. Before running it I read the instrument. It is not an S3 read.

SOURCE-CONFIRMED, `data/cot/scripts/bronze/cot_bronze_ingest.py`:
- `:698` `xlsx = download_export(cookie, guid)` -- live `GET /Api/DataMining/ExportResults/{guid}`,
  preceded by `run_query()` which POSTs a query and MINTS a `run_id`/`guid` on Black Diamond's
  platform (state on the vendor, not a read of our artifacts).
- `:710-716` a 0-row SNAPSHOT table is REJECTED pre-write -> `return None`. It never lands in S3.
- `:448` docstring: "BD's empty export is a well-formed ~4,592-byte workbook."

Elimination: my own pt2 logged `49f allocations 07-09 -> 0 rows, 4,590 B`, but no
`ALLOC_DAILY_2026-07-09.xlsx` exists in `opal-data-bd` (49F allocations last landed 2026-06-18);
cot bronze-run logs are one per night (fixed content); and the byte counts DRIFTED 4,304 -> 4,300 ->
4,302 across observations (fresh zip timestamps per download). A byte count for an artifact that was
never written, drifting per observation, has one source.

**I did not run it.** pt0/pt1/pt2 predate both prohibitions; pt3 would have breached both. CTO killed
the curve permanently (`233700Z`) and ruled the S3-only substitute IS the watch. It also violated
NEVER#4 from design (an ad-hoc vendor export, run hourly, to validate work).

Banked: `memory/feedback_curve_watch_is_a_live_vendor_call_killed.md`.

## 2. THE WATCH -- S3-only. pt3 23:19:38Z, pt4 23:59:58Z. CLEAN, no delta.

```
forwardfill_v2 (silver-read seam)          silver parquet footer row_count
cot alloc  @07-09  4,305 B  HEADER-ONLY    cot allocations 07-08=0  07-09=0   (0-row stubs)
cot unreal @07-09  3,745 B  HEADER-ONLY    cot unrealized  07-08=0  07-09=0
cot txn    @07-09  2.79 MB  REAL           bd  allocations 07-08=6,870  07-09=0
bd  unreal @07-09  3,748 B  HEADER-ONLY    bd  unrealized  07-08=103,490  07-09=0
bd  unreal @07-08  38.6 MB  REAL
bd  alloc  @07-09  ABSENT (rejected pre-write, never landed)
```

**Both planes' bronze guard is ARMED.** `cot_bronze_ingest.py` deployed 09:11:33Z (cot) / 09:11:54Z
(bd), 56,885 B, `comp-pipescript deployed` = MATCH. cot's 02:01Z and bd's 00:11Z runs are PRE-guard
(explains the stubs). bd's 09:14:56Z run is POST-guard: `_BRONZE_COMPLETE` reads
`tables:["unrealized"], count:1, as_of:{unrealized:"2026-07-08"}` -- it REJECTED the 07-09 0-row
snapshot and landed the real 07-08. **The guard's first production firing, and it worked.**

`txn_posting_watch` pt2: bd `silver/transactions/2026-07-09.parquet` = 204,043 rows, max `trade_date`
= 2026-07-07, `settle_date` reaches 07-08. **07-09 NOT POSTED. Baseline holds. [FREEZE-RISK] NOT
entered.** Missed txnwatch pt1 (22:30Z) -- deaf. Stated, not back-filled.

**A partition NAMED 2026-07-09 carries content no newer than trade_date 2026-07-07, on BOTH planes,
in a PERIOD table.** I initially generalized this as "`return_date` is a content-bound as-of";
**I then falsified my own generalization**: `return_date` is single-valued on bd (07-07 x 204,043)
but MULTI-VALUED on cot (07-01: 3,754; 06-30: 2,366; 06-26: 1,758). It is not an as-of. The claim
that survives: **a PERIOD partition's name is a run-date label, not a content vintage; the content
vintage is `max(trade_date)` and nothing binds to it.**

**`bd-cot-freshness-probe` still measures the filename** -- cot's alarm reads GREEN tomorrow
regardless. Nobody may close anything on cot's alarm state. Port is 0.8.0's, daylight.

## 3. THE GATE REVIEW -- I blocked the apply, and my live blocker was imaginary

Stood down on authoring per CTO `230737Z` (designer != author). Reviewed `0.5.0`'s `b8c2d3b09`.

**Answered the three designer questions, grounded (`233244Z`):**
- Q1: `wsd_partner_held_etf.py:31` -- "firm_id=49financial only. Inflection is Eclipse/Fidelity
  custody with no RPS." Plus `:69 PARTNER_FIRM_ID`, `:72-73` reads `opal-data-bd/schwab/silver/rps`.
  **WS-D.2 IS a 49F feeder -> SKIP.** WS-D.1 (`opal-data-etfs` -> `opal-data-mdpf`, no firm subdir) is
  cross-partner -> ALWAYS RUN.
- Q2: `build_partners` (`:322-384`) derives the firm roster ONLY from feeder frames, so skipping
  WS-B/WS-E OMITS 49financial. Option (A) (inject the block from the last-good AGGREGATE) is the only
  option that restores it. **Roll source = 2026-07-06, NOT the most-recent partition.**
- Q3: roll-forward-block supersedes null-abstain; EMIT-THE-ROW's live content is "never OMIT the row";
  `0.0` is not an acceptable stand-in for `null` (`_empty_partner` `:314-319` yields 0.0, a number that
  sums into `total_aua`).

**The 07-06 evidence (differenced three SERVED `aggregate_aua` partitions, `opal-data-portal-v2`):**
```
          model_aua         sma_aua        non_model_aua    total_aua         partner_custody_total
07-02     1,386,551,932.37  23,305,627.31  204,589,822.08   1,614,447,381.76  1,614,447,381.76
07-06     1,400,957,639.03  23,380,776.56  196,913,158.63   1,621,251,574.22  1,621,251,574.22
07-08     1,390,483,476.75  23,474,513.91  207,293,583.56   1,621,251,574.22  1,621,251,574.22
d(model) = -10,474,162.28  d(sma) = +93,737.35  d(non_model) = +10,380,424.93 = -(d_model+d_sma) EXACT
```
`partner_custody_total` last MOVED at 07-06 and is pinned to the cent since; the residual absorbs all
drift and the total never moves. **07-08's block has a correct total and a fabricated composition.**
CTO adopted 07-06 as the roll source and retracted his 07-08 ruling to `0.5.0`.

### The [STOP], and its refutation

I `[STOP]`-blocked `0.5.0`'s `safe-apply` (`234345Z`) on two blockers, exercised against live S3:
- (A) `_latest_bd_silver_partition:133-149` is a FILENAME picker; `bd/silver/allocations/2026-07-09.parquet`
  is a 0-row stub -> `bd["fresh"]=True` -> `stale_partners=[]` -> the skip never fires.
- (B) `_partner_asof` would stamp `2026-07-08` (min over filename-maxes) -- the fabricated-residual block.

**BOTH REFUTED (CTO `235110Z`), and I verified the refutation myself rather than accept it:**
```
/mdpf/custody_source = "schwab"  Version 4 (Andrew)   [PowerShell -- MSYS mangles leading-slash args]
  DENOMINATOR: 2 SSM params visible; /mdpf/custody_source among them
DEPLOYED artifact (get-function -> Code.Location -> unzip), NOT the repo:
  :295  bd = _check_schwab_rps(now) if custody_source=="schwab" else _check_bd_silver(now)
  grep -c "MDPF_STALE_PARTNERS|spine_fresh" -> 0        (gate genuinely NOT deployed)
LIVE trigger's own DEFER output (CloudWatch):
  49financial: prefix="schwab/silver/rps", latest_partition="2026-07-06", behind=3, fresh=false
  inflection: fresh=true   custody_source="schwab"   all_fresh=false
```
`_check_bd_silver` is NEVER CALLED. `_partner_asof:198` returns the schwab SCALAR = **2026-07-06**,
the correct vintage. The filename branch is never reached.

**I exercised the MECHANISM, not the PATH.** Running a function against live S3 establishes what it
returns; it never establishes that it runs. The falsifier was in a field named `prefix`, in a log I
had already quoted. `[STOP]` lifted; `0.5.0` told directly (`235446Z`) not to carry the dead blockers.

**I also hit the identical MSYS leading-slash trap** on `filter-log-events --log-group-name
/aws/lambda/...` (InvalidParameterException), one command after CTO described it. Re-ran in PowerShell
and printed the denominator. An empty result was a claim about my query, not about the world.

### What survived the review

- **LATENT TRAP (CTO ordered it fixed, ships with sites 2+3):** `_check_bd_silver` has NO content
  assertion, while `_latest_schwab_rps_partition:238-250` WAS hardened ("dir-exists != data-present").
  **`/mdpf/custody_source` was `"bd"` at version 1. One SSM write re-arms the fabrication.** A dead
  path that fabricates when re-armed is worse than a live one.
- **(C) BLOCKS:** `_partner_asof` returns `""` on unknown; the handler exports an EMPTY as_of and
  dispatches -> feeders skipped, no block to roll, Sentinel 2 `exit 1`. Stale + unknown as_of -> DEFER.
- **(D) BLOCKS:** `GATE_ENFORCE` gates only the spine DEFER (`:354`); the stamp/skip exports (`:394`)
  are unconditional. `GATE_ENFORCE=0` = "halt off, skip on" -- a rollback that does not roll back.
  Fix: `if not GATE_ENFORCE: stale_partners = []`.
- Nits: quote the interpolated exports (S3 keys -> `bash -c` string); sanitize the env-var suffix.
- **Sentinel 3 refusal (open, with COO):** `:216` coherence check DOES assert (`raise SystemExit`) --
  ratified. But on a rolled day Sentinel 3 emits a bare `PASS` having independently validated ~11.1%
  of the AUA (49F = 1,621,251,574.22 copied; inflection = 202,542,849.81 recomputed), and the new
  `and not rolled_blocks` clause turns an ALL-ROLLED day from a vacuous SKIP into a vacuous PASS.
  **Delete that clause.** COO's standalone point holds and is better without my illustration:
  a coherence check catches an INCOHERENT block, never a COHERENT-BUT-FABRICATED one. Coherence is
  not correctness -- true of 07-06 too.

## 4. THREE OF MY OWN CLAIMS DID NOT SURVIVE THEIR OWN CHECKS

1. **"the nightly makes ZERO reads of `opal-data-bd`/`schwab/`"** -- FALSE. `BD_BUCKET` is paginated by
   the TRIGGER itself (`:53`, `:137`, `:247`) every fire; that is HOW it detects staleness. The FEEDERS
   make zero bd reads. CTO had adopted this inside an hour as "the design's best argument"; struck.
2. **"the `[STOP]` costs nothing tomorrow"** -- FALSE, and the dangerous one. `bd` is `_check_schwab_rps`,
   not bd silver. RPS latest = 2026-07-06, `behind=3 > max_lag=2`; nothing lands an RPS partition tonight
   and RPS is sovereign-frozen. **At 15:03Z tomorrow the DEPLOYED code computes `all_fresh=false` and
   DEFERS AGAIN. Inflection has not advanced since 07-08T14:58Z and will not advance tomorrow without
   this deploy.** Not deploying is not a safe resting state; it is the status quo Andrew asked us to
   change. COO retracted "the block is the right resting state" on this basis (`259badf91`).
3. **(B), above.** And the `return_date` generalization (falsified on cot). And an as_of format-mismatch
   suspicion (falsified: both custody paths normalize via `.isoformat()`, `:179`/`:280`).

I caught (1), the `return_date` claim, and the format suspicion by going back to read the thing I had
already reported. (2) and (B) I caught only after CTO refuted the premise underneath them.

## 5. Stopping the record

COO's closing message (`235518Z`) recorded my refuted (B) as the night's headline finding and called
the non-deploy "the right outcome, not a failure." **Both corrected before the fabric closed**
(`259badf91`): (B) struck as false, `[STOP]`-lift recorded, non-deploy retracted as the failure it is.
COO explicitly declined to claim it had verified the refutation -- its AWS reader returned empty AND
its control returned empty, so the correction is attributed to my exercise of the deployed artifact.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-which` | "where does cot_bronze_ingest read its input allocations workbook / REJECT guard at :711" | **PARTIAL** | near-tie -> `comp-secrets` / `comp-symbols`; neither answers "what does this function DO / is there a probe-only path". Fell through to Read + guarded grep with `# rail-checked:` markers. |
| `comp-pipescript deployed` | `data/cot/scripts/bronze/cot_bronze_ingest.py` | **PASS** | `[BRONZE] MATCH`, 1 MATCH / 0 STALE. Established the guard is armed on cot; the deploy TIMESTAMP (09:11:33Z) then explained every stub artifact. |
| `comp-freshness` | **deliberately NOT run** | **N/A** | It binds mtime/filename -- exactly the proxy under investigation. Its `<MTIME-FRESH/CONTENT-STALE>` WARN keys on the normal bd ingest lag, not on a 0-row stub. Using it here would have manufactured confidence. Parquet footer `row_count` is the only discriminating predicate. |

**What worked:** `comp-pipescript deployed` MATCH + the S3 `code/` object timestamp was the single fact
that explained the whole artifact set (pre-guard vs post-guard runs). Cheap, decisive.

**What failed:** `comp-which` near-tied on a MECHANISM question ("what does this function do, does it
call a vendor") and routed to inventory tools. Every rail override this window carried an inline
`# rail-checked:` marker.

**GAP FOUND (routed):** no comp-tool answers **"does this code path EXECUTE in production?"** -- the
exact question that would have prevented my (A)/(B) error. `comp-blast` gives consumers; `comp-symbols`
gives inventory; `comp-iam` gives DESIRED. Nothing binds a **runtime branch predicate** (an SSM param,
an env var, a feature flag) to the branch it selects. A `comp-path <fn>` that resolves live SSM/env and
reports which branch is reachable would have made "exercised the mechanism, not the path" impossible.
This is the compiler-tool shaped hole under the night's largest error class.

## Blockers

**None.** The watch is read-only and unblocked. The gate is HELD (not blocked) pending CTO's ruling on
the `as_of` source + the three ordered fixes; that is `0.5.0`'s lane and CTO's ruling, not a blocker on
me. `[STOP]` lifted.

## Current State

- **Watch RUNNING, S3-only.** Curve pt4 `2026-07-09T23:59:58Z` CLEAN, no delta vs pt3. `txn_posting_watch`:
  07-09 NOT POSTED. `[FREEZE-RISK]` not entered. Next: curve pt5 00:30Z, pt6 01:00Z, pt7 01:30Z;
  txnwatch 01:00Z / 01:40Z; **02:30Z primary = cot half ONLY** (bd half sovereign-cancelled).
  Reusable read-only harnesses in scratchpad: `curve_pt3_readonly.py`, `txnwatch_pt.py`,
  `exercise_gate_predicate.py`. **No vendor call, ever, without Andrew's explicit per-use word.**
- **Gate `b8c2d3b09`: COMMITTED, NOT DEPLOYED.** Verified against live, not the commit message:
  `mdpf-daily-trigger` `LastModified 2026-07-01T21:14:05Z`, `CodeSha256` unchanged,
  `grep -c MDPF_STALE_PARTNERS` on the deployed artifact = 0. `mdpf` is not in
  `safe_deploy_core.PIPELINE_MAP`, so the push did not auto-deploy. Nothing half-landed.
- **`/mdpf/custody_source = "schwab"` (v4, Andrew).** The live gate reads `schwab/silver/rps`, stamps
  `MDPF_PARTNER_ASOF_49FINANCIAL = 2026-07-06`, `behind=3`. Two independent methods (the live gate;
  differencing served `aggregate_aua` partitions) agree on 2026-07-06. Why they agree is a 49F question,
  sovereign-closed, NOT pursued.
- **Tomorrow 15:03Z, deployed code:** `all_fresh=false` -> **DEFER**. Inflection does not advance.

## Next Steps

1. **[0.6.0_AE_PartnerETL]** Curve pt5 00:30Z / pt6 01:00Z / pt7 01:30Z; txnwatch 01:00Z / 01:40Z;
   **02:30Z primary, cot half only** -- read `s3://opal-data-cot/logs/cot-exporter/bronze-run/<ts>.log`
   for the `REJECT:` line and re-confirm cot silver row counts are unchanged. S3-only.
2. **[1.0.0_SA_CTO]** Rule the `as_of` SOURCE for the roll-forward. Nothing in bd silver partition names
   encodes `2026-07-06`; the schwab scalar does today, but the bd branch must not be allowed to derive it
   from filenames if `custody_source` ever flips back.
3. **[0.5.0_AE_OpalETL]** Ship sites 2+3 with the three additions: bd content-assertion
   (`_num_rows_from_footer` from `bd-49f-freshness-probe`), DEFER-on-unknown-as_of, `GATE_ENFORCE` gating
   the skip. Plus: delete the `and not rolled_blocks` clause; make Sentinel 3 report its validated
   fraction and name the rolled firms. Diff to CTO + 0.6.0. **The deploy IS Andrew's deliverable.**
4. **[0.8.0]** Port the content assertion to `bd-cot-freshness-probe` (daylight). Until then cot's
   `-stale-allocations`/`-unrealized` alarms read GREEN on a dead table.
5. **[CTO/COO]** Compiler-tool gap: a `comp-path` that answers "which branch actually executes in
   production" (resolve live SSM/env -> reachable branch). See Compiler Tools above.
