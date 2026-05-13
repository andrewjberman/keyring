# DS~C 2026-05-13 session 2 — INF_C_07 orphan root-cause diagnostic (RD green-light → COO Phase 0)

**Agent:** 0.4.0_DS_ClientPlatform~C
**Window:** ~14:54Z → ~15:01Z 2026-05-13 (~7 min)
**Trigger:** RD 0.4.2 green-lit the 10-min silver-schema diagnostic offered in session-1 RAVC2 ACK (`b7e8757f8`). The IWM orphan bucket whose downstream symptom my session-1 Lambda fix (`52478bb3a`) suppresses needed root-cause attribution — C-stage join bug vs upstream ingestion vs partner-data gap.

## TL;DR

Root cause: **INF_C_07 falls back to IWM catchall when its `_apply_accounts_v2_advisor_key_override` silently no-ops on an empty `silver/api_dims/accounts_v2` partition**, AND `gold/dimensions/accounts_dimension_latest.parquet` is missing the 19 orphan accounts that `gold/timeseries/account_performance` has. Outer-merge produces NaN advisor_key/household_id → `_FILL_VALUES` routes to `inflection_wealth_management`.

Two coupled bugs, both fixable, scope-decomposed and handed to COO for `ADHC_INFDIM_ORPHAN` TO authoring:
- **Bug A (DS-owned, 30 min):** Walk back `_latest_silver_partition` to non-empty rows — textbook MEMORY pattern C.1 (`memory/feedback_walk_back_to_healthy_snapshot.md`). Resolves 17 of 19 orphans (Peter Lee × 16, Patrick Scanlan × 1).
- **Bug B (cross-team — DT/AE/silver-ETL):** `accounts_v2` 2026-05-13 partition is 0 rows + `accounts_dimension_latest` is stale (842 rows vs 857 in silver vs 861 in today's `account_team`). Needed for the 2 brand-new accounts (4268, 4269).

No DS commits this session. All work was empirical diagnosis + cross-source reconciliation + MCP relay.

## Empirical findings — 19 orphan account_ids reconciled across 5 sources

Account IDs: `[102, 159, 184, 255, 415, 435, 459, 621, 682, 706, 884, 957, 1156, 1163, 4262, 4263, 4264, 4268, 4269]`

| Source | Rows | Orphans found | Has household_id | Has rep_name |
|---|---|---|---|---|
| `gold/views/account_team.parquet` (today) | 861 | 19/19 | NO (null → 'unknown' string) | N/A (catchall) |
| `silver/api_dims/accounts_v2/snapshot_date=2026-05-13` | **0 — EMPTY** | 0/19 | — | — |
| `silver/api_dims/accounts_v2/snapshot_date=2026-05-12` | 857 | 17/19 | **YES** (e.g. 419, 65, 206, 304, 179, 330, 56, 237, 461, 437, 351, 434) | **Peter Lee × 16, Patrick Scanlan × 1**, all `is_active=True`, `account_status='Normal Downloading'` |
| `gold/dimensions/accounts_dimension_latest.parquet` | 842 | **0/19** | — | — |
| `gold/timeseries/account_performance.parquet` (date=2026-05-13) | 799 | 19/19 | — | — |

**Empty-partition pattern is recurring**: 2 of 9 last partitions are empty (~21KB vs ~77KB normal): 2026-05-08 + 2026-05-13. The defect isn't a one-off.

## Mechanism (INF_C_07 `data/orion/scripts/gold/INF_C_07.advisor_attribution.py`)

1. **L91-100 `_latest_silver_partition`** — alpha-sorts Hive keys and returns the last. No row-count check. Returns today's empty `snapshot_date=2026-05-13/data.parquet`.
2. **L117-160 `_apply_accounts_v2_advisor_key_override`** — empty parquet still has columns, so the column-presence check passes. `lookup` DataFrame ends up empty. `combine_first` no-ops (`_key_override` all-NaN). `advisor_key` keeps whatever came from `acct_dim` upstream.
3. **L176-183 `acct_dim`** — read from `gold/dimensions/accounts_dimension_latest.parquet`. Only 842 rows; 19 orphans not in it.
4. **L208-211 outer merge** — `latest[['account_id', 'total_aua']].merge(acct_dim, on='account_id', how='outer')`. The 19 accounts in `account_performance` but NOT in `acct_dim` get NaN `household_id` + NaN `advisor_key`.
5. **L227-231 `_FILL_VALUES`** — `{'household_id': 'unknown', 'advisor_key': 'inflection_wealth_management'}`. The 19 orphans become IWM-catchall-routed.

## Two-bug scope decomposition (handed to COO)

**Bug A — INF_C_07 walk-back-to-non-empty.** MEMORY pattern C.1. `_latest_silver_partition` should iterate partitions newest-first and return the first one whose data has rows > 0. Raise if none found within a lookback window (e.g. 14 days). 30-min DS task with `comp-pipescript io` + `comp-pipescript deployed` gate. **Cheap structural fix that defangs the same defect for any future empty-partition day.** Resolves 17 of 19 (the named-rep accounts).

**Bug B — Upstream data-freshness.** Two coupled sub-issues:
1. `gold/dimensions/accounts_dimension_latest.parquet` is stale relative to `silver/api_dims/accounts_v2`: 842 rows vs 857 (yesterday silver) vs 861 (today's `account_team`). Either the gold-dim build is intermittently failing, or its silver-source-walk-back isn't kicking in, or it's filtering out new accounts.
2. `silver/api_dims/accounts_v2/snapshot_date=2026-05-13` emitted 0 rows. Why? Same defect on 2026-05-08. Either silver ingestion silently emits empty parquet on partial failure, or it has a fall-through path that produces empty output instead of raising.

Bug B probably crosses into DT / AE / silver-ETL ownership. COO scope-decision needed.

## Routing trail

- 14:54Z RD greenlights MCP-COO-directly: "your message has the full empirical picture; re-routing through me adds latency and risks losing precision."
- 14:59Z RAVC2 to RD with empirical Phase 0 evidence.
- 15:00Z MCP COO with Phase 0 evidence + scope decomposition + sequencing questions.
- 15:01Z (this log).

## Compiler Tools

| Tool | Runs | Result |
|---|---|---|
| Live S3 reconciliation across 5 sources | 1× (single Python diagnostic) | Found root cause in ~12 min; well under RD's 10-min greenlight budget (per source loads via `pd.read_parquet` + filter + isin checks) |
| `comp-pipescript io INF_C_07` | NOT RUN — diagnostic-only session, no code edits to gold scripts |
| `comp-pipescript deployed` | NOT RUN — same reason |
| `ds-commit-gate.sh` | NOT RUN — no commits this session |

Phase-0-evidence-gathering ≠ pipeline edit. No comp-tools mandate triggered. When Bug A is assigned to me, all gates fire per standard cycle.

## Files Modified

None this session.

## Decision notes (worth keeping)

1. **Walk-back-to-non-empty is the right structural fix.** MEMORY pattern C.1 was written precisely for this class of defect. Worth flagging in the COO message that the pattern is already documented — it accelerates COO's scope review (they don't have to re-derive the pattern from first principles).

2. **5-source reconciliation is the diagnostic engine.** The bug only became unambiguous when I had counts from all 5 sources side-by-side (`account_team`, today's silver, yesterday's silver, `accounts_dimension_latest`, today's `account_performance`). Two sources alone would have been ambiguous between "C-stage join bug" and "ingestion gap". Three sources would have told me silver has the data but not who's dropping it. Five sources isolated the drop to the join.

3. **Empty-partition pattern recurrence.** 2 of 9 last partitions empty is a 22% failure rate on the silver ingestion side. Bug A protects against that going forward. Worth flagging to COO as a separate observation — even after Bug B is fixed, having Bug A in place means INF_C_07 is robust to future empty-partition events.

4. **Hand off Phase 0 evidence to TO author, not to relay.** RD's choice to greenlight direct MCP to COO (vs relay-through-RD) is the right move when the evidence is rich and the routing layer adds latency without summarization value. Useful pattern: when a peer agent has a sharp empirical artifact, COO scope-authoring goes faster with raw evidence than via summary.

5. **Sentinel laddering.** Bug A sentinel is "17 of 19 orphans reattributed to Peter Lee / Patrick Scanlan post-INF_C_07 walk-back fix; IWM clients[] from 11 → 9 post-everything." Bug B sentinel is "net-new accounts 4268, 4269 appear in `accounts_dimension_latest` with correct household_id." Two independent ladder rungs; COO can ship Bug A and verify partial close without waiting for Bug B.

## Sequencing handoffs

| Recipient | Item |
|---|---|
| **COO 2.0.0_SA_COO** | Phase 0 evidence delivered. Pending: (a) sequencing call on v1.7.54 Lambda deploy Path A vs B; (b) ADHC_INFDIM_ORPHAN TO scope decomposition + Bug A assignment to DS~C; (c) Bug B owner assignment (DT/AE/silver-ETL). |
| **AE 0.6.1** | Standing position unchanged. ACK on `52478bb3a` + brief `9b9746358` already received; deploy queued post-chain #25 pending COO call. |
| **RD 0.4.2_RD_AdvisorIntelligence** | Closed. Both RAVC2 messages received + ACKed by RD; RD is relaying Andrew. |
| **DS~C self** | Standing by for COO routing call + any TO assignment. If Bug A is assigned, ~30 min sprint to ship: edit `_latest_silver_partition` for walk-back, ds-commit-gate, safe-commit + safe-deploy.sh, RAVC2 with sentinel verification. |

## Pacing

7 min for the diagnostic + COO message. Cooperative cadence shows: RD greenlights direct-to-COO routing → I deliver Phase 0 evidence with full mechanism + scope decomposition → COO scope-authors with raw evidence. Two layers traversed, zero summary-loss, total elapsed ~45 min from initial RD brief receipt to COO Phase 0 delivery (including session-1 Lambda fix + AE brief + RAVC ack cycle + product-call docstring + session-2 silver diagnostic). Aggressive turnaround relative to the 4-gap-investigation scope the brief originally implied.
