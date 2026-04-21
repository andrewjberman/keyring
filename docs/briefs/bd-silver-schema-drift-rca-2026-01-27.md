# BD silver/transactions schema drift — root-cause investigation

**Author:** 0.6.0_AE_PartnerETL
**Date:** 2026-04-21
**Requested by:** 1.0.0_SA_CTO (MCP `20260421T170525Z` + `20260421T172250Z` directive D)
**Scope:** Answer CTO's 5 questions. Recommend Path X vs Y.
**Time budget:** 4h SLA set at 17:22Z.

---

## TL;DR

**Root cause: `1c5b4b5d feat: Switch BD ingestion to Daily template with 99% single-day data` committed 2026-01-28 17:10-05:00.** Deployed via the `bd-exporter` EC2 service; became live on the 2026-01-27 data date. The replacement script `merge-daily-incremental.py` reads BD's daily XLSX exports directly and writes `silver/transactions/{date}.parquet` with **no NNA-classification step**. The original `bd_transaction_consolidator` Lambda computed `is_nna_*` from raw txn fields; the new pipeline skipped that logic. The Lambda was then deleted from AWS (verified: `GetFunction` returns `ResourceNotFoundException`).

Every silver/transactions partition from 2026-01-27 forward lacks `is_nna_*`. No gold-layer breakage happened because every production consumer independently recomputes NNA from `transaction_type` + `action`. My enricher was the first consumer to naively trust the `is_nna_*` contract.

**Recommendation: Path X-lite** — restore upstream emission of `is_nna` / `is_nna_inflow` / `is_nna_outflow` inside `merge-daily-incremental.py` using the recompute logic that already exists in `bd-gold-layer` / `bd_gold_common` / `parallel_process.py`. One file change, ~20 lines, reproduces the missing schema so the silver contract stops being ambiguous.

---

## Question 1 — Producer identity post-2026-01-27

**Answer: `merge-daily-incremental.py`** executed by the `bd-exporter` EC2 instance via SSM document `opal-bd-transaction-download`.

Evidence:
- `infra/aws/ssm/opal-bd-transaction-download.json` lines 41-45: `aws s3 cp s3://opal-data-bd/scripts/merge-daily-incremental.py .` → `python3 merge-daily-incremental.py`
- `infra/aws/ec2/bd-exporter/deploy-merge-daily-incremental.sh`: deploys the script to `s3://opal-data-bd/scripts/merge-daily-incremental.py` used by the SSM doc.
- Local copy: `data/black_diamond/scripts/silver/merge-daily-incremental.py` (1,147 lines).
- The script reads BD's daily `TXN_DAILY_{date}.xlsx` exports from `s3://opal-data-bd/{FORWARDFILL_PREFIX}/`, normalizes column names (snake_case), enriches with CUSIP via `bd_assets_dim`, and writes `silver/transactions/{YYYY-MM-DD}.parquet`. It does NOT compute `is_nna_*`.

The prior producer `bd_transaction_consolidator` Lambda:
- Still has source in-repo at `infra/aws/lambda/bd_transaction_consolidator/lambda_function.py` (lines 309-322 compute is_nna_*).
- **Deleted from AWS.** `aws lambda get-function --function-name bd-transaction-consolidator` returns `ResourceNotFoundException`.
- Not in any EventBridge rule (verified via `list-rules`).

## Question 2 — S3 object-owner / last-modified heuristic

**Answer: object versions confirm the drift across every version ever written.**

Probed S3 version history:

| Key | Version | LastModified | is_nna_* present | cols |
|-----|---------|-------------|------------------|-----:|
| 2026-01-26.parquet | Yq28ZBfg9xdK3DJIkJVLYBCLu4_I2._C | 2026-04-17T12:08:25Z | YES (3 cols) | 79 |
| 2026-01-26.parquet | GBtERtf0rq3dk_gudFvnxc4FGZbXBUtQ | 2026-02-23T16:24:55Z | YES (3 cols) | 78 |
| **2026-01-27.parquet** | **J0mj158tOPJXt_lLuj0ngEfkKpMBUXnv** | **2026-04-17T12:08:26Z** | **NONE** | **74** |
| 2026-01-27.parquet | sMGtIItT9wszQxHMo3ymvdQvOjtytyZg | 2026-04-10T00:31:21Z | NONE | 73 |
| 2026-01-27.parquet | UUgGxKCHOdK5MU8QwTxaIC3iBd_vlSjJ | 2026-02-17T15:16:06Z | NONE | 73 |

Interpretation: 2026-01-27 has **never had is_nna_* across any of its 3 versions** (earliest: 2026-02-17, so the drift was live by the time this partition was first written). 2026-01-26's 2 versions **always had is_nna_***. The cutover date is locked at 2026-01-27.

