# DS~A Session 1 — INFGRO Stage -1 txn_type Universe Audit
**Date:** 2026-05-13
**Agent:** 0.4.0_DS_ClientPlatform~A
**Authorization:** COO GO 14:59Z (Andrew direct routing override 2026-05-11)
**TO:** none (informal direct routing per Andrew override)
**Brief shipped:** `docs/briefs/INFGRO_TXN_TYPE_UNIVERSE_AUDIT_20260513.md`

## TL;DR

Full-universe scan of 1,513 silver/transactions partitions: 45 distinct `type_desc`, 0 zombies vs yaml v2, 2 orphans (`Stock Split` + `Unknown`). Yaml is COMPLETE for OLD-schema data.

NEW finding outside COO's ask: a `silver/transactions/2026-05-13.parquet` snapshot was written at 02:16:04Z today with a fundamentally different schema (`type_desc`→`trans_type_desc`, `activity_category`→`category`, 43-col→18-col, parquet v20→v21, 1.25M rows of full history into one file). This new snapshot collapses 21 economically-meaningful classifications into `'Unknown'` (4,299 rows). **Recommendation: PRD §2 NEEDS AMENDMENTS — Stage 1 dispatch BLOCKED on 4 CTO rulings.**

## Files Modified

| File | Change |
|------|--------|
| `docs/briefs/INFGRO_TXN_TYPE_UNIVERSE_AUDIT_20260513.md` | NEW — full audit deliverable |
| `.runtmp/infgro_txn_type_universe_audit_20260513.py` | NEW (runtime-only, gitignored) — audit script |
| `.runtmp/infgro_txn_type_universe_audit_20260513.json` | NEW (runtime-only) — full 1,513-partition universe raw output |
| `.runtmp/infgro_audit_quick_head_2026-05-13.txt` | NEW (runtime-only) — HEAD snapshot quick analysis |

## Methodology

| Step | Tool | Result |
|---|---|---|
| Read yaml baseline | Read `data/orion/scripts/silver/orion_cashflow_taxonomy.yaml` | 43 type_desc, Stage 0b ratified |
| Read DS~B 2026-05-11 audit baseline | Read `logs/2026-05-11/DSA_inf_gro_txntype_audit.md` | 1,510 partitions / 1,145,124 rows / 43 type_desc baseline |
| List silver partitions | `aws s3 ls s3://opal-data-inf/silver/transactions/` | 1,513 parquet files (3 new since DS~B audit: 05-11, 05-12, **05-13 anomalous 19.7MB snapshot**) |
| List bronze partitions | `aws s3 ls s3://opal-data-inf/bronze/transactions/` | 2 files only (05-12, 05-13) — rolling refresh, not historical |
| HEAD snapshot probe | Python + boto3 + pyarrow on 2026-05-13.parquet (1.25M rows) | 24 distinct `trans_type_desc`, 3 distinct `category`; 2 orphans |
| OLD-partition zombie probe | Python read of 2026-04-30.parquet + 2026-05-11.parquet | All 21 "snapshot-zombies" present in OLD partitions — confirms mis-classification, not data loss |
| Full-universe scan | Python over all 1,513 partitions (~17 min) | 45 distinct type_desc, 0 true zombies, 2 orphans |

## Audit Findings (brief summary; full detail in `docs/briefs/INFGRO_TXN_TYPE_UNIVERSE_AUDIT_20260513.md`)

### Full silver universe
- **45 distinct type_desc** across all 1,513 partitions
- **0 zombies** (all 43 yaml entries present in OLD partitions)
- **2 orphans:** `'Stock Split'` (558 rows), `'Unknown'` (4,299 rows)
- Sub_type: 14 distinct activity_category in OLD partitions (matches yaml `merged_from_categories` union)

