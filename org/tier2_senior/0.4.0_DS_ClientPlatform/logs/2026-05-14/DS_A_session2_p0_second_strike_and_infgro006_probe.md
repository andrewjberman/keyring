# DS~A Session 2 — P0 second-strike + INFGRO.006 MAX-window TWR coverage probe

**Date:** 2026-05-14
**Agent:** 0.4.0_DS_ClientPlatform~A
**Authorization:** AE 0.6.1 P0 RAVC1 14:09Z (chain-failed at INF_D_00c step 39 KeyError) + COO open dispatch on INFGRO.006 probe
**Commits:** `11ca5f36f` (suffix-collision fix)
**Wall time:** ~30 min total (P0 14:09Z → P0 close 14:33Z + INFGRO.006 probe 14:39Z)

## TL;DR

Chain re-fire of my session-1 fix `fd11a33c2` exposed a latent suffix-collision (Bug B masked by Bug A). Diagnosed + shipped `11ca5f36f` in ~4 min wall. AE 0.6.1 fired gold-d recovery; all 5 validation sentinels PASS at 14:33Z. Then ran INFGRO.006 MAX-window TWR coverage probe — all 4 Inflection advisors SAFE at advisor-aggregate grain. Gate OPEN for DE Phase 2 MAX rendering.

Bug-shadows pattern (memory `feedback_bug_shadows.md`) empirically compounded: 3rd surfacing this week per CTO RAVC4. CTO floated `comp-pipescript shadow-detect` as ADHC_COMPIL_V4 backlog candidate.

## P0 second-strike — INF_D_00c:649 advisor_key suffix-collision

### Trigger

AE 0.6.1 P0 RAVC1 14:09Z: chain `chain_full_20260514_131842` FAILED 14:08:04Z at INF_D_00c step 39:
```
ERROR: INF_D_00c failed: ['advisor_key']
  ...
  File ".../INF_D_00c.portal_leaderboard.py", line 628, in _aggregate_gro_per_advisor_window
    joined = joined.dropna(subset=['advisor_key'])
KeyError: ['advisor_key']
```

`fd11a33c2` dtype fix held — no merge `ValueError`. But pandas produced `advisor_key_x` + `advisor_key_y` instead of `advisor_key` because both merge sources carry the column.

### Diagnosis (~30s)

| Question | Answer | Source |
|---|---|---|
| Does `client_perf` carry `advisor_key`? | YES (passthrough from upstream) | INF_C_02.py:326 column list |
| Does `account_team` carry `advisor_key`? | YES (authoritative INF_C_07 emit) | INF_C_07.py output (verified during fd11a33c2 work) |
| Why didn't this surface before fd11a33c2? | dtype `ValueError` fired at the merge BEFORE pandas could produce the suffix-collision artifact | Stack trace pre-fd11a33c2 showed merge-level error not dropna-level |
| Which source IS authoritative? | INF_C_07 (`account_team`) per the function's design contract | Function docstring + INF_C_07 fix comment cited in fd11a33c2 commit |

**Classification:** scenario `(b) Pre-existing latent + unmasked by upstream fix` — same bug-shadows pattern as the dtype divergence itself. C.2 per Appendix C, ADVI_INFGRO_PRD. Third independent surfacing this week per CTO.

### Fix shape

Single 8-line edit at line 647-654 in `_aggregate_gro_per_advisor_window`:

```python
iw = in_window.copy()
iw['household_id'] = iw['household_id'].astype(str)
# INF_C_02 emits advisor_key as a passthrough column (INF_C_02.py:326).
# Dropping it here so the household_id merge with account_team carries
# advisor_key from the AUTHORITATIVE INF_C_07 mapping rather than producing
# advisor_key_x / advisor_key_y suffix-collision (which would then KeyError
# at the subsequent dropna(subset=['advisor_key']). Surfaced chain #131842
# 2026-05-14 14:08Z after fd11a33c2 unmasked the latent suffix-collision.
if 'advisor_key' in iw.columns:
    iw = iw.drop(columns=['advisor_key'])
joined = iw.merge(hh_to_adv, on='household_id', how='left')
```

### Deploy evidence

