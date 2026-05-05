# Session Log — DS~D AUDIT-008 + AUDIT-009 — 2026-05-05

**Agent:** 0.4.0_DS_ClientPlatform~D
**Date:** 2026-05-05
**Session covers:** ADVI_INFLEC.AUDIT-008 (AUA strip stale $183M) + AUDIT-009 (activity_scan/cash_drag per-row AUA=0)

---

## AUDIT-009 — activity_scan / cash_drag zero-AUA (closed)

### Phase 0 — Root cause investigation

**Scope:** Per-row AUA=0 in activity_scan.json (307 rows) and cash_drag.json (295 rows), observed by RD at ~18:12Z.

**S3 state at investigation time:**
- `platinum/firm/activity_scan.json` — generated 14:04Z today (fresh)
- `platinum/firm/cash_drag.json` — generated 14:06Z today (fresh)
- sample from activity_scan: `{aua: $4.47M}` non-zero rows confirmed

**Code trace (INF_D_05.activity_scan.py):**
- AUA source: `load_latest_holdings_aua()` reads `gold/holdings/` (INF_B_01 output)
- Join: `holdings.merge(accts_dim, on='account_id', how='left')` — account_id-based
- `gold/holdings/2026-04-28.parquet` market_value sum: $189.2M confirmed
- 9295/9295 account_id matches (100% join rate)
- 12 zero-AUA rows: expected (zero-balance/new-account households) — not a bug

**Verdict:** (b) stale D-chain artifact. S3 artifacts ARE fresh as of 14:04-14:06Z. RD observation at 18:12Z may have been browser/Lambda cache. DS~C's chain-full re-fire (AUDIT-002 step 4) produced the 14:04Z fresh artifacts. No code fix needed.

**AUDIT-009 verdict sent to COO:** 20260505T182136Z. Accepted.

**AC status:** CLOSED (no TO, no code change, no matrix cell — stale artifact misread)

---

## AUDIT-008 — dashboard.json AUA strip stale (in progress → tomorrow)

### Background

- dashboard.json total_aua = $182,552,380 @ generated_at 2026-05-04T16:16:27Z (stale)
- Expected: ~$199M (matching silver/assets_v2/2026-05-05.parquet AUA = $199,452,889)
- Root cause: bronze/positions/ stale through 2026-04-30; INF_B_00 had no May silver to process

### PATH A execution (AE 0.7 pinch-hit — AE 0.6.1 went dark)

AE 0.6.1 had 2 unread URGENT COO messages; AE 0.7 pinch-hit pre-authorized by CTO (20260505T183037Z).

| Dispatch | Command ID | Status | Outcome |
|----------|-----------|--------|---------|
| 1a | 281595b5 | Complete | Bronze pull only (path issue) |
| 1b | ad90f1dd | Complete | Same path issue |
| 1c | a16868ef | Complete | watchdog path fix; bronze confirmed |
| 1d | 84c01de8 | Complete | Silver convert — WRONG PATH (flat silver/positions_mv/) |
| 1e (canonical) | — | Complete | Correct Hive paths written 15:30Z |

**D1d path bug (DS~D discovery):**
- D1d wrote: `silver/positions_mv/{date}.parquet` (flat, missing `api_dims/`)
- INF_B_00 reads: `silver/api_dims/positions_mv/snapshot_date={date}/data.parquet` (Hive)
- Escalated to COO 20260505T192350Z; Scenario A confirmed via top-level ls
- Root cause: D1d used AE 0.7 custom wrapper bypassing `write_silver_api_dim_parquet`

**Silver Hive partitions confirmed (15:30-15:31Z):**
| Date | Size |
|------|------|
| snapshot_date=2026-05-01/data.parquet | 931,533 B |
| snapshot_date=2026-05-02/data.parquet | 930,928 B |
| snapshot_date=2026-05-03/data.parquet | 930,949 B |
| snapshot_date=2026-05-04/data.parquet | 930,213 B |
| snapshot_date=2026-05-05/data.parquet | 929,992 B |

