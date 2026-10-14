# Investor Reporting performance and holdings tabs: daily pulls, per firm -- scope for 1.0.0_SA_CTO~DELL2

**Author:** `4.0.0_SA_CRO~DELL2`, 2026-10-14, on crossbox ORDER XB-20261014T185521Z-75d6. Body
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_190xZ_IRPT_DAILY_6AM_ET_PULLS.md`. Andrew added scope ~19:0xZ
(record `ANDREW_DIRECT_20261014_190xZ_PER_FIRM_DAILY_TRIGGERS_AND_DRAW.md`).

**Method:** read-only, 19:05-19:30Z. Live reads only: `events describe-rule`, `scheduler get-schedule`, S3 list/head, SSM
`get-command-invocation`, Lambda logs. Nothing was written. Trading-day frontier: 2026-10-13 (`lib/trading_calendar`). Account ids are
opaque.

## Headline

**The Oct 9 staleness is not a missed schedule.** Every holdings run fired on time each weekday and SSM returned Success. The publish gate
then REFUSED the new day because accounts dropped out of the source (`account_lost`), and the page kept the last accepted day. Nobody owns
acting on that refusal.

Separately, **nothing runs at 6 AM ET**, and the triggers are not uniform across firms.

## What each firm's Holdings tab serves today

As-of is per firm: one publication per firm, and every client in it shares the date.

| Firm | Clients (directory entries) | Served as-of | Behind T-1 | Why |
|---|---|---|---|---|
| 49financial | 4,746 | 2026-10-12 | 1 trading day | The 10-09 run TimedOut (IB-pr-537). Today's candidate was refused: `account_lost` = 1 (`acc_9b783a72...`) |
| cottonwood | 271 | **2026-10-08** | 3 trading days | Runs succeeded 10-09/12/13/14 and the source silver is current at 10-13. The publish gate refused every candidate (`irpt/cottonwood/platinum/holdings/current/publish_refusal.json`, 3 versions): 10-09 `account_lost` = 9; 10-12 and 10-13 `account_lost` = 1 (`acc_729bbbc1...`) |
| inflection | 295 | 2026-10-13 | current | -- |

**Also:**
- Cottonwood's performance gold is at **2026-09-25**. It has never been scheduled; the tab uses the Black Diamond live-session path, whose
  as-of was not measured.
- Cottonwood's directory pointer did not move at today's 9:30 refresh (49F and INF did). The cause was not read.

## Per-firm source triggers: confirmed daily?

ENABLED unless marked; DESIRED (repo) = APPLIED (live) unless noted.

| Firm | Source | Trigger(s), live | Daily? | Newest |
|---|---|---|---|---|
| cottonwood | Black Diamond | `cot-bd-session-daily-et` (Scheduler, 07:30 America/New_York) -> `cot-bd-session-trigger` -> SSM doc `opal-cot-bd-session-fetch` -> `cot-session-complete` (rule, fires on SSM **Success** only); `opal-assets-ingest-mirror-cot-daily-et` (07:45 NY) | YES, daily 07:30 NY | silver 10-13 |
| 49financial | Schwab | `canonical-schwab-si2-08335338-daily-pull` (rule, UTC 09:45 and 21:45, SSM `AWS-RunPowerShellScript`); `schwab-canonical-si2-08403355-pull-daily` (rule, UTC 10:45 and 22:45); `opal-assets-silver-schwab-sweep-daily` (rule, UTC 12:15) | YES, UTC rules | 10-13 |
| 49financial | SmartX | `smartx-jwt-refresher-daily` 09:00 NY, `smartx-rest-pull-daily` 09:15 NY, `smartx-assets-daily-pull-daily` 13:02 **UTC** (Scheduler) | YES | 10-14 |
| 49financial | Black Diamond | `bd-49f-session-daily` (rule, UTC 00:00), `opal-assets-bd49f-daily-pull-reattempt-daily` (rule, UTC 08:30), `opal-assets-bd49f-dim-convert-daily` (Scheduler, UTC 07:05). **DISABLED:** `bd-49f-runner-daily`, `bd-49f-fees-runner-daily`, `bd-allocation-pipeline-trigger`, `bd-transaction-pipeline-trigger` | PARTLY: the session and the dim convert run daily; the runner, fees, allocation and transaction legs are disabled | bronze only; feeds the directory and the BD live path |
| inflection | Orion | `opal-inf-jwt-fetch` (UTC 09:50), `opal-inf-export-schedule` (UTC 21:00) -> `inf-jwt-trigger`; `inf-assets-trigger-bronze-complete` (S3 event only); `opal-inf-assets-ingest-mirror-late-daily` (UTC 17:05); `inf-performance-daily` (UTC 14:27); `inf-accounts-v2-daily` (UTC 11:07) | YES, UTC rules | 10-14 |
| inflection | Eclipse | `inf-api-eclipse-daily` (UTC 11:18), `opal-assets-silver-eclipse-sweep-daily` (UTC 16:00) | YES, UTC rules | 10-14 |

**IRPT producers:**

| Trigger | Kind and schedule | Covers | Target |
|---|---|---|---|
| `irpt-holdings-snapshot` | Scheduler, 10:15 NY Mon-Fri | all three firms | `irpt-holdings-refresh-lambda` -> SSM on i-02448edb624a7a7cf, one command per firm |
| `irpt-holdings-performance-daily` | Scheduler, 07:30 NY | 49F | -- |
| `irpt-inf-holdings-performance-daily` | **UTC** 14:00 | INF | -- |
| (none) | -- | **COT has no performance schedule** | -- |
| `irpt-49f-reporting-gold-daily`, `irpt-49f-reporting-publish-daily`, `irpt-49f-reporting-publish-summaries-daily` | 07:41 / 08:15 / 08:45 NY | **49F only** | -- |
| `irpt-directory-refresh` + `irpt-directory-refresh-retry-daily` | 09:30 / 09:40 NY | -- | -- |

## Canonical shape

- **Gold is canonical and uniform for holdings and performance.** Every firm uses the `address()` form
  `s3://opal-data-<firm>/irpt/<firm>/gold/<table>/date=D/`, from one producer and contract. Columns were not diffed.