### NEW snapshot 2026-05-13 02:16:04Z (NEW finding)
- 1,251,020 rows / 19.7 MB / parquet writer v21.0.0 / 18-col / column rename `type_desc`→`trans_type_desc`, `activity_category`→`category`
- 24 distinct `trans_type_desc` (vs 43 in yaml) — **21 classifications absent**
- `category` collapsed to 3 values (other 97.7%, billing 1.6%, activity 0.7%) — useless as classifier
- `'Unknown'` count (4,299) ≈ Σ(21 missing classifications' historical row counts) = 4,160 rows → **smoking gun: new ETL collapses 21 yaml classifications into 'Unknown'**
- Materiality if INF_C_01 migrates to NEW snapshot blind: Federal/State/Foreign Tax-Return ($2.5M), Starting Value Internal regression ($6.64M), Rollover/Cancel/Employer/Ext-Out NNA loss (495 rows), DRIP Internal loss (94 rows)

### Recommendation
PRD §2 NEEDS AMENDMENTS — Stage 1 dispatch BLOCKED on 4 CTO rulings:
1. Schema canonical (OLD per-day vs NEW snapshot for INF_C_01?)
2. 'Unknown' fix point (accept regression / fix writer / hold INF_C_01)
3. 'Stock Split' bucket ratification (proposed: Internal per Spin Off precedent)
4. Yaml v3 if column rename adopted

## False Start

Original audit script used `pq.read_table(obj['Body'])` directly on a boto3 streaming body. Boto3 S3 streams don't implement `seek()`, which pyarrow's parquet reader requires. The exception was caught silently per-partition and emitted as "ERR" lines — but the output was piped through `tail -50` which buffered everything until script end. First run returned `silver_type_desc_count: 0 / 0 matched / 43 zombies` — implausibly clean signal of FAILURE not data event. Caught on schema probe of one partition (`io.UnsupportedOperation: seek`).

Fix: wrap with `io.BytesIO(obj['Body'].read())` so the buffer is seekable. Also added schema detection so the script handles BOTH the OLD `type_desc`/`activity_category` and the NEW `trans_type_desc`/`category` columns. Re-ran clean.

**Lesson:** stream-vs-buffer is a known pyarrow gotcha on Windows + boto3. Memorize: parquet readers always need seekable input.

## Compiler Tools

| Tool | Result |
|---|---|
| `comp-pipescript io INF_C_01` | (not run — no script edits this session; audit only) |
| `comp-pipescript deployed` | (not run — no deploys) |
| `comp-validate` | (not applicable — no gold script run) |
| `aws s3 ls + aws s3api list-object-versions` | Used to probe partition timestamps + ETags; not a comp-* tool but the same intent |

No comp-* invocation this session — pure audit, no gold/lambda code changed. Recorded in `org/compiler-tools-log.md` would be N/A "no script edited."

## Deploy Evidence
N/A — audit only, no commits to gold scripts.

## Cross-pod Notes

- **AE 0.7 (PartnerETL):** v1.7.53 LIVE per RAVC2 14:26Z in pod inbox. Chain #25 GO pending COO. Will pick up DS~B/~C/~D 2026-05-12 commits + Brief C INF_D_09 fix. **Surfaced to AE indirectly:** 2026-05-13 02:16:04Z snapshot writer — was this AE? If so, please add to release notes; if not, AE may want to investigate alongside `inf-performance-daily` cadence issue.
- **CTO 1.0.0:** 4 open rulings (Stage 1 dispatch gating).
- **COO 2.0.0:** ACK + RAVC2 sent; Stage 1 dispatch BLOCKED state communicated.
- **DS~B/~C/~D:** No action required. DS~C currently active on IWM book orphan bucket fix (session1-3 today).

## Next Steps

| Recipient | Item |
|-----------|------|
| **CTO 1.0.0** | Ratify (a) schema canonical, (b) 'Unknown' fix point, (c) 'Stock Split' bucket assignment, (d) yaml v3 column rename. Brief: `docs/briefs/INFGRO_TXN_TYPE_UNIVERSE_AUDIT_20260513.md` |
| **COO 2.0.0** | Add Stage 1 dispatch gating condition #3 (schema event resolved) to ADVI_INFGRO project JSON / REGISTRY row |
| **Self** | Standing by for CTO rulings; ready to author yaml v3 + INF_C_01 read-path update if migration adopted, OR ε-bucket map for 'Unknown' if regression accepted |
| **AE 0.7** | Indirect: confirm whether 2026-05-13 02:16:04Z snapshot is part of v1.7.53 deploy scope or separate write |

## Session Telemetry

- **Wall time:** ~80 min (ACK 14:59Z → final RAVC2 ship ~16:30Z, including 17-min full-universe scan + 80-row brief authoring)
- **Quoted ETA:** ~30-45 min — overrun driven by initial-script failure + a NEW finding (schema event) requiring a 4th CTO ruling beyond the 3 COO asked for
- **Surfaced beyond GO scope:** 2026-05-13 schema event — flagged proactively rather than narrowly answering the 4-bullet GO since the schema change invalidates the canonical source assumed by COO's ask