The 2026-04-17 LastModified on both is a coincident backfill (likely one of the ADHC_HISTRY / BDPL_CNPRCS cusip reprocessings — sizes changed slightly). Not a new drift event.

## Question 3 — Root-cause timing / deploy

**Answer: commit `1c5b4b5d` 2026-01-28 17:10-05:00 = 2026-01-28 22:10:04Z.**

```
commit 1c5b4b5d84d2b65aded430da739d70000e391c08
Date:   2026-01-28 17:10:04 -0500
Subject: feat: Switch BD ingestion to Daily template with 99% single-day data
Files:
  data/black_diamond/scripts/core/merge-daily-allocation-incremental.py (+3 -1)
  data/black_diamond/scripts/core/merge-daily-incremental.py           (+3 -1)
  data/black_diamond/scripts/download-current-week.ts                   (+232 new)
  data/black_diamond/scripts/download-daily-allocation.ts               (+236 new)
  data/black_diamond/scripts/test-daily-template.ts                     (+224 new)
  data/black_diamond/scripts/utils/trading-days.ts                      (+189 new)
  data/black_diamond/scripts/FILENAME_CONVENTION_UPDATE.md              (+183 new)
```

Related deploys around the same window:
- `3f118601 Deploy bd-daily-trigger @ 45e37f5` and `0ce354f2 Deploy bd-daily-trigger @ bc0e73c` in the same general window.
- `infra/aws/terraform/bd-pipeline/CHANGELOG.json` has no entry for 2026-01-26 through 2026-01-30 — consistent with the change living in the exporter + scripts, not the Terraform pipeline.

The commit message promises `99% single-day data` (i.e. cleaner transaction_id dedup) and 4 new TS download helpers. The dropped NNA-classification logic is **not mentioned in the commit message** — likely an unintended consequence of replacing the consolidator Lambda with a direct-XLSX-to-parquet pipeline.

## Question 4 — Does bd-gold-layer recompute is_nna_* via bd_gold_common?

**Answer: YES, on the fly, and it's stable.**

Every gold-layer consumer recomputes NNA classification from raw txn fields. Audit results:

| Consumer | is_nna_* behavior | Source |
|----------|-------------------|--------|
| `bd-gold-layer` Lambda | Recomputes from `transaction_type` + `action` regex | `infra/aws/lambda/bd-pipeline/bd-gold-layer/lambda_function.py:225-232` |
| `bd_gold_common` layer | Recomputes (same logic) | `infra/aws/lambda-layers/bd-gold-common/python/bd_gold_common.py:147-156` |
| `parallel_process.py` (bd-exporter scripts) | Recomputes | `infra/aws/ec2/bd-exporter/terraform/scripts/parallel_process.py:125-129` |
| `C_01.canonical_nna.py` + `lib/nna_flows.py` | Classifies by `transaction` type strings — doesn't read is_nna_* (CTO-verified) | gold-layer |
| `D_04.client_portal_summary._build_nna_by_period` | Consumes canonical_nna output; doesn't touch is_nna_* | gold-layer |
| `bd_transaction_consolidator` Lambda (source only, not deployed) | Would have written is_nna_* | deleted |

Net: **the entire production path has been drift-tolerant by accident.** No gold/platinum/portal consumer was broken. My enricher (`enrich_transactions_with_schwab.py`) was the first and only consumer to naively trust the `is_nna_*` contract — which is how I stumbled on the finding.

## Question 5 — Any other gold/platinum consumers affected?

**Answer: NO consumers broken. Only my enricher was blind to the drift, and I already patched the fallback.**

Full audit via `grep -rn 'is_nna\|external_flow'` on `data/black_diamond/scripts/gold/`, `infra/aws/lambda/`, `infra/aws/lambda-layers/`, `infra/aws/ec2/bd-exporter/`:

- All 5 consumers above recompute on the fly — SAFE.
- `bd_transaction_consolidator` source is retained but not deployed — DEAD CODE.
- `bd_gold_common` and `parallel_process.py` share the recompute pattern — SAFE.
- No gold script reads `is_nna_*` directly (CTO verified in earlier MCP, corroborated by my grep).
- My diagnostic enricher is now relocated; its production-line 494 partitions are preserved as audit artifact with marker file `_DIAGNOSTIC_ARTIFACT.txt`.

---

## Recommendation: Path X-lite (upstream restore, minimal)

Full Path X would require auditing and restoring contract parity with the deleted consolidator Lambda — overkill. Path X-lite: patch `merge-daily-incremental.py` to emit the 3 missing cols using the recompute logic that already exists in `bd_gold_common.py`.

**Proposed ~20-line patch** (for a future TO — NOT shipping under this brief):

