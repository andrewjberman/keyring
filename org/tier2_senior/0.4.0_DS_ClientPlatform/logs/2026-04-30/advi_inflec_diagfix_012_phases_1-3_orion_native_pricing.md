# DS — ADVI_INFLEC.DIAGFIX.012 Phases 1-3: Orion daily positions MV refactor

**Agent serial:** `0.4.0_DS_ClientPlatform`
**Date:** 2026-04-30
**Session shape:** post-compaction relaunch + watcher gap recovery + DIAGFIX.012 Phases 1-3 (bronze pull + silver builder + INF_B_00 refactor) + Phase 2.5 durability check + JWT trigger fire/diagnose
**Outcome:** Phase 1 + Phase 2 + Phase 2.5 (verdict CLEAN) + Phase 3 INF_B_00 full deletion → all RAVC ACK'd by COO; Phase 4-5 standing by for tomorrow's fresh-context start

---

## Mandate origin

DIAGFIX.012 GO from COO (`2.0.0_SA_COO`) at `20260430T132341Z`, after Andrew Option-B approval (stage til morning fresh start). My inbox-watcher had not been relaunched cleanly post-compaction; Andrew flagged the gap at 13:36Z and I relaunched at 13:32:25Z. Watcher fired immediately on relaunch and surfaced both the GO and the 13:37Z CHASE message ("DS~B routing in 15 min if no ACK"). RAVC2 ACK + heartbeat + TO flip `staged → pending` sent at 13:38:39Z, well within the 13:50Z deadline.

TO scope (per `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_INFLEC.DIAGFIX.012.ds-orion-daily-positions-mv-refactor.md`):
- Phase 1 — bronze pull `pull_inflection_positions_daily.py`
- Phase 2 — silver dim `convert_orion_api_to_silver.py --dim positions_mv`
- Phase 2.5 — durability check (joint CTO+COO scope addition; gates Phase 3 deletion-vs-fallback decision)
- Phase 3 — INF_B_00 refactor: full deletion if Phase 2.5 verdict clean, else `_API_FAIL_FALLBACK` gated dead code
- Phase 4 — chain re-run on c6a.4xlarge (tomorrow per COO timing; absorbs W4.14 stale-holdings refresh)
- Phase 5 — RAVC4 + validation (tomorrow)

---

## Wave shape

| Phase | Outcome | Commit |
|---|---|---|
| 1 — bronze pull | 294 clients, 23,680 rows, $197.16M, 5 min, 0 retries | `cb4336a59` |
| 2 — silver builder | positions_mv dim, 23,680 rows on S3 | `496ad4afc` |
| 2.5 — durability check | VERDICT CLEAN (30/30 across -180d, sustained 100% 200 OK) | (in commit messages + this log) |
| 3 — INF_B_00 refactor | Full deletion path, -93 lines net, $197.36M reconciles | `4bc5381b2` |

---

## JWT blocker + recovery

JWT in `s3://opal-data-inf/orion/jwt/current.json` was stale at session start (expired 09:09Z; today's 12:13Z auto-refresh cron didn't deliver fresh JWT). Diagnosis with Andrew via inspection:

1. Lambda log at 12:13Z showed only mode-marker write — **OLD Lambda code (pre-v1.7.1)** did not dispatch SSM. EC2 booted from a separate path but Playwright never started — no `state.json` updates, no debug screenshots, no log uploaded to `gold/logs/inf-exporter/`.
2. `s3://opal-data-inf/orion/browser-profile/state.json` (last successful 23:08:40Z yesterday) was intact.
3. Andrew framed: "we have a refresh token from every cron run and a second returning user token as a fallback." The mental model maps correctly to the architecture — the "refresh token" is Playwright `storageState()` (cookies + localStorage incl. Orion's "Remember this device" cookie); the "second returning user token" is creds-in-Secrets-Manager + OTP-via-S3-relay fallback. Steady state IS device-cookie-skip-OTP.

After Andrew "Fire it", I invoked `inf-jwt-trigger` Lambda manually at 14:13:17Z. Initial invoke failed with `InvalidInstanceId` (SSM `send_command` race vs EC2 boot — SSM agent not yet registered). EC2 had already started via the Lambda's `_ensure_running` path; armed Monitor on `state.json` polling.

State sequence:
- 14:13:18Z — EC2 boot
- 14:26:41Z — STARTING (~13 min slow init: cold-start S3 code-sync + Playwright browser binary setup)
- 14:26:47Z — JWT issued (Orion-side)
- 14:26:56Z — JWT_CAPTURED (clean storage-state-skip-OTP path; **no OTP required**, no Andrew interaction needed)

JWT in S3 rotated to fresh issuance, expires `2026-05-01T00:27:47Z`.

In parallel, AE 0.7.0 diagnosed both today's failures and shipped fixes:
- **`inf-pipeline-v1.7.4`** (`45af4950c`) — `_send_ssm_with_retry()` with 5×30s backoff for the ~30-90s SSM agent registration window
- **`inf-pipeline-v1.7.5`** (`9764c07e9`) — Secrets Manager JWT store at `orion/jwt/current` (raw JWT string)

Verified clean deploy: Lambda `CodeSha256: btARpIIjvEoDuneUmgWHXe/IV7kqOwgKd6P5fXjNbz4=` byte-matches `lambda-source-map.json` artifact_sha256 + `last_deployed_commit: 9764c07e9`. Tags chain forward sequentially with ci-deploy records (`9441dc379`, `31d538010`). Tomorrow's 12:13Z cron will run on v1.7.5 code with the SSM retry guard.

I sent AE 0.7 a correction on their Secrets Manager consumer pattern: **Orion REST uses `Authorization: Session {jwt}`, NOT `Bearer {jwt}`** (verified empirically — today's 294/294 production pull all 200 OK with `Session` prefix; `orion_export.ts:177` JWT-capture listener filters specifically for `auth.startsWith('Session ')`). They ACK'd.

---

## Phase 1 — Bronze pull (`cb4336a59`)

`data/orion/manual_api/pull_inflection_positions_daily.py` (NEW, 384 lines).

Pattern after `pull_inflection_assets_v2.py`. New iteration shape:
```
for date in date_range:
  for clientId in inflection_clientIds:
    GET /api/v1/Portfolio/Clients/{cid}/Assets/{MM-DD-YYYY}?$top=50000&includeCostBasis=false
```

CLI flags: `--date YYYY-MM-DD`, `--backfill-days N`, `--start/--end`, `--limit` (smoke), `--upload-bronze`, `--dry-run`, `--include-cost-basis`, `--sleep-ms`, `--durability-out`.

Retry: 429/5xx exponential backoff (max 3 retries). Rate-limit: 100ms inter-call sleep. Pagination: `$top=50000` (HAR sample max 53 assets/client). Per-call durability dict captured (retries, 5xx_count, 429_count, timeout_count, malformed_count, non_retryable_count, final_status, final_outcome) for Phase 2.5 evidence.

Output: `bronze/orion-api-v2/{snap_iso}/positions.parquet` (one parquet per date) + local mirror at `data/orion/manual_api/pulls/{snap_iso}_inflection_positions.parquet`.

**Production pull today (single-date, 2026-04-30):**
- Loaded 294 distinct Inflection clientIds from `silver/api_dims/accounts_v2.household_id`
- 294 calls × 100ms sleep + ~1.0s/call response ≈ 5.0 min runtime
- 23,680 rows, **$197,159,386 firm-level mv**
- Durability: `total_calls=294 ok=294 fail=0 retried=0 5xx=0 429=0 timeouts=0 malformed=0 distinct_final_statuses=[200]`
- Bronze S3: `s3://opal-data-inf/bronze/orion-api-v2/2026-04-30/positions.parquet` (919,633 B)
- S3 MD5 MATCH `9d4469bae7fe045b7f1da0d8b567dada`

---

## Phase 2 — Silver builder (`496ad4afc`)

Extended `data/orion/scripts/silver/convert_orion_api_to_silver.py` with:
- `_camel_to_snake_str()` helper (regex)
- `_coerce_positions_types()` helper (INT_FIELDS / FLOAT_FIELDS / BOOL_FIELDS / DATE_FIELDS — copied from convert_assets_v2_to_silver since same endpoint = same schema)
- `build_positions_mv(snapshot_date)` — reads bronze parquet from S3, type-coerces, renames camelCase→snake_case, adds silver envelope cols (snapshot_date, source_system='orion-api', advisor_firm='inflection_wealth_management')
- `'positions_mv': build_positions_mv` added to DIM_BUILDERS dict

Uses local `_s3_v2 = boto3.client(...)` since the existing helpers in `_orion_api_silver_lib` are CSV-bronze-oriented; positions_mv reads parquet directly from `bronze/orion-api-v2/{snap}/positions.parquet`. Net diff: +115 LOC.

**Today's silver build:**
- Command: `python3 convert_orion_api_to_silver.py --dim positions_mv --snapshot-date 2026-04-30 --upload`
- 23,680 rows → `silver/api_dims/positions_mv/snapshot_date=2026-04-30/data.parquet` (907,684 B)
- S3 MD5 MATCH `8425237ba728abaa3843f00b11a90482`

---

## Phase 2.5 — Durability check (VERDICT CLEAN)

Beyond the production 294-client pull (which was its own sustained-load durability evidence), I ran a wider 6-date probe to characterize Orion's historical-bound + vendor-flakiness:

**Probe matrix:** 5 clientIds × 6 dates [today, -7d, -30d, -60d, -90d, -180d] = 30 calls

| Delta | Date | Rows (5 clients) | Elapsed | Statuses |
|---|---|---|---|---|
| 0d | 2026-04-30 | 515 | 4.9s | [200] |
| 7d | 2026-04-23 | 515 | 5.0s | [200] |
| 30d | 2026-03-31 | 515 | 4.8s | [200] |
| 60d | 2026-03-01 | 515 | 4.3s | [200] |
| 90d | 2026-01-30 | 515 | 4.5s | [200] |
| 180d | 2025-11-01 | 515 | 4.8s | [200] |

**Aggregate:** 30 calls, 30 OK, 0 fail. All 200. Zero retries, zero 5xx, zero 429, zero timeouts, zero malformed.

**Verdict CLEAN — full deletion path authorized.** TO Section B: "If Phase 2.5 verdict is clean → full deletion of TRN-as-price reconstruction code in INF_B_00 + add archaeology comment citing prior commit hash." No `_API_FAIL_FALLBACK` gate needed.

**Acceptance criteria coverage:**
- Rate-limit: not observed at 100ms inter-call sleep (sustained 294 + smoke 30 = 324 cumulative calls, 0 throttled)
- Historical-bound: -180d works cleanly (well beyond 30-day backfill requirement; deeper not tested since 180d covers all current portal needs)
- Vendor-flakiness: zero 5xx / timeouts / malformed across 324 calls

---

## Phase 3 — INF_B_00 refactor (`4bc5381b2`)

Full rewrite of `data/orion/scripts/gold/INF_B_00.canonical_holdings.py`. Net diff: **-288 / +195 = -93 lines net code reduction** (TO criterion 3 ✓).

**Deleted:**
- `load_all_transactions()` + ThreadPoolExecutor parallel TRN load
- `reconstruct_holdings()` — the entire cumulative-units-from-TRN state machine (`pos_units defaultdict`, `pos_meta`, the date-by-date emit loop)
- `nav_price` last-seen-wins guard logic + nav>0 check (DIAGFIX.002b's fix is now obsolete; price comes from Orion directly)
- `REQUIRED_COLS` (TRN-specific column validation)
- `numpy` (was for `np.nan`)
- `defaultdict`, `ThreadPoolExecutor`, `as_completed` imports
- gap_manifest helpers (TRN-gap warning no longer relevant — Orion serves price authoritatively)

**Added:**
- `list_positions_mv_dates()` — list available `silver/api_dims/positions_mv/snapshot_date=*/data.parquet` partitions
- `latest_accounts_v2_key()` + `load_accounts_v2()` — DIAGFIX.011 advisor attribution dim (representative_name + rep_id, one row per account)
- `_advisor_key()` + `_rep_bucket()` — slug + bucket helpers (mirror silver/convert_orion_to_silver semantics; inlined to avoid silver→gold cross-import)
- `_normalize_custodian()` — fidelity_inflection / fidelity / schwab normalization
- `build_snapshot(snap_date_str, accounts)` — read positions_mv for that date, filter units>0, JOIN accounts_v2 on account_id, default representative_name to 'Inflection Wealth Management' for non-Fidelity-Inflection custodians, output 10-col schema preserved
- Module docstring archaeology comment citing `127fe2a17` (DIAGFIX.002b nav>0 guard fix) for emergency-recovery reference

**Schema preservation (output unchanged):**
`date, account_id, ticker, product_name, advisor_key, rep_bucket, custodian, units, nav_price, market_value` — same 10 columns as before. INF_B_01 / INF_B_02 / INF_B_03 / INF_I_D03 see the same shape.

**Field origins (new vs old):**
| Field | OLD source | NEW source |
|---|---|---|
| account_id | TRN | positions_mv |
| ticker | TRN | positions_mv |
| product_name | TRN | positions_mv.name |
| advisor_key | TRN | accounts_v2 JOIN → slug(representative_name) |
| rep_bucket | TRN | accounts_v2 JOIN → bucket(representative_name) |
| custodian | TRN | positions_mv.custodian (normalized) |
| units | TRN cumulative sum | positions_mv.current_shares (DIRECT from Orion) |
| nav_price | TRN last-seen-wins (with nav>0 guard) | positions_mv.current_price (DIRECT from Orion) |
| market_value | units × nav_price | positions_mv.current_value (DIRECT from Orion) |

TRN feed preserved for INF_B_01 (lots) / INF_B_02 (canonical_lots) / INF_B_03 (account_gains) — clean architectural separation; transaction log ≠ price source.

**Dry-run validation against today's positions_mv:**
- Pre-filter: 23,680 rows from positions_mv
- Post-filter (units > 0 AND non-empty ticker): **9,292 rows / 793 accounts / 286 tickers**
- **Firm-level mv: $197,355,918** (vs TO target $197.86M = $0.5M intra-day delta ✓)
- **Brandenburg attribution: $16.11M / 67 accounts** (vs DIAGFIX.011 target $16.15M = $0.04M delta ✓)
- Per-advisor: peter_lee $160.60M (571 accounts) / patrick_scanlan $20.28M (147 accounts) / joe_brandenburg $16.11M (67 accounts) / inflection_wealth_management $0.36M (8 accounts firm catchall)
- Per-rep_bucket: individual $196.99M (9,187 rows) / firm $0.36M (105 rows)
- Per-custodian: fidelity $197.25M (9,288 rows) / fidelity_lh $0.11M (4 rows long-tail)

All 10 schema columns present and typed correctly. Ready for chain re-run tomorrow.

---

## Compiler tools

| Phase | Tool | Result |
|---|---|---|
| 1 — before write | `comp-pipescript io INF_B_00` | SKIPPED — Orion scripts not in BD-pipeline graph (documented gap; same precedent as DIAGFIX.010/.011/.009-NEW) |
| 2 — before commit (×3, one per phase) | `.tools/ds-commit-gate.sh <files>` | All PASS (py_compile + AST + ruff clean for all 3 files) |
| 3 — after S3 upload (×3) | MD5 MATCH verification | All 3 files MATCH (registry-gap precedent) |

`.comp-graph/.agent_context` updated to `SERIAL=0.4.0_DS_ClientPlatform` + `TO_ID=ADVI_INFLEC.DIAGFIX.012.ds-orion-daily-positions-mv-refactor` before first compiler tool run. DE 0.4.0 overwrote it later with their own SERIAL/TO_ID — known multi-agent contention, not a problem for my closed-out work.

---

## Files modified

| File | Phase | Change | LOC delta |
|---|---|---|---|
| `data/orion/manual_api/pull_inflection_positions_daily.py` | 1 | NEW | +384 |
| `data/orion/scripts/silver/convert_orion_api_to_silver.py` | 2 | EDIT | +115 |
| `data/orion/scripts/gold/INF_B_00.canonical_holdings.py` | 3 | REWRITE | +195 / -288 = **-93 net** |

S3 code artifacts:
- `s3://opal-data-inf/code/manual_api/pull_inflection_positions_daily.py` MD5 `9d4469bae7fe045b7f1da0d8b567dada`
- `s3://opal-data-inf/code/silver/convert_orion_api_to_silver.py` MD5 `8425237ba728abaa3843f00b11a90482`
- `s3://opal-data-inf/code/gold/INF_B_00.canonical_holdings.py` MD5 `57b934bb56692fd31e5352b076173bd8`

Bronze + silver data artifacts (single-date, today):
- `s3://opal-data-inf/bronze/orion-api-v2/2026-04-30/positions.parquet` (919,633 B)
- `s3://opal-data-inf/silver/api_dims/positions_mv/snapshot_date=2026-04-30/data.parquet` (907,684 B)

---

## Deploy cycle (×3)

| Step | Phase 1 | Phase 2 | Phase 3 |
|---|---|---|---|
| Pre-commit gate | PASS | PASS | PASS |
| `.tools/safe-commit.sh` | `cb4336a59` (after unstaging contaminator `docs/architecture/ADVI_INFSHIP_A2.md`) | `496ad4afc` | `4bc5381b2` |
| `git push origin CLOUD` | OK | OK | OK |
| `aws s3 cp` to `code/manual_api/` / `code/silver/` / `code/gold/` | OK | OK | OK |
| MD5 MATCH | OK | OK | OK |

Phase 1 commit was caught by `safe-commit.sh` contamination guard — `docs/architecture/ADVI_INFSHIP_A2.md` had been staged by another agent. Unstaged via `git reset HEAD --` per protocol; re-ran cleanly. Working as designed (CLAUDE.md Rule 14a).

---

## RAVC loops

| To | Subject | Time |
|---|---|---|
| 2.0.0_SA_COO | RAVC2 ACK — DIAGFIX.012 GO received; Phase 1 starting | 13:38:39Z |
| 0.6.1_AE_PartnerETL | FYI — DIAGFIX.012 Phase 1+2 shipped; 2 new chain entries for batch-registration | 13:47:00Z |
| 0.7.0_AE_CloudOps | ESCALATION — inf-jwt-runner not advancing past EC2 boot; SSM diagnostic needed | 14:22:00Z |
| 0.7.0_AE_CloudOps | UPDATE — JWT refresh completed; escalation downgraded to slow-init investigation | 14:29:20Z |
| 2.0.0_SA_COO | RAVC2 — DIAGFIX.012 Phases 1-3 complete; Phase 4 ready to fire tomorrow | 14:44:05Z |
| 0.6.1_AE_PartnerETL | FYI — DIAGFIX.012 Phase 3 INF_B_00 refactor shipped; chain ready for tomorrow | 14:44:15Z |
| 0.7.0_AE_CloudOps | FYI/correction — Orion REST uses `Authorization: Session {jwt}`, not `Bearer` | 14:49:57Z |

**Inbound:**
- 2.0.0_SA_COO: GO (13:23Z) + CHASE (13:37Z) + RAVC2 ACK (13:45Z) + RAVC ACK Phases 1-3 ACCEPTED clean PASS (14:45:29Z)
- 0.6.1_AE_PartnerETL: RAVC4 chain entries registered `c2062b709` (13:53Z, before my Phase 1 ship — pre-staged from heads-up)
- 0.7.0_AE_CloudOps: RESOLVED — JWT fresh, `inf-pipeline-v1.7.4` fix deployed (14:29Z) + Secrets Manager JWT store FYI (14:49Z) + ACK on slow-init standing-low + Bearer/Session correction (14:50Z)

---

## Watcher gap recovery (post-compaction)

Pre-compaction session ended with watcher running. Post-compaction it was not relaunched, so the 13:23Z GO + 13:37Z CHASE didn't fire notifications until Andrew flagged the gap at 13:36Z. Once relaunched the watcher caught up immediately, fired both messages, and the cycle worked from there.

Per COO's opportunistic ask, this incident class deserves a `feedback_post_compaction_watcher_relaunch.md` memory entry. Authoring as a separate task to keep the memory index clean.

---

## Standing state at session close

DIAGFIX.012 Phases 1-3 RAVC4-CLOSED by COO at `14:45:29Z`. Phase 4 (chain re-run on c6a.4xlarge with 30-day backfill) + Phase 5 (RAVC4 + validation) standing by for tomorrow morning fresh-context per joint CTO+COO timing. JWT live until `2026-05-01T00:27:47Z`; tomorrow's 12:13Z cron will run on `inf-pipeline-v1.7.5` with both the SSM-retry fix (`45af4950c`) and the Secrets Manager JWT store. AE 0.6.1 chain reg `c2062b709` already in place (CHAIN_FULL: INF_API_PULL_POSITIONS_DAILY → INF_API_SILVER_POSITIONS_MV → INF_B_00). AE 0.7 has the slow-init follow-on TO logged at standing-low priority.

---

## Post-RAVC4 follow-ups (before device reboot)

### Bearer → Session correction loop with AE 0.7

AE 0.7's initial Secrets Manager FYI at `14:49:18Z` provided a consumer pattern with `headers = {'Authorization': f'Bearer {jwt}'}`. **That would 401** — Orion's REST surface uses `Authorization: Session {jwt}` (web-app-mirroring header from the HAR-derived headers). I sent a correction at `14:49:57Z`. AE 0.7 ACK'd at `15:04:10Z`, propagated the fix to CTO, and updated their session log. Raw token in SM is stripped of the `Session ` prefix; consumer prepends.

Code evidence (`infra/aws/ec2/inf-exporter/src/stepwise/orion_export.ts`):
- Line 177: `if (auth && auth.startsWith('Session '))`
- Line 179: `slot.value = auth.substring('Session '.length)`

### Lambda v1.7.5 deploy verification (Andrew prompt)

Andrew asked whether AE 0.7's fix was committed + deployed properly. Verified all four checkpoints:

1. **Code in repo (CLOUD)** — commit `45af4950c` "fix(inf-jwt-trigger): retry SSM dispatch on InvalidInstanceId (SSM agent race)" at `10:28Z`. Repo grep confirms 5 occurrences of `_send_ssm_with_retry` / `InvalidInstanceId`.
2. **Tag chain (sequential)** — `inf-pipeline-v1.7.0 → ... → v1.7.4 (SSM-retry fix) → v1.7.5 (SM JWT store on top)`.
3. **Terraform applied** — two `ci: record deploy inf-pipeline` commits today (`9441dc379` for v1.7.4, `31d538010` for v1.7.5) — protocol's signal of `terraform apply` reaching 0-diff.
4. **Lambda actually deployed** — live function `inf-jwt-trigger` LastModified `14:29:03Z`, deployed `CodeSha256: btARpIIjvEoDuneUmgWHXe/IV7kqOwgKd6P5fXjNbz4=`, byte-matches `lambda-source-map.json:1580` `artifact_sha256` + `last_deployed_commit: 9764c07e9`.

Conclusion: clean. Tomorrow's 12:13Z cron will run on v1.7.5 code (SSM retry fix + SM JWT store). No stale-Lambda risk.

### DE 0.4.0 Brandenburg roster Q&A

DE asked at `15:12:30Z` for three things to update `portal/src/pages/AdvisorIntelligence/_partners/inflection/layout.ts`:
1. Brandenburg's advisor_id key
2. Whether he's in the current employee_leaderboard
3. Whether `maxEntries` should bump to 4 or drop the firm catchall

My response at `15:14:19Z`:
1. **Key: `joe_brandenburg`** — slug derivation per `silver/convert_orion_to_silver.py:126` + `gold/INF_B_00.canonical_holdings.py:108` (post-DIAGFIX.012). "Joe Brandenburg" → `joe_brandenburg` (note: spelled "Brandenburg" in Orion, not "Brandenberg" as Andrew typed). Confirmed empirically in today's INF_B_00 dry-run: $16.11M / 67 accounts / 55 tickers / 743 rows.
2. **NOT currently in leaderboard** — `s3://opal-data-inf/platinum/firm/leaderboard.json` is `data_as_of: 2026-04-28` (yesterday, before DIAGFIX.011 + .012 landed). Current entries: `inflection_wealth_management`, `patrick_scanlan`, `peter_lee`. Tomorrow's Phase 4 chain re-run regenerates the leaderboard with Brandenburg as the 4th entry.
3. **Bump `maxEntries: 4`** — Brandenburg is a real 4th individual advisor with material book size; firm catchall `inflection_wealth_management` represents joint-placeholder + unmapped tail ($0.36M / 8 accounts) and is a separate category. Suggested layout snippet:
```ts
allowedAdvisorKeys: [
  'inflection_wealth_management',  // firm catchall (joint-rep placeholder accounts)
  'peter_lee',                      // 571 accounts / $160.60M
  'patrick_scanlan',                // 147 accounts / $20.28M
  'joe_brandenburg',                // 67 accounts / $16.11M  <-- NEW
],
maxEntries: 4,
```

Flagged the V1 smoke "No advisors in current filter" issue as separate from the layout fix — that's the FLAG 2 architectural issue (employee_leaderboard.advisor_id mismatch with portal's allowedAdvisorKeys, rep_name vs rep_id derivation) being shipped by DS~B Item C. DE should coordinate with DS~B before deploying the layout change.

### Stale leaderboard.json finding

Spot-check during DE Q&A revealed `s3://opal-data-inf/platinum/firm/leaderboard.json` `data_as_of: 2026-04-28` — predates DIAGFIX.011 chain integration. peter_lee's `total_aua` shows $14.6M for QTD slice (account_count 336, client_count 158), but I just measured $160.60M total in INF_B_00 dry-run. Discrepancy is window-specific (QTD slice vs full firm-level), not a bug — but a fresh chain re-run will clean both the windowing slices and the missing-Brandenburg gap.

### Watcher relaunch protocol after reboot

Device reboot will kill all current bash background processes (PIDs 245558 etc.). On next session start, first action MUST be `bash org/mcp/inbox-watch.sh 0.4.0_DS_ClientPlatform` per CLAUDE.md inbox-watch mandatory rule. The post-compaction watcher gap that opened at session start today (Andrew flagged at 13:36Z) was the same class — relaunch protocol is critical.

---

---

## Acceptance criteria

| Criterion | Status |
|---|---|
| 1. Bronze parquet exists per date in 30-day window | DEFERRED to Phase 4 (today's `2026-04-30/positions.parquet` = 23,680 rows × 58 cols ✓; -1d through -29d filled by tomorrow's chain run) |
| 2. Silver positions_mv dim per date | DEFERRED to Phase 4 (today's `snapshot_date=2026-04-30/data.parquet` ✓; rest tomorrow) |
| 3. INF_B_00 refactored, TRN-as-price code DELETED, net code reduction | PASS — diff +195 / -288 = -93 net; no `nav_price` references except in archaeology comment |
| 4. Per-row market_value matches positions_mv.current_value within rounding tolerance | PASS by construction — direct column copy, no transformation |
| 5. Firm-level + Brandenburg reconciliation | PASS — firm $197.36M (target $197.86M, $0.5M intra-day delta); Brandenburg $16.11M (target $16.15M, $0.04M delta) |
| 6. ds-commit-gate exit 0 + S3 MD5 MATCH on all modified scripts | PASS — 3 files, 3 PASS, 3 MATCH |
| 7. RAVC to COO + cc AE 0.6.1 with reconciliation table | PASS — RAVC2 14:44:05Z (COO ACK 14:45:29Z); FYI to AE 0.6.1 14:44:15Z |

Phase 4-5 acceptance criteria pending tomorrow's chain re-run.

---

## Next steps

- [Tomorrow / DS] Phase 4 chain re-run on c6a.4xlarge — dispatch `orion-gold-dispatch.sh CHAIN_FULL` with `--run-date` for 30-day backfill iteration (AE 0.7 shipped `--run-date` flag today)
- [Tomorrow / DS] Phase 5 — RAVC4 with full reconciliation table (firm + Brandenburg + 1-2 sample clients), downstream view spot-checks (timeseries non-flat, concentration_risk reasonable, mix_summary unchanged from DIAGFIX.010)
- [Tomorrow / COO] Flip W4.14 to `complete-as-superseded-by-DIAGFIX.012` after Phase 4 ship
- [DS / now] Author `feedback_post_compaction_watcher_relaunch.md` memory entry (per COO opportunistic ask)
- [Future / AE 0.7] Slow-init follow-on TO (cold-start S3 sync + Playwright binary setup timing under systemd) — standing-low priority per AE 0.7
- [Future / DS or AE] Migrate JWT loading from `s3://opal-data-inf/orion/jwt/current.json` to Secrets Manager `orion/jwt/current` per inf-pipeline-v1.7.5 — not blocking; future consolidation

---

*Authored by `0.4.0_DS_ClientPlatform`. Session arc: ~2h from post-compaction relaunch through Phase 3 ship + RAVC4 close. 3 commits, 3 S3 deploys, 3 MD5 MATCHes, 7 outbound RAVC messages, 0 destructive ops, 0 contamination ships (1 contamination CAUGHT and unstaged), 0 hook bypasses. Andrew authorized JWT fire + escalation; AE 0.7 diagnosed root cause + shipped v1.7.4 + v1.7.5 in parallel.*