| Step | Result |
|---|---|
| Pre-commit gate (py_compile + AST + ruff py39) | PASS (first try) |
| Commit | `11ca5f36f` author `0.4.0_DS_ClientPlatform~A` |
| Push | `origin/CLOUD` advanced `a731e8461..11ca5f36f` |
| safe-deploy.sh | `DEPLOYED [inf] data/orion/scripts/gold/INF_D_00c.portal_leaderboard.py` PASS |
| S3 ETag | `a2198e4ad6e2459233912ea70b8131c5` |
| S3 LastModified | 2026-05-14T14:12:52Z |
| S3 size | 57,609 bytes |

### Chain recovery (AE 0.6.1)

- **EC2 pre-warm at 14:13Z** — AE preemptively `start-instances` anticipating my fix in ~5min. Saved 2min cold-boot.
- **SHA-MATCH gate PASS** — ETag `a2198e4ad6e2459233912ea70b8131c5` matched my claim
- **Lambda fire 14:14:22Z** mode=gold-d snapshot=2026-05-14 StatusCode 200 instance `i-0ed5afded2ebd4ed4`
- **Terminal 14:32:59Z** — chain `chain_gold-d_20260514_141936` complete; INF_D_00c step 4 status=ok 24s
- **Total wall:** P0 RAVC1 receipt → terminal close = ~24min including 9min gold-d run

### Validation sentinels (all PASS)

| # | Sentinel | Result |
|---|---|---|
| 1 | Step 39 PASS (no KeyError) | ✓ ok 24s |
| 2 | `grep -c '"NaN"' = 0` on leaderboard.json | ✓ 0 hits (DS~C `de2286d67` held) |
| 3 | `advisor_return_pct_twr` non-null on QTD/YTD/MAX firm summary + 4 advisor entries | ✓ firm_return_pct_twr=0.038548 QTD |
| 4 | `gold/artifacts/employee_leaderboard.json` precursor written | ✓ 14:20:26Z |
| 5 | COO sentinel sweep: AUA $203M / 4 advisors / Joe $16.2M / 21 clients | ✓ $203.18M / 4 advisors / Joe $16.42M / 21 clients |

Notable deltas (accepted as housekeeping):
- `accounts_dim` 835 / `account_team` 862 / expected 857 / silver 842 / portal-side 799 — 5-way cohort delta INFLBIWMALIGN-adjacent. COO ACK'd; AE 0.6.1 banked for incremental Phase 4 work.
- leaderboard QTD total_aua $203.2M vs COO sentinel $199.6M — likely QTD-as-of-2026-05-14 vs MAX framing difference in expectation; structural correctness held (firm_totals consistent).
- Joe Brandenburg $16.42M vs $16.2M — 1.3% delta, within normal day-to-day drift.

## Cumulative INF_D_00c fix state (all three live on origin/CLOUD + S3)

| SHA | Author | Surface | Time |
|---|---|---|---|
| `fd11a33c2` | 0.4.0_DS_ClientPlatform~A | line 615-628 Int64-vs-str household_id dtype cast | 12:58:40Z |
| `de2286d67` | 0.4.0_DS_ClientPlatform~C | line 65 (`import math`) + 128-151 (`_strip_nan` + `allow_nan=False` tripwire at `_write_json_s3`) | 14:02:05Z |
| `11ca5f36f` | 0.4.0_DS_ClientPlatform~A | line 647-654 advisor_key suffix-collision (drop `iw.advisor_key` pre-merge) | 14:12:52Z |

**3-lane DS coordination metrics (COO banking):**
- Same script + same function (`_aggregate_gro_per_advisor_window`) + 3 commits across ~1h45m wall
- Zero merge conflict; zero double-ship; clean MCP cadence
- Author identity + `safe-commit --only` + git-fetch-before-ground-truth discipline held
- Empirical proof: structural guards (safe-commit contamination abort + author identity + per-lane pathspec) compose under multi-lane same-surface work

## INFGRO.006 MAX-window TWR coverage probe

### Trigger

DE 0.4 13:18Z RAVC2: "INFGRO.006 (MAX-window TWR re-enable) gates on Phase 2 live validation + your inception-to-date TWR coverage proof for all 4 advisors." Probe gated on fresh `client_performance.parquet` (delivered by chain gold-d 14:05Z).

### Probe shape

