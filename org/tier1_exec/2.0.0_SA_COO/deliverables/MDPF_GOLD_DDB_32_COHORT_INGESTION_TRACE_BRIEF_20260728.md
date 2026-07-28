# MDPF GOLD-DDB: 32-COHORT INGESTION TRACE -- FINDINGS BRIEF

**Author:** `2.0.0_SA_COO` · **2026-07-28T223157Z** · **Andrew-direct ~2215Z** (*"assess the 13 stale but
present and 14 missing cohorts immediately, i need a list of each one and its ingestion path... subagent
fan-out"*)

**Method:** 5 parallel traces, each scoped to measured facts with mandatory `file:line` / exact-key /
exact-command citations, MEASURED-vs-INFERRED labelled per line, enumerate-never-construct, denominators
printed. **COO independently re-verified the load-bearing claim of each trace against live AWS before
inclusion** (subagents are `org/XXX.md`-banned as unreliable; every claim below that carries a number was
re-derived by me or is marked as the subagent's with its citation).

**Table:** `opal-assets-daily-aua`, keys `run_date` (HASH) + `cohort_id` (RANGE), 35,078 items.
**At `run_date=2026-07-28`: 32 cohorts = 5 fresh / 13 rolled_forward / 14 missing.** Reconciles exactly with
the emitter's own run log.

---

## 0. THE ONE-SENTENCE FINDING

>> **THE DAILY SCHEDULED PATH HAS ESSENTIALLY NEVER POPULATED THIS TABLE. Every real value in it was
>> written by manual backfill walks, and the table has been read as a daily product.** Three independent
>> traces reached this on three different cohort groups. **Bronze, silver and gold are healthy. The defect
>> is entirely in the scheduling + consumption layer.** <<

---

## 1. THE 32 COHORTS, WITH INGESTION PATH AND ROOT CAUSE

### GROUP A -- 49F MODEL COHORTS (8, all `missing`, `absent_reason=model_series_gap`)
`49f_intermediate` · `49f_short_term` · `49f_ultra_short_term` · `49f_lt_conservative` ·
`49f_lt_aggressive` · `49f_growth_sma` · `49f_dividend_sma` · `49f_smartx_platform`

**PATH:** SmartX (vendor) -> `opal-data-assets/smartx/platform/silver/fact_model_aum_daily/date={p}/data.parquet`
(+ `fact_model_allocation_roster` as the rmid->model bridge) -> `channel_sources.py:142-190`
`load_smartx_day_series()` -> **emitter OVERRIDE** at `lambda_function.py:1270` `apply_channel_resource()`
-> DDB. **These 8 never flow through platinum.**

**ROOT CAUSE (MEASURED):** `load_smartx_day_series` reads the **latest partition only**, and `:172-174`
**drops that partition's own max day** as unsettled (`T1_SETTLED`). Live run: partition `2026-07-28`,
`settled_max_day = 2026-07-24`. The lookup is `days.get(run_date)` with `run_date` = **today**. **Vendor T-1
lag + the frontier drop means today's value structurally cannot exist. The daily cron can never populate
these 8.**

**STOP DATE (MEASURED, identical for all 8):** last valued **2026-07-21**; first gap **2026-07-22**;
07-23 and 07-24 have **no rows at all**; 07-25 onward `model_series_gap`. 07-18/07-19 gaps are Sat/Sun and
**correct**.

**⚠ THE WALK-ARTIFACT PROOF (COO-VERIFIED):** every valued row cites `partition 2026-07-23` in its
`source_field` -- **including 07-16, 07-20 and 07-21, whose data predates that partition.**
```
run_date=2026-07-16  fact_model_aum_daily[opal_intermediate].closing_equity@2026-07-16 (partition 2026-07-23, T1_SETTLED)  292,964,986.93
run_date=2026-07-20  ...@2026-07-20 (partition 2026-07-23, T1_SETTLED)  291,276,704.89
run_date=2026-07-21  ...@2026-07-21 (partition 2026-07-23, T1_SETTLED)  293,270,105.24
```
**ONE backfill walk on 2026-07-23 wrote all of them. Nothing has re-walked since. The valued rows are walk
artifacts, not cron artifacts.**

**`49f_smartx_platform` is NOT derived from the other 7** (MEASURED): `channel_sources.py:185-188` sums
`CORE_MODEL_KEYS`, which is **5**, SMA-exclusive (excludes `opal_div_sma`, `opal_growth_sma`). Arithmetic
@07-24: 5-core = 1,405,847,457.15 = reported `core_5` **exact**; all-7 would be 1,428,959,469.37. It shares
the failure mode, not the derivation.

**⚠ FALSE PREMISE I SUPPLIED, corrected by the trace:** I named `wsb_49f_smartx_model_aua.py` as these
cohorts' feeder. **It is not.** It feeds platinum's `model_aua_positions` (a *different* artifact, in
`opal-data-mdpf`, genuinely current at 07-28). **Conflating the two is what produces the apparent
"current feeder, absent cohorts" contradiction.**

**BACKFILLABLE NOW:** 07-22, 07-23, 07-24 (source holds them, 7/7 models + core_5 verified).
07-25/26 weekend = correct. 07-27/07-28 = correct-by-design (unsettled frontier).

---

### GROUP B -- PARTNER CUSTODY / MODEL COHORTS (4, all `missing`)
`49f_schwab_custody` **(additive)** · `inflection_models` **(additive)** · `cottonwood_bd_holdings` ·
`cottonwood_bd_models`

**PATHS (MEASURED, exact keys the producer opens):**
| cohort | key | latest that exists | when `date=D` lands | vs 17:15Z run |
|---|---|---|---|---|
| `49f_schwab_custody` | `opal-data-assets/schwab/08242234/silver/fact_rps_s2/date={run_date}/data.parquet` | `date=2026-07-27` | **D+1 10:16Z** (6/6) | **+17h01m TOO LATE** |
| `inflection_models` | `opal-data-assets/eclipse/inflection/silver/fact_portfolios_full/date={run_date}/data.parquet` | `date=2026-07-27` | **D+1 03:30Z** | **+10h15m TOO LATE** |
| `cottonwood_bd_holdings` | `opal-data-assets/blackdiamond/cottonwood/silver/fact_holdings/date={run_date}/data.parquet` | `date=2026-07-24` | -- | source frozen 07-24 |
| `cottonwood_bd_models` | `opal-data-assets/gold/mdpf_revamp/cottonwood/aggregate_aua_timeseries.json` | axis max **2026-07-22** | -- | writer dead since 07-23T20:21Z |

>> **ROOT CAUSE: CADENCE, NOT PATH. The emitter demands a partition stamped `date == run_date`; the sources
>> are healthy T-1 producers that land the NEXT MORNING. Path mismatch DISPROVEN -- the deployed code's own
>> `source_field` names the same prefix the data lands under.** <<

**THE DISCRIMINATING POSITIVE CONTROL (COO-VERIFIED):** `inflection_orion_custody` reads
`orion/inflection/silver/fact_assets/date={run_date}` which lands **D 10:16Z -- 2h59m BEFORE the run.**
**It is the one cohort of the five that works** (`fresh`, $203,315,820.14). Same bucket, same code path,
same IAM, same invocation. **The only variable is arrival time.**
```
fact_rps_s2  date=2026-07-27 -> written 2026-07-28 10:16Z   (D+1, TOO LATE)
fact_assets  date=2026-07-28 -> written 2026-07-28 10:16Z   (D,   IN TIME)
```

**`no_source_partition` is a CALLER-SIDE sentinel** (`channel_sources.py:126-131` returns bare `None`;
label applied at `lambda_function.py:1332-1334`/`:1351-1354`). **It does not distinguish missing-key from
zero-row.**

**COTTONWOOD ROWS COME FROM THE EMITTER ITSELF, not platinum** -- appended post-hoc at `:1366-1369`.
`_override:1250-1253` sets `value=None, provenance="absent"` **with no `absent_reason`**, which is why these
two show "(none set)". `cottonwood_bd_models`' upstream writer
(`data/assets/scripts/gold/build_cottonwood_mdpf_slice.py`, dispatched at `mdpf-daily-dispatch.sh:525`,
**failure treated as non-fatal at `:551`**) has not rewritten its artifact since **2026-07-23T20:21:29Z**;
its `model_aua` array holds **2 non-null values in a 447-date axis** (07-21, 07-22, both 124,376,009.73).
**Even at its high-water mark this leg covered 2 days.**

**⚠ FALSE PREMISE I SUPPLIED:** I said `inflection_models` reads Orion. **It reads ECLIPSE.** Orion feeds
`inflection_orion_custody` -- a different cohort, which is fresh. **And orion's fresh table is
`fact_assets`, not `fact_positions`** (my 2,283-partition measurement was on `fact_assets`).

---

### GROUP C -- ETF HELD-BY-PARTNER (8, all `rolled_forward`)
`etf_{divz,idvz,pfde,pfoe}__held_49financial` (as_of **2026-07-06**) ·
`etf_{divz,idvz,pfde,pfoe}__held_cottonwood` (as_of 2026-07-24)

**PATH:** `opal-data-etfs/daily/{partner}/{date}.json` -> `_latest_partner_key()`
(`lambda_function.py:729-751`, newest `d <= run_date`) -> `build_ownership_rows()` `:754-842` -> DDB.
Every one of the 8 values is **byte-identical** to `ownership_value` in the corresponding S3 JSON.

>> **⚠⚠ THE EMITTER NEVER READS `etf_decomposition[].held_by_partner` FOR VALUES -- MY EARLIER
>> EXPLANATION TO ANDREW WAS WRONG AND IS RETRACTED HERE.** `lambda_function.py:694-698` verbatim:
>> *"SOURCE: measured `opal-data-etfs/daily/{partner}/{date}.json` -- CTO~B RATIFIED as the ONE canonical
>> held-source. **NEVER mdpf etf_decomposition target_weight: a target weight is INTENT, not an
>> OBSERVATION.** When the measured source is absent we emit an honest partial/missing -- never a fallback
>> to intent."* `etf_decomposition` is used at `:707-715` for `etf_total_net_assets` **only** (the
>> denominator of `ownership_pct`). <<

**ROOT CAUSE -- A DEAD PRODUCER (COO-VERIFIED ON THE APPLIED PLANE):**
```
bd-49f-etf-ownership-daily   aws lambda get-policy -> ResourceNotFoundException   <- NO invocation path
inf-etf-ownership-daily      Sid EventBridgeInfEtfOwnershipDaily                  <- event-triggered
cot-etf-ownership-daily      Sid ScheduleCotEtfOwnershipDaily                     <- cron(30 10 * * ? *)

opal-data-etfs/daily/49financial/  newest 2026-07-06.json  (written 2026-07-14)
opal-data-etfs/daily/inflection/   newest 2026-07-28.json
opal-data-etfs/daily/cottonwood/   newest 2026-07-24.json
```
**`bd-49f-etf-ownership-daily` has no EventBridge rule AND no resource policy -- it cannot be invoked by any
AWS service.** CloudWatch: **exactly ONE datapoint ever** -- 2026-07-14, Sum=7.0 -- which wrote exactly 7
partitions in one burst, then silence. Siblings: inf 17 datapoints, cot **31, one per day, unbroken.**

>> **THE 49F ROWS ARE STALE *BECAUSE THE GUARD IS WORKING*. The observed source died and the emitter
>> refuses to substitute target-weight intent -- exactly Andrew's ~2144Z source-over-estimate rule, already
>> implemented in this component. It labelled them `rolled_forward` honestly rather than silently filling
>> with model weights.** <<

**AND A SECOND, HEALTHY 49F PRODUCER EXISTS:** `wsd-49f-partner-held-etf-daily` (feeds
`by_feeder.partner_held_etf = {"49financial":"2026-07-28"}`) ran 7× incl. today. **Two independent 49F
held-ETF producers; the fresh one is the one the emitter is contractually forbidden from using.**

**Cottonwood's 2-day lag is the cot holdings feed, not a trigger fault** -- the cron fired 07-28 and
re-emitted the newest available partition.

---

### GROUP D -- ETF FUND-LEVEL (5, all `rolled_forward`)
`etf_divz` · `etf_idvz` (as_of 07-24) · `etf_pfde` · `etf_pfoe` (as_of 07-27) · `_total__etf_fund` (07-24)

**PATH:** TrueShares HTML / Pathfinder-Filepoint CSV -> `opal-data-assets/{trueshares|pathfinder}/…/bronze/…`
-> `opal-data-etfs/silver/netassets/{date}.parquet` -> feeder -> `opal-data-mdpf/mdpf/feeds/etf_net_assets/`
-> platinum -> DDB. **Puller `etfs-netassets-daily`, EventBridge `cron(0 22 * * ? *)`, ENABLED, firing
daily.** Arithmetic: 302,466,106 + 196,315,124 + 156,303,731 + 87,332,587 = **742,417,548** = `_total__etf_fund`
**exact**, and its `as_of` correctly takes **min(constituents)**.

**ROOT CAUSE A -- PERMANENT PHASE LAG (MEASURED, invariant across 5 platinum files):** puller fires
**22:00Z**; WS-A aggregate ran **16:45Z**; emitter **17:15Z**. **MDPF always consumes the previous evening's
draw. These 5 can NEVER read `fresh` -- `rolled_forward` is the correct permanent steady state, not an
incident.**

**ROOT CAUSE B -- TWO VENDOR DATE CONVENTIONS (this is the whole DIVZ/IDVZ vs PFDE/PFOE asymmetry):**
TrueShares stamps the **actual strike date** (page drawn Mon 07-27 says *"As of: Jul 24, 2026"*).
Filepoint's `ETF_Holdings.csv` `Date` is **forward-dated to the next business day** -- **a file drawn
Saturday 07-25 carries `Date=07/27/2026`, a date that had not happened yet**, while its own `DailyNAV.csv`
`Rate Date` says 07/24. **All four ETFs are at the same underlying valuation date, 2026-07-24. PFDE/PFOE
OVERSTATE freshness by one trading day; the split is a labelling artifact.**

**⚠ THIS REFUTES A RECORDED MECHANISM:** `0.5.0_AE_OpalETL/logs/2026-06-25/divz_idvz_etf_price_staleness_dx.md:33`
states *"PFDE/PFOE: `data_as_of == date` (lag 0) -- same-day valuation."* **MEASURED FALSE.** Its
*disposition* (benign) stands; its *mechanism* does not.

---

### GROUP E -- DERIVED TOTALS (2, both `missing`)
`_global__aua_total` · `_total__partner_aua`

>> **⚠⚠⚠ THE MOST SERIOUS DEFECT IN THE ESTATE TONIGHT -- `_total__partner_aua` HAS SERVED A PARTIAL SUM
>> AS THE FIRM-WIDE TOTAL. COO-VERIFIED FROM THE TABLE:** <<
```
run_date     value              vintage_state   legs_present   legacy_carried_total
2026-07-17   1,803,111,389.71   fresh           2              1,782,767,217.29
2026-07-18     137,170,028.82   fresh           1              1,782,163,983.16   <-- ONE LEG, SERVED AS THE TOTAL
2026-07-25         0            fresh           0              1,783,154,092.13   <-- Sat
2026-07-26         0            fresh           0              1,783,154,058.88   <-- Sun
2026-07-27         0            missing         0              1,783,154,058.88
2026-07-28         0            missing         0              1,783,405,733.70
```
**On 2026-07-18 this row served $137.17mm labelled "TOTAL -- partner AUA", `vintage_state=fresh`, while the
SAME artifact simultaneously certified the book at $1.78bn.** **A zero invites suspicion; a plausible
nine-figure number does not.** And on 07-25/07-26 it served **0 stamped `fresh`** -- the `missing` label on
07-27/28 is an *accident* of the repeat-detector (trading-day-scoped only), **not a disclosure.**

**MECHANISM, four steps (MEASURED):**
1. `:1036-1104` correctly sets the row from mdpf: `value = 1,783,405,733.70`, `reconciled=True`, `fresh`.
2. `apply_channel_resource` `:1332`/`:1351` blanks both contributors (the Group-B cadence failure).
3. **`:1398` `ours = round(sum((x.get("value") or 0) for x in additive), 2)` -- `None or 0` -> `0`**, then
   `:1402` `r["value"] = ours` **overwrites the good $1.78bn with 0**.
4. `_stamp_state` is **never called** after the overwrite, so `as_of=2026-07-28` and the freshness label
   continue to describe the discarded headline.

**THE SAME FILE DOES IT CORRECTLY ELEVEN LINES LATER.** `_total__etf_fund` `:1123-1129` sets `value=None`
when a constituent is absent, commented *"a partial sum of funds would read as the whole ETF book. Refuse
it."* **`_total__partner_aua` has no such guard.**

**`_global__aua_total` is the CORRECTLY-BEHAVING row** -- same input condition, same invocation: it emits
`value` absent, `provenance="absent"`, named `absent_reason=no_fee_basis_constituents` (all 3 fee-basis legs
absent), `legs_present=[]`. **The difference is solely that `global_rows` has an emit predicate and `:1398`
has `or 0`.**

---

## 2. INSTRUMENT DEFECTS -- GUARDS THAT CANNOT FIRE

**(a) THE AC7 RECONCILE IS A TAUTOLOGY.** `:1412`
`r["reconciled"] = (r["value"] == round(sum((x.get("value") or 0) for x in additive), 2))` -- **both sides
are the same expression over the same list.** `0 == 0` -> `True`. `assert_ac7` keys on `reconciled is False`,
so the write gate **cannot fire**. It also **destroys** the genuine reconcile verdict computed at `:1101`
against mdpf's independent headline. **The file's own docstring names this anti-pattern at `:600`:
*"A GUARD WHOSE TWO SIDES AGREE BY CONSTRUCTION CANNOT FAIL."***

**(b) 14 ALARMS THE SOURCE CLAIMS EXIST, DO NOT.** `:173-176` asserts the staleness sentinel *"is shared
with the 14 live `mdpf-cohort-freshness-stale-*` alarms so row and alarm agree by construction."*
`aws cloudwatch describe-alarms --alarm-name-prefix "mdpf-cohort-freshness-stale"` -> **0**. Account-wide: 50
alarms, **none** is a cohort-freshness alarm. **A stale claim in load-bearing source.**

**(c) THE 16-TRADING-DAY 49F GAP IS INVISIBLE IN `staleness`.** All four 49F ETF rows carry `staleness=99` --
a **dual-purpose sentinel** fired by `vintage_state=="missing" OR coverage_state=="incomplete"`. These rows
have been `coverage_incomplete` since launch (the `08335338` declared-but-unrepresented master). **The
vintage regression on 07-06 produced NO change in the staleness field at all.** Only `vintage_state` +
`as_of` disclose it, and nothing watches them.

**(d) THE VALUE-REPEAT ALARM DIAGNOSES THE WRONG CAUSE.** Its text -- *"The producer is stamping the FILE
date, not the DATA date"* -- is a **hardcoded string printed whenever `suspect > 0`, regardless of which row
tripped.** Today's sole suspect was `_total__partner_aua`, whose repeat is the emitter's own `or 0`, twice.
**The alarm sends the reader to `opal-data-etfs` to fix a bug at `lambda_function.py:1398`.** *(The named
mechanism is real and was verified live for the ETF partner files -- 3 consecutive files carrying an
identical value each stamped with its own file date -- it is simply not today's cause.)*

**(e) COVERAGE IS A `.get` DEFAULT, NOT A DERIVATION, ON CHANNEL/GLOBAL ROWS.** `_new_row` never computes
`coverage_state`; `_override` reads `row.get("coverage_state","unknown")` on absent paths and
**`...,"complete")` on the valued path** -- so `inflection_orion_custody` is stamped **`complete` by
assertion**, never measured against any declared-master set.

---

## 3. WHAT IS *NOT* BROKEN -- stated so remediation is not misaimed

- **Bronze, silver and gold are healthy.** 8 channels at T-1 or better; the ETF vendor puller fires daily
  and lands silver every day including weekends.
- **`_global__aua_total`, `_total__etf_fund`, and the ETF `rolled_forward` labels are all CORRECT behaviour.**
- **The 49F held-ETF staleness is a guard working as designed** (refusing intent-for-observation).
- **`inflection_orion_custody` proves the emitter's code path, IAM and freshness rule are sound.**

---

## 4. THE FIXES, IN DEPENDENCY ORDER

1. **`lambda_function.py:1398`** -- replace `(x.get("value") or 0)` with an explicit presence check and
   **refuse the total when no contributor carries a value**, mirroring `_total__etf_fund:1123-1129`. Then
   **call `_stamp_state` on the re-derived row**, and **stop overwriting `reconciled` with a self-comparison
   at `:1412`.** *(Highest leverage: this alone stops a partial/zero sum being served as a firm-wide total.)*
2. **Re-phase the emitter** -- either run it after its T-1 sources land (>10:16Z next-day), or accept T-1
   partitions instead of demanding `date == run_date`. **This is the cadence root cause for Groups A and B.**
3. **Wire a trigger for `bd-49f-etf-ownership-daily`** (or retire it in favour of the healthy
   `wsd-49f-partner-held-etf-daily`, which is an architecture call, not plumbing).
4. **Backfill 07-22/23/24 for the 8 model cohorts** -- data is present and verified.
5. **Fix the `staleness` sentinel + the false alarm claim** -- *subject to the standing MORATORIUM: this is
   correcting a FALSE CLAIM in source and a broken sentinel, NOT building new alerting.*

---

## 5. WHAT REMAINS UNESTABLISHED (carried, not hidden)

- **Deployed-vs-repo byte parity** for the emitter. `CodeSha256 mhT3rdRPMMR6hPQVqRQO7gCG2j3klc1deT00sh7B8Tg=`,
  deploy `2026-07-23T18:27:52Z` vs last commit `18:25:31Z` (+2m21s), worktree clean. **Behaviourally
  grounded** (live `source_field` strings match repo literals exactly) but **INFERRED**, not rebuilt.
- **Why platinum `aggregate_aua/` has no object for 2026-07-19 … 07-24** (jumps 07-18 -> 07-25). Correlates
  with the 0-row DDB dates. **Not traced.**
- **Why `bd-49f-etf-ownership-daily` has no trigger** -- never wired, or wired and removed? Its Terraform
  file exists and was **not** fully read; **TF-declared-vs-applied not reconciled.** Highest-value next step.
- **Why `cot fact_holdings` stopped after 2026-07-24**, and why the cottonwood pair artifact has not
  advanced since 07-23.
- **Whether any live consumer reads `value` without `vintage_state`.** The harm is structural, not
  demonstrated -- **but `dim_mdpf_aggregate_aua_timeseries.py` DOES `ddb.scan()` this table for
  `49f_schwab_custody`**, the Andrew-canonical 49F series, which has been absent 4 consecutive run_dates.
- **Whether the D+1 producer lags are intended T-1 design or themselves a regression.**

-- `2.0.0_SA_COO`, 2026-07-28T223157Z
