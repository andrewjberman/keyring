# The two twr_daily gap partitions cannot be filled by the producer, and the two dates are not one problem -- 0.4.0_DS_ClientPlatform~S

**archetype:** DIAGNOSE

**Date:** 2026-09-30
**Task Order:** `IRPT_BCKEND.TO-IB-pr-263` (round 26, workstream ~P, issued by `2.0.0_SA_COO~P`)
**Status:** BLOCKED -- stopped at the order's own refusal clause; remedy is a `1.0.0_SA_CTO` ruling
**Workspace CLOUD commit:** `6b5755c32c` (LOCAL; origin/CLOUD `410818259a` by `git ls-remote` at 15:3xZ)

---

## Objective

TO-IB-pr-263 (from surprise row S219) instructed a fill of `bmv`, `emv`, `cf_net`, `cf_gross` on the two 49F
`twr_daily` partitions that lack them -- `date=2024-07-08` and `date=2025-01-09` -- **by the producer's own path**
(`c02_twr_engine.py`), never by a hand-written parquet. Its refusal clause covered the case where those columns
"were NEVER populated for those two runs by design". That is the case, on both dates, for two different reasons.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-pipescript deployed | `comp-pipescript deployed --pipeline advi` | PASS | `[advi:gold] c02_twr_engine.py MATCH` -- the deployed object is byte-identical to the working tree, so the source I read is the running producer. This was the load-bearing tool of the session. |
| comp-pipescript io | `comp-pipescript io c02_twr_engine --pipeline advi` | WARN | Correct, empty WARN: "no s3_layout constants or hardcoded S3 paths detected". c02 writes through `runner_common.emit()`, so its I/O is invisible to a constants scan. Manual review was required, as the WARN says. |
| comp-pipescript postdeps | `comp-pipescript postdeps c02_twr_engine.py --firm 49financial` | FAIL | `--firm` enum is `{bd, inf, cot, mdpf}` -- there is **no 49financial/advi member**, though `--pipeline advi` exists on the sibling verbs and resolves to `s3://opal-data-49financial`. The DS role minimum in `org/XXX.md` is unrunnable for this tree. Gap, below. |
| comp-read | `comp-read chain_49f_entrypoint.py --for "..."` | PASS | Put me on `_pull_prev_valuation_into_mirror` (:314-401) in one call; its docstring already held the ruled answer. |
| comp-which / rail | `comp-which "how do I grep the repo"` | PASS | 104 of 104 comp-tools resolve bare; forwarder exercised live. |

**What worked:** `comp-pipescript deployed` converted "I read the source" into "I read the *running* source" in one
line -- without it the producer exercise would have proved nothing about production. `comp-read --for` found the
governing docstring faster than a grep would have.

**What failed:** `comp-pipescript postdeps --firm` has no `advi`/`49financial` member (enum: bd, inf, cot, mdpf).
`--pipeline` on `io`/`deployed` *does* carry `advi`, so the two verbs disagree about whether this tree exists.

**Gap found:** the `advi` tree is reachable from `comp-pipescript io`/`deployed` but not from `postdeps`. Filed here
rather than fixed -- it is the comp-tool owner's surface, not this order's `<paths>`. Not a blocker: `io` +
`deployed` covered the DS minimum that applies.

---

## Work Completed

### 1. The measurement: both gap partitions carry zero OK rows

Read live (bucket from `lib.opal_naming.lookup('49financial')['bucket']`, never typed):

| partition | rows | cols | status census | OK rows |
|---|---|---|---|---|
| `date=2024-07-08` | 4,074 | **11** | `{REFUSED-NO-BMV: 4074}` | **0** |
| `date=2024-07-09` | 4,076 | 15 | `{OK: 3516, ...}` | 3,516 |
| `date=2025-01-08` | 4,810 | 15 | `{OK: 4096, ...}` | 4,096 |
| `date=2025-01-09` | 4,808 | **11** | `{NO-PRIOR-TRADING-DAY: 4808}` | **0** |
| `date=2025-01-10` | 4,817 | 15 | `{OK: 4091, ...}` | 4,091 |

### 2. The mechanism, in the producer's own source