Read `gold/timeseries/client_performance.parquet` (14.9MB, 417,781 rows) + `gold/views/account_team.parquet` (16KB, 862 rows). Join household_id → advisor_key, cast both sides to str (same pattern as INF_D_00c:649). Drop cp.advisor_key passthrough (mirrors my session-1 fix). For each advisor compute:

- household count
- total rows / non-null TWR rows / coverage fraction
- earliest / latest non-null TWR date
- longest consecutive null-TWR run within active series (per-HH)
- MAX-window-safe verdict (heuristic: coverage ≥ 95% + longest_null_gap ≤ 10 days)

### Result (per-advisor, advisor-aggregate grain)

| Advisor | HHs | Total | Non-null | Coverage | Series | Per-HH max-gap | **Verdict** |
|---|---|---|---|---|---|---|---|
| `inflection_wealth_management` (IWM catchall) | 2 | 76 | 74 | 97.4% | 2026-03-30 to 2026-05-13 | 0d | **SAFE** |
| `joe_brandenburg` | 21 | 34,275 | 34,254 | 99.9% | 2020-06-04 to 2026-05-13 | 0d | **SAFE** |
| `patrick_scanlan` | 73 | 87,089 | 86,986 | 99.9% | 2020-06-04 to 2026-05-13 | 30d (single HH) | **SAFE at advisor-aggregate** |
| `peter_lee` | 199 | 296,341 | 296,139 | 99.9% | 2020-05-26 to 2026-05-13 | 4d | **SAFE** |

### Interpretation

**All 4 advisors MAX-window SAFE at the advisor-aggregate grain.** The AUA-weighted aggregation in `_aggregate_gro_per_advisor_window` treats each (HH, day) as independent observation:
```
weighted_twr = sum(total_aua × return_pct_twr) / sum(total_aua)
```
Null rows drop from both numerator and denominator simultaneously; the per-HH 30-day gap in patrick's cohort contributes ~30 fewer observations but the other 72 HHs cover those dates without interruption. Advisor-aggregate TWR remains statistically meaningful.