```python
# data/black_diamond/scripts/silver/merge-daily-incremental.py
# Before df.to_parquet(...)

INFLOW_TYPES  = {'Cash Deposit','Transfer In','Wire In'}
OUTFLOW_TYPES = {'Cash Withdrawal','Transfer Out','Wire Out'}

def _contains(col: pd.Series, pattern: str) -> pd.Series:
    return col.fillna('').astype(str).str.contains(pattern, case=False, na=False, regex=True)

df['is_nna_inflow'] = (
    df['transaction_type'].isin(INFLOW_TYPES)
    | _contains(df.get('action', pd.Series([''] * len(df))),
                r'Deposit|Transfer In|Wire In')
    | _contains(df.get('external_flow', pd.Series([''] * len(df))),
                r'Contribution')
)
df['is_nna_outflow'] = (
    df['transaction_type'].isin(OUTFLOW_TYPES)
    | _contains(df.get('action', pd.Series([''] * len(df))),
                r'Withdraw|Transfer Out|Wire Out')
    | _contains(df.get('external_flow', pd.Series([''] * len(df))),
                r'Withdrawal')
)
df['is_nna'] = df['is_nna_inflow'] | df['is_nna_outflow']
```

**Why Path X-lite over Path Y (per-consumer drift-tolerance):**

| Consideration | Path X-lite | Path Y |
|---------------|-------------|--------|
| Breadth of fix | 1 producer script edit | All current + future consumers must know about drift |
| Silver contract clarity | Restored — `is_nna_*` present on every partition | Permanently ambiguous ("either flag OR external_flow") |
| Risk to downstream | Zero (cols restored; consumers that recompute get identical results) | Every new consumer is a potential silent-undercount risk |
| Effort | ~20 lines + 1 backfill | Indefinite — every future consumer pays the tax |
| Deploy | SSM doc picks up on next bd-transactions run (script lives in S3) | N/A |

Path Y would be the right choice if the BD XLSX export fundamentally lost the is_nna-relevant source fields. It didn't — `transaction_type`, `action`, and `external_flow` are all present in the XLSX. The silver producer just stopped applying the classifier.

**Backfill scope for Path X-lite:**

- Partitions 2026-01-27 → present lack is_nna_*. Approximately 60 trading-day partitions.
- One-shot reprocessing can be done by running `merge-daily-incremental.py` in a backfill mode over the `s3://opal-data-bd/{FORWARDFILL_PREFIX}/TXN_DAILY_{date}.xlsx` corpus, or simply by adding is_nna_* cols to existing parquets via a read-mutate-write diagnostic.
- Better: add a `--backfill-is-nna` flag to merge-daily-incremental.py that reads existing silver partitions, recomputes the 3 cols, writes back with same transaction_id set. ~15 extra lines.

---

## Open questions for CTO (before shipping the Path X-lite patch)

1. **TO assignment:** does this go to me (0.6.0_AE_PartnerETL, since I discovered and investigated) or to the bd-exporter owner? I don't have current lane clarity on merge-daily-incremental ownership.
2. **Scope of backfill:** rewrite all 2026-01-27-onward partitions once, or just forward-fix (new partitions correct, historical left as-is because no consumer breaks)?
3. **Pre-commit gate:** should `ds-commit-gate.sh` be extended to schema-delta-check silver producer scripts against a contract doc? The drift was a 1-line regression in a 1,068-line feature commit — would have been caught by a schema unit test in CI.
4. **Consolidator Lambda source cleanup:** do we delete `infra/aws/lambda/bd_transaction_consolidator/` from the repo since the Lambda is gone? Or keep as reference? Dead code carries a "does this still work?" cost.
5. **ADR/architecture doc:** should we draft `docs/architecture/BD_SILVER_TRANSACTION_CONTRACT.md` to prevent future drift? Would name the canonical column set, the expected classifier, and the allowed producers.

---

## Appendix — Probe evidence

All probe scripts left at `/tmp/schwab_diag/`:

- `version_probe.py` — confirmed per-version schema stability across 2026-01-26 (always had flags) vs 2026-01-27 (never had flags)
- `check_2026_bd.py` — showed `external_flow` takes over as the NNA signal post-drift
- `acct_map.py` — original finding that BD.original_account_number == Schwab acct10 zero-stripped

All findings reproducible from the current S3 state and repo HEAD `768818d1`.

---

## Related

- Schema-drift flag MCP: `20260421T170302Z` from AE to CTO
- CTO alignment check: `20260421T170525Z` (the 5 questions)
- CTO DECISION on Path A canonical: `20260421T172250Z`
- ROLLUP MCP: `20260421T173708Z`
- Session log: `org/tier2_senior/0.6.0_AE_PartnerETL/logs/2026-04-21/schwab_trn_transaction_enrichment_phase1_2.md`
- Producer script: `data/black_diamond/scripts/silver/merge-daily-incremental.py`
- SSM doc: `infra/aws/ssm/opal-bd-transaction-download.json`
- Drift-introducing commit: `1c5b4b5d 2026-01-28T22:10:04Z`