**dashboard.json at session end:** still $182,552,380 @ 2026-05-04T16:16:27Z — chain-full (D2) pending.

**Strategic pivot (Andrew, ~19:32Z):** "we need to just get all the data up to date and set up the pipelines." D2 chain-full deferred to tonight's comprehensive AE 0.7 catch-up. RPBKTPI.001 AC4 verification pushes to tomorrow.

### Path Audit Deliverable

Delivered to COO: `convert_orion_api_to_silver.py` code-trace confirming all 8 dims correct.

| Dim | Expected S3 path | Format |
|-----|-----------------|--------|
| household | `silver/api_dims/household/snapshot_date={date}/data.parquet` | Hive ✓ |
| performance | `silver/api_dims/performance/snapshot_date={date}/data.parquet` | Hive ✓ |
| activity | `silver/api_dims/activity/snapshot_date={date}/data.parquet` | Hive ✓ |
| billing | `silver/api_dims/billing/snapshot_date={date}/data.parquet` | Hive ✓ |
| accounts_v2 | `silver/api_dims/accounts_v2/snapshot_date={date}/data.parquet` | Hive ✓ |
| representatives | `silver/api_dims/representatives/snapshot_date={date}/data.parquet` | Hive ✓ |
| household_rep_mapping | `silver/api_dims/household_rep_mapping/snapshot_date={date}/data.parquet` | Hive ✓ |
| positions_mv | `silver/api_dims/positions_mv/snapshot_date={date}/data.parquet` | Hive ✓ |

`_orion_api_silver_lib.py` local = S3 code/gold/ = IDENTICAL (diff confirmed, 9524 bytes). Canonical script architecturally clean. No reauthoring needed.

Audit accepted by COO as ADVI_INFINGE PRD v0.2 §5 Compiler Evidence input.

---

## Compiler Tools Log

| Tool | Target | Result | Notes |
|------|--------|--------|-------|
| aws s3 ls | silver/api_dims/positions_mv/ | top-level Hive dirs confirmed | comp-pipescript targets opal-data-bd, manual S3 substituted |
| aws ssm get-command-invocation | 84c01de8 / i-0ed5afded2ebd4ed4 | D1d flat-write confirmed | Root cause discovery |
| diff | _orion_api_silver_lib.py vs S3 | IDENTICAL | Path correctness confirmed |

---

## AUDIT-003a — Hardcoded INFLECTION_REP_IDS missing rep_id=6 (sibling fix)

**Discovery:** hardcoded-mapping audit (COO parallel prework assignment ~20:00Z) surfaced 5 BUG(b) instances where `INFLECTION_REP_IDS` excluded joe_brunswick rep_id=6. Highest-priority: `INF_D_00c.portal_leaderboard.py:446` default arg — firm perf aggregate actively excluded joe from D2c chain already running.

**Files fixed (4 code edits):**

| File | Line | Before | After |
|------|------|--------|-------|
| `silver/_orion_api_silver_lib.py` | 36 | `{3, 11, 12}` | `{3, 6, 11, 12}` — ROOT |
| `silver/convert_orion_to_silver.py` | 105 | `'inflection': {3, 11, 12}` | `{3, 6, 11, 12}` |
| `gold/INF_D_08.nmec_nmnc_nna.py` | 17 | `frozenset({3, 11, 12})` | `frozenset({3, 6, 11, 12})` |
| `gold/INF_D_00c.portal_leaderboard.py` | 446 | default `('3','11','12')` | `('3','6','11','12')` |

`build_billing_dim.py` + `build_tax_dim.py` auto-fix via lib import — no independent patches.

**Gate:** pre-commit gate PASS x4 (py_compile + AST + ruff)
**Commit:** `202fddb3b` — pushed to CLOUD
**S3:** all 4 files MATCH (silver/code/ + gold/code/)
**COO RAVC4:** accepted (~20:07Z); 7-min sprint acknowledged