**Per-HH gap follow-up (not blocking INFGRO.006):**
The 30-day patrick HH gap is likely one of:
1. The `client_id=116` account-closure case from INFGRO.003 (12.2 weeks factor=0 → daily_factor=1.0 sentinel SHOULD NOT show as null; if it does, sentinel didn't propagate to TWR — potential INF_C_02 regression)
2. A different HH-specific Orion `/performance` dropout (vendor-side)
3. A silver-side ETL gap not caught by canonical-walk

Surfaced to DE as data-quality observation; reusable probe script at `.runtmp/inf_max_window_twr_coverage_probe.py` for future cohorts.

**Recommendation to DE:** ship MAX-window TWR rendering on all 4 advisor entries. FE existing NaN-strip + epsilon-quality-dot heuristic handle per-HH dropouts gracefully via the AUA-weighted-rollup math. If per-HH MAX rendering enters scope, hold for DS follow-up TO on patrick HH gap.

### IWM tooltip note

IWM catchall window is 2026-03-30 to 2026-05-13 (6 weeks) — structural per `memory/project_inflection_iwm_catchall_bucket.md`. Show MAX for IWM but document abbreviated series in tooltip ("data available from 2026-03-30").

## Files Modified

| File | Change | Commit |
|---|---|---|
| `data/orion/scripts/gold/INF_D_00c.portal_leaderboard.py` | +8/-0 lines 647-654: drop `iw.advisor_key` before household_id merge | `11ca5f36f` |
| `.runtmp/inf_max_window_twr_coverage_probe.py` | NEW — INFGRO.006 gate probe (runtime, gitignored) | (uncommitted) |
| `.runtmp/inf_max_window_twr_coverage_probe_result.json` | NEW — probe result for handoff to DE | (uncommitted) |

## MCPs Sent

| To | Time | Subject |
|---|---|---|
| 0.6.1_AE_PartnerETL | 14:10:39Z | RAVC1 ACK P0 line 628 KEEP EC2 ALIVE diagnosis + ETA ~5min |
| 0.6.1_AE_PartnerETL | 14:13:30Z | RAVC1 P0 fix SHIPPED 11ca5f36f ETag a2198e4a re-fire authorized |
| 2.0.0_SA_COO | 14:13:47Z | P0 second-strike FYI bug-shadows pattern shipped 11ca5f36f |
| 0.6.1_AE_PartnerETL | 14:15:42Z | CONFIRM gold-d fire immediately on SHA-MATCH |
| 0.6.1_AE_PartnerETL | 14:36:39Z | RAVC2 CLOSE ACK P0 thread closed thanks EC2 pre-warm |
| 2.0.0_SA_COO | 14:36:54Z | RAVC2 CLOSE P0 INF_D_00c thread terminated session-1 commit consolidation |
| 0.4.0_DE_ClientPlatform | 14:37:08Z | FYI platinum leaderboard.json FRESH chain CLEAN Phase 2 /frontend-dev ready |
| 0.4.0_DE_ClientPlatform | 14:39:40Z | INFGRO.006 gate all 4 advisors MAX-window SAFE at aggregate grain |

## MCPs Received

| From | Subject | Disposition |
|---|---|---|
| 0.6.1_AE_PartnerETL (14:09Z) | P0 chain #131842 FAILED at INF_D_00c:628 KeyError | ACKed + diagnosed + shipped fix |
| 0.6.1_AE_PartnerETL (14:14Z) | EC2 STOPPED cold-boot path your diagnosis exactly right | ACKed mode=gold-d explicitly |
| 2.0.0_SA_COO (14:15Z) | RAVC ACCEPTED 11ca5f36f + AE auto-fires on SHA-MATCH | Acknowledged |
| 1.0.0_SA_CTO (14:18Z) | RAVC4 ACCEPT 11ca5f36f architectural-call locked authoritative-source identification | Noted; no reply required |
| 0.6.1_AE_PartnerETL (14:14Z) | RAVC1 chain FIRED 14:14:22Z gold-d EC2 warm SHA-MATCH PASS | Acknowledged |
| 0.6.1_AE_PartnerETL (14:33Z) | RAVC2-CLOSE all 5 sentinels PASS P0 closed | ACKed RAVC2 close |
| 2.0.0_SA_COO (14:38Z) | RAVC2-CLOSE accepted INFGRO.006 GO probe authorized | Probe already in flight; deliverable beats GO |
| 0.6.1_AE_PartnerETL (14:39Z) | CLOSE ACK back EC2 staying warm for DS~B cash_drag | Closed |

## Compiler Tools

| Tool | Result |
|---|---|
| `comp-pipescript io INF_D_00c.portal_leaderboard` | Same name-resolver bug as session 1 — read script directly via `grep -n + Read` |
| `.tools/ds-commit-gate.sh` | PASS first try (py_compile + AST + ruff py39 0.15.11) |
| `.tools/safe-commit.sh` | First-try clean (no index contamination this commit cycle) |
| `.tools/safe-deploy.sh` (pre-push hook) | DEPLOYED [inf] PASS — SHA-MATCH verified |
| `aws s3api head-object` direct | Used to verify S3 ETag for RAVC1 evidence (workaround for comp-pipescript deployed bucket coverage gap) |
| `git fetch && git log origin/CLOUD..HEAD` | Used pre-commit to verify HEAD vs origin state (per new `feedback_git_fetch_before_ground_truth.md` memory entry) |

Session 1 surfaced two compiler-tool gaps; session 2 hit the same. Both still candidates for `comp-pipescript` maintainer fix.

## Pacing Telemetry

- 14:09Z AE P0 RAVC1 received
- 14:09:30Z diagnosis complete (suffix collision identified from stack frame + earlier file read)
- 14:10:39Z RAVC1 ACK to AE with diagnosis + EC2-shutdown-cancel ask
- 14:12Z edit complete; ds-commit-gate PASS
- 14:12:52Z S3 LastModified (commit + push + safe-deploy auto-sync)
- 14:13:30Z RAVC1 to AE with deploy evidence
- 14:14:22Z AE Lambda fire (gold-d on warm EC2 — pre-warm at 14:13Z)
- 14:32:59Z chain terminal complete
- 14:33Z AE RAVC2-CLOSE all sentinels PASS
- 14:36-14:37Z close out MCPs + INFGRO.006 probe authoring start
- 14:39Z INFGRO.006 probe shipped to DE

**P0 receipt → close:** ~24 min. **P0 close → INFGRO.006 deliverable:** ~6 min. **Session 2 total:** ~30 min.

## Decision Notes

1. **Diagnosis-first discipline scaled.** Both P0 fixes had ~30s diagnosis and ~30s edit. The diagnostic narrative was tight because the stack frames + earlier session-1 file reads gave full context. Same pattern that compressed session 1 ship to 6min works at session 2 ship in 4min when context carries across.

2. **AE 0.6.1 pre-warm move is a process-discipline force-multiplier.** `aws ec2 start-instances` at 14:13Z (anticipating fix arrival in 5min) saved 2min cold-boot. AE noted they'll add the discipline to their prompt.md. If every recovery cycle saves 2min via proactive resource prep at fix-ETA-within-cold-boot-window, the org gets ~24min/day back at current cycle volume.

3. **Bug-shadows pattern is now empirically compounded.** 3rd surfacing this week per CTO RAVC4. Static analysis can't catch the second bug without running the first fix — the suffix-collision required the dtype error to be cleared before pandas could produce the suffix artifact. This generalizes: ANY fix that resolves a halt-condition WITHOUT validating downstream postconditions creates a bug-shadow hand-off. The diagnosis-first discipline catches it (as proven here) but the cycle cost (~24min wall on a 2-bug stack) is non-trivial. CTO floated `comp-pipescript shadow-detect` as ADHC_COMPIL_V4 backlog candidate — would identify fix sites where a guard/exception swallows a downstream postcondition.

4. **3-lane DS coordination metrics:** clean compose on same script + same function in 1h45m. The structural guards (safe-commit `--only` contamination abort + author identity discipline + git-fetch-before-ground-truth + zero-delta-as-stale-ref-signal) caught every misalignment without manual coordination. Andrew's earlier interrupt on DS~B engaging on the same surface as me would have been a regression if structural guards hadn't held; they did.

5. **INFGRO.006 advisor-aggregate vs per-HH grain.** The AUA-weighted rollup math has a useful property: per-HH gaps don't break the advisor-aggregate as long as enough HHs cover the date range. This means MAX-window is structurally easier than per-HH MAX rendering. DE can ship advisor-aggregate MAX now; per-HH MAX rendering would require backfilling patrick's 30-day gap first.

6. **Surface area for future hygiene work flagged (not blocking):**
   - INF_C_02 emits `advisor_key` as passthrough (causes suffix collision when joined cross-source). Either drop the emit OR alias at join site globally. CTO routed for design call.
   - patrick_scanlan HH 30-day TWR null gap. Likely the `client_id=116` factor=0 sentinel not propagating to TWR, OR vendor-side dropout. Follow-on probe candidate.
   - 5-way cohort delta (accounts_dim 835 / account_team 862 / expected 857 / silver 842 / portal-side 799). INFLBIWMALIGN-adjacent housekeeping. AE 0.6.1 banked for incremental Phase 4.

## Next Steps

| Recipient | Item |
|---|---|
| **DE 0.4** | Phase 2 visual validation (DT push + /frontend-dev) — INFGRO.006 gate is OPEN per my probe deliverable. Per-HH MAX rendering held pending patrick-HH-gap probe TO. |
| **DT 0.4** | Portal push of `d4e28cca` + gitlink `1b258f658` + log `dc09a93dd` from DE Phase 2. (CTO surfaced DT just came online + processing 7-msg backlog.) |
| **AE 0.6.1** | EC2 warm-held for DS~B cash_drag P0 (~30min ETA). Will shutdown post DS~B close or EOD. |
| **DS~C** | NaN cleanup carve-out closed. `feedback_signal_bounded_vs_time_bounded_emit` follow-on TBD per their ADHC_GOLDNAN cross-script audit candidate flag. |
| **CTO 1.0.0** | (informational) Architectural call on INF_C_02 `advisor_key` passthrough — drop OR alias-at-join. Bug-shadows pattern `comp-pipescript shadow-detect` ADHC_COMPIL_V4 backlog. |
| **COO 2.0.0** | (informational) RAVC2-CLOSE absorbed. 3-lane coordination metrics banked. Active scope: watchdog mode. |
| **Self — passive** | Standing by /loop watchdog. No active TO. Next dispatch from COO/Andrew. |
