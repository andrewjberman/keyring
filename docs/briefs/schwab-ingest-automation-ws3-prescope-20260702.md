# WS-3 Schwab-Ingest Automation -- PRE-SCOPE DESIGN (design-only, Andrew-gated)

**Author:** 0.6.2_AE_PartnerETL (Schwab-ingest specialist) | **Date:** 2026-07-02
**Status:** DESIGN-ONLY -- NOT a build. Andrew-gated on the WS-3 Option call (A automate vs B accept-monitored-defer; routed COO->MSTR->Andrew).
**RAVC:** COO (owner) + CTO (arch) + 0.5.0_AE (WS-3 owner, grounding). Coordinates 0.4.0_DS~A (C3 TRN-A->S3, prerequisite).
**Why now:** the 2026-07-02 4th-stall proved the risk -- MDPF 49F custody froze at 06-30 because the DELIVERY-TRIGGERED/manual Schwab-ingest (`/49-schwab-conv`) did not run for 07-01, and nothing alarmed. Silent-stall is the failure mode this design removes.

---

## 1. Current state (grounded, two half-automated paths)

**Path M (production, MANUAL -- the fragile link):**
`OneDrive local delivery C:\Users\AndrewBerman\OneDrive - Opal Capital\Documents\Schwab Data Delivery\08242234\`
-> `sync_schwab_onedrive_to_s3.py --upload` -> `s3://opal-data-schwab/01_raw/` (+ `*.RPS` mirror -> `bronze/rps/`)
-> 6 silver converters (`convert_schwab_{acc,rps,trn,trn_nna}` + `convert_schwab_lots_to_silver {uln,rld}`) -> `s3://opal-data-bd/schwab/silver/{acc,rps,trn,trn_nna,uln,rld}/date=YYYYMMDD/`
-> `build_canonical_daily.py` (Step 7.5 canonical/gold).
Trigger = **a human runs `/49-schwab-conv`.** No cron, no alarm. Floored at 06-30 today because nobody ran it.

**Path V (automated DOWNLOAD, VALIDATION-only):**
`canonical-schwab-si2` box `i-0f3d57a97f14727af` (SI2 Desktop app, GUI auto-download via `click-download.ps1`)
-> `sync-to-s3.ps1` -> `s3://opal-data-schwab/01_raw_quartz_validation/` (the VALIDATION prefix, NOT prod).
Trigger = EventBridge `canonical-schwab-si2-download-schedule` cron(35 8,20 UTC), SSM RunPowerShellScript. 14h absence alarm exists.
**Repoint validation->prod is HELD** on N=5 clean box-days (Andrew Caution-B; `EC2_MANIFEST.json`, `org/seams/canonical-schwab-ssot-ec2.md`).
Hardened today: `schedule.tf` v1.1.0 quiesce-wait (0.6.2 race-fix) -- the box now syncs same-cycle reliably, which is what earns clean N=5 days.

**The two gaps that make Path M fragile + Path V not-yet-production:**
1. Path V writes the validation prefix, not prod -> prod only advances via Path M (manual).
2. Even if raw is fresh, the 6 CONVERTERS + canonical are MANUAL (Path M steps 2-7.5). And `convert_schwab_trn_to_parquet.py` reads **LOCAL OneDrive disk** (`DEFAULT_SRC_DIR`) -> it CANNOT run headless (a bridge advancing only S3 silently no-ops TRN Layer-A -- hit today).

**ROOT-CAUSE FINDING (2026-07-02 ground-first, CONFIRMED behaviorally -- the crux blocker):** Path V and Path M are TWO SI2 clients on the SAME 08242234 enrollment, and they CONTEND for the SI2 "Download all new files" pool -- whichever client downloads a given day's file first CONSUMES its new-flag, so the other never sees it. Evidence (live file-presence): RPS by client -- 06-25 OneDrive-only / 06-26 BOX-only / 06-29 BOX-only / 06-30 OneDrive-only / 07-01 BOX-only = ZERO dates gotten by both; a near-perfect COMPLEMENTARY split across 5 dates. SOURCE-CONFIRMED sub-fact: CRS20260630.RPS is ABSENT on the box locally ("never had it") -> a DOWNLOAD gap, not a sync gap (today's sync-race-fix does NOT address it). CONSEQUENCE: while both clients run, NEITHER gets a complete daily set -> **N=5-clean-days is UNACHIEVABLE until the box is the SOLE SI2 client.** (The exact SI2-internal ack mechanism is an implementation detail; the contention is behaviorally grounded.) This is deeper than the sync-race and is the true reason the N=5 hold hasn't cleared.