- **Platinum:** `irpt/<firm>/platinum/holdings/current/manifest.json`, built by `holdings/publication.py:136` with `address()`.
- **Not canonical:**
  - the serving directory sits in legacy buckets (`opal-data-{bd,cot,inf}/investor-reporting/directory/<date>/`), and the generated
    `firm_bucket_map` maps 49F to `opal-data-bd`;
  - INF Eclipse is read from a legacy dated folder (`opal-data-inf/silver/eclipse/<D>/portfolios_*.parquet`, no `date=` key), with a
    second copy at `opal-data-assets/eclipse/inflection/silver/`;
  - INF Orion has bronze in two places.
- **Per-client paths: none.** Paths are per firm. Accounts are rows inside each firm's file, and the serving Lambda filters by account set.

## One-offs and forks against Andrew's standard ("identical naming structure and operations per firm")

1. Performance runs as a separate Lambda and schedule per firm; INF's is on UTC, and COT has none.
2. The dashboard (reporting) chain exists for 49F only.
3. The Schwab rule names are inverted against each other (`canonical-schwab-...` vs `schwab-canonical-...`), and both run on UTC.
4. EventBridge rules (always UTC) are mixed with Scheduler entries, some NY and some UTC.
5. Two triggers fire only on an upstream's success: `cot-session-complete` and `inf-assets-trigger-bronze-complete`. Both have a
   scheduled backstop elsewhere in the chain; success-only triggering is a CLAUDE.md hard-stop defect.
6. INF keeps duplicate bronze for Orion and duplicate silver for Eclipse.
7. Six 49F Black Diamond triggers are DISABLED.

## Scope for the box CTO to fold (P1 Investor Reporting, due Nov 15)

| # | Item | Owner proposed |
|---|---|---|
| S1 | **The `account_lost` publish refusal:** an owner and a route that resolves it each day (accept or exclude the lost account, with the reason shown), so a firm never sits days behind on one account. This is the actual cause of COT at 10-08 and 49F at 10-12 | IRPT_BCKEND `2.0.0_SA_COO~P2` |
| S2 | **One naming and timing pattern per firm:** every upstream pull an EventBridge Scheduler entry at `cron(0 6 * * ? *)` with `America/New_York`, named `irpt-<firm>-<source>-pull-daily`; each IRPT producer on its own NY schedule after its input lands, with a trading-day freshness basis | IRPT_BCKEND |
| S3 | A COT performance schedule (the source is declared in `sources.json` but unscheduled); INF performance moved to NY time | IRPT_BCKEND |
| S4 | The reporting/dashboard chain for COT and INF, or a ruling that it is 49F-only | IRPT_DASHBD `2.0.0_SA_COO~D2` |
| S5 | Replace the success-only triggers with schedules | IRPT_BCKEND, with the firm producers |
| S6 | One copy each of INF Orion bronze and INF Eclipse silver, read from the canonical silver | IRPT_BCKEND |
| S7 | A ruling on the six disabled 49F Black Diamond triggers (retire or re-enable) | box CTO |

No alarm or monitor is proposed (moratorium). Freshness is enforced by the schedule plus the S1 route.

## Not read

- The full stdout of each holdings run.
- The as-of of the COT Black Diamond live performance path.
- The `opal-cot-bd-session-fetch` document.
- The targets of the Schwab SSM rules.
- A column diff of gold across firms.
- Why COT's directory did not move today.

-- 4.0.0_SA_CRO~DELL2
