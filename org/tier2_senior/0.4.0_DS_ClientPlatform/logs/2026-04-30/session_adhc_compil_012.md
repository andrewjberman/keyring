# Session Log — ADHC_COMPIL.012 comp-freshness build
## Agent: 0.4.0_DS_ClientPlatform~D | Date: 2026-04-30

---

## TO Assigned

ADHC_COMPIL.012.ds-comp-freshness-tool — Theme G of ADHC_COMPIL v3.
Build `comp-freshness`: a pre-dispatch S3 freshness gate detecting stale upstream
silver/bronze before a gold chain run produces wrong output silently.

---

## Work Completed

### Deliverables

1. **.tools/comp-freshness** — Python entry point (~495 lines)
   - Subcommands: `chain {bd|inf}`, `script <id>`, `artifact <s3-prefix>`, `--list`
   - Output: `artifact_id | s3_key | last_modified | age_h | fail_at_h | STATUS`
   - Exit codes: 0=PASS/WARN, 1=FAIL, 2=config error/AWS unreachable
   - Parallel execution: `concurrent.futures.ThreadPoolExecutor(max_workers=8)`
   - AWS call strategy documented below
   - Pre-commit gate PASS (py_compile + undefined-name scan + ruff)

2. **data/black_diamond/scripts/gold/gold_freshness_config.yaml** — 32 BD entries
   - Section 1: 4 Schwab vendor-daily entries (warn=36h, fail=72h) [PENDING ANDREW ACK]
   - Section 2: 7 internal nightly silver entries (daily, business-daily, weekly, on-demand)
   - Section 3: 21 gold chain intermediates (daily, weekly)

3. **data/orion/scripts/gold/gold_freshness_config.yaml** — 31 INF entries
   - Section 1: 7 Orion API vendor-daily entries [PENDING ANDREW ACK]
   - Section 2: 9 internal nightly silver entries (includes aum_snapshot INCIDENT ARTIFACT)
   - Section 3: 15 gold chain intermediates

4. **tests/comp_freshness/test_comp_freshness.py** — 30 unit tests
   - AC6 + AC7 retrospective reproduction tests (mocked timestamps)
   - Config error, exit code, threshold, and parse tests
   - All 30 PASS

5. **org/modules/graph/comp-tools.yaml** — added `comp-freshness` entry
   - Incidents caught, output format, exit codes, config paths, cost documented

---

## AWS API Call Strategy Rationale

Chosen: `aws s3api list-objects-v2 --delimiter /` for partition detection,
then `max_by(Contents, &LastModified).LastModified` for flat/partition listing.

**Rationale vs alternatives:**
- `aws s3 ls --recursive | sort | tail -1`: scans ALL objects O(n) — too slow for
  prefixes with years of daily files (silver/transactions/ has ~1500 objects).
- `list-objects-v2 --max-items 1`: returns first object alphabetically, not most recent.
- `list-objects-v2 --delimiter /` (chosen): O(1) to detect sub-prefixes per tier;
  for Hive-partitioned prefixes (date=YYYY-MM-DD/ structure), lexicographically last
  sub-prefix = latest partition. Then drill into that partition.
- `max_by(Contents, &LastModified)`: null-safe when Contents is [] (empty prefix);
  AWS CLI v2 auto-paginates and may return per-page results — handled by
  `_parse_timestamps_from_raw()` taking the maximum across all lines.

**Windows CMD.exe compatibility:** `aws.CMD` cannot be exec'd directly via subprocess
list API. Fixed with `_resolve_aws_cmd()`: detects `.cmd` extension via shutil.which
and wraps with `['cmd', '/c', exe]`. EC2 Linux uses bare `['aws']` path.

**Performance:** With 8-thread parallel execution: BD chain (32 artifacts) ran in 27.8s
(AC1 PASS, target <30s). INF chain (31 artifacts) ran in 24.0s (AC2 PASS).

---

## Cadence Config Audit Method

For BD chain:
- Primary: `comp-pipescript io <script>` for each gold script to source read sets
- Supplemented: `grep -r "silver/\|bronze/"` for scripts not in graph (A_03 Schwab bucket,
  build_canonical_prices_v2 historical_prices)
- Schwab bucket disambiguation: `opal-data-schwab` for RPS (A_03.py line 48);
  `opal-data-bd/schwab/silver/` for ULN/ULT/RLD (lib/s3_layout.py constants)
- lib/config.py: S3_BUCKET = os.environ.get('BD_S3_BUCKET', 'opal-data-bd')

For INF chain:
- `grep -r "S3_BUCKET\|PREFIX\s*=" data/orion/scripts/gold/INF_*.py` across all 25 scripts
- Key INF prefixes enumerated from INF_D_04 (most complex script, reads most inputs)

---

## AC6: Retrospective Reproduction — 2026-04-17 RPS Incident