## 2. Design target (Option A): a durable, automated, daily, fail-loud Schwab-ingest

Make Path V the production ingest end-to-end (download -> prod raw -> silver -> canonical), retiring the manual Path M, with fail-loud monitoring so a stall is never silent.

### A. Ingest mechanism (raw -> prod S3)
- **Promote Path V to prod:** repoint `sync-to-s3.ps1` dest `01_raw_quartz_validation/` -> `01_raw/` (+ `*.RPS` -> `bronze/rps/`), the exact repoint held on N=5. PREREQUISITE: the N=5 clean-day gate clears (the v1.1.0 race-fix is what makes clean days reliable). Byte-parity already proven (today: CRS20260629 full-set validation==OneDrive, all 11 ext identical) -> the box path produces prod-identical files.
- Path M (`sync_schwab_onedrive_to_s3.py`) retained as a **manual fallback** (revert path if the box misses), not the daily driver.

### B. Trigger + converter automation (raw -> silver) -- the NEW automation
- **S3 ObjectCreated trigger** on `s3://opal-data-schwab/01_raw/CRS*.RPS` landing (RPS is the last-written per-cycle set anchor; or a manifest-complete marker the sync writes on quiesce) -> fires the converter runner.
- **Converter runner:** run the 6 converters headless. Two options:
  - (B1) EXTEND the SI2 box's EventBridge cycle: after the sync completes, the same SSM cycle kicks the converters (python on the box, or SSM-invokes a converter step). Zero new infra; fires exactly when raw lands. Pairs with the existing box.
  - (B2) A DEDICATED converter Lambda/EC2 triggered by the S3 raw landing (decoupled; the DS/AE lane owns the converter code). More isolated, more infra.
  - RECOMMEND B1 for parity with the existing box + the "zero new infra" COO Option-A precedent (Step 7.5 canonical already fires this way).
- **HARD PREREQUISITE:** `convert_schwab_trn_to_parquet.py` must read `s3://opal-data-schwab/01_raw/` (NOT local OneDrive) -- this is **0.4.0_DS~A's C3 re-point (CTO-approved)**. Without C3, TRN Layer-A silently no-ops headless. C3 is a blocking dependency for this design.

### C. Canonical refresh (silver -> canonical/gold)
- Chain `build_canonical_daily.py --date $LATEST --upload` as the TAIL after the 6 converters verify (the existing Step-7.5 pattern -- "fires when fresh Schwab silver lands"). Same runner as B1, or an S3 trigger off the silver landing.