`c02_twr_engine.daily_returns` attaches `bmv`/`emv`/`cf_net`/`cf_gross` in exactly **one** `rows.append()` -- the OK
branch at `:273-276`. Every refusal branch (`:224`, `:232`, `:253`, `:257`) omits those keys, and `pd.DataFrame(rows)`
at `:277` unions only the keys present. **Zero OK rows therefore means the four columns do not exist as columns.**
The chain already says so verbatim at `chain_49f_entrypoint.py:321`: *"the emitted partition structurally lacks
bmv/emv/cf_net/cf_gross. The columns were never dropped; they were never derivable."*

### 3. The producer exercised, not inferred

Ran the runner for both dates against a mirror of the real live inputs (`canonical_valuation`, `flow_ledger`,
`dim_calendar`, `dim_account` at `date=D`), `--local-out` with **no `--upload`** -- zero S3 writes:

```
date=2024-07-08  rc=0   EMIT: rows=4074 cols=11   no D-1 BMV: {'REFUSED-NO-BMV': 4074}
date=2025-01-09  rc=0   EMIT: rows=4808 cols=11   no D-1 BMV: {'NO-PRIOR-TRADING-DAY': 4808}
```

Same row counts and same censuses as live, at deployed bytes. A re-emit would rewrite both partitions with
equivalent 11-column content and burn two ETags for no gain.

### 4. The two dates are two classes, with different remedies (Rule 24 (iv))

- **`date=2024-07-08` -- the series' first partition.** `lib/trading_calendar.py` (NYSE/pandas_market_calendars) says
  it IS a trading day with `prev_trading_day = 2024-07-05`, also a trading day -- but `canonical_valuation` holds
  560 partitions beginning at `2024-07-08`, so **no BMV exists anywhere in the estate**. `GLD-b-3`
  (`chain_49f_entrypoint.py:370`) rules this state *"CORRECT and permanent ... must never be fixed"*; `GLD-a-4`
  (`:393`) forbids manufacturing a BMV.
- **`date=2025-01-09` -- not a trading day at all.** `is_trading_day('2025-01-09') = False` (the NYSE closure for the
  national day of mourning for President Carter). The a04 `dim_calendar` correctly has **no self-row** for it and links
  `2025-01-10` back to `2025-01-08`. A `twr_daily` partition exists for a **closed market**; no return is computable
  there, so the four columns are meaningless by construction.

### 5. The denominator, swept rather than taken from the cut (Rule 24 (i))

All **560** `twr_daily` partition manifests read, 0 unreadable:
- partitions with **zero OK rows**: **2 of 560** -- exactly the two named. The issuer's census is confirmed.
- partitions on a **non-trading day**: **1 of 560** -- exactly `2025-01-09`.

### 6. Row filed, work stopped

`IRPT_BCKEND-S236` appended to the project channel (class `BLOCKING`, `hazard_standing` `ARMED`, `disarm_owner`
`1.0.0_SA_CTO`), committed `6b5755c32c`. `surprise-row-gate` PASS (1 new row of 525 checked).

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Stop at the refusal clause rather than fill | The clause's second limb is literally true. The columns are not derivable without manufacturing a BMV, which `GLD-a-4` and the engine's own REFUSE-not-fabricate guard both forbid. |
| Do **not** widen `daily_returns` to carry the four keys as NULL on refusal rows | It is the obvious fix and may well be the right one -- but a column-set change is an **emission-contract change**, and `c02:40-49` rides those on `schema_version` as a CTO-gated act (`1.0.0_SA_CTO 85212 ruling (A)`). Not this lane's to take. Offered to the CTO in the row as option 2. |
| Do **not** open a deploy ledger | NEVER-2 ledgers a deploy. There is no deploy: zero S3 writes. Opening and closing one to turn P26-3-AC2 green would be manufacturing evidence for an act that never happened. |
| Exercise the producer locally instead of reasoning from source | The refusal clause turns on what the producer *does*. `comp-pipescript deployed` first proved the source == the deployed bytes, so the local run is evidence about production. |
| Sweep all 560 partitions rather than accept the handed-in "2 of 559" | Rule 24 (i): hunt by subtraction from a printed denominator. It confirmed the census and surfaced the non-trading-day count (1 of 560) that the cut did not name. |
| Leave the TO `pending` | A terminal status is the COO's or the issuer's, never the assignee's alone. |

---

## Files Modified

| File | Change | Committed |
|---|---|---|
| `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md` | Appended row `IRPT_BCKEND-S236` (+36 lines) | Yes -- `6b5755c32c` |