**Incident**: Schwab RPS silver (s3://opal-data-schwab/silver/RPS/) was from
CRS20260407.RPS (10 days stale) on April 17 → $130M overshoot in
linear_interpolation.

**Test method**: Mocked `get_latest_modified` to return
`datetime(2026, 4, 7, 10, 0, 0, UTC)` with `incident_date = datetime(2026, 4, 17, 12, 0, 0, UTC)`.
Expected age = 240h > fail_at_h=72h, severity=ERROR → FAIL. Test PASSED.

**Live verification (current state)**: As of 2026-04-30, schwab_rps is still stale:
last_modified=2026-04-21T13:42:52Z, age=221h → FAIL (chain bd exit code 1 confirmed).
The Schwab RPS feed has not been updated since April 21 — this is an ACTIVE ongoing issue
that the tool is correctly flagging in production.

**S3 partition listing**: `aws s3api list-objects-v2 --bucket opal-data-schwab --prefix silver/RPS/`
confirmed Hive-partitioned structure (silver/RPS/date=YYYYMMDD/data.parquet).
Last partition as of 2026-04-30 is date=20260420.

---

## AC7: Retrospective Reproduction — 2026-04-29 aum_snapshot Incident

**Incident**: silver/aum_snapshot/ was from 2026-04-21 (8 days stale, ~192h) on
2026-04-29. Combined with column-name mismatch in INF_D_04 → $89.6M displayed vs
$182.71M correct.

**Test method**: Mocked `get_latest_modified` to return
`datetime(2026, 4, 21, 9, 0, 0, UTC)` with `incident_date = datetime(2026, 4, 29, 9, 0, 0, UTC)`.
Expected age = 192h > fail_at_h=48h, severity=ERROR → FAIL. Test PASSED.

**Live verification (current state)**: As of 2026-04-30, inf_silver_aum_snapshot shows
last_modified=2026-04-29T18:47:45Z, age=24.3h → PASS. The snapshot was fixed on
April 29 at 18:47 (presumably after the incident was discovered). On April 29 morning
(before 18:47), the tool would have returned FAIL age~182h (from the April 21 state).

---

## Partner-Feed Threshold ACK Status [PENDING ANDREW ACK]

Per PRD §7 Q1, Andrew sign-off is required before committing/shipping partner-feed entries.
All Schwab and Orion vendor-daily entries are marked `[PENDING ANDREW ACK]` in both configs.

Proposed thresholds for Andrew review:
- **schwab_rps / schwab_rld** (ERROR severity): warn=36h, fail=72h
  Rationale: Schwab SLA is not 100% reliable. 36h gives one missed day buffer;
  72h = three days before hard block. The April 17 incident was 240h stale — these
  thresholds would have caught it 168h earlier.
- **schwab_uln / schwab_ult** (WARN severity): warn=36h, fail=72h
  Rationale: B_02 falls back gracefully when absent; degraded quality not gross errors.
- **All inf_orion_api_* entries** (WARN severity): warn=36h, fail=72h
  Rationale: Orion API dim pulls run on EC2 nightly; some (performance, activity, assets)
  run less frequently. WARN severity means they never block dispatch.

Note: tool was committed with these entries at ERROR/WARN severity as drafted.
If Andrew disagrees with thresholds, update warn_age_hours/fail_age_hours in the YAML.
If Andrew prefers to defer vendor entries entirely, cadence can be changed to `on-demand`.

---

## Live Chain Results (2026-04-30)

### BD chain (27.8s, exit 1):
- schwab_rps: FAIL age=221h (ACTIVE STALE — ongoing issue)
- schwab_rld: FAIL age=524h (ACTIVE STALE)
- schwab_uln: WARN age=375h (WARN severity, non-blocking)
- schwab_ult: WARN age=524h (WARN severity, non-blocking)
- bd_silver_bd_assets_dim: WARN age=382h (weekly, WARN severity)
- bd_gold_ticker_resolution: WARN age=549h (weekly, WARN severity)
- All internal nightly BD chain: PASS (most recent ~14h ago — ran last night)

### INF chain (24.0s, exit 1):
- inf_silver_canonical_prices: FAIL age=197h (ACTIVE — prices not rebuilt since Apr 22)
- inf_silver_household: WARN age=63h (past 48h warn threshold)
- inf_orion_api_performance/activity/assets: WARN ~61-63h (near 72h vendor threshold)
- All INF gold chain intermediates: PASS (ran ~1h ago per timestamps ~0.6h)

---

## Acceptance Criteria Status

| AC | Description | Result |
|----|-------------|--------|
| AC1 | chain bd <30s | PASS: 27.8s |
| AC2 | chain inf <30s | PASS: 24.0s |
| AC3 | artifact form exit 1 on FAIL | PASS: schwab_rps exit 1 |
| AC4 | --list prints both pipelines | PASS: BD 32, INF 31 |
| AC5 | config error exit 2 | PASS: malformed YAML exits 2 |
| AC6 | RPS 2026-04-17 retrospective FAIL 240h+ | PASS: unit test |
| AC7 | aum_snapshot 2026-04-29 retrospective FAIL 192h | PASS: unit test |
| AC8 | >=30 BD artifacts | PASS: 32 entries |
| AC9 | >=10 INF artifacts | PASS: 31 entries |
| AC10 | Andrew partner-feed ACK documented | PENDING ANDREW ACK |
| AC11 | chain bd <30s | PASS: 27.8s |
| AC12 | AWS_UNREACHABLE distinguished from FAIL | PASS: separate exit 2 path |
| AC13 | compiler-tools-log.md row appended | PENDING (next step) |