### D. Fail-loud monitoring (the core of "durable")
The 4th-stall lesson: a stall must ALARM, never sit silent. Layers:
1. **Download-cadence** (exists): EventBridge `TriggeredRules < 1 / 14h` absence alarm.
2. **Raw-freshness** (NEW): `01_raw/` (or `bronze/rps/`) latest CRS date not advancing on a business day past the vendor-lag window -> alarm (distinguishes vendor-not-posted (clean-skip) from box-broken).
3. **Silver-freshness** (NEW, the key one): `schwab/silver/rps/date=` not advancing -> alarm. **Tie the threshold to the WS-3/MDPF SLA (0.5.0): RPS must land within 2 TRADING DAYS** (the mdpf-daily-trigger's `BD_MAX_LAG=2` convergence tolerance). Alarm must fire BEFORE the 2-trading-day boundary so a stall is caught while MDPF still holds known-good, not after it DEFERs. Calendar-aware (weekends within tolerance). Catches the converter step silently failing -- today's exact gap. Mirror the `mdpf-freshness-checker` cron pattern.
4. **Raw-vs-silver parity** (NEW): raw landed for date D but silver/{6 tables} missing date D -> alarm (catches a partial converter run, e.g. the TRN-A no-op).
5. **Downstream** (exists): `mdpf-freshness-checker` cron(45 16) on the served MDPF rollup -- the ultimate 49F-custody-freshness backstop.

### E. Vendor-cadence handling (honest, not a bug)
- Schwab posts business-day data ~next AM (07-01 data on 07-02; 07-02 on ~07-03). Weekends/holidays = no delivery.
- The download quiesce-wait (v1.1.0) already handles "no new file this cycle" gracefully (8-min no-data early-out, logged, sync no-ops). The raw-freshness alarm (D2) must be **calendar-aware** (skip weekends/holidays, allow the ~1-day lag) so a legitimate no-delivery day is a clean-skip, not a false alarm.

## 3. Dependency order (if Andrew GO's Option A)
1. **C3** (0.4.0_DS~A): TRN-A -> S3 01_raw/ [BLOCKING -- headless converters need it].
2. **N=5 clean-day gate clears** (Andrew Caution-B) -- the v1.1.0 race-fix earns clean days; DT/CVO track the counter.
3. **Repoint** Path V sync -> prod `01_raw/` (never-widen sign-off: it moves the prod raw source; CTO+COO).
4. **Converter automation** (B1: extend the box EventBridge cycle) + **canonical tail**.
5. **Fail-loud alarms** (D2/D3/D4, calendar-aware).
6. Retire Path M to manual-fallback; update `/49-schwab-conv` skill to reflect the automated daily path.

## 4. Risks / open questions (for the WS-3 Option call)
- **Repoint irreversibility:** promoting the box to prod raw is the held Caution-B decision -- this design ASSUMES Andrew clears N=5; it does not pre-empt it.
- **Converter-on-box vs Lambda** (B1 vs B2): B1 couples ingest+convert on one GUI box (simpler, but the box is a Windows GUI box -- running python converters there is feasible but unusual; B2 is cleaner separation). CTO arch call.
- **Single point of failure:** the SI2 box is one GUI instance. Path M manual-fallback mitigates; a second box is over-engineering for a daily feed.
- **08242234 scope:** the box downloads ~30 accounts but syncs 08242234-only (NEVER-WIDEN). The automation preserves this scope exactly.

## 5. SLA + safety reconciliation (WS-3 / MDPF consumer -- 0.5.0_AE grounding)

The automation exists to serve MDPF 49F custody freshness. 0.5.0 (WS-3 MDPF-custody-durable owner) sets the consumer contract; this design meets it:
- **Freshness SLA:** `schwab/silver/rps/date=D` lands within **2 trading days** of trading day D, reliably. This is the `mdpf-daily-trigger` convergence tolerance (`BD_MAX_LAG=2`). Within it -> MDPF custody advances. Weekends are within tolerance (clean-skip).
- **Beyond-SLA behavior is SAFE by design, not silent:** if RPS stalls past 2 trading days, the mdpf convergence gate + the **leg-2 Stage-2.5 safety-gate** (fresh-but-wrong cannot replace known-stale) make MDPF **DEFER** (hold known-good) and the `mdpf-freshness-checker` alarm fires -- a MONITORED stall, never a silent stale-serve. My D3 silver-freshness alarm fires EARLIER (before the boundary) so the ingest is fixed before MDPF has to defer.
- **Mechanism-agnostic consumer:** MDPF consumes whatever lands in `schwab/silver/rps`; the mechanism (promote the SI2 box to prod, or another) is the Schwab-lane call. 0.5.0 defers it. So this design owns the mechanism; WS-3 owns the consumer-side safety-gate. The two PAIR: the gate protects MDPF whether ingest is automated OR reliably-manual.
- **Interlock:** WS-3's generalized leg-2 protection-gate is the backstop for THIS automation too -- if a future automated run lands fresh-but-wrong Schwab data, the gate blocks the bad replace. So automating ingest does not weaken the served-correctness guarantee.

## 6. Harden-phase design -- FINISH-THE-BOX (COO GO 2026-07-02; design-ready, execution Andrew-gated)

Goal: a contention-free box that produces a COMPLETE daily set (incl the MDPF-critical RPS), accrues N=5 clean days, then repoints (Caution-B). Root cause = SI2 shared-new-files contention (sec 1, exercise-confirmed). Fix = make the box the SOLE SI2 client, WITHOUT starving prod during the accrual.

### 6.1 Sole-client mechanism (PREFERRED -- the natural finish-the-box end-state)
- **Quiesce the manual OneDrive desktop SI2 pull on 08242234** so the box owns the full daily download (no manual client consuming new-flags first). Concretely: Andrew stops his desktop SI2 client from auto-downloading 08242234 (disable its scheduled/auto pull, or set it read-only/no-download for that enrollment). The box's `SchwabAutoDownload` then sees the complete daily "new files" set.
- **EXECUTION IS SOVEREIGN-GATED:** stopping Andrew's desktop pull is HIS action + ties to the Caution-B pace (MSTR carrying to Andrew). Design-ready + arch-gated NOW; DO NOT quiesce Andrew's pull without his OK.

### 6.2 Prod-continuity through the accrual (the trap -- MUST solve)
The box writes the VALIDATION prefix until the repoint (held). So if the manual pull stops for the sole-client accrual, prod `01_raw` goes UNFED for the N=5 window -> MDPF 49F custody re-freezes (the exact 4th-stall). SOLUTION: a **temporary daily bridge** during accrual -- the same validation->prod promote + converter run I executed today (2026-07-02), run DAILY (automated, event-driven off the box's clean daily sync) so prod stays current WHILE the box proves out sole-client. After N=5 + repoint, the bridge is retired (the box feeds prod directly). This decouples "prod stays fresh" from "box earns its N=5" -- both happen in parallel, no gap.

### 6.3 N=5 clean-day accrual plan
- **"Clean box-day" defined:** for trading day D, the box's daily output contains the FULL expected CRS set for D INCLUDING RPS (the file it starved on), each byte-parity-consistent with the vendor delivery. (RLY/RTY are periodic; the gate keys on the CORE set: ACC/RPS/TRN/ULN/RLD/SEC/UPN/UPT/TCF/TCFX, calendar-aware.)
- Accrue **5 consecutive clean sole-client trading days**. The per-date completeness check (6.4) IS the accrual tracker -- a missing RPS resets the counter (exactly what 06-30 would have done).
- Only from a CONTENTION-FIXED box (sole-client or fetch-by-date) -- clean days under the current 2-client contention are meaningless (the box will keep missing manual-claimed files).

### 6.4 Fail-loud (per-date completeness -- the accrual tracker AND the prod monitor)
- **Per-date completeness alarm:** for each trading day, verify the box output (then, post-repoint, prod `01_raw`) has the full CORE CRS set incl RPS; a missing MDPF-critical file -> alarm (catches the 06-30-class silent gap). Calendar-aware (weekends/holidays clean-skip).
- Ties to the WS-3/MDPF SLA (sec 5): alarm fires within the 2-trading-day window so a stall is fixed before MDPF DEFERs.
- Complements the existing 14h EventBridge absence alarm + the silver-freshness alarm (sec 2D).

### 6.5 Fetch-by-DATE fallback (contention-immune, if Andrew declines to stop the manual pull)
- If Andrew keeps his manual desktop pull, make the box download CONTENTION-IMMUNE: re-pull each date's full set by DATE, not by the "new files" flag -> the box gets complete sets regardless of what the manual client consumed. Both clients co-run, no prod gap, no Andrew behavior change.
- PREREQUISITE TO GROUND: does the SI2 Desktop app support a date-scoped re-pull (vs only "download all NEW")? Unknown -- a box-side capability probe decides feasibility. If the SI2 app cannot re-pull by date, this fallback needs a different download mechanism (heavier).

### 6.6 Sequencing (execution, Andrew-gated)
1. [SOVEREIGN] Andrew answers the Caution-B pace + agrees to stop the manual pull (or picks fetch-by-date).
2. Quiesce manual pull (6.1) [or implement fetch-by-date (6.5)] + stand up the temporary daily bridge (6.2) so prod stays fed.
3. Accrue N=5 clean sole-client days (6.3), tracked by the completeness alarm (6.4).
4. [CTO arch-gate + CTO+COO never-widen] Repoint `sync-to-s3.ps1` validation->prod `01_raw` (+RPS->bronze/rps) -- the held Caution-B repoint.
5. Retire the temporary daily bridge + the manual OneDrive path (now redundant). Automate the converter+canonical steps (sec 2B/2C). C3 (TRN-A->S3) gates the headless converter.

## 7. Deliverable status
DESIGN-READY. If Andrew GO's Option A -> this becomes the build TO (owner: 0.6.2/0.5.0 AE lane; C3 gates it). If Option B (defer) -> the fail-loud monitoring (D2/D3/D4) is the MINIMUM to add even under manual ingest, so a manual-skip alarms (the 4th-stall would have alarmed at D3). RAVC COO+CTO+0.5.0.