**D2d re-fire:** AE 0.7 routing `--from INF_D_00c` post D2c completion to produce joe-inclusive leaderboard.json + INF_D_08 nmec/nmnc artifacts.

---

## Commits This Session

| Commit | Message | Status |
|--------|---------|--------|
| `14cb47db3` | log(AUDIT-008/009): DS~D session log | PUSHED |
| `202fddb3b` | fix(ADVI_INFLEC): AUDIT-003a rep_id=6 — 4 files | PUSHED |

---

## D2c Empirical Results (20:19Z)

from_INF_C_00 completed 20:19Z. Key findings:

| Artifact | AUA | generated_at | Status |
|----------|-----|-------------|--------|
| leaderboard.json | $199,649,186 | 20:18:41Z | PASS — 4 advisors incl. joe |
| dashboard.json | $182,552,380 | 20:18:26Z | FAIL — still stale |
| header_metrics.json | $182,552,380 | 20:19:10Z | FAIL — gold/holdings source |
| nmec_nmnc_nna.json | $198,867,318 (bronze) | 20:19:44Z | OK — bronze-direct |

**Root cause of dashboard.json stale AUA:** Chain ran `from_INF_C_00` — skipped INF_B_00/INF_B_01. `gold/holdings/` max = 2026-04-28. `silver/api_dims/positions_mv/` HAS May 1-5 Hive partitions but INF_B_00 has not processed them.

**AUDIT-003a leaderboard PASS:** 4 entries in all windows (QTD/YTD/MAX). joe_brunswick/joe_brandenburg present.

### RPBKTPI.001 AC4 Cross-Validation

| Advisor | QTD period_start_aua | YTD | MAX |
|---------|---------------------|-----|-----|
| Peter Lee | $3,732,424 PASS | None FAIL | None FAIL |
| Patrick Scanlan | $266,118 PASS | None FAIL | None FAIL |
| Joe Brandenburg | None FAIL | None FAIL | None FAIL |
| Firm (aggregate) | None | None | None |
| lifecycle_aua | 0.0 all advisors all windows — suspect |

**Joe QTD None root cause:** `silver/api_dims/performance/` max = 2026-04-28; pre-AUDIT-003a partitions excluded rep_id=6. Need silver performance regeneration with rep_id=6.

**YTD/MAX all-None root cause:** performance dim likely has no 2026-01-01 anchor. DS~C to assess.

Dispatched: COO + DS~C + AE 0.7 20260505T202248Z. AE 0.7 chain-full `from_INF_B_00` requested.

---

## D2d Empirical Results (20:24Z)

from_INF_D_00c completed 20:24Z (AE 0.7 re-fire after AUDIT-003a commit). New platinum outputs:
- `nmec_nmnc_nna.json` — 16:24 local (joe-inclusive per INFLECTION_REP_IDS={3,6,11,12})
- `cash_drag.json`, `concentration_risk.json` — 16:24 local

dashboard.json NOT updated by from_INF_D_00c (INF_D_00 is upstream of INF_D_00c, not downstream).
Dashboard AUA still $182,552,380 @ generated_at 2026-05-05T20:23:35Z.

---

## D3 B-chain Confirmation (20:45Z)

AE 0.7 dispatched INF_B_00. B-chain completed 20:45 local:

| File | Timestamp |
|------|-----------|
| gold/canonical/holdings_2026-05-01.parquet | 16:45 local |
| gold/canonical/holdings_2026-05-02.parquet | 16:45 local |
| gold/canonical/holdings_2026-05-03.parquet | 16:45 local |
| gold/canonical/holdings_2026-05-04.parquet | 16:45 local |
| gold/canonical/holdings_2026-05-05.parquet | 16:45 local |

No downstream C+D chain log appeared after 16:45 — from_INF_C_00 NOT yet dispatched as of 21:06Z.