**No production file changed. No S3 object written.** All five partitions in the BEFORE record
(`.../checks/r26/twr_daily_partition_etags_BEFORE_20260930.json`) re-read UNCHANGED at 15:3xZ, including the two
gap partitions -- so this lane's zero-write claim is measured, not asserted.

---

## Acceptance

| Criterion | Last line | Why |
|---|---|---|
| `P26-3-AC1` | `P26-3-AC1 FAIL: date=2024-07-08 missing columns ['bmv', 'cf_gross', 'cf_net', 'emv'] (has 11 columns, 4074 rows)` | Base line, unchanged. The fill was refused by the clause, not left unattempted. |
| `P26-3-AC2` | not run to a pass | No deploy occurred, so no change-management entry exists to close. |

No `proof_of_spec` instance was written: it is validated "BEFORE the flip", and there is no flip.

---

## Briefs Written

| Brief | Path | Audience |
|---|---|---|
| (none -- the deliverable is the channel row) | `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md` `IRPT_BCKEND-S236` | `2.0.0_SA_COO~P`, `1.0.0_SA_CTO` |

---

## Blockers

- **BLOCKED on `1.0.0_SA_CTO`** -- `IRPT_BCKEND.TO-IB-pr-263`. The order's refusal clause names the remedy as "a
  `schema_version` bump the guard can key on, which the CTO rules". Two options are laid out in row S236: (1) bump
  `schema_version` so `f49_engine.py:124-126` refuses on a version it understands rather than on an absent column,
  letting a full-history read skip or tolerate the two days deliberately; (2) widen `daily_returns` so every row
  carries the four keys (null on refusal branches), making the column set invariant. Both are emission-contract
  changes. Verified not self-resolvable: the write would be in `<paths>`, but the *authority* is not.

---

## Current State

The 49F `twr_daily` gold at `s3://opal-data-49financial/gold/advi/canonical/twr_daily/` is **unchanged and correct**:
560 partitions, of which exactly 2 carry 11 columns instead of 15 because they have no computable row to hang the
four value columns on. `date=2024-07-08` is the series' first partition (no prior valuation exists in the estate);
`date=2025-01-09` is an NYSE closure that should arguably not have a partition at all. The adapter's reader guard at
`infra/aws/lambda/investor-reporting/performance/f49_engine.py:124-126` still refuses any full-history read touching
either date with `EnginePerformanceRefused("engine table schema changed")` -- note it requires `bmv`, `emv`, `cf_net`
but **not** `cf_gross`, so it keys on three of the four columns the order names. Row `IRPT_BCKEND-S236` at
`6b5755c32c` carries the full evidence; `2.0.0_SA_COO~P` has the report.

---

## Next Steps

1. **[`1.0.0_SA_CTO`] Rule the remedy** -- option (1) `schema_version` bump keyed by the reader guard, or option (2)
   invariant column set in `daily_returns`. Row S236 lays out both with their costs. Until then FWD-3's full-history
   read stays refused on any window spanning either date.
2. **[`2.0.0_SA_COO~P`] Decide TO-IB-pr-263's terminal status** -- `superseded` (the need is met by the CTO ruling
   instead) is the likely shape; it is the issuer's to set, not this lane's.
3. **[`1.0.0_SA_CTO` / `2.0.0_SA_COO~M`] Separately and smaller: the status-vocabulary finding.** `date=2024-07-08`'s
   4,074 rows read `REFUSED-NO-BMV`, which `c02:205-217` defines as a wiring/data-availability state and as "the
   population Andrew's ratified acceptance requires to reach ZERO". The truthful state is `NO-PRIOR-TRADING-DAY`
   ("correct at a series' first partition, not a gap"). The cause is mechanical: `dim_calendar`'s null `prev` renders
   as the literal string `"None"` under `.astype(str)`, and c02's own `prev_map` (deliberately untouched per
   `GLD-b-1`) tests it as truthy. So a ratified zero-target permanently holds 4,074 rows that no remedy moves. Not
   blocking, not this order's cell.
4. **[comp-tool owner] `comp-pipescript postdeps --firm` has no `advi`/`49financial` member** while
   `io`/`deployed --pipeline advi` do. The DS role minimum in `org/XXX.md` cannot be run for this tree.
