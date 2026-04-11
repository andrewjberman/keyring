# 0.4.0_DS_ClientPlatform — Session Log 2026-04-10

**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-04-10
**Session purpose:** RD-triggered investigation of leaderboard role_breakdown accounting; full upstream trace of the BD pipeline event chain; canonical_prices deprecation audit.

---

## Current State

All ADVI_49PUSH TOs complete at session start. Most recent commit was `16957e52` (GRO floor fix, D_00c/D_04). Working tree clean on gold scripts and Lambda code.

Andrew surfaced a conversation from 0.4.2_RD about the `role_breakdown` footnote on the Employee Leaderboard. RD claimed that when a single advisor fills two role slots on the same account (e.g. implementor + local_ops), the gold script counts the full account AUA under *both* buckets rather than dividing it. Andrew's memory was that we had already fixed this to divide by N roles, but couldn't place the fix. Task: verify RD, apply fix if missing, deploy to S3 without starting the runner, and scan gold-script parity between the repo and S3.

---

## Work Done

### Part 1 — Verify RD's reading of `D_00c.portal_leaderboard.py`

Read `data/black_diamond/scripts/gold/D_00c.portal_leaderboard.py:491-528` (the `build_employee_leaderboard` account_team melt block that produces `at_role_breakdown`). Confirmed RD was correct:

- Line 502: `melt` with `id_vars=['account_id','relationship_id','total_aua']`. This duplicates `total_aua` into every role row. If Sam Owens appears on account X as both implementor and local_ops, the melt produces two rows, each carrying the full `total_aua` of X.
- Lines 516-528: per-role loop groups by advisor and sums `total_aua` directly. No dedup, no weighting. Sam Owens' implementor bucket and local_ops bucket each get the *full* account X AUA.
- Line 509-512: the *advisor-level* `tagged_aua_counts` IS deduped by `(account_id, advisor)` so the top-line number is correct. The duplication only surfaces in `sum(at_role_breakdown[adv][role].aua)`, which is exactly what the leaderboard's "tagged AUA by role" chart sums.

**Git history check for a prior equal-split fix:**
- `git log --all --oneline -S "num_roles" -- D_00c.portal_leaderboard.py` → 0 results
- Same for `role_count`, `n_roles`, `/ n_role`, `divide.*role` → all 0
- Only match for `split` was commit `9d824fc2` which split D_00 into D_00/D_00b/D_00c (unrelated file refactor, not role AUA logic)

Andrew's memory of an equal-split fix confirmed as **never committed**. The `*_split_pct` columns that show up elsewhere (C_08.advisor_fee_efficiency, D_02.advisor_client_detail, E_22/E_23 diagnostics) come from BD-provided per-role split percentages and are used only in the **fee accounting** path (`fee_earning_aua`, `implied_annual_revenue`, etc.), not the `at_role_breakdown` display count. Two different mechanisms that both mention "split" but never crossed.