**D3 escalation (21:06Z):** DS~D pinged COO + AE 0.7 requesting --from INF_C_00 dispatch.
Status: awaiting response.

---

## ADVI_LDRBRD.001 — INF_D_00c Bug A + Bug C Pre-Authoring

**Scope:** Two bugs identified via INF_D_00c code trace (Phase 0 audit, D2c empirical):

| Bug | Root cause | Fix |
|-----|-----------|-----|
| A — MAX window period_start_aua=None | `_aua_at_start` returns empty df when no holdings snapshot <= window_start (holdings oldest = 2026-04-26; MAX window_start = ~2023) | Fallback: use `keys[0]` (earliest available snapshot) |
| C — lifecycle_aua=0 all advisors | `accounts_v2_dim` never loaded/passed to `_compute_hh_lifecycle` | Load `silver/api_dims/accounts_v2/`, pass through `compute_leaderboard_entries` → per-advisor and firm calls |

**7 edits pre-authored (all gate-passing — py_compile + AST + ruff PASS):**

1. New constant `SILVER_API_ACCOUNTS_V2_PREFIX`
2. New loader `load_accounts_v2_dim()` (graceful fallback on missing partition)
3. `_aua_at_start` fallback: `keys[0]` when no snapshot <= window_start (Bug A)
4. `compute_leaderboard_entries` signature: add `accounts_v2_dim=None`
5. Per-advisor `_compute_hh_lifecycle` call: pass `accounts_v2_dim=accounts_v2_dim`
6. Firm `_compute_hh_lifecycle` call: pass `accounts_v2_dim=accounts_v2_dim`
7. `main()`: load `accounts_v2_dim`, pass to `compute_leaderboard_entries`

**Status: HOLD** — COO message 20260505T: "hold Bug A+C until D-chain finish. Ship trigger: dashboard.json headline.total_aua ~$199M."
Edits are in working tree, NOT yet committed.

**Ship sequence (on D3 RAVC5''):**
1. `.tools/safe-commit.sh --author "0.4.0_DS_ClientPlatform_D <0.4.0_DS_ClientPlatform_D@opal.agent>" -m "feat(ADVI_LDRBRD.001): INF_D_00c MAX window fallback (Bug A) + accounts_v2_dim lifecycle wiring (Bug C)" -- data/orion/scripts/gold/INF_D_00c.portal_leaderboard.py`
2. `git push origin CLOUD`
3. `aws s3 cp data/orion/scripts/gold/INF_D_00c.portal_leaderboard.py s3://opal-data-inf/code/gold/`
4. `comp-pipescript deployed INF_D_00c` → verify MATCH
5. RAVC3 to COO + AE 0.7 → D4 `--from INF_D_00c`

**Bug B (YTD all-None):** performance dim has no pre-2026 anchor — separate fix, DS~C to assess scope.

---

## Open Items / Next Session

| Item | State | Owner |
|------|-------|-------|
| dashboard.json total_aua ~$199M | PENDING D3 --from INF_C_00 dispatch | AE 0.7 |
| D3 --from INF_C_00 dispatch | ESCALATED to COO+AE 21:06Z | COO/AE 0.7 |
| leaderboard.json joe-inclusive (AUDIT-003a) | COMPLETE — $199.6M, 4 advisors | CLOSED |
| ADVI_LDRBRD.001 Bug A+C INF_D_00c edits | HOLD pending dashboard ~$199M | DS~D |
| RPBKTPI.001 AC4 joe QTD period_start_aua | PENDING silver/performance regen w/ rep_id=6 + D4 | AE 0.7 + DS~C |
| RPBKTPI.001 AC4 YTD/MAX all-None | PENDING DS~C assessment | DS~C |
| lifecycle_aua all-zeros | PENDING LDRBRD.001 Bug C ship + D4 | DS~D → AE 0.7 |
| matrix v9/v10 cross-validation | PENDING DS~A patch | DS~D |
| ADVI_INFINGE Phase 1 TO authoring | PENDING | COO |