**Volume of the problem (per RD's audit):** 372 of ~9,943 active accounts (3.74%) have one human in 2+ role columns. Concentration: 17 advisors, top 6 cause 86% of cases (Sam Owens 87, Alex Bright 86, Sydney Cobb 41, Collin Plotts 35, Joseph Bolling 29, Micah Damrow 25). Dominant combo is implementor+local_ops (311 of 372, 84%).

### Part 2 — Apply equal-split fix to `D_00c.portal_leaderboard.py`

Edit at `D_00c.portal_leaderboard.py:509-532`. Added a pre-aggregation step that computes `n_roles_per_pair` via `groupby(['account_id', 'advisor'])['_role'].transform('size')` on the already-filtered `melted` DataFrame, then sets `melted['_weighted_aua'] = total_aua / n_roles_per_pair`. The per-role loop at line 528 was changed from `groupby(...)['total_aua'].sum()` to `groupby(...)['_weighted_aua'].sum()`.

Invariant preserved: top-level `tagged_aua_counts` (line 512) still uses the dedup path and is unchanged. Only `at_role_breakdown[adv][role].aua` is affected, and by construction now `sum(role_breakdown[*].aua) == tagged_aua_counts[adv]` for every advisor (the dedup total).

Worked example — Sam Owens on one account, $1M total_aua, implementor + local_ops:
- Before: implementor bucket += $1M, local_ops bucket += $1M, sum = $2M (wrong, 2x inflation)
- After: each row gets `_weighted_aua = $1M / 2 = $500k`, implementor bucket += $500k, local_ops bucket += $500k, sum = $1M (correct)
- `tagged_aua_counts['Sam Owens']` still = $1M from the dedup path (no change)

### Part 3 — Commit, push, S3 deploy (no runner)

Pre-deploy check (per the c6285ae8 invariant):
- `git status data/black_diamond/scripts/gold/` → only `D_00c.portal_leaderboard.py` dirty, as expected
- `python -m py_compile D_00c.portal_leaderboard.py` → clean

Full deploy sequence:
```bash
git add data/black_diamond/scripts/gold/D_00c.portal_leaderboard.py
git commit --author="0.4.0_DS_ClientPlatform <0.4.0_DS_ClientPlatform@opal.agent>" -m "..."
# → 64d9e509 (1 file, +11/-1)

git push origin CLOUD
# → 16957e52..64d9e509  CLOUD -> CLOUD

aws s3 cp data/black_diamond/scripts/gold/D_00c.portal_leaderboard.py \
          s3://opal-data-bd/code/gold/D_00c.portal_leaderboard.py
# → etag 74910d4fc0fdf0438268490355d28840, 31283 bytes
```

Runner deliberately NOT triggered. Andrew will kick it manually or let the evening event chain pick up the new script on its normal run.

### Part 4 — Gold script parity scan (local vs S3)

Per Andrew's request after the deploy. Computed `md5sum` for every local `.py` file in `data/black_diamond/scripts/gold/`, `data/black_diamond/scripts/gold/lib/`, and the non-Python sidecar files, then pulled `aws s3api list-objects-v2` etags for `s3://opal-data-bd/code/gold/` and compared. AWS S3 etag equals md5 for single-part uploads, which applies to all gold scripts (largest is D_01 at 88KB).

| Scope | Local count | S3 count | Mismatches |
|---|---|---|---|
| `gold/*.py` (top-level scripts) | 52 | 52 | 0 |
| `gold/lib/*.py` (shared modules) | 9 | 9 | 0 |
| `gold/*.sh` + `.json` + `.md` (dispatch/config) | 7 | 7 | 0 |

Every local md5 matches its S3 etag byte-for-byte, including the just-uploaded D_00c.

**One stale artifact on S3** with no local counterpart: `s3://opal-data-bd/code/gold/05_build_client_performance.py.legacy` (45 KB, dated 2026-04-09). Explicitly `.legacy`-suffixed so nothing imports or dispatches it, but it's dead weight in the prefix. Not deleted — awaiting Andrew's go-ahead before any S3 rm.

### Part 5 — Runner state verification + trigger-chain trace

Andrew's concern: "sometimes it seems like it runs when scripts go to S3, which shouldn't be a pattern but a DS told me that once." Verified current state and traced the entire upstream event chain to answer it definitively.

**Runner state at time of check:**
```bash
aws ec2 describe-instances --instance-ids i-01003b035d2988dfb \
  --query 'Reservations[0].Instances[0].[InstanceId,State.Name,LaunchTime,InstanceType]'
# → i-01003b035d2988dfb  stopped  2026-04-10T01:50:45.000Z  c6i.16xlarge
```

Instance is stopped, last state transition was 01:50:45 UTC (end of yesterday's evening chain). No active SSM commands on the instance. The code upload cannot have triggered anything — see trace below.

**S3 event notifications on `opal-data-bd`** (from `aws s3api get-bucket-notification-configuration`):

| Notification Id | Prefix filter | Suffix filter | Target Lambda |
|---|---|---|---|
| `ProcessAllocationFiles` | `forwardfill_v2/allocations/` | `.xlsx` | `bd-allocation-processor` |
| `GoldLayerPricesTrigger` | `silver/prices/20` | `.parquet` | **`bd-gold-trigger`** |
| `PortalPublisherTrigger` | `gold/pipeline-complete` | `.json` | `bd-portal-publisher` |

Only **one** S3 notification fires the gold runner, and its prefix filter is `silver/prices/20`. That matches dated parquet files (e.g. `2026-04-10.parquet`) but deliberately excludes `canonical_prices.parquet` (starts with 'c'). Our upload to `code/gold/D_00c.portal_leaderboard.py` matches zero filters. Impossible for it to auto-trigger the runner via S3.

**EventBridge rules** (from `infra/aws/terraform/bd-pipeline/eventbridge.tf`):

| UTC | Eastern | Rule | Target |
|---|---|---|---|
| 14:00 daily | 9 AM | `historical-prices-daily` | `historical-prices-scheduler` Lambda → EC2 (writes `silver/historical_prices.parquet`) |
| 21:38 Mon-Fri | 5:38 PM | `bd-unrealized-pipeline-trigger` | `bd-unrealized-trigger` Lambda → `bd-allocations` EC2 |
| 21:45 Mon-Fri | 5:45 PM | `bd-realized-pipeline-trigger` | `bd-realized-trigger` Lambda → `bd-allocations` EC2 |
| 21:53 Mon-Fri | 5:53 PM | `bd-transaction-pipeline-trigger` | `bd-transactions-trigger` Lambda → `bd-transactions` EC2 |
| 22:00 Mon-Fri | 6:00 PM | `bd-allocation-pipeline-trigger` | `bd-allocation-trigger` Lambda → `bd-allocations` EC2 |
| 22:30 Mon-Fri | 6:30 PM | `bd-allocation-file-check-daily` | `bd-allocation-file-checker` Lambda (watchdog) |
| 23:00 Mon-Fri | 7:00 PM EDT | `bd-gold-nightly-fallback` | `bd-gold-trigger` (safety net) |
| 08:00 1st of month | 3 AM | `bd-gold-layer-monthly-trigger` | `bd-gold-trigger` with `{mode: "full"}` |

**The full event chain, end to end** (BD source → gold runner boot):

```
22:00 UTC  bd-allocation-pipeline-trigger EventBridge cron
             ↓
           bd-allocation-trigger Lambda (starts bd-allocations EC2)
             ↓
           bd-allocations EC2 downloads today's allocation XLSX from BD
             ↓
           EC2 writes s3://opal-data-bd/forwardfill_v2/allocations/<file>.xlsx
             ↓
           S3 ObjectCreated:*  (filter: forwardfill_v2/allocations/ + .xlsx)
             ↓
           bd-allocation-processor Lambda
             • Converts XLSX → silver/daily_allocations/<date>.parquet
             • Checks if silver/transactions/<date>.parquet is also present
               (that file is written independently by bd-transactions EC2
                fired at 21:53 UTC — 7 minutes earlier)
             • If BOTH ready: lam.invoke('bd-price-update', InvocationType='Event')
             ↓
           bd-price-update Lambda (ASYNC invocation, Lambda-to-Lambda)
             • Reads: silver/transactions/<date>.parquet (T1 txn-observed prices)
             • Reads: silver/historical_prices.parquet (T2 yfinance, from 9 AM job)
             • Reads: silver/prices/canonical_prices.parquet (full table)
             • Writes: silver/prices/<date>.parquet      ← THE TRIGGER FILE
             • Writes: silver/prices/canonical_prices.parquet  (updated in place)
             • Writes: silver/interpolated_prices.parquet
             ↓
           S3 ObjectCreated:*  (filter: silver/prices/20 + .parquet)
             • 'silver/prices/20' matches '2026-04-10.parquet' (starts with '2')
             • does NOT match 'canonical_prices.parquet' (starts with 'c')
             • Deliberate: both files are written in the same Lambda run, but
               only the dated file should fire gold. Filename prefix discipline.
             ↓
           bd-gold-trigger Lambda (notification id GoldLayerPricesTrigger)
             • Starts i-01003b035d2988dfb (bd-gold-layer-runner, c6i.16xlarge)
             • Writes /gold/trigger-mode.json with mode='incremental' (default)
             • If EC2 already running: writes gold/trigger-pending.json marker
               (the runner re-runs after finishing current job before shutdown)
             ↓
           bd-gold-layer-runner EC2 boots via systemd
             (this is where the existing bd_pipeline_diagram.svg picks up)
```

**What the prior DS was telling Andrew:** the pattern IS real — an S3 write does trigger the runner — but the only path that triggers it is writing a dated parquet to `silver/prices/20*.parquet`. Code uploads to `code/gold/` don't match any filter and can never auto-trigger. The confusion probably came from watching the evening chain and seeing "runner started shortly after an S3 operation" without distinguishing between dropping a silver artifact vs. uploading a script.

**Safety nets we should know about:**
- `bd-gold-nightly-fallback` at 23:00 UTC weekdays (7 PM EDT / 6 PM EST) — unconditional `bd-gold-trigger` invocation. If the S3 trigger was silently dropped because the EC2 was busy with a manual QA run, this guarantees the pipeline still runs that evening. The `trigger-pending.json` marker mechanism makes it race-safe: if EC2 is in the middle of a job, the marker is written, and the runner re-runs on clean exit before shutting down.
- `bd-gold-layer-monthly-trigger` on the 1st at 08:00 UTC — fires with `{"mode": "full"}` for a full historical rebuild from script 00 onward.

### Part 6 — Canonical prices on the gold runner: **deprecated**

Andrew asked: "don't we do canonical prices in the actual gold runner, is this now deprecated?" Full audit below.

**gold_dispatch.sh CATALOG** (lines 81-107):

```
A_00..A_04  B_00..B_03  C_00..C_08  D_00..D_04
```

No `build_canonical_prices_v2`. No `inject_scoped_overrides`. No `bd_price_update`. The CATALOG is the dispatcher's single source of truth — every chain (`full`, `canonical`, `downstream`, `foundation`, `rebuild`) is composed from IDs in this list, and there is no ID for any silver/ canonical-prices script.

**EC2 boot script** at `infra/aws/ec2/bd-gold-layer-runner/run-gold-layer.sh:79`:

```bash
aws s3 sync "s3://${S3_BUCKET}/code/gold/" "$SCRIPTS_DIR/"
```

The systemd boot script only syncs `code/gold/`. It does NOT sync `code/silver/` or `code/bronze/`. Which means the silver canonical-prices scripts are never even present on the runner's filesystem on boot. They live in `s3://opal-data-bd/code/silver/` for historical reasons and for manual bootstrap from a different host, but the gold runner cannot execute them.

**Where each canonical-prices script actually lives and runs now:**

| Script | Location | Status |
|---|---|---|
| `build_canonical_prices_v2.py` | `data/black_diamond/scripts/silver/` | **Emergency bootstrap only** — runs manually on any host with AWS CLI + pandas when the canonical_prices parquet needs to be rebuilt from scratch (schema change, disaster recovery). No schedule, no cron, no SSM doc. |
| `inject_scoped_overrides.py` | `data/black_diamond/scripts/silver/` | **Manual override only** — runs after `build_canonical_prices_v2` when scoped overrides need to be layered on top. Memory rule "build_canonical_prices_v2 first, inject_scoped_overrides second" covers this manual ordering. |
| `bd_price_update.py` (silver host script) | `data/black_diamond/scripts/silver/` | **Superseded** — the host version is a historical predecessor of the Lambda, kept around but not invoked by any automated job. |
| `bd-price-update/lambda_function.py` | `infra/aws/lambda/bd-pipeline/` | **Canonical daily producer** — the Lambda described above. This is THE daily path for `silver/prices/canonical_prices.parquet` and `silver/prices/<date>.parquet`. |

**Corroboration from the Lambda's own docstring** (`bd-price-update/lambda_function.py:23`, `:181`, `:332`, `:599`):

> Line 23: "This remains the T1 source for `build_canonical_prices_v2.py` emergency full rebuilds."
> Line 181: `logger.warning(f"Not found ({e}) — Job 1 will be skipped (run build_canonical_prices_v2.py to bootstrap)")`
> Line 599: `logger.warning("canonical_prices.parquet is empty — skipping Job 1. Run build_canonical_prices_v2.py on EC2 to bootstrap.")`

The Lambda's own error-handling treats `build_canonical_prices_v2.py` as a bootstrap tool, not a daily job. Nothing in `infra/aws/` schedules it: no EventBridge rule, no Lambda invoke, no SSM doc, no cron, no systemd unit.

**The naming confusion that caused Andrew's memory to misfire:**

There are two scripts with "canonical" in the name and they do different things:

| Script | Layer | Runs where | What it builds |
|---|---|---|---|
| `B_00.canonical_holdings.py` | gold | **gold runner, daily** (CHAIN_CANONICAL) | Per-asset holdings stack written back to silver (silver/canonical_holdings/*.parquet) |
| `build_canonical_prices_v2.py` | silver | **nowhere automated — manual emergency only** | Per-asset price reference (silver/prices/canonical_prices.parquet) |

B_00 runs every night and has "canonical" in the name, so it's plausible Andrew remembered it as "the canonical prices script on the runner" when it's actually the canonical *holdings* script. The daily canonical *prices* production genuinely did move out of the runner during the ADVI_PRICES work in late March (commits around `d39a3cdb` "fix $107M MBS mispricing + T1 staleness cap" and the ADVI_PRICES.003/.004 task orders), and is now entirely in the bd-price-update Lambda.

**Net answer:** Yes, the canonical-prices build on the gold runner is deprecated. It was moved to a Lambda sometime in late March. The silver script survives as an emergency bootstrap tool only. Nothing in the daily path touches it.

### Part 7 — Stale comment in deploy-to-ec2.sh

One doc cleanup opportunity surfaced during the trace: `infra/aws/ec2/bd-gold-layer-runner/deploy-to-ec2.sh:11` still carries the comment:

```bash
#   code/silver/  ← enrichment (build_canonical_prices_v2.py, merge-daily-*.py, etc.)
```

as if silver scripts were part of the runner's sync payload. They're not — the actual boot script at `run-gold-layer.sh:79` only syncs `code/gold/`. That comment predates the Lambda migration and is actively misleading. NOT edited in this session — awaiting Andrew's go-ahead before any follow-up doc commit.

### Part 8 — Pipeline diagram generators (existing + new)

The BD pipeline is now documented end-to-end by **two** complementary Python SVG generators living side-by-side in `data/analysis/`. Together they render the full path from BD source files → event chain → silver → gold → serving → portal. The boundary between the two is `silver/prices/<date>.parquet` — the new upstream diagram ends there and the existing downstream diagram begins there.

#### 8a — Existing generator: `data/analysis/bd_pipeline_diagram_gen.py`

Referenced here for completeness since the new upstream diagram is designed to compose with it. Not modified this session, but read in full to match style / color palette / SVG defs.

**Scope:** everything from the gold runner onward. Starts at the `silver/prices/*.parquet` drop (treated as an opaque input coming from "somewhere") and traces through the runner, gold artifacts, serving layer, and portal frontend.

**Output:** `C:/Users/AndrewBerman/Desktop/bd_pipeline_diagram.svg`
**Canvas:** `W=2400, H=1680`
**Ground truth sources** (from the docstring):
- `data/black_diamond/scripts/gold/gold_dispatch.sh`
- `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-04-08/gold_pipeline_script_file_flow.md`
- `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-04-08/portal_auth_and_data_serving_flow.md`

**Layers rendered, top to bottom:**

| Layer | y-range | Contents |
|---|---|---|
| Title + subtitle | 0-110 | "BD Pipeline — AdvisorIntelligence Data Flow" |
| Sources + silver + trigger | 125-245 | Three source cards (Black Diamond, Schwab, S3 Silver) on the left; three trigger cards (EventBridge, bd-gold-trigger Lambda, StartInstances) on the right. Converging arrows into the runner header. |
| Gold runner EC2 container | 280-1045 | Big amber-bordered container labelled `bd-gold-layer-runner` / c6i.16xlarge / i-01003b035d2988dfb, with "Orchestrator: gold_dispatch.sh" header. Inside it, four horizontal **script lanes** A/B/C/D, each with a letter badge and a row of script pills. |
| S3 gold artifacts | 1065-1200 | Green bar showing `s3://opal-data-bd/gold/*` split into seven key-prefix cards: `dimensions/`, `canonical/`, `timeseries/`, `views/`, `artifacts/`, `entities/advisors/`, `entities/clients/`. Each card annotates which scripts write to it. |
| Serving layer | 1220-1430 | Two side-by-side panels: **Path A (Hot / Direct S3)** — CloudFront → auth-validator-edge → shared-advisor-router → S3; **Path B (Dynamic)** — CloudFront → API GW → opal-portal-authorizer → opal-partners-data Lambda → S3 reads. |
| Portal frontend | 1450-1610 | Blue bar for `opalinvest.dev` with five tab cards: PartnerAnalytics, Clients, Books, Distribution, Advisors. |

**Script lane detail (the `GROUPS` constant at line 30):**

| Group | Color | Purpose | Scripts (count) |
|---|---|---|---|
| **A — Foundation** | violet `#7c3aed` | Dimension tables | A_00 accounts_dimension, A_01 advisor_assignments, A_02 fee_rate_history, A_03 positions_cube, A_04 client_dimension (5) |
| **B — Holdings (canonical)** | sky `#0284c7` | Canonical holdings stack | B_00 canonical_holdings, B_01 holdings_lots, B_01b classify_new_securities, B_02 canonical_lots, B_03 account_gains (5) |
| **C — Activity & Analytics** | orange `#ea580c` | Performance, NNA, mix, tax, fee | C_00 canonical_performance, C_01 canonical_nna, C_02 client_performance, C_03 account_performance, C_04 validate_aua, C_05 client_tax_liability, C_06 client_mix_timeseries, C_07 advisor_attribution, C_08 advisor_fee_efficiency (9) |
| **D — Portal Aggregates** | emerald `#059669` | Portal publishers | D_00 portal_aggregates, D_00b portal_timeseries, D_00c portal_leaderboard, D_01 partner_analytics, D_02 advisor_client_detail, D_03 composition_artifacts, D_04 client_portal_summary (7) |

Script pills render with both the ID (e.g. `D_00c`) and the filename stub (`portal_leaderboard`). Intra-lane arrows show the chain order; inter-lane amber arrows on the label column show A → B → C → D dependency.

**Helper functions** (imported verbatim into the new upstream generator to keep style consistent):
- `rrect(x, y, w, h, fill, stroke, sw, rx, filt)` — rounded rect with optional shadow filter
- `_esc(s)` — XML escape that preserves existing `&amp;` entities
- `txt(x, y, s, size, weight, fill, anchor)` — positioned text node
- `arr(x1, y1, x2, y2, color, w, marker)` — straight arrow with marker-end

**SVG defs reused by the new generator:**
- Linear gradients: `bg` (slate background), `ec2grad` (amber EC2 container), `cfgrad` (violet serving), `apigrad` (amber API panel)
- `shadow` filter (feDropShadow dx=0 dy=6 stdDeviation=7 flood-opacity=0.18)
- Arrow markers: `arrow` (slate), `arrowAmber` (#b45309), `arrowLime` (#4d7c0f), `arrowViolet` (#6d28d9)

**What the existing diagram does NOT show** (and hence the need for the companion):
- How the silver parquet files actually get written — the sources cards on the left are just labelled "SFTP exports" with no trigger, no Lambda, no EC2 flow
- The EventBridge cron rules that start the evening chain (21:38 / 21:45 / 21:53 / 22:00 UTC)
- The five trigger Lambdas (bd-unrealized-trigger, bd-realized-trigger, bd-transactions-trigger, bd-allocation-trigger, historical-prices-scheduler)
- The bd-allocations / bd-transactions / historical-prices-scheduler EC2 instances
- The bd-allocation-processor S3-event Lambda and its gate on silver/transactions
- The bd-allocation-processor → bd-price-update async invoke (the Lambda-to-Lambda chain)
- bd-price-update's dual write (dated file fires gold, canonical_prices.parquet does not — excluded by filter prefix)
- Safety nets: bd-gold-nightly-fallback, bd-gold-layer-monthly-trigger, bd-allocation-file-check-daily

Everything above is exactly what the new upstream generator fills in.

#### 8b — New generator: `data/analysis/bd_bronze_silver_pipeline_diagram_gen.py`

Written this session. Hand-off boundary with the existing diagram is the `silver/prices/<date>.parquet` artifact and the subsequent `bd-gold-trigger → bd-gold-layer-runner` arc, which appears in both diagrams so the reader can visually snap the two canvases together.

**Output:** `C:/Users/AndrewBerman/Desktop/bd_bronze_silver_pipeline_diagram.svg` (32,701 bytes written by `python data/analysis/bd_bronze_silver_pipeline_diagram_gen.py` at session end)
**Canvas:** `W=2400, H=1920` (240 px taller than the existing diagram to accommodate the convergence gate + footer callouts)

**Style parity with the existing generator:**
- Identical helper functions (`rrect`, `_esc`, `txt`, `arr`, plus a new `wrap(text, max_chars)` for long annotation bodies)
- Identical `bg` linear gradient and `shadow` filter
- Reused arrow markers `arrow`, `arrowAmber`, `arrowLime`; added two new ones for this diagram: `arrowBlue` (#1e40af, for the allocation-processor chain) and `arrowRed` (#b91c1c, reserved for warnings — used only in the footer callouts and the canonical_prices "EXCLUDED" annotation)
- New linear gradients specific to this diagram: `convgrad` (yellow, for the convergence gate), `safegrad` (red, for safety nets), `handoffgrad` (amber, for the bd-gold-layer-runner handoff box)
- Same font stack (Segoe UI / system fallbacks)

**Data structure — the `LANES` constant at line 58:**

Five tuples, one per daily data stream, each with 10 fields: `(eastern_time, utc_time, cron_rule, trigger_lambda, ec2, bronze_key, silver_key, downstream_note, color_dark, color_light)`. Pulled from direct reads of `eventbridge.tf` and the Lambda sources — every time, rule name, Lambda name, and EC2 instance name in the diagram is grounded in a file + line number.

| Lane | ET | UTC | Cron rule | Trigger Lambda | EC2 | Bronze | Silver |
|---|---|---|---|---|---|---|---|
| 1 | 9:00 AM | 14:00 daily | `historical-prices-daily` | `historical-prices-scheduler` | historical-prices-scheduler EC2 | (yfinance fetch in-instance) | `silver/historical_prices.parquet` |
| 2 | 5:38 PM | 21:38 Mon-Fri | `bd-unrealized-pipeline-trigger` | `bd-unrealized-trigger` | bd-allocations EC2 (shared) | `bronze/unrealized/<date>` | `silver/unrealized/<date>.parquet` |
| 3 | 5:45 PM | 21:45 Mon-Fri | `bd-realized-pipeline-trigger` | `bd-realized-trigger` | bd-allocations EC2 (shared) | `bronze/realized/<date>` | `silver/realized/<date>.parquet` |
| 4 | 5:53 PM | 21:53 Mon-Fri | `bd-transaction-pipeline-trigger` | `bd-transactions-trigger` | bd-transactions EC2 | `bronze/transactions/<date>` | `silver/transactions/<date>.parquet` |
| 5 | 6:00 PM | 22:00 Mon-Fri | `bd-allocation-pipeline-trigger` | `bd-allocation-trigger` | bd-allocations EC2 (shared) | `forwardfill_v2/allocations/*.xlsx` | `silver/daily_allocations/<date>.parquet` |

Each lane also carries a downstream note: lanes 2/3 are marked as "Independent consumer" (feed the unrealized/realized pipelines, not the gold trigger chain); lane 4 is marked "GATE INPUT for bd-allocation-processor + T1 source"; lane 5 is marked "S3 event → bd-allocation-processor".

**Layers rendered, top to bottom:**

| Layer | y-range | Contents |
|---|---|---|
| Title + subtitle | 0-100 | "BD Pipeline — Bronze / Silver Upstream (Event Chain)" |
| Column headers | 138 | "EventBridge Cron" / "Trigger Lambda" / "EC2 Instance" / "Bronze + Silver Artifacts" / "Downstream" / "Safety Nets & Monthly" |
| Swim lanes | 170-890 | Five horizontal lanes (lane height 132, gap 12), each with five boxes connected by arrows: `[cron] → [trigger λ] → [EC2] → [bronze/silver stack] → [downstream note]`. Bronze + silver artifacts are stacked inside a single green box with "BRONZE" / "SILVER" labels. |
| Safety nets panel | 170-890 | Right column at `x=1950, w=420`, height matched to the swim lanes. Three stacked items: `bd-gold-nightly-fallback` (23:00 UTC weekdays), `bd-gold-layer-monthly-trigger` (08:00 UTC 1st, mode=full), `bd-allocation-file-check-daily` (22:30 UTC). Each item has a one-line schedule, a frequency tag, the rule/Lambda name, and a 4-5 line description explaining what it catches. |
| Convergence gate section | 910-1630 | Big yellow container labelled "Convergence Gate — Silver → Gold Handoff". Inside: three major nodes and the handoff column. |
| Footer callouts | 1650-1850 | Pale yellow bar with the three "easy to get wrong" facts (canonical_prices deprecated, code/gold uploads inert, dual-write filter trick). |
| Bottom source strip | 1900 | Sources cited: eventbridge.tf, s3-notifications.tf, bd-price-update, bd-allocation-processor, run-gold-layer.sh, gold_dispatch.sh. Plus cross-reference to bd_pipeline_diagram.svg. |

**Convergence gate detail** (the most complex part of the new diagram):

- **`bd-allocation-processor` Lambda box** (left, x=80 w=520 h=260). Shows the three-step logic from `bd-allocation-processor/lambda_function.py:110-121`:
  1. Convert XLSX → silver/daily_allocations/<date>.parquet
  2. Check silver/transactions/<date>.parquet exists (gate)
  3. If both present → `lam.invoke('bd-price-update', 'Event')` (async, fire-and-forget)
- **`bd-price-update` Lambda box** (middle, x=680 w=720 h=330). Two sections:
  - **READS:** silver/transactions/<date>.parquet (T1 + gate), silver/historical_prices.parquet (T2), silver/prices/canonical_prices.parquet (existing table)
  - **WRITES:** `silver/prices/<date>.parquet` (green text, "fires S3 event"), `silver/prices/canonical_prices.parquet` (red text, "EXCLUDED by filter"), `silver/interpolated_prices.parquet`
  - Source reference: `bd-price-update/lambda_function.py:450-500, 740-770`
- **Handoff column** (right, x=1440 w=400). Three stacked boxes:
  1. `silver/prices/<date>.parquet` artifact (green, e.g. "silver/prices/2026-04-10.parquet")
  2. `bd-gold-trigger` Lambda (amber, "StartInstances(i-01003b035d2988dfb)")
  3. `bd-gold-layer-runner` EC2 handoff (amber gradient, "see bd_pipeline_diagram.svg" cross-reference arrow)

**Inbound arrows from lanes into the gate** (the part that took the most routing work):

| Arrow | From | To | Style | Label |
|---|---|---|---|---|
| 1 | allocations lane artifact box | bd-allocation-processor top | solid blue `#1e40af`, w=4 | "S3 event (XLSX created)" |
| 2 | transactions lane silver artifact | bd-price-update top (left inlet) | dashed green `#166534`, w=3 | "T1 + gate" |
| 3 | historical prices lane silver artifact | bd-price-update top (right inlet) | dashed blue `#0369a1`, w=3 | "T2 (yfinance)" |

Dashed edges are "data reads" (T1/T2 price inputs plus the gate check), solid edges are "async invocation" / "S3 event" (the actual control flow). Arrow routing uses L-shaped SVG paths (`<path d="M x y L x y L x y L x y"/>`) that hop above the convergence gate header and drop into the target box tops, avoiding the descriptive text area and the solid allocations arrow.

**Footer callouts** — the three "easy to get wrong" facts, each with a numbered prefix, bold headline, and a 2-line wrapped body:

1. **Canonical prices is NOT built on the gold runner anymore.** Moved to bd-price-update Lambda in the ADVI_PRICES wave (late March). gold_dispatch.sh CATALOG has no `build_canonical_prices_v2` entry, and run-gold-layer.sh:79 only syncs code/gold/, never code/silver/.
2. **Uploading files to code/gold/ does NOT trigger the runner.** The only S3 write path in opal-data-bd that fires bd-gold-trigger is `silver/prices/20*.parquet`. Code uploads to code/gold/ are inert — they just stage scripts for the next boot.
3. **bd-price-update writes two parquets; only one fires gold.** Both `silver/prices/<date>.parquet` AND `silver/prices/canonical_prices.parquet` are written in the same Lambda run. The S3 notification filter uses prefix `silver/prices/20` — a deliberate filename trick to match dated files but skip canonical_prices.parquet (which starts with 'c').

**Rendering verification:**
```bash
cd /c/Users/AndrewBerman/Desktop/ajb_workspace
python data/analysis/bd_bronze_silver_pipeline_diagram_gen.py
# → Wrote C:\Users\AndrewBerman\Desktop\bd_bronze_silver_pipeline_diagram.svg (32,701 bytes)
```

Exit code 0. SVG writes to the same desktop location as the existing diagram so they can be viewed side-by-side. Both diagrams share the title prefix "BD Pipeline —" and differ only in the suffix ("AdvisorIntelligence Data Flow" for the gold-side diagram, "Bronze / Silver Upstream (Event Chain)" for the new one).

#### 8c — How the two diagrams compose

Together the pair gives a complete end-to-end picture of the BD pipeline on a single desktop:

```
bd_bronze_silver_pipeline_diagram.svg         bd_pipeline_diagram.svg
(new, this session)                             (existing)
┌──────────────────────────────┐               ┌──────────────────────────────┐
│ EventBridge crons            │               │ Sources (opaque) + Silver    │
│   ↓                          │               │   ↓                          │
│ Trigger Lambdas              │               │ Gold runner (A/B/C/D)        │
│   ↓                          │               │   ↓                          │
│ EC2 instances                │               │ S3 gold artifacts            │
│   ↓                          │               │   ↓                          │
│ Bronze + silver artifacts    │               │ Path A / Path B serving      │
│   ↓                          │               │   ↓                          │
│ bd-allocation-processor gate │               │ Portal frontend              │
│   ↓                          │               │                              │
│ bd-price-update              │               │                              │
│   ↓                          │               │                              │
│ silver/prices/<date>.parquet │━━handoff━━━━▶ │ (picks up here)              │
│   ↓                          │               │                              │
│ bd-gold-trigger ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━▶                              │
│   ↓                          │               │                              │
│ bd-gold-layer-runner ━━(see companion)━━━━━▶ │                              │
└──────────────────────────────┘               └──────────────────────────────┘
```

The `silver/prices/<date>.parquet`, `bd-gold-trigger`, and `bd-gold-layer-runner` nodes appear in both diagrams — that's the visual "seam" the reader can use to line them up. If we ever want to collapse them into a single canvas, the shared nodes make the merge deterministic. Until then, keeping them as two generators lets each one use its full 2400-wide canvas without cramming.

---

## Files Modified

| File | Change |
|---|---|
| `data/black_diamond/scripts/gold/D_00c.portal_leaderboard.py` | Added `n_roles_per_pair` computation at lines 516-520; per-role aggregation at line 528 now uses `_weighted_aua` instead of `total_aua`. Divides AUA evenly across overlapping roles when one advisor fills 2+ role slots on one account. |
| `data/analysis/bd_bronze_silver_pipeline_diagram_gen.py` | New file. SVG generator for the upstream event chain (EventBridge → trigger Lambdas → EC2 → bronze/silver artifacts → bd-price-update → silver/prices → gold handoff). |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-04-10/gold_trigger_chain_trace_and_d00c_role_split_fix.md` | This log. |

---

## Deploy Cycle

| Step | Result |
|---|---|
| Commit SHA | `64d9e509` (author: `0.4.0_DS_ClientPlatform`) |
| Push | `16957e52..64d9e509  CLOUD -> CLOUD` |
| S3 upload | `s3://opal-data-bd/code/gold/D_00c.portal_leaderboard.py` (etag `74910d4fc0fdf0438268490355d28840`, 31283 bytes) |
| Gold parity check | 52 .py + 9 lib + 7 sidecar files all byte-for-byte match between local and S3 |
| Trigger | NOT invoked — Andrew asked to hold runner |
| Runner state | `stopped` at session end (last transition 2026-04-10T01:50:45Z) |

---

## Compiler Tools

| Tool | Command | Result | Notes |
|---|---|---|---|
| `comp-trace` | `comp-trace "silver/prices" --direction up` | Returned 16 upstream nodes. Identified `bd-price-update` Lambda as the direct producer of `silver/prices/canonical_prices.parquet`. Other matches were gold scripts that READ canonical_prices (listed as WRITES_S3, which is the label for any file with a pricing-related S3 path — slightly misleading but didn't block the trace). | Graph built in 2.9s, 655 nodes, 279 edges |
| `comp-trace` | `comp-trace "bd-price-update" --direction up` | Returned `config/ticker_lookup.json` as the only upstream edge. The compiler's Lambda-to-Lambda invocation graph is thin — it did not surface `bd-allocation-processor` as an invoker of `bd-price-update`. Fell back to direct grep on the allocation-processor source to find the `lam.invoke(FunctionName='bd-price-update', InvocationType='Event')` call at `bd-allocation-processor/lambda_function.py:116-121`. | **Gap flagged:** compiler doesn't yet capture `lambda.invoke` calls between Lambdas. Worth adding to `org/modules/graph/` to improve future trigger-chain traces. |
| Manual read + grep | Direct reads of `gold_dispatch.sh`, `run-gold-layer.sh`, `eventbridge.tf`, `s3-notifications.tf`, `bd-price-update/lambda_function.py` | Full trigger chain reconstructed end-to-end. All claims in Parts 5-6 of this log are backed by a file + line number. | Used after compiler gap on Lambda-to-Lambda edges |

D_00c change is frontend-facing for the leaderboard only — no cross-script dependencies affected. `comp-blast` not needed because the `at_role_breakdown` dict is consumed inside the same `build_employee_leaderboard` function and doesn't cross script boundaries.

Appended to `org/compiler-tools-log.md`: `2026-04-10 0.4.0_DS comp-trace silver/prices,bd-price-update — Lambda invoke edges missing from graph, fell back to grep. D_00c role-split fix shipped.`

---

## Next Steps

- **[Andrew]** Browser QA the new role_breakdown math on opalinvest.dev after the next gold run. Spot-check Sam Owens and Alex Bright — their `role_breakdown[implementor].aua + role_breakdown[local_ops].aua` should now equal `tagged_aua` rather than ~2x it. Unaffected advisors (anyone not in the 17-advisor overlap set) should show zero change.
- **[Andrew]** Decide whether to trigger a manual incremental gold run tonight or let the 22:00 UTC evening chain pick up the new D_00c on its normal run. If you want to trigger early: `aws lambda invoke --function-name bd-gold-trigger --cli-binary-format raw-in-base64-out --payload '{"mode": "incremental"}' /tmp/gold-trigger-response.json`.
- **[Andrew / me]** On go-ahead: clean up the stale `code/silver/` comment in `infra/aws/ec2/bd-gold-layer-runner/deploy-to-ec2.sh:11`, and optionally `aws s3 rm s3://opal-data-bd/code/gold/05_build_client_performance.py.legacy` to clear the orphan.
- **[Dashboard Engineer]** Update the `role_breakdown` footnote on the Employee Leaderboard to match the new reality: *"When an advisor fills multiple roles on one account, the account's AUA is divided evenly across those overlapping roles."* The old "26 accounts / 0.039%" number was wrong — the correct scope is 372 accounts / 3.74% — but with the fix in place, the magnitude no longer needs to be disclaimed in the footnote at all.
- **[me, optional]** Write a small PR to `org/modules/graph/crossref_graph.py` (or wherever the Lambda edge extraction lives) to capture `lambda_client.invoke(FunctionName=...)` calls so `comp-trace` can follow Lambda-to-Lambda async invokes. This would have answered today's "what triggers bd-price-update" question in one compiler call instead of a grep fallback.
